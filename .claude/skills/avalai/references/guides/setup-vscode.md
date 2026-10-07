# Setup: VSCode extensions / Cursor with AvalAI

Source: docs.avalai.ir/fa/guides/setup-vscode (Persian). Applies to GitHub Copilot (BYOK), Continue, other OpenAI-compatible extensions, Cursor.

## Connection values
- OpenAI-compatible (all models): Base URL `https://api.avalai.ir/v1`, key = AvalAI key (Bearer).
- Native Anthropic / Gemini profiles: Base URL `https://api.avalai.ir` (NO `/v1`); only that provider's models.
- Key is shown once at creation; never commit it; prefer env vars / credential store.

## GitHub Copilot (VS Code BYOK)
### Method 1 – UI
Chat view → gear (Manage Language Models) or Command Palette `Chat: Manage Language Models` → Add Models → Custom Endpoint / OpenAI Compatible → Group Name `AvalAI`, Base URL `https://api.avalai.ir/v1`, API Key, API Type **Chat Completions** → save (restart VS Code if needed) → pick model in Copilot Chat picker.
### Method 2 – settings.json
```json
{
  "github.copilot.chat.customOAIModels": [
    { "modelId": "claude-opus-5", "displayName": "AvalAI Claude Opus", "endpoint": "https://api.avalai.ir/v1", "apiKey": "YOUR_AVALAI_KEY" }
  ]
}
```
(Docs sample is inconsistent: modelId `claude-opus-5` vs displayName "Opus 4.8". Verify the real id via `/v1/models`. The settings schema may differ by VS Code version; Method 1 is the safer path.)
### Method 3 – broker extension
Marketplace extensions like "Copilot Custom Provider" / "LM Custom Provider": run their setup from Command Palette, enter base URL + key, add models manually.

## Continue
Sidebar gear → edit config:
```json
{ "models": [ { "title": "AvalAI Claude Sonnet", "provider": "openai", "model": "claude-sonnet-5", "apiKey": "YOUR_AVALAI_KEY", "apiBase": "https://api.avalai.ir/v1" } ] }
```
Multiple entries = multiple profiles (fast / deep reasoning / cheap). Newer Continue versions use `config.yaml` (same fields: provider openai, apiBase, apiKey, model) – the JSON form is the docs' version.

## Other OpenAI-compatible extensions
Provider "OpenAI"/"OpenAI Compatible" → Base URL `https://api.avalai.ir/v1` → key → model id → send a test request.

## Cursor
Settings → Features → Models → Add Model; provider OpenAI, override Base URL `https://api.avalai.ir/v1`, key, model name (e.g. `gpt-5.5`, `claude-opus-4-8`). Note: Cursor's override applies to its OpenAI-style models; verify model ids via `/v1/models`.

## Model picks (docs; verify availability)
- Deep reasoning / large codebases: `claude-opus-4-8`, `gpt-5.5`, `claude-sonnet-4-6`
- Fast daily: `gpt-5.5`, `gemini-2.5-flash`, `claude-sonnet-4-6`
- Cheap: `deepseek-v4-flash` (free tier), `qwen-2.5-coder-32b-instruct`, `gemini-3.5-flash`, `kimi-k2.7-code`
- Specialist: `deepseek-v4-pro` (redirects to `deepseek-v4.1-flash` since 2026-09-14), `codestral-latest` (autocomplete)
- Docs model ids are inconsistent (`claude-opus-5` vs `claude-opus-4-8`, `gpt-5.6-luna`, `claude-sonnet-5` vs `claude-sonnet-4-6`): always confirm against live `GET /v1/models`.

## Troubleshooting
- Invalid key: re-copy, no whitespace, key active in dashboard.
- Connection: firewall/proxy to `api.avalai.ir`; Base URL must end with `/v1` (OpenAI mode).
- Model not found: wrong id or not in your tier; test with a common id.
- Slow: faster model (gemini-3.5-flash, gpt-5.4-mini), trim context.
- 429: see guides/rate-limits.md; wait/retry, upgrade tier.
- Extension ignores config: restart VS Code; check the extension supports custom OpenAI endpoints.

## Related
Related docs listed: api-reference/introduction, models/model-details, guides/rate-limits, guides/best-practices (coding assistants), guides/model-selection – not yet captured (best-practices, model-selection).
