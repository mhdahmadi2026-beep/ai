# Gemini Robotics-ER 1.5 Preview: اولین مدل هوش مصنوعی گوگل برای رباتیک اکنون در دسترس است

**تاریخ:** 1404-08-06 / (2025-10-28)

## خلاصه

پشتیبانی از `gemini-robotics-er-1.5-preview`، اولین مدل زبان-بینایی گوگل که به‌طور خاص برای کاربردهای رباتیک طراحی شده است را اعلام می‌کنیم. این مدل پیش‌نمایش، استدلال فضایی پیشرفته، هماهنگی وظایف زبان طبیعی و قابلیت‌های عامل‌محور را به سیستم‌های رباتیک می‌آورد و ربات‌ها را قادر می‌سازد تا داده‌های بصری پیچیده را تفسیر کنند، اقدامات را برنامه‌ریزی کنند و به محیط‌های پویا از طریق API AvalAI پاسخ دهند.

---

## جزئیات

### گوگل جمینای

گوگل Gemini Robotics-ER 1.5 را معرفی می‌کند، یک مدل زبان-بینایی تخصصی که قابلیت‌های Gemini را به کاربردهای رباتیک فیزیکی گسترش می‌دهد.

- **[gemini-robotics-er-1.5-preview](fa/providers/google.md#gemini-robotics-er-15-preview)**: یک مدل زبان-بینایی طراحی‌شده برای استدلال پیشرفته در محیط‌های فیزیکی، که ربات‌ها را قادر می‌سازد داده‌های بصری را تفسیر کنند، استدلال فضایی انجام دهند و اقدامات را از دستورات زبان طبیعی برنامه‌ریزی کنند.

**ویژگی‌های کلیدی:**

- **خودمختاری پیشرفته**: ربات‌ها را قادر می‌سازد تا استدلال کنند، سازگار شوند و به تغییرات در محیط‌های باز پاسخ دهند
- **تعامل زبان طبیعی**: تخصیص وظایف پیچیده با استفاده از زبان گفتگویی
- **هماهنگی وظایف**: دستورات زبان طبیعی را به زیروظایف تجزیه می‌کند و با کنترل‌کننده‌های ربات موجود یکپارچه می‌شود
- **قابلیت‌های همه‌کاره**: تشخیص اشیاء، استدلال فضایی، برنامه‌ریزی مسیر و تفسیر صحنه‌های پویا
- **بودجه تفکر**: بودجه استدلال قابل تنظیم برای متعادل‌سازی تاخیر در برابر دقت
- **پشتیبانی دوگانه SDK**: در دسترس از طریق API بومی Gemini v1beta و نقاط پایانی سازگار با OpenAI

**موارد استفاده:**
- تشخیص و مکان‌یابی اشیاء با نقاط دوبعدی و جعبه‌های محدودکننده
- ردیابی اشیاء مبتنی بر ویدئو در فریم‌ها
- برنامه‌ریزی مسیر برای حرکت ربات
- استدلال فضایی برای درک محیط
- هماهنگی وظایف طولانی‌مدت با فراخوانی تابع
- اجرای کد پویا برای رفتارهای تطبیقی

**پشتیبانی API:**

- **پشتیبانی کامل**: `v1beta/` (نقطه پایانی بومی Gemini) - دسترسی کامل به تمام ویژگی‌های رباتیک
- **پشتیبانی کامل**: `v1/chat/completions` (سازگار با OpenAI) - ورودی تصویر از طریق آرایه محتوا (مشابه سایر مدل‌های بینایی Gemini)
- **پشتیبانی جزئی**: `v1/responses` (سازگار با OpenAI) - ورودی تصویر از طریق آرایه محتوا (مشابه سایر مدل‌های بینایی Gemini)

**جزئیات قیمت‌گذاری:**

قیمت‌گذاری از همان ساختار `gemini-2.5-flash` پیروی می‌کند:

| مدل | ورودی | ورودی کش‌شده | خروجی | ورودی صوتی | ورودی صوتی کش‌شده |
|-------|-------|--------------|--------|-------------|-------------------|
| gemini-robotics-er-1.5-preview | $0.30/1M توکن | $0.15/1M توکن | $2.50/1M توکن | $1.00/1M توکن | $0.25/1M توکن |

### نمونه درخواست/پاسخ API

#### API بومی Gemini (v1beta) - تشخیص اشیاء

```bash
curl -X POST \
  "https://api.avalai.ir/v1beta/models/gemini-robotics-er-1.5-preview:generateContent" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "inlineData": {
              "mimeType": "image/jpeg",
              "data": "'$(base64 -w 0 image.jpg)'"
            }
          },
          {
            "text": "Point to no more than 10 items in the image. Return the answer in JSON format: [{\"point\": [y, x], \"label\": <label>}, ...]. The points are in [y, x] format normalized to 0-1000."
          }
        ]
      }
    ],
    "generationConfig": {
      "temperature": 0.5,
      "thinkingConfig": {
        "thinkingBudget": 0
      }
    }
  }'
```

#### نمونه پاسخ

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "[{\"point\": [376, 508], \"label\": \"banana\"}, {\"point\": [287, 609], \"label\": \"apple\"}, {\"point\": [223, 303], \"label\": \"orange\"}, {\"point\": [435, 172], \"label\": \"bowl\"}, {\"point\": [270, 786], \"label\": \"plate\"}]"
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP"
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 285,
    "candidatesTokenCount": 52,
    "totalTokenCount": 337
  }
}
```

#### API سازگار با OpenAI

برای ورودی تصویر از طریق نقطه پایانی سازگار با OpenAI:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-robotics-er-1.5-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Identify all objects in this image and return their locations as normalized 2D points."
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "data:image/jpeg;base64,/9j/4AAQSkZJRg..."
            }
          }
        ]
      }
    ]
  }'
```

