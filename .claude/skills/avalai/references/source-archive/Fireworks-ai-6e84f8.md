# Fireworks.ai

Fireworks.ai زیرساخت استنتاج production برای مدل‌های open-weight فراهم می‌کند. AvalAI مدل‌های منتخب میزبانی‌شده روی Fireworks.ai را از طریق routeهای سازگار ارائه می‌دهد؛ مالک و توسعه‌دهنده مدل همچنان شرکت اصلی مانند Meta یا NVIDIA است.

## مدل‌های موجود

- [`muse-glimmer-30b`](#muse-glimmer-30b) — مدل چندوجهی و عاملی ۳۰B از Meta
- [`nemotron-3.5-lightning`](#nemotron-35-lightning) — مدل استدلالی کارآمد ۳۰B با ۳B پارامتر فعال از NVIDIA
- [`nemotron-3-ultra`](#nemotron-3-ultra) — مدل بزرگ‌مقیاس NVIDIA برای استدلال و workflowهای عاملی

## پشتیبانی نقطه پایانی API

| مدل | `v1/chat/completions` | `v1/messages` | `v1/responses` |
| --- | --- | --- | --- |
| `muse-glimmer-30b` | ✅ کامل | ✅ کامل | ⚠️ جزئی |
| `nemotron-3.5-lightning` | ✅ کامل | ✅ کامل | ⚠️ جزئی |
| `nemotron-3-ultra` | ✅ کامل | ✅ کامل | ⚠️ جزئی |

پشتیبانی جزئی Responses یعنی ممکن است برخی فیلدهای اختصاصی Responses یا قابلیت‌های stateful در دسترس نباشند. شکل دقیق درخواست را پیش از rollout در production آزمایش کنید.

## ویژگی‌های کلیدی

- دسترسی سازگار با OpenAI به Chat Completions
- دسترسی سازگار با Anthropic به Messages
- فراخوانی تابع و workflowهای عاملی
- کش ضمنی سمت provider برای درخواست‌های واجد شرایط
- قیمت ورودی کش‌شده برای prefixهای تکراری

## muse-glimmer-30b

Muse Glimmer توسط Meta Superintelligence Lab توسعه یافته و روی Fireworks.ai میزبانی می‌شود. این مدل dense با حدود ۳۰ میلیارد پارامتر و encoder ادراکی، درک متن و تصویر، تولید چندزبانه، استفاده از ابزار، استدلال چندمرحله‌ای، بازیابی از شکست و زمینه حداقل ۱۳۱٬۰۷۲ توکن را ترکیب می‌کند.

### ویژگی‌ها

- ورودی متن و تصویر و خروجی متن
- پشتیبانی از بیش از ۱۰۰ زبان
- تکمیل وظایف عاملی، کدنویسی و استفاده از ابزار
- سطوح reasoning قابل تنظیم: `low`، `medium`، `high` و `xhigh`
- sampling پیشنهادی upstream: `temperature: 1.0`، `top_p: 0.95` و `top_k: 64`

### قیمت‌گذاری

| نوع | هزینه هر ۱ میلیون توکن |
| --- | ---: |
| ورودی | $0.35 |
| ورودی کش‌شده | $0.04 |
| خروجی | $1.50 |

### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
| --- | --- |
| `v1/chat/completions` | ✅ کامل |
| `v1/messages` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

### مثال

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "muse-glimmer-30b",
    "messages": [{"role": "user", "content": "یک workflow پژوهشی مطمئن با استفاده از ابزار طراحی کن."}]
  }'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
response = client.chat.completions.create(
    model="muse-glimmer-30b",
    messages=[
        {
            "role": "user",
            "content": "یک workflow پژوهشی مطمئن با استفاده از ابزار طراحی کن.",
        }
    ],
)
print(response.choices[0].message.content)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const response = await client.chat.completions.create({
  model: "muse-glimmer-30b",
  messages: [{ role: "user", content: "یک workflow پژوهشی مطمئن با استفاده از ابزار طراحی کن." }],
});
console.log(response.choices[0].message.content);

```


## nemotron-3.5-lightning

Nemotron 3.5 Lightning توسط NVIDIA توسعه یافته و روی Fireworks.ai میزبانی می‌شود. این مدل hybrid Mixture-of-Experts دارای ۳۰ میلیارد پارامتر کل و ۳ میلیارد پارامتر فعال است و لایه‌های Mamba-2، MoE و attention را برای استدلال عاملی، کدنویسی، RAG، خروجی ساختاریافته و استفاده از ابزار ترکیب می‌کند. زمینه ثبت‌شده این route در AvalAI برابر ۲۶۲٬۱۴۴ توکن است.

### ویژگی‌ها

- معماری hybrid MoE با ۳۰B پارامتر کل و ۳B پارامتر فعال
- مناسب reasoning، کدنویسی، RAG و عامل‌های خودمختار
- فراخوانی ابزار و خروجی ساختاریافته
- امکان فعال یا غیرفعال کردن thinking در پیاده‌سازی upstream
- sampling پیشنهادی upstream: `temperature: 1.0` و `top_p: 0.95`

### قیمت‌گذاری

| نوع | هزینه هر ۱ میلیون توکن |
| --- | ---: |
| ورودی | $0.05 |
| ورودی کش‌شده | $0.01 |
| خروجی | $0.20 |

### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
| --- | --- |
| `v1/chat/completions` | ✅ کامل |
| `v1/messages` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

### مثال

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "nemotron-3.5-lightning",
    "messages": [{"role": "user", "content": "این برنامه deployment را بررسی کن و سه ریسک اصلی را فهرست کن."}]
  }'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
response = client.chat.completions.create(
    model="nemotron-3.5-lightning",
    messages=[
        {
            "role": "user",
            "content": "این برنامه deployment را بررسی کن و سه ریسک اصلی را فهرست کن.",
        }
    ],
)
print(response.choices[0].message.content)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const response = await client.chat.completions.create({
  model: "nemotron-3.5-lightning",
  messages: [{ role: "user", content: "این برنامه deployment را بررسی کن و سه ریسک اصلی را فهرست کن." }],
});
console.log(response.choices[0].message.content);

```


## nemotron-3-ultra

مدل بزرگ‌مقیاس Nemotron از NVIDIA روی Fireworks.ai برای استدلال پیچیده، تولید باکیفیت و workflowهای چندمرحله‌ای ابزار میزبانی می‌شود.

### قیمت‌گذاری

| نوع | هزینه هر ۱ میلیون توکن |
| --- | ---: |
| ورودی | $0.60 |
| ورودی کش‌شده | $0.12 |
| خروجی | $2.40 |

### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
| --- | --- |
| `v1/chat/completions` | ✅ کامل |
| `v1/messages` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

## منابع مرتبط

- [قیمت‌گذاری](fa/pricing.md)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [Messages API](fa/api-reference/messages.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [کش کردن پرامپت](fa/guides/prompt-caching.md)
