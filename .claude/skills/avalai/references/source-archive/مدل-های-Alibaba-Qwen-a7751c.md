# مدل‌های Alibaba (Qwen)

AvalAI دسترسی جامع به خانواده کامل مدل‌های Qwen شرکت Alibaba را از طریق زیرساخت رسمی ابری [DashScope](https://dashscope.console.aliyun.com/) آن‌ها فراهم می‌کند. این مدل‌ها قابلیت‌های پیشرفته‌ای در زمینه تولید متن، پردازش چندوجهی، استدلال، ترجمه ماشینی و وظایف برنامه‌نویسی ارائه می‌دهند و همگی از طریق نقاط پایانی یکپارچه API ما قابل دسترسی هستند.

## مهم: پارامتر `enable_thinking`

> **⚠️ نکته برای درخواست‌های غیر استریمینگ**: اکثر مدل‌های Alibaba Qwen نیاز دارند که شما به صورت صریح پارامتر [`extra_body`](fa/guides/provider-specific-params.md) را با مقدار `{"enable_thinking": False}` هنگام ارسال درخواست‌های **غیر استریمینگ** (`stream=False`) تنظیم کنید. بدون این پارامتر، DashScope ممکن است خطا برگرداند.
>
> **الزامات کلیدی**:
>
> - **درخواست‌های غیر استریمینگ**: باید شامل `extra_body={"enable_thinking": False}` باشند
> - **درخواست‌های استریمینگ با تفکر**: می‌توانند از `extra_body={"enable_thinking": True}` فقط با `stream=True` استفاده کنند
> - **خطا در صورت نقض**: تنظیم `enable_thinking: True` بدون استریمینگ منجر به خطای `invalid_request` می‌شود

**مثال برای درخواست‌های غیر استریمینگ**:

```python
response = client.chat.completions.create(
    model="qwen3-8b",
    messages=[{"role": "user", "content": "سوال شما اینجا"}],
    stream=False,
    extra_body={"enable_thinking": False},  # الزامی برای غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-8b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="سوال شما اینجا",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال برای درخواست‌های استریمینگ با تفکر**:

```python
stream = client.chat.completions.create(
    model="qwen3-8b",
    messages=[{"role": "user", "content": "سوال شما اینجا"}],
    stream=True,
    extra_body={"enable_thinking": True},  # فقط با استریمینگ پشتیبانی می‌شود
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-8b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="سوال شما اینجا",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مدل‌های موجود

مدل‌های Qwen شرکت Alibaba در چندین خانواده تخصصی سازماندهی شده‌اند که هر کدام برای موارد استفاده و نیازهای عملکردی مختلف بهینه‌سازی شده‌اند. همه مدل‌ها از `v1/chat/completions` پشتیبانی می‌کنند؛ پشتیبانی از `v1/messages` و `v1/responses` به مدل وابسته است. پرچم‌دار جدید `qwen3.8-max` از `v1/chat/completions` و `v1/messages` به‌طور کامل و از `v1/responses` به‌صورت جزئی پشتیبانی می‌کند.

## سری Qwen Flash

مدل‌های با کارایی بالا که برای سرعت و بهره‌وری بهینه‌سازی شده‌اند و برای کاربردهایی که نیاز به زمان پاسخ سریع با کیفیت عالی دارند، ایده‌آل هستند.

> **⚠️ اطلاعیه منسوخ شدن:** سری قدیمی `qwen-turbo` (شامل `qwen-turbo`، `qwen-turbo-latest`، `qwen-turbo-2025-04-28`) توسط علی‌بابا بین **۱۳ می ۲۰۲۶** و **۳۱ می ۲۰۲۶** از سرویس خارج می‌شود. لطفا به `qwen-flash` یا `qwen3.6-flash` مهاجرت کنید. برای جزئیات به [صفحه منسوخ‌شدن‌ها](fa/deprecations.md) مراجعه کنید.

| ویژگی             | qwen-flash             | qwen-flash-2025-07-28 |
| ----------------- | ---------------------- | --------------------- |
| ارائه‌دهنده       | DashScope              | DashScope             |
| مالک              | Alibaba                | Alibaba               |
| پنجره زمینه       | ۱۳۱٬۰۷۲ توکن           | ۱۳۱٬۰۷۲ توکن          |
| حداکثر توکن ورودی | ۱۲۹٬۰۲۴                | ۱۲۹٬۰۲۴               |
| حداکثر توکن خروجی | ۱۶٬۳۸۴                 | ۱۶٬۳۸۴                |
| نقاط قوت          | فوق‌سریع، قیمت طبقه‌ای | نسخه پایدار flash     |
| بهترین برای       | سرعت مقرون‌به‌صرفه     | تولید flash           |

```python
# مثال استفاده از Qwen3.6 Flash برای تولید سریع متن
response = client.chat.completions.create(
    model="qwen3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "مزایای کلیدی انرژی تجدیدپذیر را در ۳ نکته خلاصه کنید.",
        }
    ],
    max_tokens=200,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مزایای کلیدی انرژی تجدیدپذیر را در ۳ نکته خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## سری Qwen3.8

این سری شامل پرچم‌دار مدیریت‌شده `qwen3.8-max`، مدل پایه وزن‌باز آن یعنی `qwen3.8-2.4t-a95b`، مدل کم‌هزینه `qwen3.8-flash` (نام مستعار `qwen3.8-flash-next`) و مدل متراکم فشرده `qwen3.8-27b` است. برای ورودی چندوجهی، تفکر اختیاری، زمینه مدیریت‌شده ۱ میلیون توکنی و قابلیت‌های production از Max استفاده کنید. مدل پایه وزن‌باز برای workloadهای فقط متن با reasoning همیشه فعال مناسب است. برای چت و گردش‌کارهای عاملی پرحجم با کمترین هزینه در سری Qwen3.8 از Flash و برای workloadهای بینایی-زبان با کنترل انعطاف‌پذیر تفکر از مدل متراکم 27B استفاده کنید.

### qwen3.8-flash

[`qwen3.8-flash`](fa/models/qwen3.8-flash.md) نام مستعار مدیریت‌شده `qwen3.8-flash-next` است؛ مدلی از جنس ترکیب متخصصان با ۱۲۵ میلیارد پارامتر کل که در هر توکن ۶ میلیارد پارامتر را فعال می‌کند. معماری ترکیبی Gated DeltaNet و توجه پراکنده Qwen (QSA) تاریخچه را در یک حالت با اندازه ثابت فشرده می‌کند و بازیابی دقیق را در زمینه طولانی حفظ می‌کند؛ همچنین ۵۱ میلیارد پارامتر additional در قالب embedding N-gram ظرفیت مدل را با هزینه محاسباتی ناچیز در هر توکن افزایش می‌دهد.

| ویژگی                     | جزئیات                                                                    |
| ------------------------- | ------------------------------------------------------------------------- |
| شناسه مدل                 | `qwen3.8-flash`                                                           |
| پنجره زمینه               | ۲۶۲٬۱۴۴ توکن                                                              |
| قیمت ورودی                | $0.15 / 1M توکن                                                           |
| ساخت کش                   | $0.20 / 1M توکن                                                           |
| ورودی کش‌شده              | $0.016 / 1M توکن                                                          |
| قیمت خروجی                | $0.47 / 1M توکن                                                           |
| روش‌های ورودی             | متن، تصویر، ویدئو                                                         |
| روش‌های خروجی             | متن                                                                       |
| حالت تفکر                 | پیش‌فرض فعال؛ غیرفعال‌سازی با `enable_thinking` در هر درخواست             |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/messages` (کامل)، `v1/responses` (جزئی) |

**ویژگی‌های کلیدی:**

- **زمینه طولانی کم‌هزینه**: توجه ترکیبی GDN + QSA هزینه سرویس‌دهی زمینه طولانی را کاهش می‌دهد و تا ۲۶۲K توکن ورودی در AvalAI پشتیبانی می‌کند
- **درک بینایی-زبان**: ورودی بومی تصویر و ویدیو برای اسناد، نمودارها و ویدیوهای چندساعته
- **توانایی عاملی**: نتایج گزارش‌شده توسط ارائه‌دهنده شامل ۷۳.۵ در Toolathlon Verified، ۷۳.۹ در CoWorkBench و ۹۱.۷ در GPQA Diamond
- **تفکر انعطاف‌پذیر**: `reasoning_effort` مقدارهای `low`، `medium` و `xhigh` را می‌پذیرد و `preserve_thinking` در صورت پشتیبانی، زمینه استدلال را بین نوبت‌ها حفظ می‌کند

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-flash",
    messages=[
        {
            "role": "user",
            "content": "این برنامه مهاجرت را بررسی کن و سه فرض پرریسک آن را مشخص کن.",
        }
    ],
    extra_body={"enable_thinking": True, "reasoning_effort": "medium"},
)

print(response.choices[0].message.content)
```

### qwen3.8-27b

[`qwen3.8-27b`](fa/models/qwen3.8-27b.md) مدل متراکم و فشرده نسل Qwen3.8 با مناسب‌ترین شکل برای استقرار است. این مدل به‌طور بومی بینایی-زبان است و تصویر و ویدیو را درک می‌کند و کنترل انعطاف‌پذیر تفکر آن برای پیش بردن کارهای پیچیده و چندمرحله‌ای با قابلیت اطمینان بیشتر طراحی شده است.

| ویژگی                     | جزئیات                                                                    |
| ------------------------- | ------------------------------------------------------------------------- |
| شناسه مدل                 | `qwen3.8-27b`                                                             |
| پنجره زمینه               | ۲۶۲٬۱۴۴ توکن                                                              |
| قیمت ورودی                | $0.50 / 1M توکن                                                           |
| ساخت کش                   | $0.625 / 1M توکن                                                          |
| ورودی کش‌شده              | $0.10 / 1M توکن                                                           |
| قیمت خروجی                | $2.00 / 1M توکن                                                           |
| روش‌های ورودی             | متن، تصویر، ویدئو                                                         |
| روش‌های خروجی             | متن                                                                       |
| حالت تفکر                 | پیش‌فرض فعال؛ غیرفعال‌سازی با `enable_thinking` در هر درخواست             |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/messages` (کامل)، `v1/responses` (جزئی) |

**ویژگی‌های کلیدی:**

- **مدل متراکم فشرده**: ۲۷B پارامتر همراه با کدکننده بینایی برای workloadهایی که مدل متراکم می‌خواهند
- **درک بینایی-زبان**: درک بومی تصویر و ویدیو، از نمودارهای STEM و اسناد تا ویدیوهای چندساعته
- **اجرای عاملی**: نتایج گزارش‌شده توسط ارائه‌دهنده شامل ۷۳.۰ در Terminal Bench 2.1، ۶۱.۷ در SWE-bench Pro و ۸۴.۳ در OSWorld-Verified
- **تفکر انعطاف‌پذیر**: `reasoning_effort` مقدارهای `low`، `medium` و `xhigh` را می‌پذیرد و `preserve_thinking` در صورت پشتیبانی، زمینه استدلال را بین نوبت‌ها حفظ می‌کند

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-27b",
    messages=[
        {
            "role": "user",
            "content": "یک بازسازی مرحله‌ای برای این سرویس با تست و معیارهای بازگشت برنامه‌ریزی کن.",
        }
    ],
    extra_body={"enable_thinking": True, "reasoning_effort": "medium"},
)

