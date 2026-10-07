# تنظیمات ایمنی Gemini

این راهنما نحوه استفاده از تنظیمات ایمنی داخلی Gemini برای نظارت بر محتوا به طور مستقیم در فراخوانی‌های API را توضیح می‌دهد. اگر به دنبال پیاده‌سازی نظارت بر محتوا در برنامه خود هستید و از مدل‌های Gemini استفاده می‌کنید، می‌توانید از این تنظیمات ایمنی به عنوان جایگزینی برای استفاده از [API نظارت](fa/api-reference/moderation.md) جداگانه بهره ببرید.

## نمای کلی

مدل‌های Gemini گوگل شامل فیلترهای ایمنی داخلی هستند که می‌توانند به طور خودکار محتوای بالقوه مضر را در چهار دسته شناسایی و مسدود کنند. برخلاف رویکرد سنتی فراخوانی endpoint نظارت جداگانه قبل یا بعد از فراخوانی API اصلی، تنظیمات ایمنی Gemini به شما امکان می‌دهد نظارت بر محتوا را مستقیما در همان درخواست API پیکربندی کنید.

### مزایای استفاده از تنظیمات ایمنی Gemini

| رویکرد | API نظارت | تنظیمات ایمنی Gemini |
|--------|-----------|----------------------|
| **فراخوانی‌های API** | نیاز به فراخوانی نظارت جداگانه | داخلی در همان فراخوانی API |
| **تاخیر** | رفت و برگشت اضافی برای نظارت | بدون تاخیر اضافی |
| **هزینه** | هزینه فراخوانی API جداگانه | شامل در تولید محتوا |
| **انعطاف‌پذیری** | فیلترینگ پس از تولید | فیلترینگ بلادرنگ در حین تولید |
| **دسته‌ها** | دسته‌های نظارت OpenAI | دسته‌های آسیب گوگل |

## دسته‌های آسیب

تنظیمات ایمنی Gemini می‌توانند محتوا را در چهار دسته آسیب فیلتر کنند:

| دسته | مقدار Enum | توضیحات |
|------|------------|---------|
| آزار و اذیت | `HARM_CATEGORY_HARASSMENT` | نظرات منفی یا مضر که هویت و/یا ویژگی‌های محافظت‌شده را هدف قرار می‌دهند |
| سخنان نفرت‌انگیز | `HARM_CATEGORY_HATE_SPEECH` | محتوایی که بی‌ادبانه، بی‌احترامانه یا زننده است |
| محتوای جنسی صریح | `HARM_CATEGORY_SEXUALLY_EXPLICIT` | شامل اشارات به اعمال جنسی یا محتوای هرزه دیگر |
| محتوای خطرناک | `HARM_CATEGORY_DANGEROUS_CONTENT` | ترویج، تسهیل یا تشویق اعمال مضر |

## آستانه‌های مسدودسازی

برای هر دسته آسیب، می‌توانید آستانه‌ای تنظیم کنید تا کنترل کنید محتوا چقدر شدید مسدود شود:

| آستانه | مقدار Enum | توضیحات |
|--------|------------|---------|
| خاموش | `OFF` | فیلتر ایمنی را کاملا خاموش کنید |
| مسدود نکن | `BLOCK_NONE` | نمایش تمام محتوا (مشابه OFF) |
| مسدود کم | `BLOCK_ONLY_HIGH` | فقط محتوای مضر با احتمال بالا را مسدود کنید |
| مسدود متوسط | `BLOCK_MEDIUM_AND_ABOVE` | محتوای با احتمال متوسط و بالا را مسدود کنید |
| مسدود بیشتر | `BLOCK_LOW_AND_ABOVE` | محتوای با احتمال کم، متوسط و بالا را مسدود کنید |

> **توجه:** برای مدل‌های Gemini 2.5 و Gemini 3، آستانه پیش‌فرض تنظیمات ایمنی `OFF` است. برای مدل‌های قدیمی‌تر، پیش‌فرض `BLOCK_MEDIUM_AND_ABOVE` است.

