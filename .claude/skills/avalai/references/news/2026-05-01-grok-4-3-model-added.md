# News 2026-05-01-grok-4-3-model-added: مدل پرچمدار جدید اضافه شد: Grok-4.3
URL: `https://docs.avalai.ir/fa/news/2026-05-01-grok-4-3-model-added`
**تاریخ:** ۱۴۰۵-۰۲-۱۱ / (2026-05-01)

# مدل پرچمدار جدید اضافه شد: Grok-4.3

**تاریخ:** ۱۴۰۵-۰۲-۱۱ / (2026-05-01)

## خلاصه

مدل استدلالی پرچمدار جدید XAI یعنی **Grok-4.3** اکنون در AvalAI از طریق Chat Completions API (`v1/chat/completions`) در دسترس است. این مدل پنجره زمینه ۱,۰۰۰,۰۰۰ توکنی، فراخوانی تابع، خروجی‌های ساختاریافته و استدلال داخلی را همراه با قیمت‌گذاری وابسته به زمینه برای درخواست‌های بالای ۲۰۰K توکن ارائه می‌کند.


### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [
      {
        "role": "user",
        "content": "مزایا و معایب event sourcing و CRUD را برای یک سیستم دفترکل مالی تحلیل کن."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-grok43-example",
  "created": 1777647600,
  "model": "grok-4.3",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Event sourcing اغلب برای دفترکل‌های مالی انتخاب مناسبی است، زیرا یک مسیر حسابرسی تغییرناپذیر حفظ می‌کند، بازسازی وضعیت تاریخی را ممکن می‌سازد و تطبیق داده‌ها را ساده‌تر می‌کند. CRUD از نظر عملیاتی ساده‌تر است، اما برای رسیدن به همان سطح حسابرسی به کنترل‌های بیشتری نیاز دارد...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 220,
    "prompt_tokens": 31,
    "total_tokens": 251,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 31,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0005887500",
    "irt": 67.48,
    "exchange_rate": 114600
  }
}
```

---

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [
      {
        "role": "user",
        "content": "برای انتقال یک monolith به سرویس‌های event-driven یک برنامه مهاجرت طراحی کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="grok-4.3",
    messages=[
        {
            "role": "user",
            "content": "برای انتقال یک monolith به سرویس‌های event-driven یک برنامه مهاجرت طراحی کن.",
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
  model: "grok-4.3",
  messages: [
    {
      role: "user",
      content: "برای انتقال یک monolith به سرویس‌های event-driven یک برنامه مهاجرت طراحی کن.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

### ویژگی‌های پیشرفته

#### فراخوانی تابع

Grok-4.3 از فراخوانی تابع برای گردش‌کارهایی پشتیبانی می‌کند که باید استدلال مدل را به سیستم‌های خارجی متصل کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [
      {
        "role": "user",
        "content": "موجودی SKU AVAL-123 را بررسی کن و پیشنهاد بده آیا باید سفارش مجدد ثبت شود یا نه."
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_inventory",
          "description": "دریافت اطلاعات موجودی فعلی برای یک SKU",
          "parameters": {
            "type": "object",
            "properties": {
              "sku": {
                "type": "string",
                "description": "Product SKU"
              }
            },
            "required": ["sku"]
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
            "name": "get_inventory",
            "description": "دریافت اطلاعات موجودی فعلی برای یک SKU",
            "parameters": {
                "type": "object",
                "properties": {
                    "sku": {
                        "type": "string",
                        "description": "Product SKU",
                    }
                },
                "required": ["sku"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="grok-4.3",
    messages=[
        {
            "role": "user",
            "content": "موجودی SKU AVAL-123 را بررسی کن و پیشنهاد بده آیا باید سفارش مجدد ثبت شود یا نه.",
        }
    ],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
  {
    type: "function",
    function: {
      name: "get_inventory",
      description: "دریافت اطلاعات موجودی فعلی برای یک SKU",
      parameters: {
        type: "object",
        properties: {
          sku: {
            type: "string",
            description: "Product SKU",
          },
        },
        required: ["sku"],
      },
    },
  },
];

const response = await client.chat.completions.create({
  model: "grok-4.3",
  messages: [
    {
      role: "user",
      content: "موجودی SKU AVAL-123 را بررسی کن و پیشنهاد بده آیا باید سفارش مجدد ثبت شود یا نه.",
    },
  ],
  tools,
  tool_choice: "auto",
});

```

#### خروجی‌های ساختاریافته

از پرامپت‌ها یا schemaهای خروجی ساختاریافته استفاده کنید تا Grok-4.3 پاسخ‌های قابل خواندن توسط ماشین را برای اتوماسیون‌های بعدی برگرداند:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.3",
    "messages": [
      {
        "role": "user",
        "content": "برای مهاجرت پایگاه داده پرداخت، یک JSON با کلیدهای risk_level، summary و next_actions برگردان."
      }
    ]
  }'
```

---

## لینک‌های مرتبط

- [مستندات مدل‌های XAI](fa/providers/xai.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [Chat Completions API](fa/api-reference/chat.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [فهرست مدل‌ها](fa/models/index.md)
