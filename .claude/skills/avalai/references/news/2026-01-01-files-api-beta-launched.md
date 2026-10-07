# News 2026-01-01 (1404-10-11): Files API beta (docs.avalai.ir/fa/news/2026-01-01-files-api-beta-launched)

OpenAI-compatible `/v1/files`: upload once → `file_id` (avoids ~33% base64 overhead), reuse in `/v1/chat/completions` (`{"type":"file","file":{"file_id":…}}`), `/v1/responses`, `/v1/messages`, `/v1/ocr`, `/v1/images/edits`.
- Endpoints: `POST /v1/files` (multipart `purpose`, `file`, optional `expires_after={"anchor":"created_at","seconds":86400}`), `GET /v1/files`, `GET/DELETE /v1/files/{id}`, `GET /v1/files/{id}/content`.
- Purposes: assistants, batch, fine-tune, vision, user_data, evals, `others` (AvalAI-specific). Use `user_data` for general documents. (Purpose existing ≠ Assistants/Batch/fine-tune features hosted.)
- Beta was FREE 2026-01-01 → 1404-12-10 (≈2026-03-01) — over; check current pricing. Max 128 MB/file (beta).
- Per-minute ops (upload/download/delete): T0 3/5/10; T1 10/100/100; T2 50/250/250; T3 250/500/500; T4 500/1000/1000; T5 1500/2000/5000. Storage: T0 250 MB, T1 2 GB, T2 5 GB, T3 15 GB, T4 50 GB, T5 200 GB.
- Storage on AWS S3 / GCP / Cloudflare; **NOT encrypted at rest** (stated); access by your API key only. Don't upload secrets/sensitive data without `expires_after` + deletion. Security reports: security@avalai.ir (bug bounty for critical).
- Status page showed /v1/files as weakest endpoint — see guides/service-status.md. Source samples use legacy `gpt-4o`; use a current model.
