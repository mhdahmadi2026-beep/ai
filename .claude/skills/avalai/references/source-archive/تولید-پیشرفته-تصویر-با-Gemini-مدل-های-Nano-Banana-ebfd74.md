# تولید پیشرفته تصویر با Gemini (مدل‌های Nano Banana)

## مقدمه

این راهنمای جامع قابلیت‌های پیشرفته تولید و ویرایش تصویر با استفاده از مدل‌های تصویری Gemini گوگل از طریق AvalAI را پوشش می‌دهد. شما یاد خواهید گرفت که چگونه از **Gemini 2.5 Flash Image (Nano Banana)** و **Gemini 3 Pro Image Preview (Nano Banana Pro)** برای تولید و ویرایش تصاویر با کیفیت حرفه‌ای استفاده کنید.

> **منبع مرجع**: این راهنما بر اساس [مستندات رسمی تولید تصویر Google Gemini](https://ai.google.dev/gemini-api/docs/image-generation) تهیه شده است.

> **💡 مزیت AvalAI**: از `https://api.avalai.ir` به جای `https://generativelanguage.googleapis.com` با کلید API AvalAI خود استفاده کنید برای سازگاری ۱۰۰٪ با API بومی Gemini و SDK‌های گوگل.

> **نکته مهم**: برای بهترین نتایج، توصیه می‌شود از پرامپت‌های انگلیسی استفاده کنید زیرا مدل‌های تولید تصویر معمولا برای زبان انگلیسی بهینه‌سازی شده‌اند.

## مقایسه مدل‌ها

| ویژگی | Gemini 2.5 Flash Image (Nano Banana) | Gemini 3 Pro Image Preview (Nano Banana Pro) |
|---------|--------------------------------------|---------------------------------------------|
| **بهترین برای** | سرعت و کارایی، وظایف با حجم بالا | تولید دارایی‌های حرفه‌ای، وظایف پیچیده |
| **حداکثر رزولوشن** | 1024px (1K) | تا 4K (4096px) |
| **تصاویر ورودی** | تا ۳ تصویر | تا ۱۴ تصویر (۵ با کیفیت بالا، ۱۴ کل) |
| **Google Search Grounding** | ❌ | ✅ |
| **فرآیند تفکر** | ❌ | ✅ (به صورت پیش‌فرض فعال) |
| **نسبت‌های تصویر** | 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 | مشابه |
| **گزینه‌های اندازه تصویر** | فقط پیش‌فرض | 1K, 2K, 4K |

## دو روش دسترسی به مدل‌های تصویری Gemini

AvalAI دو روش برای دسترسی به مدل‌های تصویری Gemini پشتیبانی می‌کند:

### روش ۱: API بومی Gemini (v1beta) - توصیه شده

استفاده از API بومی Gemini از طریق AvalAI سازگاری ۱۰۰٪ با SDK‌های رسمی گوگل و مستندات آن را فراهم می‌کند. فقط کافی است URL پایه را به `https://api.avalai.ir` تغییر دهید و از کلید API AvalAI خود استفاده کنید.

### روش ۲: API سازگار با OpenAI (v1/chat/completions)

برای کاربرانی که قبلا با SDK OpenAI آشنا هستند، می‌توانید از endpoint سازگار با OpenAI با پارامترهای خاص از طریق `extra_body` استفاده کنید.

---

## API بومی Gemini (توصیه شده)

### تولید پایه تصویر از متن

تولید تصاویر از دستورات متنی با استفاده از API بومی Gemini:

```language-selector
python=:from google import genai
from google.genai import types

# راه‌اندازی کلاینت با endpoint AvalAI
client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

prompt = (
    "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"
)

# تولید تصویر با gemini-2.5-flash-image
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt],
)

# پردازش پاسخ
for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        image = part.as_image()
        image.save("nano_banana_dish.png")
        print("✅ تصویر ذخیره شد به عنوان nano_banana_dish.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

// راه‌اندازی کلاینت با endpoint AvalAI
const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const prompt = "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme";

const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image",
    contents: prompt,
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
        console.log(part.text);
    } else if (part.inlineData) {
        const imageData = part.inlineData.data;
        const buffer = Buffer.from(imageData, "base64");
        fs.writeFileSync("nano_banana_dish.png", buffer);
        console.log("✅ تصویر ذخیره شد به عنوان nano_banana_dish.png");
    }
}

go=:package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
	"log"
	"os"
)

func main() {
	ctx := context.Background()

	// کلاینت به صورت خودکار از AvalAI استفاده می‌کند وقتی پیکربندی شده باشد
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  os.Getenv("AVALAI_API_KEY"),
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash-image",
		genai.Text("Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"),
	)

	for _, part := range result.Candidates[0].Content.Parts {
		if part.Text != "" {
			fmt.Println(part.Text)
		} else if part.InlineData != nil {
			imageBytes := part.InlineData.Data
			_ = os.WriteFile("nano_banana_dish.png", imageBytes, 0644)
			fmt.Println("✅ تصویر ذخیره شد به عنوان nano_banana_dish.png")
		}
	}
}

bash=:curl -s -X POST \
  "https://api.avalai.ir/v1beta/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {"text": "Create a picture of a nano banana dish in a fancy restaurant with a Gemini theme"}
      ]
    }]
  }' \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode >nano_banana_dish.png

echo "✅ تصویر ذخیره شد به عنوان nano_banana_dish.png"

```

**نمونه خروجی:**

![تصویر تولید شده با هوش مصنوعی از غذای nano banana](https://ai.google.dev/static/gemini-api/docs/images/nano-banana.png)

*تصویر تولید شده با هوش مصنوعی از غذای nano banana در رستوران با تم Gemini*

---

### ویرایش تصویر (متن و تصویر به تصویر)

ویرایش تصاویر موجود با استفاده از دستورات متنی:

```language-selector
python=:from google import genai
from PIL import Image

# راه‌اندازی کلاینت با endpoint AvalAI
client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

prompt = "Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation"

# بارگذاری تصویر ورودی
image = Image.open("/path/to/cat_image.png")

# تولید تصویر ویرایش شده
response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[prompt, image],
)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif part.inline_data is not None:
        result_image = part.as_image()
        result_image.save("cat_nano_banana.png")
        print("✅ تصویر ویرایش شده ذخیره شد به عنوان cat_nano_banana.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const prompt = "Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation";

// خواندن تصویر به صورت base64
const imageData = fs.readFileSync("/path/to/cat_image.png").toString("base64");

const response = await ai.models.generateContent({
    model: "gemini-2.5-flash-image",
    contents: [{
        role: "user",
        parts: [
            { text: prompt },
            {
                inlineData: {
                    mimeType: "image/png",
                    data: imageData
                }
            }
        ]
    }]
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
        console.log(part.text);
    } else if (part.inlineData) {
        const buffer = Buffer.from(part.inlineData.data, "base64");
        fs.writeFileSync("cat_nano_banana.png", buffer);
        console.log("✅ تصویر ویرایش شده ذخیره شد به عنوان cat_nano_banana.png");
    }
}

bash=:IMG_PATH=/path/to/cat_image.png

if [[ "$(base64 --version 2>&1)" == *"FreeBSD"* ]]; then
  B64FLAGS="--input"
else
  B64FLAGS="-w0"
fi

IMG_BASE64=$(base64 "$B64FLAGS" "$IMG_PATH" 2>&1)

curl -X POST \
  "https://api.avalai.ir/v1beta/models/gemini-2.5-flash-image:generateContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d "{
    \"contents\": [{
      \"parts\":[
        {\"text\": \"Create a picture of my cat eating a nano-banana in a fancy restaurant under the Gemini constellation\"},
        {
          \"inline_data\": {
            \"mime_type\":\"image/png\",
            \"data\": \"$IMG_BASE64\"
          }
        }
      ]
    }]
  }" \
  | grep -o '"data": "[^"]*"' \
  | cut -d'"' -f4 \
  | base64 --decode >cat_nano_banana.png

echo "✅ Edited image saved as cat_nano_banana.png"

```

**نمونه خروجی:**

![تصویر تولید شده با هوش مصنوعی از گربه در حال خوردن nano banana](https://ai.google.dev/static/gemini-api/docs/images/cat-banana.png)

*تصویر تولید شده با هوش مصنوعی از گربه در حال خوردن nano banana*

---

### ویرایش مکالمه‌ای چند نوبتی

استفاده از حالت چت برای بهبود تکراری تصویر:

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

# ایجاد یک جلسه چت با تولید تصویر فعال
chat = client.chats.create(
    model="gemini-3-pro-image",
    config=types.GenerateContentConfig(
        response_modalities=["TEXT", "IMAGE"],
        tools=[{"google_search": {}}],  # Enable Google Search grounding
    ),
)

# پیام اول: تولید اینفوگرافیک اولیه
message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food. Show the 'ingredients' (sunlight, water, CO2) and the 'finished dish' (sugar/energy). The style should be like a page from a colorful kids' cookbook, suitable for a 4th grader."

response = chat.send_message(message)

for part in response.parts:
    if part.text is not None:
        print(part.text)
    elif image := part.as_image():
        image.save("photosynthesis_english.png")
        print("✅ اینفوگرافیک ذخیره شد به عنوان photosynthesis_english.png")

# پیام دوم: ترجمه اینفوگرافیک
message2 = "Update this infographic to be in Spanish. Do not change any other elements of the image."

response2 = chat.send_message(
    message2,
    config=types.GenerateContentConfig(
        image_config=types.ImageConfig(
            aspect_ratio="16:9", image_size="2K"  # Use 2K resolution
        ),
    ),
)

for part in response2.parts:
    if part.text is not None:
        print(part.text)
    elif image := part.as_image():
        image.save("photosynthesis_spanish.png")
        print("✅ اینفوگرافیک اسپانیایی ذخیره شد به عنوان photosynthesis_spanish.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

// ایجاد جلسه چت
const chat = ai.chats.create({
    model: "gemini-3-pro-image",
    config: {
        responseModalities: ['TEXT', 'IMAGE'],
        tools: [{googleSearch: {}}],
    },
});

// پیام اول
const message = "Create a vibrant infographic that explains photosynthesis as if it were a recipe for a plant's favorite food.";

let response = await chat.sendMessage({message});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
        console.log(part.text);
    } else if (part.inlineData) {
        const buffer = Buffer.from(part.inlineData.data, "base64");
        fs.writeFileSync("photosynthesis_english.png", buffer);
        console.log("✅ اینفوگرافیک ذخیره شد به عنوان photosynthesis_english.png");
    }
}

// پیام دوم - ترجمه به اسپانیایی با رزولوشن 2K
const message2 = "Update this infographic to be in Spanish. Do not change any other elements.";

response = await chat.sendMessage({
    message: message2,
    config: {
        responseModalities: ['TEXT', 'IMAGE'],
        imageConfig: {
            aspectRatio: '16:9',
            imageSize: '2K',
        },
        tools: [{googleSearch: {}}],
    },
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) {
        console.log(part.text);
    } else if (part.inlineData) {
        const buffer = Buffer.from(part.inlineData.data, "base64");
        fs.writeFileSync("photosynthesis_spanish.png", buffer);
        console.log("✅ اینفوگرافیک اسپانیایی ذخیره شد به عنوان photosynthesis_spanish.png");
    }
}

```

**نمونه خروجی‌ها:**

| نسخه انگلیسی | نسخه اسپانیایی |
|-------------|---------------|
| ![اینفوگرافیک فتوسنتز به انگلیسی](https://ai.google.dev/static/gemini-api/docs/images/infographic-eng.png) | ![اینفوگرافیک فتوسنتز به اسپانیایی](https://ai.google.dev/static/gemini-api/docs/images/infographic-spanish.png) |

---

### Gemini 3 Pro: خروجی با رزولوشن بالا (تا 4K)

Gemini 3 Pro Image Preview از تولید تصاویر با رزولوشن تا 4K پشتیبانی می‌کند:

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_image(
    model="gemini-3-pro-image",
    prompt="A highly detailed map of a fantasy world, 4k resolution",
    config=types.GenerateImageConfig(
        aspect_ratio="16:9", image_size="4K"  # درخواست رزولوشن 4K
    ),
)

if response.image:
    response.image.save("fantasy_map_4k.png")
    print("✅ تصویر 4K ذخیره شد به عنوان fantasy_map_4k.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const model = ai.getGenerativeModel({ model: "gemini-3-pro-image" });

// برای مدل‌های تولید تصویر خالص، از متد مناسب استفاده کنید
// یا پیکربندی را از طریق generateContent ارسال کنید اگر نسخه SDK پشتیبانی می‌کند.
// در اینجا الگوی تولید تصویر آمده است:

const result = await model.generateImage({
  prompt: "A highly detailed map of a fantasy world, 4k resolution",
  config: {
    aspectRatio: "16:9",
    imageSize: "4K",
  }
});

if (result.image) {
    const buffer = Buffer.from(result.image.data, "base64");
    fs.writeFileSync("fantasy_map_4k.png", buffer);
    console.log("✅ تصویر 4K ذخیره شد به عنوان fantasy_map_4k.png");
}

```

### استفاده سازگار با OpenAI (Gemini 3 Pro)

همچنین می‌توانید از SDK استاندارد OpenAI برای دسترسی به قابلیت‌های تولید تصویر Gemini 3 Pro از طریق AvalAI استفاده کنید.

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="gemini-3-pro-image",
    prompt="A futuristic city skyline at night with neon lights, 4k, hyper-realistic",
    size="1024x1024",  # پارامتر اندازه استاندارد
    quality="hd",  # اشاره به کیفیت بالاتر
    n=1,
)

print(response.data[0].url)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.images.generate({
    model: "gemini-3-pro-image",
    prompt: "A futuristic city skyline at night with neon lights, 4k, hyper-realistic",
    size: "1024x1024",
    quality: "hd",
    n: 1,
});

console.log(response.data[0].url);

```

---

## Gemini 2.5 Flash Image (Nano Banana)

Gemini 2.5 Flash Image (که قبلا با نام Nano Banana شناخته می‌شد) یک مدل بسیار کارآمد است که برای سرعت و سنتز تصویر با کیفیت بالا بهینه‌سازی شده است. این مدل در پیروی از دستورات پیچیده عالی عمل می‌کند و می‌تواند برای تولید و ویرایش استفاده شود.

### تولید پیشرفته با نسبت‌های تصویر

Gemini 2.5 Flash Image از نسبت‌های تصویر مختلف به صورت بومی پشتیبانی می‌کند.

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="YOUR_AVALAI_API_KEY", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_image(
    model="gemini-2.5-flash-image",
    prompt="A cinematic wide shot of a desert landscape",
    config=types.GenerateImageConfig(
        aspect_ratio="16:9",
        person_generation="allow_adult",  # گزینه‌ها: dont_allow, allow_adult, allow_all
        safety_filter_level="block_only_high",
    ),
)

if response.image:
    response.image.save("desert_cinematic.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const model = ai.getGenerativeModel({ model: "gemini-2.5-flash-image" });

const result = await model.generateImage({
  prompt: "A cinematic wide shot of a desert landscape",
  config: {
    aspectRatio: "16:9",
    personGeneration: "allow_adult",
    safetyFilterLevel: "block_only_high"
  }
});

if (result.image) {
    const buffer = Buffer.from(result.image.data, "base64");
    fs.writeFileSync("desert_cinematic.png", buffer);
}

```

### استفاده سازگار با OpenAI (Gemini 2.5 Flash Image)

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="gemini-2.5-flash-image",
    prompt="A cute robot gardener watering plants, digital art style",
    size="1024x1024",
    n=1,
)

