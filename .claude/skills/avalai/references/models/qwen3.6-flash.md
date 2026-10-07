# Model: `qwen3.6-flash`
URL: `https://docs.avalai.ir/fa/models/qwen3.6-flash` · Provider: `alibaba` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `991,000`
- **Max output tokens**: `64,000`
- **Endpoints supported**: `/v1/chat/completions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `cache_creation_input` | $0.3125 |
| `cache_creation_input_above_256K` | $1.25 |
| `cached_input` | $0.025 |
| `cached_input_above_256K` | $0.1 |
| `input` | $0.25 |
| `input_above_256K` | $1 |
| `output` | $1.5 |
| `output_above_128K` | $4 |

### Long-context Tier Overrides
| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |
|---|---:|---:|---:|
| >256,000 | $0.75 | $3.00 | $0.00 |

## Capabilities
`supports_function_calling`, `supports_reasoning`, `supports_tool_choice`, `supports_video_input`, `supports_vision`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 100.0 | 1,000,000.0 |
| Tier 2 | 750.0 | 2,000,000.0 |
| Tier 3 | 1,500.0 | 4,000,000.0 |
| Tier 4 | 3,500.0 | 8,000,000.0 |
| Tier 5 | 10,000.0 | 10,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل Qwen3.6 Flash در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل Qwen3.6 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.6-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل Qwen3.6 Flash در AvalAI چقدر است؟**: API مدل Qwen3.6 Flash در AvalAI برای هر یک میلیون توکن ورودی — و برای هر یک میلیون توکن خروجی — هزینه دارد.
- **هزینه توکن مدل Qwen3.6 Flash چقدر است؟**: قیمت فعلی AvalAI برای مدل Qwen3.6 Flash معادل — برای ورودی و — برای خروجی است.
- **پنجره زمینه مدل Qwen3.6 Flash چقدر است؟**: حداکثر ورودی ثبت‌شده برای Qwen3.6 Flash برابر 991,000 توکن است.
- **محدودیت نرخ مدل Qwen3.6 Flash در AvalAI چقدر است؟**: در سطح 5 مدل Qwen3.6 Flash در AvalAI تا 10,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل Qwen3.6 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل Qwen3.6 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.
- **برای استفاده از مدل Qwen3.6 Flash در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل Qwen3.6 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
