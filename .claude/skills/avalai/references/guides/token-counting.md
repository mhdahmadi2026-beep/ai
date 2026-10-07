# Token counting (docs.avalai.ir/fa/guides/token-counting) — NOT IMPLEMENTED on AvalAI

> ⚠ **Banner: the input-token counting endpoint is in development and NOT available on AvalAI yet** (to be announced officially). **Never emit `client.responses.input_tokens.count(...)` or `POST /v1/responses/input_tokens` as working code.** The body of the page still describes the OpenAI-compatible pattern "if the route is enabled for your account/model" — treat it as planning reference; verify with a cURL probe; use the fallback below.

## Why count
Know before calling whether the request fits the model context window, estimate cost, route big inputs to a suitable model. OpenAI recommends counting **the same payload you'll send to Responses** — images, files, tools, schemas, message roles and request formatting add tokens local text tokenizers don't see.

## Recommended workflow
1) check model context window via Models API (api-reference/models.md); 2) when a count route exists, count input tokens before expensive calls; 3) reject/summarize/chunk/route-to-bigger-model oversize inputs; 4) leave headroom for output + reasoning with `max_output_tokens` / `max_completion_tokens`; 5) log real `usage`, `cached_tokens`, model, endpoint, service tier, `avalai-request-id`.
What local tokenizers miss: multimodal input (`input_image`, `file_id`, `file_url`, base64 `file_data`); tool schemas, structured-output schemas, MCP tools, long system instructions; hidden formatting tokens for roles, message boundaries, tool calls, response channels; model-specific behaviour (reasoning, prompt caching, truncation, conversation state).

## OpenAI-compatible shape (reference only — not available)
```python
count = client.responses.input_tokens.count(model="gpt-5.6-luna", instructions="…", input=[{"role":"user","content":"…"}])
count.input_tokens   # then guard (e.g. >120_000 → summarize/chunk), then responses.create(**payload, max_output_tokens=500)
```
cURL probe (run before depending on it; if AvalAI returns an unsupported-route error keep the fallback): `POST https://api.avalai.ir/v1/responses/input_tokens {"model":"gpt-5.6-luna","input":"Tell me a joke."}`.
OpenAI CLI preflight (if your CLI honours `OPENAI_BASE_URL`): `OPENAI_API_KEY=$AVALAI_API_KEY OPENAI_BASE_URL=https://api.avalai.ir/v1 openai responses:input-tokens count --raw-output --transform input_tokens <<YAML … YAML` (use for CI gates, batch imports, pre-upload checks, costly background jobs; doc sample uses `model: gpt-5.5`). If the CLI ignores the base URL, use the explicit cURL.

## Chat Completions preflight mapping (if counting becomes available)
`messages` → `input` array (same role/content items) · first system/developer message → `instructions` (or keep as an `input` item if ordering matters) · `tools`/function schemas → same `tools` array if the Responses-compatible route supports it · `max_completion_tokens` → reserve `max_output_tokens` headroom for the Responses payload but keep `max_completion_tokens` on the real Chat request. Treat count as a conservative planning signal, not the final bill; reconcile with `usage.prompt_tokens`, `usage.completion_tokens`, `usage.prompt_tokens_details.cached_tokens` and the User API transaction record. Keep direct audio-in/out Chat examples on `/v1/chat/completions`; count the nearest text/tool payload and validate the real route in staging.

## Multimodal + tools payloads
Count the exact request body: image input (`input_image` + `image_url`) and function tool schema together are easily under-estimated locally. Private files: use Files API or base64 per target route — don't publish a private document at a public URL just to count it.
| file input form | count it when |
|---|---|
| `file_id` | reusable private files uploaded to `/v1/files` with `purpose="user_data"` |
| `file_url` | public/temporary HTTPS files passed straight to Responses |
| `file_data` | local files sent as base64 data URLs |
PDFs may be extracted text + page images (vision-capable route/model); non-PDF docs mostly text-extracted; spreadsheet-like files may be summarized/augmented rather than raw per-cell counts → count the real `input_file` payload, then test the final route (provider behaviour and account limits differ on AvalAI).

## Output headroom
Reported output usage can include visible text, reasoning tokens, tool-call formatting and other invisible tokens. Hidden `reasoning_tokens` are billed at the model's output-token rate everywhere; if `usage.output_tokens` already includes them, `output_tokens_details.reasoning_tokens` is just a breakdown — don't add it again; if a route reports visible and reasoning separately, price both at the output rate. `max_output_tokens`/`max_completion_tokens` = shared generation budget, not reserved visible-answer room: a reasoning model can exhaust it internally and return no text → check Responses `status:"incomplete"` + `incomplete_details.reason:"max_output_tokens"`, Chat `finish_reason:"length"`; leave headroom; monitor `usage.output_tokens`, `reasoning_tokens`, final answer length; on exhaustion raise the cap, lower effort if supported, or simplify the task (guides/reasoning.md, cost-optimization.md).

## Fallback estimation (use now)
- Plain text: local tokenizer = lower bound only.
- Reserve extra budget for roles, tools, schemas, images, files, reasoning.
- Conservative request-size limits before the API call.
- After the call reconcile with `usage.input_tokens`, `usage.output_tokens`, `cached_tokens` and AvalAI billing records.
- Actual measurement sources: response `usage`, User API (`/user/v1/transactions/lookup`), Models API (context window/prices).
Related: production-best-practices, latency-optimization (not captured), prompt-caching, cost-optimization, responses-vs-chat-completions (not captured), api-reference/models.