## استفاده از تنظیمات ایمنی با API بومی Gemini

### مثال پایه

```python
from google import genai
from google.genai import types

# مقداردهی اولیه کلاینت با AvalAI
client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

# پیکربندی تنظیمات ایمنی
safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_LOW_AND_ABOVE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="BLOCK_MEDIUM_AND_ABOVE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="BLOCK_ONLY_HIGH",
    ),
]

# تولید محتوا با تنظیمات ایمنی
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="اهمیت ایمنی آنلاین را توضیح دهید.",
    config=types.GenerateContentConfig(safety_settings=safety_settings),
)

print(response.text)

```

```javascript
import { GoogleGenAI, HarmCategory, HarmBlockThreshold } from "@google/genai";

// مقداردهی اولیه کلاینت با AvalAI
const client = new GoogleGenAI({
  apiKey: process.env.AVALAI_API_KEY,
  httpOptions: { baseUrl: "https://api.avalai.ir" }
});

// پیکربندی تنظیمات ایمنی
const safetySettings = [
  {
    category: HarmCategory.HARM_CATEGORY_HARASSMENT,
    threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_HATE_SPEECH,
    threshold: HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT,
    threshold: HarmBlockThreshold.BLOCK_MEDIUM_AND_ABOVE,
  },
  {
    category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT,
    threshold: HarmBlockThreshold.BLOCK_ONLY_HIGH,
  },
];

// تولید محتوا با تنظیمات ایمنی
const response = await client.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "اهمیت ایمنی آنلاین را توضیح دهید.",
  config: { safetySettings: safetySettings },
});

console.log(response.text);

```

```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()

	// مقداردهی اولیه کلاینت با AvalAI
	client, err := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	if err != nil {
		fmt.Printf("خطا در ایجاد کلاینت: %v\n", err)
		return
	}
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")

	// پیکربندی تنظیمات ایمنی
	model.SafetySettings = []*genai.SafetySetting{
		{
			Category:  genai.HarmCategoryHarassment,
			Threshold: genai.HarmBlockMediumAndAbove,
		},
		{
			Category:  genai.HarmCategoryHateSpeech,
			Threshold: genai.HarmBlockLowAndAbove,
		},
		{
			Category:  genai.HarmCategorySexuallyExplicit,
			Threshold: genai.HarmBlockMediumAndAbove,
		},
		{
			Category:  genai.HarmCategoryDangerousContent,
			Threshold: genai.HarmBlockOnlyHigh,
		},
	}

	// تولید محتوا
	resp, err := model.GenerateContent(ctx, genai.Text("اهمیت ایمنی آنلاین را توضیح دهید."))
	if err != nil {
		fmt.Printf("خطا در تولید محتوا: %v\n", err)
		return
	}

	// چاپ پاسخ
	for _, part := range resp.Candidates[0].Content.Parts {
		fmt.Println(part)
	}
}

```

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{
    "contents": [{
      "parts": [{"text": "اهمیت ایمنی آنلاین را توضیح دهید."}]
    }],
    "safetySettings": [
      {
        "category": "HARM_CATEGORY_HARASSMENT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_HATE_SPEECH",
        "threshold": "BLOCK_LOW_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
        "threshold": "BLOCK_MEDIUM_AND_ABOVE"
      },
      {
        "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
        "threshold": "BLOCK_ONLY_HIGH"
      }
    ]
  }'

```


### غیرفعال کردن فیلترهای ایمنی

برای موارد استفاده خاص که نیاز به کنترل کامل بر فیلترینگ محتوا دارید، می‌توانید فیلترهای ایمنی را کاملا غیرفعال کنید:

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

# غیرفعال کردن تمام فیلترهای ایمنی
safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="OFF",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="OFF",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="OFF",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="OFF",
    ),
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="پرامپت شما اینجا",
    config=types.GenerateContentConfig(safety_settings=safety_settings),
)

```

