# مدل پرچم‌دار جدید اضافه شد: Claude Opus 4.8

**تاریخ:** ۱۴۰۵-۰۳-۰۷ / (2026-05-28)

## خلاصه

مدل Claude Opus 4.8، توانمندترین مدل عمومی Anthropic تا به امروز، اکنون در AvalAI در دسترس است. Opus 4.8 با بهبود در کدنویسی عاملی افق بلند، کالیبراسیون تلاش استدلالی، فراخوانی ابزار و صداقت، بر پایه Opus 4.7 ساخته شده است. این مدل دارای پنجره زمینه بومی ۱ میلیون توکنی، حداکثر ۱۲۸ هزار توکن خروجی، تفکر تطبیقی، پیام‌های سیستمی میان مکالمه، جزئیات توقف امتناع و حداقل ۱٬۰۲۴ توکنی برای کش پرامپت است. از طریق `v1/chat/completions` به همراه پشتیبانی کامل در `v1/messages` و پشتیبانی جزئی در `v1/responses` در دسترس است، همه با همان قیمت‌گذاری Opus 4.7.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Opus 4.8** (`claude-opus-4-8`)، توانمندترین مدل عمومی Anthropic تا به امروز برای استدلال پیچیده، کدنویسی عاملی افق بلند و کارهای با خودگردانی بالا را اعلام می‌کنیم. [مستندات](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**

- **بهبود کدنویسی عاملی افق بلند**: مدیریت بهتر زمینه طولانی، فشرده‌سازی‌های کمتر و بازیابی بهتر پس از فشرده‌سازی برای وظایف در مقیاس پایگاه کد
- **کالیبراسیون تلاش استدلالی**: رفتار قابل اعتمادتر در هر سطح تلاش در طیف وسیعی از حوزه‌ها
- **فراخوانی بهتر ابزار**: کاهش موارد رد کردن فراخوانی ابزار مورد نیاز وظیفه و رفع مشکلات verbosity در کامنت‌ها و فراخوانی ابزار که در Opus 4.7 دیده می‌شد
- **افزایش صداقت**: تقریبا چهار برابر کمتر از Opus 4.7 احتمال دارد که نقص‌های کد نوشته‌شده توسط خود را بدون اشاره عبور دهد، با گزارش قابل اعتمادتر عدم قطعیت
- **پنجره زمینه بومی ۱ میلیون توکنی**: پشتیبانی پیش‌فرض در Claude API برای زمینه گسترده تا ۱ میلیون توکن
- **۱۲۸ هزار توکن خروجی**: پشتیبانی از تولید خروجی بزرگتر
- **تفکر تطبیقی**: تنها حالت تفکر پشتیبانی‌شده در Opus 4.8 (بودجه تفکر گسترده حذف شده)
- **پیام‌های سیستمی میان مکالمه**: افزودن دستورالعمل‌های به‌روزرسانی شده در ادامه مکالمه‌های طولانی بدون شکستن hit کش پرامپت یا بازنویسی کامل پرامپت سیستم
- **جزئیات توقف امتناع**: شی `stop_details` در پاسخ‌های امتناع اکنون به‌طور عمومی مستند شده و مسیریابی کلاس‌های مختلف درخواست‌های رد شده را آسان می‌کند
- **حداقل کش پرامپت پایین‌تر**: حداقل طول قابل کش‌گذاری پرامپت اکنون ۱٬۰۲۴ توکن (کاهش از Opus 4.7) است که امکان ایجاد ورودی‌های کش برای پرامپت‌های کوتاه‌تر را فراهم می‌کند
- **مقادیر پیش‌فرض تلاش**: `high` سطح تلاش پیش‌فرض در Claude API و Claude Code است؛ از `low`، `medium`، `high`، `xhigh` و `max` پشتیبانی می‌کند
- **عامل‌های قوی استفاده از کامپیوتر و مرورگر**: ۸۴٪ در Online-Mind2Web، جهش قابل توجهی نسبت به Opus 4.7
- **هم‌راستایی بهبود یافته**: نرخ‌های قابل توجه پایین‌تر رفتارهای ناهم‌راستا نسبت به Opus 4.7 و ویژگی‌های اجتماعی قوی‌تر
- **مسیریابی هوشمند**: توزیع در بین Anthropic API، AWS Bedrock، Azure AI و Vertex AI برای بالاترین عملکرد و دسترسی‌پذیری
- **پشتیبانی نقاط پایانی**: در دسترس در `v1/chat/completions` (پشتیبانی کامل)، `v1/messages` (پشتیبانی کامل) و `v1/responses` (پشتیبانی جزئی)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | ورودی ایجاد کش | خروجی |
|-------|-------|--------------|----------------|--------|
| claude-opus-4-8 | ۵.۰۰ دلار/۱M توکن | ۱.۵۰ دلار/۱M توکن | ۶.۲۵ دلار/۱M توکن | ۲۵.۰۰ دلار/۱M توکن |

> قیمت‌گذاری نسبت به Claude Opus 4.7 تغییر نکرده است. AvalAI در حال حاضر Opus 4.8 را با نرخ استفاده عادی محاسبه می‌کند.

### مسیریابی هوشمند

Claude Opus 4.8 از نام مستعار `claude-opus-4-8` با مسیریابی هوشمند در تمام ارائه‌دهندگان ابری رسمی Anthropic استفاده می‌کند. ارائه‌دهنده زیرساختی می‌تواند Anthropic API، AWS Bedrock، Azure AI یا Vertex AI باشد و درخواست‌ها برای بالاترین عملکرد و دسترسی‌پذیری به بهترین ارائه‌دهنده موجود توزیع می‌شوند.

هنگامی که یک درخواست از طریق AWS Bedrock مسیریابی می‌شود، فیلد `model` در پاسخ شناسه مدل Bedrock (مانند `global.anthropic.claude-opus-4-8`) را نشان خواهد داد.

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-8",
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
  "id": "chatcmpl-2af11...",
  "created": 1779148800,
  "model": "global.anthropic.claude-opus-4-8",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "سلام! 👋 چطور می‌توانم کمکتان کنم؟",
        "role": "assistant",
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 14,
    "prompt_tokens": 9,
    "total_tokens": 23,
    "completion_tokens_details": {
      "reasoning_tokens": 0,
      "text_tokens": 14
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
    "unit": "0.0003950000",
    "irt": 60.51,
    "exchange_rate": 153200
  },
  "service_tier": "default"
}
```

> **توجه:** فیلد `model` در پاسخ ممکن است شناسه مدل ارائه‌دهنده زیرساختی (مانند `global.anthropic.claude-opus-4-8` برای AWS Bedrock) را نمایش دهد نه نام مستعار `claude-opus-4-8`. این رفتار طبیعی مسیریابی هوشمند است.

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-8",
    "messages": [
      {
        "role": "user",
        "content": "یک پایگاه کد چندسرویسی بزرگ را برای استفاده از میان‌افزار مدیریت خطای مشترک بازنویسی کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از claude-opus-4-8 با مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
completion = client.chat.completions.create(
    model="claude-opus-4-8",  # مسیریابی هوشمند در Anthropic، AWS، Azure، GCP
    messages=[
        {
            "role": "user",
            "content": "یک پایگاه کد چندسرویسی بزرگ را برای استفاده از میان‌افزار مدیریت خطای مشترک بازنویسی کن.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از claude-opus-4-8 با مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
const completion = await client.chat.completions.create({
  model: "claude-opus-4-8", // مسیریابی هوشمند در Anthropic، AWS، Azure، GCP
  messages: [
    {
      role: "user",
      content:
        "یک پایگاه کد چندسرویسی بزرگ را برای استفاده از میان‌افزار مدیریت خطای مشترک بازنویسی کن.",
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
    "model": "claude-opus-4-8",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "پیام‌های سیستمی میان مکالمه را در Claude Opus 4.8 توضیح بده."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-opus-4-8",  # مسیریابی هوشمند فعال
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "پیام‌های سیستمی میان مکالمه را در Claude Opus 4.8 توضیح بده.",
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
  model: "claude-opus-4-8", // مسیریابی هوشمند فعال
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "پیام‌های سیستمی میان مکالمه را در Claude Opus 4.8 توضیح بده.",
    },
  ],
});

console.log(message.content[0].text);

```

