---
hasH1: true
---

# مدل‌های XAI (Grok)

AvalAI دسترسی به خانواده مدل‌های Grok از XAI را فراهم می‌کند که به دلیل پنجره‌های زمینه بزرگ و قابلیت‌های دسترسی به اطلاعات بلادرنگ (هنگام استفاده مستقیم از طریق XAI) شناخته شده‌اند.

## Grok 4.7

از `grok-4.7`، تازه‌ترین مدل xAI برای کدنویسی و کار دانشی، در عامل‌های مهندسی طولانی‌مدت، راستی‌آزمایی دقیق، تهیه سند و ارائه و تحلیل فنی استفاده کنید. xAI از مدل پایه بزرگ‌تر، آموزش طولانی‌تر روی مسائل دشوار، مدیریت بهتر زمینه و بازنگری سازوکارهای ایمنی نسبت به Grok 4.6 خبر می‌دهد. نتایج ارزیابی و ادعاهای سرعت ارائه‌دهنده، تضمین عملکرد در AvalAI نیستند.

| ویژگی | جزئیات |
| --- | --- |
| شناسه مدل | `grok-4.7` |
| ارائه‌دهنده | xAI |
| حداکثر توکن ورودی در فهرست AvalAI | 500,000 |
| حداکثر توکن خروجی در فهرست AvalAI | 500,000 |
| قابلیت‌ها | بینایی، استدلال، فراخوانی ابزار، خروجی ساختاریافته، حافظه نهان پرامپت |
| پشتیبانی کامل | `v1/chat/completions`، `v1/messages` |
| پشتیبانی جزئی | `v1/responses` |

مقدارهای ورودی و خروجی سقف‌های جداگانه فهرست هستند و استفاده هم‌زمان از هر دو سقف را تضمین نمی‌کنند. Grok 4.7 مدل تولید مستقیم تصویر نیست.

قیمت‌ها به دلار آمریکا برای هر ۱ میلیون توکن هستند و نسبت به Grok 4.6 تغییری نکرده‌اند. طول ورودی درخواست، تعرفه ورودی، ورودی ذخیره‌شده و خروجی را تعیین می‌کند. تعرفه بالاتر فقط برای ورودی بیش از ۲۰۰ هزار توکن اعمال می‌شود، نه دقیقاً این مقدار، و مربوط به نسخه سریع جداگانه نیست.

| طول ورودی | ورودی | ورودی ذخیره‌شده | خروجی |
| --- | ---: | ---: | ---: |
| حداکثر 200K، شامل خود این مقدار | $2.00 | $0.50 | $6.00 |
| بیش از 200K | $4.00 | $1.00 | $12.50 |

با یک درخواست ساده Chat Completions شروع کنید:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.7",
    "messages": [
      {"role": "user", "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag."}
    ]
  }'
```

**استدلال و سازگاری:** ابتدا پارامتر `reasoning_effort` را ارسال نکنید. برچسب‌های تلاش استدلالی در ارزیابی‌های منبع معرفی، مقدارهای مجاز یا پیش‌فرض AvalAI را تعیین نمی‌کنند. هر کنترل اضافی را روی مسیر انتخابی بررسی کنید. پشتیبانی Responses **جزئی** است، نه برابری کامل ابزارهای میزبانی‌شده یا گردش‌کارهای دارای وضعیت ذخیره‌شده؛ پیش از تغییر نقطه پایانی، رفت‌وبرگشت ابزارها، خروجی ساختاریافته و ادامه مکالمه را آزمایش کنید.

این خبر ارتقای خودکار Grok 4.6، مسیر سریع جداگانه در AvalAI یا دسترسی نیازمند دعوت‌نامه برای آزمون امنیتی تهاجمی را اعلام نمی‌کند. [خبر انتشار](fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added.md)، [صفحه مدل](fa/models/grok-4.7.md)، [راهنمای استدلال](fa/guides/reasoning.md) و [قیمت‌گذاری](fa/pricing.md) را ببینید.

## Grok 4.6

از `grok-4.6` برای عامل‌های طولانی‌مدت، کدنویسی در پایگاه‌های کد بزرگ و کار دانشی شامل پژوهش، تحلیل و اصلاح استفاده کنید. توانایی این مدل در پروژه‌های تعاملی و بصری به ساختار برنامه، رابط کاربری و تعاملات آن مربوط است، نه تولید تصویر.

### grok-4.6

| ویژگی | جزئیات |
| --- | --- |
| شناسه مدل | `grok-4.6` |
| حداکثر توکن ورودی در فهرست AvalAI | 500,000 |
| حداکثر توکن خروجی در فهرست AvalAI | 500,000 |
| قابلیت‌ها | بینایی، استدلال، فراخوانی ابزار، خروجی ساختاریافته، حافظه نهان پرامپت |
| در دسترس از طریق | `v1/chat/completions`، `v1/messages`، `v1/responses` (پشتیبانی جزئی) |
| مناسب برای | عامل‌های مهندسی طولانی‌مدت، تحلیل سند، کار دانشی و نمونه‌سازی برنامه‌های تعاملی |

قیمت‌ها به دلار آمریکا برای هر ۱ میلیون توکن هستند. برای ورودی بیش از ۲۰۰ هزار توکن، تعرفه زمینه بلند اعمال می‌شود؛ این تعرفه مربوط به نسخه جداگانه Fast نیست.

| طول ورودی | ورودی | ورودی ذخیره‌شده | خروجی |
| --- | ---: | ---: | ---: |
| حداکثر 200K توکن، شامل خود این مقدار | $2.00 | $0.50 | $6.00 |
| بیش از 200K توکن | $4.00 | $1.00 | $12.50 |

با یک درخواست ساده Chat Completions شروع کنید:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.6",
    "messages": [
      {"role": "user", "content": "Plan an interactive dashboard for incident triage, including implementation steps and verification checks."}
    ]
  }'
```

