# Moonshot AI (Kimi)

OpenAI SDK format. Endpoint support: kimi-k3/kimi-latest: chat ✅, `/v1/messages` ✅, `/v1/responses` ⚠️ partial. kimi-k2.7-code(+highspeed): chat ✅, responses ⚠️. Others: chat ✅, messages ⚠️, responses ⚠️. Docs' "Responses equivalent" blocks use `gpt-5.6-luna`, not Kimi — don't copy them. Up to 128 tools/request, JSON mode (`response_format`), partial mode (assistant prefill), automatic prompt caching (no ids/params). Chinese/English optimized.

## Models ($/1M in / cached / out)
| id | ctx | notes | in | cached | out |
|---|---|---|---|---|---|
| kimi-k3 | 1M | 2.8T MoE, native vision, always-on reasoning (default `reasoning_effort:"max"`), strict JSON schema, tools | 3.00 | 0.30 | 15.00 |
| kimi-latest | 1M | alias → kimi-k3 (use `kimi-k3` for reproducibility) | 3.00 | 0.30 | 15.00 |
| kimi-k2.7-code | 262,144 | coding/agentic, served via Fireworks.ai | 0.95 | 0.19 | 4.00 |
| kimi-k2.7-code-highspeed | 262,144 | low latency | 1.90 | 0.38 | 8.00 |
| kimi-k2.6 | n/a | older coding; docs recommend k2.7-code for new work | 0.95 | 0.16 | 4.00 |
| kimi-k2.5 | n/a | multimodal, agent swarm (100 sub-agents) | 0.66 | 0.11 | 3.30 |
| kimi-k2-thinking | n/a | reasoning, `reasoning_content`; temp 1.0, max_tokens ≥16000, stream recommended; search ctx $0.005/query | 0.66 | 0.165 | 2.75 |
| kimi-k2-0711-preview | 128K | temp 0.6 | 0.60 | 0.15 | 2.50 |
| kimi-thinking-preview | 128K | CoT, temp 1.0 | 30.00 | 0.15 | 30.00 |
| moonshot-v1-8k | 8K | temp 0.6 | 0.20 | 0.15 | 2.00 |
| moonshot-v1-8k-vision-preview | 8K | JPG/PNG/BMP, base64 or URL | 0.20 | 0.15 | 2.00 |
| moonshot-v1-32k | 32K | | 1.00 | 0.15 | 3.00 |
| moonshot-v1-32k-vision-preview | 32K | | 1.00 | 0.15 | 3.00 |
| moonshot-v1-128k | 128K | | 2.00 | 0.15 | 5.00 |
| moonshot-v1-128k-vision-preview | 128K | | 2.00 | 0.15 | 5.00 |
| moonshot-v1-auto | ≤128K | auto-routes; billed at max-tier price | 2.00 | 0.15 | 5.00 |

## Rules
- k3: `reasoning_effort:"max"`, `max_completion_tokens`.
- k2-thinking multi-turn tool loop: append the whole assistant message (keeps `reasoning_content`) before tool results; read via `getattr(msg,"reasoning_content",None)`.
- Recommended temperature: 0.6 normally, 1.0 for thinking models.

## Defects / suspicious
- kimi-thinking-preview prices ($30/$30, cached $0.15) look wrong/legacy; kimi-k2.7-code ctx quoted exactly, others missing.
- Vision-preview/old moonshot-v1 ids likely retired upstream — check 10-deprecations.md.
- Sample uses `"name"` in tool messages; harmless.
