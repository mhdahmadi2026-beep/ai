# Google (Gemini / Gemma) provider page (docs: /fa/providers/google)

Two access modes: OpenAI-compatible (`/v1/chat/completions`, `base_url=…/v1`) or native Google GenAI SDK (`/v1beta`, base URL `https://api.avalai.ir` no `/v1` — see api-reference/v1beta.md). Gemini-specific (non-OpenAI) settings via OpenAI SDK go in `extra_body={"generationConfig": {…}}` (e.g. `thinkingConfig.thinkingLevel`, `imageConfig`). **Images for Gemini must be base64 data URLs, not external URLs.** Verify ids vs 10-deprecations.md (Gemini 1.5/2.0, Gemma 3, imagen removed; `gemini-2.5-flash-preview-*`, `gemini-2.0-flash-lite` removed).

## Text/multimodal Gemini models (USD / 1M tokens)
| model | ctx in / out | in | cached | out | notes |
|---|---|---|---|---|---|
| `gemini-3.8-flash` | (1M-class) | promo **0.75** (until 2026-12-31 = 1405-10-10) then 1.50 | promo 0.075 / then 0.15 | promo 3.75 / then 7.50 | newest Flash; long-horizon coding, agents, multi-step reasoning, tool loops; endpoints `v1beta`, chat, messages, responses **partial**; `gemini-flash-latest` → this (news 2026-09-03) |
| `gemini-flash-latest` | | same as 3.8 Flash | | | auto-updating alias; pin `gemini-3.8-flash` for reproducibility |
| `gemini-3.7-flash` | 1,048,576 / 65,536 | promo 0.75 → 1.50 | 0.075 → 0.15 | 3.75 → 7.50 | Aug 2026; coding, agents, web dev, doc intelligence; text/image/video/audio/PDF in; thinking, functions, structured output, code execution, caching, file search, Search grounding, URL context (news 2026-08-14) |
| `gemini-3.5-flash` | 1,048,576 / 65,536 | 1.50 | 0.25 | 9.00 | May 2026; audio in 1.00 (cached 0.50) / audio out 1.00; cutoff Jan 2025; `thinkingLevel` low/medium/high via `extra_body={"generationConfig":{"thinkingConfig":{"thinkingLevel":"high"}}}`; benchmarks (provider): Terminal-bench 2.1 76.2%, SWE-Bench Pro 55.1%, MCP Atlas 83.6% |
| `gemini-3.1-pro-preview` | 1M / 64K | 2.00 (>200K 4.00) | ctx-storage 0.825/1.00 | 12.00 (>200K 18.00) | audio in 7.00 (cached 1.50), audio out 7.00; Feb 2026; HLE 44.4%, ARC-AGI-2 77.1%, GPQA 94.3% |
| `gemini-3.1-flash-lite` (+ `-preview` alias) | 1,048,576 / 65,536 | 0.25 | 0.025 | 1.50 | audio in 0.50 / cached 0.05 / out 1.50; cheapest Gemini 3: translation, transcription, extraction, doc summarization, model routing; Batch, context caching, code exec, file search, Search grounding, structured outputs, thinking, URL context |
| `gemini-3-flash-preview` | 1,048,576 / 65,536 | 0.50 | 0.25 | 3.00 | audio in 1.50 / cached 0.50 / out 1.50; legacy → prefer 3.5 flash / 3.1 flash-lite |
| `gemini-2.5-pro` | 1M / 65,536 | 1.25 (>200K 2.50) | ctx storage 0.31/0.625 + 4.50 per 1M-token-hour | 10.00 (>200K 15.00) | thinking param |
| `gemini-2.5-flash` (listed as `gemini-2.5-flash-preview-05-20`) | 1M / 8,192(sic) | 0.15 (audio 1.00) | 0.0375 (audio 0.25) + 1.00/1M-token-hr | no-think 0.60 / think 3.50 | `thinking_budget` only for 2.5 Flash: `extra_body={"thinking":{"type":"enabled","budget_tokens":2000}}`; `budget_tokens:0` disables thinking |
| `gemini-2.5-flash-preview-09-2025` | 1M / 8,192 | 0.30 (audio 1.00) | 0.15 (audio 0.25) | 2.50 | ⛔ removed per deprecations |
| `gemini-flash-lite-latest` → `gemini-2.5-flash-lite-preview-09-2025` | 1M / 8,192 | 0.10 | 0.05 | 0.40 | cheapest at scale |
| `gemini-robotics-er-1.5-preview` | ≈2.5 Flash / 8,192 | 0.30 (audio 1.00) | 0.15 / 0.25 | 2.50 | embodied reasoning: object detection, spatial reasoning, trajectories; points `[{"point":[y,x],"label":…}]` normalized 0–1000; native v1beta full, chat partial (image via content array); news 2025-10-28; example `http_options={"api_version":"v1beta","url":…}` — real SDK key is `base_url` |
Promo prices valid until 2026-12-31 (Jalali 1405-10-10).

