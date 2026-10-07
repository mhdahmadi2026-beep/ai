# Realtime & live audio (guide) — **NOT IMPLEMENTED on AvalAI**

Banner in source: feature in development, not available; AvalAI will announce. Realtime routes/model ids are NOT in AvalAI's supported model data. **Never emit code for** `/v1/realtime`, `/v1/realtime/calls`, `/v1/realtime/client_secrets`, `/v1/realtime/translations`, SIP, `gpt-realtime-*` (incl. `gpt-realtime-whisper`, `gpt-realtime-translate`). Before ever writing such code: check `/v1/models` for an exact id + official AvalAI announcement; event names must match AvalAI route, not OpenAI beta samples; keep a request-based fallback.

## Supported alternative (use this)
| goal | route |
|---|---|
| TTS | `/v1/audio/speech` (`gpt-audio-1.5`, `gpt-audio`, `gpt-audio-mini`) |
| file STT | `/v1/audio/transcriptions` (`gpt-transcribe`, `gpt-live-transcribe`) |
| voice reasoning+tools/state | transcribe → `/v1/responses` → TTS |
| one-shot voice chat | `/v1/chat/completions` with `gpt-audio-*` |
Pipeline (python): `audio.transcriptions.create(model="gpt-transcribe", file=f, response_format="text")` → `responses.create(model=..., instructions=..., input=transcript)` → `audio.speech.create(model="gpt-audio-1.5", voice="alloy", input=answer.output_text).stream_to_file(...)`. Higher latency than WebRTC but portable.

## Architecture reference (OpenAI Realtime, for future planning only)
- Session types: voice-agent, translation (continuous, no `response.create`; send `session.close`, wait for `session.closed`), transcription (`session.type:"transcription"`, `input_audio_buffer.append/commit`, `turn_detection:null` for manual commit; `audio.input.transcription.delay` minimal|low|medium|high|xhigh; deltas `conversation.item.input_audio_transcription.delta/.completed` matched by `item_id`).
- Transports: WebRTC (browser/mobile; server mints ephemeral `client_secrets`; `Location` header gives `call_id` → server sideband WebSocket), WebSocket (server media), SIP (telephony).
- GA event names: `response.output_audio.delta`, `response.output_text.delta`, `response.output_audio_transcript.delta`, `response.output_audio.done`, `response.done`; headers: drop beta header; safety id header `OpenAI-Safety-Identifier` (AvalAI equivalent unverified).
- State machine: session.created/updated → input_audio_buffer.speech_started/stopped/committed → transcription deltas → response deltas → function_call_arguments.delta → response.done.
- Controls: `server_vad` vs `semantic_vad` (threshold, prefix_padding_ms, silence_duration_ms), interruption → `conversation.item.truncate`, `session.update`, session length limits, context truncation (retention_ratio), prompt-cache stability, `rate_limits.updated`, noise reduction, send `event_id` on client events and log with `error` events (async errors).
- Production: ephemeral creds only in browsers, AI-voice disclosure, least-privilege tools with approval for purchases/account changes/emails/deletes, keep transcripts, fallback pipeline.

Doc quirks: mentions `data/models.json` (internal, not reachable); lists `gpt-live-transcribe` as a non-realtime request model.
