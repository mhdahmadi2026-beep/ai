# Example: building conversational apps with audio models (slug probably /examples/… conversational/voice; unconfirmed)

Companion to examples/processing-audio-chat-completions.md (same models/patterns; read that first) — this page adds the architecture choice and the Responses-first pipeline.

## Architecture choice
| Architecture | When | Path |
|---|---|---|
| Direct audio Chat | need `input_audio`/`modalities`/`message.audio` in ONE call | `/v1/chat/completions` (`gpt-audio-1.5|gpt-audio|gpt-audio-mini`) |
| Responses-first voice assistant | tools, reasoning, structured output, clean state | `/v1/audio/transcriptions` → `/v1/responses` → `/v1/audio/speech` |
| Realtime | live low-latency browser/phone audio | guides/realtime-audio.md — **NOT implemented on AvalAI**; use the request-based paths above (chunked + streaming TTS) |

## Patterns (all in processing-audio-chat-completions.md)
1. One-shot spoken answer: `modalities:["text","audio"]`, `audio:{voice,format:"mp3"}` → base64 in `choices[0].message.audio.data`; keep text transcript; store audio only for playback. CLI decode: `jq -r … | base64 -D` (macOS) / `--decode` (Linux) / `[Convert]::FromBase64String` (PowerShell).
2. Multi-turn: keep text history in `messages`; don't resend generated audio. Responses variant: `previous_response_id` + `store:true` + resend stable `instructions` each turn (instructions aren't inherited), then TTS the `output_text`.
3. User audio: direct `input_audio` (`format` must match bytes) when the model must hear the audio; else transcribe first (`gpt-transcribe`, `response_format:"text"`) — easier to debug (artifact per stage), supports tools, chunking for long files.
4. Tools: let Responses pick/execute tools and write the final text, then `/v1/audio/speech` — most reliable; use direct audio Chat only if the model supports the needed tool behaviour.

## Gemini 3.8 TTS via `/v1/audio/speech`
```bash
curl --fail-with-body -sS https://api.avalai.ir/v1/audio/speech -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" \
 -d '{"model":"gemini-3.8-flash-tts","voice":{"name":"Zephyr","languageCode":"en-US"},"input":"Welcome to AvalAI…","response_format":"mp3"}' --output speech.mp3
```
`voice` is an OBJECT here (`name`, `languageCode`), unlike OpenAI's string; set `response_format` to match file extension; swap to `gemini-3.8-flash-lite-tts` for throughput. TTS only (no transcription/audio input/Live/reasoning); not on Responses/Messages/`:synthesize`; write reply with a chat model first. Native per-turn speaker/style → api-reference/v1beta.md (Gemini 3.8 TTS section).

## Production notes
`gpt-audio-mini` for prototypes; mp3 for stored files, `wav`/`pcm` for lower latency; store transcript+metadata beside audio (search, moderation, analytics); key from env; log model, modalities, format, latency, usage per turn; for big uploads use transcriptions + chunking, not base64 in chat.

## Defects / conflicts
- Page again uses **`gpt-audio-1.5` as the `/v1/audio/speech` model** in all Responses-first pipelines while listing it as a chat-audio model — unverified/contradicts api-reference/audio.md (stale `tts-1`/`gpt-4o-mini-tts`; the latter is REMOVED). Verify the speech model id in `/v1/models` before shipping.
- `gpt-transcribe` availability claim still contradicts earlier notes → verify.
- Responses `previous_response_id` sample needs stored responses (`store:true`) — conflicts with zero-retention policies (guides/data-controls.md).
- Realtime row says "start from realtime-audio guide unless enabled" but that feature is not implemented; no WebSocket/WebRTC path.
- Sample voices (`alloy`, `coral`) valid for OpenAI audio only; Persian speech quality of these voices is untested; no streaming-TTS sample despite "low-latency" advice (use `with_streaming_response`).
- Windows `curl.exe | ConvertFrom-Json` on large audio payloads is slow; JS sample says "SDK node" typo-level inconsistencies only.
