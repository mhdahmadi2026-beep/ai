# Model: `gemini-2.5-flash`
URL: `https://docs.avalai.ir/fa/models/gemini-2.5-flash` · Provider: `google` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,048,576`
- **Max output tokens**: `65,535`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `audio_cached_input` | $0.25 |
| `audio_input` | $1.0 |
| `audio_output` | $1.0 |
| `cached_input` | $0.15 |
| `input` | $0.3 |
| `output` | $2.5 |

## Capabilities
`supports_function_calling`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_url_context`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 50.0 | 1,000,000.0 |
| Tier 2 | 500.0 | 4,000,000.0 |
| Tier 3 | 1,000.0 | 8,000,000.0 |
| Tier 4 | 2,500.0 | 10,000,000.0 |
| Tier 5 | 10,000.0 | 20,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Gemini 2.5 Flash در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Gemini 2.5 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini-2.5-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Gemini 2.5 Flash در AvalAI چقدر است؟**: API مدل Gemini 2.5 Flash در AvalAI برای هر یک میلیون توکن ورودی $0.30 و برای هر یک میلیون توکن خروجی $2.50 هزینه دارد.
- **هزینه توکن مدل Gemini 2.5 Flash چقدر است؟**: قیمت فعلی AvalAI برای مدل Gemini 2.5 Flash معادل $0.30 / 1M tokens برای ورودی و $2.50 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Gemini 2.5 Flash چقدر است؟**: حداکثر ورودی ثبت‌شده برای Gemini 2.5 Flash برابر 1,048,576 توکن است.
- **محدودیت نرخ مدل Gemini 2.5 Flash در AvalAI چقدر است؟**: در سطح 5 مدل Gemini 2.5 Flash در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Gemini 2.5 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Gemini 2.5 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، زمینه از نشانی وب، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل Gemini 2.5 Flash در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Gemini 2.5 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
