---
hasH1: true
published: 2026-09-24
description: "مدل‌های GPT-6 Sol و Luna از OpenAI و Grok 4.7 از xAI را در AvalAI به کار ببرید؛ قیمت توکن، محدودیت زمینه، نقاط پایانی و نمونه‌های اتصال را مقایسه کنید."
---

# مدل‌های جدید: GPT-6 Sol، GPT-6 Luna و Grok 4.7

**Date:** ۱۴۰۵-۰۷-۰۲ / (2026-09-24)

## خلاصه

مدل‌های **GPT-6 Sol** و **GPT-6 Luna** از OpenAI و **Grok 4.7** از xAI اکنون برای کدنویسی، استدلال و کار حرفه‌ای در AvalAI در دسترس‌اند. هر سه از Chat Completions و Messages پشتیبانی می‌کنند. پشتیبانی Responses برای Sol و Luna کامل و برای Grok 4.7 جزئی است.

---

## جزئیات

### OpenAI: مدل‌های GPT-6 Sol و GPT-6 Luna

- **`gpt-6-sol`** قابلیت‌های GPT-6 را برای عامل‌های کدنویسی با بودجه محدود، تحلیل حرفه‌ای، کار با رایانه و مکالمه‌های طولانی فراهم می‌کند. OpenAI از بهبود دقت اطلاعات، مهندسی نرم‌افزار و راستی‌آزمایی نسبت به GPT-5.6 Sol خبر می‌دهد.
- **`gpt-6-luna`** گزینه کم‌هزینه‌تر برای دستیارهای پرترافیک، پردازش سند، بخش‌های کوچک‌تر کار کدنویسی و گردش‌کارهای ابزارمحور است. این مدل نیز از استدلال و درک تصویر پشتیبانی می‌کند.
- **`gpt-6-astra`** همچنان توانمندترین گزینه GPT-6 از OpenAI برای دشوارترین کارها است؛ این انتشار گزینه‌های تازه‌ای اضافه می‌کند و به معنی جایگزینی خودکار مدل‌ها نیست.

هر دو مدل جدید از ورودی متن و تصویر، خروجی متنی، استدلال، فراخوانی تابع، خروجی ساختاریافته، ورودی PDF و حافظه نهان (کش) پرامپت پشتیبانی می‌کنند. فهرست AvalAI برای هر مدل **حداکثر ۹۲۲٬۰۰۰ توکن ورودی** و **۱۲۸٬۰۰۰ توکن خروجی** ثبت کرده است. هنگام مهاجرت، محدودیت زمینه مدل دیگری را به این مدل‌ها تعمیم ندهید.

OpenAI از بهبود استفاده دوباره از کش، از جمله هنگام تغییر تلاش استدلالی یا دسترسی به ابزارها، و کنترل‌های تازه مانند تعیین صریح نقطه پایان بخش ذخیره‌شده خبر می‌دهد. این بهبودها در سرویس اصلی ارائه‌دهنده، پشتیبانی همه کنترل‌های کش در همه مسیرهای AvalAI را تأیید نمی‌کنند. پیشوندهای قابل استفاده مجدد را ثابت نگه دارید، استفاده واقعی از کش را بسنجید و [راهنمای کش پرامپت](fa/guides/prompt-caching.md) را ببینید. نرخ توکن‌های ورودی خوانده‌شده از کش در جدول زیر ۹۰٪ کمتر از نرخ متناظر ورودی عادی است؛ ایجاد کش تعرفه جداگانه دارد.

