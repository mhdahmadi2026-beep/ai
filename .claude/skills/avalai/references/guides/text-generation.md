# Text generation & prompting (guide)

Preferred API: `/v1/responses` (Responses-first). Keep `/v1/chat/completions` for legacy integrations or routes that only expose chat.

```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
r = client.responses.create(model="gpt-5.6-luna", instructions="...", input="...")
print(r.output_text)
```
Response: `output` array of items (message / reasoning / function_call …). NEVER assume text is at `output[0].content[0].text`; use SDK `output_text` or parse by `type` (`message` → content `output_text` with `annotations`).

## Migration map (Chat → Responses)
| Chat | Responses |
|---|---|
| `messages` | `input` string or message array |
| `system` message | `instructions` or `developer` message |
| `choices[0].message.content` | `output_text` / parse `output` |
| resend full history | `previous_response_id` (if supported) or app-managed (summarized) history |
| `stream:true` chunks | typed SSE events |
Checklist: `instructions` are NOT inherited via `previous_response_id` → resend every turn. `previous_response_id` isn't a free context window (prior chain still billed as input) → summarize old turns. Parse `output` defensively. If a hosted OpenAI tool isn't enabled on the AvalAI route, use function calling, own retrieval, `/v1/search`, or Files API.

## Roles
`developer` (app policy, outranks user within same request), `user`, `assistant`. Treat developer like function definitions, user like arguments. `instructions` param has priority over `input` for the current request only.

## API controls before longer prompts (when model/route supports)
| control | use |
|---|---|
| `reasoning.effort` | planning/code review; start low|medium, high/xhigh only if evals justify |
| `text.verbosity` | concise vs full; also give explicit budgets ("3 bullets", "<120 words") |
| `text.format` / schemas | structured outputs instead of prose JSON description |
| `prompt_cache_key` | many requests with shared long prefix; stable content first, user-specific last; watch cached tokens in usage |
| `previous_response_id` / replay output items | multi-step state; replay items for stateless/strict retention |
Tools: describe what/when/inputs/side-effects/retry-safety/errors in tool description. Don't add today's date to all prompts; only when business rules depend on local date/timezone.

## Length / truncation / sampling
- `max_output_tokens` caps visible + hidden reasoning tokens; if reasoning eats it → `incomplete_details.reason:"max_output_tokens"` with no visible text. Leave headroom.
- Context window shared by input + tool results + output + reasoning; compact before limit (guides/compaction.md).
- `truncation:"disabled"` (default for safety) vs `"auto"` only for low-risk history; legal/finance/support/agents → app summaries or compaction.
- Set `temperature` OR `top_p`, not both; deterministic settings for evals. (Not for Claude 5.x/reasoning models that reject sampling params.)

## Prompts as code
Keep prompt builders in app code, not hosted prompt objects. OpenAI: prompt creation deprecated from 2026-06-03, `v1/prompts` shutdown planned 2026-11-30. Send generated `instructions`+`input` directly; add fixtures/evals; roll out via flags.

## Model choice
Capabilities, provider, cost vs performance. Doc suggests `gpt-5.5` as starting point for OpenAI-family on Responses (samples use `gpt-5.6-luna` — current id check 10-deprecations/catalog); smaller models for latency/price.

## Prompt engineering
Be specific (task + output format), few-shot examples, state goals for reasoning models, evaluate with evals. Fine-tuning NOT implemented on AvalAI.

## Source defects
- Go examples use fictional `client.CreateResponse` (go-openai has none), lowercase `model:` field; PHP `$client->responses()` is from openai-php.
- JS sample omits `import OpenAI`.
- Model examples `claude-opus-4-8`, `gemini-3.5-flash`, `gpt-5.5` may not match current catalog.
