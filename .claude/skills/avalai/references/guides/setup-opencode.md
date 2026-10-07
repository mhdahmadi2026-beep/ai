# OpenCode + AvalAI (setup guide)
OpenCode = terminal coding agent; AvalAI does model processing only. OpenCode (not AvalAI) controls file access, shell commands, plugins, sharing. Validated vs official OpenCode docs 2026-09-08; no live key session run, nothing installed/executed.

## 1. Install
`pnpm install -g opencode-ai; opencode --version` (or OS-specific method from the official install guide). Record the tested version before team use. First session in a throwaway project WITHOUT secrets. OpenCode may read repo instructions/config/plugins → inspect an unknown repo before opening it.

## 2. Provider config
MERGE (don't overwrite) into `~/.config/opencode/opencode.json`; a project-level `opencode.json` can override global values → check both.
```json
{
  "$schema": "https://opencode.ai/config.json",
  "model": "avalai/gpt-5.4-mini",
  "small_model": "avalai/gpt-5.4-mini",
  "share": "disabled",
  "permission": {"*": "ask", "external_directory": "deny"},
  "provider": {"avalai": {"npm": "@ai-sdk/openai-compatible", "name": "AvalAI",
    "options": {"baseURL": "https://api.avalai.ir/v1"},
    "models": {"gpt-5.4-mini": {"name": "AvalAI GPT-5.4 mini", "limit": {"context": 272000, "output": 128000}}}}}
}
```
Uses `@ai-sdk/openai-compatible` → `/v1/chat/completions` (NOT `@ai-sdk/openai`, which is the Responses adapter). Set both `model` and `small_model` so side tasks don't silently pick another model. `limit` values are CAPACITY from AvalAI listing (2026-09-08), not a per-task output budget; recheck model list before swapping models (tools, vision, context, output cap).

## 3. Key + model
In project dir run `opencode`: `/connect` → **Other** → provider id exactly `avalai` → paste dedicated AvalAI key → `/models` → pick "AvalAI GPT-5.4 mini". `/connect` stores only a local secret; it does NOT set base URL or model. Protect OpenCode's credential store + backups; never put a real key in `opencode.json`. Secret-manager option: `options.apiKey: "{env:AVALAI_API_KEY}"` (env var must be available to the OpenCode process; use ONE credential method). `avalai/gpt-5.4-mini` = OpenCode provider/model selector; the request to AvalAI uses plain `gpt-5.4-mini` (differs from 9Router's prefixed id).

## 4. First tests
1 `Reply with exactly: AvalAI connected` / "Do not use tools or read files." 2 name a non-sensitive file → ask it to read it and explain a function; approve only that read; check the answer reflects real content. Text reply proves model processing only; file read tests the separate agent/tool path. Then run the coding-agent mini exercise (guides/coding-agent-workflows — not yet captured) before enabling edits. Config asks for approval on tools and denies access outside the working directory. Don't start with `--auto` or auto-approve (changes `ask` behaviour). Permissions/commands ≠ OS sandbox → use throwaway workspace + least-privilege credentials.

## 5. Optional features (test separately)
Tools: need model function calling + compatible schema + OpenCode permission. Vision: model support + image input format. Responses: different adapter — don't switch adapters to fix an unrelated auth error. Embeddings, images, audio, web search, MCP: not auto-configured by the language provider. 9Router: separate provider (different base URL, client-side key, prefixed ids) → guides/setup-9router.

## Troubleshooting
Provider missing in `/models` → `provider.avalai.models` exists + credential provider id equals `avalai`. 401/403 → dedicated key/account access (don't print credential file). 404 → base URL exactly one `/v1` + Chat Completions adapter. Unexpected model/permission → project config, profiles, plugins, managed settings overriding global. Tool call shown as text → function calling, adapter, try one simple read-only tool. Context/output error → recheck model-list capacities; reduce context, fresh narrowly scoped session. High usage → agent loops + small model make extra requests; check AvalAI usage (local estimate isn't billing).

## Defects
- `limit.output: 128000` is capacity; setting it as OpenCode's per-request output may cost/timeout.
- Link `/fa/guides/coding-agent-workflows` still uncaptured.
