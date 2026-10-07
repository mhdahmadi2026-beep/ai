# مدل‌های جدید اضافه شدند: Gemini 3.6 Flash و Gemini 3.5 Flash-Lite

**تاریخ:** 1405-04-30 / (2026-07-21)

## خلاصه

اضافه شدن مدل‌های [`gemini-3.6-flash`](fa/providers/google.md) و [`gemini-3.5-flash-lite`](fa/providers/google.md) گوگل را اعلام می‌کنیم. هر دو مدل استدلالی و بومی چندوجهی با پنجره ورودی ۱٬۰۴۸٬۵۷۶ توکنی هستند و از طریق API بومی Gemini یعنی [`v1beta/`](fa/api-reference/v1beta.md)، نقطه پایانی [`v1/chat/completions`](fa/api-reference/chat.md)، نقطه پایانی [`v1/messages`](fa/api-reference/messages.md) و به‌صورت جزئی از طریق [`v1/responses`](fa/api-reference/responses.md) در دسترس‌اند.

---

## جزئیات

### Google Gemini

#### Gemini 3.6 Flash

[`gemini-3.6-flash`](fa/providers/google.md) مدل همه‌کاره گوگل برای هوشمندی پایدار و باکیفیت، همراه با سرعت و هزینه سطح Flash است. این مدل ضمن مصرف توکن خروجی و فراخوانی ابزار کمتر نسبت به Gemini 3.5 Flash در گردش‌کارهای ارزیابی‌شده، کدنویسی، کار دانشی، تحلیل چندوجهی، اجرای عاملی و استدلال فضایی را بهبود می‌دهد.

**ویژگی‌های کلیدی:**

- **زمینه طولانی**: ۱٬۰۴۸٬۵۷۶ توکن ورودی و حداکثر ۶۵٬۵۳۶ توکن خروجی
- **ورودی چندوجهی**: ورودی متن، تصویر، ویدیو، صدا و PDF با خروجی متن
- **اجرای عاملی**: عملکرد قوی در چرخه‌های کدنویسی، استفاده از ابزار، گردش‌کارهای چندمرحله‌ای و استفاده از کامپیوتر
- **کارایی توکن**: مصرف ۱۷٪ توکن خروجی کمتر از Gemini 3.5 Flash در Artificial Analysis Index
- **قابلیت‌های توسعه‌دهنده**: تفکر، فراخوانی تابع، خروجی ساختاریافته، اجرای کد، کش پرامپت، جستجوی فایل، پایه‌گذاری با Google Search، پایه‌گذاری با Google Maps و زمینه URL
- **استفاده از کامپیوتر**: پشتیبانی در حالت پیش‌نمایش از طریق رابط ابزار بومی Gemini
- **مناسب برای**: کدنویسی عاملی، مهاجرت کد، تحلیل سند و نمودار، کار دانشی و گردش‌کارهای پیچیده چندوجهی

#### Gemini 3.5 Flash-Lite

[`gemini-3.5-flash-lite`](fa/providers/google.md) سریع‌ترین و مقرون‌به‌صرفه‌ترین مدل کلاس Gemini 3.5 گوگل است. این مدل برای گردش‌کارهای عاملی پرترافیک، وظایف کم‌تأخیر زیرعامل‌ها، پردازش اسناد، استخراج ساده داده، دسته‌بندی، ترجمه و سایر بارهای کاری production که سرعت و هزینه مهم‌ترین محدودیت‌ها هستند، بهینه شده است.

**ویژگی‌های کلیدی:**

- **زمینه طولانی**: ۱٬۰۴۸٬۵۷۶ توکن ورودی و حداکثر ۶۵٬۵۳۶ توکن خروجی
- **ورودی چندوجهی**: ورودی متن، تصویر، ویدیو، صدا و PDF با خروجی متن
- **توان عملیاتی بالا**: سرعت اندازه‌گیری‌شده ۳۵۰ توکن خروجی در ثانیه توسط Artificial Analysis
- **کارایی عاملی**: طراحی‌شده برای بارهای کاری پرترافیک زیرعامل‌ها و اجرای چندمرحله‌ای
- **قابلیت‌های توسعه‌دهنده**: تفکر، فراخوانی تابع، خروجی ساختاریافته، اجرای کد، کش پرامپت، جستجوی فایل، پایه‌گذاری با Google Search، پایه‌گذاری با Google Maps و زمینه URL
- **مناسب برای**: پردازش سند، استخراج داده، مسیریابی، دسته‌بندی، زیرعامل‌های جستجو، ترجمه و ترافیک production حساس به هزینه

### دسترسی نقاط پایانی

