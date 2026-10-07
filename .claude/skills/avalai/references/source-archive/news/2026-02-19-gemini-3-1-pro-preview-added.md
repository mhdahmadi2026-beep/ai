# مدل جدید اضافه شد: Gemini 3.1 Pro Preview

**تاریخ:** 1404-12-01 / (2026-02-19)

## خلاصه

ما اضافه شدن جدیدترین مدل پرچمدار گوگل را اعلام می‌کنیم: [`gemini-3.1-pro-preview`](fa/providers/google.md). Gemini 3.1 Pro نسل بعدی سری Gemini 3 است، یک مدل استدلال بسیار توانمند و بومی چندوجهی که به طور قابل توجهی از Gemini 3 Pro در معیارهای کلیدی پیشی می‌گیرد. این مدل دارای پنجره زمینه 1 میلیون توکنی است و در [`v1/chat/completions`](fa/api-reference/chat.md)، [`v1/messages`](fa/api-reference/messages.md)، پشتیبانی جزئی در [`v1/responses`](fa/api-reference/responses.md)، و [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) در دسترس است.

---

## جزئیات

### Google Gemini

#### Gemini 3.1 Pro Preview

پیشرفته‌ترین مدل گوگل از فوریه 2026، [`gemini-3.1-pro-preview`](fa/providers/google.md) نسل بعدی سری Gemini 3 است که بهبودهای قابل توجهی نسبت به Gemini 3 Pro نشان می‌دهد. این مدل بومی چندوجهی می‌تواند مجموعه داده‌های گسترده از منابع اطلاعاتی متعدد شامل متن، صدا، تصاویر، ویدیو و مخازن کد کامل را درک کند.

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 1 میلیون توکن برای مدیریت مکالمات و اسناد گسترده
- **توکن‌های خروجی**: 64 هزار توکن برای پاسخ‌های جامع
- **قابلیت‌های پیشرفته**: پشتیبانی بومی چندوجهی (متن، بینایی، صدا)، استدلال، فراخوانی تابع، خروجی‌های ساختاریافته
- **معماری**: مبتنی بر Gemini 3 Pro با قابلیت‌های استدلال بهبود یافته
- **تاریخ قطع دانش**: ژانویه 2025
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`، `v1/messages`، پشتیبانی جزئی در `v1/responses`، و [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md)

**نکات برجسته عملکرد در معیارها:**
- **آزمون آخر بشریت**: 44.4% (بدون ابزار) - بهترین در کلاس بدون ابزار
- **ARC-AGI-2**: 77.1% - بهبود قابل توجه نسبت به Gemini 3 Pro (31.1%)
- **GPQA Diamond**: 94.3% - بهترین در کلاس دانش علمی
- **Terminal-Bench 2.0**: 68.5% - بهترین عملکرد در کدنویسی عاملی ترمینال
- **LiveCodeBench Pro**: 2887 Elo - بهترین امتیاز کدنویسی رقابتی
- **BrowseComp**: 85.9% - عملکرد برتر جستجوی عاملی
- **MMMLU**: 92.6% - بهترین عملکرد پرسش و پاسخ چندزبانه

**بهترین برای:**
- عملکرد عاملی و گردش‌های کاری چند مرحله‌ای
- کدنویسی پیشرفته و توسعه الگوریتم
- درک طولانی زمینه و چندوجهی
- استدلال پیچیده و برنامه‌ریزی استراتژیک
- تحقیق و تحلیل علمی

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| gemini-3.1-pro-preview | 2.00 دلار/1 میلیون توکن | 0.825 دلار/1 میلیون توکن | 12.00 دلار/1 میلیون توکن | بالای 200K: ورودی 4.00 دلار، خروجی 18.00 دلار |

**قیمت‌گذاری صوتی:**
- ورودی صوتی: 7.00 دلار/1 میلیون توکن
- ورودی صوتی کش‌شده: 1.50 دلار/1 میلیون توکن
- خروجی صوتی: 7.00 دلار/1 میلیون توکن

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": "معماری فنی یک سیستم توزیع‌شده را تحلیل کنید و استراتژی‌های بهینه‌سازی برای مدیریت 10 برابر رشد ترافیک پیشنهاد دهید."
      }
    ],
    "max_tokens": 4096
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1740000000,
  "model": "gemini-3.1-pro-preview",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "اجازه دهید معماری سیستم توزیع‌شده شما را تحلیل کنم و استراتژی‌های بهینه‌سازی برای 10 برابر رشد ترافیک پیشنهاد کنم...\n\n## تحلیل معماری سیستم\n\n1. **ارزیابی وضعیت فعلی**\n   - شناسایی گلوگاه‌ها و نقاط شکست تکی...\n\n2. **استراتژی‌های مقیاس‌پذیری افقی**\n   - پیاده‌سازی طراحی سرویس بدون حالت...\n\n3. **بهینه‌سازی لایه داده**\n   - شاردینگ پایگاه داده و رپلیکاهای خواندن...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 850,
    "prompt_tokens": 32,
    "total_tokens": 882,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 32,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0102640000",
    "irt": 1177.63,
    "exchange_rate": 114700
  }
}
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3.1-pro-preview",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله پیچیده را گام به گام با استفاده از استدلال پیشرفته حل کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gemini-3.1-pro-preview",
    messages=[
        {
            "role": "user",
            "content": "این مسئله پیچیده را گام به گام با استفاده از استدلال پیشرفته حل کنید.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "gemini-3.1-pro-preview",
  messages: [
    {
      role: "user",
      content: "این مسئله پیچیده را گام به گام با استفاده از استدلال پیشرفته حل کنید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

## مستندات

برای اطلاعات بیشتر در مورد این مدل و قابلیت‌های آن، مراجعه کنید به:

- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [مرجع API Gemini (v1beta)](fa/api-reference/v1beta.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
