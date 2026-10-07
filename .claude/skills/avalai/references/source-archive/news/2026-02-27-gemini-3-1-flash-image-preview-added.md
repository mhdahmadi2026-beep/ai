# مدل جدید اضافه شد: Gemini 3.1 Flash Image Preview (Nano Banana 2)

**تاریخ:** ۱۴۰۴-۱۲-۰۸ / (2026-02-27)

## خلاصه

ما افزودن مدل Gemini 3.1 Flash Image Preview گوگل (`gemini-3.1-flash-image-preview`) با نام مستعار "Nano Banana 2" را اعلام می‌کنیم. این مدل تولید تصویر با کیفیت بالا و ویرایش پیشرفته سریع‌تر را به سری Flash می‌آورد و به عنوان همتای پربازده Gemini 3 Pro Image با نسبت قیمت به عملکرد استثنایی برای موارد استفاده توسعه‌دهندگان با حجم بالا بهینه‌سازی شده است.

---

## جزئیات

### Google Gemini 3.1 Flash Image Preview (Nano Banana 2)

مدل [`gemini-3.1-flash-image-preview`](fa/providers/google.md) گوگل (همچنین با نام "Nano Banana 2" شناخته می‌شود) اکنون از طریق AvalAI در دسترس است. این مدل تولید تصویر با کیفیت بالا و قابلیت‌های ویرایش پیشرفته را با بهینه‌سازی برای سرعت و گردش‌های کاری توسعه‌دهندگان با حجم بالا ارائه می‌دهد.

**نام مدل:** `gemini-3.1-flash-image-preview`  
**نام مستعار:** Nano Banana 2

#### ویژگی‌های کلیدی

- **دانش جهانی بهبود یافته**: استفاده از دانش گسترده Gemini با پایه‌گذاری جستجوی وب برای ایجاد تصاویر بهبود یافته با مراجع دنیای واقعی
- **رندر متن پیشرفته**: ارائه رندر متن قابل اعتماد و واضح با بومی‌سازی درون تصویر با پشتیبانی از چندین زبان
- **کنترل خلاقانه بیشتر**: نورپردازی پرجنب و جوش، بافت‌های غنی‌تر، جزئیات تیزتر با سطوح تفکر قابل تنظیم
- **نسبت ابعاد بومی**: پشتیبانی از تمام نسبت‌های موجود به علاوه نسبت‌های جدید 4:1، 1:4، 8:1 و 1:8
- **وضوح جدید 512px**: بهینه‌سازی برای کارایی با حداقل تاخیر برای تکرارهای سریع
- **پیروی بهبود یافته از دستورالعمل**: پایبندی دقیق‌تر به دستورات پیچیده و چندلایه
- **پشتیبانی از وضوح**: تولید تصاویر تا وضوح 4K (4096x4096px)
- **ویرایش تصویر**: قابلیت‌های ویرایش جامع شامل ویرایش مکالمه‌ای چندنوبتی
- **پایه‌گذاری جستجوی تصویر گوگل**: تولید تصاویر بر اساس مراجع تصویر دنیای واقعی (انحصاری برای 3.1 Flash)

#### قیمت‌گذاری

| نوع | هزینه |
|-----|-------|
| ورودی متن | $0.50 به ازای هر 1M توکن |
| ورودی تصویر | $0.50 به ازای هر 1M توکن |
| ورودی کش شده | $0.25 به ازای هر 1M توکن |
| خروجی متن | $3.00 به ازای هر 1M توکن |
| خروجی تصویر (1K-2K) | $0.0672 به ازای هر تصویر |
| خروجی تصویر (2K-4K) | $0.101 به ازای هر تصویر |
| خروجی تصویر (4K) | $0.151 به ازای هر تصویر |

**توجه:** خروجی تصویر به قیمت $60 به ازای هر 1M توکن است. تصاویر خروجی از 1024x1024px (1K) تا 2048x2048px (2K) تقریبا 1120 توکن مصرف می‌کنند.

#### درک خانواده Nano Banana

**Nano Banana** نام قابلیت‌های تولید تصویر بومی Gemini است. Gemini می‌تواند تصاویر را به صورت مکالمه‌ای با متن، تصاویر یا ترکیبی از هر دو تولید و پردازش کند:

- **Nano Banana 2** (`gemini-3.1-flash-image-preview`): همتای پربازده Gemini 3 Pro Image، بهینه‌سازی شده برای سرعت و موارد استفاده توسعه‌دهندگان با حجم بالا
- **Nano Banana Pro** (`gemini-3-pro-image-preview`): طراحی شده برای تولید دارایی‌های حرفه‌ای با استدلال پیشرفته ("تفکر") برای دستورالعمل‌های پیچیده و متن با کیفیت بالا
- **Nano Banana** (`gemini-2.5-flash-image`): طراحی شده برای سرعت و کارایی، بهینه‌سازی شده برای وظایف با حجم بالا و تاخیر کم

#### نمونه‌های درخواست/پاسخ API

**استفاده از Endpoint چت:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-image-preview",
    "messages": [
      {
        "role": "user",
        "content": "یک پرتره فتورئالیستیک از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز"
      }
    ],
    "modalities": ["image", "text"]
  }' | jq '.choices[0].message.images[0].image_url.url |= (.[0:100] + "...[TRUNCATED]")'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1740642000,
  "model": "gemini-3.1-flash-image-preview",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "یک تصویر فتورئالیستیک از غذای موز نانو در محیط رستوران مجلل با تم صورت‌فلکی Gemini ایجاد کردم.",
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
    "prompt_tokens": 28,
    "total_tokens": 1178,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0695000000",
    "irt": 7968.3,
    "exchange_rate": 114600
  }
}
```

#### نمونه‌های SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-image-preview",
    "messages": [
      {
        "role": "user",
        "content": "یک لوگوی مدرن برای یک شرکت فناوری به نام \"AvalAI\" با تایپوگرافی تمیز و طراحی مینیمالیست بساز"
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-image-preview",
    messages=[
        {
            "role": "user",
            "content": 'یک لوگوی مدرن برای یک شرکت فناوری به نام "AvalAI" با تایپوگرافی تمیز و طراحی مینیمالیست بساز',
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
  model: "gemini-3.1-flash-image-preview",
  messages: [
    {
      role: "user",
      content: "یک لوگوی مدرن برای یک شرکت فناوری به نام \"AvalAI\" با تایپوگرافی تمیز و طراحی مینیمالیست بساز",
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
    "model": "gemini-3.1-flash-image-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "این تصویر را به سبک سایبرپانک با رنگ‌های نئون تبدیل کن"
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
    model="gemini-3.1-flash-image-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این تصویر را به سبک سایبرپانک با رنگ‌های نئون تبدیل کن",
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

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.1-flash-image-preview",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "این تصویر را به سبک سایبرپانک با رنگ‌های نئون تبدیل کن",
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

```

#### نمونه SDK بومی Gemini

همچنین می‌توانید از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به این مدل با SDK رسمی گوگل استفاده کنید:

```python
from google import genai
from google.genai import types
from PIL import Image

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options=types.HttpOptions(base_url="https://api.avalai.ir/v1beta"),
)

prompt = "تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز"
response = client.models.generate_content(
    model="gemini-3.1-flash-image-preview",
    contents=[prompt],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("generated_image.png")
```

---

## لینک‌های مرتبط

- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [راهنمای سری Nano Banana](fa/examples/generate_images_with_nano_banana_series.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