print(response.data[0].url)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.images.generate({
    model: "gemini-2.5-flash-image",
    prompt: "A cute robot gardener watering plants, digital art style",
    size: "1024x1024",
    n: 1,
});

console.log(response.data[0].url);

```

## مقایسه: Gemini 3 Pro در مقابل Gemini 2.5 Flash Image

| ویژگی | Gemini 3 Pro Image Preview | Gemini 2.5 Flash Image (Nano Banana) |
| :--- | :--- | :--- |
| **نقاط قوت** | بالاترین کیفیت، پیروی از دستورات پیچیده، رندر متن | سرعت، کارایی، سبک‌های ثابت |
| **حداکثر رزولوشن** | تا 4K (upscale بومی) | رزولوشن بالای استاندارد |
| **ایده‌آل برای** | تصاویر بازاریابی، صحنه‌های پیچیده، تایپوگرافی | نمونه‌سازی سریع، محتوای شبکه‌های اجتماعی، تصویرسازی |
| **در دسترس بودن** | پیش‌نمایش (پیشرفته) | پایدار (آماده تولید) |

## بهترین شیوه‌ها برای تولید پیشرفته

1.  **مهندسی پرامپت**: هر دو مدل از پرامپت‌های توصیفی بهره می‌برند. نورپردازی، سبک (مثل "نقاشی رنگ روغن"، "واقع‌گرایانه") و زاویه دوربین را ذکر کنید.
2.  **پرامپت‌های منفی**: در حالی که در مثال‌های ساده به صراحت نشان داده نشده، اغلب می‌توانید مدل را با مشخص کردن آنچه *نمی‌خواهید* در توضیح پرامپت راهنمایی کنید (مثل "بدون تاری"، "بدون اعوجاج").
3.  **نسبت تصویر**: نسبت تصویر را با موضوع خود تطبیق دهید. از `16:9` برای مناظر و `9:16` برای پرتره‌ها (مثل تصاویر پس‌زمینه گوشی).
4.  **تنظیمات ایمنی**: اگر جریان کاری خلاقانه شما نیاز دارد، تنظیمات ایمنی را تنظیم کنید (مثلا برهنگی هنری یا زمینه‌های پزشکی خاص)، با احترام به پارامترهای `person_generation` و `safety_filter_level` در جایی که قابل اجرا است.

---

## ویرایش پیشرفته تصویر با Gemini 2.5 Flash Image

Gemini 2.5 Flash Image در ویرایش تصاویر موجود بر اساس دستورالعمل‌های زبان طبیعی عالی عمل می‌کند. در اینجا نحوه استفاده از قابلیت‌های ویرایش آن آورده شده است.

### ویرایش پایه تصویر (SDK بومی)

```language-selector
python=:from google import genai
from google.genai import types
from PIL import Image

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

