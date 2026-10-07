# Service status page (https://status.avalai.ir — Instatus)

Source: SCREENSHOT supplied by the user (captured on/just after 2026-10-07; status.avalai.ir is blocked in the sandbox network policy, so it can't be fetched live). Numbers below are read from a low-resolution image → treat as approximate.

## What the page shows
- Banner: **All systems operational** (at capture time). Powered by Instatus; "Report an issue", "Get updates" subscription; history ("Show history").
- Monitored components with ~30/90-day uptime bars + avg response time + uptime %: **API Services** (overall), **Web Chat Service**, **Web Chat Application**, and per-endpoint API services: `/v1/chat/completions`, `/v1/responses`, `/v1/messages`, `/v1/embeddings`, `/v1/files`, one more `/v1/…` (likely models/audio, illegible), and `/v1beta/…` (Gemini native). Overall ≈100% for API/Web Chat; per-endpoint ≈99.9x% with visible orange (degraded) bands in the same mid-window period across endpoints, and **red (major outage) blips on `/v1/files`**. Rough average response times: API overall ~0.3–0.4 s; chat/completions ~1.3 s, responses ~1.0–1.5 s, messages ~1.3 s, embeddings ~0.4 s, files ~0.5 s.
- **Third-party dependencies tracked (all Operational):** OpenAI (API), Anthropic (api.anthropic.com), Google (Gemini/AI Studio API), Cloudflare (Sites and Services → Workers AI), Stability AI (REST API), Perplexity (API).
- Recent notices (Oct 1–7, 2026): a steady stream of **short, auto-detected "Degraded performance" incidents (~1–6 min each)** on `/v1/messages`, `/v1/responses`, `/v1/chat/completions`, `/v1beta/models`, `/v1/embeddings`, plus Web Chat Application (~4 min) and one `/v1/files` **major outage (~3 min)**; all "Resolved", created/closed automatically by Instatus monitoring.

## Operational guidance (derived)
- Expect brief transient degradations (minutes) several times per week per endpoint: build retry with exponential backoff + jitter (examples/rate-limit-safe-parallel-requests.md), timeouts, idempotency, and a model/route fallback (e.g. chat/completions ↔ responses ↔ messages; another provider's model) — don't treat a single 5xx/timeout as an outage.
- On repeated 5xx/timeouts/429: check status page (and upstream providers' status: OpenAI/Anthropic/Google/Cloudflare/Stability/Perplexity), then circuit-break, queue, retry later; `/v1/files` is the least stable component in the capture → prefer base64/URL inputs over `/v1/files` for critical paths.
- Subscribe to updates (email/webhook) via "Get updates"; for programmatic checks, Instatus pages usually expose JSON at `/summary.json` (unverified for this host — test when network access allows). Add your own synthetic probe (tiny `/v1/models` + 1-token chat call) with latency/error-rate alerting; log `avalai-request-id`.
- A green status page ≠ your errors are not AvalAI-side (per-model/route issues, rate limits 429 = account tier, upstream model incidents) — check response headers and error body first.
