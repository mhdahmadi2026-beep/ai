---
hasH1: true
published: "2026-09-24"
author: "AvalAI"
description: "Claude Opus 5.5 با پشتیبانی Chat Completions، Messages و Responses، تفکر تطبیقی همیشه‌فعال و قیمت‌های جدید توکن در AvalAI در دسترس است."
---

# افزودن مدل پرچم‌دار جدید: Claude Opus 5.5

**Date:** ۱۴۰۵-۰۷-۰۲ / (2026-09-24)

## خلاصه

Claude Opus 5.5 از Anthropic برای عامل‌های کدنویسی طولانی‌مدت و کار دانشی به AvalAI اضافه شد. این مدل از Chat Completions، Messages و Responses پشتیبانی می‌کند؛ تفکر تطبیقی همیشه‌فعال، پنجره ورودی یک‌میلیون‌توکنی و تعرفه ورودی، خروجی و خواندن حافظه نهان پایین‌تری نسبت به Opus 5 دارد.

## جزئیات

### Anthropic: مدل Claude Opus 5.5

از [`claude-opus-5-5`](fa/models/claude-opus-5-5.md) برای مهندسی نرم‌افزار دشوار، پژوهش و تحلیل حرفه‌ای استفاده کنید. Anthropic این مدل را در ۱۴۰۵-۰۶-۳۱ / (2026-09-22) منتشر کرد؛ این خبر به دسترسی آن در AvalAI از ۱۴۰۵-۰۷-۰۲ / (2026-09-24) می‌پردازد.

- **کدنویسی و عامل‌های طولانی‌مدت:** برای تغییرات چندمرحله‌ای در مخزن، مهاجرت، ممیزی، اشکال‌زدایی و بررسی نتیجه پیش از اعلام پایان کار طراحی شده است.
- **کار دانشی:** از پژوهش، تحلیل سند، نگارش فنی و تهیه خروجی‌های حرفه‌ای پشتیبانی می‌کند. ادعاهای مهم را با منابع اصلی تطبیق دهید.
- **بینایی و ابزارها:** متن و تصویر را می‌پذیرد، از ورودی PDF، فراخوانی تابع، خروجی ساختاریافته و حافظه نهان پرامپت پشتیبانی می‌کند و متن تولید می‌کند. گردش‌کارهای استفاده از رایانه به تعریف ابزار سازگار و محیط اجرایی تحت کنترل برنامه نیاز دارند؛ پشتیبانی بینایی به معنی تولید تصویر نیست.
- **استدلال تطبیقی:** تفکر همیشه فعال است و تلاش پیش‌فرض ارائه‌دهنده `medium` است. تلاش را با کنترل‌های مستند Anthropic تنظیم کنید و تنظیمات ارائه‌دهندگان دیگر را تعمیم ندهید.
- **کارایی گزارش‌شده توسط ارائه‌دهنده:** Anthropic از حدود ۴۰٪ هزینه کمتر در بارهای کاری معمول با تنظیمات پیش‌فرض و بیش از ۳۰٪ سرعت بالاتر تولید خروجی نسبت به Opus 5 خبر می‌دهد. این اعداد گزارش ارائه‌دهنده درباره بارهای کاری هستند، نه تضمین کاهش تأخیر AvalAI یا تخفیف ثابت برای هر درخواست.

| مشخصه | مقدار |
| --- | --- |
| شناسه مدل در AvalAI | `claude-opus-5-5` |
| پنجره زمینه ورودی | 1,000,000 توکن |
| حداکثر خروجی | 128,000 توکن |
| تفکر | تفکر تطبیقی همیشه‌فعال |
| تلاش پیش‌فرض | `medium` |
| آخرین زمان دانش و داده آموزشی ارائه‌دهنده | June 2026 |
| دسترسی حساب | سطح ۱ یا بالاتر |

