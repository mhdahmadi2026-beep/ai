# Model: `deepseek-chat`
URL: `https://docs.avalai.ir/fa/models/deepseek-chat` · Provider: `deepseek` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `131,072`
- **Max output tokens**: `8,192`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.007 |
| `input` | $0.22 |
| `output` | $0.66 |

## Capabilities
`supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_prompt_caching`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 250.0 | 500,000.0 |
| Tier 2 | 500.0 | 2,000,000.0 |
| Tier 3 | 1,500.0 | 4,000,000.0 |
| Tier 4 | 2,500.0 | 8,000,000.0 |
| Tier 5 | 5,000.0 | 15,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل DeepSeek V3 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل DeepSeek V3 یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-chat` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل DeepSeek V3 در AvalAI چقدر است؟**: API مدل DeepSeek V3 در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.
- **هزینه توکن مدل DeepSeek V3 چقدر است؟**: قیمت فعلی AvalAI برای مدل DeepSeek V3 معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل DeepSeek V3 چقدر است؟**: حداکثر ورودی ثبت‌شده برای DeepSeek V3 برابر 131,072 توکن است.
- **محدودیت نرخ مدل DeepSeek V3 در AvalAI چقدر است؟**: در سطح 5 مدل DeepSeek V3 در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل DeepSeek V3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل DeepSeek V3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار.
- **برای استفاده از مدل DeepSeek V3 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل DeepSeek V3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
