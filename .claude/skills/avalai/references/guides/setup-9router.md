# 9Router + AvalAI (setup guide)
9Router = local OpenAI-compatible gateway; AvalAI is registered as an OpenAI-compatible upstream with a model PREFIX. Path: client ←→ local `http://localhost:20128/v1` ←→ prefixed provider node ←→ AvalAI. Two credentials, never interchange: AvalAI key (9Router→AvalAI) vs a downstream 9Router dashboard key (client→9Router). Use only when you need local gateway, prefixed model ids, multiple upstream connections, priority or controlled fallback; otherwise connect directly. Validated vs official sources 2026-08-06 (rechecked 2026-09-08: port 20128, `DATA_DIR=/app/data`, separate signing secrets + dashboard password still documented). Not run with real keys/images.

## Prereqs
Node 20+ & npm (local test) or Docker+Compose; dedicated AvalAI key; current model id + supported endpoint; strong dashboard password + independent random signing secrets; local `http://localhost:20128`; don't publish dashboard before changing credentials. Sample model `gpt-5.4-mini` (Chat + Responses, but in 9Router these are SEPARATE provider nodes). Check: base `https://api.avalai.ir/v1`; `/v1/chat/completions`; `/v1/responses`; gateway `http://localhost:20128/v1`. "Check" button only validates key/URL/API type/optional model at that moment — it does NOT create the persistent connection.
`gpt-transcribe`/`gpt-live-transcribe`: source says AvalAI doesn't support them → use model currently listed for `/v1/audio/*` (conflicts with audio guides; verify `/v1/models`).

## Install
`npm install -g 9router && 9router` → open `http://localhost:20128`. For production use the pinned Compose below, not the global package.

## Connect AvalAI
1 Providers → Add OpenAI Compatible; Name `AvalAI`; Prefix `avalai` (becomes part of every downstream model id); API type **Chat Completions** first (separate **Responses API** node only if the model supports `/v1/responses`); Base URL `https://api.avalai.ir/v1`; key in "API Key (for Check)"; optional Model ID `gpt-5.4-mini`; Check → create node.
2 Persistent connection (the Check key is temporary): provider AvalAI → Connections → Add Connection: Name e.g. `AvalAI production`, API Key (dedicated), Priority `1`, Proxy Pool `None` unless reviewed; Validate → Save; verify active before adding a 2nd key/round-robin/fallback.
3 Prefixed model id = `avalai/gpt-5.4-mini` (not the raw id). Create downstream key in dashboard; `curl http://localhost:20128/v1/models -H "Authorization: Bearer <9router key>"`.

## Verify first flow
Single active AvalAI connection, fallback OFF:
```bash
curl -N http://localhost:20128/v1/chat/completions -H "Authorization: Bearer <9router key>" -H "Content-Type: application/json" -H "X-9Router-Token-Saver: off" -d '{"model":"avalai/gpt-5.4-mini","messages":[{"role":"user","content":"Reply with exactly: AvalAI via 9Router"}],"stream":true}'
```
Layers: provider Check OK → persistent connection active → `/v1/models` lists prefixed model → streaming chat returns expected text → only then enable token saver, rewrite, round-robin, proxy pool, fallback → repeat with separate Responses node + `/v1/responses`. `X-9Router-Token-Saver: off` bypasses all token savers for one diagnostic request.

## Capability map
Direct: model discovery (`/v1/models`, prefixed), Chat Completions, Responses (separate node + model support). Model/route dependent: streaming (adapter framing), tools/structured outputs (`tools`, `tool_choice`, schema pass-through), vision. Separate configuration: **Self-hosted Embedding** (base `https://api.avalai.ir/v1`, stored key, model e.g. `text-embedding-v4`), **Self-hosted STT** (FULL URL `https://api.avalai.ir/v1/audio/transcriptions`), **Self-hosted TTS** (server ROOT `https://api.avalai.ir`, adapter appends `/v1/audio/speech`), web search (9Router search provider vs the model's own search — know which the client calls). Unverified: image generation, Realtime, video from the generic language node. STT/TTS/Embedding are 9Router provider types; no credentialed media request was run.

## Docker Compose (pinned image `decolua/9router:v0.5.35`)
```yaml
services:
  9router:
    image: decolua/9router:v0.5.35
    container_name: 9router
    restart: unless-stopped
    ports: ["127.0.0.1:20128:20128"]
    volumes: ["9router-data:/app/data"]
    env_file: [.env]
    environment: {DATA_DIR: /app/data, PORT: "20128", HOSTNAME: 0.0.0.0, NODE_ENV: production, ENABLE_REQUEST_LOGS: "false"}
volumes: {9router-data: {}}
```
`.env` (chmod 600, gitignored): `JWT_SECRET`, `INITIAL_PASSWORD`, `API_KEY_SECRET`, `MACHINE_ID_SALT` (each independent random), `DATA_DIR=/app/data`, `ENABLE_REQUEST_LOGS=false`, `AUTH_COOKIE_SECURE=false` (set `true` when dashboard served over HTTPS), `REQUIRE_API_KEY=true`. Unset `INITIAL_PASSWORD` falls back to `123456` (insecure) → set before first run. `chmod 600 .env; docker compose config --quiet; docker compose up -d; docker compose logs --tail=100 9router`. Baseline excludes Headroom sidecar, outbound proxy, reverse proxy (add only after the direct AvalAI path works and security reviewed).

## Safe operation
Keep 20128 on loopback/private network unless TLS+auth ingress; keep dashboard login, downstream gateway key, upstream AvalAI key separate; `ENABLE_REQUEST_LOGS=false` for sensitive workloads (debug logs contain prompts/responses/headers/files/personal data); one dedicated AvalAI key per deployment + monitor provider usage (dashboard cost = estimate, not AvalAI billing); when debugging, token saver and rewrite OFF then enable one by one; protect the volume (SQLite, backups, certs, logs, runtime config, stored provider creds, downstream keys). Upgrade: `docker compose stop 9router; mkdir -p backup/9router-data; docker cp 9router:/app/data/. backup/9router-data/; docker compose start 9router`; record current tag; change only vetted tag; `docker compose config --quiet`; recreate with same volume. Rollback: restore previous tag; restore SQLite only with service stopped from a tested backup.

## Troubleshooting
provider Check 401/403 → key in temporary field. Local `/v1` 401/403 → using wrong key (need 9Router downstream key). Check OK but requests fail → no persistent connection or inactive. Model not found → missing `avalai/` prefix or wrong API type (list `/v1/models`). Upstream 404 → base URL/route (keep `https://api.avalai.ir/v1`; don't swap Chat/Responses). Stream stops/output altered → token saver/rewrite/fallback/proxy (send with `X-9Router-Token-Saver: off`, disable transformations). Embeddings 404 → missing `/v1` in base. STT/TTS path doubled → STT takes full URL, TTS server root. State lost after restart → wrong `/app/data` volume or `DATA_DIR`. Dashboard cost high → estimate ≠ billing.

## Defects
- Doc flags `gpt-transcribe` unsupported (conflicts with other guides).
- Tag v0.5.35 is "earlier verified sample", not latest claim.
