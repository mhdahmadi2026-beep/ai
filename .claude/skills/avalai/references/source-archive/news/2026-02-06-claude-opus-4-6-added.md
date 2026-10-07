# مدل جدید اضافه شد: Claude Opus 4.6

**تاریخ:** 1404-11-17 / (2026-02-06)

## خلاصه

مدل Claude Opus 4.6، قدرتمندترین ارتقای مدل Anthropic، اکنون در AvalAI در دسترس است. این مدل با بهبود مهارت‌های کدنویسی نسبت به نسل قبل، برنامه‌ریزی بهتر، وظایف عاملی پایدار، عملکرد قابل اعتماد در پایگاه‌های کد بزرگتر و قابلیت‌های اشکال‌زدایی بهبود یافته ارائه می‌شود. Opus 4.6 دارای پنجره زمینه 1 میلیون توکنی در نسخه بتا و عملکرد پیشرفته در معیارهای Terminal-Bench 2.0، Humanity's Last Exam و GDPval-AA است.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Opus 4.6** (`claude-opus-4-6`)، مدل پرچمدار ارتقا یافته Anthropic با بهبودهای قابل توجه در کدنویسی عاملی و قابلیت‌های استدلال را اعلام می‌کنیم. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**

- **کدنویسی بهبود یافته**: برنامه‌ریزی بهتر، وظایف عاملی پایدار، عملکرد قابل اعتماد در پایگاه‌های کد بزرگتر، بازبینی کد و اشکال‌زدایی بهبود یافته
- **پنجره زمینه 1 میلیون توکنی**: پشتیبانی بتا برای پنجره زمینه گسترده تا 1 میلیون توکن
- **عملکرد پیشرفته**: بالاترین امتیاز در Terminal-Bench 2.0 (کدنویسی عاملی)، پیشتازی در Humanity's Last Exam (استدلال چندرشته‌ای)، برتری نسبت به GPT-5.2 در GDPval-AA
- **برتری در کار دانشی**: اجرای تحلیل‌های مالی، تحقیق، ایجاد اسناد، صفحات گسترده و ارائه‌ها
- **بهبود زمینه طولانی**: 76% در 8-needle 1M MRCR v2 در مقابل 18.5% برای Sonnet 4.5، کاهش قابل توجه افت زمینه
- **تیم‌های عامل**: قابلیت جدید برای راه‌اندازی چندین عامل به صورت موازی (Claude Code)
- **تفکر تطبیقی**: مدل می‌تواند تشخیص دهد چه زمانی استدلال عمیق‌تر مفید است
- **کنترل تلاش**: چهار سطح تلاش (پایین، متوسط، بالا، حداکثر) برای توسعه‌دهندگان
- **فشرده‌سازی زمینه**: خلاصه‌سازی خودکار برای انجام وظایف طولانی‌تر بدون رسیدن به محدودیت‌ها
- **128K توکن خروجی**: پشتیبانی از تولید خروجی بزرگتر
- **پشتیبانی نقاط پایانی**: در دسترس در v1/chat/completions (پشتیبانی کامل)، v1/messages (پشتیبانی کامل) و v1/responses (پشتیبانی جزئی)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | ورودی ایجاد کش | خروجی |
|-------|-------|--------------|----------------|--------|
| claude-opus-4-6 | 5.00 دلار/1M توکن | 1.50 دلار/1M توکن | 6.25 دلار/1M توکن | 25.00 دلار/1M توکن |

**قیمت‌گذاری پریمیوم (بالای 200K توکن):**
- ورودی: 10.00 دلار/1M توکن
- خروجی: 37.50 دلار/1M توکن

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-6",
    "messages": [
      {
        "role": "user",
        "content": "این پایگاه کد را تحلیل کن و بهبودهای معماری برای نگهداری بهتر پیشنهاد بده."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1738839600,
  "model": "claude-opus-4-6",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "بر اساس تحلیل پایگاه کد شما، بهبودهای معماری زیر را پیشنهاد می‌کنم...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 512,
    "prompt_tokens": 45,
    "total_tokens": 557,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 45,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0130225000",
    "irt": 1710.56,
    "exchange_rate": 131350
  }
}
```

#### نمونه درخواست (v1/messages - فرمت بومی Anthropic)

```bash
curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این برنامه چندفایله پیچیده را دیباگ کنم و مشکلات احتمالی را شناسایی کنم."
      }
    ]
  }'
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-6",
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="claude-opus-4-6",
    messages=[
        {
            "role": "user",
            "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "claude-opus-4-6",
  messages: [
    {
      role: "user",
      content: "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

**فرمت SDK بومی Anthropic:**

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-6",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-opus-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم.",
        }
    ],
)

print(message.content[0].text)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const message = await client.messages.create({
  model: "claude-opus-4-6",
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: "به من کمک کن این پایگاه کد را برای نگهداری بهتر بازنویسی کنم.",
    },
  ],
});

console.log(message.content[0].text);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های Anthropic](fa/providers/anthropic.md)
- [مرجع API - تکمیل چت](fa/api-reference/chat.md)
- [مرجع API - پیام‌ها](fa/api-reference/messages.md)
- [قیمت‌گذاری](fa/pricing.md)
