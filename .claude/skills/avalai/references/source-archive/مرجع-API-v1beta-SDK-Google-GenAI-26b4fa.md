# مرجع API v1beta SDK Google GenAI

API v1beta دسترسی بومی به مدل‌های Gemini گوگل را با استفاده از SDK رسمی GenAI گوگل و طرحواره یا اسکیمای API آن فراهم می‌کند. این نقطه پایانی به شما امکان استفاده از متدهای بومی گوگل از جمله `generateContent`، `streamGenerateContent`، `embedContent`، `batchEmbedContents`، `countTokens` و `predict` از طریق زیرساخت AvalAI را می‌دهد.

> **مستندات رسمی**: برای جزئیات کامل API Gemini، به [مستندات رسمی Gemini API گوگل](https://ai.google.dev/gemini-api/docs) مراجعه کنید.

## URL پایه

```
https://api.avalai.ir
```

> **مهم**: هنگام استفاده از SDK Google GenAI با AvalAI، از `https://api.avalai.ir` به عنوان URL پایه استفاده کنید (بدون `/v1`). این با نقاط پایانی سازگار با OpenAI که از `/v1` استفاده می‌کنند، متفاوت است.

## احراز هویت

API v1beta از دو روش احراز هویت پشتیبانی می‌کند:

### روش ۱: Bearer Token (توصیه شده)
```http
Authorization: Bearer $AVALAI_API_KEY
```

### روش ۲: هدر بومی گوگل
```http
x-goog-api-key: YOUR_AVALAI_API_KEY
```

## مدل‌های پشتیبانی شده

API v1beta منحصرا از مدل‌های گوگل پشتیبانی می‌کند. می‌توانید از هر مدل Gemini موجود در AvalAI، از جمله خانواده تصویری نانو بنانا، استفاده کنید. Gemini 3.8 Flash با شناسه `gemini-3.8-flash` در دسترس است و نام مستعار `gemini-flash-latest` اکنون به این مدل اشاره می‌کند. تمام مدل‌های `imagen-*` منسوخ شده و حذف شده‌اند؛ به‌جای آن‌ها از `gemini-3.1-flash-image`، `gemini-3-pro-image` یا `gemini-2.5-flash-image` استفاده کنید.

### مدل‌های Gemini (متن، بینایی، صوتی)
- `gemini-3.8-flash`
- `gemini-flash-latest` (نام مستعار `gemini-3.8-flash`)
- `gemini-3.5-flash`
- `gemini-3.1-pro-preview`
- `gemini-3.1-flash-lite`
- `gemini-3.1-flash-lite-preview`
- `gemini-2.5-pro`
- `gemini-2.5-flash`
- `gemini-robotics-er-1.5-preview` (رباتیک)
- `gemini-3.8-flash-tts` (تبدیل متن به گفتار خلاقانه)
- `gemini-3.8-flash-lite-tts` (تبدیل متن به گفتار با توان عملیاتی بالا)
- `gemini-2.5-pro-preview-tts` (تبدیل متن به گفتار)
- `gemini-2.5-flash-preview-tts` (تبدیل متن به گفتار)

### مدل‌های تصویری نانو بنانا (Gemini)
- `gemini-3.1-flash-image` (نانو بنانا ۲) - تولید تصویر پرچمدار، جایگزین `imagen-4.0-generate-001` و `imagen-4.0-fast-generate-001`
- `gemini-3-pro-image` (نانو بنانا پرو) - تولید تصویر در سطح حرفه‌ای، جایگزین `imagen-4.0-ultra-generate-001`
- `gemini-3.1-flash-lite-image` (نانو بنانا ۲ لایت) - تولید تصویر ۱K با تأخیر پایین، جایگزین `imagen-3.0-*` و `gemini-2.5-flash-image` (که در ۲ اکتبر ۲۰۲۶ متوقف می‌شود)

> **منسوخ شده:** تمام مدل‌های `imagen-*` (`imagen-4.0-*`، `imagen-3.0-*`) از فهرست AvalAI حذف شده‌اند. به [راهنمای منسوخ‌شدن و مهاجرت](fa/news/2026-09-04-model-deprecations-and-migration-guide.md) مراجعه کنید.

برای فهرست کامل مدل‌های موجود، [مستندات مدل‌های گوگل](fa/providers/google.md) را ببینید.

## نقاط پایانی

> **توجه**: تمام نقاط پایانی کاملا با [مستندات رسمی Gemini API گوگل](https://ai.google.dev/gemini-api/docs) سازگار هستند. برای مثال‌های اضافی و توضیحات دقیق پارامترها به مستندات رسمی مراجعه کنید.

### تولید محتوا

تولید محتوای متنی با استفاده از مدل Gemini.

```http
POST /v1beta/models/{model}:generateContent
```

#### پارامترها

| پارامتر | نوع | ضروری | توضیحات |
|---------|-----|-------|---------|
| `model` | string | بله | مدل Gemini مورد استفاده (مثل `gemini-3.5-flash`) |

#### بدنه درخواست

| فیلد | نوع | ضروری | توضیحات |
|------|-----|-------|---------|
| `contents` | array | بله | آرایه‌ای از اشیا محتوا که مکالمه را نمایش می‌دهد |
| `system_instruction` | object | خیر | دستورالعمل سیستمی برای کنترل رفتار مدل |
| `generationConfig` | object | خیر | پیکربندی برای تولید |
| `safetySettings` | array | خیر | تنظیمات امنیتی برای فیلتر محتوا |
| `tools` | array | خیر | ابزارهای در دسترس مدل |

#### شی محتوا

| فیلد | نوع | ضروری | توضیحات |
|------|-----|-------|---------|
| `parts` | array | بله | آرایه‌ای از قسمت‌ها (متن، تصاویر و غیره) |
| `role` | string | بله | نقش محتوا (`user`، `model`) |

> **نکته مهم**: هنگام استفاده از API بومی Gemini v1beta، فقط نقش‌های `user` و `model` در آرایه `contents` پشتیبانی می‌شوند. نقش `user` برای پیام‌های کاربر و نقش `model` برای پاسخ‌های دستیار در تاریخچه مکالمه است. برای دستورالعمل‌های سطح سیستم، از پارامتر جداگانه `system_instruction` استفاده کنید.

#### شی دستورالعمل سیستمی

| فیلد | نوع | ضروری | توضیحات |
|------|-----|-------|---------|
| `parts` | array | بله | آرایه‌ای از قسمت‌ها حاوی متن دستورالعمل سیستمی |

#### پیکربندی تولید

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `maxOutputTokens` | integer | حداکثر تعداد توکن‌های قابل تولید |
| `temperature` | number | کنترل تصادفی بودن (۰.۰ تا ۲.۰) |
| `topP` | number | کنترل تنوع از طریق نمونه‌برداری nucleus |
| `topK` | integer | کنترل تنوع از طریق نمونه‌برداری top-k |
| `stopSequences` | array | دنباله‌هایی که تولید باید در آنجا متوقف شود |
| `thinkingConfig` | object | پیکربندی رفتار تفکر (سطوح تفکر Gemini 3.5/3.1 و بودجه‌های Gemini 2.5) |
| `responseModalities` | array | حالت‌های پاسخ (برای TTS: `["AUDIO"]`) |
| `speechConfig` | object | پیکربندی تبدیل متن به گفتار |

#### پیکربندی گفتار (speechConfig)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `voiceConfig` | object | پیکربندی صدای تک گوینده |
| `multiSpeakerVoiceConfig` | object | پیکربندی صدای چند گوینده |

#### پیکربندی صدای تک گوینده (voiceConfig)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `prebuiltVoiceConfig` | object | استفاده از صدای از پیش ساخته شده |

#### پیکربندی صدای از پیش ساخته شده (prebuiltVoiceConfig)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `voiceName` | string | نام صدا (`Kore`, `Charon`, `Puck`, `Fenrir`) |

#### پیکربندی صدای چند گوینده (multiSpeakerVoiceConfig)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `speakerVoiceConfigs` | array | آرایه‌ای از پیکربندی‌های صدای گوینده |

#### پیکربندی صدای گوینده (speakerVoiceConfig)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `speaker` | string | نام گوینده (مطابق با `speechMetadata.speaker` هر بخش متنی) |
| `voiceConfig` | object | پیکربندی صدا برای این گوینده |


#### پیکربندی تفکر (مدل‌های Gemini)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `thinkingLevel` | string | عمق استدلال برای مدل‌های Gemini 3.5/3.1 (`low`، `medium`، `high`) |
| `thinkingBudget` | integer | بودجه قدیمی تفکر Gemini 2.5 Flash بر حسب توکن (۰ تفکر را غیرفعال می‌کند) |

#### نمونه درخواست

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-3.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer $AVALAI_API_KEY' \
  -d '{
	"contents": [
		{
			"parts": [
				{
					"text": "داستان کوتاهی درباره هوش مصنوعی بنویس."
				}
			],
			"role": "user"
		}
	],
	"generationConfig": {
		"maxOutputTokens": 1000,
		"temperature": 0.7
	}
}'
```

#### نمونه با دستورالعمل‌های سیستمی

اگر نیاز به ارائه دستورالعمل‌های سطح سیستم برای هدایت رفتار مدل دارید، از پارامتر `system_instruction` استفاده کنید:

```bash
curl -i https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
	"system_instruction": {
		"parts": [
			{
				"text": "به فارسی بنویس"
			}
		]
	},
	"contents": [
		{
			"parts": [
				{
					"text": "داستان کوتاهی درباره هوش مصنوعی بنویس."
				}
			],
			"role": "user"
		}
	],
	"generationConfig": {
		"thinkingConfig": {
			"thinkingBudget": 0
		},
		"maxOutputTokens": 70,
		"stopSequences": [
			"عنوان"
		],
		"temperature": 1.0,
		"topP": 0.8,
		"topK": 10
	}
}'
```

> **نکته**: API v1beta با [مستندات رسمی API Gemini](https://ai.google.dev/gemini-api/docs/text-generation) سازگار است. اگر تناقضی مشاهده کردید، لطفا با ما در [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

#### نمونه پاسخ

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "در سال ۲۰۴۵، دکتر سارا چن در برابر بزرگترین خلقت خود ایستاد..."
          }
        ],
        "role": "model"
      },
      "finishReason": "STOP",
      "index": 0,
      "safetyRatings": [
        {
          "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
          "probability": "NEGLIGIBLE"
        }
      ]
    }
  ],
  "usageMetadata": {
    "promptTokenCount": 12,
    "candidatesTokenCount": 150,
    "totalTokenCount": 162
  }
}
```

### تولید محتوای جریانی

تولید محتوای متنی جریانی با استفاده از مدل Gemini.

```http
POST /v1beta/models/{model}:streamGenerateContent
```

فرمت درخواست مشابه `generateContent` است، اما پاسخ به صورت Server-Sent Events جریانی می‌شود.

#### نمونه درخواست

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:streamGenerateContent' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer $AVALAI_API_KEY' \
  -d '{
 "contents": [
 {
 "parts": [
 {
 "text": "Explain AI"
 }
 ],
 "role": "user"
 }
 ],
 "generationConfig": {
 "maxOutputTokens": 500
 }
 }'
