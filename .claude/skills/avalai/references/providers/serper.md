# Serper Search (`serper-search`)
`POST /v1/search/serper-search` or `/v1/search` + `search_tool_name`. Google results, **$0.001/query** (cheapest). max_results 1-20.
Params: standard (`query`, `max_results`, `search_domain_filter`≤20, `max_tokens_per_page`, `country` code, `location` "Berlin,Germany") + Serper: `gl` (country, e.g. uk), `hl` (language, e.g. fa), `autocorrect` (false to disable), `tbs` (qdr:h|d|w|m|y), `page` (int).
Response: standard `{object:"search",results:[{title,url,snippet,date}]}`.
