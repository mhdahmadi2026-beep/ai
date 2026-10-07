# News 2026-04-23-new-models-grok-gpt-image-qwen-kimi-gemini-embedding: Using Qwen3.6-Flash with thinking mode
URL: `https://docs.avalai.ir/fa/news/2026-04-23-new-models-grok-gpt-image-qwen-kimi-gemini-embedding`
**تاریخ:** ۱۴۰۵-۰۲-۰۳ / (2026-04-23)

# مدل‌های جدید اضافه شدند: Grok 4.20 پایدار، GPT-Image-2، سری Qwen3.6، Kimi K2.6 و Gemini Embedding 2

**تاریخ:** ۱۴۰۵-۰۲-۰۳ / (2026-04-23)

## خلاصه

 افزودن ده مدل جدید از پنج ارائه‌دهنده پیشرو را اعلام می‌کنیم: نسخه‌های پایدار `grok-4.20-reasoning` و `grok-4.20-non-reasoning` از X.AI، مدل نسل‌بعدی تولید تصویر `gpt-image-2` از OpenAI، مدل‌های چندوجهی بینایی‌-زبانی `qwen3.6-flash`، `qwen3.6-27b`، `qwen3.6-35b-a3b` و `qwen3.6-max-preview` از Alibaba، مدل متن‌باز عامل‌محور کدنویسی `kimi-k2.6` از Moonshot AI، و نخستین مدل تعبیه چندوجهی گوگل یعنی `gemini-embedding-2`.


## خلاصه قیمت‌گذاری

| مدل | ورودی ($/1M توکن) | ورودی کش‌شده ($/1M توکن) | خروجی ($/1M توکن) |
|-----|-------------------|-------------------------|-------------------|
| `grok-4.20-reasoning` | $2.00 | $0.20 | $6.00 |
| `grok-4.20-non-reasoning` | $2.00 | $0.20 | $6.00 |
| `gpt-image-2` (متن) | $5.00 | $1.25 | $10.00 |
| `gpt-image-2` (تصویر) | $8.00 | $2.00 | $30.00 |
| `qwen3.6-flash` | $0.25 | $0.025 | $1.50 |
| `qwen3.6-27b` | $0.60 | $0.06 | $3.60 |
| `qwen3.6-35b-a3b` | $0.248 | $0.025 | $1.485 |
| `qwen3.6-max-preview` | $1.30 | $0.13 | $7.80 |
| `kimi-k2.6` | $0.95 | $0.16 | $4.00 |
| `gemini-embedding-2` (متن) | $0.20 | $0.02 | $0.15 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه Grok 4.20 Reasoning

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.20-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "Design a fault-tolerant distributed system architecture for a global payment platform."
      }
    ],
    "max_tokens": 4096
  }'
```

**نمونه پاسخ:**

```json
{
  "id": "chatcmpl-grok420-abc123",
  "created": 1776321600,
  "model": "grok-4.20-reasoning",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "A fault-tolerant global payment platform should adopt a multi-region active-active architecture...",
        "role": "assistant",
        "thinking_blocks": [
          {
            "type": "thinking",
            "thinking": "Let me break down the requirements: global reach, fault tolerance, payment-grade reliability..."
          }
        ],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1420,
    "prompt_tokens": 25,
    "total_tokens": 1445,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 25
    }
  },
  "estimated_cost": {
    "unit": "0.0085700000",
    "irt": 982.13,
    "exchange_rate": 114600
  }
}
```

### نمونه تولید GPT-Image-2

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "A modernist editorial poster titled \"Typography\" that celebrates global scripts including Japanese, Arabic, Korean, and Latin letterforms, in red, blue, and black tones.",
    "size": "1024x1024",
    "n": 1
  }'
```

**نمونه پاسخ:**

```json
{
  "created": 1776321700,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zU...[TRUNCATED]",
      "revised_prompt": "A modernist editorial poster..."
    }
  ],
  "usage": {
    "input_tokens": 32,
    "input_tokens_details": {
      "text_tokens": 32,
      "image_tokens": 0
    },
    "output_tokens": 4160,
    "total_tokens": 4192
  },
  "estimated_cost": {
    "unit": "0.1249600000",
    "irt": 14320.22,
    "exchange_rate": 114600
  }
}
```

### نمونه ویرایش GPT-Image-2

