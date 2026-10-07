# Example: document processing with Mistral OCR (slug probably /examples/mistral_ocr_… — unconfirmed)

Companion to api-reference/ocr.md and guides/pdf-files.md (those are authoritative on params/pricing/limits; this page = recipes). Page uses `mistral-ocr-latest` (now → `mistral-ocr-4-0`; pin the id for reproducibility).

## Basics
- Endpoint `POST https://api.avalai.ir/v1/ocr`; SDK `Mistral(server_url="https://api.avalai.ir", api_key=…)` (NO /v1) → `client.ocr.process(model=…, document=…, pages=[…])`.
- `document`: `{"type":"document_url","document_url":<https|data:application/pdf;base64,…>}` or `{"type":"image_url","image_url":<https|data:image/jpeg;base64,…>}`. `/v1/files` is "not fully available" → use URL or base64.
- `pages` is **0-based** list (`[0,1,5]`); response `pages[].{index, markdown, images, dimensions{dpi,height,width}}`, `model`, `usage_info{pages_processed, doc_size_bytes}`. `include_image_base64:true` only if you need images (big payload).
- Advanced: `document_annotation_format` = `{"type":"json_object"}` or `{"type":"json_schema","json_schema":{"name":…,"schema":{…}}}` → result in `document_annotation` (**JSON string** → `json.loads`; may be null); `table_format:"html"` (default markdown); `extract_header`/`extract_footer: true`. Claimed: up to 2,000 pages/min, 50 MB limit.

## Document understanding (chat)
Chat Completions with `mistral-small-latest`: content parts `{"type":"text"}` + `{"type":"document_url","document_url":…}` or `{"type":"image_url","image_url":"<url string>"}` (Mistral-native: `image_url` is a plain string here, unlike OpenAI's `{url:…}` object). Alternative two-step: OCR → markdown → LLM extracts JSON (validate with `json.loads`; ask for JSON only; use schema mode instead where possible).

## NOT available
Batch OCR/processing (page marks "not implemented"; the sample loop is also broken – see below). Do not emit batch-OCR code; loop `/v1/ocr` with bounded concurrency + retries (examples/rate-limit-safe-parallel-requests.md) and cache by file hash.

## Troubleshooting / practice
Low quality: ≥200 DPI, correct orientation, contrast, PNG over JPEG for text. base64: right MIME, no line breaks (`base64 -w 0` on Linux; macOS `-i`), ≤50 MB. Large docs: select pages / split / raise client timeout. Errors: 413 too big, 415 bad format, 429 backoff, 5xx retry. Validate extracted dates/amounts, cache OCR results, parallelise independent docs, monitor `usage_info.pages_processed`.

## Defects of the source page (don't copy)
- Samples use stale `mistral-ocr-latest`; Python error handler imports `mistralai.exceptions.MistralAPIError` (SDK v1 doesn't expose that path; v2 differs) and checks `e.status_code`.
- JS uses `baseURL` (Mistral SDK option is `serverURL`) and `pages: Array.from({length:100})` which errors/wastes for shorter docs; `pages=list(range(0,100))` ≠ "process up to 100 pages" semantic for >100-page docs (silently skips the rest).
- Go samples for chat-completions payload are missing a trailing comma before `}` (does not compile).
- Sample JSON output shows `index: 1` while indices are 0-based; `doc_size_bytes: null`; `// …` comments inside JSON.
- Batch loop sample is broken: processing code is dedented outside the `for`, and `file://` URLs aren't supported by the API.
- "Responses equivalent" blocks are generic placeholders (`file_abc123`, example.com image) — not equivalents of the OCR/Mistral-native calls.
- Receipts example reads only `pages[0]`; multi-page receipts need all pages. JSON-schema `items` has no `required`/`additionalProperties:false`.
- Privacy: documents (IDs, financial) go to a third party → see guides/data-controls.md.
- Links `fa/news/2025-05-15-mistral-ocr-latest-added.md`, `fa/examples/processing_pdfs_in_chat_completion_api.md` (= examples/processing-pdf-files-chat.md).
