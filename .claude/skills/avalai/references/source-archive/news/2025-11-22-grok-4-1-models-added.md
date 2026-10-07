# مدل‌های جدید X.AI: Grok-4.1 Fast Reasoning و Non-Reasoning

**تاریخ:** 1404-09-01 / (2025-11-22)

## خلاصه

ما افزودن دو مدل جدید Grok-4.1 از X.AI را به پلتفرم AvalAI اعلام می‌کنیم. این مدل‌های مالتی‌مودال پیشرفته برای فراخوانی ابزار عاملی (agentic tool calling) با کارایی بالا بهینه‌سازی شده‌اند و دارای پنجره زمینه 2 میلیون توکنی و پشتیبانی از فراخوانی تابع، خروجی‌های ساختاریافته و قابلیت‌های استدلال هستند.

---

## جزئیات

### X.AI

ما دو نسخه از مدل Grok-4.1 Fast را اضافه کرده‌ایم که به طور خاص برای گردش‌های کاری عاملی با کارایی بالا طراحی شده‌اند:

- **grok-4-1-fast-reasoning**: مدل مالتی‌مودال پیشرفته با قابلیت‌های استدلال گسترده برای حل مسائل پیچیده. [مستندات](fa/providers/xai.md)
- **grok-4-1-fast-non-reasoning**: مدل مالتی‌مودال پیشرفته بهینه‌شده برای پاسخ‌های سریع بدون استدلال گسترده. [مستندات](fa/providers/xai.md)

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 2,000,000 توکن برای مدیریت مکالمات و اسناد گسترده
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته و پشتیبانی از استدلال
- **پشتیبانی مالتی‌مودال**: پردازش متن و تصاویر در یک درخواست
- **فراخوانی ابزار عاملی**: بهینه‌شده برای گردش‌های کاری عامل خودکار
- **کش کردن پرامپت**: کاهش هزینه‌ها با توکن‌های ورودی کش‌شده به قیمت $0.05/1M توکن

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-------|-------|--------------|--------|
| grok-4-1-fast-reasoning | $0.20/1M توکن | $0.05/1M توکن | $0.50/1M توکن |
| grok-4-1-fast-non-reasoning | $0.20/1M توکن | $0.05/1M توکن | $0.50/1M توکن |

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-1-fast-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "your-avalai-api-key",
  "created": 1732262400,
  "model": "grok-4-1-fast-reasoning",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "درهم‌تنیدگی کوانتومی پدیده‌ای است که در آن دو یا چند ذره به گونه‌ای به هم متصل می‌شوند که حالت یک ذره فورا بر حالت ذره دیگر تاثیر می‌گذارد، صرف‌نظر از فاصله بین آن‌ها. فکر کنید مانند یک جفت تاس جادویی: وقتی یکی را می‌اندازید و عدد شش می‌آید، تاس دیگر خودکار عدد یک را نشان می‌دهد، مهم نیست چقدر از هم دور باشند. این اتصال حتی در فواصل بسیار زیاد نیز باقی می‌ماند که اینشتین آن را «عمل ترسناک از راه دور» نامید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 95,
    "prompt_tokens": 15,
    "total_tokens": 110,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 15,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000505000",
    "irt": 5.79,
    "exchange_rate": 114600
  }
}
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-1-fast-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت‌های کلیدی بین یادگیری ماشین و یادگیری عمیق چیست؟"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "تفاوت‌های کلیدی بین یادگیری ماشین و یادگیری عمیق چیست؟",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "grok-4-1-fast-reasoning",
  messages: [
    {
      role: "user",
      content: "تفاوت‌های کلیدی بین یادگیری ماشین و یادگیری عمیق چیست؟",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### نمونه‌های فراخوانی تابع

هر دو مدل از فراخوانی پیشرفته تابع برای گردش‌های کاری عاملی پشتیبانی می‌کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-1-fast-non-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوای سانفرانسیسکو چطور است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "واحد دما"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

python=:tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "واحد دما",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4-1-fast-non-reasoning",
    messages=[{"role": "user", "content": "آب و هوای سانفرانسیسکو چطور است؟"}],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر",
                    },
                    unit: {
                        type: "string",
                        enum: ["celsius", "fahrenheit"],
                        description: "واحد دما",
                    },
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "grok-4-1-fast-non-reasoning",
    messages: [{role: "user", content: "آب و هوای سانفرانسیسکو چطور است؟"}],
    tools: tools,
    tool_choice: "auto",
});

```

### خروجی‌های ساختاریافته

هر دو مدل از خروجی‌های ساختاریافته با استفاده از JSON schema پشتیبانی می‌کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-1-fast-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "اطلاعات کلیدی از این متن را استخراج کنید: جان دو، متولد 15 ژانویه 1990، به عنوان مهندس نرم‌افزار در Tech Corp کار می‌کند."
      }
    ],
    "response_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "person_info",
        "strict": true,
        "schema": {
          "type": "object",
          "properties": {
            "name": {"type": "string"},
            "birth_date": {"type": "string"},
            "occupation": {"type": "string"},
            "company": {"type": "string"}
          },
          "required": ["name", "birth_date", "occupation", "company"],
          "additionalProperties": false
        }
      }
    }
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="grok-4-1-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "اطلاعات کلیدی از این متن را استخراج کنید: جان دو، متولد 15 ژانویه 1990، به عنوان مهندس نرم‌افزار در Tech Corp کار می‌کند.",
        }
    ],
    response_format={
        "type": "json_schema",
        "json_schema": {
            "name": "person_info",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "name": {"type": "string"},
                    "birth_date": {"type": "string"},
                    "occupation": {"type": "string"},
                    "company": {"type": "string"},
                },
                "required": ["name", "birth_date", "occupation", "company"],
                "additionalProperties": False,
            },
        },
    },
)

javascript=:const response = await client.chat.completions.create({
    model: "grok-4-1-fast-reasoning",
    messages: [
        {
            role: "user",
            content: "اطلاعات کلیدی از این متن را استخراج کنید: جان دو، متولد 15 ژانویه 1990، به عنوان مهندس نرم‌افزار در Tech Corp کار می‌کند.",
        },
    ],
    response_format: {
        type: "json_schema",
        json_schema: {
            name: "person_info",
            strict: true,
            schema: {
                type: "object",
                properties: {
                    name: { type: "string" },
                    birth_date: { type: "string" },
                    occupation: { type: "string" },
                    company: { type: "string" },
                },
                required: ["name", "birth_date", "occupation", "company"],
                additionalProperties: false,
            },
        },
    },
});

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [مرجع API: Chat Completions](fa/api-reference/messages.md)
- [قیمت‌گذاری](fa/pricing.md)