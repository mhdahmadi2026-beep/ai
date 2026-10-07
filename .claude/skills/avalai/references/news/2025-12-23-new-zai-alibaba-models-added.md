# News 2025-12-23-new-zai-alibaba-models-added: خروجی: هوش مصنوعی در حال تغییر نحوه زندگی و کار ما است.
URL: `https://docs.avalai.ir/fa/news/2025-12-23-new-zai-alibaba-models-added`
**تاریخ:** ۱۴۰۴-۱۰-۰۲ / (2025-12-23)

# مدل‌های جدید اضافه شدند: GLM-4.7 از Z.AI و مدل‌های Qwen3-VL، تصویر و ترجمه از Alibaba

**تاریخ:** ۱۴۰۴-۱۰-۰۲ / (2025-12-23)

## خلاصه

AvalAI نه مدل جدید هوش مصنوعی معرفی می‌کند: GLM-4.7 یک مدل کدنویسی و استدلال پیشرفته از Z.AI، به همراه هشت مدل از Alibaba DashScope شامل ویژن، تولید تصویر، نقش‌آفرینی و قابلیت‌های ترجمه ماشینی.


### Alibaba - z-image-turbo

z-image-turbo یک مدل تولید تصویر سریع و با کیفیت بالا از Alibaba است، بهینه‌سازی شده برای تولید سریع با رندر متن عالی. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **تولید تصویر پرسرعت** برای گردش‌های کاری تولید سریع
- **رندر متن بهبود یافته** با ثبات بهتر تولید کاراکترها
- **پشتیبانی از تاج** برای مهر زدن لوگو یا واترمارک روی تصاویر تولید شده
- **اندازه‌های تصویر انعطاف‌پذیر** با ۴۲ نسبت تصویر پیش‌فرض و اندازه‌های سفارشی

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | تولید تصویر |
| ورودی | متن |
| خروجی | تصویر |
| اندازه تصویر | ۵۱۲×۵۱۲ تا ۲۰۴۸×۲۰۴۸ پیکسل |
| اندپوینت‌های پشتیبانی | `v1/images/generations` |
| نقاط قوت | سرعت، رندر متن، پشتیبانی از واترمارک |
| بهترین کاربرد | تولید سریع تصویر، تصاویر دارای متن، تصاویر برنددار |

**قیمت‌گذاری:**

| نوع | قیمت |
|-----|------|
| به ازای هر تصویر (استاندارد) | $0.015 |
| به ازای هر تصویر (حالت تفکر) | $0.030 |

---

### Alibaba - qwen-image-edit-plus

qwen-image-edit-plus یک مدل پیشرفته ویرایش تصویر است که عملیات ویرایش پیچیده شامل حذف پس‌زمینه، inpainting، و انتقال سبک را پشتیبانی می‌کند. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **حذف پس‌زمینه** برای جداسازی سوژه‌ها از پس‌زمینه
- **Inpainting تصویر** برای پر کردن یا جایگزینی قسمت‌های انتخاب شده
- **انتقال سبک** برای اعمال سبک‌های هنری به تصاویر
- **تغییر رنگ** برای تغییر رنگ‌ها در مناطق انتخاب شده

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | ویرایش و تولید تصویر |
| ورودی | تصویر، متن، ماسک (اختیاری) |
| خروجی | تصویر |
| اندپوینت‌های پشتیبانی | `v1/images/generations`، `v1/images/edits` |
| نقاط قوت | ویرایش دقیق، حذف پس‌زمینه، تغییر سبک |
| بهترین کاربرد | روتوش تصویر، ویرایش خلاقانه، تغییر سبک |

**قیمت‌گذاری:**

| نوع | قیمت |
|-----|------|
| به ازای هر تصویر | $0.03 |

---

### Alibaba - qwen-plus-character

qwen-plus-character یک مدل شخصیت نقش‌آفرینی است که برای ایجاد پاسخ‌های سازگار و جذاب از دیدگاه کاراکتر بهینه‌سازی شده است. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **ثبات شخصیت** با حفظ شخصیت‌ها، ویژگی‌ها و سبک‌های گفتاری تعریف شده
- **تنوع پاسخ** با جلوگیری از پاسخ‌های تکراری با نشانگرهای سبک
- **یادآوری رابطه** با حفظ سابقه تعامل و پویایی رابطه
- **انعطاف‌پذیری ژانر** برای فانتزی، علمی-تخیلی، رمانتیک و سناریوهای مدرن

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | تولید متن |
| ورودی | متن |
| خروجی | متن |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |
| نقاط قوت | ثبات نقش‌آفرینی، حفظ شخصیت، گفتگو |
| بهترین کاربرد | شخصیت‌های مجازی، چت‌بات‌ها، بازی‌ها، NPC‌ها |

**قیمت‌گذاری:**

| نوع توکن | قیمت به ازای ۱ میلیون توکن |
|----------|---------------------------|
| ورودی | $0.50 |
| ورودی کش شده | $0.05 |
| خروجی | $1.40 |

---

### Alibaba - qwen3-vl-32b-instruct

