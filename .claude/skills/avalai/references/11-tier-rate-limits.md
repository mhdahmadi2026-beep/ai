# Per-model rate limits by tier (RPM / TPM) — from the generated catalog on /fa/pricing (snapshot ≈ 2026-10-07)

Format `RPM/TPM`; `x` = no access (below the model's `min_tier`); `RPM` only = no TPM limit published. Columns: T0 (email, base) · T1 (phone) · T2 (≥$10 cumulative) · T3 ($50) · T4 ($250) · T5 ($1,000). K=1e3, M=1e6. **Live truth: `GET /public/models` → `tier_rate_limits["0".."5"]{max_requests_per_1_minute,max_tokens_per_1_minute}`** (no key) or `/v1/models/{id}` → `extra.rate_limits`. Odd values on the page (e.g. T3 < T2, whisper-1 TPM 2147483647, o4-mini T2 TPM < T1) are source quirks — treat as unverified. Tier rules: references/09-rate-limits.md; backoff patterns: examples/rate-limit-safe-parallel-requests.md.

## Chat / reasoning
| model | T0 | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|---|
| gpt-6.1-sol | x | 50/500K | 150/2M | 250/4M | 1500/8M | 10K/20M |
| gpt-6-sol, gpt-6-luna | 1/10K | 50/500K | 150/2M | 250/4M | 1500/8M | 10K/20M |
| gpt-6-astra | x | 2/80K | 25/1M | 75/2M | 500/8M | 3500/30M |
| gpt-5.6-sol/-terra/-luna, gpt-5.5 | 1/10K | 50/500K | 150/2M | 250/4M | 1500/8M | 10K/20M |
| gpt-5.4 | 1/10K | 250/500K | 500/2M | 1K/4M | 3500/8M | 10K/20M |
| gpt-5.4-mini, gpt-5.4-nano | 3/10K | 250/500K | 500/2M | 1K/4M | 3500/8M | 20K/30M |
| gpt-5.4-pro | x | x | 500/2M | 1K/4M | 3500/8M | 5K/30M |
| gpt-5.3-codex | 1/10K | 250/500K | 500/2M | 1K/4M | 3500/8M | 10K/20M |
| gpt-5.2 / gpt-5.1 / 5.1-codex-max | 1/10K | 250/500K | 500/1M | 1K/2M | 3500/4M | 10K/10M (5.2: T5 10M; 5.1-2025-11-13: T0 x, T5 40M) |
| gpt-5.2-pro | x | x | x | 25/2M | 250/4M | 1K/10M |
| gpt-5, gpt-5-2025-08-07 | x | 250/450K | 500/800K | 750/2M | 1500/4M | 2500/8M |
| gpt-5-mini, gpt-5-nano | 1/40K | 250/450K | 500/800K | 750/4M | 1500/10M | 2500/30M |
| gpt-5-pro | x | x | 10/450K | 50/800K | 150/1M | 5K/30M |
| codex-auto-review | 3/10K | 250/500K | 500/1M | 1K/2M | 3500/4M | 10K/10M |
| gpt-4.1 | 3/40K | 500/450K | 1500/2M | 5K/4M | 5K/8M | 10K/50M |
| gpt-4.1-mini/-nano | 3/40K | 500/1M | 5K/4M | 5K/10M | 10K/30M | 30K/150M |
| gpt-4o / 4o-mini | 3/40K | 500/300K · 500/500K | 5K/3M | 5K/4M · 7500/5M | 10K/10M · 20M | 10K/30M · 30K/150M |
| o3, o3-2025-04-16 | x | x | 500/200K | 2500/800K | 3500/2M | 5K/4M |
| o4-mini | x | 100/450K | 250/100K | 500/200K | 1K/4M | 1500/1M |
| o3-pro | x | 100/30K | 1K/450K | 1500/800K | 5K/2M | 10K/30M |
| o1 | x | x | 500/800K | 5K/2M | 5K/30M | 5K/30M |
| o1-pro | x | x | x | x | 500/1M | 1500/2M |
| o3-mini | x | x | 500/1M | 5K/4M | 10K/10M | 30K/150M |
| claude-opus-5-5, claude-opus-5, claude-fable-5, claude-opus-4-8/4-7/4-6 | x | 2/30K | 25/450K | 50/800K | 100/1M | 150/4M |
| claude-fable-5-1 | x | x | 25/450K | 50/800K | 100/1M | 150/4M |
| claude-sonnet-5-5 | x | 2/30K | 25/800K | 50/120K | 100/2M | 150/8M |
| claude-sonnet-5, claude-sonnet-4-6 | x | 10/30K | 100/450K | 250/800K | 500/1M | 1500/4M |
| claude-opus-4-5 | x | 10/30K | 100/450K | 250/800K | 500/1M | 1500/4M |
| claude-sonnet-4-5 | x | 25/30K | 100/450K | 250/800K | 500/2M | 1500/4M |
| claude-haiku-4-5 | 1/10K | 25/50K | 100/450K | 250/1M | 500/4M | 1500/8M |
| anthropic.claude-* (Bedrock ids, 4-6/4-5…) | x | 1–2 RPM, 30–200K | 5/80–100K | 10–25/100–150K | 15–50/150–200K | 50–100/300–400K |
| gemini-3.8-flash, 3.7-flash, 3.6-flash, 3.5-flash, 3-flash-preview | 1/40K (3/40K for 3-flash-prev) | 50/500K | 250/1M | 1K/2M | 3500/5M | 25K/30M |
| gemini-3.5-flash-lite, 3.1-flash-lite(-preview), 2.5-flash-lite | 3/40K | 50/500K | 500/1M | 1K/3M | 3500/5M | 25K/20M |
| gemini-3.1-pro-preview | x | 10/500K | 75/2M | 250/4M | 500/10M | 10K/20M |
| gemini-2.5-pro | x | 10/1M | 50/2M | 500/3M | 2500/10M | 10K/20M |
| gemini-2.5-flash | 3/40K | 50/1M | 500/4M | 1K/8M | 2500/10M | 10K/20M |
| gemini-flash-latest | 3/40K | 25/200K | 100/1M | 500/2M | 750/4M | 10K/20M |
| gemini-flash-lite-latest | 3/40K | 50/800K | 100/2M | 500/5M | 750/8M | 10K/15M |
| gemma-4-26b-a4b-it | 3/5K | 50/200K | 150/500K | 450/1M | 750/4M | 5500/30M |
| gemma-4-31b-it | 1/5K | 5/10K | 10/15K | 15/20K | 20/25K | 600/10M |
| gemini-robotics-er-1.5-preview | 1/40K | 25/1M | 250/2M | 500/3M | 750/5M | 1K/10M |
| grok-4.7, 4.6, 4.5, 4.3, 4.20(-reasoning/-non-reasoning), 4-fast*, 4-1-fast* | 1/40K | 50/500K | 100/1M | 150/1.5M | 200/2.4M | 400/4M |
| grok-4.20-beta-0309-* | 1/40K | 5/80K | 10/100K | 15/150K | 25/200K | 30–40/400K |
| grok-4, grok-4-0709, grok-4-latest | x | 10/80K | 50/120K | 80/200K | 120/200K | 200/200K |
| grok-3(-latest/-beta), grok-3-fast | 3/40K (fast: x) | 50/400K | 250/2M | 500/4M | 800/4M | 1200/6M |
| grok-3-mini(-fast)(-beta/-latest) | 3/40K | 100/800K | 500/2M | 800/4M | 1200/6M | 1500/10M |
| grok-code-fast-1 | 3/40K | 75/400K | 150/800K | 250/1.2M | 350/1.5M | 450/2M |
| deepseek-v4.1-flash, deepseek-flash | 3/40K | 50/1M | 500/4M | 1500/8M | 2500/8M | 10K/50M |
| deepseek-v4-flash | 3/40K | 250/2M | 500/4M | 1500/8M | 2500/8M | 10K/50M |
| deepseek-v4-pro | 4/40K | 50/1M | 150/2M | 500/4M | 1K/10M | 5K/40M |
| deepseek-v3.2(-speciale), v3.1 | 3/40K (v3.1: 1/40K) | 250/500K | 500/1M | 1500/2M | 2500/3M | 3500/5M |
| deepseek-chat/-reasoner/-coder | 3/40K | 250/500K (coder 1M) | 500/2–3M | 1500/4M | 2500/8M | 5K/15M |
| glm-5.3, glm-5.3-flash, glm-5.2 | 3/40K | 25/10M | 250/4M | 500/8M | 750/10M | 1500/30M |
| glm-5.1 | 3/40K | 50/1M | 250/4M | 500/8M | 750/10M | 1500/30M |
| kimi-k3, kimi-k2.6, kimi-k2.5 | 3/40K | 50/1M (k2.5 100/1M) | 100/4M (k2.5 250/4M) | 250/8M | 500/10M | 5K/30M |
| kimi-k2.7-code | 3/40K | 50/1M | 250/4M | 500/8M | 750/10M | 5K/30M |
| kimi-k2.7-code-highspeed | 3/40K | 50/200K | 100/500K | 250/1M | 500/2M | 5K/3M |
| kimi-latest | 3/40K | 50/200K | 100/500K | 250/1M | 500/2M | 5K/3M |
| minimax-m3 | 3/40K | 50/1M | 100/4M | 500/8M | 750/10M | 5K/30M |
| minimax-m2.7 | 1/40K | 50/1M | 100/4M | 200/8M | 750/10M | 5K/30M |
| minimax-m2.7-highspeed, m2.5, m2.5-lightning | 1/40K | 50/200K | 100/450K | 200/800K | 350/1.2M | 500/2M |
| muse-glimmer-30b, nemotron-3.5-lightning, nemotron-3-ultra | 3/40K | 50/1M | 100/4M | 200/8M | 750/10M | 5K/30M |
| qwen3.8-flash, qwen3.8-27b | 3/40K | 20/500K | 150/2M | 350/4M | 750/8M | 1500/20M |
| qwen3.8-2.4t-a95b | x | 20/500K | 150/2M | 350/4M | 750/8M | 1500/20M |
| qwen3.8-max | x | 10/100K | 50/450K | 150/1M | 350/2M | 750/4M |
| qwen3.7-plus | 3/40K | 50/1M | 250/4M | 500/8M | 1500/10M | 5K/30M |
| qwen3.7-max | 1/40K | 10/200K | 25/1M | 50/800K | 75/1M | 600/2M |
| qwen3.6-max-preview | 1/40K | 10/200K | 25/1M | 50/800K | 75/1M | 600/2M |
| qwen3.6-plus | 1/40K | 150/1M | 750/4M | 1500/8M | 3500/10M | 10K/30M |
| qwen3.6-flash | 3/40K | 100/1M | 750/2M | 1500/4M | 3500/8M | 10K/10M |
| qwen3.6-35b-a3b, qwen3.6-27b | 3/40K | 20/200K | 75/1M | 150/800K | 250/1M | 600/2M |
| qwen3.5-flash | 1/40K | 190/200K | 750/1M | 1500/2M | 3500/4M | 10K/10M |
| qwen3.5-plus | 1/40K | 150/200K | 750/1M | 1500/1M | 3500/4M | 10K/5M |
| other qwen3.5/qwen3/qwen-plus/qwen-flash/qwq/legacy qwen-max | 1–3/40K | 10–25/200K | 25–75/200K–1M | 50–150/800K | 75–1K/1–1.2M | 600–750/2M (qwen-max*: T5 only 750/2M) |
| mistral-large-3 | 1/10K | 150/450K | 500/800K | 750/2M | 1500/4M | 2500/8M |
| sonar, sonar-pro, sonar-reasoning(-pro), sonar-deep-research | 3/40K | 10/200K | 50/450K | 75/2M | 150/4M | 250/10M |
| gpt-oss-120b (hosted) | 1/40K | 250/450K | 500/800K | 750/1.2M | 1500/2M | 2500/4M |
| llama-4-maverick-fp8 / llama-4-scout | x · 3/40K | 50/400K | 150/1M | 250/2M | 500/4M | 1500/10M |
| qwen3-235b-a22b-fp8-tput | x | 100/400K | 250/1M | 500/2M | 1K/4M | 1500/10M |
| groq.* (llama-4, kimi-k2-0905, gpt-oss, qwen3-32b, guards) | 1/10K (guards 3/40K) | 15–50/50–100K | 15–100/80–150K | 50–250/20–200K | 75–500/30–250K | 100–1K/30–300K |
| cf.* (Cloudflare Workers AI) | 1–3/5–40K | 15–250/40–450K | 50–500/100–800K | 100–750/200K–1.2M | 250–1K/450K–2M | 750–3500/1M–4M |
| nvidia_nim.* | 3/10K | 5/20K | 10/30K | 15/30K | 20/30K | 25/40K |

## Embeddings
| model | T0 | T1 | T2 | T3 | T4 | T5 |
|---|---|---|---|---|---|---|
| gemini-embedding-2, gemini-embedding-001 | 3/40K | 150/1M | 250/2M | 500/3M | 750/5M | 1K/10M |
| text-embedding-3-small/-large, ada-002 | 3/40K | 3K/1M | 5K/1M | 5K/5M | 10K/5M | 10K/10M (ada T5 5M) |
| embed-v-4-0 (cohere) | 3 RPM | 15 | 30 | 75 | 150 | 250 |
| cohere.embed-v4:0 / multilingual-v3 | 3/40K | 10/80K | 20/140K | 50/200K | 60/250K | 80/300K |
| text-embedding-v4 (alibaba) | 3/40K | 75/200K | 350/500K | 750/800K | 1200/800K | 1800/1M |
| text-embedding-v3 | 3/40K | 80/200K | 150/500K | 75/800K | 350/1.2M | 750/2M |
| tongyi-embedding-vision-plus/flash | 3/40K | 80/200K · 100K | 150/500K · 100K | 75/800K · 100K | 350/1.2M · 200K | 750/1.2M · 600/200K |
| cf.plamo-embedding-1b, cf.embeddinggemma-300m | 3/40K | 50/75K | 250/100K | 500/400K | 1K/800K | 3500/2M |
| nvidia_nim.nv-embed* | 3/10K | 5/20K | 10/30K | 15/30K | 20/30K | 25/40K |

## Images (RPM unless noted)
gpt-image-2, gpt-image-2.5-flare/-sunburst: x | 1/40K | 5/500K | 50/1M | 100/4M | 250/1M · gpt-image-1.5: x | 1/40K | 5/40K | 50/40K | 100/40K | 250/40K · gpt-image-1: x | 1/40K | 5/100K | 50/400K | 100/2M | 250/6M · gpt-image-1-mini: x | 3/40K | 10/400K | 50/400K | 100/2M | 250/6M · gemini-3.1-flash-image(+lite, -preview): x | 5/100K | 15/250K | 25/450K | 50/800K | 500/1M · gemini-3-pro-image(-preview): same but T5 150/1M · gemini-2.5-flash-image: x | 10/450K | 25/1M | 50/2M | 100/4M | 250/10M · flux.2-pro: x|5|15|25|50|100 · flux-1.1-pro, flux.1-kontext-pro: x|10|25|50|150|250 · cf.flux-2-*, cf.lucid-origin, cf.phoenix: x|10|25|50|150|500 · seedream-5-0: x|10|25|100|250|500 · seedream-4-5: only T5 500 · gen4_image(+turbo): x|3|10|25|100|250 · qwen-image-2.0/3.0/plus/*pro, z-image-turbo: x|5|10|25|50|100 (qwen-image & -edit: T0 1, T1 2, then 10|25|50|100; edit-plus x|2|10|25|50|100) · wan2.2-t2i-*: x|10|25|50|75|100.

## Video (RPM)
veo-3.1-fast-generate-preview, veo-3.1-generate-preview: x|1|3|5|15|50 · veo-3.1-generate-001, -fast-001: x|1|2|3|5|10 · gen4.5, gen4_turbo: x|1|2|5|25|50.

## Audio
STT: scribe_v1/v2: 3|100|250|500|1500|3500 RPM · gpt-4o-transcribe(-diarize): 3/40K|500/200K|1500/350K|3500/2M|5K/4M|10K/6M · gpt-4o-mini-transcribe: 3/40K|500/200K|1500/450K|3500/1M|5K/3M|10K/8M · whisper-1: 3|500|2500|5K|7500|10K RPM · groq.whisper-large-v3: 1/10K|50/100K|100/150K|150/200K|200/250K|300/300K (turbo T5 400/400K).
TTS: gemini-3.8-flash-tts/-lite-tts: 1/40K|25/1M|250/2M|500/3M|750/5M|1K/10M · gemini-3.1-flash-tts-preview, 2.5-pro-tts, 2.5-pro-preview-tts: x|25/1M|… same · gemini-2.5-flash-tts: 1/40K|25/1M|… · eleven_*: 3|100|250|500|1500|3500 RPM · runwayml.eleven_multilingual_v2: 1/10K|75|150|250|500|1K · tts-1: 3 RPM/200 TPM|500|2500|5K|7500|10K · tts-1-hd: x|500|2500|5K|7500|10K · groq.playai-tts(-arabic): 1/5K|25/10K|50/20K|100/30K|150/40K|250/50K.
Audio chat: gpt-audio, gpt-audio-1.5, -2025-08-28: x|100/30K|1K/450K|1500/800K|3500/2M|10K/30M (gpt-audio-mini: T0 1/10K).

## OCR / moderation / rerank / search
mistral-ocr-4-0 & -latest: 1|10|20|60|80|500 RPM · mistral-ocr-2512: 1|10|20|30|50|60 · omni-moderation-*: 3/10K|10/10K|20/20K|50/50K|75/250K|250/2M · text-moderation-*: x|x|250/500K|500/1M|1K/2M|1500/4M · cf.llama-guard-3-8b: 1/40K|250/450K|500/800K|750/1.2M|1K/2M|1500/4M · cohere-rerank-v4.0-fast/pro, cohere.rerank-v3-5: 3|25(50 v3.5)|50(100)|100(150)|250|500 · semantic-ranker-*: 3|50|100|150|250|500 · qwen3-rerank: 3/40K|250/1M|750/5M|1500/10M|3500/20M|5K/100M · search tools (serper, firecrawl, tavily(-advanced), dataforseo, exa_ai, parallel_ai(-pro)): 3|25|50|75|100|150 RPM · perplexity-search: 3|25|50|75|500|1500.

## Practical use
- Tier 0 is for trials: chat models allow ~1–3 RPM, 10–40K TPM; many frontier models (Claude 4.x/5.x, o-series, gpt-5-pro, grok-4) are **not available below T1/T2/T3** (`x`). Opus-/Fable-class Claude needs T2 for Fable 5.1.
- The same model family can differ a lot per row (e.g. `gemini-flash-latest` vs `gemini-3.8-flash`); size per exact id. Limits are per organization+model (guides/rate-limits.md).
- For capacity planning use ≤50–75% of the limit; TPM counts input+output tokens of the request estimate.
