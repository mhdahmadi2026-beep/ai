# مدل‌های هوش مصنوعی Cloudflare به AvalAI اضافه شدند

**تاریخ:** ۱۴۰۴/۰۶/۱۱ (2025-09-01)

## خلاصه

اکنون AvalAI با افتخار پشتیبانی از ۲۱ مدل جدید هوش مصنوعی Cloudflare را اعلام می‌کند. این مجموعه شامل مدل‌های پیشرفته‌ای نظیر Llama 4 Scout، Llama 3.3، Gemma 3 و مدل‌های تخصصی استدلال است. با بهره‌گیری از شبکه جهانی Cloudflare، این مدل‌ها عملکردی بهینه، قابلیت‌های چندوجهی و استنتاجی سریع‌تر را برای کاربران ما به ارمغان می‌آورند.

---

## جزئیات

ما بسیار خرسندیم که با افزودن ۲۱ مدل جدید هوش مصنوعی Cloudflare، گامی دیگر در جهت گسترش توانمندی‌های پلتفرم AvalAI برداشته‌ایم. این مدل‌ها با استفاده از زیرساخت Workers AI شرکت Cloudflare، استنتاج هوش مصنوعی را با سرعت و پایداری بالا در لبه شبکه جهانی ممکن می‌سازند.

### مدل‌های Meta Llama

**سری Llama 4 Scout:**
- **cf.llama-4-scout-17b-16e-instruct**: جدیدترین مدل ۱۷ میلیارد پارامتری متا با ۱۶ متخصص که با قابلیت‌های چندوجهی بومی و معماری ترکیبی از متخصصان (MoE)، درک متن و تصویر را به سطحی نوین ارتقا می‌دهد. [مستندات](fa/providers/cloudflare.md)

**سری Llama 3.3:**
- **cf.llama-3.3-70b-instruct-fp8-fast**: مدل Llama 3.3 70B که با کوانتیزه‌سازی FP8، سرعت استنتاج را بدون افت محسوس کیفیت، به شکل چشمگیری افزایش داده است. [مستندات](fa/models/cf.llama-3.3-70b-instruct-fp8-fast.md)

**سری Llama 3.1:**
- **cf.llama-3.1-8b-instruct-fast**: نسخه‌ای سریع از مدل چندزبانه Llama 3.1 8B متا که برای کاربردهای مکالمه بهینه‌سازی شده است. [مستندات](fa/models/cf.llama-3.1-8b-instruct-fast.md)
- **cf.llama-3.1-8b-instruct-awq**: نسخه‌ای کوانتیزه‌شده (int4) برای استنتاج بهینه و مصرف منابع کمتر. [مستندات](fa/models/cf.llama-3.1-8b-instruct-awq.md)
- **cf.llama-3.1-8b-instruct-fp8**: نسخه‌ای کوانتیزه‌شده با دقت FP8 که تعادلی میان عملکرد و کارایی برقرار می‌کند. [مستندات](fa/models/cf.llama-3.1-8b-instruct-fp8.md)
- **cf.llama-3.1-8b-instruct**: مدل استاندارد Llama 3.1 8B که برای پیروی از دستورالعمل‌ها تنظیم شده است. [مستندات](fa/models/cf.llama-3.1-8b-instruct.md)
- **cf.llama-3.1-70b-instruct**: مدل بزرگ ۷۰ میلیارد پارامتری برای حل مسائل پیچیده و نیازمند استدلال عمیق. [مستندات](fa/models/cf.llama-3.1-70b-instruct.md)

**سری Llama 3.2:**
- **cf.llama-3.2-1b-instruct**: مدلی فشرده با ۱ میلیارد پارامتر که برای مکالمات چندزبانه بهینه‌سازی شده است. [مستندات](fa/models/cf.llama-3.2-1b-instruct.md)
- **cf.llama-3.2-3b-instruct**: مدلی با ۳ میلیارد پارامتر که برای وظایف نیازمند عاملیت (Agentic) مانند خلاصه‌سازی و بازیابی اطلاعات مناسب است. [مستندات](fa/models/cf.llama-3.2-3b-instruct.md)

**سری Llama 3:**
- **cf.meta-llama-3-8b-instruct**: مدل پیشرفته ۸ میلیارد پارامتری با قابلیت‌های استدلال بهبودیافته. [مستندات](fa/models/cf.meta-llama-3-8b-instruct.md)
- **cf.llama-3-8b-instruct-awq**: نسخه‌ای کوانتیزه‌شده برای استقرار بهینه. [مستندات](fa/models/cf.llama-3-8b-instruct-awq.md)
- **cf.llama-3-8b-instruct**: مدل استاندارد Llama 3 8B که برای پیروی از دستورالعمل‌ها تنظیم شده است. [مستندات](fa/models/cf.llama-3-8b-instruct.md)

**مدل‌های ایمنی:**
- **cf.llama-guard-3-8b**: مدلی برای طبقه‌بندی ایمنی محتوا که به فیلتر کردن درخواست‌ها و پاسخ‌ها کمک می‌کند. [مستندات](fa/models/cf.llama-guard-3-8b.md)

