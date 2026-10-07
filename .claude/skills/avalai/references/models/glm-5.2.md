# Model: `glm-5.2`
URL: `https://docs.avalai.ir/fa/models/glm-5.2` · Provider: `zai` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `991,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.26 |
| `input` | $1.4 |
| `output` | $4.4 |

## Capabilities
`supports_function_calling`, `supports_prompt_caching`, `supports_reasoning`, `supports_tool_choice`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 25.0 | 10,000,000.0 |
| Tier 2 | 250.0 | 4,000,000.0 |
| Tier 3 | 500.0 | 8,000,000.0 |
| Tier 4 | 750.0 | 10,000,000.0 |
| Tier 5 | 1,500.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GLM 5.2 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GLM 5.2 یک کلید API در داشبورد AvalAI بسازید و شناسه `glm-5.2` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GLM 5.2 در AvalAI چقدر است؟**: API مدل GLM 5.2 در AvalAI برای هر یک میلیون توکن ورودی $1.40 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.
- **هزینه توکن مدل GLM 5.2 چقدر است؟**: قیمت فعلی AvalAI برای مدل GLM 5.2 معادل $1.40 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GLM 5.2 چقدر است؟**: حداکثر ورودی ثبت‌شده برای GLM 5.2 برابر 991,000 توکن است.
- **محدودیت نرخ مدل GLM 5.2 در AvalAI چقدر است؟**: در سطح 5 مدل GLM 5.2 در AvalAI تا 1,500 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GLM 5.2 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GLM 5.2 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، انتخاب ابزار.
- **برای استفاده از مدل GLM 5.2 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GLM 5.2 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