# بارگذاری تصویر
source_image = Image.open("my_photo.jpg")

response = client.models.generate_content(
    model="gemini-2.5-flash-image",
    contents=[
        types.Part.from_image(image=source_image),
        "Change the background to a sunset beach scene while keeping the subject intact",
    ],
    config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
)

for part in response.candidates[0].content.parts:
    if part.text:
        print(part.text)
    elif part.inline_data:
        # ذخیره تصویر ویرایش شده
        image_bytes = part.inline_data.data
        with open("edited_photo.png", "wb") as f:
            f.write(image_bytes)
        print("✅ تصویر ویرایش شده ذخیره شد به عنوان edited_photo.png")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const model = ai.getGenerativeModel({ model: "gemini-2.5-flash-image" });

// خواندن تصویر به صورت base64
const imageData = fs.readFileSync("my_photo.jpg").toString("base64");

const result = await model.generateContent({
    contents: [{
        role: "user",
        parts: [
            {
                inlineData: {
                    mimeType: "image/jpeg",
                    data: imageData
                }
            },
            { text: "Change the background to a sunset beach scene while keeping the subject intact" }
        ]
    }],
    generationConfig: {
        responseModalities: ["TEXT", "IMAGE"]
    }
});

for (const part of result.response.candidates[0].content.parts) {
    if (part.text) {
        console.log(part.text);
    } else if (part.inlineData) {
        const buffer = Buffer.from(part.inlineData.data, "base64");
        fs.writeFileSync("edited_photo.png", buffer);
        console.log("✅ تصویر ویرایش شده ذخیره شد به عنوان edited_photo.png");
    }
}

