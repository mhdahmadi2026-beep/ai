---
name: avalai
description: Expert guide for building with AvalAI (اول ای‌آی / "اول ai" / "هوش مصنوعی اول"), an OpenAI-compatible AI gateway at https://api.avalai.ir/v1. Use whenever the project calls AvalAI, api.avalai.ir, AVALAI_API_KEY, or the user asks about AvalAI models, pricing, rate limits, service tiers, credit packages, deprecations, Responses/Chat Completions/Messages APIs, images, audio, tools, streaming, structured outputs, function calling, or production practices. Always consult references/ instead of guessing model IDs, prices or limits.
---

# AvalAI skill

Source of truth: https://docs.avalai.ir/fa/ (Persian) — English at https://docs.avalai.ir/en/.
Official name is always written **AvalAI**. Users may also say «اول ai», «اول ای آی», «هوش مصنوعی اول».

## Core facts (from the Introduction page)
- Single base URL for OpenAI-compatible clients: `https://api.avalai.ir/v1`
- Auth: project API key in env var `AVALAI_API_KEY`. Create it in the dashboard (https://chat.avalai.ir/platform/home). **Server-side only — never ship to browsers/mobile apps.**
- Recommended first call: **Responses API** (`client.responses.create`), read `response.output_text`.
- Works with the official OpenAI SDKs (Python/JS) and plain cURL.
- Support: ticket https://chat.avalai.ir/platform/support/create-ticket · status https://status.avalai.ir/ · debug with AvalAI chat https://chat.avalai.ir/chat

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)
print(response.output_text)
```

## Working rules
1. Read the matching file in `references/` before writing code; see `references/00-index.md` for the page map and which pages are already captured.
2. Never invent model IDs, prices, tiers or limits. If a reference file is missing or marked PENDING, say so and ask the user for that page.
3. Model availability depends on account tier (e.g. some models "from tier 1"). Check `references/` for tier and endpoint support (Chat Completions / Messages / Responses — support may be full or partial per model).
4. Keys from env, never hard-coded; plan security, retries, latency and cost per production-best-practices.
5. Dates in docs are Jalali with Gregorian in parentheses; promotional rates expire — check dates.

## References
See `references/00-index.md`.

## Practical rules from Quickstart
- New text apps → `/v1/responses` (`input`, `instructions`, `response.output_text`); keep `/v1/chat/completions` (`messages`) for legacy/chat-only models.
- On `429`: honor `Retry-After`, exponential backoff + jitter + retry cap.
- Discover models: `GET https://api.avalai.ir/public/models` (no auth) or `/v1/models`.
- Provider-specific params: `extra_body` (Python) / `@ts-expect-error` direct fields (TS).
- Exact cost: read `avalai-request-id` header → `POST /user/v1/transactions/lookup` (available ~30s later).
- Model IDs in examples may be stale; verify live before hard-coding.

## Tool integration rules (ai-workflows)
- Base URL `https://api.avalai.ir/v1`; tools append `/chat/completions` themselves — never paste the full path into a base-URL field.
- Model prefix is tool-specific: OpenCode `avalai/<id>`, Aider `openai/<id>`, direct API plain `<id>`.
- Use a dedicated AvalAI key (not OpenAI/ChatGPT credentials). Don't use `gpt-transcribe`/`gpt-live-transcribe` on AvalAI.
- Start direct; add 9Router (a gateway, not an agent) only when routing/fallback is needed. Human approval before side effects; synthetic data first.

## SDK rules (libraries)
- OpenAI SDK → base `https://api.avalai.ir/v1`. Anthropic SDK & Google GenAI SDK → base `https://api.avalai.ir` (**no `/v1`**). Anthropic SDK can call non-Claude models via `/v1/messages`; Google SDK is Gemini-only.
- Pin SDK versions; keep a raw-HTTP fallback; set explicit timeouts for flex tier / long jobs; retry only idempotent operations.
- Log `avalai-request-id`; optionally send `X-Client-Request-Id`.
- Several published snippets have SDK-version quirks (Go/.NET/Google Python) — see notes in `references/04-libraries.md` and verify against the installed SDK.

