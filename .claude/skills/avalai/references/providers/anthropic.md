# Anthropic (Claude) provider page (docs: /fa/providers/anthropic)

Two integration styles: OpenAI-compatible SDK (`base_url=https://api.avalai.ir/v1`, `/v1/chat/completions`) or official Anthropic SDK (`base_url="https://api.avalai.ir"` — **no `/v1`**, `/v1/messages`). Since June 2025 the Anthropic SDK can also reach OpenAI, Bedrock, Vertex, Gemini models (see messages.md). Verify ids vs 10-deprecations.md + `/v1/models` (Claude 3.x/4.0/4.1 removed).

## Base-model namespaces (smart routing)
Plain ids (`claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-sonnet-4-5`, `claude-haiku-4-5`, and newer `claude-opus-5`, `claude-opus-5-5`, `claude-sonnet-5`, `claude-sonnet-5-5`, `claude-fable-5-1`) route across Anthropic, AWS Bedrock, GCP, Azure: up to ~10× rate limits, automatic failover, Bedrock-equal pricing, trivial migration. Full Bedrock ids (e.g. `global.anthropic.claude-opus-4-8`, `anthropic.claude-opus-4-6-v1`, `anthropic.claude-sonnet-4-5-20250929-v1:0`, `anthropic.claude-haiku-4-5-20251001-v1:0`) still work; migrating to base ids is recommended.
Context per base id: opus-4-8/4-7 1M native; opus-4-6, sonnet-4-6 1M (beta); sonnet-4-5, haiku-4-5 200K.

## 1M-token context
Native 1M on Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 5, Opus 4.8/4.7/4.6, Sonnet 4.6 (current routes); some routes (and Sonnet 4.5) still need header `anthropic-beta: context-1m-2025-08-07` (raw HTTP header; OpenAI SDK `extra_headers={"anthropic-beta": …}`).

## Beta headers
| feature | header | notes |
|---|---|---|
| computer use | `computer-use-2025-01-24` | latest Claude 4.5+ (⚠ Opus 5.5: Anthropic no longer accepts `computer_20251124` on Claude API/Google Cloud) |
| token-efficient tools | `token-efficient-tools-2025-02-19` | 4.5+ |
| interleaved thinking | `Interleaved-thinking-2025-05-14` | 4.5+ |
| 128K output | `output-128k-2025-02-19` | Opus 5, 4.8, 4.7, 4.6, Sonnet 4.6 (Opus 5 native) |
| 1M context | `context-1m-2025-08-07` | Opus 4.8/4.7/4.6, Sonnet 4.6/4.5 |
| context management | `context-management-2025-06-27` | Sonnet 4.5, Haiku 4.5 |

## Models (USD per 1M tokens)
| model id | ctx in / max out | in | cached | cache-write | out | access / endpoints |
|---|---|---|---|---|---|---|
| `claude-sonnet-5-5` | 1M / 128K | 2.00 | 0.20 | **4.00** (not upstream 2.50) | 10.00 | tier ≥1; chat+messages full, responses **partial** |
| `claude-opus-5-5` | 1M / 128K | 4.00 | 0.20 | **8.00** (not upstream 5.00) | 20.00 | tier ≥1; chat/messages/responses **full** |
| `claude-fable-5-1` | 1M / 128K | 10.00 | 0.25 | 12.50 | 50.00 | **tier ≥2**; chat+messages full, responses partial |
| `claude-opus-5` | 1M / 128K | 5.00 | 0.50 | 6.25 | 25.00 | tier ≥1; chat+messages full, responses partial |
| `claude-opus-4-8` | 1M native | 5.00 | 1.50 | 6.25 | 25.00 | chat+messages full, responses partial |
| `claude-opus-4-7` | 1M | 5.00 | 1.50 | 6.25 | 25.00 | tier ≥1 |
| `claude-opus-4-6` | 1M (beta) | 5.00 (>200K: 10.00 in / 37.50 out) | 1.50 | 6.25 | 25.00 | tier ≥1 |
| `claude-sonnet-4-6` | 1M (beta) | 3.00 | 1.50(sic) | 3.75 | 15.00 | chat+messages full, responses partial |
| `claude-sonnet-4-5` | 200K | 3.00 | 0.30 | — | 15.00 | |
| `claude-haiku-4-5` | 200K | 1.00 | — | — | 5.00 | chat+messages |
(Page cached-price for Opus 4.x/Sonnet 4.6 shown as 1.50 looks inconsistent with Anthropic's 0.5/0.3 pattern — verify with `/v1/models/{id}`. AvalAI cache-write prices for 5.5 differ from upstream and cache TTL isn't specified.)