```

### ویرایش تصویر از طریق API سازگار با OpenAI

```language-selector
python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# خواندن و انکود کردن تصویر
with open("my_photo.jpg", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                },
                {
                    "type": "text",
                    "text": "Change the background to a sunset beach scene while keeping the subject intact",
                },
            ],
        }
    ],
    modalities=["image", "text"],
)

# دسترسی به تصویر ویرایش شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر ویرایش شده: {image_url}")

javascript=:import OpenAI from "openai";
import * as fs from "node:fs";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// خواندن و انکود کردن تصویر
const imageData = fs.readFileSync("my_photo.jpg").toString("base64");

const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "image_url",
                    image_url: {
                        url: `data:image/jpeg;base64,${imageData}`
                    }
                },
                {
                    type: "text",
                    text: "Change the background to a sunset beach scene while keeping the subject intact"
                }
            ]
        }
    ],
    modalities: ["image", "text"]
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر ویرایش شده: ${imageUrl}`);
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### استفاده از پارامترهای بومی Gemini از طریق SDK OpenAI (extra_body)

هنگام استفاده از SDK OpenAI با مدل‌های Nano Banana، می‌توانید پارامترهای بومی Gemini مانند `aspectRatio` و `imageSize` را از طریق پارامتر `extra_body` ارسال کنید. این به شما امکان می‌دهد از ویژگی‌های اختصاصی Gemini در حین استفاده از رابط آشنای SDK OpenAI بهره‌مند شوید.

**پارامترهای پشتیبانی شده `imageConfig`:**

| پارامتر | نوع | توضیحات | مقادیر پشتیبانی شده | مدل‌های پشتیبانی شده |
|---------|-----|---------|---------------------|---------------------|
| `aspectRatio` | string | نسبت ابعاد تصویر | "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9" | `gemini-2.5-flash-image`, `gemini-3.1-flash-image`, `gemini-3-pro-image` |
| `imageSize` | string | اندازه تصویر خروجی | "1K", "2K", "4K" | `gemini-3.1-flash-image`, `gemini-3-pro-image` |

#### Gemini 2.5 Flash Image (Nano Banana) با نسبت ابعاد

```language-selector
python=:from openai import OpenAI
import base64

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# تولید تصویر با نسبت ابعاد سفارشی
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a sunset beach scene",
                },
            ],
        }
    ],
    modalities=["image", "text"],
    extra_body={"generationConfig": {"imageConfig": {"aspectRatio": "16:9"}}},
)

