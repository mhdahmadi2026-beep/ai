# Building agents (guide)
App-owned orchestration over `/v1/responses` (or `/v1/chat/completions`). No hosted agent runtime on AvalAI: don't emit Agents SDK-hosted/AgentKit/Agent Builder/ChatKit-runtime code for AvalAI.

## Layers
model (reasoning/planning) · instructions (`instructions` / developer msg) · tools (function calling, web search, own tools) · state (`previous_response_id` where supported, else replay messages/typed output items) · knowledge (retrieval, embeddings, manual RAG) · guardrails (validate args, approvals, moderation) · observability (log prompts, model, tool calls/outputs, citations, latency, errors, feedback).
Doc's example models (verify live/deprecations): gpt-5.5, gpt-5.4-pro, claude-opus-4-8, gemini-3.5-flash; samples use `gpt-5.6-luna`.

## Patterns
single-shot assistant; tool-loop agent (`function_call` items → run approved fn → `function_call_output` with `call_id` until final message); RAG agent (retrieve first, answer only from cited sources); multi-agent in YOUR code (planner/retriever/executor/reviewer/final); voice/multimodal agents (same loop + audio/image APIs).

## Hosted builders
OpenAI Agent Builder shuts down 2026-11-30; ChatKit is a separate UI product. Use only as design patterns: nodes → app code/strict functions/retrieval/state object; human-approval nodes → own policy engine/UI; trace graders → agent-evals + stored traces; ChatKit widgets → own frontend. Don't claim AvalAI hosts them.

## Safety controls
| risk | control |
|---|---|
| untrusted text overrides policy | keep fetched pages/emails/tickets/user files in `input`, NOT developer/system; extract validated fields before privileged steps |
| tool over-sharing | compact tool outputs; redact secrets/tokens/raw records |
| unsafe writes | approval before payment/account change/email/delete/external post/export; separate read vs write tools |
| free-form handoff drift | structured outputs for planner decision/target/risk label/final schema |
| hidden regression | agent evals on traces, tool calls, handoffs, refusals |
Model choice is one layer only; approval, schema checks, tenant authz and audit log live in the app.

## Minimal tool loop (Responses)
```python
tools=[{"type":"function","name":"get_order_status","description":"...","parameters":{"type":"object","properties":{"order_id":{"type":"string"}},"required":["order_id"],"additionalProperties":False},"strict":True}]
r = client.responses.create(model=M, instructions="...", input="...", tools=tools)
while True:
    outs=[{"type":"function_call_output","call_id":i.call_id,"output":run(i)} for i in r.output if i.type=="function_call"]
    if not outs: print(r.output_text); break
    r = client.responses.create(model=M, previous_response_id=r.id, input=outs)
```
NOTE: `instructions` are not inherited via `previous_response_id` — resend if needed (the doc sample omits them on follow-ups). Chat Completions equivalent: `role:"tool"` messages with matching `tool_call_id`. Add a max-iteration cap (sample has an unbounded `while True`).

## Handoffs
Define input contract/allowed tools/output schema per specialist; planner picks next specialist from an allowlist; pass compact state (goal, constraints, done steps, source IDs, pending approvals); record who owns the final user-visible answer; evals for loops/early handoff/unsafe tool picks; permissions enforced in the tool executor, not in the prompt.

## Trace & eval plan
Dataset of traces: happy paths, tool errors, prompt-injection attempts, permission failures, handoff edge cases. Score tool selection, grounding (source ids), safety (refuse/escalate), handoff quality (stop loops), cost/latency (retries, fan-out, reasoning effort). Store own trace: `response.id`, model, prompt version, tool calls/outputs, approvals, final status, latency, tokens, feedback.

## Production checklist
Instructions (goal, banned behaviours, citation, escalation); strict schemas + server-side arg validation + compact structured results; approvals for risky writes; state strategy; enforce tenant/doc permissions BEFORE similarity search; stream progress but run tools only after arguments complete (`response.function_call_arguments.done`); evals.
Related guides (not yet captured): function-calling, tools, conversation-state, retrieval, agent-evals, structured-outputs.
