# Assistants API — migration reference (docs: /fa/api-reference/assistants)

> ⛔ **NOT IMPLEMENTED on AvalAI.** Don't treat examples as runnable until AvalAI announces Assistants compatibility. OpenAI deprecated Assistants API on **2025-08-26**, sunset **2026-08-26** (already past today, 2026-10-07). **Never generate code using `/v1/assistants`, `/v1/threads`, `/v1/threads/*/runs`, `client.beta.assistants`, or `OpenAI-Beta: assistants=v2`.** Use `/v1/responses` + function calling + tools + conversation state (fa/api-reference/responses, fa/guides/{function-calling,tools,conversation-state}).

## Concept mapping → Responses
| Assistants | Responses/AvalAI |
|---|---|
| Assistant instructions | top-level `instructions` in `/v1/responses` (+ agent config in your app for reusable personas) |
| Thread | `previous_response_id`, manual replay of `response.output` items, or `conversation` object where route supports |
| Message | `input` item with `role` user/assistant; keep typed output items for reasoning/tool flows |
| Run | one `/v1/responses` request (`background: true` where route supports) |
| Function tool | Responses function tool with strict schema; return `function_call_output` with matching `call_id` |
| File search / vector store | `file_search` if route supports; else RAG via `/v1/embeddings` + own store + `/v1/responses` |
| Code interpreter / hosted tools | route/model/account dependent; otherwise run code in your own sandbox/worker and expose one narrow function tool |

OpenAI mapping: Assistants→versioned Prompts, Threads→Conversations, Runs→Responses, run steps→typed response items. AvalAI hosted prompts/conversations = compatibility concept only until endpoints are announced.

## Portable migration steps
1. Version the agent profile (model, instructions, tool schemas, output schema, safety policy) in source control/config.
2. Store conversation state yourself (user/assistant msgs, tool calls, tool outputs) in your DB.
3. Call `/v1/responses` with the current turn + compressed relevant history; use `previous_response_id` only when the route supports stored state.
4. Preserve typed items (tool calls, reasoning summaries, file refs, citations) — don't flatten to text.
5. Migrate new traffic first; backfill old threads only if product continuity needs it.

## Runnable replacement (math tutor)
```python
response = client.responses.create(
    model="gpt-5.6-luna",   # verify id via /v1/models
    instructions="شما یک معلم ریاضی صبور هستید. روش حل را توضیح بده، پاسخ نهایی را نشان بده و یک سوال تمرینی کوتاه بپرس.",
    input="مساحت یک مستطیل ۸۴ و عرض آن ۷ است. طول آن چقدر است؟",
    store=False)
print(response.output_text)
```
JS: `client.responses.create({model, instructions, input, store:false})`; curl: `POST /v1/responses` with same JSON.

## Planned (unavailable) endpoints — map only
- `POST /v1/assistants` — body: `model` (req), `name` (≤256), `description` (≤512), `instructions` (≤32768), `tools` (≤128; types `code_interpreter|file_search|function`), `tool_resources`, `metadata` (≤16 pairs). Response object: `id asst_…`, `object:"assistant"`, `created_at`, `name`, `description`, `model`, `instructions`, `tools`, `file_ids`, `metadata`.
- `POST /v1/threads` (`messages`, `metadata`); `POST /v1/threads/{id}/messages` (`role` user only, `content`, `file_ids`, `metadata`); `POST /v1/threads/{id}/runs` (`assistant_id` req, `instructions`, `tools`, `metadata`).
- Source SDK examples (Python `client.beta.assistants.create`, JS, Go `CreateAssistant` from go-openai [import mismatch with `openai-go`], PHP with `OpenAI-Beta: assistants=v2`) omitted as non-runnable.

Errors 400/401/403/404/429/500 standard. Related: models, authentication, rate-limits.
