
# اضافه شدن Gemini 3 Pro Image Preview و پشتیبانی از ارائه‌دهنده groq

**تاریخ:** 1404-08-30 / (2025-11-20)

## خلاصه

ما اضافه شدن مدل Gemini 3 Pro Image Preview (Nano Banana Pro) از Google و پشتیبانی از groq به عنوان ارائه‌دهنده جدید را اعلام می‌کنیم. Gemini 3 Pro Image Preview قابلیت‌های پیشرفته تولید و ویرایش تصویر با رندر متنی استثنایی را ارائه می‌دهد، به‌ویژه در تولید حروف فارسی عملکرد برتری دارد. groq سریع‌ترین سرعت استنتاج برای مدل‌های متن‌باز را فراهم می‌کند و اکنون 14 مدل جدید از طریق AvalAI در دسترس است.

---

## جزئیات

### Google Gemini 3 Pro Image Preview

> **نکته مهم**: برای بهترین نتایج، توصیه می‌شود از پرامپت‌های انگلیسی استفاده کنید زیرا مدل‌های تولید تصویر معمولا برای زبان انگلیسی بهینه‌سازی شده‌اند. برای پشتیبانی فنی یا سوالات، با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

مدل [`gemini-3-pro-image-preview`](fa/providers/google.md) (همچنین با نام "Nano Banana Pro" شناخته می‌شود) از Google اکنون از طریق AvalAI در دسترس است. این مدل پیشرفت قابل توجهی در فناوری تولید تصویر است، به‌ویژه برای رندر متن در تصویر و پشتیبانی از حروف فارسی.

**نام مدل:** `gemini-3-pro-image-preview`  
**نام مستعار:** Nano Banana Pro

#### ویژگی‌های کلیدی

- **رندر متن پیشرفته**: تولید متن واضح و خوانا در تصاویر شامل حروف فارسی با دقت تقریبا کامل
- **کنترل کیفیت استودیویی**: کنترل دقیق بر ترکیب‌بندی، نورپردازی، درجه‌بندی رنگ و نسبت ابعاد
- **دانش واقعی**: استفاده از Google Search برای تولید تصویر دقیق و مبتنی بر واقعیت
- **پشتیبانی از وضوح**: تولید تصاویر تا وضوح 4K (4096x4096px)
- **ویرایش تصویر**: قابلیت‌های ویرایش جامع شامل تنظیم نسبت ابعاد، تغییر نورپردازی و ثبات سوژه
- **فرآیند "تفکر" پیش‌فرض**: بهینه‌سازی ترکیب‌بندی قبل از تولید برای نتایج بهینه
- **پشتیبانی چند زبانه**: قابلیت استثنایی برای بومی‌سازی طراحی‌ها در زبان‌های مختلف
- **تولید دارایی حرفه‌ای**: طراحی شده برای موارد استفاده حرفه‌ای با کیفیت استودیویی

#### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| متن ورودی | 2.00 دلار / 1 میلیون توکن |
| تصویر ورودی | 2.00 دلار / 1 میلیون توکن (0.067 دلار به ازای هر تصویر با 560 توکن) |
| ورودی کش‌شده | 0.50 دلار / 1 میلیون توکن |
| متن خروجی | 12.00 دلار / 1 میلیون توکن |
| تصویر خروجی (1K-2K) | 0.134 دلار به ازای هر تصویر |
| تصویر خروجی (4K) | 0.24 دلار به ازای هر تصویر |

**توجه:** خروجی تصویر با قیمت 120 دلار به ازای 1 میلیون توکن محاسبه می‌شود. تصاویر خروجی از 1024x1024px (1K) تا 2048x2048px (2K) معادل 1120 توکن هستند. تصاویر خروجی تا 4096x4096px (4K) معادل 2000 توکن هستند.

#### قابلیت‌های منحصر به فرد

مدل [`gemini-3-pro-image-preview`](fa/providers/google.md) اولین مدل تولید تصویر است که حروف فارسی را تقریبا به طور کامل رندر می‌کند و این آن را به بهترین مدل تولید تصویر برای ایجاد محتوای فارسی تبدیل می‌کند. این پیشرفت طراحان و توسعه‌دهندگان را قادر می‌سازد تا مواد بازاریابی بومی‌شده، پوسترها و اینفوگرافیک‌ها را با رندر دقیق متن فارسی ایجاد کنند.

#### نمونه‌های درخواست/پاسخ API

