---
hasH1: true
---

# مدل‌های گوگل

AvalAI دسترسی یکپارچه به مدل‌های Gemini گوگل را از طریق API یکپارچه ما فراهم می‌کند. این صفحه جزئیات مدل‌های موجود گوگل، قابلیت‌های آن‌ها و موارد استفاده بهینه را با تمرکز بر آخرین نسل‌ها شرح می‌دهد.

> **دو روش برای استفاده از مدل‌های Gemini**: می‌توانید به مدل‌های Gemini از طریق API سازگار با OpenAI (با استفاده از کتابخانه‌های کلاینت OpenAI) یا SDK بومی GenAI گوگل دسترسی پیدا کنید. برای نمونه‌های SDK بومی و ویژگی‌های پیشرفته، [پشتیبانی از SDK بومی Google GenAI](#پشتیبانی-از-sdk-بومی-google-genai) را ببینید.

## مدل‌های Gemini موجود

خانواده Gemini گوگل طیف وسیعی از مدل‌ها را ارائه می‌دهد که عملکرد، هزینه و ویژگی‌ها را متعادل می‌کنند، از جمله پنجره‌های زمینه بسیار بزرگ و قابلیت‌های چندوجهی پیشرفته.

### Gemini 3.8 Flash

Gemini 3.8 Flash (`gemini-3.8-flash`) جدیدترین مدل Flash گوگل برای کدنویسی بلندمدت، عامل‌های خودکار، استدلال چندمرحله‌ای و گردش‌کارهای مبتنی بر ابزار است. گوگل در مقایسه با Gemini 3.7 Flash، بهبودهایی را در مهندسی نرم‌افزار، وظایف عاملی، استدلال دقیق و کارهای تخصصی حرفه‌ای گزارش کرده است؛ در عین حال، مدل سرعت رده Flash را حفظ می‌کند.

| ویژگی | جزئیات |
|--------|---------|
| ورودی تشویقی | $0.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| ورودی ذخیره‌شده تشویقی | $0.075 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| خروجی تشویقی | $3.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| قیمت استاندارد | ورودی $1.50، ورودی ذخیره‌شده $0.15 و خروجی $7.50 / ۱ میلیون توکن پس از ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| نقاط پایانی پشتیبانی‌شده | `v1beta/`، `v1/chat/completions`، `v1/messages` و پشتیبانی جزئی `v1/responses` |
| نقاط قوت | کدنویسی بلندمدت، عامل‌های خودکار، استدلال چندمرحله‌ای و استفاده تکرارشونده از ابزار |
| نام مستعار جدید | `gemini-flash-latest` به `gemini-3.8-flash` اشاره می‌کند |

**قابلیت‌های کلیدی:**

- **کدنویسی و مهندسی نرم‌افزار**: انجام پیاده‌سازی، اشکال‌زدایی و وظایف طولانی در سطح مخزن کد
- **گردش‌کارهای خودکار**: برنامه‌ریزی و تکمیل کارهای چندمرحله‌ای با فراخوانی تکرارشونده ابزار
- **استدلال پیشرفته**: عملکرد بهتر در مسائل دقیق چندمرحله‌ای و وظایف تخصصی حرفه‌ای
- **تلاش قابل تنظیم**: ایجاد تعادل میان کیفیت وظایف دشوار، مصرف توکن و تأخیر

```python
response = client.chat.completions.create(
    model="gemini-3.8-flash",
    messages=[
        {
            "role": "user",
            "content": "این شکست استقرار را عیب‌یابی کن و یک برنامه اصلاح مرحله‌ای با معیارهای بازگشت ارائه بده.",
        }
    ],
)

print(response.choices[0].message.content)
```

برای نمونه نقاط پایانی، نکات برجسته بنچمارک به گزارش گوگل، قیمت‌گذاری و راهنمای مهاجرت، [خبر Gemini 3.8 Flash](fa/news/2026-09-03-gemini-3-8-flash-added.md) را ببینید.

### Gemini 3.7 Flash

Gemini 3.7 Flash (`gemini-3.7-flash`) مدل پرچم‌دار و همه‌کاره Flash گوگل برای کدنویسی، عامل‌ها، توسعه وب، درک اسناد پیچیده و خودکارسازی گردش‌کارهای تجاری است. این مدل که در اوت ۲۰۲۶ منتشر شده، مهندسی نرم‌افزار، کیفیت کد در اولین تلاش، پیروی از دستورالعمل، برنامه‌ریزی چندمرحله‌ای و استفاده از ابزار را نسبت به Gemini 3.6 Flash بهبود می‌دهد.

| ویژگی                      | جزئیات                                                                                                      |
| -------------------------- | ------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                | ۱٬۰۴۸٬۵۷۶ توکن ورودی، ۶۵٬۵۳۶ توکن خروجی                                                                    |
| ورودی‌ها                   | متن، تصویر، ویدیو، صدا، PDF                                                                                 |
| خروجی                      | متن                                                                                                         |
| ورودی تشویقی               | $0.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶                                                                    |
| ورودی کش‌شده تشویقی        | $0.075 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶                                                                   |
| خروجی تشویقی               | $3.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶                                                                    |
| قیمت استاندارد             | ورودی $1.50، ورودی کش‌شده $0.15 و خروجی $7.50 / ۱ میلیون توکن پس از ۳۱ دسامبر ۲۰۲۶                         |
| نقاط پایانی پشتیبانی‌شده   | `v1beta/`، `v1/chat/completions`، `v1/messages` و پشتیبانی جزئی `v1/responses`                              |
| نقاط قوت                   | کدنویسی، اجرای عاملی، توسعه وب، هوشمندی اسناد و خودکارسازی گردش‌کار                                         |

**قابلیت‌های کلیدی:**
- **کدنویسی و عامل‌ها**: بهبود اشکال‌زدایی، رفع مسئله، مهندسی بلندمدت، برنامه‌ریزی و فراخوانی ابزار
- **توسعه وب**: پایبندی بهتر به طراحی و تولید برنامه‌های کامل‌تر با پرامپت‌های کمتر
- **کار دانشی**: استدلال قوی‌تر روی اسناد پیچیده در مالی، حقوق، علوم زیستی و سایر حوزه‌های متراکم
- **چندوجهی بومی**: پذیرش ورودی متن، تصویر، ویدیو، صدا و PDF
- **قابلیت‌های توسعه‌دهنده**: تفکر، فراخوانی تابع، خروجی ساختاریافته، اجرای کد، کش پرامپت، جستجوی فایل، پایه‌گذاری با Google Search و زمینه URL

```python
response = client.chat.completions.create(
    model="gemini-3.7-flash",
    messages=[
        {
            "role": "user",
            "content": "این معماری را بررسی کن و یک برنامه پیاده‌سازی مرحله‌ای همراه با ریسک‌ها و معیارهای rollback بنویس.",
        }
    ],
)

print(response.choices[0].message.content)
```

برای نمونه نقاط پایانی، نتایج بنچمارک گزارش‌شده و راهنمای مهاجرت، [خبر Gemini 3.7 Flash](fa/news/2026-08-14-gemini-3-7-flash-added.md) را ببینید.

### Gemini 3.5 Flash

Gemini 3.5 Flash (`gemini-3.5-flash`) مدل پرچم‌دار جدید Flash گوگل است که بر پایه زیرساخت استدلالی Gemini 3 Flash ساخته شده و با سطوح تفکر قابل تنظیم، تعادل کیفیت، هزینه و تأخیر را کنترل می‌کند. این مدل که در مه ۲۰۲۶ منتشر شده، در کدنویسی، استفاده عامل‌محور از ابزارها، وظایف تخصصی، درک چندوجهی و عملکرد زمینه طولانی بهبود دارد و همچنان پروفایل سریع Flash را حفظ می‌کند.

| ویژگی                        | جزئیات                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                  | ۱,۰۴۸,۵۷۶ توکن ورودی، ۶۵,۵۳۶ توکن خروجی                                                                            |
| ورودی‌ها                     | متن، تصویر، ویدیو، صدا، PDF                                                                                        |
| خروجی                        | متن                                                                                                                |
| قیمت‌گذاری ورودی             | $1.50 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری ورودی کش شده      | $0.25 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری خروجی             | $9.00 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری ورودی صوتی        | $1.00 / ۱ میلیون توکن                                                                                              |
| قیمت ورودی صوتی کش شده       | $0.50 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری خروجی صوتی        | $1.00 / ۱ میلیون توکن                                                                                              |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                        |
| نقاط قوت                     | استدلال پرچم‌دار Flash، کدنویسی، استفاده عامل‌محور از ابزار، ورودی چندوجهی، زمینه طولانی                           |
| بهترین برای                  | گردش‌کارهای عاملی، کدنویسی پیشرفته، استدلال چندوجهی، تحلیل زمینه طولانی                                            |

**قابلیت‌های کلیدی:**
- **تفکر قابل تنظیم**: پشتیبانی از مقادیر `thinkingLevel` (`low`، `medium`، `high`) از طریق `generationConfig` مربوط به Gemini
- **چندوجهی بومی**: پذیرش ورودی متن، تصویر، ویدیو، صدا و PDF در یک درخواست
- **زمینه طولانی**: پنجره ورودی ۱M توکن برای اسناد بزرگ، مخازن کد و تحلیل چندمنبعی
- **فراخوانی تابع**: پشتیبانی کامل از فراخوانی تابع، فراخوانی تابع موازی و خروجی‌های ساختاریافته
- **پایه‌گذاری جستجو و زمینه URL**: امکان استفاده از Google Search grounding و URL Context برای پاسخ‌های آگاه از وب
- **کش پرامپت**: پشتیبانی از ورودی‌های کش‌شده برای زمینه‌های طولانی تکراری

**نکات برجسته بنچمارک:**
- **Terminal-bench 2.1**: 76.2% برای کدنویسی عاملی در ترمینال
- **SWE-Bench Pro**: 55.1% در وظایف متنوع کدنویسی عاملی
- **MCP Atlas**: 83.6% در گردش‌کارهای چندمرحله‌ای MCP
- **Toolathlon**: 56.5% در استفاده واقعی از ابزارها
- **CharXiv Reasoning**: 84.2% برای استدلال روی نمودارهای پیچیده
- **Humanity's Last Exam**: 40.2% در استدلال دانشگاهی

```python
response = client.chat.completions.create(
    model="gemini-3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "برای یک پلتفرم پرداخت جهانی، یک معماری event-driven مقاوم طراحی کن.",
        }
    ],
    extra_body={"generationConfig": {"thinkingConfig": {"thinkingLevel": "high"}}},
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="برای یک پلتفرم پرداخت جهانی، یک معماری event-driven مقاوم طراحی کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 3.1 Pro Preview

Gemini 3.1 Pro Preview (`gemini-3.1-pro-preview`) نسل بعدی سری Gemini 3 و پیشرفته‌ترین مدل گوگل از فوریه ۲۰۲۶ است. این مدل استدلال بومی چندوجهی به طور قابل توجهی در معیارهای کلیدی از Gemini 3 Pro پیشی می‌گیرد و در عین حال معماری و قیمت‌گذاری یکسانی دارد. این مدل در عملکرد عاملی، کدنویسی پیشرفته، درک زمینه طولانی و توسعه الگوریتم برتری دارد.

| ویژگی                        | جزئیات                                                                                                                    |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه                  | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                           |
| حداکثر توکن خروجی            | ۶۴ هزار توکن                                                                                                               |
| ورودی‌ها                     | صدا، تصاویر، ویدیوها، متن و مخازن کد                                                                                      |
| خروجی                        | متن                                                                                                                       |
| قیمت‌گذاری ورودی (<۲۰۰ هزار) | ۲.۰۰ دلار / ۱ میلیون توکن (متن)                                                                                           |
| قیمت‌گذاری خروجی (<۲۰۰ هزار) | ۱۲.۰۰ دلار / ۱ میلیون توکن (متن)                                                                                          |
| قیمت‌گذاری ورودی (>۲۰۰ هزار) | ۴.۰۰ دلار / ۱ میلیون توکن (متن)                                                                                           |
| قیمت‌گذاری خروجی (>۲۰۰ هزار) | ۱۸.۰۰ دلار / ۱ میلیون توکن (متن)                                                                                          |
| قیمت‌گذاری ورودی صوتی        | ۷.۰۰ دلار / ۱ میلیون توکن                                                                                                 |
| ورودی صوتی کش‌شده           | ۱.۵۰ دلار / ۱ میلیون توکن                                                                                                 |
| قیمت‌گذاری خروجی صوتی        | ۷.۰۰ دلار / ۱ میلیون توکن                                                                                                 |
| قیمت ذخیره‌سازی زمینه        | ۰.۸۲۵ دلار / ۱ میلیون توکن (≤۲۰۰ هزار)، ۱.۰۰ دلار / ۱ میلیون توکن (>۲۰۰ هزار)                                             |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                               |
| نقاط قوت                     | استدلال پیشرفته، درک چندوجهی، حل مسائل پیچیده، عملکرد عاملی                                                               |
| بهترین برای                  | استدلال پیچیده، برنامه‌ریزی استراتژیک، کدنویسی پیشرفته، توسعه الگوریتم، تحقیق                                              |

**بهبودهای کلیدی معیارها نسبت به Gemini 3 Pro:**
- **آزمون آخر بشریت**: 44.4% (در مقابل 37.5%) - بهترین در کلاس بدون ابزار
- **ARC-AGI-2**: 77.1% (در مقابل 31.1%) - بهبود قابل توجه در استدلال انتزاعی
- **GPQA Diamond**: 94.3% (در مقابل 91.9%) - دانش علمی برتر
- **Terminal-Bench 2.0**: 68.5% (در مقابل 56.9%) - بهترین کدنویسی عاملی ترمینال
- **LiveCodeBench Pro**: 2887 Elo (در مقابل 2439) - بهترین کدنویسی رقابتی
- **BrowseComp**: 85.9% (در مقابل 59.2%) - جستجوی عاملی برتر

```python
response = client.chat.completions.create(
    model="gemini-3.1-pro-preview",
    messages=[
        {"role": "system", "content": "شما یک متخصص در حل مسائل پیچیده هستید."},
        {
            "role": "user",
            "content": "یک راه‌حل جامع برای بهینه‌سازی یک سیستم توزیع‌شده در مقیاس بزرگ طراحی کنید.",
        },
    ],
    max_tokens=4096,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-pro-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک راه‌حل جامع برای بهینه‌سازی یک سیستم توزیع‌شده در مقیاس بزرگ طراحی کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 3 Pro Image (Nano Banana Pro)

Gemini 3 Pro Image (`gemini-3-pro-image`)، همچنین با نام "Nano Banana Pro" شناخته می‌شود، پیشرفته‌ترین مدل تولید و ویرایش تصویر گوگل است که برای تولید دارایی‌های حرفه‌ای و دستورالعمل‌های بصری پیچیده طراحی شده است.

> **نسخه پایدار در دسترس:** نام مستعار پایدار `gemini-3-pro-image` اکنون با قابلیت‌ها و قیمت‌گذاری یکسان در دسترس است. توصیه می‌کنیم برای محیط‌های تولید از `gemini-3-pro-image` استفاده کنید. برای جزئیات به [به‌روزرسانی ۵ ژوئن ۲۰۲۶](fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added.md) مراجعه کنید.

| ویژگی                        | جزئیات                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                  | پشتیبانی از ورودی متن و تصویر                                                                                      |
| حداکثر خروجی                 | تصاویر تا وضوح 4K (4096x4096px)، به علاوه پاسخ‌های متنی                                                             |
| ورودی‌ها                     | پرامپت‌های متنی، تصاویر مرجع                                                                                       |
| خروجی‌ها                     | تصاویر (وضوح 1K-4K) و متن                                                                                          |
| قیمت‌گذاری ورودی             | 2.00 دلار / 1 میلیون توکن (متن)، 2.00 دلار / 1 میلیون توکن (ورودی تصویر، ~0.067 دلار به ازای هر تصویر)           |
| قیمت‌گذاری خروجی             | 12.00 دلار / 1 میلیون توکن (متن)، 0.134 دلار به ازای تصویر 1K-2K، 0.24 دلار به ازای تصویر 4K                       |
| قیمت ذخیره‌سازی زمینه        | 0.50 دلار / 1 میلیون توکن                                                                                          |
| نقاط قوت                     | رندر متن پیشرفته (از جمله فارسی)، کنترل کیفیت استودیویی، دانش واقعی                                                |
| بهترین برای                  | گرافیک حرفه‌ای، مواد بازاریابی بومی‌سازی شده، تولید متن در تصویر، ویرایش تصویر                                      |
| وضعیت                        | پیش‌نمایش                                                                                                          |

**ویژگی‌های کلیدی:**
- **رندر متن پیشرفته**: اولین مدل تولید تصویر که حروف فارسی را با دقت تقریبا کامل رندر می‌کند
- **کنترل کیفیت استودیویی**: کنترل دقیق بر ترکیب‌بندی، نورپردازی، درجه‌بندی رنگ و نسبت ابعاد
- **دانش واقعی**: استفاده از Google Search برای تولید تصویر دقیق و مبتنی بر واقعیت
- **پشتیبانی از وضوح**: تولید تصاویر تا وضوح 4K (4096x4096px)
- **ویرایش تصویر**: قابلیت‌های ویرایش جامع شامل تنظیم نسبت ابعاد، تغییر نورپردازی و ثبات سوژه
- **فرآیند "تفکر" پیش‌فرض**: بهینه‌سازی ترکیب‌بندی قبل از تولید برای نتایج بهینه
- **پشتیبانی چند زبانه**: قابلیت استثنایی برای بومی‌سازی طراحی‌ها در زبان‌های مختلف

**قیمت‌گذاری خروجی تصویر**: تصاویر از 1024x1024px (1K) تا 2048x2048px (2K) معادل 1120 توکن هستند (0.134 دلار به ازای هر تصویر). تصاویر تا 4096x4096px (4K) معادل 2000 توکن هستند (0.24 دلار به ازای هر تصویر).

> **استفاده از تنظیمات اختصاصی Gemini از طریق Endpoint سازگار با OpenAI**: هنگام استفاده از `gemini-3-pro-image` از طریق endpoint سازگار با OpenAI (`v1/chat/completions`) و نیاز به استفاده از تنظیمات اختصاصی Gemini (پارامترهای غیر OpenAI)، باید دیکشنری `generationConfig` را از طریق `extra_body` ارسال کنید تا AvalAI بتواند آن را به ارائه‌دهنده نگاشت کند. این مدل از هر دو `aspectRatio` و `imageSize` در `imageConfig` پشتیبانی می‌کند. کاربران همچنین می‌توانند از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به Gemini از طریق schema API بومی و SDK رسمی گوگل استفاده کنند.

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر با متن
response = client.chat.completions.create(
    model="gemini-3-pro-image",
    messages=[
        {
            "role": "user",
            "content": "یک پوستر مینیمالیست با متن فارسی 'هوش مصنوعی' در یک سبک مدرن و الهام‌گرفته از فناوری با رنگ‌های آبی و سفید ایجاد کن",
        }
    ],
    modalities=["image", "text"],
)

# دسترسی به تصویر تولید شده
if hasattr(response.choices[0].message, "images"):
    images = getattr(response.choices[0].message, "images")
    for img in images:
        print(f"Image URL: {img.image_url.url[:100]}...")

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "یک پوستر مینیمالیست با متن فارسی"},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**با generationConfig اختصاصی Gemini (aspectRatio و imageSize):**

```python
# تولید تصویر با نسبت ابعاد و اندازه سفارشی با استفاده از extra_body
response = client.chat.completions.create(
    model="gemini-3-pro-image",
    messages=[
        {
            "role": "user",
            "content": "تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {"imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}
    },
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**نمونه ویرایش تصویر:**

```python
# ویرایش تصویر موجود
response = client.chat.completions.create(
    model="gemini-3-pro-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "نسبت ابعاد را به 16:9 تغییر بده در حالی که سوژه در مرکز باقی بماند",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/original-image.jpg"},
                },
            ],
        }
    ],
    modalities=["image", "text"],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 3.1 Flash Image (Nano Banana 2)

