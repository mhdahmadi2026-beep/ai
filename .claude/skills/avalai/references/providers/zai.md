# Z.AI (GLM) provider page (docs: /fa/providers/zai)

OpenAI-compatible chat. `thinking` / `web_search` via `extra_body` (Python) or top-level (JS). Deprecations remove several GLM ids — verify.
## Models
| id | ctx in / out | in | cached | out | endpoints / notes |
|---|---|---|---|---|---|
| `glm-5.3-flash` | 991,000 / 128,000 | **promo 0.075 until 2026-09-09 (expired) → check pricing** | promo 0.015 | promo 0.25 | 320B MoE/18B active, 45 layers, hybrid sparse+linear attention (3× less attention compute, 4.4× smaller KV vs GLM-5.3); first natively multimodal GLM-5 (30T multimodal tokens); open weights; chat+messages full, responses partial; Terminal Bench 2.1 84.3, DeepSWE 63.4, Toolathlon 78.4 |
| `glm-5.3` | 1M / 128K | 1.40 | 0.26 | 4.40 | flagship coding/agents/authorized security; chat, messages, responses(partial); **thinking mandatory**: `thinking:{"type":"enabled"}` required (`"disabled"` → error); `reasoning_effort` `low|high|max` (default `max`); Z.ai Code Bench +50% vs 5.2; Terminal-Bench 3.0 28.3, DeepSWE 66.9, CyberGym 84.5 |
| `glm-5.2` | 1M / 128K | 1.40 | 0.26 | 4.40 | chat, responses(partial); same base as 5.3 |
| `glm-5.1` | 200K / 128K | 1.54 | 0.286 | 4.84 | chat; SWE-Bench Pro 58.4% |
| `glm-5v-turbo` | 200K / 128K | 1.20 | 0.24 | 4.00 | vision (multi-image), functions, structured; chat |
| `glm-5` | 200K / 128K | 1.10 | 0.22 | 3.52 | 744B (40B active); SWE-bench Verified 77.8; chat; `thinking:{"type":"enabled","budget_tokens":15000}` example |
| `glm-5-turbo` | 200K / 128K | 1.32 | 0.264 | 4.40 | OpenClaw-native agent/tool calling, scheduled tasks, MCP; thinking + streaming |
| `glm-4.7` | 200K / 128K | 0.60 | 0.11 | 2.20 | o3-level reasoning; chat full, responses/messages partial; `thinking` with `budget_tokens` |
| `glm-4.7-flashx` | 200K / 128K | 0.077 | 0.011 | 0.44 | fastest 4.7; chat/responses(partial)/messages(partial) |
| `glm-4.7-flash` | 200K / 128K | 0.07 | 0.01 | 0.40 | balanced; ~90% cheaper than 4.7 |
| `glm-4.6` | 200K / 128K | 0.60 | 0.11 | 2.20 | + web search **$0.01/call** (`extra_body={"web_search":True}`); chat |
Migration: `thinking.type:"disabled"` fails on GLM-5.3 → use `enabled` + `reasoning_effort:"low"`.
Params: `thinking{type:"enabled"|"disabled", budget_tokens?}`; `web_search`; `temperature` (default 0.6); `max_tokens` ≤128K. Use cases (4.6): AI coding (Python/JS/Java, IDEs Claude Code/Cline/OpenCode/Roo/Kilo), smart office (PPT), translation (fr/ru/ja/ko, informal), content generation, virtual characters, smart search/deep research. Best practices: thinking for complex tasks; 200K context; cached input (−82%); web search only when needed; temp 0.3–0.6 for code, 0.7–1.0 creative; structured outputs. Docs https://docs.z.ai/.
