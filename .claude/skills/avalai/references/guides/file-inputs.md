# File inputs (guide)
Three carriers: **URL**, **Base64 data URL**, **`file_id`** (upload to `/v1/files` first). See guides/pdf-files.md, guides/vision.md, api-reference/files.md. Support depends on endpoint + model + file type + account limits → test your exact route.

| carrier | best for | pros | cons |
|---|---|---|---|
| URL | public files | simple | must be public HTTPS, fetch latency |
| Base64 | local/private | no upload step | ~+33% body; must stay under route limit |
| file id | big / reusable | clean, reusable, less network | needs upload + supported `purpose` |

## Endpoints accepting file inputs
`/v1/chat/completions`, `/v1/messages`, `/v1/responses`, `/v1/ocr`.

## How files are processed
PDFs: vision models get extracted text + page images. Text/code/rich docs: extracted text only (embedded images/charts/speaker notes/slide layout lost → convert to PDF for visual fidelity). Spreadsheets: OpenAI-style flow parses ≤ first 1000 rows per sheet + summary metadata/header, NOT every cell → use a deterministic pipeline for joins/formulas/reconciliation/charts; verify extracted facts (ask for page/row/sheet/section ids). Big knowledge base → embeddings RAG / file-search patterns, not one prompt.

## Carrier map (OpenAI-compatible)
| input | Chat Completions | Responses | note |
|---|---|---|---|
| public image URL | `image_url.url` | `input_image.image_url` | vision models |
| local image | data URL in `image_url.url` | data URL in `input_image.image_url` | reuse → upload `purpose="vision"` → `input_image.file_id` |
| public PDF/doc URL | provider-specific (Claude): `{"type":"file","file":{"file_id":"<URL>"}}` | `input_file.file_url` | don't put a URL in `file_id` for Responses; it's for uploaded files |
| uploaded PDF/doc | `{"type":"file","file":{"file_id":"file-..."}}` (provider-specific) | `input_file.file_id` | upload `purpose="user_data"` |
| inline PDF/doc | `{"type":"file","file":{"file_data":"data:application/pdf;base64,..."}}` | `input_file.filename` + `input_file.file_data` | full data URL |
| spreadsheet | provider file block | `input_file` (high-level summaries) | exact calc → parse in app |
Data URL format `data:{mime};base64,{data}`; Linux `base64 -w 0` / `| tr -d '\n'` (macOS `base64 -i`).

## Size limits (inline data)
Gemini 20 MB total inline; Mistral OCR 50 MB/doc, ≤1000 pages; OpenAI 20 MB/request; Anthropic 32 MB/request; others 20 MB. May differ from provider's own limits → contact support for more. OpenAI public doc has a combined `input_file` limit (≈50 MB/request) — AvalAI table above wins; see files API.

## Supported types
Images: JPEG, PNG, GIF (static, 1 frame), WebP. Docs: PDF. Audio: mp3 (`audio/mp3|mpeg`), wav, m4a, flac. Spreadsheets: `.xlsx` (`application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`), `.xls` (`application/vnd.ms-excel`). Some `/v1/responses` routes also take txt/md/json/html/xml/source, doc/docx/rtf/odt, ppt/pptx, csv/tsv (provider/endpoint-dependent; else convert to PDF or text).

## Files API flow
`client.files.create(file=open("document.pdf","rb"), purpose="user_data")` → `file.id`; reuse across chat/responses/messages/ocr/images edits. Beta availability/limits/pricing → api-reference/files.md + guides/rate-limits.md.

## Model specifics
- **Gemini**: image carriers must be **base64** (no URLs); 20 MB total inline; ≤3,600 images/request (2.5 Pro, 2.0 Flash, 1.5).
- **OpenAI**: Responses → `file_url` / `file_id` (`user_data`) / `filename`+`file_data`; PDF+page-image needs vision-capable model (gpt-5.5/5.4…); big/repeated corpora → retrieval.
- **Anthropic**: URL and Base64 for PDFs/images; 32 MB/request.
- **Mistral OCR**: 50 MB / 1000 pages; `document_url` and `image_url` types.

## Best practices / troubleshooting
URLs for public (smaller requests); Base64 for local under limits; file id for large/reused; check size before send, compress images, split docs; validate MIME before encoding. Errors: size exceeded → Files API/compress/split; unsupported file type → fix MIME/extension; invalid base64 → no newlines, correct data URL; unable to fetch URL → must be public (no auth), correct content-type, HTTPS.

## Audio via chat file part (Gemini-style)
`{"type":"file","file":{"file_data":"data:audio/mp3;base64,..."}}` with `gemini-2.5-flash` (transcribe). Responses route for audio inline not guaranteed → transcribe first (STT) then send transcript to `/v1/responses`.

## Defects
- Go samples mix `openai.FileRequest`/`ChatMessageFile` (non-existent in openai-go) and lowercase `model:` in several; Responses Go sample `ResponseInput`/`outputText` invented.
- Chat PDF-URL sample abuses `file_id` for a URL (Claude-specific quirk).
- Model ids used (claude-sonnet-4-6, gemini-2.5-flash) may be deprecated — check 10-deprecations.
- Mistral sample uses `mistral-ocr-latest` (now ocr-4-0).