```javascript
import { GoogleGenAI, HarmCategory, HarmBlockThreshold } from "@google/genai";

const client = new GoogleGenAI({
  apiKey: process.env.AVALAI_API_KEY,
  httpOptions: { baseUrl: "https://api.avalai.ir" }
});

// غیرفعال کردن تمام فیلترهای ایمنی
const safetySettings = [
  { category: HarmCategory.HARM_CATEGORY_HARASSMENT, threshold: "OFF" },
  { category: HarmCategory.HARM_CATEGORY_HATE_SPEECH, threshold: "OFF" },
  { category: HarmCategory.HARM_CATEGORY_SEXUALLY_EXPLICIT, threshold: "OFF" },
  { category: HarmCategory.HARM_CATEGORY_DANGEROUS_CONTENT, threshold: "OFF" },
];

const response = await client.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "پرامپت شما اینجا",
  config: { safetySettings: safetySettings },
});

```

```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()
	client, _ := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")

	// غیرفعال کردن تمام فیلترهای ایمنی
	model.SafetySettings = []*genai.SafetySetting{
		{Category: genai.HarmCategoryHarassment, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategoryHateSpeech, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategorySexuallyExplicit, Threshold: genai.HarmBlockNone},
		{Category: genai.HarmCategoryDangerousContent, Threshold: genai.HarmBlockNone},
	}

	resp, _ := model.GenerateContent(ctx, genai.Text("پرامپت شما اینجا"))
	fmt.Println(resp.Candidates[0].Content.Parts[0])
}

```

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{
    "contents": [{
      "parts": [{"text": "پرامپت شما اینجا"}]
    }],
    "safetySettings": [
      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "OFF"},
      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "OFF"},
      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "OFF"},
      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "OFF"}
    ]
  }'