### نمونه‌های استفاده از SDK

#### SDK بومی Gemini (توصیه‌شده برای رباتیک)

```language-selector
bash=:# نصب Google GenAI SDK
pip install -q google-genai

# تنظیم کلید API شما
export AVALAI_API_KEY="your-avalai-api-key"

python=:from google import genai
from google.genai import types

# مقداردهی اولیه کلاینت GenAI
client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "url": "https://api.avalai.ir"},
)

MODEL_ID = "gemini-robotics-er-1.5-preview"

# بارگذاری تصویر شما
with open("robot-scene.jpg", "rb") as f:
    image_bytes = f.read()

# یافتن اشیاء در صحنه
prompt = """
Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": [y, x], "label": <label>}, ...].
The points are in [y, x] format normalized to 0-1000.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        ),
        prompt,
    ],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

print(response.text)

javascript=:import { GoogleGenerativeAI } from "@google/generative-ai";
import fs from 'fs';

// مقداردهی اولیه کلاینت
const genAI = new GoogleGenerativeAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseUrl: "https://api.avalai.ir"
});

const model = genAI.getGenerativeModel({ 
  model: "gemini-robotics-er-1.5-preview" 
});

// بارگذاری تصویر
const imageData = fs.readFileSync('robot-scene.jpg');
const base64Image = imageData.toString('base64');

const prompt = `
Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": [y, x], "label": <label>}, ...].
The points are in [y, x] format normalized to 0-1000.
`;

const result = await model.generateContent([
  {
    inlineData: {
      data: base64Image,
      mimeType: "image/jpeg"
    }
  },
  prompt
], {
  generationConfig: {
    temperature: 0.5,
    thinkingConfig: {
      thinkingBudget: 0
    }
  }
});

console.log(result.response.text());

```

#### SDK سازگار با OpenAI

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-robotics-er-1.5-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "Find all objects in this image"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
            }
          }
        ]
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از SDK OpenAI با ورودی تصویر
response = client.chat.completions.create(
    model="gemini-robotics-er-1.5-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Identify objects and return their 2D coordinates",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/robot-scene.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "gemini-robotics-er-1.5-preview",
  messages: [
    {
      role: "user",
      content: [
        {
          type: "text",
          text: "Identify objects and return their 2D coordinates"
        },
        {
          type: "image_url",
          image_url: {
            url: "https://example.com/robot-scene.jpg"
          }
        }
      ]
    }
  ]
});

console.log(response.choices[0].message.content);

```

### ویژگی‌های پیشرفته

#### برنامه‌ریزی مسیر

مدل می‌تواند دنباله‌ای از نقاط تعریف‌کننده مسیرهای حرکت ربات تولید کند:

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "url": "https://api.avalai.ir"},
)

with open("workspace.jpg", "rb") as f:
    image_bytes = f.read()

prompt = """
Place a point on the red object, then 15 points for the trajectory of
moving it to the container on the left. Label points from '0' to '15'.
Return as JSON: [{"point": [y, x], "label": <label>}, ...].
Points are in [y, x] format normalized to 0-1000.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-1.5-preview",
    contents=[types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(temperature=0.5),
)

print(response.text)

```

#### استدلال فضایی و هماهنگی

مدل می‌تواند روابط فضایی را درک کند و وظایف چندمرحله‌ای را برنامه‌ریزی کند:

```language-selector
python=:prompt = """
Explain how to pack a lunch box with the items shown.
Point to each object you refer to.
Format: [{"point": [y, x], "label": <object_name>}, ...]
Points normalized to 0-1000.
"""

response = client.models.generate_content(
    model="gemini-robotics-er-1.5-preview",
    contents=[types.Part.from_bytes(data=lunch_image, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

# مدل دستورالعمل‌های گام‌به‌گام با مختصات ارائه می‌دهد
print(response.text)

```

---

## لینک‌های مرتبط

- [مستندات Gemini Robotics-ER](fa/providers/google.md#gemini-robotics-er-15-preview)
- [هوش مصنوعی در رباتیک: راهنمای کامل](fa/examples/ai_robotics_with_gemini_er.md)
- [پشتیبانی SDK بومی Google GenAI](fa/api-reference/v1beta.md)
- [راهنمای درک تصویر](fa/guides/vision.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [نمای کلی مدل‌های گوگل](fa/providers/google.md)
