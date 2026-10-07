# هدرهای پاسخ / Response headers — https://docs.avalai.ir/fa/api-reference/response-headers
Every AvalAI API response carries standard HTTP headers plus custom ones: request tracking, rate limits, cost tracking.

## `avalai-request-id` (most important header)
Unique UUID (**UUID v7**, e.g. `01a009d5-ec91-74c2-8ffa-9eba731dfc9e`) per request. Use for: **exact cost tracking** (`POST /user/v1/transactions/lookup`), **debugging/support reports**, request correlation in your systems, audit trail.
> **Header change notice:** `avalai-request-id` **replaces the legacy `x-request-id`**. During a **60-day transition window both headers are returned with the same value.**

### `x-request-id` (legacy, deprecated)
Some CDNs also use/overwrite `x-request-id` for their own tracing, so it can no longer be treated as AvalAI's authoritative id.
- **Until 2026-10-15 (1405-07-23):** AvalAI returns `x-request-id` alongside `avalai-request-id` (same UUID).
- **After 2026-10-15:** AvalAI no longer returns `x-request-id`; any `x-request-id` you see afterwards was added by an intermediary (CDN) and is NOT your AvalAI request id.
For cost lookup, support traces and logging read **`avalai-request-id`**. Transitional fallback only when it's absent:
```python
request_id = response.headers.get("avalai-request-id") or response.headers.get(
    "x-request-id"
)
```
Remove the fallback before the window ends. (Announcement: /fa/news/2026-08-16-avalai-request-id-header-migration.)

## Migration timeline
Why: CDNs in front of API origins write their own value to `x-request-id` and may overwrite/reuse it, so the observed value may identify the CDN hop rather than the AvalAI request → deterministic lookup/support trace needs a dedicated header.
| Phase | Date | Response headers |
|---|---|---|
| Dual-header window starts | 2026-08-16 (1405-05-25) | both `avalai-request-id` and `x-request-id` (same UUID) |
| Dual-header window ends | 2026-10-15 (1405-07-23) | last day AvalAI returns `x-request-id` |
| Legacy retired | after 2026-10-15 | only `avalai-request-id` from AvalAI |
Example headers during the window:
```
x-ratelimit-limit-requests: 1500
x-ratelimit-remaining-requests: 1499
x-ratelimit-limit-tokens: 30000000
x-ratelimit-remaining-tokens: 29999827
x-ratelimit-reset-requests: 50s
x-ratelimit-reset-tokens: 50s
x-request-id: 01a009d5-ec91-74c2-8ffa-9eba731dfc9e
avalai-request-id: 01a009d5-ec91-74c2-8ffa-9eba731dfc9e
```
Action: (1) update header readers to `avalai-request-id` before 2026-10-15 (both point to the same request in the window); (2) afterwards never parse/log/bill on `x-request-id` (may belong to the CDN); (3) body fields named `request_id` (e.g. Videos API) are unchanged — they carry the same UUID as `avalai-request-id`; (4) the request header `X-Client-Request-Id` needs no change.

## API metadata headers (route-dependent; diagnostic only — NOT guaranteed on all provider routes)
| Header | Meaning | Use |
|---|---|---|
| `openai-processing-ms` | upstream model processing time (ms) | separate provider/model latency from app, network, queue time |
| `openai-version` | REST API version used by the compatible upstream route | log during SDK/API migrations |
| `openai-organization` | upstream org tied to the request, when exposed | debugging only; never rely on it for AvalAI account authorization |
| `service_tier` / processing-tier metadata | tier actually used, when the route returns it | compare requested vs served processing mode |
Don't build billing logic on these. Authoritative for AvalAI billing & reseller reconciliation: `avalai-request-id` + User API transaction lookup.

### Client-side request IDs — request header `X-Client-Request-Id`
OpenAI-compatible routes may accept it. Use as your internal trace id: generate a unique value per API attempt, send it, and log it next to the returned `avalai-request-id`. Useful when a timeout/network error prevents you from receiving response headers; if the AvalAI route preserves OpenAI-compatible metadata, support can use your client request ID as a secondary key. **ASCII only, ≤ 512 chars, unique per request.** It does **not** replace `avalai-request-id` (authoritative for cost lookup & support).
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -H "X-Client-Request-Id: 123e4567-e89b-12d3-a456-426614174000" \
  -d '{
    "model": "gpt-5.4-mini",
    "input": "یک health check یک‌خطی برگردان."
  }'
