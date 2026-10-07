# Context compaction (guide)
Long agents/conversations accumulate context → compact old turns into a small state bundle. Hosted OpenAI compaction (`context_management`, `compact_threshold`, `/v1/responses/compact`) is **route-dependent on AvalAI — use only if model+account explicitly support it**. Portable path: app-managed summary via a normal `/v1/responses` call.

## What to preserve
goal + success criteria; facts/IDs/user preferences/constraints; actions done (tool calls, side effects, changed external records); evidence (citations, file names, request/object IDs); blockers (open questions, failed calls, retries, safety limits); next step. Never drop: latest tool outputs, safety decisions, permission checks the next turn must reason over.

## Strategies
| strategy | when | note |
|---|---|---|
| app-managed summary | portable across providers, full control | quality depends on your prompt + validation |
| server-side compaction | route supports `context_management` + `compact_threshold` | compaction item is opaque; append unchanged in stateless chaining |
| standalone compact endpoint | explicit control before next turn, route supports `/v1/responses/compact` | pass returned window as-is, don't prune |
| manual truncation | drop old irrelevant chat turns | keep last user request, tool outputs, IDs, policy constraints, human approvals VERBATIM |

## App-managed pattern
1. `client.responses.create(model=M, instructions="Compact the conversation into JSON with keys: goal, facts, decisions, completed_actions, blockers, next_step. Preserve IDs.", input=json.dumps(transcript, ensure_ascii=False), store=False)` → `state = output_text`
2. validate JSON; store in your app
3. next turn: `input=[{"role":"developer","content":f"Compacted prior state:\n{state}"},{"role":"user","content":"..."}]`, instructions "Use the compacted state as prior context. Do not invent missing details."

## Hosted behaviour (when supported)
- Server-side: inside `responses.create`, runs after rendered token count exceeds `compact_threshold` (set below model window, leave headroom for output+reasoning): `context_management=[{"type":"compaction","compact_threshold":200_000}]`; server may emit an encrypted compaction item in `response.output`/stream → opaque model state.
- Stateless input-array chaining: append ALL returned output items (incl. compaction item) to next input; after testing you may drop items before the latest compaction item to cut size/latency.
- `previous_response_id` chaining: send only new user input; don't prune manually.
- Standalone: `client.responses.compact(model=M, input=long_input_items)` → `next_input=[*compacted.output, {"type":"message","role":"user","content":"..."}]` → `responses.create(..., store=False)`. Window sent to compact must itself fit the model context.
- Compact output = machine state, not human summary: store only if retention policy allows, pass unchanged, keep a separate human audit summary in app.
No hosted controls on your route → app-managed + conversation-state guide.

## Best practices
Compact BEFORE hitting limits; validate compacted JSON before storing/sending; log tokens before/after (cost + latency); combine with token counting and prompt caching (guides not yet captured).

## Defects
- Python/JS samples reference `long_input_items`/`longInputItems` undefined; `client.responses.compact` SDK method availability depends on SDK version.
- App-managed example puts summary in `developer` role message inside `input` (fine) — but a malicious transcript could inject instructions into the summary; treat summarised user/tool content as untrusted data.
