# xAI (Grok) provider page (docs: /fa/providers/xai)

Base `https://api.avalai.ir/v1` chat completions. ⚠ Sections on Grok 3/2 use old ids; verify vs deprecations.

## Newest
- **`grok-4.7`**: coding/knowledge work, long-horizon engineering agents, documents/presentations; ctx list max in 500,000 / out 500,000 (separate caps, not simultaneous); vision, reasoning, tools, structured output, prompt cache; **chat+messages full, responses partial**; not an image generator. Prices ≤200K input: in $2.00 / cached $0.50 / out $6.00; >200K: $4.00 / $1.00 / $12.50 (same as 4.6; tier by input length, not related to a Fast variant). **Don't send `reasoning_effort` initially**; test tool round-trips/structured output/conversation continuation before moving to Responses (partial ≠ hosted tools/stateful parity). No auto-upgrade from 4.6, no separate Fast route, no invite-only offensive-security access. News 2026-09-24.
- **`grok-4.6`** (news 2026-09-11): long-horizon agents, large codebases, knowledge work; interactive/visual project building (not image gen); 500,000/500,000; chat/messages/responses(partial); same prices as 4.7; don't assume Grok 4.5's 1M window.
- **`grok-4.5`**: 1,000,000 ctx; in 2.00/cached 0.50/out 6.00 (>200K 4.00/1.00/12.50); chat + responses(partial); engineering agents, Office-style docs.
- **`grok-4.3`** (alias `grok-4.3-latest`): 1M ctx; chat only; in 1.25 / cached 0.20 / out 2.50 (>200K 2.50/0.40/5.00); reasoning, function calling, structured output.
- **`grok-4`** (`grok-4-latest`, `grok-4-0709`): 256K; vision, functions, structured, reasoning; 3.00 / 0.75 / 15.00. Vision images as base64 recommended.
- **Grok 4.20 stable**: `grok-4.20-reasoning`, `grok-4.20-non-reasoning` — 2M ctx; vision, functions, structured; 2.00 / 0.20 / 6.00 (>200K 4.00/0.40/12.00); lowest hallucination, strict prompt adherence. Beta ids: `grok-4.20-beta-0309-reasoning` (aliases `grok-4.20-beta`, `-0309`, `-latest`, `-latest-reasoning`, `-reasoning`), `grok-4.20-beta-0309-non-reasoning` — same prices.
- **Grok 4.1 Fast**: `grok-4-1-fast-reasoning`, `grok-4-1-fast-non-reasoning` — 2M ctx; vision, functions, structured; 0.20 / 0.05 / 0.50 (75% cache discount); agentic tool calling.
- **Grok 4 Fast**: `grok-4-fast-reasoning` (aliases `grok-4-fast`, `-latest`), `grok-4-fast-non-reasoning` (`-latest`) — 2M; 0.20/0.05/0.50; live search $25 per 1K sources; function-calling example uses reasoning id.
- **`grok-code-fast-1`**: agentic coding; 190+ tokens/s, >90% cache hit; 0.20 / 0.02 / 1.50; TS, Python, Java, Rust, C++, Go; chat/responses/messages.
- **Grok 3 series**: `grok-3-latest` (131,072; 0.30?/15.00 — page prints in $0.30 vs usual $3; verify), `grok-3-fast` (5.00/25.00), `grok-3-mini` (0.30/0.50), `grok-3-mini-fast-beta` (0.60/4.00). Vision: only `grok-2-vision-latest` actually supports vision (Grok 3 vision flag not yet fully enabled) → send base64 images. Grok 2 (`grok-2-latest`, `grok-2-vision-latest`) legacy.

## Notes
Function-calling uses standard OpenAI `tools`. Live Search via direct xAI only (real-time info). Grok 4.7 model pages: fa/models/grok-4.7, guides fa/guides/reasoning, pricing.

## Audit addendum — ids and aliases
`grok-4-fast-reasoning` (aliases `grok-4-fast`, `grok-4-fast-reasoning-latest`) and `grok-4-fast-non-reasoning` (+`-latest`): 2,000,000 ctx. `grok-4.20-beta-0309-reasoning` (aliases `grok-4.20-beta`, `grok-4.20-beta-0309`, `-latest`, `-latest-reasoning`, `-reasoning`): 2,000,000 ctx. Newer: `grok-4.7`, `grok-4.6`, `grok-4.5`, `grok-4.3`, `grok-4.1-fast-*`. Verify live — aliases change.
