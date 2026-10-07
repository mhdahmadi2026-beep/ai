# Files API — `https://api.avalai.ir/v1/files` (docs: /fa/api-reference/files)

**Available** (unlike Fine-tuning/Assistants/Batch). OpenAI-compatible server-side file store, usable across providers/models. Pricing, storage quota, model compatibility depend on tier and endpoint. Support: t.me/AvalAISupport; security: security@avalai.ir.

Why: upload once, reuse by `file_id` (no repeated large transfers, lower latency, avoid ~33% base64 overhead). Bearer auth. File ids look like `file-EyVi0MrxuKTgBrvkVas5ZTGz` (the source's Responses example uses `file_abc123` — id format is `file-…`; use whatever the upload returned).

**Endpoints that accept `file_id`:** `/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/ocr`, `/v1/images/edits`.

## Upload — `POST /v1/files` (multipart)
| param | req | notes |
|---|---|---|
| `file` | yes | **≤128 MB** per upload |
| `purpose` | yes | `assistants`, `batch`, `fine-tune`, `vision`, `user_data`, `evals`, `others` (AvalAI-specific generic) |
| `expires_after` | no | `{anchor:"created_at", seconds:int}` (only `created_at` anchor) |
```bash
curl https://api.avalai.ir/v1/files -H "Authorization: Bearer $AVALAI_API_KEY" -F purpose="user_data" -F file="@document.pdf"
```
```python
f = client.files.create(file=open("document.pdf","rb"), purpose="user_data")
f2 = client.files.create(file=open("temp_data.jsonl","rb"), purpose="batch", expires_after={"anchor":"created_at","seconds":2592000})
```
```javascript
const f = await client.files.create({ file: fs.createReadStream("document.pdf"), purpose: "user_data" });
```
(Go sample uses real `openai-go` v1 style: `client.Files.New(ctx, openai.FileNewParams{File: openai.F[io.Reader](file), Purpose: openai.F(openai.FilePurposeUserData)})` with `option.WithAPIKey/WithBaseURL`; PHP: `CURLFile` multipart POST.)
Response: `{"id","object":"file","bytes","created_at","expires_at":null,"filename","purpose","status":null,"status_details":null}`.

### Choosing purpose
- `user_data` → model inputs (`input_file` in Responses, chat `file` parts). 
- `batch` → JSONL for Batch API (⚠ Batch not implemented); batch files follow provider expiry (OpenAI default 30 days).
- `assistants` → hosted File Search / Assistants-style vector stores, only if enabled (⚠ Assistants not implemented).
- `fine-tune` → JSONL datasets (⚠ fine-tuning not implemented). `vision` → image storage for vision flows (png/jpg/gif/webp; vision-capable models only). 
- Delete files you no longer need; non-batch files persist until deleted unless `expires_after` is set (fa/guides/data-controls).
- Direct file input in `/v1/responses`: `purpose="user_data"` + `input_file` with `file_id`; alternatives `file_url` (public) or inline `filename`+`file_data` (base64). Batch input limit in OpenAI reference 200 MB, AvalAI account/upload limit may be lower. Image tools don't read image files unless the route attaches the file to that tool.

## List — `GET /v1/files`
Query: `purpose`, `limit` (1–10000, default 10000), `order` (`asc|desc` by `created_at`, default `desc`), `after` (cursor file id). Response `{object:"list", data:[file…], first_id, last_id, has_more}`.
## Retrieve — `GET /v1/files/{file_id}` → file object.
## Delete — `DELETE /v1/files/{file_id}` → `{"id","object":"file","deleted":true}` (JS SDK: `client.files.del(id)`; newer SDK: `.delete`).
## Content — `GET /v1/files/{file_id}/content` → raw bytes (python `client.files.content(id).read()`; JS `Buffer.from(await content.arrayBuffer())`).

## Rate limits (per minute) and storage
| tier | uploads | downloads | deletes | max storage |
|---|---|---|---|---|
| 0 | 3 | 5 | 10 | 250 MB |
| 1 | 10 | 100 | 100 | 2 GB |
| 2 | 50 | 250 | 250 | 5 GB |
| 3 | 250 | 500 | 500 | 15 GB |
| 4 | 500 | 1000 | 1000 | 50 GB |
| 5 | 1500 | 2000 | 5000 | 200 GB |
When storage is full uploads are blocked until you delete files or upgrade tier.

## Using files in calls
Support depends on endpoint+model. Responses: `input_file.file_id` (uploaded `user_data`), `file_url`, or `filename`+`file_data`. OpenAI vision-capable models can take PDF `input_file` (extracted text + page images); non-PDFs are text-extracted; spreadsheets are summarized/augmented context, not exact cell data. Chat Completions: Gemini and other document-oriented models are often best for PDF `file` parts. For big doc sets use retrieval (embeddings) instead.
```python
client.chat.completions.create(model="gemini-2.5-flash",
  messages=[{"role":"user","content":[{"type":"text","text":"این سند را خلاصه کن"},{"type":"file","file":{"file_id":"file-…"}}]}])
client.responses.create(model="gpt-5.6-luna",
  input=[{"role":"user","content":[{"type":"input_text","text":"Summarize the uploaded file."},{"type":"input_file","file_id":"file-…"}]}])
```
(Source notes `gemini-2.5-flash` may not be Responses-enabled; Responses example model `gpt-5.6-luna`, and heading text says `gpt-5.5` — inconsistent; verify live ids. `gemini-2.5-flash` itself may be removed per deprecations — verify.)

## Storage & security
Stored on AWS S3 / GCP / Cloudflare. Treat uploads as customer data: upload secrets only when needed, short `expires_after` for temporary processing, delete after workflow; don't assume all providers/downstream tools share retention; check route/model/account controls before regulated/highly sensitive files; use file ids rather than base64 in logs/prompts and redact filenames/metadata containing personal data. Report vulns to security@avalai.ir (bug bounty for critical).

## Errors
400 invalid file/params · 401 · 403 · 404 · 413 >128 MB · 429 · 507 storage limit for tier.
Related: fa/guides/file-inputs, fa/guides/rate-limits, chat, authentication.
