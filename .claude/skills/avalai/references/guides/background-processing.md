# Background processing (guide) — **hosted background Responses NOT implemented on AvalAI**
Source banner: feature in development, not available; AvalAI will announce. Page body describes an OpenAI-style pattern "route/model/account dependent". **Do NOT emit** `background:true`, `responses.retrieve/cancel` polling, `starting_after` stream resume, or `/v1/responses/{id}/cancel` as supported AvalAI code unless a probe proves it. Default → app-managed job queue.

## When
Long reasoning/deep research/code analysis/report generation exceeding browser/proxy/mobile timeouts; closing tab mustn't kill job; queueable tasks needing progress UI/retry/cancel. Short chat → normal sync or streaming Responses.

## App-managed fallback (use this)
Local job record `{id, status: queued|in_progress|completed|failed|cancelled, output_text, error, request_id}`; API endpoint only creates job + returns id; worker (Celery/BullMQ/Sidekiq/SQS/internal) calls `client.responses.create(model=..., input=..., store=False)`; expose `GET /jobs/{id}` for polling (or webhook after terminal state). Progress messages describe job state only — never invent partial model output. Cancellation: mark `cancelled`, stop queued work, ignore late worker output if call was in flight; idempotent. Use idempotency key / deterministic job key (model, prompt version, user id, created time) so repeated clicks don't spawn duplicate costly jobs. Cancelling a sync request = close client connection; make retries safe.
Poll safely: by job id (not by repeating prompt), exponential backoff + jitter, stop on ALL terminal states, store final response id, status, `avalai-request-id`, model, usage; copy output out before any retention window ends; show timeout in UI past SLA.
Terminal states: `completed` (read output/usage/citations), `failed` (safe error + request id + retryable? never auto-retry non-idempotent), `cancelled` (ignore late output), `incomplete`/`expired` (not final answer; retry smaller/clearer/managed queue).

## Hosted pattern (reference only; probe first)
`responses.create(..., background=True, store=True)` (needs `store:true`; upstream rejects background w/o stored state) → poll `retrieve(id)` while status in {queued, in_progress}. Streaming: `background:true, stream:true, store:true`, keep last `sequence_number`; resume `GET /v1/responses/{id}?stream=true&starting_after=N` (only if created with `stream:true`; TTFT higher than sync). Cancel: `POST /v1/responses/{id}/cancel` (idempotent). Compat probe checklist: create → id+status; retrieve; poll to terminal (completed|failed|cancelled|incomplete|expired); cancel mid-run; stream w/ sequence numbers; resume. Record probe results in deployment notes; if a probe fails document the managed fallback for that capability. If route rejects `background` → drop it and use own queue; don't silently retry a multi-minute call synchronously.

## Retention / ZDR
OpenAI background mode keeps response data ~10 min for polling → incompatible with strict zero-data-retention (ZDR); legacy ZDR projects may still accept `background=true` but it breaks ZDR guarantees; MAM projects can use it. AvalAI: provider/account/route-dependent → confirm before compliance claims. Retention-limited projects: managed fallback with `store:false`, store only permitted metadata/final response, delete failed/expired jobs on schedule, never put secrets in prompts.

## Defects
- Python/JS fallback sample runs the model call INLINE inside `create_job` (blocking) — the comment says to move to a real worker queue; as written it is not async.
- Sample status set (`cancelled`, `incomplete`, `expired`) vs fallback job statuses differ.
- Banner contradicts body (body reads as if feature is supported when route allows).
