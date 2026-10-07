# راه‌اندازی سطح سرویس Flex: ۵۰٪ کاهش قیمت برای مدل‌های منتخب OpenAI

**تاریخ:** ۱۴۰۴-۰۹-۲۴ / (2025-12-15)

## خلاصه

AvalAI سطح سرویس Flex را معرفی می‌کند که ۵۰٪ کاهش قیمت برای مدل‌های منتخب OpenAI ارائه می‌دهد. این سطح قیمت‌گذاری جدید صرفه‌جویی قابل توجهی در هزینه برای پردازش دسته‌ای، کارهای غیرحساس به زمان و استفاده حجم بالا از API در ازای تاخیر بالاتر فراهم می‌کند.

---

## جزئیات

### سطح سرویس Flex چیست؟

سطح سرویس Flex یک گزینه قیمت‌گذاری جدید است که **۵۰٪ کاهش هزینه** نسبت به سطح استاندارد برای مدل‌های منتخب OpenAI ارائه می‌دهد. این سطح برای کارهایی طراحی شده است که صرفه‌جویی در هزینه مهم‌تر از تاخیر پاسخ است.

### ویژگی‌های کلیدی

- **۵۰٪ کاهش هزینه**: نصف نرخ استاندارد را برای مدل‌های پشتیبانی شده بپردازید
- **پارامتر انتخابی**: به سادگی `"service_tier": "flex"` را به درخواست‌های API خود اضافه کنید
- **پیگیری پاسخ**: همه پاسخ‌های API شامل فیلد `service_tier` هستند که نشان می‌دهد کدام سطح استفاده شده است
- **یکپارچگی بدون مشکل**: با SDKهای موجود سازگار با OpenAI کار می‌کند

### مدل‌های پشتیبانی شده

سطح سرویس Flex برای مدل‌های OpenAI زیر در دسترس است:

| مدل | نام‌های مستعار مدل |
| :-- | :---------------- |
| `gpt-5.2` | `gpt-5.2-2025-12-11` |
| `gpt-5.1` | `gpt-5.1-2025-11-13` |
| `gpt-5` | `gpt-5-2025-08-07` |
| `gpt-5-mini` | `gpt-5-mini-2025-08-07` |
| `gpt-5-nano` | `gpt-5-nano-2025-08-07` |
| `o3` | - |
| `o4-mini` | - |

### قیمت‌گذاری سطح Flex

قیمت‌ها بر اساس ۱ میلیون توکن و نشان‌دهنده **۵۰٪ صرفه‌جویی** در مقایسه با قیمت‌گذاری سطح استاندارد هستند.

| مدل | ورودی | ورودی کش شده | خروجی |
| :-- | :---- | :---------- | :---- |
| `gpt-5.2` | $0.875 | $0.0875 | $7.00 |
| `gpt-5.1` | $0.625 | $0.0625 | $5.00 |
| `gpt-5` | $0.625 | $0.0625 | $5.00 |
| `gpt-5-mini` | $0.125 | $0.0125 | $1.00 |
| `gpt-5-nano` | $0.025 | $0.0025 | $0.20 |
| `o3` | $1.00 | $0.25 | $4.00 |
| `o4-mini` | $0.55 | $0.138 | $2.20 |

### ملاحظات مهم

> **⚠️ تاخیر و قابلیت اطمینان**
>
> سطح Flex دارای **تاخیر بالاتر** نسبت به سطح استاندارد است:
> - درخواست‌ها ممکن است زمان بیشتری برای پردازش ببرند
> - تایم‌اوت سرور می‌تواند تا **۹۰۰ ثانیه (۱۵ دقیقه)** باشد
> - درخواست‌ها ممکن است در حین پردازش تایم‌اوت شوند یا با شکست مواجه شوند
> - **توصیه می‌شود برای**: پردازش دسته‌ای، کارهای غیرحساس به زمان، کارهای پس‌زمینه
> - **توصیه نمی‌شود برای**: برنامه‌های تعاملی، دستیاران بلادرنگ، رابط‌های کاربری

> **⚠️ محدودیت بسته اعتباری**
>
> بسته‌های اعتباری هزینه‌های سطح Flex را پوشش **نمی‌دهند**. هنگام استفاده از `service_tier: "flex"`، هزینه‌ها از موجودی استاندارد حساب شما کسر می‌شود، نه از تخصیص بسته‌های اعتباری.

---

## مثال‌های درخواست/پاسخ API

### درخواست نمونه

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-mini",
    "messages": [
      {
        "role": "user",
        "content": "نکات کلیدی یادگیری ماشین را خلاصه کن."
      }
    ],
    "service_tier": "flex"
  }'
