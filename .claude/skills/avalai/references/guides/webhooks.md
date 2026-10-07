# Webhooks (guide) — **hosted AvalAI webhooks NOT implemented**
Banner: feature in development, not available; AvalAI will announce. OpenAI documents webhooks (`response.completed`, batch completion, fine-tuning updates); on AvalAI treat provider-hosted webhooks as route/account dependent. **Do NOT assume** a dashboard/endpoint registration or `client.webhooks.unwrap` works against AvalAI. Use polling endpoint of your own job + your own signed webhook sent by your worker (app-managed pattern below). Browser-only flows → polling; server-to-server notify → webhook.

## Use when
bg/long jobs must notify backend; batch/eval/data-enrichment workers need completion callback; video/fine-tune/file processing wakes another service; resellers need cost/status events downstream.

## If a provider does expose OpenAI-style (Standard Webhooks) webhooks
Public HTTPS endpoint (per-project in provider dashboard; signing secret shown once); subscribe only handled event types (allowlist in code); send test event first; keep RAW body for signature; verify before any side effect; reply `2xx` fast, heavy work in worker; dedupe by `webhook-id`/event `id`; retry-with-backoff expected (OpenAI retries up to 72 h — don't assume for AvalAI/provider routes). Headers: `webhook-id` (idempotency), `webhook-timestamp` (replay check), `webhook-signature`; payload `id`, `type`. Rotate leaked secret immediately with overlap window accepting old+new until retries drain. Delivery is **at-least-once**; `2xx` = endpoint accepted, not work done; 3xx = failure (configure final URL); local dev needs public tunnel (ngrok/cloud dev env/serverless), not localhost.
Receiver contract: valid+new → store, enqueue, `2xx`; duplicate id → `2xx` no side effects; bad signature/old timestamp → `400`, don't parse/queue; transient DB/queue failure → `5xx` only if you want retry.
SDK: `client.webhooks.unwrap(raw_body, headers, secret=...)` (python `InvalidWebhookSignatureError`; JS `OpenAI.InvalidWebhookSignatureError`); never `express.json()` before verification (use `express.text`/`express.raw`). Then worker retrieves `response_id = event.data.id` → `client.responses.retrieve(...)`.
Routing matrix: `response.completed` → retrieve, extract output, update job (store response_id, link id, status); failed/cancelled response → mark terminal, safe error code, retry decision; batch/eval complete → fetch result file/report (ids, counters); fine-tune complete → final job+model id before enabling traffic; video/media → fetch asset or failure, expire temp URLs; cost/reseller callback → reconcile usage, idempotent billing (request/job id, usage, ledger tx id).

## App-managed signed webhook (portable)
Your worker, after storing the final result, POSTs a signed event. Signature = HMAC-SHA256 over `f"{timestamp}.{raw_body}"` with `AVALAI_WEBHOOK_SECRET`, header `webhook-signature: v1=<hex>` (+ `webhook-id`, `webhook-timestamp`); tolerance 300 s; `hmac.compare_digest`/`crypto.timingSafeEqual`; dedupe in PERSISTENT storage (in-memory set is demo only); persist event then enqueue slow work.
Event shape: `{"object":"event","id":"evt_job_...","type":"job.completed","created_at":<unix>,"data":{"job_id":"job_...","response_id":"resp_...","status":"completed"}}`. Types: `job.completed`, `job.failed` (safe error code), `job.cancelled`, `cost.available`; version names (`job.completed.v1`) once customers depend. Keep payload small: no API keys, raw user secrets, bulky model output.
Sender checklist: unique event id; sign `timestamp.raw_body`; retry timeouts/5xx with exponential backoff; expiration window + dead-letter queue.
Receiver checklist: raw body; reject bad signature before parsing; reject stale timestamps; dedupe; fast 2xx + queue; log event id, request id, job id, status, signature result; rotate secrets; tunnel for local; treat redirects as failure.

## Defects
- Body reads as supported ("if provider offers…") while banner says not implemented.
- Sample env var `AVALAI_OR_PROVIDER_WEBHOOK_SECRET` is invented; python Flask sample verifies `unwrap` args with `request.headers` object.
- Signature format `v1=<hex>` here differs from Standard Webhooks (`v1,<base64>`) — don't mix verifiers.
