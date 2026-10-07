# News 2025-12-28-minimax-provider-support-added: 3. اگر فراخوانی ابزار وجود دارد، ابزار را اجرا کن و مکالمه را ادامه بده
URL: `https://docs.avalai.ir/fa/news/2025-12-28-minimax-provider-support-added`
**تاریخ:** ۱۴۰۴-۱۰-۰۷ / (2025-12-28)

# افزودن پشتیبانی از ارائه‌دهنده MiniMax: مدل‌های استدلال M2.1 اکنون در دسترس

**تاریخ:** ۱۴۰۴-۱۰-۰۷ / (2025-12-28)

## خلاصه

AvalAI پشتیبانی از MiniMax، یک ارائه‌دهنده جدید هوش مصنوعی، را با ۳ مدل جدید شامل مدل استدلال پرچم‌دار MiniMax M2.1 معرفی می‌کند. این مدل‌ها قابلیت‌های استثنایی برنامه‌نویسی چند زبانه، استدلال پیشرفته در سطح o3 و عملکرد برجسته در گردش‌های کاری کدنویسی عاملی ارائه می‌دهند. مدل‌های MiniMax از طریق هر دو SDK OpenAI و آنتروپیک قابل دسترسی هستند.


## روش‌های دسترسی SDK

مدل‌های MiniMax از طریق دو روش SDK قابل دسترسی هستند:

| SDK | آدرس پایه | اندپوینت | بهترین برای |
|-----|----------|----------|------------|
| OpenAI SDK | `https://api.avalai.ir/v1` | `/v1/chat/completions` | تکمیل چت استاندارد |
| Anthropic SDK | `https://api.avalai.ir` (بدون /v1) | `/v1/messages` | بلوک‌های thinking بومی، استفاده از ابزار |

---

## مثال‌های درخواست/پاسخ API

### تکمیل چت (فرمت OpenAI)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.1",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع Rust برای پیاده‌سازی یک خزنده وب همزمان با محدودیت نرخ بنویس"
      }
    ]
  }'