print(response.choices[0].message.content)
```

برای جزئیات عرضه، [به‌روزرسانی ۲۹ اوت ۲۰۲۶](fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added.md) را ببینید.

### qwen3.8-2.4t-a95b

[`qwen3.8-2.4t-a95b`](fa/models/qwen3.8-2.4t-a95b.md) مدل پایه وزن‌باز زیرساخت `qwen3.8-max` است. معماری mixture-of-experts آن ۲٫۴ تریلیون پارامتر کل دارد و در هر forward pass تعداد ۹۵ میلیارد پارامتر را فعال می‌کند. برخلاف سرویس مدیریت‌شده Max، این route فقط متن است و تفکر در آن اجباری است.

| ویژگی                     | جزئیات                                                                    |
| ------------------------- | ------------------------------------------------------------------------- |
| شناسه مدل                 | `qwen3.8-2.4t-a95b`                                                       |
| پنجره زمینه               | ۲۶۲٬۱۴۴ توکن                                                              |
| قیمت ورودی                | $2.00 / 1M توکن                                                           |
| ساخت کش                   | $2.50 / 1M توکن                                                           |
| ورودی کش‌شده              | $0.25 / 1M توکن                                                           |
| قیمت خروجی                | $6.00 / 1M توکن                                                           |
| روش‌های ورودی             | فقط متن                                                                   |
| روش‌های خروجی             | متن                                                                       |
| حالت تفکر                 | اجباری و غیرقابل غیرفعال‌سازی                                             |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/messages` (کامل)، `v1/responses` (جزئی) |

برای تنظیم بودجه reasoning اجباری از `reasoning_effort` استفاده کنید. مقدارهای پشتیبانی‌شده `low`، `medium` و `xhigh` هستند و `xhigh` مقدار پیش‌فرض است. پاسخ با reasoning درون `<think>...</think>` شروع می‌شود و سپس پاسخ نهایی می‌آید. در گردش‌کارهای چندنوبتی یا ابزارمحور، اگر route انتخابی پشتیبانی می‌کند thinking قبلی را با `preserve_thinking` حفظ کنید.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-2.4t-a95b",
    messages=[
        {
            "role": "user",
            "content": "این برنامه مهاجرت را بررسی کن و سه فرض پرریسک آن را مشخص کن.",
        }
    ],
    extra_body={"reasoning_effort": "medium"},
)

print(response.choices[0].message.content)
```

### qwen3.8-max

[`qwen3.8-max`](fa/models/qwen3.8-max.md) پرچم‌دار جدید mixture-of-experts شرکت Alibaba با ۲٫۴ تریلیون پارامتر برای کدنویسی بلندمدت، کار حرفه‌ای، درک چندوجهی و اجرای عاملی است. این مدل می‌تواند کارهای چندمرحله‌ای را در مکالمات طولانی برنامه‌ریزی، پیاده‌سازی و راستی‌آزمایی کند؛ از جمله پروژه‌هایی که بیش از ۱۰ روز ادامه دارند.

| ویژگی                     | جزئیات                                                                    |
| ------------------------- | ------------------------------------------------------------------------- |
| شناسه مدل                 | `qwen3.8-max`                                                             |
| پنجره زمینه               | ۱٬۰۰۰٬۰۰۰ توکن (حداکثر ۹۹۱٬۰۰۰ توکن ورودی)                                |
| حداکثر خروجی              | ۱۲۸٬۰۰۰ توکن                                                              |
| قیمت ورودی                | $2.00 / 1M توکن                                                           |
| ساخت کش                   | $2.50 / 1M توکن                                                           |
| ورودی کش‌شده              | $0.25 / 1M توکن                                                           |
| قیمت خروجی                | $6.00 / 1M توکن                                                           |
| روش‌های ورودی             | متن، تصویر، ویدئو                                                         |
| روش‌های خروجی             | متن                                                                       |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` (کامل)، `v1/messages` (کامل)، `v1/responses` (جزئی) |

**ویژگی‌های کلیدی:**

- **کدنویسی بلندمدت**: برنامه‌ریزی، پیاده‌سازی، آزمایش و راستی‌آزمایی پروژه‌های نرم‌افزاری چندمرحله‌ای و حجیم
- **کار حرفه‌ای**: تولید خروجی‌های سرتاسری در حوزه‌های حقوقی، مالی، طراحی و سایر زمینه‌های تخصصی
- **درک بصری بومی**: استفاده از تصویر و ویدئوی طولانی در تمام مراحل برنامه‌ریزی، اجرا و راستی‌آزمایی
- **تحلیل اسناد بسیار طولانی**: پردازش مخازن بزرگ و مجموعه اسناد گسترده در پنجره زمینه ۱ میلیون توکنی
- **حلقه‌های بازخورد عاملی**: تکرار چرخه برنامه‌ریزی، استفاده از ابزار، اجرا و راستی‌آزمایی برای کارهای پیچیده
- **قابلیت‌های توسعه‌دهنده**: فراخوانی تابع، انتخاب ابزار، خروجی ساختاریافته، کش پرامپت، جستجوی وب و استریمینگ
- **تفکر ترکیبی**: برای استدلال عمیق‌تر از `enable_thinking` استفاده کنید و الزامات استریمینگ ابتدای این صفحه را رعایت کنید

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {
            "role": "user",
            "content": "این معماری را بررسی کن و یک برنامه پیاده‌سازی مرحله‌ای با دروازه‌های راستی‌آزمایی پیشنهاد بده.",
        }
    ],
    extra_body={"enable_thinking": False},
)

