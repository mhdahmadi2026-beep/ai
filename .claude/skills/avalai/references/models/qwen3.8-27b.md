# Model: `qwen3.8-27b`
URL: `https://docs.avalai.ir/fa/models/qwen3.8-27b` · Provider: `alibaba` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `262,144`
- **Max output tokens**: `131,072`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $0.625 |
| `cached_input` | $0.1 |
| `input` | $0.5 |
| `output` | $2.0 |

## Capabilities
`supports_prompt_caching`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 20.0 | 500,000.0 |
| Tier 2 | 150.0 | 2,000,000.0 |
| Tier 3 | 350.0 | 4,000,000.0 |
| Tier 4 | 750.0 | 8,000,000.0 |
| Tier 5 | 1,500.0 | 20,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Qwen3.8 27B در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Qwen3.8 27B یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.8-27b` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Qwen3.8 27B در AvalAI چقدر است؟**: API مدل Qwen3.8 27B در AvalAI برای هر یک میلیون توکن ورودی $0.50 و برای هر یک میلیون توکن خروجی $2.00 هزینه دارد.
- **هزینه توکن مدل Qwen3.8 27B چقدر است؟**: قیمت فعلی AvalAI برای مدل Qwen3.8 27B معادل $0.50 / 1M tokens برای ورودی و $2.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Qwen3.8 27B چقدر است؟**: حداکثر ورودی ثبت‌شده برای Qwen3.8 27B برابر 262,144 توکن است.
- **محدودیت نرخ مدل Qwen3.8 27B در AvalAI چقدر است؟**: در سطح 5 مدل Qwen3.8 27B در AvalAI تا 1,500 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Qwen3.8 27B در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Qwen3.8 27B در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: کش کردن پرامپت، بینایی.
- **برای استفاده از مدل Qwen3.8 27B در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Qwen3.8 27B در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