### مدل‌های Google Gemma

- **cf.gemma-3-12b-it**: جدیدترین مدل از خانواده Gemma با قابلیت‌های چندوجهی، پنجره زمینه ۱۲۸ هزار توکنی و پشتیبانی از بیش از ۱۴۰ زبان. [مستندات](fa/models/cf.gemma-3-12b-it.md)
- **cf.gemma-7b-it-lora**: مدل پایه Gemma 7B که برای استنتاج با آداپتورهای LoRA بهینه‌سازی شده است. [مستندات](fa/models/cf.gemma-7b-it-lora.md)
- **cf.gemma-2b-it-lora**: مدل فشرده Gemma 2B برای کاربردهای تنظیم دقیق (Fine-tuning) با LoRA. [مستندات](fa/models/cf.gemma-2b-it-lora.md)
- **cf.gemma-7b-it**: مدل استاندارد Gemma 7B که برای پیروی از دستورالعمل‌ها تنظیم شده است. [مستندات](fa/models/cf.gemma-7b-it.md)

### مدل‌های Mistral AI

- **cf.mistral-small-3.1-24b-instruct**: نسخه بهبودیافته Mistral Small 3.1 با درک بصری پیشرفته و پنجره زمینه ۱۲۸ هزار توکنی. [مستندات](fa/models/cf.mistral-small-3.1-24b-instruct.md)

### مدل‌های Qwen

- **cf.qwq-32b**: مدلی پیشرفته با توانایی تفکر و استدلال که عملکردی رقابتی در برابر بهترین مدل‌های استدلال جهان دارد. [مستندات](fa/models/cf.qwq-32b.md)
- **cf.qwen2.5-coder-32b-instruct**: جدیدترین مدل تخصصی کد از خانواده Qwen با ۳۲ میلیارد پارامتر برای وظایف برنامه‌نویسی. [مستندات](fa/models/cf.qwen2.5-coder-32b-instruct.md)

### مدل‌های DeepSeek

- **cf.deepseek-r1-distill-qwen-32b**: مدلی تقطیر شده از DeepSeek-R1 که در بسیاری از معیارها، عملکردی بهتر از OpenAI-o1-mini ارائه می‌دهد. [مستندات](fa/models/cf.deepseek-r1-distill-qwen-32b.md)

### ویژگی‌های کلیدی

- **استقرار جهانی در لبه شبکه**: تمامی مدل‌ها بر روی شبکه جهانی Cloudflare اجرا می‌شوند تا کمترین تاخیر ممکن را داشته باشند.
- **قابلیت‌های چندوجهی**: بسیاری از مدل‌ها از ورودی متن و تصویر به صورت همزمان پشتیبانی می‌کنند.
- **فراخوانی توابع**: مدل‌های پیشرفته از فراخوانی توابع ساختاریافته (Function Calling) پشتیبانی می‌کنند.
- **عملکرد بهینه**: گزینه‌های متنوع کوانتیزه‌سازی (FP8, AWQ, int4) برای نیازهای مختلف عملکردی.
- **پشتیبانی از LoRA**: مدل‌های منتخب از تکنیک LoRA برای تنظیم دقیق (Fine-tuning) پشتیبانی می‌کنند.

### نقاط پایانی API

تمامی مدل‌های Cloudflare از طریق نقاط پایانی زیر در دسترس هستند:
- **تکمیل چت**: `v1/chat/completions` (پشتیبانی کامل)
- **پاسخ‌ها**: `v1/responses` (پشتیبانی جزئی)
- **پیام‌ها**: `v1/messages` (پشتیبانی جزئی)

### مثال کاربردی

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="cf.llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید.",
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
 model: "cf.llama-4-scout-17b-16e-instruct",
 messages: [
 {
 role: "user",
 content: "محاسبات کوانتومی را به زبان ساده توضیح دهید.",
 },
 ],
});

console.log(completion.choices[0].message.content);

```

### بهترین شیوه‌ها

- **انتخاب مدل**: برای سرعت بیشتر، از مدل‌های کوانتیزه‌شده (FP8, AWQ) استفاده کنید.
- **طول زمینه**: از پنجره زمینه بزرگ مدل‌های جدیدتر مانند Gemma 3 (۱۲۸ هزار توکن) بهره ببرید.
- **وظایف چندوجهی**: برای تحلیل همزمان متن و تصویر، از Llama 4 Scout استفاده کنید.
- **تولید کد**: مدل Qwen2.5-Coder بهترین گزینه برای وظایف برنامه‌نویسی است.
- **ایمنی**: برای کنترل محتوای ورودی و خروجی، از Llama Guard 3 استفاده کنید.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Cloudflare AI](fa/providers/cloudflare.md)
- [مستندات API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [راهنمای فراخوانی توابع](fa/guides/function-calling.md)
- [راهنمای قابلیت‌های بصری](fa/guides/vision.md)