## Image models (Nano Banana) — via chat (`modalities:["image","text"]`) or native; see images.md
| model | alias | notes | price |
|---|---|---|---|
| `gemini-3-pro-image` (stable alias; preview alias exists) | Nano Banana Pro | pro assets, Persian text rendering, search-grounded, up to 4K | in $2.00/1M (text) + image in ~0.067/image; out text $12/1M, **$0.134/image 1K–2K, $0.24 4K** (1120/2000 tokens); ctx storage 0.50 |
| `gemini-3.1-flash-image` | Nano Banana 2 | high-volume, 512 px–4K, aspect ratios incl. 4:1/1:4/8:1/1:8, image-search grounding (3.1 Flash exclusive) | in text/image $0.50, cached 0.25; out text $3, image $60/1M; **$0.0672 (1K–2K), $0.101 (2K–4K), $0.151 (4K)** per image |
| `gemini-3.1-flash-lite-image` | Nano Banana 2 Lite | stable; sub-2 s; **1K only**; 14 aspect ratios; function calling; SynthID+C2PA watermark; ctx 65,536 in/4,096 out | in $0.25 (cached 0.05); out text 1.50, image $30/1M; **$0.0336/image 1K (1,120 tokens)** |
| `gemini-2.5-flash-image` | Nano Banana | stable (`-preview` deprecated); 32,768 in/out; only `aspectRatio` in `imageConfig`; cutoff Jun 2025 | in 0.30; out text 2.50, image $30/1M |
`extra_body={"generationConfig":{"imageConfig":{"aspectRatio":"16:9","imageSize":"2K"}}}`; result at `response.choices[0].message.images[i]["image_url"]["url"]` (data URL → base64 decode). Guides: fa/examples/{advanced_gemini_image_generation, generate_images_with_nano_banana_series, generate_images_with_gemini_2_5_flash}.
**Imagen removed** (mapping): `imagen-4.0-ultra-generate-001`→`gemini-3-pro-image`; `imagen-4.0-generate-001`/`-fast`→`gemini-3.1-flash-image`; `imagen-3.0-*`→`gemini-3.1-flash-lite-image` (news 2026-09-04 migration guide).

## Video — Veo 3.1 (see videos.md; verify live status)
`veo-3.1-generate-001` ($0.40/s) and `veo-3.1-fast-generate-001` ($0.15/s): ≤8 s (also 4, 6), 720p/1080p (1080p 16:9 only), 16:9 & 9:16, native audio, ≤3 reference images, video extension. `client.videos.create(model=…, prompt=…, seconds="8", size="1920x1080")`; `input_reference=open(...)`. Guide fa/guides/generate-videos-using-veo; news 2025-11-18.

