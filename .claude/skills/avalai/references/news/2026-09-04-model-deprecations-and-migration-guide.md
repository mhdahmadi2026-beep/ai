# News 2026-09-04 (1405-06-13): mass model deprecation & migration guide (docs.avalai.ir/fa/news/2026-09-04-model-deprecations-and-migration-guide)

AvalAI retires a broad set of deprecated OpenAI, Google, Anthropic, Stability AI and other models **from 2026-09-04**; requests with the old ids now ERROR. Authoritative full list: `fa/deprecations` (= 10-deprecations.md + live `/v1/models`). Migration = change only `model` (endpoints/request shape unchanged); test quality/latency/cost; pin explicit ids (no `-latest`) for controlled rollouts.

## Mappings (AvalAI's own recommendations)
| Old | New |
|---|---|
| `gpt-5-chat`, `gpt-5-chat-latest`, `gpt-5.2-chat`, `gpt-5.3-chat` | `gpt-5.6-sol` |
| `gpt-5.1-chat` | `gpt-5.6-terra` |
| `gpt-4o`, `gpt-4o-mini` (legacy) | `gpt-5.6-terra` / `gpt-5.6-luna` |
| `imagen-4.0-generate-001`, `-fast-generate-001` | `gemini-3.1-flash-image` (Nano Banana 2) |
| `imagen-4.0-ultra-generate-001` | `gemini-3-pro-image` (Nano Banana Pro) |
| `imagen-4.0-fast-generate-preview-06-06` | `gemini-3.1-flash-lite-image` |
| `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd` | `gpt-audio-1.5` (or Gemini TTS) |
| `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `whisper-1` | `gpt-transcribe` (and/or `gpt-live-transcribe`) |
| `gpt-4o-transcribe-diarize` | `gpt-live-transcribe` |
| `claude-opus-4`, `claude-opus-4-1`, `anthropic.claude-opus-4-20250514-v1:0` | `claude-opus-4-7` |
| `claude-sonnet-4`, `anthropic.claude-sonnet-4-20250514-v1:0` | `claude-sonnet-4-6` |
| Stability `stability.sd3-5-large-v1:0`, `stable-image-ultra-v1:1` | `gemini-3.1-flash-image` or `gpt-image-2` |
| Stability `stable-image-core-v1:1` & other `stability.stable-image-*` | `gemini-3.1-flash-image` |
| DeepSeek `deepseek.r1-v1:0`, `deepseek-r1-0528`, `deepseek-v3-0324` | `deepseek-v4-flash` / `deepseek-v4-pro` |
| Groq `groq.playai-tts(-arabic)` | `gpt-audio-1.5` or Gemini TTS |
| Mistral `codestral-2501`, `mistral-ocr-2503/2505` | `mistral-ocr-4-0` / `mistral-ocr-latest` |
| Alibaba `qwq-32b`, `qwen3-235b-a22b-thinking-2507` | `qwen3.5-plus` / `qwen3-8-max` (⚠ ids look non-standard — verify) |
| Moonshot `kimi-k2-0905` | `kimi-k3` |
| Meta Bedrock `meta.llama2-*`, `meta.llama3-*` | `llama-4-scout-17b-16e-instruct` |
| NVIDIA NIM `nvidia_nim.*` (some), Cloudflare `cf.gemma-3-12b-it`, `cf.qwq-32b` | see live `/v1/models` |
GPT-5.6 family: `gpt-5.6-sol` (hardest coding/analysis/agents; pro mode via `reasoning.mode:"pro"`), `gpt-5.6-terra` (balanced production), `gpt-5.6-luna` (cheap/high volume). Announcement: news/2026-07-10-gpt-5-6-grok-4-5-models-added (not captured). Gemini TTS: `gemini-2.5-pro-tts`/`-flash-tts` named here as available (but Gemini 3.8 TTS pages say 2.5 TTS are being migrated — see providers/google.md).

## Impact on my notes / conflicts resolved
- **STT availability (resolves earlier conflict, partially):** AvalAI's OWN notice names `gpt-transcribe` and `gpt-live-transcribe` as the current replacements, and `whisper-1`/`gpt-4o-*transcribe*` as deprecated → treat the new ids as the intended AvalAI models and the old ones as removed/at risk. The older note in 03-ai-workflows ("do not use gpt-transcribe/gpt-live-transcribe") is stale/contradicted; still confirm via `/v1/models` before shipping. `gpt-live-transcribe` + `diarized_json` + known-speaker refs unverified.
- guides/speech-to-text.md and audio guides still list `whisper-1`/`gpt-4o-*` as usable — those are the deprecated ids.
- `gpt-audio-mini`, `gpt-realtime-mini`, `gpt-4o-mini-tts`, `o3-deep-research` appear in 10-deprecations as removed from AvalAI, yet audio example pages recommend `gpt-audio-mini` → conflict; verify live.
- Replacement `gpt-audio-1.5` for TTS (speech route) supports why pages use it with `/v1/audio/speech`, but it is also the chat-audio model — model/route semantics unclear.

## Defects
Page claims replacement mappings only for "most important" ids; `claude-opus-4-7` is not the newest Claude (5.x exist per environment — check list); Qwen replacement ids `qwen3.5-plus`/`qwen3-8-max` conflict with 10-deprecations (`qwen3.7-*`, `qwen3.6-*`); `fa/pricing.md` link not captured.