```

#### نمونه پاسخ جریانی

```
[
    {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": "An"
                        }
                    ],
                    "role": "model"
                }
            }
        ],
        "usageMetadata": {
            "promptTokenCount": 4,
            "totalTokenCount": 4,
            "promptTokensDetails": [
                {
                    "modality": "TEXT",
                    "tokenCount": 4
                }
            ]
        },
        "modelVersion": "gemini-2.5-flash",
        "responseId": "sOl_aKOWPIPxMTp1fDNn6QQ"
    },
    {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": " broad term that can encompass a few different things:\n\n*   **AI-"
                        }
                    ],
                    "role": "model"
                }
            }
        ],
        "usageMetadata": {
            "promptTokenCount": 4,
            "totalTokenCount": 4,
            "promptTokensDetails": [
                {
                    "modality": "TEXT",
                    "tokenCount": 4
                }
            ]
        },
        "modelVersion": "gemini-2.5-flash",
        "responseId": "sOl_aKOWPIPxMTp1fDNn6QQ"
    },
    
    ...

    {
        "candidates": [
            {
                "content": {
                    "parts": [
                        {
                            "text": "\n\n**In summary, an AI sentence can either be a sentence created *by* an AI or a sentence being analyzed *by* an AI. It's a fundamental component of how AI interacts with and understands human language.**\n"
                        }
                    ],
                    "role": "model"
                },
                "finishReason": "STOP"
            }
        ],
        "usageMetadata": {
            "promptTokenCount": 3,
            "candidatesTokenCount": 571,
            "totalTokenCount": 574,
            "promptTokensDetails": [
                {
                    "modality": "TEXT",
                    "tokenCount": 3
                }
            ],
            "candidatesTokensDetails": [
                {
                    "modality": "TEXT",
                    "tokenCount": 571
                }
            ]
        },
        "modelVersion": "gemini-2.5-flash",
        "responseId": "sOl_aKOWPIPxMTp1fDNn6QQ"
    }
]
```

## استفاده با SDK Google GenAI

### Python

```python
from google import genai
from google.genai.types import ContentDict, PartDict

