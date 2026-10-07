# Setup: OpenAI Codex (CLI / IDE extension) with AvalAI

Source: docs.avalai.ir/fa/guides/setup-codex (Persian). Codex supports custom model providers, so it can use any AvalAI model.

## Install
- macOS/Linux: `curl -fsSL https://chatgpt.com/codex/install.sh | sh`
- Windows: `powershell -ExecutionPolicy ByPass -c "irm https://chatgpt.com/codex/install.ps1 | iex"`
- or `npm install -g @openai/codex` / `brew install --cask codex`. CLI and IDE extension share the same config layers (IDE: gear → Codex Settings → Open config.toml).

## Key
Export `AVALAI_API_KEY` (bash/zsh: `export AVALAI_API_KEY=...` in rc file; Windows: `setx AVALAI_API_KEY "..."` then restart terminal). Codex reads it via `env_key`. Never put the key in config.toml / VCS; never print it in logs/tickets.

## ~/.codex/config.toml
```toml
model = "gpt-5.3-codex"
model_reasoning_effort = "medium"   # low | medium | high | xhigh (if model supports)
model_provider = "avalai"

[model_providers.avalai]
name = "AvalAI"
base_url = "https://api.avalai.ir/v1"
env_key = "AVALAI_API_KEY"

[projects."/abs/path/to/project"]
trust_level = "trusted"   # required for project-level config to load / fewer prompts
```
- Provider id must NOT be `openai`, `ollama`, `lmstudio` (reserved) → use `avalai`; `model_provider` must equal the `[model_providers.<name>]` table name.
- Config location: `~/.codex/config.toml` (or under `CODEX_HOME`).
- Base URL must include `/v1`.

## Responses API caveat (important)
Recent Codex sends requests ONLY to `v1/responses` (no more chat/completions). OpenAI models work fine; non-OpenAI models (Claude, Gemini, DeepSeek…) are chat-completions-compatible but `v1/responses` compatibility is best-effort and NOT guaranteed per model. If a non-OpenAI model misbehaves: try another model or contact AvalAI support (t.me/AvalAISupport). (Per this skill: Responses limits on AvalAI — no hosted background / WebSocket mode; see guides/background-processing.md, websocket-mode.md.)

## Run & override
```bash
cd /path/to/project && codex
codex --model claude-opus-4-8
codex --config model='"gemini-3.1-pro-preview"'   # value is TOML, not JSON
```
Switch models by changing `model` only (e.g. `claude-opus-5`, `gemini-3.1-pro-preview`, `deepseek-v4-pro`).

## Profiles
Per docs, a file `~/.codex/claude.config.toml` with `model`/`model_reasoning_effort` overrides, run `codex --profile claude`; layered over base config. (Docs' file-per-profile form differs from older Codex versions' `[profiles.x]` tables inside config.toml; check `codex --help`/official docs for your version.)

## Model picks (docs; verify with /v1/models)
- Complex/reasoning: `claude-opus-4-8`, `gpt-5.5`, `claude-sonnet-4-6`
- Fast agentic: `gpt-5.3-codex`, `gemini-3.1-flash` (not in the credit-package lists; verify exists), `claude-haiku-4-5`
- Cheap: `deepseek-v4-flash`, `qwen3-coder-next`, `gemini-3.5-flash`, `kimi-k2.7-code`
- Docs inconsistency: `claude-opus-4-8` vs `claude-opus-5`; `deepseek-v4-pro` redirects to `deepseek-v4.1-flash` since 2026-09-14.

## Best practices
Lower reasoning effort for simple tasks; git checkpoints before/after tasks; add `AGENTS.md` (build commands, conventions); watch rate limits (guides/rate-limits.md) and usage in dashboard; try different models per task.

## Troubleshooting
- Auth: env var present in the shell that launches Codex (restart terminal), key active, `env_key` equals variable name.
- "reserved provider ID": rename provider away from openai/ollama/lmstudio.
- Connection: firewall/proxy to api.avalai.ir; base_url exact.
- Odd non-OpenAI behavior: Responses compat (above).
- Model not found: check id; test `gpt-5.3-codex` / `claude-opus-4-8`.
- Config not loading: path, TOML syntax, project trusted.
- 429: rate limits/tier.
