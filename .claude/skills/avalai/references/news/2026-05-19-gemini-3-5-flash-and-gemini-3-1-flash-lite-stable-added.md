# News 2026-05-19-gemini-3-5-flash-and-gemini-3-1-flash-lite-stable-added: مدل پرچم‌دار Gemini 3.5 Flash اضافه شد و Gemini 3.1 Flash-Lite پایدار منتشر شد
URL: `https://docs.avalai.ir/fa/news/2026-05-19-gemini-3-5-flash-and-gemini-3-1-flash-lite-stable-added`
**تاریخ:** 2026-05-19 / (1405-02-29)

# مدل پرچم‌دار Gemini 3.5 Flash اضافه شد و Gemini 3.1 Flash-Lite پایدار منتشر شد

**تاریخ:** 2026-05-19 / (1405-02-29)

## خلاصه

اضافه شدن مدل پرچم‌دار چندوجهی و استدلالی گوگل، [`gemini-3.5-flash`](fa/providers/google.md)، و انتشار نسخه پایدار [`gemini-3.1-flash-lite`](fa/providers/google.md) را اعلام می‌کنیم. هر دو مدل اکنون از طریق endpoint سازگار با OpenAI یعنی `v1/chat/completions` و endpoint بومی Gemini یعنی `v1beta/models` در دسترس هستند.


## خلاصه قیمت‌گذاری

| مدل | ورودی ($/1M توکن) | ورودی کش‌شده ($/1M توکن) | خروجی ($/1M توکن) | ورودی صوتی | صوت کش‌شده | خروجی صوتی |
|-----|------------------|--------------------------|-------------------|-------------|------------|-------------|
| `gemini-3.5-flash` | $1.50 | $0.25 | $9.00 | $1.00 | $0.50 | $1.00 |
| `gemini-3.1-flash-lite` | $0.25 | $0.025 | $1.50 | $0.50 | $0.05 | $1.50 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه Gemini 3.5 Flash (سازگار با OpenAI)

<!-- tabs:start -->

#### **bash**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "Outline a robust strategy to migrate a large monolithic Python service to event-driven microservices."
      }
    ]
  }'
```

#### **python**

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "Outline a robust strategy to migrate a large monolithic Python service to event-driven microservices.",
        }
    ],
)

print(response.choices[0].message.content)
```

#### **javascript**

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.5-flash",
  messages: [
    {
      role: "user",
      content:
        "Outline a robust strategy to migrate a large monolithic Python service to event-driven microservices.",
    },
  ],
});

console.log(response.choices[0].message.content);
```

<!-- tabs:end -->

**پاسخ:**

```json
{
  "id": "chatcmpl-abc789",
  "created": 1747641600,
  "model": "gemini-3.5-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "A robust migration strategy starts with the strangler-fig pattern: identify bounded contexts, expose them behind a stable API, then incrementally extract each context into an independent service while keeping the monolith authoritative until cut-over. Introduce an event backbone (e.g., Kafka or Pub/Sub) early, define outbox-based publishing for transactional integrity, and require contract tests for every new service. Plan observability, schema evolution, and rollback paths before touching production traffic.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 92,
    "prompt_tokens": 23,
    "total_tokens": 115,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 23,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0008625000",
    "irt": 98.84,
    "exchange_rate": 114600
  }
}
```

### Gemini 3.5 Flash با پیکربندی تفکر

<!-- tabs:start -->

#### **bash**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "A train leaves Station A at 8:00 AM traveling at 60 km/h. Another train leaves Station B at 9:00 AM traveling at 80 km/h toward Station A. The stations are 280 km apart. When and where do they meet?"
      }
    ],
    "extra_body": {
      "generationConfig": {
        "thinkingConfig": {
          "thinkingLevel": "high"
        }
      }
    }
  }'
```

#### **python**

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "A train leaves Station A at 8:00 AM traveling at 60 km/h. Another train leaves Station B at 9:00 AM traveling at 80 km/h toward Station A. The stations are 280 km apart. When and where do they meet?",
        }
    ],
    extra_body={"generationConfig": {"thinkingConfig": {"thinkingLevel": "high"}}},
)

print(response.choices[0].message.content)
```

#### **javascript**

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.5-flash",
  messages: [
    {
      role: "user",
      content:
        "A train leaves Station A at 8:00 AM traveling at 60 km/h. Another train leaves Station B at 9:00 AM traveling at 80 km/h toward Station A. The stations are 280 km apart. When and where do they meet?",
    },
  ],
  // @ts-ignore - extra_body is supported by AvalAI for Gemini-specific options
  extra_body: {
    generationConfig: { thinkingConfig: { thinkingLevel: "high" } },
  },
});

console.log(response.choices[0].message.content);
```

