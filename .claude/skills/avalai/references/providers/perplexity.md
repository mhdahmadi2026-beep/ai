# Perplexity (Sonar + perplexity-search)

Source: /fa/providers/perplexity. Two services: Sonar LLMs (web-grounded, citations) and `perplexity-search` (raw search via `/v1/search`).

## Endpoint rules
- Sonar models: call **`/v1/chat/completions`** (native `citations`, `search_results`, `search_context_size`). `/v1/responses` only if model/route explicitly supports it; the docs' "Responses equivalent" examples actually use `gpt-5.6-luna` (summary text says `gpt-5.5`) — they are a migration pattern, NOT a Sonar call. Never send `model:"sonar*"` to `/v1/responses` unless verified.
- Raw search: `POST /v1/search/perplexity-search` or `POST /v1/search` with `search_tool_name:"perplexity-search"`.
- Python SDK: `response.citations` (extra field; use `getattr`/`model_extra` if the SDK hides it).

## Models (all: no training on customer data)
| id | ctx | reasoning | in $/1M | cached in | out | search ctx low/med/high per 1K req |
|---|---|---|---|---|---|---|
| sonar | 128K | no | 1.00 | 0.50 | 1.00 | 5 / 8 / 12 |
| sonar-pro | 200K | no (2x results) | 3.00 | 1.50 | 15.00 | 6 / 10 / 14 |
| sonar-reasoning | 128K | CoT | 1.00 | 0.50 | 5.00 | 5 / 8 / 14 |
| sonar-reasoning-pro | 128K | CoT (2x results) | 2.00 | 1.00 | 8.00 | 6 / 10 / 14 |
| sonar-deep-research | 128K | deep research | 2.00 | 1.00 | 8.00 | $5/1K all levels |

sonar-deep-research extras: reasoning tokens $3/1M, citation tokens $2/1M, $0.005 per search query. Use `max_tokens` ~8192; slow, consider streaming.

## perplexity-search params
`query` (req), `max_results`, `search_domain_filter` (array), `country` (code e.g. "US").

## Source defects
- Summary says Responses examples use `gpt-5.5`, code uses `gpt-5.6-luna`.
- Python example `api_key="your-avalai-api-key"` hard-coded; use env var.
- Check 10-deprecations.md before using sonar-reasoning* (Perplexity retires these upstream).
