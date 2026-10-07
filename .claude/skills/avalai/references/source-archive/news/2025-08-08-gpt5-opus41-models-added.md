# افزودن مدل‌های پیشرفته جدید: سری GPT-5 و Claude Opus 4.1

**تاریخ:** 1404-05-18 / (2025-08-08)

## خلاصه

اکنون AvalAI با افتخار از جدیدترین مدل‌های سری GPT-5 از OpenAI و Claude Opus 4.1 از Anthropic پشتیبانی می‌کند. این بروزرسانی دسترسی شما را به پیشرفته‌ترین قابلیت‌های هوش مصنوعی برای کدنویسی، استدلال پیچیده و وظایف عاملی (Agentic Tasks) فراهم می‌آورد. این مدل‌های نوین، عملکردی بهینه‌شده را در کنار گزینه‌های مقرون‌به‌صرفه‌تر در تمامی سطوح ارائه می‌دهند.

---

## جزئیات بیشتر

اضافه شدن مدل‌های پیشرفته از OpenAI و Anthropic را به پلتفرم خود اعلام می‌داریم. این مدل‌های جدید، جهش‌های قابل توجهی در قابلیت‌های هوش مصنوعی، به‌ویژه در زمینه‌های استدلال پیچیده، وظایف کدنویسی و گردش‌های کاری عاملی، به نمایش می‌گذارند.

### سری OpenAI GPT-5

سری GPT-5 از OpenAI، معرف پیشرفته‌ترین مدل‌های این شرکت است که عملکردی بی‌نظیر در کدنویسی، استدلال و وظایف عاملی با گزینه‌های قیمت‌گذاری منعطف ارائه می‌دهد.

- **[`gpt-5`](fa/providers/openai.md#gpt-5)**: مدل اصلی و پرچمدار، بهینه‌سازی‌شده برای کدنویسی و وظایف عاملی در حوزه‌های مختلف، با پنجره متنی 400 هزار توکنی و پشتیبانی از توکن استدلال.
- **[`gpt-5-2025-08-07`](fa/providers/openai.md#gpt-5)**: نسخه اسنپ‌شات (Snapshot) خاص GPT-5 برای تضمین عملکرد ثابت و پایدار.
- **[`gpt-5-mini`](fa/providers/openai.md#gpt-5-mini)**: نسخه‌ای سریع‌تر و بهینه‌تر از نظر هزینه، مناسب برای وظایف با تعریف مشخص، با 80% صرفه‌جویی در هزینه.
- **[`gpt-5-mini-2025-08-07`](fa/providers/openai.md#gpt-5-mini)**: نسخه اسنپ‌شات GPT-5 mini.
- **[`gpt-5-nano`](fa/providers/openai.md#gpt-5-nano)**: سریع‌ترین و مقرون‌به‌صرفه‌ترین گزینه، ایده‌آل برای خلاصه‌سازی و وظایف طبقه‌بندی.
- **[`gpt-5-nano-2025-08-07`](fa/providers/openai.md#gpt-5-nano)**: نسخه اسنپ‌شات GPT-5 nano.
- **[`gpt-5-chat`](fa/providers/openai.md#gpt-5-chat)**: همان مدلی که در رابط کاربری ChatGPT مورد استفاده قرار می‌گیرد.
- **[`gpt-5-chat-latest`](fa/providers/openai.md#gpt-5-chat)**: همواره به جدیدترین نسخه GPT-5 Chat اشاره دارد.

**ویژگی‌های کلیدی:**
- پنجره متنی 400,000 توکنی (با حداکثر 128,000 توکن خروجی).
- قابلیت‌های بینایی (ورودی متن و تصویر).
- فراخوانی توابع (Function Calling) و خروجی‌های ساختاریافته.
- پشتیبانی از توکن استدلال.
- کش کردن دستورات (Instruction Caching) برای بهینه‌سازی هزینه.
- پشتیبانی از تنظیم دقیق (Fine-tuning).

### Anthropic Claude Opus 4.1

Claude Opus 4.1 پیشرفت‌های چشمگیری در عملکرد کدنویسی ارائه می‌دهد و به نرخ 74.5% در معیار SWE-bench Verified دست یافته است. این مدل همچنین قابلیت‌های تحقیق و تحلیل داده بهبود یافته‌ای دارد.

- **[`claude-opus-4-1`](fa/providers/anthropic.md#claude-opus-41)**: مدل پیشرفته‌ای که در بازسازی کد چندفایله و اشکال‌زدایی دقیق در پایگاه‌های کد بزرگ، عملکردی بی‌نظیر از خود نشان می‌دهد.

**بهبودهای کلیدی:**
- عملکرد بهبود یافته در وظایف عاملی.
- قابلیت‌های کدنویسی واقعی و برتر.
- استدلال و ردیابی جزئیات با دقت بالاتر.
- مهارت‌های پیشرفته‌تر در تحلیل داده و تحقیق.
- قابلیت‌های استفاده از رایانه.
- پنجره متنی 200,000 توکنی.

### نمونه‌های کاربرد

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از GPT-5 برای استدلال پیچیده
completion = client.chat.completions.create(
    model="gpt-5",
    messages=[
        {
            "role": "user",
            "content": "این پایگاه کد را تحلیل کنید و بهبودهای معماری پیشنهاد دهید.",
        }
    ],
)

print(completion.choices[0].message.content)

# استفاده از GPT-5 nano برای طبقه‌بندی
completion = client.chat.completions.create(
    model="gpt-5-nano",
    messages=[
        {
            "role": "user",
            "content": "این متن را به عنوان مثبت، منفی یا خنثی طبقه‌بندی کنید: 'محصول خوب کار می‌کند اما می‌تواند بهبود یابد.'",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
apiKey: process.env.AVALAI_API_KEY,
baseURL: "https://api.avalai.ir/v1",
});

// استفاده از GPT-5 mini برای وظایف کارآمد
const completion = await client.chat.completions.create({
model: "gpt-5-mini",
messages: [
{
role: "user",
content: "یک تابع پایتون برای محاسبه اعداد فیبوناچی تولید کنید.",
},
],
});

console.log(completion.choices[0].message.content);

// استفاده از Claude Opus 4.1 برای وظایف کدنویسی پیچیده
const opusCompletion = await client.chat.completions.create({
model: "claude-opus-4-1",
messages: [
{
role: "user",
content: "این پروژه جاوا اسکریپت چندفایله را برای استفاده از TypeScript با تعاریف نوع مناسب بازسازی کنید.",
},
],
});

console.log(opusCompletion.choices[0].message.content);

```

### نمای کلی قیمت‌گذاری

سری GPT-5 سطوح قیمت‌گذاری انعطاف‌پذیری را ارائه می‌دهد:

- **GPT-5**: 1.25 دلار ورودی / 10.00 دلار خروجی به ازای هر 1 میلیون توکن
- **GPT-5 Mini**: 0.25 دلار ورودی / 2.00 دلار خروجی به ازای هر 1 میلیون توکن
- **GPT-5 Nano**: 0.05 دلار ورودی / 0.40 دلار خروجی به ازای هر 1 میلیون توکن
- **Claude Opus 4.1**: 15.00 دلار ورودی / 75.00 دلار خروجی به ازای هر 1 میلیون توکن

تمامی مدل‌ها از قابلیت کش کردن دستورات برای صرفه‌جویی بیشتر در هزینه مربوط به زمینه تکراری پشتیبانی می‌کنند.

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Anthropic](fa/providers/anthropic.md)
- [مستندات API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/guides/rate-limits.md)