## Audio: Gemini 3.8 TTS
`gemini-3.8-flash-tts` (creative, expressive, accents, multi-speaker; **130 languages incl. Persian**) / `gemini-3.8-flash-lite-tts` (throughput; **101 languages**; replaces `gemini-3.1-flash-tts-preview` at scale). Text in, audio out; input cap 8,192 tokens, output 16,384. Paths: `/v1beta/models/{m}:generateContent` (per-part `speechMetadata{speaker,style}`), `/v1/chat/completions`, `/v1/audio/speech`. **Not** `/v1/text:synthesize`. Extended Voice Library / voice design / replication are Google features, not AvalAI routes. Native sync response default **WAV `audio/wav`** (older PCM default): decode by `inlineData.mimeType` — wav as-is; `audio/L16` → 24 kHz mono 16-bit wrapper. Chat audio: `modalities:["text","audio"], audio:{"voice":"Zephyr","format":"pcm16"}` → `choices[0].message.audio.data` base64 raw PCM16 (24 kHz) — not mp3/wav. `/v1/audio/speech`: `voice:{"name":"Zephyr","languageCode":"en-US"}`, `response_format:"wav"`. Voices: Zephyr bright, Puck upbeat, Kore firm, Charon informative; multi-speaker config requires each turn's `speaker` to match `speakerVoiceConfigs`; don't put style/speaker labels in spoken text; `<laugh>`, `<sigh>`, `<short pause>` tags for events only. Don't send thinkingConfig, tools, image/audio input. Migration from 3.1/2.5 TTS: change model AND path/body (renaming isn't enough). Guide fa/guides/text-to-speech#migrate-to-gemini-38-tts; Google docs ai.google.dev/gemini-api/docs/speech-generation.
Legacy **Gemini 2.5 TTS** (`gemini-2.5-flash-tts` in 0.50/cached 0.25/out audio 10.00 per 1M; `gemini-2.5-pro-tts` 1.00/0.50/20.00; 900 bytes per text field/1800 combined(sic vs 4000 on v1-text-synthesize page); 30+ voices, 100+ languages; 32 tokens/s audio): endpoints `/v1/chat/completions`, `/v1/audio/speech` (OpenAI voice `alloy`→Kore), `/v1/text:synthesize` (Vertex-native; not on v1beta). See v1-text-synthesize.md. Preview TTS ids `gemini-2.5-*-preview-tts` also exist.

## Tools on Gemini (OpenAI endpoint; tools passed in Gemini shape)
- **Function calling:** `tools=[{"functionDeclarations":[…]}]` (Gemini shape) even on chat endpoint per page.
- **Code execution:** `tools=[{"codeExecution":{}}]` — Python sandbox, 30 s/run, ≤5 retries, ~2 MB text/CSV input, matplotlib plots; **no extra fee** beyond tokens; **no other tool alongside**.
- **Google Search:** `tools=[{"googleSearch":{}}]` (+ `{"googleSearch":{"detail_level":"high"}}` — low/medium/high context size); results carry grounding sources + search suggestions; price **$25–50 per 1,000 calls** by model/level; native v1beta returns full `groundingMetadata` (see v1beta.md).
- **URL context** (experimental): `tools=[{"urlContext":{}}]`; models: 3.5-flash, 3.1-pro-preview, 3.1-flash-lite(+preview), 3-flash-preview, 2.5-pro, 2.5-flash; ≤20 URLs/request; best on standard web pages; more tokens; can combine with Google Search.
- Compatibility: code execution excludes all other tools; function declarations alone; Google Search only combines with URL context.
- **Structured output:** `response_format={"type":"json_object"}` supported.
- Multimodal: video via `video_url`; bounding boxes `[ymin,xmin,ymax,xmax]` normalized 0–1000; Gemini 2.5 segmentation masks (base64 PNG); multi-image.

