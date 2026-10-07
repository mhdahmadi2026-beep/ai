# Responses API — `/v1/responses` (docs: /fa/api-reference/responses)

OpenAI's most advanced interface; **preferred for new apps** on AvalAI (reasoning, tools, multimodal, structured output, multi-turn). `/v1/chat/completions` stays for legacy integrations, framework compat, and models that are chat-only on AvalAI. Related guides: quickstart, text-generation, vision, structured-outputs, function-calling, conversation-state, background-processing, data-controls, streaming-responses, tools, tools-connectors-mcp; examples: responses_stateful_workflows, reasoning_function_calls, agentic_guardrails_schema_workflow.

## Migrating from Chat Completions
- `messages` → `input` (or put fixed system guidance in top-level `instructions`).
- Read `response.output_text`; inspect `response.output` for tools/reasoning/multimodal.
- Stateful chains: `previous_response_id` + `store: true`; stateless: replay prior `output` items manually.
- No `n` → issue separate requests for multiple candidates.
- `response_format` → `text.format`.
- Streaming = typed SSE events (not `choices[].delta`).

## Create — `POST https://api.avalai.ir/v1/responses`
| param | type | default | notes |
|---|---|---|---|
| `input` (req) | string \| array | | text/image/file items; files via `input_file` with `file_url`, `file_id` or base64 `file_data` (+`filename`) |
| `model` (req) | string | | e.g. `gpt-5.5`, `gpt-5.4-pro`, `gpt-5.4` (examples use `gpt-5.6-luna`). Non-OpenAI models have **limited** Responses support (text in/out + basic tools; advanced built-in tools and `reasoning` field remain OpenAI-only). **Partial** Responses support listed: `qwen3.7-max`, `claude-sonnet-5`, `claude-opus-4-8`, `minimax-m3` (⚠ differs from chat.md list — live `/v1/models` decides) |
| `background` | bool | false | background job if route/account supports; see background-processing (poll / webhook) |
| `context_management` | object | | route-dependent, e.g. server-side compaction (`compact_threshold`); else compact in your app |
| `conversation` | string \| object | | persistent conversation; don't combine with `previous_response_id`; only if route supports |
| `include` | array | | `file_search_call.results`, `web_search_call.action.sources`, `code_interpreter_call.outputs`, `computer_call_output.output.image_url`, `message.input_image.image_url`, `message.output_text.logprobs`, `reasoning.encrypted_content` (model/route/account dependent) |
| `instructions` | string | | system/developer message; **not carried over** via `previous_response_id` — resend each request |
| `max_output_tokens` | int | | cap covers visible output **and reasoning tokens**; hidden reasoning can consume all → `status:"incomplete"`, `incomplete_details.reason:"max_output_tokens"` with no text. Leave headroom / lower effort / raise cap |
| `max_tool_calls` | int | | total across all built-in tools |
| `metadata` | map | | ≤16 pairs; key ≤64, value ≤512 |
| `parallel_tool_calls` | bool | true | set false for stateful/approval/order-dependent tools |
| `previous_response_id` | string | | multi-turn chain |
| `prompt` | object | | hosted prompt template + vars, only if enabled; else keep prompts in app |
| `reasoning` | object | | OpenAI GPT-5/o-series; `reasoning.effort` tunes quality/latency/cost |
| `store` | bool | true | store response for later retrieval (`false` for stateless) |
| `stream` | bool | false | SSE |
| `stream_options` | object | | only with `stream:true`; route-dependent (obfuscation controls) |
| `temperature` | number | 1 | 0–2; change this or `top_p` |
| `text` | object | | `text.format` (text / `json_object` / `json_schema` strict) and `text.verbosity` where supported |
| `tool_choice` | string \| object | | `auto`/`required`/`none`/specific function or web search; `allowed_tools` subset where supported |
| `tools` | array | | built-in (web search, file search — if enabled for route/account), function tools (JSON Schema), custom tools (free-text payload, grammar), remote MCP |
| `top_logprobs` | int | 0 | 0–20; with `include:["message.output_text.logprobs"]` |
| `top_p` | number | 1 | |
| `truncation` | string | disabled | `auto` drops oldest items on overflow; `disabled` → 400 on overflow |
| `safety_identifier` | string | | stable hashed id ≤64 chars, no raw PII |
| `prompt_cache_key` | string | | opaque stable bucket key (assistant/tenant/policy/schema); no PII/request ids |
| `prompt_cache_retention` | string | | legacy for pre-GPT-5.6; deprecated for GPT-5.6+ (new `prompt_cache_options.ttl` upstream; AvalAI pass-through route-dependent) → drop if unsupported |
| `moderation` | object | | inline, e.g. `{"model":"omni-moderation-latest"}` where enabled; else call `/v1/moderations` |
| `user` | string | | legacy; prefer `safety_identifier` + `prompt_cache_key` |
| `service_tier` | string | default | `default` or `flex` (−50%, select OpenAI models, up to 900 s, may time out); `priority` only if explicitly enabled for your account |

