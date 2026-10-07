# `/v1/text:synthesize` — Vertex AI native Text-to-Speech (docs: /fa/api-reference/v1-text-synthesize)

Native Google Cloud TTS (Vertex AI) format: multi-speaker, style prompts, many audio encodings. **Legacy path for Gemini 2.5 TTS** (`gemini-2.5-flash-tts`, `gemini-2.5-pro-tts`). **Do NOT use it for Gemini 3.8 TTS** (`gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`) — those are only on `/v1beta/models`, `/v1/chat/completions`, `/v1/audio/speech` (see audio.md, v1beta.md). For new work prefer `/v1/audio/speech` unless you specifically need Vertex-native features.

Features: 30+ voices, 100+ languages/locales, style prompts, multi-speaker, several encodings.

`POST https://api.avalai.ir/v1/text:synthesize` — `Authorization: Bearer $AVALAI_API_KEY`.

## Request
```json
{"input":{"prompt":"<optional style>","text":"<text>"},
 "voice":{"languageCode":"fa-IR","name":"Kore","model_name":"gemini-2.5-flash-tts"},
 "audioConfig":{"audioEncoding":"MP3"}}
```
- `input.text` (req) ≤ ~4000 bytes at time of writing; `input.prompt` (opt) style instruction (≤ ~4000 bytes). Limits may change → Google docs (cloud.google.com/text-to-speech/docs/gemini-tts). (The error sample and `split_text(max_bytes=900)` helper in the page cite 900 bytes — inconsistent; split conservatively, e.g. ≤900 bytes/chunk, if you hit INVALID_ARGUMENT.)
- `voice.languageCode` (req, BCP-47, must match text language), `voice.name` (opt: Kore, Puck, Charon, Fenrir, Aoede, Zephyr…), `voice.model_name` (req: `gemini-2.5-flash-tts` | `gemini-2.5-pro-tts`), `voice.multiSpeakerVoiceConfig.speakerVoiceConfigs[{speakerAlias, speakerId}]` (alias = speaker label used in the text; `speakerId` = voice name).
- `audioConfig.audioEncoding` (req): `MP3`, `LINEAR16`, `OGG_OPUS`, `MULAW`, `ALAW`; `sampleRateHertz` (LINEAR16: 16000/24000/48000; MP3/OGG auto ~24 kHz; MULAW/ALAW 8000).
Multi-speaker text format: `"سام: سلام! باب: سلام، حال شما چطور است؟ …"`; in the Python SDK example speaker aliases **must be English** (`Sam`, `Bob`) — the JSON example with Persian aliases may fail.

## Response
`{"audioContent":"<base64>","timepoints":[],"audioConfig":{"audioEncoding":"MP3","sampleRateHertz":24000}}` → decode base64 (`jq -r .audioContent | base64 -d > out.mp3`; LINEAR16 → `.wav`).

## Voices (examples)
Kore neutral/balanced (general, professional) · Charon deep/resonant (authoritative, narration) · Fenrir storytelling (audiobooks) · Aoede strong/authoritative (announcements) · Puck bright/energetic (upbeat ads) · Zephyr soft/professional (business, presentations). 100+ languages incl. English variants, Spanish, French, German, Italian, Portuguese, Arabic, Hindi, Japanese, Korean, Mandarin, Persian (fa-IR), Turkish, Russian, Ukrainian… (full list: fa/providers/google#gemini-25-flash-tts).

## Encodings
MP3 (audio/mpeg; general/web) · LINEAR16 (audio/L16; best quality/editing, large) · OGG_OPUS (audio/ogg; streaming/web) · MULAW (audio/basic) / ALAW (audio/x-alaw-basic) (telephony, 8 kHz).

## Python (Google Cloud SDK, REST transport)
```python
from google.cloud import texttospeech
client = texttospeech.TextToSpeechClient(transport="rest",
    client_options={"api_endpoint": "https://api.avalai.ir", "api_key": os.getenv("AVALAI_API_KEY")})
r = client.synthesize_speech(
  input=texttospeech.SynthesisInput(text="…", prompt="متن زیر را با لحنی هیجان‌زده و پرانرژی بگویید"),
  voice=texttospeech.VoiceSelectionParams(language_code="fa-IR", name="Puck", model_name="gemini-2.5-pro-tts"),
  audio_config=texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3))
open("output.mp3","wb").write(r.audio_content)
```
Multi-speaker: `VoiceSelectionParams(language_code, model_name, multi_speaker_voice_config=MultiSpeakerVoiceConfig(speaker_voice_configs=[MultispeakerPrebuiltVoice(speaker_alias="Sam", speaker_id="Kore"), …]))` + LINEAR16 24000 Hz.
(Using `api_key` in `client_options` with Google auth may need `google-api-core` support; if it fails call the REST endpoint directly with `Authorization: Bearer`.)

## Errors
400 bad request (INVALID_ARGUMENT, e.g. text too long) · 401 · 413 too large · 429 · 500. Error JSON `{"error":{"code":400,"message":…,"status":"INVALID_ARGUMENT"}}`.

## Model choice & pricing
- Flash TTS: high volume, simple TTS, cost-sensitive. Pro TTS: complex style prompts, multi-speaker, premium quality.
- `gemini-2.5-flash-tts`: input $0.50/1M tokens(chars), cached $0.25, audio output $10.00/1M (32 tokens/sec audio). `gemini-2.5-pro-tts`: input $1.00, cached $0.50, output $20.00 per 1M. Example: 30 s audio = 960 tokens; Flash ≈ $0.0096 output + $0.00005 input ≈ $0.00965. (The page's gemini-2.5-* TTS ids appear on the audio page as available; verify live status — Gemini 2.5 TTS ids may be superseded by 3.8.)

Related: providers/google, audio.md, chat.md, fa/guides/audio-processing, Vertex docs.