## Performance rules
- Cache: stable prefix first, dynamic last; byte-identical prefix; verify `usage.prompt_tokens_details.cached_tokens`; app must work on cache miss and keep its own conversation state.
- Cap output (`max_output_tokens` for Responses, `max_completion_tokens` for Chat), stream, reuse connections, log p50/p90/p95 + request IDs.
- Benchmarks in docs are point-in-time observations, never guarantees. Main domain `api.avalai.ir`; `api.avalapis.ir` is a slower alternate; Guardrail adds ~200–300 ms.

## Pricing rules
- Prices are USD per 1M tokens, pass-through (no markup). Live source: `GET https://api.avalai.ir/public/models` — check `pricing`, `min_tier`, `tier_rate_limits`, `supported_endpoints` before quoting or hard-coding. Snapshot in `references/06-pricing.md`.
- Hidden reasoning tokens bill at the **output** rate; don't add `reasoning_tokens` to `output_tokens` (double count).
- `service_tier: "flex"` = 50% cheaper for select OpenAI models, up to 900 s, may fail → fall back to `default`; credit packages do NOT cover flex.
- `estimated_cost` in responses is NOT for billing; use `avalai-request-id` + User API `/user/v1/transactions/lookup` for exact cost (~30 s delay).
- Free signup credit: 25,000 T (email) → 200,000 T total after phone verification.
- Watch promo expiries (GLM-5.3-Flash 18 Shahrivar 1405, Gemini 3.8 Flash & TTS 10 Dey 1405) and the `deepseek-v4-pro` → `deepseek-v4.1-flash` reroute on 2026-09-14.

## Service-tier rules
- Public values: `default` (credit packages cover it) and `flex` (−50%, up to 900 s, no credit-package coverage, select OpenAI models only: gpt-5.5, 5.4-pro/5.4/mini/nano, 5.2-chat, 5.2, 5.1, 5, 5-mini, 5-nano, o3, o4-mini). Never send `priority`/`auto` unless the account has it.
- Flex pattern: timeout 900 s, on failure/timeout retry with `service_tier: "default"` + exponential backoff (idempotent work only). Log returned `service_tier` with `avalai-request-id`.
- Flex on an unsupported model → `invalid_request` error.

## Credit-package rules
- Packages = prepaid, discounted (20–40%), scoped to listed models, fixed validity (1/7/30/31 d), per-template purchase cap, non-transferable, flex tier NOT covered. Keep overall balance positive (≥100,000 Toman) or API is disabled.
- Package credit is consumed before general balance; out-of-scope models bill at standard rates.
- Verify with `POST /user/v1/transactions/lookup` → `cost.source` = `credit_package` | `balance`. Check live availability at the store/API before recommending a package; Claude packages are currently unavailable.

## Rate-limit rules
- Tiers: Tier 0 (email) → Tier 1 (phone verified, instant) → Tier 2/3/4/5 at cumulative top-up ≈ $10/$50/$250/$1,000. Automatic, instant, no credit deducted. Metrics: RPM, RPD, TPM, TPD, IPM (first hit wins). Per-model limits: `tier_rate_limits` in `/public/models` or per-tier pages.
- 429 `rate_limit_exceeded` → honor `Retry-After`, exponential backoff + jitter + cap; use `x-ratelimit-*` headers; client-side token bucket / queue for volume. Batch API not available yet.
- `/user/v1` limits per tier (req/min): 3, 15, 50, 150, 350, 750.

## Deprecation rules (read 10-deprecations.md before choosing a model ID)
- DeepSeek: any DeepSeek ID currently routes to `deepseek-v4.1-flash`; use only `deepseek-v4.1-flash` / `deepseek-flash`.
- GPT-5 `-chat` IDs (`gpt-5-chat`, `gpt-5.1-chat`, `gpt-5.2-chat`, `gpt-5.3-chat`, `*-chat-latest`) are removed → use base `gpt-5`, `gpt-5.1`, `gpt-5.2`, `gpt-5.3`.
- Removed families: Claude 3.x/4.0/4.1 (Bedrock + native), Imagen 4, Gemini 1.5/2.0, Gemma 3, Qwen turbo/VL/max legacy, Moonshot v1/kimi-k2-thinking, GLM ≤5, MiniMax M2/M2.1, Seedream 4.x, Stability, many NVIDIA NIM / Cloudflare cf.* IDs.
- Upcoming provider shutdowns: gpt-5.4-cyber 2026-10-01; legacy GPT snapshots 2026-10-23; Evals/Prompts/Agent Builder 2026-11-30; gpt-image-1/1-mini/1.5 2026-12-01; GPT-5/o3 snapshots 2026-12-11; legacy audio/realtime 2027-01-20; whisper/gpt-4o-transcribe 2027-02-26.
- Prefer stable (non-preview) IDs; avoid `-latest` aliases for regulated/regression-sensitive workloads. Always verify with live `/v1/models`; where reference files disagree, deprecations + live API win.