qwen3-vl-32b-instruct یک مدل ویژن-زبان منبع‌باز با ۳۲ میلیارد پارامتر است که تعادل خوبی بین دقت و هزینه ارائه می‌دهد. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **درک تصویر** برای تجزیه و تحلیل و توضیح محتوای بصری
- **تجزیه و تحلیل ویدیو** برای نمونه‌برداری از فریم‌های ویدیو و درک
- **قابلیت‌های OCR** برای استخراج متن از تصاویر
- **مدل منبع‌باز** با نسبت عملکرد به قیمت عالی

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | ویژن-زبان |
| پارامترها | ۳۲ میلیارد |
| ورودی | متن، تصویر، ویدیو |
| خروجی | متن |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |
| نقاط قوت | نسبت عملکرد به هزینه، منبع‌باز، ویژن |
| بهترین کاربرد | تحلیل تصویر، درک ویدیو، OCR |

**قیمت‌گذاری:**

| نوع توکن | قیمت به ازای ۱ میلیون توکن |
|----------|---------------------------|
| ورودی | $0.16 |
| ورودی کش شده | $0.08 |
| خروجی | $0.64 |

---

### Alibaba - qwen3-vl-plus

qwen3-vl-plus یک مدل ویژن-زبان با کارایی بالا از سری Qwen3-VL است که تعادل خوبی بین عملکرد و هزینه ارائه می‌دهد. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **پشتیبانی از متن بلند** تا میلیون‌ها توکن برای اسناد بزرگ
- **درک ویدیوهای طولانی** حداکثر ۱ ساعت ویدیو
- **قابلیت‌های عاملی** با جستجوی تصویر و استفاده از ابزار
- **قیمت‌گذاری لایه‌ای** برای مدیریت بهینه هزینه

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | ویژن-زبان |
| ورودی | متن، تصویر، ویدیو |
| خروجی | متن |
| پنجره متن | تا ۱۲۸K+ توکن |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |
| نقاط قوت | متن بلند، ویدیوی طولانی، وظایف عاملی |
| بهترین کاربرد | تحلیل سند، درک ویدیو، OCR |

**قیمت‌گذاری (لایه‌ای):**

| نوع توکن | ≤۳۲K | ۳۲K-۱۲۸K | >۱۲۸K |
|----------|------|----------|-------|
| ورودی | $0.20 | $0.30 | $0.60 |
| ورودی کش شده | $0.10 | $0.15 | $0.30 |
| خروجی | $1.60 | $2.40 | $4.80 |

---

### Alibaba - qwen3-vl-flash

qwen3-vl-flash یک مدل ویژن-زبان سریع و اقتصادی است که برای تولید بالا و وظایف حساس به تاخیر طراحی شده است. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **استنتاج سریع** برای زمان پاسخ کم
- **هزینه اقتصادی** کمترین قیمت در سری Qwen3-VL
- **پشتیبانی چندرسانه‌ای** شامل تصاویر و ویدیوها
- **قیمت‌گذاری لایه‌ای** برای بهینه‌سازی هزینه

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | ویژن-زبان |
| ورودی | متن، تصویر، ویدیو |
| خروجی | متن |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |
| نقاط قوت | سرعت، هزینه کم، تولید بالا |
| بهترین کاربرد | برنامه‌های بلادرنگ، تحلیل سریع |

**قیمت‌گذاری (لایه‌ای):**

| نوع توکن | ≤۳۲K | ۳۲K-۱۲۸K | >۱۲۸K |
|----------|------|----------|-------|
| ورودی | $0.05 | $0.075 | $0.12 |
| ورودی کش شده | $0.01 | $0.015 | $0.024 |
| خروجی | $0.40 | $0.60 | $0.96 |

---

### Alibaba - qwen-mt-flash / qwen-mt-lite

مدل‌های qwen-mt-flash و qwen-mt-lite مدل‌های ترجمه ماشینی تخصصی از Alibaba هستند که از ۹۲ زبان پشتیبانی می‌کنند. [مستندات](fa/providers/alibaba.md)

**قابلیت‌های کلیدی:**

- **پشتیبانی از ۹۲ زبان** شامل زبان‌های اروپایی، آسیایی و خاورمیانه‌ای
- **ترجمه دو سویه** بین تمام زبان‌های پشتیبانی شده
- **گزینه‌های کیفیت** با flash برای کیفیت بالاتر و lite برای سرعت/هزینه بهتر
- **ترجمه مستقیم** بین زبان‌های غیرچینی

| ویژگی | qwen-mt-flash | qwen-mt-lite |
|-------|---------------|--------------|
| نوع | تولید متن | تولید متن |
| تمرکز | کیفیت ترجمه بالا | سرعت و هزینه |
| زبان‌های پشتیبانی | ۹۲ زبان | ۹۲ زبان |
| اندپوینت‌ها | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) | همان |

**زبان‌های فارسی/دری پشتیبانی شده:**

- فارسی (Persian/Farsi)
- دری (Dari)
- عربی (Arabic)
- اردو (Urdu)
- ترکی (Turkish)
- و ۸۷ زبان دیگر...

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-----|-------|--------------|-------|
| qwen-mt-flash | $0.16 | $0.08 | $0.49 |
| qwen-mt-lite | $0.12 | $0.06 | $0.36 |

