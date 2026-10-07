# قیمت‌گذاری API AvalAI / Pricing — https://docs.avalai.ir/fa/pricing

Support & feedback for the docs: Telegram https://t.me/AvalAISupport (technical questions, finance inquiries, docs improvements).

> **Live data beats this file.** Prices change. Authoritative, always-current source: `GET https://api.avalai.ir/public/models` (no API key). The pricing page's catalog is generated from `data/models.json`, the same source. Verify before quoting prices/limits to a user or hard-coding costs.

## Principles
- AvalAI pricing is **100% aligned with the base API rates of the original providers** — no hidden markup.
- It's **pay-as-you-go token billing** like official Anthropic API, OpenAI API platform, OpenRouter.ai. **Not** the same as consumer/CLI subscriptions (Claude Pro/Max, Codex plans) whose access rules/usage terms differ from token-based API billing.

## Free credit for new users (up to 200,000 Toman)
- Sign up with **phone number + verify** → **200,000 Toman** free API credit total.
- Initial sign-up with **email** → instant **25,000 Toman**.
- Later link & verify phone → **+175,000 Toman** (total reaches 200,000 — *not* 200,000 on top of the email credit).
- Create/verify account in the dashboard https://chat.avalai.ir/platform/home; use free balance to test supported models before topping up.
- Page SEO title: «قیمت‌گذاری API AvalAI و ۲۰۰٬۰۰۰ تومان اعتبار رایگان ثبت‌نام».
Related: model details /fa/models/model-details · cost optimization (model choice, token budgets, prompt caching, async work, flex routing) /fa/guides/cost-optimization

## Live model list (public endpoint, no key)
```bash
# save response to models.json instead of printing
curl --fail --silent --show-error \
  https://api.avalai.ir/public/models \
  --output models.json
```
```powershell
# Windows PowerShell
Invoke-RestMethod -Uri "https://api.avalai.ir/public/models" `
  -OutFile "models.json"
```
```python
import requests

response = requests.get(
    "https://api.avalai.ir/public/models",
    timeout=30,
)
response.raise_for_status()
models = response.json()["data"]

for model in models:
    print(model["id"], model.get("pricing", {}))
    # rate limits for your account tier (e.g. tier 2)
    tier_limits = model.get("tier_rate_limits", {}).get("2", {})
    print(
        "  tier 2:",
        tier_limits.get("max_requests_per_1_minute"),
        "RPM",
        tier_limits.get("max_tokens_per_1_minute"),
        "TPM",
    )
```
### Response shape
```json
{
  "object": "list",
  "data": [
    {
      "id": "example-model",
      "object": "model",
      "owned_by": "provider",
      "min_tier": 0,
      "mode": "chat",
      "pricing": {
        "input": 1.25,
        "input_above_128K": 2.5,
        "cached_input": 0.125,
        "output": 10.0,
        "output_above_128K": 15.0
      },
      "max_input_tokens": 200000,
      "max_output_tokens": 32000,
      "max_requests_per_1_minute": 1000,
      "max_tokens_per_1_minute": 2000000,
      "tier_rate_limits": {
        "0": { "max_requests_per_1_minute": 1,    "max_tokens_per_1_minute": 40000 },
        "1": { "max_requests_per_1_minute": 50,   "max_tokens_per_1_minute": 500000 },
        "2": { "max_requests_per_1_minute": 250,  "max_tokens_per_1_minute": 1000000 },
        "3": { "max_requests_per_1_minute": 1000, "max_tokens_per_1_minute": 2000000 }
      },
      "supported_endpoints": ["/v1/chat/completions"],
      "supports_vision": true,
      "supports_function_calling": true
    }
  ]
}
```
| Field | Meaning |
|---|---|
| `id` | exact model name for API requests and the model docs path |
| `owned_by` | owner/provider shown in price list |
| `mode` | operation/billing class: `chat`, `embedding`, `image_generation`, `video_generation`, `audio_transcription`, `audio_speech`, `ocr`, `rerank`, `search` |
| `min_tier` | minimum AvalAI account tier required; `tier_rate_limits` always starts at this tier |
| `pricing.input`, `.cached_input`, `.output` | USD per 1M tokens |
| `pricing.*_above_*` | long-context dynamic rate after the token threshold in the key (e.g. `input_above_128K`) |
| `pricing.input_cost_per_page` | OCR per-page cost |
| `pricing.input_cost_per_annotation_page` | OCR annotation per-page cost |
| `pricing.output_cost_per_image_*` | per-image price; suffix = resolution or quality variant |
| `pricing.output_cost_per_video_per_second_*` | per-second video price; suffix = resolution |
| `max_input_tokens`, `max_output_tokens` | published token limits, if any |
| `max_requests_per_1_minute`, `max_tokens_per_1_minute` | highest rate limit available (top tier offered) |
| `tier_rate_limits` | per-tier limits keyed by account tier `"0"`–`"5"`, each with RPM/TPM; higher tiers = more throughput |
| `supported_endpoints` | API paths the model supports |
| `supports_*` | capability flags: vision, function calling, audio, PDF input, caching, structured output |
Pricing fields vary by mode — always inspect the whole `pricing` object; never assume only input/output token rates. Plan throughput from `tier_rate_limits` for **your** tier, not the max tier.

## How billing is computed
Use tables for planning but verify real production cost with the **User API** (/fa/api-reference/user): true cost can exceed visible output tokens.
> **Reasoning tokens:** for all providers/models, hidden `reasoning_tokens` are billed at the selected model's **output token rate**, even if absent from the visible text. When `output_tokens` already includes reasoning, `output_tokens_details.reasoning_tokens` is just a breakdown — **don't add both** (double count). If a route reports visible output and reasoning separately, sum them and apply the output rate to both.
- **Model tokens:** input, cached input, output, hidden reasoning — by selected model/provider.
- **Route capabilities:** Responses, Chat Completions, Batch, image, audio, video, tool workflows may report different fields; the billable unit comes from model, media unit, provider route, service tier, or tool call.
- **Hosted tools:** web search, file search, hosted containers, code-interpreter-like runtimes may add separate call/storage/session cost if enabled on your route.
- **Provider rules:** some add cache-creation cost, long-context surcharge, media seconds, image units, or account-tier-dependent rates.
- **Controls:** set token budgets; use cached prefixes for repeated context; choose `service_tier` deliberately; log `avalai-request-id` so finance/support can reconcile exact transactions.

## Flex service tier (50% cheaper, selected OpenAI models)
> ⚠ Flex has **higher latency**; requests may take longer, time out, or fail mid-processing.
- Faster processing → `service_tier: "default"`. Lower price, higher latency → `"flex"`.
- **Server timeout: flex requests may take up to 900 s (15 min).**
- Production: for time-sensitive use, implement retry with **fallback to `service_tier: "default"`**.
- Some OpenAI examples use `service_tier: "priority"` — on AvalAI use `default` unless priority is explicitly enabled for your account.
- Default: all requests use `"default"` unless specified. Enable with `"service_tier": "flex"`. Server **rejects** `flex` for unsupported models. Every API response includes a `"service_tier"` field. Public values: `"default"`, `"flex"` (`"priority"` is account-specific until documented for your route).

Flex prices (USD per 1M tokens; = 50% of standard):
| Model | Input | Cached input | Output |
|---|---|---|---|
| `gpt-5.2` | $0.875 | $0.0875 | $7.00 |
| `gpt-5.1` | $0.625 | $0.0625 | $5.00 |
| `gpt-5` | $0.625 | $0.0625 | $5.00 |
| `gpt-5-mini` | $0.125 | $0.0125 | $1.00 |
| `gpt-5-nano` | $0.025 | $0.0025 | $0.20 |
| `o3` | $1.00 | $0.25 | $4.00 |
| `o4-mini` | $0.55 | $0.275 | $2.20 |
```bash
curl -i https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5-mini",
    "messages": [{"role": "user", "content": "سلام!"}],
    "stream": false,
    "service_tier": "flex"
  }'
