# افزودن مدل‌های پرچم‌دار جدید: DeepSeek-V4-Flash و DeepSeek-V4-Pro

**تاریخ:** 1405-02-04 / (2026-04-24)

## خلاصه

ما افزودن مدل‌های پرچم‌دار جدید DeepSeek با نام‌های `deepseek-v4-flash` و `deepseek-v4-pro` را روی نقطه پایانی `v1/chat/completions` اعلام می‌کنیم. DeepSeek V4 پنجره زمینه ۱ میلیون توکن را به صورت پیش‌فرض ارائه می‌دهد، از ساختار جدید توجه مبتنی بر فشرده‌سازی توکنی و DeepSeek Sparse Attention (DSA) بهره می‌برد و هر دو حالت تفکری و غیر تفکری را پشتیبانی می‌کند. نام‌های قدیمی `deepseek-chat` و `deepseek-reasoner` اکنون به خانواده V4 هدایت می‌شوند و در تاریخ ۲۴ ژوئیه ۲۰۲۶ منسوخ خواهند شد.

---

## جزئیات

### DeepSeek

#### DeepSeek-V4-Flash

ما **DeepSeek-V4-Flash** (`deepseek-v4-flash`) را معرفی می‌کنیم؛ یک مدل پرچم‌دار سریع، کارآمد و مقرون‌به‌صرفه با ۲۸۴ میلیارد پارامتر کل / ۱۳ میلیارد پارامتر فعال. قابلیت‌های استدلالی این مدل بسیار نزدیک به V4-Pro است و در وظایف عاملی ساده عملکردی هم‌تراز با V4-Pro دارد، در حالی که اندازه پارامتر کوچک‌تر، زمان پاسخ‌دهی سریع‌تر و قیمت‌گذاری به‌شدت اقتصادی ارائه می‌دهد. [مستندات](fa/providers/deepseek.md)

#### DeepSeek-V4-Pro

ما **DeepSeek-V4-Pro** (`deepseek-v4-pro`) را معرفی می‌کنیم؛ توانمندترین مدل پرچم‌دار DeepSeek با ۱٫۶ تریلیون پارامتر کل / ۴۹ میلیارد پارامتر فعال. بر اساس بنچمارک‌های DeepSeek، مدل V4-Pro در بنچمارک‌های کدنویسی عاملی (Agentic Coding) به SOTA متن‌باز دست یافته است، استدلال کلاس جهانی ارائه می‌دهد که با برترین مدل‌های بسته در ریاضیات/STEM/کدنویسی رقابت می‌کند و دانش جهانی غنی دارد که در میان مدل‌های متن‌باز فعلی فقط پس از Gemini-3.1-Pro قرار می‌گیرد. [مستندات](fa/providers/deepseek.md)

**ویژگی‌های کلیدی (هر دو مدل):**

- **پنجره زمینه**: ۱ میلیون توکن (به صورت پیش‌فرض در تمام سرویس‌های DeepSeek V4)
- **حداکثر توکن خروجی**: تا ۳۸۴ هزار توکن
- **حالت‌های دوگانه**: پشتیبانی از هر دو حالت تفکری (پیش‌فرض) و غیر تفکری — قابل تنظیم با `extra_body={"thinking": {"type": "enabled"/"disabled"}}`
- **کنترل تلاش تفکری**: `reasoning_effort: "high"/"max"` (مقادیر low/medium به high و xhigh به max نگاشت می‌شوند)
- **نوآوری ساختاری**: فشرده‌سازی توکنی + DeepSeek Sparse Attention (DSA) برای بیشینه کارایی در زمینه‌های طولانی
- **قابلیت‌های پیشرفته**: خروجی JSON، فراخوانی ابزار، تکمیل پیشوند چت (بتا)
- **تکمیل FIM (بتا)**: فقط در حالت غیر تفکری در دسترس است
- **یکپارچه‌سازی با عامل‌ها**: ادغام یکپارچه با عامل‌های پیشرو مانند Claude Code، OpenClaw و OpenCode
- **پشتیبانی نقطه پایانی**: در دسترس از طریق [`v1/chat/completions`](fa/api-reference/chat.md)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی (Cache Miss) | ورودی (Cache Hit) | خروجی |
|-------|--------------------|-------------------|--------|
| deepseek-v4-flash | $0.14 / 1M توکن | $0.028 / 1M توکن | $0.28 / 1M توکن |
| deepseek-v4-pro | $1.74 / 1M توکن | $0.145 / 1M توکن | $3.48 / 1M توکن |

#### مسیریابی مدل و نام‌های قدیمی

برای حفظ سازگاری با کد موجود، AvalAI اکنون نام‌های قدیمی را به مدل‌های پرچم‌دار جدید V4 هدایت می‌کند:

- **`deepseek-chat`** → هدایت به **`deepseek-v4-flash`** (حالت غیر تفکری)
- **`deepseek-reasoner`** → هدایت به **`deepseek-v4-pro`** (حالت تفکری)

**اثر قیمت‌گذاری بر نام‌های قدیمی:**

- قیمت‌گذاری **`deepseek-chat`** بدون تغییر است — برابر با `deepseek-v4-flash` (ورودی / ورودی کش‌شده / خروجی: $0.14 / $0.028 / $0.28 به ازای هر ۱ میلیون توکن).
- قیمت‌گذاری **`deepseek-reasoner`** برای هماهنگی با `deepseek-v4-pro` افزایش یافته است ($1.74 / $0.145 / $3.48 به ازای هر ۱ میلیون توکن برای ورودی / ورودی کش‌شده / خروجی) تا ارتقاء توانمندی مدل زیرین را بازتاب دهد.

#### ⚠️ اعلان منسوخ‌سازی