زمینه یک‌میلیون‌توکنی در این مدل بومی است؛ صرفاً برای استفاده از این ظرفیت، هدر بتای قدیمی زمینه را اضافه نکنید. ورودی، تاریخچه گفت‌وگو، نتایج ابزارها و بودجه خروجی همچنان باید با محدودیت‌های مسیر انتخابی سازگار باشند. [راهنمای Anthropic](fa/providers/anthropic.md#claude-opus-5-5) را ببینید.

### نقاط پایانی پشتیبانی‌شده

| نقطه پایانی | پشتیبانی AvalAI |
| --- | --- |
| `v1/chat/completions` | پشتیبانی کامل |
| `v1/messages` | پشتیبانی کامل |
| `v1/responses` | پشتیبانی کامل |

در هر سه نقطه پایانی، همین شناسه دقیق مدل را به کار ببرید. آدرس پایه کلاینت‌های SDK سازگار با OpenAI برابر `https://api.avalai.ir/v1` و آدرس پایه SDK رسمی Anthropic برابر `https://api.avalai.ir` است. پشتیبانی نقطه پایانی، همه ابزارهای میزبانی‌شده، هدرهای بتا، Fast mode یا قابلیت‌های Batch ارائه‌دهنده را خودبه‌خود فعال نمی‌کند. این انتشار شامل اعلام جایگزینی خودکار `claude-opus-5` یا `claude-fable-5-1` نیست.

### قیمت‌گذاری AvalAI

همه مبلغ‌های زیر به **دلار آمریکا برای هر یک میلیون توکن** هستند.

| مدل | ورودی | ورودی از حافظه نهان | ورودی ایجاد حافظه نهان | خروجی |
| --- | ---: | ---: | ---: | ---: |
| `claude-opus-5-5` | $4.00 | $0.20 | $8.00 | $20.00 |

تعرفه ورودی و خروجی نسبت به قیمت‌های مستند Opus 5، بیست درصد و هزینه خواندن حافظه نهان شصت درصد کمتر است. ایجاد حافظه نهان هزینه جداگانه دارد: **تعرفه ۸٫۰۰ دلاری AvalAI را مبنا قرار دهید**، نه نرخ ۵٫۰۰ دلاری نوشتن پنج‌دقیقه‌ای در سرویس اصلی ارائه‌دهنده. یکسان بودن مبلغ به‌تنهایی مدت نگهداری حافظه نهان را مشخص نمی‌کند؛ برای کنترل‌های پشتیبانی‌شده، [راهنمای حافظه نهان پرامپت](fa/guides/prompt-caching.md) را ببینید.

قیمت Fast mode، تخفیف Batch و خروجی ۳۰۰ هزار توکنی نسخه بتای Batch در سرویس اصلی ارائه‌دهنده، بخشی از این اعلام AvalAI نیستند. سقف خروجی مستند در اینجا همچنان ۱۲۸٬۰۰۰ توکن است. برای جزئیات فعلی حساب، [قیمت‌گذاری](fa/pricing.md) و [محدودیت نرخ](fa/rate-limits.md) را بررسی کنید.

## نکات مهاجرت

مهاجرت از Opus 5 همیشه به تغییر نام مدل محدود نمی‌شود:

1. **تفکر غیرفعال نمی‌شود.** از تفکر تطبیقی استفاده کنید و با تلاش `medium` شروع کنید. تنظیمات غیرفعال‌سازی تفکر یا بودجه ثابت تفکر گسترده را نفرستید. پارامترهای نمونه‌برداری پشتیبانی‌نشده مانند `temperature` و `top_p` را حذف کنید و پیام دستیار را از پیش تکمیل نکنید.
2. **اجبار به استفاده از ابزار خطا ایجاد می‌کند.** تنظیماتی را که فراخوانی ابزار را اجباری می‌کنند یا ابزار مشخصی را تحمیل می‌کنند، حذف کنید. اجازه دهید مدل ابزار را به روال معمول انتخاب کند و آرگومان‌های ابزار را در برنامه اعتبارسنجی کنید.
3. **بلوک‌های تفکر به مدل و گفت‌وگو وابسته‌اند.** هنگام ادامه گفت‌وگو، محتوای کامل دستیار، بلوک‌های تفکر، امضاها و زمینه فراخوانی ابزار را حفظ کنید. آن‌ها را ویرایش نکنید یا به مدل یا گفت‌وگوی دیگری منتقل نکنید. پیش از تغییر مدیریت تاریخچه، [مستندات حفظ تفکر](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) را بخوانید.
4. **ابزار قدیمی رایانه ناسازگار است.** طبق مستندات Anthropic، ابزار `computer_20251124` در Claude API و Google Cloud پذیرفته نمی‌شود. به‌جای انتقال تنظیمات بتای قدیمی، ساختار فعلی ابزار و پشتیبانی آن در مسیر AvalAI را بررسی کنید.
5. **قالب متن پیشرفت تغییر کرده است.** متن میان فراخوانی‌های ابزار اکنون در بلوک‌های تفکر می‌آید که متن آن‌ها با تنظیم پیش‌فرض نمایش خالی است. رابط نمایش پیشرفت نباید این سکوت را به معنی توقف درخواست بداند. از رویدادهای وضعیت ابزار استفاده کنید و اگر به متن پیشرفت قابل مشاهده نیاز دارید، پشتیبانی کنترل‌های نمایش را بررسی کنید.

نتیجه کوتاه، استناد و شواهد راستی‌آزمایی بخواهید، نه زنجیره فکر پنهان. برای اقدام‌های مخرب تأیید انسانی بگیرید و اسناد بیرونی و نتایج ابزار را ورودی نامطمئن بدانید. بازگشت‌های ایمنی به مدل‌های دیگر و برنامه‌های احراز صلاحیت Anthropic از دسترسی حساب AvalAI جدا هستند؛ این خبر وعده دسترسی نامحدود به همه قابلیت‌های سرویس اصلی را نمی‌دهد. [راهنمای استدلال](fa/guides/reasoning.md#claude-opus-5-5) و [نکات رسمی مهاجرت](https://platform.claude.com/docs/en/models/opus-5-5/whats-new-opus-5-5#thinking-cant-be-disabled) را ببینید.

## نمونه‌های درخواست و پاسخ API

متغیر `AVALAI_API_KEY` را فقط در سرور نگه دارید. این درخواست‌های ساده تنظیمات اختیاری تفکر را ارسال نمی‌کنند و از رفتار تطبیقی پیش‌فرض مدل استفاده می‌کنند. برای استدلال و پاسخ نهایی، بودجه خروجی کافی در نظر بگیرید.

### Chat Completions

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-5-5",
    "max_completion_tokens": 8192,
    "messages": [
      {"role": "user", "content": "Review a staged database migration and list verification and rollback checks."}
    ]
  }'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="claude-opus-5-5",
    max_completion_tokens=8192,
    messages=[
        {
            "role": "user",
            "content": "Review a staged database migration and list verification and rollback checks.",
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "claude-opus-5-5",
  max_completion_tokens: 8192,
  messages: [
    { role: "user", content: "Review a staged database migration and list verification and rollback checks." },
  ],
});

console.log(response.choices[0].message.content);

```


### نمونه آموزشی پاسخ Chat Completions

این یک **نمونه آموزشی** است، نه پاسخ ثبت‌شده از درخواست واقعی. تعداد توکن‌ها و نرخ تبدیل ارز صرفاً برای مثال هستند و قیمت روز را نشان نمی‌دهند. تعداد توکن‌های تکمیل شامل توکن‌های استدلال است؛ خود استدلال پنهان نمایش داده نشده است. پاسخ واقعی ممکن است بلوک‌های تفکر یا ابزار بیشتری داشته باشد که باید در تاریخچه گفت‌وگو حفظ شوند.

```json
{
  "id": "chatcmpl-claude-opus-5-5-example",
  "created": 1790208000,
  "model": "claude-opus-5-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Verify backup restoration, test schema compatibility, migrate a small batch, compare row counts and checksums, monitor errors and latency, and stop or roll back if predefined checks fail.",
        "annotations": []
      }
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 400,
    "total_tokens": 500,
    "completion_tokens_details": {
      "reasoning_tokens": 300
    },
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 100,
      "audio_tokens": null,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0084000000",
    "irt": 840,
    "exchange_rate": 100000
  }
}
```

بدون خواندن یا نوشتن حافظه نهان، هزینه مثال برابر `(100 × $4 + 400 × $20) / 1,000,000 = $0.0084` است. برای صورتحساب واقعی از میزان مصرف بازگردانده‌شده و [راهنمای رهگیری هزینه](fa/pricing.md) استفاده کنید.

### Messages بومی

API بومی به بودجه خروجی نیاز دارد. بلوک‌های متنی را بر اساس نوع بخوانید و فرض نکنید اولین بلوک همیشه متن است؛ این فیلتر فقط برای نمایش است و نباید جایگزین محتوای کاملی شود که برای نوبت‌های بعدی نگه می‌دارید.

```bash
curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-5-5",
    "max_tokens": 8192,
    "messages": [
      {"role": "user", "content": "Review a staged database migration and list verification and rollback checks."}
    ]
  }'

