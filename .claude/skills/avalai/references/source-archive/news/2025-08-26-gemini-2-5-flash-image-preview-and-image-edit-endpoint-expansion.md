# قابلیت‌های جدید تولید و ویرایش تصویر: Gemini 2.5 Flash Image Preview و گسترش پشتیبانی ویرایش تصویر

**تاریخ:** 1404-06-05 / (2025-08-26)

> **به‌روزرسانی (1404-07-17 / 2025-10-09):** مدل پیش‌نمایش با نسخه پایدار [`gemini-2.5-flash-image`](fa/news/2025-10-09-gemini-2-5-flash-image-stable-release.md) جایگزین شده است. مدل پیش‌نمایش (`gemini-2.5-flash-image-preview`) به زودی منسوخ خواهد شد. لطفا برای استفاده در محیط تولید به نسخه پایدار مهاجرت کنید.

## خلاصه

AvalAI اکنون از جدیدترین مدل پیشرفته تولید تصویر گوگل، Gemini 2.5 Flash Image Preview، همراه با قابلیت‌های گسترده ویرایش تصویر از طریق endpoint مسیر v1/images/edits برای هفت مدل دیگر شامل مدل‌های Stability AI و Imagen پشتیبانی می‌کند.

---

## جزئیات

ما دو بهبود عمده در قابلیت‌های تولید و ویرایش تصویر خود را اعلام می‌کنیم که به توسعه‌دهندگان گزینه‌های قدرتمند و انعطاف‌پذیرتری برای برنامه‌های مبتنی بر هوش مصنوعی ارائه می‌دهد.

### Google Gemini 2.5 Flash Image Preview

#### Google

- **gemini-2.5-flash-image-preview** *(منسوخ - از gemini-2.5-flash-image استفاده کنید)*: جدیدترین مدل پیشرفته تولید تصویر گوگل از خانواده Gemini 2.5، دارای قابلیت‌های برتر تولید و ویرایش تصویر با پشتیبانی از تبدیل متن به تصویر و تصویر به تصویر. [مستندات](fa/providers/google.md)

**ویژگی‌های کلیدی:**
- **محدودیت توکن ورودی/خروجی**: هر کدام 32,768 توکن
- **انواع داده پشتیبانی شده**: ورودی و خروجی تصویر و متن
- **قابلیت‌ها**: تولید تصویر، خروجی‌های ساختاریافته، کش کردن
- **برش دانش**: ژوئن 2025
- **دسترسی API**: از طریق [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1beta`](fa/news/2025-07-22-native-gemini-api-support-now-available.md) بومی در دسترس است

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر از متن
response = client.chat.completions.create(
    model="gemini-2.5-flash-image-preview",
    messages=[
        {
            "role": "user",
            "content": "تصویری فتورئالیستی از منظره کوهستانی با دریاچه‌ای که غروب خورشید را منعکس می‌کند، به سبک نقاشی منظره رمانتیک",
        }
    ],
    modalities=["image", "text"],
)

# Image is now available in the response
image_url = response.choices[0].message.images[0]["image_url"]["url"]
content = (
    response.choices[0].message.content.strip()
    if response.choices[0].message.content
    else None
)

# پردازش داده تصویر برگشت داده شده
header, base64_data = image_url.split(",", 1)
ext = header.split(";")[0].split("/")[1]

import base64

image_bytes = base64.b64decode(base64_data)
with open(f"generated_image.{ext}", "wb") as f:
    f.write(image_bytes)
print(f"✅ تصویر با نام generated_image.{ext} ذخیره شد")

# Print any text response that came with the image
if content:
    print(f"پاسخ مدل: {content}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// تولید تصویر از متن
const response = await client.chat.completions.create({
 model: "gemini-2.5-flash-image-preview",
 messages: [{
 role: "user",
 content: "تصویری فتورئالیستی از منظره کوهستانی با دریاچه‌ای که غروب خورشید را منعکس می‌کند، به سبک نقاشی منظره رمانتیک",
 }],
 modalities: ["image", "text"],
});

// Image is now available in the response
const imageUrl = response.choices[0].message.images[0].image_url.url;
const content = response.choices[0].message.content ? response.choices[0].message.content.trim() : null;

// پردازش داده تصویر برگشت داده شده
const [header, base64Data] = imageUrl.split(",", 2);
const ext = header.split(";")[0].split("/")[1];

const imageBytes = Buffer.from(base64Data, 'base64');
require('fs').writeFileSync(`generated_image.${ext}`, imageBytes);
console.log(`✅ تصویر با نام generated_image.${ext} ذخیره شد`);

// Print any text response that came with the image
if (content) {
 console.log(`پاسخ مدل: ${content}`);
}

```

### گسترش پشتیبانی نقطه پایانی وبرایش تصویر

ما به طور قابل توجهی نقظه پایانی [`v1/images/edits`](fa/api-reference/images.md) را برای پشتیبانی از هفت مدل قدرتمند دیگر برای قابلیت‌های ویرایش تصویر گسترش داده‌ایم:

#### Stability AI

- **stability.sd3-large-v1:0**: مدل پیشرفته Stable Diffusion 3 برای ویرایش تصویر با کیفیت بالا
- **stability.sd3-5-large-v1:0**: جدیدترین مدل Stable Diffusion 3.5 با قابلیت‌های ویرایش بهبود یافته

#### Google

- **imagen-3.0-generate-001**: مدل Imagen 3.0 گوگل برای ویرایش و تولید پیچیده تصویر

```language-selector
python=:import requests
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# ویرایش تصویر موجود
with open("input_image.png", "rb") as image_file:
    response = client.images.edit(
        model="stability.sd3-5-large-v1:0",
        image=image_file,
        prompt="رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
        size="1024x1024",
        n=1,
        response_format="url",  # or b64_json
    )

# ذخیره تصویر ویرایش شده
edited_image_url = response.data[0].url
edited_image = requests.get(edited_image_url)
with open("edited_image.png", "wb") as f:
    f.write(edited_image.content)

print("✅ تصویر ویرایش شد و با نام edited_image.png ذخیره شد")

javascript=:import fs from 'fs';
import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// ویرایش تصویر موجود
const imageFile = fs.createReadStream("input_image.png");
const response = await client.images.edit({
 model: "stability.sd3-5-large-v1:0",
 image: imageFile,
 prompt: "رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
 size: "1024x1024",
 n: 1,
 response_format: "url", // or b64_json
});

// ذخیره تصویر ویرایش شده
const editedImageUrl = response.data[0].url;
const imageResponse = await fetch(editedImageUrl);
const imageBuffer = await imageResponse.arrayBuffer();
fs.writeFileSync("edited_image.png", Buffer.from(imageBuffer));

console.log("✅ تصویر ویرایش شد و با نام edited_image.png ذخیره شد");

```

---

## لینک‌های مرتبط

- [راهنمای تولید و ویرایش تصاویر با Gemini 2.5 Flash Image Preview](fa/examples/generate_images_with_gemini_2_5_flash.md)
- [مستندات مدل Gemini 2.5 Flash Image Preview](fa/models/gemini-2.5-flash-image-preview.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API Chat Completions](fa/api-reference/chat.md)
- [پشتیبانی بومی API Gemini](fa/news/2025-07-22-native-gemini-api-support-now-available.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
