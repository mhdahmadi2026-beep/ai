# News 2026-06-07-minimax-m3-added: افزودن مدل پرچم‌دار جدید: MiniMax M3
URL: `https://docs.avalai.ir/fa/news/2026-06-07-minimax-m3-added`


# افزودن مدل پرچم‌دار جدید: MiniMax M3

**Date:** 1405-03-17 / (2026-06-07)

## خلاصه

ما افزودن مدل پرچم‌دار جدید MiniMax با نام `minimax-m3` را اعلام می‌کنیم. M3 قابلیت‌های کدنویسی و عاملی در سطح پیشرو، پنجره زمینه ۱ میلیون توکنی مبتنی بر معماری توجه پراکنده MiniMax (MSA) و درک چندوجهی بومی برای ورودی تصویر و ویدیو را ارائه می‌دهد. این مدل روی `v1/chat/completions` در دسترس است و از طریق `v1/messages` پشتیبانی کامل و روی `v1/responses` پشتیبانی جزئی دارد.


## خلاصه قیمت‌گذاری

| مدل | ورودی ($/۱م توکن) | ورودی کش‌شده ($/۱م توکن) | خروجی ($/۱م توکن) | بالای ۵۱۲K (ورودی / کش‌شده / خروجی) |
|-----|-------------------|--------------------------|-------------------|--------------------------------------|
| `minimax-m3` | $0.60 | $0.12 | $2.40 | $1.20 / $0.24 / $4.80 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m3",
    "messages": [
      {
        "role": "user",
        "content": "این تابع پایتون را برای عملکرد بهتر بازآرایی کن و استدلال خود را توضیح بده."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه پاسخ

```json
{
  "id": "chatcmpl-minimax-m3-abc123",
  "created": 1780270281,
  "model": "minimax-m3",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "تابع بازآرایی‌شده همراه با توضیحات...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 320,
    "prompt_tokens": 28,
    "total_tokens": 348,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0007848000",
    "irt": 89.94,
    "exchange_rate": 114600
  }
}
```

---

## نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m3",
    "messages": [
      {
        "role": "user",
        "content": "یک هارنس عامل بساز که بتواند یک مقاله پژوهشی را تجزیه کرده و آزمایش‌های اصلی آن را بازتولید کند."
      }
    ],
    "max_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m3",
    messages=[
        {
            "role": "user",
            "content": "یک هارنس عامل بساز که بتواند یک مقاله پژوهشی را تجزیه کرده و آزمایش‌های اصلی آن را بازتولید کند.",
        }
    ],
    max_tokens=8192,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "minimax-m3",
  messages: [
    {
      role: "user",
      content: "یک هارنس عامل بساز که بتواند یک مقاله پژوهشی را تجزیه کرده و آزمایش‌های اصلی آن را بازتولید کند.",
    },
  ],
  max_tokens: 8192,
});

console.log(response.choices[0].message.content);

```

### Anthropic SDK (v1/messages)

M3 همچنین از طریق فرمت API پیام‌های Anthropic در دسترس است، با پشتیبانی کامل از بلوک‌های thinking بومی و استفاده از ابزار.

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "minimax-m3",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "یک صف وظایف توزیع‌شده مقاوم در برابر خطا طراحی کن."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # توجه: بدون /v1
)

message = client.messages.create(
    model="minimax-m3",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "یک صف وظایف توزیع‌شده مقاوم در برابر خطا طراحی کن."}
    ],
)

print(message.content)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",  // توجه: بدون /v1
});

const message = await client.messages.create({
  model: "minimax-m3",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "یک صف وظایف توزیع‌شده مقاوم در برابر خطا طراحی کن." }
  ],
});

console.log(message.content);

```

---

## پشتیبانی اندپوینت

- **`v1/chat/completions`**: پشتیبانی کامل از طریق API سازگار با OpenAI
- **`v1/messages`**: پشتیبانی کامل از طریق فرمت API پیام‌های Anthropic، شامل بلوک‌های thinking بومی و استفاده از ابزار
- **`v1/responses`**: پشتیبانی جزئی (ورودی/خروجی متنی و استفاده پایه از ابزار)

---

## پیوندهای مستندات

- [مستندات مدل‌های MiniMax](fa/providers/minimax.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