Gemini 3.1 Flash Image (`gemini-3.1-flash-image`)، همچنین با نام "Nano Banana 2" شناخته می‌شود، مدل پربازده تولید و ویرایش تصویر گوگل است که برای سرعت و موارد استفاده توسعه‌دهندگان با حجم بالا بهینه‌سازی شده است. این مدل به عنوان همتای پربازده Gemini 3 Pro Image با نسبت قیمت به عملکرد استثنایی عمل می‌کند.

> **نسخه پایدار در دسترس:** نام مستعار پایدار `gemini-3.1-flash-image` اکنون با قابلیت‌ها و قیمت‌گذاری یکسان در دسترس است. توصیه می‌کنیم برای محیط‌های تولید از `gemini-3.1-flash-image` استفاده کنید. برای جزئیات به [به‌روزرسانی ۵ ژوئن ۲۰۲۶](fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added.md) مراجعه کنید.

| ویژگی                        | جزئیات                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                  | پشتیبانی از ورودی متن و تصویر                                                                                      |
| حداکثر خروجی                 | تصاویر تا وضوح 4K (4096x4096px)، به علاوه پاسخ‌های متنی                                                             |
| ورودی‌ها                     | پرامپت‌های متنی، تصاویر مرجع                                                                                       |
| خروجی‌ها                     | تصاویر (وضوح 512px-4K) و متن                                                                                       |
| قیمت‌گذاری ورودی             | $0.50 / 1 میلیون توکن (متن)، $0.50 / 1 میلیون توکن (ورودی تصویر)                                                   |
| قیمت‌گذاری ورودی کش شده      | $0.25 / 1 میلیون توکن                                                                                              |
| قیمت‌گذاری خروجی             | $3.00 / 1 میلیون توکن (متن)، $60.00 / 1 میلیون توکن (خروجی تصویر)                                                  |
| قیمت‌گذاری به ازای هر تصویر  | $0.0672 برای تصویر 1K-2K، $0.101 برای تصویر 2K-4K، $0.151 برای تصویر 4K                                            |
| نقاط قوت                     | پربازده، تولید سریع، دانش جهانی با جستجوی وب، رندر متن پیشرفته                                                     |
| بهترین برای                  | برنامه‌های با حجم بالا، تکرارهای سریع، تولید تصویر مقرون به صرفه، گردش‌های کاری تولید                              |
| وضعیت                        | پیش‌نمایش                                                                                                          |

**ویژگی‌های کلیدی:**
- **دانش جهانی بهبود یافته**: استفاده از دانش گسترده Gemini با پایه‌گذاری جستجوی وب برای ایجاد تصاویر بهبود یافته
- **رندر متن پیشرفته**: رندر متن قابل اعتماد و واضح با بومی‌سازی درون تصویر با پشتیبانی از چندین زبان
- **کنترل خلاقانه بیشتر**: نورپردازی پرجنب و جوش، بافت‌های غنی‌تر، جزئیات تیزتر با سطوح تفکر قابل تنظیم
- **نسبت ابعاد بومی**: پشتیبانی از تمام نسبت‌های موجود به علاوه نسبت‌های جدید 4:1، 1:4، 8:1 و 1:8
- **وضوح جدید 512px**: بهینه‌سازی برای کارایی با حداقل تاخیر برای تکرارهای سریع
- **پیروی بهبود یافته از دستورالعمل**: پایبندی دقیق‌تر به دستورات پیچیده و چندلایه
- **پایه‌گذاری جستجوی تصویر گوگل**: تولید تصاویر بر اساس مراجع تصویر دنیای واقعی (انحصاری برای 3.1 Flash)

**قیمت‌گذاری خروجی تصویر**: تصاویر از 1024x1024px (1K) تا 2048x2048px (2K) به قیمت $0.0672 به ازای هر تصویر. تصاویر از 2K تا 4K به قیمت $0.101 به ازای هر تصویر. تصاویر با وضوح 4K به قیمت $0.151 به ازای هر تصویر.

> **استفاده از تنظیمات اختصاصی Gemini از طریق Endpoint سازگار با OpenAI**: هنگام استفاده از `gemini-3.1-flash-image` از طریق endpoint سازگار با OpenAI (`v1/chat/completions`) و نیاز به استفاده از تنظیمات اختصاصی Gemini (پارامترهای غیر OpenAI)، باید دیکشنری `generationConfig` را از طریق `extra_body` ارسال کنید تا AvalAI بتواند آن را به ارائه‌دهنده نگاشت کند. این مدل از هر دو `aspectRatio` و `imageSize` در `imageConfig` پشتیبانی می‌کند. کاربران همچنین می‌توانند از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به Gemini از طریق schema API بومی و SDK رسمی گوگل استفاده کنند.

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر با متن
response = client.chat.completions.create(
    model="gemini-3.1-flash-image",
    messages=[
        {
            "role": "user",
            "content": "یک تصویر فتورئالیستیک از غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
        }
    ],
    modalities=["image", "text"],
)

# دسترسی به تصویر تولید شده
if hasattr(response.choices[0].message, "images"):
    images = getattr(response.choices[0].message, "images")
    for img in images:
        print(f"Image URL: {img.image_url.url[:100]}...")

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "یک تصویر فتورئالیستیک از غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
                },
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**با generationConfig اختصاصی Gemini (aspectRatio و imageSize):**

```python
# تولید تصویر با نسبت ابعاد و اندازه سفارشی با استفاده از extra_body
response = client.chat.completions.create(
    model="gemini-3.1-flash-image",
    messages=[
        {
            "role": "user",
            "content": "تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {"imageConfig": {"aspectRatio": "16:9", "imageSize": "2K"}}
    },
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**نمونه ویرایش تصویر:**

```python
# ویرایش تصویر موجود
response = client.chat.completions.create(
    model="gemini-3.1-flash-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این تصویر را به سبک سایبرپانک با رنگ‌های نئون تبدیل کن",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/original-image.jpg"},
                },
            ],
        }
    ],
    modalities=["image", "text"],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 3.1 Flash Lite Image (Nano Banana 2 Lite)

مدل Gemini 3.1 Flash Lite Image (`gemini-3.1-flash-lite-image`)، همچنین با نام "Nano Banana 2 Lite" شناخته می‌شود، متخصص کارایی در خانواده تولید تصویر Gemini است. این مدل تاخیر زیر ۲ ثانیه و هزینه‌های محاسباتی به طور قابل توجهی کاهش‌یافته را هدف قرار می‌دهد و موارد استفاده تعاملی توسعه‌دهندگان با حجم بالا و برنامه‌های مصرف‌کننده بلادرنگ را ممکن می‌سازد، در حالی که کیفیت Nano Banana را در وضوح 1K حفظ می‌کند.

| ویژگی                  | جزئیات                                                                                      |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| پنجره زمینه            | 65,536 توکن ورودی، 4,096 توکن خروجی                                                          |
| حداکثر خروجی           | تصاویر در وضوح 1K (1024x1024px)، به علاوه پاسخ‌های متنی                                       |
| ورودی‌ها               | پرامپت‌های متنی، تصاویر مرجع                                                                  |
| خروجی‌ها               | تصاویر (وضوح 1K) و متن                                                                        |
| قیمت‌گذاری ورودی       | $0.25 / 1M توکن (متن)، $0.25 / 1M توکن (ورودی تصویر)                                          |
| قیمت‌گذاری ورودی کش شده | $0.05 / 1M توکن                                                                             |
| قیمت‌گذاری خروجی       | $1.50 / 1M توکن (متن)، $30.00 / 1M توکن (خروجی تصویر)                                         |
| قیمت‌گذاری هر تصویر    | $0.0336 به ازای هر تصویر 1K                                                                  |
| تاریخ قطع دانش         | ژانویه ۲۰۲۵                                                                                  |
| نقاط قوت               | تاخیر بسیار کم، مقرون‌به‌صرفه در مقیاس، تولید و ویرایش درهم‌تنیده                             |
| بهترین برای            | برنامه‌های تعاملی با حجم بالا، تولید بلادرنگ، تکرار سریع، ویرایش‌های محلی چندنوبتی            |
| وضعیت                  | پایدار                                                                                       |

**ویژگی‌های کلیدی:**
- **تاخیر زیر ۲ ثانیه**: بهینه‌سازی شده برای تاخیر بسیار کم و سرتاسری برای تکرار سریع و تعاملی
- **مقرون‌به‌صرفه در مقیاس**: تولید هزاران تصویر با کسری از هزینه مدل‌های سنگین‌تر تولید
- **تولید و ویرایش درهم‌تنیده**: پشتیبانی بومی از Text → Text + Image(s) و Image + Text → Text + Image(s)
- **ویرایش‌های محلی سریع چندنوبتی**: تعویض رنگ‌ها، ساخت استیکر و تنظیم پس‌زمینه در نوبت‌های مکالمه‌ای سریع
- **سازگاری شخصیت**: حفظ همترازی بالای شخصیت مطابق با استانداردهای اصلی Nano Banana
- **۱۴ نسبت ابعاد**: پشتیبانی از `1:1`، `3:2`، `2:3`، `3:4`، `4:3`، `4:5`، `5:4`، `9:16`، `16:9`، `21:9` و فرمت‌های استاندارد دیگر
- **فراخوانی تابع و تفکر**: فراخوانی تابع و تفکر (حداقلی و بالا) پشتیبانی می‌شود
- **واترمارک SynthID + C2PA**: واترمارک همیشه‌فعال برای تصاویر تولیدشده توسط هوش مصنوعی

**قیمت‌گذاری خروجی تصویر**: خروجی تصویر به قیمت $30 به ازای هر 1M توکن است. تصاویر خروجی در وضوح 1K (1024x1024px) تقریبا 1,120 توکن مصرف می‌کنند که معادل $0.0336 به ازای هر تصویر است. توجه: تنها وضوح 1K (1024px) پشتیبانی می‌شود؛ 2K و 4K برای این مدل در دسترس نیستند.

> **استفاده از تنظیمات اختصاصی Gemini از طریق Endpoint سازگار با OpenAI**: هنگام استفاده از `gemini-3.1-flash-lite-image` از طریق endpoint سازگار با OpenAI (`v1/chat/completions`) و نیاز به استفاده از تنظیمات اختصاصی Gemini (پارامترهای غیر OpenAI)، باید دیکشنری `generationConfig` را از طریق `extra_body` ارسال کنید تا AvalAI بتواند آن را به ارائه‌دهنده نگاشت کند. این مدل از `aspectRatio` (و `imageSize` ثابت روی `1K`) در `imageConfig` پشتیبانی می‌کند. کاربران همچنین می‌توانند از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به Gemini از طریق طرحواره API بومی و SDK رسمی گوگل استفاده کنند.

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر با متن
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": "Create a photorealistic macro photograph of a colorful spider covered in water droplets on its web",
        }
    ],
    modalities=["image", "text"],
)

# دسترسی به تصویر تولیدشده
if hasattr(response.choices[0].message, "images"):
    images = getattr(response.choices[0].message, "images")
    for img in images:
        print(f"Image URL: {img.image_url.url[:100]}...")

print(response.choices[0].message.content)
```

**با generationConfig اختصاصی Gemini (aspectRatio):**

```python
# تولید تصویر با نسبت ابعاد سفارشی در وضوح 1K با استفاده از extra_body
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": "A dynamic action shot of a swimmer performing the butterfly stroke",
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {"imageConfig": {"aspectRatio": "16:9", "imageSize": "1K"}}
    },
)
```

**نمونه ویرایش محلی سریع:**

```python
# انجام یک ویرایش محلی سریع چندنوبتی
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Change the background of this product photo to a soft studio gradient",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/original-image.jpg"},
                },
            ],
        }
    ],
    modalities=["image", "text"],
)
```

### Gemini 3.1 Flash-Lite (پایدار) و Preview

Gemini 3.1 Flash-Lite (`gemini-3.1-flash-lite`) نسخه پایدار مقرون‌به‌صرفه‌ترین مدل چندوجهی Gemini 3 گوگل است. alias قبلی `gemini-3.1-flash-lite-preview` همچنان با همان قیمت‌گذاری و قابلیت‌ها در دسترس است، اما برای یکپارچه‌سازی‌های production استفاده از alias پایدار توصیه می‌شود. این مدل برای وظایف عاملی با حجم بالا، استخراج داده ساده و برنامه‌های با تاخیر بسیار کم که بودجه و سرعت محدودیت‌های اصلی هستند، بهترین گزینه است.

| ویژگی                        | جزئیات                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                  | ۱,۰۴۸,۵۷۶ توکن ورودی، ۶۵,۵۳۶ توکن خروجی                                                                            |
| ورودی‌ها                     | متن، تصویر، ویدیو، صدا، PDF                                                                                        |
| خروجی                        | متن                                                                                                                |
| قیمت‌گذاری ورودی             | $0.25 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری ورودی کش شده      | $0.025 / ۱ میلیون توکن                                                                                             |
| قیمت‌گذاری خروجی             | $1.50 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری ورودی صوتی        | $0.50 / ۱ میلیون توکن                                                                                              |
| قیمت ورودی صوتی کش شده       | $0.05 / ۱ میلیون توکن                                                                                              |
| قیمت‌گذاری خروجی صوتی        | $1.50 / ۱ میلیون توکن                                                                                              |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                        |
| نقاط قوت                     | مقرون‌به‌صرفه، سریع‌ترین عملکرد، ورودی چندوجهی، پشتیبانی از تفکر                                                   |
| بهترین برای                  | وظایف عاملی حجم بالا، ترجمه، رونویسی، استخراج داده، مسیریابی مدل                                                   |

**قابلیت‌های کلیدی:**
- **Batch API**: پشتیبانی از پردازش حجم بالا
- **ذخیره‌سازی زمینه**: پشتیبانی برای زمینه‌های تکراری کارآمد
- **اجرای کد**: اجرای مستقیم کد در مدل
- **جستجوی فایل**: جستجو در فایل‌های آپلود شده
- **فراخوانی تابع**: پشتیبانی کامل از استفاده از ابزار و گردش‌های کاری عاملی
- **پایه‌گذاری جستجو**: یکپارچه‌سازی Google Search برای پاسخ‌های دقیق
- **خروجی‌های ساختاریافته**: تولید پاسخ‌های JSON ساختاریافته با اعتبارسنجی schema
- **تفکر/استدلال**: سطوح تفکر قابل تنظیم (کم، متوسط، زیاد) برای استدلال گام‌به‌گام
- **زمینه URL**: دریافت و پردازش مستقیم محتوای وب

**بهترین موارد استفاده:**
- **ترجمه**: ترجمه سریع، ارزان و حجم بالا برای پیام‌های چت، نظرات، تیکت‌های پشتیبانی
- **رونویسی**: رونویسی صوتی و ویدیویی بدون راه‌اندازی خطوط لوله تبدیل گفتار به متن جداگانه
- **استخراج داده**: استخراج موجودیت، طبقه‌بندی و پردازش داده سبک با خروجی JSON
- **خلاصه‌سازی اسناد**: تجزیه PDF و بازگرداندن خلاصه‌های مختصر برای خطوط لوله پردازش اسناد
- **مسیریابی مدل**: استفاده به عنوان طبقه‌بندی‌کننده کم‌هزینه برای هدایت کوئری‌ها به مدل‌های مناسب بر اساس پیچیدگی وظیفه

```python
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[
        {
            "role": "user",
            "content": "متن زیر را به آلمانی ترجمه کنید: سلام، دوست داری بعدا پیتزا بخوریم؟ من خیلی گرسنه‌ام!",
        },
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-flash-lite` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="متن زیر را به آلمانی ترجمه کنید: سلام، دوست داری بعدا پیتزا بخوریم؟ من خیلی گرسنه‌ام!",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**با فعال‌سازی تفکر:**

```python
response = client.chat.completions.create(
    model="gemini-3.1-flash-lite",
    messages=[{"role": "user", "content": "هوش مصنوعی چگونه کار می‌کند؟"}],
    extra_body={"generationConfig": {"thinkingConfig": {"thinkingLevel": "high"}}},
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3.1-flash-lite` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="هوش مصنوعی چگونه کار می‌کند؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 3 Flash Preview

Gemini 3 Flash Preview (`gemini-3-flash-preview`) یک پیش‌نمایش قدیمی‌تر Flash است که برای سرعت، پایه‌گذاری جستجو و کار چندوجهی بهینه شده است. این مدل برای سازگاری همچنان در دسترس است، اما برای یکپارچه‌سازی‌های production جدید معمولا بهتر است از `gemini-3.5-flash` یا، در صورت اولویت هزینه، alias پایدار `gemini-3.1-flash-lite` شروع کنید.

| ویژگی                        | جزئیات                                                                                                             |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه                  | تا ۱,۰۴۸,۵۷۶ توکن (۱M)                                                                                             |
| حداکثر توکن خروجی            | ۶۵,۵۳۶ توکن                                                                                                        |
| ورودی‌ها                     | متن، تصویر، ویدیو، صدا، PDF                                                                                        |
| خروجی                        | متن                                                                                                                |
| قیمت‌گذاری ورودی             | $0.50 / 1M توکن                                                                                                    |
| قیمت‌گذاری ورودی کش شده      | $0.25 / 1M توکن                                                                                                    |
| قیمت‌گذاری خروجی             | $3.00 / 1M توکن                                                                                                    |
| قیمت‌گذاری ورودی صوتی        | $1.50 / 1M توکن                                                                                                    |
| قیمت‌گذاری ورودی صوتی کش شده | $0.50 / 1M توکن                                                                                                    |
| قیمت‌گذاری خروجی صوتی        | $1.50 / 1M توکن                                                                                                    |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                        |
| نقاط قوت                     | سرعت، کارایی، استدلال سطح حرفه‌ای، پایه‌گذاری جستجو، قابلیت‌های تفکر                                                |
| بهترین برای                  | وظایف روزمره، تحلیل ویدیو، استخراج داده، پرسش و پاسخ بصری، گردش‌های کاری سریع                                      |

**قابلیت‌های کلیدی:**
- **Batch API**: پشتیبانی می‌شود
- **کش کردن زمینه**: پشتیبانی برای زمینه‌های تکراری کارآمد
- **اجرای کد**: اجرای مستقیم کد در مدل
- **جستجوی فایل**: جستجو در فایل‌های آپلود شده
- **فراخوانی تابع**: پشتیبانی کامل از استفاده از ابزار و گردش‌های کاری عاملی
- **پایه‌گذاری جستجو**: جستجو و پایه‌گذاری برتر با دانش دنیای واقعی
- **خروجی‌های ساختاریافته**: تولید پاسخ‌های JSON ساختاریافته
- **تفکر/استدلال**: استدلال داخلی برای حل مسائل پیچیده
- **متن URL**: پردازش و درک محتوای صفحات وب

**عملکرد در معیارها:**
- **آزمون آخر بشریت**: ۳۳.۷٪ (بدون استفاده از ابزار) - هم‌سطح با GPT-5.2 (۳۴.۵٪)
- **MMMU-Pro**: ۸۱.۲٪ - از همه رقبا از جمله GPT-5.2 (۷۹.۵٪) پیشی گرفته
- ۳ برابر سریع‌تر از Gemini 2.5 Pro با عملکرد هم‌سطح
- به طور متوسط ۳۰٪ کمتر توکن برای وظایف تفکر نسبت به 2.5 Pro استفاده می‌کند

```python
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {"role": "system", "content": "شما یک دستیار مفید هستید."},
        {
            "role": "user",
            "content": "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح بده.",
        },
    ],
    max_tokens=2048,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-flash-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**نمونه چندوجهی:**

```python
response = client.chat.completions.create(
    model="gemini-3-flash-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چیست؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-flash-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 2.5 Pro

Gemini 2.5 Pro (`gemini-2.5-pro`) مدل چندمنظوره پیشرفته گوگل است که در کدنویسی و وظایف استدلالی پیچیده برتری دارد.

| ویژگی                        | جزئیات                                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه                  | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                               |
| حداکثر توکن خروجی            | ۶۵٬۵۳۶ توکن                                                                                                                   |
| ورودی‌ها                     | صدا، تصاویر، ویدیوها و متن                                                                                                    |
| خروجی                        | متن                                                                                                                           |
| قیمت‌گذاری ورودی (<۲۰۰ هزار) | ۱.۲۵ دلار / ۱ میلیون توکن (متن)                                                                                               |
| قیمت‌گذاری خروجی (<۲۰۰ هزار) | ۱۰.۰۰ دلار / ۱ میلیون توکن (متن، شامل توکن‌های تفکر)                                                                          |
| قیمت‌گذاری ورودی (>۲۰۰ هزار) | ۲.۵۰ دلار / ۱ میلیون توکن (متن)                                                                                               |
| قیمت‌گذاری خروجی (>۲۰۰ هزار) | ۱۵.۰۰ دلار / ۱ میلیون توکن (متن، شامل توکن‌های تفکر)                                                                          |
| قیمت ذخیره‌سازی زمینه        | ۰.۳۱ دلار / ۱ میلیون توکن (≤۲۰۰ هزار)، ۰.۶۲۵ دلار / ۱ میلیون توکن (>۲۰۰ هزار)، ۴.۵۰ دلار / ۱ میلیون توکن در ساعت (ذخیره‌سازی) |
| نقاط قوت                     | تفکر و استدلال پیشرفته، درک چندوجهی، کدنویسی پیشرفته                                                                          |
| بهترین برای                  | وظایف استدلالی پیچیده، تحقیق، تولید کد، تحلیل چندوجهی                                                                         |
| استدلال                      | پشتیبانی از تفکر قابل تنظیم از طریق پارامتر `thinking`                                                                        |

_توجه: قیمت‌گذاری برای ورودی‌های بیش از ۲۰۰ هزار توکن افزایش می‌یابد. قیمت‌گذاری صدا/ویدیو/تصویر به طور جداگانه اعمال می‌شود._

```python
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {"role": "system", "content": "شما یک تحلیلگر چندوجهی خبره هستید."},
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این کد را تحلیل کنید و بهبودهایی پیشنهاد دهید:",
                },
                {
                    "type": "text",
                    "text": "def factorial(n):\n if n == 0:\n return 1\n else:\n return n * factorial(n-1)",
                },
            ],
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 2.5 Flash