```


> **هشدار:** غیرفعال کردن فیلترهای ایمنی به این معناست که محتوای بالقوه مضر ممکن است تولید شود. از این گزینه با مسئولیت استفاده کنید و در صورت نیاز فیلترینگ محتوای خود را پیاده‌سازی کنید.

## استفاده از تنظیمات ایمنی با OpenAI SDK (extra_body)

هنگام استفاده از API سازگار با OpenAI در `v1/chat/completions`، می‌توانید تنظیمات ایمنی Gemini را از طریق پارامتر `extra_body` ارسال کنید. این به شما امکان می‌دهد از الگوهای آشنای OpenAI SDK استفاده کنید در حالی که به ویژگی‌های ایمنی بومی Gemini دسترسی دارید.

برای اطلاعات بیشتر درباره استفاده از `extra_body` با ارائه‌دهندگان مختلف، به [راهنمای پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md) مراجعه کنید.

### مثال پایه با OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# پیکربندی تنظیمات ایمنی از طریق extra_body
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "اهمیت ایمنی آنلاین را توضیح دهید."}],
    extra_body={
        "safety_settings": [
            {
                "category": "HARM_CATEGORY_HARASSMENT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_HATE_SPEECH",
                "threshold": "BLOCK_LOW_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                "threshold": "BLOCK_MEDIUM_AND_ABOVE",
            },
            {
                "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
                "threshold": "BLOCK_ONLY_HIGH",
            },
        ]
    },
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// پیکربندی تنظیمات ایمنی از طریق پارامترهای اضافی
const response = await client.chat.completions.create({
  model: "gemini-2.5-flash",
  messages: [
    { role: "user", content: "اهمیت ایمنی آنلاین را توضیح دهید." }
  ],
  // @ts-expect-error safety_settings پارامتر اختصاصی Gemini است
  safety_settings: [
    { category: "HARM_CATEGORY_HARASSMENT", threshold: "BLOCK_MEDIUM_AND_ABOVE" },
    { category: "HARM_CATEGORY_HATE_SPEECH", threshold: "BLOCK_LOW_AND_ABOVE" },
    { category: "HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold: "BLOCK_MEDIUM_AND_ABOVE" },
    { category: "HARM_CATEGORY_DANGEROUS_CONTENT", threshold: "BLOCK_ONLY_HIGH" },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// توجه: برای Go، ممکن است نیاز به استفاده از درخواست‌های HTTP خام
	// برای ارسال safety_settings به عنوان پارامترهای extra_body داشته باشید
	// SDK Go OpenAI ممکن است مستقیما extra_body را پشتیبانی نکند

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: "اهمیت ایمنی آنلاین را توضیح دهید.",
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash",
    "messages": [
      {"role": "user", "content": "اهمیت ایمنی آنلاین را توضیح دهید."}
    ],
    "safety_settings": [
      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_LOW_AND_ABOVE"},
      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_MEDIUM_AND_ABOVE"},
      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_ONLY_HIGH"}
    ]
  }'

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="اهمیت ایمنی آنلاین را توضیح دهید.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "اهمیت ایمنی آنلاین را توضیح دهید.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "اهمیت ایمنی آنلاین را توضیح دهید.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### غیرفعال کردن فیلترهای ایمنی با OpenAI SDK

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# غیرفعال کردن تمام فیلترهای ایمنی
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "پرامپت شما اینجا"}],
    extra_body={
        "safety_settings": [
            {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
            {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"},
        ]
    },
)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// غیرفعال کردن تمام فیلترهای ایمنی
const response = await client.chat.completions.create({
  model: "gemini-2.5-flash",
  messages: [{ role: "user", content: "پرامپت شما اینجا" }],
  // @ts-expect-error safety_settings پارامتر اختصاصی Gemini است
  safety_settings: [
    { category: "HARM_CATEGORY_HARASSMENT", threshold: "BLOCK_NONE" },
    { category: "HARM_CATEGORY_HATE_SPEECH", threshold: "BLOCK_NONE" },
    { category: "HARM_CATEGORY_SEXUALLY_EXPLICIT", threshold: "BLOCK_NONE" },
    { category: "HARM_CATEGORY_DANGEROUS_CONTENT", threshold: "BLOCK_NONE" },
  ],
});

```

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash",
    "messages": [{"role": "user", "content": "پرامپت شما اینجا"}],
    "safety_settings": [
      {"category": "HARM_CATEGORY_HARASSMENT", "threshold": "BLOCK_NONE"},
      {"category": "HARM_CATEGORY_HATE_SPEECH", "threshold": "BLOCK_NONE"},
      {"category": "HARM_CATEGORY_SEXUALLY_EXPLICIT", "threshold": "BLOCK_NONE"},
      {"category": "HARM_CATEGORY_DANGEROUS_CONTENT", "threshold": "BLOCK_NONE"}
    ]
  }'

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="پرامپت شما اینجا",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "پرامپت شما اینجا",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "پرامپت شما اینجا",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


> **هشدار:** غیرفعال کردن فیلترهای ایمنی به این معناست که محتوای بالقوه مضر ممکن است تولید شود. از این گزینه با مسئولیت استفاده کنید.

## مدیریت بازخورد ایمنی در پاسخ‌ها

هنگامی که پاسخی به دلیل تنظیمات ایمنی مسدود می‌شود، می‌توانید بازخورد ایمنی را بررسی کنید تا دلیل آن را درک کنید:

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="پرامپت شما اینجا",
)

# بررسی اینکه آیا پرامپت مسدود شده است
if response.prompt_feedback and response.prompt_feedback.block_reason:
    print(f"پرامپت مسدود شد: {response.prompt_feedback.block_reason}")

# بررسی رتبه‌بندی‌های ایمنی کاندید
if response.candidates:
    for candidate in response.candidates:
        if candidate.safety_ratings:
            for rating in candidate.safety_ratings:
                print(f"دسته: {rating.category}")
                print(f"احتمال: {rating.probability}")
                print(f"مسدود شده: {rating.blocked}")

