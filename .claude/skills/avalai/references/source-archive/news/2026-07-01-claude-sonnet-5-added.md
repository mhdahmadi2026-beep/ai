# افزودن مدل پرچم‌دار جدید: Claude Sonnet 5

**تاریخ:** 1405-04-10 / (2026-07-01)

## خلاصه

مدل Claude Sonnet 5، عاملی‌ترین (agentic) مدل Sonnet شرکت Anthropic تا به امروز، اکنون در AvalAI در دسترس است. Sonnet 5 فاصله تا عملکرد کلاس Opus را با قیمتی پایین‌تر کاهش می‌دهد و بهبودهای قابل توجهی در استدلال، استفاده از ابزار، کدنویسی و کار دانشی ارائه می‌کند. این مدل از طریق `v1/chat/completions` با پشتیبانی کامل از `v1/messages` و پشتیبانی جزئی از `v1/responses` در دسترس است و با قیمت‌گذاری تبلیغاتی تا ۳۱ آگوست ۲۰۲۶ عرضه می‌شود.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Sonnet 5** (`claude-sonnet-5`)، عاملی‌ترین مدل Sonnet شرکت Anthropic را اعلام می‌کنیم؛ مدلی که برای برنامه‌ریزی، استفاده از ابزارهایی مانند مرورگر و ترمینال و اجرای مستقل در سطحی ساخته شده که تا همین اواخر به مدل‌های بزرگ‌تر و گران‌تر نیاز داشت. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**

- **عاملی‌ترین Sonnet تا کنون**: برنامه‌ریزی، استفاده از ابزارهایی مانند مرورگر و ترمینال، و اجرای مستقل در وظایف طولانی‌مدت
- **نزدیک به عملکرد کلاس Opus**: عملکرد در بسیاری از وظایف عاملی به Claude Opus 4.8 نزدیک می‌شود، با قیمت‌گذاری سطح Sonnet که پایین‌تر است
- **بهبود قابل توجه نسبت به Sonnet 4.6**: پیشرفت‌های روشن در استدلال، استفاده از ابزار، کدنویسی و کار دانشی نسبت به نسخه قبلی
- **کنترل سطح تلاش (Effort)**: طیف گسترده‌ای از گزینه‌های هزینه-عملکرد از طریق سطوح تلاش قابل تنظیم؛ تلاش بالاتر می‌تواند در برخی وظایف با Opus 4.8 برابری کند
- **کدنویسی و اشکال‌زدایی قدرتمند**: کدنویسی مداوم، استفاده از ابزار و اشکال‌زدایی در زمینه‌های فنی پیچیده، با پیگیری تغییرات چندمرحله‌ای تا انتها
- **استفاده از کامپیوتر**: بهبود استفاده عاملی از کامپیوتر در ارزیابی‌هایی مانند OSWorld-Verified
- **ایمنی بهبودیافته**: نرخ کلی رفتارهای نامطلوب پایین‌تر از Sonnet 4.6، بهتر در رد درخواست‌های مخرب و مقاومت در برابر تزریق پرامپت، با نرخ‌های پایین‌تر توهم (hallucination) و چاپلوسی (sycophancy)
- **تفکر تطبیقی**: پشتیبانی از استدلال قابل تنظیم از طریق تنظیمات تفکر و سطوح تلاش
- **پشتیبانی نقاط پایانی**: در دسترس در `v1/chat/completions` (پشتیبانی کامل)، `v1/messages` (پشتیبانی کامل) و `v1/responses` (پشتیبانی جزئی)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | ورودی ایجاد کش | خروجی |
|-------|-------|--------------|----------------|--------|
| claude-sonnet-5 (تبلیغاتی، تا 2026-08-31) | 2.00 دلار/1M توکن | 0.20 دلار/1M توکن | 4.00 دلار/1M توکن | 10.00 دلار/1M توکن |
| claude-sonnet-5 (استاندارد، پس از 2026-08-31) | 3.00 دلار/1M توکن | 0.30 دلار/1M توکن | 6.00 دلار/1M توکن | 15.00 دلار/1M توکن |

> Claude Sonnet 5 با قیمت‌گذاری تبلیغاتی معرفی ۲ دلار/1M ورودی و ۱۰ دلار/1M خروجی تا ۳۱ آگوست ۲۰۲۶ عرضه می‌شود و پس از آن به قیمت‌گذاری استاندارد ۳ دلار/1M ورودی و ۱۵ دلار/1M خروجی منتقل می‌شود.

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-5",
    "messages": [
      {
        "role": "user",
        "content": "این تست شکست‌خورده را بررسی کن، علت اصلی را پیدا کن و راه‌حلی پیشنهاد بده."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-8c2ff...",
  "created": 1782000000,
  "model": "claude-sonnet-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "علت شکست را تا ریشه ردیابی می‌کنم و راه‌حلی پایدار پیشنهاد می‌دهم...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 210,
    "prompt_tokens": 24,
    "total_tokens": 234,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "text_tokens": 210
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 24,
      "image_tokens": null,
      "video_tokens": null,
      "cache_creation_tokens": 0
    },
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  },
  "estimated_cost": {
    "unit": "0.0021480000",
    "irt": 329.07,
    "exchange_rate": 153200
  },
  "service_tier": "default"
}
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-5",
    "messages": [
      {
        "role": "user",
        "content": "سطوح حساب‌ها را به‌روزرسانی کن، سپس یک اطلاعیه راه‌اندازی برای مخاطبان سازمانی تهیه کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[
        {
            "role": "user",
            "content": "سطوح حساب‌ها را به‌روزرسانی کن، سپس یک اطلاعیه راه‌اندازی برای مخاطبان سازمانی تهیه کن.",
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
  model: "claude-sonnet-5",
  messages: [
    {
      role: "user",
      content:
        "سطوح حساب‌ها را به‌روزرسانی کن، سپس یک اطلاعیه راه‌اندازی برای مخاطبان سازمانی تهیه کن.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### استفاده از SDK بومی Anthropic (v1/messages)

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-sonnet-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "این درخواست pull را تا رسیدن به نتیجه تست‌شده و تأییدشده پیش ببر."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "این درخواست pull را تا رسیدن به نتیجه تست‌شده و تأییدشده پیش ببر.",
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
  model: "claude-sonnet-5",
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "این درخواست pull را تا رسیدن به نتیجه تست‌شده و تأییدشده پیش ببر.",
    },
  ],
});

console.log(message.content[0].text);

```

### تفکر تطبیقی و سطح تلاش (Effort)

مدل Claude Sonnet 5 از استدلال قابل تنظیم از طریق تنظیمات تفکر و سطوح تلاش پشتیبانی می‌کند و به شما امکان می‌دهد تعادل بین هزینه و عملکرد را برقرار کنید. سطوح تلاش بالاتر می‌توانند در برخی وظایف با Opus 4.8 برابری کنند، در حالی که سطوح تلاش پایین‌تر کارایی هزینه‌ای به‌طور قابل توجهی بهبودیافته ارائه می‌دهند.

```python
response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[
        {
            "role": "user",
            "content": "یک بازنویسی چندمرحله‌ای را در چند سرویس برنامه‌ریزی و اجرا کن و هر تغییر را تأیید کن.",
        }
    ],
    extra_body={
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "high"},
    },
)
```

---

## لینک‌های مرتبط

- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [قیمت‌گذاری](fa/pricing.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
