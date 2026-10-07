# News 2026-09-30 (1405-07-08): GPT-6.1 Sol & Claude Sonnet 5.5 added (docs.avalai.ir/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added)

Both from tier 1. Model rows are in `../providers/openai.md`, `../providers/anthropic.md`, `../06-pricing.md`.

| id | chat | messages | responses | limits |
|---|---|---|---|---|
| `gpt-6.1-sol` | full | full | full | 922K in / 128K out |
| `claude-sonnet-5-5` | full | full | **partial** | 1M in / 128K out |

- gpt-6.1-sol: coding, document work, reasoning at lower token price than GPT-6 Astra; text+image in, text out, PDF, function calling, structured output, prompt cache. `none`/`minimal` reasoning efforts NOT supported by local metadata; don't carry old GPT default effort over. OpenAI's "Astra-level DeepSWE at ~1/5 cost" is an upstream claim.
- Price/1M: ≤272K input (inclusive): in 2.00 / cached 0.10 / cache-create 2.50 / out 10.00; >272K: 4.00 / 0.20 / 5.00 / 15.00. Tier is decided by TOTAL request input length and the higher tier applies to the WHOLE request (incl. output rate), not just excess tokens.
- claude-sonnet-5-5: scoped coding, debugging, docs, spreadsheets, slides; complements (not replaces) Opus 5.5. Price 2.00 / cached 0.20 / **cache-create 4.00 (AvalAI; not upstream 2.50)** / out 10.00; no long-context tier. Upstream claims >30% faster, up to 30% cheaper/task vs Sonnet 5 — not AvalAI guarantees.
- Sonnet 5.5 rules: effort default differs per product (Claude apps/Code `medium`, Platform `high`) → set effort explicitly; apps that disabled thinking must migrate to the new `between_tools` setting (disables only initial thinking) per Anthropic migration guide, verify on AvalAI route; preserve signed thinking blocks + full assistant/tool turns (account-dependent preserved thinking; check before moving conversations between accounts); do NOT send `temperature`, `top_p`, assistant prefill, forced tool_choice; use adaptive thinking rather than fixed `budget_tokens`. Prefer `/v1/messages` for Sonnet thinking controls; Responses partial ≠ hosted tools/stored state/background.
- Anthropic SDK base_url = `https://api.avalai.ir` (no /v1). Example: `thinking={"type":"adaptive"}, output_config={"effort":"high"}`, `max_tokens=4096`.
- No auto-aliasing/replacement of existing ids; check tier-1 access; re-test quality, tool loop, schema, latency, token use before shifting prod; keep output budget for reasoning; ask for short rationale, not hidden CoT; watch cache usage + real billed cost.
- Sample responses are illustrative (100 in/50 out → $0.0007 = 70 toman at example rate 100,000 toman/USD, `estimated_cost{unit,irt,exchange_rate}`).
