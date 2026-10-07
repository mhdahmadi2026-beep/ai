# راهنمای پیگیری هزینه نمایندگان / Reseller cost-tracking guide — https://docs.avalai.ir/fa/resellers/cost-tracking-guide
Group: «نمایندگان فروش» (resellers). For resellers of AvalAI API who need **exact per-call cost** for correct customer billing and margin. Uses the **User API** (`POST /user/v1/transactions/lookup`, /fa/api-reference/user).

## Why exact cost tracking
Exact customer billing from real usage · keep margin (markup on exact costs, not estimates) · transparent detailed usage reports · cash-flow planning · dispute resolution with accurate records.

## The problem with `estimated_cost`
```json
{
  "usage": {"prompt_tokens": 10, "completion_tokens": 20, "total_tokens": 30},
  "estimated_cost": {"unit": "0.0000066000", "irt": 0.76, "exchange_rate": 115250}
}
```
❌ not guaranteed in all responses · ❌ may not reflect real billing (esp. credit packages, grants, special pricing) · ❌ ignores variables like cached tokens, streaming costs · ❌ exchange rate may differ from final billing rate. **Never bill customers from `estimated_cost`.** Use it only for rough UX estimates.

## Solution: User API `/user/v1/transactions/lookup`
✅ 100% accurate (matches your real invoice) · ✅ available **within 30 s** after the request completes · ✅ full detail incl. grants, packages, real charges · ✅ audit trail · ✅ multiple currencies: UNIT (USD) and IRT (Toman).
Flow: every API response carries header **`avalai-request-id`** (UUID v7) → store it with your customer's request → wait up to 30 s → query lookup with the request ID → get exact cost for billing.

## Full workflow
### Step 1 — store the request id
```python
response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers={
        "Authorization": f"Bearer {AVALAI_API_KEY}",
        "Content-Type": "application/json",
    },
    json={"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام!"}]},
)

# IMPORTANT: store avalai-request-id from headers
request_id = response.headers.get("avalai-request-id")

# store immediately with customer context
db.insert_pending_transaction(
    {
        "request_id": request_id,
        "customer_id": customer.id,
        "timestamp": datetime.now(),
        "model": "gpt-5.4-mini",
        "response_data": response.json(),
    }
)
```
Responses API equivalent (when the model supports `/v1/responses`): `messages`→`input`; system message→`instructions` (or a `developer` item); `choices[0].message.content`→`response.output_text`; for tools/multimodal inspect `response.output` by `type`.
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a helpful assistant.",
    input="سلام!",
)

print(response.output_text)
```
### Step 2 — wait for cost processing (async, up to 30 s, usually much faster)
```python
import time

# Option A: synchronous — wait right away
time.sleep(5)  # usually available in 3–5 s

# Option B: asynchronous — process later (recommended)
cost_tracking_queue.add(
    {
        "request_id": request_id,
        "customer_id": customer.id,
        "retry_after": datetime.now() + timedelta(seconds=5),
    }
)
```
### Step 3 — look up the exact cost
```python
lookup_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={
        "Authorization": f"Bearer {AVALAI_API_KEY}",
        "Content-Type": "application/json",
    },
    json={"transaction_ids": [request_id]},
)

cost_data = lookup_response.json()

if cost_data["summary"]["found"] > 0:
    transaction = cost_data["transactions"][0]

    actual_cost_usd = float(transaction["cost"]["unit"])
    actual_cost_irt = float(transaction["cost"]["paid_irt"]) + float(
        transaction["cost"]["paid_grant_irt"]
    )

    db.update_transaction_cost(
        request_id=request_id,
        cost_usd=actual_cost_usd,
        cost_irt=actual_cost_irt,
        cost_details=transaction["cost"],
    )
```
Response shape used: `summary.found`, `transactions[]` each with `id`, `model`, `requested_at`, `tokens`, `cost{unit, paid_unit, paid_irt, paid_grant_irt, source, currency}`, `packages[]` (see 08-credit-packages).
### Step 4 — bill the customer
```python
# pricing (example: 20% markup)
customer_cost_usd = actual_cost_usd * 1.20
customer_cost_irt = actual_cost_irt * 1.20

db.insert_customer_charge(
    {
        "customer_id": customer.id,
        "request_id": request_id,
        "avalai_cost_usd": actual_cost_usd,
        "customer_cost_usd": customer_cost_usd,
        "markup_percent": 20,
        "timestamp": datetime.now(),
    }
)

