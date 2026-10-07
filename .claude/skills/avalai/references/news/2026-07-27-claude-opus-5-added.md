# News 2026-07-27-claude-opus-5-added: افزودن مدل پرچم‌دار جدید: Claude Opus 5
URL: `https://docs.avalai.ir/fa/news/2026-07-27-claude-opus-5-added`
**تاریخ:** 1405-05-05 / (2026-07-27)

# افزودن مدل پرچم‌دار جدید: Claude Opus 5

**تاریخ:** 1405-05-05 / (2026-07-27)

## خلاصه

مدل Claude Opus 5، پرچم‌دار جدید خانواده Opus شرکت Anthropic، اکنون با شناسه `claude-opus-5` در AvalAI در دسترس است. این مدل کدنویسی، کار دانشی، استفاده از کامپیوتر و اجرای عاملی بلندمدت قوی‌تر را با پنجره ورودی ۱ میلیون توکنی و تلاش استدلالی قابل تنظیم ترکیب می‌کند. مدل از `v1/chat/completions` و `v1/messages` به‌طور کامل و از `v1/responses` به‌صورت جزئی پشتیبانی می‌کند.


## قیمت‌گذاری

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند.

| مدل | ورودی | ورودی کش‌شده | ورودی ایجاد کش | خروجی |
|-----|-------|----------------|----------------|--------|
| `claude-opus-5` | $5.00 | $0.50 | $6.25 | $25.00 |

Claude Opus 5 نرخ ۵.۰۰ دلار برای ورودی و ۲۵.۰۰ دلار برای خروجی Claude Opus 4.8 را حفظ می‌کند، اما نرخ ورودی کش‌شده را به ۰.۵۰ دلار به ازای ۱ میلیون توکن کاهش می‌دهد. هنگام فعال بودن کش پرامپت، ایجاد کش به‌صورت جداگانه محاسبه می‌شود.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-5",
    "messages": [
      {
        "role": "user",
        "content": "این برنامه مهاجرت را بررسی کن، حالت‌های شکست پنهان را پیدا کن و یک rollout مرحله‌ای امن‌تر پیشنهاد بده."
      }
    ]
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد:

```json
{
  "id": "chatcmpl-claude-opus-5-example",
  "created": 1785160800,
  "model": "claude-opus-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "ریسک‌های پنهان اصلی شامل واگرایی dual-write، مسیرهای rollback ناسازگار و idempotency آزمایش‌نشده مصرف‌کننده‌ها هستند. با shadow read شروع کنید، معیارهای reconciliation اضافه کنید، هر بار یک bounded context را مهاجرت دهید و پیش از هر افزایش ترافیک، معیارهای rollback آزمایش‌شده داشته باشید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 68,
    "prompt_tokens": 24,
    "total_tokens": 92,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 24,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0018200000",
    "irt": 278.82,
    "exchange_rate": 153200
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
    "model": "claude-opus-5",
    "messages": [
      {
        "role": "user",
        "content": "معماری این مخزن را تحلیل کن و یک برنامه نوسازی قابل اتکا پیشنهاد بده."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="claude-opus-5",
    messages=[
        {
            "role": "user",
            "content": "معماری این مخزن را تحلیل کن و یک برنامه نوسازی قابل اتکا پیشنهاد بده.",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "claude-opus-5",
  messages: [
    {
      role: "user",
      content: "معماری این مخزن را تحلیل کن و یک برنامه نوسازی قابل اتکا پیشنهاد بده.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

### SDK بومی Anthropic (`v1/messages`)

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-5",
    "max_tokens": 2048,
    "messages": [
      {
        "role": "user",
        "content": "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و آزمایشی برای بازتولید آن پیشنهاد بده."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",
)

message = client.messages.create(
    model="claude-opus-5",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و آزمایشی برای بازتولید آن پیشنهاد بده.",
        }
    ],
)

print(message.content[0].text)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const message = await client.messages.create({
  model: "claude-opus-5",
  max_tokens: 2048,
  messages: [
    {
      role: "user",
      content: "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و آزمایشی برای بازتولید آن پیشنهاد بده.",
    },
  ],
});

console.log(message.content[0].text);

```

---

## تفکر تطبیقی و تلاش

Claude Opus 5 از تفکر تطبیقی و تلاش قابل تنظیم پشتیبانی می‌کند. برای کارهای معمول از تلاش پایین‌تر شروع کنید و فقط وقتی ارزیابی‌ها نشان دادند استدلال بیشتر موفقیت وظیفه را بهتر می‌کند، تلاش را افزایش دهید. از مدل نخواهید chain-of-thought پنهان را نمایش دهد؛ در عوض دلیل کوتاه، چک‌لیست بررسی یا شواهد درخواست کنید.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="claude-opus-5",
    messages=[
        {
            "role": "user",
            "content": "یک مهاجرت مرحله‌ای از monolith به سرویس‌های event-driven طراحی کن و راهبرد rollback را بررسی کن.",
        }
    ],
    extra_body={
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "xhigh"},
    },
)

print(response.choices[0].message.content)
```

---

## بارهای کاری پیشنهادی

| بار کاری | دلیل تناسب Claude Opus 5 |
|----------|--------------------------|
| مهندسی نرم‌افزار پیچیده | تحلیل قوی علت ریشه‌ای، درک کدبیس، تکرار دقیق و استفاده از ابزار |
| عامل‌های طولانی‌مدت | حفظ زمینه وظیفه در گردش‌کارهای چندمرحله‌ای و بررسی نتایج میانی |
| کار دانشی | عملکرد قوی در پژوهش، تحلیل، due diligence، استدلال عددی و کار با جدول |
| استفاده از کامپیوتر | عملکرد بهتر در گردش‌کارهای دسکتاپ، مرورگر و وظایف کسب‌وکار سرتاسری |
| تحلیل علمی | بهبود نسبت به Opus 4.8 در علوم زیستی، شیمی، بیوانفورماتیک و وظایف مرتبط با پروتئین |
| artifactهای بصری و تعاملی | خروجی بصری قوی‌تر برای رابط‌ها، نمودارها، شبیه‌سازی‌ها و خروجی‌های تعاملی |

---

## لینک‌های مرتبط

- [جزئیات مدل Claude Opus 5](fa/models/claude-opus-5.md)
- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [قیمت‌گذاری](fa/pricing.md)
