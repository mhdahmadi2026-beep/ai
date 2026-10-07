# Web search tool (docs.avalai.ir/fa/guides/tools-web-search)

Let models search the web before answering, via `/v1/responses` `tools:[{"type":"web_search"}]`. The model decides whether to search unless you force it with `tool_choice`.

## Which path
| Need | Path | Note |
|---|---|---|
| New AI answers with citations | `/v1/responses` + `web_search` | default for Responses-first apps |
| Raw search results for your app | `/v1/search` (api-reference/search.md) | URLs/snippets/provider metadata, no LLM synthesis |
| Existing Chat-Completions search apps | `/v1/chat/completions` + search model | **legacy; the search-preview models are REMOVED** (see below) |
`search_context_size`: `low` quick lookup · `medium` (default) balanced · `high` richer sources (higher cost/latency). It's a quality/cost/latency knob, NOT a token counter, source-count or citation-count guarantee, and doesn't persist context across turns. Pricing per 1K calls by model/size: see guides/tools.md / 06-pricing.md.

```python
client.responses.create(model="gpt-5.6-luna", tools=[{"type":"web_search"}], input="…")  # response.output_text
```
(Go sample bug: `model:` lowercase field in `ResponsesCreateParams` doesn't compile → `Model`; PHP/JS/cURL equivalents are the same body.) Force: `tool_choice={"type":"web_search"}` (or `"required"`).

## Versions / legacy migration
Use `web_search` for new work. `web_search_preview` = legacy, lacks filters, live-access control and token-budget return → migrate to `{"type":"web_search"}`.
**⚠ Conflict:** the page says `gpt-4o-search-preview` / `gpt-4o-mini-search-preview` are still listed with shutdown planned **2026-07-23**; per 10-deprecations.md (lines 56, 74) the shutdown already happened (replacement `gpt-5.6-terra`) and the aliases are "removed" — today is 2026-10-07 → **don't use them**; use Responses `web_search` (e.g. with `gpt-5.5`). Raw `/v1/search` stays for URL/snippet needs.
Modes: quick lookup (low/medium, optional search, short answer) · agentic research (reasoning models search, inspect, re-search) · deep research (high effort + background processing; guides/background-processing.md — hosted background is NOT available on AvalAI, see that file; guides/deep-research.md).

## Output & citations
`response.output` contains `web_search_call` (id, status, `action` = `search` | `open_page` | `find_in_page`, e.g. `{"type":"search","query":"…"}`) and a `message` with `content[0].text` + `content[0].annotations` of `url_citation` (`url`, `title`, `start_index`, `end_index`). Inline citations must be **clearly visible and clickable** in your UI.
Checklist: render url_citation as clickable links near the claim; keep url/title/span; request `include:["web_search_call.action.sources"]` for the full list of consulted sources (audit); log `web_search_call.action`; a recency-sensitive answer with no citations = ungrounded → retry with `tool_choice:"required"` or sharper prompt. (See guides/citation-formatting – not yet captured.)

## User location (hint only)
`tools:[{"type":"web_search","user_location":{"type":"approximate","country":"GB","city":"London","region":"London"}}]`; `country` ISO-3166 2-letter, `timezone` IANA (e.g. `America/Chicago`), city/region free text. Only a relevance hint — never for compliance, billing, access control or safety decisions. Not supported in deep-research web search.

## Advanced controls (when model/route supports)
- `filters.allowed_domains` / `filters.blocked_domains` (≤100 each; no `https://`, e.g. `who.int`, `pubmed.ncbi.nlm.nih.gov`; subdomains covered).
- `include:["web_search_call.action.sources"]` (full source list), `["web_search_call.results"]` (image results).
- `external_web_access:false` → cached/indexed only (offline/restricted runs); default live access.
- `return_token_budget`: `"default"` | `"unlimited"` (only GPT-5-family reasoning search, if route supports; higher latency/cost; pair with background for multi-minute reports).
- Image search: `search_content_types:["image","text"]`, `image_settings:{"max_results":3,"caption":true}`, read `web_search_call.results` items (`image_url`, `source_website_url`, `thumbnail_url`, `caption`); validate source domain and image URL before displaying/proxying.
Example (trusted sources + audit): allowed `["who.int","cdc.gov","fda.gov"]`, blocked `["reddit.com","quora.com"]`, `include=["web_search_call.action.sources"]`, `tool_choice="auto"`.
Privacy: live web search = external data flow; claim HIPAA/BAA/ZDR/residency or offline guarantees only if the chosen model's route explicitly supports it; never put secrets/private account data/raw personal identifiers in search queries.

## Limits
- Chat-Completions search models use a specialist path without the new Responses controls (filters, full sources, live-access, token budget).
- Only use model ids that exist in AvalAI's catalog (page says `data/models.json`; live `/v1/models` for you).
- `auto` = optional search; `required`/explicit tool when it must run.
- Model rate limits apply along with tool pricing; see privacy-policy and content-policy (safety pages not captured).
Related: api-reference/responses, citation-formatting, tools, pricing, providers/openai.