```

## Accessing `avalai-request-id` via SDKs
**Python (OpenAI SDK) — raw response API:**
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

raw_response = client.chat.completions.with_raw_response.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "سلام!"}],
)
completion = raw_response.parse()

request_id = raw_response.headers.get("avalai-request-id")
print(f"request id: {request_id}")
# e.g. 01a009d5-ec91-74c2-8ffa-9eba731dfc9e
```
(During the window `raw_response.headers.get("x-request-id")` gives the same value; after 2026-10-15 don't rely on SDK attributes derived from the old header name. Note: other pages say `response._request_id` — derived from `x-request-id` in the OpenAI SDK → **may stop working/get CDN's id after the window; prefer reading `avalai-request-id` from raw headers.**)
Responses API equivalent: `client.responses.with_raw_response.create(model=…, instructions=…, input=…)` → `.headers.get("avalai-request-id")`, `.parse().output_text`.
**LangChain v0.3 (sync)** — custom httpx client + callback:
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
        print(f"captured request id: {self.request_id}")


http_client = HeaderCapturingClient()
chat_generator = ChatOpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key=os.getenv("AVALAI_API_KEY"),
    model="gpt-5.4-mini",
    http_client=http_client,
)

callback = HeaderAccessCallback()
response = chat_generator.invoke("بگو سلام", config={"callbacks": [callback]})

print(f"request id from callback: {callback.request_id}")
```
**LangChain v0.3 (async):**
```python
import httpx
from contextvars import ContextVar
from langchain_openai import ChatOpenAI
from langchain_core.callbacks import AsyncCallbackHandler
import os

request_headers: ContextVar[dict] = ContextVar("request_headers", default={})


class AsyncHeaderCapturingClient(httpx.AsyncClient):
    async def send(self, request, **kwargs):
        response = await super().send(request, **kwargs)
        request_headers.set(dict(response.headers))
        return response


class AsyncHeaderAccessCallback(AsyncCallbackHandler):
    def __init__(self):
        self.request_id = None

    async def on_llm_end(self, response, **kwargs):
        headers = request_headers.get()
        self.request_id = headers.get("avalai-request-id")
        print(f"captured request id: {self.request_id}")


http_client = AsyncHeaderCapturingClient()
chat_generator = ChatOpenAI(
    base_url="https://api.avalai.ir/v1",
    api_key=os.getenv("AVALAI_API_KEY"),
    model="gpt-5.4-mini",
    http_async_client=http_client,
)

callback = AsyncHeaderAccessCallback()
response = await chat_generator.ainvoke("بگو سلام", config={"callbacks": [callback]})
```
How it works: custom `httpx` client stores response headers in a context var; the LangChain callback reads them after the LLM call; `ContextVar` keeps it thread/task-safe for concurrent requests. During the window, fall back to `headers.get("x-request-id")` if the new header is absent.
**Other SDKs / direct HTTP:**
| SDK / method | How |
|---|---|
| Python (OpenAI) | `client.chat.completions.with_raw_response.create(...).headers.get("avalai-request-id")` |
| Python (requests) | `response.headers.get("avalai-request-id")` |
| JavaScript (OpenAI) | `(await ...create(...).withResponse()).response.headers.get("avalai-request-id")` |
| JavaScript (fetch) | `response.headers.get("avalai-request-id")` |
| Go (net/http) | `resp.Header.Get("avalai-request-id")` |
| PHP (curl) | `preg_match('/avalai-request-id:\s*([^\r\n]+)/i', …)` (with `CURLOPT_HEADER`) |
> **For resellers:** capture & store this header for every call; `/user/v1/transactions/lookup` returns 100%-accurate cost within 30 s. See resellers/cost-tracking-guide.md.

## Rate-limit headers (on every response)
Request-based: `x-ratelimit-limit-requests` (max requests in window, e.g. `30000`) · `x-ratelimit-remaining-requests` (e.g. `29999`) · `x-ratelimit-reset-requests` (time until reset, **duration string like `45s`**).
Token-based: `x-ratelimit-limit-tokens` (e.g. `150000000`) · `x-ratelimit-remaining-tokens` · `x-ratelimit-reset-tokens` (e.g. `45s`).
> ⚠ Reset values are strings such as `45s` — **don't `int()` them** (the 09-rate-limits sample does; fix by parsing durations). (The User API's own reset header is in seconds — see user.md.)
### Project-level token headers (some upstream-compatible routes, when a project-level token bucket applies)
`x-ratelimit-limit-project-tokens` (e.g. `60000`) · `x-ratelimit-remaining-project-tokens` (e.g. `57000`) · `x-ratelimit-reset-project-tokens` (e.g. `3s`). A request can be throttled by an exhausted project bucket even when the route's token bucket has capacity — monitor these in addition to request/token headers.
### Tiers
Limits depend on account tier (0–5) — see 09-rate-limits.md.
### 429
```
HTTP/2 429
Retry-After: 45
x-ratelimit-limit-requests: 30000
x-ratelimit-remaining-requests: 0
x-ratelimit-reset-requests: 45s
```
### Header-based retry workflow
1. **Store `avalai-request-id` first** — log before parsing the body so support, reseller cost lookup and internal traces point to the same request.
2. **On 429 honor `Retry-After`;** if absent use exponential backoff + jitter + max retries.
3. **Check all buckets** — a request can stall on request, token or project-token limits; monitor `x-ratelimit-remaining-requests`, `-tokens` and any `-project-tokens`.
4. **Reduce token pressure** — lower `max_tokens`, shorten prompts, summarize earlier turns, move non-urgent bulk work to batch-style workflows.
5. **Fail gracefully** — after retries are exhausted show a clear "try later" message and keep the stored `avalai-request-id` in logs.

## Standard HTTP headers
`Content-Type: application/json` · `Content-Length: 970` · `Date: Thu, 27 Nov 2025 09:24:15 GMT`.

## Full example
```bash
# use -i to show headers
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.4-mini",
    "messages": [{"role": "user", "content": "سلام"}]
  }'

