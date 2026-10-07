# مدل‌های پیشرفته جدید: Gemini 3 Pro Preview و Kimi K2 Thinking

**تاریخ:** 1404-08-27 / (2025-11-18)

## خلاصه

ما اضافه شدن دو مدل پرچمدار را اعلام می‌کنیم: [`gemini-3-pro-preview`](fa/providers/google.md) از Google و [`kimi-k2-thinking`](fa/providers/moonshotai.md) از Moonshot AI. Gemini 3 Pro Preview پیشرفته‌ترین مدل Google برای وظایف استدلال پیچیده با پنجره زمینه 1 میلیون توکن است، در حالی که Kimi K2 Thinking جدیدترین مدل پرچمدار Moonshot AI با قابلیت‌های استدلال عمیق و استفاده از ابزار چند مرحله‌ای است. هر دو مدل در [`v1/chat/completions`](fa/api-reference/chat.md) با پشتیبانی جزئی در [`v1/responses`](fa/api-reference/responses.md) در دسترس هستند.

---

## جزئیات

### Google Gemini

#### Gemini 3 Pro Preview

پیشرفته‌ترین مدل Google در سری Gemini، [`gemini-3-pro-preview`](fa/providers/google.md) نشان‌دهنده پیشرفت قابل توجهی در قابلیت‌های هوش مصنوعی است. این مدل چندوجهی بومی در وظایف استدلال پیچیده برتری دارد و می‌تواند مجموعه داده‌های گسترده از منابع اطلاعاتی متعدد شامل متن، صدا، تصویر، ویدیو و مخازن کد کامل را درک کند.

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 1 میلیون توکن برای مدیریت مکالمات و اسناد گسترده
- **توکن‌های خروجی**: 64 هزار توکن برای پاسخ‌های جامع
- **قابلیت‌های پیشرفته**: پشتیبانی بومی چندوجهی (متن، بینایی، صدا)، استدلال، فراخوانی تابع، خروجی‌های ساختاریافته
- **معماری**: مدل مبتنی بر ترنسفورمر با ترکیب متخصصان پراکنده (MoE)
- **تاریخ قطع دانش**: ژانویه 2025
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`، پشتیبانی جزئی در `v1/responses`

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| gemini-3-pro-preview | 2.00 دلار/1 میلیون توکن | 0.825 دلار/1 میلیون توکن | 12.00 دلار/1 میلیون توکن | بالای 200K: ورودی 4.00 دلار، خروجی 18.00 دلار |

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": "معماری فنی یک سیستم توزیع‌شده را تحلیل کنید و استراتژی‌های بهینه‌سازی پیشنهاد دهید."
      }
    ],
    "max_tokens": 2048
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1731945600,
  "model": "gemini-3-pro-preview",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "بگذارید معماری سیستم توزیع‌شده را تحلیل کنم...\n\n## تحلیل معماری سیستم\n\n1. **لایه توازن بار**\n   - پیاده‌سازی فعلی از round-robin استفاده می‌کند...\n\n2. **استراتژی‌های بهینه‌سازی**\n   - پیاده‌سازی توازن بار تطبیقی...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 450,
    "prompt_tokens": 25,
    "total_tokens": 475,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 25,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0054500000",
    "irt": 624.93,
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
    "model": "gemini-3-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله پیچیده را گام به گام حل کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gemini-3-pro-preview",
    messages=[
        {
            "role": "user",
            "content": "این مسئله پیچیده را گام به گام حل کنید.",
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
  model: "gemini-3-pro-preview",
  messages: [
    {
      role: "user",
      content: "این مسئله پیچیده را گام به گام حل کنید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

### Moonshot AI

#### Kimi K2 Thinking

جدیدترین مدل پرچمدار Moonshot AI، [`kimi-k2-thinking`](fa/providers/moonshotai.md)، یک مدل استدلال عاملی چندمنظوره است که برای استدلال عمیق و استفاده از ابزار چند مرحله‌ای طراحی شده است. این مدل در حل مسائل بسیار پیچیده از طریق زنجیره‌های استدلال گسترده و فراخوانی‌های متوالی ابزار برتری دارد.

**ویژگی‌های کلیدی:**
- **استدلال عمیق**: قابلیت‌های استدلال گسترده با فیلد `reasoning_content`
- **استفاده از ابزار چند مرحله‌ای**: طراحی شده برای انجام استدلال عمیق در فراخوانی‌های متعدد ابزار
- **عملکرد عاملی**: برتری در برنامه‌ریزی و اجرای وظایف چند مرحله‌ای پیچیده
- **حل مسئله پیشرفته**: قادر به مقابله با سخت‌ترین مسائل از طریق استدلال گام به گام
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`، پشتیبانی جزئی در `v1/responses`

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| kimi-k2-thinking | 0.60 دلار/1 میلیون توکن | 0.15 دلار/1 میلیون توکن | 2.50 دلار/1 میلیون توکن | زمینه جستجو: 0.005 دلار به ازای هر پرس‌وجو |

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2-thinking",
    "messages": [
      {
        "role": "user",
        "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید"
      }
    ],
    "max_tokens": 16000,
    "temperature": 1.0,
    "stream": true
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-xyz789",
  "created": 1731945600,
  "model": "kimi-k2-thinking",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "## استراتژی جامع بازاریابی دیجیتال\n\n### فاز 1: پایه‌گذاری\n1. **توسعه هویت برند**\n   - تعریف ارزش‌های اصلی و ماموریت\n   - ایجاد سیستم هویت بصری\n\n### فاز 2: استراتژی کانال\n...",
        "role": "assistant",
        "reasoning_content": "بگذارید این موضوع را به صورت سیستماتیک بررسی کنم. ابتدا، باید زمینه استارتاپ را درک کنم... سپس یک رویکرد چند فازی را ساختار می‌دهم...",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1250,
    "prompt_tokens": 20,
    "total_tokens": 1270,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 20,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0034125000",
    "irt": 391.07,
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
    "model": "kimi-k2-thinking",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله پیچیده را حل کنید."
      }
    ],
    "max_tokens": 16000,
    "temperature": 1.0
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="kimi-k2-thinking",
    messages=[
        {
            "role": "user",
            "content": "این مسئله پیچیده را حل کنید.",
        }
    ],
    max_tokens=16000,
    temperature=1.0,
)

