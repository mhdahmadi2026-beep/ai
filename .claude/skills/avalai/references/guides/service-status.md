# Service status page (https://status.avalai.ir — Instatus)

Source: Live Instatus verification (2026-10-07) and status dashboard at https://status.avalai.ir.

## Live Status Check API
AvalAI provides a live programmatic status endpoint powered by Instatus:
- **Status Endpoint**: `GET https://status.avalai.ir/summary.json`
- **Current Live Status (as of 2026-10-07)**:
```json
{"page":{"name":"AvalAI","url":"https://status.avalai.ir","status":"UP"}}
```

## Monitored System Components & Endpoints
The status dashboard monitors both core services and granular HTTP API routes:
- **API Services (Overall)**: Gateway availability and latency (~0.3–0.4s avg response time)
- **Web Chat Service & Application**: Frontend UI and chat interface
- **Per-Endpoint Monitored Routes**:
  - `/v1/chat/completions` (OpenAI-compatible Chat completions, ~1.3s avg latency)
  - `/v1/responses` (AvalAI unified responses API, ~1.0–1.5s avg latency)
  - `/v1/messages` (Anthropic Messages API, ~1.3s avg latency)
  - `/v1/embeddings` (Text embeddings endpoint, ~0.4s avg latency)
  - `/v1/files` (File upload and retrieval endpoint, ~0.5s avg latency)
  - `/v1beta/models` & `/v1beta/...` (Google Gemini Native API)
  - `/v1/models` & `/v1/audio`
- **Third-Party Upstream Dependencies Tracked**:
  - OpenAI API
  - Anthropic (`api.anthropic.com`)
  - Google Gemini / AI Studio API
  - Cloudflare Workers AI
  - Stability AI REST API
  - Perplexity API

## Operational Guidance & Best Practices
- Expect brief transient degradations (minutes) several times per week per endpoint: build retry with exponential backoff + jitter (`references/examples/rate-limit-safe-parallel-requests.md`), timeouts, idempotency, and a model/route fallback (e.g. `chat/completions` ↔ `responses` ↔ `messages`; alternative provider model) — don't treat a single 5xx/timeout as an outage.
- On repeated 5xx/timeouts/429: query `https://status.avalai.ir/summary.json` first, then circuit-break, queue, and retry later. Note that `/v1/files` historically experienced occasional outage blips; prefer direct base64 data URLs when possible for latency-critical paths.
- Programmatic health checks: Call `GET https://status.avalai.ir/summary.json` before triggering batch workloads. Always log the `avalai-request-id` response header for tracing.
- A green status page (`status: UP`) does not preclude account-level rate limits (HTTP 429 based on tier limits) or model-specific quotas. Check response headers and error JSON payloads.
