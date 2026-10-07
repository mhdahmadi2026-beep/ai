# مدل جدید اضافه شد: Gemini 3 Flash Preview

**تاریخ:** ۱۴۰۴-۰۹-۲۶ / (2025-12-17)

## خلاصه

AvalAI مدل Gemini 3 Flash Preview (`gemini-3-flash-preview`) از گوگل را معرفی می‌کند، جدیدترین مدل کارآمد که هوش مرزی را با قابلیت‌های برتر جستجو و پایه‌گذاری ترکیب می‌کند. این مدل عملکرد استدلال سطح حرفه‌ای را با کسری از هزینه ارائه می‌دهد و برای استفاده روزمره با پنجره متن ۱ میلیون توکن ایده‌آل است.

---

## جزئیات

### گوگل - Gemini 3 Flash Preview

Gemini 3 Flash Preview (`gemini-3-flash-preview`) هوشمندترین مدل گوگل است که برای سرعت ساخته شده و هوش مرزی را با جستجو و پایه‌گذاری برتر ترکیب می‌کند. این مدل که در دسامبر ۲۰۲۵ منتشر شده، بهبودهای قابل توجهی نسبت به Gemini 2.5 Flash ارائه می‌دهد و در معیارهای کلیدی با سایر مدل‌های مرزی هم‌سطح است. [مستندات](fa/providers/google.md)

**قابلیت‌های کلیدی:**

- **پنجره متن ۱ میلیون توکن**: مدیریت مکالمات گسترده، اسناد و مخازن کد
- **ورودی چندوجهی**: پردازش متن، تصاویر، ویدیو، صوت و فایل‌های PDF
- **تفکر/استدلال**: قابلیت‌های استدلال داخلی برای حل مسائل پیچیده
- **فراخوانی تابع**: پشتیبانی کامل از استفاده از ابزار و گردش‌های کاری عاملی
- **خروجی‌های ساختاریافته**: تولید پاسخ‌های JSON ساختاریافته
- **پایه‌گذاری جستجو**: جستجو و پایه‌گذاری برتر با دانش دنیای واقعی
- **اجرای کد**: اجرای کد مستقیم در مدل
- **متن URL**: پردازش و درک محتوای صفحات وب
- **کش کردن متن**: کش کردن کارآمد توکن برای متن‌های تکراری

| ویژگی | جزئیات |
|-------|--------|
| کد مدل | `gemini-3-flash-preview` |
| پنجره متن | تا ۱,۰۴۸,۵۷۶ توکن (۱M) |
| حداکثر توکن خروجی | ۶۵,۵۳۶ توکن |
| ورودی‌ها | متن، تصویر، ویدیو، صوت، PDF |
| خروجی | متن |
| برش دانش | ژانویه ۲۰۲۵ |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/completions` |
| نقاط قوت | سرعت، کارایی، استدلال سطح حرفه‌ای، پایه‌گذاری جستجو |
| بهترین کاربرد | وظایف روزمره، تحلیل ویدیو، استخراج داده، پرسش و پاسخ بصری، گردش‌های کاری سریع |

**قیمت‌گذاری:**

| نوع توکن | قیمت به ازای ۱ میلیون توکن |
|----------|---------------------------|
| ورودی | $0.50 |
| ورودی کش شده | $0.25 |
| خروجی | $3.00 |
| ورودی صوتی | $1.50 |
| ورودی صوتی کش شده | $0.50 |
| خروجی صوتی | $1.50 |

**عملکرد در معیارها:**

- **آزمون آخر بشریت**: ۳۳.۷٪ (بدون استفاده از ابزار) - هم‌سطح با GPT-5.2 (۳۴.۵٪)
- **MMMU-Pro**: ۸۱.۲٪ - از همه رقبا از جمله GPT-5.2 (۷۹.۵٪) پیشی گرفته
- بهبود قابل توجه نسبت به Gemini 2.5 Flash در همه معیارهای اصلی
- ۳ برابر سریع‌تر از Gemini 2.5 Pro با عملکرد هم‌سطح
- به طور متوسط ۳۰٪ کمتر توکن برای وظایف تفکر نسبت به 2.5 Pro استفاده می‌کند

**قابلیت‌های پشتیبانی شده:**

| قابلیت | وضعیت |
|--------|-------|
| Batch API | ✓ پشتیبانی می‌شود |
| کش کردن | ✓ پشتیبانی می‌شود |
| اجرای کد | ✓ پشتیبانی می‌شود |
| جستجوی فایل | ✓ پشتیبانی می‌شود |
| فراخوانی تابع | ✓ پشتیبانی می‌شود |
| پایه‌گذاری جستجو | ✓ پشتیبانی می‌شود |
| خروجی‌های ساختاریافته | ✓ پشتیبانی می‌شود |
| تفکر | ✓ پشتیبانی می‌شود |
| متن URL | ✓ پشتیبانی می‌شود |
| تولید صوت | ✗ پشتیبانی نمی‌شود |
| تولید تصویر | ✗ پشتیبانی نمی‌شود |
| Live API | ✗ پشتیبانی نمی‌شود |
| پایه‌گذاری با Google Maps | ✗ پشتیبانی نمی‌شود |

---

## مثال‌های درخواست/پاسخ API

### تکمیل چت پایه

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده"
      }
    ]
  }'
```

**پاسخ نمونه:**

```json
{
  "id": "chatcmpl-gemini3flash-abc123",
  "created": 1765933200,
  "model": "gemini-3-flash-preview",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "محاسبات کوانتومی نوع جدیدی از محاسبات است که از اصول مکانیک کوانتومی برای پردازش اطلاعات استفاده می‌کند...",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 245,
    "prompt_tokens": 12,
    "total_tokens": 257
  },
  "estimated_cost": {
    "unit": "0.0007410000",
    "irt": 97.39,
    "exchange_rate": 131400
  }
}
```

### با تفکر/استدلال

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله را قدم به قدم حل کن: اگر یک قطار ۱۲۰ کیلومتر را در ۲ ساعت طی کند، سپس ۳۰ دقیقه توقف کند، سپس ۹۰ کیلومتر دیگر را در ۱.۵ ساعت طی کند، میانگین سرعت برای کل سفر چقدر است؟"
      }
    ],
    "max_tokens": 2048
  }'
```

### ورودی چندوجهی (تحلیل تصویر)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "این تصویر را تحلیل کن و آنچه می‌بینی را با جزئیات توصیف کن"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/image.jpg"
            }
          }
        ]
      }
    ]
  }'
```

### فراخوانی تابع

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوا در توکیو چگونه است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "واحد دما"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'
```

---

## مثال‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای محاسبه دنباله فیبوناچی بنویس"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای محاسبه دنباله فیبوناچی بنویس",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3-flash-preview",
  messages: [
    {
      role: "user",
      content: "یک تابع پایتون برای محاسبه دنباله فیبوناچی بنویس",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### با ورودی چندوجهی

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-flash-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "در این تصویر چیست؟"},
          {"type": "image_url", "image_url": {"url": "https://example.com/image.jpg"}}
        ]
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چیست؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3-flash-preview",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "در این تصویر چیست؟" },
        { type: "image_url", image_url: { url: "https://example.com/image.jpg" } },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [راهنمای تولید متن](fa/guides/text-generation.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای بینایی](fa/guides/vision.md)
- [قیمت‌گذاری](fa/pricing.md)