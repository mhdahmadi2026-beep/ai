# Model: `claude-sonnet-5`
URL: `https://docs.avalai.ir/fa/models/claude-sonnet-5` · Provider: `anthropic` · Mode: `chat` · Min Tier: `1`

## Overview & Token Limits
- **Max input tokens (Context)**: `1,000,000`
- **Max output tokens**: `128,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $6.0 |
| `cached_input` | $0.3 |
| `input` | $3.0 |
| `output` | $15.0 |

## Capabilities
`supports_adaptive_thinking`, `supports_anthropic_compaction`, `supports_computer_use`, `supports_function_calling`, `supports_max_reasoning_effort`, `supports_mid_conversation_system`, `supports_native_structured_output`, `supports_output_config`, `supports_pdf_input`, `supports_prompt_caching`, `supports_reasoning`, `supports_response_schema`, `supports_thinking_cache_preservation`, `supports_tool_choice`, `supports_vision`, `supports_xhigh_reasoning_effort`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 1 | 10.0 | 30,000.0 |
| Tier 2 | 100.0 | 450,000.0 |
| Tier 3 | 250.0 | 800,000.0 |
| Tier 4 | 500.0 | 1,000,000.0 |
| Tier 5 | 1,500.0 | 4,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Claude Sonnet 5 در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Claude Sonnet 5 یک کلید API در داشبورد AvalAI بسازید و شناسه `claude-sonnet-5` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Claude Sonnet 5 در AvalAI چقدر است؟**: API مدل Claude Sonnet 5 در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.
- **هزینه توکن مدل Claude Sonnet 5 چقدر است؟**: قیمت فعلی AvalAI برای مدل Claude Sonnet 5 معادل $2.00 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل Claude Sonnet 5 چقدر است؟**: حداکثر ورودی ثبت‌شده برای Claude Sonnet 5 برابر 1,000,000 توکن است.
- **محدودیت نرخ مدل Claude Sonnet 5 در AvalAI چقدر است؟**: در سطح 5 مدل Claude Sonnet 5 در AvalAI تا 1,500 درخواست در دقیقه و 4,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Claude Sonnet 5 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Claude Sonnet 5 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: تفکر تطبیقی، Anthropic compaction، کنترل رایانه، فراخوانی توابع، Max reasoning effort، پیام سیستمی میان گفت‌وگو، خروجی ساختاریافته، Output config، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، Thinking cache preservation، انتخاب ابزار، بینایی، Xhigh reasoning effort.
- **برای استفاده از مدل Claude Sonnet 5 در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Claude Sonnet 5 در AvalAI به سطح 1 یا بالاتر نیاز دارید.
