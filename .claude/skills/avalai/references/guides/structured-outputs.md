# Structured outputs (guide)
Two modes: **`json_schema` (recommended)** = valid JSON that matches your schema + explicit `refusal`; **`json_object`** = valid JSON only, no schema guarantee. Responses: `text.format`; Chat: `response_format`. Route/model dependent — test your exact model+endpoint; fallback to json_object + app-side validation.

## Choose
| need | use |
|---|---|
| typed final answer (UI/storage/routing) | Responses `text.format:{"type":"json_schema",...}` |
| args for YOUR code | function calling `strict:true` |
| just valid JSON, no schema | `json_object` (+ validate) |
| input may not fit the task | schema with nullable fields / app-level error object |
Prefer `/v1/responses` for new work; keep Chat `response_format` for existing integrations.

## Shapes
Chat: `response_format={"type":"json_schema","json_schema":{"name":"calendar_event","strict":True,"schema":{...}}}`; check `message.refusal`, else `json.loads(message.content)`.
Responses: `text={"format":{"type":"json_schema","name":"calendar_event","strict":True,"schema":{...}}}` (name/strict/schema are flat siblings of `type`, not nested in `json_schema`); read `json.loads(response.output_text)`.
json_object: Responses `text={"format":{"type":"json_object"}}`; Chat `response_format={"type":"json_object"}`; prompt MUST mention "JSON" (system/developer), else error or endless whitespace.

## Parse before trusting
Check `response.status` (incomplete → `incomplete_details.reason`), refusal content parts (`item.type=="message"` → content `type=="refusal"`; Chat `finish_reason`), app invariants, then validate with runtime types (Pydantic/Zod). Log schema name/version, model, route, validation errors. Keep schema and runtime types in sync (generate from Pydantic `model_json_schema()` with `extra="forbid"`; CI check).

## Schema design / contract checklist
`strict:true`; `additionalProperties:false` on EVERY object; ALL properties in `required` (optional → `{"type":["string","null"]}`); root must be an object (no root `anyOf`); nested `anyOf` only if route supports; descriptive names (`customer_refund_requested`), short `description`s, enums for downstream-critical values; split unrelated decisions; versioned names (`support_ticket_v1`); small stable schemas (first request with a new schema is slower — schema processed/cached; don't create per-request schemas; warm at deploy); NO tenant/user ids, secrets or business secrets in names/descriptions/enums/`$defs` (schemas may be cached/retained by provider); put user data in input. Parsers read by field name, not order.
Tool functions: set `strict:true` explicitly (Responses may auto-strictify compatible schemas; Chat defaults non-strict; non-strictifiable schema → `strict:false` silently — test for it).

## `$defs`/`$ref` & recursion
Supported incl. root recursion `$ref:"#"`, same subset rules. Keep shallow; app-side limits on depth/array length/string size; enums for node type/state/action; validate whole tree before rendering/executing/writing; test recursion fixture on your route, else flatten with ids + parent refs.

## Refusals / incomplete
Refusal arrives as `refusal` (Chat message field) / refusal content part (Responses) — do not parse as JSON. Incomplete (max tokens, content filter) → retry with clearer instructions, smaller schema or bigger output cap. Tell the model what to return when input doesn't map (nulls / error object).

## Streaming
Responses `client.responses.stream(model, input, text_format=PydanticModel)`; events `response.output_text.delta` (partial text), `response.refusal.delta`, `response.failed`, `error`, final via `stream.get_final_response()`; JS may also emit `response.output_text.done`. Keep refusal deltas separate; check `final_response.status` before parsing; don't act on partial JSON; tool-argument streaming → function-calling guide.

## Supported schema subset
Types string/number/integer/boolean/object/array; `properties`, `required`, `additionalProperties:false` (mandatory), `items`, `enum`, `anyOf` (nested valid), `$defs`/`$ref`. Limits: ≤5,000 object properties total; ≤10 nesting levels; ≤120,000 chars total over property names + definition names + enum values + consts; ≤1,000 enum values total; string enum >250 values → total enum string length <15,000. Unsupported: `allOf`, `not`, `dependentRequired`, `dependentSchemas`, `if/then/else` (+ for fine-tuned routes minLength/pattern/minimum/patternProperties/minItems). Unsupported keyword → API error.

## Models
Doc says: gpt-5.5, gpt-5.4 + snapshots; other models/routes vary (tested per route); older → json_object only. Pre-prod tests: happy path, non-matching input, safety-sensitive prompt; confirm schema features (strict, nullable optionals, nested anyOf, `$defs`, enum size); record schema name/version with response id + model.

## Troubleshooting
schema rejected → missing additionalProperties:false / not all in required / unsupported keyword / root anyOf. JSON mode returns whitespace → mention JSON in instructions or use json_schema. Refusal → check refusal before parse, show safe fallback UI. Incomplete → check status/finish_reason first.

## Defects
- Chat sample passes system message + uses `gpt-5.6-luna`; json_object sample comment "updated from gpt-3.5-turbo".
- Doc says "typeless root `anyOf` not allowed" but also allows nested anyOf "only if route supports" — test.
- Streaming sample mixes Pydantic helper (`text_format=`) which depends on SDK version.
