# Data controls in AvalAI APIs (docs.avalai.ir/fa/guides/data-controls)

Privacy-safe integration design. Adapts OpenAI's your-data / conversation-state / background / prompt-caching guides to the AvalAI gateway. AvalAI's own policy: safety/privacy-policy + content-policy (pages not yet captured). Because AvalAI routes to upstream providers, always separate **AvalAI service metadata** from **provider-side application state**.

## Data layers
| layer | may contain | action |
|---|---|---|
| request/response content | prompt, messages, tool output, files, images, audio | send only the minimum needed |
| AvalAI service metadata | model, route, token usage, cost, IP, request id | keep logs only for billing, support, rate-limit debugging, abuse review |
| provider application state | stored Responses, files, batches, vector stores, background jobs | use `store:false`, `expires_after`, delete APIs, or app-managed state where supported |
| tools / third parties | web search, MCP servers, external APIs, provider-native services | check each service's retention before sending customer data |

## OpenAI reference behaviour (checklist, NOT automatic AvalAI guarantees — verify route/provider/contract)
Distinguish **abuse-monitoring logs** (may keep prompt, response, derived safety metadata for policy enforcement) from **application state** (data a feature must persist to function). Store operational metadata (`avalai-request-id`, model, usage, cost, error class) separately from customer content; don't treat billing/support logs as a safe place for full prompts.
Reference numbers (risk review only): abuse-monitoring logs ~30 days; stored Responses ≥30 days when storage enabled; background Responses keep data briefly (~10 min) for polling; multi-turn audio output state ~1 h; ZDR and Modified Abuse Monitoring are approved account controls (under ZDR `store` is treated as `false`, but endpoints needing application state may still be ineligible); extended prompt caching up to 24 h. Everything = route/provider/customer-contract dependent.
| capability | OpenAI reference | safe AvalAI default |
|---|---|---|
| API training | not used for training unless opt-in | don't assume upstream training policy; document the route's contract |
| `/v1/responses` | stored by default or `store:true`; `store:false` disables later retrieval | `store:false` unless you need later retrieval/`previous_response_id` |
| background mode | short-term storage for polling; needs stored state | only if the route supports it; else own async job + stateless calls |
| files / batches | persist until deletion/expiry (also evals, fine-tuning artifacts) | set `expires_after` where supported; schedule cleanup jobs |
| tools / MCP | data to remote tool = that third party's policy | classify each tool call as a transfer to an external service |
| prompt caching | latency/cost optimization, NOT a deletion/privacy boundary | user-specific data after the shared prefix; no raw ids in cache keys |
Retention controls aren't generic: features needing application state (stored responses, background polling, files, batches, eval artifacts, vector stores, hosted tools, video jobs, third-party tool calls) may keep data even when a provider offers ZDR-like controls. Treat retention as a **per-route contract**: confirm model, endpoint, provider, feature flags before accepting regulated data or promising deletion timelines. Stateless design: `store:false`, app-managed history, short-lived files, explicit cleanup jobs, independent `/v1/moderations`.

## Responses-specific checks before launch
- Stored responses: retrievable later unless `store:false`; use `store:true` only for `previous_response_id`, polling, retrieval, or debugging with confirmed retention.
- Background mode (~10 min stored in OpenAI reference): `background:true` conflicts with strict stateless/zero-retention designs unless route contract says otherwise.
- Audio output: multi-turn audio may need short-lived state (OpenAI ref 1 h) — document audio retention separately from text.
- Compaction: opaque machine state; with `store:false` don't persist compaction items outside your retention policy.
- 3rd-party tools (remote MCP, hosted code/shell, live web search, provider-native connectors) = external retention obligations → document as data processors.

