# DeepSeek provider page (docs: /fa/providers/deepseek)

**Timeline (today 2026-10-07):** `deepseek-v4-pro` was to be redirected to `deepseek-v4.1-flash` on 2026-09-14 04:00 UTC — already past → treat as **redirected, billed at V4.1 Flash rates**. All legacy ids route to `deepseek-v4.1-flash` per 10-deprecations.md. New integrations: `deepseek-v4.1-flash`. Always send real `reasoning_content` back during tool loops (see below).

## deepseek-v4.1-flash (recommended)
552B MoE total; causal encoder–decoder; 8B active for input processing / 16B active for output; native vision; thinking & non-thinking; tool calling; JSON output; prompt cache. Ctx list max in **1,000,000**, out **393,216** (provider "384K"). Endpoints: chat, messages, responses (**partial**). Price/1M: in $0.15, cached **$0.003**, out $0.60. AvalAI always applies this fixed low-load tariff (no off-peak scheduling; don't halve table values again). Don't carry old reasoning-effort values to this model.
## Prior V4 (history; pre-redirect)
- `deepseek-v4-flash` (backend 0731; 284B/13B active; DSpark speculative decoding; effort low|high|max; $0.22 / cached 0.007 / $0.66; chat only). Provider retired V4-Flash and V4-Flash-Vision-Exp on its own service — no AvalAI redirect implied by that alone.
- `deepseek-v4-pro` (0813; 1.6T/49B active; 1M ctx/384K out; thinking default on; `reasoning_effort` high|max (low/medium→high, xhigh→max); $0.66 / cached 0.022 / $1.98; `reasoning_content`; JSON, tools, chat-prefix completion (beta)). Pre-redirect only.
## Compatibility aliases (policy 2026-08-14; per deprecations all now → `deepseek-v4.1-flash`)
`deepseek-chat`→v4-flash (non-thinking default; $0.22/0.007/0.66; JSON, tools, prefix completion beta, FIM beta non-thinking), `deepseek-coder`→v4-flash, `deepseek-reasoner`→v4-pro (thinking default; effort high|max; `reasoning_content`), `deepseek-v3-0324`, `deepseek-r1-0528`, `deepseek-v3.1`→v4-pro. Target model's fixed tariff applies.
## Via Azure AI (not in alias table; verify live)
- `deepseek-v3.2`: 128K; in $0.28 / cached 0.028 / out 0.42; non-thinking; JSON, tools, prefix completion; chat, `/v1/completions`, responses, messages; DSA sparse attention; Azure = higher rate limits/lower latency.
- `deepseek-v3.2-speciale`: 128K; same prices; deep reasoning only, **no tool calling**; IMO 2025/IOI gold-level; same endpoints.
- `deepseek-v3.1`: 128K; cached 0.07 / in 0.27 / out 1.10; chat, responses, messages.

## Thinking mode API
- Reasoner/thinking returns `choices[0].message.reasoning_content` (CoT) + `content`. Control with `extra_body={"thinking":{"type":"enabled"|"disabled"}}`, `reasoning_effort`.
- **Multi-turn:** send back only `content` of previous turns (not `reasoning_content`).
- **Tool calling in thinking mode (critical):** within the same turn, when appending the assistant tool-call message you **must include `reasoning_content`** (else 400 `Missing reasoning_content field in the assistant message`). You may drop old `reasoning_content` when a new user turn starts. Loop pattern: call → if `tool_calls`: append assistant message `{role, content or "", tool_calls[...], reasoning_content}` → append `role:"tool"` results → repeat. (Page's PHP uses `OpenAI::factory()`; fine.)
- Hybrid inference, DSA token compression for 1M context, agent focus (Claude Code/OpenClaw/OpenCode integration), strong coding; benchmarks per DeepSeek.
## Pricing table ($/1M)
| model | cached | in | out |
|---|---:|---:|---:|
| `deepseek-v4.1-flash` | 0.003 | 0.15 | 0.60 |
| `deepseek-v4-pro` before 2026-09-14 | 0.022 | 0.66 | 1.98 |
| `deepseek-v4-pro` after (→ V4.1 Flash) | 0.003 | 0.15 | 0.60 |
Context for V4 base models 1M; redirected ids inherit target route limits (check `/v1/models`).
Note: earlier chat.md said DeepSeek callout stale — this page confirms V4.1 Flash is the target.
