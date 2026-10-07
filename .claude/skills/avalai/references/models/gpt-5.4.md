# Model: `gpt-5.4`
URL: `https://docs.avalai.ir/fa/models/gpt-5.4` · Provider: `openai` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,050,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/responses`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cached_input` | $0.25 |
| `cached_input_above_272K` | $0.5 |
| `input` | $2.5 |
| `input_above_272K` | $5.0 |
| `output` | $15.0 |
| `output_above_272K` | $22.5 |
| `search_context_cost_per_query` | ${'low': 0.03, 'medium': 0.035, 'high': 0.05} |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >272,000 | $5.00 | $22.50 | $0.50 |

## Capabilities
`supports_function_calling`, `supports_native_streaming`, `supports_none_reasoning_effort`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_vision`, `supports_xhigh_reasoning_effort`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 10,000.0 |
| Tier 1 | 250.0 | 500,000.0 |
| Tier 2 | 500.0 | 2,000,000.0 |
| Tier 3 | 1,000.0 | 4,000,000.0 |
| Tier 4 | 3,500.0 | 8,000,000.0 |
| Tier 5 | 10,000.0 | 20,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GPT-5.4 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GPT-5.4 یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-5.4` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GPT-5.4 در AvalAI چقدر است؟**: API مدل GPT-5.4 در AvalAI برای هر یک میلیون توکن ورودی $2.50 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.
- **هزینه توکن مدل GPT-5.4 چقدر است؟**: قیمت فعلی AvalAI برای مدل GPT-5.4 معادل $2.50 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GPT-5.4 چقدر است؟**: حداکثر ورودی ثبت‌شده برای GPT-5.4 برابر 1,050,000 توکن است.
- **محدودیت نرخ مدل GPT-5.4 در AvalAI چقدر است؟**: در سطح 5 مدل GPT-5.4 در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GPT-5.4 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GPT-5.4 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، None reasoning effort، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی، Xhigh reasoning effort.
- **برای استفاده از مدل GPT-5.4 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GPT-5.4 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