---

## مثال‌های درخواست/پاسخ API

### تکمیل چت GLM-4.7

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7",
    "messages": [
      {
        "role": "user",
        "content": "یک الگوریتم مرتب‌سازی سریع را در پایتون پیاده‌سازی کن و پیچیدگی زمانی آن را توضیح بده"
      }
    ]
  }'
```

**پاسخ نمونه:**

```json
{
  "id": "chatcmpl-abc123",
  "created": 1766500800,
  "model": "glm-4.7",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا یک پیاده‌سازی الگوریتم QuickSort در پایتون آورده شده است:\n\n
```python\ndef quicksort(arr):\n    if len(arr) <= 1:\n        return arr\n    pivot = arr[len(arr) // 2]\n    left = [x for x in arr if x < pivot]\n    middle = [x for x in arr if x == pivot]\n    right = [x for x in arr if x > pivot]\n    return quicksort(left) + middle + quicksort(right)\n```\n\n**تحلیل پیچیدگی زمانی:**\n- بهترین حالت: O(n log n)\n- میانگین: O(n log n)\n- بدترین حالت: O(n²)...",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 256,
    "prompt_tokens": 28,
    "total_tokens": 284
  }
}
```

### تولید تصویر z-image-turbo

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "z-image-turbo",
    "prompt": "یک منظره کوهستانی زیبا با دریاچه‌ای آبی در پیش‌زمینه و آسمان صاف",
    "size": "1024x1024",
    "n": 1
  }'
```

### تحلیل تصویر qwen3-vl-plus

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-vl-plus",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/sample.jpg"
            }
          },
          {
            "type": "text",
            "text": "این تصویر را توضیح بده و اشیاء موجود را لیست کن"
          }
        ]
      }
    ]
  }'
```

### ترجمه با qwen-mt-flash

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-mt-flash",
    "messages": [
      {
        "role": "system",
        "content": "You are a professional translator. Translate the following text from Persian to English."
      },
      {
        "role": "user",
        "content": "هوش مصنوعی در حال تغییر نحوه زندگی و کار ما است."
      }
    ]
  }'
```

---

## مثال‌های استفاده از SDK

### GLM-4.7

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7",
    "messages": [
      {
        "role": "user",
        "content": "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.7",
    messages=[
        {
            "role": "user",
            "content": "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن",
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
  model: "glm-4.7",
  messages: [
    {
      role: "user",
      content: "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### z-image-turbo

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "z-image-turbo",
    "prompt": "یک لوگوی حرفه‌ای با متن AVALAI",
    "size": "1024x1024",
    "n": 1
  }'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="z-image-turbo",
    prompt="یک لوگوی حرفه‌ای با متن AVALAI",
    size="1024x1024",
    n=1,
    response_format="b64_json",
)

# ذخیره تصویر
img_data = base64.b64decode(response.data[0].b64_json)
with open("logo.png", "wb") as f:
    f.write(img_data)

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "z-image-turbo",
  prompt: "یک لوگوی حرفه‌ای با متن AvalAI",
  size: "1024x1024",
  n: 1,
  response_format: "b64_json",
});

// ذخیره تصویر
const imgData = Buffer.from(response.data[0].b64_json, "base64");
fs.writeFileSync("logo.png", imgData);

```

### qwen3-vl-plus

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-vl-plus",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "image_url",
            "image_url": {"url": "https://example.com/image.jpg"}
          },
          {
            "type": "text",
            "text": "این تصویر چه چیزی را نشان می‌دهد؟"
          }
        ]
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="qwen3-vl-plus",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
                {
                    "type": "text",
                    "text": "این تصویر چه چیزی را نشان می‌دهد؟",
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
  model: "qwen3-vl-plus",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "image_url",
          image_url: { url: "https://example.com/image.jpg" },
        },
        {
          type: "text",
          text: "این تصویر چه چیزی را نشان می‌دهد؟",
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

### qwen-mt-flash (ترجمه)

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-mt-flash",
    "messages": [
      {
        "role": "system",
        "content": "Translate from English to Persian"
      },
      {
        "role": "user",
        "content": "Artificial intelligence is transforming the way we live and work."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="qwen-mt-flash",
    messages=[
        {
            "role": "system",
            "content": "Translate from English to Persian",
        },
        {
            "role": "user",
            "content": "Artificial intelligence is transforming the way we live and work.",
        },
    ],
)

print(response.choices[0].message.content)
# خروجی: هوش مصنوعی در حال تغییر نحوه زندگی و کار ما است.

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen-mt-flash",
  messages: [
    {
      role: "system",
      content: "Translate from English to Persian",
    },
    {
      role: "user",
      content: "Artificial intelligence is transforming the way we live and work.",
    },
  ],
});

console.log(response.choices[0].message.content);
// خروجی: هوش مصنوعی در حال تغییر نحوه زندگی و کار ما است.

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های Z.AI](fa/providers/zai.md)
- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API - تصاویر](fa/api-reference/images.md)
- [قیمت‌گذاری](fa/pricing.md)