# response headers:
# HTTP/2 200
# date: Thu, 27 Nov 2025 09:24:15 GMT
# content-type: application/json
# content-length: 970
# openai-processing-ms: 842
# openai-version: 2020-10-01
# x-ratelimit-limit-requests: 30000
# x-ratelimit-remaining-requests: 29999
# x-ratelimit-limit-tokens: 150000000
# x-ratelimit-remaining-tokens: 149999982
# x-ratelimit-reset-requests: 45s
# x-ratelimit-reset-tokens: 45s
# x-ratelimit-remaining-project-tokens: 57000
# x-request-id: 01a009d5-ec91-74c2-8ffa-9eba731dfc9e
# avalai-request-id: 01a009d5-ec91-74c2-8ffa-9eba731dfc9e
```
```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام"}]},
)

request_id = response.headers.get("avalai-request-id")
remaining_requests = response.headers.get("x-ratelimit-remaining-requests")
remaining_tokens = response.headers.get("x-ratelimit-remaining-tokens")
reset_time = response.headers.get("x-ratelimit-reset-requests")
```
```javascript
const response = await fetch("https://api.avalai.ir/v1/chat/completions", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ model: "gpt-5.4-mini", messages: [{ role: "user", content: "سلام" }] }),
});
const requestId = response.headers.get("avalai-request-id");
const remainingRequests = response.headers.get("x-ratelimit-remaining-requests");
const remainingTokens = response.headers.get("x-ratelimit-remaining-tokens");
const resetTime = response.headers.get("x-ratelimit-reset-requests");
```
(Go: `resp.Header.Get(...)` for the same four headers; PHP: `CURLOPT_HEADER` + `preg_match` per header — same pattern as above.)
Responses API equivalent of the call: `client.responses.create(model="gpt-5.4-mini", instructions="You are a helpful assistant.", input="سلام")` → `response.output_text`; curl to `/v1/responses` with `input` + `instructions`.

## Best practices
1. **Always capture `avalai-request-id`** (cost tracking, support, audit). In the window you may fall back to `x-request-id`, but remove the fallback before it ends. If you also send `X-Client-Request-Id`, log both so timeouts and successes correlate.
```python
request_id = response.headers.get("avalai-request-id")
db.store_request_log(user_id=user.id, request_id=request_id, timestamp=now())
```
2. **Monitor rate limits proactively** — don't wait for 429:
```python
remaining = int(response.headers.get("x-ratelimit-remaining-requests", 0))
if remaining < 100:  # fewer than 100 requests left
    time.sleep(1)  # back off
```
3. **Handle 429 gracefully** with `Retry-After`/backoff:
```python
import time


def make_request_with_retry(max_retries=3):
    for attempt in range(max_retries):
        response = requests.post(...)

        if response.status_code == 429:
            retry_after = int(response.headers.get("retry-after", 60))
            time.sleep(retry_after)
            continue

        return response

    raise Exception("max retries exceeded")
```
4. **Use request IDs for cost lookup** — wait ≤30 s then `POST /user/v1/transactions/lookup` (see user.md).
5. **Log headers for debugging** — include `avalai-request-id`, status code and rate-limit headers when reporting to support.

## Related
/fa/news/2026-08-16-avalai-request-id-header-migration · user.md · 09-rate-limits.md · resellers/cost-tracking-guide.md · /fa/guides/error-handling · /fa/api-reference/chat
