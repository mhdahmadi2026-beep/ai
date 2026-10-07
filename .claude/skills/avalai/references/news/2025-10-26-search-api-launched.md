# News 2025-10-26 (1404-08-04): Search API (docs.avalai.ir/fa/news/2025-10-26-search-api-launched)

`/v1/search` (Perplexity-search-compatible), tool in URL (`/v1/search/{tool}`) or body `search_tool_name`.
Tools & $/query: dataforseo-search 0.003; parallel_ai-search 0.004; perplexity-search 0.005; google_pse-search 0.005; tavily-search 0.008; parallel_ai-search-pro 0.009; tavily-search-advanced 0.016; exa_ai-search 0.025.
Params: `query` (string or list), `max_results` 1–20, `search_domain_filter` (≤20 domains), `country`, tokens per page. Response `{object:"search", results:[{title,url,snippet,date}]}`. Multi-query = more results (cost per query likely multiplies — verify). Examples in examples/using-v1-search.md.