print(response.choices[0].message.content)
```

برای جزئیات عرضه، [به‌روزرسانی ۳ اوت ۲۰۲۶](fa/news/2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade.md) را ببینید.

---

## سری Qwen3.7

نسل اختصاصی قبلی Qwen از Alibaba برای عصر عامل‌ها طراحی شده است. برای بالاترین توانایی فعلی در کارهای بلندمدت از `qwen3.8-max`، برای نسل قبلی Max از `qwen3.7-max` و برای گزینه کم‌هزینه‌تر با زمینه بلند، کدنویسی، استدلال و گردش‌کارهای چندوجهی از `qwen3.7-plus` استفاده کنید.

### qwen3.7-max

پرچم‌دار قبلی Qwen Max که برای گردش‌کارهای عاملی ساخته شده است. این مدل قابلیت‌های کدنویسی پیشرو، استدلال قوی و اجرای خودکار بلندمدت در صدها یا هزاران فراخوانی ابزار را ارائه می‌دهد؛ برای جدیدترین نسل پرچم‌دار از `qwen3.8-max` استفاده کنید.

> **نکته قیمت‌گذاری:** جدول زیر متادیتای فعلی مدل در AvalAI را نشان می‌دهد. پیش از نقل قیمت در گردش‌کارهای مشتری‌محور، با `GET /v1/models/qwen3.7-max` قیمت زنده را تأیید کنید.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.7-max` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۶۵٬۵۳۶ توکن |
| قیمت ورودی | $2.50 / 1M توکن |
| ساخت کش | $3.125 / 1M توکن |
| ورودی کش‌شده | $0.25 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $7.50 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions`، `v1/responses` (نسبی) |

**ویژگی‌های کلیدی:**
- **پایه عامل**: ساخته شده برای عصر عامل‌ها — کدنویسی، بهره‌وری اداری و اجرای بلندمدت
- **عامل کدنویسی پیشرو**: ۸۰.۴ در SWE-Verified، ۶۰.۶ در SWE-Pro، ۷۸.۳ در SWE-Multilingual، ۶۹.۷ در Terminal-Bench 2.0
- **استدلال قوی**: ۹۲.۴ در GPQA Diamond، ۹۷.۱ در HMMT 2026 Feb، ۹۰.۰ در IMOAnswerBench، ۴۴.۵ در Apex
- **بنچمارک‌های عامل**: ۶۰.۸ در MCP-Mark، ۷۶.۴ در MCP-Atlas، ۸۷.۰ در SpreadSheetBench-v1، ۷۵.۰ در BFCL-V4
- **اجرای بلندمدت**: نمایش بهینه‌سازی خودکار ۳۵ ساعته کرنل با ۱٬۱۵۸ فراخوانی ابزار و افزایش سرعت ۱۰.۰ برابر
- **تعمیم میان چارچوب‌ها**: عملکرد پایدار در Claude Code، OpenClaw، Qwen Code و چارچوب‌های سفارشی
- **تفکر ترکیبی**: حالت استدلال اختیاری از طریق `enable_thinking` (فقط استریمینگ)
- **حفظ تفکر**: توصیه‌شده برای گردش‌کارهای عاملی چندنوبتی از طریق `preserve_thinking`

**عملکرد بنچمارک:**
- SWE-Verified: ۸۰.۴ (هم‌تراز با Opus-4.6 Max با ۸۰.۸)
- SWE-Pro: ۶۰.۶ (در برابر K2.6 با ۵۹.۵)
- SWE-Multilingual: ۷۸.۳ (در برابر Opus-4.6 با ۷۷.۵)
- Terminal-Bench 2.0: ۶۹.۷ (در برابر DS-V4-Pro Max با ۶۷.۹)
- NL2Repo: ۴۷.۲
- HMMT 2026 Feb: ۹۷.۱ (بهترین در کلاس)
- GPQA Diamond: ۹۲.۴ (بهترین در کلاس)
- IMOAnswerBench: ۹۰.۰ (بهترین در کلاس)
- MMLU-Pro: ۸۹.۶
- MRCR-v2 128k: ۹۰.۴ (بهترین در کلاس)
- WMT24++: ۸۵.۸ (بهترین در کلاس)

```python
# مثال استفاده از Qwen3.7-Max برای وظایف عاملی بلندمدت
stream = client.chat.completions.create(
    model="qwen3.7-max",
    messages=[
        {
            "role": "user",
            "content": "یک CLI پایتون چندفایلی بساز که فایل‌های CSV را از S3 دانلود، اعتبارسنجی و ادغام کند.",
        }
    ],
    stream=True,
    extra_body={
        "enable_thinking": True,
        "preserve_thinking": True,
    },
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.7-max` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک CLI پایتون چندفایلی بساز که فایل‌های CSV را از S3 دانلود، اعتبارسنجی و ادغام کند.",
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

### qwen3.7-plus

مدل متعادل Qwen3.7 برای چت عمومی باکیفیت، کدنویسی عاملی، استدلال چندوجهی و بارهای کاری تولیدی با زمینه بلند، زمانی که `qwen3.7-max` بیش از نیاز وظیفه است.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.7-plus` |
| پنجره زمینه | تا ۱٬۰۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۶۵٬۵۳۶ توکن |
| قیمت ورودی | $0.40 / 1M توکن |
| ساخت کش | $0.50 / 1M توکن |
| ورودی کش‌شده | $0.04 / 1M توکن |
| قیمت خروجی | $1.60 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**بهترین برای:**
- بارهای کاری عمومی Qwen3.7 با هزینه کمتر از `qwen3.7-max`
- عامل‌های کدنویسی، پرامپت‌های سنگین از نظر سند و تحلیل چندوجهی
- برنامه‌های پرترافیکی که همچنان به زمینه بزرگ و رفتار آگاه از ابزار نیاز دارند

```python
# نمونه استفاده از Qwen3.7-Plus برای کدنویسی عاملی متعادل
response = client.chat.completions.create(
    model="qwen3.7-plus",
    messages=[
        {
            "role": "user",
            "content": "این طرح معماری را بررسی کن و پرریسک‌ترین مراحل مهاجرت را مشخص کن.",
        }
    ],
    extra_body={"enable_thinking": False},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.7-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این طرح معماری را بررسی کن و پرریسک‌ترین مراحل مهاجرت را مشخص کن.",
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

## سری Qwen3.6 Plus

مدل پرچم‌دار Qwen3.6 از Alibaba با ارتقاء قابلیت‌های عظیم، با پنجره زمینه ۱ میلیون توکن به صورت پیش‌فرض، قابلیت‌های کدنویسی عاملی بهبود یافته قابل توجه، و درک و استدلال چندحالتی بهتر.

### qwen3.6-plus

یک مدل توانمند Qwen3.6 با قابلیت‌های پیشرفته کدنویسی عاملی و چندحالتی.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.6-plus` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن (پیش‌فرض) |
| قیمت ورودی | ۰.۵۰ دلار / ۱ میلیون توکن |
| قیمت ورودی (بالای ۲۵۶K) | ۲.۰۰ دلار / ۱ میلیون توکن |
| ایجاد کش | ۰.۶۲۵ دلار / ۱ میلیون توکن |
| ایجاد کش (بالای ۲۵۶K) | ۲.۵۰ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۰۵ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| ورودی کش شده (بالای ۲۵۶K) | ۰.۲۰ دلار / ۱ میلیون توکن |
| قیمت خروجی | ۳.۰۰ دلار / ۱ میلیون توکن |
| قیمت خروجی (بالای ۲۵۶K) | ۶.۰۰ دلار / ۱ میلیون توکن |
| ورودی‌های پشتیبانی‌شده | متن، تصویر |
| خروجی‌های پشتیبانی‌شده | متن |
| نقاط پایانی پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **پنجره زمینه ۱M**: زمینه پیش‌فرض یک میلیون توکن برای اسناد و مکالمات گسترده
- **کدنویسی عاملی SOTA**: از توسعه فرانت‌اند وب تا حل مسائل سطح ریپو پیچیده
- **چندحالتی پیشرفته**: دقت بیشتر و استدلال چندحالتی تیزتر
- **برتری عامل کدنویسی**: ۷۸.۸٪ در SWE-bench Verified، ۶۱.۶٪ در Terminal-Bench 2.0
- **برنامه‌ریزی عمیق**: ۴۱.۵٪ در معیار DeepPlanning (عملکرد پیشرو)
- **پشتیبانی MCP**: ۴۸.۲٪ در MCPMark برای یکپارچه‌سازی Model Context Protocol
- **دکاتلون ابزار**: عملکرد قوی در سناریوهای متنوع استفاده از ابزار

**عملکرد معیار:**
- SWE-bench Verified: ۷۸.۸٪
- SWE-bench Multilingual: ۷۳.۸٪
- SWE-bench Pro: ۵۶.۶٪
- Terminal-Bench 2.0: ۶۱.۶٪
- TAU3-Bench: ۷۰.۷٪
- DeepPlanning: ۴۱.۵٪
- MCPMark: ۴۸.۲٪
- MMLU-Pro: ۸۸.۵٪
- SuperGPQA: ۷۱.۶٪

```python
# نمونه استفاده از Qwen3.6-Plus برای کدنویسی عاملی
response = client.chat.completions.create(
    model="qwen3.6-plus",
    messages=[
        {
            "role": "user",
            "content": "این کدبیس را تحلیل کن و یک رفع باگ برای ماژول احراز هویت پیاده‌سازی کن.",
        }
    ],
    max_tokens=4000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این کدبیس را تحلیل کن و یک رفع باگ برای ماژول احراز هویت پیاده‌سازی کن.",
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

## سری Qwen3.6 (Flash، 27B، 35B-A3B، Max-Preview)

چهار مدل جدید از سری Qwen3.6 با بهبودهای قابل‌توجه در کدنویسی عامل‌محور، استدلال STEM، هوشمندی فضایی و تشخیص اشیا نسبت به نسل Qwen3.5. انواع flash/27B/35B-A3B مدل‌های بینایی‌-زبانی بومی هستند؛ max-preview بزرگ‌ترین و توانمندترین نوع صرفا متنی است.

### qwen3.6-flash

مدل Flash بینایی‌-زبانی بومی Qwen3.6 با پنجره زمینه ۱ میلیون توکنی و بهبود چشم‌گیر در کدنویسی عامل‌محور، استدلال ریاضی و هوشمندی فضایی نسبت به qwen3.5-flash.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.6-flash` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن (قیمت‌گذاری رده‌یک ۲۵۶K) |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.25 / 1M توکن |
| قیمت ورودی (بالای ۲۵۶K) | $1.00 / 1M توکن |
| ساخت کش | $0.3125 / 1M توکن |
| ساخت کش (بالای ۲۵۶K) | $1.25 / 1M توکن |
| قیمت ورودی کش‌شده | $0.025 / 1M توکن (۹۰٪ کاهش هزینه) |
| ورودی کش‌شده (بالای ۲۵۶K) | $0.10 / 1M توکن |
| قیمت خروجی | $1.50 / 1M توکن |
| قیمت خروجی (بالای ۱۲۸K) | $4.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بینایی‌-زبانی بومی**: پردازش بومی متن، تصویر و ویدیو
- **پنجره زمینه ۱M**: زمینه گسترده برای اسناد و مکالمات طولانی
- **کدنویسی عامل‌محور**: به‌طور قابل‌توجه از Qwen3.5-Flash در معیارهای code-agent بهتر عمل می‌کند
- **هوشمندی فضایی**: بهبود چشم‌گیر در مکان‌یابی و تشخیص اشیا
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`
- **پشتیبانی ابزار**: فراخوانی توابع، خروجی ساختارمند و جستجوی وب

```python
response = client.chat.completions.create(
    model="qwen3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "Implement a binary search tree in Python with insert, delete, and in-order traversal methods.",
        }
    ],
    extra_body={"enable_thinking": True},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Implement a binary search tree in Python with insert, delete, and in-order traversal methods.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### qwen3.6-27b

