# Rerank API — `POST https://api.avalai.ir/v1/rerank` (docs: /fa/api-reference/rerank)

Re-order documents by relevance to a query (RAG quality, search relevance). **Not supported by the official OpenAI SDK** → call plain HTTP/REST (requests/fetch/curl/net/http).

## Request
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | `cohere-rerank-v4.0-pro`, `cohere-rerank-v4.0-fast`, `cohere.rerank-v3-5:0`, `qwen3-rerank` |
| `query` | string | yes | |
| `documents` | array | yes | array of strings **or** objects `{ "id": "doc1", "text": "…" }` |
| `top_n` | int | no | default = all documents |
| `return_documents` | bool | no | default `true` |
| `user` | string | no | end-user id |

```bash
curl https://api.avalai.ir/v1/rerank -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"cohere.rerank-v3-5:0","query":"مزایای انرژی‌های تجدیدپذیر چیست؟","documents":["…","…","…","…"]}'
```
```python
r = requests.post("https://api.avalai.ir/v1/rerank", headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}", "Content-Type":"application/json"},
    json={"model":"cohere-rerank-v4.0-fast","query":q,"documents":docs,"top_n":3})
for d in r.json()["results"]: print(d["index"], d["relevance_score"], d["document"]["text"])
```
(Source snippets hard-code `API_KEY = "YOUR_AVALAI_API_KEY"` — use the env var; JS uses `require("node-fetch")` — Node 18+ has global `fetch`; Go uses deprecated `ioutil` → `io.ReadAll`; PHP plain cURL.)

## Response
```json
{"results":[{"index":0,"relevance_score":0.9876,"document":{"text":"…"}}, …]}
```
Sorted by `relevance_score` descending (0–1). `index` = position in your input array (use it to map back); `document` holds `text` (+ original `id` if given). With `return_documents:false` don't rely on `document` being present.

## Models
| provider | model | context | price |
|---|---|---|---|
| Cohere | `cohere-rerank-v4.0-pro` | 32,768 tokens | $0.0025/query — best quality, 8× larger window, 100+ languages, YAML docs |
| Cohere | `cohere-rerank-v4.0-fast` | 32,768 | $0.002/query — cost-efficient high throughput, 100+ languages |
| Cohere | `cohere.rerank-v3-5:0` | 4,096 | $1.00 / 1K units — previous generation |
| Alibaba | `qwen3-rerank` | (not in table) | see pricing |
Prefer v4 models for new work; v3.5 has a small 4,096-token window. (Source examples all use `cohere.rerank-v3-5:0`.)

## Patterns
- **RAG:** retrieve candidates (embeddings/keyword) → rerank with `query` → keep top 2–N → put into LLM prompt (chat or responses). Typical: over-retrieve (e.g. 20–50), rerank, pass top 3–5.
- **Search relevance:** cheap keyword/vector recall first, rerank for semantic precision.
- Pairs with `/v1/embeddings` (see embeddings.md) and fa/guides/rag-best-practices.
- Source RAG example uses `gpt-5.6-luna`; its Responses note incorrectly shows a file-summary snippet (copy-paste artifact) — ignore; verify model ids via `/v1/models`.

## Errors
400/401/403/404/429/500 standard (fa/guides/error-handling). Related: fa/providers/cohere, authentication, rate-limits.
