# Rate-limit-safe parallel requests (docs.avalai.ir/fa/examples/rate_limit_safe_parallel_requests)

Parallel workers (embeddings, classification, extraction, batch jobs) without a throttle cause many `429`s. Adapted from OpenAI Cookbook `How_to_handle_rate_limits.ipynb` + `api_request_parallel_processor.py`. Related: guides/rate-limits.md, error-handling.md, api-reference/response-headers.md, batch-processing.md (hosted Batch not available → this is the app-side pattern).

## Strategy (use all three layers)
1. Retry `429` and transient server errors with exponential backoff + jitter. 2. Cap concurrent requests. 3. Pace requests to stay below your tier's RPM/TPM. Also read rate-limit headers and slow down before request/token budgets hit zero.

## Python: async worker with backoff (`AsyncOpenAI`)
- `with_backoff(operation, max_retries=6, initial_delay=1.0, max_delay=60.0)`: on `RateLimitError` read `retry-after` from `exc.headers`, sleep `max(retry_after, delay) + uniform(0, 0.25*delay)`, `delay=min(delay*2, max_delay)`, re-raise at last attempt; on `APIStatusError` retry only `status_code >= 500` (4xx raised immediately).
- `classify_ticket(ticket)`: `client.responses.create(model="gpt-5.6-luna", instructions="Classify the ticket as Billing, Technical, Account, or Other. Return only the label.", input=ticket)` inside `with_backoff`.
- `run_batch(tickets, max_concurrency=5)`: `asyncio.Semaphore(max_concurrency)` + `asyncio.gather` over guarded calls (results keep input order).
## JS: worker pool
`withBackoff(operation, maxRetries=6)`: retryable = 429 or 5xx; `retry-after` seconds ×1000; jitter `random*delay*0.25`; delay doubles to 60 s. `runBatch(items, maxConcurrency=3)`: N workers pulling a shared `nextIndex` and writing `results[current]` (order preserved).

## Header-based pacing (python)
Headers: `x-ratelimit-remaining-requests`, `x-ratelimit-remaining-tokens`, `x-ratelimit-reset-requests`, `x-ratelimit-reset-tokens`. `parse_reset_seconds` parses durations like `1m30s`, `250ms`, `2h` via regex `(\d+(?:\.\d+)?)(ms|s|m|h)`; `pace_from_headers(headers, floor=2)` sleeps `max(reset_requests, reset_tokens, 1.0)` when remaining ≤ floor. Use `client.responses.with_raw_response.create(...)` → `raw.headers`, then `raw.parse()`. Keep the retry wrapper anyway: headers help planned pacing; `Retry-After` + exponential backoff are needed for bursts, contention and transient server errors.
## cURL: honour Retry-After
Loop up to 5 attempts: `curl -sS -o body -D headers -w "%{http_code}"`; 200 → print; non-429 → print + exit 1; 429 → sleep `Retry-After` (awk on the headers file, strip `\r`) else `attempt²` seconds.

## Throughput checklist
Headroom: target 50–75% of documented RPM/TPM for your tier; track BOTH requests and tokens (one may run out first); header-based pacing for long workers; honour `Retry-After`, else exponential backoff + jitter; lower `max_output_tokens` for short answers; batch small classifications when latency isn't critical; save partial results as you go so interrupted jobs resume; log request ids and error bodies.

## Pitfalls in the page's samples (fixes)
- **SDK built-in retries stack with yours**: the OpenAI SDKs retry 429/5xx by default (`max_retries=2`) → set `max_retries=0` on the client when you own the backoff, otherwise attempts multiply (and cost/limits).
- `Retry-After` may be an HTTP-date, not just seconds → parse defensively (the sample `float(...)` would crash).
- JS `error.headers?.["retry-after"]` — in recent SDK versions `error.headers` is a `Headers` object (use `.get("retry-after")`).
- Semaphore/worker caps limit concurrency, NOT RPM/TPM: add a shared token-bucket/rate limiter (e.g. N requests/s and a tokens/min budget) for sustained throughput; each worker sleeping independently on header values is racy (many workers read the same header state).
- `pace_from_headers` int() parsing assumes headers exist; default `floor` when absent can wrongly trigger sleeps — treat missing as unknown.
- 429 can also mean quota/credit exhaustion or tier limits: retrying doesn't fix a depleted balance (see error-handling.md).
- Don't retry non-idempotent side effects blindly; make writes idempotent.
- Reasoning models: `max_output_tokens` caps include hidden reasoning (cost-optimization.md).