# راه‌اندازی کلاینت
client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

# تولید محتوا
contents = ContentDict(parts=[PartDict(text="سلام، حال شما چطور است؟")], role="user")

response = await client.agenerate_content(
    contents=contents, model="gemini-2.5-flash", max_tokens=100
)

print(response)
```

### جریان با Python

```python
# تولید جریانی
response = await client.agenerate_content_stream(
    contents=contents, model="gemini-2.5-flash", max_tokens=500
)

async for chunk in response:
    print(chunk)
```

<a id="gemini-38-native-text-to-speech"></a>

### تبدیل متن به گفتار بومی با Gemini ۳٫۸

برای کاربردهای جدید تبدیل متن به گفتار، `gemini-3.8-flash-tts` را برای کیفیت خلاقانه، اجرای احساسی، لهجه‌های منطقه‌ای و ثبات گفت‌وگوهای طولانی انتخاب کنید. برای توان عملیاتی بالا، تأخیر کم و خواندن متن‌های روزمره، `gemini-3.8-flash-lite-tts` مناسب‌تر است. هر دو مدل **متن دریافت می‌کنند و صوت تولید می‌کنند**؛ برای رونویسی، گفت‌وگو با ورودی صوتی، Live API یا استدلال طراحی نشده‌اند.

AvalAI این مدل‌های TTS را فقط از طریق روش‌های بومی `/v1beta/models`، مسیر `/v1/chat/completions` و مسیر `/v1/audio/speech` ارائه می‌دهد. آن‌ها را به `/v1/responses`، `/v1/messages` یا مسیر قدیمی `/v1/text:synthesize` نفرستید. ابتدا پاسخ را با یک مدل گفت‌وگومحور یا استدلالی جداگانه بنویسید و سپس متن نهایی را به TTS بدهید.

هر بخش متنی `speechMetadata` با `speaker` و `style` دارد؛ مقدار گوینده باید با `speakerVoiceConfigs` مطابقت داشته باشد. متن عیناً خوانده می‌شود، پس دستورهای نحوه بیان و برچسب گوینده را داخل متن گفتار ننویسید. برای توان عملیاتی بالاتر، فقط شناسه مدل در URL را به `gemini-3.8-flash-lite-tts` تغییر دهید. `thinkingConfig`، ابزارها، ورودی تصویر یا ورودی صوتی را به این مدل‌های TTS نفرستید.

پاسخ بومی غیرجریانی به‌طور پیش‌فرض WAV با نوع `audio/wav` است؛ برخلاف خروجی خام PCM پیش‌فرض در `gemini-3.1-flash-tts-preview` و مدل‌های قدیمی‌تر Gemini TTS. رمزگشای زیر `inlineData.mimeType` را بررسی می‌کند، بایت‌های WAV را مستقیم ذخیره می‌کند و فقط برای PCM16 با نوع `audio/L16`، نرخ ۲۴٬۰۰۰ هرتز و یک کانال هدر می‌سازد. برای نوع‌های دیگر خطا می‌دهد و قالب را از پسوند فایل حدس نمی‌زند.

```bash
curl --fail-with-body -sS \
  https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {"text": "Welcome to AvalAI.", "speechMetadata": {"speaker": "Host", "style": "Warm and welcoming."}},
        {"text": "Have a wonderful day!", "speechMetadata": {"speaker": "Guest", "style": "Cheerful and relaxed."}}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {"speaker": "Host", "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zephyr"}}},
            {"speaker": "Guest", "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Puck"}}}
          ]
        }
      }
    }
  }' \
  --output native-speech.json
```

```python
import base64
import json
import wave
from pathlib import Path

response = json.loads(Path("native-speech.json").read_text())
parts = response["candidates"][0]["content"]["parts"]
audio_parts = [part["inlineData"] for part in parts if "inlineData" in part]
if not audio_parts:
    raise ValueError("No audio returned; inspect the response before decoding")

for index, audio in enumerate(audio_parts):
    data = base64.b64decode(audio["data"], validate=True)
    mime_type = audio["mimeType"].split(";", 1)[0].strip().lower()
    filename = f"speech-{index}.wav"
    if mime_type == "audio/wav":
        # فایل WAV هدر RIFF دارد؛ آن را بدون افزودن هدر دوباره ذخیره کنید.
        Path(filename).write_bytes(data)
    elif mime_type == "audio/l16":
        # خروجی PCM16 مدل Gemini: نرخ ۲۴٬۰۰۰ هرتز، یک کانال و دو بایت برای هر نمونه.
        with wave.open(filename, "wb") as output:
            output.setnchannels(1)
            output.setsampwidth(2)
            output.setframerate(24000)
            output.writeframes(data)
    else:
        raise ValueError(f"Unsupported audio MIME type: {audio['mimeType']}")
