# PDF file inputs (guide)
Complements api-reference/files.md, api-reference/ocr.md, providers/mistral.md, guides/vision.md.

## Pick a path
| need | use |
|---|---|
| one-shot understanding of a public PDF | `/v1/responses` + `input_file` with `file_url` (HTTPS) |
| private PDF reused several times | upload `/v1/files` with `purpose="user_data"` → `input_file` `file_id` (needs file storage enabled; else URL/base64) |
| small local PDF, no persistence | `input_file` with `filename` + `file_data:"data:application/pdf;base64,..."` |
| many PDFs / repeated questions on a knowledge base | chunk → embed (`/v1/embeddings`) → retrieve → answer with `/v1/responses` (manual RAG / file-search patterns) |
| layout-aware extraction (Markdown + bboxes + confidence) | Mistral OCR (`/v1/ocr`, `mistral-ocr-4-0`) |

## Processing
Vision-capable models get BOTH extracted text and page images (useful for charts/forms/tables). Non-PDF docs / text files: text only, embedded images/charts NOT passed → convert to PDF first if visual fidelity matters. Spreadsheets = structured data: small sheets can go direct; for joins/aggregation/large sheets extract in your app and send compact summary or use retrieval. Don't stuff big document sets into one request.

## Request shapes (Responses)
`input:[{"role":"user","content":[{"type":"input_text","text":"..."},{"type":"input_file","file_url":"https://.../x.pdf"}]}]` (also `file_id`, or `filename`+`file_data`). Order of text/file parts is free. Upload: `client.files.create(file=open(...,"rb"), purpose="user_data")`. Linux base64: `base64 -w 0` (macOS `-i`).
Usage notes: PDFs cost text + page-image tokens even for text-heavy pages → test representative docs, log `usage.input_tokens`. Size: keep each file <50 MB and total file payload per request <50 MB (provider/model limits may be stricter → split or retrieve). Needs a model accepting text+image input. Auditable answers: ask for page numbers, visible quotes, table names/section headings; verify sample pages outside the model for contracts, invoices, medical, financial.

## Mistral OCR 4
Models `mistral-ocr-4-0`; `mistral-ocr-latest` now → ocr-4-0 (pin id for reproducibility). Markdown + bounding boxes, block-type classification (title, table, equation, signature), confidence info, 170 languages / 10 groups, complex layouts. Price: $0.004 per OCR page, $0.005 per annotated page. Limits: file ≤50 MB, ≤1000 pages; images PNG/JPEG/WEBP/non-animated GIF. Input: valid HTTP(S) URL or base64 data URL (file ids only if route supports for OCR). SDK: `Mistral(server_url="https://api.avalai.ir", api_key=...)` → `client.ocr.process(model="mistral-ocr-4-0", document={"type":"document_url","document_url":url_or_data_url}, pages=list(range(0,100)))`; images: `{"type":"image_url","image_url":...}`. REST: `POST /v1/ocr` with `{"model","document":{...},"include_image_base64":true}`. Output: `pages[]` `{index, markdown, images, dimensions{dpi,height,width}}`, `model`, `usage_info{pages_processed, doc_size_bytes}`.
Document understanding: Chat Completions with `mistral-small-latest` and content part `{"type":"document_url","document_url":...}` (Mistral-native part type; Responses equivalent uses `input_file`).

## Defects
- OCR "Responses equivalent" block shows `file_id` "Summarize the uploaded file" (generic, not same task).
- Mistral SDK samples use `baseURL` in JS (SDK option may differ: `serverURL`).
- Linked page /fa/providers/mistralai.md vs captured providers/mistral.md.
- Doc says 'pages=range(0,100)' as "up to 100 pages" – page indexes are 0-based.
