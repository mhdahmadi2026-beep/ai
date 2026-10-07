# Model: `gpt-6-astra`
URL: `https://docs.avalai.ir/fa/models/gpt-6-astra` · Provider: `openai` · Mode: `chat` · Min Tier: `1`

## Overview & Token Limits
- **Max input tokens (Context)**: `922,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/responses`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $12.5 |
| `cache_creation_input_above_272K` | $25.0 |
| `cached_input` | $1.0 |
| `cached_input_above_272K` | $2.0 |
| `input` | $10.0 |
| `input_above_272K` | $20.0 |
| `output` | $50.0 |
| `output_above_272K` | $75.0 |
| `search_context_cost_per_query` | ${'low': 0.03, 'medium': 0.035, 'high': 0.05} |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >272,000 | $20.00 | $75.00 | $2.00 |

## Capabilities
`supports_computer_use`, `supports_function_calling`, `supports_max_reasoning_effort`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_cache_breakpoint`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_system_messages`, `supports_tool_choice`, `supports_vision`, `supports_web_search`, `supports_xhigh_reasoning_effort`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 1 | 2.0 | 80,000.0 |
| Tier 2 | 25.0 | 1,000,000.0 |
| Tier 3 | 75.0 | 2,000,000.0 |
| Tier 4 | 500.0 | 8,000,000.0 |
| Tier 5 | 3,500.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GPT-6 Astra در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GPT-6 Astra یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-6-astra` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GPT-6 Astra در AvalAI چقدر است؟**: API مدل GPT-6 Astra در AvalAI برای هر یک میلیون توکن ورودی $10.00 و برای هر یک میلیون توکن خروجی $50.00 هزینه دارد.
- **هزینه توکن مدل GPT-6 Astra چقدر است؟**: قیمت فعلی AvalAI برای مدل GPT-6 Astra معادل $10.00 / 1M tokens برای ورودی و $50.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GPT-6 Astra چقدر است؟**: حداکثر ورودی ثبت‌شده برای GPT-6 Astra برابر 922,000 توکن است.
- **محدودیت نرخ مدل GPT-6 Astra در AvalAI چقدر است؟**: در سطح 5 مدل GPT-6 Astra در AvalAI تا 3,500 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GPT-6 Astra در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GPT-6 Astra در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: کنترل رایانه، فراخوانی توابع، Max reasoning effort، پخش زنده، فراخوانی موازی توابع، ورودی PDF، Prompt cache breakpoint، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی، جست‌وجوی وب، Xhigh reasoning effort.
- **برای استفاده از مدل GPT-6 Astra در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GPT-6 Astra در AvalAI به سطح 1 یا بالاتر نیاز دارید.
