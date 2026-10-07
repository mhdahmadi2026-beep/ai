# Model: `gemini-3.8-flash`
URL: `https://docs.avalai.ir/fa/models/gemini-3.8-flash` · Provider: `google` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,048,576`
- **Max output tokens**: `65,536`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.075 |
| `input` | $0.75 |
| `output` | $3.75 |

## Capabilities
`supports_audio_input`, `supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_url_context`, `supports_video_input`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 40,000.0 |
| Tier 1 | 50.0 | 500,000.0 |
| Tier 2 | 250.0 | 1,000,000.0 |
| Tier 3 | 1,000.0 | 2,000,000.0 |
| Tier 4 | 3,500.0 | 5,000,000.0 |
| Tier 5 | 25,000.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Gemini 3.8 Flash در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Gemini 3.8 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini-3.8-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Gemini 3.8 Flash در AvalAI چقدر است؟**: API مدل Gemini 3.8 Flash در AvalAI برای هر یک میلیون توکن ورودی $0.75 و برای هر یک میلیون توکن خروجی $3.75 هزینه دارد.
- **هزینه توکن مدل Gemini 3.8 Flash چقدر است؟**: قیمت فعلی AvalAI برای مدل Gemini 3.8 Flash معادل $0.75 / 1M tokens برای ورودی و $3.75 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Gemini 3.8 Flash چقدر است؟**: حداکثر ورودی ثبت‌شده برای Gemini 3.8 Flash برابر 1,048,576 توکن است.
- **محدودیت نرخ مدل Gemini 3.8 Flash در AvalAI چقدر است؟**: در سطح 5 مدل Gemini 3.8 Flash در AvalAI تا 25,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Gemini 3.8 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Gemini 3.8 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، زمینه از نشانی وب، ورودی ویدئو، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل Gemini 3.8 Flash در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Gemini 3.8 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
