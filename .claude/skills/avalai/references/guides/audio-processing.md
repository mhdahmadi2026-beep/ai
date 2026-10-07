# Audio processing guide
Complements api-reference/audio.md, providers/elevenlabs.md, providers/google.md, api-reference/v1beta.md. Deprecations override.

## Which path
| goal | route |
|---|---|
| text → audio file | `/v1/audio/speech` |
| file → text | `/v1/audio/transcriptions` |
| speech → English text | `/v1/audio/translations` (`gpt-transcribe`) |
| audio in/out inside chat | `/v1/chat/completions` with audio model (`modalities:["text","audio"]`, `audio:{voice,format}`, content part `input_audio:{data(base64),format}`) |
| assistant reasoning on voice | transcribe → `/v1/responses` → TTS |
| live speech-to-speech | Realtime NOT announced on AvalAI → don't emit `/v1/realtime`, `/v1/realtime/translations`, SIP, client secrets |

## Models (doc list)
TTS: `gpt-audio-1.5`, `gpt-audio`, `gpt-audio-mini`; ElevenLabs `eleven_v3`, `eleven_multilingual_v2`, `eleven_flash_v2_5`; Gemini `gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`. STT: `gpt-transcribe`, `gpt-live-transcribe` (diarization), `scribe_v2`. Chat audio: `gpt-audio-1.5`, `gpt-audio-mini`.
**Removed/deprecated**: `gpt-4o-mini-tts`, `tts-1`, `tts-1-hd`, `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`, `whisper-1`. (Earlier note in 10-deprecations: `gpt-audio*` shutdown 2027-01-20.)

## TTS
`model`, `input`, `voice`, optional `instructions` (tone/pacing/emotion), `response_format` mp3|opus|aac|flac|wav|pcm, `speed` (route-dependent, start 1.0). OpenAI-compatible: ≤4,096 chars per request; try voices `marin`/`cedar` for quality. Disclose AI voice to users. Streaming: binary stream by default; `stream_format:"sse"` only if route supports. Python `audio.stream_to_file(path)`; JS `Buffer.from(await audio.arrayBuffer())`.

### Gemini 3.8 TTS
Text in → audio out only (no STT/chat/live/reasoning). Allowed routes ONLY: `/v1beta/models/...`, `/v1/chat/completions`, `/v1/audio/speech`. NOT `/v1/responses`, `/v1/messages`, `/v1/text:synthesize`. On `/v1/audio/speech`:
```json
{"model":"gemini-3.8-flash-tts","voice":{"name":"Zephyr","languageCode":"en-US"},"input":"...","response_format":"mp3"}
```
(`voice` is an OBJECT here, unlike OpenAI's string.) lite = higher throughput/lower latency. Native route: decode output by MIME (WAV vs audio/L16).

## STT
Formats mp3, mp4, mpeg, mpga, m4a, wav, webm; ≈25 MB upload (OpenAI-compatible) → split on sentence/turn boundaries. Params: `response_format` (text|json|verbose_json|diarized_json…), `prompt` (domain terms; not supported by diarization model), `timestamp_granularities[]` (word-level with `gpt-transcribe` + `verbose_json`), `chunking_strategy:"auto"` for long diarization, `stream=true` for completed recordings (live mic needs Realtime). Speaker labels: `gpt-live-transcribe` + `diarized_json`.

## Production checklist
Disclose AI audio; server-side keys only; validate type/size/duration; consent/privacy for recording/diarization; domain prompts; evaluate accents/noise; test pronunciation/latency. For live systems design: short-lived creds, safety identifier, VAD/turn detection, interruption, partial transcripts, latency metrics, logging.

## Defects
- Gemini TTS sample's `voice` object vs OpenAI string; `gpt-audio-1.5` presented as TTS model on `/v1/audio/speech` — verify against audio.md.
- Links to guides realtime-audio/speech-to-text/text-to-speech not yet captured.
