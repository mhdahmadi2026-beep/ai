# File search tool (docs.avalai.ir/fa/guides/tools-file-search) — HOSTED VERSION NOT AVAILABLE

> ⚠ **Hosted File Search and provider-managed vector stores are IN DEVELOPMENT on AvalAI.** NEVER emit `client.vector_stores.*`, `vector_stores` REST calls, `purpose="assistants"` retrieval uploads or `tools:[{"type":"file_search"}]` as working code. For production RAG today: `/v1/embeddings` + your own chunk store/vector index + `/v1/responses`. (See guides/retrieval.md, embeddings.md; related pages not yet captured: examples/manual_rag_with_embeddings, rag-best-practices, citation-formatting.)

## What to build today (manual RAG)
1. Chunk files; keep stable source IDs (`policy.pdf#page=3`).
2. Embed with `/v1/embeddings`.
3. Store text, embedding, permissions, metadata in your DB/vector index.
4. Retrieve + rerank with filters (tenant, product, date, doc type).
5. Send only selected context to `/v1/responses`; require citations of source IDs.
```python
context = "\n\n".join(f"[{c['source_id']}]\n{c['text']}" for c in chunks)   # chunks from YOUR vector DB
client.responses.create(model="gpt-5.6-luna", input=[
  {"role":"system","content":"Answer only from the provided context. Cite source IDs in brackets. If the context is insufficient, say what is missing."},
  {"role":"user","content":f"Context:\n{context}\n\nQuestion: ..."}])
```
(JS equivalent identical; use `model` ids verified in `/v1/models`.)

## Preparing files & metadata (applies to manual and future hosted)
- Normalize text files to `utf-8` / `utf-16` / `ascii`; reject or convert unknown encodings before chunking.
- Keep source identity per chunk: file name, page/section, tenant, owner, version, last-updated timestamp.
- OpenAI-hosted formats (`.pdf .docx .md .txt .json`, code, `.pptx`) = planning reference only until AvalAI announces hosted support.
- Metadata small and filterable (OpenAI allows ≤16 attribute keys per vector-store file): stable keys such as `tenant`, `document_type`, `region`, `effective_date`, `version`.
- **Apply tenant/permission filters BEFORE retrieval** — the model must never receive chunks the current user can't read; keep access control out of the prompt.

## Mapping hosted controls → manual
| hosted | manual today |
|---|---|
| `vector_store_ids` | collection/tenant/namespace in your vector DB |
| `max_num_results` | `top_k` / reranked chunk cap |
| `filters` | SQL / vector-DB metadata filters |
| `ranking_options` | your reranker, score threshold, hybrid weights |
| `include:["file_search_call.results"]` | debug log of selected chunks, scores, source IDs |
| `file_citation` annotations | source IDs you ask the model to cite |
| `expires_after` | TTL / cleanup job for temp indexes & uploads |

## Future hosted flow (OpenAI-compatible; NOT enabled)
Upload (`purpose="assistants"`) → `vector_stores.create` (optional `expires_after:{anchor:"last_active_at",days:30}`) → attach files with `create_and_poll` (or poll `file_counts` until `completed`; `attributes`, `chunking_strategy:{type:"static",max_chunk_size_tokens:1000,chunk_overlap_tokens:200}`) → `/v1/responses` with `tools:[{"type":"file_search","vector_store_ids":[…],"max_num_results":5}]` → read `file_search_call` + `message` items. Large KBs: `file_batches.create_and_poll` (≤500 files/batch; per-file `attributes`/`chunking_strategy` via `files`). Filters shape: `{"type":"and","filters":[{"type":"eq","key":"tenant","value":"acme"},{"type":"in","key":"category","value":["policy","faq"]}]}`; `ranking_options:{ranker:"auto",score_threshold:0.25,hybrid_search:{embedding_weight:0.7,text_weight:0.3}}` (hybrid: at least one weight >0); `include:["file_search_call.results"]`.
Output: `file_search_call` (status; `queries`/`search_results` if included) + `message` with `file_citation` annotations in `output_text`. Render citations from annotations/source IDs (not free prose); hide citations to files the current user may not access and recheck the retrieval filter.

## Design notes (OpenAI retrieval docs)
Semantic search finds relevant chunks with little keyword overlap; hosted stores parse/chunk/embed/index; direct search returns 10 results by default (`max_num_results` ≤50); improve quality with query rewriting (`rewrite_query=true`; log both original and rewritten query), metadata filters, ranking options, score threshold; default chunk 800 tokens / 400 overlap, custom 100–4096 tokens, overlap ≤ half chunk; per-file limits 512 MB / 5,000,000 tokens (planning only, not an AvalAI commitment); `expires_after` for temp indexes/demos/customer uploads.

## Safety & ops
Upload only trusted, authorized files; tenant/permission filters outside the model; log retrieved chunk ids, scores, filters, final citations; validate tool args and returned links (prompt-injection/exfiltration); delete unused files/stores once hosted exists; after deleting a hosted file allow short eventual consistency (keep permission checks; cached results may linger); evaluate retrieval with real questions + expected source IDs before launch.
