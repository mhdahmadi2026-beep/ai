# News 2025-12-15 (1404-09-24): Flex service tier (docs.avalai.ir/fa/news/2025-12-15-flex-service-tier-launched)

`"service_tier":"flex"` = 50% off standard for select OpenAI models; response echoes `service_tier`.
- Models: `gpt-5.2`, `gpt-5.1`, `gpt-5`, `gpt-5-mini`, `gpt-5-nano`, `o3`, `o4-mini` (+ dated aliases). Others (e.g. gpt-4o-mini) → 400 `invalid_request` listing supported models (see fa/service-tiers).
- Flex price/1M (in / cached / out): gpt-5.2 0.875/0.0875/7.00; gpt-5.1 & gpt-5 0.625/0.0625/5.00; gpt-5-mini 0.125/0.0125/1.00; gpt-5-nano 0.025/0.0025/0.20; o3 1.00/0.25/4.00; o4-mini 0.55/0.138/2.20. (Snapshot Dec 2025; o3/GPT-5 snapshots are deprecated Dec 2026 — check 10-deprecations.md and live catalog.)
- Slower: server timeout up to **900 s**; may time out/fail. For batch/background/non-prod only; NOT for interactive. Set client `timeout=900` and fall back to `service_tier="default"` on error.
- **Credit packages do NOT cover Flex** — charged to standard balance.
