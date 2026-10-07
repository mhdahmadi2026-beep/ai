# افزودن مدل GPT-5.1

**تاریخ:** 1404-08-23 / (2025-11-14)

## خلاصه

مدل پیشرفته GPT-5.1 از OpenAI اکنون در AvalAI در دسترس است. این مدل پیشرفته با قابلیت تنظیم تلاش استدلال، برای وظایف کدنویسی و عاملی با پنجره زمینه 400,000 توکن و حداکثر 128,000 توکن خروجی ایده‌آل است.

---

## جزئیات

### OpenAI

ما افزودن GPT-5.1، مدل پیشرفته OpenAI طراحی شده برای وظایف کدنویسی و عاملی با قابلیت‌های استدلالی پیشرفته را اعلام می‌کنیم.

- **[`gpt-5.1`](fa/providers/openai.md)**: مدل پیشرفته OpenAI برای وظایف کدنویسی و عاملی با قابلیت تنظیم تلاش استدلالی و غیر استدلالی. دارای پنجره زمینه 400,000 توکن و حداکثر 128,000 توکن خروجی با پشتیبانی از توکن‌های استدلال.

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 400,000 توکن برای مدیریت مکالمات و اسناد گسترده
- **حداکثر توکن‌های خروجی**: 128,000 توکن برای پاسخ‌های جامع
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته، پشتیبانی از توکن‌های استدلال، بینایی (ورودی تصویر)
- **تاریخ قطع دانش**: 31 مه 2024
- **پشتیبانی از نقاط پایانی**: در دسترس در [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/responses`](fa/api-reference/responses.md)
- **پشتیبانی از ابزار**: جستجوی وب، جستجوی فایل، تولید تصویر، مفسر کد، و MCP

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5.1 | $1.25/1M توکن | $0.125/1M توکن | $10.00/1M توکن |

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای محاسبه دنباله فیبوناچی با استفاده از برنامه‌نویسی پویا بنویس."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123def456",
  "created": 1731569214,
  "model": "gpt-5.1",
  "object": "chat.completion",
  "system_fingerprint": "fp_abc123",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا یک تابع کارآمد پایتون برای محاسبه دنباله فیبوناچی با استفاده از برنامه‌نویسی پویا آمده است:\n\n
```python\ndef fibonacci(n):\n    \"\"\"محاسبه nامین عدد فیبوناچی با استفاده از برنامه‌نویسی پویا.\"\"\"\n    if n <= 1:\n        return n\n    \n    # مقداردهی اولیه آرایه برای ذخیره اعداد فیبوناچی\n    fib = [0] * (n + 1)\n    fib[1] = 1\n    \n    # ساخت دنباله\n    for i in range(2, n + 1):\n        fib[i] = fib[i-1] + fib[i-2]\n    \n    return fib[n]\n```\n\nاین رویکرد دارای پیچیدگی زمانی O(n) و پیچیدگی فضایی O(n) است.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 156,
    "prompt_tokens": 28,
    "total_tokens": 184,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0015950000",
    "irt": 182.77,
    "exchange_rate": 114600
  }
}
```

### نمونه استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1",
    "messages": [
      {
        "role": "user",
        "content": "توضیح بده که مدل‌های یادگیری ماشین چگونه از داده‌ها یاد می‌گیرند."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {
            "role": "user",
            "content": "توضیح بده که مدل‌های یادگیری ماشین چگونه از داده‌ها یاد می‌گیرند.",
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
  model: "gpt-5.1",
  messages: [
    {
      role: "user",
      content: "توضیح بده که مدل‌های یادگیری ماشین چگونه از داده‌ها یاد می‌گیرند.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### نمونه فراخوانی تابع

GPT-5.1 از قابلیت‌های پیشرفته فراخوانی تابع پشتیبانی می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1",
    "messages": [
      {
        "role": "user",
        "content": "هوای نیویورک چطور است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات آب و هوای فعلی",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
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
            "description": "دریافت اطلاعات آب و هوای فعلی",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    }
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[{"role": "user", "content": "هوای نیویورک چطور است؟"}],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات آب و هوای فعلی",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر",
                    }
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "gpt-5.1",
    messages: [{role: "user", content: "هوای نیویورک چطور است؟"}],
    tools: tools,
    tool_choice: "auto",
});

```

### قابلیت‌های بینایی

GPT-5.1 از ورودی تصویر برای وظایف چندوجهی پشتیبانی می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "در این تصویر چه چیزی است؟"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://example.com/image.jpg"
            }
          }
        ]
      }
    ]
  }'

python=:response = client.chat.completions.create(
    model="gpt-5.1",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی است؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
    model: "gpt-5.1",
    messages: [
        {
            role: "user",
            content: [
                { type: "text", text: "در این تصویر چه چیزی است؟" },
                {
                    type: "image_url",
                    image_url: { url: "https://example.com/image.jpg" },
                },
            ],
        },
    ],
});

console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای بینایی](fa/guides/vision.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
