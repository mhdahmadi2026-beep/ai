# News 2026-09-02-claude-fable-5-1-added: افزودن مدل پرچم‌دار جدید: Claude Fable 5.1
URL: `https://docs.avalai.ir/fa/news/2026-09-02-claude-fable-5-1-added`
**تاریخ:** ۱۴۰۵-۰۶-۱۱ / (2026-09-02)

# افزودن مدل پرچم‌دار جدید: Claude Fable 5.1

**تاریخ:** ۱۴۰۵-۰۶-۱۱ / (2026-09-02)

## خلاصه

Claude Fable 5.1، پرچم‌دار جدید Anthropic برای کدنویسی، کار دانشی و حل مسئله بلندمدت، اکنون با شناسه `claude-fable-5-1` در AvalAI در دسترس است. این مدل پنجره ورودی ۱ میلیون توکنی، حداکثر ۱۲۸٬۰۰۰ توکن خروجی، تفکر تطبیقی همیشه‌فعال و نرخ ۰.۲۵ دلار به ازای هر ۱ میلیون توکن ورودی کش‌شده را ارائه می‌دهد.

---

## جزئیات

### Anthropic

دسترسی به **Claude Fable 5.1** ([`claude-fable-5-1`](fa/models/claude-fable-5-1.md))، پرچم‌دار عمومی Anthropic برای مهندسی نرم‌افزار دشوار، پژوهش، کار دانشی، استفاده از کامپیوتر و گردش‌کارهای عاملی چندمرحله‌ای را اعلام می‌کنیم. بر اساس گزارش Anthropic، این مدل در کدنویسی عاملی، استدلال چندرشته‌ای، گردش‌کارهای تجاری و پژوهش علمی از Claude Fable 5 عملکرد بهتری دارد و در وظایف طولانی، خروجی خواناتری ارائه می‌دهد.

**ویژگی‌های کلیدی:**

- **کدنویسی پیشرفته و کار دانشی**: برای یافتن علت ریشه‌ای، کار با کدبیس‌های بزرگ و آماده‌سازی خروجی‌های کامل پژوهشی و حرفه‌ای طراحی شده است
- **عامل‌های بلندمدت**: برای گردش‌کارهای پایدار و ابزارمحوری مناسب است که به برنامه‌ریزی، بررسی نتیجه و اولویت‌بندی دوباره نیاز دارند
- **پژوهش علمی**: Anthropic از بهبود در پژوهش علمی عاملی، تحلیل محاسباتی و استدلال چندرشته‌ای خبر داده است
- **پنجره ورودی ۱M توکنی**: حداکثر ۱٬۰۰۰٬۰۰۰ توکن ورودی برای مخازن بزرگ، مجموعه‌های گسترده اسناد و گفت‌وگوهای طولانی
- **ظرفیت خروجی ۱۲۸K**: حداکثر ۱۲۸٬۰۰۰ توکن خروجی برای کد، تحلیل و خروجی‌های ساختاریافته حجیم
- **تفکر تطبیقی همیشه‌فعال**: از تلاش قابل تنظیم، از جمله `xhigh` و `max`، پشتیبانی می‌کند و استدلال را فعال نگه می‌دارد
- **قابلیت‌های چندوجهی و توسعه‌دهنده**: بینایی، ورودی PDF، استفاده از کامپیوتر، فراخوانی تابع، انتخاب ابزار، خروجی ساختاریافته بومی، response schema و کش پرامپت
- **هزینه کمتر خواندن از کش**: ورودی کش‌شده ۰.۲۵ دلار به ازای هر ۱ میلیون توکن هزینه دارد؛ ۷۵٪ کمتر از نرخ ۱.۰۰ دلاری Claude Fable 5
- **پشتیبانی نقاط پایانی**: پشتیبانی کامل در `v1/chat/completions` و `v1/messages` و پشتیبانی جزئی در `v1/responses`
- **سطح دسترسی حساب**: در دسترس حساب‌های سطح ۲ و بالاتر AvalAI

### دسترسی نقاط پایانی

| نقطه پایانی                                       | پشتیبانی | توضیحات                                                                         |
| ------------------------------------------------- | -------- | ------------------------------------------------------------------------------- |
| [`v1/chat/completions`](fa/api-reference/chat.md) | کامل     | چت سازگار با OpenAI، استدلال، بینایی، خروجی ساختاریافته و گردش‌کارهای ابزارمحور |
| [`v1/messages`](fa/api-reference/messages.md)     | کامل     | پیام‌های بومی سازگار با Anthropic، تفکر تطبیقی و استفاده از ابزار               |
| [`v1/responses`](fa/api-reference/responses.md)   | جزئی     | همه پارامترها و ابزارهای موردنیاز را پیش از استفاده در محیط تولید بررسی کنید    |

---

## قیمت‌گذاری

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند.

| مدل                | ورودی  | ورودی کش‌شده | ورودی ایجاد کش | خروجی  |
| ------------------ | ------ | ------------ | -------------- | ------ |
| `claude-fable-5-1` | $10.00 | $0.25        | $12.50         | $50.00 |

