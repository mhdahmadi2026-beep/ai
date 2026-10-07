# مدل‌های جدید هوش مصنوعی اضافه شد: GPT-5 Codex، Gemini Flash Latest و Qwen3-Max

**تاریخ:** 1404-07-06 / (2025-09-28)

## خلاصه

شش مدل جدید هوش مصنوعی از OpenAI، Google و Alibaba را اعلام می‌کنیم که شامل GPT-5 Codex پیشرفته برای وظایف کدنویسی، Gemini Flash Latest با قابلیت‌های استدلال ترکیبی و Qwen3-Max با ویژگی‌های بهبود یافته برنامه‌نویسی عامل می‌باشد. این مدل‌ها قابلیت‌های پلتفرم ما را در زمینه کدنویسی، استدلال و راه‌حل‌های هوش مصنوعی مقرون به صرفه گسترش می‌دهند.

---

## جزئیات

### OpenAI

* **[`gpt-5-codex`](fa/providers/openai.md)**: مدل پیشرفته کدنویسی بهینه شده برای وظایف کدنویسی عاملی با قابلیت‌های استدلال و پنجره متنی 400K. در Responses API با به‌روزرسانی‌های منظم نسخه مدل در دسترس است.

**ویژگی‌های کلیدی:**
- **پنجره متنی**: 400,000 توکن برای تجزیه و تحلیل و تولید کد گسترده
- **قابلیت‌های پیشرفته**: پشتیبانی از توکن‌های استدلال، فراخوانی تابع، خروجی‌های ساختاریافته
- **تمرکز تخصصی**: بهینه شده برای وظایف کدنویسی عاملی در محیط‌های Codex
- **پشتیبانی نقطه پایانی**: در دسترس در v1/chat/completions، v1/responses، v1/assistants، v1/batch

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5-codex | $1.25/1M توکن | $0.125/1M توکن | $10.00/1M توکن |

### Google

* **[`gemini-flash-latest`](fa/providers/google.md)**: به gemini-2.5-flash-preview-09-2025 اشاره می‌کند، مدل استدلال ترکیبی ما با پنجره متنی 1M توکن و بودجه‌های تفکر.
* **[`gemini-2.5-flash-preview-09-2025`](fa/providers/google.md)**: آخرین پیش‌نمایش Gemini 2.5 Flash با قابلیت‌های استدلال بهبود یافته و مدیریت متن گسترده.
* **[`gemini-flash-lite-latest`](fa/providers/google.md)**: به gemini-2.5-flash-lite-preview-09-2025 اشاره می‌کند، مقرون‌به‌صرفه‌ترین مدل ساخته شده برای استفاده در مقیاس.
* **[`gemini-2.5-flash-lite-preview-09-2025`](fa/providers/google.md)**: کوچک‌ترین و مقرون‌به‌صرفه‌ترین مدل در سری Gemini 2.5 با قیمت‌گذاری بهینه شده.

**ویژگی‌های کلیدی:**
- **پنجره متنی**: تا 1M توکن برای پردازش اسناد گسترده
- **قابلیت‌های پیشرفته**: استدلال ترکیبی، بودجه‌های تفکر، فراخوانی تابع
- **دو سطح قیمت‌گذاری**: نسخه‌های استاندارد Flash و مقرون‌به‌صرفه Flash-Lite
- **نام‌های مستعار جدید**: Flash-latest و Flash-lite-latest به جدیدترین نسخه‌های پیش‌نمایش اشاره می‌کنند

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| gemini-flash-latest | $0.30/1M توکن | $0.15/1M توکن | $2.50/1M توکن |
| gemini-2.5-flash-preview-09-2025 | $0.30/1M توکن | $0.15/1M توکن | $2.50/1M توکن |
| gemini-flash-lite-latest | $0.10/1M توکن | $0.05/1M توکن | $0.40/1M توکن |
| gemini-2.5-flash-lite-preview-09-2025 | $0.10/1M توکن | $0.05/1M توکن | $0.40/1M توکن |

### Alibaba

* **[`qwen3-max`](fa/providers/alibaba.md)**: آخرین مدل سری Qwen 3 Max با ارتقاهای تخصصی در برنامه‌نویسی عامل و فراخوانی ابزار، که عملکرد پیشرفته‌ای برای سناریوهای پیچیده عامل ارائه می‌دهد.

**ویژگی‌های کلیدی:**
- **پنجره متنی**: مدیریت متن پیشرفته با قیمت‌گذاری طبقه‌بندی شده بالای 32K و 128K توکن
- **قابلیت‌های پیشرفته**: برنامه‌نویسی عامل بهبود یافته، فراخوانی ابزار، استدلال پیچیده
- **تمرکز تخصصی**: بهینه شده برای عامل‌های عاملی در سناریوهای پیچیده
- **عملکرد**: عملکرد پیشرفته (SOTA) در وظایف برنامه‌نویسی عامل

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| qwen3-max | $1.20/1M توکن | $0.10/1M توکن | $6.00/1M توکن | بالای 32K: ورودی $2.40/1M، خروجی $12.00/1M |
| qwen3-max | - | - | - | بالای 128K: ورودی $3.00/1M، خروجی $15.00/1M |

### نمونه‌های استفاده

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-codex",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی با عملیات درج، جستجو و حذف بنویس."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5-codex",
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی با عملیات درج، جستجو و حذف بنویس.",
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
  model: "gpt-5-codex",
  messages: [
    {
      role: "user",
      content: "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی با عملیات درج، جستجو و حذف بنویس.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### ویژگی‌های پیشرفته

#### قابلیت‌های استدلال
مدل‌های GPT-5 Codex و Gemini Flash از استدلال پیشرفته با فرآیندهای تفکر قابل مشاهده در پاسخ‌ها پشتیبانی می‌کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-flash-latest",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن"
      }
    ],
    "max_tokens": 2048
  }'

python=:response = client.chat.completions.create(
    model="gemini-flash-latest",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن",
        }
    ],
    max_tokens=2048,
)

# مدل فرآیند تفکر خود را قبل از ارائه پاسخ نهایی نشان خواهد داد
print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
    model: "gemini-flash-latest",
    messages: [
        {
            role: "user",
            content: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن",
        },
    ],
    max_tokens: 2048,
});

// مدل فرآیند تفکر خود را قبل از ارائه پاسخ نهایی نشان خواهد داد
console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

* [مستندات مدل‌های OpenAI](fa/providers/openai.md)
* [مستندات مدل‌های Google](fa/providers/google.md)
* [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
* [مرجع API تکمیل چت](fa/api-reference/chat.md)
* [راهنمای فراخوانی تابع](fa/guides/function-calling.md)