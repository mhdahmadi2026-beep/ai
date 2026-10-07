# مدل جدید اضافه شد: Claude Sonnet 4.6

**تاریخ:** 1404-11-30 / (2026-02-19)

## خلاصه

مدل Claude Sonnet 4.6، قوی‌ترین مدل Sonnet شرکت Anthropic، اکنون در AvalAI در دسترس است. این ارتقای کامل، مهارت‌های کدنویسی، استفاده از کامپیوتر، استدلال زمینه طولانی، برنامه‌ریزی عامل، کار دانشی و طراحی را بهبود می‌بخشد. Sonnet 4.6 دارای پنجره زمینه ۱ میلیون توکنی در نسخه بتا است و در بسیاری از وظایف دنیای واقعی با عملکرد کلاس Opus برابری یا از آن پیشی می‌گیرد، در حالی که قیمت‌گذاری سطح Sonnet را حفظ می‌کند.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Sonnet 4.6** (`claude-sonnet-4-6`)، مدل ارتقا یافته Sonnet شرکت Anthropic با بهبودهای قابل توجه در کدنویسی، استفاده از کامپیوتر و قابلیت‌های عاملی را اعلام می‌کنیم. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**

- **ارتقای کامل مدل**: بهبود در کدنویسی، استفاده از کامپیوتر، استدلال زمینه طولانی، برنامه‌ریزی عامل، کار دانشی و طراحی
- **پنجره زمینه ۱ میلیون توکنی**: پشتیبانی بتا از پنجره زمینه گسترده تا ۱ میلیون توکن
- **برتری در استفاده از کامپیوتر**: بهبود چشمگیر در مهارت‌های استفاده از کامپیوتر نسبت به مدل‌های Sonnet قبلی، با مقاومت بهبود یافته در برابر تزریق پرامپت
- **عملکرد کلاس Opus**: نزدیک به هوش سطح Opus با قیمت‌گذاری Sonnet در وظایف اداری ارزشمند اقتصادی دنیای واقعی
- **بهبودهای کدنویسی**: ۷۰٪ ترجیح نسبت به Sonnet 4.5 در Claude Code، خواندن بهتر زمینه قبل از تغییر کد، تجمیع منطق مشترک به جای تکرار
- **حتی از Opus 4.5 بهتر**: کاربران Sonnet 4.6 را ۵۹٪ مواقع به Opus 4.5 ترجیح دادند با مهندسی بیش از حد و "تنبلی" به طور قابل توجهی کمتر
- **استدلال زمینه طولانی**: استدلال مؤثر در کل پایگاه‌های کد، قراردادهای طولانی، یا ده‌ها مقاله تحقیقاتی
- **تفکر تطبیقی**: پشتیبانی از هر دو تفکر تطبیقی و تفکر گسترده
- **فشرده‌سازی زمینه**: پشتیبانی بتا از خلاصه‌سازی خودکار هنگام نزدیک شدن مکالمات به محدودیت‌ها
- **پشتیبانی نقاط پایانی**: در دسترس در v1/chat/completions (پشتیبانی کامل)، v1/messages (پشتیبانی کامل) و v1/responses (پشتیبانی جزئی)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | ورودی ایجاد کش | خروجی |
|-------|-------|--------------|----------------|--------|
| claude-sonnet-4-6 | 3.00 دلار/1M توکن | 1.50 دلار/1M توکن | 3.75 دلار/1M توکن | 15.00 دلار/1M توکن |

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-6",
    "messages": [
      {
        "role": "user",
        "content": "این کد را بررسی کن و بهبودهایی برای نگهداری بهتر پیشنهاد بده."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1739956800,
  "model": "claude-sonnet-4-6",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "کد شما را بررسی می‌کنم و پیشنهادهایی برای بهبود نگهداری ارائه می‌دهم...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 256,
    "prompt_tokens": 32,
    "total_tokens": 288,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 32,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0039360000",
    "irt": 517.11,
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
    "model": "claude-sonnet-4-6",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این برنامه چندفایله را برای ماژولاریتی بهتر بازنویسی کنم."
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
    "model": "claude-sonnet-4-6",
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم.",
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
  model: "claude-sonnet-4-6",
  messages: [
    {
      role: "user",
      content: "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم.",
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
    "model": "claude-sonnet-4-6",
    "max_tokens": 4096,
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-sonnet-4-6",
    max_tokens=4096,
    messages=[
        {
            "role": "user",
            "content": "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم.",
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
  model: "claude-sonnet-4-6",
  max_tokens: 4096,
  messages: [
    {
      role: "user",
      content: "به من کمک کن این پایگاه کد را برای نگهداری بهتر بهبود دهم.",
    },
  ],
});

console.log(message.content[0].text);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های Anthropic](fa/providers/anthropic.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [مرجع API - تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API - پیام‌ها](fa/api-reference/messages.md)
