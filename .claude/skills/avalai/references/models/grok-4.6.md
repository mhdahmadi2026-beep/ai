# Model: `grok-4.6`
URL: `https://docs.avalai.ir/fa/models/grok-4.6` · Provider: `xai` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `500,000`
- **Max output tokens**: `500,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.5 |
| `cached_input_above_200K` | $1.0 |
| `input` | $2.0 |
| `input_above_200K` | $4.0 |
| `output` | $6.0 |
| `output_above_200K` | $12.5 |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >200,000 | $4.00 | $12.00 | $1.00 |

## Capabilities
`supports_function_calling`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_tool_choice`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 40,000.0 |
| Tier 1 | 50.0 | 500,000.0 |
| Tier 2 | 100.0 | 1,000,000.0 |
| Tier 3 | 150.0 | 1,500,000.0 |
| Tier 4 | 200.0 | 2,400,000.0 |
| Tier 5 | 400.0 | 4,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Grok 4.6 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Grok 4.6 یک کلید API در داشبورد AvalAI بسازید و شناسه `xai/grok-4.6` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Grok 4.6 در AvalAI چقدر است؟**: API مدل Grok 4.6 در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $6.00 هزینه دارد.
- **هزینه توکن مدل Grok 4.6 چقدر است؟**: قیمت فعلی AvalAI برای مدل Grok 4.6 معادل $2.00 / 1M tokens برای ورودی و $6.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Grok 4.6 چقدر است؟**: حداکثر ورودی ثبت‌شده برای Grok 4.6 برابر 500,000 توکن است.
- **محدودیت نرخ مدل Grok 4.6 در AvalAI چقدر است؟**: در سطح 5 مدل Grok 4.6 در AvalAI تا 400 درخواست در دقیقه و 4,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Grok 4.6 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Grok 4.6 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل Grok 4.6 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Grok 4.6 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
