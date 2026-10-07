# Retrieval (guide) — hosted `vector_stores` / `file_search` NOT available on AvalAI
Banner: hosted Retrieval, provider-managed `vector_stores`, hosted `file_search` are in development. **Don't emit `client.vector_stores.*` / `file_search` tool code as working.** Build retrieval in your app: `/v1/embeddings` + your own vector DB/search index + `/v1/responses` or `/v1/chat/completions` for generation.

## Availability
| capability | status | today |
|---|---|---|
| `/v1/embeddings` | available | embed chunks + queries |
| `/v1/responses` | available for supported models | grounded answers |
| `/v1/chat/completions` | available | keep existing flows, put retrieved context in messages |
| hosted `vector_stores` | in development | own DB/vector DB/search index |
| hosted `file_search` | in development | app-side retrieval; migrate when announced |

## Pattern
1 prepare docs (extract, chunk by topic, stable source ids) 2 embed chunks and query (`/v1/embeddings`, same model+dims) 3 retrieve: tenant/permission filters FIRST, then similarity 4 rerank + truncate to confident chunks that fit context budget 5 generate with sources and REQUIRE citations by source id.
Source formatting: `[{source_id} score={score}]\n{text}` joined by blank lines. Developer instruction: "Answer only from the provided sources. Cite source IDs in brackets. If the sources are insufficient, say what is missing." Chat: roles `developer` + `user` ("Sources:\n…\n\nQuestion: …") (doc example model `claude-sonnet-5`); Responses: `instructions=…`, `input=f"Sources:\n{sources}\n\nQuestion: {question}"` → `output_text`. Migration: messages→input, developer/system→instructions, `choices[0].message.content`→`output_text`, tool calls/citations/structured items → inspect `response.output` by `type`.

## Query rewriting
Rewrite vague conversational questions into short searchable phrases ("Can I get my money back if I never used the product?" → "refund policy unused digital product"); log original AND rewritten query (hosted future: `rewrite_query=true`, returned `search_query` is telemetry, not a replacement for the user's message).

## Filter + ranking
Deterministic filters before similarity (e.g. `{"tenant":"acme","language":"fa","document_type":["policy","faq"],"published_after":"2026-01-01"}`); never rely on the model for access control. Tune: `top_k`/`max_num_results` (lower = latency/cost, higher = recall); score threshold (drop weak chunks, let the model say context is insufficient); `ranker` (hosted: start `auto`, pin only for reproducible evals); `hybrid_search.embedding_weight` (↑ semantic) / `text_weight` (↑ exact product names/IDs/policy terms; at least one > 0); rerank top candidates before synthesis.

## Hosted reference (future compat only — don't run)
`files.create(purpose="assistants")` → `vector_stores.create(name, expires_after={"anchor":"last_active_at","days":14})` → `vector_stores.files.create_and_poll(vector_store_id, file_id, attributes={...}, chunking_strategy={"type":"static","max_chunk_size_tokens":1000,"chunk_overlap_tokens":200})` → `vector_stores.search(vector_store_id, query, max_num_results=5, rewrite_query=True, ranking_options={"ranker":"auto","score_threshold":0.25,"hybrid_search":{"embedding_weight":0.7,"text_weight":0.3}})`. Batch ingest `file_batches.create_and_poll` with `file_ids` (shared settings) OR per-file `files` array (attributes/chunking) — not both.
OpenAI reference numbers (planning only, not AvalAI commitments): default 10 results, `max_num_results` ≤50; file attributes ≤16 keys, 256 chars per key; default chunk 800 tokens/overlap 400, custom 100–4096 tokens, overlap ≤ half chunk; file ≤512 MB and 5,000,000 tokens; ≤500 files per batch; `expires_after` deletes related `vector_store.file` objects on expiry; deletion/expiry eventually consistent → keep authorization at retrieval layer.

## Safety & eval
Permissions (tenant/user/document) at retrieval layer; store source id with every chunk; enforce citations in instructions; validate retrieved links and tool args (prompt injection/exfiltration); log query rewrites, filters, scores, selected chunks, model answer, user feedback; eval retrieval separately from answer quality (source recall, source precision, first-correct-rank, MRR, MAP) on a small real-question set; eval sets with expected answer, expected source ids, unacceptable hallucinations.
Related (not yet captured): guides/tools-file-search, citation-formatting, rag-best-practices, examples/manual_rag_with_embeddings.

## Defects
- Banner says hosted is "in development" yet a long hosted code sample is shown (reference only).
- Chat sample uses role `developer` with Claude (adapter-dependent).
