خب من بهت تیکه تیکه میدم! تو در سریعترین حالت ممکن درست کن و بهم بگو که انجام شد و نکته خاصی اگر مد نظرت بود بهم بگو

[رفتن به محتوای اصلی](https://docs.avalai.ir/fa/#doc-content)
[AvalAI Docs](https://docs.avalai.ir/fa/)
[راهنماها](https://docs.avalai.ir/fa/guides/best-practices)[مرجع API](https://docs.avalai.ir/fa/api-reference/introduction)[مدل‌ها](https://docs.avalai.ir/fa/models)[قیمت‌گذاری](https://docs.avalai.ir/fa/pricing)
جستجو در مستندات⌘ K[فاA](https://docs.avalai.ir/en/)[داشبورد توسعه‌دهنده](https://chat.avalai.ir/platform/home)
خبر‌ها
شروع به کار

* [معرفی](https://docs.avalai.ir/fa/)
* [شروع سریع](https://docs.avalai.ir/fa/quickstart)
* [استفاده عملی از هوش مصنوعی](https://docs.avalai.ir/fa/guides/ai-workflows)
* [کتابخانه‌ها](https://docs.avalai.ir/fa/libraries)
* [عملکرد](https://docs.avalai.ir/fa/performance)
* [قیمت‌گذاری](https://docs.avalai.ir/fa/pricing)
* [سطوح سرویس](https://docs.avalai.ir/fa/service-tiers)
* [بسته‌های اعتباری](https://docs.avalai.ir/fa/credit-packages)
* [محدودیت‌های نرخ مدل](https://docs.avalai.ir/fa/rate-limits)
* [مدل‌های منسوخ شده](https://docs.avalai.ir/fa/deprecations)

نمایندگان فروش
مرجع API
ارائه‌دهندگان
راهنماها
ابزار‌های داخلی
بهترین شیوه‌ها
مثال‌ها
منابع
به کمک نیاز دارید؟
[ایجاد تیکت پشتیبانی](https://chat.avalai.ir/platform/support/create-ticket)[رفع اشکال با چت AvalAI](https://chat.avalai.ir/chat)
پیوند صفحات مستندات را در صفحه چت AvalAI جای‌گذاری کنید و از مدل‌ هوش مصنوعی برای کمک به رفع اشکال سوال کنید.
کپی لینک
کپی Markdownپرسش از هوش مصنوعی
توسعه هوش مصنوعی با AvalAI
با یک درخواست واقعی شروع کنید و سپس مسیر مستنداتی را دنبال کنید که با محصول شما هماهنگ است. AvalAI با یک آدرس پایه واحد در کلاینت‌های سازگار با OpenAI کار می‌کند.
[شروع راه‌اندازی سریع](https://docs.avalai.ir/fa/quickstart)[مشاهده مرجع API](https://docs.avalai.ir/fa/api-reference/introduction)

کاربران ممکن است AvalAI را با املاهای رایج «اول ai» یا «اول ای آی» و یا «هوش مصنوعی اول» پیدا کنند؛ نام رسمی در مستندات همیشه به همین شکل نوشته می‌شود.

اولین درخواست خود را ارسال کنید
با Responses API مطمئن شوید کلید، کلاینت و مدل به‌درستی با هم کار می‌کنند.

1. یک کلید API بسازید[داشبورد AvalAI را باز کنید](https://chat.avalai.ir/platform/home)، یک کلید پروژه بسازید و آن را فقط در سرور نگه دارید.
2. یک کلاینت نصب کنیداز SDK سازگار با OpenAI برای Python یا JavaScript استفاده کنید یا همان درخواست را با cURL بفرستید.
3. درخواست Responses را اجرا کنیدمتغیر `AVALAI_API_KEY` را تنظیم کنید، مثال را اجرا کنید و `response.output_text` را بخوانید.

PythonJavaScriptBash

```
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)

print(response.output_text)
```

1
2
3
4
5
6
7
8
9
10
11
12
13
14
مسیر مناسب کار خود را انتخاب کنید
مستقیم به API و راهنماهای مرتبط با نیاز خود بروید.
[متن و استدلالپاسخ‌های حالت‌مند، خروجی ساختاریافته و گردش‌کارهای استدلالی بسازید.←](https://docs.avalai.ir/fa/api-reference/responses)[تصویر و بیناییمحتوای تصویری را تولید، ویرایش و تحلیل کنید.←](https://docs.avalai.ir/fa/api-reference/images)[صوت و گفتارصوت را رونویسی کنید و خروجی گفتاری بسازید.←](https://docs.avalai.ir/fa/api-reference/audio)[ابزارها و بازیابیمدل‌ها را به توابع، فایل‌ها، جست‌وجو و داده‌های برنامه متصل کنید.←](https://docs.avalai.ir/fa/guides/tools)
مدل مناسب و هزینه آن را پیدا کنید
ابتدا قابلیت‌های مستندشده را مقایسه کنید و سپس قیمت فعلی ورودی و خروجی را ببینید.
[جدید: Gemini 3.8 Flash و Flash-Lite TTSFlash را برای روایت خلاقانه، لهجه‌ها و پایداری گفتار طولانی و Lite را برای زنجیره پردازش عامل صوتی پرحجم و خواندن متن با صدا انتخاب کنید. هر دو فارسی دارند؛ نرخ تشویقی توکن تا ۱۰ دی ۱۴۰۵ (2026-12-31) و نکات درخواست ساختاریافته و مهاجرت قالب صوت را ببینید.←](https://docs.avalai.ir/fa/news/2026-09-30-gemini-3-8-tts-models-added)[جدید: GPT-6.1 Sol و Claude Sonnet 5.5از سطح ۱ با ](https://docs.avalai.ir/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added)`gpt-6.1-sol`[ یا ](https://docs.avalai.ir/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added)`claude-sonnet-5-5`[ گردش‌کارهای کدنویسی و اسنادی بسازید. هر دو از Chat Completions و Messages کامل پشتیبانی می‌کنند؛ Responses برای Sol کامل و برای Sonnet جزئی است. نرخ استاندارد هر میلیون توکن ورودی ۲ دلار و خروجی ۱۰ دلار است؛ قیمت حافظه نهان و مهاجرت تفکر Sonnet را مقایسه کنید.←](https://docs.avalai.ir/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added)[پرچم‌دار جدید Anthropic: Claude Opus 5.5از ](https://docs.avalai.ir/fa/news/2026-09-24-claude-opus-5-5-added)`claude-opus-5-5`[ برای کدنویسی طولانی‌مدت و کار دانشی با تفکر تطبیقی همیشه‌فعال، پنجره ورودی یک‌میلیون‌توکنی و پشتیبانی کامل Chat Completions، Messages و Responses استفاده کنید. از سطح ۱ در دسترس است؛ قیمت هر یک میلیون توکن ورودی ۴ دلار و خروجی ۲۰ دلار است.←](https://docs.avalai.ir/fa/news/2026-09-24-claude-opus-5-5-added)[جدید: GPT-6 Sol، GPT-6 Luna و Grok 4.7از ](https://docs.avalai.ir/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added)`gpt-6-sol`[ و ](https://docs.avalai.ir/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added)`gpt-6-luna`[ از OpenAI برای استدلال کم‌هزینه، یا از ](https://docs.avalai.ir/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added)`grok-4.7`[ از xAI برای کدنویسی طولانی‌مدت و کار دانشی استفاده کنید. هر سه از Chat Completions و Messages پشتیبانی می‌کنند؛ پشتیبانی Responses برای Sol و Luna کامل و برای Grok جزئی است.←](https://docs.avalai.ir/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added)[جدید: GPT Image 2.5، DeepSeek V4.1 Flash و Grok 4.6با Flare یا Sunburst تصویر بسازید و ویرایش کنید و با DeepSeek V4.1 Flash یا Grok 4.6 عامل‌های استدلالی بسازید. تعرفه کم‌بار DeepSeek شبانه‌روزی است؛ پیش از تغییر مسیریابی V4-Pro در ۲۳ شهریور (2026-09-14) مهاجرت کنید.←](https://docs.avalai.ir/fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added)[پرچم‌دار جدید OpenAI: GPT-6 Astraاز ](https://docs.avalai.ir/fa/news/2026-09-05-gpt-6-astra-added)`gpt-6-astra`[ برای کارهای دشوار رایانه‌ای، مهندسی نرم‌افزار، حرفه‌ای، علمی، امنیت سایبری و زمینه بلند با پشتیبانی کامل Chat Completions، Messages و Responses استفاده کنید.←](https://docs.avalai.ir/fa/news/2026-09-05-gpt-6-astra-added)[پرچم‌دار جدید Anthropic: Claude Fable 5.1از ](https://docs.avalai.ir/fa/news/2026-09-02-claude-fable-5-1-added)`claude-fable-5-1`[ برای کدنویسی پیشرفته، پژوهش، کار دانشی و عامل‌های طولانی‌مدت با پنجره ورودی ۱M، تفکر تطبیقی همیشه‌فعال و هزینه کمتر خواندن از کش استفاده کنید.←](https://docs.avalai.ir/fa/news/2026-09-02-claude-fable-5-1-added)[مدل‌های جدید Alibaba: Qwen3.8-27B و Qwen3.8-Flashاز ](https://docs.avalai.ir/fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added)`qwen3.8-flash`[ برای گردش‌کارهای کم‌هزینه بینایی و عامل‌ها، یا از ](https://docs.avalai.ir/fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added)`qwen3.8-27b`[ برای استدلال بینایی-زبان متراکم و فشرده با کنترل انعطاف‌پذیر تفکر استفاده کنید.←](https://docs.avalai.ir/fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added)[پرچم‌دار جدید Z.AI: GLM-5.3-Flashاز ](https://docs.avalai.ir/fa/news/2026-08-26-glm-5-3-flash-added)`glm-5.3-flash`[ برای گردش‌کارهای چندوجهی کدنویسی و عامل‌ها با ۳۲۰B پارامتر کل، ۱۸B پارامتر فعال، پنجره ورودی ۹۹۱K و قیمت تشویقی تا ۱۸ شهریور ۱۴۰۵ استفاده کنید.←](https://docs.avalai.ir/fa/news/2026-08-26-glm-5-3-flash-added)[پرچم‌دار Z.AI: GLM-5.3گردش‌کارهای پیچیده کدنویسی و عامل‌های بلندمدت را با تفکر اجباری، سطح استدلال انتخابی و پنجره زمینه ۱ میلیون توکنی بسازید.←](https://docs.avalai.ir/fa/news/2026-08-18-glm-5-3-added)[مدل‌های جدید Alibaba: مدل وزن‌باز Qwen3.8 و Qwen Image 3از qwen3.8-2.4t-a95b برای workloadهای متنی با تفکر اجباری یا از qwen-image-3.0-pro و qwen-image-3.0 برای تولید و ویرایش تصویر استفاده کنید.←](https://docs.avalai.ir/fa/news/2026-08-15-qwen3-8-open-weight-and-qwen-image-3-added)[مدل جدید: Gemini 3.8 Flashعامل‌های کدنویسی بلندمدت و گردش‌کارهای مبتنی بر ابزار را با نرخ تشویقی تا ۱۰ دی ۱۴۰۵ (December 31, 2026) بسازید. نام مستعار ](https://docs.avalai.ir/fa/news/2026-09-03-gemini-3-8-flash-added)`gemini-flash-latest`[ اکنون به این مدل اشاره می‌کند.←](https://docs.avalai.ir/fa/news/2026-09-03-gemini-3-8-flash-added)[جدید: Muse Glimmer 30Bاز مدل چندوجهی و عاملی Meta روی Fireworks.ai برای reasoning، ابزار، کدنویسی و کار چندزبانه استفاده کنید.←](https://docs.avalai.ir/fa/models/muse-glimmer-30b)[جدید: Nemotron 3.5 Lightningاز مدل کارآمد NVIDIA با ۳۰B پارامتر کل و ۳B فعال برای reasoning، کدنویسی، RAG و عامل‌ها استفاده کنید.←](https://docs.avalai.ir/fa/models/nemotron-3.5-lightning)[بهبود چشمگیر مسیریابی cacheمسیریابی هر کاربر و مدل اکنون آخرین زیرساخت موفق را در یک بازه sticky و rolling پانزده‌دقیقه‌ای ترجیح می‌دهد.←](https://docs.avalai.ir/fa/guides/prompt-caching)[مرور مدل‌هاخانواده مدل، نوع ورودی و خروجی، طول زمینه و نقاط پایانی پشتیبانی‌شده را مقایسه کنید.←](https://docs.avalai.ir/fa/models/index)[بررسی قیمت‌گذاریپیش از انتخاب مدل برای محیط تولید، قیمت فعلی توکن و رسانه را ببینید.←](https://docs.avalai.ir/fa/pricing)
راهنماهای محبوب و کارهای رایج توسعه‌دهندگان
پس از یک درخواست موفق، رفتار قابل اتکای برنامه را پیاده‌سازی کنید.
[بازگرداندن داده ساختاریافتهپاسخ را به اسکیمایی محدود کنید که برنامه بتواند اعتبارسنجی کند.](https://docs.avalai.ir/fa/guides/structured-outputs)[فراخوانی توابع برنامهبه مدل اجازه درخواست ابزار بدهید و اجرای آن را در کد کنترل کنید.](https://docs.avalai.ir/fa/guides/function-calling)[پخش جریانی پاسخهم‌زمان با رسیدن رویدادهای پاسخ، خروجی مفید را نمایش دهید.](https://docs.avalai.ir/fa/guides/streaming-responses)[آماده‌سازی برای محیط تولیدامنیت، پایداری، تاخیر و هزینه را از قبل برنامه‌ریزی کنید.](https://docs.avalai.ir/fa/guides/production-best-practices)
پشتیبانی و وضعیت سرویس
برای حساب کاربری یا یکپارچه‌سازی خود کمک بگیرید یا بررسی کنید آیا رویداد فعالی روی درخواست‌ها اثر می‌گذارد.
[ایجاد تیکت پشتیبانیجزئیات درخواست و زمینه خطا را برای بررسی پشتیبانی ارسال کنید.↖](https://chat.avalai.ir/platform/support/create-ticket)[مشاهده وضعیت سرویسوضعیت فعلی سرویس‌ها و رخدادهای اخیر را بررسی کنید.↖](https://status.avalai.ir/)
[قبلیآخرین تغییرات](https://docs.avalai.ir/fa/news/)[بعدیشروع سریع](https://docs.avalai.ir/fa/quickstart)
در این صفحه
[اولین درخواست خود را ارسال کنید](https://docs.avalai.ir/fa/#first-request-title)[مسیر مناسب کار خود را انتخاب کنید](https://docs.avalai.ir/fa/#task-paths-title)[مدل مناسب و هزینه آن را پیدا کنید](https://docs.avalai.ir/fa/#models-pricing-title)[راهنماهای محبوب و کارهای رایج توسعه‌دهندگان](https://docs.avalai.ir/fa/#popular-guides-title)[پشتیبانی و وضعیت سرویس](https://docs.avalai.ir/fa/#support-status-title)
تنظیمات حریم خصوصی


این اولیش