```

برای مهاجرت و تبدیل PCM مدل قدیمی، [راهنمای تبدیل متن به گفتار](fa/guides/text-to-speech.md#migrate-to-gemini-38-tts) را ببینید.

## پشتیبانی چندوجهی

API v1beta از ورودی‌های چندوجهی شامل متن، تصاویر، صدا و ویدیو پشتیبانی می‌کند.

### نمونه ورودی تصویر

```python
# نکته: تصاویر باید برای مدل‌های Gemini به صورت base64 کدگذاری شوند
contents = ContentDict(
    parts=[
        PartDict(text="در این تصویر چه چیزی هست؟"),
        PartDict(
            inline_data={"mime_type": "image/jpeg", "data": "base64_encoded_image_data"}
        ),
    ],
    role="user",
)

response = await client.agenerate_content(contents=contents, model="gemini-2.5-flash")
```

## پایه‌گذاری با جستجوی گوگل (Grounding with Google Search)

پایه‌گذاری با جستجوی گوگل مدل‌های Gemini را به محتوای وب بلادرنگ متصل می‌کند و با تمام زبان‌های موجود کار می‌کند. این امکان به Gemini اجازه می‌دهد پاسخ‌های دقیق‌تر ارائه دهد و منابع قابل تأیید را فراتر از تاریخ قطع دانش خود ذکر کند.

### مزایای کلیدی

- **افزایش دقت واقعی**: کاهش توهمات مدل با مبنا قرار دادن پاسخ‌ها بر اطلاعات دنیای واقعی
- **دسترسی به اطلاعات بلادرنگ**: پاسخ به سؤالات درباره رویدادها و موضوعات اخیر
- **ارائه استنادات**: ایجاد اعتماد کاربر با نمایش منابع ادعاهای مدل

### نمونه درخواست

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "چه کسی یورو ۲۰۲۴ را برد؟"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

### استفاده با SDK Google GenAI

#### Python

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="چه کسی یورو ۲۰۲۴ را برد؟",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    ),
)

print(response.text)
```

#### JavaScript

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}
});

const response = await ai.models.generateContent({
    model: "gemini-2.5-flash",
    contents: "چه کسی یورو ۲۰۲۴ را برد؟",
    config: {
        tools: [{ googleSearch: {} }]
    }
});

console.log(response.text);
```

### نحوه کار پایه‌گذاری

وقتی ابزار `google_search` را فعال می‌کنید، مدل به طور خودکار کل گردش کار را مدیریت می‌کند:

1. **تحلیل پرامپت**: مدل پرامپت را تحلیل می‌کند و تعیین می‌کند که آیا جستجوی گوگل می‌تواند پاسخ را بهبود بخشد
2. **جستجوی گوگل**: در صورت نیاز، مدل به طور خودکار یک یا چند پرس‌وجوی جستجو تولید و اجرا می‌کند
3. **پردازش نتایج جستجو**: مدل نتایج جستجو را پردازش، اطلاعات را ترکیب و پاسخ را فرمول‌بندی می‌کند
4. **پاسخ پایه‌گذاری‌شده**: API یک پاسخ نهایی پایه‌گذاری‌شده بر نتایج جستجو با استنادات برمی‌گرداند

### درک پاسخ پایه‌گذاری

هنگامی که یک پاسخ با موفقیت پایه‌گذاری می‌شود، پاسخ شامل یک فیلد `groundingMetadata` است:

```json
{
  "candidates": [
    {
      "content": {
        "parts": [
          {
            "text": "اسپانیا یورو ۲۰۲۴ را برد و انگلستان را ۲-۱ در فینال شکست داد. این پیروزی چهارمین عنوان قهرمانی اروپای رکوردشکن اسپانیا را رقم زد."
          }
        ],
        "role": "model"
      },
      "groundingMetadata": {
        "webSearchQueries": [
          "برنده یورو ۲۰۲۴",
          "چه کسی یورو ۲۰۲۴ را برد"
        ],
        "searchEntryPoint": {
          "renderedContent": "<!-- HTML و CSS برای ویجت جستجو -->"
        },
        "groundingChunks": [
          {"web": {"uri": "https://...", "title": "aljazeera.com"}},

            {"web": {"uri": "https://...", "title": "uefa.com"}}

            ],
            "groundingSupports": [
              {
                "segment": {"startIndex": 0, "endIndex": 85, "text": "اسپانیا یورو ۲۰۲۴ را برد..."},
                "groundingChunkIndices": [0]
              },
              {
                "segment": {"startIndex": 86, "endIndex": 210, "text": "این پیروزی چهارمین..."},
                "groundingChunkIndices": [0, 1]
              }
            ]
          }
        }
      ]
    }
```

`groundingMetadata` شامل موارد زیر است:

| فیلد | توضیحات |
|-------|-------------|
| `webSearchQueries` | آرایه‌ای از پرس‌وجوهای جستجوی استفاده‌شده. مفید برای اشکال‌زدایی و درک فرآیند استدلال مدل |
| `searchEntryPoint` | شامل HTML و CSS برای رندر کردن پیشنهادات جستجوی مورد نیاز |
| `groundingChunks` | آرایه‌ای از اشیاء حاوی منابع وب (uri و title) |
| `groundingSupports` | آرایه‌ای از قطعات که متن پاسخ مدل را به منابع متصل می‌کند. هر قطعه یک بخش متنی (تعریف‌شده با startIndex و endIndex) را به یک یا چند groundingChunkIndices پیوند می‌دهد |

### نسبت‌دهی منابع با استنادات درون‌خطی

می‌توانید از فیلدهای `groundingSupports` و `groundingChunks` برای ایجاد استنادات درون‌خطی استفاده کنید:

```python
def add_citations(response):
    text = response.text
    supports = response.candidates[0].grounding_metadata.grounding_supports
    chunks = response.candidates[0].grounding_metadata.grounding_chunks

    # مرتب‌سازی supports بر اساس end_index به صورت نزولی برای جلوگیری از مشکلات جابجایی هنگام درج
    sorted_supports = sorted(supports, key=lambda s: s.segment.end_index, reverse=True)

    for support in sorted_supports:
        end_index = support.segment.end_index
        if support.grounding_chunk_indices:
            # ایجاد رشته استناد مانند [1](link1)[2](link2)
            citation_links = []
            for i in support.grounding_chunk_indices:
                if i < len(chunks):
                    uri = chunks[i].web.uri
                    citation_links.append(f"[{i + 1}]({uri})")

            citation_string = ", ".join(citation_links)
            text = text[:end_index] + citation_string + text[end_index:]

    return text


