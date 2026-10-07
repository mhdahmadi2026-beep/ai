# Model: `qwen3.8-max`
URL: `https://docs.avalai.ir/fa/models/qwen3.8-max` · Provider: `alibaba` · Mode: `chat` · Min Tier: `1`

## Overview & Token Limits
- **Max input tokens (Context)**: `991,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $2.5 |
| `cached_input` | $0.25 |
| `input` | $2.0 |
| `output` | $6.0 |

## Capabilities
`supports_function_calling`, `supports_reasoning`, `supports_tool_choice`, `supports_video_input`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 1 | 10.0 | 100,000.0 |
| Tier 2 | 50.0 | 450,000.0 |
| Tier 3 | 150.0 | 1,000,000.0 |
| Tier 4 | 350.0 | 2,000,000.0 |
| Tier 5 | 750.0 | 4,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Qwen3.8 Max در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Qwen3.8 Max یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.8-max` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Qwen3.8 Max در AvalAI چقدر است؟**: API مدل Qwen3.8 Max در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $6.00 هزینه دارد.
- **هزینه توکن مدل Qwen3.8 Max چقدر است؟**: قیمت فعلی AvalAI برای مدل Qwen3.8 Max معادل $2.00 / 1M tokens برای ورودی و $6.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Qwen3.8 Max چقدر است؟**: حداکثر ورودی ثبت‌شده برای Qwen3.8 Max برابر 991,000 توکن است.
- **محدودیت نرخ مدل Qwen3.8 Max در AvalAI چقدر است؟**: در سطح 5 مدل Qwen3.8 Max در AvalAI تا 750 درخواست در دقیقه و 4,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Qwen3.8 Max در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Qwen3.8 Max در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.
- **برای استفاده از مدل Qwen3.8 Max در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Qwen3.8 Max در AvalAI به سطح 1 یا بالاتر نیاز دارید.