## Reseller billing rules (references/resellers/)
- Never bill from `estimated_cost`. Store `avalai-request-id` (response HEADER; OpenAI SDK: `response._request_id`) per customer request, wait ~5 s (≤30 s), then `POST /user/v1/transactions/lookup` (≤1000 ids per call) and bill from `cost.unit` (USD) / `paid_irt + paid_grant_irt` (Toman). Prefer async worker; retry with backoff; store full transaction detail; key charges on `request_id` (idempotent).
- Enterprise tracking: tag requests with `safety_identifier` (e.g. `dept-<id>`) in the body, store `avalai-request-id` + tags locally, batch-lookup ≤1000 ids, re-queue not-yet-found ids. Video API bodies include `request_id`/`safety_identifier`, but Sora/OpenAI Videos shut down 2026-09-24.

## Auth rules
- `Authorization: Bearer $AVALAI_API_KEY`, server-side only; separate key per env/service/tenant; rotate on any leak. No Admin API, no workload-identity exchange, and **organization header/option is NOT implemented — don't send it**. Don't use OpenAI admin keys/IP ranges with AvalAI. Log `avalai-request-id` + hashed `safety_identifier`.

## User API quick map (`https://api.avalai.ir/user/v1`, Bearer key; rate-limited 3/15/50/150/350/750 req/min by tier)
`GET /credit` (balance, tier, packages/grants) · `GET /transactions` (filters: hours_ago≤720, dates, page_size≤1000, model, provider, status_code, api_key_id, safety_identifier) · `POST /transactions/lookup` (≤1000 ids, exact `cost`) · `GET /transactions/summary?group_by=model|provider|date|hour` · `GET /health`. Records kept ≥90 days. Error shape is flat `{error, message}`.

## Models API rules
- `GET /v1/models` (+`/{id}`), `GET /public/models` (no auth). Header decides format: `Authorization: Bearer` → OpenAI, `x-api-key` → Anthropic (Anthropic SDK base URL has no `/v1`). Only `GET /v1/models/{id}` returns `extra.{metadata,pricing,rate_limits}` (per-tier rpm/tpm + your `current` tier). Use it/`/public/models` instead of guessing IDs, prices, limits, `min_tier`, capabilities.

