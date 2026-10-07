# Embeddings API — `POST https://api.avalai.ir/v1/embeddings` (docs: /fa/api-reference/embeddings)

Convert text (and, on some models, images/audio/video/PDF) to vectors for semantic search, clustering, classification, recommendation, dedup, anomaly detection.

## Workflow
1. One model + one dimension size per index; query and docs MUST use the same model and dims.
2. Normalize + chunk text first; keep stable chunk ids so unchanged docs aren't re-embedded.
3. Store vectors with metadata (source URL, doc id, permissions, language, updated-at, tenant).
4. Search by cosine or dot product (per vector store); same metric at index and query time.
5. Feed retrieved snippets to `/v1/responses` or `/v1/chat/completions`; don't let the model guess from memory. Full flow: fa/examples/manual_rag_with_embeddings, fa/guides/rag-best-practices.

## Request body
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | embedding model id |
| `input` | string \| array | yes | string or array of strings (batching in ONE request; different from hosted `/v1/batches`, which AvalAI says is separate/offline — note rate-limits doc says no Batch API) |
| `encoding_format` | string | no | `float` (default) or `base64` — use float for most vector DBs |
| `dimensions` | int | no | only on models that support it (text-embedding-3-*, Gemini); smaller = cheaper storage/search, maybe lower quality |
| `user` | string | no | end-user id |

Notes: plan cost from input; OpenAI-compatible responses give `usage.prompt_tokens/total_tokens`; AvalAI pricing and provider routes may differ → check pricing before big backfills. Count tokens first (fa/guides/token-counting; OpenAI `text-embedding-3-*` use `cl100k_base`). **No empty strings.** Per-input and aggregate request limits vary by model/provider route/tier → split big ingests into bounded batches and retry failed chunks safely. Manual truncation: normalize before comparing (prefer the `dimensions` param).

```bash
curl https://api.avalai.ir/v1/embeddings -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"text-embedding-3-small","input":"The food was delicious and the service was excellent."}'
```
```python
import os
from openai import OpenAI
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
r = client.embeddings.create(model="text-embedding-3-small", input="The food was delicious and the service was excellent.")
v = r.data[0].embedding; print(len(v), v[:5])
```
```javascript
const r = await client.embeddings.create({ model: "text-embedding-3-small", input: "…" });
const v = r.data[0].embedding;
```
Go (as in source; `openai.EmbeddingRequest`/`CreateEmbeddings` belong to the **sashabaranov/go-openai** API, not `github.com/openai/openai-go` — source import mismatch; use go-openai with `config.BaseURL`):
```go
resp, err := client.CreateEmbeddings(ctx, openai.EmbeddingRequest{Model: openai.SmallEmbedding3, Input: []string{"…"}})
```
PHP: POST JSON with cURL to `/v1/embeddings` with Bearer header; read `$data['data'][0]['embedding']` (HTTP ≥400 → print body).

### Batch inputs / custom dims
```python
r = client.embeddings.create(model="text-embedding-3-small", input=["a","b","c"])
for i, e in enumerate(r.data): print(i, len(e.embedding))
r = client.embeddings.create(model="text-embedding-3-large", input="…", dimensions=1024, encoding_format="float")
```

## Response
```json
{"object":"list","data":[{"object":"embedding","embedding":[0.0023064255,-0.009327292,…],"index":0}],
 "model":"text-embedding-3-small","usage":{"prompt_tokens":8,"total_tokens":8}}
```
`data[].index` maps to input array position; `usage.total_tokens == prompt_tokens`.

## Models (mode `embedding`)
| provider | model | dims / input window | note |
|---|---|---|---|
| OpenAI | `text-embedding-3-large` | 3072; 8191 tok | supports `dimensions` |
| OpenAI | `text-embedding-3-small` | 1536; 8191 | search/cluster/classify/recommend |
| OpenAI | `text-embedding-ada-002` | 1536; 8191 | legacy, for existing indexes |
| Google | `gemini-embedding-2` | up to 3072; 8192 | multimodal (text/image/audio/video/PDF) on supported routes |
| Google | `gemini-embedding-001` | up to 3072; 2048 | task-specific via provider params |
| Cohere | `embed-v-4-0` | up to 3072; 128k | via Azure AI; text+image on `/v1/embeddings` |
| Cohere | `cohere.embed-v4:0` | up to 1536; 128k | via AWS Bedrock, multimodal |
| Cohere | `cohere.embed-multilingual-v3` | 1024; provider window | multilingual |
| Alibaba | `text-embedding-v4` | 2048; 1024 | latest Qwen text |
| Alibaba | `text-embedding-v3` | 1024; 1024 | multilingual |
| Alibaba | `tongyi-embedding-vision-plus` | 1152; 1024 | multimodal text/image/video |
| Alibaba | `tongyi-embedding-vision-flash` | 768; 1024 | faster multimodal |
| Cloudflare | `cf.plamo-embedding-1b` | provider; 4096 | |
| Cloudflare | `cf.embeddinggemma-300m` | provider; 2048 | compact |
| Nvidia NIM | `nvidia_nim.nv-embedqa-e5-v5`, `nvidia_nim.nv-embed-v1` | provider | |
| BAAI via NIM | `nvidia_nim.bge-m3` | provider | multilingual |
(Deprecations page removed many NIM ids → verify live via `/v1/models`.)

