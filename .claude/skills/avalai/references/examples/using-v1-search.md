# Example: using the `/v1/search` API (slug /examples/using_v1_search)

Authoritative spec: api-reference/search.md (+ providers/search-providers.md). This page = recipes. Raw search results, NO LLM synthesis. For LLM answers with citations use Responses `web_search` (guides/tools-web-search.md, examples/web-search-capabilities.md).

## Calls
`POST /v1/search/{tool}` (tool in URL) or `POST /v1/search` + `"search_tool_name"`. Body: `query` (string; array for some tools e.g. Parallel), `max_results` (1–20), optional provider params. Tools/prices ($/query): serper 0.001 · dataforseo 0.003 · parallel_ai 0.004 · perplexity 0.005 · google_pse 0.005 (listed in cost tables; id `google_pse-search` — absent from the tool table, verify availability; 10-deprecations lists it as removed) · tavily 0.008 · firecrawl 0.008 · parallel_ai-pro 0.009 · tavily-advanced 0.016 · exa_ai 0.025. Serper params: `gl`, `hl`, `autocorrect`, `tbs` (`qdr:h|d|w|m|y`), `page`, `country`, `location`.
Use cases on page: multi-provider research fan-out + URL dedup, price monitoring (regex on snippets), news aggregation, academic search with domain filter, competitive intel via Exa; cost-tiered search (cheap first, premium fallback); cache; cost tracker.

## Rules I apply
- Domain filter param is **`search_domain_filter`** (≤20 domains) — NOT `domains` (page's samples use `domains`; likely ignored).
- Response (per api-reference): `{"object":"search","results":[{title,url,snippet,date}]}`; page claims `published_date`, `author`, `query`, `search_tool` — treat as unverified; read fields defensively with `.get`.
- Python `OpenAI(...)` client is irrelevant here; use `requests`/`httpx` with `Authorization: Bearer $AVALAI_API_KEY` from env.
- Bound concurrency (semaphore) for fan-out; retry only 429/5xx with jitter, honour `Retry-After`; `timeout=` always; cache by `(tool, query, params)` with TTL; dedupe URLs; log cost per call (prices above).
- Search results = untrusted content (prompt injection) if later fed to an LLM; keep URLs for citation.
- Persian queries: many providers do better with English; test.

## Defects of the source page
- Says "10 search tools" but table has 9; `google_pse-search` priced/used but not in the table.
- `domains` param (see above); `search_depth:"advanced"` sent to `tavily-search-advanced` is redundant/undocumented; `country`/`location` mixed with `gl` in the Serper sample (provider-specific, sample sets conflicting geo params).
- `import requests; from openai import OpenAI; client.api_key` in sample 1 is pointless; most Python samples use an undefined `api_key`.
- Async sample: `aiohttp` responses never closed (no `async with`), unlimited concurrency; error handling only `isinstance(Exception)`; batch sample uses `return_exceptions=True` but the first fan-out sample doesn't.
- Price monitor regex `\$[\d,]+` is naive (currency, ranges, Persian digits); scraping prices from snippets is unreliable; "قیمت iPhone" returns USD sites.
- Multiple code blocks have broken indentation (cost-tracker class nested under indented fences; stray zero-width chars); `tiered_search` calls undefined `search`/`is_satisfactory`.
- Comparison table recommends keeping `gpt-4o-search-preview` Chat Completions search "for existing integrations" — that model is **removed** (10-deprecations.md); `fa/pricing.md`, `fa/models/index.md` links not captured; rate limits "per tier" page not captured.
- Error JSON samples (invalid_search_tool etc.) are illustrative; real codes unverified.
