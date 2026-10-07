# Model selection (docs.avalai.ir/fa/guides/model-selection)

Pick the best model for performance and cost across AvalAI providers. **Model ids below are copied from the docs page and many may be stale — verify against live `GET /v1/models`, 10-deprecations.md and models/ pages before use** (e.g. `o4-mini` → `gpt-5.6-terra` on the deprecation list; `gemini-2.5-flash-image` retired; fine-tuning/distillation isn't available on AvalAI).

## Principles
1. **Optimize accuracy first** with the strongest models until you hit your target.  2. **Then optimize cost and latency** with the cheapest/fastest model that keeps accuracy.

## GPT-5.5 / Responses-first defaults
For OpenAI-family workloads start complex new integrations with `gpt-5.5` on `/v1/responses` (OpenAI positions GPT-5.5 for complex production workflows, tool-heavy agents, grounded assistants, long-context retrieval, coding, spec→plan). Check the model-details page, provider page and account tier before final rollout.
- Strong baseline → route down: build the eval baseline with `gpt-5.5`/`gpt-5.4-pro`/another top model, then send simple cases to `gpt-5.4-mini`, `gpt-5.4-nano`, flash/haiku or fast provider-specific models.
- Prefer Responses for reasoning, tool calling, stateful turns, structured outputs, multimodal; keep `/v1/chat/completions` for existing integrations, framework compat, chat-only models.
- Tune reasoning, not only the model: GPT-5.5 default `medium`; `low` for latency-sensitive flows; `high`/`xhigh` only when evals show measurable gains; `none` only for light tasks without planning/multi-step tools.
- Control length separately (`text.verbosity`, explicit output budget, `max_output_tokens`) instead of long prompts.
- Cache-friendly prompts: fixed policies/schemas/tool descriptions first, dynamic user context and retrieval snippets later.

### Migration checklist for new flagship models
1) freeze the old baseline (accuracy, latency, token use, tool-call behaviour, failure examples); 2) start with the smallest safe prompt (keep product policy, output contract, safety; drop legacy step-by-step scaffolding); 3) tune API controls before adding prose (`reasoning.effort`, `text.verbosity`, `max_output_tokens`, structured outputs) on the same eval set; 4) validate tool orchestration (tool preambles, returned output items, `phase` when replaying state manually, `previous_response_id` handling); 5) keep hosted-feature assumptions explicit (hosted OpenAI tools, tool search, compaction, prompt-cache behaviour vary per route/provider/model/account); 6) route after measuring — move easy cases down only when evals show they don't need the flagship.

### Provider & deployment-path checks
| check | why |
|---|---|
| model id & route | same family can have different id, context limit, `/v1/responses` vs `/v1/chat/completions` support per provider |
| feature parity | hosted tools, MCP, web/file search, prompt caching, image/audio input, streaming differ per route |
| data & safety boundary | external providers' retention, residency, logging, safety guarantees differ once data leaves the main AvalAI path |
| billing & quota | cheaper model may have lower rate limit, different service tier or regional cost |
| eval coverage | run the same local eval set on every candidate route; compare accuracy, latency, cost, refusals, tool-call behaviour before rollout |
If a deployment path exists only via a provider's native API, keep it in your backend and expose it to the model as a narrow `function` tool.