```

```python
import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir",
)

message = client.messages.create(
    model="claude-opus-5-5",
    max_tokens=8192,
    messages=[
        {
            "role": "user",
            "content": "Review a staged database migration and list verification and rollback checks.",
        }
    ],
)

print("".join(block.text for block in message.content if block.type == "text"))

```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const message = await client.messages.create({
  model: "claude-opus-5-5",
  max_tokens: 8192,
  messages: [
    { role: "user", content: "Review a staged database migration and list verification and rollback checks." },
  ],
});

console.log(message.content.filter((block) => block.type === "text").map((block) => block.text).join(""));

```


### Responses

در کلاینت‌های Responses سازگار با OpenAI، به‌جای `messages` از `input` استفاده کنید و `response.output_text` را بخوانید. فیلدهای استدلال اختصاصی OpenAI را کپی نکنید و صرف پشتیبانی نقطه پایانی را به معنی دسترسی به ابزارهای میزبانی‌شده ندانید.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-5-5",
    "max_output_tokens": 8192,
    "input": "Review a staged database migration and list verification and rollback checks."
  }'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="claude-opus-5-5",
    max_output_tokens=8192,
    input="Review a staged database migration and list verification and rollback checks.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "claude-opus-5-5",
  max_output_tokens: 8192,
  input: "Review a staged database migration and list verification and rollback checks.",
});

console.log(response.output_text);

```


## منابع مرتبط

- [مرجع مدل Claude Opus 5.5](fa/models/claude-opus-5-5.md)
- [راهنمای Anthropic](fa/providers/anthropic.md#claude-opus-5-5)
- [API تکمیل گفت‌وگو](fa/api-reference/chat.md)، [Messages API](fa/api-reference/messages.md) و [Responses API](fa/api-reference/responses.md)
- [راهنمای استدلال](fa/guides/reasoning.md#claude-opus-5-5) و [حافظه نهان پرامپت](fa/guides/prompt-caching.md)
- [قیمت‌گذاری AvalAI](fa/pricing.md) و [محدودیت نرخ](fa/rate-limits.md)
- [کارت سیستمی Anthropic](https://anthropic.com/claude-opus-5-5-system-card)
