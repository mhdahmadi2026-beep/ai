# Text-to-speech guide
Endpoint `POST /v1/audio/speech`. Complements api-reference/audio.md, guides/audio-processing.md, api-reference/v1beta.md (Gemini native), providers/elevenlabs.md.

## ⚠ Model status (this page is newer than api-reference/audio.md)
`gpt-4o-mini-tts`, `tts-1`, `tts-1-hd` = deprecated/NOT available (10-deprecations also lists gpt-4o-mini-tts removed). api-reference/audio.md samples that use them are STALE → use `gpt-audio-1.5` / `gpt-audio` / `gpt-audio-mini` or Gemini 3.8 / ElevenLabs. (`gpt-audio*` themselves have a provider shutdown 2027-01-20 per 10-deprecations — verify `/v1/models`.)

| model | best for |
|---|---|
| gpt-audio-1.5 | top OpenAI-compat quality, tone/speed/style control (default) |
| gpt-audio | balanced |
| gpt-audio-mini | cheap/high-volume |
| gemini-3.8-flash-tts | creative, emotional, regional accents, long dialogue |
| gemini-3.8-flash-lite-tts | high throughput, low latency, everyday reading |
| gemini-2.5-pro-tts / -flash-tts | legacy Vertex `/v1/text:synthesize` only; new work → 3.8 |
| gemini-3.1-flash-tts-preview | legacy, PCM16 only (`response_format:"pcm"`) |
| eleven_v3, eleven_multilingual_v2, eleven_turbo_v2_5, eleven_flash_v2_5 | ElevenLabs voices |

## Basic
`audio.speech.create(model="gpt-audio-1.5", voice="coral", input=..., response_format="mp3")`; Python `with_streaming_response…stream_to_file(path)`; JS `Buffer.from(await speech.arrayBuffer())`. curl `--output speech.mp3`.

## Gemini 3.8 migration rules
- Text in → audio out only (no STT/chat-audio-in/Live/reasoning). Routes: v1beta native, `/v1/chat/completions`, `/v1/audio/speech` ONLY (never `/v1/responses`, `/v1/messages`, `/v1/text:synthesize`). Draft text with another model first.
- `/v1/audio/speech` body: `{"model":"gemini-3.8-flash-tts","voice":{"name":"Zephyr","languageCode":"en-US"},"input":"...","response_format":"mp3"}`; Flash-Lite = swap model id. For 3.1-flash-tts-preview voice is a plain string ("Zephyr") + `response_format:"pcm"` → raw PCM16 24 kHz mono: `ffmpeg -f s16le -ar 24000 -ac 1 -i x.pcm x.mp3` (don't just rename .pcm to .mp3).
- Input is read VERBATIM: "Say cheerfully:" / "Speaker 1:" get spoken. Native GenerateContent: put `speechMetadata:{"speaker":"Host","style":"Warm and welcoming."}` on each text part; each multi-speaker part must name a defined speaker; sustained delivery in `style`; inline tags `<laugh>`, `<sigh>`, `<short pause>` only for momentary events.
- Native non-streaming response default = WAV (`audio/wav`, RIFF). Check `inlineData.mimeType`: wav → save decoded bytes as-is; `audio/L16` raw PCM16 → add WAV header 24 kHz mono; never double-header.
- Chat Completions: use `audio.format` (not `response_format`); ask `pcm16`; decode `choices[0].message.audio.data` (NOT `message.content`; don't strip any prefix from the base64); convert with ffmpeg as above.

## Voices
OpenAI-compat: alloy, ash, ballad, coral, echo, fable, nova, onyx, sage, shimmer, verse, marin, cedar (model-dependent; try marin/cedar first). ElevenLabs/Gemini/PlayAI have own voices; on voice error read provider docs. Disclose AI-generated voice to users.
Language/pronunciation: test target languages incl. Persian with real names; keep glossary/numbers/abbreviations consistent across chunks; wav/pcm for low-latency tests, mp3 for storage; native-speaker review; log model, voice, language, style, format, latency.
Custom voice: NOT a public AvalAI endpoint; use built-in or provider voice IDs; consent + disclosure + audit trail for any cloning.

## Formats
mp3 (default), opus (streaming), aac (mobile), flac (lossless), wav (low-latency), pcm (raw/realtime playback).

## Streaming / long text
Binary stream by default; `stream_format:"sse"` only if route supports. ≤4,096 chars per `input` (OpenAI-compat; providers vary). Split by paragraph/slide/scene, keep speaker/pronunciation/style fixed, add pauses in your app, store chunk order, cache static narration. `speed` 0.25–4.0 (use sparingly).

## With Responses
`responses.create(...)` → `output_text` → `audio.speech`. Chat audio models (`gpt-audio-*` in `/v1/chat/completions`) return text+audio in one call.

## Defects
- Page links `#gemini-38-native-text-to-speech` in v1beta.md; the "legacy" tag on `gemini-2.5-*` conflicts with audio.md (lists them valid).
- JS streaming sample buffers the entire response before writing (not real streaming).
