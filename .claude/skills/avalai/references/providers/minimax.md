# MiniMax

Endpoints: chat/completions (OpenAI SDK, base `https://api.avalai.ir/v1`), `/v1/messages` (Anthropic SDK, base `https://api.avalai.ir` NO /v1; native `thinking` blocks). m3: chat ✅, messages ✅, responses ⚠️ partial. Docs' "Responses equivalent" blocks use `gpt-5.6-luna` — not MiniMax; ignore.

## Models ($/1M)
| id | notes | in | cached | cache-write | out |
|---|---|---|---|---|---|
| minimax-m3 | flagship, 1M ctx (guaranteed ≥512K), native multimodal (image+video in), thinking on/off at same price, MSA sparse attention | ≤512K: 0.60 / >512K: 1.20 | 0.12 / 0.24 | – | 2.40 / 4.80 |
| minimax-m2.7 | self-evolving, ~60 tps, `reasoning_split` | 0.30 | 0.06 | 0.375 | 1.20 |
| minimax-m2.7-highspeed | ~100 tps | 0.60 | 0.06 | 0.375 | 2.40 |
| minimax-m2.5 | 204K, ~50 tps, `<think>` tags, `reasoning_split` | 0.30 | 0.03 | 0.375 | 1.20 |
| minimax-m2.5-lightning | ~100 tps | 0.30 | 0.03 | 0.375 | 2.40 |
| minimax-m2.1 | 204K ctx, 128K max out, ~60 tps, interleaved thinking | 0.30 | 0.03 | 0.375 | 1.20 |
| minimax-m2.1-lightning | ~100 tps | 0.30 | 0.03 | 0.375 | 2.40 |
| minimax-m2 | older, 204K | 0.30 | 0.03 | 0.375 | 1.20 |

## Rules
- Reasoning appears inline in `<think>…</think>` in `content` by default. To separate: `extra_body={"reasoning_split": True}` → `message.reasoning_details` (thinking) and `message.content` (answer). (m2.5, m2.7; see provider-specific-params guide.)
- Multi-turn tool use: append the FULL assistant message (tool_calls/thinking blocks intact). With Anthropic SDK append `response.content` unchanged (thinking blocks preserved) then `tool_result` user block.
- Block types via Anthropic SDK: `thinking`, `text`, `tool_use`.

## Defects
- "Comparison table" has mismatched columns (header lists 3 models, rows have 4 values) and claims m2.1 has 1M ctx/multimodal — that's m3; trust model sections above.
- Check 10-deprecations.md for retired m2.* ids.