```bash
curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gpt-image-2" \
  -F "image=@input.png" \
  -F "prompt=Add a gold Art Deco frame and soft sunrise lighting" \
  -F "size=1024x1024"
```

### نمونه Qwen3.6-Flash با حالت تفکر

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "Implement a binary search tree in Python with insert, delete, and in-order traversal methods."
      }
    ],
    "extra_body": {
      "enable_thinking": true
    },
    "stream": true
  }'
```

### نمونه Qwen3.6-Max-Preview

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.6-max-preview",
    "messages": [
      {
        "role": "user",
        "content": "Build a polished Next.js landing page for a SaaS product with hero, features, testimonials, and pricing sections."
      }
    ],
    "max_tokens": 8192
  }'
```

### نمونه Agent Swarm در Kimi K2.6

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.6",
    "messages": [
      {
        "role": "user",
        "content": "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI."
      }
    ],
    "max_tokens": 8192
  }'
```

### نمونه Gemini Embedding 2 (متن)

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-2",
    "input": "task: search result | query: What is the meaning of life?",
    "dimensions": 768
  }'
```

**نمونه پاسخ:**

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0.0123,
        -0.0456,
        0.0789,
        "...[TRUNCATED 768 values]"
      ]
    }
  ],
  "model": "gemini-embedding-2",
  "usage": {
    "prompt_tokens": 14,
    "total_tokens": 14
  },
  "estimated_cost": {
    "unit": "0.0000028000",
    "irt": 0.32,
    "exchange_rate": 114600
  }
}
```

### Gemini Embedding 2 چندوجهی از طریق اندپوینت سازگار با OpenAI

اندپوینت `v1/embeddings` ورودی‌های چندوجهی (تصاویر، صوت، ویدیو) را به‌صورت URI‌های `data:` در آرایه `input` می‌پذیرد:

```bash
# متن + تصویر (base64 data URI) از طریق اندپوینت سازگار با OpenAI
curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": [
      "The food was delicious and the waiter...",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII"
    ],
    "model": "gemini-embedding-2"
  }'
```

```bash
# متن + صوت (base64 data URI) از طریق اندپوینت سازگار با OpenAI
AUDIO_PATH="./speech.mp3"
AUDIO_BASE64="$(base64 -i "$AUDIO_PATH" | tr -d '\n')"

cat >/tmp/embeddings-audio.json <<EOF
{
  "input": [
    "The food was delicious and the waiter...",
    "data:audio/mpeg;base64,${AUDIO_BASE64}"
  ],
  "model": "gemini-embedding-2"
}
EOF

curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer ${AVALAI_API_KEY}" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/embeddings-audio.json
```

```bash
# متن + ویدیو (base64 data URI) از طریق اندپوینت سازگار با OpenAI
VIDEO_PATH="./sample_video.mp4"
VIDEO_BASE64="$(base64 -i "$VIDEO_PATH" | tr -d '\n')"

cat >/tmp/embeddings-video.json <<EOF
{
  "input": [
    "The food was delicious and the waiter...",
    "data:video/mp4;base64,${VIDEO_BASE64}"
  ],
  "model": "gemini-embedding-2"
}
EOF

curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer ${AVALAI_API_KEY}" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/embeddings-video.json
```

### Gemini Embedding 2 از طریق API بومی Gemini (`v1beta`)

`gemini-embedding-2` همچنین از طریق اندپوینت بومی Gemini یعنی `v1beta/models/{model}:embedContent` در دسترس است که بخش‌های `inline_data` را برای تصاویر، صوت، ویدیو و PDF می‌پذیرد.

**تعبیه متن (API بومی):**

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  -d '{
    "model": "gemini-embedding-2",
    "content": {
      "parts": [{
        "text": "What is the meaning of life?"
      }]
    }
  }'
```

**تعبیه تصویر (API بومی):**

```bash
IMG_PATH="./sample_image.jpg"
# macOS: IMG_BASE64="$(base64 -i "$IMG_PATH" | tr -d '\n')"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

cat >/tmp/payload.json <<EOF
{
  "content": {
    "parts": [
      {
        "inline_data": {
          "mime_type": "image/png",
          "data": "${IMG_BASE64}"
        }
      }
    ]
  }
}
EOF

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  --data-binary @/tmp/payload.json
```

