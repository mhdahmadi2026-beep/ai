# Setup: Claude Code with AvalAI

Source: docs.avalai.ir/fa/guides/setup-claude-code (Persian). AvalAI natively serves the Anthropic Messages API (`/v1/messages`, see api-reference/messages.md) → no LiteLLM/proxy needed for Claude (and many other) models.

## Install
- macOS/Linux/WSL: `curl -fsSL https://claude.ai/install.sh | bash`
- Windows: Node.js ≥18, admin PowerShell, `npm install -g @anthropic-ai/claude-code` (npm also works on macOS/Linux/WSL). Check: `claude --version`.

## Direct config (recommended) – env vars
```bash
export ANTHROPIC_BASE_URL="https://api.avalai.ir"      # NO /v1
export ANTHROPIC_AUTH_TOKEN="$AVALAI_API_KEY"
export ANTHROPIC_MODEL="claude-opus-5"
export ANTHROPIC_SMALL_FAST_MODEL="claude-haiku-4-5"   # cheap background tasks (titles, summaries)
```
Persist in `~/.zshrc` / `~/.bashrc` (then `source`). Never commit the key.

### Windows PowerShell
Session: set `$env:ANTHROPIC_BASE_URL`, `ANTHROPIC_AUTH_TOKEN`, **and `ANTHROPIC_API_KEY` = same AvalAI key** (otherwise a fresh install may still open the Anthropic browser login; answer **Yes** when Claude Code asks to use the detected custom API key), `ANTHROPIC_MODEL`, `ANTHROPIC_SMALL_FAST_MODEL`. Persist with `[Environment]::SetEnvironmentVariable(name, value, "User")`, then reopen PowerShell and `echo $env:ANTHROPIC_BASE_URL` to verify.

## Alternative: settings.json
`~/.claude/settings.json` (user) or `.claude/settings.json` (project):
```json
{ "env": { "ANTHROPIC_BASE_URL": "https://api.avalai.ir", "ANTHROPIC_AUTH_TOKEN": "...", "ANTHROPIC_API_KEY": "...", "ANTHROPIC_MODEL": "claude-opus-5", "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-4-5" } }
```
If the project file is committed, keep only non-secret values (base URL, model names); keep the key in the environment.

## Run / verify / override
`cd project && claude`. In session: `/status` (active endpoint+model), `/model` (list/switch). One-off: `claude --model claude-sonnet-5` or `ANTHROPIC_MODEL=claude-opus-5 claude`. If still hitting Anthropic: base URL exactly `https://api.avalai.ir`, log out of any Anthropic account, check `/status`.

## Non-Claude models
Set `ANTHROPIC_MODEL` to e.g. `glm-5.2`, `kimi-k2.7-code`, `gemini-3.1-pro-preview`, `gpt-5.6-luna` (docs sample has typo `ANTHROPIC_model` – variable names are upper-case). Most work via `/v1/messages` but compatibility (message format, tool calling) is NOT guaranteed per model → try another model or contact AvalAI support (t.me/AvalAISupport). Proxy/LiteLLM only for models that are OpenAI-chat-only (rarely needed).

## Model picks (docs; verify via /v1/models)
- Deep: `claude-opus-4-8` / `claude-opus-5`, `claude-sonnet-5`, `gpt-5.5`
- Fast: `claude-haiku-4-5` (good small-fast model), `claude-sonnet-5`, `kimi-k2.7-code`
- Cheap: `glm-5.2`, `gemini-3.1-pro-preview`
- Pair strong main + cheap small-fast model to balance cost.
- Ids inconsistent across docs (`claude-opus-4-8` vs `claude-opus-5`); `claude-haiku-4-5` may no longer be available (Claude packages historical) – verify.

## Best practices
Key from env; git checkpoints; `CLAUDE.md` in repo; watch rate limits; monitor usage in dashboard.

## Troubleshooting
- Auth: `echo $ANTHROPIC_AUTH_TOKEN` (PowerShell `$env:...`), first-run Windows also `ANTHROPIC_API_KEY`; reopen terminal; key active.
- Still going to Anthropic: see above.
- Connection: firewall/proxy to api.avalai.ir.
- Model not found: check id, try `claude-opus-4-8` / `claude-sonnet-5`; see news page.
- Tool calling broken: pick a model with tool support; Claude models support tools on Messages API; report non-Claude cases to support.
- 429: tiers/rate limits.
