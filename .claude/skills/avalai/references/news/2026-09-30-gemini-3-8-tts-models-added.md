# News 2026-09-30 (1405-07-08): Gemini 3.8 Flash & Flash-Lite TTS added (docs.avalai.ir/fa/news/2026-09-30-gemini-3-8-tts-models-added)

Model detail lives in `../providers/google.md` (TTS section) and `../guides/text-to-speech.md`; this file keeps the news-specific facts.

- `gemini-3.8-flash-tts` (creative narration, audiobooks, accents, multi-turn voice identity; 130 languages incl. Persian) · `gemini-3.8-flash-lite-tts` (high volume, voice-agent pipelines, single-speaker daily speech; 101 languages incl. Persian). Text in → audio out. Lite throughput/latency claims are provider guidance, not AvalAI measurements.
- AvalAI routes ONLY: native `/v1beta/models/{m}:generateContent`, `/v1/chat/completions`, `/v1/audio/speech`. NOT Responses, Messages, `/v1/text:synthesize`, Live, Interactions; no voice library/design/cloning; upstream Batch/Flex/Priority ≠ available. Google's serving caps 8,192 in / 16,384 out tokens (not an AvalAI quota).
- Price (USD / 1M tokens; input & cached = text tokens, output = AUDIO tokens, not seconds):

| model | input | cached | audio out | period |
|---|---:|---:|---:|---|
| flash-tts | 0.50 | 0.125 | 9.00 | promo 2026-09-30 → 2026-12-31 (1405-10-10) |
| flash-lite-tts | 0.50 | 0.125 | 6.00 | promo |
| flash-tts | 1.00 | 0.25 | 18.00 | standard from 2027-01-01 |
| flash-lite-tts | 1.00 | 0.25 | 12.00 | standard |

- Migration (from `gemini-3.1-flash-tts-preview`, `gemini-2.5-{flash,pro}[-preview]-tts`): Lite for throughput, Flash for creative; change endpoint+body, not only the id (no auto-redirect). Treat input as verbatim transcript — no "Say cheerfully:"/"Speaker 1:" in text; use per-part `speechMetadata{speaker,style}` (camelCase); every multi-speaker part's `speaker` must match a configured speaker; tags `<laugh>`,`<sigh>`,`<short pause>` for momentary events only.
- Native response default = **WAV `audio/wav` with RIFF header** (old = headerless PCM): check `inlineData.mimeType`; write WAV bytes as-is, wrap only `audio/L16` (24 kHz mono s16); never add a second header; reject unknown mime.
- Chat: `audio.format` (e.g. `pcm16`) → decode only `choices[0].message.audio.data`; Speech: `response_format` (mp3 example works with `voice:{"name":"Zephyr","languageCode":"en-US"}`). `gemini-3.1-flash-tts-preview` supports ONLY PCM16 → send `response_format:"pcm"`, convert with `ffmpeg -f s16le -ar 24000 -ac 1 -i in.pcm out.mp3` (renaming .pcm→.mp3 doesn't convert).
- Source-page honesty: examples verified only locally, NOT run against the API; responses are ILLUSTRATIVE; don't invent usage/cost; `/v1/audio/speech` returns binary audio (check HTTP status + Content-Type first; no JSON usage fields).