### پیام‌های سیستمی میان مکالمه

Claude Opus 4.8 از پیام‌های `role: "system"` بلافاصله پس از یک نوبت کاربر در آرایه `messages` پشتیبانی می‌کند. این قابلیت به شما اجازه می‌دهد دستورالعمل‌های به‌روزرسانی‌شده را در ادامه یک مکالمه طولانی بدون بازنویسی کامل پرامپت سیستم اضافه کنید، که hit کش پرامپت در نوبت‌های قبلی را حفظ کرده و هزینه ورودی در حلقه‌های عاملی را کاهش می‌دهد. هیچ هدر بتایی لازم نیست.

```python
message = client.messages.create(
    model="claude-opus-4-8",
    max_tokens=1024,
    system="شما یک ایجنت کدنویسی خودگردان هستید.",
    messages=[
        {"role": "user", "content": "مهاجرت را شروع کن."},
        {"role": "assistant", "content": "شروع مهاجرت..."},
        {"role": "user", "content": "بررسی‌های قالب‌بندی را اعمال کن."},
        {
            "role": "system",
            "content": "از این به بعد، linter را روی هر فایلی که تغییر می‌دهی اجرا کن.",
        },
        {"role": "user", "content": "با src/services/ ادامه بده."},
    ],
)
```

