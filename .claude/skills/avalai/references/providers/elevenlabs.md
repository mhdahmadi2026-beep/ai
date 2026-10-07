# ElevenLabs (speech)

TTS → `POST /v1/audio/speech`; STT → `POST /v1/audio/transcriptions` (multipart). See api-reference/audio.md.

## TTS models (priced per second of generated audio)
| id | langs | char limit | latency | $/s |
|---|---|---|---|---|
| eleven_v3 | 70+ (incl. Persian) multi-speaker, emotional | 5,000 | higher | 0.005 |
| eleven_multilingual_v2 | 29 (NO Persian) | 10,000 | higher | 0.005 |
| eleven_turbo_v2_5 | 32 | 40,000 | ~250-300 ms | 0.0025 |
| eleven_turbo_v2 | English | 40,000 | ~250-300 ms | 0.0025 |
| eleven_flash_v2_5 | 32 | 40,000 | ~75 ms | 0.0025 |
| eleven_flash_v2 | English | 40,000 | ~75 ms | 0.0025 |
Voices (OpenAI-style names): alloy, coral, echo, fable, nova, onyx, sage, shimmer. Persian TTS → `eleven_v3` (only listed model with فارسی among v3 list; v2.5 turbo/flash list per docs excludes it).

## STT
`scribe_v2`, `scribe_v1`: $0.00009722/s (~$0.35/h). 90+ langs. scribe_v2: keyterm prompting (≤100), entity detection (56 types), word timestamps, diarization (≤32 speakers), audio-event tagging, auto language detect. Response: `{text, task, language, duration, words:[{word,start,end}]}`.

## Via RunwayML
`runwayml.eleven_multilingual_v2` listed separately at $0.000015/char (see runwayml.md).

## Defects
- Docs say "8 models" in intro but table lists 6 TTS + 2 STT (consistent). Char limits may differ from audio.md (check there).
- Turbo v2.5 lang list "all Multilingual v2 + Hungarian, Norwegian, Vietnamese" — Persian not included there.
