# News 2026-05-22-qwen3-7-max-added: مدل پرچم‌دار جدید اضافه شد: Qwen3.7-Max
URL: `https://docs.avalai.ir/fa/news/2026-05-22-qwen3-7-max-added`
**تاریخ:** ۱۴۰۵-۰۳-۰۱ / (2026-05-22)

# مدل پرچم‌دار جدید اضافه شد: Qwen3.7-Max

**تاریخ:** ۱۴۰۵-۰۳-۰۱ / (2026-05-22)

## خلاصه

مدل پایه عامل پرچم‌دار جدید Alibaba با نام **Qwen3.7-Max** اکنون در AvalAI از طریق Chat Completions API (`v1/chat/completions`) و با پشتیبانی نسبی از Responses API (`v1/responses`) در دسترس است. این مدل برای گردش‌کارهای عاملی بلندمدت، کدنویسی پیشرفته و استدلال طراحی شده و با **تخفیف ترویجی ۵۰٪ تا ۲۲ ژوئن ۲۰۲۶** ارائه می‌شود.


### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.7-max",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون بنویس که دو لینک لیست مرتب را با هم ادغام کند."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-qwen37max-example",
  "created": 1779768420,
  "model": "qwen3.7-max",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در ادامه یک تابع پایتون برای ادغام دو لینک لیست مرتب با استفاده از یک گره ساختگی برای خوانایی آورده شده است...\n\n
