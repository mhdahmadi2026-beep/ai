---
hasH1: true
---

# افزودن مدل پرچم‌دار جدید: GLM-5.3-Flash

**تاریخ:** ۱۴۰۵-۰۶-۰۴ / (2026-08-26)

## خلاصه

مدل پرچم‌دار کارآمد جدید Z.AI با شناسه [`glm-5.3-flash`](fa/providers/zai.md#glm-53-flash) اکنون برای کدنویسی، گردش‌کارهای عاملی، استدلال و کارهای چندوجهی از طریق AvalAI در دسترس است. این مدل از [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/messages`](fa/api-reference/messages.md) پشتیبانی می‌کند، برای [`v1/responses`](fa/api-reference/responses.md) پشتیبانی جزئی دارد و تا ۹ سپتامبر ۲۰۲۶ با قیمت تشویقی ارائه می‌شود.

---

## جزئیات

### Z.AI GLM-5.3-Flash

مدل [`glm-5.3-flash`](fa/providers/zai.md#glm-53-flash) نخستین مدل چندوجهی بومی در سری GLM-5 است. معماری ترکیب متخصصان آن ۳۲۰ میلیارد پارامتر کل دارد و برای هر توکن ۱۸ میلیارد پارامتر را فعال می‌کند. ترکیب توجه پراکنده و خطی، هزینه سرویس‌دهی زمینه طولانی را کاهش می‌دهد و در عین حال بازیابی دقیق را در پنجره ورودی ثبت‌شده ۹۹۱٬۰۰۰ توکنی حفظ می‌کند.

**ویژگی‌های کلیدی:**

- **معماری کارآمد**: ۳۲۰B پارامتر کل، ۱۸B پارامتر فعال، ۴۵ لایه و طراحی ترکیبی توجه پراکنده و خطی
- **زمینه طولانی**: حداکثر ۹۹۱٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی در AvalAI
- **چندوجهی بومی**: آموزش اولیه روی پیکره چندوجهی ۳۰ تریلیون توکنی برای استدلال هم‌زمان روی متن، تصویر و ساختار
- **کدنویسی و عامل‌ها**: مناسب کار در سطح مخزن، وظایف ترمینال، استفاده از ابزار، کدنویسی بصری و راستی‌آزمایی تکرارشونده
- **قابلیت‌های توسعه‌دهنده**: استدلال، فراخوانی تابع، انتخاب ابزار، کش پرامپت و پاسخ جریانی
- **وزن‌های باز**: Z.AI وزن‌های مدل را برای استقرار محلی با چارچوب‌هایی مانند SGLang، vLLM و TokenSpeed منتشر کرده است
- **مناسب برای**: عامل‌های کدنویسی کم‌هزینه، تحلیل زمینه طولانی، اسناد تجاری، اعتبارسنجی رابط و کار دانشی چندوجهی

### نکات برجسته بنچمارک به گزارش Z.AI

| ارزیابی | GLM-5.3-Flash | GLM-5.2 |
|---------|---------------|---------|
| Terminal-Bench 2.1 | 84.3 | 81.0 |
| DeepSWE v1.1 | 63.4 | 46.2 |
| Toolathlon Verified | 78.4 | 59.9 |
| AutomationBench v1.0.6 | 48.8 | 26.2 |
| Agents' Last Exam | 26.3 | 20.4 |
| GDPval-AA v2 | 1773 | 1504 |

این نتایج که Z.AI گزارش کرده است، شواهدی جهت‌دهنده هستند. پیش از هدایت ترافیک محیط تولید، مدل را با پرامپت‌ها، ابزارها، رسانه‌ها و معیارهای پذیرش متناسب با کاربرد خود ارزیابی کنید.

### دسترسی نقاط پایانی

| نقطه پایانی | پشتیبانی | توضیحات |
|-------------|----------|---------|
| [`v1/chat/completions`](fa/api-reference/chat.md) | پشتیبانی می‌شود | Chat Completions سازگار با OpenAI |
| [`v1/messages`](fa/api-reference/messages.md) | پشتیبانی می‌شود | Messages API سازگار با Anthropic |
| [`v1/responses`](fa/api-reference/responses.md) | پشتیبانی جزئی | پارامترها، ابزارها و نوع‌های ورودی موردنیاز را پیش از استفاده در محیط تولید بررسی کنید |

---

## قیمت‌گذاری تشویقی

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند. قیمت‌گذاری تشویقی تا **۹ سپتامبر ۲۰۲۶** اعمال می‌شود.

| دوره | ورودی | ورودی کش‌شده | خروجی |
|------|-------|----------------|--------|
| تا September 9, 2026 (۱۸ شهریور ۱۴۰۵) | $0.075 | $0.015 | $0.25 |
| پس از September 9, 2026 (۱۸ شهریور ۱۴۰۵) | $0.15 | $0.03 | $0.50 |

نرخ‌های تشویقی نصف نرخ‌های استاندارد هستند. هنگام برآورد هزینه بارهای کاری که ممکن است پس از پایان دوره تشویقی ادامه یابند، [صفحه قیمت‌گذاری](fa/pricing.md) را بررسی کنید.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.3-flash",
    "messages": [
      {
        "role": "user",
        "content": "این برنامه استقرار را بررسی کن، سه ریسک عملیاتی اصلی را مشخص کن و مراحل راستی‌آزمایی پیشنهاد بده."
      }
    ]
  }'
```

### پاسخ

نمونه کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد. تعداد توکن‌ها و هزینه با توجه به درخواست و خروجی تولیدشده تغییر می‌کند.

```json
{
  "id": "chatcmpl-glm53flash-example",
  "created": 1787774400,
  "model": "glm-5.3-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "سه ریسک اصلی عبارت‌اند از مسیر بازگشت آزمایش‌نشده، نبود کنترل سلامت وابستگی‌ها و مشاهده‌پذیری ناکافی. یک canary مرحله‌ای اجرا کنید، پیش از گسترش بازگشت را تمرین کنید و در هر مرحله آستانه‌های تأخیر، نرخ خطا و اشباع را الزامی کنید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 73,
    "prompt_tokens": 25,
    "total_tokens": 98,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 25,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000201250",
    "irt": 2.31,
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
    "model": "glm-5.3-flash",
    "messages": [
      {
        "role": "user",
        "content": "برای بازآرایی ایمن و مرحله‌ای این سرویس برنامه‌ریزی کن و آزمایش‌ها و معیارهای بازگشت را نیز بنویس."
      }
    ]
  }'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="glm-5.3-flash",
    messages=[
        {
            "role": "user",
            "content": "برای بازآرایی ایمن و مرحله‌ای این سرویس برنامه‌ریزی کن و آزمایش‌ها و معیارهای بازگشت را نیز بنویس.",
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
  model: "glm-5.3-flash",
  messages: [
    {
      role: "user",
      content: "برای بازآرایی ایمن و مرحله‌ای این سرویس برنامه‌ریزی کن و آزمایش‌ها و معیارهای بازگشت را نیز بنویس.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## راهنمای استفاده

- از شناسه دقیق `glm-5.3-flash` استفاده کنید.
- پیش از تغییر ترافیک محیط تولید، رفتار مدل در کدنویسی، استفاده از ابزار، زمینه طولانی و ورودی چندوجهی را با بارهای کاری واقعی ارزیابی کنید.
- پیش از استفاده از نقطه پایانی `v1/responses` با پشتیبانی جزئی، پشتیبانی همه پارامترها، ابزارها و نوع‌های ورودی موردنیاز را تأیید کنید.
- برای پیشوندهای طولانی و تکراری از کش پرامپت استفاده کنید و تعداد توکن‌های کش‌شده را در فیلدهای مصرف پاسخ بررسی کنید.
- هنگام برآورد هزینه بلندمدت، نرخ‌های استاندارد پس از ۹ سپتامبر ۲۰۲۶ را در نظر بگیرید.

---

## پیوندهای مرتبط

- [مستندات مدل‌های Z.AI](fa/providers/zai.md)
- [مرجع مدل GLM-5.3-Flash](fa/models/glm-5.3-flash.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [قیمت‌گذاری](fa/pricing.md)
