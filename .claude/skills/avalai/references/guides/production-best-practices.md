# Production best practices (docs.avalai.ir/fa/guides/production-best-practices)

Moving AI projects from prototype to production.

## Organization setup
- **API keys:** keep secret (never client-side code/public repos); env vars not hard-coded; **separate keys for dev/test/prod**; rotate regularly. Set an email **notification threshold** and optionally a **monthly budget** (careful: hitting the budget can disrupt your app/users); use the usage dashboard for current/past billing cycles.
- **Staging vs production isolation:** separate keys/projects/accounts for local dev, staging, production; production access only for services/operators who need it; lower cost + rate-limit alerts in staging so runaway tests fail safely; model ID, provider route and feature flags in env vars (rollback without a code deploy); test route-dependent features (stored Responses, background jobs, hosted tools, Files API cleanup, Realtime sessions) in staging before promising them in prod.

## Model version management
Use **stable** model names when available; migrate from preview ids ASAP (preview models can be deprecated with short notice; stable ones get longer availability and predictable behaviour). Subscribe to deprecation notices (10-deprecations.md); model name from env var; plan migration before preview deadlines. `MODEL_NAME = os.getenv("AI_MODEL", …)`.
⚠ The page's example pair `gemini-2.5-flash-image-preview` → `gemini-2.5-flash-image` is outdated: **`gemini-2.5-flash-image` itself retired 2026-10-02** (10-deprecations) → use the current image model (see guides/image-generation.md).

## Rate limits
See guides/rate-limits.md: exponential backoff on 429; monitor usage; batch inputs (e.g. embeddings); monitor response headers (`x-ratelimit-remaining-requests`, `x-ratelimit-remaining-tokens`, `x-ratelimit-reset-requests`; api-reference/response-headers) and back off proactively. Doc sample bugs: `api_key` and `import time` missing; defaults to 0 when headers absent (→ false alarm) — treat missing as unknown.
Tiers (automatic, instant upgrade): **Tier 0** email signup, 25,000 T activation credit · **Tier 1** verified phone → total 200,000 T (or +175,000 T on top of email account), no top-up needed (NOT additive to the email credit) · **Tier 2** cumulative top-up ≈ $10 · **Tier 3** $50 · **Tier 4** $250 · **Tier 5** $1,000. Per-model limits: rate-limits pages.

## Reasoning & agentic workflows
New GPT-5-series and agentic workloads → Responses API (unless maintaining Chat Completions). Checklist:
- State: `previous_response_id` for simple multi-turn; manual item replay for stateless/compliance-sensitive; context compaction for long-running agents.
- **Resend stable `instructions` on every request** when using `previous_response_id`; `store:true` only if retention policy allows.
- `reasoning.effort`: GPT-5.5 defaults to `medium`; use the lowest level passing evals; `high`/`xhigh` when latency+cost justified.
- Control length separately via `text.verbosity`, word limits, section counts, table width, JSON-only.
- Contract via schema: Structured Outputs `text.format` over prompt-only JSON descriptions.
- Cacheable context stable: long reusable policy/product context first, dynamic user facts near the end, stable `prompt_cache_key` for repeating traffic.
- Tool descriptions as interfaces (what it does, when to call, required inputs, side effects, when retry is safe, common errors).
- Show progress: short preamble/status for tool-heavy flows.
Migrating old prompts to GPT-5.5: start from the smallest prompt that preserves the product contract (outcome, success criteria, allowed side effects, evidence rules, output shape); drop legacy step-by-step guidance unless that exact process is needed.

### Gate advanced Responses features in staging (route-dependent)
| feature | use | AvalAI release check |
|---|---|---|
| `tool_search`/deferred tools | big tool catalog | if hosted discovery isn't enabled, filter tools in your app before calling |
| hosted tools | web/file search, code exec, image gen, computer-use | prefer documented AvalAI endpoints first; verify provider-native hosted tools before relying |
| compaction | long agents lose state | hosted only if supported; else app-managed summary (decisions, IDs, open tasks) |
| `reasoning.encrypted_content` | reasoning continuity without stored state | round-trip returned reasoning items exactly; don't parse/rewrite |
| `background:true` | long tasks / polling | NOT hosted on AvalAI unless route proves it → app-managed jobs |
| WebSocket mode | multi-turn tool agent | keep HTTP + `previous_response_id` or manual replay unless staging proves WS + recovery |
Record unsupported hosted features as explicit product decisions. Deep go/no-go list: deployment-checklist (not captured).

## Observability
Log `avalai-request-id`, model, endpoint, service tier, latency, input/output/cached-input tokens, tool-call count, final status; for chained Responses also the current response id and state strategy.

## Release confidence: eval, guardrails, rollout
- Define KPIs/SLOs: task accuracy, refusal quality, hallucination rate, tool success rate, p95 latency, token cost, error rate.
- Keep a golden eval set in the repo (representative inputs, expected behaviour, pass/fail rubrics, known edge cases); local/CI evals (guides/evals.md, promptfoo example) until hosted eval endpoints exist.
- Calibrate automated graders vs human labels before CI; human review for safety, financial, legal, medical, data deletion and other high-impact actions.
- Guardrails at the right boundary: user input before costly work; tool args before side effects; final output before delivery; human approval for production-state changes (agentic_guardrails_schema_workflow example – not captured).
- Gradual rollout: pin current model+prompt, A/B or canary the candidate, compare eval + production metrics, keep rollback ready. Add production failures to the dataset before fixing the prompt.