مدل متراکم بینایی‌-زبانی بومی ۲۷ میلیارد پارامتری Qwen3.6 با بهبودهای کلیدی در کدنویسی عامل‌محور، استدلال STEM و قابلیت‌های عامل بصری.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.6-27b` |
| پنجره زمینه | ۲۵۶٬۰۰۰ توکن |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.60 / 1M توکن |
| قیمت ورودی کش‌شده | $0.06 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $3.60 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بینایی‌-زبانی بومی**: پردازش بومی متن، تصویر و ویدیو
- **پنجره زمینه ۲۵۶K**: زمینه گسترده برای وظایف پیچیده
- **استدلال STEM ارتقایافته**: مهارت‌های بهبودیافته استدلال ریاضی و کدنویسی
- **عوامل بصری**: پیشرفت در درک ویدیو، OCR اسناد و قابلیت‌های عامل بصری
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

```python
response = client.chat.completions.create(
    model="qwen3.6-27b",
    messages=[
        {
            "role": "user",
            "content": "Analyze this diagram and extract the workflow steps.",
        }
    ],
    max_tokens=4096,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-27b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Analyze this diagram and extract the workflow steps.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### qwen3.6-35b-a3b

مدل بینایی‌-زبانی بومی ۳۵B-A3B از Qwen3.6 با معماری ترکیبی متشکل از توجه خطی با چارچوب ترکیب پراکنده متخصصان (sparse MoE) برای راندمان استنتاج بالاتر.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.6-35b-a3b` |
| پنجره زمینه | ۲۵۶٬۰۰۰ توکن |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.248 / 1M توکن |
| قیمت ورودی کش‌شده | $0.025 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $1.485 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **معماری ترکیبی**: توجه خطی همراه با MoE پراکنده برای راندمان بالاتر
- **کدنویسی عامل‌محور بهبودیافته**: عملکرد به‌مراتب بهتر code-agent
- **هوشمندی فضایی**: پیشرفت در مکان‌یابی و تشخیص اشیا
- **مقرون‌به‌صرفه**: قیمت‌گذاری بسیار پایین به لطف فعال‌سازی پراکنده کارآمد
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

```python
response = client.chat.completions.create(
    model="qwen3.6-35b-a3b",
    messages=[
        {
            "role": "user",
            "content": "Refactor this monolithic service into microservices.",
        }
    ],
    max_tokens=4096,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-35b-a3b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Refactor this monolithic service into microservices.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### qwen3.6-max-preview

بزرگ‌ترین و توانمندترین نوع سری Qwen3.6 که در حالت پیش‌نمایش با قابلیت‌های صرفا متنی ارائه می‌شود. شامل vibe coding پیشرفته، اجرای کارآمد عامل کدنویسی و بازیابی دانش long-tail ارتقایافته.

| ویژگی | جزئیات |
|-------|--------|
| شناسه مدل | `qwen3.6-max-preview` |
| پنجره زمینه | ۲۵۶٬۰۰۰ توکن (قیمت‌گذاری رده‌یک ۱۲۸K) |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $1.30 / 1M توکن |
| قیمت ورودی (بالای ۱۲۸K) | $2.00 / 1M توکن |
| ساخت کش | $1.625 / 1M توکن |
| ساخت کش (بالای ۱۲۸K) | $2.50 / 1M توکن |
| قیمت ورودی کش‌شده | $0.13 / 1M توکن (۹۰٪ کاهش هزینه) |
| ورودی کش‌شده (بالای ۱۲۸K) | $0.20 / 1M توکن |
| قیمت خروجی | $7.80 / 1M توکن |
| قیمت خروجی (بالای ۱۲۸K) | $12.00 / 1M توکن |
| روش‌های ورودی | متن |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بزرگ‌ترین مدل Qwen3.6**: توانمندترین نوع در سری Qwen3.6
- **Vibe Coding ارتقایافته**: توسعه فرانت‌اند قوی‌تر و اجرای عامل کدنویسی
- **دانش Long-Tail**: بازیابی دانش ارتقایافته برای موضوعات تخصصی
- **پنجره زمینه ۲۵۶K**: زمینه گسترده برای وظایف پیچیده
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

```python
response = client.chat.completions.create(
    model="qwen3.6-max-preview",
    messages=[
        {
            "role": "user",
            "content": "Build a polished Next.js landing page for a SaaS product with hero, features, testimonials, and pricing sections.",
        }
    ],
    max_tokens=8192,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.6-max-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Build a polished Next.js landing page for a SaaS product with hero, features, testimonials, and pricing sections.",
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

## سری Qwen Plus

مدل‌های متعادل که عملکرد عالی در وظایف متنوع ارائه می‌دهند و ترکیب بهینه‌ای از قابلیت و بهره‌وری فراهم می‌کنند.

| ویژگی             | qwen-plus     | qwen-plus-latest  | qwen-plus-2025-09-11 | qwen-plus-2025-07-28 | qwen-plus-2025-07-14 | qwen-plus-2025-04-28 |
| ----------------- | ------------- | ----------------- | -------------------- | -------------------- | -------------------- | -------------------- |
| ارائه‌دهنده       | DashScope     | DashScope         | DashScope            | DashScope            | DashScope            | DashScope            |
| مالک              | Alibaba       | Alibaba           | Alibaba              | Alibaba              | Alibaba              | Alibaba              |
| پنجره زمینه       | ۱۳۱٬۰۷۲ توکن  | ۱۳۱٬۰۷۲ توکن      | ۱۳۱٬۰۷۲ توکن         | ۱۳۱٬۰۷۲ توکن         | ۱۳۱٬۰۷۲ توکن         | ۱۳۱٬۰۷۲ توکن         |
| حداکثر توکن ورودی | ۱۲۹٬۰۲۴       | ۱۲۹٬۰۲۴           | ۱۲۹٬۰۲۴              | ۱۲۹٬۰۲۴              | ۱۲۹٬۰۲۴              | ۱۲۹٬۰۲۴              |
| حداکثر توکن خروجی | ۱۶٬۳۸۴        | ۱۶٬۳۸۴            | ۱۶٬۳۸۴               | ۱۶٬۳۸۴               | ۱۶٬۳۸۴               | ۱۶٬۳۸۴               |
| نقاط قوت          | عملکرد متعادل | آخرین ویژگی‌ها    | استدلال بهبود یافته  | پایدار قبلی          | انتشار پایدار        | نسخه قدیمی           |
| بهترین برای       | وظایف عمومی   | ویژگی‌های پیشرفته | تحلیل پیشرفته        | استفاده تولیدی       | تولید پایدار         | سازگاری قدیمی        |

```python
# مثال استفاده از Qwen Plus برای وظایف عمومی
response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": "مفهوم یادگیری ماشین را برای مبتدی توضیح دهید."}
    ],
    max_tokens=500,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مفهوم یادگیری ماشین را برای مبتدی توضیح دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## سری Qwen3 Max

مدل‌های پریمیوم طراحی‌شده برای پرتقاضاترین کاربردها که قابلیت‌های استدلال برتر و حل مسائل پیچیده ارائه می‌دهند.

> **جدید:** مدل پرچم‌دار `qwen3-max` اکنون برای استدلال پیچیده و گردش‌های کاری عاملی در دسترس است. برای جزئیات به [به‌روزرسانی ۵ ژوئن ۲۰۲۶](fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added.md) مراجعه کنید.

> **⚠️ اطلاعیه منسوخ شدن:** سری قدیمی `qwen-max` (شامل `qwen-max`، `qwen-max-latest`، `qwen-max-2025-01-25`) توسط علی‌بابا بین **۱۳ می ۲۰۲۶** و **۳۱ می ۲۰۲۶** از سرویس خارج می‌شود. لطفا به `qwen3.7-max`، `qwen3-max`، `qwen3.6-plus` یا `qwen3.6-max-preview` مهاجرت کنید. برای جزئیات به [صفحه منسوخ‌شدن‌ها](fa/deprecations.md) مراجعه کنید.

| ویژگی             | qwen3-max                           | qwen3-max-2026-01-23 | qwen3-max-preview |
| ----------------- | ----------------------------------- | -------------------- | ----------------- |
| ارائه‌دهنده       | DashScope                           | DashScope            | DashScope         |
| مالک              | Alibaba                             | Alibaba              | Alibaba           |
| پنجره زمینه       | ۲۶۲٬۱۴۴ توکن                        | ۲۶۲٬۱۴۴ توکن         | ۲۶۲٬۱۴۴ توکن      |
| حداکثر توکن ورودی | ۲۵۸٬۰۴۸                             | ۲۵۸٬۰۴۸              | ۲۵۸٬۰۴۸           |
| حداکثر توکن خروجی | ۳۲٬۷۶۸                              | ۳۲٬۷۶۸               | ۳۲٬۷۶۸            |
| نقاط قوت          | برنامه‌نویسی عامل بهبود یافته       | آخرین نسخه           | ۱T+ پارامتر       |
| بهترین برای       | برنامه‌نویسی عامل، سناریوهای پیچیده | پایداری تولید        | پرتقاضاترین وظایف |

```python
# مثال استفاده از Qwen3-Max برای وظایف برنامه‌نویسی عامل بهبود یافته
response = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {
            "role": "user",
            "content": "یک سیستم عامل هوشمند طراحی کنید که بتواند به طور خودکار گردش‌های کاری چندمرحله‌ای پیچیده را با قابلیت‌های فراخوانی ابزار مدیریت کند.",
        }
    ],
    max_tokens=2000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

# مثال استفاده از Qwen3-Max-Preview برای پرتقاضاترین وظایف
response = client.chat.completions.create(
    model="qwen3-max-preview",
    messages=[
        {
            "role": "user",
            "content": "تحلیل جامعی از تاثیر بالقوه محاسبات کوانتومی بر رمزنگاری و امنیت داده‌ها انجام دهید.",
        }
    ],
    max_tokens=2000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-max` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="تحلیل جامعی از تاثیر بالقوه محاسبات کوانتومی بر رمزنگاری و امنیت داده‌ها انجام دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## سری Qwen 3.5

مدل‌های بومی بینایی-زبان نسل بعدی که بر اساس معماری هیبریدی ساخته شده‌اند و مکانیزم‌های توجه خطی را با ترکیب پراکنده متخصصین ادغام می‌کنند و کارایی استنتاج بالاتری با عملکرد پیشرفته به دست می‌آورند.

| ویژگی             | qwen3.5-plus                         | qwen3.5-plus-2026-02-15              | qwen3.5-flash                        | qwen3.5-397b-a17b                    | qwen3.5-35b-a3b                      |
| ----------------- | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ | ------------------------------------ |
| ارائه‌دهنده       | DashScope                            | DashScope                            | DashScope                            | DashScope                            | DashScope                            |
| مالک              | Alibaba                              | Alibaba                              | Alibaba                              | Alibaba                              | Alibaba                              |
| پارامترها         | میزبانی شده                          | میزبانی شده                          | میزبانی شده                          | ۳۹۷ میلیارد کل، ۱۷ میلیارد فعال      | ۳۵ میلیارد کل، ۳ میلیارد فعال        |
| پنجره زمینه       | ۱٬۰۰۰٬۰۰۰ توکن                       | ۱٬۰۰۰٬۰۰۰ توکن                       | ۱٬۰۰۰٬۰۰۰ توکن                       | ۱۳۱٬۰۷۲ توکن                         | ۱۳۱٬۰۷۲ توکن                         |
| حداکثر توکن خروجی | ۳۲٬۷۶۸                               | ۳۲٬۷۶۸                               | ۱۶٬۳۸۴                               | ۱۶٬۳۸۴                               | ۱۶٬۳۸۴                               |
| ورودی‌ها          | متن، تصویر، ویدیو                    | متن، تصویر، ویدیو                    | متن، تصویر، ویدیو                    | متن، تصویر، ویدیو                    | متن، تصویر، ویدیو                    |
| نقاط قوت          | زمینه ۱ میلیون، ابزارهای داخلی       | نسخه پایدار                          | زمینه ۱ میلیون، کارایی بالا          | Open-weight، عامل‌های قوی            | Open-weight، MoE سبک                 |
| بهترین برای       | زمینه طولانی، عامل‌های چندوجهی       | استقرارهای تولیدی                    | زمینه طولانی مقرون به صرفه            | استقرارهای متن‌باز                   | استقرار لبه، استنتاج کارآمد          |

**ویژگی‌های کلیدی:**

- **معماری هیبریدی**: ادغام توجه خطی (از طریق Gated Delta Networks) با ترکیب پراکنده متخصصین برای کارایی استنتاج بالاتر
- **بینایی-زبان بومی**: پردازش متن، تصویر و ویدیو به صورت بومی
- **پنجره زمینه ۱ میلیون**: زمینه گسترده برای qwen3.5-plus و qwen3.5-flash از طریق Alibaba Cloud Model Studio
- **۲۰۱ زبان**: گسترش پشتیبانی زبان و لهجه از ۱۱۹ به ۲۰۱ زبان
- **ابزارهای داخلی**: پشتیبانی رسمی از استفاده تطبیقی ابزار برای گردش‌های کاری عاملی
- **تفکر عمیق**: قابلیت‌های استدلال پیشرفته هم‌تراز با مدل‌های پیشرو
- **مدل‌های Open-Weight**: qwen3.5-397b-a17b و qwen3.5-35b-a3b متن‌باز تحت مجوز Apache 2.0 هستند

**قیمت‌گذاری:**

| مدل | ورودی | ورودی >256K | ایجاد کش | ایجاد کش >256K | ورودی کش‌شده | ورودی کش‌شده >256K | خروجی | خروجی >256K |
|-------|-------|-------------|----------------|----------------------|--------------|-------------------|--------|--------------|
| qwen3.5-plus | $0.40/1M | $1.20/1M | $0.50/1M | $1.50/1M | $0.04/1M | $0.12/1M | $2.40/1M | $7.20/1M |
| qwen3.5-flash | $0.10/1M | $0.30/1M | $0.125/1M | $0.375/1M | $0.01/1M | $0.03/1M | $0.40/1M | $1.20/1M |
| qwen3.5-397b-a17b | $0.60/1M | - | - | - | $0.06/1M | - | $3.60/1M | - |
| qwen3.5-35b-a3b | $0.25/1M | - | - | - | $0.12/1M | - | $2.00/1M | - |

```python
# مثال استفاده از Qwen3.5 Plus برای وظایف عاملی چندوجهی
response = client.chat.completions.create(
    model="qwen3.5-plus",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این تصویر را تحلیل کن و عناصر کلیدی را توصیف کن.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.png"},
                },
            ],
        }
    ],
    max_tokens=2000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

# مثال استفاده از Qwen3.5-397B برای وظایف استدلال پیچیده
response = client.chat.completions.create(
    model="qwen3.5-397b-a17b",
    messages=[
        {
            "role": "user",
            "content": "یک معماری نرم‌افزاری جامع برای سیستم میکروسرویس‌های توزیع‌شده طراحی کن.",
        }
    ],
    max_tokens=4000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

# مثال استفاده از Qwen3.5-Flash برای پردازش زمینه طولانی مقرون به صرفه
response = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "نکات کلیدی این سند طولانی را خلاصه کن...",
        }
    ],
    max_tokens=2000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

# مثال استفاده از Qwen3.5-35B-A3B برای استنتاج کارآمد open-weight
response = client.chat.completions.create(
    model="qwen3.5-35b-a3b",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "آنچه در این تصویر می‌بینی را توصیف کن."},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=1000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3.5-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
                    "text": "نکات کلیدی این سند طولانی را خلاصه کن...",
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


## جستجوی وب

مدل `qwen3-max` از قابلیت‌های جستجوی وب بلادرنگ پشتیبانی می‌کند و به آن امکان می‌دهد اطلاعات به‌روز را از اینترنت بازیابی کند تا به سوالات درباره رویدادهای جاری، قیمت سهام، آب‌وهوا و سایر داده‌های بلادرنگ که ممکن است در داده‌های آموزشی مدل نباشند، پاسخ دهد.

> **توجه**: از دسامبر ۲۰۲۵، فقط مدل‌های `qwen3-max` و `qwen3-max-2025-09-23` از قابلیت جستجوی وب پشتیبانی می‌کنند. استراتژی جستجو باید برای مناطق بین‌المللی روی `agent` تنظیم شود.

### نحوه کار

وقتی جستجوی وب را با ارسال `enable_search: true` فعال می‌کنید، مدل:
1. تحلیل می‌کند که آیا سوال کاربر نیاز به اطلاعات بلادرنگ دارد
2. در صورت نیاز، یک جستجوی وب انجام می‌دهد و از نتایج برای تولید پاسخ استفاده می‌کند
3. در غیر این صورت، از دانش خود برای پاسخ‌دهی استفاده می‌کند

### مثال استفاده

```language-selector
bash=:curl -X POST https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "qwen3-max",
    "messages": [
        {
            "role": "user",
            "content": "قیمت سهام علی‌بابا چقدر است"
        }
    ],
    "enable_search": true,
    "search_options": {"search_strategy": "agent"}
}'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="qwen3-max",
    messages=[{"role": "user", "content": "پیش‌بینی آب‌وهوا برای فردا در تهران چیست؟"}],
    extra_body={"enable_search": True, "search_options": {"search_strategy": "agent"}},
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3-max",
  messages: [
    { role: "user", content: "آخرین اخبار فناوری امروز چیست؟" }
  ],
  enable_search: true,
  search_options: { search_strategy: "agent" }
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-max` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="آخرین اخبار فناوری امروز چیست؟",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "آخرین اخبار فناوری امروز چیست؟",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "آخرین اخبار فناوری امروز چیست؟",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پارامترها

| پارامتر | نوع | توضیحات |
|---------|-----|---------|
| `enable_search` | boolean | برای فعال‌سازی جستجوی وب روی `true` تنظیم کنید. مدل تصمیم می‌گیرد آیا جستجو لازم است. |
| `search_options.search_strategy` | string | باید برای مناطق بین‌المللی روی `"agent"` تنظیم شود. |

### موارد استفاده

- **قیمت‌های بلادرنگ سهام**: دریافت داده‌های فعلی بازار و اطلاعات سهام
- **پیش‌بینی آب‌وهوا**: بازیابی پیش‌بینی‌های به‌روز آب‌وهوا برای هر مکان
- **رویدادهای جاری**: پاسخ به سوالات درباره اخبار و رویدادهای اخیر
- **نتایج ورزشی**: دریافت نتایج زنده یا اخیر مسابقات
- **اطلاعات محصول**: یافتن قیمت‌ها و موجودی فعلی

### صورتحساب

جستجوی وب شامل دو جزء هزینه است:
1. **هزینه‌های فراخوانی مدل**: نتایج جستجوی وب به پرامپت اضافه می‌شوند و توکن‌های ورودی را افزایش می‌دهند. قیمت‌گذاری استاندارد مدل اعمال می‌شود.
2. **هزینه‌های سیاست جستجو**: برای استراتژی `agent` در مناطق بین‌المللی، هزینه ۱۰.۰۰ دلار به ازای هر ۱٬۰۰۰ فراخوانی است.

## مدل‌های بینایی-زبانی

مدل‌های چندوجهی قادر به درک و پردازش هم ورودی‌های متنی و هم بصری که امکان تحلیل و توصیف پیچیده تصاویر را فراهم می‌کنند.

### سری Qwen3 VL

مدل‌های بینایی-زبانی نسل جدید با قابلیت‌های بهبود یافته برای درک تصاویر، ویدیوها و متن.

| مدل                   | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | بهترین برای                      |
| --------------------- | ----------- | ------------ | ------------ | -------------------------------- |
| qwen3-vl-32b-instruct | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۸٬۱۹۲        | وظایف VL متعادل منبع‌باز         |
| qwen3-vl-plus         | ۱۳۱٬۰۷۲+    | ۱۲۹٬۰۲۴+     | ۸٬۱۹۲        | متن بلند، ویدیو، وظایف عامل     |
| qwen3-vl-flash        | ۱۳۱٬۰۷۲+    | ۱۲۹٬۰۲۴+     | ۸٬۱۹۲        | وظایف VL سریع و مقرون‌به‌صرفه   |

**ویژگی‌های کلیدی:**

- **پشتیبانی از اسناد بلند**: پردازش اسناد با میلیون‌ها توکن
- **درک ویدیوی طولانی**: تحلیل ویدیوهای تا ۱ ساعت
- **قابلیت‌های OCR**: استخراج متن پیشرفته از تصاویر
- **قابلیت‌های عامل**: بازیابی تصویر و استفاده از ابزار
- **قیمت‌گذاری طبقه‌ای**: بهینه‌سازی هزینه بر اساس طول زمینه

```python
# مثال استفاده از Qwen3-VL-Plus برای وظایف بینایی-زبانی
response = client.chat.completions.create(
    model="qwen3-vl-plus",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این سند را تحلیل کن و اطلاعات کلیدی را استخراج کن.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/document.png"},
                },
            ],
        }
    ],
    extra_body={"enable_thinking": False},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-vl-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