Gemini 2.5 Flash (`gemini-2.5-flash-preview-05-20`) اولین مدل استدلال ترکیبی گوگل است که از پنجره زمینه ۱ میلیون توکنی پشتیبانی می‌کند و دارای بودجه‌های تفکر است.

| ویژگی                 | جزئیات                                                                                                                         |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------ |
| پنجره زمینه           | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                                |
| حداکثر توکن خروجی     | ۸٬۱۹۲ توکن                                                                                                                     |
| ورودی‌ها              | صدا، تصاویر، ویدیوها و متن                                                                                                     |
| خروجی                 | متن                                                                                                                            |
| قیمت‌گذاری ورودی      | ۰.۱۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۱.۰۰ دلار / ۱ میلیون توکن (صدا)                                                   |
| قیمت‌گذاری خروجی      | بدون تفکر: ۰.۶۰ دلار / ۱ میلیون توکن، با تفکر: ۳.۵۰ دلار / ۱ میلیون توکن                                                       |
| قیمت ذخیره‌سازی زمینه | ۰.۰۳۷۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۲۵ دلار / ۱ میلیون توکن (صدا)، ۱.۰۰ دلار / ۱ میلیون توکن در ساعت (ذخیره‌سازی) |
| نقاط قوت              | تفکر انطباقی، کارایی هزینه، پنجره زمینه ۱ میلیون توکنی                                                                         |
| بهترین برای           | وظایف پیچیده که نیاز به استدلال کارآمد با کنترل هزینه دارند                                                                    |
| استدلال               | پشتیبانی از بودجه‌های تفکر قابل تنظیم از طریق پارامتر `thinking`                                                               |

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "اصول کلیدی یادگیری ماشین را به صورت مختصر خلاصه کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="اصول کلیدی یادگیری ماشین را به صورت مختصر خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای کنترل قابلیت‌های تفکر/استدلال مدل، می‌توانید از پارامتر `thinking` استفاده کنید:

?> **نکته:** `thinking_budget` تنها در Gemini 2.5 Flash پشتیبانی می‌شود. این اطلاعات در زمان نگارش این مطلب صحیح است و ممکن است در طول زمان تغییر کند. برای آخرین اطلاعات، به [مستندات رسمی Google AI](https://ai.google.dev/gemini-api/docs/thinking#set-budget) مراجعه کنید.

```python
# استفاده از کتابخانه‌های کلاینت OpenAI با AvalAI
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[{"role": "user", "content": "این مسئله پیچیده را گام به گام حل کن..."}],
    extra_body={
        "thinking": {"type": "enabled", "budget_tokens": 2000}
    },  # اجازه استفاده تا 2000 توکن برای استدلال
)

# استفاده از فراخوانی‌های مستقیم API
# پارامتر thinking مستقیما در بدنه درخواست قرار می‌گیرد
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این مسئله پیچیده را گام به گام حل کن...",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


تنظیم `budget_tokens` به 0 تفکر را غیرفعال می‌کند، در حالی که یک مقدار مثبت مانند 2000 به مدل اجازه می‌دهد تا حداکثر آن تعداد توکن را برای استدلال استفاده کند. این هم بر قیمت‌گذاری و هم بر عمق تحلیلی که مدل می‌تواند انجام دهد تاثیر می‌گذارد.


### مدل‌های تولید ویدیوی Veo 3.1

سری Veo 3.1 گوگل قابلیت‌های پیشرفته تولید ویدیوی هوش مصنوعی را ارائه می‌دهد و به توسعه‌دهندگان امکان می‌دهد ویدیوهای با کیفیت بالا را از پرامپت‌های متنی یا تصاویر مرجع ایجاد کنند. این مدل‌ها دارای تولید صدای بومی، کیفیت بصری بهبود یافته و رعایت بهتر پرامپت هستند.

#### Veo 3.1 Generate

Veo 3.1 Generate (`veo-3.1-generate-001`) کیفیت خروجی برتر با صدای بومی غنی، مکالمات طبیعی و جلوه‌های صوتی همگام‌سازی شده ارائه می‌دهد.

| ویژگی | جزئیات |
| ----------------------- | ------------------------------------------------------------------------------------ |
| حداکثر مدت زمان | 8 ثانیه (همچنین از 4، 6 ثانیه پشتیبانی می‌کند) |
| ورودی‌ها | پرامپت‌های متنی، تصاویر مرجع |
| خروجی | ویدیو با صدا (MP4) |
| رزولوشن‌ها | 720p، 1080p (فقط 16:9) |
| نسبت‌های تصویر | 16:9 (افقی)، 9:16 (عمودی) |
| صدا | صدای بومی با جلوه‌های صوتی و صدای محیطی |
| قیمت‌گذاری خروجی | 0.40 دلار / ثانیه ویدیو |
| نقاط قوت | بالاترین کیفیت، صدای غنی، ثبات کاراکتر |
| بهترین برای | محتوای آماده تولید، ویدیوهای حرفه‌ای، کیفیت سینمایی |
| وضعیت | پایدار |

**ویژگی‌های کلیدی:**
- **تولید صدای بومی**: ویدیوها شامل صدای همگام‌سازی شده با جلوه‌های صوتی طبیعی هستند
- **تصویر-به-ویدیو**: تولید ویدیو از تصاویر مرجع با رعایت بهتر پرامپت
- **تصاویر مرجع**: استفاده از تا 3 تصویر مرجع برای ثبات کاراکتر/سبک
- **گسترش ویدیو**: گسترش ویدیوهای موجود برای ایجاد توالی‌های طولانی‌تر
- **رزولوشن بالا**: پشتیبانی از خروجی 1080p در نسبت تصویر 16:9

```python
from openai import OpenAI
import time

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید ویدیو از متن
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب",
    seconds="8",
)

print(f"تولید ویدیو شروع شد: {video.id}")

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(video.id)

    if video_status.status == "completed":
        print(f"ویدیو آماده است! ID: {video.id}")

        # دانلود ویدیو
        content = client.videos.download_content(video.id)
        with open("output.mp4", "wb") as f:
            f.write(content.read())
        print("ویدیو با موفقیت دانلود شد!")
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    time.sleep(10)
```

#### Veo 3.1 Fast Generate

Veo 3.1 Fast Generate (`veo-3.1-fast-generate-001`) برای سرعت بهینه شده است در حالی که کیفیت بالا را حفظ می‌کند، ایده‌آل برای تکرار سریع و پروژه‌های با حجم بالا.

| ویژگی | جزئیات |
| ----------------------- | ------------------------------------------------------------------------------------ |
| حداکثر مدت زمان | 8 ثانیه (همچنین از 4، 6 ثانیه پشتیبانی می‌کند) |
| ورودی‌ها | پرامپت‌های متنی، تصاویر مرجع |
| خروجی | ویدیو با صدا (MP4) |
| رزولوشن‌ها | 720p، 1080p (فقط 16:9) |
| نسبت‌های تصویر | 16:9 (افقی)، 9:16 (عمودی) |
| صدا | صدای بومی با کیفیت بالا |
| قیمت‌گذاری خروجی | 0.15 دلار / ثانیه ویدیو |
| نقاط قوت | تولید سریع، مقرون‌به‌صرفه، کیفیت بالا |
| بهترین برای | تکرار سریع، برنامه‌های با حجم بالا، پروژه‌های حساس به هزینه |
| وضعیت | پایدار |

```python
# تولید سریع ویدیو برای تکرارهای سریع
video = client.videos.create(
    model="veo-3.1-fast-generate-001",
    prompt="گربه‌ای که در یک باغ آفتابی با توپ نخ بازی می‌کند",
    seconds="4",
)

print(f"تولید سریع ویدیو شروع شد: {video.id}")
```

#### تولید تصویر-به-ویدیو

از تصاویر مرجع برای هدایت تولید ویدیو استفاده کنید:

```python
# تولید ویدیو از تصویر مرجع
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="منظره زنده می‌شود با آب جاری و ابرهای متحرک، پرندگان در بالای سر پرواز می‌کنند",
    input_reference=open("reference_image.jpg", "rb"),
    seconds="8",
)
```

#### کنترل نسبت تصویر و رزولوشن

```python
# افقی 1080p
video_landscape = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="تصویر هوایی پهپاد از شهر ساحلی در غروب خورشید",
    size="1920x1080",  # نگاشت به نسبت تصویر 16:9 در 1080p
    seconds="8",
)

