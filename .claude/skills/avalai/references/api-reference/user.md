# مرجع API کاربر / User API — https://docs.avalai.ir/fa/api-reference/user
Programmatic access to account info, credit balance and transaction history: monitor consumption, track costs, get exact per-call cost.
**Base URL:** `https://api.avalai.ir/user/v1`

## Overview / key features
Monitor credit (remaining balance & sources) · list/filter transactions with flexible params · cost analytics (aggregates by model, provider, day/hour — page intro also says "or API key", but `group_by` only lists model|provider|date|hour) · look up specific transactions by request ID for exact cost.
| Feature | Description |
|---|---|
| Real-time credit data | credit info always up to date |
| Flexible filtering | by model, provider, time range, etc. |
| Aggregate stats | summaries grouped by day, model, provider (or hour) |
| Batch lookup | up to **1000** transactions per request |
| Exact cost tracking | exact cost per API call by request id |
| **90-day retention** | transaction records available for **at least 90 days**; no guarantee beyond 3 months → store transaction details in your own DB if you need longer |

## Authentication
Bearer token with your AvalAI API key on every endpoint.
```bash
export AVALAI_API_KEY="your-avalai-api-key"
curl -X GET "https://api.avalai.ir/user/v1/credit" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
import requests

api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

response = requests.get("https://api.avalai.ir/user/v1/credit", headers=headers)
print(response.json())
```
```javascript
const apiKey = process.env.AVALAI_API_KEY;

const response = await fetch("https://api.avalai.ir/user/v1/credit", {
  method: "GET",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
});

const data = await response.json();
console.log(data);
```
(Page also shows Go (`net/http`, `req.Header.Set("Authorization","Bearer "+apiKey)`) and PHP (`curl_init` + `CURLOPT_HTTPHEADER`) versions — same request.)
Auth errors: **401 `unauthorized`** (missing/invalid key) · **403 `forbidden`** (account suspended/disabled).

## Rate limiting (per user by account tier)
| Tier | Requests/min |
|---|---|
| Base (0) | 3 |
| 1 | 15 |
| 2 | 50 |
| 3 | 150 |
| 4 | 350 |
| 5 | 750 |
Headers on every response: `x-ratelimit-limit-requests` (max/min) · `x-ratelimit-remaining-requests` · `x-ratelimit-reset-requests` (**seconds** until reset).
Exceeded: `{"error": "rate_limit_exceeded", "message": "Rate limit exceeded. Try again in 45 seconds."}`

---
## GET /credit — balance, limits, credit sources
`GET https://api.avalai.ir/user/v1/credit`
```bash
curl -X GET "https://api.avalai.ir/user/v1/credit" -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
import requests
api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}"}
response = requests.get("https://api.avalai.ir/user/v1/credit", headers=headers)
credit_info = response.json()
print(f"remaining credit: {credit_info['remaining_irt']} Toman")
print(f"account tier: {credit_info['account_tier']}")
```
```javascript
const response = await fetch("https://api.avalai.ir/user/v1/credit", {
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
});
const creditInfo = await response.json();
console.log(`remaining credit: ${creditInfo.remaining_irt} Toman`);
console.log(`account tier: ${creditInfo.account_tier}`);
```
Go struct from the page: `CreditResponse{ Limit float64 "limit"; RemainingIRT float64 "remaining_irt"; AccountTier int "account_tier" }`.
Response:
```json
{
  "limit": 0.0,
  "remaining_irt": 742927.85,
  "remaining_unit": 0.0,
  "total_unit": 6.44622863340564,
  "exchange_rate": 115250,
  "account_tier": 5,
  "credit_sources": {
    "grants": [],
    "packages": [
      {
        "id": "25",
        "template_id": "d-o3050s",
        "name": "مدل‌های زبانی منتخب OpenAI روزانه پایه",
        "description": "٪۴۰ تخفیف در مدل‌های منتخب OpenAI",
        "amount_irt": "500000.00",
        "remaining_irt": "498447.15",
        "end_date": "2025-11-27T15:05:07.404882+00:00",
        "allowed_services": ["api"],
        "scope_details": {
          "api": ["gpt-5-chat", "gpt-5-mini", "gpt-5.6-luna", "gpt-5.4-mini", "o4-mini", "o3-mini"]
        }
      }
    ]
  }
}
```
| Field | Type | Meaning |
|---|---|---|
| `limit` | float | total credit limit (Toman) |
| `remaining_irt` | float | remaining credit (Toman) |
| `remaining_unit` | float | remaining credit in unit (USD) |
| `total_unit` | float | total credit in unit |
| `exchange_rate` | int | current Toman→unit(USD) rate |
| `account_tier` | int | tier 0–5; affects rate limits |
| `credit_sources.grants` / `.packages` | array | active grants / packages |
**Grant fields:** `id`, `description`, `amount_irt` (string), `remaining_irt` (string), `end_date` (ISO 8601), `allowed_services` (array), `scope_details` (model/provider restrictions).
**Package fields:** `id`, `template_id`, `name`, `description`, `amount_irt`, `remaining_irt`, `end_date`, `allowed_services`, `scope_details`.
> Note: example `scope_details` lists `gpt-5-chat` (now removed — see 10-deprecations); treat as illustrative.