**سازگاری و مهاجرت:** هنگام مهاجرت از Grok 4.5، پرامپت‌ها، چرخه‌های فراخوانی ابزار، خروجی ساختاریافته و بودجه توکن را با محدودیت‌های ثبت‌شده Grok 4.6 آزمایش کنید؛ پنجره ۱ میلیون توکنی مدل قبلی را به این مدل تعمیم ندهید. پشتیبانی Responses جزئی است و به معنی برابری کامل ابزارهای داخلی یا گردش‌کارهای دارای وضعیت ذخیره‌شده نیست. پیش از تغییر نقطه پایانی، گردش‌کار دقیق خود را بررسی کنید. پشتیبانی از استدلال به‌تنهایی مقدارهای مجاز `reasoning_effort` را مشخص نمی‌کند؛ تا زمانی که پشتیبانی مسیر تأیید نشده، این پارامتر را ارسال نکنید.

[اعلامیه انتشار ۱۴۰۵-۰۶-۲۰ / (2026-09-11)](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md) را ببینید.

## Grok 4.5

مدل نسل پیشین XAI برای کدنویسی، وظایف عاملی و کار دانشی. Grok 4.5 برای مهندسی نرم‌افزار واقعی، گردش‌کارهای طولانی ابزارمحور، کارهای سندی شبیه Office و استدلال سریع با قیمت‌گذاری وابسته به زمینه بالای ۲۰۰K توکن بهینه شده است.

### grok-4.5

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.5` |
| پنجره زمینه | ۱,۰۰۰,۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، کدنویسی عاملی |
| در دسترس در | `v1/chat/completions`، `v1/responses` (پشتیبانی جزئی) |
| قیمت ورودی | $2.00 / 1M توکن |
| قیمت ورودی کش‌شده | $0.50 / 1M توکن |
| قیمت خروجی | $6.00 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $4.00 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $1.00 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $12.50 / 1M توکن |
| نقاط قوت | کدنویسی، گردش‌کارهای عاملی، استدلال مهندسی، کارهای سندی/Office، تولید سریع توکن |
| بهترین برای | عامل‌های مهندسی نرم‌افزار، کدنویسی ابزارمحور، تحلیل فنی، کار دانشی زمینه‌طولانی |

**ویژگی‌های کلیدی:**
- **استدلال متمرکز بر مهندسی**: عملکرد قوی در بنچمارک‌های کدنویسی، ترمینال و مهندسی نرم‌افزار.
- **گردش‌کارهای عاملی**: مناسب برای وظایف چندمرحله‌ای که به استفاده از ابزار، debugging و اصلاح تکرارشونده نیاز دارند.
- **سرویس‌دهی سریع**: xAI مدل Grok 4.5 را به‌عنوان مدلی با سرعت سرویس‌دهی بالا و کارایی توکنی قوی معرفی کرده است.
- **قیمت‌گذاری وابسته به زمینه**: برای درخواست‌های بالای ۲۰۰K توکن، نرخ‌های بالاتر ورودی، ورودی کش‌شده و خروجی اعمال می‌شود.
- **پشتیبانی جزئی Responses**: برای سازگاری گسترده، Chat Completions را ترجیح دهید؛ در صورت پشتیبانی route و حساب، از Responses استفاده کنید.

```python
response = client.chat.completions.create(
    model="grok-4.5",
    messages=[
        {
            "role": "user",
            "content": "باگ این تابع median را پیدا کن و یک اصلاح امن توضیح بده: function median(a){a.sort();return a[a.length/2]}",
        },
    ],
)
```

---

## Grok 4.3

مدل استدلالی پرچمدار جدید XAI با پنجره زمینه ۱,۰۰۰,۰۰۰ توکنی، فراخوانی تابع، خروجی‌های ساختاریافته و قیمت‌گذاری وابسته به زمینه برای درخواست‌های بالای ۲۰۰K توکن.

### grok-4.3

Grok-4.3 برای استدلال پیشرفته، تحلیل زمینه‌طولانی، خروجی‌های ساختاریافته و گردش‌کارهای چت مجهز به ابزار از طریق Chat Completions API طراحی شده است.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.3` |
| نام مستعار بالادستی | `grok-4.3-latest` |
| پنجره زمینه | ۱,۰۰۰,۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال |
| در دسترس در | `v1/chat/completions` |
| قیمت ورودی | $1.25 / 1M توکن |
| قیمت ورودی کش‌شده | $0.20 / 1M توکن (۸۴٪ کاهش هزینه) |
| قیمت خروجی | $2.50 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $2.50 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $0.40 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $5.00 / 1M توکن |
| نقاط قوت | استدلال پیشرفته، تحلیل زمینه‌طولانی، خروجی‌های ساختاریافته، فراخوانی تابع |
| بهترین برای | حل مسئله پیچیده، گردش‌کارهای عاملی، تحلیل اسناد، چت مجهز به ابزار |