# دسترسی به تصویر تولید شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر تولید شده: {image_url}")

javascript=:import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// تولید تصویر با نسبت ابعاد سفارشی
const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "text",
                    text: "Generate a sunset beach scene"
                }
            ]
        }
    ],
    modalities: ["image", "text"],
    extra_body: {
        generationConfig: {
            imageConfig: {
                aspectRatio: "16:9"
            }
        }
    }
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر تولید شده: ${imageUrl}`);
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### Gemini 3 Pro Image Preview (Nano Banana Pro) با نسبت ابعاد و اندازه تصویر

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# تولید تصویر 4K با نسبت ابعاد سفارشی
response = client.chat.completions.create(
    model="gemini-3-pro-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a sunset beach scene",
                },
            ],
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "4k",  # توسط gemini-3.1-flash-image و gemini-3-pro-image پشتیبانی می‌شود
            }
        }
    },
)

# دسترسی به تصویر تولید شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر 4K تولید شده: {image_url}")

javascript=:import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// تولید تصویر 4K با نسبت ابعاد سفارشی
const response = await client.chat.completions.create({
    model: "gemini-3-pro-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "text",
                    text: "Generate a sunset beach scene"
                }
            ]
        }
    ],
    modalities: ["image", "text"],
    extra_body: {
        generationConfig: {
            imageConfig: {
                aspectRatio: "16:9",
                imageSize: "4k"  // توسط gemini-3.1-flash-image و gemini-3-pro-image پشتیبانی می‌شود
            }
        }
    }
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر 4K تولید شده: ${imageUrl}`);
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### ویرایش تصویر با نسبت ابعاد