## Response-header rules (important, time-sensitive)
- Read **`avalai-request-id`** (UUID v7) from response headers. Legacy `x-request-id` is returned only until **2026-10-15**; afterwards it may be a CDN's id — never use it. The OpenAI SDK's `response._request_id` was derived from `x-request-id` → prefer `with_raw_response(...).headers.get("avalai-request-id")` (older references in this skill that say `_request_id` should be treated with that caveat).
- Optional request header `X-Client-Request-Id` (ASCII ≤512 chars, unique per attempt) → log with `avalai-request-id`.
- Rate-limit headers: `x-ratelimit-{limit,remaining,reset}-{requests,tokens}` (+ `-project-tokens` on some routes); reset values are duration strings like `45s` (don't `int()`); on 429 honor `Retry-After`.

## Chat Completions rules (see api-reference/chat.md)
- `POST /v1/chat/completions`. Use `max_completion_tokens` (covers hidden reasoning tokens — leave headroom or you get `finish_reason: "length"` with no text). Prefer `response_format: json_schema` over `json_object` and still validate. Prefer `safety_identifier` (hashed, ≤64 chars) + `prompt_cache_key` over `user`.
- Model quirks: Claude Opus 5.5 / Fable 5.1 / Opus 5 → adaptive thinking always on, tune via `output_config.effort` in `extra_body`, **no** `temperature`/`top_p`, no prefill, no forced tool use; Kimi K3 → no fixed sampling fields; GLM-5.3 → must send `thinking.type:"enabled"` + `reasoning_effort` low|high|max; Qwen3.8-2.4t → text-only, thinking mandatory (`low|medium|xhigh`); GPT-6.1 Sol → never `none`/`minimal` effort; Grok 4.7 → don't send `reasoning_effort`. Responses is PARTIAL for Claude Sonnet 5.5/Fable 5.1/Opus 5, Grok, GLM, Kimi K3, Qwen3.8, Gemini 3.8 Flash, Fireworks models.
- TTS: Gemini 3.8 TTS only via `/v1beta/models`, `/v1/chat/completions`, `/v1/audio/speech`; chat audio at `choices[0].message.audio.data`; `pcm16` = 24 kHz mono headerless.

## Images API rules (see api-reference/images.md)
- Default `gpt-image-2.5-flare` (fast); `gpt-image-2.5-sunburst` for precise pro edits. `quality: xhigh|max` ONLY on those two. GPT Image returns Base64 → decode `data[0].b64_json` (edits may also return a `data:` URL or URL — handle all). Never put image-model ids in `/v1/responses` `model`; `gpt-6-sol/luna`, `grok-4.7` are not image generators.
- Edits: multipart (`image`) or JSON (`images:[{image_url|file_id}]`, ≤16); mask needs alpha, same size/format; prompt describes whole final image; no `input_fidelity` for `gpt-image-2`; `background` stay `auto|opaque`; `moderation: auto`.
- Non-OpenAI params via `extra_body` (FLUX: `response_format:"b64_json"` only). Qwen supports OpenAI format (`1328x1328`) and Dashscope-native (`input`/`parameters`, `1328*1328`). Gemini image models only via chat/completions or `/v1beta`; `imagen-*` removed. Variations endpoint = placeholder.
- Cost: image output $30/1M tokens (2.5 and gpt-image-2); estimates cover output only — add prompt + reference-image tokens. Never auto-retry `moderation_blocked`.

## Embeddings rules (see api-reference/embeddings.md)
- `POST /v1/embeddings`; `input` = string or array (no empty strings; chunk big ingests, retry failed chunks). Same model + same `dimensions` for index and queries; never mix models/dims in one index. `encoding_format: float` by default. `dimensions` only on text-embedding-3-* / Gemini.
- Models: `text-embedding-3-small` (1536), `-large` (3072), Gemini `gemini-embedding-001/2` (≤3072, `extra_body: {task_type, output_dimensionality}`; use RETRIEVAL_DOCUMENT for docs, RETRIEVAL_QUERY for queries; L2-normalize when dims < 3072), Cohere, Alibaba `text-embedding-v4`. Native Gemini: `/v1beta/models/<id>:embedContent`.
- Vectors are derived user data: apply tenant isolation/retention/deletion. Use RAG: retrieve then answer via Responses/Chat.

## Audio API rules (see api-reference/audio.md)
- TTS `/v1/audio/speech` (≤4096 chars OpenAI-compat; chunk+concat; send `response_format` explicitly; `gemini-3.1-flash-tts-preview` needs `pcm`; Gemini 3.8 voice = object `{name,languageCode}`; Gemini TTS never on `/v1/responses`, `/v1/messages`, `/v1/text:synthesize`). STT `/v1/audio/transcriptions` (≤~25 MB; `gpt-4o-transcribe*`, `whisper-1`, `scribe_v*`, groq whisper; diarize → `diarized_json` + `chunking_strategy:"auto"`; whisper-1 can't stream; don't set multipart Content-Type manually). Translation → English only (`whisper-1`).
- Direct audio in/out → Chat Completions (`gpt-audio*`, `modalities`, `message.audio.data` base64). Responses flow = transcribe → responses → speech. Tell users audio is AI-generated; keep consent for voice cloning.

## Moderation rules (see api-reference/moderation.md)
- `POST /v1/moderations`, models `omni-moderation-latest` (text+image, free, no audio), `text-moderation-*`, `cf.llama-guard-3-8b`. Array input → one result each. Use `category_scores` with per-category thresholds (stricter `sexual/minors`), not only `flagged`; keep result `id` + hashed `safety_identifier` for audit; human review for borderline.
- Inline `moderation:{model}` on Responses/Chat only if route supports it; check input/output error objects first; streamed output is unmoderated until the final result; tool names/schemas aren't checked.

## Fine-tuning (see api-reference/fine-tuning.md)
- **Not implemented on AvalAI** — no fine-tunable models/routes; never generate code relying on `/v1/fine-tuning/*`. Offer prompting / structured outputs / few-shot / RAG instead.

## Assistants API (see api-reference/assistants.md)
- **Not implemented on AvalAI** (and OpenAI sunset it 2026-08-26). Never emit `/v1/assistants|threads|runs` code. Migrate to `/v1/responses`: instructions→`instructions`, thread→`previous_response_id`/own DB state, run→response, store history yourself, keep typed output items, RAG via embeddings if `file_search` unavailable.

## Batch API (see api-reference/batch.md)
- **Not implemented** on AvalAI: no `/v1/batches`, no 50% batch discount, no hosted webhooks. Build client-side workers (bounded concurrency, `custom_id`, retry/backoff, job state machine) and consider the flex service tier (−50%) for non-urgent OpenAI-model work.

## Files API rules (see api-reference/files.md)
- Available: `/v1/files` (upload ≤128 MB multipart, list, retrieve, delete, `/content`). Use `purpose="user_data"` for model inputs; reference by `file_id` in chat (`{"type":"file","file":{"file_id"}}`), responses (`input_file`), messages, ocr, images/edits. Tier limits: uploads/min 3/10/50/250/500/1500, storage 250 MB→200 GB; 507 when full. Set `expires_after`, delete when done, avoid base64 in logs. PDFs: Gemini/vision models; big corpora → embeddings/RAG.

## Responses API rules (see api-reference/responses.md) — preferred API for new apps
- `POST /v1/responses`: `input` (+ `instructions`, resend each turn; NOT inherited via `previous_response_id`); read `response.output_text` (SDK-only) or iterate `output` by `type`. `max_output_tokens` includes reasoning → leave headroom, check `status`/`incomplete_details` before parsing. Structured: `text.format` json_schema strict. No `n`. One state strategy: `previous_response_id` | `conversation` | manual replay; `store:false` + `include:["reasoning.encrypted_content"]` for stateless reasoning; chain tokens still billed.
- Streaming = typed SSE events: accumulate `response.output_text.delta`, run function calls only after `response.function_call_arguments.done`, finish on `response.completed`, handle `response.failed`/`error`; save `sequence_number` for resume.
- Non-OpenAI models: partial support (text + basic tools); hosted tools/`reasoning` OpenAI-only and route/account dependent → fall back to function tools / manual RAG. `service_tier`: `default`|`flex` only. Use `safety_identifier` + `prompt_cache_key`, not `user`.

## Rerank rules (see api-reference/rerank.md)
- `POST /v1/rerank` — raw HTTP only (OpenAI SDK has no rerank). Models: `cohere-rerank-v4.0-pro|fast` (32K ctx, per-query price), `cohere.rerank-v3-5:0` (4K ctx, legacy), `qwen3-rerank`. `documents` = strings or `{id,text}`; use `top_n`; map results back via `index`; scores 0–1 sorted desc. RAG: over-retrieve → rerank → top few into the LLM.

## Messages API rules (see api-reference/messages.md)
- `POST /v1/messages` (Anthropic format). Anthropic SDK `base_url="https://api.avalai.ir"` (NO `/v1`); raw HTTP uses `x-api-key`. `max_tokens` is required. Multi-provider (Claude, OpenAI, Bedrock, Vertex, Gemini, MiniMax `minimax-m3`). Don't use removed Claude ids (docs' `anthropic.claude-sonnet-4-20250514-v1:0` is stale); Sonnet 5/Opus 4.8 support mid-conversation `role:"system"` and `stop_details`.