### سری Qwen 2.5 VL

| مدل                     | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | بهترین برای          |
| ----------------------- | ----------- | ------------ | ------------ | -------------------- |
| qwen2.5-vl-72b-instruct | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۸٬۱۹۲        | وظایف بینایی پیچیده  |
| qwen2.5-vl-32b-instruct | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۸٬۱۹۲        | پردازش بینایی متعادل |
| qwen2.5-vl-7b-instruct  | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۸٬۱۹۲        | وظایف بینایی کارآمد  |
| qwen2.5-vl-3b-instruct  | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۸٬۱۹۲        | بینایی سبک           |

### Qwen VL OCR

> **⚠️ اطلاعیه منسوخ شدن:** سری‌های قدیمی `qwen-vl-max` و `qwen-vl-plus` (شامل `-latest` و snapshotهای تاریخ‌دار) توسط علی‌بابا بین **۱۳ می ۲۰۲۶** و **۳۱ می ۲۰۲۶** از سرویس خارج می‌شوند. لطفا به سری Qwen3 VL (مثلا `qwen3-vl-plus`، `qwen3-vl-flash`) یا مدل‌های Qwen 3.5 VL مهاجرت کنید. برای جزئیات به [صفحه منسوخ‌شدن‌ها](fa/deprecations.md) مراجعه کنید.

| مدل          | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص             |
| ------------ | ----------- | ------------ | ------------ | ---------------- |
| qwen-vl-ocr  | ۳۴٬۰۹۶      | ۳۰٬۰۰۰       | ۴٬۰۹۶        | تشخیص نویسه نوری |

```python
# مثال استفاده از Qwen VL برای تحلیل تصویر
response = client.chat.completions.create(
    model="qwen2.5-vl-72b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "چه اشیایی در این تصویر می‌بینید و موقعیت تقریبی آن‌ها کجاست؟",
                },
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
                    },
                },
            ],
        }
    ],
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen2.5-vl-72b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


## سری Qwen 3

مدل‌های نسل بعدی با قابلیت‌های بهبود یافته و عملکرد بهتر در وظایف مختلف.

### مدل‌های استاندارد Qwen 3

| مدل        | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | پارامترها |
| ---------- | ----------- | ------------ | ------------ | --------- |
| qwen3-32b  | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۱۶٬۳۸۴       | ۳۲B       |
| qwen3-14b  | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۸٬۱۹۲        | ۱۴B       |
| qwen3-8b   | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۸٬۱۹۲        | ۸B        |
| qwen3-4b   | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۸٬۱۹۲        | ۴B        |
| qwen3-1.7b | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۸٬۱۹۲        | ۱.۷B      |
| qwen3-0.6b | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۸٬۱۹۲        | ۰.۶B      |

### سری Qwen 3 A3B

| مدل                         | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص                            |
| --------------------------- | ----------- | ------------ | ------------ | ------------------------------- |
| qwen3-next-80b-a3b-thinking | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۳۲٬۷۶۸       | استدلال پیشرفته با تفکر         |
| qwen3-next-80b-a3b-instruct | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۳۲٬۷۶۸       | پیروی بهبود یافته از دستورالعمل |
| qwen3-30b-a3b               | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۳۲٬۷۶۸       | استدلال پیشرفته                 |
| qwen3-30b-a3b-thinking-2507 | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۳۲٬۷۶۸       | فرآیندهای تفکر                  |
| qwen3-30b-a3b-instruct-2507 | ۱۳۱٬۰۷۲     | ۹۸٬۳۰۴       | ۳۲٬۷۶۸       | پیروی از دستورالعمل             |

### سری Qwen 3 A22B

| مدل                           | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص                   |
| ----------------------------- | ----------- | ------------ | ------------ | ---------------------- |
| qwen3-235b-a22b               | ۱۳۱٬۰۷۲     | ۱۳۱٬۰۷۲      | ۳۲٬۷۶۸       | استدلال بزرگ مقیاس     |
| qwen3-235b-a22b-instruct-2507 | ۱۳۱٬۰۷۲     | ۱۳۱٬۰۷۲      | ۳۲٬۷۶۸       | دستورالعمل‌های پیشرفته |
| qwen3-235b-a22b-thinking-2507 | ۱۳۱٬۰۷۲     | ۱۳۱٬۰۷۲      | ۳۲٬۷۶۸       | تفکر پیچیده            |

## مدل‌های تخصصی

### سری QWQ Plus (مدل‌های استدلال)

| مدل                 | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تمرکز           |
| ------------------- | ----------- | ------------ | ------------ | --------------- |
| qwq-plus            | ۱۳۱٬۰۷۲     | ۱۳۱٬۰۷۲      | ۸٬۱۹۲        | استدلال پیشرفته |
| qwq-plus-2025-03-05 | ۱۳۱٬۰۷۲     | ۱۳۱٬۰۷۲      | ۸٬۱۹۲        | استدلال پایدار  |

### مدل‌های ترجمه ماشینی

مدل‌های ترجمه حرفه‌ای با پشتیبانی از ۹۲ زبان و ترجمه دوطرفه با کیفیت بالا.

| مدل           | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص              |
| ------------- | ----------- | ------------ | ------------ | ----------------- |
| qwen-mt-plus  | ۲٬۰۴۸       | ۲٬۰۴۸        | ۲٬۰۴۸        | ترجمه پیشرفته     |
| qwen-mt-turbo | ۲٬۰۴۸       | ۲٬۰۴۸        | ۲٬۰۴۸        | ترجمه سریع        |
| qwen-mt-flash | ۸٬۱۹۲       | ۸٬۱۹۲        | ۸٬۱۹۲        | ترجمه با کیفیت بالا |
| qwen-mt-lite  | ۸٬۱۹۲       | ۸٬۱۹۲        | ۸٬۱۹۲        | سریع و مقرون‌به‌صرفه |

**ویژگی‌های کلیدی:**

- **۹۲ زبان**: پشتیبانی از زبان‌های اصلی جهان شامل اروپایی، آسیایی و خاورمیانه‌ای
- **دوطرفه**: ترجمه بین هر جفت زبان پشتیبانی شده
- **ترجمه مستقیم**: ترجمه بین زبان‌های غیرچینی بدون چینی واسط
- **پشتیبانی فارسی/دری**: پشتیبانی کامل از فارسی، دری، عربی، اردو، ترکی و بیشتر

**زبان‌های پشتیبانی شده شامل:**
عربی، چینی (ساده‌شده/سنتی)، هلندی، انگلیسی، فرانسوی، آلمانی، ایتالیایی، ژاپنی، کره‌ای، فارسی، پرتغالی، روسی، اسپانیایی، ترکی، ویتنامی و ۷۷ زبان دیگر.

```python
# مثال استفاده از Qwen-MT برای ترجمه
response = client.chat.completions.create(
    model="qwen-mt-flash",
    messages=[
        {"role": "system", "content": "از انگلیسی به فارسی ترجمه کن"},
        {
            "role": "user",
            "content": "Artificial intelligence is transforming the way we live and work.",
        },
    ],
    extra_body={"enable_thinking": False},
)
# خروجی: هوش مصنوعی در حال تغییر نحوه زندگی و کار ما است.
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen-mt-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Artificial intelligence is transforming the way we live and work.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدل‌های شخصیت/نقش‌آفرینی