## Similarity & storage
- Cosine is a safe default; OpenAI embeddings are unit-length, so cosine ≈ dot product ≈ same ranking as Euclidean.
- Don't mix providers/dimensions in one index unless validated with a small labelled eval set; keep that eval when changing model/chunking/dims.
- Vectors are derived user data: apply source-doc retention, deletion, access control, tenant isolation (they can leak similarity/corpus membership). Embeddings are not a factual knowledge base about recent events — embed your own current docs and retrieve.
- K-nearest at scale: use a vector DB/search service; store source id, tenant/permission metadata, language, time, doc type for deterministic pre-filtering.

## Common uses (code in source)
- **Semantic search:** embed query + docs (array input), cosine via numpy `np.dot(a,b)/(norm(a)*norm(b))`, rank.
- **Classification:** embed labelled texts → `LogisticRegression().fit(embeddings, labels)` → predict on embedded new texts.

## Gemini embeddings
Two ways. Default (no params) at 3072 dims is pre-normalized.
### A) OpenAI schema on `/v1/embeddings` + `extra_body`
```python
r = client.embeddings.create(model="gemini-embedding-001",
    input=["معنای زندگی چیست؟","هدف وجود چیست؟","چگونه کیک درست کنم؟"],
    extra_body={"task_type":"SEMANTIC_SIMILARITY","output_dimensionality":768})
```
JS needs `// @ts-expect-error` + `extra_body:{task_type, output_dimensionality}`. curl: nest `"extra_body":{…}` in JSON body as shown in docs (with the OpenAI SDK, `extra_body` is merged into the top-level body — in raw curl the source nests it literally; if raw curl ignores it, put `task_type`/`output_dimensionality` at top level — verify).
Task types: `SEMANTIC_SIMILARITY`, `CLASSIFICATION`, `CLUSTERING`, `RETRIEVAL_DOCUMENT` (index docs), `RETRIEVAL_QUERY` (queries), `CODE_RETRIEVAL_QUERY`, `QUESTION_ANSWERING`, `FACT_VERIFICATION`.
### B) Native Google GenAI SDK (base `https://api.avalai.ir`, `api_version:"v1beta"`)
```python
from google import genai; from google.genai import types
client = genai.Client(api_key=os.environ["AVALAI_API_KEY"], http_options={"api_version":"v1beta","base_url":"https://api.avalai.ir"})
r = client.models.embed_content(model="gemini-embedding-001", contents=[…],
    config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY", output_dimensionality=768))
vals = [e.values for e in r.embeddings]
```
JS: `new GoogleGenAI({apiKey, httpOptions:{apiVersion:"v1beta", baseUrl:"https://api.avalai.ir"}})` (source snippet has an extra `}` — typo); `ai.models.embedContent({model, contents, taskType, outputDimensionality})` (in the real SDK these go in `config:{…}` — flagged).
curl native: `POST https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent` header `x-goog-api-key: $AVALAI_API_KEY`, body `{"contents":[{"parts":[{"text":"…"}]}], "embedding_config":{"task_type":…,"output_dimensionality":768}}`. Native response: `{"embeddings":[{"values":[…]}]}`.
### Output dims (Matryoshka/MRL)
3072 (default, normalized) · 1536 · 768 · 512 · 256 · 128. **For dims < 3072 you must L2-normalize** (`v/np.linalg.norm(v)`) before similarity.
### RAG pattern
Docs with `RETRIEVAL_DOCUMENT` + queries with `RETRIEVAL_QUERY`, both `output_dimensionality=768`, normalize all, cosine, `np.argsort(sim)[-k:][::-1]`.

## Errors
400/401/403/404/429/500 standard; see fa/guides/error-handling.

## Related
fa/models/model-details · fa/examples/manual_rag_with_embeddings · fa/guides/rag-best-practices · fa/guides/token-counting · authentication · fa/guides/rate-limits.
