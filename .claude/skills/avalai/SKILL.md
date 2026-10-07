---
name: avalai
description: Expert guide for building with AvalAI (اول ای‌آی / "اول ai" / "هوش مصنوعی اول"), an OpenAI-compatible AI gateway at https://api.avalai.ir/v1. Use whenever the project calls AvalAI, api.avalai.ir, AVALAI_API_KEY, or the user asks about AvalAI models, pricing, rate limits, service tiers, credit packages, deprecations, Responses/Chat Completions/Messages APIs, images, audio, tools, streaming, structured outputs, function calling, or production practices. Always consult references/ instead of guessing model IDs, prices or limits.
---

# AvalAI skill

Source of truth: https://docs.avalai.ir/fa/ (Persian) — English at https://docs.avalai.ir/en/.
Official name is always written **AvalAI**. Users may also say «اول ai», «اول ای آی», «هوش مصنوعی اول».

## Core facts (from the Introduction page)
- Single base URL for OpenAI-compatible clients: `https://api.avalai.ir/v1`
- Auth: project API key in env var `AVALAI_API_KEY`. Create it in the dashboard (https://chat.avalai.ir/platform/home). **Server-side only — never ship to browsers/mobile apps.**
- Recommended first call: **Responses API** (`client.responses.create`), read `response.output_text`.
- Works with the official OpenAI SDKs (Python/JS) and plain cURL.
- Support: ticket https://chat.avalai.ir/platform/support/create-ticket · status https://status.avalai.ir/ · debug with AvalAI chat https://chat.avalai.ir/chat

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)
print(response.output_text)
```

## Working rules
1. Read the matching file in `references/` before writing code; see `references/00-index.md` for the page map and which pages are already captured.
2. Never invent model IDs, prices, tiers or limits. If a reference file is missing or marked PENDING, say so and ask the user for that page.
3. Model availability depends on account tier (e.g. some models "from tier 1"). Check `references/` for tier and endpoint support (Chat Completions / Messages / Responses — support may be full or partial per model).
4. Keys from env, never hard-coded; plan security, retries, latency and cost per production-best-practices.
5. Dates in docs are Jalali with Gregorian in parentheses; promotional rates expire — check dates.

## References
See `references/00-index.md`.

## Practical rules from Quickstart
- New text apps → `/v1/responses` (`input`, `instructions`, `response.output_text`); keep `/v1/chat/completions` (`messages`) for legacy/chat-only models.
- On `429`: honor `Retry-After`, exponential backoff + jitter + retry cap.
- Discover models: `GET https://api.avalai.ir/public/models` (no auth) or `/v1/models`.
- Provider-specific params: `extra_body` (Python) / `@ts-expect-error` direct fields (TS).
- Exact cost: read `avalai-request-id` header → `POST /user/v1/transactions/lookup` (available ~30s later).
- Model IDs in examples may be stale; verify live before hard-coding.

## Tool integration rules (ai-workflows)
- Base URL `https://api.avalai.ir/v1`; tools append `/chat/completions` themselves — never paste the full path into a base-URL field.
- Model prefix is tool-specific: OpenCode `avalai/<id>`, Aider `openai/<id>`, direct API plain `<id>`.
- Use a dedicated AvalAI key (not OpenAI/ChatGPT credentials). Don't use `gpt-transcribe`/`gpt-live-transcribe` on AvalAI.
- Start direct; add 9Router (a gateway, not an agent) only when routing/fallback is needed. Human approval before side effects; synthetic data first.

## SDK rules (libraries)
- OpenAI SDK → base `https://api.avalai.ir/v1`. Anthropic SDK & Google GenAI SDK → base `https://api.avalai.ir` (**no `/v1`**). Anthropic SDK can call non-Claude models via `/v1/messages`; Google SDK is Gemini-only.
- Pin SDK versions; keep a raw-HTTP fallback; set explicit timeouts for flex tier / long jobs; retry only idempotent operations.
- Log `avalai-request-id`; optionally send `X-Client-Request-Id`.
- Several published snippets have SDK-version quirks (Go/.NET/Google Python) — see notes in `references/04-libraries.md` and verify against the installed SDK.

## Performance rules
- Cache: stable prefix first, dynamic last; byte-identical prefix; verify `usage.prompt_tokens_details.cached_tokens`; app must work on cache miss and keep its own conversation state.
- Cap output (`max_output_tokens` for Responses, `max_completion_tokens` for Chat), stream, reuse connections, log p50/p90/p95 + request IDs.
- Benchmarks in docs are point-in-time observations, never guarantees. Main domain `api.avalai.ir`; `api.avalapis.ir` is a slower alternate; Guardrail adds ~200–300 ms.

