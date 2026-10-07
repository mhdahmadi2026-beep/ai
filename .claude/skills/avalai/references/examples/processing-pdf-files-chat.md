# Example: processing PDF files with Claude/Gemini via Chat Completions (slug probably /examples/processing_pdf_files — unconfirmed)

Chat-Completions-flavoured companion to guides/pdf-files.md (Responses `input_file`). Use this for Claude/Gemini models on `/v1/chat/completions`.

## Models (page)
Claude: `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5` (samples also use `claude-sonnet-5` — inconsistent; verify the id in 06-pricing/models before use). Gemini: `gemini-3.1-pro-preview`, `gemini-3.5-flash`, `gemini-2.5-pro`, `gemini-2.5-flash`. Gemini also takes base64 of: PDF `application/pdf`, JS, Python, TXT, HTML, CSS, Markdown (`text/md`), CSV, XML, RTF.

## Request shape (Chat Completions content part)
```json
{"type":"file","file":{"file_id":"https://host/doc.pdf"}}                       // URL (Claude only)
{"type":"file","file":{"file_data":"data:application/pdf;base64,<B64>"}}         // base64 (Claude + Gemini)
{"type":"file","file":{"file_id":"<url>","format":"application/pdf"}}            // optional explicit format
```
Put the text part alongside; best results with the question AFTER the PDF. Note: `file_id` carries a **URL** here (AvalAI/Claude extension), unlike OpenAI where it is an uploaded-file id. Gemini = base64 only (no URL).

## Limits (page)
| | Claude | Gemini |
|---|---|---|
| file size | 32 MB/request | 20 MB inline (up to 50 MB via File API — not available via Chat Completions here) |
| pages | 100 | 1,000 |
| tokens | ~1,500–3,000/page | ~258/page |
| format | standard PDF, no password/encryption | same |
Tips: URL path is more efficient for big files; low temperature (~0.2) for fact extraction (only non-reasoning models); split big docs; scanned/complex PDFs may parse poorly → consider `/v1/ocr` (guides/pdf-files.md); log `usage.prompt_tokens`; ask for page numbers/quotes for auditability.

## Defects / conflicts
- Bash base64 sample uses `base64 -i` (macOS); Linux needs `base64 -w 0`. The curl sample builds JSON by shell interpolation of a huge string → write the body to a file and use `curl -d @body.json`.
- Python base64 sample reuses the name `response` for requests and OpenAI results; the Go samples (`openai.ChatMessageContent`, `ChatMessageFile`) don't exist in the official SDK; PHP samples hard-code `claude-sonnet-4-6` while others use `claude-sonnet-5`.
- "Responses equivalent" blocks are auto-generated placeholders (`file_id: file_abc123`, summarize-upload) — NOT equivalents of the URL/base64 samples; for Responses use `input_file` with `file_url`/`file_data` (guides/pdf-files.md). They say Claude may not be enabled on `/v1/responses`.
- Page links `fa/guides/rate-limits.md` (not captured; tiers pages still pending).
- Troubleshooting says "specify `application/pdf`"; `format` is optional and not in standard OpenAI schema → provider-specific.