# ویدیوی عمودی برای رسانه‌های اجتماعی
video_portrait = client.videos.create(
    model="veo-3.1-fast-generate-001",
    prompt="مدل فشن که در خیابان شهر راه می‌رود",
    size="1080x1920",  # نگاشت به نسبت تصویر 9:16
    seconds="6",
)
```

برای راهنمای جامع استفاده از مدل‌های Veo برای تولید ویدیو، [راهنمای تولید ویدیو با استفاده از Veo](fa/guides/generate-videos-using-veo.md) و [اطلاعیه Veo 3.1](fa/news/2025-11-18-veo-3-1-video-models-added.md) را ببینید.


### Gemini Flash Latest

Gemini Flash Latest (`gemini-flash-latest`) نام مستعاری با به‌روزرسانی خودکار است که اکنون به `gemini-3.8-flash` اشاره می‌کند. این نام مستعار همان قابلیت‌های کدنویسی، عاملی و استدلالی، نقاط پایانی و قیمت‌گذاری مسیر فعلی Gemini 3.8 Flash را دارد.

| ویژگی | جزئیات |
|--------|---------|
| مقصد فعلی | `gemini-3.8-flash` |
| ورودی تشویقی | $0.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| ورودی ذخیره‌شده تشویقی | $0.075 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| خروجی تشویقی | $3.75 / ۱ میلیون توکن تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| قیمت استاندارد | ورودی $1.50، ورودی ذخیره‌شده $0.15 و خروجی $7.50 / ۱ میلیون توکن پس از ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) |
| نقاط پایانی پشتیبانی‌شده | `v1beta/`، `v1/chat/completions`، `v1/messages` و پشتیبانی جزئی `v1/responses` |
| نقاط قوت | کدنویسی بلندمدت، عامل‌های خودکار، استدلال چندمرحله‌ای و استفاده تکرارشونده از ابزار |
| بهترین کاربرد | برنامه‌هایی که آگاهانه جدیدترین مدل Gemini Flash را دنبال می‌کنند |

اگر به نسخه ثابت، نتایج ارزیابی تکرارپذیر یا عرضه کنترل‌شده در محیط عملیاتی نیاز دارید، به‌جای نام مستعار از `gemini-3.8-flash` استفاده کنید. این نام مستعار ممکن است در آینده به مدل جدیدتری از Flash منتقل شود.

```python
response = client.chat.completions.create(
    model="gemini-flash-latest",
    messages=[
        {
            "role": "user",
            "content": "این سناریو پیچیده را تحلیل کنید و استدلال دقیق ارائه دهید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون پشتیبانی `gemini-flash-latest` از `/v1/responses` جزئی است.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این سناریو پیچیده را تحلیل کنید و استدلال دقیق ارائه دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 2.5 Flash Preview 09-2025

Gemini 2.5 Flash Preview 09-2025 (`gemini-2.5-flash-preview-09-2025`) جدیدترین نسخه پیش‌نمایش Gemini 2.5 Flash با قابلیت‌های استدلال بهبود یافته و عملکرد پیشرفته است.

| ویژگی                        | جزئیات                                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه                  | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                               |
| حداکثر توکن خروجی            | ۸٬۱۹۲ توکن                                                                                                                     |
| ورودی‌ها                     | صدا، تصاویر، ویدیوها و متن                                                                                                    |
| خروجی                        | متن                                                                                                                           |
| قیمت‌گذاری ورودی             | ۰.۳۰ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۱.۰۰ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری ورودی کش شده     | ۰.۱۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۲۵ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری خروجی             | ۲.۵۰ دلار / ۱ میلیون توکن                                                                                                      |
| نقاط قوت                     | استدلال بهبود یافته، عملکرد پیشرفته، قابلیت‌های چندوجهی                                                                       |
| بهترین برای                  | وظایف استدلالی پیشرفته، حل مسائل پیچیده، تحلیل چندوجهی                                                                       |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                                   |

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash-preview-09-2025",
    messages=[
        {
            "role": "user",
            "content": "این مسئله چندمرحله‌ای را با استدلال دقیق حل کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-preview-09-2025` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این مسئله چندمرحله‌ای را با استدلال دقیق حل کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini Flash Lite Latest

Gemini Flash Lite Latest (`gemini-flash-lite-latest`) نام مستعاری است که به مقرون‌به‌صرفه‌ترین مدل Gemini (`gemini-2.5-flash-lite-preview-09-2025`) اشاره می‌کند که برای استفاده در مقیاس بالا بهینه شده است.

| ویژگی                        | جزئیات                                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه                  | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                               |
| حداکثر توکن خروجی            | ۸٬۱۹۲ توکن                                                                                                                     |
| ورودی‌ها                     | صدا، تصاویر، ویدیوها و متن                                                                                                    |
| خروجی                        | متن                                                                                                                           |
| قیمت‌گذاری ورودی             | ۰.۱۰ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۱۰ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری ورودی کش شده     | ۰.۰۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۰۵ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری خروجی             | ۰.۴۰ دلار / ۱ میلیون توکن                                                                                                      |
| نقاط قوت                     | مقرون‌به‌صرفه‌ترین، بهینه برای مقیاس، عملکرد مناسب                                                                            |
| بهترین برای                  | برنامه‌های پرحجم، پروژه‌های حساس به هزینه، پردازش دسته‌ای                                                                     |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                                   |

```python
response = client.chat.completions.create(
    model="gemini-flash-lite-latest",
    messages=[
        {
            "role": "user",
            "content": "این متن را به صورت کارآمد با بهینه‌سازی هزینه پردازش کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-flash-lite-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این متن را به صورت کارآمد با بهینه‌سازی هزینه پردازش کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 2.5 Flash Lite Preview 09-2025

Gemini 2.5 Flash Lite Preview 09-2025 (`gemini-2.5-flash-lite-preview-09-2025`) کوچک‌ترین و مقرون‌به‌صرفه‌ترین مدل در سری Gemini 2.5 است که برای استفاده در مقیاس طراحی شده است.

| ویژگی                        | جزئیات                                                                                                                        |
| ---------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه                  | تا ۱ میلیون توکن (حداکثر ورودی)                                                                                               |
| حداکثر توکن خروجی            | ۸٬۱۹۲ توکن                                                                                                                     |
| ورودی‌ها                     | صدا، تصاویر، ویدیوها و متن                                                                                                    |
| خروجی                        | متن                                                                                                                           |
| قیمت‌گذاری ورودی             | ۰.۱۰ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۱۰ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری ورودی کش شده     | ۰.۰۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۰۵ دلار / ۱ میلیون توکن (صدا)                                                |
| قیمت‌گذاری خروجی             | ۰.۴۰ دلار / ۱ میلیون توکن                                                                                                      |
| نقاط قوت                     | فوق‌العاده مقرون‌به‌صرفه، عملکرد مناسب برای وظایف ساده، مقیاس‌پذیر                                                            |
| بهترین برای                  | استقرارهای بزرگ‌مقیاس، برنامه‌های حساس به هزینه، وظایف با پیچیدگی ساده تا متوسط                                              |
| تاریخ قطع دانش               | ژانویه ۲۰۲۵                                                                                                                   |

```python
response = client.chat.completions.create(
    model="gemini-2.5-flash-lite-preview-09-2025",
    messages=[
        {
            "role": "user",
            "content": "این سند را به طور کارآمد خلاصه کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-lite-preview-09-2025` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="این سند را به طور کارآمد خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Gemini 2.5 Flash Image یا Nano Banana

Gemini 2.5 Flash Image (`gemini-2.5-flash-image`) مدل پایدار و پیشرفته تولید تصویر گوگل از خانواده Gemini 2.5 است که دارای قابلیت‌های برتر تولید و ویرایش تصویر می‌باشد.

> **توجه:** نسخه پیش‌نمایش (`gemini-2.5-flash-image-preview`) اکنون منسوخ شده و به نفع نسخه پایدار جایگزین شده است. لطفا برای استفاده در محیط تولید به `gemini-2.5-flash-image` مهاجرت کنید.

برای راهنمای جامع در مورد استفاده از Gemini 2.5 Flash Image، [ساخت تصویر با مدل‌های سری Nano Banana](fa/examples/advanced_gemini_image_generation.md) را ببینید. برای جزئیات در مورد استفاده از پارامترهای اختصاصی ارائه‌دهنده، به [راهنمای پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md) مراجعه کنید.


| ویژگی | جزئیات |
| --------------------- | ------------------------------------------------------------------------------------- |
| پنجره زمینه | ۳۲٬۷۶۸ توکن (حداکثر ورودی) |
| حداکثر توکن خروجی | ۳۲٬۷۶۸ توکن |
| ورودی‌ها | تصاویر و متن |
| خروجی‌ها | تصاویر و متن |
| قیمت‌گذاری ورودی | ۰.۳۰ دلار / ۱ میلیون توکن (متن)، ۰.۳۰ دلار / ۱ میلیون توکن (تولید تصویر) |
| قیمت‌گذاری خروجی | ۲.۵۰ دلار / ۱ میلیون توکن (متن)، ۳۰.۰۰ دلار / ۱ میلیون توکن (تولید تصویر) |
| نقاط قوت | تولید تصویر پیشرفته، تبدیل متن به تصویر، تبدیل تصویر به تصویر |
| بهترین برای | تولید تصویر حرفه‌ای، کاربردهای خلاقانه، وظایف ویرایش تصویر |
| برش دانش | ژوئن ۲۰۲۵ |

> **استفاده از تنظیمات اختصاصی Gemini از طریق Endpoint سازگار با OpenAI**: هنگام استفاده از `gemini-2.5-flash-image` از طریق endpoint سازگار با OpenAI (`v1/chat/completions`) و نیاز به استفاده از تنظیمات اختصاصی Gemini (پارامترهای غیر OpenAI)، باید دیکشنری `generationConfig` را از طریق `extra_body` ارسال کنید تا AvalAI بتواند آن را به ارائه‌دهنده نگاشت کند. این مدل فقط از `aspectRatio` در `imageConfig` پشتیبانی می‌کند. کاربران همچنین می‌توانند از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به Gemini از طریق schema API بومی و SDK رسمی گوگل استفاده کنند.

## تولید تصویر از متن
```python
# تولید تصویر از متن
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": "تصویری فتورئالیستی از منظره کوهستانی با دریاچه‌ای که غروب خورشید را منعکس می‌کند، به سبک نقاشی منظره رمانتیک",
        }
    ],
    modalities=["image", "text"],
)

# Image is now available in the response
image_url = response.choices[0].message.images[0]["image_url"]["url"]
content = (
    response.choices[0].message.content.strip()
    if response.choices[0].message.content
    else None
)

# پردازش داده تصویر برگشت داده شده
header, base64_data = image_url.split(",", 1)
ext = header.split(";")[0].split("/")[1]

import base64

image_bytes = base64.b64decode(base64_data)
with open(f"generated_image.{ext}", "wb") as f:
    f.write(image_bytes)
print(f"✅ تصویر با نام generated_image.{ext} ذخیره شد")

# Print any text response that came with the image
if content:
    print(f"پاسخ مدل: {content}")
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "تصویری فتورئالیستی از منظره کوهستانی با دریاچه‌ای که غروب خورشید را منعکس می‌کند، به سبک نقاشی منظره رمانتیک",
                },
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## با generationConfig اختصاصی Gemini (aspectRatio)

```python
# تولید تصویر با نسبت ابعاد سفارشی با استفاده از extra_body
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": "تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
        }
    ],
    modalities=["image", "text"],
    extra_body={"generationConfig": {"imageConfig": {"aspectRatio": "16:9"}}},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="تصویری از یک غذای موز نانو در یک رستوران مجلل با تم Gemini بساز",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## تبدیل تصویر به تصویر

```python
# تبدیل تصویر به تصویر
prompt = "این تصویر را به سبک Ghibli بازسازی کن"
image_url = "https://storage.googleapis.com/github-repo/img/gemini/intro/landmark3.jpg"

messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای راهنمای جامع در مورد استفاده از Gemini 2.5 Flash Image، [ساخت تصویر با مدل‌های سری Nano Banana](fa/examples/advanced_gemini_image_generation.md) را ببینید. برای جزئیات در مورد استفاده از پارامترهای اختصاصی ارائه‌دهنده، به [راهنمای پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md) مراجعه کنید.

### Gemini Robotics-ER 1.5 Preview

Gemini Robotics-ER 1.5 Preview (`gemini-robotics-er-1.5-preview`) اولین مدل زبان-بینایی گوگل است که به‌طور خاص برای کاربردهای رباتیک طراحی شده و استدلال فضایی پیشرفته و قابلیت‌های عامل‌محور را به سیستم‌های رباتیک فیزیکی می‌آورد.

| ویژگی | جزئیات |
| --------------------- | ------------------------------------------------------------------------------------- |
| پنجره زمینه | مشابه Gemini 2.5 Flash |
| حداکثر توکن خروجی | ۸٬۱۹۲ توکن |
| ورودی‌ها | تصاویر، ویدیوها، صدا و متن |
| خروجی | متن با مختصات ساختاریافته (نقاط ۲D، جعبه‌های محدودکننده، مسیرها) |
| قیمت‌گذاری ورودی | ۰.۳۰ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۱.۰۰ دلار / ۱ میلیون توکن (صدا) |
| قیمت‌گذاری ورودی کش شده | ۰.۱۵ دلار / ۱ میلیون توکن (متن/تصویر/ویدیو)، ۰.۲۵ دلار / ۱ میلیون توکن (صدا) |
| قیمت‌گذاری خروجی | ۲.۵۰ دلار / ۱ میلیون توکن |
| نقاط قوت | استدلال فضایی، تشخیص اشیاء، برنامه‌ریزی مسیر، هماهنگی وظایف |
| بهترین برای | کاربردهای رباتیک، سیستم‌های هوش مصنوعی فیزیکی، برنامه‌ریزی دستکاری اشیاء |
| وضعیت | پیش‌نمایش |

**ویژگی‌های کلیدی:**
- **خودمختاری پیشرفته**: ربات‌ها را قادر می‌سازد تا استدلال کنند، سازگار شوند و به تغییرات در محیط‌های باز پاسخ دهند
- **تعامل زبان طبیعی**: تخصیص وظایف پیچیده با استفاده از زبان گفتگویی
- **هماهنگی وظایف**: دستورات زبان طبیعی را به زیروظایف برای وظایف طولانی‌مدت تجزیه می‌کند
- **قابلیت‌های همه‌کاره**: تشخیص اشیاء، استدلال فضایی، برنامه‌ریزی مسیر، تفسیر صحنه‌های پویا
- **بودجه تفکر**: بودجه استدلال قابل تنظیم برای متعادل‌سازی تاخیر در برابر دقت
- **پشتیبانی دوگانه SDK**: در دسترس از طریق API بومی Gemini v1beta و نقاط پایانی سازگار با OpenAI

**پشتیبانی API:**
- **پشتیبانی کامل**: `v1beta/` (نقطه پایانی بومی Gemini) - دسترسی کامل به تمام ویژگی‌های رباتیک
- **پشتیبانی جزئی**: `v1/chat/completions` (سازگار با OpenAI) - ورودی تصویر از طریق آرایه محتوا (مشابه سایر مدل‌های بینایی Gemini)

#### استفاده از API بومی Gemini (توصیه‌شده)

```python
from google import genai
from google.genai import types

# مقداردهی اولیه کلاینت GenAI
client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "url": "https://api.avalai.ir"},
)

MODEL_ID = "gemini-robotics-er-1.5-preview"

# بارگذاری تصویر شما
with open("robot-scene.jpg", "rb") as f:
    image_bytes = f.read()

# یافتن اشیاء در صحنه
prompt = """
Point to no more than 10 items in the image. The label returned
should be an identifying name for the object detected.
The answer should follow the json format: [{"point": [y, x], "label": <label>}, ...].
The points are in [y, x] format normalized to 0-1000.
"""

response = client.models.generate_content(
    model=MODEL_ID,
    contents=[
        types.Part.from_bytes(
            data=image_bytes,
            mime_type="image/jpeg",
        ),
        prompt,
    ],
    config=types.GenerateContentConfig(
        temperature=0.5, thinking_config=types.ThinkingConfig(thinking_budget=0)
    ),
)

print(response.text)
```

#### استفاده سازگار با OpenAI

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از SDK OpenAI با ورودی تصویر
response = client.chat.completions.create(
    model="gemini-robotics-er-1.5-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "اشیاء را شناسایی کنید و مختصات 2D آن‌ها را به فرمت JSON برگردانید",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/robot-scene.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-robotics-er-1.5-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای راهنمای جامع استفاده از Gemini Robotics-ER برای هوش مصنوعی در کاربردهای رباتیک، [هوش مصنوعی در رباتیک با Gemini Robotics-ER](fa/examples/ai_robotics_with_gemini_er.md) و [اعلامیه](fa/news/2025-10-28-gemini-robotics-er-model-added.md) را ببینید.


### Gemini 3.8 Flash TTS

مدل `gemini-3.8-flash-tts` انتخاب پیشنهادی برای تولید گفتار خلاقانه است: روایت استودیویی، کتاب صوتی، اجرای احساسی، لهجه‌های منطقه‌ای و گفت‌وگوهای پیچیده چندگوینده. این مدل کیفیت صدا و ثبات هویت گوینده را در گفتار طولانی و چندنوبتی در اولویت قرار می‌دهد و از ۱۳۰ زبان، از جمله فارسی، پشتیبانی می‌کند.

### Gemini 3.8 Flash-Lite TTS

مدل `gemini-3.8-flash-lite-tts` برای توان عملیاتی بالا پیشنهاد می‌شود: تولید انبوه، زنجیره‌های پردازش عامل صوتی با تأخیر کم، بلندخوانی و گفتار روزمره تک‌گوینده. این مدل از ۱۰۱ زبان، از جمله فارسی، پشتیبانی می‌کند و برای پردازش پرحجم جایگزین `gemini-3.1-flash-tts-preview` است.

هر دو مدل متن دریافت می‌کنند و صدا تولید می‌کنند. سقف ورودی ۸٬۱۹۲ توکن و سقف خروجی ارائه‌شده در Gemini API برابر با ۱۶٬۳۸۴ توکن است. ساختار درخواست گفتار در هر دو یکسان است؛ برای جابه‌جایی میان دو مدل ۳.۸ فقط شناسه مدل را تغییر دهید. برای کنترل خلاقانه و تلفظ دشوار، Flash و برای تأخیر کمتر، حجم بالا و هزینه بهینه، Flash-Lite را انتخاب کنید.

#### مسیرهای پشتیبانی‌شده در AvalAI

- `/v1beta/models/{model}:generateContent` — درخواست بومی Gemini با `speechMetadata` در هر بخش برای تعیین گوینده و سبک.
- `/v1/chat/completions` — پاسخ صوتی سازگار با OpenAI.
- `/v1/audio/speech` — تولید مستقیم گفتار.

مسیر قدیمی Vertex یعنی `/v1/text:synthesize` برای **هیچ‌یک از دو مدل Gemini 3.8 TTS پشتیبانی نمی‌شود**. قابلیت‌های مرجع گوگل مانند Extended Voice Library، Voice design و Voice replication به این معنی نیست که مسیرهای جداگانه آن‌ها در AvalAI ارائه می‌شوند.

[نمونه‌های گفتار در ادامه](#تولید-گفتار-تبدیل-متن-به-گفتار)، [مرجع API صوتی](fa/api-reference/audio.md) و [قیمت‌های فعلی](fa/pricing.md) را ببینید. قیمت‌ها و تخفیف‌های موقت در صفحه قیمت‌گذاری نگهداری می‌شوند و در اینجا تکرار نشده‌اند.

#### راهنمای قدیمی Gemini 2.5 در Vertex TTS

بخش‌های Gemini 2.5 و نمونه‌های Vertex زیر برای یکپارچه‌سازی‌های موجود حفظ شده‌اند؛ برای پروژه جدید از آن‌ها شروع نکنید. درخواست‌های `/v1/text:synthesize` باید شناسه مدل قدیمی خود را نگه دارند؛ آن را با شناسه ۳.۸ جایگزین نکنید. برای مهاجرت از ۳.۱ یا ۲.۵، از جمله نسخه‌های پیش‌نمایش، [راهنمای مهاجرت در ادامه](#مهاجرت-از-مدلهای-قدیمی-tts) را ببینید.

### Gemini 2.5 Flash TTS

Gemini 2.5 Flash TTS (`gemini-2.5-flash-tts`) مدل سریع و مقرون‌به‌صرفه تبدیل متن به گفتار گوگل است که برای برنامه‌های با حجم بالا که نیاز به تولید گفتار طبیعی دارند بهینه شده است.

| ویژگی | جزئیات |
| --------------------- | ------------------------------------------------------------------------------------- |
| پنجره زمینه | ۹۰۰ بایت برای هر فیلد متن، ۱۸۰۰ بایت ترکیبی (متن + پرامپت) |
| خروجی صوتی | ۳۲ توکن در هر ثانیه صدای تولید شده |
| ورودی‌ها | متن، پرامپت‌های استایل |
| خروجی | صدا (MP3، LINEAR16، OGG_OPUS، MULAW، ALAW) |
| زبان‌ها | 100+ زبان از جمله انگلیسی، اسپانیایی، فرانسوی، عربی، فارسی و غیره |
| صداها | 30+ صدای طبیعی |
| قیمت‌گذاری ورودی | ۰.۵۰ دلار / ۱ میلیون توکن (کاراکتر) |
| قیمت‌گذاری ورودی کش شده | ۰.۲۵ دلار / ۱ میلیون توکن |
| قیمت‌گذاری خروجی صوتی | ۱۰.۰۰ دلار / ۱ میلیون توکن (۳۲ توکن به ازای هر ثانیه) |
| قیمت‌گذاری خروجی متنی | ۱۰.۰۰ دلار / ۱ میلیون توکن |
| نقاط قوت | تولید سریع، مقرون‌به‌صرفه، پشتیبانی چند زبانه، صداهای طبیعی |
| بهترین برای | TTS با حجم بالا، هوش مصنوعی مکالمه‌ای، سرویس‌های دسترسی‌پذیری، روایت محتوا |

#### Endpointهای در دسترس
- `v1/chat/completions` - برای TTS در زمینه‌های مکالمه‌ای (سازگار با OpenAI)
- `v1/audio/speech` - برای تولید مستقیم TTS (سازگار با OpenAI)
- `v1/text:synthesize` - فرمت بومی Vertex AI با ویژگی‌های کامل

?> **توجه:** `gemini-2.5-flash-tts` یک مدل انحصاری Vertex AI است و از طریق endpoint Gemini API `v1beta` در دسترس نیست، اما از طریق چندین endpoint سازگار با OpenAI برای یکپارچه‌سازی آسان قابل دسترسی است.

#### استفاده سازگار با OpenAI

```python
# استفاده از فرمت SDK OpenAI - Audio Speech endpoint
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.audio.speech.create(
    model="gemini-2.5-flash-tts",
    voice="alloy",  # به صدای Gemini "Kore" نگاشت می‌شود
    input="سلام! به پلتفرم ما خوش آمدید.",
)

response.stream_to_file("speech.mp3")
```

#### دسترسی بومی قدیمی Vertex AI

```python
# استفاده از فرمت بومی Vertex AI با Google Cloud SDK
from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient(
    transport="rest",
    client_options={
        "api_endpoint": "https://api.avalai.ir",
        "api_key": os.getenv("AVALAI_API_KEY"),
    },
)

synthesis_input = texttospeech.SynthesisInput(text="سلام! به پلتفرم ما خوش آمدید.")

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR", name="Kore", model_name="gemini-2.5-flash-tts"
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
```

### Gemini 2.5 Pro TTS

Gemini 2.5 Pro TTS (`gemini-2.5-pro-tts`) مدل تبدیل متن به گفتار با کیفیت برتر گوگل با قابلیت کنترل پیشرفته برای نیازهای استایل پیچیده و سناریوهای چند گوینده است.

| ویژگی | جزئیات |
| --------------------- | ------------------------------------------------------------------------------------- |
| پنجره زمینه | ۹۰۰ بایت برای هر فیلد متن، ۱۸۰۰ بایت ترکیبی (متن + پرامپت) |
| خروجی صوتی | ۳۲ توکن در هر ثانیه صدای تولید شده |
| ورودی‌ها | متن، پرامپت‌های استایل، پیکربندی‌های چند گوینده |
| خروجی | صدا (MP3، LINEAR16، OGG_OPUS، MULAW، ALAW) |
| زبان‌ها | 100+ زبان از جمله انگلیسی، اسپانیایی، فرانسوی، عربی، فارسی و غیره |
| صداها | 30+ صدای طبیعی با کنترل پیشرفته آهنگ |
| قیمت‌گذاری ورودی | ۱.۰۰ دلار / ۱ میلیون توکن (کاراکتر) |
| قیمت‌گذاری ورودی کش شده | ۰.۵۰ دلار / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | ۲۰.۰۰ دلار / ۱ میلیون توکن (۳۲ توکن به ازای هر ثانیه) |
| نقاط قوت | کیفیت برتر، قابلیت کنترل پیشرفته، پشتیبانی چند گوینده، پرامپت‌های پیچیده |
| بهترین برای | کتاب‌های صوتی، محتوای پریمیوم، مکالمات چند گوینده، نیازهای استایل پیچیده |

#### Endpointهای در دسترس
- `v1/chat/completions` - برای TTS در زمینه‌های مکالمه‌ای (سازگار با OpenAI)
- `v1/audio/speech` - برای تولید مستقیم TTS (سازگار با OpenAI)
- `v1/text:synthesize` - فرمت بومی Vertex AI با ویژگی‌های کامل

?> **توجه:** `gemini-2.5-pro-tts` یک مدل انحصاری Vertex AI است و از طریق endpoint Gemini API `v1beta` در دسترس نیست، اما از طریق چندین endpoint سازگار با OpenAI برای یکپارچه‌سازی آسان قابل دسترسی است.

#### کنترل سبک در Vertex قدیمی

```python
# استفاده از فرمت بومی با پرامپت‌های استایل
from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient(
    transport="rest",
    client_options={
        "api_endpoint": "https://api.avalai.ir",
        "api_key": os.getenv("AVALAI_API_KEY"),
    },
)

synthesis_input = texttospeech.SynthesisInput(
    text="به آینده هوش مصنوعی خوش آمدید!",
    prompt="متن زیر را با لحنی هیجان‌زده و پرانرژی بگویید",
)

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR",
    name="Puck",  # صدای روشن و پرانرژی
    model_name="gemini-2.5-pro-tts",
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
```

#### مکالمات چندگوینده در Vertex قدیمی

```python
# تولید مکالمات چند گوینده
synthesis_input = texttospeech.SynthesisInput(
    text="Sam: سلام! Bob: سلام، حال شما چطور است؟ Sam: عالی هستم، ممنون!"
)

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR",
    model_name="gemini-2.5-pro-tts",
    multi_speaker_voice_config=texttospeech.MultiSpeakerVoiceConfig(
        speaker_voice_configs=[
            texttospeech.MultispeakerPrebuiltVoice(
                speaker_alias="Sam", speaker_id="Kore"  # must be English
            ),
            texttospeech.MultispeakerPrebuiltVoice(
                speaker_alias="Bob", speaker_id="Charon"  # must be English
            ),
        ]
    ),
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16, sample_rate_hertz=24000
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("conversation.wav", "wb") as out:
    out.write(response.audio_content)
```

برای نمونه‌های جامع و الگوهای استفاده پیشرفته، [اخبار: افزودن مدل‌های پیشرفته TTS و رونویسی](fa/news/2025-10-20-advanced-tts-and-transcription-models-added.md) و [مرجع API Vertex AI Text:Synthesize](fa/api-reference/v1-text-synthesize.md) را ببینید.

برای راهنمای جامع استفاده از Gemini 2.5 Flash Image [راهنمای تولید و ویرایش تصاویر با Gemini 2.5 Flash Image](fa/examples/generate_images_with_gemini_2_5_flash.md) ما را ببینید.

## مدل‌های Google Imagen (منسوخ شده)

> **منسوخ شده:** تمام مدل‌های Google Imagen (`imagen-4.0-ultra-generate-001`، `imagen-4.0-generate-001`، `imagen-4.0-fast-generate-001`، `imagen-3.0-generate-002`، `imagen-3.0-generate-001`، `imagen-3.0-fast-generate-001`) منسوخ شده و از فهرست AvalAI حذف شده‌اند. درخواست‌ها به این شناسه‌های مدل با خطا مواجه می‌شوند.

به‌جای آن‌ها از خانواده تصویری نانو بنانای گوگل استفاده کنید — به [تولید تصاویر با خانواده نانو بنانا](fa/examples/generate_images_with_nano_banana_series.md) مراجعه کنید:

| مدل بازنشسته Imagen | جایگزین |
| -------------------- | ----------- |
| `imagen-4.0-ultra-generate-001` | `gemini-3-pro-image` (نانو بنانا پرو) |
| `imagen-4.0-generate-001` | `gemini-3.1-flash-image` (نانو بنانا ۲) |
| `imagen-4.0-fast-generate-001` | `gemini-3.1-flash-image` (نانو بنانا ۲) |
| `imagen-3.0-generate-002` / `imagen-3.0-generate-001` / `imagen-3.0-fast-generate-001` | `gemini-3.1-flash-lite-image` (نانو بنانا ۲ لایت) |

برای جزئیات مهاجرت، به [راهنمای منسوخ‌شدن و مهاجرت مدل‌ها](fa/news/2026-09-04-model-deprecations-and-migration-guide.md) مراجعه کنید.

## قابلیت‌های کلیدی

### درک چندوجهی پیشرفته

مدل‌های Gemini 3.1، 3.0 و 2.5 از ترکیب‌های مختلف ورودی‌های متن، تصویر، صدا، ویدیو و PDF پشتیبانی می‌کنند که امکان تحلیل و استدلال عمیق در بین وجه‌ها را فراهم می‌کند.

#### قابلیت‌های درک تصویر

مدل‌های Gemini ویژگی‌های پیشرفته درک تصویر را ارائه می‌دهند:

1. **تشخیص اشیا با کادرهای محدودکننده**: مدل‌ها می‌توانند اشیا را در تصاویر شناسایی کرده و مختصات کادر محدودکننده آنها را در قالب [ymin, xmin, ymax, xmax]، نرمال‌سازی شده به 0-1000 ارائه دهند.

2. **قطعه‌بندی تصویر** (مدل‌های Gemini 2.5): فراتر از تشخیص، این مدل‌ها می‌توانند اشیا را قطعه‌بندی کرده و ماسک‌های کانتور آنها را به صورت PNG کدگذاری شده با base64 ارائه دهند.

3. **تحلیل چند تصویری**: مدل‌ها می‌توانند چندین تصویر را در یک پرامپت واحد پردازش و مقایسه کنند.

```python
# مثال: تحلیل تصویر با تشخیص اشیا
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "تمام اشیا برجسته در این تصویر را تشخیص دهید و کادرهای محدودکننده را در قالب [ymin, xmin, ymax, xmax] نرمال‌سازی شده به 0-1000 ارائه دهید.",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "data:image/jpeg;base64,..."
                    },  # برای مدل‌ها مانند Gemini ممکن است نیاز باشد از base64 به جای آدرس url استفاده کنید
                },
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


> **نکته مهم**: هنگام استفاده از مدل‌های Gemini از طریق AvalAI، تصاویر باید به صورت URL‌های داده کدگذاری شده با base64 ارائه شوند، نه به صورت URL‌های خارجی. این محدودیتی است که مختص مدل‌های Gemini است.

```python
# مثال: تحلیل ویدیو و متن
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "اقدامات اصلی در حال وقوع در این کلیپ ویدیویی را شرح دهید.",
                },
                {
                    "type": "video_url",
                    "video_url": {"url": "https://example.com/video.mp4"},
                },  # داده‌های ویدیو را به درستی ارائه دهید
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پنجره زمینه طولانی

مدل‌های Gemini 3.1، 3.0 و 2.5 دارای پنجره‌های زمینه ۱ میلیون توکنی یا بیشتر هستند که امکان تحلیل و استدلال روی حجم عظیمی از اطلاعات مانند کل پایگاه‌های کد، کتاب‌ها یا ساعت‌ها ویدیو/صدا را فراهم می‌کند.

### فراخوانی تابع و استفاده از ابزار

تمام مدل‌های مدرن Gemini از انواع مختلفی از ابزارها برای افزایش قابلیت‌های خود پشتیبانی می‌کنند، از جمله فراخوانی تابع، اجرای کد، جستجوی گوگل و پردازش زمینه URL.

#### فراخوانی تابع

فراخوانی تابع به مدل‌های Gemini اجازه می‌دهد با سیستم‌های خارجی تعامل داشته باشند یا داده‌های ساختاریافته بر اساس طرح‌های تعریف شده تولید کنند.

```python
# مثال: فراخوانی تابع
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[{"role": "user", "content": "هوای بوستون چطور است؟"}],
    tools=[
        {
            "functionDeclarations": [
                {
                    "name": "getWeather",
                    "description": "دریافت آب و هوای یک شهر درخواستی",
                    "parameters": {
                        "type": "object",
                        "properties": {"city": {"type": "string"}},
                    },
                },
            ]
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="هوای بوستون چطور است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### اجرای کد

ابزار اجرای کد به Gemini اجازه می‌دهد کد پایتون را تولید و اجرا کند تا مسائل پیچیده را حل کند. هنگامی که این ابزار فعال است، هیچ ابزار دیگری نمی‌تواند همزمان استفاده شود.

```python
# مثال: اجرای کد
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[{"role": "user", "content": "۱۰ عدد اول فیبوناچی را محاسبه کن"}],
    tools=[
        {"codeExecution": {}},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="۱۰ عدد اول فیبوناچی را محاسبه کن",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


محیط اجرای کد شامل کتابخانه‌های متعددی مانند matplotlib، numpy، pandas، scikit-learn، scipy، tensorflow و موارد دیگر است. حداکثر زمان اجرا ۳۰ ثانیه برای هر اجرا است، و محیط ممکن است در صورت بروز خطا تا ۵ بار تولید کد را تکرار کند.

برای عملیات ورودی/خروجی، اجرای کد از ورودی فایل (فایل‌های متنی و CSV) و خروجی نمودار (از طریق matplotlib) پشتیبانی می‌کند. حداکثر اندازه فایل ورودی توسط پنجره توکن مدل محدود می‌شود (حدود ۲ مگابایت برای فایل‌های متنی).

**قیمت‌گذاری**: هزینه اضافی برای فعال‌سازی اجرای کد فراتر از نرخ‌های استاندارد توکن وجود ندارد. توکن‌های نمایانگر کد تولید شده، نتایج اجرای کد و خلاصه نهایی همگی به عنوان توکن‌های خروجی محاسبه می‌شوند.

#### جستجوی گوگل

مدل‌های Gemini می‌توانند در صورت نیاز از جستجوی گوگل برای بازیابی اطلاعات به‌روز استفاده کنند. مدل می‌تواند بر اساس نیازهای پرسش تصمیم بگیرد که چه زمانی از جستجو استفاده کند. هنگامی که فعال است، پاسخ‌ها شامل منابع پایه (پیوندهای پشتیبانی درون‌خطی) و پیشنهادات جستجو هستند.

```python
# مثال: جستجوی گوگل
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[{"role": "user", "content": "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟"}],
    tools=[
        {"googleSearch": {}},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


می‌توانید رفتار جستجو را با پیکربندی اندازه زمینه جستجو سفارشی کنید:

```python
# مثال: جستجوی گوگل با سطح جزئیات بالا
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
        }
    ],
    tools=[
        {"googleSearch": {"detail_level": "high"}},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


گزینه‌های اندازه زمینه جستجو عبارتند از:
- **low**: کمتر جامع اما سریع‌تر و ارزان‌تر
- **medium**: تنظیم پیش‌فرض، رویکرد متعادل
- **high**: نتایج جامع‌تر اما هزینه بالاتر

**قیمت‌گذاری**: قیمت‌گذاری جستجوی وب به مدل مورد استفاده و اندازه زمینه جستجو بستگی دارد، با هزینه‌هایی از ۲۵.۰۰ تا ۵۰.۰۰ دلار به ازای هر ۱۰۰۰ فراخوانی بسته به مدل و سطح جزئیات.

**توجه**: برای مدل‌های Gemini 2.5 و بعدی، از جستجو به عنوان یک ابزار همانطور که در بالا نشان داده شده استفاده کنید.

##### API بومی Gemini (v1beta) برای جستجوی گوگل

همچنین می‌توانید از API بومی v1beta گوگل برای ویژگی‌های پیشرفته‌تر پایه‌گذاری استفاده کنید، از جمله دسترسی به متادیتای پایه‌گذاری دقیق با استنادات و اطلاعات منبع.

```bash
# استفاده از API بومی Gemini v1beta با cURL
curl "https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -X POST \
  -d '{
    "contents": [
      {
        "parts": [
          {"text": "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟"}
        ]
      }
    ],
    "tools": [
      {
        "google_search": {}
      }
    ]
  }'
```

```python
# استفاده با SDK Google GenAI
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
    config=types.GenerateContentConfig(
        tools=[types.Tool(google_search=types.GoogleSearch())]
    ),
)

print(response.text)

# دسترسی به متادیتای پایه‌گذاری برای استنادات
if response.candidates[0].grounding_metadata:
    metadata = response.candidates[0].grounding_metadata
    print(f"پرس‌وجوهای جستجوی استفاده‌شده: {metadata.web_search_queries}")
    for chunk in metadata.grounding_chunks:
        print(f"منبع: {chunk.web.title} - {chunk.web.uri}")
```

API بومی `groundingMetadata` دقیقی برمی‌گرداند که شامل:
- `webSearchQueries`: آرایه‌ای از پرس‌وجوهای جستجوی استفاده‌شده
- `groundingChunks`: آرایه‌ای از منابع وب (uri و title)
- `groundingSupports`: پیوند بخش‌های متن پاسخ به منابع برای استنادات درون‌خطی

برای مستندات دقیق درباره API بومی، [مرجع API v1beta](fa/api-reference/v1beta.md#پایه‌گذاری-با-جستجوی-گوگل-grounding-with-google-search) را ببینید.

#### زمینه URL

این ویژگی آزمایشی به مدل‌های Gemini اجازه می‌دهد محتوای URL‌های ارائه شده در پرامپت‌ها را بازیابی و تحلیل کنند. مدل می‌تواند اطلاعات کلیدی را از صفحات وب استخراج کرده و از آن برای پاسخ‌های خود استفاده کند. این ویژگی فقط در مدل‌های پشتیبانی شده زیر در دسترس است:

- gemini-3.5-flash
- gemini-3.1-pro-preview
- gemini-3.1-flash-lite
- gemini-3.1-flash-lite-preview
- gemini-3-flash-preview
- gemini-2.5-pro
- gemini-2.5-flash

```python
# مثال: زمینه URL (می‌تواند با جستجوی گوگل ترکیب شود)
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {
            "role": "user",
            "content": "این مقاله را خلاصه کن: https://example.com/article",
        }
    ],
    tools=[
        {"urlContext": {}},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Explain how AvalAI provides a unified API for this request.",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


زمینه URL به ویژه برای وظایف زیر مفید است:
- استخراج نکات کلیدی از مقالات
- مقایسه اطلاعات در چندین لینک
- ترکیب داده‌ها از چندین منبع
- پاسخ به سؤالات بر اساس محتوای خاص وب

**محدودیت‌ها**:
- این ابزار تا ۲۰ URL در هر درخواست را پردازش می‌کند
- بهترین عملکرد را با صفحات وب استاندارد دارد نه محتوای چندرسانه‌ای
- بازیابی URL منجر به افزایش مصرف توکن می‌شود

می‌توانید از زمینه URL به تنهایی یا در ترکیب با جستجوی گوگل استفاده کنید تا مدل بتواند هم اطلاعات مرتبط را کشف کند و هم آن را به طور عمیق تحلیل نماید.

برای اطلاعات بیشتر، [مستندات رسمی در مورد زمینه URL](https://ai.google.dev/gemini-api/docs/url-context) را ببینید.

> **توجه**: محدودیت‌های سازگاری ابزارها:
>
> - هنگامی که اجرای کد فعال است، هیچ ابزار دیگری نمی‌تواند استفاده شود
> - اعلان‌های تابع فقط می‌توانند به تنهایی استفاده شوند
> - جستجوی گوگل فقط می‌تواند با زمینه URL ترکیب شود

### خروجی ساختاریافته (حالت JSON)

می‌توان به مدل‌های Gemini دستور داد تا خروجی‌ها را در قالب‌های خاصی مانند JSON تولید کنند که برای یکپارچه‌سازی API و استخراج داده‌های ساختاریافته مفید است.

```python
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {"role": "system", "content": "فقط JSON خروجی دهید."},
        {"role": "user", "content": "۳ زبان برنامه‌نویسی برتر را لیست کنید."},
    ],
    response_format={"type": "json_object"},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="۳ زبان برنامه‌نویسی برتر را لیست کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## راهنمای انتخاب مدل

### انتخاب مدل Gemini مناسب

هنگام انتخاب مدل Gemini از طریق AvalAI، موارد زیر را در نظر بگیرید:

1. **پیچیدگی وظیفه و نیاز به استدلال**: Gemini 3.5 Flash گزینه پرچم‌دار Flash برای استدلال قوی، کدنویسی و گردش‌کارهای عاملی است. Gemini 3.1 Pro استدلال پیشرفته کلاس Pro ارائه می‌دهد. Gemini 3.1 Flash-Lite زمانی بهترین است که هزینه و تأخیر مهم‌ترین معیارها باشند.
2. **طول زمینه**: مدل‌های Gemini 3.5، 3.1، 3 و 2.5 حداقل از ۱ میلیون توکن پشتیبانی می‌کنند.
3. **نیازهای چندوجهی**: آیا به ورودی صدا/ویدیو نیاز دارید؟ خروجی تصویر (مدل‌های تصویری Gemini)؟
4. **سرعت در مقابل هزینه**: مدل‌های Flash و Flash-Lite به طور قابل توجهی سریع‌تر و ارزان‌تر هستند و برای برنامه‌های بلادرنگ یا با حجم بالا مناسب‌اند. مدل‌های Pro کیفیت بالاتری را با هزینه/تاخیر بیشتر ارائه می‌دهند.
5. **اندازه خروجی**: Gemini 3.5 Flash و 3.1 Pro تا ۶۵ هزار توکن خروجی مجاز می‌دانند.

### مقایسه عملکرد

| وظیفه                          | مدل Gemini پیشنهادی           | مدل‌های جایگزین               |
| ------------------------------ | ----------------------------- | ----------------------------- |
| استدلال پیچیده / تحقیق         | Gemini 3.1 Pro Preview        | Gemini 3.5 Flash، Claude Opus 4.7، GPT-5.5 |
| کدنویسی عاملی / استفاده از ابزار | Gemini 3.5 Flash              | Gemini 3.1 Pro Preview، GPT-5.5 |
| چت با کیفیت بالا / تولید محتوا | Gemini 3.5 Flash              | Claude Sonnet 4.6، GPT-5.5 |
| تحلیل اسناد طولانی             | Gemini 3.5 Flash / 3.1 Pro    | سری Claude 4 (زمینه ۲۰۰ هزار) |
| تحلیل چندوجهی (ویدیو/صدا)      | Gemini 3.5 Flash              | Gemini 3.1 Pro Preview، GPT-5.2-chat |
| بلادرنگ / حجم بالا             | Gemini 3.1 Flash-Lite         | Gemini 3 Flash، Claude Haiku 4.5 |

## بهترین شیوه‌ها برای مدل‌های Gemini

### پرامپت‌نویسی مؤثر

دستورالعمل‌های واضح و مشخص ارائه دهید. جزئیات قالب، شخصیت، محدودیت‌ها و زمینه مورد نظر را شرح دهید.

### دستورالعمل‌های سیستمی

از نقش `system` به طور مؤثر برای هدایت رفتار، شخصیت و سبک پاسخ مدل به طور مداوم استفاده کنید.

### پرامپت‌نویسی چندوجهی

هنگام استفاده از ورودی‌های چندوجهی (تصاویر، صدا، ویدیو)، اطمینان حاصل کنید که به وضوح به آن‌ها ارجاع داده شده یا با دستورالعمل‌های متنی که توضیح می‌دهد مدل باید با آن‌ها چه کاری انجام دهد، در هم آمیخته شده‌اند.

### تنظیمات Temperature و Top_P

`temperature` و `top_p` را برای کنترل تصادفی بودن تنظیم کنید. مقادیر پایین‌تر (مثلا temp=0.2) خروجی‌های قطعی‌تر و متمرکزتری تولید می‌کنند. مقادیر بالاتر (مثلا temp=0.8) خلاقیت و تنوع را تشویق می‌کنند.

## استفاده از مدل‌های Gemini از طریق AvalAI

تمام مدل‌های Gemini از طریق نقاط پایانی استاندارد API AvalAI با استفاده از کتابخانه‌های کلاینت سازگار با OpenAI قابل دسترسی هستند:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

# از هر مدل Gemini با شناسه AvalAI آن استفاده کنید
response = client.chat.completions.create(
    model="gemini-2.5-pro", messages=[{"role": "user", "content": "سلام!"}]
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="سلام!",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## پشتیبانی از SDK بومی Google GenAI

AvalAI اکنون از دسترسی بومی به مدل‌های Gemini با استفاده از SDK رسمی GenAI گوگل پشتیبانی می‌کند و گزینه سوم SDK را در کنار رویکردهای سازگار با OpenAI و بومی Anthropic ارائه می‌دهد.

### استفاده از SDK بومی گوگل

#### تولید متن پایه

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "هوش مصنوعی چگونه کار می‌کند؟"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 500
    },
    "model": "gemini-2.5-flash"
  }'

```

```python
from google import genai

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_content(
    model="gemini-2.5-flash", contents="هوش مصنوعی چگونه کار می‌کند؟"
)
print(response.text)

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "هوش مصنوعی چگونه کار می‌کند؟",
    });
    console.log(response.text);
}

await main();

```

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("هوش مصنوعی چگونه کار می‌کند؟"),
		nil,
	)

	fmt.Println(result.Text())
}

```

#### دستورالعمل‌های سیستمی

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    config=types.GenerateContentConfig(
        system_instruction="شما یک گربه هستید. نام شما نکو است."
    ),
    contents="سلام",
)

print(response.text)

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "سلام",
        config: {
            systemInstruction: "شما یک گربه هستید. نام شما نکو است.",
        },
    });
    console.log(response.text);
}

await main();

```

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	config := &genai.GenerateContentConfig{
		SystemInstruction: genai.NewContentFromText("شما یک گربه هستید. نام شما نکو است.", genai.RoleUser),
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("سلام"),
		config,
	)

	fmt.Println(result.Text())
}

```


#### پیکربندی تفکر (مدل‌های Gemini 2.5)

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "هوش مصنوعی چگونه کار می‌کند؟"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "thinkingConfig": {
            "thinkingBudget": 0
        },
        "maxOutputTokens": 500,
        "temperature": 0.7
    },
    "model": "gemini-2.5-flash"
  }'

```

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="هوش مصنوعی چگونه کار می‌کند؟",
    config=types.GenerateContentConfig(
        thinking_config=types.ThinkingConfig(thinking_budget=0)  # تفکر را غیرفعال می‌کند
    ),
)
print(response.text)

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "هوش مصنوعی چگونه کار می‌کند؟",
        config: {
            thinkingConfig: {
                thinkingBudget: 0, // تفکر را غیرفعال می‌کند
            },
        }
    });
    console.log(response.text);
}

