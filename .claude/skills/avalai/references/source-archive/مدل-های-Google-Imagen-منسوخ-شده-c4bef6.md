# مدل‌های Google Imagen (منسوخ شده)

تمام شناسه‌های مدل Google Imagen منسوخ شده‌اند و دیگر در `data/models.json` فهرست نمی‌شوند؛ بنابراین از مثال‌های قدیمی `imagen-*` یا مسیر تصویر `:predict` در v1beta برای یکپارچه‌سازی‌های جدید AvalAI استفاده نکنید. این صفحه فقط برای کمک به مهاجرت bookmarkها و snippetهای قدیمی باقی مانده است.

## مدل‌های منسوخ شده

| مدل منسوخ شده | جایگزین |
| ---------------- | ----------- |
| `imagen-4.0-ultra-generate-001` | `gemini-3-pro-image` (نانو بنانا پرو) |
| `imagen-4.0-generate-001` | `gemini-3.1-flash-image` (نانو بنانا ۲) |
| `imagen-4.0-fast-generate-001` | `gemini-3.1-flash-image` (نانو بنانا ۲) |
| `imagen-3.0-generate-002` | `gemini-3.1-flash-lite-image` (نانو بنانا ۲ لایت) |
| `imagen-3.0-generate-001` | `gemini-3.1-flash-lite-image` (نانو بنانا ۲ لایت) |
| `imagen-3.0-fast-generate-001` | `gemini-3.1-flash-lite-image` (نانو بنانا ۲ لایت) |

## جایگزین‌های پیشنهادی

- **خانواده نانو بنانا:** برای تولید و ویرایش تصویر با گوگل از [`gemini-3.1-flash-image`، `gemini-3-pro-image` یا `gemini-3.1-flash-lite-image`](fa/examples/generate_images_with_nano_banana_series.md) از طریق `v1/chat/completions` یا نقطه پایانی بومی `:generateContent` در `v1beta` استفاده کنید. (`gemini-2.5-flash-image` در تاریخ ۲ اکتبر ۲۰۲۶ متوقف می‌شود، بنابراین برای یکپارچه‌سازی‌های جدید مدل‌های تصویری Gemini 3.x را ترجیح دهید.)
- **GPT Image:** برای تولید باکیفیت، ویرایش، متن داخل تصویر، compositing و ویرایش با mask از [`gpt-image-2`](fa/examples/generate_images_with_gpt_image.md) در `v1/images/generations` و `v1/images/edits` استفاده کنید.
- **سایر ارائه‌دهندگان:** مدل‌های FLUX (`flux.2-pro`، `flux.1-kontext-pro`)، Qwen Image و Seedream همچنان برای گردش‌کارهای مستقیم تولید تصویر در دسترس هستند.

## مثال مهاجرت

فراخوانی قدیمی API بومی Imagen:

```bash
# منسوخ شده - استفاده نکنید
curl -X POST \
  "https://api.avalai.ir/v1beta/models/imagen-4.0-fast-generate-001:predict" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"instances": [{"prompt": "A serene Japanese garden"}], "parameters": {"sampleCount": 1}}'
```

فراخوانی جدید نانو بنانا از طریق نقطه پایانی سازگار با OpenAI:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-image",
    "messages": [
      {"role": "user", "content": "Generate a serene Japanese garden with a koi pond"}
    ],
    "modalities": ["image", "text"]
  }'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini-3.1-flash-image",
    messages=[
        {"role": "user", "content": "Generate a serene Japanese garden with a koi pond"}
    ],
    modalities=["image", "text"],
)

images = response.choices[0].message.images
if images:
    print("Image URL:", images[0]["image_url"]["url"])

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.1-flash-image",
  messages: [
    { role: "user", content: "Generate a serene Japanese garden with a koi pond" },
  ],
  modalities: ["image", "text"],
});

const images = response.choices[0].message.images;
if (images?.length) {
  console.log("Image URL:", images[0].image_url.url);
}

```

برای راهنمای کامل پرامپت‌نویسی، کنترل نسبت ابعاد و اندازه تصویر و نمونه‌های ویرایش، به [راهنمای خانواده نانو بنانا](fa/examples/generate_images_with_nano_banana_series.md) و [راهنمای منسوخ‌شدن و مهاجرت مدل‌ها](fa/news/2026-09-04-model-deprecations-and-migration-guide.md) مراجعه کنید.

برای بررسی در دسترس بودن مدل‌ها، همیشه [`data/models.json`](/data/models.json) را از طریق [Models API](fa/api-reference/models.md) یا [مرورگر مدل‌ها](fa/models/model-details.md) بررسی کنید.