## Scaling
Horizontal (more nodes + load balancing, design for multi-node), vertical (bigger nodes; app must use resources), caching (DB/file/memory; invalidate when data changes), load balancing (LB or DNS round-robin).

## Latency
Request ≈ network (user→API) + prompt-token processing + token generation + network back; **generation dominates** (tokens sequential; prompt tokens add little).
Seven levers: 1) faster token processing — route simple tasks to smaller/lower-latency models after evals; 2) generate fewer tokens — explicit budget, `max_output_tokens` (Responses) / `max_completion_tokens` (Chat); 3) fewer input tokens — prune RAG context, strip HTML, dedupe history, cache-friendly prefix; 4) fewer requests — merge steps into one structured response; 5) parallelize independent classification/retrieval/moderation/enrichment (respect rate limits); 6) reduce perceived wait — stream, show tool/workflow status; 7) don't default to the LLM — hard-code bounded confirmations, precompute common answers, dedicated UI for metrics/search results. Prioritize cutting output tokens.
Factors: model choice (bigger = slower); completion tokens (lower max, stop sequences, fewer completions `n`/`best_of`); streaming (`stream:true` → faster first token; same total time). `max_tokens` = legacy compatibility.
⚠ **Reasoning models:** caps include hidden reasoning tokens → possible `status:"incomplete"`, `incomplete_details.reason:"max_output_tokens"`, empty text (Responses) or `finish_reason:"length"` (Chat). Check `usage.output_tokens_details.reasoning_tokens`; raise the cap, lower `reasoning.effort` (`low`/`none` if supported), simplify/split the task, leave final-answer headroom (guides/reasoning.md).
Streaming/async samples = Chat-based (same as best-practices). Doc defects: Go samples use lowercase `model:` (doesn't compile) and write to a shared map from goroutines (race); JS async sample hard-codes `"AVALAI_API_KEY"` literal; PHP `Promise` not defined by the OpenAI client; Responses-equivalent blocks are non-streaming.

## Cost
Notification threshold + optional monthly budget; usage dashboard. User API (api-reference/user.md): `/user/v1/transactions/lookup` with `avalai-request-id` for exact per-call cost; poll balance for budget alerts; track usage over time. Example flow: call API → read `avalai-request-id` → wait a few seconds → `POST /user/v1/transactions/lookup {"transaction_ids":[id]}`. Resellers: resellers/cost-tracking-guide.
Token usage: pay-as-you-go priced per 1K tokens (~750 words); forecast using traffic, interaction frequency, data volume.
**Hidden `reasoning_tokens` are billed at the model's output-token rate across providers. `usage.output_tokens` already includes them (`output_tokens_details.reasoning_tokens` is a breakdown): cost = `output_tokens × output_price` — NOT `(output_tokens + reasoning_tokens)`.** Only if a route reports visible + reasoning separately do you price both at the output rate.
Reduce cost = cheaper per token (smaller models for simple tasks) and fewer tokens (shorter prompts, caching common queries, fine-tuning [hosted fine-tuning not available on AvalAI]). Measure with `usage`, User API, Models API — not character estimates. Pre-send estimation: guides/token-counting (not captured); verify `POST /v1/responses/input_tokens` is enabled on your route before building controls on it.
Also: prompt caching (watch `cached_tokens` + cached-input price), batch/low-priority/async modes only for delay-tolerant work.

## MLOps
Data/model management (dataset versioning, transform tracking, quality checks, source/preprocessing docs); model monitoring (accuracy/performance, degradation alerts, usage patterns, concept/data drift); **service status: status.avalai.ir** (subscribe for maintenance/incidents; add health checks before critical operations); retraining criteria/automation/validation/version history; deployment (CI/CD, rollback, staging, config docs). (Hosted fine-tuning/MLOps for it isn't available — see fine-tuning.md.)

## Security & compliance
Content filtering via moderation endpoints; usage policies; minimize data shared, inform users, retention policy.
**`safety_identifier`** (where the route supports it): stable privacy-preserving per-end-user id so abuse can be attributed to a user without raw PII. Hash a stable internal user id/username/email (one-way); anonymous previews → opaque session id; keep it SEPARATE from `prompt_cache_key`; it is not carried automatically across APIs/sessions → send the same value on every related Responses / Chat Completions / Messages / realtime request; log hashed id with `avalai-request-id`, model, route, moderation result; store full prompts only if retention policy allows. With `store:false` examples see safety-best-practices + data-controls (not captured).
Errors: handle HTTP statuses, log API errors, user-friendly messages (guides/error-handling.md). Data storage/transfer/retention, encryption/anonymization, input sanitization, secure coding.

## Business considerations
Clear success metrics/KPIs, alignment with business goals, user adoption/training, feedback loops, scalability of the business model.
Related: deployment-checklist, data-controls, authentication, user API, rate-limits, response-headers, deprecations, error-handling, streaming-responses, safety-best-practices, examples (promptfoo, agentic guardrails, rate_limit_safe_parallel_requests), fine-tuning, status.avalai.ir.
