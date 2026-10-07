# Model: `gpt-audio-mini`
URL: `https://docs.avalai.ir/fa/models/gpt-audio-mini` · Provider: `openai` · Mode: `chat` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `128,000`
- **Max output tokens**: `16,384`
- **Endpoints supported**: `/v1/chat/completions`, `/v1/responses`, `/v1/realtime`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `audio_input` | $10.0 |
| `audio_output` | $20.0 |
| `cached_input` | $0.3 |
| `input` | $0.6 |
| `output` | $2.4 |

## Capabilities
`supports_audio_input`, `supports_audio_output`, `supports_function_calling`, `supports_native_streaming`, `supports_parallel_function_calling`, `supports_system_messages`, `supports_tool_choice`

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 1.0 | 10,000.0 |
| Tier 1 | 100.0 | 30,000.0 |
| Tier 2 | 1,000.0 | 450,000.0 |
| Tier 3 | 1,500.0 | 800,000.0 |
| Tier 4 | 3,500.0 | 2,000,000.0 |
| Tier 5 | 10,000.0 | 30,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل GPT Audio Mini در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل GPT Audio Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-audio-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل GPT Audio Mini در AvalAI چقدر است؟**: API مدل GPT Audio Mini در AvalAI برای هر یک میلیون توکن ورودی $0.60 و برای هر یک میلیون توکن خروجی $2.40 هزینه دارد.
- **هزینه توکن مدل GPT Audio Mini چقدر است؟**: قیمت فعلی AvalAI برای مدل GPT Audio Mini معادل $0.60 / 1M tokens برای ورودی و $2.40 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل GPT Audio Mini چقدر است؟**: حداکثر ورودی ثبت‌شده برای GPT Audio Mini برابر 128,000 توکن است.
- **محدودیت نرخ مدل GPT Audio Mini در AvalAI چقدر است؟**: در سطح 5 مدل GPT Audio Mini در AvalAI تا 10,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **مدل GPT Audio Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟**: مدل GPT Audio Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، خروجی صوتی، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، پیام‌های سیستمی، انتخاب ابزار.
- **برای استفاده از مدل GPT Audio Mini در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل GPT Audio Mini در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
