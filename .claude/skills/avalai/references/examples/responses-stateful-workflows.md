# Stateful workflows with the Responses API (docs.avalai.ir/fa/examples/responses_stateful_workflows — slug from api-reference/responses.md)

Practical patterns: continue a conversation, branch from an earlier response, retrieve stored responses, add web search. Adapted from OpenAI Cookbook "responses_example.ipynb". Setup: `pip install openai` / `npm install openai`, `AVALAI_API_KEY`, `base_url="https://api.avalai.ir/v1"`. Concepts: guides/conversation-state.md, responses-vs-chat-completions.md, data-controls.md.

## Basic stateful chat
```python
first = client.responses.create(model="gpt-5.6-luna", input="Give me a concise deployment checklist for a small API service.")
follow_up = client.responses.create(model="gpt-5.6-luna", input="Now turn that checklist into five acceptance criteria.",
                                    previous_response_id=first.id)
```
(JS/cURL same; cURL: capture `.id` with `jq -r .id` and pass `"previous_response_id"`. Doc cURL mixes `gpt-5.6-luna` for the first call and `gpt-5.5` for continuation — keep ONE model per chain unless you intend to switch.)
`previous_response_id` needs the prior response to be **stored** (`store` true) — don't combine with `store:false` for the earlier turn. Instructions are not inherited (resend `instructions`).

## State, retention & cost decisions
- `previous_response_id` = easiest, relies on service-side state. Manual history when you need exact retention control, deterministic replay, or a fallback for routes that don't resolve the prior response.
- CI/eval/sensitive debugging: `store=false` unless you need later retrieval.
- If continuation fails because the prior response can't be resolved → resend with FULL context and without `previous_response_id`.
- Budget the whole chain: earlier thread input still counts as input tokens; reasoning models spend reasoning tokens inside the context window.
Manual stateless replay:
```python
history=[{"role":"user","content":"Draft a rollback checklist for a payment API."}]
first=client.responses.create(model=M, input=history, store=False)
history.extend(first.output)            # keep structured output items, not just output_text
history.append({"role":"user","content":"Now make it safe for a junior on-call engineer."})
second=client.responses.create(model=M, input=history, store=False)
```
(JS: `history.push(...first.output)`.)

## Branching
Fork a new path from an earlier response without touching the original: `client.responses.create(model, input="Use the same original checklist, but rewrite it for a solo developer who deploys manually once per week.", previous_response_id=first.id)` — good for prompt A/B, different tones, retry with a new constraint.

## Retrieve a stored response
`client.responses.retrieve(first.id)` / `GET /v1/responses/{id}` for logging, debugging, delayed processing after a background workflow. Create with `store=true` if you need later retrieval; otherwise prefer `store=false` and keep only the fields your app needs. (Hosted background mode isn't available on AvalAI — background-processing.md.)

## Web search
`tools=[{"type":"web_search"}]`; iterate `response.output` item types (`web_search_call`, `message`); explicitly ask for citations in the prompt if the UI needs source links (see tools-web-search.md for annotations/`include` sources).

## Production notes
Store response ids only when you truly need continuation/audit; keep history in your own system when retention/deletion/compliance control matters; on manual replay append the structured `response.output` items so tool calls and reasoning items survive; keep fixed instructions stable and per-user details in the last input (cache-friendly); with tools inspect `response.output` (`output_text` = final plain text only; tool calls/annotations live in typed items); log `response.id`, model, latency, `usage`.