## Native Google SDK (`/v1beta`; see v1beta.md)
Python `genai.Client(api_key, http_options={"base_url":"https://api.avalai.ir"})`; JS `httpOptions:{apiVersion:"v1beta", baseUrl}` (page snippets have a stray `}`); Go `genai.NewClient(ctx, &genai.ClientConfig{APIKey, BaseURL})`. Chat: `client.chats.create(model)`; streaming `generate_content_stream`; `system_instruction` (not role-based); thinking `thinking_budget=0` disables on 2.5 Flash. Safety settings: categories HARASSMENT, HATE_SPEECH, SEXUALLY_EXPLICIT, DANGEROUS_CONTENT; thresholds OFF, BLOCK_NONE, BLOCK_ONLY_HIGH, BLOCK_MEDIUM_AND_ABOVE, BLOCK_LOW_AND_ABOVE, UNSPECIFIED; default for Gemini 2.5/3 = `OFF`; response `promptFeedback.blockReason`, `candidate.finishReason=="SAFETY"` + `safetyRatings`; lax settings may be reviewed (Google terms). Limitations: Gemini only; base URL without `/v1`; `/v1beta/models/{m}:{method}`.

## Embeddings (see embeddings.md)
- `gemini-embedding-2` (alias `gemini-embedding-2-preview`): first multimodal embedding (text/image/video/audio/PDF in one space; 100+ languages); max 8,192 tokens; dims 128–3072 (default 3072; recommended 768/1536/3072); in text $0.20 (cached 0.02), image $0.45, audio $6.50, video $12.00, out $0.15 per 1M; limits 6 images, 180 s audio, 120 s video (32 frames), 6 PDF pages; task via prompt prefix `task: search result | query: …`; endpoints `/v1/embeddings` and `v1beta/models/gemini-embedding-2:embedContent`; MRL auto-renormalizes truncated; multi-part input → ONE aggregated embedding (use separate requests/Batch for per-input).
- `gemini-embedding-001`: 2,048 tokens; dims 128–3072 (default 3072; recommended 768/1536/3072); in $0.15, out $0.075; 8 task types; normalize manually when <3072.
- `gemini-embedding-exp-03-07` experimental (don't use in prod).

## Gemma (open weights)
Gemma 4 (from Gemini 3 research; 128K ctx; text/image/audio in; 140+ languages; thinking mode, function calling, agentic; sizes 26B A4B MoE, 31B dense, E2B, E4B): `gemma-4-26b-a4b-it` (in 0.13 / cached 0.013 / out 0.40; chat + responses) — Arena AI 1441, MMMLU 82.6, AIME 2026 88.3, LiveCodeBench v6 77.1, GPQA 82.3; `gemma-4-31b-it` (0.14 / 0.014 / 0.40; chat) — Arena 1452, MMMLU 85.2, AIME 2026 89.2, LCB v6 80.0, GPQA 84.3, τ2-bench retail 86.4. Gemma 3 (`gemma-3-1b-it` text-only, `gemma-3-4b-it`, `-12b-it`, `-27b-it`, `gemma-3n-e4b-it`; 128K; image+text) — ⛔ Gemma 3 removed per deprecations.

## Selection
Flash 3.5 flagship-flash for reasoning/coding/agents; 3.1 Pro for deepest reasoning; 3.1 Flash-Lite for cost/latency; ≥1M context for 3.5/3.1/3/2.5; Pro 64K output; (page table: reasoning → 3.1 Pro; agentic/chat → 3.5 Flash; docs → 3.5 Flash/3.1 Pro; multimodal → 3.5 Flash; high volume → 3.1 Flash-Lite). Names: aliases `gemini-3.1-pro`, `gemini-3-flash`, `gemini-2.5-pro` vs snapshots `gemini-3.1-pro-preview`, `gemini-3-flash-preview`. Best practices: precise prompts, `system` role, interleave multimodal instructions, temperature/top_p.

## Source defects
Page repeatedly swaps Google ids for `gpt-5.6-luna` in "Responses equivalents"; `gemini-2.5-flash` heading lists `…preview-05-20` id; Robotics example uses `"url"` instead of `base_url`; v1beta doc says `Veo` price vs videos page (veo not in videos.md pricing) — check pricing; 2.5-flash max output 8,192 looks stale vs 65,536.
