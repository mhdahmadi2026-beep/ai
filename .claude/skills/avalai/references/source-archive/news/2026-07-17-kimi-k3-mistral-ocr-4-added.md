# مدل‌های جدید: Kimi K3 و Mistral OCR 4

**تاریخ:** ۱۴۰۵-۰۴-۲۶ / (2026-07-17)

## خلاصه

AvalAI اکنون از پرچم‌دار Kimi K3 شرکت Moonshot AI و Mistral OCR 4 پشتیبانی می‌کند. Kimi K3 استدلال همیشه‌فعال، بینایی بومی و زمینه ۱ میلیون توکنی را اضافه می‌کند؛ OCR 4 نیز استخراج layout-aware با bounding box، طبقه‌بندی بلوک، اطلاعات confidence و پشتیبانی از ۱۷۰ زبان را ارائه می‌دهد.

---

## مدل‌های جدید

### Moonshot AI: Kimi K3

`kimi-k3` توانمندترین مدل پرچم‌دار Moonshot AI تا امروز است. این مدل پراکنده Mixture-of-Experts دارای ۲٫۸ تریلیون پارامتر کل است و برای بارهای کاری زمینه‌طولانی از Kimi Delta Attention و Attention Residuals استفاده می‌کند.

**قابلیت‌های کلیدی:**

- پنجره زمینه ۱ میلیون توکنی
- درک بومی تصویر
- استدلال همیشه‌فعال با `reasoning_effort: "max"`
- کدنویسی بلندمدت و مهندسی در مقیاس ریپو
- خروجی ساختاریافته با JSON Schema سخت‌گیرانه
- فراخوانی ابزار سفارشی و گردش‌کارهای چندمرحله‌ای
- کش خودکار پرامپت برای پیشوندهای بدون تغییر
- بودجه خروجی تا ۱٬۰۴۸٬۵۷۶ توکن با `max_completion_tokens`

**پشتیبانی endpoint:**

| Endpoint | پشتیبانی |
|----------|---------|
| `v1/chat/completions` | کامل |
| `v1/messages` | کامل |
| `v1/responses` | جزئی |

> `kimi-latest` اکنون به `kimi-k3` اشاره می‌کند. درخواست‌های موجود مبتنی بر alias، قابلیت‌ها و قیمت Kimi K3 را دریافت می‌کنند. وقتی بازتولیدپذیری نسخه مدل اهمیت دارد از شناسه صریح `kimi-k3` استفاده کنید.

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-------|-------|--------------|--------|
| `kimi-k3` / `kimi-latest` | $3.00/1M توکن | $0.30/1M توکن | $15.00/1M توکن |

> **به‌روزرسانی قیمت‌گذاری Moonshot AI:** شرکت Moonshot AI مالیات ۹٪ GST سنگاپور را لغو کرده است. در نتیجه، AvalAI نیز افزایش ۱۰٪ مرتبط را حذف کرده و قیمت مدل‌های Moonshot AI در AvalAI اکنون با قیمت رسمی ارائه‌دهنده هم‌راستا است.

### Mistral AI: Mistral OCR 4

`mistral-ocr-4-0` جدیدترین مدل استخراج و درک سند Mistral AI است. این مدل صفحات سند را به Markdown ساختاریافته تبدیل می‌کند و موقعیت، نوع و confidence هر ناحیه تشخیص‌داده‌شده را نیز ارائه می‌دهد.

**قابلیت‌های کلیدی:**

- bounding box برای هایلایت، citation و redaction
- طبقه‌بندی بلوک برای عنوان، جدول، معادله، امضا و انواع دیگر محتوا
- اطلاعات confidence درون‌خطی برای اعتبارسنجی خودکار و بازبینی انسانی
- پشتیبانی از ۱۷۰ زبان در ۱۰ گروه زبانی
- خروجی ساختاریافته برای RAG، جستجو، workflowهای اسنادی عاملی، فاکتور و فرم
- پشتیبانی از فرمت‌های متداول شامل PDF، DOC، PPT، OpenDocument و تصاویر

**پشتیبانی endpoint:**

| Endpoint | پشتیبانی |
|----------|---------|
| `v1/ocr` | کامل |