await main();

```

```go
package main

import (
    "context"
    "fmt"
    "google.golang.org/genai"
)

func main() {
    ctx := context.Background()
    client, err := genai.NewClient(ctx, &genai.ClientConfig{
        APIKey: "your-avalai-api-key",
        BaseURL: "https://api.avalai.ir",
    })
    if err != nil {
        log.Fatal(err)
    }

    result, _ := client.Models.GenerateContent(
        ctx,
        "gemini-2.5-flash",
        genai.Text("هوش مصنوعی چگونه کار می‌کند؟"),
        &genai.GenerateContentConfig{
            ThinkingConfig: &genai.ThinkingConfig{
                ThinkingBudget: int32(0), // تفکر را غیرفعال می‌کند
            },
        }
    )

    fmt.Println(result.Text())
}

```


#### پاسخ‌های جریانی

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:streamGenerateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "هوش مصنوعی چگونه کار می‌کند را توضیح دهید"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 1000
    }
}' --no-buffer

```

```python
from google import genai

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)

response = client.models.generate_content_stream(
    model="gemini-2.5-flash", contents=["هوش مصنوعی چگونه کار می‌کند را توضیح دهید"]
)
for chunk in response:
    print(chunk.text, end="")

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const response = await ai.models.generateContentStream({
        model: "gemini-2.5-flash",
        contents: "هوش مصنوعی چگونه کار می‌کند را توضیح دهید",
    });

    for await (const chunk of response) {
        console.log(chunk.text);
    }
}

await main();

```

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	stream := client.Models.GenerateContentStream(
		ctx,
		"gemini-2.5-flash",
		genai.Text("داستانی درباره کوله‌پشتی جادویی بنویسید."),
		nil,
	)

	for chunk, _ := range stream {
		part := chunk.Candidates[0].Content.Parts[0]
		fmt.Print(part.Text)
	}
}

