# مدل جدید اضافه شد: Claude Opus 4.7

**تاریخ:** ۱۴۰۵-۰۱-۲۸ / (2026-04-17)

## خلاصه

مدل Claude Opus 4.7، توانمندترین مدل عمومی Anthropic، اکنون در AvalAI در دسترس است. Opus 4.7 بهبودهای قابل توجهی نسبت به Opus 4.6 در مهندسی نرم‌افزار پیشرفته، بینایی با وضوح بالا، پیروی از دستورالعمل‌ها و کار عاملی افق بلند ارائه می‌دهد. این مدل دارای پنجره زمینه ۱ میلیون توکنی، حداکثر ۱۲۸ هزار توکن خروجی، تفکر تطبیقی و سطح تلاش جدید `xhigh` است. از طریق `v1/chat/completions` و نقطه پایانی بومی Anthropic در `v1/messages` با مسیریابی هوشمند در بین Anthropic API، AWS Bedrock، Azure AI و Vertex AI در دسترس است.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Opus 4.7** (`claude-opus-4-7`)، توانمندترین مدل عمومی Anthropic برای استدلال پیچیده و کدنویسی عاملی را اعلام می‌کنیم. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**

- **مهندسی نرم‌افزار پیشرفته**: بهبود قابل توجه نسبت به Opus 4.6، با پیشرفت‌های ویژه در سخت‌ترین وظایف کدنویسی. مدیریت وظایف پیچیده و طولانی‌مدت با دقت و ثبات
- **بینایی با وضوح بالا**: پذیرش تصاویر تا ۲,۵۷۶ پیکسل در لبه بلند (~۳.۷۵ مگاپیکسل)، بیش از سه برابر مدل‌های قبلی Claude
- **پنجره زمینه ۱ میلیون توکنی**: پشتیبانی کامل از پنجره زمینه گسترده تا ۱ میلیون توکن
- **۱۲۸K توکن خروجی**: پشتیبانی از تولید خروجی بزرگتر
- **تفکر تطبیقی**: تنها حالت تفکر پشتیبانی‌شده در Opus 4.7 (بودجه تفکر گسترده حذف شده)
- **سطح تلاش جدید `xhigh`**: پنج سطح تلاش (پایین، متوسط، بالا، فوق‌بالا، حداکثر) برای کنترل دقیق‌تر استدلال در مقابل تاخیر
- **بودجه وظایف (بتا)**: بودجه‌های مشاوره‌ای توکن در حلقه‌های عاملی کامل
- **بهبود پیروی از دستورالعمل‌ها**: اجرای دقیق دستورالعمل‌ها، انطباق بسیار بهتر
- **حافظه سیستم فایلی**: بهتر در نوشتن و استفاده از حافظه مبتنی بر سیستم فایل در بین جلسات
- **مسیریابی هوشمند**: توزیع درخواست‌ها در بین Anthropic API، AWS Bedrock، Azure AI و Vertex AI برای بالاترین عملکرد
- **پشتیبانی نقاط پایانی**: در دسترس در `v1/chat/completions` و `v1/messages` (SDK بومی Anthropic)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | ورودی ایجاد کش | خروجی |
|-------|-------|--------------|----------------|--------|
| claude-opus-4-7 | ۵.۰۰ دلار/۱M توکن | ۱.۵۰ دلار/۱M توکن | ۶.۲۵ دلار/۱M توکن | ۲۵.۰۰ دلار/۱M توکن |

### مسیریابی هوشمند

Claude Opus 4.7 از نام مستعار `claude-opus-4-7` با مسیریابی هوشمند در تمام ارائه‌دهندگان ابری رسمی Anthropic استفاده می‌کند. ارائه‌دهنده زیرساختی می‌تواند Anthropic API، AWS Bedrock، Azure AI یا Vertex AI باشد و درخواست‌ها برای بالاترین عملکرد و دسترسی‌پذیری به بهترین ارائه‌دهنده موجود توزیع می‌شوند.

هنگامی که یک درخواست از طریق AWS Bedrock مسیریابی می‌شود، فیلد `model` در پاسخ شناسه مدل Bedrock (مانند `global.anthropic.claude-opus-4-7`) را نشان خواهد داد.

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [
      {
        "role": "user",
        "content": "سلام!"
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-1af11...",
  "created": 1776413861,
  "model": "global.anthropic.claude-opus-4-7",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Hi there! 👋 How are you doing today? Is there anything I can help you with?",
        "role": "assistant",
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 25,
    "prompt_tokens": 9,
    "total_tokens": 34,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "text_tokens": 25
    },
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 9,
      "image_tokens": null,
      "video_tokens": null,
      "cache_creation_tokens": 0
    },
    "cache_creation_input_tokens": 0,
    "cache_read_input_tokens": 0
  },
  "estimated_cost": {
    "unit": "0.0006700000",
    "irt": 102.64,
    "exchange_rate": 153200
  },
  "service_tier": "default"
}
```

> **توجه:** فیلد `model` در پاسخ ممکن است شناسه مدل ارائه‌دهنده زیرساختی (مانند `global.anthropic.claude-opus-4-7` برای AWS Bedrock) را نمایش دهد نه نام مستعار `claude-opus-4-7`. این رفتار طبیعی مسیریابی هوشمند است.

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-7",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای جستجوی دودویی بنویس."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از claude-opus-4-7 با مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
completion = client.chat.completions.create(
    model="claude-opus-4-7",  # مسیریابی هوشمند در Anthropic، AWS، Azure، GCP
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای جستجوی دودویی بنویس.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از claude-opus-4-7 با مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
const completion = await client.chat.completions.create({
  model: "claude-opus-4-7",  // مسیریابی هوشمند در Anthropic، AWS، Azure، GCP
  messages: [
    {
      role: "user",
      content: "یک تابع پایتون برای جستجوی دودویی بنویس.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### استفاده از SDK Anthropic (v1/messages)

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-7",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "تفکر تطبیقی در Claude Opus 4.7 را توضیح بده."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-opus-4-7",  # مسیریابی هوشمند فعال
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "تفکر تطبیقی در Claude Opus 4.7 را توضیح بده.",
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
  model: "claude-opus-4-7",  // مسیریابی هوشمند فعال
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "تفکر تطبیقی در Claude Opus 4.7 را توضیح بده.",
    },
  ],
});

console.log(message.content[0].text);

```

### تغییرات کلیدی نسبت به Opus 4.6

- **حذف بودجه تفکر گسترده**: تنظیم `thinking: {"type": "enabled", "budget_tokens": N}` خطای 400 برمی‌گرداند. به جای آن از `thinking: {"type": "adaptive"}` استفاده کنید.
- **حذف پارامترهای نمونه‌برداری**: تنظیم غیرپیش‌فرض `temperature`، `top_p` یا `top_k` خطای 400 برمی‌گرداند.
- **حذف محتوای تفکر به صورت پیش‌فرض**: از `display: "summarized"` برای فعال‌سازی مجدد استفاده کنید.
- **بروزرسانی توکنایزر**: ورودی یکسان ممکن است تقریبا ۱ تا ۱.۳۵ برابر توکن بیشتر نسبت به Opus 4.6 مصرف کند.
- **سطح تلاش جدید `xhigh`**: بین `high` و `max`، توصیه شده برای کدنویسی و موارد استفاده عاملی.

---

## لینک‌های مرتبط

- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [مسیریابی هوشمند Claude](fa/news/2025-11-28-claude-base-models-smart-routing.md)
