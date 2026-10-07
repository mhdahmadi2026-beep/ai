# News 2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added: افزودن مدل‌های جدید: Qwen3.8-27B و Qwen3.8-Flash
URL: `https://docs.avalai.ir/fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added`
**تاریخ:** ۱۴۰۵-۰۶-۰۷ / (2026-08-29)

# افزودن مدل‌های جدید: Qwen3.8-27B و Qwen3.8-Flash

**تاریخ:** ۱۴۰۵-۰۶-۰۷ / (2026-08-29)

## خلاصه

مدل‌های جدید Qwen3.8 شرکت Alibaba با شناسه‌های [`qwen3.8-27b`](fa/providers/alibaba.md#qwen38-27b) و [`qwen3.8-flash`](fa/providers/alibaba.md#qwen38-flash) اکنون برای کدنویسی، کارهای عاملی، استدلال و درک چندوجهی از طریق AvalAI در دسترس هستند. هر دو مدل از [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/messages`](fa/api-reference/messages.md) پشتیبانی می‌کنند و برای [`v1/responses`](fa/api-reference/responses.md) پشتیبانی جزئی دارند.

---

## جزئیات

### Alibaba Qwen3.8

مدل [`qwen3.8-27b`](fa/providers/alibaba.md#qwen38-27b) یک مدل متراکم و فشرده ۲۷ میلیارد پارامتری است که نسل Qwen3.8 را به شکلی مناسب برای استقرار ارائه می‌دهد. این مدل به‌طور بومی بینایی-زبان است و تصویر و ویدیو را درک می‌کند و کنترل انعطاف‌پذیر تفکر با تنظیم `reasoning_effort` و پشتیبانی از `preserve_thinking` برای گردش‌کارهای چندنوبتی دارد.

مدل [`qwen3.8-flash`](fa/providers/alibaba.md#qwen38-flash) نام مستعار مدیریت‌شده `qwen3.8-flash-next` است؛ مدلی از جنس ترکیب متخصصان با ۱۲۵ میلیارد پارامتر کل که در هر توکن ۶ میلیارد پارامتر را فعال می‌کند. معماری ترکیبی Gated DeltaNet و توجه پراکنده Qwen (QSA) هزینه سرویس‌دهی زمینه طولانی را کاهش می‌دهد و ۵۱ میلیارد پارامتر additional در قالب embedding N-gram، ظرفیت مدل را با هزینه محاسباتی ناچیز در هر توکن افزایش می‌دهد. در AvalAI این مدل تا ۲۶۲٬۱۴۴ توکن ورودی و ۶۵٬۵۳۶ توکن خروجی پشتیبانی می‌کند.

**ویژگی‌های کلیدی:**

- **درک بینایی-زبان**: هر دو مدل ورودی تصویر و ویدیو را می‌پذیرند؛ از نمودارهای STEM و اسناد تا ویدیوهای چندساعته
- **کنترل انعطاف‌پذیر تفکر**: حالت تفکر به‌صورت پیش‌فرض فعال است؛ `reasoning_effort` مقدارهای `low`، `medium` و `xhigh` را برای تنظیم عمق و هزینه می‌پذیرد
- **زمینه طولانی**: پنجره ورودی ۲۶۲٬۱۴۴ توکنی در AvalAI برای هر دو مدل
- **توانایی عاملی**: نتایج گزارش‌شده توسط ارائه‌دهنده شامل ۷۳.۰ در Terminal Bench 2.1، ۶۱.۷ در SWE-bench Pro و ۸۴.۳ در OSWorld-Verified برای `qwen3.8-27b` و ۷۳.۵ در Toolathlon Verified و ۹۱.۷ در GPQA Diamond برای `qwen3.8-flash`
- **قابلیت‌های توسعه‌دهنده**: فراخوانی تابع، انتخاب ابزار، پاسخ جریانی و پشتیبانی از محتوای استدلالی در تمام نقاط پایانی
- **مناسب برای**: `qwen3.8-flash` برای چت و گردش‌کارهای عاملی پرحجم و کم‌هزینه؛ `qwen3.8-27b` برای استقرارهای مدل متراکم که به بینایی، کدنویسی و قابلیت اطمینان بلندمدت نیاز دارند

### نکات برجسته بنچمارک به گزارش Alibaba

| ارزیابی | qwen3.8-flash | qwen3.8-27b |
|---------|---------------|-------------|
| GPQA Diamond | 91.7 | 89.2 |
| LiveCodeBench v6 | 91.9 | 90.3 |
| SWE-bench Pro | 62.5 | 61.7 |
| CoWorkBench | 73.9 | 70.7 |
| Toolathlon Verified | 73.5 | 67.1 |
| OSWorld-Verified | 52.3 (partial) | 84.3 |

این نتایج که Alibaba گزارش کرده است، شواهدی جهت‌دهنده هستند. پیش از هدایت ترافیک محیط تولید، مدل‌ها را با پرامپت‌ها، ابزارها، رسانه‌ها و معیارهای پذیرش متناسب با کاربرد خود ارزیابی کنید.

### دسترسی نقاط پایانی

| نقطه پایانی | پشتیبانی | توضیحات |
|-------------|----------|---------|
| [`v1/chat/completions`](fa/api-reference/chat.md) | پشتیبانی می‌شود | Chat Completions سازگار با OpenAI |
| [`v1/messages`](fa/api-reference/messages.md) | پشتیبانی می‌شود | Messages API سازگار با Anthropic |
| [`v1/responses`](fa/api-reference/responses.md) | پشتیبانی جزئی | پارامترها، ابزارها و نوع‌های ورودی موردنیاز را پیش از استفاده در محیط تولید بررسی کنید |

---

## قیمت‌گذاری

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند.

| مدل | ورودی | ساخت کش | ورودی کش‌شده | خروجی |
|-----|-------|----------|----------------|--------|
| `qwen3.8-flash` | $0.15 | $0.20 | $0.016 | $0.47 |
| `qwen3.8-27b` | $0.50 | $0.625 | $0.10 | $2.00 |

تفکیک کامل محدودیت نرخ بر اساس سطح حساب را در [صفحه قیمت‌گذاری](fa/pricing.md) ببینید.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-flash",
    "messages": [
      {
        "role": "user",
        "content": "این برنامه مهاجرت را بررسی کن و سه فرض پرریسک آن را مشخص کن."
      }
    ]
  }'
```

### پاسخ

نمونه کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد. تعداد توکن‌ها و هزینه با توجه به درخواست و خروجی تولیدشده تغییر می‌کند.

```json
{
  "id": "chatcmpl-qwen38flash-example",
  "created": 1788000000,
  "model": "qwen3.8-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "سه فرض پرریسک عبارت‌اند از بازه بازگشت (rollback)، تضمین نوشتن دوگانه داده‌ها در حین تغییر مسیر و بدون‌تغییر ماندن قراردادهای سمت کلاینت. پیش از تغییر ترافیک، هر یک را با یک تمرین آزمایشی راستی‌آزمایی کنید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 46,
    "prompt_tokens": 24,
    "total_tokens": 70,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 24,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000258200",
    "irt": 2.96,
    "exchange_rate": 114600
  }
}
```

---

## نمونه‌های استفاده با SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-27b",
    "messages": [
      {
        "role": "user",
        "content": "یک بازسازی مرحله‌ای برای این سرویس با تست و معیارهای بازگشت برنامه‌ریزی کن."
      }
    ],
    "extra_body": {
      "enable_thinking": true
    }
  }'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-27b",
    messages=[
        {
            "role": "user",
            "content": "یک بازسازی مرحله‌ای برای این سرویس با تست و معیارهای بازگشت برنامه‌ریزی کن.",
        }
    ],
    stream=True,
    extra_body={"enable_thinking": True, "reasoning_effort": "medium"},
)

for chunk in response:
    if chunk.choices:
        print(chunk.choices[0].delta.content or "", end="")

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3.8-27b",
  messages: [
    {
      role: "user",
      content: "یک بازسازی مرحله‌ای برای این سرویس با تست و معیارهای بازگشت برنامه‌ریزی کن.",
    },
  ],
  stream: true,
});

for await (const chunk of response) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}

```

---

## راهنمای پذیرش

- از شناسه‌های دقیق مدل یعنی `qwen3.8-flash` و `qwen3.8-27b` استفاده کنید.
- `qwen3.8-flash` نام مستعار تولیدی و مدیریت‌شده `qwen3.8-flash-next` است؛ در ارائه‌دهنده اصلی ابزارهای رسمی داخلی و پیکربندی پیش‌فرض مناسب محیط تولید دارد.
- تفکر به‌صورت پیش‌فرض فعال است. برای دریافت پاسخ مستقیم در درخواست‌های غیرجریانی `extra_body={"enable_thinking": false}` را بفرستید و برای دریافت خروجی استدلالی، `enable_thinking: true` را همراه `stream: true` نگه دارید.
- عمق استدلال را با `reasoning_effort` (`low`، `medium` یا `xhigh`) تنظیم کنید و در صورت پشتیبانی route، زمینه استدلال چندنوبتی را با `preserve_thinking` حفظ کنید.
- پیش از استفاده از نقطه پایانی `v1/responses` که پشتیبانی جزئی دارد، از پشتیبانی همه پارامترها، ابزارها و نوع‌های ورودی موردنیاز مطمئن شوید.

---

## پیوندهای مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مرجع API Chat Completions](fa/api-reference/chat.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [قیمت‌گذاری](fa/pricing.md)