# استفاده با پاسخ پایه‌گذاری‌شده
text_with_citations = add_citations(response)
print(text_with_citations)
```

### مدل‌های پشتیبانی‌شده

| مدل | پایه‌گذاری با جستجوی گوگل |
|-------|------------------------------|
| Gemini 3.1 Pro Preview | ✔️ |
| Gemini 3 Pro Preview | ✔️ |
| Gemini 3 Flash Preview | ✔️ |
| Gemini 2.5 Pro | ✔️ |
| Gemini 2.5 Flash | ✔️ |
| Gemini 2.5 Flash-Lite | ✔️ |

> **توجه**: مدل‌های قدیمی‌تر از ابزار `google_search_retrieval` استفاده می‌کنند. برای تمام مدل‌های فعلی، از ابزار `google_search` همانطور که در مثال‌ها نشان داده شده استفاده کنید.

### قیمت‌گذاری

هنگام استفاده از پایه‌گذاری با جستجوی گوگل با مدل‌های Gemini 3، پروژه شما برای هر پرس‌وجوی جستجویی که مدل تصمیم به اجرای آن می‌گیرد صورتحساب می‌شود. اگر مدل تصمیم بگیرد چندین پرس‌وجوی جستجو برای پاسخ به یک پرامپت اجرا کند (مثلا جستجوی "برنده یورو ۲۰۲۴" و "نتیجه فینال اسپانیا - انگلستان یورو ۲۰۲۴" در یک فراخوانی API)، این به عنوان چندین استفاده قابل صورتحساب از ابزار برای آن درخواست محاسبه می‌شود.

برای مدل‌های Gemini 2.5 و قدیمی‌تر، پروژه شما به ازای هر پرامپت که از پایه‌گذاری جستجو استفاده می‌کند صورتحساب می‌شود.

برای اطلاعات دقیق قیمت‌گذاری، [صفحه قیمت‌گذاری](fa/pricing.md) را ببینید.

## تعبیه‌سازی محتوا (Embed Content)

تولید تعبیه‌سازی‌ متن با استفاده از مدل‌های تعبیه‌سازی Gemini از طریق نقطه پایانی SDK بومی Google GenAI.

```http
POST /v1beta/models/{model}:embedContent
```

### پارامترها

| پارامتر | نوع | الزامی | توضیحات |
|-----------|------|----------|-------------|
| `model` | string | بله | مدل تعبیه‌سازی Gemini مورد استفاده (مثل `gemini-embedding-001`) |

### بدنه درخواست

| فیلد | نوع | الزامی | توضیحات |
|-------|------|----------|-------------|
| `contents` | array | بله | آرایه‌ای از اشیاء محتوا برای تعبیه‌سازی |
| `embedding_config` | object | خیر | تنظیمات برای تولید تعبیه‌سازی |

### شیء محتوا

| فیلد | نوع | الزامی | توضیحات |
|-------|------|----------|-------------|
| `parts` | array | بله | آرایه‌ای از قسمت‌ها حاوی متن برای تعبیه‌سازی |

### تنظیمات تعبیه‌سازی

| فیلد | نوع | توضیحات |
|-------|------|-------------|
| `task_type` | string | نوع وظیفه برای بهینه‌سازی (مثل "SEMANTIC_SIMILARITY"، "CLASSIFICATION") |
| `output_dimensionality` | integer | تعداد ابعاد برای تعبیه‌سازی خروجی (۱۲۸-۳۰۷۲) |

### مدل‌های پشتیبانی‌شده

نقطه پایانی embedContent از مدل‌های تعبیه‌سازی Gemini زیر پشتیبانی می‌کند:

- `gemini-embedding-2` (نام مستعار: `gemini-embedding-2-preview`) - مدل تعبیه‌سازی چندوجهی نسل بعدی با پشتیبانی بومی از متن، تصویر، صدا، ویدیو و PDF از طریق بخش‌های `inline_data`
- `gemini-embedding-001` - مدل تعبیه‌سازی پایدار با ویژگی‌های پیشرفته

### مثال درخواست

#### تعبیه‌سازی پایه

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "معنای زندگی چیست؟"
          }
        ]
      }
    ]
  }'
```

#### تعبیه‌سازی پیشرفته با نوع وظیفه

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "معنای زندگی چیست؟"
          }
        ]
      },
      {
        "parts": [
          {
            "text": "هدف وجود چیست؟"
          }
        ]
      }
    ],
    "embedding_config": {
      "task_type": "SEMANTIC_SIMILARITY",
      "output_dimensionality": 768
    }
  }'
```

### مثال پاسخ

```json
{
  "embeddings": [
    {
      "values": [
        0.0023064255,
        -0.009327292,
        -0.0028842222,
        ...
      ]
    }
  ]
}
```

### استفاده با SDK Google GenAI

#### پایتون

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# تعبیه‌سازی پایه
result = client.models.embed_content(
    model="gemini-embedding-001", contents="معنای زندگی چیست؟"
)

print(f"ابعاد تعبیه‌سازی: {len(result.embeddings[0].values)}")

# تعبیه‌سازی پیشرفته با نوع وظیفه و ابعاد سفارشی
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY", output_dimensionality=768
    ),
)

for i, embedding in enumerate(result.embeddings):
    print(f"تعبیه‌سازی {i}: {len(embedding.values)} بعد")
```

#### جاوااسکریپت

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

// تعبیه‌سازی پایه
const response = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: "معنای زندگی چیست؟"
});

console.log(`ابعاد تعبیه‌سازی: ${response.embeddings[0].values.length}`);

// تعبیه‌سازی پیشرفته با نوع وظیفه
const advancedResponse = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟"
    ],
    taskType: "SEMANTIC_SIMILARITY",
    outputDimensionality: 768
});