---
## GET /transactions — paginated list
`GET https://api.avalai.ir/user/v1/transactions`
| Param | Type | Default | Meaning |
|---|---|---|---|
| `hours_ago` | int | 24 | hours back (1–720); ignored if dates provided |
| `start_date` | string | – | YYYY-MM-DD; requires `end_date` |
| `end_date` | string | – | YYYY-MM-DD; requires `start_date` |
| `page` | int | 1 | 1–10000 |
| `page_size` | int | 100 | 1–1000 |
| `safety_identifier` | string | – | filter by your internal id |
| `api_key_id` | int | – | filter by specific API key id |
| `model` | string | – | model name (partial match) |
| `provider` | string | – | provider name |
| `status_code` | int | – | HTTP status |
```bash
# last 24h (default)
curl -X GET "https://api.avalai.ir/user/v1/transactions" -H "Authorization: Bearer $AVALAI_API_KEY"
# last 7 days
curl -X GET "https://api.avalai.ir/user/v1/transactions?hours_ago=168" -H "Authorization: Bearer $AVALAI_API_KEY"
# date range
curl -X GET "https://api.avalai.ir/user/v1/transactions?start_date=2025-01-01&end_date=2025-01-07" -H "Authorization: Bearer $AVALAI_API_KEY"
# filter by model
curl -X GET "https://api.avalai.ir/user/v1/transactions?model=gpt-5.5&page_size=50" -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
import requests
api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get(
    "https://api.avalai.ir/user/v1/transactions",
    headers=headers,
    params={"model": "gpt-5.6-luna", "hours_ago": 168, "page_size": 50},  # last 7 days
)

transactions = response.json()
for tx in transactions["transactions"]:
    print(f"{tx['id']}: {tx['model']} - {tx['tokens']['total']} tokens")
```
```javascript
const params = new URLSearchParams({ model: "gpt-5.6-luna", hours_ago: "168", page_size: "50" });
const response = await fetch(`https://api.avalai.ir/user/v1/transactions?${params}`, {
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
});
const data = await response.json();
data.transactions.forEach((tx) => console.log(`${tx.id}: ${tx.model} - ${tx.tokens.total} tokens`));
```
Response:
```json
{
  "transactions": [
    {
      "id": "019ac1c0-9ff3-7663-b0b9-fbcf2461939a",
      "created_at": "2025-11-26T20:06:23.442Z",
      "requested_at": "2025-11-26T20:00:18.031Z",
      "safety_identifier": null,
      "model": "gpt-5.4-mini",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {"total": 30, "prompt": 10, "completion": 20, "reasoning": 0, "cached": 0}
    }
  ],
  "total": 100,
  "page": 1,
  "page_size": 100,
  "has_more": false
}
```
Fields: `id` (UUID v7 = the `avalai-request-id` header) · `created_at` (when the cost was processed) · `requested_at` (request start) · `model` · `provider` · `status_code` · `stream` · `tokens.total/prompt/completion/reasoning/cached` · `safety_identifier`. Note: list items do **not** include `cost` — use lookup for cost.

---
## POST /transactions/lookup — exact cost by request id (batch ≤1000)
`POST https://api.avalai.ir/user/v1/transactions/lookup`
> **For resellers:** returns the **exact cost** (100% accurate), available **≤30 s** after the request completes. Full workflow: resellers/cost-tracking-guide.md.
### Getting the request id from SDKs
| SDK | How |
|---|---|
| Python (OpenAI SDK) | `response._request_id` (works for chat completions, embeddings, images, other endpoints when base URL is AvalAI) |
| Python (requests) | `response.headers.get("avalai-request-id")` |
| JavaScript (fetch) | `response.headers.get("avalai-request-id")` |
| Go (net/http) | `resp.Header.Get("avalai-request-id")` |
| PHP (curl) | parse response headers (`preg_match('/avalai-request-id:\s*([^\r\n]+)/i', $headers, $m)` with `CURLOPT_HEADER`) |
```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "سلام!"}],
)

request_id = response._request_id
print(f"request id: {request_id}")
```
Responses API equivalent: `client.responses.create(model="gpt-5.4-mini", instructions="…", input="…")` → `response.output_text` (`response._request_id` too).
Body: `transaction_ids` (array, required, 1–1000 UUIDs).
```bash
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام!"}]}'
# response headers include: avalai-request-id: 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a

# wait up to 30 s for processing, then:
curl -X POST "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]}'
```
```python
import requests, time

api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers=headers,
    json={"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام!"}]},
)
request_id = response.headers.get("avalai-request-id")

time.sleep(5)  # usually available much sooner

lookup_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers=headers,
    json={"transaction_ids": [request_id]},
)

transaction = lookup_response.json()
if transaction["summary"]["found"] > 0:
    tx = transaction["transactions"][0]
    print(f"exact cost: {tx['cost']['unit']} USD")
    print(f"exact cost: {tx['cost']['paid_irt']} Toman")
```
```javascript
const headers = { Authorization: `Bearer ${process.env.AVALAI_API_KEY}`, "Content-Type": "application/json" };
const chatResponse = await fetch("https://api.avalai.ir/v1/chat/completions", {
  method: "POST", headers,
  body: JSON.stringify({ model: "gpt-5.4-mini", messages: [{ role: "user", content: "سلام!" }] }),
});
const requestId = chatResponse.headers.get("avalai-request-id");
await new Promise((resolve) => setTimeout(resolve, 5000));
const lookupResponse = await fetch("https://api.avalai.ir/user/v1/transactions/lookup", {
  method: "POST", headers, body: JSON.stringify({ transaction_ids: [requestId] }),
});
const data = await lookupResponse.json();
if (data.summary.found > 0) {
  const tx = data.transactions[0];
  console.log(`exact cost: ${tx.cost.unit} USD`, `${tx.cost.paid_irt} Toman`);
}
```
(Go & PHP versions on the page do the same: POST chat → read `avalai-request-id` header → sleep 5 s → POST lookup.)
### Response example 1 — paid from UNIT balance (no package)
```json
{
  "transactions": [
    {
      "id": "019ac4a0-a8f4-7041-845f-3ea8f15dcf1a",
      "created_at": "2025-11-27T09:24:18.129Z",
      "requested_at": "2025-11-27T09:24:14.709Z",
      "safety_identifier": null,
      "model": "gpt-5.4-mini-2026-03-17",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {
        "total": 17, "prompt": 8, "completion": 9, "reasoning": 0, "cached": 0,
        "prompt_details": {"text_tokens": 8, "audio_tokens": 0, "image_tokens": 0, "cached_tokens": 0, "audio_input_duration": 0, "cache_creation_tokens": 0},
        "completion_details": {"text_tokens": 9, "audio_tokens": 0, "image_tokens": 0, "reasoning_tokens": 0, "audio_output_duration": 0, "accepted_prediction_tokens": 0, "rejected_prediction_tokens": 0}
      },
      "ip_address": "192.168.1.1",
      "tools": {},
      "api_key_suffix": "...6I20",
      "cost": {"unit": "0.00000660", "paid_unit": "0.00000660", "paid_irt": "0", "paid_grant_irt": "0", "source": "credit", "currency": "UNIT"},
      "grants": [],
      "packages": []
    }
  ],
  "summary": {"requested": 1, "found": 1, "not_found_ids": []}
}
```
### Example 2 — paid from a credit package
`cost`: `{"unit":"0.00001350","paid_unit":"0.00001350","paid_irt":"0.00","paid_grant_irt":"1.55","source":"credit_package","currency":"UNIT"}`; `packages[]`: `{id:"1234", template_id:"d-o3050s", name, amount_irt:"500000.00", remaining_irt:"498447.15", allowed_services:["api"], scope_details:{api:[…]}, end_date}`; `summary.found = 1`.
### Field reference
**Top:** `transactions` (array), `summary` (`requested`, `found`, `not_found_ids`).
**Transaction:** `id` (UUID v7 = `avalai-request-id`) · `created_at` · `requested_at` · `safety_identifier` (string|null) · `model` (e.g. `gpt-5.4-mini-2026-03-17`) · `provider` · `status_code` · `stream` · `tokens` · `ip_address` · `tools` (tools/functions used) · `api_key_suffix` (last 4 chars) · `cost` · `grants` · `packages`.
**tokens:** `total`, `prompt`, `completion`, `reasoning`, `cached`, `prompt_details{text_tokens, audio_tokens, image_tokens, cached_tokens, audio_input_duration (s), cache_creation_tokens}`, `completion_details{text_tokens, audio_tokens, image_tokens, reasoning_tokens, audio_output_duration (s), accepted_prediction_tokens, rejected_prediction_tokens}`.
**cost:** `unit` (total USD/unit, string) · `paid_unit` (paid, USD) · `paid_irt` (Toman paid from balance) · `paid_grant_irt` (covered by grants/packages) · `source`: `credit` | `credit_package` | `grant` | `balance` · `currency` (always "UNIT").
> Other pages mention `source == "balance"` for overall-balance payments; this page's example shows `credit` for plain balance. Handle all four values.