# دسترسی به محتوای استدلال در صورت وجود
message = completion.choices[0].message
if hasattr(message, "reasoning_content"):
    reasoning = getattr(message, "reasoning_content")
    print("استدلال:", reasoning)

print("پاسخ:", message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "kimi-k2-thinking",
  messages: [
    {
      role: "user",
      content: "این مسئله پیچیده را حل کنید.",
    },
  ],
  max_tokens: 16000,
  temperature: 1.0,
});

// دسترسی به محتوای استدلال در صورت وجود
const message = completion.choices[0].message;
if ("reasoning_content" in message) {
  console.log("استدلال:", message.reasoning_content);
}

console.log("پاسخ:", message.content);

```

### تنظیمات توصیه‌شده برای Kimi K2 Thinking

برای عملکرد بهینه با [`kimi-k2-thinking`](fa/providers/moonshotai.md):

- **max_tokens**: حداقل 16,000 تنظیم کنید تا اطمینان حاصل شود که reasoning_content و محتوای نهایی کامل برگردانده می‌شوند
- **temperature**: از 1.0 برای بهترین عملکرد استفاده کنید
- **stream**: فعال‌سازی streaming (`stream: true`) برای تجربه کاربری بهتر و جلوگیری از مشکلات timeout
- **استدلال چند مرحله‌ای**: کل `reasoning_content` از پاسخ‌های قبلی را در زمینه خود قرار دهید

---

## منسوخ شدن مدل‌های Google

Google مدل‌های زیر را منسوخ کرده است که از همین الان اعمال می‌شود. ما توصیه می‌کنیم به [`gemini-3-pro-preview`](fa/providers/google.md) یا سایر مدل‌های فعلی مهاجرت کنید. برای جزئیات بیشتر به [صفحه منسوخ‌شده‌ها](fa/deprecations.md) مراجعه کنید.

**مدل‌های منسوخ‌شده:**
- `gemini-2.0-flash-exp`
- `gemini-2.0-flash-lite-preview`
- `gemini-2.0-flash-lite-preview-02-05`
- `gemini-2.0-flash-thinking-exp`
- `gemini-2.0-flash-thinking-exp-01-21`
- `gemini-2.0-flash-thinking-exp-1219`
- `gemini-2.5-flash-lite-preview-06-17`
- `gemini-2.5-flash-preview-05-20`
- `gemini-2.5-pro-preview-06-05`
- `gemini-2.5-pro-preview-03-25`
- `gemini-2.5-pro-preview-05-06`

---

## لینک‌های مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [مستندات مدل‌های Moonshot AI](fa/providers/moonshotai.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [قیمت‌گذاری مدل](fa/pricing.md)
- [منسوخ‌شدن مدل‌ها](fa/deprecations.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)