**استفاده از نقطه پایانی Chat Completions:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "messages": [
      {
        "role": "user",
        "content": "یک پوستر مینیمالیست با متن فارسی \"هوش مصنوعی\" در یک سبک مدرن و الهام‌گرفته از فناوری با رنگ‌های آبی و سفید ایجاد کن"
      }
    ],
    "modalities": ["image", "text"]
  }' | jq '.choices[0].message.images[0].image_url.url |= (.[0:100] + "...[TRUNCATED]")'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1732147200,
  "model": "gemini-3-pro-image-preview",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "من یک پوستر مینیمالیست با الهام از فناوری با متن فارسی \"هوش مصنوعی\" در یک سبک مدرن با رنگ‌های آبی و سفید ایجاد کرده‌ام.",
        "role": "assistant",
        "images": [
          {
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zU...[TRUNCATED]",
              "detail": "auto"
            },
            "index": 0,
            "type": "image_url"
          }
        ],
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1150,
    "prompt_tokens": 32,
    "total_tokens": 1182,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 32,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.1558000000",
    "irt": 17864.68,
    "exchange_rate": 114600
  }
}
```

#### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "messages": [
      {
        "role": "user",
        "content": "یک لوگوی مدرن برای یک شرکت فناوری به نام \"AvalAI\" با تایپوگرافی تمیز و طراحی مینیمالیست ایجاد کن"
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3-pro-image-preview",
    messages=[
        {
            "role": "user",
            "content": 'یک لوگوی مدرن برای یک شرکت فناوری به نام "AvalAI" با تایپوگرافی تمیز و طراحی مینیمالیست ایجاد کن',
        }
    ],
    extra_body={"modalities": ["image", "text"]},
)

# دسترسی به تصویر تولید شده
if hasattr(response.choices[0].message, "images"):
    images = getattr(response.choices[0].message, "images")
    for img in images:
        print(f"Image URL: {img.image_url.url[:100]}...")

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3-pro-image-preview",
  messages: [
    {
      role: "user",
      content: "یک لوگوی مدرن برای یک شرکت فناوری به نام \"AvalAI\" با تایپوگرافی تمیز و طراحی مینیمالیست ایجاد کن",
    },
  ],
  modalities: ["image", "text"],
});

// دسترسی به تصویر تولید شده
if (response.choices[0].message.images) {
  const images = response.choices[0].message.images;
  images.forEach((img, idx) => {
    console.log(`Image ${idx}: ${img.image_url.url.substring(0, 100)}...`);
  });
}

console.log(response.choices[0].message.content);

```

#### نمونه ویرایش تصویر

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-image-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "نسبت ابعاد را به 16:9 تغییر بده در حالی که سوژه در مرکز باقی بماند"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/original-image.jpg"
            }
          }
        ]
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3-pro-image-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "نسبت ابعاد را به 16:9 تغییر بده در حالی که سوژه در مرکز باقی بماند",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/original-image.jpg"},
                },
            ],
        }
    ],
    extra_body={"modalities": ["image", "text"]},
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3-pro-image-preview",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "نسبت ابعاد را به 16:9 تغییر بده در حالی که سوژه در مرکز باقی بماند",
        },
        {
          type: "image_url",
          image_url: { url: "https://example.com/original-image.jpg" },
        },
      ],
    },
  ],
  modalities: ["image", "text"],
});

console.log(response.choices[0].message.content);

