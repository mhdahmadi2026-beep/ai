# Speech-to-text guide
Endpoints: `POST /v1/audio/transcriptions`, `POST /v1/audio/translations` (OpenAI-compatible, base `https://api.avalai.ir/v1`). See api-reference/audio.md and guides/audio-processing.md.

## ⚠ Model availability verification (Live catalog 2026-10-07)
Notice: while a 2026-09-04 announcement mentioned `gpt-transcribe`/`gpt-live-transcribe` as future replacements, **neither id exists in the live catalog (`GET /public/models`)**. The current active live models for speech-to-text are `gpt-4o-transcribe`, `gpt-4o-mini-transcribe`, `gpt-4o-transcribe-diarize`, `whisper-1`, and `groq.whisper-large-v3` / `-turbo`. Do NOT hardcode `gpt-transcribe` or `gpt-live-transcribe` as they will fail with 404/model not found.

## Models (as listed in this page)
| model | use | notes |
|---|---|---|
| gpt-4o-transcribe | high accuracy file STT (LIVE) | prompt; `json`/`text` |
| gpt-4o-mini-transcribe | cheaper default (LIVE) | |
| gpt-4o-transcribe-diarize | speaker labels (LIVE) | `response_format="diarized_json"`, `chunking_strategy="auto"` (>30 s), NO prompt |
| whisper-1 | srt, vtt, verbose_json, word timestamps, translation (LIVE) | no streaming |
| scribe_v2 / scribe_v1 | ElevenLabs STT | (scribe_v1 → scribe_v2 per deprecations) |
| groq.whisper-large-v3 / -turbo | Groq Whisper routes (LIVE) | low latency |

## Audio prep
mp3, mp4, mpeg, mpga, m4a, wav, webm (flac/ogg on some routes); ≈25 MB upload max; mono speech, trim long silence, don't cut mid-sentence; short `prompt` for product names/acronyms/spelling (model-dependent; not for diarize); send `input_audio` in chat only when the model must analyse audio itself, else transcribe first.

## Language
Persian supported by Whisper-style models but quality varies (accent, noise, domain terms, route). Set `language` when known; glossary in `prompt` (for chunked files pass previous transcript as prompt if supported); post-process with `/v1/responses` (punctuation, glossary fix, classify, extract, translate to non-English targets); human review for low-confidence/sensitive; eval Persian/mixed-language/noisy samples before choosing a cheaper route.

## Basic call
```python
client.audio.transcriptions.create(model="gpt-4o-transcribe", file=f, response_format="text", prompt="...")
```
(Use live model `gpt-4o-transcribe` or `gpt-4o-mini-transcribe`.)

## Migrating from Whisper
Keep endpoint, input file and `response_format="json"` constant; switch only `model`; compare outputs to a human-reviewed reference (WER, name/term accuracy, accents, noise, mixed language, completeness, p95 + first-delta latency, retries, cost/rate limit). Canary + rollback to old model.
| need | decision |
|---|---|
| plain json file transcription | evaluate gpt-4o-transcribe (→ gpt-transcribe); read `.text` |
| srt/vtt/verbose_json/word timestamps | keep whisper-1 until replacement route proves the format |
| translation to English | `/v1/audio/translations` with whisper-1 unless other model enabled |
| speaker labels | diarize model + `diarized_json` (separate workflow) |
| incremental text of finished file | `stream=true` on GPT-4o-transcribe-family; events `transcript.text.delta`, finish with `transcript.text.done` |
| live mic/call | Realtime only if enabled (it isn't) → rolling short chunks |

## Response formats
json (default, GPT-4o family), text, verbose_json (segments/timestamps, whisper-1), srt/vtt (whisper-1/Whisper-compatible), diarized_json. Confidence: `include[]=logprobs` only with GPT-4o transcription + `json`. Don't assume logprobs+timestamps+diarization+prompt combine.

## Diarization
>30 s → `chunking_strategy:"auto"`. Known speakers: 2–10 s reference clips as data URLs via `known_speaker_names[]` + `known_speaker_references[]` (Python: `extra_body={"known_speaker_names":[...],"known_speaker_references":[data_url]}`); always have fallback to generic `speaker_0/1`. Result `transcript.segments[]` with `speaker,start,end,text`. File/request model, not realtime.

## Streaming
`stream=True` on GPT-4o transcribe models only; handle `transcript.text.delta`, require `transcript.text.done` (raise if absent). whisper-1 can't stream.

## Translation
Audio → English only (`whisper-1`). Other target languages: transcribe, then `/v1/responses` translate.

## Pipeline
transcribe (`text`) → `/v1/responses` summarize/extract/tool → optional TTS. Long audio: split on silence/speaker turns, pass previous text as prompt, store chunk start times, retry with backoff + idempotent names.

## Best practices
Quality/noisy → top STT model; volume → mini/Groq; srt/vtt/timestamps/translation → whisper-1 (while available); diarize only if needed; log model, size, duration, language, format, latency, retries; treat transcripts as user data, redact sensitive fields.
