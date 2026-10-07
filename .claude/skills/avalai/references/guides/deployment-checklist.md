# API deployment checklist (docs.avalai.ir/fa/guides/deployment-checklist)

Pre-launch go/no-go list for AvalAI apps; adapts OpenAI's deployment checklist + production best practices to AvalAI (base URL, tiers, provider routing). Companion: guides/production-best-practices.md.

## 1. Choose the API surface
- New text/reasoning/structured-output/tool workflows → `/v1/responses` where the model supports it; keep `/v1/chat/completions` for existing integrations and chat-only models.
- Document migration: `messages`→`input`, system/developer prompts→`instructions`, `max_completion_tokens`→`max_output_tokens`, `choices[0].message.content`→`response.output_text`.
- Pin in config per release: `AVALAI_MODEL`, `AVALAI_BASE_URL=https://api.avalai.ir/v1`, prompt version label.
- ⚠ Hosted Responses features (hosted tools, background jobs, compaction, encrypted reasoning, WebSocket mode) are route/model-dependent on AvalAI — keep the checklist item but roll out only after observing real behaviour of that provider/model in staging.
- **Capability matrix per model route:** `/v1/responses`, streaming, `reasoning.effort`, `text.verbosity`, `previous_response_id`, `prompt_cache_key`, tool calling, background jobs, WebSocket continuation. Every "yes" needs a staging request ID; every "no" needs a documented fallback.

## 2. Tune quality, cost, latency
| lever | use | AvalAI guidance |
|---|---|---|
| `reasoning.effort` | reasoning depth | lowest effort passing evals; high only for complex decisions |
| `text.verbosity` | answer length | keep prod answers short unless UX needs more |
| `max_output_tokens` / `max_completion_tokens` | shared output+reasoning budget | cap every request but leave headroom for visible answer; reasoning can consume the whole cap → incomplete/empty; alert on `max_output_tokens` / `length` and tune with effort |
| `prompt_cache_key` | repeated context | stable policy/product context first, dynamic user context last; avoid one over-hot key across unrelated tenants/workflows |
| assistant `phase` | long-running agents | when replaying assistant history keep `commentary` vs `final_answer` |
| `tool_search` / deferred tools | big tool catalog | small namespaces, lazy loading; short namespace description, precise usage rules inside deferred tool definitions; if hosted isn't enabled filter tools in-app before calling |
| compaction | long conversations | hosted if enabled (forward compacted output unchanged — machine state, not editable summary); else app summary preserving decisions, IDs, tool results, open tasks |
| `reasoning.encrypted_content` | continuity without stored state | round-trip returned reasoning items exactly if supported; don't parse/rewrite |
| streaming | perceived latency | stream visible answer; show status in tool flows |
| background | resumability | app-managed jobs/queue+workers unless hosted background is enabled on the route (hosted background normally needs stored response state; zero-retention posture → app queues) |
| WebSocket mode | multi-step tool flows | only after staging proves route support, reconnect, cancel, timeout, HTTP fallback; one workflow per connection, separate connection for parallel work |
Prompt caching: opaque `prompt_cache_key` per workload/tenant, never raw user id.

## 3. Credentials & user identity
`AVALAI_API_KEY` in secret manager/env, never browser/mobile; separate keys/projects for dev, staging, prod; rotate leaked keys immediately (name an owner); send hashed `safety_identifier` per end user; never send passwords, API/private keys or unneeded customer data to the model.

## 4. Lock down access & operations
(OpenAI RBAC/Admin API/workload identity/IP egress = checklist ideas; verify AvalAI account capability before launch via dashboard, reseller contract or support.)
- Least privilege: human admin access separate from runtime key; restrict prod key to needed routes/models where project/model allowlists exist.
- Project boundaries: experiment/staging/prod/reseller-customer in separate projects/accounts (files, cost, rate limit, logs).
- Service credentials: workload credential/service account for servers & CI where available; long-lived keys rotated on schedule and after incidents.
- Model governance: per-environment allowlist; experimental models stay out of regulated workloads until privacy/cost/latency/eval review passes.
- Cost & rate-limit ops: owners for budget alerts, quota changes, escalation; limit-increase requests backed by `avalai-request-id` evidence + expected traffic.
- Audit: log changes to keys, routing, model allowlist, prompt version, data-retention settings, reseller budgets with actor identity; export/archive audit events if plan allows.
- Network: IP allowlist identifies a network, not an authenticated user → keep request auth, mTLS/OAuth for tools, signed webhooks.
### CI/CD & workload identity (principle, not OpenAI-specific API calls)
AvalAI may not expose a token-exchange / service-account-mapping endpoint → apply the design: keyless where possible (GitHub Actions/Kubernetes/AWS/Azure/GCP/SPIFFE authenticate via OIDC to YOUR secret manager, fetch `AVALAI_API_KEY` at job runtime); match claims tightly (issuer, audience, repo, branch/ref, environment, workflow, namespace, service account); never give prod credentials to untrusted fork PRs; separate identities for CI, staging, prod runtime, reseller billing jobs, data backfill (build pipeline ≠ live user-facing key); short-lived tokens exchanged only at job start, masked in logs; revoke/rotate the underlying AvalAI key after incidents; audit mappings (repo transfers, branch protection, environment approvals, JWKS/key rotation, disabled workflows). If AvalAI adds native workload identity: exact claim matching, least privilege, separate environments, short-lived tokens, alerts on failed/unexpected exchanges.

## 5. Safety gates
Moderate risky input/output with `/v1/moderations`; validate structured outputs against schema before downstream use; validate tool args before execution and tool output before returning to the model; human approval for refunds, deletes, writes, shell commands, financial actions, medical/legal/security decisions and other side effects; red-team (guides/red-teaming.md) for prompt injection, tool abuse, data leakage, policy-boundary pressure.

## 6. Evals & rollout
Golden dataset in repo (representative prompts, edge cases, expected behaviour, pass/fail rubrics); smoke eval on every PR that changes prompt/model id/retrieval/tools/moderation/routing; full suite before launch (promptfoo example/own CI); canary small traffic; compare production metrics vs evals; rollback config ready; add every production failure to the eval set before fixing the prompt; validate long-context workflows at multiple context sizes (lost-in-the-middle regressions).

## 7. Scale & rate limits
Read rate-limits pages (tier/model); exponential backoff + jitter on 429 and transient 5xx; track `x-ratelimit-*`, `avalai-request-id`, latency, token usage, final status; batch embeddings/batch-safe work only if it cuts request count without raising output tokens; queues for bursty load; app-managed workers for long flows.

## 8. Observability (log enough to reproduce without leaking secrets)
route, model, provider, service tier, prompt version, deployment version; `avalai-request-id`, response ID, latency, retries, streaming mode, final status; input/output/cached tokens + estimated cost; tool-call names, validated args, result status, approval decisions; moderation result, `safety_identifier` hash, red-team/eval failure reason.

## 9. Go / No-Go (ship only if every answer is yes)
API surface + model config as intended? API keys/user ids/logs privacy-safe? Access controls, model allowlists, cost owners, audit logs ready? Evals, red-team tests, schema checks pass? Rate-limit, timeout, retry, rollback paths tested? Support can trace a user report from `avalai-request-id` to prompt version and model route? UX is clear about AI limits, review path, unsafe-content decisions?
Related: production-best-practices (captured), responses-vs-chat-completions, data-controls, rate-limits, safety-best-practices, red-teaming (captured), cost-optimization (not captured).