<!-- tabs:end -->

### Gemini 3.5 Flash از طریق endpoint بومی v1beta

<!-- tabs:start -->

#### **bash**

```bash
curl https://api.avalai.ir/v1beta/models/gemini-3.5-flash:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "Summarize the main advantages of event-driven architectures in three bullet points."}
        ]
      }
    ],
    "generationConfig": {
      "thinkingConfig": {"thinkingLevel": "medium"}
    }
  }'
```

#### **python**

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"base_url": "https://api.avalai.ir"},
)

response = client.models.generate_content(
    model="gemini-3.5-flash",
    contents="Summarize the main advantages of event-driven architectures in three bullet points.",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_level="medium"),
    ),
)

print(response.text)
```

#### **javascript**

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
  apiKey: process.env.AVALAI_API_KEY,
  httpOptions: { baseUrl: "https://api.avalai.ir" },
});

const response = await ai.models.generateContent({
  model: "gemini-3.5-flash",
  contents:
    "Summarize the main advantages of event-driven architectures in three bullet points.",
  config: {
    thinkingConfig: { thinkingLevel: "medium" },
  },
});

console.log(response.text);
```

<!-- tabs:end -->

### نمونه Gemini 3.1 Flash-Lite پایدار

<!-- tabs:start -->

#### **bash**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-lite",
    "messages": [
      {
        "role": "user",
        "content": "Classify the following support ticket into one of: billing, technical, account, other. Ticket: I cannot reset my password and the email link has expired."
      }
    ]
  }'
```

#### **python**

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[
        {
            "role": "user",
            "content": "Classify the following support ticket into one of: billing, technical, account, other. Ticket: I cannot reset my password and the email link has expired.",
        }
    ],
)

print(response.choices[0].message.content)
```

#### **javascript**

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.1-flash-lite",
  messages: [
    {
      role: "user",
      content:
        "Classify the following support ticket into one of: billing, technical, account, other. Ticket: I cannot reset my password and the email link has expired.",
    },
  ],
});

console.log(response.choices[0].message.content);
```

<!-- tabs:end -->

**پاسخ:**

```json
{
  "id": "chatcmpl-def456",
  "created": 1747641900,
  "model": "gemini-3.1-flash-lite",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "account",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 2,
    "prompt_tokens": 41,
    "total_tokens": 43,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 41,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000132500",
    "irt": 1.52,
    "exchange_rate": 114600
  }
}
```

### Gemini 3.1 Flash-Lite از طریق endpoint بومی v1beta

```bash
curl https://api.avalai.ir/v1beta/models/gemini-3.1-flash-lite:generateContent \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "contents": [
      {
        "role": "user",
        "parts": [
          {"text": "Extract the company names from: Apple announced a partnership with OpenAI and Microsoft this quarter."}
        ]
      }
    ]
  }'
```

---

## نکات مهاجرت

- یکپارچه‌سازی‌های موجود که از [`gemini-3.1-flash-lite-preview`](fa/providers/google.md) استفاده می‌کنند، می‌توانند بدون تغییر در کد یا قیمت‌گذاری به alias پایدار [`gemini-3.1-flash-lite`](fa/providers/google.md) مهاجرت کنند.
- alias نسخه preview برای سازگاری عقب‌رو همچنان در دسترس می‌ماند.
- [`gemini-3.5-flash`](fa/providers/google.md) یک مدل پرچم‌دار Flash جداگانه و توانمندتر است و جایگزین مستقیم [`gemini-3.1-flash-lite`](fa/providers/google.md) نیست. انتخاب را بر اساس تعادل کیفیت و هزینه انجام دهید:
  - از [`gemini-3.5-flash`](fa/providers/google.md) برای کارهای عامل‌محور، کدنویسی، استدلال چندوجهی و زمینه طولانی که کیفیت اهمیت بالاتری دارد استفاده کنید.
  - از [`gemini-3.1-flash-lite`](fa/providers/google.md) برای دسته‌بندی، استخراج، ترجمه و مسیریابی پرترافیک که کمترین هزینه اولویت اصلی است استفاده کنید.

---

## مستندات

- [مستندات مدل‌های Google Gemini](fa/providers/google.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API بومی Gemini v1beta](fa/api-reference/v1beta.md)
- [مرجع Chat Completions API](fa/api-reference/chat.md)
- [فهرست مدل‌ها](fa/models/index.md)
