# Rate limits & tiers (guide) — complements ../09-rate-limits.md
Metrics: RPM, RPD, TPM, TPD, IPM — whichever hits first. Limits are per organization AND per model (shared across keys; sibling aliases may share a pool; use exact model id; long-context requests may have lower upstream limits).

## Tiers (auto, instant upgrade, no tickets; credit kept)
| tier | how | free credit |
|---|---|---|
| 0 | email signup | 25,000 toman |
| 1 | phone verified (total 200,000 toman; +175,000 on top of email credit — NOT additive 200k) | 200,000 |
| 2 | cumulative top-up ≥ $10 | |
| 3 | ≥ $50 | |
| 4 | ≥ $250 | |
| 5 | ≥ $1,000 | |
Tier 2+ computed from cumulative historic top-ups (not balance), in rial converted at the rate on chat.avalai.ir/platform. Toman credit isn't auto-converted to USDT; optional conversion with 3% fee at /platform/billing/credit. No monthly spend cap. Per-tier pages `/rate-limits-tier0..5` hold per-model numbers (not yet captured).

## Files API limits (per minute; beta free 11 Dey–10 Esfand 1404)
| tier | upload | download | delete | storage |
|---|---|---|---|---|
| 0 | 3 | 5 | 10 | 250 MB |
| 1 | 10 | 100 | 100 | 2 GB |
| 2 | 50 | 250 | 250 | 5 GB |
| 3 | 250 | 500 | 500 | 15 GB |
| 4 | 500 | 1000 | 1000 | 50 GB |
| 5 | 1500 | 2000 | 5000 | 200 GB |
Max file 128 MB (beta). Source says beta window already over (today 2026-10-07) — verify billing for files.

## Headers
`x-ratelimit-limit-requests`, `-remaining-requests`, `-reset-requests`, `-limit-tokens`, `-remaining-tokens`, `-reset-tokens`; maybe `x-ratelimit-*-project-tokens`. 429 body: `{error:{type:"rate_limit_error",code:"rate_limit_exceeded"}}`; `Retry-After` seconds.

## Handling
Exponential backoff + jitter, honour Retry-After, cap retries (failed requests still consume RPM), client-side token bucket, batch embeddings inputs, cache, cap per-user product quotas. Multiple keys don't raise limits (org-level).
Doc bugs: Go sample uses lowercase `model:` field & `openai.APIError` from go-openai; token-bucket sample has indentation bug (usage inside `_refill`); bash sample reads nonexistent `retry_after` JSON key; Python `RateLimitError.headers` should be `e.response.headers`.