```

```javascript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({
  apiKey: process.env.AVALAI_API_KEY,
  httpOptions: { baseUrl: "https://api.avalai.ir" }
});

const response = await client.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "پرامپت شما اینجا",
});

// بررسی اینکه آیا پرامپت مسدود شده است
if (response.promptFeedback?.blockReason) {
  console.log(`پرامپت مسدود شد: ${response.promptFeedback.blockReason}`);
}

// بررسی رتبه‌بندی‌های ایمنی کاندید
if (response.candidates) {
  for (const candidate of response.candidates) {
    if (candidate.safetyRatings) {
      for (const rating of candidate.safetyRatings) {
        console.log(`دسته: ${rating.category}`);
        console.log(`احتمال: ${rating.probability}`);
        console.log(`مسدود شده: ${rating.blocked}`);
      }
    }
  }
}

```

```go
package main

import (
	"context"
	"fmt"
	"github.com/google/generative-ai-go/genai"
	"google.golang.org/api/option"
)

func main() {
	ctx := context.Background()
	client, _ := genai.NewClient(ctx,
		option.WithAPIKey("your-avalai-api-key"),
		option.WithEndpoint("https://api.avalai.ir"))
	defer client.Close()

	model := client.GenerativeModel("gemini-2.5-flash")
	resp, err := model.GenerateContent(ctx, genai.Text("پرامپت شما اینجا"))

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	// بررسی بازخورد پرامپت
	if resp.PromptFeedback != nil {
		fmt.Printf("دلیل مسدودسازی: %v\n", resp.PromptFeedback.BlockReason)
	}

	// بررسی رتبه‌بندی‌های ایمنی کاندید
	for _, candidate := range resp.Candidates {
		for _, rating := range candidate.SafetyRatings {
			fmt.Printf("دسته: %v، احتمال: %v، مسدود شده: %v\n",
				rating.Category, rating.Probability, rating.Blocked)
		}
	}
}

```

```bash
# پاسخ شامل رتبه‌بندی‌های ایمنی در خروجی JSON خواهد بود
# ساختار پاسخ نمونه با بازخورد ایمنی:
# {
#   "candidates": [{
#     "content": {...},
#     "safetyRatings": [
#       {"category": "HARM_CATEGORY_HARASSMENT", "probability": "NEGLIGIBLE"},
#       {"category": "HARM_CATEGORY_HATE_SPEECH", "probability": "NEGLIGIBLE"}
#     ]
#   }],
#   "promptFeedback": {
#     "safetyRatings": [...]
#   }
# }

curl "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{"contents": [{"parts": [{"text": "پرامپت شما اینجا"}]}]}'

```


### فیلدهای بازخورد ایمنی

| فیلد | توضیحات |
|------|---------|
| `promptFeedback.blockReason` | دلیل مسدود شدن پرامپت (در صورت وجود) |
| `promptFeedback.safetyRatings` | رتبه‌بندی‌های ایمنی برای خود پرامپت |
| `candidates[].safetyRatings` | رتبه‌بندی‌های ایمنی برای هر پاسخ تولید شده |
| `safetyRatings[].category` | دسته آسیب در حال ارزیابی |
| `safetyRatings[].probability` | سطح احتمال (NEGLIGIBLE، LOW، MEDIUM، HIGH) |
| `safetyRatings[].blocked` | آیا محتوا برای این دسته مسدود شده است |

## مقایسه: API نظارت در مقابل تنظیمات ایمنی Gemini

### چه زمانی از API نظارت استفاده کنیم

[API نظارت](fa/api-reference/moderation.md) زمانی ایده‌آل است که:

- از مدل‌های غیر Gemini (OpenAI، Anthropic و غیره) استفاده می‌کنید
- نیاز به نظارت بر محتوای تولید شده توسط کاربر قبل از پردازش دارید
- به امتیازات دقیق دسته‌بندی برای گزارش‌دهی انطباق نیاز دارید
- به نظارت یکسان در ارائه‌دهندگان مدل مختلف نیاز دارید

### چه زمانی از تنظیمات ایمنی Gemini استفاده کنیم

تنظیمات ایمنی Gemini زمانی ایده‌آل هستند که:

- در حال حاضر از مدل‌های Gemini برای تولید استفاده می‌کنید
- می‌خواهید فراخوانی‌های API و تاخیر را به حداقل برسانید
- به فیلترینگ بلادرنگ در حین تولید محتوا نیاز دارید
- می‌خواهید آستانه‌های ایمنی را در هر درخواست سفارشی‌سازی کنید
- می‌خواهید خط لوله نظارت خود را ساده‌سازی کنید

### رویکرد ترکیبی

برای حداکثر ایمنی، استفاده از هر دو رویکرد را در نظر بگیرید:

```python
from openai import OpenAI
from google import genai
from google.genai import types