```

#### مکالمات چندمرحله‌ای (چت)

```bash
# پیام اول
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "من ۲ سگ در خانه‌ام دارم."}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 300
    },
    "model": "gemini-2.5-flash"
  }'

# پیام پیگیری با تاریخچه مکالمه
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "من ۲ سگ در خانه‌ام دارم."}],
            "role": "user"
        },
        {
            "parts": [{"text": "چه عالی! سگ‌ها دوستان فوق‌العاده‌ای هستند."}],
            "role": "model"
        },
        {
            "parts": [{"text": "چند پنجه در خانه‌ام هست؟"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 200
    },
    "model": "gemini-2.5-flash"
  }'

```

```python
from google import genai

client = genai.Client(
    api_key="your-avalai-api-key", http_options={"base_url": "https://api.avalai.ir"}
)
chat = client.chats.create(model="gemini-2.5-flash")

response = chat.send_message("من ۲ سگ در خانه‌ام دارم.")
print(response.text)

response = chat.send_message("چند پنجه در خانه‌ام هست؟")
print(response.text)

for message in chat.get_history():
    print(f"نقش - {message.role}", end=": ")
    print(message.parts[0].text)

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const chat = ai.chats.create({
        model: "gemini-2.5-flash",
        history: [
            {
                role: "user",
                parts: [{ text: "سلام" }],
            },
            {
                role: "model",
                parts: [{ text: "خوشحالم که شما را ملاقات کردم. چه چیزی می‌خواهید بدانید؟" }],
            },
        ],
    });

    const response1 = await chat.sendMessage({
        message: "من ۲ سگ در خانه‌ام دارم.",
    });
    console.log("پاسخ چت ۱:", response1.text);

    const response2 = await chat.sendMessage({
        message: "چند پنجه در خانه‌ام هست؟",
    });
    console.log("پاسخ چت ۲:", response2.text);
}

await main();

```

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	history := []*genai.Content{
		genai.NewContentFromText("سلام، خوشحالم که شما را ملاقات کردم! من ۲ سگ در خانه‌ام دارم.", genai.RoleUser),
		genai.NewContentFromText("خوشحالم که شما را ملاقات کردم. چه چیزی می‌خواهید بدانید؟", genai.RoleModel),
	}

	chat, _ := client.Chats.Create(ctx, "gemini-2.5-flash", nil, history)
	res, _ := chat.SendMessage(ctx, genai.Part{Text: "چند پنجه در خانه‌ام هست؟"})

	if len(res.Candidates) > 0 {
		fmt.Println(res.Candidates[0].Content.Parts[0].Text)
	}
}

```


### دسترسی مستقیم API

همچنین می‌توانید مستقیما از نقاط پایانی بومی استفاده کنید:

```bash
# تولید متن پایه
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "هایکویی درباره هوش مصنوعی بنویس"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 100
    },
    "model": "gemini-2.5-flash"
  }'

# استفاده از دستورالعمل‌های سیستمی برای رفتار سفارشی
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "system_instruction": {
        "parts": [
            {
                "text": "شما یک دستیار خلاق شعر هستید. به سبک شاعرانه و تخیلی بنویسید."
            }
        ]
    },
    "contents": [
        {
            "parts": [{"text": "هایکویی درباره هوش مصنوعی بنویس"}],
            "role": "user"
        }
    ],
    "generationConfig": {
        "thinkingConfig": {
            "thinkingBudget": 0
        },
        "maxOutputTokens": 100,
        "temperature": 0.8
    },
    "model": "gemini-2.5-flash"
  }'
```

