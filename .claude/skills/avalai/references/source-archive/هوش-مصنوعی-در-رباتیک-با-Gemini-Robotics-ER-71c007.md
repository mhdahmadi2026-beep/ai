# هوش مصنوعی در رباتیک با Gemini Robotics-ER

این راهنمای جامع نحوه استفاده از مدل Gemini Robotics-ER 1.5 گوگل برای کاربردهای رباتیک را نشان می‌دهد. Gemini Robotics-ER یک مدل بینایی-زبانی است که به طور خاص برای رباتیک طراحی شده و قابلیت‌های پیشرفته استدلال فضایی، هماهنگی وظایف زبان طبیعی و قابلیت‌های عاملیت را به سیستم‌های رباتیک فیزیکی می‌آورد.

> این راهنما با اقتباس از [مستندات Gemini](https://ai.google.dev/gemini-api/docs/robotics-overview) و با تغییراتی برای پیاده‌سازی AvalAI تهیه شده است.

## فهرست مطالب

- [مقدمه](#مقدمه)
- [پیش‌نیازها](#پیشنیازها)
- [شروع کار: یافتن اشیاء](#شروع-کار-یافتن-اشیاء)
- [تشخیص اشیاء با کادرهای محدودکننده](#تشخیص-اشیاء-با-کادرهای-محدودکننده)
- [ردیابی اشیاء در ویدیو](#ردیابی-اشیاء-در-ویدیو)
- [برنامه‌ریزی مسیر](#برنامهریزی-مسیر)
- [استدلال فضایی](#استدلال-فضایی)
- [هماهنگی وظایف](#هماهنگی-وظایف)
- [اجرای کد برای وظایف پویا](#اجرای-کد-برای-وظایف-پویا)
- [بهترین شیوه‌ها](#بهترین-شیوهها)
- [عیب‌یابی](#عیبیابی)
- [موارد استفاده پیشرفته](#موارد-استفاده-پیشرفته)

## مقدمه

Gemini Robotics-ER 1.5 اولین مدل بینایی-زبانی گوگل است که به طور خاص برای کاربردهای رباتیک طراحی شده است. این مدل در موارد زیر برتری دارد:

- **تشخیص اشیاء**: شناسایی و موقعیت‌یابی اشیاء با نقاط دوبعدی یا کادرهای محدودکننده
- **استدلال فضایی**: درک روابط اشیاء و زمینه صحنه
- **برنامه‌ریزی مسیر**: تولید مسیرهای حرکتی برای دستکاری‌کننده‌های رباتیک
- **هماهنگی وظایف**: تجزیه دستورات پیچیده به زیروظایف قابل اجرا
- **اجرای کد**: تولید و اجرای پویای کد برای رفتارهای تطبیقی

**ویژگی‌های کلیدی:**
- خودمختاری پیشرفته در محیط‌های باز
- تعامل زبان طبیعی برای تخصیص وظایف پیچیده
- بودجه تفکر قابل تنظیم برای توازن تاخیر/دقت
- پشتیبانی دوگانه SDK (نیتیو Gemini v1beta و سازگار با OpenAI)

## پیش‌نیازها

قبل از شروع، اطمینان حاصل کنید که موارد زیر را دارید:

1. **کلید API AvalAI**: برای دریافت کلید API خود در [AvalAI](https://avalai.ir) ثبت‌نام کنید
2. **محیط Python**: Python 3.8+ با pip نصب شده
3. **کتابخانه‌های مورد نیاز**:

```bash
# نصب Google GenAI SDK (توصیه شده برای رباتیک)
pip install -U google-genai

# یا نصب OpenAI SDK برای فرمت سازگار با OpenAI
pip install -U openai

```

```python
# نصب Google GenAI SDK
import subprocess

subprocess.run(["pip", "install", "-U", "google-genai"])

# یا OpenAI SDK
subprocess.run(["pip", "install", "-U", "openai"])

```

```javascript
# نصب Google GenAI SDK
npm install @google/generative-ai

# یا OpenAI SDK
npm install openai

```

```go
# نصب OpenAI Go SDK
go get github.com/openai/openai-go

```

```php
# نصب OpenAI PHP SDK
composer require openai-php/client

```


4. **فایل‌های تصویری/ویدیویی**: نمونه تصاویر یا ویدیوهای صحنه‌های رباتیک برای تست

## شروع کار: یافتن اشیاء

ابتدایی‌ترین مورد استفاده رباتیک شناسایی اشیاء در یک صحنه است. مدل مختصات دوبعدی نرمال شده (محدوده 0-1000) را برای اشیاء تشخیص داده شده برمی‌گرداند.

### مثال: تشخیص اشیاء روی میز

```bash
# رمزگذاری تصویر به base64
IMAGE_BASE64=$(base64 -w 0 workspace.jpg)

curl -X POST \
  "https://api.avalai.ir/v1beta/models/gemini-robotics-er-1.5-preview:generateContent" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [
        {
          "inlineData": {
            "mimeType": "image/jpeg",
            "data": "'"${IMAGE_BASE64}"'"
          }
        },
        {
          "text": "Point to no more than 10 items in the image. Return JSON: [{\"point\": [y, x], \"label\": <label>}, ...]. Points in [y, x] format normalized to 0-1000."
        }
      ]
    }],
    "generationConfig": {
      "temperature": 0.5,
      "thinkingConfig": {"thinkingBudget": 0}
    }
  }'

```

```python
from google import genai
from google.genai import types

# مقداردهی اولیه کلاینت GenAI
client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "url": "https://api.avalai.ir"},
)

MODEL_ID = "gemini-robotics-er-1.5-preview"

# بارگذاری تصویر
with open("workspace.jpg", "rb") as f:
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

```

```javascript
import { GoogleGenerativeAI } from "@google/generative-ai";
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
const imageData = fs.readFileSync('workspace.jpg');
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

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"os"

	"github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	// خواندن و رمزگذاری تصویر
	imageData, _ := os.ReadFile("workspace.jpg")
	base64Image := base64.StdEncoding.EncodeToString(imageData)

	resp, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gemini-robotics-er-1.5-preview"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage([]openai.ChatCompletionContentPartUnionParam{
				openai.TextPart("Identify objects and return 2D coordinates in JSON format"),
				openai.ImagePart("data:image/jpeg;base64," + base64Image),
			}),
		}),
	})

	if err != nil {
		panic(err)
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey($_ENV['AVALAI_API_KEY'])
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// خواندن و رمزگذاری تصویر
$imageData = file_get_contents('workspace.jpg');
$base64Image = base64_encode($imageData);

$response = $client->chat()->create([
    'model' => 'gemini-robotics-er-1.5-preview',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                [
                    'type' => 'text',
                    'text' => 'Identify objects and return 2D coordinates in JSON format'
                ],
                [
                    'type' => 'image_url',
                    'image_url' => [
                        'url' => 'data:image/jpeg;base64,' . $base64Image
                    ]
                ]
            ]
        ]
    ]
]);

echo $response['choices'][0]['message']['content'];

```


**خروجی مورد انتظار:**

```json
[
  {
    "point": [
      376,
      508
    ],
    "label": "آچار"
  },
  {
    "point": [
      287,
      609
    ],
    "label": "پیچ‌گوشتی"
  },
  {
    "point": [
      223,
      303
    ],
    "label": "انبردست"
  },
  {
    "point": [
      435,
      172
    ],
    "label": "جعبه ابزار"
  },
  {
    "point": [
      270,
      786
    ],
    "label": "چکش"
  }
]
```

<!-- responses-equivalent:start -->

<details>
<summary>مسیر مهاجرت به Responses API</summary>

`gemini-robotics-er-1.5-preview` یک مدل رباتیک Gemini است و در AvalAI فعلا با مسیر نیتیو Gemini `v1beta` یا مسیر سازگار OpenAI یعنی `/v1/chat/completions` استفاده می‌شود. وقتی به همین مدل رباتیک نیاز دارید، مثال‌های بالا را نگه دارید. اگر برای یک گردش‌کار بینایی قابل‌حمل به شکل `/v1/responses` نیاز دارید، به یک مدل بینایی سازگار با Responses مثل `gpt-5.5` مهاجرت کنید، تصویر و prompt را داخل `input` بفرستید و متن نهایی را از `response.output_text` بخوانید.

```python
import base64
import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("workspace.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a robotic vision assistant. Return only valid JSON.",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": (
                        "Point to no more than 10 items in the image. "
                        "Return normalized [y, x] points in the 0-1000 range."
                    ),
                },
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
    text={
        "format": {
            "type": "json_schema",
            "name": "robot_points",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "objects": {
                        "type": "array",
                        "items": {
                            "type": "object",
                            "properties": {
                                "point": {
                                    "type": "array",
                                    "items": {"type": "integer"},
                                    "minItems": 2,
                                    "maxItems": 2,
                                },
                                "label": {"type": "string"},
                            },
                            "required": ["point", "label"],
                            "additionalProperties": False,
                        },
                    }
                },
                "required": ["objects"],
                "additionalProperties": False,
            },
        }
    },
)

objects = json.loads(response.output_text)["objects"]
print(objects)

```

```javascript
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const base64Image = fs.readFileSync("workspace.jpg").toString("base64");

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a robotic vision assistant. Return only valid JSON.",
  input: [
    {
      role: "user",
      content: [
        {
          type: "input_text",
          text:
            "Point to no more than 10 items in the image. " +
            "Return normalized [y, x] points in the 0-1000 range.",
        },
        {
          type: "input_image",
          image_url: `data:image/jpeg;base64,${base64Image}`,
        },
      ],
    },
  ],
  text: {
    format: {
      type: "json_schema",
      name: "robot_points",
      strict: true,
      schema: {
        type: "object",
        properties: {
          objects: {
            type: "array",
            items: {
              type: "object",
              properties: {
                point: {
                  type: "array",
                  items: { type: "integer" },
                  minItems: 2,
                  maxItems: 2,
                },
                label: { type: "string" },
              },
              required: ["point", "label"],
              additionalProperties: false,
            },
          },
        },
        required: ["objects"],
        additionalProperties: false,
      },
    },
  },
});

console.log(JSON.parse(response.output_text).objects);

```

```bash
IMAGE_BASE64=$(base64 -w 0 workspace.jpg)

curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "You are a robotic vision assistant. Return only valid JSON.",
    "input": [{
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "Point to no more than 10 items in the image. Return normalized [y, x] points in the 0-1000 range."
        },
        {
          "type": "input_image",
          "image_url": "data:image/jpeg;base64,'"$IMAGE_BASE64"'"
        }
      ]
    }],
    "text": {
      "format": {
        "type": "json_schema",
        "name": "robot_points",
        "strict": true,
        "schema": {
          "type": "object",
          "properties": {
            "objects": {
              "type": "array",
              "items": {
                "type": "object",
                "properties": {
                  "point": {
                    "type": "array",
                    "items": {"type": "integer"},
                    "minItems": 2,
                    "maxItems": 2
                  },
                  "label": {"type": "string"}
                },
                "required": ["point", "label"],
                "additionalProperties": false
              }
            }
          },
          "required": ["objects"],
          "additionalProperties": false
        }
      }
    }
  }'

```


برای کنترل ربات، نسخه Responses را مهاجرت orchestration بدانید، نه مهاجرت ایمنی. calibration، بررسی برخورد، بازبینی انسانی و منطق توقف اضطراری را بیرون از مدل نگه دارید.

</details>

<!-- responses-equivalent:end -->

![An example that displays the points of objects in an image](https://ai.google.dev/static/gemini-api/docs/images/robotics/point-to-object.png)

*شکل 1: تشخیص اشیاء با نقاط دوبعدی که مختصات نرمال شده برای هر شیء شناسایی شده را نشان می‌دهد*

## تشخیص اشیاء با کادرهای محدودکننده

برای موقعیت‌یابی دقیق‌تر اشیاء، به جای نقاط منفرد، کادرهای محدودکننده دوبعدی درخواست کنید.

```python
prompt = """
Return bounding boxes as a JSON array with labels. Never return masks
or code fencing. Limit to 25 objects. Include as many objects as you
can identify on the table.
If an object is present multiple times, name them according to their
unique characteristic (colors, size, position, etc.).
The format should be: [{"box_2d": [ymin, xmin, ymax, xmax],
"label": <label>}] normalized to 0-1000. Values must be integers.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

import json

boxes = json.loads(response.text)
print(f"تشخیص {len(boxes)} شیء")

```

```javascript
const prompt = `
Return bounding boxes as a JSON array with labels. Limit to 25 objects.
Format: [{"box_2d": [ymin, xmin, ymax, xmax], "label": <label>}]
normalized to 0-1000. Values must be integers.
`;

const result = await model.generateContent([
  {inlineData: {data: base64Image, mimeType: "image/jpeg"}},
  prompt
], {
  generationConfig: {
    temperature: 0.5,
    thinkingConfig: {thinkingBudget: 0}
  }
});

const boxes = JSON.parse(result.response.text());
console.log(`تشخیص ${boxes.length} شیء`);

```


**مثال خروجی:**

```json
[
  {
    "box_2d": [
      100,
      200,
      300,
      400
    ],
    "label": "بلوک قرمز"
  },
  {
    "box_2d": [
      150,
      500,
      350,
      700
    ],
    "label": "سیلندر آبی"
  },
  {
    "box_2d": [
      200,
      100,
      400,
      300
    ],
    "label": "کره سبز"
  }
]
```

![An example showing bounding boxes for objects found](https://ai.google.dev/static/gemini-api/docs/images/robotics/bounding-boxes.png ':size=1000')

*شکل 2: تشخیص اشیاء با کادرهای محدودکننده دوبعدی که مناطق مستطیلی دقیق برای هر شیء فراهم می‌کند*

## ردیابی اشیاء در ویدیو

اشیاء را در فریم‌های ویدیو برای کاربردهای رباتیک پویا ردیابی کنید.

```python
import cv2

# تعریف اشیاء برای ردیابی
queries = [
    "بلوک قرمز (روی میز)",
    "بلوک قرمز (در گیره)",
    "سیلندر آبی",
]

base_prompt = f"""
Point to the following objects: {', '.join(queries)}.
Return JSON: [{{"point": [y, x], "label": <label>}}, ...].
Points in [y, x] format normalized to 0-1000.
If no objects found, return empty list [].
"""

# بارگذاری ویدیو
video = cv2.VideoCapture("robot_manipulation.mp4")
frame_count = 0
tracking_data = []

while video.isOpened():
    ret, frame = video.read()
    if not ret:
        break

    # پردازش هر 5 فریم
    if frame_count % 5 == 0:
        # رمزگذاری فریم
        _, buffer = cv2.imencode(".jpg", frame)
        frame_bytes = buffer.tobytes()

        # تشخیص اشیاء
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                types.Part.from_bytes(data=frame_bytes, mime_type="image/jpeg"),
                base_prompt,
            ],
            config=types.GenerateContentConfig(
                temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
            ),
        )

        frame_data = {"frame": frame_count, "objects": json.loads(response.text)}
        tracking_data.append(frame_data)
        print(f"فریم {frame_count}: {len(frame_data['objects'])} شیء تشخیص داده شد")

    frame_count += 1

video.release()
print(f"پردازش {len(tracking_data)} فریم")

```


![An example that shows objects being tracked through frames in a GIF](https://ai.google.dev/static/gemini-api/docs/images/robotics/object-tracking.gif)

*شکل 3: ردیابی اشیاء در فریم‌های ویدیو که تحلیل زمانی حرکت اشیاء را نشان می‌دهد*

## برنامه‌ریزی مسیر

مسیرهای حرکتی را برای دستکاری‌کننده‌های رباتیک تولید کنید تا اشیاء را به طور ایمن جابجا کنند.

```python
prompt = """
Place a point on the red block, then 15 points for the trajectory of
moving the red block to the top of the container on the left.
The points should be labeled by order of the trajectory, from '0'
(start point) to '15' (final point).
Return JSON: [{"point": [y, x], "label": <label>}, ...].
Points in [y, x] format normalized to 0-1000.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(temperature=0.5),
)

trajectory = json.loads(response.text)
print(f"مسیر تولید شده با {len(trajectory)} نقطه میانی")


# تبدیل مختصات نرمال شده به مختصات فضای کاری ربات
def normalize_to_robot_coords(point, workspace_dims):
    """تبدیل مختصات نرمال (0-1000) به مختصات فضای کاری ربات"""
    y_norm, x_norm = point
    x_robot = (x_norm / 1000.0) * workspace_dims["width"] + workspace_dims["x_min"]
    y_robot = (y_norm / 1000.0) * workspace_dims["height"] + workspace_dims["y_min"]
    return (x_robot, y_robot)


workspace = {"x_min": -0.5, "width": 1.0, "y_min": -0.5, "height": 1.0}

robot_trajectory = []
for waypoint in trajectory:
    robot_coords = normalize_to_robot_coords(waypoint["point"], workspace)
    robot_trajectory.append({"label": waypoint["label"], "coords": robot_coords})
    print(f"نقطه میانی {waypoint['label']}: {robot_coords}")

```


![An example showing the planned trajectory](https://ai.google.dev/static/gemini-api/docs/images/robotics/trajectories.png ':size=1000')

*شکل 4: برنامه‌ریزی مسیر با 15 نقطه میانی که مسیر حرکت ربات را تعریف می‌کند*

## استدلال فضایی

از درک مدل در مورد روابط فضایی برای وظایف پیچیده استفاده کنید.

### مثال: ایجاد فضا برای یک شیء

```python
prompt = """
Point to the object that I need to remove to make room for my laptop.
Return JSON: [{"point": [y, x], "label": <label>}, ...].
Points in [y, x] format normalized to 0-1000.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=desk_image, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

result = json.loads(response.text)
print(f"شیء برای حذف: {result[0]['label']}")
print(f"موقعیت: {result[0]['point']}")

```


![An example that shows which object needs to be moved for another object](https://ai.google.dev/static/gemini-api/docs/images/robotics/spatial-reasoning.png ':size=1000')

*شکل 5: استدلال فضایی برای شناسایی شیئی که باید جابجا شود تا فضا برای لپ‌تاپ ایجاد گردد*

### مثال: برنامه‌ریزی وظایف چند مرحله‌ای

```python
prompt = """
Explain how to pack the lunch box and lunch bag. Point to each
object you refer to. Each point format:
[{"point": [y, x], "label": <object_name>}]
Coordinates normalized to 0-1000.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=lunch_image, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

print(response.text)

```


![An image of a lunch box and items to put into it](https://ai.google.dev/static/gemini-api/docs/images/robotics/packing-lunch.png ':size=1000')

*شکل 6: برنامه‌ریزی وظایف چند مرحله‌ای برای بسته‌بندی جعبه ناهار با دستورالعمل‌های گام به گام*

## هماهنگی وظایف

از فراخوانی تابع برای هماهنگی وظایف رباتیک پیچیده با APIهای سفارشی استفاده کنید.

### مثال: عملیات برداشتن و قرار دادن

```python
# تعریف API ربات شبیه‌سازی شده
def move(x, y, high):
    """حرکت بازو به مختصات. high=True بازو را بالای صحنه بلند می‌کند."""
    print(f"حرکت به: x={x}, y={y}, z={'بالا' if high else 'پایین'}")


def setGripperState(opened):
    """باز یا بسته کردن گیره."""
    print("باز کردن گیره" if opened else "بستن گیره")


def returnToOrigin():
    """بازگشت به حالت اولیه."""
    print("بازگشت به مبدا")


# ابتدا، مکان اشیاء را پیدا کنید
locate_prompt = """
Locate and point to the blue block and the orange bowl.
Return JSON: [{"point": [y, x], "label": <label>}, ...].
Points in [y, x] format normalized to 0-1000.
"""

locate_response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(data=scene_image, mime_type="image/jpeg"),
        locate_prompt,
    ],
    config=types.GenerateContentConfig(temperature=0.5),
)

objects = json.loads(locate_response.text)
block = next(obj for obj in objects if "block" in obj["label"].lower())
bowl = next(obj for obj in objects if "bowl" in obj["label"].lower())

print(f"بلوک در: {block['point']}")
print(f"کاسه در: {bowl['point']}")

# حالا عملیات برداشتن و قرار دادن را هماهنگ کنید
robot_origin = [500, 500]  # مختصات نرمال شده
block_relative = [
    block["point"][0] - robot_origin[0],
    block["point"][1] - robot_origin[1],
]
bowl_relative = [bowl["point"][0] - robot_origin[0], bowl["point"][1] - robot_origin[1]]

orchestrate_prompt = f"""
You are a robotic arm with six degrees-of-freedom. You have these functions:

def move(x, y, high):
  # Moves arm to coordinates. high=True lifts arm above scene.

def setGripperState(opened):
  # Opens gripper if opened=True, closes if False

def returnToOrigin():
  # Returns robot to initial state

Origin point is at normalized {robot_origin}.
Perform pick and place: pick up blue block at {block['point']}
(relative: {block_relative}) and place in orange bowl at {bowl['point']}
(relative: {bowl_relative}).

Provide sequence of function calls as JSON list:
[{{"function": <name>, "args": [<args>]}}, ...]
Include your reasoning before the JSON.
"""

orchestrate_response = client.models.generate_content(
    model=MODEL_ID,
    contents=[orchestrate_prompt],
    config=types.GenerateContentConfig(temperature=0.5),
)

print("برنامه مدل:")
print(orchestrate_response.text)

# تجزیه و اجرای فراخوانی‌های تابع
import re

json_match = re.search(r"\[.*\]", orchestrate_response.text, re.DOTALL)
if json_match:
    function_calls = json.loads(json_match.group())
    print("\nدر حال اجرا:")
    for call in function_calls:
        func_name = call["function"]
        args = call["args"]
        if func_name == "move":
            move(*args)
        elif func_name == "setGripperState":
            setGripperState(*args)
        elif func_name == "returnToOrigin":
            returnToOrigin()

```


![Example of robot API scenario](https://ai.google.dev/static/gemini-api/docs/images/robotics/robot-api-example.png ':size=1000')

*شکل 7: سناریوی وظیفه برداشتن و قرار دادن با بلوک آبی و کاسه نارنجی*

## اجرای کد برای وظایف پویا

مدل را قادر سازید تا کد بنویسد و برای رفتارهای تطبیقی اجرا کند.

```python
from google import genai
from google.genai import types

prompt = """
What is the reading on this device? Using code execution,
zoom in on the image to take a closer look if needed.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[types.Part.from_bytes(data=device_image, mime_type="image/jpeg"), prompt],
    config=types.GenerateContentConfig(
        temperature=0.5, tools=[types.Tool(code_execution=types.ToolCodeExecution)]
    ),
)

# نمایش تفکر و اجرای کد مدل
for part in response.candidates[0].content.parts:
    if part.text:
        print("پاسخ مدل:", part.text)
    if part.executable_code:
        print("کد تولید شده:", part.executable_code.code)
    if part.code_execution_result:
        print("نتیجه اجرا:", part.code_execution_result.output)

```


## بهترین شیوه‌ها

### 1. استفاده از زبان واضح و ساده

مدل برای درک زبان طبیعی و گفتگویی طراحی شده است. پرامپت‌ها را به صورت معنایی واضح ساختاربندی کنید:

```python
# خوب: زبان طبیعی
prompt = "تمام میوه‌های روی میز را پیدا کن و موقعیت‌هایشان را برگردان"

# همچنین خوب: الزامات فرمت خاص
prompt = """
تمام اشیاء روی میز را شناسایی کن.
به صورت JSON برگردان: [{"point": [y, x], "label": <name>}, ...]
نقاط نرمال شده به 0-1000.
"""
```

### 2. بهینه‌سازی ورودی بصری

- **زوم برای جزئیات**: برای اشیاء کوچک یا دور، ابتدا ناحیه مورد نظر را برش دهید
- **نور مناسب**: از نور کافی و کنتراست رنگی مطمئن شوید
- **دید واضح**: انسدادها را به حداقل برسانید و در صورت امکان دیدهای بدون مانع فراهم کنید

```python
# برش به ناحیه مورد نظر برای دقت بهتر
from PIL import Image

img = Image.open("workspace.jpg")
roi = img.crop((400, 300, 800, 700))  # تمرکز بر ناحیه خاص
roi.save("workspace_roi.jpg")
```

### 3. تعادل بودجه تفکر

از `thinking_budget` برای کنترل تاخیر در مقابل دقت استفاده کنید:

```python
# سریع، تاخیر کم (خوب برای تشخیص ساده)
config = types.GenerateContentConfig(
    temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
)

# دقیق‌تر (خوب برای استدلال پیچیده)
config = types.GenerateContentConfig(
    temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=2000)
)
```

### 4. تجزیه مشکلات پیچیده

برای وظایف چند مرحله‌ای، مدل را در هر مرحله راهنمایی کنید:

```python
# مرحله 1: شناسایی اشیاء
objects_prompt = "تمام اشیاء روی میز را لیست کن"
objects = get_objects(objects_prompt)

# مرحله 2: برنامه‌ریزی مسیر
trajectory_prompt = f"مسیر حرکت {objects[0]} به ظرف را برنامه‌ریزی کن"
trajectory = plan_trajectory(trajectory_prompt)

# مرحله 3: اجرای حرکت
execute_motion(trajectory)
```

### 5. بهبود دقت از طریق اجماع

برای وظایف با دقت بالا، چندین بار پرس و جو کنید و نتایج را میانگین بگیرید:

```python
def get_consensus_location(image, object_name, iterations=3):
    """دریافت موقعیت شیء با اجماع از پرس و جوهای متعدد"""
    results = []

    for i in range(iterations):
        prompt = f'به {object_name} اشاره کن. JSON برگردان: [{{"point": [y, x], "label": "{object_name}"}}]'
        response = client.models.generate_content(
            model=MODEL_ID,
            contents=[
                types.Part.from_bytes(data=image, mime_type="image/jpeg"),
                prompt,
            ],
            config=types.GenerateContentConfig(temperature=0.5),
        )
        location = json.loads(response.text)[0]["point"]
        results.append(location)

    # میانگین مختصات
    avg_y = sum(r[0] for r in results) / iterations
    avg_x = sum(r[1] for r in results) / iterations

    return [int(avg_y), int(avg_x)]


# استفاده
consensus_location = get_consensus_location(image_bytes, "بلوک قرمز", iterations=3)
print(f"موقعیت اجماعی: {consensus_location}")
```

## عیب‌یابی

### مشکلات رایج و راه‌حل‌ها

#### مشکل: مدل متن به جای JSON برمی‌گرداند

**مشکل**: مدل شامل فرمت‌بندی markdown یا متن توضیحی است.

**راه‌حل**: در پرامپت خود صریح باشید و پاسخ را تجزیه کنید:

```python
import re
import json

response_text = response.text

# حذف حصارهای کد markdown
fence_pattern = r"`{3}json\n(.*?)\n`{3}"
json_match = re.search(fence_pattern, response_text, re.DOTALL)
if json_match:
    json_text = json_match.group(1)
else:
    # سعی در یافتن آرایه یا شیء JSON
    json_match = re.search(r"[\[\{].*[\]\}]", response_text, re.DOTALL)
    json_text = json_match.group(0) if json_match else response_text

try:
    data = json.loads(json_text)
except json.JSONDecodeError as e:
    print(f"تجزیه JSON ناموفق: {e}")
    print(f"متن پاسخ: {response_text}")
```

#### مشکل: تشخیص نادرست اشیاء

**مشکل**: مدل اشیاء را اشتباه شناسایی می‌کند یا مختصات نادرستی ارائه می‌دهد.

**راه‌حل**:
1. بهبود کیفیت تصویر و نور
2. افزایش بودجه تفکر برای صحنه‌های پیچیده
3. استفاده از توضیحات خاص‌تر برای اشیاء
4. زوم روی ناحیه مورد نظر

```python
# استفاده از بودجه تفکر بالاتر برای صحنه‌های پیچیده
config = types.GenerateContentConfig(
    temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=1000)
)

# خاص‌تر بودن در پرامپت‌ها
prompt = "بلوک مستطیلی قرمز (نه سیلندر) در سمت چپ میز را پیدا کن"
```

#### مشکل: زمان پاسخ کند

**مشکل**: مدل برای پاسخ زمان زیادی می‌برد.

**راه‌حل**:
1. بودجه تفکر را برای وظایف ساده به 0 تنظیم کنید
2. وضوح تصویر را کاهش دهید
3. فریم‌ها را با فرکانس کمتری در ویدیو پردازش کنید

```python
# تغییر اندازه تصاویر بزرگ
from PIL import Image

img = Image.open("large_image.jpg")
img.thumbnail((800, 600))  # کاهش اندازه با حفظ نسبت ابعاد
img.save("resized_image.jpg")

# استفاده از تفکر حداقل برای تشخیص سریع
config = types.GenerateContentConfig(
    temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
)
```

#### مشکل: عدم تطابق سیستم مختصات

**مشکل**: مختصات نرمال شده با فضای کاری ربات هم‌راستا نیست.

**راه‌حل**: تبدیل مناسب مختصات را پیاده‌سازی کنید:

```python
def transform_coordinates(normalized_point, camera_calibration, robot_workspace):
    """
    تبدیل از مختصات نرمال شده تصویر به فضای کاری ربات

    Args:
        normalized_point: [y, x] در محدوده 0-1000
        camera_calibration: ماتریس کالیبراسیون دوربین
        robot_workspace: مرزهای فضای کاری ربات

    Returns:
        [x, y, z] در مختصات ربات
    """
    # تبدیل نرمال شده به مختصات پیکسل
    y_norm, x_norm = normalized_point
    x_pixel = (x_norm / 1000.0) * camera_calibration["image_width"]
    y_pixel = (y_norm / 1000.0) * camera_calibration["image_height"]

    # اعمال ماتریس کالیبراسیون دوربین
    # (بر اساس کالیبراسیون دوربین خاص خود پیاده‌سازی کنید)
    x_camera = x_pixel * camera_calibration["scale_x"]
    y_camera = y_pixel * camera_calibration["scale_y"]

    # تبدیل به فضای کاری ربات
    x_robot = x_camera + robot_workspace["offset_x"]
    y_robot = y_camera + robot_workspace["offset_y"]
    z_robot = robot_workspace["table_height"]

    return [x_robot, y_robot, z_robot]
```

### بهینه‌سازی عملکرد

#### پردازش دسته‌ای

پردازش کارآمد چندین تصویر:

```python
import concurrent.futures


def process_image(image_path):
    """پردازش تصویر تکی"""
    with open(image_path, "rb") as f:
        image_bytes = f.read()

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image_bytes, mime_type="image/jpeg"),
            detection_prompt,
        ],
        config=config,
    )

    return json.loads(response.text)


# پردازش موازی تصاویر
image_paths = ["img1.jpg", "img2.jpg", "img3.jpg"]
with concurrent.futures.ThreadPoolExecutor(max_workers=3) as executor:
    results = list(executor.map(process_image, image_paths))

for i, result in enumerate(results):
    print(f"تصویر {i+1}: {len(result)} شیء تشخیص داده شد")
```

#### کش کردن برای پرس و جوهای تکراری

از کش کردن پرامپت برای سناریوهای تکراری استفاده کنید:

```python
# مدل به طور خودکار پرامپت‌های طولانی را کش می‌کند
# پرامپت‌های خود را ساختار دهید تا بیشترین بهره‌وری از کش را داشته باشید

base_instructions = """
شما یک سیستم بینایی رباتیک هستید. همیشه نتایج را به صورت JSON برگردانید.
برای تشخیص اشیاء، از این فرمت استفاده کنید: [{"point": [y, x], "label": <name>}, ...]
نقاط در فرمت [y, x] نرمال شده به 0-1000 هستند.
هرگز فرمت‌بندی markdown یا حصار کد نگنجانید.
"""

# این دستورالعمل پایه کش خواهد شد
# فقط پرس و جوی خاص را تغییر دهید
query = "تمام ابزارها را روی میز کار پیدا کن"
full_prompt = base_instructions + "\n\n" + query
```

## موارد استفاده پیشرفته

### هماهنگی چند رباته

هماهنگی چندین ربات با استفاده از درک صحنه:

```python
def allocate_tasks(scene_image, robots, tasks):
    """
    تخصیص وظایف به چندین ربات بر اساس تحلیل صحنه

    Args:
        scene_image: تصویر فضای کاری
        robots: لیست موقعیت‌های ربات [{"id": 1, "pos": [x, y]}, ...]
        tasks: لیست وظایف [{"obj": "block", "target": "bin"}, ...]

    Returns:
        دیکشنری تخصیص وظایف
    """
    # تشخیص تمام اشیاء
    detect_prompt = "تمام اشیاء را شناسایی کن. JSON با موقعیت‌ها برگردان."
    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=scene_image, mime_type="image/jpeg"),
            detect_prompt,
        ],
        config=types.GenerateContentConfig(temperature=0.5),
    )

    objects = json.loads(response.text)

    # تخصیص وظایف بر اساس نزدیکی
    allocation = {}
    for task in tasks:
        # یافتن شیء
        obj = next(o for o in objects if task["obj"] in o["label"].lower())

        # یافتن نزدیک‌ترین ربات
        min_dist = float("inf")
        closest_robot = None
        for robot in robots:
            dist = (
                (obj["point"][0] - robot["pos"][0]) ** 2
                + (obj["point"][1] - robot["pos"][1]) ** 2
            ) ** 0.5
            if dist < min_dist:
                min_dist = dist
                closest_robot = robot["id"]

        allocation[closest_robot] = allocation.get(closest_robot, [])
        allocation[closest_robot].append(task)

    return allocation
```

### نظارت ایمنی

نظارت بر شرایط ناایمن:

```python
def check_workspace_safety(image):
    """بررسی فضای کاری برای خطرات ایمنی"""
    safety_prompt = """
    این فضای کاری رباتیک را برای مسائل ایمنی تحلیل کن.
    بررسی کن:
    1. موانع در مسیر ربات
    2. اشیاء نزدیک به لبه‌های فضای کاری
    3. انسان‌ها یا اعضای بدن در صحنه
    4. آرایش ناپایدار اشیاء
    
    JSON برگردان: {"safe": true/false, "issues": [<list of issues>]}
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image, mime_type="image/jpeg"),
            safety_prompt,
        ],
        config=types.GenerateContentConfig(temperature=0.5),
    )

    return json.loads(response.text)


# استفاده
safety_status = check_workspace_safety(workspace_image)
if not safety_status["safe"]:
    print("هشدار ایمنی:", safety_status["issues"])
    # توقف عملیات ربات
```

### گرفتن تطبیقی

برنامه‌ریزی پیکربندی گرفتن بر اساس ویژگی‌های شیء:

```python
def plan_grasp(image, object_name):
    """برنامه‌ریزی پیکربندی گرفتن برای شیء"""
    grasp_prompt = f"""
    {object_name} را تحلیل کن و پیکربندی گرفتن را توصیه کن.
    در نظر بگیر:
    - شکل و اندازه شیء
    - نقاط گرفتن (مکان‌های تماس پایدار)
    - زاویه نزدیک شدن
    - عرض مورد نیاز گیره
    
    JSON برگردان: {{
        "grasp_points": [[y1, x1], [y2, x2]],
        "approach_angle": <degrees>,
        "gripper_width": <mm>,
        "confidence": <0-1>
    }}
    """

    response = client.models.generate_content(
        model=MODEL_ID,
        contents=[
            types.Part.from_bytes(data=image, mime_type="image/jpeg"),
            grasp_prompt,
        ],
        config=types.GenerateContentConfig(temperature=0.5),
    )

    return json.loads(response.text)
```

## لینک‌های مرتبط

- [اطلاعیه مدل Gemini Robotics-ER](fa/news/2025-10-28-gemini-robotics-er-model-added.md)
- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [مرجع Native Gemini API (v1beta)](fa/api-reference/v1beta.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای بینایی](fa/guides/vision.md)
- [بهترین شیوه‌ها برای Production](fa/guides/production-best-practices.md)

## نتیجه‌گیری

Gemini Robotics-ER 1.5 قابلیت‌های قدرتمند هوش مصنوعی را به کاربردهای رباتیک می‌آورد. با ترکیب بینایی، درک زبان و استدلال فضایی، تعاملات رباتیک طبیعی‌تر و انعطاف‌پذیرتری را امکان‌پذیر می‌سازد. با تشخیص ساده اشیاء شروع کنید، سپس به تدریج ویژگی‌های پیشرفته‌تر مانند برنامه‌ریزی مسیر و هماهنگی وظایف را بگنجانید.

برای استقرار در محیط تولید، همیشه مدیریت خطای مناسب، بررسی‌های ایمنی و کالیبراسیون سیستم مختصات را پیاده‌سازی کنید. معیارهای عملکرد را نظارت کنید و بودجه‌های تفکر را بر اساس نیازهای تاخیر و دقت خود تنظیم کنید.

موفق باشید! 🤖
