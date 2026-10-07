# Responses vs Chat Completions (docs.avalai.ir/fa/guides/responses-vs-chat-completions)

Compare `/v1/responses` and `/v1/chat/completions` (adapts OpenAI's migrate-to-responses, function-calling, structured-outputs guides; AvalAI endpoint/key/route notes).

## Why Responses
Newest primary, agentic API: simplicity of Chat + agentic capability; typed output items, `instructions` + flexible `input`, `previous_response_id` state, reasoning, built-in tools (route/model dependent): web search, file search (hosted NOT available), computer use, code interpreter, image generation tool, Remote MCP, custom function loops. On AvalAI start new text/reasoning/tool flows on Responses when the chosen model supports `/v1/responses`; keep Chat Completions for stable existing integrations and chat-only providers.

## Capability comparison
| capability | Chat | Responses |
|---|---|---|
| text generation | ✓ | ✓ |
| audio | ✓ | route/model dependent → `/v1/audio` or Realtime routes (hosted Realtime not available) |
| vision | ✓ | ✓ |
| structured outputs | ✓ | ✓ |
| function calling | ✓ | ✓ |
| web / file search / computer use | — | route/model dependent |
| code interpreter | — | planned / route dependent |
| remote MCP / connectors | — | route/model/account dependent |
| image generation as tool | — | route/model dependent; else `/v1/images` |
| reasoning summaries | — | route/model dependent |
Hosted tools aren't generic across providers: check provider page/API reference before release. Provider-independent web retrieval → AvalAI `/v1/search` unless the route explicitly supports Responses `web_search`.

## Chat isn't going away
Industry standard, still supported for existing integrations; Responses recommended for new projects (tools, code execution, state management, future model features). New models are added to both APIs when possible; some are Responses-only (built-in-tool models like computer use; multi-turn background generation like o1-pro). Each model page says Chat, Responses or both.

## Stateful API & semantic events
Responses has a predictable event-driven architecture (typed semantic events, e.g. text-added), vs Chat appending to `content` as tokens arrive (manual diff tracking). Multi-turn + reasoning logic is easier; handlers target specific events with better type safety.

## Migration path (per integration, stepwise)
1. `POST /v1/chat/completions` → `POST /v1/responses`. 2. `messages` → `input` (plain transcripts often map directly); stable system/developer guidance → top-level `instructions`. 3. Read text from `response.output_text`, not `choices[0].message.content`. 4. For reasoning/tools/files/images/multimodal iterate `response.output` by `type`. 5. Multi-step: `previous_response_id` (API-managed) vs re-sending prior output items (stateless control). 6. Update streaming consumers to typed Responses events, not Chat `delta` chunks. 7. `response_format` → `text.format`. 8. Function calling: return tool results as `function_call_output` items with matching `call_id`. 9. Function schemas: tools are internally tagged (flat), compatible schemas may be normalized to strict mode unless `strict:false`. 10. Decide state retention: `store:true` or `store:false`.

### Field map
| Chat | Responses | note |
|---|---|---|
| `messages` | `input` (string or array of input items) | separate stable system/developer guidance into `instructions` |
| `choices[0].message.content` | `response.output_text` / `response.output` | typed items for tools/reasoning/images/multimodal |
| `choices[].message.tool_calls` | `output` items `type:"function_call"` | reply with `function_call_output` + same `call_id` |
| `response_format` | `text.format` | prefer strict JSON Schema when supported; JSON mode as fallback |
| `reasoning_effort` | `reasoning.effort` | only on models/routes exposing it |
| `n` (multiple choices) | not supported | send separate requests and pay each |
| stream chunks `choices[].delta` | typed SSE: `response.created`, `response.output_text.delta`, `response.completed`, `error`, function-call-argument events | branch on `event.type`; don't append non-text events to the UI buffer |
| `user` | `safety_identifier` and/or `prompt_cache_key` | opaque privacy-preserving ids; never raw PII/request ids as cache keys |

### Gradual rollout checklist
Start with a simple text path, then tool-heavy ones; compare behaviour, latency, token use, errors before routing prod traffic; keep Chat active for stable integrations, migrate flow by flow; for compliance/stateless flows don't assume `previous_response_id` is allowed — re-send needed output items; `previous_response_id` simplifies context but prior context still counts toward input tokens.
Per-flow metrics: output quality (golden prompts, reasoning/tool success, Structured Output validity, refusals); latency (TTFT, full latency, background completion, tail); cost (in/out/reasoning/cache-hit tokens, tool-call extras); reliability (error codes, retries, incomplete responses, stream drops, tool-call idempotency); compliance (`store:true`, `previous_response_id`, encrypted reasoning, manual item replay, app storage).

### State, storage & compliance
- **API-managed state**: `previous_response_id` where the route stores prior responses and policy allows server-side continuity; resend stable `instructions` every request (not carried over).
- **App-managed state**: `store:false` and re-send needed input/output items (stateless, deterministic replay, stricter retention).
- **Reasoning continuity**: request `include:["reasoning.encrypted_content"]` if supported and return items next turn; otherwise keep ordinary `reasoning`/`function_call`/`function_call_output` items or use `previous_response_id`.
- Not a cost shortcut. Regulated workloads: document the chosen state mode vs retention requirements before production (data-controls.md).

### Native tools vs custom functions
Web: AvalAI `/v1/search` for provider-independent retrieval; Responses `web_search` only if the route/model explicitly supports it. Keep custom `function` tools for internal DBs, CRMs, billing, private APIs, write operations, any side effect your server must authorize (validate args server-side, idempotent retries). Hosted file search, code interpreter, computer use, image generation, Remote MCP, connectors = route/model/account dependent → keep a fallback (your retrieval layer, sandbox, image endpoint, file workflow, app-managed MCP proxy). In tool-heavy reasoning migrations, don't drop typed output items when carrying context manually: keep `reasoning`, `function_call`, `function_call_output`, plus `phase` if present — or use `previous_response_id` where stored state is allowed. Put tool-specific guidance in the tool description (what it does, when to use, inputs, side effects, retry safety, common errors); system/developer prompts for global policies.

## Code comparison
Text generation: Chat `messages=[{"role":"user","content":…}]` → `completion.choices[0].message.content`; Responses `input=[{"role":"user","content":…}]` (or string) → `response.output_text`. Response shapes: Chat `[{index, message:{role,content,refusal}, logprobs, finish_reason}]`; Responses `[{id:"msg_…", type:"message", role:"assistant", content:[{type:"output_text", text, annotations:[]}]}]`. Responses are stored by default; Chat completions stored by default for new accounts; `store:false` disables for either.
Doc sample defects: Go example mixes `openai.F(…)` (v1 style) with `openai-go/v3` imports and has lowercase `model:` in `ResponseNewParams` (doesn't compile); the "Chat Completions" Python block redefines `client` mid-snippet; the PHP block re-creates the client; JS shows both calls in one snippet.

## Key differences
`output` vs `choices`; one candidate per request (no `n`); `text.format` vs `response_format` (structured-outputs.md); function-calling shapes differ in request config AND response items (function-calling.md); `reasoning.effort` vs `reasoning_effort` (reasoning.md); Responses SDK `output_text` helper; manual state in Chat vs `previous_response_id`; typed streaming events (`response.created`, `response.output_text.delta`, `response.completed`, `error`, `response.function_call_arguments.delta/.done`); tool + reasoning flows are item-based — preserve `reasoning`, `function_call`, `function_call_output`.

## Common migration mistakes
Reading `choices[0].message.content` instead of `output_text`/`output`; assuming every output item is a message; dropping `reasoning`/`function_call`/`function_call_output` on manual replay; returning tool results without the matching `call_id`; assuming Chat non-strict function schemas stay non-strict (check `strict`, `required`, `additionalProperties`); sending `response_format` to `/v1/responses`; reusing Chat stream handlers; assuming `previous_response_id` removes the input-token cost of earlier context.

## Existing APIs
Chat stays the most widely used, continues to get new models/capabilities; if you don't need built-in tools it's safe to keep using it; new models keep landing on Chat when they don't rely on built-in tools/multi-call; prefer Responses for advanced agentic workflows.
**Assistants**: OpenAI deprecated Assistants API (2025-08-26) with shutdown 2026-08-26 → on AvalAI Assistants aren't implemented anyway; write new agentic examples Responses-first; map assistants/threads/runs → Responses state + tools + `previous_response_id` + app-managed storage; verify which hosted OpenAI tools the AvalAI route supports.
Related: function-calling, realtime-audio, structured-outputs, tools, reasoning (captured).
