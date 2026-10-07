# Reasoning models (guide)
Reasoning = hidden internal process; ask for final answer + short rationale/checklist/cited evidence, NOT hidden chain-of-thought. Billed: reasoning tokens use OUTPUT rate and consume context. In OpenAI-style usage `output_tokens` already INCLUDES `output_tokens_details.reasoning_tokens` → never add them (double count).
Doc date mismatch: page says V4-Pro redirect "pending, not done at 2026-09-11"; today = 2026-10-07 → **already effective** (since 2026-09-14 04:00 UTC).

## Model families on AvalAI (as of page; verify /v1/models + 10-deprecations)
- **OpenAI**: gpt-6.1-sol (in 922K/out 128K; chat+messages+responses full, tier ≥1), gpt-6-sol, gpt-6-luna (922K/128K, full 3 endpoints), gpt-6-astra (strongest; computer use, SWE, science, long-context), gpt-5.6-sol/-terra/-luna (1M ctx), gpt-5.5 (effort none/low/medium/high/xhigh, 1M), gpt-5.4-pro (1.05M; medium/high/xhigh), gpt-5.4 (none…xhigh), gpt-5.4-mini (none/low/medium, 400K), gpt-5.4-nano (none/low, 400K), gpt-5-pro (tier≥2, Responses only), gpt-5.3-codex (Responses only), o4-mini, o3, o3-mini.
- **Google**: gemini-3.8-flash (= alias `gemini-flash-latest`), gemini-3.6-flash, gemini-3.5-flash-lite, gemini-3.5-flash, gemini-3.1-pro-preview, gemini-3.1-flash-lite(+-preview alias), gemini-2.5-pro, gemini-2.5-flash.
- **Anthropic**: claude-sonnet-5-5, claude-opus-5-5, claude-fable-5-1 (tier≥2), claude-opus-5, claude-opus-4-8 (default effort high), claude-opus-4-7, claude-sonnet-5, claude-sonnet-4-6, claude-haiku-4-5.
- **Moonshot**: kimi-k3 (+alias kimi-latest).
- **DeepSeek**: deepseek-v4.1-flash (use for new work; native vision; thinking/non-thinking; tools; caching; AvalAI limits in 1,000,000 / out 393,216, provider says 384K), deepseek-v4-pro → redirected to v4.1-flash with V4.1 Flash pricing, deepseek-v4-flash (legacy V4 route), `deepseek-reasoner`/`deepseek-chat` aliases kept (per 2026-08-14 policy → v4-pro / v4-flash, i.e. now v4.1-flash chain; verify).
- **xAI**: grok-4.7 (in/out 500K each; chat+messages full, responses partial), grok-4.6 (500K/500K), grok-4.5 (1M), grok-4.3 (1M, >200K pricing tier), grok-4.20-reasoning / -non-reasoning (2M).
- **MiniMax**: minimax-m3, m2.7, m2.7-highspeed, m2.5, m2.5-lightning.
- **Z.AI**: glm-5.3-flash (320B/18B active, 991K in), glm-5.3 (mandatory thinking; `thinking.type:"enabled"`, level low|high|max), glm-5.2, glm-5.1, glm-5v-turbo, glm-5-turbo.
- **Alibaba**: qwen3.8-flash (alias qwen3.8-flash-next; 125B/6B MoE, vision, thinking default ON, 262K, `reasoning_effort` low|medium|xhigh), qwen3.8-27b (dense, vision, same effort set), qwen3.8-2.4t-a95b (open-weight base, text only, thinking ALWAYS on, effort low|medium|xhigh), qwen3.8-max (managed flagship, hybrid via `enable_thinking`, 1M ctx, 128K out), qwen3.7-max, qwen3-max, qwen3.6-plus/-flash/-max-preview/-35b-a3b/-27b (remember: non-streaming needs `enable_thinking:false`; true only with stream).
- **Fireworks**: muse-glimmer-30b (low|medium|high|xhigh; temp 1.0, top_p 0.95, top_k 64), nemotron-3.5-lightning (temp 1.0 top_p 0.95), nemotron-3-ultra.
Don't assume thinking controls pass through on every endpoint; check response, drop unsupported fields. `o1-pro`-style models may need Responses.

## When / how to prompt
Use for ambiguity, long-context synthesis, agentic planning, multi-file review, grading. Planner (reasoning) + executor (fast GPT-style) pattern. Prompt: simple, zero-shot first; rules in `developer`, task in `user`; delimiters (Markdown/XML); constraints + success criteria + tools; ask short rationale/checklist, not CoT; Markdown off by default on some o-series → first line of developer message `Formatting re-enabled`. Reasoning models: high-level goals; GPT models: explicit instructions.

