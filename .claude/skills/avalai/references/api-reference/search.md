# Search API — `/v1/search` (docs: /fa/api-reference/search)

Standalone web-search API returning **raw structured results** for programmatic use. **Different** from the hosted web-search tool in Chat/Responses (fa/guides/tools-web-search), which augments LLM answers with live data. Launch news: fa/news/2025-10-26-search-api-launched.

## Endpoints
- `POST https://api.avalai.ir/v1/search` — tool in body as `search_tool_name`
- `POST https://api.avalai.ir/v1/search/{search_tool_name}` — tool in URL
Bearer auth.

## Tools (page says "10 tools from 8 providers"; table lists 9 rows — the 10th, Google PSE, is referenced under providers/google but its id/price isn't in the table → check `/v1/models` / pricing)
| tool | provider | $/query | best for |
|---|---|---|---|
| `serper-search` | Serper | 0.001 | cheapest Google-based; localization, time filters |
| `dataforseo-search` | DataForSEO | 0.003 | low cost, advanced filtering (device/os/depth) |
| `parallel_ai-search` | Parallel AI | 0.004 | fast parallel processing, multi-query |
| `perplexity-search` | Perplexity | 0.005 | AI-enhanced quality results |
| `tavily-search` | Tavily | 0.008 | general web search, country filter |
| `firecrawl-search` | Firecrawl | 0.008 | multi-source search + content extraction/scraping |
| `parallel_ai-search-pro` | Parallel AI | 0.009 | advanced parallel, multi-query |
| `tavily-search-advanced` | Tavily | 0.016 | advanced filtering, higher quality |
| `exa_ai-search` | Exa AI | 0.025 | neural semantic search |

## Standard body
| param | type | req | notes |
|---|---|---|---|
| `query` | string \| array | yes | array = multiple queries at once (supported by some tools, e.g. Parallel AI) |
| `search_tool_name` | string | conditional | required for `/v1/search` (not when in URL) |
| `max_results` | int | no | 1–20, default 10 |
| `search_domain_filter` | array | no | ≤20 domains |
| `max_tokens_per_page` | int | no | default 1024 |
| `country` | string | no | format varies per provider |

## Provider-specific params
- **Tavily**: `country` = full lowercase name (`"united states"`, `"united kingdom"`) — list in fa/providers/tavily.
- **Serper**: `gl` (country code e.g. `uk`,`us`,`de`), `hl` (language), `autocorrect` (bool), `tbs` (`qdr:h|d|w|m|y`), `page`, `location` (`"Berlin,Germany"`), `country` (`"DE"`).
- **DataForSEO**: `country` (full name `"United States"`), `language_code`, `depth` (≤700 results), `device` (desktop|mobile|tablet), `os` (windows|macos|android|ios).
- **Firecrawl**: `sources` (`web|news|images`), `categories` (`[{"type":"github"|"research"|"pdf"}]`), `tbs`, `location`, `ignoreInvalidURLs`, `scrapeOptions` (fa/providers/firecrawl).
- **Parallel AI**: `processor` (`base`|`pro`), `max_chars_per_result`.
(Perplexity example uses `country: "US"` ISO code — Tavily wants full name; per-provider mismatch is expected.)

## Response (consistent across providers)
```json
{"object":"search","results":[{"title":"…","url":"https://…","snippet":"…","date":"2024-01-15"}]}
```
`date` optional.

## Examples
```bash
curl https://api.avalai.ir/v1/search/perplexity-search -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"query":"latest AI developments 2024","max_results":5,"search_domain_filter":["arxiv.org","nature.com"],"country":"US"}'
curl https://api.avalai.ir/v1/search -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"search_tool_name":"tavily-search","query":"machine learning tutorials","max_results":10}'
curl https://api.avalai.ir/v1/search/serper-search … -d '{"query":"restaurants","max_results":10,"gl":"uk","hl":"en","autocorrect":false,"tbs":"qdr:d","page":1,"country":"DE","location":"Berlin,Germany"}'
curl https://api.avalai.ir/v1/search/parallel_ai-search-pro … -d '{"query":["AI developments","machine learning trends","neural networks"],"max_results":5}'
```
```python
r = requests.post("https://api.avalai.ir/v1/search/perplexity-search",
    headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}", "Content-Type":"application/json"},
    json={"query":"…","max_results":5,"search_domain_filter":["arxiv.org"],"country":"US"})
for x in r.json()["results"]: print(x["title"], x["url"])
```
(Source snippets use an undefined `api_key` variable — use env var. JS: `fetch` + `data.results.forEach`.)

## Choosing
- By cost: serper < dataforseo < parallel_ai < perplexity < tavily/firecrawl < parallel_ai pro < tavily advanced < exa.
- High volume: serper · cost-sensitive filtering: dataforseo · AI-quality: perplexity · semantic: exa · general: tavily · extraction: firecrawl · multi-query: parallel_ai(-pro).

## Best practices
Pick tool by need (cost/quality/features); use `search_domain_filter`; set `max_results`; handle errors; respect per-provider rate limits; **cache results** to cut cost. Errors: 200/400/401/429/500.
Related: fa/providers/{perplexity,tavily,firecrawl,dataforseo,exa_ai,google,parallel_ai,serper}, pricing, authentication, fa/examples/web_search_capabilities, fa/guides/tools-web-search.
