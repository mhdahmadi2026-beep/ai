# افزودن مدل جدید: Claude 4.5 Sonnet

**تاریخ:** 1404-07-07 / (2025-09-29)

## خلاصه

افزودن Claude 4.5 Sonnet (`claude-sonnet-4-5`) را اعلام می‌کنیم، پیشرفته‌ترین مدل Anthropic برای ساخت عامل‌های پیچیده که قادر به کار مستقل برای مدت‌های طولانی هستند. این مدل مرزهای قابلیت‌های کدنویسی را پیش می‌برد، عملکرد پیشرفته‌ای در استفاده از رایانه دارد و در تقویت عامل‌ها برای تحلیل مالی، امنیت سایبری و کاربردهای تحقیقاتی برتری دارد.

---

## جزئیات بیشتر

### Anthropic

- **Claude 4.5 Sonnet**: بهترین مدل ما برای ساخت عامل‌های پیچیده با قابلیت‌های کدنویسی پیشرفته و عملکرد مستقل گسترده. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**
- **پنجره متنی**: 200 هزار توکن برای مدیریت مکالمات و اسناد گسترده
- **قابلیت‌های پیشرفته**: برتری در کدنویسی، قابلیت‌های عاملی، استفاده بهبود یافته از ابزارها و تولید محتوای خلاقانه
- **قیمت‌گذاری**: همان قیمت‌گذاری Sonnet 4 با ورودی 3 دلار/1 میلیون توکن و خروجی 15 دلار/1 میلیون توکن
- **پشتیبانی دوگانه SDK**: سازگار با هر دو SDK OpenAI و API بومی Anthropic
- **پشتیبانی Endpoint**: در دسترس در v1/chat/completions و v1/messages

**بهبودهای کلیدی نسبت به Sonnet 4:**

#### برتری در کدنویسی
- **عملکرد SWE-bench Verified**: پیشرفته‌ترین عملکرد در معیارهای کدنویسی
- **برنامه‌ریزی بهبود یافته**: تصمیمات معماری بهتر و سازماندهی کد
- **مهندسی امنیت بهبود یافته**: شیوه‌های امنیتی مقاوم‌تر و تشخیص آسیب‌پذیری‌ها
- **پیروی بهتر از دستورالعمل‌ها**: پایبندی دقیق‌تر به مشخصات و الزامات کدنویسی
- **تفکر گسترده**: عملکرد بهتری در وظایف کدنویسی هنگام فعال‌سازی تفکر گسترده

#### قابلیت‌های عاملی
- **عملکرد مستقل گسترده**: قابلیت کار مستقل برای ساعت‌ها با حفظ وضوح و تمرکز بر پیشرفت تدریجی
- **آگاهی متنی**: ردیابی استفاده از توکن در طول مکالمات و دریافت به‌روزرسانی پس از هر فراخوانی ابزار
- **استفاده بهبود یافته از ابزارها**: استفاده مؤثرتر از فراخوانی‌های موازی ابزار و هماهنگی بهبود یافته در میان ابزارهای متعدد
- **مدیریت متن پیشرفته**: حفظ ردیابی وضعیت استثنایی در فایل‌های خارجی و حفظ هدف‌گرایی در جلسات

#### سبک ارتباط و تعامل
- **ارتباط بهینه‌شده**: رویکرد مختصر، مستقیم و طبیعی با به‌روزرسانی‌های پیشرفت مبتنی بر واقعیت
- **حفظ جریان کار**: ممکن است خلاصه‌های پرمفصل پس از فراخوانی ابزارها را نادیده بگیرد (قابل تنظیم با دستورات)

#### تولید محتوای خلاقانه
- **ارائه‌ها و انیمیشن‌ها**: برابر یا بهتر از Claude Opus 4.1 برای ایجاد اسلایدها و محتوای بصری
- **ذوق خلاقانه**: تولید خروجی صیقلی و حرفه‌ای با پیروی قوی از دستورالعمل‌ها
- **کیفیت تلاش اول**: تولید محتوای قابل استفاده و طراحی‌شده در تلاش‌های اولیه

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | خروجی |
|-------|-------|--------|
| claude-sonnet-4-5 | $3.00/1M توکن | $15.00/1M توکن |