مدل‌های تخصصی برای ایجاد تعاملات ثابت شخصیت مجازی با حفظ شخصیت.

| مدل                | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص                          |
| ------------------ | ----------- | ------------ | ------------ | ----------------------------- |
| qwen-plus-character | ۱۳۱٬۰۷۲     | ۱۲۹٬۰۲۴      | ۱۶٬۳۸۴       | شخصیت‌های مجازی، نقش‌آفرینی |

**ویژگی‌های کلیدی:**

- **ثبات شخصیت**: حفظ شخصیت‌ها، ویژگی‌ها و سبک‌های گفتار تعریف‌شده در مکالمات
- **تنوع پاسخ**: جلوگیری از پاسخ‌های تکراری با نشانگرهای سبک
- **حافظه رابطه**: حفظ تاریخچه تعامل و پویایی رابطه
- **انعطاف‌پذیری ژانر**: پشتیبانی از فانتزی، علمی-تخیلی، رمانتیک و سناریوهای مدرن

```python
# مثال استفاده از Qwen-Plus-Character برای شخصیت‌های مجازی
response = client.chat.completions.create(
    model="qwen-plus-character",
    messages=[
        {
            "role": "system",
            "content": "تو یک جادوگر خردمند به نام مرلین از دنیای فانتزی هستی. با حکمت باستانی و گاهی معماها صحبت کن.",
        },
        {"role": "user", "content": "مرلین، چگونه می‌توانم یک جادوگر بزرگ شوم؟"},
    ],
    extra_body={"enable_thinking": False},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen-plus-character` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مرلین، چگونه می‌توانم یک جادوگر بزرگ شوم؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدل‌های زمینه طولانی

| مدل                     | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص               |
| ----------------------- | ----------- | ------------ | ------------ | ------------------ |
| qwen2.5-7b-instruct-1m  | ۱٬۰۰۸٬۱۹۲   | ۱٬۰۰۰٬۰۰۰    | ۸٬۱۹۲        | زمینه میلیون توکنی |
| qwen2.5-14b-instruct-1m | ۱٬۰۰۸٬۱۹۲   | ۱٬۰۰۰٬۰۰۰    | ۸٬۱۹۲        | زمینه توسعه‌یافته  |

### مدل‌های برنامه‌نویسی

| مدل                            | پنجره زمینه | حداکثر ورودی | حداکثر خروجی | تخصص                              |
| ------------------------------ | ----------- | ------------ | ------------ | --------------------------------- |
| qwen3-coder-480b-a35b-instruct | ۲۶۲٬۱۴۴     | ۲۰۴٬۸۰۰      | ۶۵٬۵۳۶       | برنامه‌نویسی پیشرفته              |
| qwen3-coder-next               | ۱٬۰۰۰٬۰۰۰   | ۹۹۷٬۹۵۲      | ۶۵٬۵۳۶       | عامل‌های کدنویسی پیشرو (80B MoE)  |
| qwen3-coder-flash              | ۱٬۰۰۰٬۰۰۰   | ۹۹۷٬۹۵۲      | ۶۵٬۵۳۶       | برنامه‌نویسی سریع با قیمت طبقه‌ای |
| qwen3-coder-flash-2025-07-28   | ۱٬۰۰۰٬۰۰۰   | ۹۹۷٬۹۵۲      | ۶۵٬۵۳۶       | برنامه‌نویسی سریع پایدار          |
| qwen3-coder-plus               | ۱٬۰۰۰٬۰۰۰   | ۹۹۷٬۹۵۲      | ۶۵٬۵۳۶       | تولید کد                          |
| qwen3-coder-plus-2025-07-22    | ۱٬۰۰۰٬۰۰۰   | ۹۹۷٬۹۵۲      | ۶۵٬۵۳۶       | آخرین برنامه‌نویسی                |

**Qwen3-Coder-Next**

Qwen3-Coder-Next یک مدل پیشرو 80B MoE (ترکیب متخصصین) است که برای عامل‌های برنامه‌نویسی بهینه‌سازی شده و دارای ۱۰ میلیارد پارامتر فعال برای استنتاج کارآمد است.

**ویژگی‌های کلیدی:**

- **معماری 80B MoE**: ترکیب متخصصین در مقیاس بزرگ با ۱۰ میلیارد پارامتر فعال
- **پنجره زمینه ۱ میلیون**: زمینه گسترده برای درک پایگاه‌های کد بزرگ
- **بهینه‌سازی عاملی**: طراحی شده برای گردش‌های کاری برنامه‌نویسی خودمختار
- **کارایی بالا**: استنتاج بهینه با فعال‌سازی پراکنده

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش‌شده | خروجی |
|-------|-------|--------------|--------|
| qwen3-coder-next | $0.30/1M | $0.15/1M | $1.50/1M |

```python
# مثال استفاده از Qwen3-Coder-Next برای وظایف کدنویسی عاملی
response = client.chat.completions.create(
    model="qwen3-coder-next",
    messages=[
        {
            "role": "user",
            "content": "این پایگاه کد را تحلیل کن و ماژول احراز هویت را بازنویسی کن تا از توکن‌های JWT با چرخش توکن رفرش استفاده کند.",
        }
    ],
    max_tokens=8000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

# مثال استفاده از Qwen Coder برای وظایف برنامه‌نویسی
response = client.chat.completions.create(
    model="qwen3-coder-plus",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای پیاده‌سازی الگوریتم جستجوی دودویی با مدیریت خطای مناسب بنویسید.",
        }
    ],
    max_tokens=1000,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-coder-next` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع Python برای پیاده‌سازی الگوریتم جستجوی دودویی با مدیریت خطای مناسب بنویسید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مدل‌های تولید تصویر

مدل‌های پیشرفته تولید و ویرایش تصویر با پشتیبانی دوگانه SDK، سازگار با schema OpenAI و schema بومی Alibaba Dashscope.

| مدل                  | تخصص                   | هزینه به ازای تصویر    | گزینه‌های رزولوشن         | بهترین برای              |
| -------------------- | ---------------------- | --------------------- | ------------------------- | ------------------------ |
| qwen-image-3.0-pro   | تولید و ویرایش حرفه‌ای | $0.04 در حدود ۱ MP؛ $0.075 در ۲ تا ۴ MP | ۱K تا ۴ MP | گردش‌کارهای تصویری production |
| qwen-image-3.0       | تولید و ویرایش عمومی   | $0.04 در حدود ۱ MP؛ $0.075 در ۲ تا ۴ MP | ۱K تا ۴ MP | گردش‌کارهای تصویری عمومی |
| qwen-image-2.0-pro   | تایپوگرافی حرفه‌ای     | $0.06                 | رزولوشن بومی ۲K           | اینفوگرافیک‌ها، متن پیچیده |
| qwen-image-2.0       | تولید متعادل          | $0.04                 | رزولوشن بومی ۲K           | تولید تصویر همه‌منظوره    |
| qwen-image           | تولید متن-به-تصویر     | $0.035                | 1:1، 4:3، 3:4، 16:9، 9:16 | تولید تصویر خلاقانه      |
| qwen-image-edit      | ویرایش و اصلاح تصویر   | $0.045                | بر اساس تصویر ورودی       | بهبود و ویرایش تصویر     |
| z-image-turbo        | متن-به-تصویر سریع      | $0.015 (استاندارد) / $0.030 (تفکر) | ۵۱۲×۵۱۲ تا ۲۰۴۸×۲۰۴۸ | تولید سریع، رندر متن |
| qwen-image-edit-plus | ویرایش پیشرفته تصویر   | $0.03                 | بر اساس تصویر ورودی       | ویرایش حرفه‌ای، انتقال سبک |

### qwen-image-3.0-pro و qwen-image-3.0

[`qwen-image-3.0-pro`](fa/models/qwen-image-3.0-pro.md) و [`qwen-image-3.0`](fa/models/qwen-image-3.0.md) از تولید تصویر جدید و ویرایش تصویر منبع از طریق Images API سازگار با OpenAI پشتیبانی می‌کنند.

| ویژگی | جزئیات |
|--------|--------|
| شناسه مدل‌ها | `qwen-image-3.0-pro`، `qwen-image-3.0` |
| نرخ حسابداری خروجی | $40.00 / 1M توکن خروجی |
| تصویر خروجی ۱K / حدود ۱ MP | $0.04 / تصویر |
| تصویر خروجی ۲ تا ۴ MP | $0.075 / تصویر |
| تصویر مرجع/ورودی | $0.003 / تصویر |
| اندپوینت‌های پشتیبانی‌شده | `/v1/images/generations`، `/v1/images/edits` |

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

result = client.images.generate(
    model="qwen-image-3.0-pro",
    prompt="یک تصویرسازی editorial تمیز از شهر انرژی‌های تجدیدپذیر با فضای خالی برای عنوان",
    size="1024x1024",
)