## v1beta / Gemini-native rules (see api-reference/v1beta.md)
- Google SDK base URL `https://api.avalai.ir` (no `/v1`, `api_version="v1beta"`); paths `/v1beta/models/{m}:{generateContent|streamGenerateContent|embedContent|batchEmbedContents|countTokens}`; auth Bearer or `x-goog-api-key`. Roles only `user`/`model`; system via `system_instruction`; `thinkingLevel` (Gemini 3.x) vs `thinkingBudget` (2.5). Images base64 only. Search grounding: `tools:[{google_search:{}}]` (Gemini 3 billed per query). `imagen-*` removed; `gemini-2.5-flash-image` stops 2026-10-02 → use `gemini-3.1-flash-image`/`gemini-3-pro-image` via generateContent/chat. Gemini 3.8 TTS native: `speechMetadata{speaker,style}` + `responseModalities:["AUDIO"]`; check `inlineData.mimeType` (WAV vs `audio/L16` 24 kHz). Use `client.models.generate_content` (not `agenerate_content`).

## `/v1/text:synthesize` (see api-reference/v1-text-synthesize.md)
- Vertex-native TTS for **Gemini 2.5** TTS only (`voice.model_name`, `audioConfig.audioEncoding`, base64 `audioContent`, multi-speaker with English aliases). Not for Gemini 3.8 TTS; default to `/v1/audio/speech` for new code.

