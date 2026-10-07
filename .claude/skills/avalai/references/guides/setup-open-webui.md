# Open WebUI + AvalAI (setup guide)
Open WebUI = self-hosted multi-user chat UI; it owns users, chats, files, retrieval, tools, task models and media settings. AvalAI just authenticates API calls. A working chat connection does NOT configure embeddings/RAG, images, speech or transcription (separate settings). Validated vs official sources 2026-08-06 (rechecked 2026-09-08: path **Settings → Admin → Connections**; **Model IDs (Filter)** when model listing fails). Not run with real keys.

## Prereqs
Docker+Compose; dedicated AvalAI key; chat model e.g. `gpt-5.4-mini`; stable random `WEBUI_SECRET_KEY` (outside VCS); plan for first admin + approval of later signups; network must support WebSocket for streaming. First account on a fresh data volume becomes Administrator; later signups are Pending until approved.
Checks: base `https://api.avalai.ir/v1`; required route `/v1/chat/completions`; discovery `/v1/models`; optional experimental `/v1/responses`. Open WebUI verifies a connection by calling `/models` with Bearer auth; if the provider lacks it verification may fail while chat works → use **Model IDs (Filter)** instead of changing the (correct) chat endpoint. Docs say AvalAI doesn't support `gpt-transcribe`/`gpt-live-transcribe` — conflicts with audio guides; choose models currently listed for `/v1/audio/transcriptions`.

## Install (pinned `v0.11.0`)
`.env`: `WEBUI_AUTH=True`, `WEBUI_SECRET_KEY=<independent random>`. `chmod 600 .env; docker volume create open-webui; docker run -d --name open-webui --restart unless-stopped -p 127.0.0.1:3000:8080 --env-file .env -v open-webui:/app/backend/data ghcr.io/open-webui/open-webui:v0.11.0; docker logs --tail=100 open-webui`. Open `http://localhost:3000`, create the intended admin FIRST, confirm volume persists across restart before adding provider credentials.

## Connect
Admin Settings → Connections → OpenAI → Add Connection: URL `https://api.avalai.ir/v1`; API Key = dedicated AvalAI key; Model IDs (Filter) = empty if discovery works, else `gpt-5.4-mini` (allowlist + discovery fallback; doesn't change real model capability). Save, keep the enable toggle ON. Start with Chat Completions (select model, simple prompt, check streaming before tools/files). **Open Responses** support in Open WebUI is experimental → configure/test separately; model must support `/v1/responses`; not a drop-in replacement for the chat connection.

## Verify in order
container health + `/app/backend/data` mounted → first account is Administrator → connection saved+enabled → discovery works or model visible via Filter → fresh chat, plain text, no tools/files → streaming incremental → dependent 2nd turn → then tools, vision, RAG, image, STT/TTS one at a time. If simple chat fails, don't debug retrieval/media: separate container health, auth, model selection, endpoint shape, streaming.

## Capability map
Direct: model discovery (`/v1/models` recommended; Filter fallback), Chat Completions. Model/route dependent: Open Responses (experimental), streaming (WebSocket/SSE through proxy), tools/structured output (`tools`/`tool_choice`, tool mode), vision (vision model + attachment path). Separate configuration: **Documents** embeddings/RAG (base `https://api.avalai.ir/v1`, dedicated key, model e.g. `text-embedding-v4`; retrieval also depends on extraction, chunking, storage, permissions); **Images** (`/v1/images/generations`, model e.g. `gpt-image-2`; not inherited from chat); **Audio** STT (`/v1/audio/transcriptions`, e.g. `gpt-transcribe`) and TTS (`/v1/audio/speech`, e.g. `gpt-audio-1.5`); web search/app tools. Unverified: Realtime audio, video. Open WebUI may send extra requests (title, tags, follow-up suggestions, task model, tools, embeddings, media) that consume quota even if UI shows one user turn.

## Docker Compose (pinned)
```yaml
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:v0.11.0
    container_name: open-webui
    restart: unless-stopped
    ports: ["127.0.0.1:3000:8080"]
    volumes: ["open-webui:/app/backend/data"]
    env_file: [.env]
    environment: {WEBUI_AUTH: "True", WEBUI_SECRET_KEY: "${WEBUI_SECRET_KEY}"}
volumes: {open-webui: {}}
```
`chmod 600 .env; docker compose config --quiet; docker compose up -d; docker compose logs --tail=100 open-webui`. Don't use floating `:main`/`:latest`; read release notes/migrations before changing tag. Keep auth ON: `WEBUI_AUTH=False` is a one-way choice (single-user vs multi-account), unsuitable for shared instances.

## Safe operation
Keep port 3000 on loopback/private net (reverse proxy: TLS + auth, keep WebSocket upgrade); register intended admin before inviting users, restrict signup, review Pending accounts; keep `WEBUI_SECRET_KEY` constant across rebuilds (changing/removing logs users out, breaks persisted sessions); separate AvalAI keys for chat/embeddings/media if you want separate revocation/attribution; treat `/app/backend/data` (chat history, uploads, retrieval index, provider creds, user records) as sensitive; scrub keys, Authorization headers, prompts, responses, uploads, personal data from logs/support bundles. Upgrade: `docker compose stop open-webui; mkdir -p backup/open-webui-data; docker cp open-webui:/app/backend/data/. backup/open-webui-data/; docker compose start open-webui`; record tag; read notes; change only the pinned tag; recreate with same volume+secret. Rollback: previous tag; restore data only with service stopped and migration compatibility checked on a copy.

## Troubleshooting
Verification 400/401/403 → `/v1/models`/Bearer key/discovery (keep correct base URL; add exact id to Filter if only discovery fails). Chat 401/403 → re-save key, check toggle. Chat 404 → missing `/v1`, wrong model, Responses vs Chat mismatch (start with Chat Completions). Model missing → Filter, account tier, stale catalog (add current id, new chat). Chat OK but tools not → function calling/tool mode/schema (limit to one tool). Vision fails → model capability/attachment path (small image, verified vision model). RAG fails → embedding setting/extractor/chunk/permissions/storage (test embeddings alone on a small doc). Image/audio fails → engine/URL/key/model of THAT setting. No streaming → WebSocket/SSE in proxy (test on loopback, check buffering/upgrade). Users logged out after restart → `WEBUI_SECRET_KEY` lost. Data gone after restart → no named volume on `/app/backend/data`.

## Defects
- "Open WebUI verification uses /models": AvalAI exposes `/v1/models` — failure is probably account/key related, not missing route.
- `gpt-transcribe` support statement conflicts with other guides (unverified).