customer.deduct_balance(customer_cost_usd)
```

## Architecture options
1. **Synchronous** (simple, more latency): customer → your API → AvalAI; store `avalai-request-id`; wait ~5 s; lookup exact cost; return to customer. Pro: simple, immediate cost. Con: +5 s response time.
2. **Asynchronous (recommended):** store `request_id`, return immediately; background worker looks up cost ~5 s later and updates DB. Pro: fast, scalable. Con: slightly more complex.
3. **Batch (high volume):** collect request_ids during the day → hourly batch job → lookup in batches (**up to 1000 IDs**) → update costs → generate customer invoices. Pro: efficient, fewer API calls. Con: delayed cost data.

## Complete Python implementation
```python
import requests
import time
from datetime import datetime, timedelta
from typing import Dict, List
import logging


class AvalAIReseller:
    def __init__(self, avalai_api_key: str):
        self.api_key = avalai_api_key
        self.base_url = "https://api.avalai.ir"

    def make_customer_request(
        self, customer_id: str, model: str, messages: List[Dict], **kwargs
    ) -> Dict:
        """Make an API request on behalf of a customer and track costs."""
        # Step 1: API call
        response = requests.post(
            f"{self.base_url}/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {self.api_key}",
                "Content-Type": "application/json",
            },
            json={"model": model, "messages": messages, **kwargs},
        )

        # Step 2: store avalai-request-id
        request_id = response.headers.get("avalai-request-id")
        if not request_id:
            logging.error("No avalai-request-id in response headers!")
            raise ValueError("avalai-request-id header missing")

        # Step 3: store for cost lookup
        self.store_pending_transaction(
            request_id=request_id,
            customer_id=customer_id,
            model=model,
            response_data=response.json(),
        )

        # Step 4: queue cost processing (async)
        self.queue_cost_lookup(request_id, customer_id)

        return {"request_id": request_id, "response": response.json()}

    def lookup_transaction_cost(
        self, request_ids: List[str], max_retries: int = 3
    ) -> Dict:
        """Look up exact costs for one or more transactions; retry if not yet available."""
        for attempt in range(max_retries):
            response = requests.post(
                f"{self.base_url}/user/v1/transactions/lookup",
                headers={
                    "Authorization": f"Bearer {self.api_key}",
                    "Content-Type": "application/json",
                },
                json={"transaction_ids": request_ids},
            )

            data = response.json()

            if data["summary"]["found"] == len(request_ids):
                return data

            if attempt < max_retries - 1:
                wait_time = 5 * (attempt + 1)  # backoff
                logging.info(f"Transactions not ready, waiting {wait_time}s...")
                time.sleep(wait_time)

        return data

    def process_transaction_cost(self, request_id: str, customer_id: str):
        """Process cost for one transaction and bill the customer."""
        cost_data = self.lookup_transaction_cost([request_id])

        if cost_data["summary"]["found"] == 0:
            logging.error(f"Transaction {request_id} not found!")
            return

        transaction = cost_data["transactions"][0]

        avalai_cost_usd = float(transaction["cost"]["unit"])
        avalai_cost_irt = float(transaction["cost"]["paid_irt"]) + float(
            transaction["cost"]["paid_grant_irt"]
        )

        markup = 1.20  # e.g. 20%
        customer_cost_usd = avalai_cost_usd * markup
        customer_cost_irt = avalai_cost_irt * markup

        self.record_customer_charge(
            customer_id=customer_id,
            request_id=request_id,
            avalai_cost_usd=avalai_cost_usd,
            customer_cost_usd=customer_cost_usd,
            avalai_cost_irt=avalai_cost_irt,
            customer_cost_irt=customer_cost_irt,
            transaction_details=transaction,
        )

        logging.info(
            f"Customer {customer_id} billed: ${customer_cost_usd:.6f} "
            f"(AvalAI: ${avalai_cost_usd:.6f}, markup: 20%)"
        )

    def store_pending_transaction(self, request_id, customer_id, model, response_data):
        """Implement your DB storage logic"""
        pass

    def queue_cost_lookup(self, request_id, customer_id):
        """Implement your queue logic (Redis, Celery, ...)"""
        pass

    def record_customer_charge(self, **kwargs):
        """Implement your billing logic"""
        pass


reseller = AvalAIReseller(avalai_api_key="your-key")