## Search API rules (see api-reference/search.md)
- `POST /v1/search` (`search_tool_name` in body) or `/v1/search/{tool}`; returns raw `{object:"search", results:[{title,url,snippet,date?}]}` (not an LLM answer — distinct from hosted web-search tool). Tools by cost: `serper-search` $0.001, `dataforseo-search` .003, `parallel_ai-search` .004, `perplexity-search` .005, `tavily-search`/`firecrawl-search` .008, `parallel_ai-search-pro` .009, `tavily-search-advanced` .016, `exa_ai-search` .025. `max_results` 1–20; `search_domain_filter` ≤20; per-provider params (Serper `gl/hl/tbs`, Tavily country full name). Cache results.

## OCR rules (see api-reference/ocr.md)
- `POST /v1/ocr` model `mistral-ocr-4-0` ($0.004/page; $0.005 annotated; `mistral-ocr-latest` alias). `document:{type:"document_url"|"image_url", …}` (public URL or base64 data URL); `pages` 0-based; `table_format` markdown|html; structured output via `document_annotation_format` json_schema → `document_annotation` is a JSON *string*. Request images (`include_image_base64`) only when needed. Mistral SDK works with `server_url="https://api.avalai.ir"`.

## Videos API (see api-reference/videos.md) — ⚠ verify availability
- `/v1/videos` (create/retrieve/list/delete/remix/content). Sora models + OpenAI Videos API had a provider shutdown 2026-09-24 → treat Sora as unavailable; verify Veo (`veo-3.1-*`) / Runway (`gen4.5`, `gen4_turbo`) live via `/v1/models`. Async: poll `status`; download only when `completed`; never resubmit after a dropped connection — list videos first (`failed` = not billed, otherwise billed). `seconds` is a string (multiples of 4 for Sora). Characters/extensions/edits not supported.

## Alibaba/Qwen rules (see providers/alibaba.md)
- Non-streaming Qwen calls → `extra_body={"enable_thinking": False}`; `enable_thinking: True` only with `stream=True` (else `invalid_request`). Qwen3.8-flash/27b/max accept `reasoning_effort` (low|medium|xhigh) / `preserve_thinking`; `qwen3.8-2.4t-a95b` text-only, thinking mandatory.
- Prefer current ids: `qwen3.8-max|flash|27b`, `qwen3.7-max|plus`, `qwen3.6-plus|flash`, `qwen3-max`, `qwen3-coder-next`, `qwen3-vl-plus|flash`. Retired (May 2026): `qwen-max`, `qwen-turbo`, `qwen-vl-max|plus`, qwen2.5-vl, small qwen3-0.6b/1.7b/4b, qwen2.5-*-1m → don't use. Web search only on `qwen3-max` (`enable_search` + `search_strategy:"agent"`, +$10/1K searches). Image/embedding/rerank Qwen models: see images.md/embeddings.md/rerank.md (`text-embedding-v4` supports `text_type`/`instruct`).

## OpenAI provider rules (see providers/openai.md)
- Newest: `gpt-6.1-sol` (tier ≥1; no `none`/`minimal` effort), `gpt-6-sol|luna|astra`, `gpt-5.6-sol|terra|luna`, `gpt-5.5`, `gpt-5.4*`. Tiered pricing keyed on **total input length** (>272K → higher rate for the whole request). Responses-only: `gpt-5.4-pro`, `gpt-5.2-pro`, `gpt-5-pro`, `gpt-5.x-codex`, `o3-deep-research`/`o4-mini-deep-research` (tool required; use background mode). Web search: Responses `web_search` tool, or `gpt-4o-search-preview` in Chat. Don't trust examples in the page that POST `messages` to `/v1/responses`. Many ids (gpt-5 `-chat`, gpt-4.5, Sora, gpt-image-1.x, gpt-audio*, o3/GPT-5 snapshots) are removed or scheduled for shutdown → check deprecations first.