### تفکر تطبیقی و تلاش

Claude Opus 4.8 همان مدل تفکر تطبیقی Opus 4.7 را به ارث می‌برد. از بودجه تفکر گسترده پشتیبانی نمی‌کند — `thinking: {"type": "adaptive"}` را تنظیم کنید و از پارامتر `effort` برای کنترل عمق استدلال استفاده کنید. تلاش پیش‌فرض در Opus 4.8 در همه سطوح، شامل Claude API و Claude Code، `high` است. پنج سطح تلاش عبارتند از `low`، `medium`، `high`، `xhigh` و `max`.

```python
response = client.chat.completions.create(
    model="claude-opus-4-8",
    messages=[
        {
            "role": "user",
            "content": "یک مهاجرت چند هفته‌ای از monolith به microservices را با در نظر گرفتن ریسک مهاجرت داده برنامه‌ریزی کن.",
        }
    ],
    extra_body={
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "xhigh"},
    },
)
```

### تغییرات کلیدی نسبت به Opus 4.7

- **پیام‌های سیستمی میان مکالمه**: قابلیت جدید برای افزودن پیام‌های `role: "system"` در میانه مکالمه با حفظ hit کش پرامپت.
- **جزئیات توقف امتناع**: شی `stop_details` در پاسخ‌های امتناع اکنون به‌طور عمومی مستند شده و برای مسیریابی کلاس‌های مختلف درخواست‌های رد شده مفید است.
- **حداقل کش پرامپت پایین‌تر**: طول قابل کش‌گذاری پرامپت اکنون ۱٬۰۲۴ توکن (کاهش از Opus 4.7) است و امکان ایجاد ورودی‌های کش برای پرامپت‌های کوتاه‌تر را فراهم می‌کند.
- **مقادیر پیش‌فرض تلاش**: سطح تلاش پیش‌فرض اکنون در همه سطوح (Claude API و Claude Code) برابر `high` است.
- **بهبود فراخوانی ابزار و مدیریت فشرده‌سازی**: مسیرهای عاملی طولانی پس از فشرده‌سازی با انحرافات کمتر روی وظیفه باقی می‌مانند؛ فراخوانی‌های ابزار از دست‌رفته کمتر.
- **محدودیت‌های API بدون تغییر**: پارامترهای نمونه‌برداری (`temperature`، `top_p`، `top_k`) و بودجه‌های تفکر گسترده همچنان پشتیبانی نمی‌شوند، مشابه Opus 4.7.
- **همان قیمت‌گذاری**: قیمت‌گذاری استفاده عادی با Opus 4.7 یکسان است (۵ دلار/۱M ورودی، ۲۵ دلار/۱M خروجی).

---

## لینک‌های مرتبط

- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [قیمت‌گذاری](fa/pricing.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
