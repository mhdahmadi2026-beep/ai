# OCR API — `POST https://api.avalai.ir/v1/ocr` (docs: /fa/api-reference/ocr)

Mistral OCR 4 (`mistral-ocr-4-0`): extracts structured content from documents/images. Returns Markdown plus layout-aware info (bounding boxes, block classification, confidence), 170 languages. **Not an OpenAI-standard endpoint** — AvalAI-specific document-processing service (Mistral-style schema). `mistral-ocr-latest` is now an alias of `mistral-ocr-4-0` priced as OCR 4; pin `mistral-ocr-4-0` for reproducible deployments. (Page-ocr file model page: fa/models/mistral-ocr-2512; the older id may be removed — check live.)

Also accepts `file_id` from Files API per files.md (`/v1/ocr` listed as supported).

## Request
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | `mistral-ocr-4-0` |
| `document` | object | yes | `{type:"document_url", document_url:"…"}` (PDF/docs) or `{type:"image_url", image_url:"…"}`; base64 via data URL `data:application/pdf;base64,…` |
| `pages` | array | no | 0-based page indexes |
| `include_image_base64` | bool | no | return extracted images base64 (only when needed — big responses) |
| `image_limit` | int | no | max images |
| `image_min_size` | int | no | min px size (filter icons) |
| `id` | string | no | optional request id |
| `document_annotation_format` | object | no | structured doc-level output |
| `bbox_annotation_format` | object | no | structured bbox-level output |
| `extract_header` | bool | no | default false |
| `extract_footer` | bool | no | default false |
| `table_format` | string | no | `markdown` (default) or `html` (tables as `<table>` in `markdown` field) |

Annotation format `type`: `text` (default markdown), `json_object` (valid JSON; must instruct the model to produce JSON), `json_schema` (`{"type":"json_schema","json_schema":{"name":…,"schema":{…}}}` guaranteed to follow schema). Doc-level structured output returns in **`document_annotation` as a JSON string** → `json.loads(result["document_annotation"])`.
```json
{"model":"mistral-ocr-4-0","document":{"type":"document_url","document_url":"https://example.com/invoice.pdf"},
 "document_annotation_format":{"type":"json_schema","json_schema":{"name":"invoice_data","schema":{"type":"object","properties":{"invoice_number":{"type":"string"},"date":{"type":"string"},"total_amount":{"type":"number"},"vendor_name":{"type":"string"},"line_items":{"type":"array","items":{"type":"object","properties":{"description":{"type":"string"},"quantity":{"type":"number"},"unit_price":{"type":"number"}}}}},"required":["invoice_number","total_amount"]}}}}
```

## Pricing
`mistral-ocr-4-0`: **$0.004/page** OCR extraction; **$0.005/page** annotated.

## Examples
```bash
curl https://api.avalai.ir/v1/ocr -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"mistral-ocr-4-0","document":{"type":"document_url","document_url":"https://arxiv.org/pdf/2201.04234"},"pages":[0,1,2]}'
```
```python
r = requests.post("https://api.avalai.ir/v1/ocr", headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}", "Content-Type":"application/json"},
    json={"model":"mistral-ocr-4-0","document":{"type":"document_url","document_url":"https://…pdf"},"include_image_base64":True,"image_limit":10,"image_min_size":100,"table_format":"html"})
for p in r.json()["pages"]: print(p["index"], p["markdown"][:100])
```
Image: `document:{type:"image_url", image_url:"https://…png"}`. Go sample hard-codes the key and slices `Markdown[:100]` (panics on short pages) — use env var + bounds check. PHP: cURL, loop `$responseData['pages']`.
### Mistral SDK
```python
from mistralai import Mistral
client = Mistral(server_url="https://api.avalai.ir", api_key=os.environ["AVALAI_API_KEY"])
ocr = client.ocr.process(model="mistral-ocr-4-0", document={"type":"document_url","document_url":"https://arxiv.org/pdf/1805.04770"}, pages=list(range(0,100)))
```
Works for other Mistral SDKs with custom server URL (fa/providers/mistralai).

## Response
```json
{"pages":[{"index":0,"markdown":"# …","dimensions":{"dpi":200,"height":2200,"width":1700},"images":[{"image_base64":"…","bbox":{"x":100,"y":200,"width":300,"height":400}}]}],
 "model":"mistral-ocr-4-0","usage_info":{"pages_processed":29,"doc_size_bytes":3002783},"document_annotation":null,"object":"ocr"}
```
`document_annotation` is a JSON **string** when `document_annotation_format` is used (table says object; treat as string/null). `images` only when `include_image_base64:true`.

## Errors
400 invalid params/URL · 401 · 403 (permissions/quota) · 404 document URL unreachable · 413 too large · 429 · 500.

## Best practices
Use `pages` for big docs; only request images when needed; `image_min_size` to drop icons; document URLs must be publicly reachable (use base64 data URL or Files API for private docs); expect large payloads; cache OCR results; JSON Schema for invoices/forms/receipts; `table_format:"html"` for web display.
Related: fa/examples/processing_documents_with_mistral_ocr, fa/guides/pdf-files, vision, authentication, rate-limits, files.md.
