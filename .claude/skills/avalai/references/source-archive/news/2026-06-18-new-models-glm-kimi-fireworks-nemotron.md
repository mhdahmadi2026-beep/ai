# مدل‌های جدید اضافه شدند: GLM-5.2، Kimi K2.7 Code و ارائه‌دهنده جدید Fireworks.ai با Nemotron-3-Ultra

**Date:** 1405-03-28 / (2026-06-18)

## خلاصه

افزودن چهار مدل جدید از سه ارائه‌دهنده، از جمله یک ارائه‌دهنده جدید با نام Fireworks.ai را اعلام می‌کنیم. مدل `glm-5.2` از Z.AI نسخه GLM-5.1 را با پنجره زمینه ۱ میلیون توکنی گسترش می‌دهد، مدل‌های `kimi-k2.7-code` و `kimi-k2.7-code-highspeed` از Moonshot.ai کدنویسی متن‌باز SOTA ارائه می‌دهند و مدل `nemotron-3-ultra` از NVIDIA اکنون از طریق ارائه‌دهنده جدید Fireworks.ai در دسترس است. همه مدل‌ها روی `v1/chat/completions` در دسترس هستند و پشتیبانی جزئی روی `v1/responses` دارند.

---

## جزئیات

### Z.AI

#### GLM-5.2

[`glm-5.2`](fa/providers/zai.md#glm-52) جدیدترین مدل پرچمدار Z.AI برای مهندسی عاملی است که GLM-5.1 را با پنجره زمینه گسترش‌یافته ۱ میلیون توکنی و قابلیت اطمینان بهبودیافته در افق بلند توسعه می‌دهد. این مدل عملکرد کدنویسی پیشرو را با پنجره زمینه بزرگ مناسب برای کدبیس‌های چند فایلی و جلسات عاملی طولانی ترکیب می‌کند.

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `glm-5.2` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، تفکر عمیق |
| قیمت ورودی | $1.40 / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | $0.26 / ۱ میلیون توکن |
| قیمت خروجی | $4.40 / ۱ میلیون توکن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/responses` (جزئی) |

### Moonshot.ai

#### Kimi K2.7 Code

[`kimi-k2.7-code`](fa/providers/moonshotai.md#kimi-k27-code) جدیدترین مدل متن‌باز Moonshot AI است که به‌طور ویژه برای مهندسی نرم‌افزار و کدنویسی عاملی ساخته شده و نتایج پیشرو را در معیارهای کدنویسی و عاملی ارائه می‌دهد. این مدل از طریق ارائه‌دهنده API شرکت Fireworks.ai سرویس‌دهی می‌شود.

[`kimi-k2.7-code-highspeed`](fa/providers/moonshotai.md#kimi-k27-code-highspeed) یک نسخه سرویس‌دهی پرسرعت است که برای بارهای کاری کدنویسی با تأخیر پایین بهینه شده و همان قابلیت‌ها را حفظ می‌کند و در عین حال توان عملیاتی را در اولویت قرار می‌دهد.

| ویژگی | `kimi-k2.7-code` | `kimi-k2.7-code-highspeed` |
|---------|------------------|----------------------------|
| پنجره زمینه | ۲۶۲٬۱۴۴ توکن | ۲۶۲٬۱۴۴ توکن |
| قیمت ورودی | $0.95 / ۱ میلیون توکن | $1.90 / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | $0.19 / ۱ میلیون توکن | $0.38 / ۱ میلیون توکن |
| قیمت خروجی | $4.00 / ۱ میلیون توکن | $8.00 / ۱ میلیون توکن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/responses` (جزئی) | `v1/chat/completions` (کامل)، `v1/responses` (جزئی) |


### Fireworks.ai (ارائه‌دهنده جدید)

ما Fireworks.ai را به‌عنوان یک ارائه‌دهنده جدید در AvalAI معرفی می‌کنیم. Fireworks.ai یک پلتفرم استنتاج سریع برای مدل‌های هوش مصنوعی متن‌باز است که استنتاج آماده تولید با توان عملیاتی بالا و قیمت‌گذاری رقابتی ارائه می‌دهد. اولین مدل میزبانی‌شده از طریق Fireworks.ai مدل `nemotron-3-ultra` از NVIDIA است.

#### Nemotron-3-Ultra

[`nemotron-3-ultra`](fa/providers/fireworksai.md#nemotron-3-ultra) مدل پرچمدار بزرگ‌مقیاس Nemotron از NVIDIA برای استدلال پیچیده، گردش‌کارهای عاملی و تولید متن باکیفیت است که قابلیت‌های قدرتمند را با استنتاج مقرون‌به‌صرفه ترکیب می‌کند.

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `nemotron-3-ultra` |
| مالک | NVIDIA |
| ارائه‌دهنده API | Fireworks.ai |
| قیمت ورودی | $0.60 / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | $0.12 / ۱ میلیون توکن |
| قیمت خروجی | $2.40 / ۱ میلیون توکن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/responses` (جزئی) |

---

## خلاصه قیمت‌گذاری

| مدل | ارائه‌دهنده | ورودی ($/۱ میلیون توکن) | ورودی کش‌شده ($/۱ میلیون توکن) | خروجی ($/۱ میلیون توکن) |
|-------|----------|---------------------|----------------------------|----------------------|
| `glm-5.2` | Z.AI | $1.40 | $0.26 | $4.40 |
| `kimi-k2.7-code` | Moonshot.ai | $0.95 | $0.19 | $4.00 |
| `kimi-k2.7-code-highspeed` | Moonshot.ai | $1.90 | $0.38 | $8.00 |
| `nemotron-3-ultra` | Fireworks.ai | $0.60 | $0.12 | $2.40 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.2",
    "messages": [
      {
        "role": "user",
        "content": "این کدبیس چند فایلی بزرگ را برای افزودن یک لایه کش بازنویسی کن و برنامه مهاجرت را توضیح بده."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه پاسخ

```json
{
  "id": "chatcmpl-glm-5-2-abc123",
  "created": 1781827200,
  "model": "glm-5.2",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا برنامه مهاجرت و لایه کش بازنویسی‌شده آمده است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 412,
    "prompt_tokens": 36,
    "total_tokens": 448,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 36,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0018632000",
    "irt": 213.52,
    "exchange_rate": 114600
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
    "model": "kimi-k2.7-code",
    "messages": [
      {
        "role": "user",
        "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن."
      }
    ],
    "max_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {
            "role": "user",
            "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
        }
    ],
    max_tokens=8192,
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "kimi-k2.7-code",
  messages: [
    {
      role: "user",
      content: "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
    },
  ],
  max_tokens: 8192,
});

console.log(completion.choices[0].message.content);

```

---

## پیوندهای مرتبط

- [مدل‌های Z.AI](fa/providers/zai.md)
- [مدل‌های Moonshot.ai](fa/providers/moonshotai.md)
- [مدل‌های Fireworks.ai](fa/providers/fireworksai.md)
- [قیمت‌گذاری](fa/pricing.md)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
