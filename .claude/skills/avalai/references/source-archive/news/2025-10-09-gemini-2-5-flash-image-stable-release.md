# انتشار نسخه پایدار Gemini 2.5 Flash Image (Nano Banana)

**تاریخ:** 1404-07-17 / (2025-10-09)

## خلاصه

گوگل جمینای نسخه پایدار مدل پیشرفته تولید تصویر خود با نام **gemini-2.5-flash-image** (**Nano Banana**) را منتشر کرده است. این مدل جایگزین نسخه پیش‌نمایش شده و پایداری و عملکرد بهبود یافته‌ای را برای استفاده در محیط تولید فراهم می‌کند. نسخه پیش‌نمایش (**gemini-2.5-flash-image-preview**) در هفته‌های آینده منسوخ خواهد شد.

---

## جزئیات

### انتشار مدل پایدار

ما در دسترس بودن **gemini-2.5-flash-image**، نسخه پایدار و آماده برای تولید مدل پیشرفته تولید و ویرایش تصویر گوگل از خانواده Gemini 2.5 را اعلام می‌کنیم. این انتشار نشان‌دهنده انتقال از مرحله پیش‌نمایش به یک مدل کاملا پشتیبانی‌شده و در سطح تولید است.

### Google

- **gemini-2.5-flash-image**: مدل پایدار و پیشرفته تولید تصویر گوگل با قابلیت‌های برتر تولید و ویرایش تصویر با پشتیبانی از تبدیل متن به تصویر و تصویر به تصویر. [مستندات](fa/providers/google.md)

**ویژگی‌های کلیدی:**
- **تولید تصویر در سطح پیشرفته** - ایجاد تصاویر واقع‌گرایانه با کیفیت بالا از توصیفات متنی دقیق
- **ویرایش پیشرفته تصویر** - تبدیل تصاویر موجود با دستورالعمل‌های زبان طبیعی
- **ثبات شخصیت** - حفظ ظاهر ثابت سوژه‌ها در چندین نسل تولید
- **ترکیب چند تصویر** - ترکیب چندین تصویر ورودی در ترکیب‌بندی‌های منسجم
- **ویرایش مکالمه‌ای** - اصلاح تکراری از طریق گفتگوی طبیعی
- **پایداری تولید** - قابلیت اطمینان بهبود یافته و عملکرد ثابت برای بارهای کاری تولید
- **پنجره زمینه**: 32,768 توکن برای مدیریت مکالمات گسترده
- **خروجی دوگانه**: پشتیبانی از خروجی‌های تصویری و متنی
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions` با پارامتر modalities

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | خروجی (متن) | خروجی (تصویر) |
|-------|-------|---------------|----------------|
| gemini-2.5-flash-image | $0.30/1M توکن | $2.50/1M توکن | $30.00/1M توکن |

### مهاجرت از نسخه پیش‌نمایش

اگر در حال حاضر از **gemini-2.5-flash-image-preview** استفاده می‌کنید، توصیه می‌کنیم به مدل پایدار **gemini-2.5-flash-image** مهاجرت کنید. نسخه پیش‌نمایش به زودی منسوخ خواهد شد. مهاجرت یکپارچه است - به سادگی نام مدل را در فراخوانی‌های API خود به‌روزرسانی کنید:

```diff
- model="gemini-2.5-flash-image-preview"
+ model="gemini-2.5-flash-image"
```

تمام ویژگی‌ها و قابلیت‌ها یکسان باقی می‌مانند، با پایداری و عملکرد بهبود یافته در نسخه پایدار.

### مثال استفاده

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash-image",
    "messages": [
      {
        "role": "user",
        "content": "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند"
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر از متن
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند",
        }
    ],
    modalities=["image", "text"],
)

# تصویر در پاسخ موجود است
image_url = response.choices[0].message.images[0]["image_url"]["url"]
content = (
    response.choices[0].message.content.strip()
    if response.choices[0].message.content
    else None
)

# پردازش داده‌های تصویر برگشتی
header, base64_data = image_url.split(",", 1)
ext = header.split(";")[0].split("/")[1]

# رمزگشایی و ذخیره تصویر
image_bytes = base64.b64decode(base64_data)
filename = f"generated_image.{ext}"
with open(filename, "wb") as f:
    f.write(image_bytes)
print(f"✅ تصویر با نام {filename} ذخیره شد")

javascript=:import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تولید تصویر از متن
const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: [{
        role: "user",
        content: "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند"
    }],
    modalities: ["image", "text"],
});

// تصویر در پاسخ موجود است
const imageUrl = response.choices[0].message.images[0].image_url.url;
const content = response.choices[0].message.content ? response.choices[0].message.content.trim() : null;

// پردازش داده‌های تصویر برگشتی
const [header, base64Data] = imageUrl.split(",", 2);
const ext = header.split(";")[0].split("/")[1];

// رمزگشایی و ذخیره تصویر
const imageBytes = Buffer.from(base64Data, 'base64');
const filename = `generated_image.${ext}`;
fs.writeFileSync(filename, imageBytes);
console.log(`✅ تصویر با نام ${filename} ذخیره شد`);

```

### مثال ویرایش تصویر به تصویر

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash-image",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "این تصویر را به سبک انیمه استودیو جیبلی تبدیل کن"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/your-image.jpg"
            }
          }
        ]
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:# تبدیل تصویر به تصویر
prompt = "این تصویر را به سبک انیمه استودیو جیبلی تبدیل کن"
image_url = "https://example.com/your-image.jpg"

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)

# پردازش پاسخ مشابه متن به تصویر
image_url = response.choices[0].message.images[0]["image_url"]["url"]

javascript=:// تبدیل تصویر به تصویر
const prompt = "این تصویر را به سبک انیمه استودیو جیبلی تبدیل کن";
const imageUrl = "https://example.com/your-image.jpg";

const messages = [
    {
        role: "user",
        content: [
            { type: "text", text: prompt },
            { type: "image_url", image_url: { url: imageUrl } },
        ],
    }
];

const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: messages,
    modalities: ["image", "text"],
});

// پردازش پاسخ
const resultImageUrl = response.choices[0].message.images[0].image_url.url;

```

---

## لینک‌های مرتبط

- [راهنمای تولید و ویرایش تصاویر با Gemini 2.5 Flash](fa/examples/generate_images_with_gemini_2_5_flash.md)
- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API تصاویر](fa/api-reference/images.md)