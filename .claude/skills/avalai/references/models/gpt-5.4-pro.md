# Model: `gpt-5.4-pro`
URL: `https://docs.avalai.ir/fa/models/gpt-5.4-pro` · Provider: `openai` · Mode: `responses` · Min Tier: `2`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,050,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/responses`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `input` | $30.0 |
| `input_above_272K` | $60.0 |
| `output` | $180.0 |
| `output_above_272K` | $270.0 |
| `search_context_cost_per_query` | ${'low': 0.03, 'medium': 0.035, 'high': 0.05} |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >272,000 | $60.00 | $270.00 | $0.00 |

## Capabilities
`supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_system_messages`, `supports_tool_choice`, `supports_vision`, `supports_web_search`, `supports_xhigh_reasoning_effort`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 2 | 500.0 | 2,000,000.0 |
| Tier 3 | 1,000.0 | 4,000,000.0 |
| Tier 4 | 3,500.0 | 8,000,000.0 |
| Tier 5 | 5,000.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GPT-5.4 Pro در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GPT-5.4 Pro یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-5.4-pro` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GPT-5.4 Pro در AvalAI چقدر است؟**: API مدل GPT-5.4 Pro در AvalAI برای هر یک میلیون توکن ورودی $30.00 و برای هر یک میلیون توکن خروجی $180.00 هزینه دارد.
- **هزینه توکن مدل GPT-5.4 Pro چقدر است؟**: قیمت فعلی AvalAI برای مدل GPT-5.4 Pro معادل $30.00 / 1M tokens برای ورودی و $180.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GPT-5.4 Pro چقدر است؟**: حداکثر ورودی ثبت‌شده برای GPT-5.4 Pro برابر 1,050,000 توکن است.
- **محدودیت نرخ مدل GPT-5.4 Pro در AvalAI چقدر است؟**: در سطح 5 مدل GPT-5.4 Pro در AvalAI تا 5,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GPT-5.4 Pro در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GPT-5.4 Pro در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، پیام‌های سیستمی، انتخاب ابزار، بینایی، جست‌وجوی وب، Xhigh reasoning effort.
- **برای استفاده از مدل GPT-5.4 Pro در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GPT-5.4 Pro در AvalAI به سطح 2 یا بالاتر نیاز دارید.
