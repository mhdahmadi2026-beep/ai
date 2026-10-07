# News 2026-06-18-new-models-glm-kimi-fireworks-nemotron: مدل‌های جدید اضافه شدند: GLM-5.2، Kimi K2.7 Code و ارائه‌دهنده جدید Fireworks.ai با Nemotron-3-Ultra
URL: `https://docs.avalai.ir/fa/news/2026-06-18-new-models-glm-kimi-fireworks-nemotron`


# مدل‌های جدید اضافه شدند: GLM-5.2، Kimi K2.7 Code و ارائه‌دهنده جدید Fireworks.ai با Nemotron-3-Ultra

**Date:** 1405-03-28 / (2026-06-18)

## خلاصه

افزودن چهار مدل جدید از سه ارائه‌دهنده، از جمله یک ارائه‌دهنده جدید با نام Fireworks.ai را اعلام می‌کنیم. مدل `glm-5.2` از Z.AI نسخه GLM-5.1 را با پنجره زمینه ۱ میلیون توکنی گسترش می‌دهد، مدل‌های `kimi-k2.7-code` و `kimi-k2.7-code-highspeed` از Moonshot.ai کدنویسی متن‌باز SOTA ارائه می‌دهند و مدل `nemotron-3-ultra` از NVIDIA اکنون از طریق ارائه‌دهنده جدید Fireworks.ai در دسترس است. همه مدل‌ها روی `v1/chat/completions` در دسترس هستند و پشتیبانی جزئی روی `v1/responses` دارند.


## خلاصه قیمت‌گذاری

| مدل | ارائه‌دهنده | ورودی ($/۱ میلیون توکن) | ورودی کش‌شده ($/۱ میلیون توکن) | خروجی ($/۱ میلیون توکن) |
|-------|----------|---------------------|----------------------------|----------------------|
| `glm-5.2` | Z.AI | $1.40 | $0.26 | $4.40 |
| `kimi-k2.7-code` | Moonshot.ai | $0.95 | $0.19 | $4.00 |
| `kimi-k2.7-code-highspeed` | Moonshot.ai | $1.90 | $0.38 | $8.00 |
| `nemotron-3-ultra` | Fireworks.ai | $0.60 | $0.12 | $2.40 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.2",
    "messages": [
      {
        "role": "user",
        "content": "این کدبیس چند فایلی بزرگ را برای افزودن یک لایه کش بازنویسی کن و برنامه مهاجرت را توضیح بده."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه پاسخ

```json
{
  "id": "chatcmpl-glm-5-2-abc123",
  "created": 1781827200,
  "model": "glm-5.2",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا برنامه مهاجرت و لایه کش بازنویسی‌شده آمده است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 412,
    "prompt_tokens": 36,
    "total_tokens": 448,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 36,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0018632000",
    "irt": 213.52,
    "exchange_rate": 114600
  }
}
```

---

## نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.7-code",
    "messages": [
      {
        "role": "user",
        "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن."
      }
    ],
    "max_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {
            "role": "user",
            "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
        }
    ],
    max_tokens=8192,
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "kimi-k2.7-code",
  messages: [
    {
      role: "user",
      content: "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
    },
  ],
  max_tokens: 8192,
});

console.log(completion.choices[0].message.content);

```

---

## پیوندهای مرتبط

- [مدل‌های Z.AI](fa/providers/zai.md)
- [مدل‌های Moonshot.ai](fa/providers/moonshotai.md)
- [مدل‌های Fireworks.ai](fa/providers/fireworksai.md)
- [قیمت‌گذاری](fa/pricing.md)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
