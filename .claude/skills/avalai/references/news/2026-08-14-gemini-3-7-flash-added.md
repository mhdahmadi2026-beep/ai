# News 2026-08-14-gemini-3-7-flash-added: افزودن مدل پرچم‌دار جدید: Gemini 3.7 Flash
URL: `https://docs.avalai.ir/fa/news/2026-08-14-gemini-3-7-flash-added`
**تاریخ:** ۱۴۰۵-۰۵-۲۳ / (2026-08-14)

# افزودن مدل پرچم‌دار جدید: Gemini 3.7 Flash

**تاریخ:** ۱۴۰۵-۰۵-۲۳ / (2026-08-14)

## خلاصه

مدل پرچم‌دار جدید Flash گوگل، [`gemini-3.7-flash`](fa/providers/google.md)، اکنون برای کدنویسی، عامل‌ها، توسعه وب، تحلیل اسناد و کار دانشی پیچیده از طریق AvalAI در دسترس است. این مدل از API بومی Gemini یعنی [`v1beta/`](fa/api-reference/v1beta.md)، نقاط پایانی [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/messages`](fa/api-reference/messages.md) پشتیبانی می‌کند و برای [`v1/responses`](fa/api-reference/responses.md) پشتیبانی جزئی دارد.

---

## جزئیات

### Google Gemini 3.7 Flash

[`gemini-3.7-flash`](fa/providers/google.md) توانمندترین مدل همه‌کاره Flash گوگل برای کدنویسی و گردش‌کارهای عاملی است. این مدل بر پایه Gemini 3.6 Flash توسعه یافته و مهندسی نرم‌افزار، توسعه وب، درک اسناد پیچیده، خودکارسازی گردش‌کارهای تجاری، پیروی از دستورالعمل، برنامه‌ریزی چندمرحله‌ای و استفاده از ابزار را بهبود می‌دهد.

**ویژگی‌های کلیدی:**

- **زمینه طولانی**: ۱٬۰۴۸٬۵۷۶ توکن ورودی و حداکثر ۶۵٬۵۳۶ توکن خروجی
- **ورودی چندوجهی**: ورودی متن، تصویر، ویدیو، صدا و PDF با خروجی متن
- **کدنویسی و عامل‌ها**: بهبود اشکال‌زدایی، رفع مسئله، مهندسی نرم‌افزار بلندمدت، برنامه‌ریزی و فراخوانی ابزار
- **توسعه وب**: دقت بهتر کد در اولین تلاش، پایبندی بیشتر به طراحی و تولید برنامه‌های کامل‌تر
- **کار دانشی**: استدلال قوی‌تر روی اسناد پیچیده در حوزه‌هایی مانند مالی، حقوق و علوم زیستی
- **خودکارسازی گردش‌کار**: تکمیل بهتر گردش‌کارهای تجاری چندمهارتی با نظارت دستی و تلاش مجدد کمتر
- **قابلیت‌های توسعه‌دهنده**: تفکر، فراخوانی تابع، خروجی ساختاریافته، اجرای کد، کش پرامپت، جستجوی فایل، پایه‌گذاری با Google Search و زمینه URL
- **مناسب برای**: کدنویسی عاملی، توسعه برنامه production، هوشمندی اسناد، خودکارسازی گردش‌کار و وظایف پیچیده چندوجهی

### نکات برجسته بنچمارک به گزارش گوگل

گوگل نتایج زیر را در مقایسه با Gemini 3.6 Flash گزارش کرده است:

| ارزیابی | Gemini 3.7 Flash | Gemini 3.6 Flash |
|---------|------------------|------------------|
| FrontierCode 1.1 Main | 43.6% | 34.4% |
| DeepSWE v1.1 | 65.3% | 49.0% |
| WebDev Arena | 1588 Elo | 1538 Elo |
| GDP.pdf | 34.0% | 22.0% |
| AutomationBench | 30.4% | 17.0% |

نتایج بنچمارک شواهد جهت‌دهنده مفیدی هستند، اما ارزیابی production باید با پرامپت‌ها، ابزارها و معیارهای پذیرش متناسب با بار کاری خودتان انجام شود.

### دسترسی نقاط پایانی

| نقطه پایانی | پشتیبانی | توضیحات |
|-------------|----------|---------|
| [`v1beta/`](fa/api-reference/v1beta.md) | پشتیبانی می‌شود | اسکیمای درخواست و پاسخ بومی Gemini |
| [`v1/chat/completions`](fa/api-reference/chat.md) | پشتیبانی می‌شود | Chat Completions سازگار با OpenAI |
| [`v1/messages`](fa/api-reference/messages.md) | پشتیبانی می‌شود | Messages API سازگار با Anthropic |
| [`v1/responses`](fa/api-reference/responses.md) | پشتیبانی جزئی | پارامترها و ابزارهای موردنیاز را پیش از استفاده در production بررسی کنید |

---

## قیمت‌گذاری تشویقی

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند. قیمت‌گذاری تشویقی گوگل تا **۳۱ دسامبر ۲۰۲۶** اعمال می‌شود.

| دوره | ورودی | ورودی کش‌شده | خروجی |
|------|-------|----------------|--------|
| تا ۳۱ دسامبر ۲۰۲۶ | $0.75 | $0.075 | $3.75 |
| پس از ۳۱ دسامبر ۲۰۲۶ | $1.50 | $0.15 | $7.50 |

نرخ‌های تشویقی نصف نرخ‌های استاندارد هستند. پیش از استقرار بارهای کاری بلندمدتی که ترافیک آن‌ها ممکن است بعد از دوره تشویقی ادامه یابد، [صفحه قیمت‌گذاری](fa/pricing.md) را بررسی کنید.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.7-flash",
    "messages": [
      {
        "role": "user",
        "content": "طراحی این سرویس را بررسی کن و یک مهاجرت مرحله‌ای به معماری رویدادمحور پیشنهاد بده. ریسک‌ها و معیارهای rollback را نیز بنویس."
      }
    ]
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد. تعداد توکن‌ها و هزینه با توجه به درخواست و خروجی تولیدشده تغییر می‌کند.

```json
{
  "id": "chatcmpl-gemini37-example",
  "created": 1786651200,
  "model": "gemini-3.7-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "ابتدا دامنه‌ها و وابستگی‌ها را مشخص کنید، سپس رویدادهای نسخه‌بندی‌شده و transactional outbox را پشت قراردادهای فعلی سرویس قرار دهید. هر بار یک دامنه کم‌ریسک را مهاجرت کنید، سازگاری dual-write را بسنجید و تا پایدار شدن lag مصرف‌کننده و نرخ خطا، مسیر rollback برای تغییر ترافیک را حفظ کنید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 160,
    "prompt_tokens": 24,
    "total_tokens": 184,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 24,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0006180000",
    "irt": 70.82,
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
    "model": "gemini-3.7-flash",
    "messages": [
      {
        "role": "user",
        "content": "ریسک‌های پایداری این برنامه استقرار را پیدا کن و یک checklist اولویت‌بندی‌شده برای کاهش ریسک برگردان."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini-3.7-flash",
    messages=[
        {
            "role": "user",
            "content": "ریسک‌های پایداری این برنامه استقرار را پیدا کن و یک checklist اولویت‌بندی‌شده برای کاهش ریسک برگردان.",
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
  model: "gemini-3.7-flash",
  messages: [
    {
      role: "user",
      content: "ریسک‌های پایداری این برنامه استقرار را پیدا کن و یک checklist اولویت‌بندی‌شده برای کاهش ریسک برگردان.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### نمونه API بومی Gemini

زمانی از نقطه پایانی بومی Gemini استفاده کنید که برنامه به فیلدهای درخواست یا ابزارهای اختصاصی Gemini نیاز دارد:

```bash
curl https://api.avalai.ir/v1beta/models/gemini-3.7-flash:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "عاملی ابزارمحور طراحی کن که رخدادها را triage کند و یک برنامه اصلاحی قابل بازبینی توسط انسان آماده کند."
          }
        ]
      }
    ]
  }'
```

---

## راهنمای مهاجرت

- برای استفاده از مدل جدید، شناسه دقیق `gemini-3.7-flash` را به کار ببرید.
- پیش از تغییر ترافیک production، مدل را با بارهای کاری واقعی کدنویسی، استفاده از ابزار و اسناد ارزیابی کنید.
- برنامه‌های فعلی Gemini 3.6 Flash معمولا می‌توانند ساختار نقطه پایانی و درخواست خود را حفظ کنند و فقط شناسه مدل را تغییر دهند.
- پیش از استفاده از نقطه پایانی `v1/responses` با پشتیبانی جزئی، پشتیبانی از تمام پارامترها و ابزارهای موردنیاز را تأیید کنید.
- هنگام پیش‌بینی هزینه بلندمدت، نرخ‌های استاندارد پس از ۳۱ دسامبر ۲۰۲۶ را در نظر بگیرید.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [مرجع مدل Gemini 3.7 Flash](fa/models/gemini-3.7-flash.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [قیمت‌گذاری](fa/pricing.md)
