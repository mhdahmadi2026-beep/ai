# مدل‌های منسوخ شده / Deprecations — https://docs.avalai.ir/fa/deprecations
Last updated on the page: **1405-07-08 (2026-09-30)**. Covers provider deprecation timelines, models removed from AvalAI, and compatibility routing exceptions. **A provider's deprecation announcement alone does not mean the AvalAI ID is gone.** Check live `GET /v1/models` (or `/public/models`) before relying on any ID.

## ⚠ DeepSeek compatibility routing (as of 2026-09-30)
- DeepSeek IDs in AvalAI were **not** deprecated/disabled in favor of `deepseek-v4.1-flash` / `deepseek-flash`; AvalAI keeps them for compatibility **but does NOT process requests with the original models.**
- Requests using **any** DeepSeek ID — incl. `deepseek-v4-pro`, `deepseek-v4-flash`, `deepseek-chat`, `deepseek-reasoner`, `deepseek.r1-v1:0`, `deepseek-r1-0528`, `deepseek-v3-0324` — are currently **routed to `deepseek-v4.1-flash`**. Alias `deepseek-flash` also → `deepseek-v4.1-flash`.
- **Recommendation:** in integrations use only `deepseek-v4.1-flash` or `deepseek-flash`.
- Behaviour may change: a future DeepSeek release may repoint the compat routes and `deepseek-flash`; continued routing to V4.1 Flash is not guaranteed; using an old ID doesn't preserve the original model's behavior/capabilities/price. Check this page + `/v1/models`.
- Provider vs AvalAI difference: DeepSeek's retirement notice for `deepseek-chat`/`deepseek-reasoner` was **2026-07-24 15:59 UTC** — does NOT mean AvalAI disabled them. The 2026-09-30 policy supersedes the earlier page advice about routing to V4 Pro/V4 Flash and listing DeepSeek IDs as unavailable on 2026-09-04.

## ⚠ GPT-5 `-chat` tags are GONE (errors, not auto-routed)
| Removed | Use instead |
|---|---|
| `gpt-5-chat` | `gpt-5` |
| `gpt-5-chat-latest` | `gpt-5` |
| `gpt-5.1-chat` | `gpt-5.1` |
| `gpt-5.2-chat` | `gpt-5.2` |
| `gpt-5.3-chat` | `gpt-5.3` |
Requests with these IDs **fail**; drop the `-chat` suffix. OpenAI's tables below suggest `gpt-5.6-sol/terra/luna` for many old models — those are provider suggestions, not the newest-GPT list; verify the replacement exists in AvalAI.
> **Cross-reference conflict:** 07-service-tiers lists `gpt-5.2-chat` as flex-supported and 06 shows `gpt-5.4-pro`, etc.; but `gpt-5.2-chat` is removed here → treat `gpt-5.2-chat` as unavailable.

## Lifecycle (OpenAI definitions)
- **Legacy**: no active updates; plan migration. **Deprecated**: retirement announced with shutdown/sunset date. **Shut down**: requests no longer served after the date.
- OpenAI notice: ≥6 months for general public models; ≥3 months for specialized public versions (chat snapshots, Codex, deep research) unless safety/compliance requires shorter; preview models can be ~2 weeks. Don't use previews for critical production unless you can migrate quickly. Other AvalAI providers may differ. Source: https://developers.openai.com/api/docs/deprecations
> If OpenAI suggests a replacement not yet active in AvalAI, pick the nearest supported option via /fa/guides/model-selection, provider page or `/v1/models` — don't hard-code a non-existent model.

## Migration checklist
1. Inventory: search code, prompts, config, queues, eval fixtures, saved presets for deprecated IDs/aliases. 2. Pick supported replacement: prefer **stable, non-preview** models; avoid `-latest` aliases for regression/regulated workloads. 3. Parallel evals: quality, latency, cost, context usage, tool behavior, structured-output validity, safety. 4. Controlled rollout (feature flag / per-customer config) with quick rollback. 5. Monitor cutover: alerts for `404`, `model_not_found`, provider-routing errors, cost shifts, unexpected `usage` differences.
**Naming best practice:** use stable (non-preview) model names when available (e.g. `gemini-2.5-flash-image-preview` → `gemini-2.5-flash-image`); migrate off previews ASAP.

