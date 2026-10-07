# AvalAI docs map & capture status

Mark each page DONE when its file exists in this folder. Base: https://docs.avalai.ir/fa/

## Top navigation
| Section | URL | Status |
|---|---|---|
| راهنماها | /guides/best-practices | PENDING |
| مرجع API | /api-reference/introduction | PENDING |
| مدل‌ها | /models (index: /models/index) | PENDING |
| قیمت‌گذاری | /pricing | PENDING |

## Sidebar
### خبرها — /news/ — PENDING
### شروع به کار
| Page | URL | File | Status |
|---|---|---|---|
| معرفی | / | 01-introduction.md | DONE |
| شروع سریع | /quickstart | 02-quickstart.md | DONE |
| استفاده عملی از هوش مصنوعی | /guides/ai-workflows | 03-ai-workflows.md | DONE |
| کتابخانه‌ها | /libraries | 04-libraries.md | DONE |
| عملکرد | /performance | 05-performance.md | DONE (cache benchmark source missing) |
| قیمت‌گذاری | /pricing | 06-pricing.md | DONE (per-tier RPM/TPM per model not transcribed → see rate-limits page / live API) |
| سطوح سرویس | /service-tiers | 07-service-tiers.md | DONE |
| بسته‌های اعتباری | /credit-packages | 08-credit-packages.md | DONE |
| محدودیت‌های نرخ مدل | /rate-limits | 09-rate-limits.md | DONE |
| مدل‌های منسوخ شده | /deprecations | 10-deprecations.md | DONE |

### Collapsed groups (sub-pages still unknown — need user to expand)
- نمایندگان فروش
- مرجع API (known: /api-reference/introduction, /api-reference/responses, /api-reference/images, /api-reference/audio)
- ارائه‌دهندگان
- راهنماها (known: /guides/best-practices, /guides/tools, /guides/structured-outputs, /guides/function-calling, /guides/streaming-responses, /guides/production-best-practices, /guides/prompt-caching)
- ابزارهای داخلی
- بهترین شیوه‌ها
- مثال‌ها
- منابع

## Known model pages (from intro/news)
/models/muse-glimmer-30b, /models/nemotron-3.5-lightning

## Additional URLs discovered in Quickstart (pages still PENDING)
/api-reference/chat, /api-reference/models, /api-reference/user, /api-reference/authentication, /api-reference/response-headers, /guides/responses-vs-chat-completions, /guides/provider-specific-params, /models/model-details, /resellers/cost-tracking-guide, /resellers/enterprise-guide, /safety/content-policy, /news/2025-06-03-anthropic-sdk-support-added, /news/2025-06-09-anthropic-sdk-multi-provider-support
Public endpoints: https://api.avalai.ir/public/models (no auth), /v1/models, /user/v1/transactions/lookup

## Discovered in ai-workflows page (PENDING)
/examples/evidence_based_workflows, /examples/speaker_aware_meeting_intelligence, /examples/manual_rag_with_embeddings, /guides/coding-agent-workflows, /guides/setup-open-webui, /guides/setup-hermes, /guides/setup-opencode, /guides/setup-aider, /guides/setup-9router, /guides/setup-n8n, /guides/speech-to-text, /guides/evals, /guides/rate-limits, /models/

## Discovered in libraries page (PENDING)
/api-reference/v1beta, /api-reference/response-headers (also `X-Client-Request-Id` request header), /guides/responses-vs-chat-completions

## Discovered in performance page (PENDING)
/guides/latency-optimization, /guides/cost-optimization, /guides/token-counting, /guides/prompt-caching

## Discovered in pricing page (PENDING)
/models/model-details, /models/<model-id> pages (one per model), /api-reference/images, /api-reference/user, /resellers/cost-tracking-guide, /resellers/enterprise-guide, /guides/cost-optimization, /news/2026-09-11-..., /news/2026-09-30-gemini-3-8-tts-models-added

## Discovered in service-tiers page (PENDING)
/guides/error-handling, /guides/production-best-practices, /api-reference/responses, /api-reference/chat

## Discovered in rate-limits page (PENDING)
/rate-limits-tier0 … /rate-limits-tier5 (per-model RPM/TPM per tier — high value), /api-reference/user

## Discovered in deprecations page (PENDING)
/guides/model-selection, /providers/{moonshotai,elevenlabs,alibaba,google,zai,minimax}, /examples/{generate_images_with_gpt_image,generate_images_with_seedream_4,web_search_capabilities}, /api-reference/search, /news/2025-11-18-new-models-gemini-3-pro-kimi-k2-thinking, /news/2025-09-27-google-gemini-models-deprecation

## ALL 10 'شروع به کار' sidebar pages are now captured. Remaining groups: خبرها, نمایندگان فروش, مرجع API, ارائه‌دهندگان, راهنماها, ابزارهای داخلی, بهترین شیوه‌ها, مثال‌ها, منابع.

## نمایندگان فروش group
| Page | URL | File | Status |
|---|---|---|---|
| راهنمای پیگیری هزینه نمایندگان | /resellers/cost-tracking-guide | resellers/cost-tracking-guide.md | DONE |
| راهنمای سازمانی | /resellers/enterprise-guide | resellers/enterprise-guide.md | DONE |
(other pages in this group unknown — ask user to expand the group)

Discovered (PENDING): /api-reference/videos, /api-reference/response-headers (incl. LangChain async section)

## مرجع API group
| Page | URL | File | Status |
|---|---|---|---|
| مقدمه | /api-reference/introduction | api-reference/introduction.md | DONE |
| احراز هویت | /api-reference/authentication | api-reference/authentication.md | DONE |
| پاسخ‌ها (Responses) | /api-reference/responses | — | PENDING |
| تکمیل گفتگو | /api-reference/chat | api-reference/chat.md | DONE |
| تصاویر | /api-reference/images | api-reference/images.md | DONE |
| بردارهای تعبیه‌سازی | /api-reference/embeddings | api-reference/embeddings.md | DONE |
| صدا | /api-reference/audio | api-reference/audio.md | DONE |
| نظارت | /api-reference/moderation | api-reference/moderation.md | DONE |
| API کاربر | /api-reference/user | api-reference/user.md | DONE |
| هدرهای پاسخ | /api-reference/response-headers | api-reference/response-headers.md | DONE |
| مدل‌ها | /api-reference/models | api-reference/models.md | DONE |
| v1beta (Gemini native) | /api-reference/v1beta | — | PENDING |
| تنظیم دقیق (Fine-tuning) — NOT IMPLEMENTED | /api-reference/fine-tuning | api-reference/fine-tuning.md | DONE |
| ویدیوها | /api-reference/videos | — | PENDING |
| جستجو | /api-reference/search | — | PENDING |
| (also guides) | /guides/realtime-audio, /guides/error-handling | — | PENDING |

Discovered (PENDING): /guides/{reasoning,predicted-outputs,safety-best-practices,structured-outputs,text-to-speech}, /providers/{openai,anthropic,xai,fireworksai,deepseek}, /examples/processing_audio_in_chat_completion_api, /api-reference/{moderation,search,audio}