همچنین می‌توانید هنگام ویرایش تصاویر از پارامترهای `extra_body` استفاده کنید:

```language-selector
python=:from openai import OpenAI
import base64

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# خواندن و انکود کردن تصویر
with open("my_photo.jpg", "rb") as f:
    image_base64 = base64.b64encode(f.read()).decode("utf-8")

# ویرایش تصویر با نسبت ابعاد سفارشی
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{image_base64}"},
                },
                {
                    "type": "text",
                    "text": "Transform this image into a cinematic widescreen format with dramatic lighting",
                },
            ],
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {
            "imageConfig": {"aspectRatio": "21:9"}  # نسبت سینمایی فوق عریض
        }
    },
)

# دسترسی به تصویر ویرایش شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر ویرایش شده: {image_url}")

javascript=:import OpenAI from "openai";
import * as fs from "node:fs";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// خواندن و انکود کردن تصویر
const imageData = fs.readFileSync("my_photo.jpg").toString("base64");

// ویرایش تصویر با نسبت ابعاد سفارشی
const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "image_url",
                    image_url: {
                        url: `data:image/jpeg;base64,${imageData}`
                    }
                },
                {
                    type: "text",
                    text: "Transform this image into a cinematic widescreen format with dramatic lighting"
                }
            ]
        }
    ],
    modalities: ["image", "text"],
    extra_body: {
        generationConfig: {
            imageConfig: {
                aspectRatio: "21:9"  // نسبت سینمایی فوق عریض
            }
        }
    }
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر ویرایش شده: ${imageUrl}`);
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای اطلاعات بیشتر درباره پارامترهای اختصاصی ارائه‌دهنده، به [راهنمای پارامترهای اختصاصی ارائه‌دهنده](/fa/guides/provider-specific-params.md) مراجعه کنید.

