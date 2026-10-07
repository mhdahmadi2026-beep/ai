# Example: audio processing in Chat Completions (/examples/processing_audio_in_chat_completion_api)

Related: api-reference/audio.md, guides/audio-processing.md, guides/text-to-speech.md, providers/google.md (Gemini 3.8 TTS), guides/responses-vs-chat-completions.md.

## When to use
Keep `/v1/chat/completions` when the model must ACCEPT `input_audio` or RETURN `message.audio` directly. Need reasoning on a transcript, tools, structured output, `previous_response_id` → use the Responses pipeline below.

## Audio chat models
`gpt-audio-1.5` (higher quality, longer context), `gpt-audio` (balanced), `gpt-audio-mini` (cheap dev / support bots / high traffic). Access can depend on account tier/route → check models/model-details before deploying.

## Pattern 1 — text in, speech out
```python
c = client.chat.completions.create(model="gpt-audio-mini",
    modalities=["text","audio"], audio={"voice":"alloy","format":"wav"},
    messages=[{"role":"system","content":"…"},{"role":"user","content":"…"}])
m = c.choices[0].message; m.content  # text/transcript
open("answer.wav","wb").write(base64.b64decode(m.audio.data))   # base64 in message.audio.data
```
Shell: `curl … | jq -r '.choices[0].message.audio.data' | base64 --decode > answer.mp3` (macOS `base64 -D`; PowerShell `[Convert]::FromBase64String`). Must set `"audio"` in `modalities` AND `audio:{voice,format}`.

## Gemini 3.8 TTS via Chat
`gemini-3.8-flash-tts` (expressive/long dialogues) / `gemini-3.8-flash-lite-tts` (throughput). Text in, audio out ONLY — no transcription, audio input, Live API, reasoning. Allowed routes: native `/v1beta/models`, `/v1/chat/completions`, `/v1/audio/speech`; NOT `/v1/responses`, `/v1/messages`, `/v1/text:synthesize`. Compose reply with a chat/reasoning model first, then send final text to TTS.
Body: `{"model":"gemini-3.8-flash-tts","messages":[{"role":"user","content":"Have a wonderful day!"}],"modalities":["audio"],"audio":{"voice":"Zephyr","format":"pcm16"}}` → `choices[0].message.audio.data` (base64; not `.content`; don't strip `DEPRECATED`). `pcm16` = raw signed 16-bit LE, 24 kHz, mono, NO header → `ffmpeg -f s16le -ar 24000 -ac 1 -i speech.pcm speech.wav`. Native non-stream 3.8 default is WAV → check `mimeType` before adding a header. Use `--fail-with-body` and `base64.b64decode(..., validate=True)`.

## Pattern 2 — audio in
`content:[{"type":"text","text":"…"},{"type":"input_audio","input_audio":{"data":<b64>,"format":"wav"}}]`. Keep clips short (model/request size limits); format must match bytes; for files/long audio use `/v1/audio/transcriptions` + chunking.

## Pattern 3 — multi-turn
Keep the TEXT transcript in `messages` (user/assistant text); store audio bytes separately; resend audio only if the model must re-hear it. Raw audio doesn't persist between requests.

## Responses migration (staged pipeline)
`/v1/audio/transcriptions` (`gpt-transcribe`, `response_format:"text"`) → `/v1/responses` (`input=transcript`, read `output_text`) → `/v1/audio/speech` (`gpt-audio-1.5`, `voice:"coral"`, `with_streaming_response…stream_to_file`). Use when tools/structured outputs/`previous_response_id`/manual item replay are needed.

## Format/latency tips
Chat: `wav`/`pcm16` for low latency; `/v1/audio/speech` raw format name is `pcm`; `mp3` for small files/compat. Dev with `gpt-audio-mini`.

## Troubleshooting
No audio back → add `"audio"` to modalities + `audio` object. `input_audio` rejected → model lacks audio input or `format` mismatch. Payload too big → transcriptions endpoint/compress/split. No memory of earlier audio → resend transcript. Need tools/JSON → Responses pipeline.

## Defects / caveats
- `gpt-audio-1.5` used as a **speech** model in `/v1/audio/speech` in the migration sample, while the page lists it as a chat-audio model; verify against api-reference/audio.md (which also has stale `gpt-4o-mini-tts`/`tts-1`). `gpt-transcribe` support claim contradicts earlier notes — verify.
- Page has no Go/PHP samples; assistant turns resend only text (the doc's Pattern 3 drops the first reply's audio).
- Gemini section says `pcm16` is chat-only; Responses-equivalent block is a custom pipeline, not a drop-in.
- Windows sample parses JSON via `curl.exe | ConvertFrom-Json` (needs the response as a single string; large audio may be slow).
- Pattern-3 sample reuses `alloy` voice and mp3 without saving audio — demo only.