## Pricing rules
- Prices are USD per 1M tokens, pass-through (no markup). Live source: `GET https://api.avalai.ir/public/models` — check `pricing`, `min_tier`, `tier_rate_limits`, `supported_endpoints` before quoting or hard-coding. Snapshot in `references/06-pricing.md`.
- Hidden reasoning tokens bill at the **output** rate; don't add `reasoning_tokens` to `output_tokens` (double count).
- `service_tier: "flex"` = 50% cheaper for select OpenAI models, up to 900 s, may fail → fall back to `default`; credit packages do NOT cover flex.
- `estimated_cost` in responses is NOT for billing; use `avalai-request-id` + User API `/user/v1/transactions/lookup` for exact cost (~30 s delay).
- Free signup credit: 25,000 T (email) → 200,000 T total after phone verification.
- Watch promo expiries (GLM-5.3-Flash 18 Shahrivar 1405, Gemini 3.8 Flash & TTS 10 Dey 1405) and the `deepseek-v4-pro` → `deepseek-v4.1-flash` reroute on 2026-09-14.

## Service-tier rules
- Public values: `default` (credit packages cover it) and `flex` (−50%, up to 900 s, no credit-package coverage, select OpenAI models only: gpt-5.5, 5.4-pro/5.4/mini/nano, 5.2-chat, 5.2, 5.1, 5, 5-mini, 5-nano, o3, o4-mini). Never send `priority`/`auto` unless the account has it.
- Flex pattern: timeout 900 s, on failure/timeout retry with `service_tier: "default"` + exponential backoff (idempotent work only). Log returned `service_tier` with `avalai-request-id`.
- Flex on an unsupported model → `invalid_request` error.

## Credit-package rules
- Packages = prepaid, discounted (20–40%), scoped to listed models, fixed validity (1/7/30/31 d), per-template purchase cap, non-transferable, flex tier NOT covered. Keep overall balance positive (≥100,000 Toman) or API is disabled.
- Package credit is consumed before general balance; out-of-scope models bill at standard rates.
- Verify with `POST /user/v1/transactions/lookup` → `cost.source` = `credit_package` | `balance`. Check live availability at the store/API before recommending a package; Claude packages are currently unavailable.

## Rate-limit rules
- Tiers: Tier 0 (email) → Tier 1 (phone verified, instant) → Tier 2/3/4/5 at cumulative top-up ≈ $10/$50/$250/$1,000. Automatic, instant, no credit deducted. Metrics: RPM, RPD, TPM, TPD, IPM (first hit wins). Per-model limits: `tier_rate_limits` in `/public/models` or per-tier pages.
- 429 `rate_limit_exceeded` → honor `Retry-After`, exponential backoff + jitter + cap; use `x-ratelimit-*` headers; client-side token bucket / queue for volume. Batch API not available yet.
- `/user/v1` limits per tier (req/min): 3, 15, 50, 150, 350, 750.

## Deprecation rules (read 10-deprecations.md before choosing a model ID)
- DeepSeek: any DeepSeek ID currently routes to `deepseek-v4.1-flash`; use only `deepseek-v4.1-flash` / `deepseek-flash`.
- GPT-5 `-chat` IDs (`gpt-5-chat`, `gpt-5.1-chat`, `gpt-5.2-chat`, `gpt-5.3-chat`, `*-chat-latest`) are removed → use base `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.3`.
- Removed families: Claude 3.x/4.0/4.1 (Bedrock + native), Imagen 4, Gemini 1.5/2.0, Gemma 3, Qwen turbo/VL/max legacy, Moonshot v1/kimi-k2-thinking, GLM ≤5, MiniMax M2/M2.1, Seedream 4.x, Stability, many NVIDIA NIM / Cloudflare cf.* IDs.
- Upcoming provider shutdowns: gpt-5.4-cyber 2026-10-01; legacy GPT snapshots 2026-10-23; Evals/Prompts/Agent Builder 2026-11-30; gpt-image-1/1-mini/1.5 2026-12-01; GPT-5/o3 snapshots 2026-12-11; legacy audio/realtime 2027-01-20; whisper/gpt-4o-transcribe 2027-02-26.
- Prefer stable (non-preview) IDs; avoid `-latest` aliases for regulated/regression-sensitive workloads. Always verify with live `/v1/models`; where reference files disagree, deprecations + live API win.

## Reseller billing rules (references/resellers/)
- Never bill from `estimated_cost`. Store `avalai-request-id` (response HEADER; OpenAI SDK: `response._request_id`) per customer request, wait ~5 s (≤30 s), then `POST /user/v1/transactions/lookup` (≤1000 ids per call) and bill from `cost.unit` (USD) / `paid_irt + paid_grant_irt` (Toman). Prefer async worker; retry with backoff; store full transaction detail; key charges on `request_id` (idempotent).
