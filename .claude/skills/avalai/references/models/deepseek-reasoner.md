# Model: `deepseek-reasoner`
URL: `https://docs.avalai.ir/fa/models/deepseek-reasoner` · Provider: `deepseek` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `131,072`
- **Max output tokens**: `65,536`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.022 |
| `input` | $0.66 |
| `output` | $1.98 |

## Capabilities
`supports_native_streaming`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 250.0 | 500,000.0 |
| Tier 2 | 500.0 | 3,000,000.0 |
| Tier 3 | 1,500.0 | 4,000,000.0 |
| Tier 4 | 2,500.0 | 8,000,000.0 |
| Tier 5 | 5,000.0 | 15,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل deepseek-reasoner در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل deepseek-reasoner یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-reasoner` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل deepseek-reasoner در AvalAI چقدر است؟**: API مدل deepseek-reasoner در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.
- **هزینه توکن مدل deepseek-reasoner چقدر است؟**: قیمت فعلی AvalAI برای مدل deepseek-reasoner معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل deepseek-reasoner چقدر است؟**: حداکثر ورودی ثبت‌شده برای deepseek-reasoner برابر 131,072 توکن است.
- **محدودیت نرخ مدل deepseek-reasoner در AvalAI چقدر است؟**: در سطح 5 مدل deepseek-reasoner در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل deepseek-reasoner در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل deepseek-reasoner در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پخش زنده، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی.
- **برای استفاده از مدل deepseek-reasoner در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل deepseek-reasoner در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