console.log(`${advancedResponse.embeddings.length} تعبیه‌سازی تولید شد`);
```

### انواع وظایف پشتیبانی‌شده

| نوع وظیفه | توضیحات | موارد استفاده |
|-----------|-------------|-----------|
| **SEMANTIC_SIMILARITY** | بهینه‌سازی شده برای اندازه‌گیری شباهت متن | سیستم‌های توصیه، تشخیص تکراری |
| **CLASSIFICATION** | بهینه‌سازی شده برای وظایف طبقه‌بندی متن | تحلیل احساسات، تشخیص اسپم |
| **CLUSTERING** | بهینه‌سازی شده برای گروه‌بندی متن‌های مشابه | سازماندهی اسناد، تحقیقات بازار |
| **RETRIEVAL_DOCUMENT** | بهینه‌سازی شده برای نمایه‌سازی اسناد | سیستم‌های RAG، موتورهای جستجو |
| **RETRIEVAL_QUERY** | بهینه‌سازی شده برای پرس‌وجوهای جستجو | برنامه‌های جستجوی سفارشی |
| **CODE_RETRIEVAL_QUERY** | بهینه‌سازی شده برای پرس‌وجوهای جستجوی کد | جستجوی کد، جستجوی مستندات |
| **QUESTION_ANSWERING** | بهینه‌سازی شده برای سیستم‌های پرسش و پاسخ | چت‌بات‌ها، سیستم‌های FAQ |
| **FACT_VERIFICATION** | بهینه‌سازی شده برای بررسی حقایق | سیستم‌های تایید خودکار |

### ابعاد خروجی

تعبیه‌سازی‌ Gemini از یادگیری نمایش ماتریوشکا (MRL) پشتیبانی می‌کنند که امکان ابعاد خروجی انعطاف‌پذیر را فراهم می‌کند:

- **۳۰۷۲ بعد**: ظرفیت کامل مدل (پیش‌فرض، از قبل نرمال‌سازی شده)
- **۱۵۳۶ بعد**: عملکرد متعادل و کارایی
- **۷۶۸ بعد**: کارآمد با عملکرد خوب
- **۵۱۲ بعد**: فشرده با عملکرد قابل قبول
- **۲۵۶ بعد**: بسیار فشرده
- **۱۲۸ بعد**: حداقل اندازه

> **مهم**: برای ابعاد غیر از ۳۰۷۲، تعبیه‌سازی‌‌ها را برای عملکرد بهینه شباهت معنایی نرمال‌سازی کنید.

### فرمت پاسخ

نقطه پایانی embedContent تعبیه‌سازی‌‌ها را در فرمت زیر برمی‌گرداند:

| فیلد | نوع | توضیحات |
|-------|------|-------------|
| `embeddings` | array | آرایه‌ای از اشیاء تعبیه‌سازی |

#### شیء تعبیه‌سازی

| فیلد | نوع | توضیحات |
|-------|------|-------------|
| `values` | array | آرایه‌ای از اعداد اعشاری نمایانگر بردار تعبیه‌سازی |

## تعبیه‌سازی دسته‌ای محتوا (Batch Embed Contents)

تولید تعبیه‌سازی برای چندین قطعه متن به صورت همزمان با استفاده از مدل‌های تعبیه‌سازی Gemini. این روش کارآمدتر از ارسال درخواست‌های جداگانه `embedContent` برای پردازش چندین متن است.

```http
POST /v1beta/models/{model}:batchEmbedContents
```

### پارامترها

| پارامتر | نوع | الزامی | توضیحات |
|-----------|------|----------|-------------|
| `model` | string | بله | مدل تعبیه‌سازی Gemini مورد استفاده (مثل `gemini-embedding-001`) |

### بدنه درخواست

| فیلد | نوع | الزامی | توضیحات |
|-------|------|----------|-------------|
| `requests` | array | بله | آرایه‌ای از اشیاء درخواست تعبیه‌سازی |

### شیء درخواست تعبیه‌سازی

| فیلد | نوع | الزامی | توضیحات |
|-------|------|----------|-------------|
| `model` | string | بله | مدل مورد استفاده (باید با پارامتر URL مطابقت داشته باشد) |
| `content` | object | بله | شیء محتوا حاوی متن برای تعبیه‌سازی |
| `task_type` | string | خیر | نوع وظیفه برای بهینه‌سازی |
| `output_dimensionality` | integer | خیر | اندازه ابعاد خروجی (۱۲۸-۳۰۷۲) |

### مثال درخواست

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-embedding-001:batchEmbedContents' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "requests": [
      {
        "model": "models/gemini-embedding-001",
        "content": {
          "parts": [{
            "text": "معنای زندگی چیست؟"
          }]
        }
      },
      {
        "model": "models/gemini-embedding-001",
        "content": {
          "parts": [{
            "text": "چه مقدار چوب یک چاک‌وود می‌تواند بتکند؟"
          }]
        }
      },
      {
        "model": "models/gemini-embedding-001",
        "content": {
          "parts": [{
            "text": "مغز چگونه کار می‌کند؟"
          }]
        }
      }
    ]
  }'
```

### مثال پاسخ

```json
{
  "embeddings": [
    {
      "values": [0.0023064255, -0.009327292, -0.0028842222, ...]
    },
    {
      "values": [0.0034521123, -0.007234567, -0.0021234567, ...]
    },
    {
      "values": [0.0045678901, -0.008765432, -0.0012345678, ...]
    }
  ]
}
```

### استفاده با SDK Google GenAI

#### پایتون

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# تعبیه‌سازی دسته‌ای چندین متن
texts = [
    "معنای زندگی چیست؟",
    "چه مقدار چوب یک چاک‌وود می‌تواند بتکند؟",
    "مغز چگونه کار می‌کند؟",
]

# توجه: از embed_content با لیستی از متن‌ها استفاده کنید
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=texts,
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY", output_dimensionality=768
    ),
)

for i, embedding in enumerate(result.embeddings):
    print(f"متن {i}: {len(embedding.values)} بعد")
