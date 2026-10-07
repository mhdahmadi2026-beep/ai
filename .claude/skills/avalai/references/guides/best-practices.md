# API best practices (docs.avalai.ir/fa/guides/best-practices)

Quick production checklist for the OpenAI-compatible API at `https://api.avalai.ir/v1` (adapts OpenAI production/deployment/prompting/safety/accuracy guidance). Use it as an index, not the sole decision source.

## Reading map
| goal | go to |
|---|---|
| ship new AI feature | deployment-checklist (not captured) — Responses-first setup, reasoning effort, verbosity, cache, background jobs |
| production readiness | production-best-practices (not captured) — scaling, observability, rate limits, cost, security, release discipline |
| prompt quality | prompt-engineering (not captured) / guides/text-generation.md |
| cost/latency | cost-optimization, latency-optimization (not captured); guides/rate-limits.md |
| factual accuracy | optimizing-llm-accuracy (not captured), guides/evals.md — run evals before changing prompt/retrieval/fine-tune/model |
| safety risk | safety-best-practices, safety-checks (not captured), guides/red-teaming.md |

## Core API usage
- New work: `/v1/responses` (state, tools, reasoning, structured outputs, new model behaviour). `/v1/chat/completions` for stable existing integrations and chat-only models.
- Secrets server-side: `AVALAI_API_KEY` from env/secret manager; never in browser/mobile/public repo/logs/screenshots.
- Design rate limits early: monitor response headers, exponential backoff + jitter, batching/background only when it helps throughput.
- Log for debugging: request id (`avalai-request-id`), model, provider, endpoint, latency, retries, status, usage, tenant/user id; no secrets/unneeded personal data.
- Validate input/output: schema, size limits, file type, moderation, tool allowlists before costly/risky operations.

## Model/API starting points (verify via /v1/models)
- General assistants: `gpt-5.5`, `gpt-5.4-mini`, `gpt-5.4-nano` (route by quality/latency/cost; `text.verbosity` in Responses).
- Complex reasoning: `gpt-5.5`, `gpt-5.4-pro` etc.; tune `reasoning.effort` per task, not max by default without eval.
- Code: `gpt-5.3-codex`, `gpt-5.5`, `claude-opus-4-8`, `kimi-k2.7-code` (Responses for API workflows; Codex guides for repo-editing agents).
- Fast support/routing: small GPT, Claude Haiku, Gemini Flash, Qwen Flash; short prompts, bounded output, stream only if UX improves.
- Retrieval/search: `/v1/embeddings` + `/v1/responses`, build retrieval app-side (hosted File Search not available).
- Image/audio/video: dedicated API guides.

## Prompt defaults
Stable behaviour in `instructions` (Responses) or system/developer message (Chat); explicit task, audience, constraints, output format; only relevant context (retrieval/file input rather than whole KB); structured outputs or function tools when downstream code needs exact fields; evaluate prompts on representative examples before switching model, effort or fine-tuning.

## Production rules (aligned with OpenAI)
- Parse Responses defensively: `output_text` for plain text; inspect `response.output` by `type` when tool calls, refusals, annotations, files, images or reasoning metadata may appear.
- Version prompts in code (builders, schemas, examples, eval fixtures); don't rely on hosted prompt objects unless the route is confirmed.
- Separate final JSON from tool args: Structured Outputs for typed user-facing answers, function calling for app actions; always re-validate server-side.
- Strict tool contracts: `strict:true`, `additionalProperties:false`, all fields required (optional = union with `null`); `parallel_tool_calls:false` for writes/payments/approvals.
- State deliberately: `previous_response_id` when retention is acceptable; otherwise replay only needed output items incl. matching `call_id`s.
- Long tasks: stream a short preamble/event before the final answer so the user sees progress.

## Specific use cases
- Chat: keep relevant history only; cap conversation length (long = more tokens + lost context); function calling for actions, Structured Outputs when the answer itself must be JSON.
  Chat tool shape: `{"type":"function","function":{name,description,parameters,strict:true}}` (nested); Responses tool is flat (`{"type":"function","name":…,"parameters":…,"strict":true}`); read `function_call` items; `parallel_tool_calls=False`.
- Embeddings: normalize vectors for similarity; dimensionality reduction (t-SNE/UMAP) for visualization; chunk long docs. Doc sample bug: `cosine_similarity` returns plain dot product (correct only for pre-normalized vectors); the `lru_cache` + md5 cache-key sample doesn't actually use the key and `client` isn't defined — use a real cache (Redis/DB with TTL).
- Image gen: be specific, state style/medium, iterate (good prompt = detailed scene+style vs "a futuristic city").

## Cost
Monitor token usage; keep prompts concise but sufficient; smaller models for simple tasks; batch multiple inputs where appropriate; cache identical/similar responses with a TTL suited to the use case.

## Safety & privacy
Content filtering via moderation endpoints; define usage policies; send only necessary user data; tell users how data is used; define data retention policy.

## Testing & evaluation
Define metrics; human evaluation for subjective tasks; automated tests; A/B compare model/prompt versions on real users (satisfaction, completion rate).

## Architecture
Async processing for long tasks (`AsyncOpenAI` + `asyncio.gather`; watch rate limits); streaming for UX — Chat: iterate chunks `delta.content`; Responses: handle `response.output_text.delta`, finish on `response.completed`, raise on `response.failed`/`error`.
Responses equivalents in the page swap models to `gpt-5.6-luna` and use generic prompts — informational only.

## Tip
Paste a docs.avalai.ir page URL into chat.avalai.ir messages so the model can use that page to explain, debug, or draft examples.