[راهنمای OpenAI](fa/providers/openai.md#gpt-6-sol-و-gpt-6-luna)، [صفحه GPT-6 Sol](fa/models/gpt-6-sol.md) و [صفحه GPT-6 Luna](fa/models/gpt-6-luna.md) را ببینید.

### xAI: مدل Grok 4.7

از **`grok-4.7`** برای عامل‌های کدنویسی طولانی‌مدت، راستی‌آزمایی دقیق، تهیه سند و ارائه و تحلیل فنی استفاده کنید. xAI از مدل پایه بزرگ‌تر، آموزش طولانی‌تر روی مسائل دشوار، مدیریت بهتر زمینه بلند و بازنگری سازوکارهای ایمنی نسبت به Grok 4.6 خبر می‌دهد. این بهبودها گزارش ارائه‌دهنده‌اند، نه تضمین عملکرد در AvalAI.

فهرست AvalAI **حداکثر ۵۰۰٬۰۰۰ توکن ورودی** و **۵۰۰٬۰۰۰ توکن خروجی** را همراه با قابلیت‌های بینایی، استدلال، فراخوانی ابزار، خروجی ساختاریافته و کش پرامپت ثبت کرده است. این‌ها سقف‌های جداگانه فهرست هستند و به معنی امکان استفاده هم‌زمان از هر دو سقف نیستند.

منبع معرفی، نتایج ارزیابی با تلاش استدلالی بالاتر را نیز آورده است؛ اما این برچسب‌ها مقدارهای مجاز یا پیش‌فرض `reasoning_effort` در AvalAI را مشخص نمی‌کنند. ابتدا این پارامتر را ارسال نکنید و هر کنترل اضافی را روی مسیر انتخابی خود بررسی کنید. نسخه سریع جداگانه و قابلیت‌های امنیتی نیازمند دعوت‌نامه که ارائه‌دهنده معرفی کرده است، در این خبر به‌عنوان مسیر یا دسترسی AvalAI اعلام نمی‌شوند.

[راهنمای xAI](fa/providers/xai.md#grok-4-7) و [صفحه Grok 4.7](fa/models/grok-4.7.md) را ببینید.

### دسترسی به نقاط پایانی

| مدل | `v1/chat/completions` | `v1/messages` | `v1/responses` |
| --- | --- | --- | --- |
| `gpt-6-sol` | کامل | کامل | کامل |
| `gpt-6-luna` | کامل | کامل | کامل |
| `grok-4.7` | کامل | کامل | جزئی |

**پشتیبانی جزئی Responses به معنی برابری کامل ابزارهای میزبانی‌شده یا گردش‌کارهای دارای وضعیت ذخیره‌شده نیست.** پیش از انتقال گردش‌کارهای Grok به Responses، رفت‌وبرگشت ابزارها، قالب خروجی و ادامه مکالمه را آزمایش کنید. دسترسی به یک نقطه پایانی به‌تنهایی همه ابزارهای میزبانی‌شده را برای همه مدل‌ها یا حساب‌ها فعال نمی‌کند.

### درک تصویر با تولید تصویر فرق دارد

این سه مدل **مدل تولید تصویر نیستند**. از آن‌ها برای تحلیل تصویر یا آماده‌سازی دستورهای متنی استفاده کنید، نه به‌عنوان مدل تصویر در `v1/images/generations` یا `v1/images/edits`. برای تولید و ویرایش مستقیم، همچنان مدل‌های اختصاصی مانند `gpt-image-2.5-flare` یا `gpt-image-2.5-sunburst` را به کار ببرید.

استفاده از ابزار میزبانی‌شده `image_generation` در Responses قابلیت جداگانه‌ای است که باید برای مدل، مسیر و حساب انتخابی بررسی شود. پشتیبانی کامل نقطه پایانی Responses برای Sol و Luna به‌تنهایی این ابزار را تأیید نمی‌کند و پشتیبانی جزئی Grok 4.7 نیز به معنی دسترسی به آن نیست. [API تصویر](fa/api-reference/images.md) و [راهنمای تولید تصویر](fa/guides/image-generation.md) را ببینید.

---

## قیمت‌گذاری

همه قیمت‌های زیر **به دلار آمریکا برای هر ۱ میلیون توکن** هستند، نه هزینه اشتراک. آستانه طول ورودی تعیین می‌کند کدام تعرفه ورودی، کش و خروجی برای درخواست اعمال شود. تعرفه بالاتر فقط وقتی اعمال می‌شود که طول ورودی **از آستانه بیشتر باشد**؛ این تعرفه هزینه‌ای نیست که فقط برای توکن‌های مازاد محاسبه شود.

### GPT-6 Sol و GPT-6 Luna

| مدل | طول ورودی | ورودی | ورودی ذخیره‌شده | ایجاد کش ورودی | خروجی |
| --- | --- | ---: | ---: | ---: | ---: |
| `gpt-6-sol` | حداکثر 272K، شامل خود این مقدار | $2.00 | $0.20 | $2.50 | $10.00 |
| `gpt-6-sol` | بیش از 272K | $4.00 | $0.40 | $5.00 | $15.00 |
| `gpt-6-luna` | حداکثر 272K، شامل خود این مقدار | $0.10 | $0.01 | $0.125 | $0.50 |
| `gpt-6-luna` | بیش از 272K | $0.20 | $0.02 | $0.25 | $0.75 |

### Grok 4.7

| طول ورودی | ورودی | ورودی ذخیره‌شده | خروجی |
| --- | ---: | ---: | ---: |
| حداکثر 200K، شامل خود این مقدار | $2.00 | $0.50 | $6.00 |
| بیش از 200K | $4.00 | $1.00 | $12.50 |

تعرفه توکن Grok 4.7 با Grok 4.6 یکسان است. تعرفه ورودی بیش از ۲۰۰ هزار توکن مربوط به زمینه بلند است، نه نسخه سریع ارائه‌دهنده. برای فهرست کامل، ابزارهایی که هزینه جداگانه دارند و محدودیت نرخ هر سطح حساب، [قیمت‌گذاری](fa/pricing.md) را ببینید.

---

## نمونه درخواست API و استفاده از SDK

مقدار `AVALAI_API_KEY` را در محیط سرور قرار دهید. مثال‌ها یک درخواست ساده و یکسان Chat Completions را اجرا می‌کنند. برای مقایسه مدل‌های دیگر، فقط شناسه مدل را به `gpt-6-luna` یا `grok-4.7` تغییر دهید؛ تنظیمات تلاش استدلالی یا نمونه‌برداری مدل قدیمی را بدون تأیید پشتیبانی به کار نبرید.

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-6-sol",
    "messages": [
      {"role": "user", "content": "Suggest a concise verification checklist for deploying an API behind a feature flag."}
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
    model="gpt-6-sol",
    messages=[
        {
            "role": "user",
            "content": "Suggest a concise verification checklist for deploying an API behind a feature flag.",
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
  model: "gpt-6-sol",
  messages: [
    { role: "user", content: "Suggest a concise verification checklist for deploying an API behind a feature flag." },
  ],
});

console.log(response.choices[0].message.content);

```


### پاسخ نمونه آموزشی

این یک **نمونه آموزشی** است، نه پاسخ ثبت‌شده از API زنده. شناسه، زمان، تعداد توکن‌ها و نرخ تبدیل صرفاً نمونه‌اند. با ۱۰۰ توکن ورودی عادی و ۵۰ توکن خروجی، بدون ایجاد کش یا ابزار پولی و با ورودی کمتر از ۲۷۲ هزار توکن، هزینه توکن Sol برابر ۰٫۰۰۰۷ دلار است. نرخ تبدیل این مثال ۱۰۰٬۰۰۰ تومان برای هر دلار است و نرخ روز نیست. مصرف واقعی، فیلدهای اختیاری و صورتحساب به درخواست بستگی دارند.

```json
{
  "id": "chatcmpl-gpt-6-sol-example",
  "created": 1790208000,
  "model": "gpt-6-sol",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "Verify the flag defaults off, test both paths, check authentication and error handling, monitor latency and errors during a limited rollout, and confirm rollback restores the previous behavior.",
        "annotations": []
      }
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 50,
    "total_tokens": 150,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 100,
      "audio_tokens": null,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0007000000",
    "irt": 70,
    "exchange_rate": 100000
  }
}
```

### نمونه Responses برای Sol و Luna

برای یکپارچه‌سازی مبتنی بر Responses، درخواست زیر را به کار ببرید و در صورت نیاز `gpt-6-luna` را با `gpt-6-sol` جایگزین کنید. این مثال هیچ ابزار میزبانی‌شده‌ای درخواست نمی‌کند. چون پشتیبانی Responses در Grok 4.7 جزئی است، گردش‌کار آن همچنان باید جداگانه آزمایش شود.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-6-luna",
    "input": "Give a concise rollout checklist for a new API endpoint."
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
    model="gpt-6-luna",
    input="Give a concise rollout checklist for a new API endpoint.",
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
  model: "gpt-6-luna",
  input: "Give a concise rollout checklist for a new API endpoint.",
});

console.log(response.output_text);

```


---

## چک‌لیست یکپارچه‌سازی

1. شناسه صریح مدل را انتخاب کنید: `gpt-6-sol`، `gpt-6-luna` یا `grok-4.7`. این خبر تغییر مسیر خودکار یا بازنشستگی مدل‌های قبلی را اعلام نمی‌کند.
2. پیش از انتقال ترافیک محیط عملیاتی، پرامپت‌های نماینده، نتایج ابزارها، خروجی‌های ساختاریافته، ورودی‌های تصویری و کیفیت پاسخ را مقایسه کنید.
3. محدودیت ورودی را بررسی کنید، برای توکن‌های استدلال پنهان در بودجه خروجی جا بگذارید و کنترل‌ها را با نقطه پایانی انتخابی تطبیق دهید. نتیجه کوتاه و مراحل راستی‌آزمایی بخواهید، نه زنجیره فکر پنهان.
4. استفاده از کش و هزینه کل توکن را همراه با تعرفه زمینه بلند و ابزارهای دارای هزینه جداگانه بسنجید.
5. برای گردش‌کارهای جدید Sol و Luna، Responses را در نظر بگیرید. برای Grok 4.7 با Chat Completions شروع کنید، مگر اینکه گردش‌کار دقیق Responses خود را آزموده باشید.

## مستندات مرتبط

- [مدل‌های OpenAI](fa/providers/openai.md#gpt-6-sol-و-gpt-6-luna)
- [مدل‌های xAI](fa/providers/xai.md#grok-4-7)
- [Chat Completions](fa/api-reference/chat.md)، [Messages](fa/api-reference/messages.md) و [Responses](fa/api-reference/responses.md)
- [مدل‌های استدلالی](fa/guides/reasoning.md) و [کش پرامپت](fa/guides/prompt-caching.md)
- [قیمت‌گذاری](fa/pricing.md) و [مقایسه مدل‌ها](fa/models/index.md)

برای پرسش‌های یکپارچه‌سازی یا صورتحساب، با [پشتیبانی AvalAI](https://chat.avalai.ir/platform/support/create-ticket) تماس بگیرید.
