# Aider + AvalAI (setup guide)
Aider = terminal pair-programming tool (chat about chosen files, edits them). Connect via its OpenAI-compatible provider directly to AvalAI. Start in **ask mode**, no auto-commits, no repo map; enable editing deliberately. Validated vs official Aider docs 2026-09-08; no live session run, nothing installed/executed.

## 1. Install
`python3 -m pip install aider-install; aider-install; aider --version` (official installer creates a separate Python env; check Python/OS requirements). Record the version for team use. First session in a throwaway project with a harmless `README.md`, not a company repo containing secrets.

## 2. Keep base URL + key private
`mkdir -p "$HOME/.config/aider"`; create `~/.config/aider/avalai.env` (don't commit; don't paste real key into shell commands):
```dotenv
OPENAI_API_BASE=https://api.avalai.ir/v1
OPENAI_API_KEY=<dedicated AvalAI key>
```
`chmod 600 "$HOME/.config/aider/avalai.env"`. Variable name is **`OPENAI_API_BASE`** (NOT `OPENAI_BASE_URL`). If your shell already exports `OPENAI_API_BASE`/`OPENAI_API_KEY` for another service, unset them in this session first; don't guess credential precedence.

## 3. Chat-only session
```bash
aider --env-file "$HOME/.config/aider/avalai.env" \
  --model openai/gpt-5.4-mini --weak-model openai/gpt-5.4-mini \
  --chat-mode ask --map-tokens 0 \
  --no-auto-commits --no-dirty-commits README.md
```
`openai/` prefix selects Aider/LiteLLM's OpenAI-compatible adapter — the AvalAI model id is plain `gpt-5.4-mini` (don't send Aider's prefix to AvalAI). Set main AND weak model; other modes (architect, edit) may use other models → configure separately. `--chat-mode ask` = conversation without auto-edits (NOT a file/network sandbox); `--map-tokens 0` disables repo map for the first test; `--no-auto-commits --no-dirty-commits` stop automatic commits of generated or pre-existing changes. AvalAI lists the model for Chat Completions; Aider compatibility also depends on model metadata and edit format — an accepted HTTP request doesn't prove edit quality.

## 4. First request
"Summarize the purpose of README.md in one sentence. Do not edit files, run commands, or suggest installing anything." Verify the answer matches the file and source is unchanged: `git status --short; git diff`. Aider may still create config/history files (`.aider*`) → protect them; don't commit private history; inspect `.aider.conf.yml` and project commands before trusting a repo (CLI flags aren't a complete security boundary). When ready to edit: do the coding-agent mini exercise (guides/coding-agent-workflows, not captured), choose coding mode explicitly, review diffs, run tests yourself; don't enable `--yes-always` in trial stage.

## Troubleshooting
Request goes to another service → check `OPENAI_API_BASE`, inherited shell vars, chosen env file. 401/403 → dedicated key, account access, stray whitespace (don't print the env file in diagnostics). Model not found → use `openai/gpt-5.4-mini` (exact AvalAI id after prefix). Capacity/cost warning for unknown model → read Aider's model-warnings docs; don't hide the warning or invent metadata; check AvalAI model list/pricing. Chat OK but edits not → edit format/model ability ≠ API compat; try a small file, review proposed diff. High usage → fewer files/shorter history, keep repo map off at first; check AvalAI usage, not just local cost estimate. Voice/image features → separate routes; chat URL doesn't configure STT or media generation.

## Defects
- None noted beyond: no live verification; `gpt-5.4-mini` listed for Chat Completions only per this guide.