```

---

### پشتیبانی از ارائه‌دهنده groq

ما پشتیبانی از groq (groq.com) را به عنوان ارائه‌دهنده جدید اعلام می‌کنیم که سریع‌ترین سرعت استنتاج برای مدل‌های متن‌باز را ارائه می‌دهد. معماری سخت‌افزاری تخصصی groq عملکرد استثنایی برای برنامه‌های هوش مصنوعی بلادرنگ فراهم می‌کند.

#### مدل‌های موجود

ما 14 مدل از groq را در چندین دسته اضافه کرده‌ایم:

**مدل‌های ایمنی و تعدیل محتوا:**
- **`groq.llama-guard-4-12b`**: مدل پیشرفته تعدیل محتوا
- **`groq.llama-prompt-guard-2-22m`**: تشخیص سبک تزریق پرامپت (22 میلیون پارامتر)
- **`groq.llama-prompt-guard-2-86m`**: تشخیص پیشرفته تزریق پرامپت (86 میلیون پارامتر)

**مدل‌های زبان بزرگ:**
- **`groq.llama-4-maverick-17b-128e-instruct`**: مدل پیشرفته Llama 4 با 128 متخصص
- **`groq.llama-4-scout-17b-16e-instruct`**: مدل کارآمد Llama 4 با 16 متخصص
- **`groq.kimi-k2-instruct-0905`**: مدل دنبال‌کننده دستورالعمل Kimi K2
- **`groq.gpt-oss-120b`**: مدل بزرگ GPT متن‌باز (120 میلیارد پارامتر)
- **`groq.gpt-oss-20b`**: مدل کارآمد GPT متن‌باز (20 میلیارد پارامتر)
- **`groq.gpt-oss-safeguard-20b`**: مدل GPT با ایمنی بهبودیافته (20 میلیارد پارامتر)
- **`groq.qwen3-32b`**: مدل چندزبانه Qwen 3 (32 میلیارد پارامتر)

**مدل‌های صوتی:**
- **`groq.playai-tts`**: سنتز گفتار با کیفیت بالا
- **`groq.playai-tts-arabic`**: تبدیل متن به گفتار بهینه‌شده برای عربی
- **`groq.whisper-large-v3`**: مدل پیشرفته تشخیص گفتار
- **`groq.whisper-large-v3-turbo`**: تشخیص گفتار سریع‌تر با حفظ دقت

#### ویژگی‌های کلیدی

- **استنتاج فوق‌سریع**: سرعت استنتاج پیشرو در صنعت که توسط سخت‌افزار سفارشی groq پشتیبانی می‌شود
- **مدل‌های متن‌باز**: دسترسی به مدل‌های محبوب متن‌باز با عملکرد آماده برای تولید
- **قیمت‌گذاری رقابتی**: گزینه‌های مقرون‌به‌صرفه با پشتیبانی از کش پرامپت
- **قابلیت‌های متنوع**: از تعدیل ایمنی تا تولید متن چندزبانه و پردازش صوتی
- **آماده برای تولید**: قابلیت اطمینان و عملکرد سطح سازمانی

#### قیمت‌گذاری

| مدل | ورودی | ورودی کش‌شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| groq.llama-guard-4-12b | 0.20 دلار/1م توکن | 0.10 دلار/1م توکن | 0.20 دلار/1م توکن | - |
| groq.llama-prompt-guard-2-22m | 0.03 دلار/1م توکن | 0.015 دلار/1م توکن | 0.03 دلار/1م توکن | - |
| groq.llama-prompt-guard-2-86m | 0.04 دلار/1م توکن | 0.02 دلار/1م توکن | 0.04 دلار/1م توکن | - |
| groq.llama-4-maverick-17b-128e-instruct | 0.20 دلار/1م توکن | 0.10 دلار/1م توکن | 0.60 دلار/1م توکن | - |
| groq.llama-4-scout-17b-16e-instruct | 0.11 دلار/1م توکن | 0.055 دلار/1م توکن | 0.34 دلار/1م توکن | - |
| groq.kimi-k2-instruct-0905 | 1.00 دلار/1م توکن | 0.50 دلار/1م توکن | 0.34 دلار/1م توکن | - |
| groq.gpt-oss-120b | 0.15 دلار/1م توکن | 0.075 دلار/1م توکن | 0.75 دلار/1م توکن | - |
| groq.gpt-oss-20b | 0.075 دلار/1م توکن | 0.0375 دلار/1م توکن | 0.30 دلار/1م توکن | - |
| groq.gpt-oss-safeguard-20b | 0.075 دلار/1م توکن | 0.0375 دلار/1م توکن | 0.30 دلار/1م توکن | - |
| groq.playai-tts | 50.00 دلار/1م کاراکتر | - | - | 0.00005 دلار به ازای هر کاراکتر |
| groq.playai-tts-arabic | 50.00 دلار/1م کاراکتر | - | - | 0.00005 دلار به ازای هر کاراکتر |
| groq.qwen3-32b | 0.29 دلار/1م توکن | 0.145 دلار/1م توکن | 0.59 دلار/1م توکن | - |
| groq.whisper-large-v3 | - | - | 0.00185 دلار/1م توکن | 0.000031 دلار به ازای هر ثانیه |
| groq.whisper-large-v3-turbo | - | - | 0.000067 دلار/1م توکن | 0.00001111 دلار به ازای هر ثانیه |

#### نمونه‌های درخواست/پاسخ API

**نمونه تولید متن:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.llama-4-maverick-17b-128e-instruct",
    "messages": [
      {
        "role": "user",
        "content": "مزایای استنتاج سریع هوش مصنوعی در سیستم‌های تولیدی را توضیح بده."
      }
    ],
    "temperature": 0.7,
    "max_tokens": 1024
  }'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-abc789",
  "created": 1732147200,
  "model": "groq.llama-4-maverick-17b-128e-instruct",
  "object": "chat.completion",
  "system_fingerprint": "fp_groq_v1",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "استنتاج سریع هوش مصنوعی در سیستم‌های تولیدی مزایای کلیدی زیر را ارائه می‌دهد:\n\n1. **کاهش تاخیر**: زمان پاسخ سریع تجربه کاربری را بهبود می‌بخشد...",
        "role": "assistant",
        "tool_calls": null
      }
    }
  ],
  "usage": {
    "completion_tokens": 256,
    "prompt_tokens": 18,
    "total_tokens": 274,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "estimated_cost": {
    "unit": "0.0001572000",
    "irt": 18.01,
    "exchange_rate": 114600
  }
}
```

#### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.llama-4-maverick-17b-128e-instruct",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع Python برای محاسبه اعداد اول بنویس."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="groq.llama-4-maverick-17b-128e-instruct",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای محاسبه اعداد اول بنویس.",
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
  model: "groq.llama-4-maverick-17b-128e-instruct",
  messages: [
    {
      role: "user",
      content: "یک تابع Python برای محاسبه اعداد اول بنویس.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

#### نمونه تعدیل محتوا

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.llama-guard-4-12b",
    "messages": [
      {
        "role": "user",
        "content": "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="groq.llama-guard-4-12b",
    messages=[
        {
            "role": "user",
            "content": "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
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
  model: "groq.llama-guard-4-12b",
  messages: [
    {
      role: "user",
      content: "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## پیوندهای مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [مستندات مدل‌های groq](fa/providers/groq.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [قیمت‌گذاری API](fa/pricing.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