```

## شمارش توکن‌ها (Count Tokens)

شمارش تعداد توکن‌ها در محتوا قبل از ارسال به مدل. این به شما کمک می‌کند تا استفاده از توکن را درک کرده و در محدودیت‌های مدل باقی بمانید.

```http
POST /v1beta/models/{model}:countTokens
```

### پارامترها

| پارامتر | نوع | الزامی | توضیحات |
|-----------|------|----------|-------------|
| `model` | string | بله | مدل Gemini مورد استفاده (مثل `gemini-2.5-flash`) |

### بدنه درخواست

| فیلد | نوع | الزامی | توضیحات |
|-------|------|----------|-------------|
| `contents` | array | بله | آرایه‌ای از اشیاء محتوا برای شمارش توکن |
| `system_instruction` | object | خیر | دستورالعمل سیستمی (در شمارش توکن لحاظ می‌شود) |
| `tools` | array | خیر | ابزارها/توابع (در شمارش توکن لحاظ می‌شوند) |

### مثال درخواست

#### شمارش پایه توکن

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:countTokens' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
      {
        "parts": [
          {
            "text": "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد."
          }
        ],
        "role": "user"
      }
    ]
  }'
```

#### شمارش توکن با دستورالعمل‌های سیستمی

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:countTokens' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "system_instruction": {
      "parts": [
        {
          "text": "شما یک دستیار مفید هستید."
        }
      ]
    },
    "contents": [
      {
        "parts": [
          {
            "text": "معنای زندگی چیست؟"
          }
        ],
        "role": "user"
      }
    ]
  }'
```

### مثال پاسخ

```json
{
  "totalTokens": 11
}
```

### استفاده با SDK Google GenAI

#### پایتون

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# شمارش توکن برای متن ساده
prompt = "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد."
result = client.models.count_tokens(model="gemini-2.5-flash", contents=prompt)
print(f"مجموع توکن‌ها: {result.total_tokens}")

# شمارش توکن برای یک مکالمه
chat_history = [
    types.Content(role="user", parts=[types.Part(text="سلام، اسم من باب است")]),
    types.Content(role="model", parts=[types.Part(text="سلام باب!")]),
    types.Content(
        role="user",
        parts=[types.Part(text="در یک جمله توضیح دهید کامپیوتر چگونه کار می‌کند.")],
    ),
]

result = client.models.count_tokens(model="gemini-2.5-flash", contents=chat_history)
print(f"مجموع توکن‌ها در مکالمه: {result.total_tokens}")

# شمارش توکن با دستورالعمل سیستمی
result = client.models.count_tokens(
    model="gemini-2.5-flash",
    contents=prompt,
    config=types.GenerateContentConfig(system_instruction="شما یک دستیار مفید هستید."),
)
print(f"مجموع توکن‌ها با دستورالعمل سیستمی: {result.total_tokens}")
```

#### جاوااسکریپت

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {apiVersion: "v1beta", baseUrl: "https://api.avalai.ir"}
});

// شمارش توکن برای متن ساده
const result = await ai.models.countTokens({
    model: "gemini-2.5-flash",
    contents: "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد."
});

console.log(`مجموع توکن‌ها: ${result.totalTokens}`);

// شمارش توکن برای محتوای چندوجهی
const multimodalResult = await ai.models.countTokens({
    model: "gemini-2.5-flash",
    contents: [
        {
            role: "user",
            parts: [
                { text: "درباره این تصویر بگو" },
                { inlineData: { mimeType: "image/jpeg", data: base64ImageData } }
            ]
        }
    ]
});

console.log(`توکن‌های چندوجهی: ${multimodalResult.totalTokens}`);
```

### شمارش توکن برای محتوای چندوجهی

شمارش توکن برای تمام انواع ورودی کار می‌کند:

- **متن**: توکن‌سازی استاندارد (حدود ۴ کاراکتر در هر توکن)
- **تصاویر**:
  - Gemini 2.5 به بعد: تصاویر با ابعاد ≤۳۸۴ پیکسل در هر دو بعد = ۲۵۸ توکن
  - تصاویر بزرگ‌تر به کاشی‌های ۷۶۸×۷۶۸ پیکسلی تقسیم می‌شوند، هر کاشی = ۲۵۸ توکن
- **صدا**: ۳۲ توکن در ثانیه
- **ویدیو**: ۲۶۳ توکن در ثانیه

#### مثال: شمارش توکن با تصاویر

```python
from google import genai
import PIL.Image

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

image = PIL.Image.open("path/to/image.jpg")

result = client.models.count_tokens(
    model="gemini-2.5-flash", contents=["درباره این تصویر بگو", image]
)

