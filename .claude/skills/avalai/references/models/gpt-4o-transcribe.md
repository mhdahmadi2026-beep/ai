# Model: `gpt-4o-transcribe`
URL: `https://docs.avalai.ir/fa/models/gpt-4o-transcribe` · Provider: `openai` · Mode: `audio_transcription` · Min Tier: `0`

## Overview & Token Limits
- **Max input tokens (Context)**: `16,000`
- **Max output tokens**: `2,000`
- **Endpoints supported**: `/v1/audio/transcriptions`

## Pricing (USD per 1M tokens)
| Metric | Rate ($/1M) |
|---|---:|
| `audio_input` | $6.0 |
| `cached_input` | $1.5 |
| `input` | $2.5 |
| `input_cost_per_second` | $0.0001 |
| `output` | $10.0 |

## Tier Rate Limits
| Tier | RPM | TPM |
|---|---:|---:|
| Tier 0 | 3.0 | 40,000.0 |
| Tier 1 | 500.0 | 200,000.0 |
| Tier 2 | 1,500.0 | 350,000.0 |
| Tier 3 | 3,500.0 | 2,000,000.0 |
| Tier 4 | 5,000.0 | 4,000,000.0 |
| Tier 5 | 10,000.0 | 6,000,000.0 |

## FAQ & Quirks
- **چگونه به API مدل gpt-4o-transcribe در AvalAI دسترسی پیدا کنم؟**: برای دسترسی به API مدل gpt-4o-transcribe یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-4o-transcribe` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.
- **هزینه API مدل gpt-4o-transcribe در AvalAI چقدر است؟**: API مدل gpt-4o-transcribe در AvalAI برای هر یک میلیون توکن ورودی $2.50 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.
- **هزینه توکن مدل gpt-4o-transcribe چقدر است؟**: قیمت فعلی AvalAI برای مدل gpt-4o-transcribe معادل $2.50 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.
- **پنجره زمینه مدل gpt-4o-transcribe چقدر است؟**: حداکثر ورودی ثبت‌شده برای gpt-4o-transcribe برابر 16,000 توکن است.
- **محدودیت نرخ مدل gpt-4o-transcribe در AvalAI چقدر است؟**: در سطح 5 مدل gpt-4o-transcribe در AvalAI تا 10,000 درخواست در دقیقه و 6,000,000 توکن در دقیقه را پشتیبانی می‌کند.
- **برای استفاده از مدل gpt-4o-transcribe در AvalAI چه سطحی لازم است؟**: برای فراخوانی مدل gpt-4o-transcribe در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.
