# Model: `gpt-6-sol`
URL: `https://docs.avalai.ir/fa/models/gpt-6-sol` · Provider: `openai` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `922,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/responses`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $2.5 |
| `cache_creation_input_above_272K` | $5.0 |
| `cached_input` | $0.2 |
| `cached_input_above_272K` | $0.4 |
| `input` | $2.0 |
| `input_above_272K` | $4.0 |
| `output` | $10.0 |
| `output_above_272K` | $15.0 |
| `search_context_cost_per_query` | ${'low': 0.03, 'medium': 0.035, 'high': 0.05} |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >272,000 | $4.00 | $15.00 | $0.40 |

## Capabilities
`supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_vision`, `supports_web_search`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 10,000.0 |
| Tier 1 | 50.0 | 500,000.0 |
| Tier 2 | 150.0 | 2,000,000.0 |
| Tier 3 | 250.0 | 4,000,000.0 |
| Tier 4 | 1,500.0 | 8,000,000.0 |
| Tier 5 | 10,000.0 | 20,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GPT-6 Sol در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GPT-6 Sol یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-6-sol` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GPT-6 Sol در AvalAI چقدر است؟**: API مدل GPT-6 Sol در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.
- **هزینه توکن مدل GPT-6 Sol چقدر است؟**: قیمت فعلی AvalAI برای مدل GPT-6 Sol معادل $2.00 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GPT-6 Sol چقدر است؟**: حداکثر ورودی ثبت‌شده برای GPT-6 Sol برابر 922,000 توکن است.
- **محدودیت نرخ مدل GPT-6 Sol در AvalAI چقدر است؟**: در سطح 5 مدل GPT-6 Sol در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GPT-6 Sol در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GPT-6 Sol در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی، جست‌وجوی وب.
- **برای استفاده از مدل GPT-6 Sol در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GPT-6 Sol در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