**ویژگی‌های کلیدی:**
- **پنجره زمینه بزرگ**: ۱ میلیون توکن برای اسناد طولانی، مکالمات گسترده و زمینه‌های بزرگ
- **استدلال**: مدل پیش از پاسخ‌گویی فکر می‌کند تا مسائل پیچیده را بهتر حل کند
- **فراخوانی تابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی‌های ساختاریافته**: ارائه پاسخ‌ها در قالب‌های مشخص و سازمان‌یافته
- **قیمت‌گذاری وابسته به زمینه**: برای درخواست‌های فراتر از پنجره ۲۰۰K، نرخ‌های متفاوت اعمال می‌شود

```python
response = client.chat.completions.create(
    model="grok-4.3",
    messages=[
        {
            "role": "user",
            "content": "این پیشنهاد معماری را تحلیل کن و پرریسک‌ترین فرضیات را مشخص کن.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.3` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این پیشنهاد معماری را تحلیل کن و پرریسک‌ترین فرضیات را مشخص کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال فراخوانی تابع:**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_inventory",
            "description": "دریافت اطلاعات موجودی فعلی برای یک SKU",
            "parameters": {
                "type": "object",
                "properties": {
                    "sku": {
                        "type": "string",
                        "description": "Product SKU",
                    }
                },
                "required": ["sku"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4.3",
    messages=[{"role": "user", "content": "موجودی SKU AVAL-123 را بررسی کن."}],
    tools=tools,
    tool_choice="auto",
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.3` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="موجودی SKU AVAL-123 را بررسی کن.",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## Grok 4

جدیدترین و پیشرفته‌ترین مدل از XAI که عملکرد بی‌نظیری در پردازش زبان طبیعی، ریاضیات و قابلیت‌های استدلال ارائه می‌دهد.

### Grok 4

مدل پرچمدار XAI که به عنوان راه‌حل هوش مصنوعی همه‌منظوره مناسب با قابلیت‌های استثنایی در کاربردهای متنوع عمل می‌کند.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4`، `grok-4-latest`، `grok-4-0709` |
| پنجره زمینه | ۲۵۶٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال |
| قیمت‌گذاری ورودی | ۳.۰۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۷۵ دلار / ۱ میلیون توکن (۷۵٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۱۵.۰۰ دلار / ۱ میلیون توکن |
| نقاط قوت | استدلال پیشرفته، محاسبات ریاضی، درک بینایی، وظایف زبان طبیعی |
| بهترین برای | حل مسائل پیچیده، تولید کد، تحلیل تصویر، تحقیق و تجزیه و تحلیل |

**ویژگی‌های کلیدی:**
- **قابلیت‌های بینایی**: تجزیه و تحلیل و درک تصاویر در کنار متن
- **فراخوانی تابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی‌های ساختاریافته**: ارائه پاسخ‌ها در قالب‌های خاص و سازمان‌یافته
- **استدلال**: مدل قبل از پاسخ دادن فکر می‌کند تا پاسخ‌های دقیق‌تری ارائه دهد
- **پنجره زمینه بزرگ**: مدیریت مکالمات و اسناد گسترده

```python
response = client.chat.completions.create(
    model="grok-4",
    messages=[
        {
            "role": "user",
            "content": "محاسبات کوانتومی را توضیح دهید و یک مثال ریاضی ارائه دهید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="محاسبات کوانتومی را توضیح دهید و یک مثال ریاضی ارائه دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال فراخوانی تابع:**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_math",
            "description": "انجام محاسبات ریاضی",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "عبارت ریاضی برای ارزیابی",
                    }
                },
                "required": ["expression"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4",
    messages=[{"role": "user", "content": "۱۵ ضرب در ۲۳ به علاوه ۴۷ چقدر می‌شود؟"}],
    tools=tools,
    tool_choice="auto",
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="۱۵ ضرب در ۲۳ به علاوه ۴۷ چقدر می‌شود؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال بینایی:**

```python
import base64


# تابع برای کدگذاری تصویر
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# مسیر تصویر شما
image_path = "path/to/your/image.jpg"
base64_image = encode_image(image_path)

# ایجاد یک پیام با متن و تصویر
response = client.chat.completions.create(
    model="grok-4",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "در این تصویر چه چیزی وجود دارد؟ تحلیل دقیقی ارائه دهید.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## Grok 4.20 (پایدار)

نسخهٔ پایدار مدل پرچمدار Grok 4.20 از X.AI که اکنون به‌صورت عمومی با هر دو نوع reasoning و non-reasoning در دسترس است. این مدل سرعت پیشرو در صنعت، فراخوانی ابزار عامل‌محور، پایین‌ترین نرخ توهم در بازار و پایبندی دقیق به پرامپت را برای پاسخ‌های پیوسته دقیق و صادقانه ترکیب می‌کند.

### grok-4.20-reasoning

نسخهٔ پایدار استدلالی Grok 4.20، طراحی‌شده برای وظایف حل مسئله پیچیده که به تفکر تحلیلی عمیق نیاز دارند.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.20-reasoning` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی توابع، خروجی ساختارمند، استدلال |
| قیمت ورودی | $2.00 / 1M توکن |
| قیمت ورودی کش‌شده | $0.20 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $6.00 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $4.00 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $0.40 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $12.00 / 1M توکن |
| نقاط قوت | سرعت پیشرو در صنعت، پایین‌ترین نرخ توهم، پایبندی دقیق به پرامپت، فراخوانی ابزار عامل‌محور |
| بهترین برای | استدلال پیچیده، جریان‌های کاری عامل‌محور، پاسخ‌های دقیق، خروجی‌های صادقانه |

**ویژگی‌های کلیدی:**
- **حالت استدلال**: تفکر گسترده پیش از پاسخ‌گویی برای حل مسائل پیچیده
- **پنجره زمینه عظیم**: ۲ میلیون توکن برای اسناد و مکالمات گسترده
- **پایین‌ترین نرخ توهم**: دقت و صحت پیشرو در صنعت
- **پایبندی دقیق به پرامپت**: پاسخ‌های پیوسته دقیق
- **فراخوانی توابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی ساختارمند**: بازگرداندن پاسخ‌ها در قالب‌های مشخص و سازمان‌یافته
- **قیمت‌گذاری زمینه بالاتر**: نرخ‌های متفاوت برای درخواست‌های فراتر از پنجره ۲۰۰K

```python
response = client.chat.completions.create(
    model="grok-4.20-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Design a fault-tolerant distributed system architecture for a global payment platform.",
        },
    ],
    max_tokens=4096,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.20-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Design a fault-tolerant distributed system architecture for a global payment platform.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### grok-4.20-non-reasoning

نسخهٔ پایدار non-reasoning که برای پاسخ‌های سریع بدون تفکر گسترده بهینه‌سازی شده و برای برنامه‌های پرتوان ایده‌آل است.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.20-non-reasoning` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی توابع، خروجی ساختارمند |
| قیمت ورودی | $2.00 / 1M توکن |
| قیمت ورودی کش‌شده | $0.20 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $6.00 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $4.00 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $0.40 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $12.00 / 1M توکن |
| نقاط قوت | استنتاج سریع، زمینه عظیم، توان بالا، پاسخ‌های دقیق |
| بهترین برای | برنامه‌های پرتوان، سیستم‌های بلادرنگ، اجرای سریع ابزار |

**ویژگی‌های کلیدی:**
- **استنتاج سریع**: بهینه‌سازی‌شده برای پاسخ‌های سریع بدون سربار استدلال
- **پنجره زمینه عظیم**: ظرفیت ۲ میلیون توکنی برای مدیریت زمینه گسترده
- **کش مقرون‌به‌صرفه**: ۹۰٪ کاهش هزینه با توکن‌های ورودی کش‌شده
- **فراخوانی توابع**: قابلیت‌های یکپارچه‌سازی ابزار خارجی
- **خروجی ساختارمند**: قالب‌بندی سازمان‌یافته پاسخ

```python
response = client.chat.completions.create(
    model="grok-4.20-non-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Summarize the key points from this document.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.20-non-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "Summarize the key points from this document.",
                },
                {"type": "input_file", "file_id": "file_abc123"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## Grok 4.20 Beta

مدل پرچم‌دار بتای X.AI با سرعت پیشرو در صنعت و قابلیت‌های فراخوانی ابزار عاملی. این مدل کمترین نرخ توهم‌زایی در بازار را با پایبندی دقیق به پرامپت ترکیب می‌کند و پاسخ‌های دقیق و صادقانه ارائه می‌دهد.

### grok-4.20-beta-0309-reasoning

نسخه استدلالی Grok 4.20 Beta، طراحی شده برای وظایف حل مسئله پیچیده که نیاز به تفکر تحلیلی عمیق دارند.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.20-beta-0309-reasoning` |
| نام‌های مستعار | `grok-4.20-beta`، `grok-4.20-beta-0309`، `grok-4.20-beta-latest`، `grok-4.20-beta-latest-reasoning`، `grok-4.20-beta-reasoning` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال |
| قیمت‌گذاری ورودی | ۲.۰۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۲۰ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۶.۰۰ دلار / ۱ میلیون توکن |
| قیمت ورودی (بالای ۲۰۰K) | ۴.۰۰ دلار / ۱ میلیون توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | ۰.۴۰ دلار / ۱ میلیون توکن |
| قیمت خروجی (بالای ۲۰۰K) | ۱۲.۰۰ دلار / ۱ میلیون توکن |
| نقاط قوت | سرعت پیشرو در صنعت، کمترین نرخ توهم‌زایی، پایبندی دقیق به پرامپت، فراخوانی ابزار عاملی |
| بهترین برای | استدلال پیچیده، گردش‌کارهای عاملی، پاسخ‌های دقیق، خروجی‌های صادقانه |

**ویژگی‌های کلیدی:**
- **حالت استدلال**: مدل قبل از پاسخ‌دهی فکر می‌کند برای حل مسائل پیچیده
- **پنجره زمینه عظیم**: ۲ میلیون توکن برای اسناد و مکالمات گسترده
- **کمترین نرخ توهم‌زایی**: دقت و صداقت پیشرو در صنعت
- **پایبندی دقیق به پرامپت**: پاسخ‌های دقیق و مداوم
- **فراخوانی تابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی‌های ساختاریافته**: بازگرداندن پاسخ‌ها در قالب‌های خاص و سازمان‌یافته
- **قیمت‌گذاری زمینه بالاتر**: نرخ‌های متفاوت برای درخواست‌هایی که از پنجره زمینه ۲۰۰K فراتر می‌روند

```python
response = client.chat.completions.create(
    model="grok-4.20-beta-0309-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
        },
    ],
    max_tokens=4096,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.20-beta-0309-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### grok-4.20-beta-0309-non-reasoning

نسخه غیراستدلالی بهینه‌سازی شده برای پاسخ‌های سریع بدون تفکر گسترده، مناسب برای برنامه‌های با توان عملیاتی بالا.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4.20-beta-0309-non-reasoning` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت‌گذاری ورودی | ۲.۰۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۲۰ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۶.۰۰ دلار / ۱ میلیون توکن |
| قیمت ورودی (بالای ۲۰۰K) | ۴.۰۰ دلار / ۱ میلیون توکن |
| قیمت خروجی (بالای ۲۰۰K) | ۱۲.۰۰ دلار / ۱ میلیون توکن |
| نقاط قوت | استنتاج سریع، زمینه عظیم، توان عملیاتی بالا، پاسخ‌های دقیق |
| بهترین برای | برنامه‌های توان عملیاتی بالا، سیستم‌های بلادرنگ، اجرای سریع ابزار |

**ویژگی‌های کلیدی:**
- **استنتاج سریع**: بهینه‌سازی شده برای پاسخ‌های سریع بدون سربار استدلال
- **پنجره زمینه عظیم**: ظرفیت ۲ میلیون توکن برای مدیریت زمینه گسترده
- **کش‌گذاری مقرون‌به‌صرفه**: ۹۰٪ کاهش هزینه با توکن‌های ورودی کش‌شده
- **فراخوانی تابع**: قابلیت‌های یکپارچه‌سازی ابزار خارجی
- **خروجی‌های ساختاریافته**: قالب‌بندی پاسخ سازمان‌یافته

```python
response = client.chat.completions.create(
    model="grok-4.20-beta-0309-non-reasoning",
    messages=[
        {
            "role": "user",
            "content": "نکات کلیدی این سند را خلاصه کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4.20-beta-0309-non-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="نکات کلیدی این سند را خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## Grok 4.1 Fast

آخرین پیشرفت از XAI، بهینه‌سازی شده به طور خاص برای فراخوانی ابزار عاملی با کارایی بالا با قابلیت‌های استدلال گسترده و پنجره زمینه عظیم 2 میلیون توکنی.

### grok-4-1-fast-reasoning

مدل مالتی‌مودال پیشرفته با قابلیت‌های استدلال گسترده برای حل مسائل پیچیده و گردش‌کارهای عاملی.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4-1-fast-reasoning` |
| پنجره زمینه | 2,000,000 توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال |
| قیمت‌گذاری ورودی | $0.20 / 1M توکن |
| قیمت‌گذاری ورودی کش‌شده | $0.05 / 1M توکن (75% کاهش هزینه) |
| قیمت‌گذاری خروجی | $0.50 / 1M توکن |
| نقاط قوت | استدلال گسترده، فراخوانی ابزار عاملی، درک مالتی‌مودال |
| بهترین برای | گردش‌کارهای عاملی پیچیده، سیستم‌های خودکار، برنامه‌های سنگین ابزار |

**ویژگی‌های کلیدی:**
- **استدلال گسترده**: مدل قبل از پاسخ دادن به تفکر تحلیلی عمیق می‌پردازد
- **فراخوانی ابزار عاملی**: بهینه‌سازی شده برای گردش‌کارهای عامل خودکار با استفاده پیچیده از ابزار
- **زمینه عظیم**: 2 میلیون توکن امکان پردازش اسناد و مکالمات گسترده را فراهم می‌کند
- **مالتی‌مودال**: پردازش متن و تصاویر در یک درخواست
- **کش کردن پرامپت**: صرفه‌جویی قابل توجه در هزینه با توکن‌های ورودی کش‌شده

```python
response = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-1-fast-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### grok-4-1-fast-non-reasoning

مدل مالتی‌مودال پیشرفته بهینه‌شده برای پاسخ‌های سریع بدون استدلال گسترده، مناسب برای برنامه‌های با توان عملیاتی بالا.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4-1-fast-non-reasoning` |
| پنجره زمینه | 2,000,000 توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت‌گذاری ورودی | $0.20 / 1M توکن |
| قیمت‌گذاری ورودی کش‌شده | $0.05 / 1M توکن (75% کاهش هزینه) |
| قیمت‌گذاری خروجی | $0.50 / 1M توکن |
| نقاط قوت | پاسخ‌های سریع، فراخوانی ابزار عاملی، درک مالتی‌مودال |
| بهترین برای | برنامه‌های با توان عملیاتی بالا، سیستم‌های زمان واقعی، اجرای سریع ابزار |

**ویژگی‌های کلیدی:**
- **استنتاج سریع**: بهینه‌سازی شده برای پاسخ‌های سریع بدون سربار استدلال گسترده
- **فراخوانی ابزار عاملی**: طراحی هدفمند برای گردش‌کارهای عامل خودکار
- **زمینه عظیم**: 2 میلیون توکن برای مدیریت اطلاعات گسترده
- **مالتی‌مودال**: پشتیبانی از پردازش متن و تصویر
- **کش کردن مقرون‌به‌صرفه**: کاهش هزینه‌ها با کش کردن پرامپت

```python
response = client.chat.completions.create(
    model="grok-4-1-fast-non-reasoning",
    messages=[
        {
            "role": "user",
            "content": "نکات کلیدی از این سند را خلاصه کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-1-fast-non-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="نکات کلیدی از این سند را خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال فراخوانی تابع:**

```python
tools = [
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
                        "description": "نام شهر",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "واحد دما",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4-1-fast-non-reasoning",
    messages=[{"role": "user", "content": "آب و هوای نیویورک چطور است؟"}],
    tools=tools,
    tool_choice="auto",
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-1-fast-non-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="آب و هوای نیویورک چطور است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## Grok 4 Fast

آخرین پیشرفت XAI در مدل‌های استدلال مقرون‌به‌صرفه که عملکرد استثنایی را با قیمت‌گذاری مناسب و پنجره‌های زمینه عظیم ارائه می‌دهد.

### grok-4-fast-reasoning

نسخه استدلالی Grok 4 Fast، طراحی شده برای وظایف حل مسئله پیچیده که نیاز به تفکر تحلیلی عمیق دارند.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4-fast-reasoning`، `grok-4-fast`، `grok-4-fast-reasoning-latest` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال |
| قیمت‌گذاری ورودی | ۰.۲۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۰۵ دلار / ۱ میلیون توکن (۷۵٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۰.۵۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری جستجوی زنده | ۲۵.۰۰ دلار / ۱ هزار منبع |
| نقاط قوت | استدلال مقرون‌به‌صرفه، زمینه عظیم، حل مسائل پیشرفته |
| بهترین برای | تحلیل پیچیده، برنامه‌ریزی استراتژیک، وظایف تحقیق، پردازش اسناد بزرگ |

**ویژگی‌های کلیدی:**
- **پنجره زمینه عظیم**: مدیریت تا ۲ میلیون توکن برای مکالمات و اسناد گسترده
- **استدلال مقرون‌به‌صرفه**: قابلیت‌های استدلال پیشرفته با قیمت‌گذاری مناسب
- **فراخوانی تابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی‌های ساختاریافته**: ارائه پاسخ‌ها در قالب‌های خاص و سازمان‌یافته
- **بهینه‌سازی ورودی کش‌شده**: صرفه‌جویی قابل توجه در هزینه با توکن‌های کش‌شده

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="grok-4-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید که شامل تخصیص بودجه و جدول زمانی باشد",
        }
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-fast-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید که شامل تخصیص بودجه و جدول زمانی باشد",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### grok-4-fast-non-reasoning

نسخه غیراستدلالی بهینه‌شده برای وظایف چت عمومی و تولید محتوا بدون سربار استدلال.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-4-fast-non-reasoning`، `grok-4-fast-non-reasoning-latest` |
| پنجره زمینه | ۲٬۰۰۰٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت‌گذاری ورودی | ۰.۲۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۰۵ دلار / ۱ میلیون توکن (۷۵٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۰.۵۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری جستجوی زنده | ۲۵.۰۰ دلار / ۱ هزار منبع |
| نقاط قوت | پاسخ‌های سریع، زمینه عظیم، مقرون‌به‌صرفه برای وظایف عمومی |
| بهترین برای | چت عمومی، تولید محتوا، پاسخ‌های سریع، برنامه‌های پرحجم |

**ویژگی‌های کلیدی:**
- **پردازش پرسرعت**: بهینه‌شده برای پاسخ‌های سریع بدون سربار استدلال
- **پنجره زمینه عظیم**: ظرفیت ۲ میلیون توکن برای مدیریت زمینه گسترده
- **مقرون‌به‌صرفه**: قیمت‌گذاری مناسب برای برنامه‌های پرحجم
- **فراخوانی تابع**: قابلیت‌های ادغام ابزار خارجی
- **خروجی‌های ساختاریافته**: قالب‌بندی پاسخ سازمان‌یافته

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="grok-4-fast-non-reasoning",
    messages=[
        {
            "role": "user",
            "content": "آخرین روندهای هوش مصنوعی در سال ۲۰۲۵ را خلاصه کنید",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-fast-non-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="آخرین روندهای هوش مصنوعی در سال ۲۰۲۵ را خلاصه کنید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال فراخوانی تابع:**

```python
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات آب و هوای فعلی",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    }
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4-fast-reasoning",
    messages=[{"role": "user", "content": "آب و هوای نیویورک چگونه است؟"}],
    tools=tools,
    tool_choice="auto",
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-4-fast-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="آب و هوای نیویورک چگونه است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## Grok Code Fast 1

مدل تخصصی بهینه‌سازی شده برای گردش‌کارهای کدنویسی عامل با سرعت استثنایی و تسلط بر ابزارها.

### grok-code-fast-1

مدل هدفمند XAI برای توسعه‌دهندگان، طراحی شده برای برتری در وظایف کدنویسی با استنتاج فوق‌العاده سریع و ادغام ابزار برتر.

| ویژگی | جزئیات |
| ---------------- | -------------------------------------------- |
| شناسه مدل | `grok-code-fast-1` |
| پنجره زمینه | پشتیبانی از زمینه بزرگ برای کدبیس‌های گسترده |
| قابلیت‌ها | چت، تولید کد، استفاده از ابزار، گردش‌کارهای عامل |
| قیمت‌گذاری ورودی | ۰.۲۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری ورودی کش‌شده | ۰.۰۲ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت‌گذاری خروجی | ۱.۵۰ دلار / ۱ میلیون توکن |
| نقاط قوت | پاسخ‌های فوق‌العاده سریع (۱۹۰+ TPS)، کدنویسی عامل، تسلط بر ابزارها |
| بهترین برای | ادغام IDE، تولید کد، دیباگ، تجزیه و تحلیل pull request |
| زبان‌های پشتیبانی شده | TypeScript، Python، Java، Rust، C++، Go |
| در دسترس در | `v1/chat/completions`، `v1/responses`، `v1/messages` |

**ویژگی‌های کلیدی:**
- **کدنویسی عامل**: طراحی هدفمند برای گردش‌کارهای کدنویسی با حلقه‌های استدلال و فراخوانی ابزار
- **تسلط بر ابزارها**: برتری در استفاده از grep، terminal، ویرایش فایل، و سایر ابزارهای توسعه
- **عملکرد بالا**: ۱۹۰+ توکن در ثانیه با نرخ cache hit بالای ۹۰٪
- **چندزبانه**: تطبیق‌پذیری در کل پشته توسعه نرم‌افزار
- **مقرون به صرفه**: قیمت‌گذاری اقتصادی برای وظایف توسعه پرحجم

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="grok-code-fast-1",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای پیاده‌سازی جستجوی دودویی با مدیریت خطای مناسب و type hints ایجاد کنید",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-code-fast-1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک تابع Python برای پیاده‌سازی جستجوی دودویی با مدیریت خطای مناسب و type hints ایجاد کنید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال کدنویسی:**

```python
response = client.chat.completions.create(
    model="grok-code-fast-1",
    messages=[
        {
            "role": "user",
            "content": "این کد TypeScript را بررسی کنید و بهبودهایی پیشنهاد دهید:\n\nfunction processData(data: any[]) {\n  return data.map(item => item.value * 2);\n}",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-code-fast-1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Explain how AvalAI provides a unified API for this request.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## سری Grok 3

آخرین نسل مدل‌های Grok که استدلال پیشرفته، قابلیت‌های چندوجهی و پنجره‌های زمینه بزرگ را ارائه می‌دهند.

### قابلیت‌های درک تصویر

در حال حاضر، تنها مدل `grok-2-vision-latest` از میان مدل‌های XAI از قابلیت‌های بینایی پشتیبانی می‌کند. با این مدل، می‌توانید:

- توضیح و توصیف محتوای تصویر
- پاسخ به سؤالات در مورد عناصر بصری در تصاویر
- تشخیص اشیا و ارائه مختصات کادر محدودکننده
- تجزیه و تحلیل محتوای بصری در کنار متن

**نکات مهم:**

- هنگام استفاده از مدل‌های XAI با قابلیت‌های بینایی از طریق AvalAI، اگرچه ورودی‌های تصویر مبتنی بر URL به صورت فنی پشتیبانی می‌شوند، اما ممکن است همیشه به طور قابل اعتماد کار نکنند. برای بهترین نتایج، توصیه می‌کنیم تصاویر را به صورت رشته‌های کدگذاری شده base64 ارائه دهید.
- اگرچه مدل‌های سری Grok 3 با قابلیت‌های بینایی فهرست شده‌اند، این ویژگی ممکن است هنوز به طور کامل فعال نشده باشد. ما مستندات را هنگامی که این مدل‌ها به طور کامل از ویژگی‌های بینایی پشتیبانی کنند، به‌روزرسانی خواهیم کرد.

### Grok 3

توانمندترین مدل در سری Grok 3 که عملکرد و هزینه را متعادل می‌کند.

| ویژگی            | جزئیات                                       |
| ---------------- | -------------------------------------------- |
| شناسه مدل        | `grok-3-latest`                                |
| پنجره زمینه      | ۱۳۱٬۰۷۲ توکن                                 |
| قابلیت‌ها        | چت، بینایی، فراخوانی تابع، انتخاب ابزار      |
| قیمت‌گذاری ورودی | ۰.۳۰ دلار / ۱ میلیون توکن                    |
| قیمت‌گذاری خروجی | ۱۵.۰۰ دلار / ۱ میلیون توکن                   |
| نقاط قوت         | استدلال قوی، زمینه بزرگ، درک چندوجهی         |
| بهترین برای      | وظایف پیچیده نیازمند درک عمیق و زمینه گسترده |

```python
response = client.chat.completions.create(
    model="grok-3-latest",
    messages=[
        {
            "role": "user",
            "content": "اهمیت مدل‌های Grok در چشم‌انداز هوش مصنوعی را توضیح دهید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-3-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="اهمیت مدل‌های Grok در چشم‌انداز هوش مصنوعی را توضیح دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Grok 3 Fast

بهینه‌شده برای سرعت در حالی که قابلیت‌های قوی را حفظ می‌کند.

| ویژگی            | جزئیات                                                       |
| ---------------- | ------------------------------------------------------------ |
| شناسه مدل        | `grok-3-fast`                                           |
| پنجره زمینه      | ۱۳۱٬۰۷۲ توکن                                                 |
| قابلیت‌ها        | چت، بینایی، فراخوانی تابع، انتخاب ابزار                      |
| قیمت‌گذاری ورودی | ۵.۰۰ دلار / ۱ میلیون توکن                                    |
| قیمت‌گذاری خروجی | ۲۵.۰۰ دلار / ۱ میلیون توکن                                   |
| نقاط قوت         | سرعت استنتاج سریع‌تر در مقایسه با Grok 3 استاندارد           |
| بهترین برای      | برنامه‌هایی که به پاسخ‌های سریع‌تر با قابلیت بالا نیاز دارند |

```python
response = client.chat.completions.create(
    model="grok-3-fast",
    messages=[
        {
            "role": "user",
            "content": "آخرین اخبار مربوط به اکتشافات فضایی را خلاصه کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-3-fast` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="آخرین اخبار مربوط به اکتشافات فضایی را خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Grok 3 Mini

نسخه‌ای کوچکتر و بسیار مقرون به صرفه در سری Grok 3.

| ویژگی            | جزئیات                                                                                 |
| ---------------- | -------------------------------------------------------------------------------------- |
| شناسه مدل        | `grok-3-mini`                                                                     |
| پنجره زمینه      | ۱۳۱٬۰۷۲ توکن                                                                           |
| قابلیت‌ها        | چت، بینایی، فراخوانی تابع، انتخاب ابزار                                                |
| قیمت‌گذاری ورودی | ۰.۳۰ دلار / ۱ میلیون توکن                                                              |
| قیمت‌گذاری خروجی | ۰.۵۰ دلار / ۱ میلیون توکن                                                              |
| نقاط قوت         | بسیار مقرون به صرفه، پنجره زمینه بزرگ برای کلاس خود                                    |
| بهترین برای      | برنامه‌های حساس به هزینه، وظایفی که از زمینه بزرگ بهره می‌برند اما پیچیدگی کمتری دارند |

```python
response = client.chat.completions.create(
    model="grok-3-mini",
    messages=[
        {"role": "user", "content": "چند حقیقت جالب درباره سیاره مریخ چیست؟"},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-3-mini` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="چند حقیقت جالب درباره سیاره مریخ چیست؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Grok 3 Mini Fast

سریع‌ترین مدل در رده Grok 3 Mini، بهینه‌شده برای تاخیر.

| ویژگی            | جزئیات                                                                   |
| ---------------- | ------------------------------------------------------------------------ |
| شناسه مدل        | `grok-3-mini-fast-beta`                                                  |
| پنجره زمینه      | ۱۳۱٬۰۷۲ توکن                                                             |
| قابلیت‌ها        | چت، بینایی، فراخوانی تابع، انتخاب ابزار                                  |
| قیمت‌گذاری ورودی | ۰.۶۰ دلار / ۱ میلیون توکن                                                |
| قیمت‌گذاری خروجی | ۴.۰۰ دلار / ۱ میلیون توکن                                                |
| نقاط قوت         | بهینه‌شده برای سرعت در رده Mini                                          |
| بهترین برای      | برنامه‌های بلادرنگ که به پاسخ‌های مقرون به صرفه با زمینه بزرگ نیاز دارند |

```python
response = client.chat.completions.create(
    model="grok-3-mini-fast-beta",
    messages=[
        {"role": "user", "content": "'صبح بخیر' را به اسپانیایی ترجمه کنید."},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-3-mini-fast-beta` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مدل‌های Grok قبلی

نسل‌های قبلی مانند Grok 2 (`grok-2-latest`) و Grok 2 Vision (`grok-2-vision-latest`) نیز ممکن است از طریق AvalAI در دسترس باشند و ویژگی‌های عملکرد و قیمت‌گذاری متفاوتی را ارائه دهند. برای دسترسی کامل، صفحه [جزئیات مدل](fa/models/model-details.md) را بررسی کنید.

### استفاده از Grok Vision با تصاویر

هنگام استفاده از مدل `grok-2-vision-latest` با تصاویر، باید تصاویر را به صورت رشته‌های کدگذاری شده base64 ارائه دهید:

```python
import base64
from openai import OpenAI

client = OpenAI(
    api_key="AVALAI_API_KEY",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)


# تابع برای کدگذاری تصویر
def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# مسیر تصویر شما
image_path = "path/to/your/image.jpg"
base64_image = encode_image(image_path)

# ایجاد یک پیام با متن و تصویر
response = client.chat.completions.create(
    model="grok-2-vision-latest",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی وجود دارد؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-2-vision-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## استفاده از مدل‌های XAI از طریق AvalAI

با استفاده از نقاط پایانی استاندارد API AvalAI و کتابخانه‌های سازگار با OpenAI به مدل‌های Grok دسترسی پیدا کنید.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

# مثال استفاده از Grok 3 Mini
response = client.chat.completions.create(
    model="grok-3-mini",
    messages=[{"role": "user", "content": "یک لطیفه بگو."}],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `grok-3-mini` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک لطیفه بگو.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## منابع مرتبط

- [Chat Completions API](fa/api-reference/chat.md)
- [فهرست مدل‌ها](fa/models/index.md)
- [احراز هویت](fa/api-reference/authentication.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