## Anthropic/Claude provider rules (see providers/anthropic.md)
- Use base ids (`claude-opus-5-5`, `claude-opus-5`, `claude-sonnet-5-5`, `claude-fable-5-1`, `claude-opus-4-8`, `claude-sonnet-4-6`, `claude-haiku-4-5`) for smart multi-cloud routing (≈10× limits). Anthropic SDK base URL has NO `/v1`. 1M context native on 5.x/4.6+ (else `anthropic-beta: context-1m-2025-08-07`). Fable 5.1 needs tier ≥2; Opus 5.5 responses full, others responses partial.
- Opus 5.5 / Fable 5.1 / Opus 5: thinking is adaptive & **cannot be disabled**, control with `output_config.effort`; never send `temperature`/`top_p`/prefill/forced tool_choice; keep signed thinking blocks intact. Sonnet 5.5: `between_tools` to limit thinking. AvalAI cache-write prices: Sonnet 5.5 $4, Opus 5.5 $8.

## Provider pages added: Google, Meta, Mistral, xAI, Cohere (see providers/*.md)
- Google: Gemini extras via `extra_body={"generationConfig":{…}}`; images base64 only; `gemini-flash-latest`→`gemini-3.8-flash` (promo $0.75/$3.75 until 2026-12-31); code-execution tool excludes all other tools; Google Search billed per call; image models `gemini-3-pro-image`/`3.1-flash-image`/`3.1-flash-lite-image` (Imagen removed); Gemini 3.8 TTS paths only v1beta/chat/audio-speech.
- xAI: `grok-4.7`/`4.6` 500K in/out, don't send `reasoning_effort`; Responses partial; prices ≤200K $2/$6, >200K $4/$12.50.
- Mistral SDK `server_url` without `/v1`; OCR `mistral-ocr-4-0`. Cohere: rerank via raw HTTP; `embed-v-4-0` Azure = 30× limits. Meta: Llama via Bedrock ids; many removed.

## More providers (see providers/{deepseek,zai,bfl,cloudflare,byteplus,stability}.md)
- DeepSeek: all legacy ids route to `deepseek-v4.1-flash` ($0.15/$0.60, cached $0.003); `deepseek-v4-pro` redirected since 2026-09-14. Thinking+tool loops: resend `reasoning_content` within the same turn (else 400), drop it on new user turn.
- Z.AI: `glm-5.3` thinking mandatory (`thinking.type:"enabled"`, effort low|high|max); glm-5.3-flash promo ended 2026-09-09.
- BFL FLUX: `response_format:"b64_json"` only; flux.2-pro per-megapixel pricing. BytePlus `seedream-5-0-260128` $0.035/img, URLs expire 24 h, set `watermark:false`. Stability: no U+200C, English prompts, ids likely removed. Cloudflare `cf.*` ids (many removed).

## Perplexity + search providers (references/providers/perplexity.md, search-providers.md)
- Sonar models (`sonar`, `sonar-pro`, `sonar-reasoning[-pro]`, `sonar-deep-research`): use `/v1/chat/completions`; read `citations`/`search_results`. Do not use `/v1/responses` for them unless verified.
- Raw search: `/v1/search/{tool}` with ids `perplexity-search`, `tavily-search[-advanced]`, `dataforseo-search`, `exa_ai-search`, `parallel_ai-search[-pro]`. Tavily `country` takes full lowercase names; others codes/names per file. Max 20 results, ≤20 domain filters.

## Firecrawl, Moonshot, RunwayML, Groq, NVIDIA NIM
- `firecrawl-search` via `/v1/search` (sources/categories/tbs/scrapeOptions); see providers/firecrawl.md.
- Kimi: prefer `kimi-k3` (alias `kimi-latest`), `reasoning_effort:"max"`; k2-thinking needs max_tokens ≥16000, stream, keep `reasoning_content` in tool loops. Never copy the docs' Responses examples (they use gpt-5.6-luna).
- RunwayML video: `/v1/videos`, prompt ≤1000 chars, input_reference required for gen4.5/gen4_turbo.
- Groq ids `groq.*`; NVIDIA NIM ids `nvidia_nim.*` are research-only (low RPM) — don't use in production.

## MiniMax, ElevenLabs, Serper, Fireworks, rate-limit & batch guides
- MiniMax: `minimax-m3` flagship (1M ctx, price doubles >512K); M2.x reasoning via `extra_body={"reasoning_split":True}` → `reasoning_details`; keep full assistant message/thinking blocks in tool loops; Anthropic SDK base has no /v1.
- ElevenLabs: TTS `/v1/audio/speech` (`eleven_v3` for Persian; priced per second), STT `scribe_v2` `/v1/audio/transcriptions`.
- Serper `serper-search` $0.001/query; Fireworks models: muse-glimmer-30b, nemotron-3.5-lightning, nemotron-3-ultra (responses partial).
- Rate limits are per org+model; Tier 1 = phone verify (200k toman total), Tier2+ = cumulative top-ups $10/50/250/1000; see guides/rate-limits.md. Batch = client-side worker only (guides/batch-processing.md).

