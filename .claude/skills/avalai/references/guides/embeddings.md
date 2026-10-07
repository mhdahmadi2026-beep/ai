# Embeddings guide
Endpoint `POST /v1/embeddings` (see api-reference/embeddings.md). Uses: semantic search, RAG, recommendations, clustering, duplicate detection, classification, anomaly detection, code/docs search, diversity measurement, feature encoding.

## Pipeline
1 chunk docs with stable ids → 2 embed chunks → 3 store vectors + metadata (`document_id`, source URL, permissions, language, updated_at) → 4 embed query with SAME model + SAME dimensions → 5 nearest chunks (cosine/dot) → 6 pass best snippets to `/v1/responses` or `/v1/chat/completions`. Never mix models/dimensions in one index. Define index contract before ingest: model id, `dimensions`, distance metric, chunking policy, language strategy, metadata filters, retention rules, rebuild triggers (changing any → rebuild/backfill).

## Models / dimensions
OpenAI-compatible `text-embedding-3-small` (default 1536), `text-embedding-3-large` (default 3072), `text-embedding-ada-002`; provider-specific from Gemini, Cohere, Alibaba, Cloudflare, BAAI, NVIDIA NIM (check model-details + 10-deprecations). Use `dimensions` only if the model supports shortened vectors; smaller = cheaper storage/search but may hurt retrieval; set at embed time (don't truncate by hand if your store has a cap). v3 embeddings are normalized (length 1) → cosine and dot give same ranking. Token estimate: `cl100k_base`. Embeddings aren't fresh facts → embed & retrieve current docs. Empty input rejected; token limits per model/provider/route/tier → dry-run + check model-details and rate limits before bulk backfill.

## Cost / scale / freshness
Cost ≈ input tokens (`usage.prompt_tokens` → log), then storage/search. Cache embeddings for unchanged chunks, incremental backfill not full rebuild. Beyond small in-memory sets use a vector DB/search service (KNN). Enforce metadata filters OUTSIDE the model: tenant, permission, language, product, freshness, doc type first, then rank by similarity.

## Tuning semantic search
Rewrite vague queries into short searchable phrases (keep original question for final call); filter before ranking; tune `top_k` and similarity thresholds so weak chunks don't pollute context; combine semantic + keyword (exact IDs, product names, legal terms, Persian/English spelling variants); evaluate changes (chunk size, overlap, model, dimensions, ranking) with labelled questions first. See guides/retrieval.

## Retrieval eval set
Fields: `query`, `must_include_doc_ids`, `forbidden_doc_ids`, `filters`, `expected_answer_source`. Metrics: recall@k, MRR, latency, token cost, % grounded answers. Run before/after every index rebuild; include Persian-on-Persian, English-on-English and mixed-language queries.

## Call
```python
r = client.embeddings.create(model="text-embedding-3-small", input=[t1,t2], encoding_format="float")
vectors = [d.embedding for d in r.data]
```
Array `input` for immediate multi-text embedding; hosted batch NOT implemented (use client-side worker for offline jobs, see batch-processing).

## Production notes
Cache; stable chunk ids; store permission metadata and filter before sending context; count tokens first (token-counting guide); vectors are derived user data → same tenant isolation, retention and deletion as source docs (can reveal similarity patterns).

## Defects
- Cited limits are OpenAI's; AvalAI per-provider limits unspecified.
- "batch processing" mention conflicts with Batch API not being implemented.
