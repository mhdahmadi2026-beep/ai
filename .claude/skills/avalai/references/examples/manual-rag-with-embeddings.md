# Manual RAG with embeddings (docs.avalai.ir/fa/examples/manual_rag_with_embeddings)

Small RAG pipeline with embeddings + Responses API; adapted from OpenAI Cookbook (Question_answering_using_embeddings, File_Search_Responses). **This is the supported path on AvalAI today**: hosted File Search / vector stores are in development (tools-file-search.md). Use it when you want your own DB/search, deterministic filters before generation, direct retrieval-quality evaluation, or hosted vector stores aren't available for your endpoint.

## Mapping hosted File Search → manual
| hosted | manual today |
|---|---|
| `vector_store` | DB table, object store, FAISS/Milvus/Pinecone index or your search service |
| `vector_store.file` | chunk with stable `id`, source filename, attributes, text, embedding |
| `max_num_results` | retrieval `k` + context token budget |
| `filters` / `attributes` | SQL/search filter applied BEFORE vector similarity |
| `include` search results | log chunk id, score, filename, retrieved text |
| `file_citation` | source IDs you instruct the model to cite |
(Hosted flow for reference: upload → create vector store → attach files → wait for indexing `completed` → `/v1/responses` with `file_search` → inspect `file_search_call` + `message` items.)

## Retrieval controls worth keeping
Query rewriting (vague question → short searchable query before embedding); hybrid retrieval (dense + keyword/BM25 for product names, exact IDs, policy terms); metadata filters (tenant, region, product, permission, date, doc type) before ranking; score threshold to drop weak chunks; chunking by heading/semantic section with small overlap + source metadata; evaluate `Recall@k`, `MRR`, grounded answers before changing chunk size or `k`. Document retrieval vs user memory need different write policies → examples/persistent-agent-memory.md (slug `durable_agent_memory` per this page's link).

## Python example (`rag_demo.py`)
`pip install openai numpy`; `EMBEDDING_MODEL="text-embedding-3-small"`, `GENERATION_MODEL="gpt-5.6-luna"`, `MIN_RETRIEVAL_SCORE=0.2`; `Document(id,title,text,embedding)` list (3 support policies: refunds, rate-limits, keys). Flow: `embed_texts(list)` (ONE batched `client.embeddings.create(model, input=[...])`) → `index_documents()` stores embeddings → `retrieve(query,k=2)` (embed query, cosine, sort, threshold, top-k) → `answer_with_context(question)`: context = `[id] title\ntext` blocks; `client.responses.create(model, instructions="Answer only from the provided context. If the context is not enough, say that the documentation does not contain the answer. Cite source IDs.", input=f"Context:\n{context}\n\nQuestion: {question}")` → `output_text`.
JS version: same, but **`retrieve()` re-embeds ALL documents on every question** (embeddings should be cached/indexed once) — fix by computing `documentEmbeddings` once at startup. cURL: test `/v1/embeddings` (array input) and `/v1/responses` separately.
Defects/notes: cosine without zero-norm guard (v3 embeddings are normalized, fine); no `store:false`; if `matches` is empty the prompt has empty context — handle explicitly ("not enough information"); `MIN_RETRIEVAL_SCORE=0.2` is arbitrary → tune on labelled queries.

## Evaluate retrieval from day one
Store the expected document id per test question; `Recall@k` (expected doc in top k?); `MRR` (rank of first correct doc); log retrieved ids next to each generated answer; review low-score matches before raising `k` (more context ≠ better answers).

## Best practices
Chunk long docs by section/heading (not just character count); keep source IDs stable so citations stay usable; store metadata per chunk for pre-retrieval filtering; `dimensions` only if your vector store needs shorter vectors — same dimension for documents and queries; put retrieved context before the user question and clearly separate chunks; tell the model to say so when context is insufficient; cache embeddings of unchanged docs.
Related: api-reference/embeddings, responses, rag-best-practices, rate-limits.
