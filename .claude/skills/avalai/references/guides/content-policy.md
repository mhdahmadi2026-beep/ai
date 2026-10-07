# API content policy & safeguards (docs.avalai.ir/fa/safety/content-policy)

AvalAI's own statement about what it does with API call content. Pair with guides/data-controls.md (per-route retention checklist) and guides/safety-best-practices.md. Support: Telegram t.me/AvalAISupport.

## What AvalAI states
- **No-retention policy for API call content:** AvalAI says it does NOT collect, store or use request-body content — prompts, chat messages, audio (transcription/STT inputs), images (analysis/generation inputs), or any other body content. Content is processed in real time only to produce the response; stated aim is to eliminate leak risk even under breach/hack.
- **Minimal metadata retained** (billing, rate limiting, abuse detection, security): **model name, IP address, timestamp, usage metrics (e.g. token counts)**. Not used to analyse or exploit private content.
- **Chat platform vs API:** the AvalAI chat product has a "help improve the model" setting (off by default); the API has no such interaction with call content.
- **Third-party providers disclaimer:** AvalAI is a gateway; it is responsible only for its own service and has **no control over upstream providers' privacy/data practices**. `gpt-5.4` calls go to OpenAI; `gemini-2.5-pro` calls go to Google (Gemini AI Studio); likewise for other models. Users must read each provider's privacy policy/ToS.

## How to apply (my rules)
- Treat the statement as **AvalAI-layer only**. Upstream retention/abuse-monitoring/training terms depend on the model route → document per route; classify web-search/MCP/tools as transfers to external parties (data-controls.md).
- The no-retention claim covers AvalAI, not provider *application state*: Responses may be stored upstream unless `store:false`; files, batches, videos, vector-store-like features and background jobs can persist at the provider/route → minimise, set expiry, delete.
- Log in your own system only operational metadata (request id, model, usage, cost, error class), not raw prompts, unless required and protected (encryption, retention limit, access control).
- Don't send secrets/PII unless necessary; use AvalAI Guardrails `"guardrails":["hide-secrets"]` and your own redaction; get end-user consent for audio/voice data (see examples/speaker-aware-meeting-intelligence.md).
- For compliance claims to your customers, cite this policy + each provider's policy + your own retention; don't promise "nothing is stored anywhere".
- IP address, timestamp, model, usage ARE retained by AvalAI — disclose in your privacy notice if your users' IPs are forwarded (server-side calls hide end-user IPs; prefer server proxying with `safety_identifier` hashed ids).

## Caveats / gaps in the page
- Statement is a policy claim, not a contract/SLA, ZDR certification or audit report; no retention durations for the kept metadata; no mention of abuse-monitoring content review by AvalAI or upstream, error-log sampling, support-ticket attachments, uploaded files (`/v1/files`), batch/video jobs, or the Guardrails feature.
- "Gemini AI Studio" is named as Gemini's destination: free vs paid tier data-use terms differ at Google — verify which tier AvalAI's account uses (unknown here).
- Does not address content *moderation/acceptable-use* despite the title; for those see guides/safety-checks.md, guides/red-teaming.md, `/v1/moderations`. Separate "privacy policy" page (safety/privacy-policy) not yet captured.
