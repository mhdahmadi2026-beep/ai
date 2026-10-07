# Model: `kimi-k3`
URL: `https://docs.avalai.ir/fa/models/kimi-k3` · Provider: `moonshot` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `262,144`
- **Max output tokens**: `262,144`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.3 |
| `input` | $3.0 |
| `output` | $15.0 |
| `search_context_cost_per_query` | ${'low': 0.005, 'medium': 0.005, 'high': 0.01} |

## Capabilities
`supports_function_calling`, `supports_tool_choice`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 50.0 | 1,000,000.0 |
| Tier 2 | 100.0 | 4,000,000.0 |
| Tier 3 | 250.0 | 8,000,000.0 |
| Tier 4 | 500.0 | 10,000,000.0 |
| Tier 5 | 5,000.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Kimi K3 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Kimi K3 یک کلید API در داشبورد AvalAI بسازید و شناسه `kimi-k3` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Kimi K3 در AvalAI چقدر است؟**: API مدل Kimi K3 در AvalAI برای هر یک میلیون توکن ورودی $3.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.
- **هزینه توکن مدل Kimi K3 چقدر است؟**: قیمت فعلی AvalAI برای مدل Kimi K3 معادل $3.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Kimi K3 چقدر است؟**: حداکثر ورودی ثبت‌شده برای Kimi K3 برابر 262,144 توکن است.
- **محدودیت نرخ مدل Kimi K3 در AvalAI چقدر است؟**: در سطح 5 مدل Kimi K3 در AvalAI تا 5,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Kimi K3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Kimi K3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، انتخاب ابزار، جست‌وجوی وب.
- **برای استفاده از مدل Kimi K3 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Kimi K3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
