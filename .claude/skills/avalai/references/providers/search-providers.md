# Search tools via /v1/search (Tavily, DataForSEO, Exa, Parallel AI, + Perplexity)

Call `POST /v1/search/{tool}` or `POST /v1/search` with `search_tool_name`. Auth Bearer. Response (all): `{"object":"search","results":[{title,url,snippet,date}]}`. See api-reference/search.md.

## Tools
| tool id | $/query | notes |
|---|---|---|
| tavily-search | 0.008 | general web, RAG |
| tavily-search-advanced | 0.016 | deeper quality/filtering |
| dataforseo-search | 0.003 | cheapest, SEO, high volume |
| exa_ai-search | 0.025 | neural/semantic (note underscore in id) |
| parallel_ai-search | 0.004 | `processor` base |
| parallel_ai-search-pro | 0.009 | `processor:"pro"` |
| perplexity-search | see perplexity.md | |

## Common params
`query` (string; Parallel also accepts array of strings), `max_results` 1-20 (default 10), `search_domain_filter` (≤20 domains), `max_tokens_per_page` (default 1024), `country`.

## Per-tool params
- **Tavily `country`**: full lowercase English country NAME (e.g. `"united states"`, `"iran"`), only effective when topic=general. NOT ISO codes.
- **DataForSEO**: `country` = location name ("United States"), `language_code` ("en"), `depth` (≤700), `device` desktop|mobile|tablet, `os` (windows/macos/android/ios).
- **Exa / Parallel**: `country` documented as code ("US","GB","DE").
- **Parallel**: `processor` base|pro, `max_chars_per_result`.

## Choosing
Cheapest/high volume: dataforseo. RAG general: tavily. Semantic/research: exa. Fast/cheap batch: parallel. Pro quality: tavily-advanced / parallel pro.

## Source defects
- Exa/Parallel country described as code but Tavily needs names; inconsistent — test.
- Python samples use undefined `api_key`.
- Response JSON in docs lacks content/score fields; don't assume them.