```python\nclass ListNode:\n    def __init__(self, val=0, next=None):\n        self.val = val\n        self.next = next\n\ndef merge_two_sorted_lists(l1, l2):\n    dummy = ListNode()\n    tail = dummy\n    while l1 and l2:\n        if l1.val <= l2.val:\n            tail.next, l1 = l1, l1.next\n        else:\n            tail.next, l2 = l2, l2.next\n        tail = tail.next\n    tail.next = l1 or l2\n    return dummy.next\n```",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 175,
    "prompt_tokens": 22,
    "total_tokens": 197,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 22,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0013675000",
    "irt": 156.72,
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
    "model": "qwen3.7-max",
    "messages": [
      {
        "role": "user",
        "content": "یک message broker مقاوم در برابر خطا برای یک سیستم معاملاتی پرحجم طراحی کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {
            "role": "user",
            "content": "یک message broker مقاوم در برابر خطا برای یک سیستم معاملاتی پرحجم طراحی کن.",
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
  model: "qwen3.7-max",
  messages: [
    {
      role: "user",
      content: "یک message broker مقاوم در برابر خطا برای یک سیستم معاملاتی پرحجم طراحی کن.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

### تفکر ترکیبی با استریمینگ

Qwen3.7-Max از حالت تفکر ترکیبی DashScope پشتیبانی می‌کند. برای مشاهده محتوای استدلال در کنار پاسخ نهایی، از `extra_body={"enable_thinking": True}` همراه با `stream=True` استفاده کنید. برای گردش‌کارهای عاملی چندنوبتی، `preserve_thinking` را نیز فعال کنید تا استدلال قبلی در بین نوبت‌ها در دسترس بماند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.7-max",
    "messages": [
      {
        "role": "user",
        "content": "یک ریفکتور چندمرحله‌ای برای انتقال یک سرویس پرداخت monolithic به میکروسرویس‌های event-driven برنامه‌ریزی کن."
      }
    ],
    "stream": true,
    "enable_thinking": true,
    "preserve_thinking": true
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

stream = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {
            "role": "user",
            "content": "یک ریفکتور چندمرحله‌ای برای انتقال یک سرویس پرداخت monolithic به میکروسرویس‌های event-driven برنامه‌ریزی کن.",
        }
    ],
    stream=True,
    extra_body={
        "enable_thinking": True,
        "preserve_thinking": True,
    },
)

for chunk in stream:
    if not chunk.choices:
        continue
    delta = chunk.choices[0].delta
    if hasattr(delta, "reasoning_content") and delta.reasoning_content:
        print(delta.reasoning_content, end="", flush=True)
    if getattr(delta, "content", None):
        print(delta.content, end="", flush=True)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const stream = await client.chat.completions.create({
  model: "qwen3.7-max",
  messages: [
    {
      role: "user",
      content: "یک ریفکتور چندمرحله‌ای برای انتقال یک سرویس پرداخت monolithic به میکروسرویس‌های event-driven برنامه‌ریزی کن.",
    },
  ],
  stream: true,
  // @ts-ignore - پارامترهای اختصاصی DashScope که مستقیم منتقل می‌شوند
  enable_thinking: true,
  preserve_thinking: true,
});

for await (const chunk of stream) {
  const delta = chunk.choices?.[0]?.delta;
  if (delta?.reasoning_content) process.stdout.write(delta.reasoning_content);
  if (delta?.content) process.stdout.write(delta.content);
}

```

> **توجه:** برای درخواست‌های غیر استریمینگ، `enable_thinking: false` را در `extra_body` تنظیم کنید. تفکر ترکیبی بر اساس راهنمایی‌های DashScope تنها با استریمینگ پشتیبانی می‌شود. برای جزئیات بیشتر به [مدل‌های Alibaba](fa/providers/alibaba.md) مراجعه کنید.

---

### فراخوانی تابع

Qwen3.7-Max از فراخوانی تابع برای گردش‌کارهای عاملی پشتیبانی می‌کند که باید استدلال مدل را به ابزارها و سیستم‌های خارجی متصل کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.7-max",
    "messages": [
      {
        "role": "user",
        "content": "وضعیت استقرار تولید سرویس `payments-api` را بررسی کن و pod‌های ناموفق را گزارش کن."
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_deploy_status",
          "description": "دریافت وضعیت فعلی استقرار برای یک سرویس",
          "parameters": {
            "type": "object",
            "properties": {
              "service": {
                "type": "string",
                "description": "Service name"
              }
            },
            "required": ["service"]
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
            "name": "get_deploy_status",
            "description": "دریافت وضعیت فعلی استقرار برای یک سرویس",
            "parameters": {
                "type": "object",
                "properties": {
                    "service": {
                        "type": "string",
                        "description": "Service name",
                    }
                },
                "required": ["service"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {
            "role": "user",
            "content": "وضعیت استقرار تولید سرویس `payments-api` را بررسی کن و pod‌های ناموفق را گزارش کن.",
        }
    ],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
  {
    type: "function",
    function: {
      name: "get_deploy_status",
      description: "دریافت وضعیت فعلی استقرار برای یک سرویس",
      parameters: {
        type: "object",
        properties: {
          service: {
            type: "string",
            description: "Service name",
          },
        },
        required: ["service"],
      },
    },
  },
];

const response = await client.chat.completions.create({
  model: "qwen3.7-max",
  messages: [
    {
      role: "user",
      content: "وضعیت استقرار تولید سرویس `payments-api` را بررسی کن و pod‌های ناموفق را گزارش کن.",
    },
  ],
  tools,
  tool_choice: "auto",
});

```

---

### Responses API (پشتیبانی نسبی)

Qwen3.7-Max همچنین می‌تواند از طریق Responses API سازگار با OpenAI (`v1/responses`) فراخوانی شود. پشتیبانی نسبی برای ورودی/خروجی متنی و استفاده از ابزار پایه فراهم است؛ ابزارهای داخلی پیشرفته (مانند جستجوی وب، جستجوی فایل) و فیلد پیکربندی `reasoning` همچنان به مدل‌های سری o از OpenAI محدود می‌مانند:

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.7-max",
    "input": "خطرات معماری انتقال یک دفترکل مبتنی بر SQL به یک طراحی event-sourced را خلاصه کن."
  }'
```

برای دیدن کامل اسکیمای درخواست و پاسخ، به [مرجع Responses API](fa/api-reference/responses.md) مراجعه کنید.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [Chat Completions API](fa/api-reference/chat.md)
- [Responses API](fa/api-reference/responses.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [فهرست مدل‌ها](fa/models/index.md)