---
## GET /transactions/summary — aggregates
`GET https://api.avalai.ir/user/v1/transactions/summary`
Params: `hours_ago` (int, 24, 1–720) · `start_date` / `end_date` (YYYY-MM-DD) · `group_by` (default `model`; one of `model`, `provider`, `date`, `hour`).
```bash
curl -X GET "https://api.avalai.ir/user/v1/transactions/summary" -H "Authorization: Bearer $AVALAI_API_KEY"
curl -X GET ".../summary?group_by=provider" -H "Authorization: Bearer $AVALAI_API_KEY"
curl -X GET ".../summary?group_by=date&hours_ago=168" -H "Authorization: Bearer $AVALAI_API_KEY"
curl -X GET ".../summary?group_by=hour&hours_ago=24" -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
response = requests.get(
    "https://api.avalai.ir/user/v1/transactions/summary",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"group_by": "hour", "hours_ago": 24},
)
for hour_data in response.json()["summary"]:
    print(f"hour {hour_data['hour']}: {hour_data['count']} requests, {hour_data['total_cost_unit']} USD")
```
Response shapes (`summary[]` + `period{start,end,hours}`); each row has `count`, `total_tokens`, `total_cost_unit` (string, USD), `total_cost_irt` (string) plus the group key:
- `group_by=model` → `{"model":"gpt-5.6-luna","count":150,"total_tokens":45000,"total_cost_unit":"0.450000","total_cost_irt":"51862.50"}`
- `group_by=provider` → `{"provider":"openai","count":450,...}`
- `group_by=date` → `{"date":"2025-11-26","count":650,...}`
- `group_by=hour` → `{"hour":"2025-11-26T14:00:00.000Z","count":45,...}`
- `period`: `{"start":"2025-11-26T00:00:00.000Z","end":"2025-11-27T00:00:00.000Z","hours":24}`

---
## GET /health
`GET https://api.avalai.ir/user/v1/health` (with Bearer header) →
```json
{ "status": "healthy", "timestamp": "2025-11-27T09:30:00.000Z" }
```

## Error handling
`{"error": "error_code", "message": "human-readable description"}`
| Status | Code | Meaning |
|---|---|---|
| 400 | `bad_request` | invalid request params |
| 401 | `unauthorized` | missing/invalid API key |
| 403 | `forbidden` | account suspended/disabled |
| 404 | `not_found` | resource not found |
| 429 | `rate_limit_exceeded` | too many requests |
| 500 | `internal_error` | server error |
(Note: this is a *flat* error shape, different from the OpenAI-style `{"error": {...}}` of `/v1/*`.)

## Related
/fa/api-reference/response-headers (`avalai-request-id`, rate-limit headers) · resellers/cost-tracking-guide.md · 09-rate-limits.md · authentication.md · /fa/api-reference/chat