نرخ ورودی، ایجاد کش و خروجی با Claude Fable 5 یکسان است. نرخ ورودی کش‌شده از ۱.۰۰ دلار به ۰.۲۵ دلار به ازای هر ۱ میلیون توکن کاهش یافته است. Anthropic برآورد می‌کند که این تغییر می‌تواند هزینه بارهای کاری معمول با صورتحساب توکنی را حدود ۲۵٪ کاهش دهد و در کارهای عاملی با استفاده زیاد از کش، صرفه‌جویی بیشتری ایجاد کند؛ میزان واقعی صرفه‌جویی به استفاده دوباره از کش و ترکیب درخواست بستگی دارد.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-fable-5-1",
    "messages": [
      {
        "role": "user",
        "content": "خط زمانی این رخداد را بررسی کن، محتمل‌ترین علت ریشه‌ای را پیدا کن و برنامه‌ای برای راستی‌آزمایی آن پیشنهاد بده."
      }
    ]
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد. تعداد توکن‌ها و هزینه نمونه هستند و با هر درخواست تغییر می‌کنند.

```json
{
  "id": "chatcmpl-claude-fable-5-1-example",
  "created": 1788350400,
  "model": "claude-fable-5-1",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "قوی‌ترین فرضیه، وضعیت رقابتی میان تلاش دوباره مصرف‌کننده صف و پردازش‌گر پایان مهلت است. برای بررسی آن، شناسه‌های تکراری کار را با پایان اجاره زمانی تطبیق دهید، زمان‌بندی را زیر بار بازتولید کنید و مطمئن شوید افزودن محافظ idempotency نوشتن‌های تکراری را حذف می‌کند.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 70,
    "prompt_tokens": 25,
    "total_tokens": 95,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 25,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0037500000",
    "irt": 574.5,
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
    "model": "claude-fable-5-1",
    "messages": [
      {
        "role": "user",
        "content": "معماری این مخزن را تحلیل کن و یک برنامه نوسازی همراه با راستی‌آزمایی پیشنهاد بده."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="claude-fable-5-1",
    messages=[
        {
            "role": "user",
            "content": "معماری این مخزن را تحلیل کن و یک برنامه نوسازی همراه با راستی‌آزمایی پیشنهاد بده.",
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
  model: "claude-fable-5-1",
  messages: [
    {
      role: "user",
      content: "معماری این مخزن را تحلیل کن و یک برنامه نوسازی همراه با راستی‌آزمایی پیشنهاد بده.",
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
    "model": "claude-fable-5-1",
    "max_tokens": 2048,
    "messages": [
      {
        "role": "user",
        "content": "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و یک آزمون رگرسیون طراحی کن."
      }
    ]
  }'

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",
)

message = client.messages.create(
    model="claude-fable-5-1",
    max_tokens=2048,
    messages=[
        {
            "role": "user",
            "content": "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و یک آزمون رگرسیون طراحی کن.",
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
  model: "claude-fable-5-1",
  max_tokens: 2048,
  messages: [
    {
      role: "user",
      content: "علت ریشه‌ای این خطای هم‌زمانی متناوب را پیدا کن و یک آزمون رگرسیون طراحی کن.",
    },
  ],
});

console.log(message.content[0].text);

```

---

## تفکر تطبیقی و تلاش

تفکر در Claude Fable 5.1 همیشه فعال است و مدل از تفکر تطبیقی با تلاش قابل تنظیم پشتیبانی می‌کند. از `medium` یا `high` شروع کنید و فقط وقتی ارزیابی‌ها بهبود معنادار موفقیت وظیفه را نشان دادند، سطح را به `xhigh` یا `max` افزایش دهید. از مدل نخواهید chain-of-thought پنهان را آشکار کند؛ در عوض دلیل کوتاه، شواهد یا چک‌لیست راستی‌آزمایی بخواهید.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="claude-fable-5-1",
    messages=[
        {
            "role": "user",
            "content": "یک مهاجرت مرحله‌ای طراحی کن و راهبرد بازگشت آن را بررسی کن.",
        }
    ],
    extra_body={
        "thinking": {"type": "adaptive"},
        "output_config": {"effort": "high"},
    },
)

print(response.choices[0].message.content)
```

---

## بارهای کاری پیشنهادی

| بار کاری                | دلیل تناسب Claude Fable 5.1                                                               |
| ----------------------- | ----------------------------------------------------------------------------------------- |
| مهندسی نرم‌افزار پیچیده | تحلیل قوی علت ریشه‌ای، درک کدبیس، راستی‌آزمایی و استفاده از ابزار                         |
| عامل‌های طولانی‌مدت     | ادامه کار چندمرحله‌ای، تنظیم دوباره اولویت‌ها با تغییر شواهد و بررسی نتایج میانی          |
| کار دانشی               | انجام پژوهش، تحلیل سند، بررسی موشکافانه، استدلال عددی و آماده‌سازی خروجی ساختاریافته      |
| تحلیل علمی              | بر اساس گزارش Anthropic، پژوهش عاملی و استدلال چندرشته‌ای قوی‌تر از Claude Fable 5        |
| استفاده از کامپیوتر     | پشتیبانی از اسکرین‌شات، تصویر، PDF و گردش‌کارهای مرورگر یا دسکتاپ                         |
| گردش‌کارهای متکی بر کش  | نرخ ۰.۲۵ دلاری ورودی کش‌شده، هزینه زمینه تکراری را در cache hitهای واجد شرایط کاهش می‌دهد |

---

## لینک‌های مرتبط

- [جزئیات مدل Claude Fable 5.1](fa/models/claude-fable-5-1.md)
- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [قیمت‌گذاری](fa/pricing.md)
