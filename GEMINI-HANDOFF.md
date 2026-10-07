# Handoff prompt for Gemini (Antigravity) — finish the AvalAI skill + MCP server

Paste everything below the line into Gemini. Gemini must run in an environment that CAN reach
`docs.avalai.ir`, `api.avalai.ir`, `status.avalai.ir` (the Claude cloud session could not).

---

You are continuing a project in repo `mhdahmadi2026-beep/ai` (public, MIT): a Claude Code skill + MCP server
for AvalAI (OpenAI-compatible gateway `https://api.avalai.ir/v1`). The user writes Persian: answer the user in
Persian, keep code/ids/file names in English.

## 0. Setup and rules
- Clone the repo, create/use a working branch, never push directly to `main`.
- First read: `AGENTS.md`, `.claude/skills/avalai/SKILL.md` (START HERE section),
  `.claude/skills/avalai/references/00-index.md`, `references/MISSING-PAGES.md`.
- Verify network first: `curl -s -o /dev/null -w '%{http_code}' https://docs.avalai.ir/fa/` and
  `https://api.avalai.ir/public/models` must return 200. If not, STOP and tell the user which host failed.
- Never commit API keys. `AVALAI_API_KEY` may or may not exist in the environment; never print it.
- Commit in logical chunks with clear messages. Keep fenced-code format of the existing files.
- Be faithful: copy facts (ids, prices, limits, dates, endpoints) exactly from the source pages; flag broken
  sample code instead of silently "fixing" it. Dates in docs are Jalali (write Gregorian in parentheses).

## 1. LIVE CATALOG
1. Save `https://api.avalai.ir/public/models` to
   `.claude/skills/avalai/references/live/public-models-<YYYY-MM-DD>.json`.
2. Generate `live-snapshot.md` with `python3 -I .claude/skills/avalai/references/scripts/avalai_live.py snapshot`.
3. Resolve the DeepSeek V4.1 Flash price conflict: docs news says $0.15 in / $0.003 cached / $0.60 out, while a
   models-explorer screenshot showed $0.3. Report the true live value and fix `06-pricing.md`,
   `providers/deepseek.md`, the news files and `SKILL.md`.
4. Diff live prices / ids / `min_tier` / `tier_rate_limits` / `supported_endpoints` against
   `06-pricing.md`, `11-tier-rate-limits.md`, `providers/*.md`, `10-deprecations.md`. Fix every discrepancy and
   mark the snapshot date.
5. Verify STT/TTS ids exist live: `gpt-transcribe`, `gpt-live-transcribe`, `gpt-audio-mini`,
   `gemini-3.8--tts` (note the double dash — check the exact live id). Fix `guides/speech-to-text.md`,
   `api-reference/audio.md`, `starters/voice-assistant.md` accordingly.

## 2. NEWS
Fetch every page under "Uncaptured news pages" in `references/MISSING-PAGES.md`
(`https://docs.avalai.ir/fa/news/<slug>`, also try the `.md` suffix). Write each as
`references/news/<slug>.md`: a complete, faithful, well-structured knowledge file (all ids, prices, endpoints,
migration notes, dates, caveats; keep correct code samples, flag broken ones) — not a thin summary.
Update `news/index.md` (captured column), `00-index.md` rows, `MISSING-PAGES.md`, and add important rules to
`SKILL.md`.

## 3. MODEL PAGES
Fetch `https://docs.avalai.ir/fa/models/<model-id>` for the top ~40 models (all current OpenAI, Anthropic,
Google, xAI, DeepSeek, Qwen, Kimi, GLM, Mistral ids from the live catalog). Store as
`references/models/<id>.md` with complete facts: context, limits, endpoints, params, quirks, pricing including
long-context tiers. Update `references/models/index.md`.

## 4. RE-VERIFY DOCS
Fetch the main docs pages (guides, api-reference, providers, pricing, rate-limits, deprecations, service-tiers,
credit-packages) and diff against `source-archive/` and the curated references. Update anything that changed;
replace `source-archive/` copies with the fresh ones where they differ (keep fenced-code format).

## 5. STATUS
Fetch `https://status.avalai.ir/` (and its API/history if available). Update `guides/service-status.md` with
real current data and the endpoint list.

## 6. TEST LIVE
- Run `python3 -I .claude/skills/avalai/references/scripts/avalai_live.py` (`check`, `price`, `cost`,
  `snapshot`) and `python3 mcp-server/avalai_mcp.py --selftest` against live data; fix bugs.
- Verify Responses vs Chat output shapes and the Laravel guide request shapes
  (`references/examples/laravel-complete-guide.md`) against `api-reference/` docs.
- Only if `AVALAI_API_KEY` is set: run one tiny real chat call and one embeddings call to validate examples.
  Otherwise skip and say so.

## 7. SEMANTIC INDEX (only with AVALAI_API_KEY)
Pick the cheapest suitable embedding model from the live catalog, run
`python3 mcp-server/build_index.py --dry-run`, show the cost estimate, then build with `--dimensions 512` only
if the cost is trivial (< $0.50) and commit `mcp-server/index/`. No key → document clearly that it was skipped.

## 8. SYNC + DOCS
- MCP corpus: new pages must be indexed automatically; confirm with `avalai_index_status`-equivalent selftest.
- Update READMEs (root, skill, `mcp-server/`) with what changed. Bump nothing secret.

## 9. Git / delivery
Push the branch, open a PR to `main`, and merge it (the repo owner authorized PR + merge). Use the `gh` CLI or
the GitHub web UI.

## 10. Final report (in Persian)
Concise: what was fetched/fixed, discrepancies found (especially prices), anything still blocked, and the repo
link https://github.com/mhdahmadi2026-beep/ai.