## Stateless default
```python
client.responses.create(model=os.getenv("AVALAI_MODEL","gpt-5.6-luna"), instructions="Answer using only the provided support policy.",
  input="Summarize the refund policy in two bullets.", store=False, safety_identifier="user_hash_8f3a2c")
```
If the route doesn't support `store`, treat the behaviour as provider-dependent and keep your own retention policy conservative. Chat Completions: resend only needed turns; keep long-term memory in your DB if policy allows; don't log full prompts by default.
**Stateless multi-turn reasoning** (no stored Response object): request encrypted reasoning items and replay `response.output`:
```python
history=[{"role":"user","content":"Draft a two-step migration plan."}]
r=client.responses.create(model=M,input=history,store=False,include=["reasoning.encrypted_content"])
history += r.output; history.append({"role":"user","content":"Now make it safer for production."})
client.responses.create(model=M,input=history,store=False,include=["reasoning.encrypted_content"])
```
(JS: `history.push(...response.output)`.) Requires route support for `reasoning.encrypted_content`.

## When stored state is useful
`previous_response_id`/conversation objects (prefer manual replay + `store:false` for sensitive/regulated data); background processing (only if route supports hosted `background:true`; else own job table); Files API (`expires_after` for temp files, DELETE when done); Batch/evals/fine-tuning/vector stores (assume persistent until provider deletion/expiry).

## Prompt caching & privacy
Optimization, not a control boundary: stable policy text + tool schemas first, per-user detail last; `prompt_cache_key` buckets a workload (not a raw user id) and is separate from `safety_identifier`; `prompt_cache_retention` only if model/route/account supports it; for strict retention check whether provider uses in-memory vs extended cache; don't set `prompt_cache_retention:"in_memory"` on OpenAI-family models that need extended caching unless the route documents it; extended caching may keep KV tensors up to 24 h — don't promise cache-retention guarantees without provider confirmation.

## File & tool hygiene
Public URLs only for public documents (private → Base64/Files API); delete files once no longer needed; image/file inputs = special retention (upstream safety scanners may retain flagged media for manual review even with strict controls); remove/redact secrets, credentials, payment data, private keys, unrelated PII before model calls; validate tool args before execution and tool output before returning to the model; human approval before account changes, messages, deletes, payments, external system calls; live web search, remote MCP, hosted code/shell, provider-native connectors = external/provider-managed processing — use offline/cache-only search only if the route explicitly supports it; don't assume retention, residency, HIPAA or BAA terms equal AvalAI policy.

## Data residency & regional routes
OpenAI residency is project-level with regional API domains for eligible endpoints/models/accounts. Via AvalAI don't assume regional domains, ZDR settings or regional processing guarantees apply automatically. For regulated deployments keep an **evidence record per route**: AvalAI endpoint, provider, model id, service tier; whether content is stored/processed only in the required region or routed globally; whether prompt caching, background jobs, Files API, tools, web search, video generation or provider-native connectors create application state outside the main model call; whether the customer account has a signed data-processing/residency/BAA-HIPAA/enterprise-retention agreement for that route; fallback behaviour if the preferred regional route is unavailable. Keep residency separate from security controls (encryption, `store:false`, moderation, caching, residency each need independent verification).

## Enterprise key management / BYOK
OpenAI documents EKM for eligible application state (keys synced from supported external KMS). Don't assume it applies via AvalAI/other upstreams. If customer-managed encryption is required: verify the exact AvalAI route/provider/endpoint/artifact type supports BYOK/EKM; define which state is covered (stored responses, Files API objects, vector stores, batches, evals, fine-tuning artifacts, hosted tool containers, provider logs); define the failure path for an endpoint incompatible with the customer key policy; keep app-side encryption for your own DBs, logs, queues, object storage regardless.

## Production checklist
Data-flow diagram per route receiving customer content; record whether each request uses `store`, `previous_response_id`, background, Files, Batch, tools, external search; record whether provider-side state is covered by customer-managed encryption or avoid it for that workflow; `safety_identifier` = stable hash/opaque id (no raw email/phone/username); log `avalai-request-id`, model, route, tokens, latency, error class without storing full customer content; verify provider retention for the exact model+endpoint before regulated/sensitive data.
Related: privacy-policy, content-policy (safety pages not captured), conversation-state (captured), background-processing (captured), prompt-caching (not captured), safety-best-practices (not captured), api-reference/files.md.
