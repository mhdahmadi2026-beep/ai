# Firecrawl Search (`firecrawl-search`)

`POST /v1/search/firecrawl-search` or `/v1/search` with `search_tool_name:"firecrawl-search"`. $0.008/query. Max results 1-20. Response = standard search format `{object:"search",results:[{title,url,snippet,date}]}`.

## Params
`query` (req), `max_results` (1-20, default 10), `sources` ["web"(default),"news","images"], `categories` [{"type":"github"|"research"|"pdf"}], `tbs` (qdr:h|d|w|m|y), `location` ("City,State,Country"), `country` (code), `ignoreInvalidURLs` (bool), `scrapeOptions` {formats:["markdown"], onlyMainContent, removeBase64Images}, `search_domain_filter` (≤20), `max_tokens_per_page` (1024).
Scraping full page content happens only when `scrapeOptions` is set (docs say default markdown/main-content is applied by the gateway).
Operators in query: `"exact"`, `-term`, `-site:`, `site:`, `inurl:`, `allinurl:`, `intitle:`, `allintitle:`, `related:`.

## Defects
- Docs mention "LiteLLM" as the layer — gateway internals leak; ignore.
- Response example shows only snippet, scraped markdown field name is undocumented — inspect real response.
- `api_key` undefined in samples.
