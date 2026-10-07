# Model: `deepseek-v4.1-flash`
URL: `https://docs.avalai.ir/fa/models/deepseek-v4.1-flash` · Provider: `deepseek` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,000,000`
- **Max output tokens**: `393,216`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.003 |
| `input` | $0.15 |
| `output` | $0.6 |

## Capabilities
`supports_assistant_prefill`, `supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 50.0 | 1,000,000.0 |
| Tier 2 | 500.0 | 4,000,000.0 |
| Tier 3 | 1,500.0 | 8,000,000.0 |
| Tier 4 | 2,500.0 | 8,000,000.0 |
| Tier 5 | 10,000.0 | 50,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل DeepSeek V4.1 Flash در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل DeepSeek V4.1 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-v4.1-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل DeepSeek V4.1 Flash در AvalAI چقدر است؟**: API مدل DeepSeek V4.1 Flash در AvalAI برای هر یک میلیون توکن ورودی $0.30 و برای هر یک میلیون توکن خروجی $1.20 هزینه دارد.
- **هزینه توکن مدل DeepSeek V4.1 Flash چقدر است؟**: قیمت فعلی AvalAI برای مدل DeepSeek V4.1 Flash معادل $0.30 / 1M tokens برای ورودی و $1.20 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل DeepSeek V4.1 Flash چقدر است؟**: حداکثر ورودی ثبت‌شده برای DeepSeek V4.1 Flash برابر 1,000,000 توکن است.
- **محدودیت نرخ مدل DeepSeek V4.1 Flash در AvalAI چقدر است؟**: در سطح 5 مدل DeepSeek V4.1 Flash در AvalAI تا 10,000 درخواست در دقیقه و 50,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل DeepSeek V4.1 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل DeepSeek V4.1 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پیش‌پرکردن پاسخ دستیار، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی.
- **برای استفاده از مدل DeepSeek V4.1 Flash در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل DeepSeek V4.1 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
