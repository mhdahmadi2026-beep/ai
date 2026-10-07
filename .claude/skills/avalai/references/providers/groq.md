# Groq (ids prefixed `groq.`)

LPU fast inference. Endpoints: LLM/safety → `/v1/chat/completions`; TTS → `/v1/audio/speech`; Whisper → `/v1/audio/transcriptions`.

## LLM / safety ($/1M in / cached / out)
| id | in | cached | out |
|---|---|---|---|
| groq.llama-guard-4-12b | 0.20 | 0.10 | 0.20 |
| groq.llama-prompt-guard-2-22m | 0.03 | 0.015 | 0.03 |
| groq.llama-prompt-guard-2-86m | 0.04 | 0.02 | 0.04 |
| groq.llama-4-maverick-17b-128e-instruct | 0.20 | 0.10 | 0.60 |
| groq.llama-4-scout-17b-16e-instruct | 0.11 | 0.055 | 0.34 |
| groq.kimi-k2-instruct-0905 | 1.00 | 0.50 | 0.34 (suspicious: out < in) |
| groq.gpt-oss-120b | 0.15 | 0.075 | 0.75 |
| groq.gpt-oss-20b | 0.075 | 0.0375 | 0.30 |
| groq.gpt-oss-safeguard-20b | 0.075 | 0.0375 | 0.30 |
| groq.qwen3-32b | 0.29 | 0.145 | 0.59 |

## Audio
- groq.playai-tts, groq.playai-tts-arabic: $50/1M base input tokens + $0.00005/char. Voice ids like `Aaliyah-PlayAI`, Adelaide, Angelo, Arista, Atlas, Basil, Briggs, Calum, Celeste, Cheyenne, Chip, Cillian, Deedee, Eleanor, Fritz, Gail, Indigo, Jennifer, Judy, Mamaw, Mason, Mikail, Mitch, Nia, Quinn, Ruby, Thunder (all `-PlayAI`). PlayAI TTS is likely retired by Groq — check 10-deprecations.md.
- groq.whisper-large-v3: $0.00185/min; groq.whisper-large-v3-turbo: $0.000067/min.

## Defects
- Persian example prompt for TTS (PlayAI isn't Persian); llama-guard sample just asks "is it safe?" (real use needs Llama Guard chat template/content to classify).
