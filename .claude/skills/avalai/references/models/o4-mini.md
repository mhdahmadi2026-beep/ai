# Model: `o4-mini`
URL: `https://docs.avalai.ir/fa/models/o4-mini` · Provider: `openai` · Mode: `chat` · Min Tier: `1`

## Overview & Token Limits
- **Max input tokens (Context)**: `200,000`
- **Max output tokens**: `100,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.55 |
| `input` | $1.1 |
| `output` | $4.4 |

## Capabilities
`supports_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_tool_choice`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 1 | 100.0 | 450,000.0 |
| Tier 2 | 250.0 | 100,000.0 |
| Tier 3 | 500.0 | 200,000.0 |
| Tier 4 | 1,000.0 | 4,000,000.0 |
| Tier 5 | 1,500.0 | 1,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل o4 Mini در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل o4 Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `o4-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل o4 Mini در AvalAI چقدر است؟**: API مدل o4 Mini در AvalAI برای هر یک میلیون توکن ورودی $1.10 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.
- **هزینه توکن مدل o4 Mini چقدر است؟**: قیمت فعلی AvalAI برای مدل o4 Mini معادل $1.10 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل o4 Mini چقدر است؟**: حداکثر ورودی ثبت‌شده برای o4 Mini برابر 200,000 توکن است.
- **محدودیت نرخ مدل o4 Mini در AvalAI چقدر است؟**: در سطح 5 مدل o4 Mini در AvalAI تا 1,500 درخواست در دقیقه و 1,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل o4 Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل o4 Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل o4 Mini در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل o4 Mini در AvalAI به سطح 1 یا بالاتر نیاز دارید.
