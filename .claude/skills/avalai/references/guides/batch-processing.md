# Batch processing (guide)
**Hosted Batch API NOT implemented** (see api-reference/batch.md). Use client-side workers.
- JSONL rows `{custom_id, method:"POST", url, body}`; unique stable `custom_id`; output order not guaranteed. Prefer `/v1/responses` rows (instructions + input). Row URLs possible: responses, chat/completions, embeddings (≤50k inputs total), moderations, images, videos (JSON body only). Never `stream:true`.
- Local worker: ThreadPoolExecutor with low concurrency (4), route by `url`, retry 429 with 2^n backoff (cap 60 s), checkpoint per chunk, write results.jsonl, retry only failed `custom_id`s.
- Job table states: queued/in_progress/completed/failed/cancelled (+expired); expose `GET /jobs/{id}`; webhook after terminal state (respond 2xx fast, dedupe by event id, sign payloads).
- Limits to mind: RPM and TPM both; JSONL < 200 MB; OpenAI's 50% discount / separate pool are NOT AvalAI guarantees; OpenAI batch output files expire after 30 days (reference only).
- Doc bug: `except` retry check matches "429"/"rate" string (use RateLimitError).
