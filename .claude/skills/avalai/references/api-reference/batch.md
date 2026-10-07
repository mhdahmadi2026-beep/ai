# Batch API (docs: /fa/api-reference/batch)

> ⛔ **NOT IMPLEMENTED on AvalAI** (in development). **Never emit `/v1/batches` code.** Use client-side workers: fa/guides/batch-processing and fa/examples/rate_limit_safe_parallel_requests (and fa/examples/promptfoo_evals_with_avalai for evals). OpenAI's 50% Batch discount, separate rate-limit pool, file-retention policy are OpenAI-hosting terms — NOT AvalAI guarantees; until `/v1/batches` is live, batch-style work is billed at normal per-model prices and normal rate limits.
> (Consistent with rate-limits page: "no Batch API". The Moderation/Embeddings pages' "Batch API" mentions are conditional on this.)
> No hosted batch webhooks either: if you need completion notifications, run jobs in your own worker and fire your own webhook (stable event id for idempotency, signed payload, ack `2xx` fast before heavy work; fa/guides/webhooks). OpenAI "background Responses" is a separate async pattern; if AvalAI adds it, poll the Response until it leaves `queued`/`in_progress`; until then model it in your own job table.

## Planned OpenAI-compatible lifecycle (for future / mirroring in your worker)
1. Build `.jsonl` (one request per line). 2. Upload via Files API (`purpose="batch"`, fa/api-reference/files — not yet captured). 3. Create batch with `input_file_id`, `endpoint`, `completion_window`. 4. Poll until `completed|failed|expired|cancelled`. 5. Download `output_file_id` (successes) and `error_file_id` (failed/expired rows).
Planning limits: one `endpoint` + one `model` per input file; unique `custom_id` (join outputs by `custom_id`, order not guaranteed); never `stream:true`; OpenAI reference limits 50,000 requests / 200 MB per file (AvalAI may be lower); `/v1/embeddings` batches ≤50,000 total inputs; moderations rows use `input` (prefer `image_url` over big base64); `/v1/videos` JSON body with pre-uploaded assets/file IDs (⚠ Videos API shut down 2026-09-24 per deprecations).

### State machine (mirror in your own worker for painless migration)
| status | meaning | do |
|---|---|---|
| `validating` | input being checked | poll with backoff |
| `failed` | validation failed | stop retrying same file; read `errors`/`error_file_id`; fix JSONL; new batch |
| `in_progress` | rows running | keep polling; outputs incomplete |
| `finalizing` | result files being prepared | keep polling; prep storage |
| `completed` | results ready | download output, join by `custom_id`, archive batch metadata |
| `expired` | 24 h window ended | keep completed rows; resubmit only unfinished `custom_id`s from error file |
| `cancelling` | cancel in progress (~10 min) | stop downstream consumers; wait for `cancelled` |
| `cancelled` | done | download partial results; mark unfinished cancelled; don't reprocess completed rows |

## Endpoints (planned)
- `POST /v1/batches` — body: `input_file_id` (req, JSONL, purpose `batch`, ≤50k reqs/200 MB), `endpoint` (req; `/v1/responses`, `/v1/chat/completions`, `/v1/embeddings`, `/v1/completions`(legacy), `/v1/moderations`, `/v1/images/generations`, `/v1/images/edits`, `/v1/videos`; AvalAI may be narrower), `completion_window` (req; only `24h`), `metadata` (≤16 pairs; key ≤64, value ≤512), `output_expires_after` (optional `{anchor:"created_at", seconds}` per Files API expiry policy; download results before expiry).
- `GET /v1/batches/{id}` · `POST /v1/batches/{id}/cancel` · `GET /v1/batches?after&limit` (1–100, default 20).
- Batch object: `id`, `object:"batch"`, `endpoint`, `errors`, `input_file_id`, `completion_window`, `status`, `output_file_id`, `error_file_id`, `created_at`, `in_progress_at`, `expires_at`, `finalizing_at`, `completed_at`, `failed_at`, `expired_at`, `cancelling_at`, `cancelled_at`, `request_counts{total,completed,failed}`, `metadata`.
- Expiry: finished rows stay available; unfinished rows reported as errors.

### Input line
```json
{"custom_id":"request-1","method":"POST","url":"/v1/chat/completions","body":{"model":"gpt-5.4-mini","messages":[{"role":"system","content":"…"},{"role":"user","content":"۲+۲ چند می‌شود؟"}]}}
```
Responses form: `"url":"/v1/responses"`, `body:{model, input, instructions}`; read `body.output_text`/`response.output`. (Source example model id `gpt-5.4-mini` — verify live.)
### Output line
Success: `{"id":"batch_req_…","custom_id":"request-2","response":{"status_code":200,"request_id":"req_…","body":{…}},"error":null}`. Error: `{"custom_id":"request-3","response":null,"error":{"code":"invalid_request_error","message":"…"}}`.

## Practical advice (what to do today)
Own worker with bounded concurrency honoring `x-ratelimit-*`/`Retry-After`, stable `custom_id`s, per-row retry with backoff, persisted job table with the states above, result store keyed by `custom_id`, flex tier (−50%, select OpenAI models) for non-urgent work (see 07-service-tiers.md).
