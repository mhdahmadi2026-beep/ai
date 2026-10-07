# عملکرد AvalAI / Performance — https://docs.avalai.ir/fa/performance

Covers: prompt-cache usage, regional latency, token generation speed, and how to measure correctly in production. Newest experiments first. Numbers come from specific runs — **not a permanent service guarantee**.

## Reports of 1405-05-23 (2026-08-14 artifacts) — cache hit
Latest benchmark sends a realistic **legal-document-analysis** request via AvalAI and via each model's official provider, on both `v1/chat/completions` and `v1/responses`. Round 1 primes each service's cache; runner waits **15 s**; rounds 2–5 measure **warm** behavior. A request counts as a cache hit only when the API reports cached tokens — mainly `usage.prompt_tokens_details.cached_tokens / usage.prompt_tokens` — **not** by request order, response time or assumed constant prefix.
Setup: one run, 5 paired sequential rounds per API, 3 models: `deepseek-v4-flash`, `glm-5.2`, `kimi-k3`. Observations only, not an SLA.

### `deepseek-v4-flash` — AvalAI vs DeepSeek
Both succeeded 5/5 on both APIs. AvalAI reported **99.9%** cache hit every round (1,400 of 1,401 tokens); DeepSeek **95.1%** (1,408 of 1,480). Warm difference **+4.8 pp** for AvalAI on both APIs.
| Service | API | Warm cache hit | Avg latency | Success |
|---|---|---:|---:|---:|
| AvalAI | chat/completions | **99.9%** | 1.704s | 5/5 |
| DeepSeek | chat/completions | 95.1% | 6.201s | 5/5 |
| AvalAI | responses | **99.9%** | 18.282s | 5/5 |
| DeepSeek | responses | 95.1% | 6.444s | 5/5 |
Charts (not downloaded): `/fa/_media/img/cache_hit_{bar,line}_deepseek-v4-flash_{chat_completions,responses}_20260814_175107.png`

### `glm-5.2` — AvalAI vs Z.AI
Chat Completions: both 5/5 and **99.9%** warm (AvalAI 1,409/1,410 in rounds 2–5; Z.AI 1,408/1,410). Responses: AvalAI 5/5, **99.9%** after priming; Z.AI returned **404 Not Found** for all five because the tested public base URL doesn't offer that endpoint — an endpoint-availability result, **not** 0% cache hit on successful requests.
| Service | API | Warm cache hit | Avg latency | Success |
|---|---|---:|---:|---:|
| AvalAI | chat/completions | **99.9%** | 20.394s | 5/5 |
| Z.AI | chat/completions | 99.9% | 4.971s | 5/5 |
| AvalAI | responses | **99.9%** | 2.830s | 5/5 |
| Z.AI | responses | n/a | — | 0/5 |
Charts: `cache_hit_{bar,line}_glm-5.2_{chat_completions,responses}_20260814_175704.png`

### `kimi-k3` — AvalAI vs Moonshot AI
Both 5/5 on Chat Completions with **85.8%** cache hit every round (1,280 of 1,492 tokens). AvalAI Responses 5/5, **85.8%**. Moonshot's tested public API rejected `v1/responses`: four access errors + one connection error. **AvalAI still accepts Responses requests for this model and converts them in its internal routing layer to the compatible upstream flow.**
| Service | API | Warm cache hit | Avg latency | Success |
|---|---|---:|---:|---:|
| AvalAI | chat/completions | **85.8%** | 4.187s | 5/5 |
| Moonshot AI | chat/completions | 85.8% | 7.819s | 5/5 |
| AvalAI | responses | **85.8%** | 4.401s | 5/5 |
| Moonshot AI | responses | n/a | — | 0/5 |
Charts: `cache_hit_{bar,line}_kimi-k3_{chat_completions,responses}_20260814_180128.png`

### Method & reproduction
Runner sends requests sequentially — AvalAI first, then the official provider — and builds an **independent `previous_response_id` chain per service** for Responses rounds. JSON artifacts keep the full provider-reported `usage` object; docs deliberately publish no local paths/credentials.
```bash
python tests/benchmarks/test_cache_hit_ratio.py \
  --model deepseek-v4-flash --rounds 5 --prefix-tokens 2000 \
  --official-provider deepseek

python tests/benchmarks/test_cache_hit_ratio.py \
  --model glm-5.2 --rounds 5 --prefix-tokens 2000 \
  --official-provider zai

python tests/benchmarks/test_cache_hit_ratio.py \
  --model kimi-k3 --rounds 5 --prefix-tokens 2000 \
  --official-provider moonshot.ai
```
The full corrected script (both APIs, independent Responses chain per service, OpenAI- and Anthropic-style `usage` shapes, auto provider/alias detection, stream stall guard, JSON artifacts, per-endpoint charts; keys read from flags or standard env vars, never written to artifacts) is included on the site via a code-include `../tests/benchmarks/test_cache_hit_ratio.py`. **That source was NOT in the captured text — PENDING (ask user for the file if needed).**

