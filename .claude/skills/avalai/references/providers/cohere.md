# Cohere provider page (docs: /fa/providers/cohere)

Enterprise chat, RAG, embeddings, rerank.
## Chat (Command)
- `cohere.command-r-plus`: 128K; 0.50 in / 1.50 out per 1M (page); advanced RAG, tool use (function calling), multilingual.
- `cohere.command-r`: 128K; page lists the same 0.50/1.50 (note "usually lower than R+ — check Cohere pricing"); RAG/tool use balance.
- `cohere.command`, `cohere.command-light` older, smaller ctx. RAG docs/citations passed per Cohere chat shape (OpenAI endpoint ignores `documents`; put snippets in the prompt).
## Rerank (`POST /v1/rerank`, see rerank.md)
`cohere-rerank-v4.0-pro` (32,768 ctx; $0.0025/query; 100+ languages), `cohere-rerank-v4.0-fast` ($0.002/query), `cohere.rerank-v3-5:0` ($1.00 / 1K search units). Use raw HTTP with `query`, `documents`, `top_n`.
## Embeddings (see embeddings.md)
- `cohere.embed-english-v3.0`: 1024 dims, max 512 tokens, $0.10/1M; `input_type` = `search_document|search_query|classification|clustering` (pass via `extra_body` on OpenAI SDK — the page shows it as a direct kwarg; not valid in OpenAI SDK).
- `cohere.embed-multilingual-v3.0`: 1024 dims, 512 tokens text, $0.10/1M; 100+ languages; image embedding needs special handling.
- `cohere.embed-v4:0` (AWS): multimodal text/image/PDF mix; 128K ctx; dims 256/512/1024/**1536 default**; pricing: contact; cosine/dot/euclid.
- `embed-v-4-0` (Azure AI Services): same embeddings, **up to 30× higher rate limits than the AWS endpoint**; text $0.12/1M, image $0.47/1M; best for high-throughput production. Both produce identical embeddings → choose by rate limit needs. Params: `dimensions` (256/512/1024/1536), `encoding_format:"float"`.
- Light and v2 variants may exist.