```

**پاسخ نمونه:**

```json
{
  "id": "chatcmpl-minimax-abc123",
  "created": 1766500800,
  "model": "minimax-m2.1",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا یک پیاده‌سازی خزنده وب همزمان در Rust با محدودیت نرخ آورده شده است:\n\n
```rust\nuse std::sync::Arc;\nuse tokio::sync::{Semaphore, RwLock};\nuse tokio::time::{sleep, Duration};\nuse reqwest::Client;\nuse std::collections::HashSet;\n\nstruct Crawler {\n    client: Client,\n    rate_limiter: Arc<Semaphore>,\n    visited: Arc<RwLock<HashSet<String>>>,\n    max_concurrent: usize,\n}\n...",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 512,
    "prompt_tokens": 24,
    "total_tokens": 536
  }
}
```

---

## مثال‌های استفاده از SDK

### OpenAI SDK - استفاده پایه

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.1",
    "messages": [
      {
        "role": "user",
        "content": "یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-AvalAI-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.1",
    messages=[
        {
            "role": "user",
            "content": "یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "minimax-m2.1",
  messages: [
    {
      role: "user",
      content: "یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### Anthropic SDK - استفاده پایه

مدل‌های MiniMax همچنین از طریق Anthropic SDK و اندپوینت `v1/messages` قابل دسترسی هستند. از `base_url="https://api.avalai.ir"` (بدون `/v1`) استفاده کنید.

```language-selector
python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # توجه: بدون /v1
)

message = client.messages.create(
    model="minimax-m2.1",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن"}
    ],
)

print(message.content)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",  // توجه: بدون /v1
});

const message = await client.messages.create({
  model: "minimax-m2.1",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن" }
  ],
});

console.log(message.content);

```

### Anthropic SDK - استفاده از ابزار با تفکر درهم‌تنیده

MiniMax M2.1 به صورت بومی از **تفکر درهم‌تنیده (Interleaved Thinking)** پشتیبانی می‌کند که به مدل اجازه می‌دهد بین هر دور تعامل با ابزار استدلال کند. قبل از هر استفاده از ابزار، مدل روی محیط فعلی و خروجی‌های ابزار تامل می‌کند تا اقدام بعدی را تصمیم بگیرد.

```language-selector
python=:import anthropic
import json

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # توجه: بدون /v1
)

# تعریف ابزار: استعلام آب و هوا
tools = [
    {
        "name": "get_weather",
        "description": "دریافت آب و هوای یک مکان، کاربر باید ابتدا مکان را مشخص کند.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "شهر و کشور، مثلا تهران، ایران",
                }
            },
            "required": ["location"],
        },
    }
]


def send_messages(messages):
    response = client.messages.create(
        model="minimax-m2.1",
        max_tokens=4096,
        messages=messages,
        tools=tools,
    )
    return response


def process_response(response):
    thinking_blocks = []
    text_blocks = []
    tool_use_blocks = []

    for block in response.content:
        if block.type == "thinking":
            thinking_blocks.append(block)
            print(f"💭 تفکر>\n{block.thinking}\n")
        elif block.type == "text":
            text_blocks.append(block)
            print(f"💬 مدل>\t{block.text}")
        elif block.type == "tool_use":
            tool_use_blocks.append(block)
            print(
                f"🔧 ابزار>\t{block.name}({json.dumps(block.input, ensure_ascii=False)})"
            )

    return thinking_blocks, text_blocks, tool_use_blocks


# 1. پرسش کاربر
messages = [{"role": "user", "content": "آب و هوای تهران چگونه است؟"}]
print(f"\n👤 کاربر>\t {messages[0]['content']}")

# 2. مدل پاسخ اول را برمی‌گرداند (ممکن است شامل فراخوانی ابزار باشد)
response = send_messages(messages)
thinking_blocks, text_blocks, tool_use_blocks = process_response(response)

# 3. اگر فراخوانی ابزار وجود دارد، ابزار را اجرا کن و مکالمه را ادامه بده
if tool_use_blocks:
    # ⚠️ مهم: پاسخ کامل دستیار را به تاریخچه پیام اضافه کن
    # response.content شامل تمام بلوک‌ها است: [بلوک thinking، بلوک text، بلوک tool_use]
    messages.append({"role": "assistant", "content": response.content})

    # اجرای ابزار و بازگرداندن نتیجه (شبیه‌سازی فراخوانی API آب و هوا)
    print(f"\n🔨 در حال اجرای ابزار: {tool_use_blocks[0].name}")
    tool_result = "24℃، آفتابی"
    print(f"📊 نتیجه ابزار: {tool_result}")

    # اضافه کردن نتیجه اجرای ابزار
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_blocks[0].id,
                    "content": tool_result,
                }
            ],
        }
    )

    # 4. دریافت پاسخ نهایی
    final_response = send_messages(messages)
    process_response(final_response)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",  // توجه: بدون /v1
});

const tools = [
  {
    name: "get_weather",
    description: "دریافت آب و هوای یک مکان، کاربر باید ابتدا مکان را مشخص کند.",
    input_schema: {
      type: "object",
      properties: {
        location: {
          type: "string",
          description: "شهر و کشور، مثلا تهران، ایران",
        }
      },
      required: ["location"]
    }
  }
];

async function sendMessages(messages) {
  return await client.messages.create({
    model: "minimax-m2.1",
    max_tokens: 4096,
    messages: messages,
    tools: tools,
  });
}

// پرسش کاربر
let messages = [{ role: "user", content: "آب و هوای تهران چگونه است؟" }];
console.log(`👤 کاربر: ${messages[0].content}`);

// دریافت پاسخ اولیه
let response = await sendMessages(messages);

// پردازش بلوک‌های پاسخ
for (const block of response.content) {
  if (block.type === "thinking") {
    console.log(`💭 تفکر: ${block.thinking}`);
  } else if (block.type === "text") {
    console.log(`💬 مدل: ${block.text}`);
  } else if (block.type === "tool_use") {
    console.log(`🔧 ابزار: ${block.name}(${JSON.stringify(block.input)})`);
    
    // اضافه کردن پاسخ دستیار به تاریخچه
    messages.push({ role: "assistant", content: response.content });
    
    // شبیه‌سازی اجرای ابزار
    const toolResult = "24℃، آفتابی";
    messages.push({
      role: "user",
      content: [{ type: "tool_result", tool_use_id: block.id, content: toolResult }]
    });
    
    // دریافت پاسخ نهایی
    const finalResponse = await sendMessages(messages);
    for (const finalBlock of finalResponse.content) {
      if (finalBlock.type === "text") {
        console.log(`💬 نهایی: ${finalBlock.text}`);
      }
    }
  }
}

```

### OpenAI SDK - فراخوانی تابع

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.1",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوای توکیو چگونه است؟"
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
                "description": "نام شهر، مثلا توکیو"
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

python=:from openai import OpenAI

client = OpenAI(api_key="your-AvalAI-api-key", base_url="https://api.avalai.ir/v1")

tools = [
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
                        "description": "نام شهر، مثلا توکیو",
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
    model="minimax-m2.1",
    messages=[{"role": "user", "content": "آب و هوای توکیو چگونه است؟"}],
    tools=tools,
    tool_choice="auto",
)

print(response.choices[0].message)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const tools = [
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
            description: "نام شهر، مثلا توکیو",
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
  },
];

const response = await client.chat.completions.create({
  model: "minimax-m2.1",
  messages: [{ role: "user", content: "آب و هوای توکیو چگونه است؟" }],
  tools: tools,
  tool_choice: "auto",
});

console.log(response.choices[0].message);

```

### MiniMax M2.1 Lightning (حالت سریع)

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.1-lightning",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-AvalAI-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.1-lightning",
    messages=[
        {
            "role": "user",
            "content": "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "minimax-m2.1-lightning",
  messages: [
    {
      role: "user",
      content: "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## تفکر درهم‌تنیده: مفاهیم کلیدی

قابلیت **تفکر درهم‌تنیده (Interleaved Thinking)** در MiniMax M2.1 به مدل اجازه می‌دهد بین تعاملات ابزار استدلال کند، که آن را برای گردش‌های کاری عاملی بسیار قدرتمند می‌سازد.

### نحوه کار

1. **قبل از استفاده از ابزار**: مدل روی محیط فعلی تامل می‌کند و تصمیم می‌گیرد کدام ابزار را فراخوانی کند
2. **بعد از نتیجه ابزار**: مدل خروجی ابزار را تحلیل می‌کند و اقدام بعدی را برنامه‌ریزی می‌کند
3. **زنجیره تفکر**: زنجیره استدلال کامل در طول چندین تعامل ابزار حفظ می‌شود

### بهترین شیوه‌ها

- **حفظ پاسخ کامل**: همیشه `response.content` کامل (شامل بلوک‌های thinking) را به تاریخچه پیام اضافه کنید
- **محتوا را تغییر ندهید**: بلوک‌های thinking را دست‌نخورده نگه دارید - آن‌ها تداوم استدلال را حفظ می‌کنند
- **از Anthropic SDK استفاده کنید**: برای پشتیبانی بومی از بلوک thinking، از Anthropic SDK با `base_url="https://api.avalai.ir"` استفاده کنید

### فرمت پاسخ

هنگام استفاده از Anthropic SDK، پاسخ‌ها شامل سه نوع بلوک هستند:

| نوع بلوک | توضیحات |
|----------|---------|
| `thinking` | فرآیند استدلال داخلی مدل |
| `text` | محتوای متنی خروجی مدل |
| `tool_use` | اطلاعات فراخوانی ابزار با نام تابع و آرگومان‌ها |

---

## لینک‌های مرتبط

- [مستندات مدل‌های MiniMax](fa/providers/minimax.md)
- [مستندات رسمی MiniMax](https://platform.minimax.io/docs/guides/quickstart)
- [کتابخانه‌ها و SDK‌ها](fa/libraries.md)
- [قیمت‌گذاری](fa/pricing.md)
- [راهنمای شروع سریع](fa/quickstart.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