## 1. Accuracy first
Set a concrete accuracy target; build an eval dataset (e.g. 100 samples: user request, model answer, correct answer, accuracy); start with the strongest models of each provider (page list — verify):
OpenAI `gpt-5.5`, `gpt-5.4-pro`, `gpt-5.4`, `gpt-5.3-codex` · Anthropic `claude-opus-4-8`, `claude-opus-4-7`, `claude-sonnet-4-6`, `claude-haiku-4-5` · Google `gemini-3.5-flash`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite`, `gemma-4-26b-a4b-it` · xAI `grok-4.20-reasoning`, `grok-4.20-non-reasoning` · DeepSeek `deepseek-v4-pro` (→ `deepseek-v4.1-flash` since 2026-09-14), `deepseek-v4-flash` · Alibaba `qwen3.7-max`, `qwen3.7-plus`, `qwen3.6-plus`, `qwen3.6-flash` · Moonshot `kimi-k2.7-code`, `kimi-k2.7-code-highspeed`, `kimi-k2.6` · Z.AI `glm-5.2`, `glm-5.1`, `glm-5v-turbo` · MiniMax `minimax-m3`, `minimax-m2.7`, `minimax-m2.7-highspeed` · Fireworks `nemotron-3-ultra`.
**Realistic accuracy target from economics** (fake-news example): correct classification saves $50 of human review; a wrong one costs $300 → break-even accuracy = 300/(50+300) ≈ **85.7%** (page says 85.8%); aim ≥ 90% for positive ROI. Compute the same way from your own cost structure.

## 2. Then cost & latency
Compare cheaper/faster models: `gpt-5.4-mini`/`gpt-5.4-nano`/`o4-mini` instead of `gpt-5.5`/`gpt-5.4-pro`; `claude-haiku-4-5` instead of `claude-opus-4-7`; `gemini-3.1-flash-lite`/`-preview`/`gemini-2.5-flash` instead of `gemini-3.5-flash`; `deepseek-v4-flash` vs `-pro`; `qwen3.6-flash`/`qwen3.6-35b-a3b` instead of `qwen3.7-max`/`plus`; MiniMax: `minimax-m3` (multimodal long context), `minimax-m2.7-highspeed` (throughput), `minimax-m2.5` (cheaper coding); `grok-4.20-non-reasoning` instead of `-reasoning` when little reasoning needed. **Model distillation / fine-tuning a smaller model is not available on AvalAI (fine-tuning.md)**.
Core strategies: fewer requests, fewer tokens (shorter input, shorter outputs), smaller model keeping accuracy. **Exceptions:** if strongly cost/latency-bound set thresholds up front, drop models beyond them, then optimize accuracy within constraints.

## Worked example (fake-news classifier: ≥90% accuracy, <$5 per 1,000 articles, <2 s each)
| # | method | accuracy | cost | latency |
|---|---|---|---|---|
| 1 | gpt-5.5 zero-shot | 93.0% ✓ | $6.80 ❌ | ~2 s ✓ |
| 2 | gpt-5.4-mini few-shot (n=5) | 91.2% ✓ | $2.40 ✓ | <2 s ✓ |
| 3 | routing: easy → gemini-3.1-flash-lite-preview, hard → gpt-5.5 | 92.1% ✓ | $1.10 ✓ | <2 s ✓ |

## AvalAI provider cheat-sheet (page's table; verify ids)
| use case | top performance | balanced | cost-effective |
|---|---|---|---|
| general chat | gpt-5.5, claude-opus-4-8 | claude-sonnet-4-6, gemini-3.5-flash | gpt-5.4-mini, gemini-3.1-flash-lite |
| complex reasoning | gpt-5.5, gpt-5.4-pro, claude-opus-4-8 | deepseek-v4-pro, glm-5.2, qwen3.7-max | deepseek-v4-flash, qwen3.6-flash, gemini-3.1-flash-lite |
| code generation | gpt-5.5, claude-opus-4-8, glm-5.2 | kimi-k2.7-code, minimax-m3, qwen3.7-plus | gpt-5.4-mini, deepseek-v4-flash, qwen3.6-flash |
| vision | gpt-5.5, claude-opus-4-8, gemini-3.5-flash | gemini-3.1-pro-preview, qwen3.7-max, minimax-m3 | gemini-2.5-flash, glm-5v-turbo |
| function calling | gpt-5.5, claude-opus-4-8, grok-4.3 | gemini-3.5-flash, deepseek-v4-pro, qwen3.7-max | gpt-5.4-mini, deepseek-v4-flash, gemini-3.1-flash-lite |
| embeddings | gemini-embedding-2, text-embedding-3-large | embed-v4.0, text-embedding-3-small | qwen3-embedding, embed-english-v3.0 |
| image generation | gpt-image-2, qwen-image-2.0-pro | gpt-image-1.5, gemini-3.1-flash-image | qwen-image-2.0, seedream-5-0-260128 |
⚠ Cross-check vs deprecations & other captured pages: `gpt-image-1.5`/`gpt-image-1` are on the removal/deprecation list (default image model is `gpt-image-2.5-flare`/`-sunburst`); `seedream` ids differ per BytePlus page; `gpt-4o`-era and `o4-mini` ids deprecated; `grok-4.3` appears here only.

## Sample (page) — BROKEN
`from avalai import AvalAI; client = AvalAI(api_key=…)` — there is NO `avalai` SDK; use the OpenAI SDK: `OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")`, `chat.completions.create` / `responses.create`. Swap `model` only (strong → cheaper) while keeping the same code.
Related: models/model-details, fine-tuning (not available), latency-optimization (not captured), evals/promptfoo example, pricing, OpenAI latest-model guide, prompt-engineering (captured).
