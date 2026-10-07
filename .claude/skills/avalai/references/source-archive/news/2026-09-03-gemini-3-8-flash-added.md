---
hasH1: true
---

# مدل جدید اضافه شد: Gemini 3.8 Flash

**تاریخ:** ۱۴۰۵-۰۶-۱۲ / (2026-09-03)

## خلاصه

مدل [`gemini-3.8-flash`](fa/providers/google.md) گوگل اکنون برای کدنویسی بلندمدت، عامل‌های خودکار، استدلال چندمرحله‌ای و گردش‌کارهای مبتنی بر ابزار از طریق AvalAI در دسترس است. این مدل از API بومی Gemini در [`v1beta/`](fa/api-reference/v1beta.md)، نقطه پایانی [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/messages`](fa/api-reference/messages.md) پشتیبانی می‌کند و پشتیبانی آن از [`v1/responses`](fa/api-reference/responses.md) جزئی است. نام مستعار `gemini-flash-latest` اکنون به `gemini-3.8-flash` اشاره می‌کند.

---

## جزئیات

### Google Gemini 3.8 Flash

[`gemini-3.8-flash`](fa/providers/google.md) جدیدترین مدل Flash گوگل برای بارهای کاری دشوار در حوزه استدلال، کدنویسی و عامل‌های هوشمند است. گوگل در مقایسه با Gemini 3.7 Flash، بهبودهایی را در مهندسی نرم‌افزار، تکمیل خودکار وظایف، استدلال چندمرحله‌ای دقیق و حوزه‌های تخصصی حرفه‌ای گزارش کرده است؛ در عین حال، مدل سرعت رده Flash را حفظ می‌کند.

**ویژگی‌های کلیدی:**

- **کدنویسی بلندمدت**: مناسب وظایف چندمرحله‌ای مهندسی نرم‌افزار، اشکال‌زدایی، پیاده‌سازی و کار روی مخزن کد
- **عامل‌های خودکار**: برنامه‌ریزی، انتخاب ابزار، استفاده تکرارشونده از ابزار و تکمیل گردش‌کارهای طولانی با عملکرد بهتر
- **استدلال پیچیده**: عملکرد قوی‌تر در مسائل مهم چندمرحله‌ای و وظایف تخصصیِ نیازمند دانش
- **تلاش استدلالی قابل تنظیم**: تلاش بیشتر می‌تواند کیفیت وظایف دشوار را افزایش دهد و تلاش کمتر مصرف توکن و تأخیر را کاهش می‌دهد
- **گردش‌کارهای توسعه‌دهندگان**: مناسب عامل‌های کدنویسی، خط لوله‌های پژوهشی، تحلیل سند و خودکارسازی مبتنی بر ابزار
- **انتخاب نقطه پایانی**: قابل استفاده از طریق API بومی Gemini، Chat Completions سازگار با OpenAI و Messages سازگار با Anthropic

### نکته برجسته بنچمارک به گزارش گوگل

گوگل برای Gemini 3.8 Flash امتیاز **۵۴٫۹٪ در HLE-Verified** و عملکرد قوی‌تری در DeepSWE v1.1 گزارش کرده است. این نتایج نشانه پیشرفت در استدلال پیشرفته و مهندسی نرم‌افزار هستند، اما بنچمارک‌ها تنها شواهد جهت‌دهنده‌اند و جای ارزیابی با پرامپت‌ها، ابزارها و معیارهای پذیرش واقعی شما را نمی‌گیرند.

مدل در سطح تلاش استدلالی بالاتر ممکن است توکن خروجی بیشتری مصرف کند، زیرا استدلال و فراخوانی‌های تکرارشونده ابزار بیشتری انجام می‌دهد. هنگام انتخاب سطح تلاش، کیفیت، تأخیر و مصرف توکن را در کنار یکدیگر ارزیابی کنید.

### دسترسی نقاط پایانی

| نقطه پایانی | پشتیبانی | توضیحات |
|-------------|----------|---------|
| [`v1beta/`](fa/api-reference/v1beta.md) | پشتیبانی می‌شود | طرح‌واره بومی درخواست و پاسخ Gemini |
| [`v1/chat/completions`](fa/api-reference/chat.md) | پشتیبانی می‌شود | Chat Completions سازگار با OpenAI |
| [`v1/messages`](fa/api-reference/messages.md) | پشتیبانی می‌شود | Messages API سازگار با Anthropic |
| [`v1/responses`](fa/api-reference/responses.md) | پشتیبانی جزئی | پیش از استفاده در محیط عملیاتی، پارامترها و ابزارهای مورد نیاز را بررسی کنید |

### نام مستعار جدید

نام مستعار `gemini-flash-latest` اکنون به `gemini-3.8-flash` اشاره می‌کند. اگر به نسخه ثابت، ارزیابی تکرارپذیر یا عرضه کنترل‌شده در محیط عملیاتی نیاز دارید، شناسه صریح `gemini-3.8-flash` را به کار ببرید. تنها زمانی از نام مستعار استفاده کنید که برنامه شما برای پذیرش خودکار نسخه‌های آینده Flash آماده باشد.

---

## قیمت‌گذاری تشویقی

قیمت‌ها به دلار آمریکا و به‌ازای هر ۱ میلیون توکن هستند. قیمت‌گذاری آغازین تا **۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰)** اعتبار دارد.

| دوره | ورودی | ورودی ذخیره‌شده در حافظه نهان | خروجی |
|------|-------|-------------------------------|-------|
| تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) | $0.75 | $0.075 | $3.75 |
| پس از ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) | $1.50 | $0.15 | $7.50 |

نرخ‌های تشویقی نصف نرخ‌های استاندارد هستند. پیش از استقرار بارهای کاری بلندمدتی که ممکن است پس از پایان دوره تشویقی نیز ترافیک داشته باشند، [صفحه قیمت‌گذاری](fa/pricing.md) را بررسی کنید.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.8-flash",
    "messages": [
      {
        "role": "user",
        "content": "Review this distributed job processor, identify its three highest reliability risks, and propose an implementation plan with rollback criteria."
      }
    ]
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد. تعداد توکن‌ها و هزینه با توجه به درخواست و خروجی تولیدشده تغییر می‌کند.

```json
{
  "id": "chatcmpl-gemini38-example",
  "created": 1788422400,
  "model": "gemini-3.8-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "The highest risks are duplicate execution, unbounded retry storms, and loss of in-flight state during failover. Introduce idempotency keys and durable leases first, then add bounded exponential backoff with a dead-letter queue, and finally persist checkpoint state. Roll back each phase if duplicate-job rate, queue age, or recovery time exceeds its pre-deployment threshold.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 75,
    "prompt_tokens": 28,
    "total_tokens": 103
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
    "model": "gemini-3.8-flash",
    "messages": [
      {
        "role": "user",
        "content": "Plan a safe migration from scheduled workers to an event-driven processing pipeline."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {
            "role": "user",
            "content": "Plan a safe migration from scheduled workers to an event-driven processing pipeline.",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.8-flash",
  messages: [
    {
      role: "user",
      content: "Plan a safe migration from scheduled workers to an event-driven processing pipeline.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### نمونه API بومی Gemini

هنگامی که برنامه شما به فیلدهای درخواست یا ابزارهای اختصاصی Gemini نیاز دارد، از نقطه پایانی بومی Gemini استفاده کنید:

```bash
curl https://api.avalai.ir/v1beta/models/gemini-3.8-flash:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "Design a tool-using coding agent that diagnoses a failing deployment and prepares a human-reviewable remediation plan."
          }
        ]
      }
    ]
  }'
```

---

## راهنمای مهاجرت

- اگر در محیط عملیاتی به نسخه ثابت نیاز دارید، از شناسه دقیق `gemini-3.8-flash` استفاده کنید.
- نام مستعار `gemini-flash-latest` اکنون به `gemini-3.8-flash` اشاره می‌کند؛ این نام مستعار ممکن است با عرضه نسخه‌های جدیدتر Flash دوباره تغییر کند.
- برنامه‌های موجود Gemini Flash معمولاً می‌توانند ساختار نقطه پایانی و درخواست خود را حفظ کنند و تنها شناسه مدل را تغییر دهند.
- پیش از انتقال ترافیک عملیاتی، مدل را با بارهای کاری واقعی کدنویسی، استدلال و استفاده از ابزار ارزیابی کنید.
- هنگام افزایش تلاش استدلالی یا اجازه دادن به چرخه‌های طولانی ابزار، مصرف توکن و تأخیر را پایش کنید.
- پیش از استفاده از نقطه پایانی `v1/responses` با پشتیبانی جزئی، پشتیبانی همه پارامترها و ابزارهای مورد نیاز را بررسی کنید.
- در برآورد هزینه بلندمدت، نرخ‌های استاندارد پس از ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) را در نظر بگیرید.

---

## لینک‌های مرتبط

- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [قیمت‌گذاری](fa/pricing.md)
