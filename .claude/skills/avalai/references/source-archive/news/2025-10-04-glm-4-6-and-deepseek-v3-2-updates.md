# مدل جدید اضافه شد: GLM-4.6 از Z.AI و ارتقاء DeepSeek-V3.2

**تاریخ:** 1404-07-12 / (2025-10-04)

## خلاصه

ما اضافه شدن GLM-4.6، یک مدل هوش مصنوعی پیشرفته از Z.AI که برای کدنویسی و وظایف با زمینه طولانی بهینه‌سازی شده است، را به همراه ارتقاء خودکار مدل‌های DeepSeek به پایه جدید DeepSeek-V3.2-Exp با کاهش بیش از 50٪ قیمت اعلام می‌کنیم. GLM-4.6 عملکرد برتر کدنویسی با پنجره زمینه 200K توکن ارائه می‌دهد، در حالی که DeepSeek-V3.2 مکانیزم توجه پراکنده کارآمد (fine-grained sparse attention) را برای پردازش بهبود یافته زمینه طولانی معرفی می‌کند.

---

## جزئیات

### Z.AI

#### GLM-4.6

ما **GLM-4.6** را معرفی می‌کنیم، جدیدترین مدل از Z.AI که پیشرفت‌های جامع در حوزه‌های مختلف از جمله کدنویسی واقعی، پردازش زمینه طولانی، استدلال، جستجو، نوشتن و برنامه‌های عامل‌محور دست یافته است. [مستندات](fa/providers/zai.md)

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 200K توکن (گسترش یافته از 128K) برای مدیریت وظایف پیچیده عامل‌محور
- **قابلیت‌های پیشرفته**: عملکرد برتر کدنویسی، استفاده از ابزار در حین استنتاج، فراخوانی تابع، خروجی‌های ساختاریافته
- **حداکثر خروجی**: 128K توکن
- **پشتیبانی استدلال**: حالت تفکر داخلی با پارامتر `thinking`
- **عملکرد واقعی**: عملکرد بهتر از Claude Sonnet 4 در تست‌های عملی کدنویسی در محیط Claude Code
- **پشتیبانی نقطه پایانی**: در دسترس در v1/chat/completions
- **جستجوی وب**: قابلیت‌های جستجوی وب یکپارچه به قیمت $0.01 به ازای هر فراخوانی ابزار

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی | جستجوی وب |
|-------|-------|--------------|--------|------------|
| glm-4.6 | $0.60/1M توکن | $0.11/1M توکن | $2.20/1M توکن | $0.01/فراخوانی |

**نکات برجسته عملکرد:**

GLM-4.6 عملکردی برابر با Claude Sonnet 4/Claude Sonnet 4.6 در 8 معیار معتبر (AIME 25، GPQA، LCB v6، HLE، SWE-Bench Verified) به دست می‌آورد و جایگاه خود را به عنوان یک مدل سطح بالا تثبیت می‌کند. در تست‌های کدنویسی واقعی، GLM-4.6 کارایی توکن بیش از 30٪ بهتر نسبت به نسخه قبلی خود نشان می‌دهد.

**مثال استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.6",
    "messages": [
      {
        "role": "user",
        "content": "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن."
      }
    ],
    "thinking": {
      "type": "enabled"
    },
    "max_tokens": 4096,
    "temperature": 0.6
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن.",
        }
    ],
    extra_body={"thinking": {"type": "enabled"}},
    max_tokens=4096,
    temperature=0.6,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.6",
    messages: [
        {
            role: "user",
            content: "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن."
        }
    ],
    thinking: {
        type: "enabled"
    },
    max_tokens: 4096,
    temperature: 0.6
});

console.log(response.choices[0].message.content);

```

**موارد استفاده:**

- **کدنویسی هوش مصنوعی**: عملکرد برتر در Claude Code، Cline، OpenCode و Roo Code با زیبایی‌شناسی بهبود یافته فرانت‌اند
- **دفتر هوشمند**: ایجاد PowerPoint پیشرفته و اتوماسیون اداری با ساختارهای منطقی واضح
- **ترجمه**: کیفیت بهینه‌شده برای فرانسوی، روسی، ژاپنی، کره‌ای و زمینه‌های غیررسمی
- **تولید محتوا**: بیان طبیعی در رمان‌ها، فیلمنامه‌ها و متن‌نویسی با گسترش زمینه‌ای
- **شخصیت‌های مجازی**: لحن ثابت در مکالمات چند دوره‌ای برای برنامه‌های هوش مصنوعی اجتماعی
- **جستجوی هوشمند**: درک بهبود یافته قصد و قابلیت‌های تحقیق عمیق

### DeepSeek

#### ارتقاء خودکار به DeepSeek-V3.2-Exp

مدل‌های DeepSeek به طور خودکار به مدل پایه جدید **DeepSeek-V3.2-Exp** ارتقا یافته‌اند که دارای DeepSeek Sparse Attention (DSA) برای آموزش و استنتاج سریع‌تر و کارآمدتر در زمینه طولانی است. این ارتقا یکپارچه است و نیازی به تغییر در پیاده‌سازی موجود شما ندارد.

**چه چیزی جدید است:**

- **فناوری DSA**: مکانیزم DeepSeek Sparse Attention (DSA) بهبود یافته با تاثیر حداقل بر کیفیت خروجی
- **کارایی بهبود یافته**: عملکرد بهبود یافته زمینه طولانی با کاهش هزینه محاسباتی
- **عملکرد**: برابر با V3.1-Terminus در معیارها
- **کاهش قیمت**: کاهش بیش از 50٪ هزینه در قیمت‌گذاری API

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

**قیمت‌گذاری به‌روزشده:**

| مدل | ورودی قبلی | خروجی قبلی | ورودی جدید | خروجی جدید | صرفه‌جویی |
|-------|----------------|-----------------|-----------|------------|---------|
| deepseek-chat | $0.56/1M | $1.68/1M | $0.28/1M | $0.42/1M | 50%+ |
| deepseek-reasoner | $0.56/1M | $1.68/1M | $0.28/1M | $0.42/1M | 50%+ |

**توجه:** قیمت ورودی کش‌شده نیز از $0.07/1M به $0.028/1M توکن کاهش یافته است.

**مسیریابی مدل:**

فراخوانی‌های API موجود شما به `deepseek-chat` (برای گفتگوی استاندارد) و `deepseek-reasoner` (برای حالت استدلال) به طور خودکار به مدل پایه جدید DeepSeek-V3.2-Exp هدایت می‌شوند. نیازی به اقدام از طرف شما نیست.

**مثال استفاده:**

```language-selector
bash=:# حالت گفتگوی استاندارد
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."
      }
    ]
  }'

# حالت استدلال
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# حالت گفتگوی استاندارد
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."}
    ],
)

print(response.choices[0].message.content)

# حالت استدلال
reasoning_response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
        }
    ],
)

print(reasoning_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// حالت گفتگوی استاندارد
const response = await client.chat.completions.create({
    model: "deepseek-chat",
    messages: [
        {
            role: "user",
            content: "محاسبات کوانتومی را به زبان ساده توضیح بده."
        }
    ]
});

console.log(response.choices[0].message.content);

// حالت استدلال
const reasoningResponse = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: [
        {
            role: "user",
            content: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن."
        }
    ]
});

console.log(reasoningResponse.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های Z.AI](fa/providers/zai.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/guides/rate-limits.md)
- [بهترین شیوه‌ها برای تولید](fa/guides/production-best-practices.md)