## Per-provider knobs
- OpenAI Responses: `reasoning:{"effort":"low|medium|high|xhigh|…"}`; Chat: `reasoning_effort`. gpt-6.x: don't send unsupported values (local metadata says `none`/`minimal` unsupported on 6.1 sol); defaults vary per model. Responses-first checklist: gpt-6-astra with `medium` (raise to `high` only if evals justify); reserve `max_output_tokens` for reasoning + visible text; `store:true` + replay reasoning/function_call items or `previous_response_id`; stateless/zero-retention → `include:["reasoning.encrypted_content"]`; `reasoning.summary` only where supported (observability, not raw CoT).
- gpt-6.1-sol pricing ($/1M): input ≤272K: 2.00 / cached 0.10 / cache-write 2.50 / out 10.00; input >272K: 4.00 / 0.20 / 5.00 / 15.00 (input length decides output tier too).
- **Claude**: Messages `thinking:{"type":"adaptive"}` + `output_config:{"effort":...}`; Chat Completions via `extra_body={"thinking":{"type":"adaptive"},"output_config":{"effort":"high"}}`. NEVER fixed `budget_tokens`, temperature/top_p, prefill, forced tool use. Sonnet 5.5: tier≥1, 1M in/128K out, chat+messages full, responses partial, migrating from thinking-disabled → `between_tools`; price 2.00/0.20/cache-write 4.00/10.00. Opus 5.5: always-on adaptive thinking (can't disable), default effort `medium`, efforts low|medium|high|xhigh|max, price 4.00/0.20/8.00/20.00, tier≥1 all 3 endpoints; keep full signed assistant content/thinking blocks, don't move between conversations; text between tools now lives in thinking blocks (empty display default—not a hang). Fable 5.1 default effort high, always-on thinking.
- **GPT-6 Sol/Luna & Grok 4.7**: not image generators. Sol/Luna: pass effort only with route-confirmed values. Grok 4.7: omit `reasoning_effort` until values confirmed; responses is partial (test tool roundtrip/state). Long-context price tiers: Sol/Luna >272K, Grok 4.7 >200K, Grok 4.6 >200K (in $2.00/cached 0.50/out 6.00 ≤200K; $4.00/1.00/12.50 above).
- **DeepSeek V4.1 Flash**: $0.15 in / $0.003 cached / $0.60 out, fixed off-peak tariff always (no scheduling/doubling); chat+messages full, responses partial. Historic V4 settings: `reasoning_effort` low|high|max (V4-Flash-0731), `extra_body={"thinking":{"type":"enabled"|"disabled"}}`, `reasoning_content` field. **CRITICAL tool loop**: within the SAME turn include `reasoning_content` in the assistant message with `tool_calls` (else error "Missing reasoning_content field in the assistant message"); between turns (new user msg) send only `content`.
- **Kimi K3**: top-level `reasoning_effort:"max"` only (always-on); no `thinking` param, no temperature/top_p; keep full assistant message in tool loops.
- **Gemini 3.x**: via `extra_body={"generationConfig":{"thinkingConfig":{"thinkingLevel":"high"}}}` (native v1beta same body). Gemini 3.8 more effort = more tokens/tool calls. Gemini 3.6 flash / 3.5 flash-lite responses = partial. Gemini 2.5 Flash: `extra_body={"thinking":{"type":"enabled","budget_tokens":2000}}` (thinking_budget is 2.5-only).
- Direct HTTP: params go at top level of the JSON body.

## Effort selection
| workload | start |
|---|---|
| voice, classification, simple retrieval | none/low |
| support, drafts, tool planning | low/medium |
| coding, research, spreadsheet/doc analysis | medium |
| deep research, security review, hard debugging | high/xhigh after eval |
Defaults are model-specific (don't generalize medium). Log effort, tokens (output & reasoning), latency, status in evals; lower effort if reasoning tokens high without quality gain.

## Phase (Responses, long tool flows; gpt-5.5/5.4/5.6 etc., route-dependent)
Preserve assistant `phase`: `"commentary"` for mid-run updates, `"final_answer"` for final; never add phase to user messages; dropping it can make commentary read as final. Prefer `previous_response_id` when retention OK; else replay items unchanged. Preamble pattern: one status sentence then analysis; final = decision + evidence + verification checklist.

## Output budget
`max_output_tokens` (Responses) / `max_completion_tokens` (Chat; `max_tokens` legacy) = shared budget for hidden reasoning + visible answer. Symptom of exhaustion: Responses `status:"incomplete"` + `incomplete_details.reason:"max_output_tokens"`, reasoning ≈ output_tokens, empty text; Chat `finish_reason:"length"` with empty content. Fix: raise cap (to model max), lower effort, simplify/split task, headroom measured per model/prompt. Context window shared by input + tool output + output + reasoning; reasoning needs thousands to tens of thousands of tokens.
Usage example: `{input_tokens:75, output_tokens:1186, output_tokens_details:{reasoning_tokens:1024}, total_tokens:1261}`.
Cost control: effort + output cap; log per model/prompt-type.

## Source defects
- Mixed model ids across examples (gpt-5.6-sol / gpt-5.6-luna vs "gpt-5.5" in summaries); Go samples use fictional `client.CreateChatCompletion` + lowercase `model:` + `MaxTokens` (go-openai style) while import is openai-go.
- Chat-completions samples pass `temperature` to reasoning models (OpenAI reasoning models and Claude 5.x reject it) — ignore.
- DeepSeek section is "historical V4" with V4-Pro samples that now redirect.
- Gemini direct-HTTP sample sends `thinking{type,budget_tokens}` to gemini-3.1-flash-lite-preview (conflicts with thinkingLevel guidance).
- Bash sample builds JSON by string-splicing; PHP uses `finishReason` camel-case property.
- Links to model-details, production-best-practices not captured.