### Per-model notes
- **Sonnet 5.5** (news 2026-09-30): scoped coding, debugging, docs/slides/sheets; Opus 5.5 better for open-ended judgment. Upstream claims >30% faster output and ≤30% lower cost per task than Sonnet 5 (not AvalAI guarantees). Reasoning: adaptive thinking + supported effort; Anthropic default effort `high` (Platform) / `medium` (Claude apps/Code) — don't assume Opus 5.5's default. Migration: previously disabled thinking → use new `between_tools` setting (disables thinking at turn start only; see Anthropic migration guide). Preserved thinking account-dependent: keep signed thinking blocks + full assistant/tool turns. **Don't send** `temperature`, `top_p`, prefill, forced tool use, copied fixed `budget_tokens`. Endpoint access ≠ Batch / Fast mode / computer-use schema / hosted tool permission.
- **Opus 5.5** (news 2026-09-24): long-running coding agents, repo migrations, audits, research. Upstream claims lower cost and faster output than Opus 5. Knowledge cutoff June 2026. **Thinking cannot be disabled** (adaptive always on; default effort `medium`; control via `output_config.effort`). No fixed thinking budget, no temperature/top_p, no prefill. **Forced tool use errors** → never require a tool call/force a specific tool. Thinking blocks are conversation/model-specific: keep complete assistant content, signatures, tool-call context unedited; don't move across conversations. Between-tool text now arrives in thinking blocks (display empty by default) → use tool-status events for progress. Hosted tools, computer-use schema, beta headers, Fast mode, Batch need separate route support; provider's 300K-output Batch beta ≠ the usual 128K cap.
- **Fable 5.1** (news 2026-09-02): new general flagship (advanced coding, knowledge work, science, computer use, long agents); cached input −75% vs Fable 5. Adaptive thinking always on; effort incl. `xhigh`, `max`. Tools, native structured outputs + response schema, prompt caching, mid-conversation system messages, output config.
- **Opus 5** (news 2026-07-27): flagship Opus for hard SWE, knowledge work, computer use, science, long agents; keeps Opus 4.8 rates ($5/$25) but cached input $0.50. Adaptive thinking; native structured output.
- **Opus 4.8**: ex-flagship; 1M native, 128K out, adaptive thinking, mid-conversation `role:"system"` messages (keep cache hits), public `stop_details` on refusals, **min cacheable prompt 1,024 tokens**, default effort `high` everywhere (levels low/medium/high/xhigh/max), cutoff May 2026; Online-Mind2Web 84%; ~4× less likely than 4.7 to gloss over flaws in own code. **Inherited API limits**: sampling params (`temperature`, `top_p`, `top_k`) not supported on Messages (non-default → 400); extended thinking budgets unsupported → `thinking:{"type":"adaptive"}` + `effort`.
- **Opus 4.7**: cutoff Apr 2026; hi-res vision (≤2,576 px long edge, ~3.75 MP, >3× earlier); new `xhigh` effort; task budgets (beta); better instruction following; filesystem memory.
- **Opus 4.6**: 1M (beta), cutoff 2026-02-06, 128K out, adaptive thinking, effort low/medium/high/max, context compaction, agent teams (Claude Code); premium pricing >200K.
- **Sonnet 4.6**: cutoff 2026-02-19; near-Opus quality at Sonnet price; computer use; adaptive+extended thinking; compaction beta.
- **Sonnet 4.5**: 200K; cutoff 2025-09-29; best coding of its time; long autonomous runs.
- **Haiku 4.5**: 200K; cutoff Oct 2025; fast/cheap; real-time chat, pair programming; chat+messages only.

## Code
```python
# OpenAI SDK
client.chat.completions.create(model="claude-opus-5-5", max_completion_tokens=8192, messages=[…],
    extra_body={"thinking":{"type":"adaptive"}, "output_config":{"effort":"medium"}})
# Anthropic SDK (no /v1)
from anthropic import Anthropic
c = Anthropic(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir")
c.messages.create(model="claude-sonnet-5-5", max_tokens=4096, thinking={"type":"adaptive"}, output_config={"effort":"high"}, messages=[…])
```
Anthropic SDK can call non-Claude ids: `model="gpt-5.4"`, `model="gemini-3.7-flash"` (page example id). Go: `option.WithBaseURL("https://api.avalai.ir")` + `anthropic.NewClient`; (page Go sample `anthropic.F(...)` style belongs to older SDK versions — verify); Ruby: `Anthropic::Client.new(api_key:, base_url:)` (`client.messages(...)` per page). TS: `new Anthropic({apiKey, baseURL:"https://api.avalai.ir"})`.

## Capabilities (usage patterns)
- Vision: Opus/Sonnet/Haiku accept `image_url` parts in chat completions.
- Tools: page shows legacy XML-in-system-prompt example for tools — **prefer standard `tools` parameter** (OpenAI-format function calling works; AvalAI converts).
- Structured output: ask for JSON in system prompt, or native structured outputs/response schema on newer models.
- XML tags help structure outputs; few-shot examples help; clear system prompts.
- Differences vs OpenAI: Claude native tool format XML/JSON conversion handled by AvalAI; system-prompt conventions; parameter support differs (see model quirks above).

## Model selection
Hardest coding/research/long-run: Fable 5.1 (then Opus 5.5 / Opus 5); cost-sensitive frontier: Opus 5; simpler tasks: Haiku 4.5; real-time: Haiku 4.5; enterprise/coding mid: Sonnet 4.6/5.5; general chat: Sonnet; vision: Opus. (Page comparison table still lists Opus 4.8/4.7 as top picks.) Context 200K–1M by model.

## Source defects
- Page's own example `claude-sonnet-5` ids in 4.6 sections (and `claude-opus-5` in 4.8 sections) mismatch headings; `claude-sonnet-4-5` listed in alias list but check deprecations.
- Responses-equivalent blocks swap Claude for `gpt-5.6-luna` (copy artifacts).
- Gemini id `gemini-3.7-flash` in Anthropic-SDK example vs v1beta page's `gemini-3.8-flash` — verify.