| نقطه پایانی | Gemini 3.6 Flash | Gemini 3.5 Flash-Lite | توضیحات |
|-------------|------------------|-----------------------|---------|
| [`v1beta/`](fa/api-reference/v1beta.md) | پشتیبانی می‌شود | پشتیبانی می‌شود | اسکیمای درخواست و پاسخ بومی Gemini |
| [`v1/chat/completions`](fa/api-reference/chat.md) | پشتیبانی می‌شود | پشتیبانی می‌شود | Chat Completions سازگار با OpenAI |
| [`v1/messages`](fa/api-reference/messages.md) | پشتیبانی می‌شود | پشتیبانی می‌شود | Messages API سازگار با Anthropic |
| [`v1/responses`](fa/api-reference/responses.md) | پشتیبانی جزئی | پشتیبانی جزئی | پارامترها و ابزارهای موردنیاز را پیش از استفاده در production بررسی کنید |

---

## قیمت‌گذاری

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند.

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-----|-------|----------------|--------|
| `gemini-3.6-flash` | $1.50 | $0.15 | $7.50 |
| `gemini-3.5-flash-lite` | $0.30 | $0.03 | $2.50 |

Gemini 3.6 Flash برای بارهای کاری مناسب است که کیفیت بالاتر کدنویسی، اجرای عاملی و کار دانشی را در اولویت قرار می‌دهند. Gemini 3.5 Flash-Lite گزینه کم‌هزینه‌تر برای پردازش حساس به تأخیر و پرترافیک است.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "معماری این سرویس را بررسی کن و یک برنامه مهاجرت قابل اتکا به میکروسرویس‌های رویدادمحور پیشنهاد بده."
      }
    ]
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد:

```json
{
  "id": "chatcmpl-gemini36-example",
  "created": 1784650800,
  "model": "gemini-3.6-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "ابتدا bounded contextها را مشخص کنید، یک transactional outbox اضافه کنید و هر بار یک دامنه کم‌ریسک را پشت قراردادهای پایدار مهاجرت دهید. پیش از انتقال ترافیک production، نسخه‌بندی schema، مصرف‌کننده‌های idempotent، ردیابی توزیع‌شده و معیارهای rollback را تعریف کنید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 147,
    "prompt_tokens": 22,
    "total_tokens": 169,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 22,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0011355000",
    "irt": 130.13,
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
    "model": "gemini-3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "ریسک‌ها، پیش‌نیاز‌ها و اقدامات بعدی را از این گزارش پروژه استخراج کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini-3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "ریسک‌ها، پیش‌نیاز‌ها و اقدامات بعدی را از این گزارش پروژه استخراج کن.",
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
  model: "gemini-3.6-flash",
  messages: [
    {
      role: "user",
      content: "ریسک‌ها، پیش‌نیاز‌ها و اقدامات بعدی را از این گزارش پروژه استخراج کن.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### نمونه API بومی Gemini

زمانی از نقطه پایانی بومی Gemini استفاده کنید که برنامه به فیلدهای درخواست یا ابزارهای اختصاصی Gemini نیاز دارد:

```bash
curl https://api.avalai.ir/v1beta/models/gemini-3.5-flash-lite:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "این درخواست پشتیبانی را در یکی از دسته‌های billing، account، technical یا other قرار بده: لینک بازنشانی رمز عبور من منقضی شده است."
          }
        ]
      }
    ]
  }'
```

---

## انتخاب بین مدل‌ها

| بار کاری | مدل پیشنهادی | دلیل |
|----------|--------------|------|
| کدنویسی عاملی و مهاجرت کد | `gemini-3.6-flash` | کیفیت کدنویسی بالاتر، چرخه‌های اجرای کمتر و استفاده کارآمد از ابزار |
| کار دانشی و تهیه گزارش | `gemini-3.6-flash` | تحلیل بهبودیافته سند، نمودار و داده |
| گردش‌کارهای پیچیده چندوجهی | `gemini-3.6-flash` | استدلال چندوجهی و فضایی قوی‌تر |
| استخراج و دسته‌بندی پرترافیک | `gemini-3.5-flash-lite` | هزینه توکن کمتر و توان عملیاتی بالا |
| زیرعامل‌های جستجو و مسیریابی | `gemini-3.5-flash-lite` | تأخیر کم همراه با قابلیت استدلال قابل تنظیم |
| پردازش اسناد در مقیاس بزرگ | `gemini-3.5-flash-lite` | زمینه ۱M توکنی با قیمت ورودی و خروجی کمتر |

---

## لینک‌های مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [قیمت‌گذاری](fa/pricing.md)
