# افزودن مدل‌های جدید: GPT-5.1-Codex-Max و Mistral Large 3

**تاریخ:** ۱۴۰۴-۰۹-۱۵ / (2025-12-06)

## خلاصه

ما افزودن دو مدل قدرتمند جدید را اعلام می‌کنیم: GPT-5.1-Codex-Max از OpenAI، هوشمندترین مدل کدنویسی بهینه‌شده برای کارهای عاملی کدنویسی طولانی‌مدت، و Mistral Large 3 از Mistral AI، یک مدل متن‌باز پیشرفته با ۶۷۵ میلیارد پارامتر کل و قابلیت‌های چندوجهی. هر دو مدل اکنون از طریق API AvalAI در دسترس هستند.

---

## جزئیات

### OpenAI

#### GPT-5.1-Codex-Max

ما **GPT-5.1-Codex-Max** (`gpt-5.1-codex-max`) را معرفی می‌کنیم، هوشمندترین مدل کدنویسی OpenAI که به طور خاص برای کدنویسی عاملی طراحی شده است. این مدل برای کارهای برنامه‌نویسی طولانی‌مدت و چندمرحله‌ای و جریان‌های کاری عامل خودکار بهینه‌سازی شده است. [مستندات](fa/providers/openai.md)

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: ۴۰۰٬۰۰۰ توکن برای مدیریت کدبیس‌ها و اسناد گسترده
- **حداکثر توکن خروجی**: ۱۲۸٬۰۰۰ توکن برای تولید کد جامع
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته، پشتیبانی از توکن‌های استدلال، بینایی (ورودی تصویر)
- **تمرکز عاملی**: بهینه‌شده برای کارهای کدنویسی طولانی‌مدت و جریان‌های کاری برنامه‌نویسی خودکار
- **تاریخ دانش**: ۳۰ سپتامبر ۲۰۲۴
- **پشتیبانی نقاط پایانی**: در دسترس در [`v1/chat/completions`](fa/api-reference/chat.md) و [`v1/responses`](fa/api-reference/responses.md)
- **استریمینگ**: کاملا پشتیبانی می‌شود

**روش‌های ورودی/خروجی:**
- **ورودی**: متن، تصویر
- **خروجی**: متن

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5.1-codex-max | $1.25/1M توکن | $0.125/1M توکن | $10.00/1M توکن |

**نمونه استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1-codex-max",
    "messages": [
      {
        "role": "user",
        "content": "یک پیاده‌سازی کامل TypeScript از سیستم صف کار توزیع‌شده با مدیریت کارگر، اولویت‌بندی کارها و بازیابی از خطا ایجاد کنید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5.1-codex-max",
    messages=[
        {
            "role": "user",
            "content": "یک پیاده‌سازی کامل TypeScript از سیستم صف کار توزیع‌شده با مدیریت کارگر، اولویت‌بندی کارها و بازیابی از خطا ایجاد کنید.",
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
  model: "gpt-5.1-codex-max",
  messages: [
    {
      role: "user",
      content: "یک پیاده‌سازی کامل TypeScript از سیستم صف کار توزیع‌شده با مدیریت کارگر، اولویت‌بندی کارها و بازیابی از خطا ایجاد کنید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### Mistral AI

#### Mistral Large 3

ما **Mistral Large 3** (`mistral-large-3`) را معرفی می‌کنیم، توانمندترین مدل Mistral AI تا به امروز. این مدل متن‌باز پیشرفته یک معماری مخلوط-متخصصان پراکنده با ۴۱ میلیارد پارامتر فعال و ۶۷۵ میلیارد پارامتر کل است که تحت مجوز Apache 2.0 منتشر شده است. [مستندات](fa/providers/mistralai.md)

**ویژگی‌های کلیدی:**
- **معماری**: مخلوط-متخصصان پراکنده (۴۱ میلیارد فعال / ۶۷۵ میلیارد کل پارامتر)
- **متن‌باز**: منتشر شده تحت مجوز Apache 2.0
- **چندوجهی**: قابلیت‌های بومی درک تصویر
- **چندزبانه**: بهترین عملکرد در کلاس در مکالمات غیر انگلیسی/چینی با ۴۰+ زبان بومی
- **پنجره زمینه**: پنجره زمینه بزرگ برای پردازش اسناد گسترده
- **رتبه LMArena**: رتبه ۲ در دسته مدل‌های OSS غیر استدلالی (رتبه ۶ کلی در میان مدل‌های OSS)
- **پشتیبانی نقاط پایانی**: در دسترس در [`v1/chat/completions`](fa/api-reference/chat.md)

**چه چیزی Mistral Large 3 را خاص می‌کند:**
- اولین مدل مخلوط-متخصصان از Mistral از زمان سری اصلی Mixtral
- به برابری با بهترین مدل‌های متن‌باز تنظیم‌شده با دستورالعمل در درخواست‌های عمومی می‌رسد
- چک‌پوینت بهینه‌شده در فرمت NVFP4 برای استقرار کارآمد در دسترس است
- می‌تواند روی یک گره تک 8×A100 یا 8×H100 با استفاده از vLLM اجرا شود

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی | هر صفحه |
|-------|-------|--------------|--------|----------|
| mistral-large-3 | $0.50/1M توکن | $0.05/1M توکن | $1.50/1M توکن | $0.001/صفحه |

**نمونه استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-large-3",
    "messages": [
      {
        "role": "user",
        "content": "پیامدهای محاسبات کوانتومی بر رمزنگاری مدرن را تحلیل کنید و استراتژی‌های کاهش ریسک پیشنهاد دهید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="mistral-large-3",
    messages=[
        {
            "role": "user",
            "content": "پیامدهای محاسبات کوانتومی بر رمزنگاری مدرن را تحلیل کنید و استراتژی‌های کاهش ریسک پیشنهاد دهید.",
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
  model: "mistral-large-3",
  messages: [
    {
      role: "user",
      content: "پیامدهای محاسبات کوانتومی بر رمزنگاری مدرن را تحلیل کنید و استراتژی‌های کاهش ریسک پیشنهاد دهید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

**استفاده از SDK Mistral:**

```language-selector
python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

response = client.chat.complete(
    model="mistral-large-3",
    messages=[
        {
            "role": "user",
            "content": "مزایای معماری مخلوط-متخصصان در مدل‌های زبان بزرگ را توضیح دهید.",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "[REDACTED]",
  baseURL: "https://api.avalai.ir",
});

const response = await client.chat.complete({
  model: "mistral-large-3",
  messages: [
    {
      role: "user",
      content: "مزایای معماری مخلوط-متخصصان در مدل‌های زبان بزرگ را توضیح دهید.",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Mistral AI](fa/providers/mistralai.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)