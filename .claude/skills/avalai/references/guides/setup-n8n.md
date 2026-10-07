# n8n integration (setup guide)
n8n = open-source workflow automation. Just point it at AvalAI: base URL `https://api.avalai.ir/v1` (OpenAI node) / `https://api.avalai.ir` (Gemini + Anthropic nodes) with the AvalAI key. "410+ models" claim (OpenAI, Anthropic, Google, xAI, DeepSeek, Alibaba, Moonshot, Z.AI, MiniMax, Fireworks, Mistral, Meta…). Pricing aligned to provider base API rates (no markup per docs).

## Easiest: HTTP Request node (recommended for beginners; 100% reliable)
Key: dashboard → API keys → new secret key (copy immediately). Free credit: phone-verified = 200,000 toman total; email-only 25,000 + 175,000 after phone verification (not additive 200k+25k).
Node config: Method `POST`, URL `https://api.avalai.ir/v1/chat/completions`; Authentication `Generic Credential Type` → `Header Auth` (credential "AvalAI API": Name `Authorization`, Value `Bearer <KEY>` — keep word Bearer + space); header `Content-Type: application/json`; Body Content Type `JSON`:
```json
{"model":"gpt-5.4-mini","messages":[{"role":"user","content":"سلام! یک جوک بگو."}]}
```
Dynamic: `{"role":"user","content":"{{ $json.userMessage }}"}` (+ system message). Responses variant (if node can call it): URL `https://api.avalai.ir/v1/responses`, body `{"model":"gpt-5.6-luna","instructions":"...","input":"{{ $json.userMessage }}"}`, read `output_text` downstream; keep Chat form if workflow/model only supports `messages`. Test with "Execute Node".

## Credentials per node
- **OpenAI node**: credential type OpenAI; API Key = AvalAI key; Base URL / Custom URL = `https://api.avalai.ir/v1`. Works with ALL models (chat, image, text). Chat examples: gpt-5.5, gpt-5.4-mini, claude-opus-4-8, claude-sonnet-4-6, gemini-3.5-flash, grok-4.3, deepseek-v4-pro (redirects to v4.1-flash), qwen3.7-max, kimi-k2.7-code, glm-5.2, nemotron-3-ultra, minimax-m3. Images: gpt-image-2, gpt-image-1.5 (shutdown 2026-12-01), qwen-image-2.0(-pro), gemini-3.1-flash-image, seedream-5-0-260128, "DALL·E 3 / Stability" (stale — likely removed). Prefer "Chat" resource over legacy Completions.
- **Google Gemini(PaLM) Api credential**: API Key = AvalAI key; Host/Base URL = `https://api.avalai.ir` (no /v1). **Model name MUST start with `models/`** (e.g. `models/gemini-2.5-flash`, `models/gemini-3.5-flash`, `models/gemini-3.1-pro-preview`, `models/gemini-3.1-flash-lite-preview`); without it → 404 (n8n doesn't prepend it; endpoint is `v1beta/models/<id>:generateContent`).
- **Anthropic credential**: API Key = AvalAI key; Host/Base URL = `https://api.avalai.ir` (no /v1). Works for all Anthropic models (claude-opus-4-8/4-7, sonnet-4-6, haiku-4-5) plus most other AvalAI models (compat expanding).
Roles in chat prompts: system (behaviour), user (task), assistant (previous replies).

## Tips / troubleshooting
Treat key like a password; separate keys per project; respect rate limits (add delays/queues/batching in workflows); pricing = provider base rates; "invalid API key" → recheck copy/field (new keys can take ≤60 s); connectivity: n8n host must reach `https://api.avalai.ir/v1` and `https://api.avalai.ir`; wrong base URL (OpenAI node needs `/v1`; Gemini/Anthropic nodes don't); model not working in a node → try OpenAI node (all models); Gemini native node → add `models/`; rate-limit errors → lower frequency/batch.

## Defects
- Many example model ids may be deprecated (check 10-deprecations): DALL·E 3, Stability models, gpt-image-1.5, claude-opus-4-7, deepseek-v4-pro.
- Docs claim "no workflow changes needed" but Gemini node requires `models/` prefix.
