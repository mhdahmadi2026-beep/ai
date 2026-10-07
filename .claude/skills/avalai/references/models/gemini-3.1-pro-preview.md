# Model: `gemini-3.1-pro-preview`
URL: `https://docs.avalai.ir/fa/models/gemini-3.1-pro-preview` · Provider: `google` · Mode: `chat` · Min Tier: `1`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,048,576`
- **Max output tokens**: `65,536`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `audio_cached_input` | $1.5 |
| `audio_input` | $7.0 |
| `audio_output` | $7.0 |
| `cached_input` | $0.825 |
| `input` | $2.0 |
| `input_above_200k` | $4.0 |
| `output` | $12.0 |
| `output_above_200k` | $18.0 |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >200,000 | $4.00 | $18.00 | $0.40 |

## Capabilities
`supports_audio_input`, `supports_function_calling`, `supports_native_streaming`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_url_context`, `supports_video_input`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 1 | 10.0 | 500,000.0 |
| Tier 2 | 75.0 | 2,000,000.0 |
| Tier 3 | 250.0 | 4,000,000.0 |
| Tier 4 | 500.0 | 10,000,000.0 |
| Tier 5 | 10,000.0 | 20,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Gemini 3.1 Pro Preview در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Gemini 3.1 Pro Preview یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini-3.1-pro-preview` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟**: API مدل Gemini 3.1 Pro Preview در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $12.00 هزینه دارد.
- **هزینه توکن مدل Gemini 3.1 Pro Preview چقدر است؟**: قیمت فعلی AvalAI برای مدل Gemini 3.1 Pro Preview معادل $2.00 / 1M tokens برای ورودی و $12.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Gemini 3.1 Pro Preview چقدر است؟**: حداکثر ورودی ثبت‌شده برای Gemini 3.1 Pro Preview برابر 1,048,576 توکن است.
- **محدودیت نرخ مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟**: در سطح 5 مدل Gemini 3.1 Pro Preview در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Gemini 3.1 Pro Preview در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Gemini 3.1 Pro Preview در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، فراخوانی توابع، پخش زنده، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، زمینه از نشانی وب، ورودی ویدئو، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل Gemini 3.1 Pro Preview در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Gemini 3.1 Pro Preview در AvalAI به سطح 1 یا بالاتر نیاز دارید.