# مرحله 1: پیش‌بررسی ورودی کاربر با API نظارت
openai_client = OpenAI(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1"
)

user_input = "پیام کاربر اینجا"
moderation_result = openai_client.moderations.create(input=user_input)

if moderation_result.results[0].flagged:
    print("محتوا توسط پیش‌نظارت مسدود شد")
else:
    # مرحله 2: تولید با Gemini و تنظیمات ایمنی اضافی
    gemini_client = genai.Client(
        api_key="your-avalai-api-key",
        http_options={"base_url": "https://api.avalai.ir"},
    )

    response = gemini_client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
        config=types.GenerateContentConfig(
            safety_settings=[
                types.SafetySetting(
                    category="HARM_CATEGORY_HARASSMENT",
                    threshold="BLOCK_MEDIUM_AND_ABOVE",
                ),
            ]
        ),
    )
    print(response.text)
```

## مدل‌های پشتیبانی شده

تنظیمات ایمنی در تمام مدل‌های Gemini موجود از طریق AvalAI پشتیبانی می‌شوند:

| مدل | آستانه پیش‌فرض | توضیحات |
|-----|----------------|---------|
| gemini-2.5-flash | OFF | مدل پایدار قدیمی Flash |
| gemini-2.5-pro | OFF | قابلیت‌های استدلال پیشرفته |
| gemini-3.5-flash | OFF | مدل فعلی Flash |
| gemini-3.1-pro-preview | OFF | مدل پیش‌نمایش |

## بهترین شیوه‌ها

1. **با پیش‌فرض‌ها شروع کنید**: با تنظیمات ایمنی پیش‌فرض شروع کنید و بر اساس مورد استفاده خود تنظیم کنید
2. **کامل آزمایش کنید**: تنظیمات ایمنی خود را با موارد لبه قبل از استقرار در تولید آزمایش کنید
3. **محتوای مسدود شده را به درستی مدیریت کنید**: همیشه مدیریت خطا برای محتوای مسدود شده پیاده‌سازی کنید
4. **رویدادهای ایمنی را ثبت کنید**: پیگیری کنید که محتوا چه زمانی مسدود می‌شود برای نظارت و بهبود
5. **رویکردها را ترکیب کنید**: برای برنامه‌های حساس، استفاده از هر دو API نظارت و تنظیمات ایمنی Gemini را در نظر بگیرید
6. **انتخاب‌های خود را مستند کنید**: به وضوح مستند کنید که چرا آستانه‌های خاصی برای انطباق انتخاب شده‌اند

## منابع مرتبط

- [مدل‌های گوگل](fa/providers/google.md) - مستندات کامل مدل‌های Google Gemini
- [API نظارت](fa/api-reference/moderation.md) - endpoint نظارت سازگار با OpenAI
- [راهنمای نظارت](fa/safety/moderation-guide.md) - بهترین شیوه‌ها برای نظارت بر محتوا
- [v1beta GenAI SDK](fa/api-reference/v1beta.md) - مستندات SDK بومی Google GenAI
- [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md) - راهنمای‌های عمومی ایمنی