**تعبیه صوت (API بومی):**

```bash
AUDIO_PATH="./speech.mp3"
AUDIO_BASE64="$(base64 -i "$AUDIO_PATH" | tr -d '\n')"

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  -d '{
    "content": {
      "parts": [{
        "inline_data": {
          "mime_type": "audio/mpeg",
          "data": "'"${AUDIO_BASE64}"'"
        }
      }]
    }
  }'
```

**تعبیه ویدیو (API بومی):**

```bash
VIDEO_PATH="./sample_video.mp4"
VIDEO_BASE64="$(base64 -i "$VIDEO_PATH" | tr -d '\n')"

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  --data-binary @- <<EOF
{
  "content": {
    "parts": [
      {
        "inline_data": {
          "mime_type": "video/mp4",
          "data": "${VIDEO_BASE64}"
        }
      }
    ]
  }
}
EOF
```

**تجمیع متن + تصویر (API بومی):**

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{
    "content": {
      "parts": [
        {"text": "An image of a dog"},
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "iVBORw0KGgo...[TRUNCATED]"
          }
        }
      ]
    }
  }'
```

> **یادداشت**: زمانی که چندین بخش در یک درخواست واحد ارائه می‌شوند، `gemini-embedding-2` یک تعبیه تجمیع‌شده واحد برمی‌گرداند. اگر به تعبیه‌های جداگانه برای هر ورودی نیاز دارید، از Batch API یا درخواست‌های متعدد استفاده کنید.

---

## نمونه‌های استفاده از SDK

### Chat Completions (Grok، Qwen، Kimi)

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.6",
    "messages": [
      {
        "role": "user",
        "content": "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# Using Kimi K2.6 for full-stack coding
response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {
            "role": "user",
            "content": "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form.",
        }
    ],
)

print(response.choices[0].message.content)

# Using Grok 4.20 Reasoning
response = client.chat.completions.create(
    model="grok-4.20-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Design a fault-tolerant distributed system architecture.",
        }
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)

# Using Qwen3.6-Flash with thinking mode
response = client.chat.completions.create(
    model="qwen3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "Explain quantum entanglement with practical implications.",
        }
    ],
    extra_body={"enable_thinking": True},
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// Using Kimi K2.6
const kimiResponse = await client.chat.completions.create({
  model: "kimi-k2.6",
  messages: [
    {
      role: "user",
      content: "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form.",
    },
  ],
});

console.log(kimiResponse.choices[0].message.content);

// Using Qwen3.6-Max-Preview
const qwenResponse = await client.chat.completions.create({
  model: "qwen3.6-max-preview",
  messages: [
    {
      role: "user",
      content: "Build a polished Next.js landing page for a SaaS product.",
    },
  ],
  max_tokens: 8192,
});

console.log(qwenResponse.choices[0].message.content);

```

### تولید تصویر (GPT-Image-2)

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
    "size": "1024x1024",
    "n": 1
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="gpt-image-2",
    prompt="A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
    size="1024x1024",
    n=1,
)

print(response.data[0].b64_json[:100] + "...")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "gpt-image-2",
  prompt: "A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
  size: "1024x1024",
  n: 1,
});

console.log(response.data[0].b64_json.slice(0, 100) + "...");

```

### Embeddings (Gemini Embedding 2)

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-2",
    "input": "task: search result | query: What is the meaning of life?",
    "dimensions": 768
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="gemini-embedding-2",
    input="task: search result | query: What is the meaning of life?",
    dimensions=768,
)

print(f"Embedding length: {len(response.data[0].embedding)}")
print(f"First 5 values: {response.data[0].embedding[:5]}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "gemini-embedding-2",
  input: "task: search result | query: What is the meaning of life?",
  dimensions: 768,
});

console.log(`Embedding length: ${response.data[0].embedding.length}`);
console.log(`First 5 values:`, response.data[0].embedding.slice(0, 5));

```

---

## لینک‌های مستندات

- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مستندات مدل‌های Moonshot AI](fa/providers/moonshotai.md)
- [مستندات مدل‌های Google](fa/providers/google.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API گفتگو](fa/api-reference/chat.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API Embeddings](fa/api-reference/embeddings.md)
- [مرجع API بومی Gemini v1beta](fa/api-reference/v1beta.md)