## OpenAI deprecations (checked 2026-09-30; provider-side, availability via AvalAI may differ)
### Upcoming / recent
**2026-09-11 notice — `gpt-5.4-cyber`**: shutdown **2026-10-01** (1405-07-09). Replacement: most capable cyber model you have access to.
**2026-08-26 notice — transcription models**, shutdown **2027-02-26 (1405-12-07)**: `whisper-1`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize` → `gpt-live-transcribe` or `gpt-transcribe` (guide: https://developers.openai.com/api/docs/guides/transcription). ⚠ But 03-ai-workflows says **don't use `gpt-transcribe`/`gpt-live-transcribe` on AvalAI** — verify availability first.
**2026-07-20 notice — legacy audio/realtime/transcribe families**, shutdown **2027-01-20 (1405-10-30)**: `gpt-realtime`→`gpt-realtime-2.1`; `gpt-audio`→`gpt-audio-1.5`; `gpt-4o-audio`→`gpt-audio-1.5`; `gpt-4o-realtime`→`gpt-realtime-2.1`; `gpt-realtime-mini`→`gpt-realtime-2.1-mini`; `gpt-audio-mini`→`gpt-audio-1.5`; `gpt-4o-mini-realtime`→`gpt-realtime-2.1-mini`; `gpt-4o-mini-audio`→`gpt-audio-1.5`; `gpt-4o-mini-transcribe-2025-03-20`→`gpt-4o-mini-transcribe-2025-12-15`.
**2026-06-11 notice — GPT-5 & o3 snapshots**, shutdown **2026-12-11**: `gpt-5-2025-08-07`→`gpt-5.6-sol`; `gpt-5-mini-2025-08-07`→`gpt-5.6-terra`; `gpt-5-nano-2025-08-07`→`gpt-5.6-luna`; `gpt-5-pro-2025-10-06`→`gpt-5.6-sol` + `reasoning.mode: pro`; `o3-2025-04-16`→`gpt-5.6-sol`; `o3-pro-2025-06-10`→`gpt-5.6-sol` + `reasoning.mode: pro`.
**2026-06-03 — Reusable prompt objects** (dashboard + API `v1/prompts`): deprecated 3 Jun 2026; **stops 30 Nov 2026**. Move prompt content into app code (migration guide: https://developers.openai.com/api/docs/guides/prompting/migrate-from-prompt-object).
**2026-06-03 — Evals platform (incl. graders)**: deprecated 3 Jun 2026; existing evals read-only **31 Oct 2026**; dashboard & API stop **30 Nov 2026**. Migration: Promptfoo (https://developers.openai.com/cookbook/examples/evaluation/moving-from-openai-evals-to-promptfoo).
**2026-06-03 — Agent Builder**: deprecated 3 Jun 2026; stops **30 Nov 2026**; ChatKit stays. Migrate to Agents SDK / ChatGPT Workspace Agents (https://developers.openai.com/api/docs/guides/agent-builder/migrate-from-agent-builder).
**2026-06-02 — GPT Image models**, shutdown **1 Dec 2026**: `gpt-image-1-mini`, `gpt-image-1.5`, `chatgpt-image-latest` → `gpt-image-2.5-sunburst` or `gpt-image-2.5-flare` (example: /fa/examples/generate_images_with_gpt_image).
**2026-05-07 — self-serve fine-tuning access**: 7 May 2026: new fine-tuning/training jobs disabled for orgs that never ran fine-tuning; 2 Jul 2026: disabled for orgs with no inference on a fine-tuned model in last 60 days; **6 Jan 2027**: existing active customers can't create new jobs. Inference on fine-tuned models continues until the base model is deprecated.
**2026-04-22 — legacy GPT snapshots, shutdown 2026-10-23** → replacement:
- `gpt-3.5-turbo-0125`, `gpt-3.5-turbo`, `gpt-3.5-turbo-completions` → `gpt-5.6-terra`
- `gpt-4-0613`, `gpt-4`, `gpt-4-0613-completions`, `gpt-4-completions` → `gpt-5.6-sol`
- `gpt-4-1106-preview` → `gpt-5.6-sol`; `gpt-4-turbo`, `gpt-4-turbo-2024-04-09`, `gpt-4-turbo-completions` → `gpt-5.6-sol`
- `gpt-4.1-nano`, `gpt-4.1-nano-2025-04-14` → `gpt-5.6-luna`; `gpt-4o-2024-05-13` → `gpt-5.6-sol`
- `gpt-image-1` → `gpt-image-2.5-sunburst`/`-flare`; `o1-2024-12-17`, `o1` → `gpt-5.6-sol`; `o1-pro-2025-03-19`, `o1-pro` → `gpt-5.6-sol` + `reasoning.mode: pro`; `o3-mini-2025-01-31`, `o3-mini` → `gpt-5.6-sol`
- `ft-o4-mini-2025-04-16`, `o4-mini-2025-04-16`, `o4-mini` → `gpt-5.6-terra`
- fine-tuned (also 2026-10-23): `ft-gpt-3.5-turbo`→`gpt-5.6-terra`; `ft-gpt-4`→`gpt-5.6-sol`; `ft-gpt-4.1-nano-2025-04-14`→`gpt-5.6-luna`; `ft-babbage-002`, `ft-davinci-002`→`gpt-5.6-terra`

### Past OpenAI deprecations (already shut down)
- **2026-09-24** (notice 2026-03-24): Videos API, `sora-2`, `sora-2-pro`, `sora-2-2025-10-06`, `sora-2-2025-12-08`, `sora-2-pro-2025-10-06` — no replacement.
- **2026-09-28**: `gpt-3.5-turbo-instruct`, `babbage-002`, `davinci-002`, `gpt-3.5-turbo-1106` → `gpt-5.6-terra`.
- **2026-08-26**: Assistants API → Responses + Conversations (https://developers.openai.com/api/docs/assistants/migration).
- **2026-08-10**: `gpt-5.2-chat-latest`, `gpt-5.3-chat-latest` → `gpt-5.6-sol`.
- **2026-07-23**: `computer-use-preview(-2025-03-11)`→`gpt-5.6-terra`; `gpt-4o-mini-search-preview-2025-03-11`, `gpt-4o-search-preview-2025-03-11`→`gpt-5.6-terra`; `gpt-5-chat-latest`, `gpt-5-codex`, `gpt-5.1-chat-latest`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.2-codex`→`gpt-5.6-sol`; `gpt-5.1-codex-mini`→`gpt-5.6-terra`; `gpt-audio-mini-2025-10-06`→`gpt-audio-1.5`; `gpt-realtime-mini-2025-10-06`→`gpt-realtime-2.1-mini`; `o3-deep-research(-2025-06-26)`, `o4-mini-deep-research(-2025-06-26)`→`gpt-5.6-sol`.
- **2026-05-12**: `dall-e-2`, `dall-e-3` → `gpt-image-2`/`gpt-image-1`/`gpt-image-1-mini`. Realtime API beta header `OpenAI-Beta: realtime=v1` → Realtime GA (https://developers.openai.com/api/docs/guides/realtime#beta-to-ga-migration).
- **2026-05-07**: `gpt-4o-realtime-preview` (+`-2025-06-03`, `-2024-12-17`)→`gpt-realtime-1.5`; `gpt-4o-mini-realtime-preview`→`gpt-realtime-mini`; `gpt-4o-audio-preview`→`gpt-audio-1.5`; `gpt-4o-mini-audio-preview`→`gpt-audio-mini`.
- **2026-03-26**: `gpt-4-0314`, `gpt-4-1106-preview`, `gpt-4-0125-preview`, `gpt-4-turbo-preview(-completions)` → `gpt-5` or `gpt-4.1` (*gpt-4.1 for very latency-sensitive, non-reasoning).
- **2026-02-17**: `chatgpt-4o-latest` → `gpt-5.1-chat-latest`. **2026-02-12**: `codex-mini-latest` → `gpt-5-codex-mini` (legacy local shell tool ended too).
- **2025-10-10**: `gpt-4o-realtime-preview-2024-10-01`→`gpt-realtime-1.5`; `gpt-4o-audio-preview-2024-10-01`→`gpt-audio-1.5`.
- **2025-10-27**: `text-moderation-007/-stable/-latest` → `omni-moderation`; `o1-mini` → `o4-mini`. **2025-07-28**: `o1-preview` → `o3`. **2025-07-14**: `gpt-4.5-preview` → `gpt-4.1`.
- **2024-12-18**: `OpenAI-Beta: assistants=v1` → `assistants=v2`. **2024-10-28**: new fine-tuning on `babbage-002`/`davinci-002` → `gpt-4o-mini`.
- **2025-06-06**: `gpt-4-32k`, `gpt-4-32k-0613`, `gpt-4-32k-0314` ($60/$120 per 1M) → `gpt-4o`. **2024-12-06**: `gpt-4-vision-preview`, `gpt-4-1106-vision-preview` ($10/$30) → `gpt-4o`.
- **2024-09-13**: `gpt-3.5-turbo-0613`, `-16k-0613` → `gpt-3.5-turbo`; `gpt-3.5-turbo-0301` → `gpt-3.5-turbo`. **2025-06-06**: `gpt-4-32k-0314` → `gpt-4o`. `gpt-4-0314`: not before 2024-06-13 → `gpt-4o`.
- **2024-01-04**: `/v1/fine-tunes` → `/v1/fine_tuning/jobs`; InstructGPT `text-ada/babbage/curie/davinci-001/002/003` → `gpt-3.5-turbo-instruct`; base `ada/babbage`→`babbage-002`, `curie/davinci`→`davinci-002`, `code-davinci-002`→`gpt-3.5-turbo-instruct`; `text-davinci-edit-001`, `code-davinci-edit-001`, `/v1/edits` → `gpt-4o` / `/v1/chat/completions`; fine-tune base `ada/babbage/curie/davinci` → `babbage-002`/`davinci-002`(`/gpt-3.5-turbo`/`gpt-4o`); first-gen embeddings (`text-similarity-*-001`, `text-search-*-doc/query-001`, `code-search-*-001`, ada/babbage/curie/davinci) → `text-embedding-3-small`.
- **2023-03-23**: Codex `code-davinci-002/001`, `code-cushman-002/001` → `gpt-4o`. **2022-12-03**: `/v1/engines`→`/v1/models`; `/v1/search`, `/v1/classifications`, `/v1/answers` → OpenAI transition guides.

## AvalAI list updates — removed from AvalAI (deprecated 1405-06-13 / 2026-09-04) — no longer available
**Bedrock / Anthropic / Cohere / Meta / OpenAI-OSS:** `anthropic.claude-opus-4-1-20250805-v1:0`, `claude-opus-4-1`; `anthropic.claude-opus-4-20250514-v1:0`, `claude-opus-4`; `anthropic.claude-sonnet-4-20250514-v1:0`, `claude-sonnet-4`; `cohere.embed-english-v3`, `cohere.command-light-text-v14`, `cohere.command-r-plus-v1:0`, `cohere.command-r-v1:0`, `cohere.command-text-v14`; `meta.llama3-1-8b/70b/405b-instruct-v1:0`, `meta.llama3-3-70b-instruct-v1:0`; `mistral.mistral-large-2407-v1:0`; `openai.gpt-oss-20b-1:0`, `openai.gpt-oss-120b-1:0`.
**Stability AI image:** `stability.stable-image-inpaint-v1:0`, `-search-recolor-v1:0`, `-search-replace-v1:0`, `-erase-object-v1:0`, `-remove-background-v1:0`, `-control-sketch-v1:0`, `-control-structure-v1:0`, `-style-guide-v1:0`, `stability.stable-style-transfer-v1:0`, `stability.sd3-5-large-v1:0`, `stability.stable-image-ultra-v1:1`, `stability.stable-image-core-v1:1` (and earlier `stability.sd3-large-v1:0`). Migrate to any image model in live `/v1/models`.
**NVIDIA NIM:** `nvidia_nim.llama-3.2-nv-rerankqa-1b-v2`, `llama-3.2-nemoretriever-300m-embed-v1`/`-v2`, `llama-3.2-nemoretriever-1b-vlm-embed-v1`, `llama-3.2-nv-embedqa-1b-v2`, `llama-3.2-nemoretriever-500m-rerank-v2`, `nv-rerankqa-mistral-4b-v3`, `qwen3-next-80b-a3b-thinking`, `nvidia-nemotron-nano-9b-v2`, `llama-4-scout-17b-16e-instruct`, `llama-3.1-nemotron-ultra-253b-v1`, `eurollm-9b-instruct`, `gemma-3-1b-it`, `bge-m3`.
**Google / image / search / speech / misc:** `models/gemini-2.0-flash-lite`, `gemini-2.5-flash-preview-04-17`, `gemini-2.5-flash-preview-09-2025`; `imagen-4.0-fast-generate-preview-06-06`, `imagen-4.0-generate-001`, `imagen-4.0-ultra-generate-001`, `imagen-4.0-fast-generate-001` (→ use `gemini-3.1-flash-image`); `sora`, `qwq-32b`, `google_pse-search`; `seedream-4-0-250828`, `seedream-4-5-251128`.
**Other OpenAI aliases removed:** `gpt-4o-mini-search-preview`, `gpt-4o-search-preview`, `gpt-4o-mini-tts`; `gpt-5-chat-latest`, `gpt-5-codex`, `gpt-5.1-chat-latest`, `gpt-5.1-codex`, `gpt-5.1-codex-max`, `gpt-5.1-codex-mini`; `gpt-audio-mini`, `gpt-realtime-mini`, `o3-deep-research`, `o4-mini-deep-research`, `gpt-5.2-codex`, `gpt-5.2-chat-latest`, `gpt-5.3-chat-latest`.
**Alibaba / Moonshot / Mistral / Cloudflare / others:** `qwen3-235b-a22b-thinking-250`, `qwen-turbo`, `qwen-turbo-2024-11-01`; `qwen-vl-max`, `qwen-vl-max-2025-08-13`, `qwen-vl-plus`, `qwen-vl-plus-2025-08-15`, `-2025-07-10`, `-2025-01-25`; `mistral-ocr-2505`, `mistral-ocr-2503` (→ `mistral-ocr-4-0`/`mistral-ocr-latest`); `cf.gemma-3-12b-it`.
> **Cross-reference conflicts to watch:** 06-pricing still lists (stale) `qwq-32b`, `qwen-max*`, `seedream-4-5-251128`, `groq.playai-tts*`, `kimi-k2-thinking`(04-libraries lists it), `gpt-5.1-codex-max`, `gpt-5.2-pro`... — those catalog rows may be stale vs this page. **This page + live `/v1/models` win.** 04-libraries/01 examples using `claude-opus-4-7`, `claude-sonnet-4-5` etc. may be affected; `claude-opus-4-1`/`claude-opus-4` are removed.

## Moonshot.ai legacy (deprecated)
`kimi-k2-thinking`, `kimi-k2-0711-preview`, `kimi-thinking-preview`, `kimi-latest-8k/32k/128k`, `moonshot-v1-auto`, `moonshot-v1-8k`, `-32k`, `-128k` and the `-vision-preview` variants (8k/32k/128k). Migrate to a currently supported Moonshot model (/fa/providers/moonshotai) and verify in `/v1/models`.

## ElevenLabs legacy (removed 9 Jul 2026)
| Removed | Replacement |
|---|---|
| `scribe_v1` | `scribe_v2` (speaker diarization, word timestamps, entity detection) |
| `eleven_monolingual_v1` | `eleven_turbo_v2` or `eleven_flash_v2` (English TTS) |
| `eleven_multilingual_v1` | `eleven_multilingual_v2`, `eleven_turbo_v2_5` or `eleven_flash_v2_5` |
(/fa/providers/elevenlabs) ⚠ 06-pricing still lists `scribe_v1`.

## Anthropic Claude 4 (deprecated 15 Jun 2026)
`anthropic.claude-sonnet-4-20250514-v1:0`, `anthropic.claude-opus-4-20250514-v1:0` → `claude-sonnet-4-6`, `claude-opus-4-8` (page's suggested "latest" — newer 5.x IDs exist elsewhere in AvalAI).

## Gemini 2.0 Flash / Flash Lite (retired 1 Jun 2026)
`gemini-2.0-flash`, `gemini-2.0-flash-001`, `gemini-2.0-flash-lite`, `gemini-2.0-flash-lite-001` → `gemini-2.5-flash`, `gemini-2.5-flash-lite`.

## Alibaba Qwen legacy snapshots (retired 13–31 May 2026, UTC+8; calls may error/hang)
Affected (base, `-latest`, dated): `qwen-max`/`-latest`/`-2025-01-25`; `qwen-turbo`/`-latest`/`-2025-04-28`/`-2024-11-01`; `qwen-vl-max`/`-latest`/`-2025-08-13`/`-2025-04-08`; `qwen-vl-plus`/`-latest`/`-2025-08-15`/`-2025-07-10`/`-2025-05-07`/`-2025-01-25`; `qvq-max`/`-latest`/`-2025-03-25`; open-source: `qwen2.5-vl-32b/72b/7b/3b-instruct`, `qwen2.5-7b/14b-instruct-1m`, `qwen2.5-72b/32b/14b/7b-instruct`, `qwen3-0.6b`, `qwen3-1.7b`, `qwen3-4b`.
Migrate: `qwen3.7-max` (→qwen-max), `qwen3.7-plus`, `qwen3.6-plus` (1M-token), `qwen3.6-flash` (→qwen-turbo), `qwen3.6-max-preview`, `qwen3-vl-plus`/`qwen3-vl-flash` (→ qwen-vl-*, qvq-max). /fa/providers/alibaba

## Other provider deprecations
- **Gemini 2.5 Flash Lite preview Sep-2025**: retired 31 Mar 2026 (Gemini API/AI Studio, not Vertex) → `gemini-3.1-flash-lite-preview` (`-latest` alias now points there).
- **`gemini-3-pro-preview`**: retired 9 Mar 2026; `-latest` moved to 3.1 Pro Preview on 6 Mar → `gemini-3.1-pro-preview`.
- **`gemini-2.5-flash-image-preview`**: retired 15 Jan 2026 → `gemini-2.5-flash-image`.
- **Groq PlayAI TTS** (31 Dec 2025): `groq.playai-tts`, `groq.playai-tts-arabic` — requests fail; migrate to another TTS model available in AvalAI.
- **Gemma 3** (11 Jul 2026): `gemma-3n-e4b-it`, `gemma-3n-e2b-it`, `gemma-3-27b-it`, `gemma-3-12b-it`, `gemma-3-4b-it`, `gemma-3-1b-it` → Gemini models e.g. `gemini-2.5-flash`/`gemini-2.5-flash-lite`.
- **Z.AI GLM legacy** (1405-04-06): `glm-5v-turbo`, `glm-5-turbo`, `glm-5`, `glm-4.7-flashx`, `glm-4.7-flash`, `glm-4.7`, `glm-4.6` → `glm-5.2` (flagship; 1M context) — newer `glm-5.3`/`glm-5.3-flash` exist per 06-pricing. ⚠ 06 still lists `glm-5.1`.
- **MiniMax legacy** (1405-04-06): `minimax-m2.1`, `minimax-m2.1-lightning`, `minimax-m2` → `minimax-m3` (1M ctx, native multimodal, MSA, switchable thinking). ⚠ 06 still lists `minimax-m2.5/m2.7`.
- **Google PSE `google_pse-search`** (Apr 2026): migrate to Gemini built-in `google_search` tool (Gemini 3 Flash, 3.1 Pro, 2.5 Pro; /fa/examples/web_search_capabilities) or another `v1/search` provider e.g. `serper-search` (cheapest Google-based; /fa/api-reference/search).
- **Mistral `codestral-2501`** (1405-03-13) → `codestral-latest`.
- **Cloudflare Workers AI** (1405-03-13): `cf.qwen3-embedding-0.6b`, `cf.meta-llama-3-8b-instruct`, `cf.llama-3.1-8b-instruct-awq`, `cf.llama-3.1-8b-instruct-fp8`, `cf.llama-3.1-8b-instruct`, `cf.llama-3-8b-instruct-awq`, `cf.llama-3-8b-instruct`, `cf.gemma-7b-it-lora`, `cf.gemma-2b-it-lora`, `cf.gemma-7b-it`, `cf.llama-3.1-70b-instruct`.
- **Gemini preview/experimental** (1404-08-27): `gemini-2.0-flash-exp`, `gemini-2.0-flash-lite-preview(-02-05)`, `gemini-2.0-flash-thinking-exp(-01-21,-1219)`, `gemini-2.5-flash-lite-preview-06-17`, `gemini-2.5-flash-preview-05-20`, `gemini-2.5-pro-preview-06-05/-03-25/-05-06` → `gemini-3.1-pro-preview`, `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-2.5-flash-preview-09-2025`(also later removed), `gemini-2.5-flash-lite`. Announcement /fa/news/2025-11-18-new-models-gemini-3-pro-kimi-k2-thinking.
- **Gemini image & embedding** (1404-08-06): `gemini-2.5-flash-image-preview`→`gemini-2.5-flash-image`; embeddings `embedding-001`, `embedding-gecko-001`, `gemini-embedding-exp-03-07`, `gemini-embedding-exp` → `text-embedding-004`, `text-multilingual-embedding-002` (page's suggestions; `gemini-embedding-2` exists in 06).
- **BytePlus Seedream** (1405-02-16): `seedream-4-0-250828`, `seedream-4-5-251128` → `seedream-5-0-260128` (CoT reasoning, better prompt optimization, MJ-style, hi-res). /fa/examples/generate_images_with_seedream_4
- **OpenAI (1404-08-06):** `dall-e-3` → `gpt-image-2` (better prompt adherence, multilingual text rendering, both `v1/images/generations` and `v1/images/edits`); `gpt-3.5-turbo` → `gpt-5.6-terra`; `gpt-4`, `gpt-4-0125-preview`, `gpt-4-1106-preview`, `gpt-4-turbo`, `gpt-4-turbo-2024-04-09` → `gpt-5.6-sol`; `o1-preview`, `gpt-4.5-preview` → `gpt-5.6-sol`/`gpt-5.6-terra`. **Don't migrate to `gpt-5-chat`** (unavailable → errors).
- **Claude 3.x on Bedrock** (1404-08-06): `anthropic.claude-3-opus-20240229-v1:0`, `-3-haiku-20240307-v1:0`, `-3-sonnet-20240229-v1:0`, `-3-5-haiku-20241022-v1:0`, `-3-5-sonnet-20240620-v1:0`, `-3-7-sonnet-20250219-v1:0` → `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`.
- **Gemini 1.5 / early (1404-07-06):** `gemini-pro`, `gemini-1.5-pro` (+`-002`,`-001`,`-latest`,`-exp-0801`,`-exp-0827`), `gemini-2.0-flash-exp`, `gemini-exp-1114`, `gemini-exp-1206`, `gemini-1.5-flash-latest`, `gemini-1.5-flash-8b` (+`-exp-0924`, `-exp-0827`), `gemini-1.5-flash-exp-0827` → `gemini-2.5-pro/flash/flash-lite` (2.0 replacements also later retired). Announcement /fa/news/2025-09-27-google-gemini-models-deprecation.

## Migration support
Review current usage → choose replacements per use case → update model names → test thoroughly → monitor performance. Resources: /fa/guides/model-selection · /fa/guides/best-practices · /fa/guides/error-handling · support https://avalai.ir/contact-us-avalai · model details /fa/models/model-details.
Historical deprecations section: "will be updated over time."