> **مهم**: API v1beta با [مستندات رسمی API Gemini](https://ai.google.dev/gemini-api/docs/text-generation) سازگار است. برای رفتار سفارشی از `system_instruction` استفاده کنید، نه دستورالعمل‌های مبتنی بر نقش. برای تناقضات، با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

### تنظیمات ایمنی

API Gemini تنظیمات ایمنی قابل تنظیم را فراهم می‌کند که می‌توانید آنها را پیکربندی کنید تا تعیین کنید آیا برنامه شما نیاز به پیکربندی ایمنی محدودتر یا آزادتر دارد. می‌توانید این تنظیمات را در چهار دسته فیلتر برای محدود کردن یا اجازه انواع خاصی از محتوا تنظیم کنید.

#### دسته‌های آسیب

| دسته | توضیحات |
|----------|-------------|
| `HARM_CATEGORY_HARASSMENT` | نظرات منفی یا مضر که هویت و/یا ویژگی‌های محافظت‌شده را هدف قرار می‌دهند |
| `HARM_CATEGORY_HATE_SPEECH` | محتوایی که بی‌ادبانه، بی‌احترامانه یا توهین‌آمیز است |
| `HARM_CATEGORY_SEXUALLY_EXPLICIT` | شامل ارجاعات به اعمال جنسی یا محتوای هرزه دیگر |
| `HARM_CATEGORY_DANGEROUS_CONTENT` | اعمال مضر را ترویج، تسهیل یا تشویق می‌کند |

#### آستانه‌های مسدودسازی

می‌توانید سیستم را برای مسدود کردن محتوا بر اساس احتمال ناامن بودن آن پیکربندی کنید:

| آستانه | توضیحات |
|-----------|-------------|
| `OFF` | خاموش کردن فیلتر ایمنی |
| `BLOCK_NONE` | همیشه نمایش بده صرف‌نظر از احتمال محتوای ناامن |
| `BLOCK_ONLY_HIGH` | مسدود کن وقتی احتمال بالای محتوای ناامن وجود دارد |
| `BLOCK_MEDIUM_AND_ABOVE` | مسدود کن وقتی احتمال متوسط یا بالای محتوای ناامن وجود دارد |
| `BLOCK_LOW_AND_ABOVE` | مسدود کن وقتی احتمال پایین، متوسط یا بالای محتوای ناامن وجود دارد |
| `HARM_BLOCK_THRESHOLD_UNSPECIFIED` | آستانه مشخص نشده است، با استفاده از آستانه پیش‌فرض مسدود کن |

> **نکته**: اگر آستانه تنظیم نشده باشد، آستانه مسدودسازی پیش‌فرض برای مدل‌های Gemini 2.5 و 3 `OFF` است.

#### استفاده از تنظیمات ایمنی با API بومی

```bash
curl -X POST 'https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent' \
  -H 'Content-Type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
    "contents": [
        {
            "parts": [{"text": "پرامپت شما اینجا"}],
            "role": "user"
        }
    ],
    "safetySettings": [
        {
            "category": "HARM_CATEGORY_HARASSMENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_HATE_SPEECH",
            "threshold": "BLOCK_LOW_AND_ABOVE"
        },
        {
            "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
            "threshold": "BLOCK_ONLY_HIGH"
        },
        {
            "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
            "threshold": "BLOCK_MEDIUM_AND_ABOVE"
        }
    ],
    "generationConfig": {
        "maxOutputTokens": 500
    },
    "model": "gemini-2.5-flash"
  }'

```

```python
from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# پیکربندی تنظیمات ایمنی
safety_settings = [
    types.SafetySetting(
        category="HARM_CATEGORY_HARASSMENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_HATE_SPEECH",
        threshold="BLOCK_LOW_AND_ABOVE",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_SEXUALLY_EXPLICIT",
        threshold="BLOCK_ONLY_HIGH",
    ),
    types.SafetySetting(
        category="HARM_CATEGORY_DANGEROUS_CONTENT",
        threshold="BLOCK_MEDIUM_AND_ABOVE",
    ),
]

response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="پرامپت شما اینجا",
    config=types.GenerateContentConfig(safety_settings=safety_settings),
)

print(response.text)

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: "your-avalai-api-key",
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

async function main() {
    const response = await ai.models.generateContent({
        model: "gemini-2.5-flash",
        contents: "پرامپت شما اینجا",
        config: {
            safetySettings: [
                {
                    category: "HARM_CATEGORY_HARASSMENT",
                    threshold: "BLOCK_MEDIUM_AND_ABOVE"
                },
                {
                    category: "HARM_CATEGORY_HATE_SPEECH",
                    threshold: "BLOCK_LOW_AND_ABOVE"
                },
                {
                    category: "HARM_CATEGORY_SEXUALLY_EXPLICIT",
                    threshold: "BLOCK_ONLY_HIGH"
                },
                {
                    category: "HARM_CATEGORY_DANGEROUS_CONTENT",
                    threshold: "BLOCK_MEDIUM_AND_ABOVE"
                }
            ]
        }
    });
    console.log(response.text);
}

await main();

```

```go
package main

import (
	"context"
	"fmt"
	"google.golang.org/genai"
)

func main() {
	ctx := context.Background()
	client, err := genai.NewClient(ctx, &genai.ClientConfig{
		APIKey:  "your-avalai-api-key",
		BaseURL: "https://api.avalai.ir",
	})
	if err != nil {
		log.Fatal(err)
	}

	result, _ := client.Models.GenerateContent(
		ctx,
		"gemini-2.5-flash",
		genai.Text("پرامپت شما اینجا"),
		&genai.GenerateContentConfig{
			SafetySettings: []*genai.SafetySetting{
				{
					Category:  genai.HarmCategoryHarassment,
					Threshold: genai.HarmBlockThresholdBlockMediumAndAbove,
				},
				{
					Category:  genai.HarmCategoryHateSpeech,
					Threshold: genai.HarmBlockThresholdBlockLowAndAbove,
				},
				{
					Category:  genai.HarmCategorySexuallyExplicit,
					Threshold: genai.HarmBlockThresholdBlockOnlyHigh,
				},
				{
					Category:  genai.HarmCategoryDangerousContent,
					Threshold: genai.HarmBlockThresholdBlockMediumAndAbove,
				},
			},
		},
	)

	fmt.Println(result.Text())
}

```


#### بازخورد ایمنی در پاسخ‌ها

هنگامی که درخواستی ارسال می‌کنید، محتوا تحلیل شده و یک رتبه‌بندی ایمنی به آن اختصاص داده می‌شود. پاسخ شامل بازخورد ایمنی است:

- **بازخورد پرامپت**: در `promptFeedback` شامل می‌شود. اگر `promptFeedback.blockReason` تنظیم شده باشد، محتوای پرامپت مسدود شده است.
- **بازخورد کاندیدای پاسخ**: در `Candidate.finishReason` و `Candidate.safetyRatings` شامل می‌شود. اگر محتوای پاسخ مسدود شده و `finishReason` برابر `SAFETY` باشد، می‌توانید `safetyRatings` را برای جزئیات بیشتر بررسی کنید.

```python
# بررسی رتبه‌بندی‌های ایمنی در پاسخ
response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents="پرامپت شما اینجا",
    config=types.GenerateContentConfig(safety_settings=safety_settings),
)

# بررسی اینکه آیا پرامپت مسدود شده است
if response.prompt_feedback and response.prompt_feedback.block_reason:
    print(f"پرامپت مسدود شد: {response.prompt_feedback.block_reason}")

# بررسی رتبه‌بندی‌های ایمنی کاندید
for candidate in response.candidates:
    if candidate.finish_reason == "SAFETY":
        print("پاسخ به دلیل ایمنی مسدود شد")
        for rating in candidate.safety_ratings:
            print(f"  {rating.category}: {rating.probability}")
```

> **نکته**: برنامه‌هایی که از تنظیمات ایمنی کمتر محدودکننده استفاده می‌کنند ممکن است مشمول بررسی شوند. برای اطلاعات بیشتر [شرایط خدمات](https://ai.google.dev/terms) را ببینید.

### ویژگی‌های کلیدی پشتیبانی بومی

- **طرحواره API بومی**: دسترسی مستقیم با استفاده از نقاط پایانی `generateContent`، `streamGenerateContent`، `embedContent`، `batchEmbedContents` و `countTokens` گوگل
- **احراز هویت انعطاف‌پذیر**: پشتیبانی از هر دو هدر `Authorization: Bearer` و `x-goog-api-key`
- **پشتیبانی کامل از جریان**: جریان بومی با `agenerate_content_stream`
- **قابلیت‌های چندوجهی**: پشتیبانی بومی از ورودی‌های متن، تصویر، صدا و ویدیو
- **تولید تعبیه‌سازی**: پشتیبانی بومی از تعبیه‌سازی متن با انواع وظایف و ابعاد قابل تنظیم
- **شمارش توکن**: شمارش توکن داخلی برای ردیابی دقیق استفاده قبل از فراخوانی API

### محدودیت‌های مهم

- **فقط مدل‌های Gemini**: پشتیبانی بومی منحصرا برای مدل‌های Gemini است
- **URL پایه**: از `https://api.avalai.ir` (بدون `/v1`) برای SDK Google GenAI استفاده کنید
- **نقاط پایانی v1beta**: نقاط پایانی بومی از فرمت `/v1beta/models/{model}:generateContent` استفاده می‌کنند

برای مستندات کامل API بومی، [مرجع API v1beta](fa/api-reference/v1beta.md) را ببینید.

## تفاوت‌ها با مدل‌های OpenAI/Anthropic

در حالی که AvalAI یک API یکپارچه ارائه می‌دهد، تفاوت‌های ظریفی وجود دارد:

1. **قابلیت‌های چندوجهی**: Gemini قابلیت‌های پردازش صدا/ویدیو متمایزی نسبت به دیگران ارائه می‌دهد.
2. **فراخوانی تابع**: جزئیات پیاده‌سازی و قابلیت اطمینان ممکن است کمی متفاوت باشد.
3. **اثرات پارامتر**: پارامترهایی مانند `temperature` ممکن است در خانواده‌های مختلف مدل رفتار متفاوتی داشته باشند.
4. **حالت JSON**: حالت JSON بومی Gemini ممکن است با `json_object` OpenAI یا ساختار XML Anthropic متفاوت باشد.

AvalAI تلاش می‌کند این تفاوت‌ها را عادی‌سازی کند، اما آگاهی می‌تواند به بهینه‌سازی پرامپت‌ها کمک کند.

## نسخه‌بندی مدل

گوگل به طور منظم نسخه‌های به‌روز شده را منتشر می‌کند. AvalAI با استفاده از نام‌های مستعار عمومی و اسنپ‌شات‌های نسخه خاص دسترسی را فراهم می‌کند:

- نام‌های مستعار عمومی: `gemini-3.1-pro`, `gemini-3-flash`, `gemini-2.5-pro`
- اسنپ‌شات‌های خاص: به عنوان مثال  `gemini-3.1-pro-preview`, `gemini-3-flash-preview` و غیره.

استفاده از یک اسنپ‌شات خاص، رفتار ثابت را در طول زمان تضمین می‌کند. برای آخرین اسنپ‌شات‌های موجود، صفحه [جزئیات مدل](fa/models/model-details.md) را بررسی کنید.

## منابع مرتبط

- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API تعبیه‌سازی](fa/api-reference/embeddings.md)
- [مرجع API آوا](fa/api-reference/audio.md)
- [مرجع API نظارت](fa/api-reference/moderation.md)
- [احراز هویت](fa/api-reference/authentication.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)

## مدل‌های Gemma 4

خانواده Gemma 4 هوشمندترین مدل‌های باز گوگل است که از تحقیقات و فناوری Gemini 3 ساخته شده‌اند تا هوش به ازای هر پارامتر را به حداکثر برسانند. این مدل‌ها کارایی بی‌سابقه‌ای با قابلیت‌های چندحالتی، چندزبانه و عاملی قوی ارائه می‌دهند.

| ویژگی              | جزئیات                                                                   |
| ------------------ | ------------------------------------------------------------------------ |
| پنجره زمینه        | تا ۱۲۸ هزار توکن                                                         |
| اندازه‌های موجود   | ۲۶ میلیارد A4B (MoE)، ۳۱ میلیارد (متراکم)، E2B، E4B                      |
| قابلیت‌های چندحالتی | ورودی تصویر، صدا و متن                                                   |
| پشتیبانی زبان      | بیش از ۱۴۰ زبان                                                          |
| ویژگی‌های کلیدی    | حالت تفکر، فراخوانی تابع، گردش‌های کاری عاملی، تنظیم دقیق                |
| بهترین استفاده     | IDE، دستیاران کدنویسی، گردش‌های کاری عاملی، استقرار GPU مصرفی           |

### gemma-4-26b-a4b-it

مدل باز گوگل با معماری Mixture-of-Experts (۲۶ میلیارد کل، ۴ میلیارد فعال)، ارائه کارایی هوش به ازای هر پارامتر بی‌سابقه.

| ویژگی | جزئیات |
|-------|--------|
| کل پارامترها | ۲۶ میلیارد (۴ میلیارد فعال) |
| معماری | Mixture-of-Experts (MoE) |
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن |
| قیمت ورودی | ۰.۱۳ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۰۱۳ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | ۰.۴۰ دلار / ۱ میلیون توکن |
| ورودی‌های پشتیبانی‌شده | متن، تصویر، صدا |
| خروجی‌های پشتیبانی‌شده | متن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions`، `v1/responses` |

**ویژگی‌های کلیدی:**
- **هوش پیشرو**: ساخته شده از تحقیقات Gemini 3 برای حداکثر هوش به ازای هر پارامتر
- **معماری MoE**: ۲۶ میلیارد پارامتر کل با فقط ۴ میلیارد فعال برای کارایی
- **چندحالتی**: درک قوی صدا و تصویر
- **گردش‌های کاری عاملی**: پشتیبانی بومی از فراخوانی تابع و عامل‌های خودمختار
- **۱۴۰ زبان**: پشتیبانی چندزبانه فراتر از ترجمه
- **حالت تفکر**: استدلال گسترده برای مسائل پیچیده

**عملکرد معیار:**
- Arena AI (متن): ۱۴۴۱
- MMMLU: ۸۲.۶٪
- MMMU Pro: ۷۳.۸٪
- AIME 2026: ۸۸.۳٪
- LiveCodeBench v6: ۷۷.۱٪
- GPQA Diamond: ۸۲.۳٪

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemma-4-26b-a4b-it",
    messages=[
        {
            "role": "user",
            "content": "مزایای معماری MoE در LLMها را توضیح دهید",
        },
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemma-4-26b-a4b-it` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="مزایای معماری MoE در LLMها را توضیح دهید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### gemma-4-31b-it

نسخه متراکم Gemma 4 از گوگل، ارائه حداکثر قابلیت با استفاده کامل از پارامتر. بالاترین امتیاز Arena AI ELO (۱۴۵۲) برای کلاس اندازه خود.

| ویژگی | جزئیات |
|-------|--------|
| پارامترها | ۳۱ میلیارد |
| معماری | ترنسفورمر متراکم |
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن |
| قیمت ورودی | ۰.۱۴ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۰۱۴ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | ۰.۴۰ دلار / ۱ میلیون توکن |
| ورودی‌های پشتیبانی‌شده | متن، تصویر، صدا |
| خروجی‌های پشتیبانی‌شده | متن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **کارایی پیشرو در صنعت**: بالاترین امتیاز Arena AI ELO (۱۴۵۲) برای کلاس اندازه خود
- **معماری متراکم**: ۳۱ میلیارد پارامتر کامل فعال برای حداکثر قابلیت
- **استدلال چندحالتی**: درک قوی صدا و تصویر
- **گردش‌های کاری عاملی**: فراخوانی تابع بومی و پشتیبانی از عامل
- **تنظیم دقیق**: بهبود عملکرد برای وظایف خاص با استفاده از فریم‌ورک‌های مورد نظر شما
- **حالت تفکر**: قابلیت‌های استدلال گسترده

**عملکرد معیار:**
- Arena AI (متن): ۱۴۵۲
- MMMLU: ۸۵.۲٪
- MMMU Pro: ۷۶.۹٪
- AIME 2026: ۸۹.۲٪
- LiveCodeBench v6: ۸۰.۰٪
- GPQA Diamond: ۸۴.۳٪
- τ2-bench Retail: ۸۶.۴٪

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemma-4-31b-it",
    messages=[
        {
            "role": "user",
            "content": "یک راه‌حل جامع برای بهینه‌سازی یک سیستم توزیع‌شده طراحی کنید",
        },
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemma-4-31b-it` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک راه‌حل جامع برای بهینه‌سازی یک سیستم توزیع‌شده طراحی کنید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## مدل‌های Gemma 3

خانواده Gemma 3 نماینده جدیدترین مدل‌های وزن-باز گوگل است که برای دسترسی گسترده در محیط‌های محاسباتی مختلف طراحی شده است.

| ویژگی              | جزئیات                                                                   |
| ------------------ | ------------------------------------------------------------------------ |
| پنجره زمینه        | تا ۱۲۸ هزار توکن                                                         |
| اندازه‌های موجود   | ۱ میلیارد (فقط متن)، ۴ میلیارد، ۱۲ میلیارد، ۲۷ میلیارد، و نسخه تخصصی e4B |
| قابلیت‌های چندوجهی | ورودی تصویر و متن (به جز مدل ۱ میلیاردی که فقط متنی است)                 |
| پشتیبانی زبان      | بیش از ۱۴۰ زبان                                                          |
| ویژگی‌های کلیدی    | فراخوانی تابع، پشتیبانی گسترده زبان، قابلیت‌های چندوجهی                  |
| بهترین برای        | استقرار در محیط‌های با منابع محدود، تنظیم دقیق برای وظایف خاص            |

### gemma-3-1b-it

یک مدل سبک فقط متنی با آموزش دستورالعمل، مناسب برای برنامه‌های با منابع محاسباتی محدود.

```python
response = client.chat.completions.create(
    model="gemma-3-1b-it",
    messages=[
        {"role": "user", "content": "ترانسفورمرها در یادگیری ماشین چگونه کار می‌کنند؟"},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemma-3-1b-it` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="ترانسفورمرها در یادگیری ماشین چگونه کار می‌کنند؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### gemma-3-4b-it

یک مدل چندوجهی متعادل که از ورودی‌های متن و تصویر با پنجره زمینه ۱۲۸ هزار توکنی پشتیبانی می‌کند.

```python
response = client.chat.completions.create(
    model="gemma-3-4b-it",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی وجود دارد؟"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
                    },
                },
            ],
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemma-3-4b-it` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### gemma-3-12b-it

یک مدل چندوجهی قدرتمندتر با قابلیت‌های استدلال پیشرفته و پشتیبانی از بیش از ۱۴۰ زبان.

### gemma-3-27b-it

بزرگترین مدل Gemma 3، با ارائه عملکرد برتر برای وظایف پیچیده با ورودی‌های تصویر و متن.

### gemma-3n-e4b-it

یک مدل تخصصی کارآمد با ۴ میلیارد پارامتر که برای موارد استفاده خاص بهینه‌سازی شده است.

## مدل‌های تعبیه‌سازی Gemini

مدل‌های تعبیه‌سازی Gemini گوگل، تعبیه‌سازی‌ متن پیشرفته با ویژگی‌های پیشرفته مانند بهینه‌سازی خاص وظیفه و کنترل انعطاف‌پذیر ابعاد ارائه می‌دهند.

### gemini-embedding-2

**نخستین مدل تعبیه چندوجهی در Gemini API** — متن، تصویر، ویدیو، صوت و PDF را در یک فضای تعبیه یکپارچه نگاشت می‌کند و جستجو، طبقه‌بندی و خوشه‌بندی میان‌وجهی در بیش از ۱۰۰ زبان را ممکن می‌سازد.

| ویژگی | جزئیات |
|-------|--------|
| **شناسه مدل** | `gemini-embedding-2` |
| **نام‌های مستعار** | `gemini-embedding-2-preview` |
| **حداکثر توکن‌های ورودی** | ۸٬۱۹۲ توکن |
| **ابعاد خروجی** | انعطاف‌پذیر ۱۲۸ تا ۳۰۷۲ (پیش‌فرض ۳۰۷۲؛ پیشنهادی ۷۶۸/۱۵۳۶/۳۰۷۲) |
| **روش‌های ورودی** | متن، تصویر، صوت، ویدیو، PDF |
| **روش‌های خروجی** | Embeddings |
| **اندپوینت‌های پشتیبانی‌شده** | `v1/embeddings`, `v1beta/models/gemini-embedding-2:embedContent` (Gemini بومی) |
| **قیمت ورودی متنی** | $0.20 / 1M توکن |
| **ورودی متنی کش‌شده** | $0.02 / 1M توکن (۹۰٪ کاهش هزینه) |
| **قیمت ورودی تصویری** | $0.45 / 1M توکن |
| **قیمت ورودی صوتی** | $6.50 / 1M توکن |
| **قیمت ورودی ویدیویی** | $12.00 / 1M توکن |
| **قیمت خروجی** | $0.15 / 1M توکن |
| **محدودیت روش‌های پشتیبانی‌شده** | ۶ تصویر (PNG/JPEG)، ۱۸۰ ثانیه صوت (MP3/WAV)، ۱۲۰ ثانیه ویدیو (MP4/MOV، ۳۲ فریم)، ۶ صفحه PDF |

**ویژگی‌های کلیدی:**
- **نخستین تعبیه چندوجهی**: فضای تعبیه یکپارچه در سراسر متن، تصویر، ویدیو، صوت و PDF
- **جستجوی میان‌وجهی**: مقایسه و بازیابی محتوا در وجه‌های مختلف در همان فضای برداری
- **بیش از ۱۰۰ زبان**: پشتیبانی گسترده چندزبانه
- **یادگیری بازنمایی Matryoshka (MRL)**: ابعاد خروجی انعطاف‌پذیر بدون افت کیفیت، با نرمال‌سازی مجدد خودکار برای ابعاد برش‌داده‌شده
- **تجمیع تعبیه**: یک تعبیه تجمیع‌شده واحد برای ورودی‌های چندبخشی (مانند متن + تصویر)
- **دستورالعمل وظیفه**: درج انواع وظیفه مستقیما در دستورالعمل‌ها (مثلا `task: search result | query: ...`) برای عملکرد بهینه
- **پشتیبانی دوگانه API**: در دسترس در هم اندپوینت سازگار با OpenAI یعنی `v1/embeddings` و هم اندپوینت بومی Gemini یعنی `v1beta/models/{model}:embedContent`

**مثال (API سازگار با OpenAI):**

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-2",
    "input": "task: search result | query: What is the meaning of life?",
    "dimensions": 768
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="gemini-embedding-2",
    input="task: search result | query: What is the meaning of life?",
    dimensions=768,
)

print(f"Embedding length: {len(response.data[0].embedding)}")

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "gemini-embedding-2",
  input: "task: search result | query: What is the meaning of life?",
  dimensions: 768,
});

console.log(`Embedding length: ${response.data[0].embedding.length}`);

```


**مثال (API بومی Gemini v1beta — تجمیع چندوجهی):**

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{
    "content": {
      "parts": [
        {"text": "An image of a dog"},
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "iVBORw0KGgo...[TRUNCATED]"
          }
        }
      ]
    }
  }'
```

> **یادداشت**: زمانی که چندین بخش در یک درخواست واحد ارائه می‌شوند، `gemini-embedding-2` یک تعبیه تجمیع‌شده واحد برمی‌گرداند. برای تعبیه‌های جداگانه به ازای هر ورودی از درخواست‌های متعدد یا Batch API استفاده کنید.

---

### gemini-embedding-001

مدل تعبیه‌سازی اصلی Gemini که نمایش‌های برداری با کیفیت بالا بهینه‌سازی شده برای وظایف مختلف NLP از جمله جستجوی معنایی، خوشه‌بندی، طبقه‌بندی و تولید تقویت‌شده بازیابی (RAG) تولید می‌کند.

| ویژگی | جزئیات |
|---------|---------|
| **شناسه مدل** | `gemini-embedding-001` |
| **حداکثر توکن‌های ورودی** | ۲٬۰۴۸ توکن |
| **ابعاد خروجی** | انعطاف‌پذیر: ۱۲۸-۳۰۷۲ (توصیه‌شده: ۷۶۸، ۱۵۳۶، ۳۰۷۲) |
| **ابعاد پیش‌فرض** | ۳۰۷۲ |
| **قیمت‌گذاری ورودی** | ۰.۱۵ دلار / ۱ میلیون توکن |
| **قیمت‌گذاری خروجی** | ۰.۰۷۵ دلار / ۱ میلیون توکن |
| **انواع وظایف پشتیبانی‌شده** | SEMANTIC_SIMILARITY، CLASSIFICATION، CLUSTERING، RETRIEVAL_DOCUMENT، RETRIEVAL_QUERY، CODE_RETRIEVAL_QUERY، QUESTION_ANSWERING، FACT_VERIFICATION |
| **بهترین برای** | جستجوی معنایی، سیستم‌های RAG، خوشه‌بندی اسناد، طبقه‌بندی متن |

#### استفاده پایه (طرحواره OpenAI)

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # نقطه پایانی API AvalAI
)

# تولید تعبیه‌سازی پایه
response = client.embeddings.create(
    model="gemini-embedding-001",
    input="روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد",
)

embedding = response.data[0].embedding
print(f"ابعاد تعبیه‌سازی: {len(embedding)}")
print(f"چند مقدار اول: {embedding[:5]}")

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تولید تعبیه‌سازی پایه
const response = await client.embeddings.create({
    model: "gemini-embedding-001",
    input: "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد",
});

const embedding = response.data[0].embedding;
console.log(`ابعاد تعبیه‌سازی: ${embedding.length}`);
console.log(`چند مقدار اول: ${embedding.slice(0, 5)}`);

```

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-001",
    "input": "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"
  }'

```


#### ویژگی‌های پیشرفته با انواع وظایف

برای عملکرد بهینه، نوع وظیفه را مشخص کنید تا مدل تعبیه‌سازی‌‌ها را برای مورد استفاده خاص شما بهینه‌سازی کند:

```python
# بهینه‌سازی خاص وظیفه با ابعاد سفارشی
response = client.embeddings.create(
    model="gemini-embedding-001",
    input=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    extra_body={"task_type": "SEMANTIC_SIMILARITY", "output_dimensionality": 768},
)

# محاسبه شباهت کسینوسی
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings = [item.embedding for item in response.data]
embeddings_matrix = np.array(embeddings)
similarity_matrix = cosine_similarity(embeddings_matrix)

print(f"شباهت بین دو متن اول: {similarity_matrix[0, 1]:.4f}")

