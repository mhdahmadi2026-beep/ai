# News 2026-06-05-gemini-image-stable-and-qwen3-max-added: Access the generated image
URL: `https://docs.avalai.ir/fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added`
**تاریخ:** ۱۴۰۵-۰۳-۱۵ / (2026-06-05)

# مدل‌های جدید اضافه شدند: Gemini 3 Pro Image، Gemini 3.1 Flash Image پایدار و Qwen3-Max

**تاریخ:** ۱۴۰۵-۰۳-۱۵ / (2026-06-05)

## خلاصه

ما افزودن سه مدل جدید را اعلام می‌کنیم. مدل‌های [`gemini-3-pro-image`](fa/providers/google.md) (Nano Banana Pro) و [`gemini-3.1-flash-image`](fa/providers/google.md) (Nano Banana 2) از Google اکنون به عنوان نام‌های مستعار پایدار در دسترس هستند و از نسخه‌های پیش‌نمایش خود با قابلیت‌ها و قیمت‌گذاری یکسان ارتقا یافته‌اند. مدل پرچم‌دار [`qwen3-max`](fa/providers/alibaba.md) از Alibaba نیز برای استدلال پیچیده و گردش‌های کاری عاملی در دسترس است.


## خلاصه قیمت‌گذاری

| مدل | ورودی ($/1M توکن) | ورودی کش شده ($/1M توکن) | خروجی ($/1M توکن) | قیمت‌گذاری ویژه |
|-----|-------------------|--------------------------|-------------------|-----------------|
| `gemini-3-pro-image` | $2.00 (متن)، $2.00 (تصویر) | $0.50 | $12.00 (متن)، $120.00 (تصویر) | $0.134 به ازای تصویر 1K-2K، $0.24 به ازای تصویر 4K |
| `gemini-3.1-flash-image` | $0.50 (متن)، $0.50 (تصویر) | $0.25 | $3.00 (متن)، $60.00 (تصویر) | $0.0672 (1K-2K)، $0.101 (2K-4K)، $0.151 (4K) به ازای هر تصویر |
| `qwen3-max` | $1.20 | $0.10 | $6.00 | بالای 32K: $2.40/$12.00، بالای 128K: $3.00/$15.00 |

---

## نمونه‌های درخواست/پاسخ API

### Gemini 3 Pro Image (سازگار با OpenAI)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-image",
    "messages": [
      {
        "role": "user",
        "content": "Create a minimalist poster with Persian text that says \"هوش مصنوعی\" (Artificial Intelligence) in a modern, tech-inspired style with blue and white colors"
      }
    ],
    "modalities": ["image", "text"]
  }' | jq '.choices[0].message.images[0].image_url.url |= (.[0:100] + "...[TRUNCATED]")'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1780000000,
  "model": "gemini-3-pro-image",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "I've created a minimalist tech-inspired poster featuring the Persian text \"هوش مصنوعی\" in a modern style with blue and white colors.",
        "role": "assistant",
        "images": [
          {
            "image_url": {
              "url": "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zU...[TRUNCATED]",
              "detail": "auto"
            },
            "index": 0,
            "type": "image_url"
          }
        ],
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1150,
    "prompt_tokens": 32,
    "total_tokens": 1182,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 32,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.1558000000",
    "irt": 17864.68,
    "exchange_rate": 114600
  }
}
```

### Gemini 3 Pro Image (API بومی Gemini)

همچنین می‌توانید از endpoint [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) استفاده کنید:

```bash
GEMINI_API_KEY="$AVALAI_API_KEY"
MODEL_ID="gemini-3-pro-image"
GENERATE_CONTENT_API="generateContent"

cat <<EOF >request.json
{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "a cat"
          }
        ]
      }
    ],
    "generationConfig": {
      "responseModalities": ["IMAGE", "TEXT"]
    }
}
EOF