### Tool configuration notes
- Function tools: `strict:true`, `additionalProperties:false`, explicit `required`; execute only allow-listed functions in your app. Return `function_call_output` with matching `call_id`.
- `parallel_tool_calls:false` for mutating/approval/order-dependent tools; built-in tools may have own sequencing.
- Web search (route-dependent): `search_context_size`, `filters.allowed_domains`/`blocked_domains`, `external_web_access`, `return_token_budget`, `include:["web_search_call.action.sources"]`.
- File search: future hosted form uses `vector_store_ids`, `max_num_results`, `filters`, `ranking_options`, `include:["file_search_call.results"]`. Until AvalAI announces hosted vector stores → manual RAG (fa/guides/tools-file-search).
- Remote MCP/connectors: expose only trusted servers; pass OAuth `authorization` outside prompts; restrict `allowed_tools`; `require_approval` for sensitive ops; if `type:"mcp"` isn't enabled, wrap the service in your own function tool.
- Deferred tools (`tool_search`, namespaced tools, `defer_loading`, `additional_tools`) shrink initial context for big catalogs — model/route dependent.

### Text / structured output notes
- Prefer `text.format = {"type":"json_schema","strict":true,"schema":…}`; `json_object` only as fallback (then instruct the model to output JSON). Before parsing `output_text`, check `response.output` parts, `status`, `incomplete_details` (refusals/truncation break schemas). Keep schemas stable/versioned; test the exact route before using sensitive or one-off per-user schemas.

### State / compaction / cost notes
- Pick ONE state strategy: `previous_response_id` (simple stored chain) · `conversation` (only if persistent conversations enabled) · manual replay (trimming/stateless).
- `store:false` on supported OpenAI routes: add `include:["reasoning.encrypted_content"]` and append returned reasoning/output items to next `input` to keep reasoning context.
- Long chats: `context_management`+`compact_threshold` (server-side) or standalone `POST /v1/responses/compact` (feed returned compacted window as-is); if unavailable, summarize in app.
- `previous_response_id` isn't a free context window: earlier chain tokens are still billed as input. Budget with `usage` and `POST /v1/responses/input_tokens` where enabled.
- Related endpoints: `POST /v1/responses/{id}/cancel` (background), `GET /v1/responses/{id}/input_items`, `POST /v1/responses/input_tokens`, `POST /v1/responses/compact` (each only if enabled on your route).

### Example
```python
response = client.responses.create(model="gpt-5.6-luna", input="یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.")
print(response.output_text)
```
```javascript
const response = await client.responses.create({ model: "gpt-5.6-luna", input: "…" }); console.log(response.output_text);
```
```bash
curl https://api.avalai.ir/v1/responses -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" -d '{"model":"gpt-5.6-luna","input":"…"}'
```
Go: raw `net/http` POST, decode `output[].content[].text` where `type=="output_text"`. PHP: cURL, `$r['output'][0]['content'][0]['text']` (fragile with reasoning/tool items — iterate `output` by `type`).
Sample response: `{id:"resp_…", object:"response", created_at, status:"completed", error:null, incomplete_details:null, instructions:null, max_output_tokens:null, model, output:[{type:"message", id:"msg_…", status:"completed", role:"assistant", content:[{type:"output_text", text, annotations:[]}]}], parallel_tool_calls:true, previous_response_id:null, reasoning:{effort:null, summary:null}, store:true, temperature:1.0, text:{format:{type:"text"}}, tool_choice:"auto", tools:[], top_p:1.0, truncation:"disabled", usage:{input_tokens, input_tokens_details:{cached_tokens}, output_tokens, output_tokens_details:{reasoning_tokens}, total_tokens}, user:null, metadata:{}}`.