---

## مکالمات تصویری چند مرحله‌ای

هم Gemini 3 Pro و هم Gemini 2.5 Flash Image از بهبود تکراری تصویر از طریق مکالمه پشتیبانی می‌کنند. این قابلیت برای جریان‌های کاری خلاقانه بسیار قدرتمند است.

### مثال بهبود تکراری

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="YOUR_AVALAI_API_KEY", http_options={"base_url": "https://api.avalai.ir"}
)

chat = client.chats.create(
    model="gemini-2.5-flash-image",
    config=types.GenerateContentConfig(response_modalities=["TEXT", "IMAGE"]),
)

# نوبت اول: تولید مفهوم اولیه
response1 = chat.send_message(
    "Create a logo for a coffee shop called 'Morning Brew'. Use warm colors and a minimalist style."
)

for part in response1.parts:
    if part.text:
        print("Model:", part.text)
    elif image := part.as_image():
        image.save("logo_v1.png")
        print("✅ Logo v1 saved")

# نوبت دوم: بهبود بر اساس بازخورد
response2 = chat.send_message(
    "I like it! Can you make the text more prominent and add a small steam effect above the cup?"
)

for part in response2.parts:
    if part.text:
        print("Model:", part.text)
    elif image := part.as_image():
        image.save("logo_v2.png")
        print("✅ Logo v2 saved")

# نوبت سوم: تنظیمات نهایی
response3 = chat.send_message(
    "Perfect! Now create a version with a dark background for use on light surfaces."
)

for part in response3.parts:
    if part.text:
        print("Model:", part.text)
    elif image := part.as_image():
        image.save("logo_v3_dark.png")
        print("✅ Logo v3 (dark) saved")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

const chat = ai.chats.create({
    model: "gemini-2.5-flash-image",
    config: {
        responseModalities: ["TEXT", "IMAGE"]
    }
});

// نوبت اول
let response = await chat.sendMessage({ 
    message: "Create a logo for a coffee shop called 'Morning Brew'. Use warm colors and a minimalist style."
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) console.log("Model:", part.text);
    else if (part.inlineData) {
        fs.writeFileSync("logo_v1.png", Buffer.from(part.inlineData.data, "base64"));
        console.log("✅ Logo v1 saved");
    }
}

// نوبت دوم
response = await chat.sendMessage({ 
    message: "I like it! Can you make the text more prominent and add a small steam effect above the cup?"
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) console.log("Model:", part.text);
    else if (part.inlineData) {
        fs.writeFileSync("logo_v2.png", Buffer.from(part.inlineData.data, "base64"));
        console.log("✅ Logo v2 saved");
    }
}

