# Example: web search capabilities in LLMs (docs.avalai.ir/fa/examples/web_search_capabilities)

Overview page of the three search routes. Prefer `guides/tools-web-search.md` (newer, authoritative); this page is older and has several stale/broken samples. NOT the same as raw `/v1/search` (api-reference/search.md), which returns raw results with no LLM synthesis.

## Routes
| Route | Models listed on page | How |
|---|---|---|
| Native search (Chat Completions) | `gpt-4o-search-preview`, `gpt-4o-mini-search-preview` | none — model searches on its own |
| Tool-based (Responses) | `gpt-5.5`, `gpt-5.4`, `gpt-5.4-chat` (samples use `gpt-5.6-luna`) | `tools:[{"type":"web_search"}]` |
| Gemini (Chat Completions) | `gemini-3.5-flash`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite`, `gemini-2.5-pro/flash` | `tools:[{"googleSearch":{}}]` |
| Gemini native v1beta | same | `POST https://api.avalai.ir/v1beta/models/<m>:generateContent`, header `x-goog-api-key`, `tools:[{"google_search":{}}]`; SDK `genai.Client(api_key=…, http_options={"api_version":"v1beta","base_url":"https://api.avalai.ir"})` (NO /v1); read `candidates[0].grounding_metadata` (`web_search_queries`, `grounding_chunks[].web.{title,uri}`, `grounding_supports`) |
| Qwen (Chat Completions) | `qwen3.7-max`, `qwen3.7-plus`, `qwen3.6-flash` | `enable_search:true`, `search_options:{"search_strategy":"agent"}` (python: via `extra_body`); cost = tokens + $10 per 1,000 calls (agent, international) |

## Advanced (Responses, OpenAI)
- Types: non-reasoning quick lookup; agentic search with reasoning model (`reasoning:{"effort":"medium"}`); deep research (`o3-deep-research`, `search_context_size:"high"`).
- `filters:{"allowed_domains":[…]}` (domains without scheme), `user_location` (approximate hint only), `include:["web_search_call.action.sources"]` for all consulted URLs.
- Citations: Chat Completions → inline links; Responses → `url_citation` annotations (`url`, `title`, `start_index`, `end_index`) inside `output[*].content[*].annotations`.
- Pricing per 1K calls: gpt-5.5/gpt-4o(-search-preview) low $30 / medium $35 / high $50; gpt-5-mini/gpt-4o-mini(-search-preview) $25 / $27.5 / $30; Gemini "similar to OpenAI" (unverified — check 06-pricing.md). Plus token costs.
- Tips: precise questions, ask for sources, low temperature (0.1–0.3, ONLY on non-reasoning models), cache frequent searches, mini model for simple queries, verify critical facts, mock search in tests, backoff on 429.

## Defects / conflicts (do not copy)
- **Removed models:** `gpt-4o-search-preview` / `gpt-4o-mini-search-preview` are removed (10-deprecations.md); `o3-deep-research`/`o4-mini` samples are stale. Use Responses `web_search` with a current model; cannot assume `/v1/responses` for Gemini/Qwen.
- Citation code reads `response.annotations` — doesn't exist; walk `response.output` → `message` → `content` → `annotations`. Sources sample `response.json()["web_search_call"]["action"]["sources"]` is also wrong: `web_search_call` is an item inside `output`.
- jq sample `.annotations[]` on curl output is wrong for the same reason.
- Python `requests` samples use `"Bearer $AVALAI_API_KEY"` literally (no shell expansion) → use `os.environ`.
- Go samples use a non-existent `openai.NewClient(key)`/`CreateChatCompletion`/`CreateResponse` API, lowercase `model:`; several PHP/Go blocks are corrupted (PHP boilerplate pasted mid-Go code); PHP `OpenAI::client(key,[base_url])` is wrong → use `OpenAI::factory()->withBaseUri()`.
- Gemini `googleSearch:{"detail_level":"high"}` is not a documented parameter — don't use it. Responses-equivalent blocks use a dummy weather `function` tool instead of search (auto-generated, ignore).
- `temperature` with search-preview models; "searches mostly optimized for English" claim is a page statement, not guaranteed.
- Page links to `fa/examples/using_v1_search.md` (raw search example) — not yet captured.