بر اساس اعلامیه رسمی DeepSeek، مدل‌های `deepseek-chat` و `deepseek-reasoner` پس از **۲۴ ژوئیه ۲۰۲۶، ساعت ۱۵:۵۹ (UTC)** به طور کامل بازنشسته شده و غیرقابل دسترس خواهند بود. از کاربران درخواست می‌شود به نام‌های صریح `deepseek-v4-flash` و `deepseek-v4-pro` مهاجرت کنند. برای جزئیات کامل به [صفحه منسوخ‌سازی‌ها](fa/deprecations.md) مراجعه کنید.

### نمونه درخواست/پاسخ API

#### نمونه درخواست — DeepSeek-V4-Flash (حالت غیر تفکری)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {
        "role": "user",
        "content": "مزایای کلیدی DeepSeek Sparse Attention (DSA) را در یک پاراگراف توضیح دهید."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-deepseek-v4-flash-xxxxx",
  "created": 1745481600,
  "model": "deepseek-v4-flash",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "DeepSeek Sparse Attention (DSA) با ترکیب فشرده‌سازی توکنی و الگوی توجه پراکنده، هزینه محاسباتی و حافظه را در سناریوهای زمینه طولانی به شدت کاهش می‌دهد. این ویژگی امکان ارائه زمینه پیش‌فرض ۱ میلیون توکنی در سرویس‌های DeepSeek را فراهم می‌کند و در عین حال استنتاج را سریع و اقتصادی نگه می‌دارد.",
        "role": "assistant",
        "reasoning_content": null,
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 58,
    "prompt_tokens": 22,
    "total_tokens": 80,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 22,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000193200",
    "irt": 2.21,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست — DeepSeek-V4-Pro (حالت تفکری)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4-pro",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری تحمل‌پذیر خطا برای یک پردازنده پرداخت جهانی با ۵۰٬۰۰۰ TPS طراحی کنید."
      }
    ],
    "reasoning_effort": "high"
  }'
```

#### نمونه پاسخ (حالت تفکری)

```json
{
  "id": "chatcmpl-deepseek-v4-pro-xxxxx",
  "created": 1745481700,
  "model": "deepseek-v4-pro",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "معماری تحمل‌پذیر خطا برای یک پردازنده پرداخت جهانی به شرح زیر است ...",
        "reasoning_content": "کاربر یک معماری تحمل‌پذیر خطا برای ۵۰ هزار TPS در سطح جهانی می‌خواهد. باید استقرار Active-Active منطقه‌ای، اجماع برای سازگاری دفتر کل، کلیدهای Idempotency، ارکستراسیون مبتنی بر Saga و بازیابی از فاجعه را پوشش دهم ...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1842,
    "prompt_tokens": 35,
    "total_tokens": 1877,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 35,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0064703100",
    "irt": 741.5,
    "exchange_rate": 114600
  }
}
```

### نمونه استفاده SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {
        "role": "user",
        "content": "مزایای پنجره زمینه ۱ میلیون توکنی برای تحلیل اسناد را خلاصه کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# حالت غیر تفکری (سریع و اقتصادی)
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "user",
            "content": "مزایای پنجره زمینه ۱ میلیون توکنی برای تحلیل اسناد را خلاصه کنید.",
        }
    ],
    extra_body={"thinking": {"type": "disabled"}},
)

print(response.choices[0].message.content)

# حالت تفکری (استدلال عمیق)
reasoning_response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {
            "role": "user",
            "content": "ثابت کنید مجموع n عدد فرد اول برابر n^2 است.",
        }
    ],
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

print(reasoning_response.choices[0].message.reasoning_content)
print(reasoning_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// حالت غیر تفکری (سریع و اقتصادی)
const response = await client.chat.completions.create({
  model: "deepseek-v4-flash",
  messages: [
    {
      role: "user",
      content: "مزایای پنجره زمینه ۱ میلیون توکنی برای تحلیل اسناد را خلاصه کنید.",
    },
  ],
});

console.log(response.choices[0].message.content);

// حالت تفکری (استدلال عمیق)
const reasoningResponse = await client.chat.completions.create({
  model: "deepseek-v4-pro",
  messages: [
    {
      role: "user",
      content: "ثابت کنید مجموع n عدد فرد اول برابر n^2 است.",
    },
  ],
  reasoning_effort: "high",
});

console.log(reasoningResponse.choices[0].message.reasoning_content);
console.log(reasoningResponse.choices[0].message.content);

```

### راهنمای مهاجرت

- **نیازی به اقدام برای یکپارچه‌سازی‌های موجود نیست**: فراخوانی‌های `deepseek-chat` و `deepseek-reasoner` تا تاریخ **۲۴ ژوئیه ۲۰۲۶** به کار خود ادامه می‌دهند و به صورت خودکار به خانواده V4 هدایت می‌شوند.
- **توصیه می‌شود**: شناسه‌های مدل خود را به `deepseek-v4-flash` یا `deepseek-v4-pro` به‌روزرسانی کنید تا از پنجره زمینه ۱ میلیون توکنی، کنترل صریح حالت از طریق پارامتر `thinking` بهره ببرید و از اختلال پس از بازنشستگی نام‌های قدیمی در امان بمانید.
- **آگاهی از قیمت‌گذاری**: اگر در حال حاضر از `deepseek-reasoner` استفاده می‌کنید، توجه داشته باشید که قیمت‌گذاری خروجی آن اکنون منعکس‌کننده `deepseek-v4-pro` است ($3.48 به ازای هر ۱ میلیون توکن خروجی) تا با مدل زیرین ارتقا یافته هماهنگ باشد.

---

## منابع مرتبط

- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [منسوخ‌سازی‌ها](fa/deprecations.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
