# Tools overview (docs.avalai.ir/fa/guides/tools)

Extend model capability with web search, function calling, deferred tool loading and route-dependent hosted tools. **Most portable AvalAI pattern: `/v1/responses` with `web_search` for public/fresh web context + custom `function` tools for your data, side effects and approval flows.** Other hosted tool families depend on model AND route; when a hosted tool isn't enabled, implement it in your app and return results via `function_call_output`.

```python
client.responses.create(model="gpt-5.6-luna", tools=[{"type":"web_search"}], input="What was a positive news story from today?")  # output_text
```
(cURL/JS/Go/PHP samples are the same body to `POST /v1/responses`.)

## Tool families
| Family | OpenAI-compatible shape | AvalAI guidance |
|---|---|---|
| Web search | `{"type":"web_search"}` | best default for fresh public context (guides/tools-web-search – not yet captured) |
| Function calling | `{"type":"function",…}` | private data, side effects, human approval, your integrations (guides/function-calling.md) |
| File search | `{"type":"file_search",…}` | **hosted vector store NOT available** → app-side RAG with embeddings (guides/retrieval.md, embeddings.md) |
| Computer use / shell / code interpreter | hosted tool objects | availability-dependent; unless AvalAI announces support for the chosen model → your own function tool/runtime |
| `tool_search` | `{"type":"tool_search"}` | OpenAI documents for `gpt-5.4`+; verify AvalAI/model support first |
| Image generation tool | `{"type":"image_generation"}` | prefer AvalAI image endpoints (guides/image-generation.md migration path) unless route supports it |
| Remote MCP / connectors | `{"type":"mcp",…}` | only if route supports AND server/connector/OAuth domains/approval policy trusted |

Choosing the smallest sufficient layer: fresh public → `web_search` (inspect `web_search_call` items for sources/query metadata); private data/side effects → narrow `function` tool with strict JSON Schema; big private KB → app-side RAG; many related ops → namespaces (<10 functions each) and `tool_search` only after confirming support; third-party services → official remote MCP/trusted connectors with `allowed_tools` and required approval for writes/sensitive reads; hosted runtimes (shell, code interpreter, skills, computer use) → run your own sandbox if not enabled.

## GPT Actions → AvalAI (don't document as an API route)
Actions = ChatGPT/Custom-GPT surface (OpenAPI+auth+instructions). Port the principles: OpenAPI operation schema → `function` JSON Schema (or small MCP server); read action → read-only backend fn (`lookup_order`, `search_docs`, `get_forecast`); consequential action → write/purchase fn with app-side approval before execution; action auth → keep credentials in backend, never in prompt; response → compact raw JSON for the model to summarize.
Auth mapping: **None** only for public read-only data (add rate limit/abuse monitoring); **API key** server-side, model calls e.g. `lookup_shipping_rate`, backend validates args then adds key; **OAuth** run login flow in your app, refresh tokens in secret store, send short-lived access token downstream (MCP/connectors: `authorization` field on every request); keep OAuth `state` check, exact redirect URL, log auth errors without secrets; split unauthenticated discovery (`search_public_docs`) from personal/write actions (`create_ticket`, `send_email` need login+approval). Keep endpoints narrow, short precise descriptions, validate args before network calls, backoff on 429/5xx, async long jobs. OpenAI Actions assume public HTTPS/TLS, ~45 s timeout, text payloads, <100,000 chars → treat as conservative guardrails.

## Code Interpreter / hosted runtime fallback
Use hosted `{"type":"code_interpreter"}` only if the route explicitly supports it. Otherwise expose a function (e.g. `run_python_analysis`) with explicit inputs (code, allowed files, time limit, expected artifact type): server-side restricted container (no raw shell/arbitrary network), validate code/args, CPU/mem/time/file limits, idempotent retries, store uploaded/generated files in your storage and return stable URL/file id + summary + `stdout`/`stderr` via `function_call_output`; treat charts/CSVs/notebooks as untrusted until scanned/signed/approved. Keep artifact/approval policy if hosted becomes available.

## Standard tool guides (links, mostly uncaptured)
tools-web-search, tools-file-search, tools-computer-use, function-calling (captured), tools-code-interpreter, tools-shell, tools-connectors-mcp.

