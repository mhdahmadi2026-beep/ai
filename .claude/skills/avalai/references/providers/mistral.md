# Mistral AI provider page (docs: /fa/providers/mistralai)

## Endpoint style
Mistral SDK uses `server_url="https://api.avalai.ir"` (**no `/v1`**): `Mistral(server_url=…, api_key=…)`. Chat models are also reachable OpenAI-style via `/v1/chat/completions`.

## Models
- `mistral-large-3` — open-source (Apache 2.0) sparse MoE, 41B active / 675B total; native multimodal (image understanding); 40+ languages; LMArena OSS non-reasoning #2; NVFP4 checkpoint, runs on one 8×A100/H100 node (vLLM). Price: in $0.50, cached $0.05, out $1.50 per 1M (+$0.001/page). Reasoning, multilingual chat, doc understanding, code, agents.
- `codestral-2501` — 22B code model, 80+ languages, fill-in-the-middle, 32K ctx; HumanEval/MBPP/CruxEval/RepoBench leader; code completion, tests, SQL, translation, debugging.
- `mistral-small-2503` — general efficient model; 1M-token ctx(as stated); cost-effective generation/summarization/QA/classification.
- `mistral-large-latest` used in the page's chat-over-OCR examples (verify id).
## OCR — `mistral-ocr-4-0` (see ocr.md)
Markdown + bounding boxes + block classification (title/table/equation/signature) + inline confidence; 170 languages / 10 language groups; PDF, DOC, PPT, OpenDocument, images; structured Document AI annotation in the same endpoint. `mistral-ocr-latest` → `mistral-ocr-4-0` (same price); pin versioned id. Price: **$0.004/page** OCR (=$4/1000), **$0.005/annotated page**. Files: PDF ≤50 MB and 1000 pages; PNG/JPEG/WEBP/non-animated GIF. (`mistral-ocr-2505`, `mistral-ocr-2503` removed.) News 2026-07-17-kimi-k3-mistral-ocr-4-added.
```python
client = Mistral(server_url="https://api.avalai.ir", api_key=…)
client.ocr.process(model="mistral-ocr-4-0", document={"type":"document_url","document_url":"https://arxiv.org/pdf/1805.04770"}, pages=list(range(0,100)))
```
Base64 PDF: `document_url = "data:application/pdf;base64,…"`. Specific pages: `pages=[0,1,5]`. JS: `new Mistral({apiKey, baseURL})` (SDK option name may be `serverURL` — verify). Document Q&A: OCR pages → feed `ocr_response.pages[i].text` (SDK field is `.markdown`, page snippet uses `.text`) into `client.chat(...)` (legacy API; newer SDK `client.chat.complete(...)` with plain dict messages; `mistralai.models.chat.ChatMessage` import is old). Use cases: scientific papers, historical docs, KB building, lecture notes, legal, engineering.