## Error handling (references/guides/error-handling.md)
- Always log `error.request_id` / `avalai-request-id`; send `X-Client-Request-Id` for correlation. Retry only 429(rate), 5xx, timeouts, network drops with capped exponential backoff + jitter and `Retry-After`; never blind-retry 400/401/403/404/422, `unsupported_model`, `content_policy_violation`, `insufficient_quota`, `quota_exceeded` (these need a code/account fix, even though quota errors come as 429).
- Read `error.solution` field. WebSocket Responses: `previous_response_not_found` → resend full input with `previous_response_id:null`.

## Text generation guide (references/guides/text-generation.md)
- Default to `/v1/responses` with `instructions` + `input`; read `output_text`; parse `output` by `type`. `instructions` aren't inherited across `previous_response_id`; prior chain is billed. `max_output_tokens` includes reasoning. Prefer `truncation:"disabled"`; set temperature OR top_p. Keep prompts in code, not hosted prompt objects (deprecated).

## Vision (references/guides/vision.md)
- Chat: `image_url:{url,detail}`; Responses: `input_image` with `image_url` as STRING (or `file_id` from Files `purpose:"vision"`). Inline ≤20 MB; set `detail` explicitly. Gemini images must be base64 (no URLs); bbox coords are [ymin,xmin,ymax,xmax] in 0-1000.

## Image generation (references/guides/image-generation.md)
- Use `/v1/images/generations|edits` by default; Responses `image_generation` tool only if verified. Default model `gpt-image-2.5-flare` (pro edits: `gpt-image-2.5-sunburst`); `xhigh`/`max` quality only on those two; results are base64. gpt-6-sol/luna, grok-4.7 are NOT image generators. No `imagen-*`; `gemini-2.5-flash-image` retired 2026-10-02. Non-OpenAI params via `extra_body`; edit prompt must describe full final image + invariants.

## Audio processing (references/guides/audio-processing.md)
- TTS `/v1/audio/speech`, STT `/v1/audio/transcriptions` (`gpt-transcribe`, diarization `gpt-live-transcribe`, `scribe_v2`), translation `/v1/audio/translations`, chat audio via `/v1/chat/completions`. `gpt-4o-mini-tts` is removed; `whisper-1`, `gpt-4o-*transcribe*` are legacy with shutdown 2027-02-26 (sources conflict on whether live now — prefer `gpt-transcribe`/`scribe_v2`, verify `/v1/models`). Realtime is NOT available — don't emit realtime/SIP code. Gemini 3.8 TTS: only v1beta, chat, `/v1/audio/speech` (voice as object).

## Realtime (references/guides/realtime-audio.md) — NOT implemented
- Never generate code for `/v1/realtime*`, WebRTC/SIP sessions or `gpt-realtime-*`. Use transcribe → Responses → TTS.

## Speech-to-text (references/guides/speech-to-text.md)
- STT: file transcription only; legacy ids (`whisper-1`, `gpt-4o-*transcribe*`) shut down 2027-02-26 — prefer `gpt-transcribe`/`gpt-live-transcribe`/`scribe_v2` after checking `/v1/models`. Diarization: `diarized_json` + `chunking_strategy:"auto"`; streaming only on non-Whisper models; translation → English only.

## Text-to-speech (references/guides/text-to-speech.md)
- TTS default `gpt-audio-1.5` (voices marin/cedar first); `gpt-4o-mini-tts`/`tts-1*` are gone — api-reference/audio.md samples using them are stale. Gemini 3.8 TTS: object voice, verbatim text (no "Say:" prefixes), check MIME (wav vs L16), only speech/chat/v1beta routes. ≤4,096 chars/request.

## Moderation guide (references/guides/moderation.md)
- Use `omni-moderation-latest` on `/v1/moderations` for input AND output checks; image input only with omni; `sexual/minors`, harassment/hate are text-only. Inline `moderation={...}` on Responses is route-dependent; log request ids, never silently drop blocked requests.
