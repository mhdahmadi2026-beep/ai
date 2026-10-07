# Safety checks (docs.avalai.ir/fa/guides/safety-checks)

Identify risky usage before it becomes an incident for the account, user or product. Adapts OpenAI's safety-checks guidance to `https://api.avalai.ir/v1`. Use with safety-best-practices.md, moderation (api-reference/moderation.md, guides/moderation.md), red-teaming.md.

## What to check
| layer | check | AvalAI pattern |
|---|---|---|
| user identity | can you tie a risky request to a stable user without storing raw PII? | send hashed `safety_identifier` on every supported request |
| input risk | policy violation, secret leakage, unsafe tool call | `/v1/moderations`, schema validation, tool allowlist before costly work |
| output risk | unsafe/sensitive/high-stakes answer | moderate or review output before display; buffer streams for high-risk surfaces |
| tool action | can the tool write data, spend money, call privileged systems? | validate args; human approval for side effects |
| release change | prompt/model/routing/retrieval/moderation-threshold changed? | evals + red-team smoke tests before rollout |

## `safety_identifier`
Stable, privacy-preserving per-end-user id: hash internal user id/email/account id before sending. **Don't rotate it to evade enforcement** — block/review the abusive account instead.
```python
user_hash = hashlib.sha256(b"user_123").hexdigest()[:64]
client.chat.completions.create(model="gpt-5.6-luna", messages=[…], max_completion_tokens=120, safety_identifier=user_hash)
```
Responses: `instructions`, `input`, `max_output_tokens=120`, `safety_identifier=user_hash`, read `response.output_text`. cURL: `"safety_identifier":"<hex>"`.

## Graceful handling of safety enforcement
Provider safety systems may add latency, return errors or restrict access when traffic repeatedly looks abusive — NOT an ordinary transient error.
- GPT-5+ safety classifiers (OpenAI-documented) classify requests at risk thresholds; repeated high-risk traffic can trigger warnings, errors or model-access restrictions. Exact enforcement on AvalAI depends on provider route, model and account standing.
- Streaming: show a loading state while a safety check delays the stream; don't spawn duplicate retries.
- **Don't blind-retry policy/safety blocks**: retry network errors; send policy/safety errors to a safe fallback, account review or support.
- Log `avalai-request-id`, model, route, hashed `safety_identifier`, moderation result, final action; raw prompts only if retention policy allows.
- Scope blame to the right subject: a safety identifier lets you review/limit the abusive user, not the whole integration.
- **Never mint a fresh identifier to bypass a block**; review the original account and harden product controls.

## Realtime / session-based routes
Safety identifiers aren't carried across APIs or sessions. If AvalAI enables a Realtime-compatible route for your account (hosted Realtime is NOT currently available — see guides/realtime-audio.md), bind the same stable hashed id when creating/connecting the session via that route's supported header/metadata. OpenAI shape (architecture reference only): server-side `POST /v1/realtime/client_secrets` with header `OpenAI-Safety-Identifier: <hash>` and `{"session":{"type":"realtime","model":"gpt-realtime-2"}}`. Never ship the long-lived API key to browsers; mint a short-lived client secret in your backend and bind the id there. Chat/audio request-based flows use `safety_identifier`.

## Products serving minors (under-18)
Treat as a high-sensitivity release; verify legal/privacy/retention per provider route.
Define age scope (minors / mixed / classroom / family / adults-only) + age gate/assurance where needed; don't process personal data of children under 13 (or under the digital age of consent in the jurisdiction) unless the route has the required retention controls and you've documented a legal basis; age-appropriate disclosure (AI, capabilities/limits, when to ask a trusted adult/professional); age-appropriate input+output moderation for sexual content, violence, self-harm, exploitation, illegal activity, bullying, other sensitive content; escalation path (who reviews risky interactions, how reports are handled, when parents/school admins/moderators/legal/emergency contacts step in); minimize/segregate data: no raw PII, hashed `safety_identifier`, support logs/moderation results/customer content under the documented retention plan (data-controls.md). Don't copy OpenAI ZDR claims into customer-facing AvalAI text unless the route/provider/contract supports exactly that control; if unsure keep stateless, don't store full prompts, require human review before offering the feature to minors.

## Cyber & research traffic
OpenAI documents extra automated safeguards for high-cyber-capability model families; AvalAI behaviour depends on route, model, account policy, upstream controls.
- Expect policy errors such as **`cyber_policy`** from upstream — enforcement signal, not a 5xx to retry blindly.
- Separate end users with stable `safety_identifier` so provider + your review can restrict one risky user, not everyone behind one API key.
- If an identifier/account/org gets restricted: review activity, tighten product controls, contact support — don't issue fresh identifiers to continue the same behaviour.
- Legitimate defensive-security, life-science, chemistry or dual-use workflows need authorization controls, narrower prompts/tools, human review and a documented escalation path before production traffic.

## Release checklist
Add `safety_identifier` to every supported user-facing call; run `/v1/moderations` or inline moderation where the route supports it; validate tool args before execution and tool output before returning to the model; feed safety failures into eval datasets + red-team smoke tests; define product paths for `cyber_policy`, blocked identifiers and other enforcement errors; for minors: age-appropriate disclosure, sensitive-content filters, reporting/escalation, route-level retention review; name who reviews blocked users, borderline moderation results and risky generated content; document user-appeal path, support and escalation timing.
