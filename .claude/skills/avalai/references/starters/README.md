# Starters — copy-paste project blueprints on AvalAI

Each file = file tree + complete code + `.env` + run/test steps + cost/limits notes. Models are read from env (`AVALAI_MODEL`, …) so a deprecation never breaks code — pick ids with `scripts/avalai_live.py models --mode chat --tier <yours>` (or MCP `avalai_models`) and verify with `check`.

| Starter | Stack | Use when |
|---|---|---|
| `fastapi-chat-rag.md` | Python · FastAPI · SSE · SQLite embeddings | chatbot over your docs (manual RAG; AvalAI has no hosted vector store) |
| `nextjs-streaming-chat.md` | Next.js 14+ App Router · TS | web chat UI with streaming, key server-side |
| `telegram-bot.md` | Python · aiogram 3 | Persian Telegram assistant with per-user budget |
| `laravel-chat.md` | Laravel 11 · Blade/JS · SSE | chat inside an existing Laravel app (builds on examples/laravel-complete-guide.md) |
| `node-agent-cli.md` | Node/TS · tools loop | CLI/agent with function calling + approvals |
| `ocr-to-json.md` | Python · OCR + structured output | invoices/forms/PDFs → validated JSON |
| `voice-assistant.md` | Python · STT → LLM → TTS | Persian voice assistant / call-center prototype |

Common rules (all starters): key from env only · explicit timeouts · retry only 429/5xx with `Retry-After` · log `avalai-request-id` · validate model JSON/tool args · human approval before side effects · per-user budget + rate limits · never expose key to browsers.