```
Sample response (abridged): `"model": "gpt-5-mini-2025-08-07"`, `"service_tier": "flex"`, `"usage": {"completion_tokens":123,"prompt_tokens":7,"total_tokens":130}`, `"estimated_cost": {"unit": "0.0001238750", "irt": 16.27, "exchange_rate": 131350}`.
> ⚠ **Credit packages do NOT cover flex.** Flex cost is deducted from your standard account balance, never from credit-package allocation. Packages apply only to the standard service tier. (see 08-credit-packages)

## Price-update notes (20 Shahrivar)
Covers `deepseek-v4.1-flash`, `grok-4.6`, `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` (USD).
- **DeepSeek V4.1 Flash** per 1M: $0.15 in, $0.003 cached in, $0.60 out. **Flat off-peak rate at all hours** — no peak surcharge, no re-halving. From **23 Shahrivar 1405 (2026-09-14) 04:00 UTC**, `deepseek-v4-pro` requests are **routed to `deepseek-v4.1-flash`** at the same rate. The V4-Pro catalog row shows the pre-change price. Switch to V4.1 Flash now and test before the change.
- **Grok 4.6:** input ≤200K tokens (inclusive): $2.00 in / $0.50 cached / $6.00 out per 1M; >200K: $4.00 / $1.00 / $12.50.
- **GPT Image 2.5 Flare & Sunburst** per 1M tokens: $5.00 text in, $1.25 cached text in, $8.00 image in, $2.00 cached image in, $0.00 text out, $30.00 image out. Zero text-out ≠ free image generation.
- Estimated cost per **one 1024×1024 output image** (identical for both models; add prompt/reference-image input cost; not fixed per-edit prices): `low` $0.00588 · `medium` $0.01317 · `high` $0.05268 · `xhigh` $0.09366 · `max` $0.21072.
- See /fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added and /fa/api-reference/images (image cost notes).

## GPT-6.1 Sol & Claude Sonnet 5.5 (USD per 1M tokens; available from tier 1)
| Model / total request input length | Input | Cached input | Cache-creation input | Output |
|---|---:|---:|---:|---:|
| `gpt-6.1-sol`, ≤272K (inclusive) | $2.00 | $0.10 | $2.50 | $10.00 |
| `gpt-6.1-sol`, >272K | $4.00 | $0.20 | $5.00 | $15.00 |
| `claude-sonnet-5-5` | $2.00 | $0.20 | $4.00 | $10.00 |
For Sol, exactly 272K input stays in the lower band; total request input length decides input & output rate. Cache read in the standard band is half the GPT-6 Sol cache-read price. **Sonnet 5.5 cache-creation on AvalAI = $4.00** (differs from upstream $2.50); it doesn't specify cache retention time and has no separate long-context band. Reasoning consumes billable output tokens — include in estimates. Both fully support Chat Completions & Messages; Responses: **full for Sol, partial for Sonnet 5.5**. /fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added

## Gemini 3.8 TTS promo & migration (USD per 1M tokens: text in, cached text in, audio out — not per second/file)
**Promo: 8 Mehr → end of 10 Dey 1405 (2026-09-30 → 2026-12-31)**
| Model | In | Cached | Audio out |
|---|---:|---:|---:|
| `gemini-3.8-flash-tts` | $0.50 | $0.125 | $9.00 |
| `gemini-3.8-flash-lite-tts` | $0.50 | $0.125 | $6.00 |
**Standard from 11 Dey 1405 (2027-01-01)**
| Model | In | Cached | Audio out |
|---|---:|---:|---:|
| `gemini-3.8-flash-tts` | $1.00 | $0.25 | $18.00 |
| `gemini-3.8-flash-lite-tts` | $1.00 | $0.25 | $12.00 |
Flash: creative narration, regional accents, long-speech voice stability; Lite: high-volume voice-agent pipelines & read-aloud. Flash supports **130** languages, Lite **101**; Persian in both. Rates don't specify cache retention, account-tier or throughput quota.
Migration (from `gemini-3.1-flash-tts-preview`, `gemini-2.5-flash-tts`, `gemini-2.5-pro-tts`, `gemini-2.5-flash-preview-tts`, `gemini-2.5-pro-preview-tts`): change request structure and, if needed, endpoint. AvalAI serves 3.8 **only** via native `/v1beta/models`, `/v1/chat/completions`, `/v1/audio/speech` — not legacy Vertex, Live, Interactions or extra upstream audio endpoints. Keep speech text verbatim; put each native part's `speaker` and `style` in `speechMetadata` (camelCase). Single-request native 3.8 response is **WAV by default** — check MIME before decoding. Chat uses `audio.format: "pcm16"`; Speech can explicitly ask `response_format: "mp3"`. Legacy 3.1 is PCM16-only — never save raw PCM with an .mp3 extension. /fa/news/2026-09-30-gemini-3-8-tts-models-added

## Promotional rates noted in catalog preamble
- **GLM-5.3-Flash:** $0.075 in / $0.015 cached / $0.25 out until **18 Shahrivar 1405 (Sept 9, 2026)**; standard after: $0.15 / $0.03 / $0.50.
- **Gemini 3.8 Flash** (`gemini-3.8-flash`, alias `gemini-flash-latest`): $0.75 / $0.075 / $3.75 until **10 Dey 1405 (Dec 31, 2026)**; standard after: $1.50 / $0.15 / $7.50.
- "Prices labeled *above N tokens* apply when billable context exceeds the provider threshold." Catalog column "rate limits" shows RPM/TPM per tier from `tier_rate_limits`; tiers below a model's `min_tier` are **"no access"**.

## Built-in tools (not model IDs; tokens used by tools are still billed at the chosen model's rate)
| Tool | Cost | Note |
|---|---|---|
| Code Interpreter | $0.03 / session | |
| File Search Storage | $0.10 / GB / day | first 1 GB free |
| File Search Tool Call | $2.50 / 1000 calls | Responses API |

## Cost tracking
### 1) Estimated cost (basic) — field `estimated_cost` (optional) in responses
| Field | Meaning |
|---|---|
| `unit` | cost in USD/USDT |
| `irt` | cost in Toman = USD cost × USDT→Toman rate |
| `exchange_rate` | current USDT→Toman rate used |
```json
{
  "id": "response-123456",
  "object": "chat.completion",
  "created": 1714911234,
  "model": "gpt-4o",
  "choices": [...],
  "usage": {"prompt_tokens": 42, "completion_tokens": 128, "total_tokens": 170},
  "estimated_cost": {"unit": 0.0025, "irt": 200, "exchange_rate": 80000}
}
```
Notes: may be absent from some responses; non-stream → in main response; streaming → attached to the **last chunk**; **not guaranteed — never use for billing/accounting.**
### 2) User API (exact, guaranteed) — base `https://api.avalai.ir/user/v1`
Exact cost per call; track via `avalai-request-id` response header (/fa/api-reference/response-headers#avalai-request-id); available within **30 s**; transaction history with filters; usage analytics by model/provider/date/hour. For resellers, large orgs, production apps.
```bash
# 1. call API, get avalai-request-id from response headers
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o-mini", "messages": [{"role": "user", "content": "سلام"}]}'
# response includes: avalai-request-id: 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a

# 2. exact cost (available within 30 s)
curl "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]}'
```
More: /fa/api-reference/user · /fa/resellers/cost-tracking-guide · /fa/resellers/enterprise-guide
Related: /fa/models/model-details · /fa/quickstart · /fa/performance · /fa/guides/rate-limits

---
# Model price catalog snapshot (generated on the page from data/models.json; snapshot ≈ Mehr 1405)
Compact form. **USD per 1M tokens** unless stated. Columns: `in / cached-in / out`; `cw` = cache-creation input; `>N` = rate when input exceeds N tokens (shown as in/cached/out or cw). `search ctx` = web-search context fee per request (low $0.03 / medium $0.035 / high $0.05 for OpenAI models; xAI $0.025; Moonshot $0.005/$0.005/$0.01). **Per-tier RPM/TPM and access tiers are NOT transcribed here** — they come from `tier_rate_limits` live and from 09-rate-limits when captured.
Where I noticed tier access limits in the catalog: models marked "no access" at base tier include gpt-6.1-sol, claude-sonnet-5-5, claude-opus-5-5, gpt-6-astra, claude-fable-5-1 (also none at tier 1), qwen3.8-2.4t-a95b, qwen3.8-max, claude-opus-5, claude-fable-5, claude-sonnet-5, all Claude 4.x, gpt-5.4-pro (none at base & T1), gpt-5.2-pro (none until T3), o1-pro (none until T4), o3 (T2+), qwen-max (T5 only), gpt-5-pro (T2+), o3-pro, grok-4 family (T1+), image/video models (T1+).

## Chat / Responses / Completion
| Model | Owner | Pricing |
|---|---|---|
| gpt-6.1-sol | openai | 2 / 0.10 / 10; cw 2.50; >272K: 4 / 0.20 / 15, cw 5; search ctx |
| claude-sonnet-5-5 | anthropic | 2 / 0.20 / 10; cw 4 |
| claude-opus-5-5 | anthropic | 4 / 0.20 / 20; cw 8 |
| gpt-6-sol | openai | 2 / 0.20 / 10; cw 2.50; >272K: 4 / 0.40 / 15, cw 5; search ctx |
| gpt-6-luna | openai | 0.10 / 0.01 / 0.50; cw 0.125; >272K: 0.20 / 0.02 / 0.75, cw 0.25; search ctx |
| grok-4.7 | xai | 2 / 0.50 / 6; >200K: 4 / 1 / 12.50 |
| deepseek-v4.1-flash | deepseek | 0.15 / 0.003 / 0.60 |
| gpt-6-astra | openai | 10 / 1 / 50; cw 12.50; >272K: 20 / 2 / 75, cw 25; search ctx |
| gemini-3.8-flash | google | 0.75 / 0.075 / 3.75 (promo; std 1.50/0.15/7.50) |
| claude-fable-5-1 | anthropic | 10 / 0.25 / 50; cw 12.50 |
| glm-5.3-flash | zai | 0.075 / 0.015 / 0.25 (promo) |
| glm-5.3 | zai | 1.40 / 0.26 / 4.40 |
| gemini-3.7-flash | google | 0.75 / 0.075 / 3.75 |
| qwen3.8-flash | alibaba | 0.15 / 0.016 / 0.47; cw 0.20 |
| qwen3.8-27b | alibaba | 0.50 / 0.10 / 2; cw 0.625 |
| qwen3.8-2.4t-a95b | alibaba | 2 / 0.25 / 6; cw 2.50 |
| qwen3.8-max | alibaba | 2 / 0.25 / 6; cw 2.50 |
| claude-opus-5 | anthropic | 5 / 0.50 / 25; cw 6.25 |
| gemini-3.6-flash | google | 1.50 / 0.15 / 7.50 |
| gemini-3.5-flash-lite | google | 0.30 / 0.03 / 2.50 |
| kimi-k3 | moonshot | 3 / 0.30 / 15; search ctx (Moonshot rates) |
| gpt-5.6-sol | openai | 5 / 0.50 / 12; cw 2.50; >272K: 10 / 1 / 45, cw 12.50 (as printed); search ctx |
| gpt-5.6-terra | openai | 2 / 0.20 / 12; cw 2.50; >272K: 4 / 0.40 / 18, cw 5; search ctx |
| gpt-5.6-luna | openai | 0.20 / 0.02 / 1.20; >272K: 0.40 / 0.04 / 1.80; search ctx |
| grok-4.6 | xai | 2 / 0.50 / 6; >200K: 4 / 1 / 12.50 |
| grok-4.5 | xai | 2 / 0.50 / 6; >200K: 4 / 1 / 12.50 |
| claude-fable-5 | anthropic | 10 / 1 / 50; cw 12.50 |
| claude-sonnet-5 | anthropic | 3 / 0.30 / 15; cw 6 |
| glm-5.2 | zai | 1.40 / 0.26 / 4.40 |
| kimi-k2.7-code | moonshot | 0.95 / 0.19 / 4; search ctx |
| kimi-k2.7-code-highspeed | moonshot | 1.90 / 0.38 / 8; search ctx |
| muse-glimmer-30b | nvidia | 0.35 / 0.04 / 1.50 |
| nemotron-3.5-lightning | nvidia | 0.05 / 0.01 / 0.20 |
| nemotron-3-ultra | nvidia | 0.60 / 0.12 / 2.40 |
| minimax-m3 | minimax | 0.30 / 0.06 / 1.20; >512K: 0.60 / 0.12 / 2.40 |
| qwen3.7-plus | alibaba | 0.40 / 0.04 / 1.60; cw 0.50; >256K: 1.20 / 0.12 / 0.12(as printed), cw 1.50 |
| claude-opus-4-8 | anthropic | 5 / 0.50 / 25; cw 6.25 |
| qwen3.7-max | alibaba | 2.50 / 0.25 / 7.50; cw 3.125 |
| gemini-3.5-flash | google | 1.50 / 0.25 / 9; audio in 1, cached audio 0.50, audio out 1 |
| gemini-3.1-flash-lite | google | 0.25 / 0.025 / 1.50; audio in 0.50 / 0.05, audio out 1.50 |
| grok-4.3 | xai | 1.25 / 0.20 / 2.50; >200K: 2.50 / 0.40 / 5 |
| gpt-5.5 | openai | 5 / 0.50 / 30; >272K: 10 / 1 / 45; search ctx |
| deepseek-flash | deepseek | 0.15 / 0.003 / 0.60 |
| deepseek-v4-pro | deepseek | 0.66 / 0.022 / 1.98 (pre-reroute price; reroutes to v4.1-flash 2026-09-14) |
| deepseek-v4-flash | deepseek | 0.22 / 0.007 / 0.66 |
| qwen3.6-max-preview | alibaba | 1.30 / 0.13 / 7.80; cw 1.625; >128K: 2 / 0.20 / 12, cw 2.50 |
| qwen3.6-flash | alibaba | 0.25 / 0.025 / 1.50; cw 0.3125; >256K: 1 / 0.10, cw 1.25; out >128K: 4 |
| qwen3.6-35b-a3b | alibaba | 0.248 / 0.025 / 1.485 |
| qwen3.6-27b | alibaba | 0.60 / 0.06 / 3.60 |
| kimi-k2.6 | moonshot | 0.95 / 0.16 / 4; search ctx |
| claude-opus-4-7 | anthropic | 5 / 0.50 / 25; cw 6.25 |
| qwen3.6-plus | alibaba | 0.50 / 0.05 / 3; cw 0.625; >256K: 2 / 0.20 / 6, cw 2.50 |
| gemma-4-26b-a4b-it | google | 0.13 / 0.013 / 0.40 |
| gemma-4-31b-it | google | 0.14 / 0.014 / 0.40 |
| gpt-5.4-nano | openai | 0.20 / 0.02 / 1.25; search ctx |
| gpt-5.4-mini | openai | 0.75 / 0.075 / 4.50; search ctx |
| gpt-5.4-pro | openai | 30 / – / 180; >272K: 60 / – / 270; search ctx |
| gpt-5.4 | openai | 2.50 / 0.25 / 15; >272K: 5 / 0.50 / 22.50; search ctx |
| gemini-3.1-flash-lite-preview | google | = gemini-3.1-flash-lite |
| gpt-5.3-codex | openai | 1.75 / 0.175 / 14; search ctx |
| gemini-3.1-pro-preview | google | 2 / 0.825 / 12; >200K: 4 / – / 18; audio in 7 / cached 1.50 / out 7 |
| claude-sonnet-4-6 | anthropic | 3 / 1.50 / 15; cw 3.75 |
| glm-5.1 | zai | 1.40 / 0.26 / 4.40 |
| claude-opus-4-6 | anthropic | 5 / 1.50 / 25; cw 6.25 |
| gemini-3-flash-preview | google | 0.50 / 0.25 / 3; audio in 1.50 / 0.50, out 1.50 |
| gpt-5.2-pro, gpt-5.2-pro-2025-12-11 | openai | 21 / 2.10 / 168; search ctx |
| gpt-5.2, gpt-5.2-2025-12-11 | openai | 1.75 / 0.175 / 14; search ctx |
| gpt-5.1-codex-max | openai | 1.25 / 0.125 / 10; search ctx |
| mistral-large-3 | mistral ai | 0.50 / 0.05 / 1.50; OCR page $0.004, annotation page $0.005 |
| anthropic.claude-opus-4-8, anthropic.claude-opus-4-7 | anthropic | 5 / 0.50 / 25; cw 6.25 |
| claude-opus-4-5 | anthropic | 5 / 1.50 / 25; cw 6.25 |
| claude-sonnet-4-5 | anthropic | 3 / 1.50 / 15; cw 3.75 |
| claude-haiku-4-5 | anthropic | 1 / 0.50 / 5; cw 1.25 |
| anthropic.claude-sonnet-4-6 | anthropic | 3 / 1.50 / 15; cw 3.75 |
| anthropic.claude-opus-4-6-v1 | anthropic | 5 / 1.50 / 25; cw 6.25 |
| codex-auto-review | openai | 2 / 0.20 / 12; cw 2.50; >272K: 4 / 0.40 / 18, cw 5 |
| gpt-5.1, gpt-5.1-2025-11-13 | openai | 1.25 / 0.125 / 10; search ctx |
| gpt-audio-1.5, gpt-audio, gpt-audio-2025-08-28 | openai | 2.50 / 1.25 / 10; audio in 32, audio out 64 |
| gpt-audio-mini, gpt-audio-mini-2025-10-06 | openai | 0.60 / 0.30 / 2.40; audio in 10, audio out 20 |
| gemini-robotics-er-1.5-preview | google | 0.30 / 0.15 / 2.50; audio in 1 / 0.25 |
| gemini-2.5-pro-tts | google | 1 / 0.50 / audio out 20 |
| gemini-2.5-flash-tts | google | 0.50 / 0.25 / audio out 10 |
| anthropic.claude-haiku-4-5-20251001-v1:0 | anthropic | 1 / 0.50 / 5; cw 1.25 |
| gpt-5-pro, gpt-5-pro-2025-10-06 | openai | 15 / 1.50 / 120 |
| anthropic.claude-sonnet-4-5-20250929-v1:0 | anthropic | 3 / 1.50 / 15; cw 3.75 |
| groq.llama-guard-4-12b | meta | 0.20 / 0.10 / 0.20 |
| groq.llama-prompt-guard-2-22m | meta | 0.03 / 0.015 / 0.03 |
| groq.llama-prompt-guard-2-86m | meta | 0.04 / 0.02 / 0.04 |
| groq.llama-4-maverick-17b-128e-instruct | meta | 0.20 / 0.10 / 0.60 |
| groq.llama-4-scout-17b-16e-instruct | meta | 0.11 / 0.055 / 0.34 |
| groq.kimi-k2-instruct-0905 | moonshot | 1 / 0.50 / 0.34 (as printed) |
| groq.gpt-oss-120b | openai | 0.15 / 0.075 / 0.75 |
| groq.gpt-oss-20b, groq.gpt-oss-safeguard-20b | openai | 0.075 / 0.0375 / 0.30 |
| groq.qwen3-32b | alibaba | 0.29 / 0.145 / 0.59 |
| sonar | perplexity | 1 / 0.50 / 1; search ctx low 0.005 / med 0.008 / high 0.012 per request |
| sonar-deep-research | perplexity | 2 / 1 / 8; reasoning out 3; citations 2; search ctx 0.005 each |
| sonar-pro | perplexity | 3 / 1.50 / 15; search ctx 0.006 / 0.01 / 0.014 |
| sonar-reasoning | perplexity | 1 / 0.50 / 5; search ctx 0.005 / 0.008 / 0.014 |
| sonar-reasoning-pro | perplexity | 2 / 1 / 8; search ctx 0.006 / 0.01 / 0.014 |
| gemini-flash-lite-latest | google | 0.30 / 0.03 / 2.50; audio in 0.50 / 0.05, out 1.50 |
| gemini-flash-latest | google | 0.75 / 0.075 / 3.75 (promo; alias → gemini-3.8-flash) |
| qwen3.5-flash | alibaba | 0.10 / 0.01 / 0.40; cw 0.125 |
| qwen3-coder-next | alibaba | 0.30 / 0.15 / 1.50 |
| qwen3.5-27b | alibaba | 0.30 / 0.03 / 2.40 |
| qwen3.5-35b-a3b | alibaba | 0.25 / 0.12 / 2 |
| qwen3.5-122b-a10b | alibaba | 0.40 / 0.04 / 3.20 |
| qwen3.5-397b-a17b | alibaba | 0.60 / 0.06 / 3.60 |
| qwen3.5-plus | alibaba | 0.40 / 0.04 / 2.40; cw 0.50; >256K: 1.20 / 0.12 / 7.20, cw 1.50 |
| qwen3-vl-32b-instruct | alibaba | 0.16 / 0.08 / 0.64 |
| qwen-plus-character | alibaba | 0.50 / 0.05 / 1.40 |
| qwen3-max, qwen3-max-2026-01-23, qwen3-max-2025-09-23, qwen3-max-preview | alibaba | 1.20 / 0.10 / 6; >32K: 2.40 / 0.60 / 12; >128K: 3 / 1.20 / 15 |
| grok-4.20-reasoning, grok-4.20-non-reasoning, grok-4.20-beta-0309-reasoning, grok-4.20-beta-0309-non-reasoning | xai | 2 / 0.20 / 6; >200K: 4 / 0.40 / 12 |
| grok-4-1-fast-reasoning, grok-4-1-fast-non-reasoning, grok-4-fast-reasoning, grok-4-fast-non-reasoning | xai | 0.20 / 0.05 / 0.50; search ctx 0.025 |
| minimax-m2.7 | minimax | 0.30 / 0.06 / 1.20; cw 0.375 |
| minimax-m2.7-highspeed | minimax | 0.60 / 0.06 / 2.40; cw 0.375 |
| minimax-m2.5 | minimax | 0.30 / 0.03 / 1.20; cw 0.375 |
| minimax-m2.5-lightning | minimax | 0.30 / 0.03 / 2.40; cw 0.375 |
| deepseek-v3.2, deepseek-v3.2-speciale | deepseek | 0.22 / 0.007 / 0.66 |
| deepseek-v3.1 | deepseek | 0.66 / 0.022 / 1.98 |
| grok-code-fast-1 | xai | 0.20 / 0.02 / 1.50; search ctx 0.025 |
| gpt-oss-120b | openai | 0.30 / 0.15 / 2.50 |
| gpt-5, gpt-5-2025-08-07 | openai | 1.25 / 0.125 / 10 |
| gpt-5-mini, gpt-5-mini-2025-08-07 | openai | 0.25 / 0.025 / 2 |
| gpt-5-nano, gpt-5-nano-2025-08-07 | openai | 0.05 / 0.005 / 0.40 |
| gemini-2.5-flash-lite | google | 0.10 / 0.05 / 0.40; audio 0.10 / 0.05 / 0.40 |
| grok-4-0709, grok-4, grok-4-latest | xai | 3 / 0.75 / 15; search ctx 0.025 |
| o3-pro, o3-pro-2025-06-10 | openai | 20 / 10 / 80 |
| gemini-2.5-pro | google | 1.25 / 0.625 / 10; >200K: 2.50 / – / 15; audio in 1.25 (2.50 >200K), cached 1.50, out 10 (15) |
| gemini-2.5-flash | google | 0.30 / 0.15 / 2.50; audio in 1 / 0.25, out 1 |
| kimi-k2.5 | moonshot | 0.60 / 0.10 / 3; search ctx |
| kimi-latest | moonshot | 3 / 0.30 / 15; search ctx |
| cf.glm-5.2 | google (as printed) | 1.40 / 0.26 / 4.40 |
| cf.kimi-k2.7-code | google (as printed) | 0.95 / 0.19 / 4; search ctx |
| cf.gemma-4-26b-a4b-it | google | 0.10 / 0.01 / 0.30 |
| cf.nemotron-3-120b-a12b | openai (as printed) | 0.50 / 0.05 / 1.50 |
| cf.gpt-oss-120b | openai | 0.35 / 0.175 / 0.75 |
| cf.gpt-oss-20b | openai | 0.20 / 0.10 / 0.30 |
| cf.qwen3-30b-a3b-fp8 | alibaba | 0.051 / 0.025 / 0.34 |
| cf.granite-4.0-h-micro | ibm | 0.017 / 0.008 / 0.11 |
| cf.gemma-sea-lion-v4-27b-it | google | 0.35 / 0.165 / 0.46 |
| cf.llama-4-scout-17b-16e-instruct | meta | 0.27 / 0.14 / 0.85 |
| cf.llama-3.3-70b-instruct-fp8-fast | meta | 0.29 / 0.15 / 2.25 |
| cf.llama-3.1-8b-instruct-fast | meta | 0.045 / 0.022 / 0.384 |
| cf.mistral-small-3.1-24b-instruct | mistral ai | 0.351 / 0.175 / 0.555 |
| cf.qwq-32b, cf.qwen2.5-coder-32b-instruct | alibaba | 0.66 / 0.33 / 1 |
| cf.deepseek-r1-distill-qwen-32b | deepseek | 0.497 / 0.25 / 4.881 |
| cf.llama-3.2-1b-instruct | meta | 0.027 / 0.014 / 0.201 |
| cf.llama-3.2-3b-instruct | meta | 0.051 / 0.025 / 0.335 |
| gemini-2.5-pro-preview-tts | google | 1 / 0.50 / audio out 20 |
| mistral-small-2503 | google (as printed) | 0.10 / 0.05 / 0.30; OCR page 0.004, annotation 0.005 |
| grok-3, grok-3-latest, grok-3-beta | xai | 3 / 1.50 / 15; search ctx 0.025 |
| grok-3-fast, grok-3-fast-latest, grok-3-fast-beta | xai | 5 / 2.50 / 25 |
| grok-3-mini, grok-3-mini-latest, grok-3-mini-beta | xai | 0.30 / 0.15 / 0.50 |
| grok-3-mini-fast, grok-3-mini-fast-latest, grok-3-mini-fast-beta | xai | 0.60 / 0.30 / 4 |
| o1-pro, o1-pro-2025-03-19 | openai | 150 / 75 / 600 |
| o3, o3-2025-04-16 | openai | 2 / 0.50 / 8 |
| qwen3-235b-a22b-fp8-tput | alibaba | 0.20 / 0.10 / 0.60 |
| o4-mini, o4-mini-2025-04-16 | openai | 1.10 / 0.55 / 4.40 |
| gpt-4.1, gpt-4.1-2025-04-14 | openai | 2 / 0.50 / 8; search ctx |
| gpt-4.1-mini, gpt-4.1-mini-2025-04-14 | openai | 0.40 / 0.10 / 1.60; search ctx |
| gpt-4.1-nano, gpt-4.1-nano-2025-04-14 | openai | 0.10 / 0.025 / 0.40 |
| llama-4-maverick-17b-128e-instruct-fp8 | meta | 0.27 / 0.14 / 0.85 |
| llama-4-scout-17b-16e-instruct | meta | 0.18 / 0.09 / 0.59 |
| qwen-flash, qwen-flash-2025-07-28 | alibaba | 0.05 / 0.025 / 0.40; >256K: 0.25 / 0.125 / 2 |
| qwen3-vl-flash, qwen3-vl-flash-2026-01-22, qwen3-vl-flash-2025-10-15 | alibaba | 0.05 / 0.01 / 0.40; >32K: 0.075 / 0.015 / 0.60; >128K: 0.12 / 0.024 / 0.96 |
| qwen3-vl-plus, qwen3-vl-plus-2025-12-19 | alibaba | 0.20 / 0.10 / 1.60; >32K: 0.30 / 0.15 / 2.40; >128K: 0.60 / 0.30 / 4.80 |
| qwen-plus, qwen-plus-latest, qwen-plus-2025-12-01, -2025-09-11, -2025-07-28, -2025-07-14, -2025-04-28 | alibaba | 0.40 / 0.20 / 4 |
| qwen3-next-80b-a3b-thinking | alibaba | 0.144 / 0.072 / 1.434 |
| qwen3-next-80b-a3b-instruct | alibaba | 0.144 / 0.072 / 0.574 |
| qwen3-coder-flash, qwen3-coder-flash-2025-07-28 | alibaba | 0.30 / 0.10 / 1.50; >32K: 0.50 / 0.18 / 2.50; >128K: 0.80 / 0.30 / 4; >256K: 1.60 / 0.60 / 9.60 |
| qwen3-coder-plus, -2025-09-23, -2025-07-22 | alibaba | 1 / 0.10 / 5; >32K: 1.80 / 0.18 / 9; >128K: 3 / 0.30 / 15; >256K: 6 / 0.60 / 60 |
| qwen3-coder-480b-a35b-instruct | alibaba | 1.50 / 0.15 / 7.50; >32K: 2.70 / 0.27 / 13.50; >128K: 4.50 / 0.45 / 22.50 |
| qwen3-235b-a22b-instruct-2507 | alibaba | 0.70 / 0.35 / 2.80 |
| qwen3-235b-a22b-thinking-2507, qwen3-235b-a22b, qwen3-32b | alibaba | 0.70 / 0.35 / 8.40 |
| qwq-32b | alibaba | 1.20 / 0.60 / 1.20 |
| qwq-plus, qwq-plus-2025-03-05 | alibaba | 0.80 / 0.40 / 2.40 |
| qwen3-30b-a3b, qwen3-30b-a3b-thinking-2507 | alibaba | 0.20 / 0.10 / 2.40 |
| qwen3-30b-a3b-instruct-2507 | alibaba | 0.20 / 0.10 / 0.80 |
| qwen3-14b | alibaba | 0.35 / 0.16 / 4.20 |
| qwen3-8b | alibaba | 0.18 / 0.09 / 2.10 |
| qwen-mt-flash, qwen-mt-turbo | alibaba | 0.16 / 0.08 / 0.49 |
| qwen-mt-lite | alibaba | 0.12 / 0.06 / 0.36 |
| qwen-mt-plus | alibaba | 2.46 / 1.20 / 7.37 |
| qwen-max, qwen-max-latest, qwen-max-2025-01-25 | alibaba | 1.60 / 0.80 / 6.40 (tier 5 only) |
| o3-mini, o3-mini-2025-01-31 | openai | 1.10 / 0.55 / 4.40 |
| deepseek-reasoner | deepseek | 0.66 / 0.022 / 1.98 |
| deepseek-chat, deepseek-coder | deepseek | 0.22 / 0.007 / 0.66 |
| gpt-4o-2024-11-20, gpt-4o-2024-08-06, gpt-4o | openai | 2.50 / 1.25 / 10 |
| o1, o1-2024-12-17 | openai | 15 / 7.50 / 60 |
| gpt-4o-2024-05-13 | openai | 5 / 1.25 / 15 |
| gpt-4o-mini, gpt-4o-mini-2024-07-18 | openai | 0.15 / 0.075 / 0.60 |
| nvidia_nim.nemotron-parse, nvidia_nim.nemotron-nano-12b-v2-vl, nvidia_nim.llama-3.3-nemotron-super-49b-v1.5 | nvidia | 0.01 / 0.001 / 0.06 (parse & nano-vl); 0.01 / 0.001 / 0.03 (super-49b) |
| nvidia_nim.gpt-oss-20b | openai | 0.007 / 0.001 / 0.03 |
| nvidia_nim.gpt-oss-120b | openai | 0.03 / 0.015 / 0.25 |

## Embedding models
| Model | Owner | Pricing |
|---|---|---|
| gemini-embedding-2 | google | 0.20 / cached 0.02; image in 0.45, audio in 6.50, video in 12; out 0.15 |
| embed-v-4-0 | cohere | 0.12; image in 0.47 |
| cohere.embed-v4:0 | cohere | 0.12 / 0.06 |
| cf.plamo-embedding-1b | pfn | 0.019 |
| cf.embeddinggemma-300m | google | 0.012 |
| gemini-embedding-001 | google | 0.15 / 0.075 / out 0.15 |
| tongyi-embedding-vision-plus, tongyi-embedding-vision-flash | alibaba | 0.09; image in 0.03; cached 0.0045; out 0.09 |
| text-embedding-v4, text-embedding-v3 | alibaba | 0.07 / 0.0035 / 0.07 |
| cohere.embed-multilingual-v3 | cohere | 0.10 / 0.05 |
| text-embedding-3-large | openai | 0.13 / 0.06 / 0.13 |
| text-embedding-3-small | openai | 0.02 / 0.01 / 0.02 |
| text-embedding-ada-002 | openai | 0.10 / 0.05 / 0.05 |
| nvidia_nim.nv-embedqa-e5-v5, nvidia_nim.nv-embed-v1 | nvidia | 0.002 / 0.001 / 0.002 |

## Image generation models
Token-priced: **gpt-image-2.5-sunburst / -flare**: in 5, image in 8, cached 1.25, cached image 2, image out 30 (per 1M). **gpt-image-2**: in 5, img in 8, cached 1.25, cached img 2, out 10, img out 30. **gpt-image-1.5**: same but img out 32. **gpt-image-1**: in 5, img in 10, cached 1.25, cached img 2.50, out 20, img out 40. **gpt-image-1-mini**: in 2, img in 2.50, cached 0.50, cached img 0.625, out 4, img out 8.
Gemini image (token rates + per-image prices): 
| Model | Token rates (per 1M) | Per image |
|---|---|---|
| gemini-3.1-flash-lite-image | in 0.25, img in 0.25, cached 0.05, img out 30, out 1.50 | $0.0336; 2048² $0.0672; 4096² $0.1344 |
| gemini-3.1-flash-image, gemini-3.1-flash-image-preview | in 0.50, img in 0.50, cached 0.25, img out 60, out 3 | $0.0672; 2048² $0.101; 4096² $0.151 |
| gemini-3-pro-image, gemini-3-pro-image-preview | in 2, img in 2, cached 0.50, img out 120, out 12 | $0.134; 4096² $0.24 |
| gemini-2.5-flash-image | in 0.30, img in 0.30, cached 0.15, img out 30, out 2.50 | $0.04 |
Per-image priced:
| Model | Owner | Price |
|---|---|---|
| flux.2-pro | BFL | out 30/1M-token equivalent; $0.03/img (2MP $0.045, 3MP $0.06, 4MP $0.075); reference MP $0.015/MP; extra MP $0.015/MP |
| gen4_image | runwayml | $0.05 (1920×1080 $0.08) |
| gen4_image_turbo | runwayml | $0.02 |
| seedream-5-0-260128 | bytedance | $0.035 |
| seedream-4-5-251128 | bytedance | $0.04 |
| flux-1.1-pro, flux.1-kontext-pro | BFL | $0.04 |
| wan2.2-t2i-flash | alibaba | $0.025 |
| wan2.2-t2i-plus | alibaba | $0.05 |
| cf.flux-2-klein-9b | BFL | $0.015 (2MP .017, 3MP .019, 4MP .021); extra/ref MP $0.002 |
| cf.flux-2-klein-4b | BFL | $0.01 (.012/.014/.016); extra/ref MP $0.002 |
| cf.flux-2-dev | BFL | $0.01 (.011/.012/.013); extra/ref MP $0.001 |
| cf.lucid-origin, cf.phoenix-1.0 | BFL | $0.015 (.017/.019/.021) |
| z-image-turbo | alibaba | $0.015 standard; $0.03 thinking |
| qwen-image-3.0-pro, qwen-image-3.0 | alibaba | $0.04; 2–4MP $0.075; input image $0.003 |
| qwen-image-2.0-pro | alibaba | $0.075 |
| qwen-image-2.0, qwen-image | alibaba | $0.035 |
| qwen-image-plus, qwen-image-edit-plus | alibaba | $0.03 |
| qwen-image-edit | alibaba | $0.045 |

## Video generation (per second of output video)
veo-3.1-fast-generate-preview $0.15 · veo-3.1-generate-preview $0.40 · veo-3.1-generate-001 $0.40 · veo-3.1-fast-generate-001 $0.15 · gen4.5 (runwayml) $0.12 · gen4_turbo (runwayml) $0.05

## Audio transcription
scribe_v2, scribe_v1 (elevenlabs): $0.00009722/s · gpt-4o-transcribe-diarize & gpt-4o-transcribe: in 2.50, audio in 6, cached 1.50, out 10 /1M, or $0.0001/s · groq.whisper-large-v3: $0.000031/s · groq.whisper-large-v3-turbo: $0.00001111/s · gpt-4o-mini-transcribe: in 1.25, audio in 3, cached 0.75, out 5 /1M or $0.00005/s · whisper-1: $0.0001/s.

## Text-to-speech
gemini-3.8-flash-tts: 0.50 / 0.125 / audio out 9 · gemini-3.8-flash-lite-tts: 0.50 / 0.125 / 6 · gemini-3.1-flash-tts-preview: 1 / 0.50 / 20 · eleven_v3 $0.005/s · eleven_turbo_v2, eleven_turbo_v2_5, eleven_flash_v2, eleven_flash_v2_5 $0.0025/s · eleven_multilingual_v2 $0.005/s · runwayml.eleven_multilingual_v2 $0.000015/char · groq.playai-tts & groq.playai-tts-arabic $0.00005/char · gemini-2.5-flash-preview-tts 0.50 / 0.25 / 10 · tts-1-hd $0.00003/char · tts-1 $0.000015/char.

## OCR
mistral-ocr-2512 $0.002/page (annotation $0.005) · mistral-ocr-4-0 & mistral-ocr-latest $0.004/page (annotation $0.005)

## Moderation
cf.llama-guard-3-8b (meta): 0.484 / 0.242 / 0.03 · omni-moderation-latest, omni-moderation-2024-09-26, text-moderation-latest, text-moderation-stable: no published price field.

## Reranking
cohere-rerank-v4.0-fast $0.002/req · cohere-rerank-v4.0-pro $0.0025/req · semantic-ranker-default-004 $0.001/req · semantic-ranker-fast-004 $0.001/req · cohere.rerank-v3-5:0 $0.002/req · qwen3-rerank in 0.10 / cached 0.0035 per 1M.

## Search models (per request)
serper-search $0.001 · firecrawl-search $0.008 · perplexity-search $0.005 · tavily-search $0.008 · tavily-search-advanced $0.016 · dataforseo-search $0.003 · exa_ai-search $0.025 (results 0–25: $0.005; 26–100: $0.025) · parallel_ai-search $0.004 · parallel_ai-search-pro $0.009.

## Related
/fa/models/model-details · /fa/quickstart · /fa/performance · /fa/guides/rate-limits
