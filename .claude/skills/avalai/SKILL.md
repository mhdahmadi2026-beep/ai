---
name: avalai
description: Expert guide for building with AvalAI (اول ای‌آی / "اول ai" / "هوش مصنوعی اول"), an OpenAI-compatible AI gateway at https://api.avalai.ir/v1. Use whenever the project calls AvalAI, api.avalai.ir, AVALAI_API_KEY, or the user asks about AvalAI models, pricing, rate limits, service tiers, credit packages, deprecations, Responses/Chat Completions/Messages APIs, images, audio, tools, streaming, structured outputs, function calling, or production practices. Always consult references/ instead of guessing model IDs, prices or limits.
---

# AvalAI skill

Source of truth: https://docs.avalai.ir/fa/ (Persian) — English at https://docs.avalai.ir/en/.
Official name is always written **AvalAI**. Users may also say «اول ai», «اول ای آی», «هوش مصنوعی اول».

## Core facts (from the Introduction page)
- Single base URL for OpenAI-compatible clients: `https://api.avalai.ir/v1`
- Auth: project API key in env var `AVALAI_API_KEY`. Create it in the dashboard (https://chat.avalai.ir/platform/home). **Server-side only — never ship to browsers/mobile apps.**
- Recommended first call: **Responses API** (`client.responses.create`), read `response.output_text`.
- Works with the official OpenAI SDKs (Python/JS) and plain cURL.
- Support: ticket https://chat.avalai.ir/platform/support/create-ticket · status https://status.avalai.ir/ · debug with AvalAI chat https://chat.avalai.ir/chat

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)
print(response.output_text)
```

## Working rules
1. Read the matching file in `references/` before writing code; see `references/00-index.md` for the page map and which pages are already captured.
2. Never invent model IDs, prices, tiers or limits. If a reference file is missing or marked PENDING, say so and ask the user for that page.
3. Model availability depends on account tier (e.g. some models "from tier 1"). Check `references/` for tier and endpoint support (Chat Completions / Messages / Responses — support may be full or partial per model).
4. Keys from env, never hard-coded; plan security, retries, latency and cost per production-best-practices.
5. Dates in docs are Jalali with Gregorian in parentheses; promotional rates expire — check dates.

## References
See `references/00-index.md`.

## Practical rules from Quickstart
- New text apps → `/v1/responses` (`input`, `instructions`, `response.output_text`); keep `/v1/chat/completions` (`messages`) for legacy/chat-only models.
- On `429`: honor `Retry-After`, exponential backoff + jitter + retry cap.
- Discover models: `GET https://api.avalai.ir/public/models` (no auth) or `/v1/models`.
- Provider-specific params: `extra_body` (Python) / `@ts-expect-error` direct fields (TS).
- Exact cost: read `avalai-request-id` header → `POST /user/v1/transactions/lookup` (available ~30s later).
- Model IDs in examples may be stale; verify live before hard-coding.

## Tool integration rules (ai-workflows)
- Base URL `https://api.avalai.ir/v1`; tools append `/chat/completions` themselves — never paste the full path into a base-URL field.
- Model prefix is tool-specific: OpenCode `avalai/<id>`, Aider `openai/<id>`, direct API plain `<id>`.
- Use a dedicated AvalAI key (not OpenAI/ChatGPT credentials). Don't use `gpt-transcribe`/`gpt-live-transcribe` on AvalAI.
- Start direct; add 9Router (a gateway, not an agent) only when routing/fallback is needed. Human approval before side effects; synthetic data first.

## SDK rules (libraries)
- OpenAI SDK → base `https://api.avalai.ir/v1`. Anthropic SDK & Google GenAI SDK → base `https://api.avalai.ir` (**no `/v1`**). Anthropic SDK can call non-Claude models via `/v1/messages`; Google SDK is Gemini-only.
- Pin SDK versions; keep a raw-HTTP fallback; set explicit timeouts for flex tier / long jobs; retry only idempotent operations.
- Log `avalai-request-id`; optionally send `X-Client-Request-Id`.
- Several published snippets have SDK-version quirks (Go/.NET/Google Python) — see notes in `references/04-libraries.md` and verify against the installed SDK.
