---
hasH1: true
published: 2026-08-15
author: تیم انتشار AvalAI
---

# مدل وزن‌باز Qwen3.8 و مدل‌های Qwen Image 3 اضافه شدند

**تاریخ:** ۱۴۰۵-۰۵-۲۴ / 2026-08-15

## خلاصه

سه مدل جدید Alibaba اکنون در AvalAI در دسترس‌اند: مدل وزن‌باز، فقط متن و دارای تفکر اجباری `qwen3.8-2.4t-a95b` و دو مدل تولید و ویرایش تصویر `qwen-image-3.0-pro` و `qwen-image-3.0`. مدل متنی از Chat Completions و Messages به‌طور کامل و از Responses به‌صورت جزئی پشتیبانی می‌کند. هر دو مدل تصویر از endpointهای تولید و ویرایش Images API پشتیبانی می‌کنند.

## جزئیات

### Alibaba

#### qwen3.8-2.4t-a95b

`qwen3.8-2.4t-a95b` مدل پایه وزن‌باز زیرساخت سرویس مدیریت‌شده `qwen3.8-max` است. معماری mixture-of-experts آن ۲٫۴ تریلیون پارامتر کل دارد و در هر forward pass تعداد ۹۵ میلیارد پارامتر را فعال می‌کند.

برخلاف `qwen3.8-max`، route وزن‌باز فقط متن است و همیشه در حالت thinking کار می‌کند. تفکر را نمی‌توان غیرفعال کرد. برای تنظیم بودجه reasoning از `reasoning_effort` با مقدارهای `low`، `medium` یا `xhigh` استفاده کنید؛ مقدار پیش‌فرض `xhigh` است.

| ویژگی | جزئیات |
| --- | --- |
| شناسه مدل | `qwen3.8-2.4t-a95b` |
| ورودی | فقط متن |
| خروجی | متن |
| پنجره زمینه | ۲۶۲٬۱۴۴ توکن |
| معماری | ۲٫۴ تریلیون پارامتر کل، ۹۵ میلیارد فعال |
| تفکر | اجباری |
| Endpointها | `v1/chat/completions` (کامل)، `v1/messages` (کامل)، `v1/responses` (جزئی) |

**قیمت‌گذاری:**

| نوع مصرف | قیمت برای ۱ میلیون توکن |
| --- | ---: |
| ورودی | $2.00 |
| ورودی ایجاد کش | $2.50 |
| ورودی کش‌شده | $0.25 |
| خروجی | $6.00 |

#### qwen-image-3.0-pro و qwen-image-3.0

هر دو مدل Qwen Image 3 از تولید تصویر جدید و ویرایش تصویر منبع از طریق Images API سازگار با OpenAI پشتیبانی می‌کنند.

| شناسه مدل | Endpoint تولید | Endpoint ویرایش |
| --- | --- | --- |
| `qwen-image-3.0-pro` | `v1/images/generations` | `v1/images/edits` |
| `qwen-image-3.0` | `v1/images/generations` | `v1/images/edits` |

قیمت هر دو مدل یکسان است:

| نوع مصرف | قیمت |
| --- | ---: |
| نرخ حسابداری خروجی | $40 / ۱ میلیون توکن خروجی |
| تصویر خروجی ۱K / حدود ۱ MP | $0.04 / تصویر |
| تصویر خروجی ۲ تا ۴ MP | $0.075 / تصویر |
| تصویر مرجع یا ورودی | $0.003 / تصویر |
| ورودی متن | $0 |
| ورودی متن کش‌شده | $0 |

## نمونه درخواست و پاسخ API

### Chat Completions

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-2.4t-a95b",
    "messages": [
      {
        "role": "user",
        "content": "پرریسک‌ترین فرض این برنامه مهاجرت را مشخص کن."
      }
    ],
    "reasoning_effort": "medium"
  }'
```

#### نمونه پاسخ

چون thinking اجباری است، متن مدل می‌تواند با یک بلوک reasoning درون `<think>...</think>` شروع شود.

```json
{
  "id": "chatcmpl_qwen38_example",
  "object": "chat.completion",
  "model": "qwen3.8-2.4t-a95b",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "<think>در حال بررسی وابستگی‌ها و فرض‌های rollback...</think>\n\nپرریسک‌ترین فرض این است که همه سرویس‌های وابسته می‌توانند در یک پنجره نگهداری مهاجرت کنند. سازگاری را سرویس‌به‌سرویس اعتبارسنجی و cutover برگشت‌پذیر تعریف کنید."
      },
      "finish_reason": "stop"
    }
  ]
}
```

### تولید تصویر

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-image-3.0-pro",
    "prompt": "یک تصویرسازی editorial تمیز از شهر انرژی‌های تجدیدپذیر با فضای خالی برای عنوان",
    "size": "1024x1024",
    "n": 1
  }'
```

#### نمونه پاسخ

```json
{
  "created": 1786795200,
  "data": [
    {
      "url": "https://example.invalid/generated/qwen-image-3-output.png",

      "revised_prompt": "یک تصویرسازی editorial تمیز از شهر انرژی‌های تجدیدپذیر با فضای مشخص برای عنوان"
    }
  ]
}
```

برای ویرایش، تصویر منبع و prompt را به `v1/images/edits` بفرستید. هر تصویر مرجع یا ورودی $0.003 به هزینه درخواست اضافه می‌کند.

## نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-2.4t-a95b",
    "messages": [{"role": "user", "content": "این برنامه استقرار را بررسی کن."}],
    "reasoning_effort": "medium"
  }'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-2.4t-a95b",
    messages=[{"role": "user", "content": "این برنامه استقرار را بررسی کن."}],
    extra_body={"reasoning_effort": "medium"},
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3.8-2.4t-a95b",
  messages: [
    { role: "user", content: "این برنامه استقرار را بررسی کن." },
  ],
  reasoning_effort: "medium",
});

console.log(response.choices[0].message.content);

```

## نکات یکپارچه‌سازی

- تصویر یا ویدئو به `qwen3.8-2.4t-a95b` نفرستید؛ برای درک چندوجهی از `qwen3.8-max` استفاده کنید.
- تلاش نکنید thinking را در `qwen3.8-2.4t-a95b` غیرفعال کنید.
- به‌جای کنترل `enable_thinking` مدل مدیریت‌شده Max، از `reasoning_effort` استفاده کنید.
- پشتیبانی `v1/responses` مدل متنی را جزئی در نظر بگیرید و پیش از مهاجرت فیلدهای مورد نیاز را بررسی کنید.
- برای هر دو مدل Qwen Image 3 از مسیر جمع `v1/images/edits` استفاده کنید.
- در گردش‌کار ویرایش، هزینه $0.003 برای هر تصویر مرجع/ورودی را لحاظ کنید.

## پیوندهای مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [صفحه مدل Qwen3.8-2.4T-A95B](fa/models/qwen3.8-2.4t-a95b.md)
- [صفحه مدل Qwen Image 3.0 Pro](fa/models/qwen-image-3.0-pro.md)
- [صفحه مدل Qwen Image 3.0](fa/models/qwen-image-3.0.md)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [Images API](fa/api-reference/images.md)
- [راهنمای reasoning](fa/guides/reasoning.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [قیمت‌گذاری](fa/pricing.md)
