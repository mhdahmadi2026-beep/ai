# avalai — Claude Code / agent skill for AvalAI

OpenAI-compatible gateway `https://api.avalai.ir/v1`. Built from the full AvalAI docs (https://docs.avalai.ir/fa/).

**Install (Claude Code):** copy this folder to `.claude/skills/avalai/` in your project (or `~/.claude/skills/avalai/` for all projects), e.g.
`git clone https://github.com/mhdahmadi2026-beep/ai /tmp/ai && cp -r /tmp/ai/.claude/skills/avalai .claude/skills/` (checkout branch `claude/elegant-heisenberg-31a212` until merged).
**Other agents (Cursor/Codex/etc.):** point them at `SKILL.md` (agent playbook at top) and `references/00-index.md`.

**Live data:** `python3 -I references/scripts/avalai_live.py check|price|cost|models|snapshot` — always verify prices/ids live (no API key needed). Env var for code: `AVALAI_API_KEY`.
Layout: `SKILL.md` (playbook + rules) · `references/` (docs by topic, news, examples, scripts) · `references/MISSING-PAGES.md` (what's not captured).