curl \
  -X POST \
  -H "Content-Type: application/json" \
  "https://api.avalai.ir/v1beta/models/${MODEL_ID}:${GENERATE_CONTENT_API}?key=${GEMINI_API_KEY}" \
  -d '@request.json' \
  --output response.json
```

### Gemini 3.1 Flash Image (API بومی Gemini)

```bash
GEMINI_API_KEY="$AVALAI_API_KEY"
MODEL_ID="gemini-3.1-flash-image"
GENERATE_CONTENT_API="generateContent"

cat <<EOF >request.json
{
    "contents": [
      {
        "role": "user",
        "parts": [
          {
            "text": "a cat"
          }
        ]
      }
    ],
    "generationConfig": {
      "responseModalities": ["IMAGE", "TEXT"]
    }
}
EOF

curl \
  -X POST \
  -H "Content-Type: application/json" \
  "https://api.avalai.ir/v1beta/models/${MODEL_ID}:${GENERATE_CONTENT_API}?key=${GEMINI_API_KEY}" \
  -d '@request.json' \
  --output response.json
```

### نمونه Qwen3-Max

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-max",
    "messages": [
      {
        "role": "user",
        "content": "Design an intelligent agent system that can autonomously manage complex multi-step workflows with tool invocation capabilities."
      }
    ],
    "max_tokens": 2000
  }'
```

**پاسخ:**

```json
{
  "id": "chatcmpl-abc789",
  "created": 1780000000,
  "model": "qwen3-max",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Here's a comprehensive design for an intelligent agent system...",
        "role": "assistant",
        "tool_calls": null
      }
    }
  ],
  "usage": {
    "completion_tokens": 512,
    "prompt_tokens": 24,
    "total_tokens": 536,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "estimated_cost": {
    "unit": "0.0031008000",
    "irt": 355.35,
    "exchange_rate": 114600
  }
}
```

---

## نمونه‌های استفاده از SDK

### تولید تصویر Gemini

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-flash-image",
    "messages": [
      {
        "role": "user",
        "content": "Create a modern logo for a tech company called \"AvalAI\" with clean typography and a minimalist design"
      }
    ],
    "modalities": ["image", "text"]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-3.1-flash-image",
    messages=[
        {
            "role": "user",
            "content": 'Create a modern logo for a tech company called "AvalAI" with clean typography and a minimalist design',
        }
    ],
    extra_body={"modalities": ["image", "text"]},
)

# Access the generated image
if hasattr(response.choices[0].message, "images"):
    images = getattr(response.choices[0].message, "images")
    for img in images:
        print(f"Image URL: {img.image_url.url[:100]}...")

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.1-flash-image",
  messages: [
    {
      role: "user",
      content: "Create a modern logo for a tech company called \"AvalAI\" with clean typography and a minimalist design",
    },
  ],
  modalities: ["image", "text"],
});

// Access the generated image
if (response.choices[0].message.images) {
  const images = response.choices[0].message.images;
  images.forEach((img, idx) => {
    console.log(`Image ${idx}: ${img.image_url.url.substring(0, 100)}...`);
  });
}

console.log(response.choices[0].message.content);

```

### Qwen3-Max

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-max",
    "messages": [
      {
        "role": "user",
        "content": "Perform a comprehensive analysis of quantum computing's potential impact on cryptography."
      }
    ],
    "max_tokens": 2000
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {
            "role": "user",
            "content": "Perform a comprehensive analysis of quantum computing's potential impact on cryptography.",
        }
    ],
    max_tokens=2000,
    extra_body={"enable_thinking": False},  # Required for non-streaming requests
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3-max",
  messages: [
    {
      role: "user",
      content: "Perform a comprehensive analysis of quantum computing's potential impact on cryptography.",
    },
  ],
  max_tokens: 2000,
});

console.log(response.choices[0].message.content);

```

---

## پیوندهای مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [راهنمای سری Nano Banana](fa/examples/generate_images_with_nano_banana_series.md)
- [مرجع API بومی Gemini](fa/api-reference/v1beta.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
