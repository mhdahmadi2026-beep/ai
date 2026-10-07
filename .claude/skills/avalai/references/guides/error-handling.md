# Error handling (guide)

## Error body
```json
{"error":{"message":"...","type":"invalid_request_error","param":null,"code":"invalid_api_key","solution":"...","request_id":"<uuid v7>"}}
```
Fields: message, type, param, code, `solution` (AvalAI extra), `request_id`. Success responses carry header `avalai-request-id`. Optionally send `X-Client-Request-Id` (ASCII, <512 chars, new per logical request, reuse only on retry of the same idempotent op) so you can correlate even on timeouts.
Support bundle (support@avalai.ir / t.me/AvalAISupport): request_id, client request id, model, endpoint, status, timestamp+tz, safe metadata (token counts, file size, retries), full message/type/code/param. NEVER send API keys, raw user secrets, private files, full prompts unless asked (redacted).

## Status codes
200/201/204 ok. 400 bad request, 401 auth, 403 forbidden, 404 not found, 409 conflict, 422 unprocessable, 429 limits, 500/502/503/504 server.

## Codes (type = code unless noted)
| HTTP | code | meaning / fix |
|---|---|---|
| 401 | invalid_api_key (type invalid_request_error) | wrong/revoked key; new keys can take up to 60 s to activate |
| 400 | invalid_request_format | malformed/missing params |
| 400 | context_window_exceeded (param messages) | shorten input / bigger-context model |
| 400 | unsupported_model (param model) | model not valid for this endpoint (e.g. embedding model on chat) |
| 400 | content_policy_violation | safety rejection; edit prompt |
| 403 | model_access_denied | no access/does not exist; check chat.avalai.ir/platform/limits |
| 403 | insufficient_tier | tier too low for model |
| 404 | resource_not_found (type not_found) | bad model/resource id |
| 429 | rate_limit_exceeded | pace requests, honour Retry-After |
| 429 | quota_exceeded | credit exhausted (billing page) |
| 429 | insufficient_quota | balance doesn't cover estimated cost → top up |
| 500 | internal_server_error | retry after wait |
| 500 | provider_server_error | upstream error; retry or other model |
| 503 | service_unavailable | temporary/maintenance |
| 503 | model_overloaded (param model) | reduce concurrency, retry, alternative model |
Note: quota/insufficient credit return HTTP 429 per docs but are NOT retryable by waiting.

## SDK exceptions → action
APIConnectionError (network/proxy/TLS; retry after health check), APITimeoutError (retry idempotent, send X-Client-Request-Id), AuthenticationError (no retry), BadRequestError (no retry), PermissionDeniedError (no retry), NotFoundError (check ids), ConflictError (re-read state), RateLimitError (Retry-After + jitter + lower concurrency), InternalServerError (backoff, failover), UnprocessableEntityError (fix input).

## Retry matrix
Retry with capped exponential backoff + jitter + max attempts: 429(rate), 500, 502, 503, 504, timeouts, dropped connections. Honour `Retry-After`. DO NOT blind-retry 400/401/403/404/422, policy errors, unsupported model, insufficient_quota/quota_exceeded. Stream cut mid-way: keep partial output, resume from explicit conversation/job state. After retries exhausted: stop, log ids, fallback/human review. For overload/`slow_down`: drop concurrency to last stable level, hold minutes, ramp up; combine backoff with queue-level concurrency control (thundering herd).

## Responses WebSocket mode errors
`previous_response_not_found` → resend full input with `previous_response_id: null`. `websocket_connection_limit_reached` → open new socket, continue from last stable state; checkpoint conversation outside the socket.

## Production
Centralized handling, Sentry-like reporting, health checks, circuit breaker, fallbacks for critical features, user-friendly messages; log avalai-request-id, model, route, status, retries, latency.

## Source defects
- Python retry sample uses `e.headers` (should be `e.response.headers` / `e.response.headers.get("retry-after")`) and catches RateLimitError before APIError (fine) but not APIConnectionError/timeouts.
- Bash sample parses nonexistent `retry_after` JSON key (use header).
- Go sample: lowercase `model:` field, go-openai APIError mismatch.
- Circuit breaker sample hard-codes `gpt-4` (stale; use a current model) and nested `main` in logging sample is mis-indented.
- Both "Responses equivalent" blocks are just migration hints.