print(result.data[0].url)
```

برای ویرایش، تصویر منبع را به `/v1/images/edits` بفرستید؛ هر تصویر مرجع/ورودی $0.003 به هزینه درخواست اضافه می‌کند.

### qwen-image-2.0-pro

**مدل تولید تصویر Qwen-Image-2.0-Pro** با تمرکز بر تایپوگرافی حرفه‌ای و طراحی‌های پیچیده بصری.

**ویژگی‌های کلیدی:**

- **تایپوگرافی پیشرفته**: رندر متن با خطاهای نزدیک به صفر در بیش از ۴۰ زبان
- **رزولوشن بومی ۲K**: خروجی با کیفیت بالا بدون نیاز به upscaling
- **تولید و ویرایش یکپارچه**: پشتیبانی از هر دو گردش‌کار در یک مدل
- **پشتیبانی چندزبانه**: رندر حرفه‌ای متن فارسی، عربی، چینی و سایر زبان‌ها

**قیمت‌گذاری:**

| مدل | هزینه به ازای تصویر |
|-------|---------------------|
| qwen-image-2.0-pro | $0.06 |

```python
# تولید اینفوگرافیک حرفه‌ای با Qwen-Image-2.0-Pro
response = client.images.generate(
    model="qwen-image-2.0-pro",
    prompt="یک اینفوگرافیک حرفه‌ای برای معماری هوش مصنوعی با عنوان 'سیستم پردازش زبان طبیعی' شامل نمودارهای جریان داده و برچسب‌های فارسی",
    size="2048x2048",
    n=1,
)
```

### qwen-image-2.0

**مدل تولید تصویر Qwen-Image-2.0** با تعادل بهینه بین کیفیت و هزینه.

**ویژگی‌های کلیدی:**

- **فوتورئالیسم بهبود یافته**: تولید تصاویر واقع‌گرایانه با جزئیات بالا
- **رندر متن قابل اعتماد**: پشتیبانی از متن چندزبانه با دقت بالا
- **رزولوشن بومی ۲K**: خروجی با کیفیت بدون نیاز به پس‌پردازش
- **پشتیبانی از ویرایش**: قابلیت تولید و ویرایش تصویر

**قیمت‌گذاری:**

| مدل | هزینه به ازای تصویر |
|-------|---------------------|
| qwen-image-2.0 | $0.04 |

```python
# تولید تصویر با Qwen-Image-2.0
response = client.images.generate(
    model="qwen-image-2.0",
    prompt="یک منظره طبیعی با کوه‌های برفی و دریاچه آبی در غروب آفتاب با سبک فوتورئالیستیک",
    size="2048x2048",
    n=1,
)
```

### z-image-turbo

مدل تولید تصویر سریع و با کیفیت بالا که برای سرعت بهینه‌سازی شده با رندر متن عالی.

**ویژگی‌های کلیدی:**

- **تولید پرسرعت**: بهینه‌سازی شده برای گردش‌های کاری تولید سریع
- **رندر متن بهبود یافته**: ثبات بهتر تولید کاراکتر و متن
- **پشتیبانی از تاج**: افزودن لوگو یا واترمارک به تصاویر تولید شده
- **اندازه‌های انعطاف‌پذیر**: ۴۲ نسبت پیش‌فرض به علاوه اندازه‌های سفارشی (۵۱۲×۵۱۲ تا ۲۰۴۸×۲۰۴۸)
- **حالت تفکر**: تولید بهبود یافته اختیاری با $0.030 به ازای هر تصویر

```python
# مثال استفاده از z-image-turbo
response = client.images.generate(
    model="z-image-turbo",
    prompt="یک لوگوی حرفه‌ای با متن 'AI TECH' به سبک مینیمالیست مدرن",
    size="1024x1024",
    n=1,
)
```

### qwen-image-edit-plus

مدل ویرایش پیشرفته تصویر که عملیات پیچیده شامل حذف پس‌زمینه، inpainting و انتقال سبک را پشتیبانی می‌کند.

**ویژگی‌های کلیدی:**

- **حذف پس‌زمینه**: جداسازی سوژه‌ها از پس‌زمینه
- **Inpainting تصویر**: پر کردن یا جایگزینی نواحی انتخاب شده
- **انتقال سبک**: اعمال سبک‌های هنری به تصاویر
- **جستجو و تغییر رنگ**: تغییر رنگ‌ها در نواحی خاص
- **کنترل ساختار**: حفظ سازگاری ساختاری در ویرایش‌ها

```python
# مثال استفاده از qwen-image-edit-plus برای حذف پس‌زمینه
import requests

with open("input_image.png", "rb") as image_file:
    response = requests.post(
        "https://api.avalai.ir/v1/images/edits",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"image": image_file},
        data={
            "model": "qwen-image-edit-plus",
            "prompt": "پس‌زمینه را حذف کن و فقط سوژه اصلی را نگه دار",
        },
    )
```

### ویژگی‌های کلیدی

- **پشتیبانی دوگانه SDK**: سازگار با فرمت OpenAI SDK و API بومی Dashscope
- **رزولوشن‌های متعدد**: پشتیبانی از نسبت‌های مختلف ابعاد (1328×1328، 1664×928، 1472×1140، 1140×1472، 928×1664)
- **پارامترهای پیشرفته**: promptهای منفی، بازنویسی هوشمند prompt، کنترل watermark، پشتیبانی seed
- **کیفیت بالا**: تولید تصویر درجه حرفه‌ای با پارامترهای قابل تنظیم

### مثال‌های استفاده

```python
# تولید متن-به-تصویر با استفاده از فرمت OpenAI SDK
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="qwen-image",
    prompt="منظره آرام کوهستانی با دریاچه شفاف که قله‌های برفی را منعکس می‌کند",
    size="1328x1328",
    n=1,
    response_format="url",  # or b64_json
)

print(response.data[0].url)

# ویرایش تصویر با استفاده از فرمت OpenAI SDK
import requests

with open("input_image.jpg", "rb") as image_file:
    response = requests.post(
        "https://api.avalai.ir/v1/images/edits",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"image": image_file},
        data={
            "model": "qwen-image-edit",
            "prompt": "آسمان را به غروب دراماتیک با رنگ‌های نارنجی و بنفش تغییر دهید",
        },
    )

print(response.json())
```

### فرمت بومی Dashscope

```python
# استفاده از schema بومی Dashscope برای پارامترهای پیشرفته
import requests

response = requests.post(
    "https://api.avalai.ir/v1/images/generations",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "qwen-image",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "عکس پرتره حرفه‌ای از یک فرد تجاری مطمئن در محیط اداری مدرن"
                        }
                    ],
                }
            ]
        },
        "parameters": {
            "size": "1328*1328",
            "prompt_extend": True,
            "watermark": False,
            "negative_prompt": "تار، کیفیت پایین، تحریف شده",
        },
    },
)

print(response.json())
```

## مدل‌های Embedding

مدل‌های embedding پیشرفته برای محتوای متنی و چندوجهی که از جستجوی معنایی، محاسبه شباهت و طبقه‌بندی محتوا پشتیبانی می‌کنند.

### مدل‌های Embedding متنی

| مدل               | ابعاد بردار           | حداکثر توکن | تخصص                               | قیمت (به ازای 1M توکن) |
| ----------------- | --------------------- | ----------- | ---------------------------------- | ---------------------- |
| text-embedding-v4 | 64-2,048 (قابل تنظیم) | 8,192       | آخرین نسل، دستورالعمل‌های کار، بردارهای پراکنده | $0.07   |
| text-embedding-v3 | 512-1,024 (قابل تنظیم) | 8,192       | نسل قبلی، عملکرد اثبات شده         | $0.07                  |

#### text-embedding-v4

آخرین نسل مدل embedding متنی با ویژگی‌های پیشرفته:

**ویژگی‌های کلیدی:**
- **ابعاد قابل تنظیم**: 2,048، 1,536، 1,024 (پیش‌فرض)، 768، 512، 256، 128، 64
- **دستورالعمل‌های کار (instruct)**: بهینه‌سازی کیفیت بردار برای سناریوهای بازیابی خاص
- **تمایز نوع متن**: embedding‌های جداگانه برای متن پرس‌وجو در مقابل سند
- **بردارهای متراکم و پراکنده**: تولید هر دو نوع برای جستجوی ترکیبی
- **پردازش دسته‌ای**: پردازش تا 10 متن در هر درخواست

**موارد استفاده:**
- جستجو و بازیابی معنایی
- گفتگوی هوش مصنوعی و توصیه محتوا
- موتورهای جستجوی تولیدی با کیفیت بالا
- طبقه‌بندی و خوشه‌بندی

**مثال:**

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "text-embedding-v4",
    "input": "یادگیری ماشین در حال تحول فناوری است",
    "dimensions": 1024
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="text-embedding-v4",
    input="یادگیری ماشین در حال تحول فناوری است",
    dimensions=1024,
)

print(response.data[0].embedding)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "text-embedding-v4",
  input: "یادگیری ماشین در حال تحول فناوری است",
  dimensions: 1024,
});

console.log(response.data[0].embedding);

```

**ویژگی‌های پیشرفته با API بومی:**

```python
# استفاده از extra_body برای ویژگی‌های پیشرفته
response = client.embeddings.create(
    model="text-embedding-v4",
    input="مقالات تحقیقاتی درباره یادگیری ماشین",
    dimensions=1024,
    extra_body={
        "text_type": "query",  # یا "document"
        "instruct": "با توجه به یک پرس‌وجوی مقاله تحقیقاتی، مقالات تحقیقاتی مرتبط را بازیابی کنید",
    },
)
```

#### text-embedding-v3

نسل قبلی مدل embedding متنی با عملکرد اثبات شده:

**ویژگی‌های کلیدی:**
- **ابعاد قابل تنظیم**: 1,024 (پیش‌فرض)، 768، 512
- **عملکرد قابل اعتماد**: آزمایش شده در بیش از 50 زبان
- **پردازش دسته‌ای**: پردازش تا 10 متن در هر درخواست

### مدل‌های Embedding چندوجهی

| مدل                          | ابعاد بردار | حداکثر توکن متن | پشتیبانی تصویر/ویدیو | قیمت (به ازای 1M توکن) |
| ---------------------------- | ----------- | --------------- | -------------------- | ---------------------- |
| tongyi-embedding-vision-plus | 1,152       | 1,024           | تصاویر و ویدیوها    | $0.09                  |
| tongyi-embedding-vision-flash | 768         | 1,024           | تصاویر و ویدیوها    | تصویر/ویدیو: $0.03، متن: $0.09 |

#### tongyi-embedding-vision-plus

مدل embedding چندوجهی پیشرفته با پشتیبانی از متن، تصاویر و ویدیوها:

**ویژگی‌های کلیدی:**
- **بازیابی متقابل**: جستجوی متن-به-تصویر، تصویر-به-ویدیو، تصویر-به-تصویر
- **شباهت معنایی**: محاسبه شباهت در روش‌های مختلف
- **ورودی‌های متعدد**: پشتیبانی تا 8 تصویر در هر درخواست
- **پشتیبانی ویدیو**: پردازش ویدیوها تا 10 MB (MP4, MPEG, AVI, MOV, MPG, WEBM, FLV, MKV)
- **فرمت‌های تصویر**: JPG, PNG, BMP (Base64 یا URL)

**موارد استفاده:**
- جستجوی معنایی متقابل
- طبقه‌بندی و تحلیل ویدیو
- جستجوی تصویر با استفاده از متن یا تصاویر دیگر
- طبقه‌بندی و خوشه‌بندی محتوا

