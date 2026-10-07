# Model: `kimi-latest`
URL: `https://docs.avalai.ir/fa/models/kimi-latest` · Provider: `moonshot` · Mode: `None` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,048,576`
- **Max output tokens**: `943,718`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.3 |
| `input` | $3.0 |
| `output` | $15.0 |
| `search_context_cost_per_query` | ${'low': 0.005, 'medium': 0.005, 'high': 0.01} |

## Capabilities
`supports_function_calling`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_tool_choice`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 50.0 | 200,000.0 |
| Tier 2 | 100.0 | 500,000.0 |
| Tier 3 | 250.0 | 1,000,000.0 |
| Tier 4 | 500.0 | 2,000,000.0 |
| Tier 5 | 5,000.0 | 3,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Kimi Latest در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Kimi Latest یک کلید API در داشبورد AvalAI بسازید و شناسه `openrouter/~moonshotai/kimi-latest` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Kimi Latest در AvalAI چقدر است؟**: API مدل Kimi Latest در AvalAI برای هر یک میلیون توکن ورودی $3.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.
- **هزینه توکن مدل Kimi Latest چقدر است؟**: قیمت فعلی AvalAI برای مدل Kimi Latest معادل $3.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Kimi Latest چقدر است؟**: حداکثر ورودی ثبت‌شده برای Kimi Latest برابر 1,048,576 توکن است.
- **محدودیت نرخ مدل Kimi Latest در AvalAI چقدر است؟**: در سطح 5 مدل Kimi Latest در AvalAI تا 5,000 درخواست در دقیقه و 3,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Kimi Latest در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Kimi Latest در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی.
- **برای استفاده از مدل Kimi Latest در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Kimi Latest در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
