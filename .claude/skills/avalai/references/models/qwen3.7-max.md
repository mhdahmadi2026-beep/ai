# Model: `qwen3.7-max`
URL: `https://docs.avalai.ir/fa/models/qwen3.7-max` · Provider: `alibaba` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `997,952`
- **Max output tokens**: `65,536`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $3.125 |
| `cached_input` | $0.25 |
| `input` | $2.5 |
| `output` | $7.5 |

## Capabilities
`supports_function_calling`, `supports_reasoning`, `supports_tool_choice`, `supports_video_input`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 40,000.0 |
| Tier 1 | 10.0 | 200,000.0 |
| Tier 2 | 25.0 | 1,000,000.0 |
| Tier 3 | 50.0 | 800,000.0 |
| Tier 4 | 75.0 | 1,000,000.0 |
| Tier 5 | 600.0 | 2,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Qwen3.7 Max در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Qwen3.7 Max یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.7-max` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Qwen3.7 Max در AvalAI چقدر است؟**: API مدل Qwen3.7 Max در AvalAI برای هر یک میلیون توکن ورودی $5.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.
- **هزینه توکن مدل Qwen3.7 Max چقدر است؟**: قیمت فعلی AvalAI برای مدل Qwen3.7 Max معادل $5.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Qwen3.7 Max چقدر است؟**: حداکثر ورودی ثبت‌شده برای Qwen3.7 Max برابر 997,952 توکن است.
- **محدودیت نرخ مدل Qwen3.7 Max در AvalAI چقدر است؟**: در سطح 5 مدل Qwen3.7 Max در AvalAI تا 600 درخواست در دقیقه و 2,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Qwen3.7 Max در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Qwen3.7 Max در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.
- **برای استفاده از مدل Qwen3.7 Max در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Qwen3.7 Max در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
