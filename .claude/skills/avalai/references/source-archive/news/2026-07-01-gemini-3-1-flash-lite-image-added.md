# مدل جدید اضافه شد: Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)

**تاریخ:** ۱۴۰۵-۰۴-۱۰ / (2026-07-01)

## خلاصه

ما افزودن مدل Gemini 3.1 Flash Lite Image گوگل (`gemini-3.1-flash-lite-image`) با نام مستعار "Nano Banana 2 Lite" را اعلام می‌کنیم. این مدل متخصص کارایی در خانواده تولید تصویر Gemini است و تولید و ویرایش تصویر با تاخیر بسیار کم و مقرون‌به‌صرفه را از طریق endpoint `v1/chat/completions` ارائه می‌دهد؛ که آن را برای برنامه‌های تعاملی و بلادرنگ با حجم بالا مناسب می‌سازد.

---

## جزئیات

### Google Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)

مدل [`gemini-3.1-flash-lite-image`](fa/providers/google.md) گوگل (همچنین با نام "Nano Banana 2 Lite" شناخته می‌شود) اکنون از طریق AvalAI در دسترس است. این مدل تاخیر زیر ۲ ثانیه و هزینه‌های محاسباتی به طور قابل توجهی کاهش‌یافته را هدف قرار می‌دهد و موارد استفاده تعاملی توسعه‌دهندگان با حجم بالا و برنامه‌های مصرف‌کننده بلادرنگ را ممکن می‌سازد، در حالی که کیفیت Nano Banana را حفظ می‌کند.

**نام مدل:** `gemini-3.1-flash-lite-image`  
**نام مستعار:** Nano Banana 2 Lite

#### ویژگی‌های کلیدی

- **تاخیر زیر ۲ ثانیه**: بهینه‌سازی شده برای تاخیر بسیار کم و سرتاسری برای تکرار سریع و تعاملی
- **مقرون‌به‌صرفه در مقیاس**: تولید هزاران تصویر با کسری از هزینه مدل‌های سنگین‌تر تولید
- **تولید و ویرایش درهم‌تنیده**: پشتیبانی بومی از Text → Text + Image(s) و Image + Text → Text + Image(s)
- **ویرایش‌های محلی سریع چندنوبتی**: تعویض رنگ‌ها، ساخت استیکر و تنظیم پس‌زمینه در نوبت‌های مکالمه‌ای سریع
- **سازگاری شخصیت**: حفظ همترازی بالای شخصیت مطابق با استانداردهای اصلی Nano Banana
- **۱۴ نسبت ابعاد**: پشتیبانی از `1:1`، `3:2`، `2:3`، `3:4`، `4:3`، `4:5`، `5:4`، `9:16`، `16:9`، `21:9` و فرمت‌های استاندارد دیگر
- **بهینه‌سازی برای وضوح 1K**: مقدار `image_size` برابر `1024px` (1K) پشتیبانی می‌شود (2K و 4K پشتیبانی نمی‌شوند)
- **فراخوانی تابع و تفکر**: فراخوانی تابع و تفکر (حداقلی و بالا) پشتیبانی می‌شود
- **واترمارک SynthID + C2PA**: واترمارک همیشه‌فعال برای تصاویر تولیدشده توسط هوش مصنوعی

#### قیمت‌گذاری

| نوع | هزینه |
|-----|-------|
| ورودی متن | $0.25 به ازای هر 1M توکن |
| ورودی تصویر | $0.25 به ازای هر 1M توکن |
| ورودی کش شده | $0.05 به ازای هر 1M توکن |
| خروجی متن | $1.50 به ازای هر 1M توکن |
| خروجی تصویر (1K) | $0.0336 به ازای هر تصویر |
| خروجی تصویر (2048x2048) | $0.0672 به ازای هر تصویر |
| خروجی تصویر (4096x4096) | $0.1344 به ازای هر تصویر |

**توجه:** خروجی تصویر به قیمت $30 به ازای هر 1M توکن است. تصاویر خروجی در وضوح 1K (1024x1024px) تقریبا 1,120 توکن مصرف می‌کنند که معادل $0.0336 به ازای هر تصویر است.

#### درک خانواده Nano Banana

**Nano Banana** نام قابلیت‌های تولید تصویر بومی Gemini است. Gemini می‌تواند تصاویر را به صورت مکالمه‌ای با متن، تصاویر یا ترکیبی از هر دو تولید و پردازش کند:

