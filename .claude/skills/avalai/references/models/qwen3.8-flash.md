# Model: `qwen3.8-flash`
URL: `https://docs.avalai.ir/fa/models/qwen3.8-flash` · Provider: `alibaba` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `991,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $0.2 |
| `cached_input` | $0.016 |
| `input` | $0.15 |
| `output` | $0.47 |

## Capabilities
`supports_function_calling`, `supports_reasoning`, `supports_tool_choice`, `supports_video_input`, `supports_vision`

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
- **چگونه به API مدل Qwen3.8 Flash در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Qwen3.8 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.8-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Qwen3.8 Flash در AvalAI چقدر است؟**: API مدل Qwen3.8 Flash در AvalAI برای هر یک میلیون توکن ورودی $0.15 و برای هر یک میلیون توکن خروجی $0.47 هزینه دارد.
- **هزینه توکن مدل Qwen3.8 Flash چقدر است؟**: قیمت فعلی AvalAI برای مدل Qwen3.8 Flash معادل $0.15 / 1M tokens برای ورودی و $0.47 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Qwen3.8 Flash چقدر است؟**: حداکثر ورودی ثبت‌شده برای Qwen3.8 Flash برابر 991,000 توکن است.
- **محدودیت نرخ مدل Qwen3.8 Flash در AvalAI چقدر است؟**: در سطح 5 مدل Qwen3.8 Flash در AvalAI تا 1,500 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Qwen3.8 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Qwen3.8 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.
- **برای استفاده از مدل Qwen3.8 Flash در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Qwen3.8 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
