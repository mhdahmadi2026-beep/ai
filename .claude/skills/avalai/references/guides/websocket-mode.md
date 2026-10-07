# Responses WebSocket mode (guide) — **NOT implemented on AvalAI**
Banner: feature in development, not available; AvalAI will announce. OpenAI documents a persistent WebSocket transport for `/v1/responses`; on AvalAI route/model/account dependent → **do NOT emit `wss://api.avalai.ir/v1/responses` code** unless staging proves it (override URL via `AVALAI_RESPONSES_WS_URL`). Fallback = HTTP `POST /v1/responses` (+ `previous_response_id` if hosted state OK, or manual item replay with `store:false`, + `stream:true` SSE for UI).

## When (if ever enabled)
Long tool-heavy loops (agentic coding, orchestration workers keeping a task across many turns, low-latency tool chains, stateful flows already using `previous_response_id`). NOT for one-shot prompts, browser clients (no API key in browser), or parallel responses on one socket (each connection owns ONE in-flight response; sequential; use pool for parallel).

## Transport model
Persistent WebSocket; send JSON `{"type":"response.create", model, store, input, tools, previous_response_id?, ...}` (same payload as POST /v1/responses minus transport fields `stream`/`background`); continuation = another `response.create` with `previous_response_id` + ONLY new input items; active connection may cache latest previous response in memory; max connection life ≈ 60 min → reconnect plan. Events streamed back: `response.output_text.delta`, `response.completed` (`event.response.id`), `response.failed`, `error`.
Client libs: `pip install websocket-client`, `npm install ws`; header `Authorization: Bearer $AVALAI_API_KEY`. Resend `instructions` every turn (not inherited). Continuation input example: `function_call_output` item (call_id, output) + user `message`.

## State / recovery matrix
- `store:true` + persisted previous response → reconnect, continue with `previous_response_id` + new items.
- `store:false`, ZDR-like flow, or id not in connection cache → start fresh chain with `previous_response_id:null` + full (or compacted) context.
- `previous_response_not_found` → retry as new response with full context (server doesn't always rehydrate).
- `websocket_connection_limit_reached` → open new socket, resume from last stable state.
- failed continuation (4xx/5xx) → rebuild from your own log before retrying.
Chained requests still bill prior context as input.

## Compaction
Server-side (`context_management` + `compact_threshold`, if route supports): just continue with latest id + new items. Standalone `/v1/responses/compact` via HTTP then start a new WS response with compacted window as `input` and `previous_response_id` omitted/null. Portable: summarize in app. Never edit opaque compaction items.

## Migration path
1 build with plain POST; 2 add `previous_response_id`/replay; 3 add `stream:true`; 4 move only qualifying long tool workers to WS after staging; 5 keep HTTP for recovery, unsupported routes, compliance-sensitive flows.

## Checklist
Confirm exact WS URL/model/entitlement in staging; keys server-side only; store task id, response id, request id, tenant, usage; ONE running response per socket; reconnect before 60 min; handle `previous_response_not_found`, close, timeout, 429, provider 4xx/5xx.

## Defects
- Sample sends `"tools": []` + `store:false`; Python loop has no timeout/ping handling; both samples use unproven host.