- **Nano Banana 2 Lite** (`gemini-3.1-flash-lite-image`): متخصص کارایی، بهینه‌سازی شده برای تاخیر بسیار کم و تولید و ویرایش تصویر مقرون‌به‌صرفه با حجم بالا در وضوح 1K
- **Nano Banana 2** (`gemini-3.1-flash-image`): همتای پربازده Gemini 3 Pro Image، بهینه‌سازی شده برای سرعت و موارد استفاده توسعه‌دهندگان با حجم بالا با وضوح تا 4K
- **Nano Banana Pro** (`gemini-3-pro-image`): طراحی شده برای تولید دارایی‌های حرفه‌ای با استدلال پیشرفته ("تفکر") برای دستورالعمل‌های پیچیده و متن با کیفیت بالا
- **Nano Banana** (`gemini-2.5-flash-image`): طراحی شده برای سرعت و کارایی، بهینه‌سازی شده برای وظایف با حجم بالا و تاخیر کم

#### نمونه‌های درخواست/پاسخ API

**استفاده از Endpoint چت:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-lite-image",
    "messages": [
      {
        "role": "user",
        "content": "Create a photorealistic macro photograph of a colorful spider covered in water droplets on its web"
      }
    ],
    "modalities": ["image", "text"]
  }' | jq '.choices[0].message.images[0].image_url.url |= (.[0:100] + "...[TRUNCATED]")'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-abc789",
  "created": 1782000000,
  "model": "gemini-3.1-flash-lite-image",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "I've created a photorealistic macro photograph of a colorful spider covered in water droplets on its web.",
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
    "completion_tokens": 1120,
    "prompt_tokens": 24,
    "total_tokens": 1144,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 24,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0336060000",
    "irt": 3851.24,
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
    "model": "gemini-3.1-flash-lite-image",
    "messages": [
      {
        "role": "user",
        "content": "Create a modern logo for a tech company called \"AvalAI\" with clean typography and a minimalist design"
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": 'Create a modern logo for a tech company called "AvalAI" with clean typography and a minimalist design',
        }
    ],
    extra_body={"modalities": ["image", "text"]},
)

# دسترسی به تصویر تولیدشده
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
  model: "gemini-3.1-flash-lite-image",
  messages: [
    {
      role: "user",
      content: "Create a modern logo for a tech company called \"AvalAI\" with clean typography and a minimalist design",
    },
  ],
  modalities: ["image", "text"],
});

// دسترسی به تصویر تولیدشده
if (response.choices[0].message.images) {
  const images = response.choices[0].message.images;
  images.forEach((img, idx) => {
    console.log(`Image ${idx}: ${img.image_url.url.substring(0, 100)}...`);
  });
}

console.log(response.choices[0].message.content);

```

#### نمونه ویرایش تصویر

از آنجایی که Nano Banana 2 Lite از تولید و ویرایش درهم‌تنیده پشتیبانی می‌کند، می‌توانید با ارسال یک تصویر موجود در کنار یک دستورالعمل متنی، ویرایش‌های محلی سریع چندنوبتی انجام دهید:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-lite-image",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Change the background of this product photo to a soft studio gradient"
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
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Change the background of this product photo to a soft studio gradient",
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
  model: "gemini-3.1-flash-lite-image",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Change the background of this product photo to a soft studio gradient",
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

#### تنظیم نسبت ابعاد

Nano Banana 2 Lite از ۱۴ نسبت ابعاد در وضوح 1K پشتیبانی می‌کند. هنگام استفاده از endpoint سازگار با OpenAI، تنظیمات اختصاصی Gemini را از طریق `extra_body` ارسال کنید:

```python
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": "A dynamic action shot of a swimmer performing the butterfly stroke",
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {"imageConfig": {"aspectRatio": "16:9", "imageSize": "1K"}}
    },
)
```

#### نمونه SDK بومی Gemini

همچنین می‌توانید از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به این مدل با SDK رسمی گوگل استفاده کنید:

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options=types.HttpOptions(base_url="https://api.avalai.ir/v1beta"),
)

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)
response = client.models.generate_content(
    model="gemini-3.1-flash-lite-image",
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

## پیوندهای مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [تولید تصویر پیشرفته با Gemini (سری Nano Banana)](fa/examples/advanced_gemini_image_generation.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [مرجع API تولید تصویر](fa/api-reference/images.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