```

```javascript
// بهینه‌سازی خاص وظیفه با ابعاد سفارشی
const response = await client.embeddings.create({
    model: "gemini-embedding-001",
    input: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟",
        "چگونه کیک درست کنم؟"
    ],
    // @ts-expect-error extra_body is a provider-specific parameter
    extra_body: {
        task_type: "SEMANTIC_SIMILARITY",
        output_dimensionality: 768
    }
});

const embeddings = response.data.map(item => item.embedding);
console.log(`${embeddings.length} تعبیه‌سازی با ${embeddings[0].length} بعد تولید شد`);

```

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-001",
    "input": ["معنای زندگی چیست؟", "هدف وجود چیست؟"],
    "extra_body": {
      "task_type": "SEMANTIC_SIMILARITY",
      "output_dimensionality": 768
    }
  }'

```


#### استفاده از API بومی Gemini

همچنین می‌توانید از تعبیه‌سازی‌ Gemini از طریق SDK بومی Google GenAI استفاده کنید:

```python
from google import genai

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# تعبیه‌سازی پایه
result = client.models.embed_content(
    model="gemini-embedding-001", contents="معنای زندگی چیست؟"
)

print(f"ابعاد تعبیه‌سازی: {len(result.embeddings[0].values)}")

# استفاده پیشرفته با نوع وظیفه و ابعاد سفارشی
from google.genai import types

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY", output_dimensionality=768
    ),
)

for i, embedding in enumerate(result.embeddings):
    print(f"تعبیه‌سازی {i}: {len(embedding.values)} بعد")

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

// تعبیه‌سازی پایه
const response = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: "معنای زندگی چیست؟"
});

console.log(`ابعاد تعبیه‌سازی: ${response.embeddings[0].values.length}`);

// استفاده پیشرفته با نوع وظیفه
const advancedResponse = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟"
    ],
    taskType: "SEMANTIC_SIMILARITY",
    outputDimensionality: 768
});

console.log(`${advancedResponse.embeddings.length} تعبیه‌سازی تولید شد`);

```

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {"parts": [{"text": "معنای زندگی چیست؟"}]}
    ],
    "embedding_config": {
      "task_type": "SEMANTIC_SIMILARITY",
      "output_dimensionality": 768
    }
  }'

```


#### انواع وظایف پشتیبانی‌شده

| نوع وظیفه | توضیحات | موارد استفاده |
|-----------|-------------|-----------|
| **SEMANTIC_SIMILARITY** | بهینه‌سازی شده برای اندازه‌گیری شباهت متن | سیستم‌های توصیه، تشخیص تکراری |
| **CLASSIFICATION** | بهینه‌سازی شده برای وظایف طبقه‌بندی متن | تحلیل احساسات، تشخیص اسپم |
| **CLUSTERING** | بهینه‌سازی شده برای گروه‌بندی متن‌های مشابه | سازماندهی اسناد، تحقیقات بازار |
| **RETRIEVAL_DOCUMENT** | بهینه‌سازی شده برای نمایه‌سازی اسناد | سیستم‌های RAG، موتورهای جستجو |
| **RETRIEVAL_QUERY** | بهینه‌سازی شده برای پرس‌وجوهای جستجو | برنامه‌های جستجوی سفارشی |
| **CODE_RETRIEVAL_QUERY** | بهینه‌سازی شده برای پرس‌وجوهای جستجوی کد | جستجوی کد، جستجوی مستندات |
| **QUESTION_ANSWERING** | بهینه‌سازی شده برای سیستم‌های پرسش و پاسخ | چت‌بات‌ها، سیستم‌های FAQ |
| **FACT_VERIFICATION** | بهینه‌سازی شده برای بررسی حقایق | سیستم‌های تایید خودکار |

#### کنترل ابعاد خروجی

تعبیه‌سازی‌ Gemini از یادگیری نمایش ماتریوشکا (MRL) پشتیبانی می‌کنند که امکان کوتاه کردن تعبیه‌سازی‌‌ها به ابعاد کوچک‌تر بدون از دست دادن کیفیت قابل توجه را فراهم می‌کند:

- **۳۰۷۲ بعد**: ظرفیت کامل مدل (پیش‌فرض، نرمال‌سازی شده)
- **۱۵۳۶ بعد**: عملکرد متعادل و کارایی
- **۷۶۸ بعد**: کارآمد با عملکرد خوب
- **۵۱۲ بعد**: فشرده با عملکرد قابل قبول
- **۲۵۶ بعد**: بسیار فشرده
- **۱۲۸ بعد**: حداقل اندازه

> **مهم**: برای ابعاد غیر از ۳۰۷۲، باید تعبیه‌سازی‌‌ها را به صورت دستی نرمال‌سازی کنید تا عملکرد بهینه شباهت معنایی داشته باشید.

```python
import numpy as np

# نرمال‌سازی تعبیه‌سازی‌‌ها برای ابعاد < ۳۰۷۲
embedding_values = np.array(embedding)
normalized_embedding = embedding_values / np.linalg.norm(embedding_values)
```

### gemini-embedding-exp-03-07

نسخه آزمایشی مدل تعبیه‌سازی Gemini با آخرین بهبودها و ویژگی‌ها.

| ویژگی | جزئیات |
|---------|---------|
| **شناسه مدل** | `gemini-embedding-exp-03-07` |
| **وضعیت** | آزمایشی |
| **قیمت‌گذاری** | مشابه gemini-embedding-001 |
| **ویژگی‌ها** | آخرین بهبودهای آزمایشی |
| **بهترین برای** | آزمایش قابلیت‌های جدید، برنامه‌های تحقیقاتی |

> **نکته**: مدل‌های آزمایشی ممکن است رفتار متفاوتی داشته باشند و در معرض تغییر هستند. برای برنامه‌های تولیدی از `gemini-embedding-001` پایدار استفاده کنید.

## تولید گفتار (تبدیل متن به گفتار)

برای پروژه جدید، Gemini 3.8 Flash TTS را برای کیفیت خلاقانه و Gemini 3.8 Flash-Lite TTS را برای توان عملیاتی بالا انتخاب کنید. برخلاف Live API تعاملی، این مدل‌ها متن ارائه‌شده را می‌خوانند و صدا تولید می‌کنند. درخواست بومی فقط ورودی متنی می‌پذیرد؛ سقف ورودی دو مدل ۳.۸ برابر با ۸٬۱۹۲ توکن و سقف خروجی ارائه‌شده در Gemini API برابر با ۱۶٬۳۸۴ توکن است.

### مهاجرت از مدل‌های قدیمی TTS

- برای جایگزینی `gemini-3.1-flash-tts-preview` در پردازش پرحجم، `gemini-3.8-flash-lite-tts` را انتخاب کنید؛ برای روایت احساسی از Flash استفاده کنید.
- هنگام مهاجرت از `gemini-2.5-flash-tts`، `gemini-2.5-pro-tts`، `gemini-2.5-flash-preview-tts` یا `gemini-2.5-pro-preview-tts`، بر اساس توان عملیاتی یا کیفیت خلاقانه مدل را انتخاب کنید و در صورت نیاز مسیر و ساختار درخواست را هم تغییر دهید. تغییر نام مدل در درخواست قدیمی Vertex برای مهاجرت کافی نیست.
- متن هر بخش باید **عین متن گفتار** باشد. دستورهای پایدار اجرا را در `speechMetadata.style` و نام گوینده را در `speechMetadata.speaker` قرار دهید، نه در پیشوند متن که ممکن است بلند خوانده شود. در درخواست چندگوینده، هر نوبت باید نام یکی از گویندگان پیکربندی‌شده را داشته باشد. برچسب‌های میان علامت‌های زاویه‌دار مانند `<laugh>`، `<sigh>` و `<short pause>` را فقط برای رویدادهای صوتی لحظه‌ای به کار ببرید.
- در مرجع بومی گوگل، خروجی پیش‌فرض درخواست غیرجریانی اکنون WAV با نوع `audio/wav` است؛ مدل قدیمی ۳.۱ فقط `pcm16` را پشتیبانی می‌کند. نوع MIME پاسخ را بررسی کنید: بایت‌های WAV را مستقیم بنویسید و سرآیند دوم اضافه نکنید. داده بدون سرآیند `audio/L16` از نوع PCM16 را به صدای تک‌کاناله ۱۶ بیتی با نرخ ۲۴٬۰۰۰ هرتز تبدیل کنید. پیش‌فرض بومی را با قالبی که در مثال Chat Completions صریحاً درخواست می‌شود، یکی ندانید.
- هیچ‌یک از مدل‌های ۳.۸ را به `/v1/text:synthesize` نفرستید. از `/v1beta/models`، `/v1/chat/completions` یا `/v1/audio/speech` در AvalAI استفاده کنید. یکپارچه‌سازی‌های موجود Vertex با مدل‌های ۲.۵ تا زمان مهاجرت تابع راهنمای قدیمی بالا هستند.

### گفتار تک‌گوینده با API بومی

این نمونه‌های HTTP از فیلد بومی `speechMetadata` با نام‌گذاری camelCase استفاده می‌کنند و به پشتیبانی SDK از فیلدهای تازه وابسته نیستند. برای توان عملیاتی بالا، همین بدنه را با `gemini-3.8-flash-lite-tts` ارسال کنید.

```bash
curl --fail-with-body "https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{"role": "user", "parts": [{
      "text": "Have a wonderful day!",
      "speechMetadata": {"speaker": "Narrator", "style": "Cheerful and warm"}
    }]}],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zephyr"}}
      }
    }
  }' -o tts-response.json
python3 - <<'PYTHON'
import base64
import json
import wave
from pathlib import Path

response = json.loads(Path("tts-response.json").read_text())
audio = next(part["inlineData"] for part in response["candidates"][0]["content"]["parts"] if "inlineData" in part)
data = base64.b64decode(audio["data"], validate=True)
mime = audio["mimeType"].split(";", 1)[0].lower()
if mime == "audio/wav":
    Path("out.wav").write_bytes(data)
elif mime == "audio/l16":
    with wave.open("out.wav", "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(24000)
        output.writeframes(data)
else:
    raise ValueError(f"Unexpected audio MIME type: {mime}")
PYTHON

```

```python
import base64
import json
import os
import wave
from pathlib import Path
from urllib.request import Request, urlopen

payload = {
    "contents": [
        {
            "role": "user",
            "parts": [
                {
                    "text": "Have a wonderful day!",
                    "speechMetadata": {
                        "speaker": "Narrator",
                        "style": "Cheerful and warm",
                    },
                }
            ],
        }
    ],
    "generationConfig": {
        "responseModalities": ["AUDIO"],
        "speechConfig": {
            "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zephyr"}},
        },
    },
}
request = Request(
    "https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent",
    data=json.dumps(payload).encode(),
    headers={
        "x-goog-api-key": os.environ["AVALAI_API_KEY"],
        "Content-Type": "application/json",
    },
)
with urlopen(request) as result:
    response = json.load(result)
audio = next(
    part["inlineData"]
    for part in response["candidates"][0]["content"]["parts"]
    if "inlineData" in part
)
data = base64.b64decode(audio["data"], validate=True)
mime = audio["mimeType"].split(";", 1)[0].lower()
if mime == "audio/wav":
    Path("out.wav").write_bytes(data)
elif mime == "audio/l16":
    with wave.open("out.wav", "wb") as output:
        output.setnchannels(1)
        output.setsampwidth(2)
        output.setframerate(24000)
        output.writeframes(data)
else:
    raise ValueError(f"Unexpected audio MIME type: {mime}")

```

```javascript
import { writeFile } from "node:fs/promises";

const result = await fetch(
  "https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent",
  {
    method: "POST",
    headers: {
      "x-goog-api-key": process.env.AVALAI_API_KEY,
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      contents: [{ role: "user", parts: [{
        text: "Have a wonderful day!",
        speechMetadata: { speaker: "Narrator", style: "Cheerful and warm" },
      }] }],
      generationConfig: {
        responseModalities: ["AUDIO"],
        speechConfig: {
          voiceConfig: { prebuiltVoiceConfig: { voiceName: "Zephyr" } },
        },
      },
    }),
  },
);
if (!result.ok) throw new Error(await result.text());
const response = await result.json();
const audio = response.candidates[0].content.parts.find(part => part.inlineData).inlineData;
const data = Buffer.from(audio.data, "base64");
const mime = audio.mimeType.split(";", 1)[0].toLowerCase();
if (mime === "audio/wav") {
  await writeFile("out.wav", data);
} else if (mime === "audio/l16") {
  await writeFile("out.pcm", data);
} else {
  throw new Error(`Unexpected audio MIME type: ${mime}`);
}

```


در شاخه PCM نمونه JavaScript، فایل `out.pcm` نوشته می‌شود. فقط وقتی نوع MIME برابر با `audio/L16` است، آن را تبدیل کنید:

```bash
ffmpeg -f s16le -ar 24000 -ac 1 -i out.pcm out.wav
```

### گفتار چندگوینده با API بومی

بدنه زیر را به همان مسیر بومی Flash بفرستید و از روش رمزگشایی مبتنی بر MIME در بالا استفاده کنید. هر نوبت، گوینده و سبک جداگانه‌ای دارد که با صدای پیکربندی‌شده تطابق دارد؛ نام گوینده جزئی از متن خواندنی نیست.

```json
{
  "contents": [
    {
      "role": "user",
      "parts": [
        {
          "text": "How is your day going?",
          "speechMetadata": {
            "speaker": "Joe",
            "style": "Friendly and curious"
          }
        },
        {
          "text": "Very well, thank you!",
          "speechMetadata": {
            "speaker": "Jane",
            "style": "Upbeat"
          }
        }
      ]
    }
  ],
  "generationConfig": {
    "responseModalities": [
      "AUDIO"
    ],
    "speechConfig": {
      "multiSpeakerVoiceConfig": {
        "speakerVoiceConfigs": [
          {
            "speaker": "Joe",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Zephyr"
              }
            }
          },
          {
            "speaker": "Jane",
            "voiceConfig": {
              "prebuiltVoiceConfig": {
                "voiceName": "Puck"
              }
            }
          }
        ]
      }
    }
  }
}
```

### پاسخ صوتی Chat Completions

هر دو حالت متن و صدا را با صدای `Zephyr` و قالب `pcm16` درخواست کنید. فقط `choices[0].message.audio.data` را رمزگشایی کنید؛ محتوای پیام جایگزین داده صوتی نیست. خروجی، PCM16 خام با کدگذاری base64 است، نه MP3 یا فایل WAV.

```bash
curl --fail-with-body https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-lite-tts",
    "messages": [{"role": "user", "content": "Have a wonderful day!"}],
    "modalities": ["text", "audio"],
    "audio": {"voice": "Zephyr", "format": "pcm16"}
  }' -o chat-response.json
python3 - <<'PYTHON'
import base64
import json
from pathlib import Path

response = json.loads(Path("chat-response.json").read_text())
Path("chat.pcm").write_bytes(base64.b64decode(response["choices"][0]["message"]["audio"]["data"], validate=True))
PYTHON
ffmpeg -f s16le -ar 24000 -ac 1 -i chat.pcm chat.wav

```

```python
import base64
import os
import wave
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
response = client.chat.completions.create(
    model="gemini-3.8-flash-lite-tts",
    messages=[{"role": "user", "content": "Have a wonderful day!"}],
    modalities=["text", "audio"],
    audio={"voice": "Zephyr", "format": "pcm16"},
)
data = base64.b64decode(response.choices[0].message.audio.data, validate=True)
with wave.open("chat.wav", "wb") as output:
    output.setnchannels(1)
    output.setsampwidth(2)
    output.setframerate(24000)
    output.writeframes(data)

```

```javascript
import OpenAI from "openai";
import { writeFile } from "node:fs/promises";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const response = await client.chat.completions.create({
  model: "gemini-3.8-flash-lite-tts",
  messages: [{ role: "user", content: "Have a wonderful day!" }],
  modalities: ["text", "audio"],
  audio: { voice: "Zephyr", format: "pcm16" },
});
await writeFile("chat.pcm", Buffer.from(response.choices[0].message.audio.data, "base64"));

```


برای نمونه JavaScript، فایل `chat.pcm` را با دستور `ffmpeg -f s16le -ar 24000 -ac 1 -i chat.pcm chat.wav` تبدیل کنید.

### تولید مستقیم گفتار

شیء صدا از `name` و `languageCode` استفاده می‌کند. این نمونه‌ها عمداً متن انگلیسی را همراه با `en-US` می‌فرستند، WAV درخواست می‌کنند و پاسخ دودویی را مستقیم ذخیره می‌کنند.

```bash
curl --fail-with-body https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-lite-tts",
    "input": "Have a wonderful day!",
    "voice": {"name": "Zephyr", "languageCode": "en-US"},
    "response_format": "wav"
  }' --output speech.wav

```

```python
import os
from pathlib import Path
import requests

response = requests.post(
    "https://api.avalai.ir/v1/audio/speech",
    headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}"},
    json={
        "model": "gemini-3.8-flash-lite-tts",
        "input": "Have a wonderful day!",
        "voice": {"name": "Zephyr", "languageCode": "en-US"},
        "response_format": "wav",
    },
    timeout=120,
)
response.raise_for_status()
Path("speech.wav").write_bytes(response.content)

```

```javascript
import { writeFile } from "node:fs/promises";

const response = await fetch("https://api.avalai.ir/v1/audio/speech", {
  method: "POST",
  headers: {
    Authorization: `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "gemini-3.8-flash-lite-tts",
    input: "Have a wonderful day!",
    voice: { name: "Zephyr", languageCode: "en-US" },
    response_format: "wav",
  }),
});
if (!response.ok) throw new Error(await response.text());
await writeFile("speech.wav", Buffer.from(await response.arrayBuffer()));

```


### صداها و زبان‌ها

صداهای آماده شامل Zephyr با لحن روشن، Puck با لحن پرانرژی، Kore با لحن محکم و Charon با لحن آموزنده هستند. Flash از ۱۳۰ زبان و Flash-Lite از ۱۰۱ زبان پشتیبانی می‌کند؛ هر دو انگلیسی و فارسی را پوشش می‌دهند و زبان ورودی بومی را خودکار تشخیص می‌دهند. فهرست کامل صداها و زبان‌های مرجع گوگل را در [راهنمای تولید گفتار](https://ai.google.dev/gemini-api/docs/speech-generation) ببینید. پیش از استفاده از دیگر سرویس‌های صوتی گوگل، پشتیبانی مسیر مربوطه را در AvalAI جداگانه بررسی کنید.

برای جزئیات مشترک مسیرها، [قیمت‌های فعلی](fa/pricing.md) و [مرجع API صوتی](fa/api-reference/audio.md) را ببینید.
