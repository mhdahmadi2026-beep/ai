# Streaming responses (guide)
`stream=true` over HTTP SSE on `/v1/responses` and `/v1/chat/completions`. WebSocket mode = separate pattern (guides/websocket-mode, not captured; only if AvalAI offers the route). Headers: `Accept: text/event-stream`; curl `--no-buffer`.

## Chat → Responses migration
| Chat | Responses |
|---|---|
| `choices[0].delta.content` per chunk | `response.output_text.delta` (append `event.delta`) |
| tool args in delta chunks | `response.function_call_arguments.delta` … `.done` → parse/execute only after `done` |
| finish metadata in last chunks | `response.completed` carries final response (usage, status, output) |
| transport/chunk errors | `response.failed` or `error` → stop + normal retry policy |
Disable response buffering in browser/proxy stacks; flush every text delta to UI; keep an internal buffer to reconcile with `response.output_text.done` / `response.completed`.

## Event families (Responses)
`response.created` / `.in_progress` (init); `response.output_item.added/.done` (typed items: message, tool call, reasoning); `response.content_part.added/.done`; `response.output_text.delta` (append to visible buffer); `response.output_text.done` (reconcile final text); `response.output_text.annotation.added` (store citations/annotations; display after offsets stable); `response.refusal.delta/.done` (stream separately; terminal safe answer; never parse as structured output); `response.function_call_arguments.delta/.done`; file search: `response.file_search_call.in_progress/.searching/.completed`; code interpreter: `response.code_interpreter_call.in_progress`, `response.code_interpreter_call_code.delta`, `.completed` (show progress/code in side panel; outputs after completion; don't append to assistant text); `response.completed` (final usage/status; if status `incomplete` check `incomplete_details.reason` e.g. `max_output_tokens`, `content_filter` before using partial output); `response.failed` (has response object) / `error` (stream-level, may lack response) → stop, log separately.
Consumer rules: branch on `event.type`; don't assume every event has text; only text deltas go into visible buffer; hosted-tool payloads kept in separate UI areas; keep `response.id` for next turn only if route supports `previous_response_id`, else own state.

## Minimal consumer
```python
for event in client.responses.create(model=M, input=[...], stream=True):
    t = event.type
    if t in ("response.output_text.delta","response.refusal.delta"): print(event.delta, end="", flush=True)
    elif t == "response.completed": ...
    elif t == "response.failed": raise RuntimeError(event.response.error)
    elif t == "error": raise RuntimeError(event)
```

## Reconnect / resume
Foreground streams are best-effort: keep enough app state to rerun or (if route supports) retrieve the completed response. Background streaming (OpenAI) = `background:true` + `stream:true`, save last `sequence_number`, resume `GET /v1/responses/{id}?stream=true&starting_after=<seq>` — ONLY if route supports (hosted background is NOT implemented on AvalAI per background-processing guide); TTFT differs. Otherwise keep text buffer + request state, dedupe repeated deltas, or fetch final result. Stream obfuscation is on by default; `include_obfuscation=false` only for trusted internal networks.

## Advanced
Tool-call streaming (`response.output_item.added` + argument events); structured outputs streaming with `text.format` (partials are incomplete JSON); hosted-tool progress as operational status only (RAG/code exec fallbacks in app if tools unavailable).

## Moderation risk
Streaming raw output to end users makes moderation harder; inline moderation scores arrive only AFTER output completes (not with deltas). For high-risk surfaces: buffer, post-stream review, or hybrid with lightweight local checks.

## Defects
- Go sample just copies raw SSE bytes to stdout (no event parsing); PHP `createStreamed` for responses depends on openai-php version.
- Chat Completions streaming (delta format, `stream_options.include_usage`) is not demonstrated here — see api-reference/chat.md.
- Python concept sample's `break` inside loop leaves stream unclosed (use context manager/`stream.close()`).
