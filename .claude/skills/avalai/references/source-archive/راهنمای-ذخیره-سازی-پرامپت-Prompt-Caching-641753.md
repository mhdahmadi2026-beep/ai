# راهنمای ذخیره‌سازی پرامپت (Prompt Caching)

با استفاده از کش کردن پرامپت، تاخیر و هزینه را کاهش دهید.

## فهرست مطالب

- [نمای کلی](#نمای-کلی)
- [ساختاردهی پرامپت‌ها برای کش شدن](#ساختاردهی-پرامپت‌ها-برای-کش-شدن)
- [نحوه عملکرد](#نحوه-عملکرد)
- [هزینه نوشتن کش و کنترل‌های بالادستی GPT-5.6](#هزینه-نوشتن-کش-و-کنترل‌های-بالادستی-gpt-56)
- [مسیریابی و ماندگاری کش پرامپت](#مسیریابی-و-ماندگاری-کش-پرامپت)
- [الگوهای Responses و Chat Completions](#الگوهای-responses-و-chat-completions)
- [الزامات](#الزامات)
- [اندازه‌گیری عملکرد کش](#اندازه‌گیری-عملکرد-کش)
- [چه چیزهایی می‌توانند کش شوند](#چه-چیزهایی-می‌توانند-کش-شوند)
- [بهترین شیوه‌ها](#بهترین-شیوه‌ها)
- [عیب‌یابی Cache Miss](#عیب‌یابی-cache-miss)
- [کش کردن زمینه Gemini](#کش-کردن-زمینه-gemini)
  - [کش ضمنی در مقابل کش صریح](#کش-ضمنی-در-مقابل-کش-صریح)
  - [وضعیت پشتیبانی AvalAI](#وضعیت-پشتیبانی-avalai)
  - [جزئیات کش ضمنی](#جزئیات-کش-ضمنی)
  - [بررسی Cache Hit در پاسخ‌های Gemini](#بررسی-cache-hit-در-پاسخ‌های-gemini)
  - [کش صریح (پشتیبانی نمی‌شود)](#کش-صریح-پشتیبانی-نمی‌شود)
- [سوالات متداول](#سوالات-متداول-بر-اساس-پیاده‌سازی-openai)
- [منابع مرتبط](#منابع-مرتبط)

## نمای کلی

پرامپت‌های مدل اغلب حاوی محتوای تکراری مانند پرامپت‌های سیستمی و دستورالعمل‌های رایج هستند. ارائه‌دهندگان مدل‌های زیربنایی (مانند OpenAI) ممکن است درخواست‌های API را به سرورهایی هدایت کنند که اخیرا همان پرامپت را پردازش کرده‌اند، که این امر باعث می‌شود پردازش پرامپت نسبت به پردازش از ابتدا، به طور بالقوه ارزان‌تر و سریع‌تر باشد. OpenAI کش کردن پرامپت را یک بهینه‌سازی خودکار معرفی می‌کند که در ترافیک واجد شرایط می‌تواند latency را تا ۸۰٪ و هزینه توکن ورودی را تا ۹۰٪ کاهش دهد؛ هنگام استفاده از AvalAI این اعداد را وابسته به provider/model بدانید و فیلدهای واقعی `usage` همان route را بررسی کنید. نوشتن کش برای مدل‌های OpenAI پیش از خانواده GPT-5.6 هزینه جداگانه ندارد. نوشتن کش در GPT-5.6 با نرخ ۱.۲۵ برابر ورودی عادی محاسبه می‌شود.

*توجه: در دسترس بودن و تخفیف‌های خاص به ارائه دهنده مدل زیربنایی و مدل خاص مورد استفاده بستگی دارد. لطفا برای جزئیات دقیق به مستندات ارائه دهنده مدل مراجعه کنید.*

در AvalAI، کش کردن پرامپت می‌تواند برای مدل‌های سازگار با OpenAI که رفتار کش سمت ارائه‌دهنده را expose می‌کنند اعمال شود؛ از جمله `gpt-5.6-sol`، `gpt-5.6-terra`، `gpt-5.6-luna`، `gpt-5.5`، `gpt-5.4`، `gpt-5.4-pro`، `gpt-5.2`، `gpt-5.1`، `gpt-5-mini`، `gpt-4.1`، `gpt-4o`، `o3` و `o4-mini`. در دسترس بودن، کنترل‌های request، رفتار ماندگاری و تخفیف همچنان به provider و route بستگی دارد؛ فیلدهای `usage` پاسخ همان درخواستی را بررسی کنید که واقعا ارسال می‌کنید.

این راهنما نحوه عملکرد کلی کش کردن پرامپت را شرح می‌دهد تا بتوانید پرامپت‌های خود را برای تاخیر و هزینه بالقوه کمتر بهینه‌سازی کنید.

## ساختاردهی پرامپت‌ها برای کش شدن

Cache hit (موفقیت در یافتن کش) معمولا فقط برای تطابق دقیق پیشوند (prefix) در یک پرامپت امکان‌پذیر است. برای به حداکثر رساندن مزایای بالقوه کش، محتوای ثابت مانند دستورالعمل‌ها و مثال‌ها را در ابتدای پرامپت خود قرار دهید و محتوای متغیر مانند اطلاعات خاص کاربر را در انتها قرار دهید. این اصل همچنین در مورد تصاویر و ابزارها صدق می‌کند، که معمولا باید بین درخواست‌ها یکسان باشند تا پیشوند مطابقت داشته باشد.

![Prompt Caching visualization](https://openaidevs.retool.com/api/file/8593d9bb-4edb-4eb6-bed9-62bfb98db5ee)
*(منبع تصویر: OpenAI)*

## نحوه عملکرد

کش کردن ممکن است به طور خودکار توسط ارائه‌دهنده مدل برای پرامپت‌هایی که از طول توکن مشخصی فراتر می‌روند فعال شود (برای OpenAI، ۱۰۲۴ توکن یا بیشتر). هنگامی که از طریق AvalAI به چنین مدلی درخواست API ارسال می‌کنید:

1. **مسیریابی کش (Cache Routing)**: ارائه‌دهنده درخواست را بر اساس hash پیشوند پرامپت مسیریابی می‌کند. OpenAI مستند می‌کند که این hash معمولا از ۲۵۶ توکن اول شروع می‌شود، هرچند طول دقیق می‌تواند بر اساس مدل فرق کند. وقتی پشتیبانی شود، `prompt_cache_key` با hash پیشوند ترکیب می‌شود تا locality کش برای ترافیک تکراری بهتر شود.
2. **جستجوی کش (Cache Lookup)**: ارائه‌دهنده بررسی می‌کند که آیا بخش اولیه (پیشوند) پرامپت شما روی ماشین انتخاب‌شده در کش وجود دارد یا خیر.
3. **Cache Hit**: اگر پیشوند منطبقی پیدا شود، ارائه‌دهنده پیشوند کش‌شده را reuse می‌کند. این کار می‌تواند تاخیر را کم کند و هزینه توکن‌های ورودی کش‌شده را کاهش دهد.
4. **Cache Miss**: اگر پیشوند منطبقی یافت نشود، ارائه‌دهنده کل پرامپت را پردازش می‌کند و ممکن است پیشوند را برای درخواست‌های آینده کش کند.

پیشوندهای کش‌شده معمولا برای دوره‌ای از عدم فعالیت فعال باقی می‌مانند، اما این زمان به ارائه‌دهنده و سیاست ماندگاری بستگی دارد. کش in-memory در OpenAI معمولا پس از ۵ تا ۱۰ دقیقه عدم فعالیت منقضی می‌شود و سقف آن حدود یک ساعت است؛ routeهای AvalAI وقتی ارائه‌دهنده زیربنایی OpenAI نباشد می‌توانند رفتار متفاوتی داشته باشند.

## هزینه نوشتن کش و کنترل‌های بالادستی GPT-5.6

GPT-5.6 مدل هزینه و کنترل کش در OpenAI را تغییر می‌دهد. OpenAI توکن‌های نوشته‌شده در کش را با نرخ ۱.۲۵ برابر ورودی عادی محاسبه می‌کند، تعداد توکن‌های نوشته‌شده را در `cache_write_tokens` و تعداد توکن‌های خوانده‌شده را در `cached_tokens` گزارش می‌دهد. رفتار پشتیبانی‌شده در AvalAI همچنان کش ضمنی خودکار است.

OpenAI برای استفاده مستقیم بالادستی از GPT-5.6 و خانواده‌های بعدی کنترل‌هایی مانند `prompt_cache_options`، `prompt_cache_options.ttl` و `prompt_cache_breakpoint` تعریف می‌کند. **AvalAI در حال حاضر از کش صریح یا breakpoint صریح کش پشتیبانی نمی‌کند.** این فیلدها را در درخواست‌های AvalAI ارسال نکنید و markerهای صریح مخصوص provider مانند `cache_control` را نیز حذف کنید.

کاتالوگ مدل AvalAI قابلیت prompt caching و قیمت نوشتن کش را برای routeهای GPT-5.6 تایید می‌کند، اما کنترل صریح کش را تایید نمی‌کند. از کش ضمنی خودکار استفاده کنید و نتیجه را با فیلدهای `usage` پاسخ بسنجید.

## مسیریابی و ماندگاری کش پرامپت

AvalAI یک تجمیع‌کننده است: یک شناسه عمومی مدل ممکن است توسط چند provider یا مجموعه زیرساخت سرو شود. در گذشته، دو درخواست منطبق می‌توانستند به زیرساخت‌های متفاوت برسند و در نتیجه نسبت به فراخوانی مستقیم یک provider، cache hit کمتری از کش ضمنی یا in-memory ارائه‌دهنده ایجاد کنند.

مسیریاب هوشمند اکنون مسیر موفق را برای ترکیب دقیق **هر کاربر، هر مدل و هر زیرساخت** نگه می‌دارد و **آخرین زیرساخت سالم و موفق** همان کاربر و مدل را ترجیح می‌دهد. این affinity تا **15 دقیقه پس از آخرین درخواست موفق** sticky می‌ماند و هر موفقیت، بازه 15 دقیقه‌ای را از نو تمدید می‌کند. این تغییر locality و cache hit را به‌شکل چشمگیری بهتر کرده است، اما رفتار همچنان **best effort است و تضمین نمی‌شود**؛ سلامت، ظرفیت، failover، دسترس‌پذیری مدل یا مسیریابی خود provider می‌تواند درخواست را جابه‌جا کند. بازه sticky فقط ترجیح routing است و عمر cache خود provider را افزایش یا تضمین نمی‌کند.

همگام‌سازی cache key کاربر و affinity مدل/زیرساخت به زمان نیاز دارد. برای `deepseek-v4-flash` مسیریابی در تست کنترل‌شده تقریبا آنی بود: یک بنچمارک paired در 2026-08-13 پس از **15 ثانیه** انتظار بعد از priming، به همان warm cache-hit ratio در endpoint رسمی DeepSeek رسید. با این حال زمان انتشار به مدل و زیرساخت وابسته است. اجرای اولیه `deepseek-v4-pro` پس از همین انتظار روی 0.0% ماند، اما اجرای بعدی کمی بعد به 99.9% در برابر 98.6% در DeepSeek رسید. عدد 15 ثانیه یک نتیجه مشاهده‌شده است، نه deadline عمومی برای فعال‌شدن affinity. برنامه شما باید در cache miss هم درست کار کند و نباید affinity کش را به‌عنوان state مکالمه استفاده کند.

برای ترافیک تکراری سازگار با OpenAI از طریق AvalAI، پیشوند را ثابت نگه دارید و در صورت پشتیبانی، برای workload، tenant یا پیکربندی assistant از `prompt_cache_key` ثابت استفاده کنید. کلیدی انتخاب نکنید که حجم زیادی از ترافیک را در یک bucket جمع کند: مستندات OpenAI توضیح می‌دهد که اگر ترکیب یک پیشوند و cache key از حدود ۱۵ درخواست در دقیقه بیشتر شود، بخشی از درخواست‌ها ممکن است به ماشین‌های دیگر overflow شوند و اثر کش کمتر شود.

با `prompt_cache_key` مثل یک برچسب مسیریابی رفتار کنید، نه داده کاربر. bucketهای opaque مانند `support-policy-v3`، `tenant-acme-chat-v2` یا `invoice-extractor-schema-v1` را ترجیح دهید. ایمیل، شماره تلفن، شناسه کاربر، شناسه ticket، کلید API یا secret خام را در key قرار ندهید؛ شناسه‌های مخصوص هر درخواست را نزدیک انتهای prompt بگذارید تا پیشوند مشترک را خراب نکنند.

کنترل retention بر اساس نسل مدل فرق می‌کند. برای GPT-5.6 و خانواده‌های بعدی از `prompt_cache_options.ttl` استفاده کنید؛ `prompt_cache_retention` برای این مدل‌ها deprecated است. برای مدل‌های پیش از GPT-5.6، `prompt_cache_retention` در صورت پشتیبانی همان سیاست حداکثر ماندگاری است. مثال `gpt-5.5` زیر عمدا یک نمونه legacy برای retention است.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are the BrightCart support assistant. Follow the fixed policy below...",
    input="Draft a two-sentence reply for ticket ORDER-8831.",
    prompt_cache_key="brightcart-support-policy-v1",
    prompt_cache_retention="24h",
)

cached = response.usage.input_tokens_details.cached_tokens
print(f"cached prompt tokens: {cached}")
print(response.output_text)
```

از `prompt_cache_retention="24h"` فقط برای مدل‌ها و ارائه‌دهندگانی استفاده کنید که ماندگاری extended را پشتیبانی می‌کنند. OpenAI برای بسیاری از مدل‌های قابل cache ماندگاری کوتاه in-memory را مستند می‌کند (معمولا ۵ تا ۱۰ دقیقه عدم فعالیت، با سقف حدود یک ساعت) و برای مدل‌های پشتیبانی‌شده ماندگاری extended تا ۲۴ ساعت را ارائه می‌دهد. OpenAI همچنین مستند می‌کند که قیمت‌گذاری prompt cache برای ماندگاری in-memory و extended یکسان است؛ در AvalAI همچنان قیمت و فیلدهای usage همان route/model انتخابی را بررسی کنید. اگر provider یا مدل این پارامتر را از طریق AvalAI expose نمی‌کند، آن را حذف کنید و به کش خودکار in-memory تکیه کنید.

ماندگاری extended همچنان یک ویژگی performance است، نه state برنامه. OpenAI مستند می‌کند که extended caching ممکن است key/value tensorهای مشتق‌شده از محتوای مشتری را در storage محلی GPU نگه دارد، نه پاسخ نهایی؛ بیشتر استفاده‌ها پس از ۱ تا ۲ ساعت منقضی می‌شوند و سقف ماندگاری ۲۴ ساعت است. رفتار دقیق حریم خصوصی، residency و retention هنگام استفاده از AvalAI همچنان به provider و route وابسته است.

OpenAI در حال حاضر ماندگاری extended prompt cache را برای این خانواده مدل‌ها فهرست می‌کند: `gpt-5.5`، `gpt-5.5-pro`، `gpt-5.4`، `gpt-5.2`، `gpt-5.1-codex-max`، `gpt-5.1`، `gpt-5.1-codex`، `gpt-5.1-codex-mini`، `gpt-5.1-chat-latest`، `gpt-5`، `gpt-5-codex` و `gpt-4.1`. این را یک فهرست قابلیت upstream بدانید، نه تضمین AvalAI؛ پشتیبانی AvalAI به route، حساب و alias دقیق مدلی که فراخوانی می‌کنید وابسته است.

پیش از تنظیم این پارامتر، این چک‌لیست retention را اجرا کنید:

- برای مدل‌های پیش از GPT-5.6 مانند `gpt-5.5` که extended caching را از طریق AvalAI expose می‌کنند، فقط وقتی AvalAI پارامتر را عبور می‌دهد از `prompt_cache_retention="24h"` استفاده کنید. این پشتیبانی را برای GPT-5.6 یا خانواده‌های بعدی فرض نکنید؛ آن مدل‌ها به‌جای آن از `prompt_cache_options.ttl` استفاده می‌کنند.
- برای مدل‌های قدیمی‌تر OpenAI که هم `in_memory` و هم `24h` را پشتیبانی می‌کنند، بر اساس نیازمندی retention داده خودتان آگاهانه انتخاب کنید و به defaultها تکیه نکنید، چون defaultها هنگام فعال بودن Zero Data Retention می‌توانند متفاوت باشند.
- برای Zero Data Retention، residency یا workloadهای regulated، تا وقتی route و policy دقیق provider را تأیید نکرده‌اید، حذف پارامترهای retention را ترجیح دهید.
- هیچ‌وقت prompt caching را جایگزین ذخیره state مکالمه یا رکوردهای کسب‌وکار در دیتابیس برنامه خودتان نکنید.

## الگوهای Responses و Chat Completions

برای اپلیکیشن‌های جدید AvalAI، API پاسخ‌ها (Responses API) را ترجیح دهید، چون با workflowهای stateful، چندوجهی و ابزارمحور هماهنگ‌تر است. برای اپلیکیشن‌های موجود `v1/chat/completions`، اگر migration پرریسک است همان route را نگه دارید؛ همان اصول caching وقتی اعمال می‌شود که prefix طولانی سیستم/developer، schema ابزارها، ترتیب تصاویر و schema خروجی ساختاریافته ثابت بمانند.

هنگام مهاجرت یک workload کش‌شده از Chat Completions به `v1/responses`، prefix ثابت را حفظ کنید و فقط شکل endpoint را تغییر دهید:

- دستورالعمل‌های سیستمی طولانی و مشترک را در `instructions` یا اولین آیتم ثابت input قرار دهید.
- متن پویا کاربر، snippetهای retrieval، timestampها و request IDها را نزدیک انتها نگه دارید.
- برای همان assistant، tenant، policy یا schema از همان bucket در `prompt_cache_key` استفاده کنید.
- برای Responses مقدار `usage.input_tokens_details.cached_tokens` و برای Chat Completions مقدار `usage.prompt_tokens_details.cached_tokens` را بررسی کنید؛ cache hit نشانه بهینه‌سازی است، نه نشانه correctness.

```python
# Responses API — گزینه پیشنهادی برای کارهای جدید AvalAI
response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are the BrightCart support assistant. Follow the fixed policy below...",
    input="Draft a two-sentence reply for ticket ORDER-8831.",
    prompt_cache_key="brightcart-support-policy-v1",
    prompt_cache_retention="24h",
)
print(response.usage.input_tokens_details.cached_tokens)
```

```python
# Chat Completions API — برای اپلیکیشن‌های موجود نگه دارید
chat_response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "system",
            "content": "You are the BrightCart support assistant. Follow the fixed policy below...",
        },
        {
            "role": "user",
            "content": "Draft a two-sentence reply for ticket ORDER-8831.",
        },
    ],
    prompt_cache_key="brightcart-support-policy-v1",
    prompt_cache_retention="24h",
)
print(chat_response.usage.prompt_tokens_details.cached_tokens)
```

## الزامات

در دسترس بودن و رفتار کش به provider و مدل بستگی دارد. درخواست زیر حداقل لازم بدون خطا به‌طور عادی پردازش می‌شود، اما cache read رخ نمی‌دهد.

| provider یا خانواده مدل | حداقل توکن ورودی |
| --- | ---: |
| OpenAI | 1,024 |
| Anthropic Claude 3.x | 1,024 |
| Anthropic Claude Sonnet/Opus 4.x | 2,048 |
| Anthropic Claude Haiku 4.5+ و Opus 4.5+ | 4,096 |
| Bedrock Claude 3.5/3.7 | 1,024 |
| Bedrock Claude Sonnet 4.x | 2,048 |
| کش ضمنی Google Gemini | 1,024 |

آستانه خانواده Anthropic با release و route دقیق تغییر می‌کند. نمونه‌های فعلی شامل ۵۱۲ توکن برای Claude Opus 5، Fable 5 و Mythos 5؛ ۱٬۰۲۴ برای Claude Opus 4.8، Sonnet 5، Sonnet 4.6/4.5/4 و Opus 4.1/4؛ ۲٬۰۴۸ برای Claude Mythos Preview، Opus 4.7 و Haiku 3.5؛ و ۴٬۰۹۶ برای Claude Opus 4.6/4.5 و Haiku 4.5 است. به‌جای تعمیم یک آستانه به همه aliasها، مستندات مدل route انتخابی را بررسی کنید.

برخی از پاسخ‌های API شامل جزئیاتی درباره توکن‌های کش‌شده در آبجکت `usage` هستند:

```json
{
  "usage": {
    "prompt_tokens": 2006,
    "completion_tokens": 300,
    "total_tokens": 2306,
    "prompt_tokens_details": {
      "cached_tokens": 1920,
      "cache_write_tokens": 0
    },
    "completion_tokens_details": {
      "reasoning_tokens": 0
    }
  }
}
```

در این مثال، `1920` توکن prompt از cache خوانده شده و هیچ توکنی در cache نوشته نشده است. برای GPT-5.6 و خانواده‌های بعدی، وقتی route انتخابی این فیلد را expose کند، `cache_write_tokens` تعداد توکن‌های نوشته‌شده را نشان می‌دهد.

برای فراخوانی‌های Responses API، همین مفهوم زیر `usage.input_tokens_details.cached_tokens` دیده می‌شود. برای Chat Completions مقدار `usage.prompt_tokens_details.cached_tokens` را در پاسخ chat بررسی کنید. APIهای native provider مانند Gemini ممکن است نام‌های متفاوتی داشته باشند.

### بنچمارک مسیریابی بهتر cache

در 2026-08-13 یک بنچمارک streaming و paired، prefix تولیدشده با byteهای یکسان و generation seed مشترک را به AvalAI و endpoint رسمی DeepSeek فرستاد. هر دو route priming شدند، **15 ثانیه** صبر انجام شد و سپس 10 round ترتیبی با `deepseek-v4-flash` اجرا شد:

```bash
python -m tests.benchmarks.test_cache_hit_ratio \
  --model deepseek-v4-flash \
  --rounds 10 \
  --prefix-tokens 2000
```

| معیار | AvalAI | DeepSeek رسمی |
| --- | ---: | ---: |
| round 1 | 0/1,948 cacheشده (0.0%) | 1,920/1,948 cacheشده (98.6%) |
| میانگین warm در rounds 2–10 | **98.6%** | **98.6%** |
| اختلاف warm cache | **+0.0 percentage points** | مبنا |
| درخواست موفق | 10/10 | 10/10 |

اولین hit در AvalAI در round 2 و 2.683 ثانیه پس از شروع roundهای اندازه‌گیری‌شده ثبت شد. DeepSeek با وجود prefix تصادفی و یکتا در round 1 یک hit گزارش کرد؛ بنابراین پاسخ اول آن مدرک یک cold miss رسمی و تمیز نیست. مقایسه قابل اتکا rounds 2–10 است که در آن هر دو endpoint برای هر prompt با 1,948 توکن، 1,920 توکن cacheشده برگرداندند.

این اجرای تک‌مدل پیشرفت مسیریابی تقریبا آنی را پس از انتظار اندازه‌گیری‌شده 15 ثانیه‌ای نشان می‌دهد؛ اما همگام‌سازی بدون delay یا hit rate برابر 98.6% را تضمین نمی‌کند. یک تست جداگانه `deepseek-v4-pro` ابتدا 0.0% warm hit در AvalAI داشت و اجرای بعدی به 99.9% رسید؛ یعنی شکل‌گیری اولیه affinity برای بعضی مدل‌ها یا زیرساخت‌ها می‌تواند بیشتر طول بکشد. پس از شکل‌گیری، routeهای موفق بازه sticky و rolling پانزده‌دقیقه‌ای را تمدید می‌کنند. نتیجه با prompt دقیق، مدل، provider، بار و وضعیت routing تغییر می‌کند. روش کامل، نمودارها، نتیجه latency/TTFT و محدودیت‌ها در صفحه [عملکرد AvalAI](/fa/performance.md) آمده است.

## اندازه‌گیری عملکرد کش

Prompt caching را یک بهینه‌سازی قابل مشاهده بدانید. پیش و پس از بازچینی promptها، metricهای سبک اضافه کنید:

```text
cache_hit_ratio = cached_tokens / input_or_prompt_tokens
uncached_tokens = input_or_prompt_tokens - cached_tokens
```

این فیلدها را بر اساس route، مدل، `prompt_cache_key` و نسخه پایدار prompt ثبت کنید:

- توکن‌های ورودی/prompt، `cached_tokens`، در صورت بازگشت `cache_write_tokens`، توکن‌های خروجی، توکن‌های کل، latency p50/p95 و تعداد درخواست.
- نسبت cache hit برای درخواست دوم و درخواست‌های بعدی در workload تکراری؛ درخواست اول معمولا warm-up miss است.
- نرخ خطا یا fallback وقتی route انتخابی `prompt_cache_retention` را به‌دلیل پشتیبانی نکردن از extended retention رد می‌کند.

برای ترافیک GPT-5.6 هزینه read و write را جداگانه محاسبه کنید. cache write فقط وقتی به‌صرفه است که readهای تخفیف‌دار بعدی هزینه بیشتر write را جبران کنند. به جای اینکه هر مقدار غیرصفر را صرفه‌جویی بدانید، `cache_write_tokens` درخواست‌های warm-up را با `cached_tokens` درخواست‌های بعدی مقایسه کنید.

از این metricها برای تصمیم درباره split یا rotate کردن bucketهای cache استفاده کنید. یک `prompt_cache_key` مشترک می‌تواند locality را برای prefixهای مشترک بهتر کند، اما اگر یک key ترافیک بسیار متنوع یا زیاد را مخلوط کند، routing ارائه‌دهنده ممکن است overflow شود و hit rate افت کند. بررسی correctness را جدا نگه دارید: توکن‌های cacheشده می‌توانند هزینه و latency را کم کنند، اما کل prompt همچنان می‌تواند در rate limit حساب شود و پاسخ هر بار تازه تولید می‌شود.

## چه چیزهایی می‌توانند کش شوند

محتوای زیر، در صورت پشتیبانی provider، می‌تواند بخشی از پیشوند دقیق قابل cache باشد:

* **تعریف ابزارها** و ترتیب ثابت آن‌ها.
* **پیام‌های system** و متن طولانی policy.
* **بلوک‌های متن در پیام‌ها**.
* **تصاویر و اسناد کاربر** با bytes، ترتیب و تنظیمات detail یکسان.
* **بلوک‌های tool-use و tool-result** از نوبت‌های قبلی.
* **بلوک‌های thinking قبلی دستیار** فقط وقتی همراه محتوای قابل cache نوبت‌های قبلی replay شوند؛ بلوک thinking را نمی‌توان مستقیما با `cache_control` علامت‌گذاری کرد.

زیر‌بلوک citation را نمی‌توان مستقیم cache کرد؛ بلوک document سطح بالا را cache کنید. بلوک متن خالی قابل cache نیست. marker صریح `cache_control` در AvalAI پشتیبانی نمی‌شود.

### سلسله‌مراتب باطل‌شدن کش

باطل‌شدن کش از سلسله‌مراتب `tools → system → messages` پیروی می‌کند:

- تغییر تعریف ابزارها، tools، system و messages را باطل می‌کند.
- تغییر web search، citation یا speed mode می‌تواند system و messages را باطل کند.
- تغییر `tool_choice`، تصاویر و بسیاری از کنترل‌های thinking/effort، messages را باطل می‌کند.
- باطل‌شدن tools یا system به‌دلیل تنظیمات thinking می‌تواند مختص مدل باشد.

## بهترین شیوه‌ها

*   پرامپت‌ها را با محتوای ثابت در ابتدا و محتوای پویا در انتها ساختاردهی کنید.
*   جزئیات `usage` پاسخ API را برای `cached_tokens`، latency و cache-hit rate مانیتور کنید.
*   برای پیشوندهای تکراری از `prompt_cache_key` ثابت استفاده کنید، اما granularity را طوری انتخاب کنید که زیر محدودیت‌های مسیریابی provider بماند.
*   تعریف ابزارها، ترتیب تصاویر، schema خروجی ساختاریافته و متن policy طولانی را بین درخواست‌ها ثابت نگه دارید.
*   timestampها، user IDها، snippetهای بازیابی‌شده و facts مخصوص هر درخواست را نزدیک انتها بگذارید تا پیشوند مشترک را خراب نکنند.
*   کش را یک بهینه‌سازی بدانید، نه ویژگی correctness؛ برنامه شما باید حتی در cache miss هم درست کار کند.

## عیب‌یابی Cache Miss

اگر `cached_tokens` برای ترافیکی که باید تکراری باشد همچنان `0` می‌ماند، قبل از تغییر مدل این موارد را بررسی کنید:

| نشانه | علت محتمل | راه‌حل |
| --- | --- | --- |
| پرامپت‌های کوتاه هرگز cache نمی‌شوند | درخواست زیر حداقل طول cacheable ارائه‌دهنده است | instruction، schema یا context مرجع ثابت را ترکیب کنید تا prefix تکراری به اندازه کافی بلند شود. |
| پرامپت‌های طولانی بعد از هر درخواست miss می‌شوند | مقدارهای پویا خیلی زود در prompt آمده‌اند | متن مخصوص کاربر، timestamp، snippetهای retrieval و request ID را بعد از prefix ثابت قرار دهید. |
| درخواست‌های tool-heavy به شکل غیرمنتظره miss می‌شوند | schema یا ترتیب ابزارها تغییر کرده است | نام ابزار، description، schema و ترتیب ابزارها را بین درخواست‌ها ثابت نگه دارید. |
| درخواست‌های تصویری miss می‌شوند | ترتیب تصویر، URL/bytes base64 یا مقدار `detail` تغییر کرده است | برای prefix مشترک از همان representation تصویر و همان مقدار `detail` استفاده کنید. |
| hit rate زیر بار افت می‌کند | یک `prompt_cache_key` ترافیک خیلی زیادی را در یک bucket جمع کرده است | کلیدها را بر اساس assistant، tenant یا workload جدا کنید تا هر ترکیب prefix/key در محدوده منطقی بماند. |
| فقط یک provider miss می‌دهد | route/model انتخابی جزئیات caching را از طریق AvalAI expose نمی‌کند | صفحه provider را بررسی کنید، پارامترهای retention پشتیبانی‌نشده را حذف کنید و به رفتار عادی درخواست تکیه کنید. |
| hit rate در AvalAI به‌طور معنادار از استفاده مستقیم provider کمتر است | affinity هنوز در حال انتشار است، failover درخواست را جابه‌جا کرده یا provider رفتار کش متفاوتی دارد | پس از بازه انتشار دوباره آزمایش کنید، مدل، زمان درخواست‌ها و `usage` را ثبت کنید و سپس [ایجاد تیکت پشتیبانی](https://chat.avalai.ir/platform/support/create-ticket) را انجام دهید. |

برای پاسخ‌های سبک Anthropic، هر دو فیلد `cache_creation_input_tokens` و `cache_read_input_tokens` را بررسی کنید. اگر هر دو صفر باشند، در آن درخواست caching رخ نداده است.

## کش کردن زمینه Gemini

مدل‌های Gemini مکانیزم کش زمینه مخصوص خود را با دو نوع متمایز دارند: **کش ضمنی (Implicit Caching)** و **کش صریح (Explicit Caching)**.

### کش ضمنی در مقابل کش صریح

| ویژگی | کش ضمنی | کش صریح |
|-------|---------|---------|
| **فعال‌سازی** | خودکار | دستی (کنترل توسط توسعه‌دهنده) |
| **صرفه‌جویی در هزینه** | تضمین نشده | تضمین شده |
| **تنظیمات مورد نیاز** | هیچ | ایجاد/مدیریت محتوای کش شده |
| **کنترل TTL** | خیر | بله (قابل تنظیم) |
| **پشتیبانی AvalAI** | ⚠️ ممکن اما تضمین نشده | ❌ در حال حاضر پشتیبانی نمی‌شود |

### وضعیت پشتیبانی AvalAI

> **مهم**: مسیریاب هوشمند AvalAI اکنون آخرین route سالم و موفق را برای هر کاربر، مدل و زیرساخت تا 15 دقیقه پس از آخرین درخواست موفق نگه می‌دارد و هر موفقیت این بازه sticky را تمدید می‌کند. این تغییر locality را به‌شکل چشمگیری بهتر کرده است، اما best effort است و failover یا ظرفیت همچنان می‌تواند درخواست را جابه‌جا کند.

| نوع کش | وضعیت | توضیحات |
|--------|-------|---------|
| **کش ضمنی** | ⚠️ best effort | ترجیح rolling ده‌دقیقه‌ای آخرین زیرساخت موفق |
| **کش صریح** | ❌ پشتیبانی نمی‌شود | ممکن است در به‌روزرسانی‌های آینده اضافه شود |

### جزئیات کش ضمنی

کش ضمنی به طور پیش‌فرض در مدل‌های Gemini فعال است. هنگامی که درخواست شما به کش برخورد کند، Google به طور خودکار صرفه‌جویی در هزینه را اعمال می‌کند.

#### حداقل الزامات توکن برای Gemini

| مدل | حداقل تعداد توکن |
|-----|------------------|
| Gemini 3 Flash Preview | ۱،۰۲۴ توکن |
| Gemini 3 Pro Preview | ۴،۰۹۶ توکن |
| Gemini 2.5 Flash | ۱،۰۲۴ توکن |
| Gemini 2.5 Pro | ۴،۰۹۶ توکن |

#### نکاتی برای افزایش احتمال Cache Hit

1. **محتوای بزرگ و ثابت را در ابتدای پرامپت قرار دهید**
   - دستورالعمل‌های سیستمی
   - اسناد مرجع
   - مثال‌های Few-shot

2. **درخواست‌های مشابه را در فاصله زمانی کوتاه ارسال کنید**
   - درخواست‌هایی با همان پیشوند که نزدیک به هم ارسال می‌شوند احتمال cache hit بالاتری دارند

3. **محتوای پویا را در انتها نگه دارید**
   - اطلاعات خاص کاربر
   - پرسش‌های متغیر
   - برچسب‌های زمانی و شناسه‌های یکتا

### بررسی Cache Hit در پاسخ‌های Gemini

هنگام استفاده از API بومی Gemini، می‌توانید cache hitها را در پاسخ بررسی کنید:

<!-- tabs:start -->
#### **Python**

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["AVALAI_API_KEY"],
    http_options={"base_url": "https://api.avalai.ir"},
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="پرامپت شما با زمینه قابل توجه..."
)

# بررسی متادیتای استفاده برای اطلاعات کش
if hasattr(response, "usage_metadata"):
    usage = response.usage_metadata
    print(f"توکن‌های پرامپت: {usage.prompt_token_count}")
    print(f"توکن‌های کش شده: {getattr(usage, 'cached_content_token_count', 0)}")
    print(f"توکن‌های خروجی: {usage.candidates_token_count}")
```

#### **JavaScript**

```javascript
import { GoogleGenAI } from "@google/genai";

const client = new GoogleGenAI({
  apiKey: process.env.AVALAI_API_KEY,
  httpOptions: { baseUrl: "https://api.avalai.ir" }
});

const response = await client.models.generateContent({
  model: "gemini-2.5-flash",
  contents: "پرامپت شما با زمینه قابل توجه..."
});

// بررسی متادیتای استفاده برای اطلاعات کش
if (response.usageMetadata) {
  console.log(`توکن‌های پرامپت: ${response.usageMetadata.promptTokenCount}`);
  console.log(`توکن‌های کش شده: ${response.usageMetadata.cachedContentTokenCount || 0}`);
  console.log(`توکن‌های خروجی: ${response.usageMetadata.candidatesTokenCount}`);
}
```

#### **cURL**

```bash
curl -X POST "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "parts": [{"text": "پرامپت شما با زمینه قابل توجه..."}]
    }]
  }'

# پاسخ شامل usage_metadata با تعداد توکن‌های کش شده خواهد بود
```
<!-- tabs:end -->

### کش صریح (پشتیبانی نمی‌شود)

کش صریح به شما امکان می‌دهد محتوا را به صورت دستی کش کنید و در درخواست‌های بعدی با استفاده از `cachedContent` به آن ارجاع دهید. این روش صرفه‌جویی در هزینه را تضمین می‌کند اما نیاز به تنظیمات اضافی دارد.

> **توجه**: endpointهای کش صریح (`/cachedContents`) در حال حاضر در AvalAI پشتیبانی نمی‌شوند. ممکن است در به‌روزرسانی‌های آینده پشتیبانی اضافه شود.

#### چرا کش صریح پشتیبانی نمی‌شود

به عنوان یک تجمیع‌کننده API، AvalAI درخواست‌ها را در چندین زیرساخت برای اطمینان و عملکرد توزیع می‌کند. کش صریح نیاز دارد به:

- ذخیره‌سازی پایدار متصل به زیرساخت خاص
- هدایت ثابت همه درخواست‌های مرتبط به همان سرورها
- مدیریت مستقیم چرخه حیات کش

این الزامات با معماری توزیع شده AvalAI در تضاد هستند.

#### موارد استفاده مناسب برای کش کردن

کش کردن زمینه به ویژه برای موارد زیر مفید است:

1. **چت‌بات‌ها با دستورالعمل‌های سیستمی گسترده** - تعریف شخصیت بزرگ، پایگاه دانش شرکت
2. **برنامه‌های تحلیل اسناد** - پرسش‌های تکراری از همان اسناد
3. **ابزارهای تحلیل کد** - تحلیل مخزن، رفع اشکال در کدبیس‌های مشابه
4. **تحلیل ویدیو/صوت** - سوالات متعدد درباره همان فایل رسانه‌ای

## سوالات متداول (بر اساس پیاده‌سازی OpenAI)

1.  **حریم خصوصی داده‌ها برای کش‌ها چگونه حفظ می‌شود؟**
    کش‌های پرامپت معمولا بین سازمان‌ها به اشتراک گذاشته نمی‌شوند. فقط اعضای همان سازمان می‌توانند از کش‌های پرامپت‌های یکسان ارسال شده توسط آن سازمان بهره‌مند شوند. AvalAI به عنوان یک پروکسی عمل می‌کند، بنابراین مزایای کش به نحوه مدیریت درخواست‌ها توسط ارائه دهنده زیربنایی از زیرساخت AvalAI یا به طور بالقوه سازمان خاص شما (در صورت استفاده از ویژگی‌های قابل اعمال ارائه دهنده) بستگی دارد.
2.  **آیا کش کردن پرامپت بر پاسخ نهایی تاثیر می‌گذارد؟**
    خیر. کش کردن پرامپت نباید بر تولید توکن‌های خروجی یا پاسخ نهایی تاثیر بگذارد. فقط پردازش پرامپت به طور بالقوه بهینه می‌شود؛ پاسخ هر بار بر اساس پرامپت کامل (که ممکن است بخشی از آن کش شده باشد) دوباره محاسبه می‌شود.
3.  **آیا راهی برای پاک کردن دستی کش وجود دارد؟**
    پاک کردن دستی کش معمولا در دسترس نیست. کش‌ها معمولا پس از دوره‌های عدم فعالیت به طور خودکار پاک می‌شوند.
4.  **آیا هزینه اضافی برای کش کردن پرامپت وجود دارد؟**
    نوشتن cache برای مدل‌های OpenAI پیش از GPT-5.6 هزینه جداگانه ندارد. در GPT-5.6 و خانواده‌های بعدی، cache write با نرخ ۱.۲۵ برابر ورودی عادی محاسبه می‌شود و readهای بعدی از نرخ تخفیف‌دار ورودی کش‌شده استفاده می‌کنند. پیش از ادعای صرفه‌جویی خالص، هم `cache_write_tokens` و هم `cached_tokens` را بررسی کنید.
5.  **آیا پرامپت‌های کش شده به محدودیت‌های نرخ TPM کمک می‌کنند؟**
    بله، توکن‌های کامل پرامپت (کش شده + غیر کش شده) معمولا در محدودیت‌های نرخ مانند توکن در دقیقه (TPM) محاسبه می‌شوند. کش کردن بر هزینه و تاخیر تاثیر می‌گذارد، نه محاسبه محدودیت نرخ.
6.  **آیا تخفیف برای کش کردن پرامپت در همه جا در دسترس است؟**
    در دسترس بودن به ارائه دهنده و سطوح خدمات خاص بستگی دارد (به عنوان مثال، OpenAI آن را در APIهای استاندارد و Scale Tier ارائه می‌دهد، اما نه در Batch API).
7.  **آیا کش کردن پرامپت با درخواست‌های Zero Data Retention (ZDR) کار می‌کند؟**
    رفتار ارائه‌دهنده به مدل و حالت نگه‌داری cache وابسته است. OpenAI نگه‌داری cache در حافظه و extended را جداگانه مستند می‌کند؛ در AvalAI پیش از وعده دادن تضمین شبیه ZDR، route انتخابی را تأیید کنید.
8.  **آیا کش کردن پرامپت روی data residency اثر دارد؟**
    residency را وابسته به provider و route بدانید. OpenAI مستند می‌کند که in-memory caching داده prompt را روی disk ذخیره نمی‌کند و extended caching هنگام استفاده از regional inference باید در همان region بماند. در AvalAI پیش از تعهد residency به مشتری، route، region و رفتار retention ارائه‌دهنده انتخابی را بررسی کنید.
9.  **آیا `prompt_cache_key` باید کاربران فردی را شناسایی کند؟**
    معمولا نه. از bucketهای پایدار و opaque برای workload، tenant، assistant، policy یا schema استفاده کنید و شناسه‌های شخصی خام را بیرون از cache key نگه دارید. هر وقت policy طولانی‌مدت، schema ابزار یا prefix prompt تغییر کرد، key را rotate کنید.
10.  **آیا می‌توانم برای correctness یا continuity به prompt cache تکیه کنم؟**
    خیر. Cache hit فقط پردازش prompt تکراری را بهینه می‌کند. جایگزین ارسال context کامل موردنیاز نیست، state مکالمه برنامه شما را نگه نمی‌دارد و توکن‌های prompt کش‌شده همچنان می‌توانند در محدودیت TPM حساب شوند.

## منابع مرتبط

*   [راهنمای انتخاب مدل](fa/guides/model-selection.md)
*   [بهینه‌سازی تاخیر](fa/guides/latency-optimization.md)
*   [کنترل داده‌ها](fa/guides/data-controls.md)
*   [قیمت‌گذاری](fa/pricing.md)
*   [مدل‌های OpenAI](fa/providers/openai.md)
*   [مدل‌های Google](fa/providers/google.md)
*   [SDK بومی GenAI (v1beta)](fa/api-reference/v1beta.md)
*   [راهنمای رسمی Prompt Caching در OpenAI](https://developers.openai.com/api/docs/guides/prompt-caching)

> این راهنما با اقتباس از [OpenAI Cookbook رسمی](https://developers.openai.com/cookbook/) و مخزن [openai/openai-cookbook](https://github.com/openai/openai-cookbook)، با تغییرات endpoint، کلید API، مدل و مرزهای پشتیبانی AvalAI تهیه شده است.