```

### پاسخ نمونه

```json
{
  "id": "chatcmpl-123",
  "created": 1765789075,
  "model": "gpt-5-mini-2025-08-07",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است که به سیستم‌ها امکان می‌دهد از تجربه یاد بگیرند و بهبود یابند بدون اینکه صریحا برنامه‌نویسی شوند. نکات کلیدی عبارتند از:\n\n۱. **یادگیری نظارت شده**: آموزش با داده‌های برچسب‌گذاری شده\n۲. **یادگیری بدون نظارت**: یافتن الگوها در داده‌های بدون برچسب\n۳. **یادگیری تقویتی**: یادگیری از طریق آزمون و خطا\n۴. **یادگیری عمیق**: شبکه‌های عصبی با لایه‌های متعدد\n۵. **کاربردها**: تشخیص تصویر، NLP، سیستم‌های توصیه‌گر",
        "role": "assistant",
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 150,
    "prompt_tokens": 20,
    "total_tokens": 170,
    "completion_tokens_details": {
      "accepted_prediction_tokens": 0,
      "audio_tokens": 0,
      "reasoning_tokens": 0,
      "rejected_prediction_tokens": 0
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "cached_tokens": 0
    }
  },
  "service_tier": "flex",
  "estimated_cost": {
    "unit": "0.0001525000",
    "irt": 20.03,
    "exchange_rate": 131350
  }
}
```

### خطای مدل پشتیبانی نشده

اگر تلاش کنید از سطح Flex با یک مدل پشتیبانی نشده استفاده کنید:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "سلام"}],
    "service_tier": "flex"
  }'
```

**پاسخ خطا:**

```json
{
  "error": {
    "message": "Model 'gpt-4o-mini' does not support service_tier='flex'. Flex tier is only available for: gpt-5, gpt-5-2025-08-07, gpt-5-mini, gpt-5-mini-2025-08-07, gpt-5-nano, gpt-5-nano-2025-08-07, gpt-5.1, gpt-5.1-2025-11-13, gpt-5.2, gpt-5.2-2025-12-11, o3, o4-mini. checkout https://docs.avalai.ir/fa/service-tiers for more information.",

    "type": "invalid_request",
    "param": null,
    "code": "invalid_request",
    "request_id": "019b214f-4f5d-7321-8a3a-59f89d473c7c"
  }
}
```

---

## مثال‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-mini",
    "messages": [
      {
        "role": "user",
        "content": "نکات کلیدی یادگیری ماشین را خلاصه کن."
      }
    ],
    "service_tier": "flex"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از سطح flex برای صرفه‌جویی در هزینه کارهای غیرحساس به زمان
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[
        {
            "role": "user",
            "content": "نکات کلیدی یادگیری ماشین را خلاصه کن.",
        }
    ],
    service_tier="flex",
)

print(response.choices[0].message.content)
print(f"سطح سرویس استفاده شده: {response.service_tier}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از سطح flex برای صرفه‌جویی در هزینه کارهای غیرحساس به زمان
const response = await client.chat.completions.create({
  model: "gpt-5-mini",
  messages: [
    {
      role: "user",
      content: "نکات کلیدی یادگیری ماشین را خلاصه کن.",
    },
  ],
  service_tier: "flex"
});

console.log(response.choices[0].message.content);
console.log(`سطح سرویس استفاده شده: ${response.service_tier}`);

```

---

## بهترین شیوه‌ها

### چه زمانی از سطح Flex استفاده کنیم

- **پردازش دسته‌ای**: پردازش مقادیر زیاد داده که زمان حیاتی نیست
- **کارهای پس‌زمینه**: کارهای زمان‌بندی شده، تحلیل داده، تولید محتوا
- **بهینه‌سازی هزینه**: زمانی که کاهش هزینه اولویت است و می‌توانید تاخیرها را تحمل کنید
- **بارهای کاری غیرپروداکشن**: تست، توسعه، آزمایش

### چه زمانی از سطح default استفاده کنیم

- **برنامه‌های تعاملی**: چت‌بات‌ها، دستیاران بلادرنگ، رابط‌های کاربری
- **کارهای حساس به زمان**: زمانی که پاسخ‌های سریع مورد نیاز است
- **جریان‌های کاری پروداکشن**: جایی که قابلیت اطمینان حیاتی است
- **استفاده از بسته اعتباری**: زمانی که می‌خواهید هزینه‌ها توسط بسته‌های اعتباری پوشش داده شوند

### پیاده‌سازی منطق تلاش مجدد

برای برنامه‌های پروداکشن که از سطح Flex استفاده می‌کنند، منطق تلاش مجدد با بازگشت به سطح استاندارد پیاده‌سازی کنید:

```python
def make_request_with_fallback(messages, model="gpt-5-mini"):
    # ابتدا سطح flex را برای صرفه‌جویی در هزینه امتحان کنید
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            service_tier="flex",
            timeout=900,  # تایم‌اوت ۱۵ دقیقه‌ای
        )
        return response, "flex"
    except Exception as e:
        print(f"سطح flex ناموفق: {e}. بازگشت به استاندارد...")

    # بازگشت به سطح استاندارد
    response = client.chat.completions.create(
        model=model, messages=messages, service_tier="default"
    )
    return response, "default"
```

---

## لینک‌های مرتبط

- [مستندات سطوح سرویس](fa/service-tiers.md) - راهنمای جامع سطوح سرویس
- [قیمت‌گذاری](fa/pricing.md#سطح-سرویس-flex) - اطلاعات کامل قیمت‌گذاری
- [بسته‌های اعتباری](fa/credit-packages.md) - محدودیت‌های بسته اعتباری با سطح Flex
- [API تکمیل گفتگو](fa/api-reference/chat.md) - مرجع API با پارامتر service_tier
- [API پاسخ‌ها](fa/api-reference/responses.md) - Responses API با پارامتر service_tier