result = reseller.make_customer_request(
    customer_id="cust_123",
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "سلام!"}],
)
# cost will be processed asynchronously in the background
```
> Skill notes on this sample: it calls `response.json()` which won't work for **streaming** requests; and `data` after the retry loop can contain partial results — always check `summary.found`. For idempotent billing, key charges on `request_id`.

## Best practices
### 1) Always store `avalai-request-id`
- **requests / any HTTP client:** `request_id = response.headers.get("avalai-request-id")`; raise if missing (can't track cost).
  - ✅ `response.headers.get(...)` · ❌ `response.json().get("avalai-request-id")` — it's in headers, not body.
- **OpenAI SDK (recommended):** `response._request_id` is auto-populated by the OpenAI SDK against AvalAI's endpoint:
```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "سلام!"}],
)

request_id = response._request_id
if not request_id:
    raise ValueError("request_id missing - cannot track cost!")

print(f"request id: {request_id}")
# e.g. 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a
```
- **LangChain** (doesn't expose HTTP headers directly) — capture via custom httpx client + callback (async: use `httpx.AsyncClient` + `AsyncCallbackHandler`; full async examples: /fa/api-reference/response-headers#access-avalai-request-id-with-langchain):
```python
import httpx
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import BaseCallbackHandler
from contextvars import ContextVar
import os

# store headers in a context var for thread safety
request_headers: ContextVar[dict] = ContextVar("request_headers", default={})


class HeaderCapturingClient(httpx.Client):
    def send(self, request, **kwargs):
        response = super().send(request, **kwargs)
        request_headers.set(dict(response.headers))
        return response


class HeaderAccessCallback(BaseCallbackHandler):
    def __init__(self):
        self.request_id = None

    def on_llm_end(self, response, **kwargs):
        headers = request_headers.get()
        self.request_id = headers.get("avalai-request-id")


http_client = HeaderCapturingClient()
chat_generator = ChatOpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key=os.getenv("AVALAI_API_KEY"),
    model="gpt-5.4-mini",
    http_client=http_client,
)

callback = HeaderAccessCallback()
response = chat_generator.invoke("سلام!", config={"callbacks": [callback]})

request_id = callback.request_id
if not request_id:
    raise ValueError("request_id missing - cannot track cost!")

print(f"request id: {request_id}")
```
### 2) Retry with backoff (costs may not be instantly available)
```python
def lookup_with_retry(request_id, max_attempts=3):
    for attempt in range(max_attempts):
        data = lookup_cost(request_id)
        if data["summary"]["found"] > 0:
            return data
        time.sleep(5 * (attempt + 1))  # 5s, 10s, 15s
    raise Exception("cost unavailable after retries")
```
### 3) Batch lookups for efficiency (up to 1000 IDs)
```python
request_ids = get_pending_request_ids(limit=1000)
cost_data = lookup_transaction_cost(request_ids)

for transaction in cost_data["transactions"]:
    process_cost(transaction)
```
### 4) Store complete transaction detail for audit (not only the cost)
```python
db.store_transaction({
    "request_id": request_id,
    "customer_id": customer_id,
    "timestamp": transaction["requested_at"],
    "model": transaction["model"],
    "tokens": transaction["tokens"],
    "avalai_cost_unit": transaction["cost"]["unit"],
    "avalai_cost_irt": transaction["cost"]["paid_irt"],
    "markup_percent": 20,
})
```
> The published snippet is syntactically broken (`markup_percent": 20` missing opening quote/key with blank line) — fixed above.

## Troubleshooting
- **`avalai-request-id` missing from response headers:** old SDK or wrong place — read **headers**, not body.
- **Transaction not found after 30 s:** very rare, may happen under heavy load → retry longer (e.g. up to 60 s, interval 10 s); if still missing, contact support with the request ID.
```python
max_wait = 60
interval = 10
for i in range(max_wait // interval):
    data = lookup_cost(request_id)
    if data["summary"]["found"] > 0:
        return data
    time.sleep(interval)
# still not found: contact support with the request id
```
- **Costs differ from `estimated_cost`:** expected — `estimated_cost` is an estimate; `/transactions/lookup` is real. Always bill from lookup; use `estimated_cost` only for rough UX.

## Related
/fa/api-reference/user · /fa/api-reference/response-headers (`avalai-request-id`, rate limits) · /fa/resellers/enterprise-guide · /fa/guides/rate-limits
Support for resellers: **support@avalai.ir** — include your reseller/agency ID and the specific request IDs.
