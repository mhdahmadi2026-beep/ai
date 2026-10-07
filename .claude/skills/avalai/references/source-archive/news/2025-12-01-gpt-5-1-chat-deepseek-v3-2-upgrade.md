# افزودن مدل جدید: GPT-5.1 Chat و ارتقاء DeepSeek-V3.2

**تاریخ:** 1404-09-10 / (2025-12-01)

## خلاصه

ما افزودن GPT-5.1 Chat، نسخه بهینه‌شده برای گفتگو از GPT-5.1 OpenAI، همراه با ارتقاء خودکار مدل‌های DeepSeek به پایه جدید DeepSeek-V3.2 را اعلام می‌کنیم. GPT-5.1 Chat با همان قیمت‌گذاری GPT-5.1 و قابلیت‌های محاوره‌ای بهینه ارائه می‌شود. بر اساس بنچمارک‌های DeepSeek، مدل DeepSeek-V3.2 در حالت غیر استدلالی عملکردی در سطح GPT-5 و در حالت استدلالی رقیب Gemini-3.0-Pro ارائه می‌دهد، بدون نیاز به هیچ اقدامی از سوی کاربران.

---

## جزئیات

### OpenAI

#### GPT-5.1 Chat

ما **GPT-5.1 Chat** (`gpt-5.1-chat`) را معرفی می‌کنیم، نسخه بهینه‌شده برای گفتگو از GPT-5.1 که برای برنامه‌های محاوره‌ای طراحی شده است. این مدل همان قابلیت‌های پیشرفته GPT-5.1 را با بهینه‌سازی بیشتر برای تجربه‌های گفتگوی تعاملی ارائه می‌دهد. [مستندات](fa/providers/openai.md)

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: ۴۰۰٬۰۰۰ توکن برای مدیریت مکالمات و اسناد گسترده
- **حداکثر توکن خروجی**: ۱۲۸٬۰۰۰ توکن برای پاسخ‌های جامع
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته، پشتیبانی از توکن‌های استدلال، بینایی (ورودی تصویر)
- **بهینه‌سازی گفتگو**: بهبود یافته برای جریان‌های محاوره‌ای و برنامه‌های تعاملی
- **تاریخ دانش**: ۳۱ می ۲۰۲۴
- **پشتیبانی نقاط پایانی**: در دسترس در [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/responses`](fa/api-reference/responses.md)
- **پشتیبانی ابزار**: جستجوی وب، جستجوی فایل، تولید تصویر، مفسر کد و MCP

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5.1-chat | $1.25/1M توکن | $0.125/1M توکن | $10.00/1M توکن |

**نمونه استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1-chat",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت‌های کلیدی بین معماری میکروسرویس و یکپارچه را توضیح دهید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5.1-chat",
    messages=[
        {
            "role": "user",
            "content": "تفاوت‌های کلیدی بین معماری میکروسرویس و یکپارچه را توضیح دهید.",
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
  model: "gpt-5.1-chat",
  messages: [
    {
      role: "user",
      content: "تفاوت‌های کلیدی بین معماری میکروسرویس و یکپارچه را توضیح دهید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### DeepSeek

#### ارتقاء خودکار به DeepSeek-V3.2

مدل‌های DeepSeek به طور خودکار به پایه جدید **DeepSeek-V3.2** ارتقا یافته‌اند. بر اساس بنچمارک‌های رسمی DeepSeek، این یک نقطه عطف مهم در قابلیت‌های هوش مصنوعی استدلالی است. این ارتقا در سطح ارائه‌دهنده انجام می‌شود و نیازی به هیچ اقدامی از سوی کاربران نیست.

**ویژگی‌های جدید (بر اساس ادعاهای DeepSeek):**

- **DeepSeek-V3.2** (`deepseek-chat`): استنتاج متعادل در برابر طول - مدل روزانه شما با عملکرد سطح GPT-5
- **DeepSeek-V3.2-Speciale** (`deepseek-reasoner`): قابلیت‌های استدلال حداکثری که رقیب Gemini-3.0-Pro است
- **تفکر در استفاده از ابزار**: اولین مدل DeepSeek که تفکر را مستقیما در استفاده از ابزار یکپارچه می‌کند، با پشتیبانی از استفاده از ابزار در هر دو حالت تفکری و غیر تفکری
- **قابلیت‌های عامل**: سنتز داده‌های آموزش عامل گسترده شامل ۱۸۰۰+ محیط و ۸۵ هزار+ دستورالعمل پیچیده
- **عملکرد مدال طلا**: DeepSeek-V3.2-Speciale نتایج سطح طلا در IMO، CMO، فینال جهانی ICPC و IOI 2025 کسب کرده است

#### ⚠️ مهم: تغییرات API حالت تفکری (به‌روزرسانی دسامبر ۲۰۲۵)

DeepSeek API خود را برای حالت تفکری (`deepseek-reasoner`) به‌روزرسانی کرده است. هنگام استفاده از فراخوانی ابزار با حالت تفکری، **باید اکنون فیلد `reasoning_content` را** به API در درخواست‌های بعدی برگردانید.

**تغییرات کلیدی:**

1. **فیلدهای پاسخ**: API اکنون هم `reasoning_content` (استدلال CoT) و هم `content` (پاسخ نهایی) را برمی‌گرداند
2. **مکالمات چند نوبتی**: فقط `content` از نوبت‌های قبلی را ارسال کنید، نه `reasoning_content`
3. **فراخوانی ابزار با حالت تفکری**: **باید** `reasoning_content` را در پیام‌های دستیار هنگام پردازش فراخوانی‌های ابزار در همان نوبت درج کنید

**خطا در صورت عدم پیاده‌سازی:**

```
Missing reasoning_content field in the assistant message
```

**مثال رفع سریع:**

```python
# هنگام دریافت tool_calls از deepseek-reasoner:
assistant_message = {
    "role": "assistant",
    "content": message.content or "",
    "tool_calls": [...],
    # بحرانی: reasoning_content را درج کنید
    "reasoning_content": message.reasoning_content,
}
messages.append(assistant_message)
```

برای مستندات کامل و مثال‌ها به زبان‌های مختلف، به [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md#جزئیات-api-حالت-تفکری) مراجعه کنید.

**مرجع رسمی:** [DeepSeek Thinking Mode - Tool Calls](https://api-docs.deepseek.com/guides/thinking_mode#tool-calls)

**مسیریابی مدل:**

فراخوانی‌های API موجود شما بدون تغییر باقی می‌ماند:
- `deepseek-chat` → به حالت غیر تفکری DeepSeek-V3.2 هدایت می‌شود (سطح GPT-5 بر اساس بنچمارک‌های DeepSeek)
- `deepseek-reasoner` → به حالت تفکری DeepSeek-V3.2 هدایت می‌شود (رقیب Gemini-3.0-Pro بر اساس بنچمارک‌های DeepSeek)

**نیازی به اقدام نیست** - یکپارچه‌سازی‌های موجود شما به طور خودکار از مدل ارتقا یافته بهره‌مند خواهند شد.

**قیمت‌گذاری (بدون تغییر):**

| مدل | ورودی (Cache Hit) | ورودی (Cache Miss) | خروجی |
|-------|-------------------|-------------------|--------|
| deepseek-chat | $0.028/1M توکن | $0.28/1M توکن | $0.42/1M توکن |
| deepseek-reasoner | $0.028/1M توکن | $0.28/1M توکن | $0.42/1M توکن |

**جزئیات مدل:**

| ویژگی | deepseek-chat | deepseek-reasoner |
|---------|---------------|-------------------|
| نسخه مدل | DeepSeek-V3.2 (حالت غیر تفکری) | DeepSeek-V3.2 (حالت تفکری) |
| طول زمینه | 128K | 128K |
| حداکثر خروجی (پیش‌فرض) | 4K (حداکثر: 8K) | 32K (حداکثر: 64K) |
| خروجی JSON | ✓ | ✓ |
| فراخوانی ابزار | ✓ | ✓ |
| تکمیل پیشوند چت (بتا) | ✓ | ✓ |
| تکمیل FIM (بتا) | ✓ | ✗ |

**نمونه استفاده:**

```language-selector
bash=:# حالت چت استاندارد (عملکرد سطح GPT-5)
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."
      }
    ]
  }'

# حالت استدلال (عملکرد سطح Gemini-3.0-Pro)
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# حالت چت استاندارد (عملکرد سطح GPT-5)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."}
    ],
)

print(response.choices[0].message.content)

# حالت استدلال (عملکرد سطح Gemini-3.0-Pro)
reasoning_response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کنید.",
        }
    ],
)

print(reasoning_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// حالت چت استاندارد (عملکرد سطح GPT-5)
const response = await client.chat.completions.create({
    model: "deepseek-chat",
    messages: [
        {
            role: "user",
            content: "محاسبات کوانتومی را به زبان ساده توضیح دهید."
        }
    ]
});

console.log(response.choices[0].message.content);

// حالت استدلال (عملکرد سطح Gemini-3.0-Pro)
const reasoningResponse = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: [
        {
            role: "user",
            content: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کنید."
        }
    ]
});

console.log(reasoningResponse.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)