### Scope & limits
Three 5-round experiments observed on 1405-05-23. An official-provider Responses error means that endpoint wasn't available on the tested public API — not 0% cache hit. Latency depends on model/network conditions; one slow request shifts a 5-round mean noticeably. **Apps must work correctly on cache miss and must not treat affinity as a substitute for conversation state.** Details: /fa/guides/prompt-caching

## Optimization guide
### Improve cache-hit ratio
- Put stable instructions, policy text, tool schemas, images and reusable examples **first**; dynamic context and timestamps **last**.
- Keep the prefix **byte-identical**; verify `usage.prompt_tokens_details.cached_tokens` (or the provider-native field).
- Compare warm requests separately from priming; log model, route, prompt version, request ID and timestamps.
### Reduce latency / raise throughput
- Start with the smallest model that passes your evals; keep large reasoning models for hard decisions.
- Cap output: `max_output_tokens` (`/v1/responses`) or `max_completion_tokens` (`/v1/chat/completions`).
- Stream user-facing output; parallelize only independent work; reuse HTTP connections.
- Remove unnecessary model calls; combine adjacent steps into one structured response when possible.
### Measure production behavior
Log TTFT/TTFB, total latency, model, endpoint, input/output/cached tokens, request ID, status, retry/fallback count. Report **p50, p90, p95**, not one mean. Read with /fa/guides/latency-optimization and /fa/guides/cost-optimization.

## Regional latency benchmarks
Studies used main domain **`api.avalai.ir`** with **Guardrail disabled** for like-for-like infrastructure comparison. Guardrail is recommended for most apps but added ~**200–300 ms** in these historical tests. The alternate connectivity domain **`api.avalapis.ir`** inherently has higher latency and was not used.
AvalAI keeps persistent connections and provider connection pools; optimized request processing/networking/repeated calls reduce platform overhead. Geography, model load, output length, security settings and network still affect every measurement.

### Latest — 20-07-1404 (as printed; Jalali 1404-07-20)
Setup (both regions): model `gpt-4o-mini`; 4 GB RAM, 2 vCPUs.
**Europe — Microsoft Azure EU VM, vs direct OpenAI from same location**
| Metric | AvalAI | OpenAI |
|---|---:|---:|
| Avg TTFB (s) | 0.435 | 0.717 |
| Median TTFB (s) | 0.393 | 0.685 |
| p95 TTFB (s) | 0.605 | 1.032 |
| Avg tokens/s | 24.5 | 13.8 |
| Success | 100% | 100% |
Claim: AvalAI **~39% faster** than direct OpenAI (median 0.393 vs 0.685 s) and **77% higher** token throughput. Attributed to persistent connections to OpenAI infrastructure and optimized request handling. Chart: `_media/img/api_performance_comparison_20251012_a.png`

**Middle East — Arvancloud VM**
| Metric | AvalAI | OpenAI |
|---|---:|---:|
| Avg TTFB (s) | 0.703 | 1.246 |
| Median TTFB (s) | 0.668 | 1.048 |
| p95 TTFB (s) | 0.947 | 2.309 |
| Avg tokens/s | 14.9 | 8.4 |
| Success | 100% | 100% |
Claim: **44% faster** response time (0.668 vs 1.048 s median), **77% higher** throughput (14.9 vs 8.4). Gap grew significantly since the Khordad (June 2025) benchmarks. Chart: `api_performance_comparison_20251012_b.png`

### Historical — Khordad 1404 (22-03-1404)
**Europe (Azure)**
| Metric | AvalAI | OpenAI |
|---|---:|---:|
| Avg TTFB | 0.728 | 0.531 |
| Median TTFB | 0.683 | 0.510 |
| p95 TTFB | 1.056 | 0.740 |
| Avg tokens/s | 15.9 | 18.9 |
| Success | 100% | 100% |
Then: ~200 ms overhead vs direct OpenAI (expected: OpenAI hosted mainly on Azure); value-adds = unified routing, security layers, multi-provider. Chart: `api_performance_comparison_53111243.png`
**Middle East (Arvancloud)**
| Metric | AvalAI | OpenAI |
|---|---:|---:|
| Avg TTFB | 0.993 | 1.095 |
| Median TTFB | 0.929 | 0.951 |
| p95 TTFB | 1.479 | 1.386 |
| Avg tokens/s | 11.4 | 9.6 |
| Success | 100% | 100% |
Then: already competitive in Middle East (lower latency, higher throughput). Chart: `api_performance_comparison_53111244.png`

## Reproduce regional latency
Script saved verbatim at `references/scripts/latency_benchmark.py` (60 requests per API, prompt "Say hi", `gpt-4o-mini`, env vars `AVALAI_API_KEY` & `OPENAI_API_KEY`; outputs table, `api_performance_comparison.png`, `api_performance_results.json`). Install: `requests numpy matplotlib seaborn tabulate tqdm`. Requires **Python 3.12+** (nested same-type quotes in f-strings). Benchmarks used `gpt-4o-mini` but improvements apply to all models; test any model you want.

## Related
/fa/guides/latency-optimization · /fa/guides/token-counting · /fa/guides/prompt-caching · /fa/guides/rate-limits
