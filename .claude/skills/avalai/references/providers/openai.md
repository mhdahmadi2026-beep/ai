# OpenAI models on AvalAI (docs: /fa/providers/openai)

Large catalog page. **Verify every id against 10-deprecations.md and live `/v1/models`** — several models below are removed/scheduled for shutdown (⛔ marks). Prices USD per 1M tokens. Tiered context pricing: **total input length picks the tier for both input and output**; exactly 272K stays in the lower tier; higher rate applies to the *whole* request, not only the excess.

## Newest flagship families
### GPT-6.1 Sol — `gpt-6.1-sol` (announced 2026-09-30, fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added)
Upgraded Sol: coding, professional docs, reasoning; cheaper than Astra. Max input 922,000 / output 128,000 (separate caps). Text+image in, text out; reasoning, PDF input, function calling, structured outputs, prompt caching; not an image generator. **Access: tier ≥1.** Full on chat/messages/responses. Reasoning: send no extra param initially; `reasoning_effort` (chat) / `reasoning.effort` (responses) only with route-confirmed values; **`none` and `minimal` unsupported**. Price: ≤272K: in $2.00 / cached $0.10 / cache-write $2.50 / out $10.00; >272K: $4.00 / $0.20 / $5.00 / $15.00 (cache read 95% cheaper than uncached; half the cache-read price of GPT-6 Sol). Batch/Flex/Priority/hosted tools need separate confirmation; current Sol routes are not auto-redirected.
### GPT-6 Sol & Luna — `gpt-6-sol`, `gpt-6-luna` (news 2026-09-24)
Sol = budget coding agents, pro analysis, computer use, long conversations; Luna = high-traffic assistants/doc processing, cheapest. `gpt-6-astra` stays most capable. Max input 922,000 / out 128,000; text+image in, text out; reasoning, vision, PDF, functions, structured outputs, caching; full on chat/messages/responses. Not image generators; vision/Responses support does NOT enable hosted `image_generation`.
| model | input len | in | cached | cache-write | out |
|---|---|---|---|---|---|
| `gpt-6-sol` | ≤272K | 2.00 | 0.20 | 2.50 | 10.00 |
| `gpt-6-sol` | >272K | 4.00 | 0.40 | 5.00 | 15.00 |
| `gpt-6-luna` | ≤272K | 0.10 | 0.01 | 0.125 | 0.50 |
| `gpt-6-luna` | >272K | 0.20 | 0.02 | 0.25 | 0.75 |
Cache read = 90% cheaper. On migration re-test prompts, tool loops, reasoning budget, cache usage, 922K input cap; no automatic GPT-5.6 redirect announced.
### GPT-6 Astra — `gpt-6-astra` (news 2026-09-05)
Top flagship: computer use, software engineering, pro work, science, math, cyber, long context. Price in $10 (>272K $20) / cached $1 ($2) / cache-write $12.50 ($25) / out $50 (>272K $75). chat/responses/messages full. Reasoning: start `medium`, `high` for hard tasks. Best for complex agents, repo-scale coding, research, quant analysis, authorized security work.
### GPT-5.6 family (previous gen): `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`
Context 1,000,000 in / 128,000 out; text+image in; chat/responses/messages; effort none (default)/low/medium/high/xhigh/max where supported. Price in/cached/out: Sol 5.00/0.50/30.00 · Terra 2.50/0.25/15.00 · Luna 1.00/0.10/6.00. (This is the id used as `gpt-5.6-luna` in docs examples.)
### GPT-5.5 — `gpt-5.5`
1M in / 128K out; in 5.00, cached 0.50, out 30.00; chat + responses; effort none (default)…xhigh; Terminal-Bench 2.0 82.7%, GDPval 84.9%, OSWorld-Verified 78.7% (provider-reported). Tools: function calling, structured outputs, web search, file search, image gen, computer use, MCP.
### GPT-5.4 family
- `gpt-5.4-pro`: 1.05M in/128K out; in 30, cached 0.30(sic), out 180; **Responses only**, effort medium/high/xhigh; tiers 2–5 only; >272K input → 2× input / 1.5× output; long requests → use background mode.
- `gpt-5.4`: 1.05M/128K; in 2.50, cached 0.25, out 15; chat+responses; effort none…xhigh; >272K → 2× in/1.5× out for whole session.
- `gpt-5.4-mini`: 400K/100K; in 0.75, cached 0.075, out 4.50; chat; effort none/low/medium. 
- `gpt-5.4-nano`: 400K/100K; in 0.20, cached 0.02, out 1.25; chat; effort none/low.
### GPT-5.3 / 5.2 / 5.1 / 5 / codex
- `gpt-5.3-chat`(`-latest`): 128K/16,384; 1.75/0.175/14.00; chat+responses. (⛔ per deprecations, GPT-5 `-chat` ids removed — verify.)
- `gpt-5.3-codex`: 512K in/150K out; 1.75/0.175/14; **responses only**; temperature fixed 1.0; cutoff 2026-01-15.
- `gpt-5.2`: 400K/128K; 1.75/0.175/14. `gpt-5.2-pro`: 400K/128K; 21/168; Responses only; tiers 2–5; effort medium/high/xhigh; background mode. `gpt-5.2-codex`: 400K/128K; 1.75/0.175/14; chat+responses+realtime.
- `gpt-5.1`: 400K/128K; 1.25/0.125/10. `gpt-5.1-chat`; `gpt-5.1-codex` & `gpt-5.1-codex-mini` (0.25/0.025/2.00) **Responses only**; `gpt-5.1-codex-max` 1.25/0.125/10 (flagged stale in deprecations cross-refs).
- `gpt-5`: 400K/128K; 1.25/0.125/10; `gpt-5-mini` 0.25/0.025/2.00; `gpt-5-nano` 0.05/0.005/0.40; `gpt-5-pro` 15/120 (272K out; Responses only; tiers 2–5); `gpt-5-chat-latest` ⛔; `gpt-5-codex` 1.25/0.125/10.
### o-series & deep research
- `o3` 200K/100K; 10/40 · `o3-pro` 15/60 · `o4-mini` 1.10/4.40 · `o1` 15/60 · `o1-mini` 1.10/4.40 (128K/65,536).
- `o3-deep-research` (10 / cached 2.50 / 40) and `o4-mini-deep-research` (2 / 0.50 / 8): **Responses only and require a tool** (`web_search`, optional `filters.allowed_domains`; `user_location` NOT supported for deep-research models). Use background mode.
- GPT-5/o3 snapshots shutdown 2026-12-11 (deprecations).
### GPT-4 family
`gpt-4.1` (1,047,576 in/32,768 out; 2/8), `gpt-4.1-mini` 0.40/1.60, `gpt-4.1-nano` 0.10/0.40; `gpt-4o` (128K/16,384; 2.50/10), `gpt-4o-mini` 0.15/0.60; search-preview chat models `gpt-4o-search-preview`, `gpt-4o-mini-search-preview` (50 RPM / 100K TPM; use these for web search in Chat Completions); `gpt-4-turbo` (128K/4,096; 10/30 — page's example mistakenly uses `gpt-4.1`); `gpt-3.5-turbo` (16,385/4,096; 1.50/2.00); `gpt-4.5-preview` ⛔ deprecated.

## Open-weight (Apache 2.0; configurable effort low/medium/high; full CoT; fine-tunable upstream — not on AvalAI)
`gpt-oss-120b` (Azure AI; 131,072/131,072; 0.30/2.50), `openai.gpt-oss-120b-1:0` (AWS Bedrock; 0.15/0.60), `openai.gpt-oss-20b-1:0` (Bedrock; 0.07/0.30).

## Images (see images.md)
`gpt-image-2.5-flare` (default fast) / `-sunburst` (pro precision): in text $5, image $8, cached text 1.25, cached image 2, image out $30; est. output per 1024² low $0.00588 … max $0.21072. `gpt-image-2` edit billing token-based (see images.md). `gpt-image-1.5` (in text 5, cached 2, image in 8, image out 32), `gpt-image-1` (sizes 1024x1024/1024x1792/1792x1024; page example uses `quality="hd"` which GPT Image doesn't accept — use low/medium/high), `gpt-image-1-mini` (tier 3–5; $0.011/0.042?/0.036 per image — medium priced above high in source: typo; tokens in 5/cached 1.25/out 40) — ⛔ gpt-image-1/1-mini/1.5 shutdown 2026-12-01.

## Video (⛔ shut down 2026-09-24 — see videos.md)
`sora-2` ($0.10/s; 720x1280, 1280x720), `sora-2-pro` ($0.30/s; $0.50/s for 1024x1792/1792x1024); `/v1/videos` only. Page example passes `seconds=4` integer — API wants string.

## Embeddings (see embeddings.md)
`text-embedding-3-large` (3072, 8191 tok, $0.13), `text-embedding-3-small` (1536, $0.02), `text-embedding-ada-002` (1536, $0.10; legacy).

## Audio (see audio.md)
- `gpt-audio-1.5` (256K ctx, out 32,768; cutoff 2026-02-01; text in 2.50 / cached 1.25 / text out 10; audio in 32 / out 64) ids `gpt-audio-1.5`, `-2026-02-15`; `gpt-audio` (128K/16,384; same prices; `-2025-08-28`); `gpt-audio-mini` (0.60/0.30/2.40; audio in 10 / out 20; `-2025-10-06`); legacy previews `gpt-4o-audio-preview`, `gpt-4o-mini-audio-preview`. Formats mp3/wav/pcm16/opus/aac/flac; voices alloy/echo/fable/onyx/nova/shimmer (+ more). ⛔ `gpt-audio*` shutdown 2027-01-20. For Responses text flow the page uses `gpt-audio` (inconsistent with chat-only audio).
- STT: `whisper-1` ($0.006/min, ≤25 MB), `gpt-4o-transcribe`, `gpt-4o-mini-transcribe` (500 RPM/200K TPM), `gpt-4o-transcribe-diarize` (text in 2.50, audio in 6.00, cached 1.50, out 10.00; response_format `verbose_json`/`diarized_json`, segments with `speaker`; ~15 s per 10 min audio; 100+ languages). (Page text is garbled: the diarize section is interleaved inside the text-embedding-3-small block, which has price `$0.02`.)
- TTS: `tts-1` ($15/1M chars), `tts-1-hd` ($30/1M chars), `gpt-4o-mini-tts`.

## Moderation (free): `omni-moderation-latest`, `text-moderation-latest` (see moderation.md).

## Hosted web search (Responses `web_search`; guide fa/guides/tools-web-search)
Types: non-reasoning (fast), agentic with reasoning models (search/open_page/find_in_page), deep research (hundreds of sources; minutes; use background). Config: `tools:[{"type":"web_search"}]`; `filters.allowed_domains` (≤20; pass bare domains — the page's markdown-link domains like `[www.who.int](https://www.who.int)` are a render bug); `user_location{type:"approximate",country,city,region,timezone}` (not for deep research); `include:["web_search_call.action.sources"]`; `tool_choice:"auto"`, `reasoning:{effort}`. Response: `web_search_call` item (`action`: search/open_page/find_in_page) + `message` with `output_text.annotations[url_citation{start_index,end_index,url,title}]`. Aliases: `web_search` (GA), `web_search_preview` (older). In Chat Completions use `gpt-4o-search-preview`/`gpt-4o-mini-search-preview`. Limits: not on `gpt-5` with minimal reasoning or `gpt-4.1-nano`; same tiered rate limits as underlying model; 128K context cap even for gpt-4.1(-mini). (Deprecations: hosted tool availability per route/account.)

## Model-choice cheat sheet (page)
Reasoning/research: GPT-5/o3/o4-mini/GPT-4o · chat/content: GPT-5-chat/mini · code: GPT-5-chat/GPT-4.1 · high volume: GPT-5 mini/4.1 mini · vision: GPT-5 Chat/4.1/5 mini · images: GPT Image 2.5 Flare (default) / Sunburst · embeddings: 3-small (balanced) / 3-large (best) · STT: Whisper. (Older picks; prefer GPT-6.x/5.6/5.5 where available.)

## Versioning
Aliases (`gpt-4o`, `gpt-5`, …) vs dated snapshots (`gpt-4o-2024-08-06`, `gpt-5-2025-08-07`, `o3-2025-04-16`, `gpt-4.1-2025-04-14`, `o1-2024-12-17`, …) — pin snapshots for stability; `dall-e-3` listed but ⛔ not an AvalAI-current image model. Full list: fa/models/model-details.

## Source defects to remember
- Code samples for Responses-only models (`gpt-5.1-codex`, `-mini`) POST `messages` and read `result["choices"]…` — wrong; use `input` and `output_text`/`output[]`.
- Several "Responses equivalent" blocks swap in `gpt-5.6-luna` or the wrong prompt; ignore.
- GPT-5.5 sample actually calls `gpt-5.6-luna`.
- `gpt-5.4-pro` cached price $0.30 (vs input $30) looks like a typo (expect $3.00).
- GPT-5.2/5.1 etc. may be listed here although deprecations remove/replace them (e.g. `gpt-5.2-chat`); `/v1/models` decides.