print(f"مجموع توکن‌ها (متن + تصویر): {result.total_tokens}")
```

## Predict (تولید تصویر)

تولید تصاویر با استفاده از مدل‌های تصویری گوگل از طریق API بومی v1beta. این متد از نقطه پایانی `:predict` برای وظایف تولید تصویر استفاده می‌کند.

> **منسوخ شده:** تمام مدل‌های `imagen-*` (`imagen-4.0-ultra-generate-001`، `imagen-4.0-generate-001`، `imagen-4.0-fast-generate-001`، `imagen-3.0-generate-002`، `imagen-3.0-generate-001`، `imagen-3.0-fast-generate-001`) منسوخ شده و از فهرست AvalAI حذف شده‌اند. به خانواده نانو بنانا — `gemini-3.1-flash-image`، `gemini-3-pro-image` یا `gemini-2.5-flash-image` — از طریق `v1/chat/completions` یا نقطه پایانی بومی `:generateContent` مهاجرت کنید. به [راهنمای خانواده نانو بنانا](fa/examples/generate_images_with_nano_banana_series.md) و [راهنمای منسوخ‌شدن و مهاجرت](fa/news/2026-09-04-model-deprecations-and-migration-guide.md) مراجعه کنید.

```http
POST /v1beta/models/{model}:predict
```

### پارامترها

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|----------|
| `model` | string | بله | مدل تصویری مورد استفاده. شناسه‌های قبلی Imagen حذف شده‌اند؛ به‌جای آن‌ها از یک مدل نانو بنانا مانند `gemini-3.1-flash-image` از طریق `:generateContent` استفاده کنید. |

### مدل‌های پشتیبانی شده

- ~~`imagen-4.0-generate-001`~~ - حذف شده. از `gemini-3.1-flash-image` استفاده کنید
- ~~`imagen-4.0-ultra-generate-001`~~ - حذف شده. از `gemini-3-pro-image` استفاده کنید
- ~~`imagen-4.0-fast-generate-001`~~ - حذف شده. از `gemini-3.1-flash-image` استفاده کنید
- ~~`imagen-3.0-generate-002`~~ - حذف شده. از `gemini-3.1-flash-lite-image` استفاده کنید

### بدنه درخواست

| فیلد | نوع | الزامی | توضیحات |
|------|-----|--------|----------|
| `instances` | array | بله | آرایه‌ای از نمونه‌های درخواست تولید |
| `parameters` | object | خیر | پارامترهای پیکربندی برای تولید تصویر |

### شیء Instance

| فیلد | نوع | الزامی | توضیحات |
|------|-----|--------|----------|
| `prompt` | string | بله | توصیف متنی تصویر مورد نظر برای تولید |

### شیء Parameters

| فیلد | نوع | پیش‌فرض | توضیحات |
|------|-----|---------|----------|
| `sampleCount` | integer | 1 | تعداد تصاویر برای تولید (1-8) |
| `aspectRatio` | string | "1:1" | نسبت ابعاد تصویر ("1:1", "9:16", "16:9", "3:4", "4:3") |
| `personGeneration` | string | "allow_all" | سیاست تولید افراد ("allow_all", "allow_adult") |
| `safetyFilterLevel` | string | "block_some" | قدرت فیلتر ایمنی ("block_most", "block_some", "block_few") |
| `negativePrompt` | string | null | آنچه باید در تصویر تولید شده اجتناب شود |

### مثال درخواست

```bash
curl -X POST \
  "https://api.avalai.ir/v1beta/models/gemini-3.1-flash-image:predict" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "instances": [
      {
        "prompt": "یک باغ ژاپنی آرام با استخر ماهی کوی، شکوفه‌های گیلاس و یک پل چوبی سنتی"
      }
    ],
    "parameters": {
      "sampleCount": 1,
      "aspectRatio": "16:9"
    }
  }'
```

### مثال پاسخ

```json
{
  "predictions": [
    {
      "bytesBase64Encoded": "/9j/4AAQSkZJRgABAQAAAQABAAD...",
      "mimeType": "image/png"
    }
  ],
  "metadata": {
    "tokenMetadata": {
      "outputImageCount": {
        "gemini-3.1-flash-image": 1
      }
    }
  }
}
```

### فیلدهای پاسخ

| فیلد | نوع | توضیحات |
|------|-----|----------|
| `predictions` | array | آرایه‌ای از پیش‌بینی‌های تصویر تولید شده |
| `bytesBase64Encoded` | string | داده‌های تصویر کدگذاری شده base64 |
| `mimeType` | string | نوع MIME تصویر (معمولا "image/png") |
| `metadata` | object | متادیتای استفاده شامل تعداد توکن‌ها |

### رمزگشایی تصاویر

برای ذخیره تصویر تولید شده، رشته base64 را رمزگشایی کنید:

```python
import base64

# رمزگشایی و ذخیره تصویر
image_data = base64.b64decode(response["predictions"][0]["bytesBase64Encoded"])
with open("generated_image.png", "wb") as f:
    f.write(image_data)
```

### بهترین شیوه‌ها

1. **مهندسی پرامپت**: از پرامپت‌های دقیق و مشخص برای نتایج بهتر استفاده کنید
2. **نسبت ابعاد**: نسبت ابعاد مناسب را برای مورد استفاده خود انتخاب کنید
3. **تعداد نمونه**: چندین تصویر (2-4) تولید کنید تا نتایج متنوع دریافت کنید
4. **فیلترهای ایمنی**: فیلترهای ایمنی را بر اساس سیاست محتوای خود تنظیم کنید
5. **پرامپت‌های منفی**: از پرامپت‌های منفی برای اجتناب از عناصر ناخواسته استفاده کنید

برای مثال‌های دقیق و راهنمای مهندسی پرامپت، مراجعه کنید به:
- [تولید تصاویر با خانواده نانو بنانا](fa/examples/generate_images_with_nano_banana_series.md)
- [مستندات رسمی تولید تصویر گوگل](https://ai.google.dev/gemini-api/docs/image-generation)

## مدیریت خطا

API v1beta کدهای وضعیت HTTP استاندارد را برمی‌گرداند:

- `200` - موفقیت
- `400` - درخواست نامعتبر (پارامترهای نامعتبر)
- `401` - غیرمجاز (کلید API نامعتبر)
- `429` - درخواست‌های زیاد (محدودیت نرخ فراتر رفته)
- `500` - خطای داخلی سرور

### فرمت پاسخ خطا

```json
{
  "error": {
    "code": 400,
    "message": "فرمت درخواست نامعتبر",
    "status": "INVALID_ARGUMENT"
  }
}
```

## محدودیت‌های نرخ

محدودیت‌های نرخ برای API v1beta از همان ساختار سایر نقاط پایانی AvalAI پیروی می‌کند. برای جزئیات [مستندات محدودیت‌های نرخ](fa/guides/rate-limits.md) را ببینید.

## محدودیت‌ها

- **فقط مدل‌های گوگل**: API v1beta منحصرا از مدل‌های گوگل (Gemini، از جمله خانواده تصویری نانو بنانا) پشتیبانی می‌کند. سایر سرویس‌های گوگل در دسترس نیستند.
- **URL پایه**: هنگام پیکربندی SDK Google GenAI باید از `https://api.avalai.ir` (بدون `/v1`) استفاده کرد.
- **فرمت تصویر**: تصاویر باید به صورت داده‌های کدگذاری شده base64 ارائه شوند، نه به عنوان URL های خارجی.

## منابع مرتبط

- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [راهنمای احراز هویت](fa/api-reference/authentication.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [مستندات کتابخانه‌ها](fa/libraries.md)
- [تولید تصاویر با خانواده نانو بنانا](fa/examples/generate_images_with_nano_banana_series.md)
- [مستندات رسمی Gemini API گوگل](https://ai.google.dev/gemini-api/docs)

</div>