**نمونه‌های استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-5",
    "messages": [
      {
        "role": "system",
        "content": "شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید."
      },
      {
        "role": "user",
        "content": "این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="claude-sonnet-4-5",
    messages=[
        {
            "role": "system",
            "content": "شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید.",
        },
        {
            "role": "user",
            "content": "این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید.",
        },
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "claude-sonnet-4-5",
  messages: [
    {
      role: "system",
      content: "شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید.",
    },
    {
      role: "user",
      content: "این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

**فرمت SDK بومی Anthropic:**

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-5",
    "max_tokens": 1000,
    "system": "شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید.",
    "messages": [
      {
        "role": "user",
        "content": "این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-sonnet-4-5",
    max_tokens=1000,
    system="شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید.",
    messages=[
        {
            "role": "user",
            "content": "این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید.",
        }
    ],
)

print(message.content)

javascript=:import Anthropic from '@anthropic-ai/sdk';

const anthropic = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: 'https://api.avalai.ir',
});

const message = await anthropic.messages.create({
  model: 'claude-sonnet-4-5',
  max_tokens: 1000,
  system: 'شما یک مهندس نرم‌افزار متخصص در بازنویسی کد هستید.',
  messages: [
    {
      role: 'user',
      content: 'این پروژه پایتون چندفایله را برای بهبود قابلیت نگهداری و اضافه کردن مدیریت خطای مناسب بازنویسی کنید.',
    },
  ],
});

console.log(message.content);

```

### ویژگی‌های پیشرفته

#### استفاده بهبود یافته از ابزارها
Claude 4.5 Sonnet شامل مدیریت بهبود یافته پارامترهای ابزار است که قالب‌بندی عمدی در پارامترهای رشته‌ای فراخوانی ابزار را حفظ می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-sonnet-4-5",
    "messages": [
      {
        "role": "user",
        "content": "در مدیریت وظایف پروژه‌ام کمک کنید"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "edit_file",
          "description": "ویرایش فایل با قالب‌بندی دقیق",
          "parameters": {
            "type": "object",
            "properties": {
              "filename": {
                "type": "string",
                "description": "نام فایل برای ویرایش"
              },
              "content": {
                "type": "string",
                "description": "محتوای فایل با حفظ قالب‌بندی"
              }
            },
            "required": ["filename", "content"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

python=:tools = [
    {
        "type": "function",
        "function": {
            "name": "edit_file",
            "description": "ویرایش فایل با قالب‌بندی دقیق",
            "parameters": {
                "type": "object",
                "properties": {
                    "filename": {
                        "type": "string",
                        "description": "نام فایل برای ویرایش",
                    },
                    "content": {
                        "type": "string",
                        "description": "محتوای فایل با حفظ قالب‌بندی",
                    },
                },
                "required": ["filename", "content"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="claude-sonnet-4-5",
    messages=[{"role": "user", "content": "در مدیریت وظایف پروژه‌ام کمک کنید"}],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
    {
        type: "function",
        function: {
            name: "edit_file",
            description: "ویرایش فایل با قالب‌بندی دقیق",
            parameters: {
                type: "object",
                properties: {
                    filename: {
                        type: "string",
                        description: "نام فایل برای ویرایش",
                    },
                    content: {
                        type: "string",
                        description: "محتوای فایل با حفظ قالب‌بندی",
                    }
                },
                required: ["filename", "content"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "claude-sonnet-4-5",
    messages: [{role: "user", content: "در مدیریت وظایف پروژه‌ام کمک کنید"}],
    tools: tools,
    tool_choice: "auto",
});

```

### مهاجرت از Sonnet 4

اگر در حال حاضر از Claude Sonnet 4 استفاده می‌کنید، ارتقا به Sonnet 4.5 ساده است:

1. نام مدل خود را به `claude-sonnet-4-5` به‌روزرسانی کنید
2. فراخوانی‌های API موجود همچنان کار خواهند کرد
3. فعال‌سازی ویژگی‌های جدید مانند ابزارهای حافظه برای عامل‌های طولانی‌مدت را در نظر بگیرید

---

## لینک‌های مرتبط

- [مستندات مدل‌های Anthropic](fa/providers/anthropic.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [بهترین شیوه‌های توسعه عامل](fa/guides/agents.md)
- [پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md)
