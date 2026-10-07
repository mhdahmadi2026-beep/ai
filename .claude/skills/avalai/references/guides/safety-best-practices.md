# Safety best practices (docs.avalai.ir/fa/guides/safety-best-practices)

Production AI needs layered safety: input control, moderation, per-user abuse tracking, output checks, and a user reporting path. OpenAI-compatible request shape via `https://api.avalai.ir/v1`.

## Guardrails (AvalAI feature)
- Enable **AvalAI Guardrails** so API keys, tokens and credentials are detected and stripped **before** content reaches the model.
- Scans compatible fields (`messages`, `input`, `prompt`) on routes such as `/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/completions`.
- Request shape: `{"messages":[…], "guardrails":["hide-secrets"]}`.
- Still don't send credentials/private keys/sensitive customer data unless truly needed — guardrails reduce risk, not eliminate it.

## Prompt injection & tool-abuse defence
Treat user input, retrieved docs, web text, tool output and uploaded files as untrusted unless your app validated them.
- Never put untrusted text in `instructions`/system-developer; send in `input`/message content.
- Separate data from instruction: label retrieval snippets as reference material; tell the model not to execute instructions inside.
- Structured boundary between workflow stages (Structured Outputs) so an attacker can't hide free-form commands in intermediate text.
- Validate tool calls twice: args before execution, tool output before returning to the model; human approval for write/refund/delete/shell/DB changes.
- Least-privilege tools: if hosted tool/MCP isn't enabled for the route, keep the capability in your backend and give the model one narrow `function` tool with validated params.
- Eval adversarial paths (prompt injection, jailbreak, malicious docs, unsafe tool calls) before changing prompt/model/retrieval/tool schema.

## Input & output moderation
- `/v1/moderations`: classify user input before generation and model output before display. `omni-moderation-latest` handles text + images; text aliases `text-moderation-latest`, `text-moderation-stable`.
- Scores are signals: check `flagged`, then `categories`, `category_scores`, `category_applied_input_types` for routing, audit logs and human review queues.
- Inline moderation where supported: top-level `moderation:{"model":"omni-moderation-latest"}` on `/v1/responses` / `/v1/chat/completions` may return input+output scores alongside the response; if the route doesn't support it call `/v1/moderations` separately.
- Streaming: inline moderation scores for generated content arrive only after the whole output completes (not with partial deltas).
- Coverage: moderation covers tool-call arguments and tool output when they appear in conversation content; it does NOT moderate tool names, tool descriptions, tool schemas or response-format schemas.
- Re-evaluate custom `category_scores` thresholds periodically (models improve).
| workflow | when | AvalAI pattern |
|---|---|---|
| standalone moderation | classify text/images without generating | `POST /v1/moderations` before or after generation |
| with generation | need output + scores together | add `moderation` object if enabled |
| human review | risky, borderline or business-critical | queue with `flagged`, category scores, hashed user id, conversation text |
(See guides/moderation.md; for Gemini built-in filters see guides/gemini-safety-settings.md.)

## Age-sensitive products (possible under-18 users)
Add dedicated safeguards; don't rely on model behaviour. Verify route/provider/retention/local law separately.
Define audience (adults-only / mixed / minors) + age-gating/assurance; age-appropriate disclosure (it's AI, what it can't do, how to report unsafe/harassing content); stricter content control (moderation, allow/deny topic lists, shorter generation limits, human escalation for high-risk categories); protect young users' data (no unnecessary personal data, no raw child/teen identifiers, approved retention/compliance path for regulated minors' data); check child-privacy laws early (some locales/customer policies ban processing personal data below an age — enforce outside the prompt); define who reviews risky chats, response time, when to restrict/suspend access. Combine with guides/data-controls.md for strict retention.

## `safety_identifier`
Send a stable, privacy-preserving per-end-user id (hash username/email/internal id; anonymous previews → session id). **Not carried automatically between APIs or sessions** → send the same stable value on every related request.
```python
def safety_identifier(raw): return hashlib.sha256(raw.encode()).hexdigest()[:64]
client.chat.completions.create(model=…, messages=[…], max_completion_tokens=50, safety_identifier=safety_identifier("user_123"))
```
Responses: same field + `max_output_tokens`; `user` → `safety_identifier` for abuse monitoring; use `prompt_cache_key` separately for cache bucketing. cURL: `"safety_identifier":"<hex>"`. (Doc cURL uses a 32-char value while samples slice to 64 — both fine; any stable opaque string ≤64.)

## Protecting keys & sessions
Rotate a leaked key immediately (revoke, create new before resuming traffic); hashed/opaque safety ids only (never email, phone, national id or raw DB primary key); log `request_id`, `safety_identifier`, moderation result, model, route and final user-facing action for abuse investigation without raw PII; Realtime-compatible routes: bind the same stable hashed id via the route's supported parameter/header/server metadata (no automatic carry-over).

## Red teaming & evaluation
Test representative and adversarial inputs (normal use, prompt injection, off-topic, malformed payloads, policy-boundary pushing); pair evals (expected behaviour) with red teaming (abuse, jailbreaks, unexpected risky interactions); Promptfoo (open-source) is mentioned for LLM red teaming — only test systems you own/are authorized to test; playbook: guides/red-teaming.md.

## Human & product controls
Human-in-the-loop for high-risk outputs (medical, legal, financial, security, code generation); constrain input/output (dropdowns, validated ids, retrieval from trusted content, bounded `max_output_tokens`) over fully open generation; know your customer (mandatory login; stronger verification for abuse-prone use cases); provide a monitored reporting path for unsafe/incorrect/abusive output; state limitations clearly (where errors occur, where human review is required, how moderation decisions can be appealed).
Related: moderation API, safety-checks (not captured), red-teaming (captured), production-best-practices (captured), data-controls (captured), prompt-engineering (captured), safety/content-policy (not captured).