> `mistral-ocr-latest` اکنون به `mistral-ocr-4-0` اشاره می‌کند و قیمت OCR 4 را دارد. ادغام‌های مبتنی بر alias می‌توانند به کار ادامه دهند، اما شناسه نسخه‌دار برای پردازش قابل بازتولید توصیه می‌شود.

**قیمت‌گذاری:**

| مدل | استخراج OCR | Annotation سند/تصویر |
|-------|----------------|---------------------------|
| `mistral-ocr-4-0` / `mistral-ocr-latest` | $0.004/صفحه | $0.005/صفحه annotation‌شده |

---

## نمونه درخواست و پاسخ API

### درخواست Chat Completions با Kimi K3

در Kimi K3 تفکر همیشه فعال است. از `reasoning_effort: "max"` استفاده کنید و فیلدهای sampling ثابت مانند `temperature` و `top_p` را ارسال نکنید.

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k3",
    "messages": [
      {
        "role": "user",
        "content": "برای جدا کردن یک مونولیت بزرگ Python برنامه مهاجرت امن پیشنهاد کن."
      }
    ],
    "reasoning_effort": "max",
    "max_completion_tokens": 4096
  }'
```

### پاسخ Kimi K3

پاسخ خلاصه‌شده زیر فیلدهای مورد استفاده در یک ادغام non-streaming استاندارد را نشان می‌دهد:

```json
{
  "id": "chatcmpl_example",
  "object": "chat.completion",
  "created": 1784275200,
  "model": "kimi-k3",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "reasoning_content": "[reasoning omitted]",
        "content": "ابتدا مرز سرویس‌ها، تست‌های characterization و مهاجرت برگشت‌پذیر strangler را تعریف کنید..."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 19,
    "completion_tokens": 248,
    "total_tokens": 267
  },
  "estimated_cost": {
    "unit": "0.004153",
    "irt": 0,
    "exchange_rate": 0
  }
}
```

در پاسخ‌های streaming، reasoning و متن نهایی می‌توانند جداگانه در deltaهای `reasoning_content` و `content` برسند. در مکالمات چندنوبتی یا فراخوانی ابزار، پیام کامل assistant برگشتی API را به درخواست بعدی اضافه کنید.

### درخواست Mistral OCR 4

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://example.com/invoice.pdf"
    },
    "include_image_base64": false
  }'
```

### پاسخ Mistral OCR 4

پاسخ زیر برای نمایش ساختار صفحه و usage بدون قراردادن داده تصاویر استخراج‌شده کوتاه شده است:

```json
{
  "pages": [
    {
      "index": 0,
      "markdown": "# فاکتور\n\nشماره فاکتور: INV-1042...",
      "images": [],
      "dimensions": {
        "dpi": 200,
        "height": 2200,
        "width": 1700
      }
    }
  ],
  "model": "mistral-ocr-4-0",
  "usage_info": {
    "pages_processed": 1
  },
  "estimated_cost": {
    "unit": "0.004000",
    "irt": 0,
    "exchange_rate": 0
  }
}
```

---

## استفاده از SDK

### Kimi K3

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k3",
    "messages": [{"role": "user", "content": "این معماری را از نظر ریسک‌های reliability بررسی کن."}],
    "reasoning_effort": "max"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {
            "role": "user",
            "content": "این معماری را از نظر ریسک‌های reliability بررسی کن.",
        }
    ],
    reasoning_effort="max",
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k3",
  messages: [
    { role: "user", content: "این معماری را از نظر ریسک‌های reliability بررسی کن." },
  ],
  reasoning_effort: "max",
});

console.log(response.choices[0].message.content);

```

### Mistral OCR 4

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://example.com/document.pdf"
    }
  }'

python=:import os
import requests

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={
        "Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://example.com/document.pdf",
        },
    },
)
response.raise_for_status()
print(response.json())

javascript=:const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://example.com/document.pdf",
    },
  }),
});

if (!response.ok) throw new Error(`OCR request failed: ${response.status}`);
console.log(await response.json());

```

---

## لینک‌های مرتبط

- [مدل‌های Moonshot AI](fa/providers/moonshotai.md)
- [مدل‌های Mistral AI](fa/providers/mistralai.md)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [API OCR](fa/api-reference/ocr.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [راهنمای فایل‌های PDF](fa/guides/pdf-files.md)
- [قیمت‌گذاری](fa/pricing.md)