**مثال:**

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "tongyi-embedding-vision-plus",
    "input": {
      "contents": [
        {"text": "یک غروب زیبا بر فراز کوه‌ها"},
        {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"}
      ]
    }
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از extra_body برای فرمت بومی Alibaba
response = client.embeddings.create(
    model="tongyi-embedding-vision-plus",
    input="placeholder",  # مورد نیاز OpenAI SDK
    extra_body={
        "input": {
            "contents": [
                {"text": "یک غروب زیبا بر فراز کوه‌ها"},
                {
                    "image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
                },
            ]
        }
    },
)

print(response.data[0].embedding)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// توجه: برای embedding‌های چندوجهی، از درخواست‌های HTTP بومی استفاده کنید
const response = await fetch("https://api.avalai.ir/v1/embeddings", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        model: "tongyi-embedding-vision-plus",
        input: {
            contents: [
                { text: "یک غروب زیبا بر فراز کوه‌ها" },
                { image: "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png" }
            ]
        }
    })
});

const result = await response.json();
console.log(result.data[0].embedding);

```

#### tongyi-embedding-vision-flash

مدل embedding چندوجهی سریع بهینه‌شده برای سرعت:

**ویژگی‌های کلیدی:**
- **سرعت بالا**: بهینه‌سازی شده برای پردازش سریع
- **پشتیبانی چندوجهی**: متن، تصاویر و ویدیوها
- **مقرون به صرفه**: قیمت‌گذاری پایین‌تر برای پردازش تصویر/ویدیو
- **قابلیت‌های یکسان**: ویژگی‌های مشابه vision-plus با استنتاج سریع‌تر

**قیمت‌گذاری:**
- توکن‌های تصویر/ویدیو: $0.03 به ازای 1M توکن
- توکن‌های متن: $0.09 به ازای 1M توکن

### بهترین شیوه‌های Embedding

1. **انتخاب بُعد**:
   - از 1024 بُعد برای تعادل بهینه عملکرد و هزینه استفاده کنید
   - از ابعاد بالاتر (1536، 2048) برای حوزه‌هایی که به دقت بالا نیاز دارند استفاده کنید
   - از ابعاد پایین‌تر (768 یا کمتر) برای سناریوهای حساس به هزینه استفاده کنید

2. **تمایز نوع متن** (فقط text-embedding-v4):
   - از `text_type: "query"` برای پرس‌وجوهای جستجوی کاربر استفاده کنید
   - از `text_type: "document"` برای اسناد در پایگاه داده خود استفاده کنید

3. **دستورالعمل‌های کار** (فقط text-embedding-v4):
   - دستورالعمل‌های واضح انگلیسی برای بهینه‌سازی کیفیت بردار ارائه دهید
   - مثال: "با توجه به یک پرس‌وجوی مقاله تحقیقاتی، مقالات تحقیقاتی مرتبط را بازیابی کنید"

4. **Embedding‌های چندوجهی**:
   - همه روش‌ها بردارها را در همان فضای معنایی تولید می‌کنند
   - شباهت کسینوسی را مستقیما بین روش‌های مختلف محاسبه کنید
   - از vision-flash برای برنامه‌های پرحجم استفاده کنید

5. **پردازش دسته‌ای**:
   - چندین متن را در یک درخواست پردازش کنید (تا 10)
   - هر متن نباید از محدودیت‌های توکن تجاوز کند

### منابع مرتبط

- [راهنمای Embedding و بازیابی](fa/guides/retrieval.md)
- [پارامترهای خاص ارائه‌دهنده](fa/guides/provider-specific-params.md)
- [راهنمای قابلیت‌های بینایی](fa/guides/vision.md)

## مدل‌های رتبه‌بندی مجدد (Rerank)

مدل‌های رتبه‌بندی مجدد مرتب‌سازی دقیق‌تری از اسناد بازیابی شده انجام می‌دهند تا اطمینان حاصل شود که مرتبط‌ترین نتایج در بالا ظاهر شوند، که برای برنامه‌های RAG و جستجوی معنایی ضروری است.

| مدل | حداکثر اسناد | حداکثر توکن در هر مورد | حداکثر توکن در هر درخواست | زبان‌ها | قیمت‌گذاری (به ازای 1M توکن) |
|-----|--------------|------------------------|--------------------------|---------|------------------------------|
| qwen3-rerank | 500 | 4,000 | 30,000 | بیش از 100 زبان | $0.10 |

### qwen3-rerank

یک مدل رتبه‌بندی متن آموزش دیده بر پایه LLM Qwen که رتبه‌بندی ارتباط برای پرس‌وجوهای ورودی و اسناد کاندید انجام می‌دهد. این مدل از بیش از 100 زبان و ورودی‌های متن طولانی پشتیبانی می‌کند.

**ویژگی‌های کلیدی:**
- **رتبه‌بندی با دقت بالا**: امتیازدهی دقیق ارتباط برای اسناد
- **پشتیبانی چندزبانه**: بیش از 100 زبان شامل چینی، انگلیسی، اسپانیایی، فرانسوی، پرتغالی، اندونزیایی، ژاپنی، کره‌ای، آلمانی و روسی
- **پشتیبانی از متن طولانی**: تا 4,000 توکن در هر سند
- **بهینه‌سازی شده برای RAG**: طراحی شده برای خطوط لوله تولید تقویت شده با بازیابی
- **کش کردن پرامپت**: پشتیبانی از ورودی کش شده برای صرفه‌جویی در هزینه

**موارد استفاده:**
- بازیابی معنایی متن
- برنامه‌های RAG
- رتبه‌بندی مجدد نتایج جستجو
- امتیازدهی ارتباط اسناد

**قیمت‌گذاری:**

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $0.10 به ازای 1M توکن |
| توکن‌های ورودی کش‌شده | $0.0035 به ازای 1M توکن |

**مثال:**

```language-selector
bash=:curl https://api.avalai.ir/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-rerank",
    "query": "یادگیری ماشین چیست؟",
    "documents": [
      "یادگیری ماشین یک حوزه مطالعاتی است...",
      "یادگیری عمیق زیرمجموعه‌ای از یادگیری ماشین است...",
      "سیب نوعی میوه است..."
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از نقطه پایانی rerank
import requests

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={
        "Authorization": f"Bearer {client.api_key}",
        "Content-Type": "application/json",
    },
    json={
        "model": "qwen3-rerank",
        "query": "یادگیری ماشین چیست؟",
        "documents": [
            "یادگیری ماشین یک حوزه مطالعاتی است...",
            "یادگیری عمیق زیرمجموعه‌ای از یادگیری ماشین است...",
            "سیب نوعی میوه است...",
        ],
    },
)

print(response.json())

```

**نمونه پاسخ:**

```json
{
  "model": "qwen3-rerank",
  "results": [
    {
      "index": 1,
      "relevance_score": 0.98,
      "document": {
        "text": "یادگیری عمیق زیرمجموعه‌ای از یادگیری ماشین است..."
      }
    },
    {
      "index": 0,
      "relevance_score": 0.95,
      "document": {
        "text": "یادگیری ماشین یک حوزه مطالعاتی است..."
      }
    },
    {
      "index": 2,
      "relevance_score": 0.01,
      "document": {
        "text": "سیب نوعی میوه است..."
      }
    }
  ],
  "usage": {
    "total_tokens": 45
  }
}
```

### منابع مرتبط

- [مرجع API رتبه‌بندی مجدد](fa/api-reference/rerank.md)
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md)
- [راهنمای بازیابی](fa/guides/retrieval.md)

## نقاط پایانی API و یکپارچگی

### پشتیبانی اصلی: API تکمیل چت

همه مدل‌های Alibaba به طور کامل در نقطه پایانی `v1/chat/completions` با سازگاری کامل ویژگی‌ها پشتیبانی می‌شوند شامل:

- فراخوانی تابع و استفاده از ابزار
- پاسخ‌های جریانی
- پیام‌های سیستم
- دما و سایر پارامترهای تولید
- ورودی‌های چندوجهی (برای مدل‌های بینایی)

### پشتیبانی محدود: API پیام‌ها

تولید متن پایه در نقطه پایانی `v1/messages` برای موارد استفاده ساده موجود است، اگرچه پشتیبانی کامل ویژگی‌ها از طریق API تکمیل چت توصیه می‌شود.

## مثال‌های استفاده

### تولید متن پایه

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."}
    ],
    max_tokens=500,
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen-plus` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="محاسبات کوانتومی را به زبان ساده توضیح دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پردازش چندوجهی

```python
# مثال مدل بینایی-زبانی
response = client.chat.completions.create(
    model="qwen2.5-vl-72b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این نمودار و بینش‌های کلیدی آن را توصیف کنید.",
                },
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/chart.png"},
                },
            ],
        }
    ],
    extra_body={"enable_thinking": False},  # الزامی برای درخواست‌های غیر استریمینگ
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen2.5-vl-72b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


### پاسخ جریانی

```python
# مثال جریانی (enable_thinking می‌تواند حذف شود یا False باشد برای استریمینگ استاندارد)
stream = client.chat.completions.create(
    model="qwen3-max",
    messages=[
        {"role": "user", "content": "تحلیل دقیقی از روندهای انرژی تجدیدپذیر بنویسید."}
    ],
    stream=True,
    # اختیاری: extra_body={"enable_thinking": True} فقط اگر به حالت تفکر نیاز دارید
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `qwen3-max` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="تحلیل دقیقی از روندهای انرژی تجدیدپذیر بنویسید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## بهترین روش‌ها

1. **انتخاب مدل**: مدل‌ها را بر اساس نیازهای خاص خود انتخاب کنید:

- از **Flash** (مانند `qwen-flash`، `qwen3.6-flash`) برای کاربردهای پرحجم که نیاز به سرعت دارند استفاده کنید
- از **Plus** (مانند `qwen-plus`، `qwen3.6-plus`) برای عملکرد متعادل در وظایف عمومی استفاده کنید
- از **Qwen3 Max** (`qwen3.8-max` برای جدیدترین پرچم‌دار و `qwen3.7-max`، `qwen3-max` یا `qwen3.6-max-preview` برای نسل‌های قبلی) برای استدلال پیچیده، گردش‌کارهای عاملی و اجرای بلندمدت استفاده کنید
- از **مدل‌های Qwen3 VL** برای وظایف شامل تصویر استفاده کنید
- از **مدل‌های Coder** برای وظایف مرتبط با برنامه‌نویسی استفاده کنید

2. **مدیریت زمینه**: هنگام پردازش اسناد طولانی یا مکالمات، به پنجره‌های زمینه توجه کنید.

3. **بهینه‌سازی API**: از API تکمیل چت برای پشتیبانی کامل ویژگی‌ها و از API پیام‌ها فقط برای تولید متن ساده استفاده کنید.

4. **مدیریت نسخه**: از نسخه‌های تاریخ‌دار مشخص برای کاربردهای تولیدی که نیاز به سازگاری دارند استفاده کنید.

## اطلاعات قیمت‌گذاری

برای اطلاعات دقیق قیمت‌گذاری شامل هزینه‌های ورودی، هزینه‌های خروجی و قیمت‌گذاری خواندن کش برای همه مدل‌های Alibaba، لطفا به مستندات جامع [جزئیات مدل‌ها](fa/models/model-details.md) مراجعه کنید.

## منابع مرتبط

- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [جزئیات مدل‌ها و قیمت‌گذاری](fa/models/model-details.md)
- [راهنمای احراز هویت](fa/api-reference/authentication.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [راهنمای بینایی](fa/guides/vision.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [کنسول رسمی DashScope](https://dashscope.console.aliyun.com/)
