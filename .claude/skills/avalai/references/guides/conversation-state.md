# Conversation state with Responses API (guide)
`previous_response_id` links turns server-side. Your DB remains the source of truth for identity, permissions, long-term memory, business records, audit log. Hosted state = model context only. Cross-session memory → app-owned layer (e.g. embeddings-based durable agent memory), not a response chain.

## Use when
User continues same task across turns; avoid rebuilding message arrays; reasoning/tool workflow must see prior items; branch from a response and compare paths.

## Strategies
| strategy | when | note |
|---|---|---|
| `previous_response_id` | API chains turns, keeps recent reasoning/tool context | simplest; RESEND important `instructions` every turn (not inherited); prior context still billed as input |
| manual items | stateless/custom trimming/strict audit | you choose which `response.output` items to resend; with `store=False` |
| persistent `conversation` object | only if route explicitly supports OpenAI `conversation` param / Conversations API | durable server threads; account/route dependent; NEVER send together with `previous_response_id` |
| compaction | long workflows / long tool outputs | only where route supports server-side or standalone `/v1/responses/compact`; keep returned compaction items opaque (don't edit, re-summarize, show); pass compacted window as-is to next `/v1/responses`; else summarize facts, ids, tool results, assumptions, blockers, next action yourself |
Compliance/data-minimization → manual items + `store=False`. Reasoning continuity without stored state → keep needed output items (not whole transcript).

## store / retention / cost
`previous_response_id` needs `store=True` on responses you will continue (be explicit). `store=False` → use manual replay. OpenAI reference: response objects stored by default, ~30-day retention, retrievable unless `store=False`; conversation objects/items outside that TTL. AvalAI: retention, zero-retention behaviour, Conversations API access vary by route/provider/account → record AvalAI response id, internal request id, model, user/tenant context, token usage in YOUR DB; don't treat hosted state as the only audit trail. Treat chain as budgeted input (prior items count); when it grows, summarize/compact and restart chain or replay selected items. Context window = shared budget input + output + reasoning; leave room via output cap.
WebSocket mode (route-dependent, guides/websocket-mode — not captured): `previous_response_id` = same logical continuation; always keep a full-context recovery path (server keeps only the latest response in connection-local cache; unresolved id → send new turn with full context; error `previous_response_not_found`).

## Continue
```python
first = client.responses.create(model=M, instructions=INS, input="...", store=True)
nxt   = client.responses.create(model=M, instructions=INS, previous_response_id=first.id, input="...", store=True)
```
Branching: reuse same `previous_response_id` for multiple follow-ups. Retrieve: `client.responses.retrieve("resp_...")` (needs store on). Use `store=False` for non-retained requests.

## Manual context carry
Append needed `response.output` items to next `input`, preserving types `message`, `reasoning`, `function_call`, `function_call_output` (dropping tool/reasoning items degrades next turn). Preserve assistant `phase` (`commentary` / `final_answer`) unchanged. Stateless reasoning: `include=["reasoning.encrypted_content"]` (route-dependent; drop if unsupported), replay returned items, never fabricate/reveal reasoning text.
```python
nxt = client.responses.create(model=M, input=[*first.output, {"role":"user","content":"..."}], store=False, include=["reasoning.encrypted_content"])
```

## Best practices
Store response id with user/task/permission context; explicit `instructions` each turn; one state mechanism per request (never `previous_response_id` + `conversation`); `metadata` for tenant_id/workflow_id/request_id; compact long agents (facts, open questions, done actions, next goal); log request id + token usage; stream long replies; function calling for deterministic system access.

## Defects
- bash sample mixes model ids (`gpt-5.6-luna` first call, `gpt-5.5` second) — likely typo; keep the same model.
- Linked pages not captured: compaction, websocket-mode, streaming-responses, durable_agent_memory, responses_stateful_workflows.
