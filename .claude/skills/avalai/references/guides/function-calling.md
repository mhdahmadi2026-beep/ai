# Function calling (guide)
Model emits JSON arguments for YOUR functions. Flow: 1 define tools → 2 model returns tool call(s) → 3 your code runs them → 4 send results back → 5 final answer.

## Route choice
| use | route |
|---|---|
| existing chat integration | `/v1/chat/completions` (messages, `tool_calls`, `role:"tool"`) |
| new agentic workflow | `/v1/responses` (typed `response.output`, `function_call_output`, reasoning items) |
| big catalogs | Responses + namespaces/`tool_search` (route-dependent) else small direct `tools` |
| state-changing/paid ops | either; `strict:true`, server-side validate, `parallel_tool_calls:false` |
Responses + reasoning models: when continuing manually, replay reasoning + function_call items (dropping them loses tool context).

## Wire shapes
- Chat tool: `{"type":"function","function":{"name","description","parameters":{...},"strict":true}}`; response `choices[0].message.tool_calls[]` = `{id,type:"function",function:{name,arguments:"<JSON string>"}}`; result message `{"role":"tool","tool_call_id":<id>,"name":<fn>,"content":"<string>"}` after the assistant message that contains tool_calls.
- Responses tool (internally tagged, flat): `{"type":"function","name","description","parameters","strict":true}`; call = item in `response.output` with `type:"function_call"` (`name`, `arguments` JSON string, `call_id`, optional `namespace`); result = input item `{"type":"function_call_output","call_id":<same>,"output":"<string>"}`; send prior `response.output` items back too (`input_items += response.output`).
- `arguments` is a JSON STRING → parse.

## Schema checklist
Clear name + description (format of each param, what output means, when NOT to call, what to do when info missing); `strict:true`, `additionalProperties:false`, all props `required`, optional → `["string","null"]` (+ `null` in enum); inject known values (ids, permissions, prices, UI-selected state) in handler, don't make the model guess; ALWAYS re-validate/authorize arguments server-side; enums for fixed choices; merge always-sequential functions; "intern test"; make misuse hard (`refund_order({reason})` vs two booleans). Generated schemas (Pydantic/Zod/Playground) need manual review; keep type, schema, validator in sync.

## Scale
Tool defs cost input tokens and hurt selection accuracy; aim < ~20 active tools/turn; group by domain; `allowed_tools` restricts callable tools without changing `tools` list (cache-friendly): `{"type":"allowed_tools","mode":"auto","tools":[{"type":"function","name":"get_weather"}]}`. Namespaces:
```python
{"type":"namespace","name":"crm","description":"...","tools":[{"type":"function","name":"get_customer_profile",...,"strict":True},{"type":"function","name":"list_open_orders","defer_loading":True,...}]}  # + {"type":"tool_search"}
```
Loaded deferred tools are appended near context end (cache preserved) → keep namespace descriptions stable, don't mutate loaded set mid-conversation. Client-executed tool_search: keep `tool_search_call.call_id` in `tool_search_output`; hosted: `execution:"server"`, `call_id:null`. `additional_tools` only to make tools appear at a fixed point in replayed state. No `tool_search` → small direct list.
Custom tools (free-text payload, optional grammar `lark`|`regex` — Rust-regex syntax, no lookaround/lazy) are route-dependent; prefer schema functions; treat payload as untrusted (allowlist, sandbox, policy before executing SQL/code).

## Handler checklist
allowlist function names (never eval); parse+validate args; handle 0..N calls; short results; keep ids (`tool_call_id` / `call_id`); gate side effects with approval (refund, purchase, account change, notifications, irreversible). Tool output design: bounded, explicit envelope `{"ok":true,"data":..}` / `{"ok":false,"error_code":"not_found"}`; no raw DB rows/secrets/stack traces/hidden instructions; large artifacts → store + reference (file_id/url), then use file-inputs/vision/retrieval; Responses output may be string (arrays of file/image objects route-dependent); log tool name, id, validation, status, latency, redacted size.

## tool_choice
`"auto"` (default), `"required"`, `"none"`, force one: Responses `{"type":"function","name":"x"}` / Chat `{"type":"function","function":{"name":"x"}}`, `allowed_tools`. (Claude 5.x forbids forced tool use.)

## parallel_tool_calls
Default true (client defaults vary); set false for sequenced/stateful/paid flows (0 or 1 call per turn). Applies to custom functions; provider built-in tools have own sequencing (OpenAI built-ins don't parallel-call); fine-tuned models → don't rely on strict/parallel. Test per route.

## strict mode
Requires `additionalProperties:false` + all props in `required`; Chat default non-strict, Responses may normalize compatible schemas to strict and fall back to best-effort silently if not strictifiable → verify; first call slower; schemas cached (not zero-retention eligible); schema subset (see structured-outputs).

## Streaming
Chat: accumulate `delta.tool_calls[index].function.arguments`. Responses SSE: `response.output_item.added` (start), `response.function_call_arguments.delta` (accumulate by `item_id`), `response.function_call_arguments.done` (complete → only then run tool).

## Function calling vs structured outputs
Functions = trigger your code; structured outputs = shape the final user-facing answer.

## Models
gpt-5.4, gpt-5.5 + snapshots; Anthropic/Google/Cohere etc. per model-details. Older models: limited `tools`, no strict/parallel.

## Source defects
- Python processing sample uses `locals()` checks; bash sample for step 4 has undefined vars.
- Go samples use go-openai types while import path is openai-go; PHP `$responseMessage->toolCalls`.
- Chat tool message sample includes `name` (optional/not required by OpenAI).
- Responses bash example hard-codes call_id `call_abc123` (illustrative).
- "[Chat] example weather tool uses nullable `unit` enum"; Responses version drops it.
