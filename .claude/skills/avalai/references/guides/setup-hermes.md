# Hermes Agent + AvalAI (setup guide)
Hermes Agent (NousResearch; terminal/messenger agent with tools, resumable sessions, gateways) can use AvalAI as a **named OpenAI-compatible provider**. AvalAI only authenticates model requests; Hermes separately controls files, commands, network, ports. A valid key doesn't make tool/filesystem policy safe. Doc validated vs public sources 2026-08-06 (re-checked 2026-09-08: named provider, `key_env`, `chat_completions`, `/model custom:<name>:<model>` still documented). Not tested with a real key/container.

## Prereqs
Linux/macOS/Windows via WSL2; recent Hermes; dedicated AvalAI key (separate from other apps); model with **≥64,000 input tokens** (Hermes rejects smaller context for agent work) and all needed capabilities. Sample model `gpt-5.4-mini` (listed: Chat+Responses, streaming, tools, structured output, vision, 272,000 input). Check: base `https://api.avalai.ir/v1`; safest route `/v1/chat/completions`; optional `/v1/responses`. Model id, API route, capabilities are 3 separate checks (listed in `/v1/models` ≠ supports every endpoint/tool). AvalAI does NOT support `gpt-transcribe` / `gpt-live-transcribe` for this (don't import upstream samples using them — contradicts audio guides; verify).

## Install
Official install guide; `hermes --version`; `hermes doctor`. Secrets in `~/.hermes/.env`, non-secret config in `~/.hermes/config.yaml`; never put the key in project scripts.

## Connect
Interactive: `hermes model` (outside an active session) → "Custom endpoint (self-hosted / VLLM / etc.)": base `https://api.avalai.ir/v1`, key, model `gpt-5.4-mini`, API mode `chat_completions`, context `272000`.
Named/auditable:
```dotenv
# ~/.hermes/.env
AVALAI_API_KEY=...
```
```yaml
# ~/.hermes/config.yaml
providers:
  avalai:
    api: https://api.avalai.ir/v1
    key_env: AVALAI_API_KEY
    transport: chat_completions
    default_model: gpt-5.4-mini
    models:
      gpt-5.4-mini: {context_length: 272000, supports_vision: true}
```
`key_env` = which env var holds the secret; never inline `api_key` in config/backups/images/shared logs.
Optional Responses (separate provider, only after seeing `/v1/responses` for the model): `providers.avalai-responses` with `transport: codex_responses` (Hermes' transport name; doesn't prove all models/servers support Responses).

## Verify in order
`hermes doctor` → run `hermes`, confirm provider+model in banner → simple prompt + dependent follow-up → (if function calling) read-only task (list current dir; don't start with writes/shell changes) → exit and `hermes --continue` → only then in-session `/model custom:avalai:gpt-5.4-mini`. Add/change providers via `hermes model` in a terminal; `/model` only switches among already configured providers.

## Capability map
Chat Completions: direct, start here. Responses, streaming, system messages/sampling, tools + structured output, vision: model/route dependent (set `supports_vision:true` only for verified vision models; unsupported params may be rejected/ignored). Embeddings/RAG: not from the main provider; image gen, STT/TTS, web search/browser automation: separate Hermes backends/credentials/billing; Realtime audio and video: no verified mapping. Auxiliary models (vision analysis, web summarization, image, audio, browser, memory, gateway) may have separate config/billing — check each active provider before assuming the AvalAI key is used.

## Docker Compose (official files, tag `v2026.8.3`)
```bash
git clone https://github.com/NousResearch/hermes-agent.git && cd hermes-agent && git checkout v2026.8.3
HERMES_UID="$(id -u)" HERMES_GID="$(id -g)" docker compose up -d --build
docker compose exec gateway hermes doctor
docker compose logs --tail=100 gateway dashboard
```
Compose: builds local image from checked-out source; mounts host `~/.hermes` → `/opt/data` (config + sessions persist); aligns service user with UID/GID; dashboard host-network bound to `127.0.0.1`; OpenAI-compatible API server OFF until BOTH `API_SERVER_HOST` and `API_SERVER_KEY` set. Don't expose dashboard with `--insecure --host 0.0.0.0` (use SSH tunnel or TLS+auth ingress); don't enable messenger gateway before an explicit user allowlist.

## Safe operation
Mount only needed workspace; keep `.env`, auth store, sessions, backups owner-readable only; keep dashboard/gateway private (strong separate `API_SERVER_KEY` if API server on); review terminal/browser/network/messenger permissions, disable unneeded tools; strip Authorization headers, prompts, responses, file contents, personal data from diagnostics; monitor AvalAI usage/rate limits (retries/auxiliary models create hidden requests). Upgrade: `docker compose stop`; record `git rev-parse HEAD`; `tar -czf hermes-data-backup.tgz -C "$HOME" .hermes`; `docker compose start`; upgrade = checkout vetted tag + rebuild; rollback = stop, checkout recorded revision, rebuild, restore backup only if data migration needed (test restore on a copy first).

## Troubleshooting
401/403 → key env/file ownership/account (run doctor, check `key_env` without printing secret). 404 → base URL/transport (keep `/v1`; `chat_completions` unless model supports Responses). Model not found → exact id + named-provider (`/v1/models`, `/model custom:avalai:...`). Context error at start → metadata <64K → bigger model or fix `context_length`. Tool call shown as text → model compat/tool schema → verify function calling, limit to one read-only tool. Chat works but vision no → `supports_vision`, input shape, auxiliary routing. Empty/garbled stream → Chat vs Responses mismatch/proxy buffering → plain non-stream chat, enable layers one by one. Session won't resume → data path/volume ownership (`~/.hermes` → `/opt/data`, UID). Root-owned files in container → UID/GID mapping or modified entrypoint → use official Compose and don't replace `/init`.

## Defects
- "Validated 2026-08-06" but "tag v2026.8.3" and "Compose label is the earlier verified sample, not latest release claim".
- Statement that AvalAI doesn't support `gpt-transcribe`/`gpt-live-transcribe` conflicts with audio guides which list them as current STT models (03-ai-workflows also warned) — treat as unverified; check `/v1/models`.
- Links to coding-agent-workflows / ai-workflows guides not yet captured (03-ai-workflows.md exists).
