# News 2026-03-10-new-openai-gemini-models-added: استفاده از API پاسخ‌ها برای استدلال پیشرفته
URL: `https://docs.avalai.ir/fa/news/2026-03-10-new-openai-gemini-models-added`
**تاریخ:** ۱۴۰۴-۱۲-۱۹ / (2026-03-10)

# مدل‌های جدید اضافه شدند: سری GPT-5.4 و Gemini 3.1 Flash-Lite Preview

**تاریخ:** ۱۴۰۴-۱۲-۱۹ / (2026-03-10)

## خلاصه

ما افزودن مدل‌های سری GPT-5.4 از OpenAI (شامل GPT-5.4 Pro، GPT-5.4 و GPT-5.3 Chat) و Gemini 3.1 Flash-Lite Preview از گوگل را اعلام می‌کنیم. این مدل‌ها قابلیت‌های استدلال پیشرو، پنجره‌های زمینه گسترده تا ۱.۰۵ میلیون توکن و پردازش چندوجهی مقرون‌به‌صرفه برای وظایف حجم بالا را ارائه می‌دهند.


## خلاصه قیمت‌گذاری

| مدل | ورودی (دلار/۱م توکن) | ورودی کش شده (دلار/۱م توکن) | خروجی (دلار/۱م توکن) |
|-----|----------------------|----------------------------|----------------------|
| `gpt-5.4-pro` | $30.00 | $0.30 | $180.00 |
| `gpt-5.4` | $2.50 | $0.25 | $15.00 |
| `gpt-5.3-chat` | $1.75 | $0.175 | $14.00 |
| `gemini-3.1-flash-lite-preview` | $0.25 | $0.025 | $1.50 |

---

## نمونه درخواست و پاسخ API

### نمونه GPT-5.4 Pro

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.4-pro",
    "input": "یک معماری سیستم توزیع‌شده جامع با در نظر گرفتن تحمل خطا، مقیاس‌پذیری و امنیت برای یک پلتفرم مالی جهانی طراحی کنید.",
    "reasoning": {"effort": "high"}
  }'
```

### نمونه GPT-5.4

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.4",
    "messages": [
      {
        "role": "user",
        "content": "یک ویرایشگر سند مشترک بلادرنگ با حل تعارض پیاده‌سازی کنید."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه GPT-5.3 Chat

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.3-chat",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."
      }
    ]
  }'
```

### نمونه Gemini 3.1 Flash-Lite Preview

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-lite-preview",
    "messages": [
      {
        "role": "user",
        "content": "متن زیر را به آلمانی ترجمه کنید: سلام، دوست داری بعدا پیتزا بخوریم؟ من خیلی گرسنه‌ام!"
      }
    ]
  }'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1741608788,
  "model": "gemini-3.1-flash-lite-preview",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hey, hast du Lust, später Pizza zu holen? Ich bin am Verhungern!",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 22,
    "prompt_tokens": 28,
    "total_tokens": 50,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000400000",
    "irt": 4.58,
    "exchange_rate": 114600
  }
}
```

---

## نمونه‌های استفاده از SDK

### استفاده از GPT-5.4 Pro با پایتون

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از API پاسخ‌ها برای استدلال پیشرفته
response = client.responses.create(
    model="gpt-5.4-pro",
    input="یک معماری سیستم توزیع‌شده جامع برای یک پلتفرم مالی جهانی طراحی کنید.",
    reasoning={"effort": "high"},
)

print(response.output)
```

### استفاده از GPT-5.4 با پایتون

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[
        {"role": "system", "content": "شما یک معمار نرم‌افزار متخصص هستید."},
        {
            "role": "user",
            "content": "یک ویرایشگر سند مشترک بلادرنگ با حل تعارض پیاده‌سازی کنید.",
        },
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)
```

### استفاده از Gemini 3.1 Flash-Lite با پایتون

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[
        {
            "role": "user",
            "content": "نکات کلیدی این سند را به صورت نقطه‌ای خلاصه کنید.",
        }
    ],
)

print(response.choices[0].message.content)
```

### استفاده از Gemini 3.1 Flash-Lite با تفکر

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-preview",
    messages=[{"role": "user", "content": "هوش مصنوعی چگونه کار می‌کند؟"}],
    extra_body={"generationConfig": {"thinkingConfig": {"thinkingLevel": "high"}}},
)

print(response.choices[0].message.content)
```

---

## مستندات

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Google Gemini](fa/providers/google.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
