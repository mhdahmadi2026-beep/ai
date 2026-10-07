# مدل‌های DeepSeek-V3.1، Grok Code Fast 1، و بهبود عملکرد استریمینگ

**تاریخ:** 1404-06-24 / (2025-09-14)

## خلاصه

AvalAI مدل‌های DeepSeek-V3.1 را از طریق Azure AI در چندین endpoint معرفی می‌کند، grok-code-fast-1 جدید X.AI را که برای محیط‌های کدنویسی بر پایه Agent بهینه‌سازی شده اضافه می‌کند، و بهبودهای قابل توجهی در API جریانی (استریمینگ) با سرعت پاسخ تا 6 برابر سریع‌تر و دستیابی به 95% برابری عملکرد ارائه‌دهنده ارائه می‌دهد.

---

## جزئیات

خرسندیم سه پیشرفت کلیدی را معرفی کنیم که نه‌ تنها قابلیت‌های هوش مصنوعی ما را به سطحی نوین ارتقا می‌دهد، بلکه عملکرد کلی پلتفرم را نیز به شکلی چشمگیر بهبود می‌بخشد.

### مدل‌های DeepSeek-V3.1 از طریق Azure AI

ما DeepSeek-V3.1، آخرین پیشرفت در هوش مصنوعی استدلالی که برای عصر عامل طراحی شده است، را از طریق Azure AI در چندین endpoint ادغام کرده‌ایم.

#### DeepSeek

- **deepseek-v3.1**: DeepSeek-V3.1 در حالت غیر تفکری، برای پاسخ‌های سریع و کارآمد با قابلیت‌های استنتاج ترکیبی و استفاده بهبود یافته از ابزار بهینه‌سازی شده است. [مستندات](https://api-docs.deepseek.com/news/news250821)

**ویژگی‌های کلیدی:**
- **پنجره متن**: 128K توکن
- **حداکثر توکن‌های خروجی**: محدودیت‌های استاندارد خروجی
- **حالت**: حالت غیر تفکری برای پاسخ‌های کارآمد
- **قیمت ورودی (cache hit)**: $0.07 / 1M توکن
- **قیمت ورودی (cache miss)**: $0.27 / 1M توکن
- **قیمت خروجی**: $1.10 / 1M توکن
- **نقاط قوت**: پاسخ‌های سریع، پردازش کارآمد، قابلیت‌های کلی قوی، استفاده بهبود یافته از ابزار
- **بهترین برای**: گفتگوی عمومی، پاسخ‌های سریع، برنامه‌های پرحجم، گردش‌کارهای عامل
- **استدلال**: استدلال استاندارد بدون فرآیند تفکر آشکار
- **در دسترس در**: [`v1/chat/completions`](fa/api-reference/chat.md)، [`v1/responses`](fa/api-reference/responses.md)، [`v1/messages`](fa/api-reference/messages.md)

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-v3.1",
    messages=[
        {
            "role": "user",
            "content": "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
    model: "deepseek-v3.1",
    messages: [
        {
            role: "user",
            content: "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
        },
    ],
});

console.log(response.choices[0].message.content);

```

### X.AI Grok Code Fast 1

ما grok-code-fast-1 جدید X.AI را اضافه کرده‌ایم، یک مدل استدلالی سریع و اقتصادی که در گردش‌کارهای کدنویسی عامل با سرعت استنتاج فوق‌العاده عالی عمل می‌کند.

#### X.AI

- **grok-code-fast-1**: مدلی که به طور خاص برای گردش‌کارهای کدنویسی عامل با سرعت استثنایی و تسلط بر ابزارها بهینه‌سازی شده است. [مستندات](https://x.ai/news/grok-code-fast-1)

**ویژگی‌های کلیدی:**
- **پنجره متن**: پشتیبانی از متن بزرگ برای کدبیس‌های گسترده
- **قیمت ورودی**: $0.20 / 1M توکن
- **قیمت خروجی**: $1.50 / 1M توکن
- **قیمت ورودی کش شده**: $0.02 / 1M توکن
- **نقاط قوت**: پاسخ‌های فوق‌العاده سریع، کدنویسی عامل، تسلط بر ابزارها (grep، terminal، ویرایش فایل)
- **بهترین برای**: ادغام IDE، تولید کد، دیباگ، تجزیه و تحلیل pull request
- **عملکرد**: 190+ توکن در ثانیه با نرخ cache hit بالای 90%
- **زبان‌ها**: TypeScript، Python، Java، Rust، C++، Go
- **در دسترس در**: [`v1/chat/completions`](fa/api-reference/chat.md)، [`v1/responses`](fa/api-reference/responses.md)، [`v1/messages`](fa/api-reference/messages.md)

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="grok-code-fast-1",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای پیاده‌سازی جستجوی دودویی با مدیریت خطای مناسب ایجاد کنید",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
    model: "grok-code-fast-1",
    messages: [
        {
            role: "user",
            content: "یک interface TypeScript برای سیستم مدیریت کاربر ایجاد کنید",
        },
    ],
});

console.log(response.choices[0].message.content);

```

### بهبود عملکرد API استریمینگ

ما زیرساخت اصلی API خود را با بهبودهای مهم استریمینگ که عملکرد استثنایی را در تمام endpoint های پشتیبانی شده ارائه می‌دهد، به طور قابل توجهی ارتقا داده‌ایم.

**بهبودهای عملکرد:**
- **بهبود سرعت**: تا 6 برابر سریع‌تر پاسخ‌های استریمینگ (chunks/second)
- **برابری ارائه‌دهنده**: 95% عملکرد یکسان با استریمینگ ارائه‌دهنده اصلی
- **پوشش**: بهبودها در API های Chat Completions، Responses، Messages، و Gemini v1beta/models
- **بهینه‌سازی**: پردازش chunk پیشرفته و مدیریت اتصال
- **قابلیت اطمینان**: مدیریت خطای بهبود یافته و پایداری اتصال

**Endpoint های تحت تاثیر:**
- [`v1/chat/completions`](fa/api-reference/chat.md) - تکمیل گفتگو با استریمینگ
- [`v1/responses`](fa/api-reference/responses.md) - تولید پاسخ با استریمینگ
- [`v1/messages`](fa/api-reference/messages.md) - پردازش پیام با استریمینگ
- [`/v1beta/models`](fa/news/2025-07-22-native-gemini-api-support-now-available.md) - استریمینگ API بومی Gemini

این بهبودها تضمین می‌کنند که پاسخ‌های استریمینگ اکنون با سرعت و قابلیت اطمینان دسترسی مستقیم ارائه‌دهنده مطابقت دارند در حالی که تمام مزایای رویکرد API یکپارچه AvalAI را حفظ می‌کنند.

---

## لینک‌های مرتبط

- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [مرجع API Chat Completions](fa/api-reference/chat.md)
- [مرجع API Responses](fa/api-reference/responses.md)
- [مرجع API Messages](fa/api-reference/messages.md)
- [راهنمای پاسخ‌های استریمینگ](fa/guides/streaming-responses.md)
- [مستندات رسمی DeepSeek](https://api-docs.deepseek.com/news/news250821)