// نوبت سوم
response = await chat.sendMessage({ 
    message: "Perfect! Now create a version with a dark background for use on light surfaces."
});

for (const part of response.candidates[0].content.parts) {
    if (part.text) console.log("Model:", part.text);
    else if (part.inlineData) {
        fs.writeFileSync("logo_v3_dark.png", Buffer.from(part.inlineData.data, "base64"));
        console.log("✅ Logo v3 (dark) saved");
    }
}

```

---

## مدیریت خطا و ایمنی

هنگام کار با تولید تصویر، مدیریت صحیح خطاها ضروری است:

```language-selector
python=:from google import genai
from google.genai import types
from google.api_core import exceptions

client = genai.Client(
    api_key="YOUR_AVALAI_API_KEY", http_options={"base_url": "https://api.avalai.ir"}
)

try:
    response = client.models.generate_image(
        model="gemini-2.5-flash-image",
        prompt="Your prompt here",
        config=types.GenerateImageConfig(safety_filter_level="block_medium_and_above"),
    )

    if response.image:
        response.image.save("output.png")
    else:
        # بررسی بلوک‌های ایمنی
        if response.prompt_feedback:
            print(f"Prompt blocked: {response.prompt_feedback}")
        else:
            print("No image generated. Try a different prompt.")

except exceptions.InvalidArgument as e:
    print(f"Invalid request: {e}")
except exceptions.ResourceExhausted as e:
    print(f"Rate limited. Please wait and retry: {e}")
except Exception as e:
    print(f"An error occurred: {e}")

javascript=:import { GoogleGenAI } from "@google/genai";
import * as fs from "node:fs";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: { baseURL: "https://api.avalai.ir" }
});

try {
    const model = ai.getGenerativeModel({ model: "gemini-2.5-flash-image" });
    
    const result = await model.generateImage({
        prompt: "Your prompt here",
        config: {
            safetyFilterLevel: "block_medium_and_above"
        }
    });
    
    if (result.image) {
        fs.writeFileSync("output.png", Buffer.from(result.image.data, "base64"));
    } else if (result.promptFeedback) {
        console.log(`Prompt blocked: ${JSON.stringify(result.promptFeedback)}`);
    } else {
        console.log("No image generated. Try a different prompt.");
    }
} catch (error) {
    if (error.status === 400) {
        console.log(`Invalid request: ${error.message}`);
    } else if (error.status === 429) {
        console.log(`Rate limited. Please wait and retry.`);
    } else {
        console.log(`An error occurred: ${error.message}`);
    }
}

```

---

## نتیجه‌گیری

AvalAI دسترسی یکپارچه به پیشرفته‌ترین مدل‌های تولید تصویر گوگل را فراهم می‌کند:

- **Gemini 3 Pro Image Preview**: برای خروجی‌های با بالاترین کیفیت، صحنه‌های پیچیده و رزولوشن تا 4K
- **Gemini 2.5 Flash Image (Nano Banana)**: برای تولید و ویرایش سریع و آماده تولید تصویر

هر دو مدل پشتیبانی می‌کنند از:
- SDK بومی Google AI (endpoint v1beta) با دسترسی کامل به ویژگی‌ها
- API سازگار با OpenAI برای ادغام آسان با کدهای موجود
- مکالمات چند مرحله‌ای برای بهبود تکراری
- کنترل‌های ایمنی پیشرفته و پیکربندی نسبت تصویر

### گام‌های بعدی

- [ویرایش تصویر با Stability AI](/fa/examples/stability_ai_image_editing.md) را برای جریان‌های کاری ویرایش تخصصی بررسی کنید
- درباره [تولید ویدیو با Veo](/fa/guides/generate-videos-using-veo.md) برای محتوای متحرک بیاموزید
- [صفحه مدل‌ها](/fa/providers/gemini.md) را برای لیست کامل مدل‌های موجود و قابلیت‌های آن‌ها بررسی کنید

---

*برای سوالات یا پشتیبانی، با support@avalai.ir تماس بگیرید*