## Retrieve — `GET /v1/responses/{response_id}`
Query: `include[]`, `stream` (bool; only if route supports streaming retrieve), `starting_after` (resume after event `sequence_number`), `include_obfuscation` (leave default unless you control the network path and need bandwidth savings). Returns the Response object.
## Delete — `DELETE /v1/responses/{response_id}` → `{"id","object":"response","deleted":true}` (SDKs: `responses.delete` / JS older `responses.del`; Go source sample uses non-existent `openai.DefaultConfig` → use raw HTTP).
## Input items — `GET /v1/responses/{response_id}/input_items`
Query: `after`, `before` (cursor ids), `include[]`, `limit` 1–100 (default 20), `order` `asc|desc` (default asc). Returns `{object:"list", data:[{id:"msg_…", type:"message", role, content:[{type:"input_text", text}]}], first_id, last_id, has_more}`.

## Response object (fields)
`id`, `object:"response"`, `created_at`, `completed_at` (if route returns), `status` ∈ completed|failed|in_progress|incomplete, `background`, `error{code,message}`, `incomplete_details{reason}`, `conversation`, `context_management`, `instructions`, `max_output_tokens`, `max_tool_calls`, `metadata`, `model`, `output[]` (typed items: `message`, tool calls, reasoning…), `output_text` (**SDK-only** aggregate; not in raw JSON), `parallel_tool_calls`, `previous_response_id`, `prompt`, `reasoning`, `store`, `temperature`, `text`, `tool_choice`, `tools`, `top_logprobs`, `top_p`, `truncation`, `usage` (`input_tokens`, `input_tokens_details{cached_tokens, cache_write_tokens on GPT-5.6-compatible routes}`, `output_tokens`, `output_tokens_details{reasoning_tokens}`, `total_tokens`), `safety_identifier`, `prompt_cache_key`, `prompt_cache_retention`, `moderation`, `user`, `service_tier` (`default`|`flex`).

## Streaming (`stream:true`, SSE)
Typed events, **not** `choices[].delta`. Always branch on `event.type`:
| event | use |
|---|---|
| `response.created` / `response.in_progress` | init UI, store response id |
| `response.output_item.added/done` | track typed items (message, tool call, reasoning) |
| `response.content_part.added/done` | content parts of a message |
| `response.output_text.delta` | append `event.delta` to display text |
| `response.output_text.done` | reconcile with final text of the part |
| `response.output_text.annotation.added` | citations/file refs/search annotations |
| `response.refusal.delta/done` | keep refusal text separate; final refusal = terminal assistant reply |
| `response.function_call_arguments.delta/done` | buffer args; **execute only after `done`** |
| `response.file_search_call.in_progress/searching/completed` | retrieval progress (if hosted file search enabled) |
| `response.code_interpreter_call.in_progress`, `…_code.delta`, `.completed` | interpreter status/code (publish outputs after completion) |
| `response.completed` | finalize; read usage/status |
| `response.failed` / `error` | stop, show/retry |
For long/background responses store the last `sequence_number`; reconnect with `GET /v1/responses/{id}?stream=true&starting_after=<seq>` (if supported; keep `include_obfuscation` on unless internal trusted stream). Patterns: fa/guides/streaming-responses.
```python
stream = client.responses.create(model="gpt-5.6-luna", input="…", stream=True)
for event in stream:
    if event.type == "response.output_text.delta": print(event.delta, end="", flush=True)
    elif event.type == "response.completed": print()
    elif event.type == "error": raise RuntimeError(event.error)
```
JS: `for await (const event of stream)` same branches. curl: `-H "Accept: text/event-stream" --no-buffer`, parse `event:`/`data:` lines. Go/PHP examples parse `data: ` lines, stop at `[DONE]` (may not appear for Responses; rely on `response.completed`). Legacy `choices[0].delta.content` patterns do NOT apply.

## Pitfalls to remember
- `max_output_tokens` includes reasoning → incomplete/empty text (see chat.md `max_completion_tokens`).
- Many non-OpenAI models are PARTIAL on Responses; hosted tools (image_generation, file_search, web_search, MCP, code interpreter) depend on model+route+account — verify, else use function tools/own RAG/sandbox. Image models never go in `model` here; Gemini 3.8 TTS never here.
- Voice/audio input isn't accepted directly (transcribe first).
- Source-doc issues: example model ids vary (`gpt-5.5`, `gpt-5.6-luna`, `gpt-5.4-pro`) → verify live; Go delete sample uses non-existent `DefaultConfig`.