## Gemini-specific tools (Chat Completions, camelCase tool objects)
Models: `gemini-3.5-flash`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite`, `gemini-2.5-pro/flash` (verify live).
- `tools=[{"codeExecution":{}}]` — code execution; **when enabled no other tool can be used**.
- `tools=[{"googleSearch":{}}]` — Google Search grounding; **can only combine with `urlContext`**.
- `tools=[{"urlContext":{}}]` — experimental; model fetches URLs in the user content; raises input tokens; can combine with googleSearch.
- Function declarations can only be used alone.
Responses migration: no direct equivalent of `codeExecution`/`urlContext` (don't replace with an unrelated function tool; keep Gemini Chat, or fetch+clean the page server-side and pass text); `googleSearch` → `web_search` (+ `search_context_size`, `include=["web_search_call.action.sources"]` for structured sources) with a Responses-capable model. (The page's "Responses equivalent" blocks swap in `gpt-5.6-luna`.)

## Alibaba/DashScope web search
Qwen uses a parameter, not `tools`: `extra_body={"enable_search": True, "search_options": {"search_strategy": "agent"}}` on Chat Completions (`qwen3.7-max`, `qwen3.7-plus`, `qwen3.6-plus`, `qwen3.6-flash`; old `qwen3-max` snapshots maybe). `search_strategy:"agent"` required for international regions; results are added to the prompt (more input tokens). Don't carry `enable_search` to `/v1/responses` → use `web_search` with a Responses model if you want Responses.

## Tool pricing (on top of token cost)
Code Interpreter $0.03/session · File Search storage $0.10/GB/day (1 GB free) · File Search tool calls $2.50/1K (Responses only) · Web search per 1K calls: gpt-5.5/5.4/5.4-pro low $30, medium (default) $35, high $50; gpt-5.4-mini/nano low $25, medium $27.50, high $30; Qwen3.7-max/plus, 3.6-flash (agent) $10. See 06-pricing.md. (File Search/Code Interpreter hosted prices are listed though hosted vector stores aren't available on AvalAI.)

## Using tools in the API
`tools` param on `/v1/responses`; model decides automatically; steer with `tool_choice` (`auto` | `required` | `none`).
Output item model (`response.output` is a typed array): `message`; `reasoning` (keep with later tool outputs if the route returns it); `web_search_call`; `function_call` (parse `arguments`, run trusted code, send `function_call_output` with same `call_id`); `function_call_output`; `tool_search_call`/`tool_search_output` (hosted: `execution:"server"`, `call_id:null`; client-executed: return same `call_id`); `mcp_list_tools`/`mcp_call` (validate/cache tools, approval for sensitive ops, treat outputs as third-party data); `image_generation_call`. With `previous_response_id` compatible routes carry these items forward; when replaying state yourself append prior typed items + new tool outputs in order.

### Design checklist
- `tool_choice`: `auto`/`required`/`none`.
- `parallel_tool_calls:false` when tools mutate state, need confirmation or ordered execution.
- `max_tool_calls` (where supported) = overall cap on built-in hosted tool calls, not per tool.
- `include` extras only when needed: `web_search_call.action.sources`, `code_interpreter_call.outputs`, `file_search_call.results`, computer output image URL.
- Many functions: expose only likely ones; namespaces for CRM/billing/doc ops (<10 fns each); `additional_tools` input item for tools discovered outside `tools` (keep its position when replaying).
- Keep tool surface small, descriptions precise, don't make the model guess args the app knows.

### Deferred loading with `tool_search` (only after verifying support)
`defer_loading:true` on functions inside a `namespace` tool (not on the namespace); add `{"type":"tool_search"}`. Hosted: API loads relevant deferred tools; client-executed: `tool_search` with `execution:"client"` → model emits `tool_search_call`, you search your registry and return `tool_search_output` with loaded tools (same `call_id`). Prefer namespaces/MCP servers over many individual deferred functions (a standalone deferred function still shows name+description). Loaded tools are injected near the end of context to preserve prompt cache — don't change the loaded set mid-conversation. Example body: `{"model","input","tools":[{"type":"namespace","name":"crm","description":…,"tools":[{"type":"function","name":"get_customer_profile",…,"strict":true},{"type":"function","name":"list_open_orders","defer_loading":true,…,"strict":true}]},{"type":"tool_search"}],"parallel_tool_calls":false}`.

### Remote MCP / connectors safety
Route/model-dependent; if `type:"mcp"`/connector not enabled keep the integration in your backend as `function` tools. When enabled: trusted (ideally official) servers only; least-privilege OAuth/API tokens, never in prompts, rotate; pass `authorization` on every request that needs it (don't assume hosted Responses state stores secrets); limit tools with `allowed_tools`; require approval for payments/account changes/deletes/email/external writes (continue approved calls with `previous_response_id` or replay typed items); review/log data sent to third-party MCP; validate domains of URLs/images returned by MCP; keep `mcp_list_tools` items in state to avoid relisting. (Guide guides/tools-connectors-mcp not yet captured.)

### Agents SDK
Same concepts: attach hosted/function tools to a specialist agent or expose a specialist agent as a tool for a manager. Treat as orchestration pattern, not hosted feature; use SDK only if it can target AvalAI (base URL/model options), else orchestrate yourself against `/v1/responses`. Keep strict schemas, clear descriptions, bounded outputs; approval/multi-tenancy/secrets/side-effect checks in your app; inspect typed items (`function_call`, `mcp_call`, `web_search_call`, `message`) for audit/billing; return compact summaries from sub-agents.

### Function calling
Custom functions via `tools` — see guides/function-calling.md.
