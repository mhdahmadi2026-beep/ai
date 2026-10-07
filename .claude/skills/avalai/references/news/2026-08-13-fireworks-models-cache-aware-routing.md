# News 2026-08-13 (1405-05-22): Fireworks models & cache-aware routing (docs.avalai.ir/fa/news/2026-08-13-fireworks-models-cache-aware-routing)

- `muse-glimmer-30b` (Meta via Fireworks.ai; reasoning, function calling, image input, prompt cache; 131,072 ctx; in $0.35 / cached 0.04 / out 1.50) and `nemotron-3.5-lightning` (NVIDIA; efficient reasoning/agentic, function calling, cache; 262,144 ctx; 0.05 / 0.01 / 0.20). Both: chat full, messages full, responses partial.
- **Cache-aware routing (best effort):** per user + model + infrastructure, the router prefers the last healthy, successful infra for **15 min after the last successful request** (rolling; each success extends it). Not guaranteed — health/capacity/failover can move requests; warm-up takes time (deepseek-v4-flash ~15 s, v4-pro longer). Keep stable prefixes, dynamic content last; verify via `usage.prompt_tokens_details.cached_tokens`.
- Benchmark (2026-08-13, deepseek-v4-flash, 15 s wait, 10 rounds): rounds 2–10 warm hit 98.6% on both AvalAI and DeepSeek direct (+0.0 pp); single model/run, no global guarantee. Details at fa/performance.
- Explicit cache creation / breakpoints / provider cache markers still NOT supported.
- Source defect: page embeds `<<< ../../tests/benchmarks/test_cache_hit_ratio.py{python}` (unresolved include — benchmark source not captured).
