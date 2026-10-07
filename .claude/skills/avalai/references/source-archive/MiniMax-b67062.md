# MiniMax

این صفحه اطلاعاتی درباره مدل‌های MiniMax موجود در AvalAI ارائه می‌دهد.

MiniMax یک شرکت هوش مصنوعی متمرکز بر توسعه مدل‌های پایه پیشرو برای متن، گفتار، ویدیو و موسیقی است. مدل پرچم‌دار M3 آن‌ها کدنویسی پیشرو، پنجره زمینه ۱ میلیون توکنی و چندوجهی بودن بومی را در یک مدل واحد گرد هم می‌آورد، در حالی که سری M2.5 عملکرد SOTA در کدنویسی (۸۰.۲٪ SWE-Bench Verified)، استفاده عاملی از ابزار و وظایف بهره‌وری دنیای واقعی را با کارایی هزینه‌ای بی‌سابقه ارائه می‌دهد. [مستندات رسمی](https://platform.minimax.io/docs/guides/quickstart)

## مدل‌های موجود

### مدل‌های متن و چت

MiniMax مدل‌های زبانی قدرتمندی برای تولید متن و برنامه‌های عاملی ارائه می‌دهد.

#### minimax-m3

مدل `minimax-m3` مدل پرچم‌دار جدید MiniMax است که قابلیت کدنویسی پیشرو، پنجره زمینه فوق‌طولانی ۱ میلیون توکنی و چندوجهی بودن بومی را در یک مدل واحد ترکیب می‌کند. M3 که بر پایه معماری اختصاصی توجه پراکنده MiniMax (MSA) ساخته شده است، از تجزیه خودکار وظایف، فراخوانی ابزار و استدلال چندمرحله‌ای پشتیبانی می‌کند.

**ویژگی‌های کلیدی:**

- قابلیت‌های کدنویسی و عاملی پیشرو: SWE-Bench Pro ۵۹.۰٪، Terminal-Bench 2.1 ۶۶.۰٪، MCP Atlas ۷۴.۲٪، BrowseComp ۸۳.۵
- پنجره زمینه ۱ میلیون توکنی: مبتنی بر توجه پراکنده MiniMax (MSA) برای وظایف عاملی طولانی‌مدت، کدنویسی طولانی و درک ویدیوهای بلند، با حداقل تضمین‌شده ۵۱۲K توکن
- چندوجهی بومی: آموزش‌دیده با داده‌های چندوجهی از گام صفر، با پشتیبانی از ورودی تصویر و ویدیو
- تفکر قابل تغییر: روشن کردن استدلال برای وظایف عاملی پیچیده و طولانی‌مدت، یا خاموش کردن آن برای سناریوهای سریع‌تر و حساس به تأخیر — هر دو حالت قیمت یکسانی دارند
- وظایف خودکار طولانی‌مدت: قابلیت اجرای خودکار چندساعته با فراخوانی ابزار و خود-اعتبارسنجی
- قیمت‌گذاری مبتنی بر زمینه: نرخ استاندارد برای محدوده رایج ورودی ≤۵۱۲K، با نرخ بالاتر زمینه طولانی فقط بالای ۵۱۲K توکن

**قیمت‌گذاری:**

| سطح | ورودی | ورودی کش شده | خروجی |
|-----|-------|--------------|-------|
| ≤۵۱۲K توکن | $0.60/۱م توکن | $0.12/۱م توکن | $2.40/۱م توکن |
| بالای ۵۱۲K توکن | $1.20/۱م توکن | $0.24/۱م توکن | $4.80/۱م توکن |

**موارد استفاده:**

- کدنویسی عاملی پیشرو و مهندسی نرم‌افزار
- وظایف زمینه طولانی: درک کد کل مخزن، تجزیه اسناد فوق‌طولانی
- درک چندوجهی با ورودی تصویر و ویدیو
- گردش‌های کاری عامل خودکار طولانی‌مدت
- استدلال چندمرحله‌ای و اتوماسیون مبتنی بر ابزار

**پشتیبانی اندپوینت:**

- `v1/chat/completions`: پشتیبانی کامل از طریق API سازگار با OpenAI
- `v1/messages`: پشتیبانی کامل از طریق فرمت API پیام‌های Anthropic
- `v1/responses`: پشتیبانی جزئی (ورودی/خروجی متنی و استفاده پایه از ابزار)

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m3",
    messages=[
        {
            "role": "user",
            "content": "این تابع پایتون را برای عملکرد بهتر بازآرایی کن و استدلال خود را توضیح بده.",
        }
    ],
    max_tokens=8192,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m3` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این تابع پایتون را برای عملکرد بهتر بازآرایی کن و استدلال خود را توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2.1

مدل `minimax-m2.1` مدل استدلال پرچم‌دار MiniMax با عملکرد در سطح o3 است. این مدل در قابلیت‌های برنامه‌نویسی چند زبانه و گردش‌های کاری عاملی برتری دارد.

**ویژگی‌های کلیدی:**

- قابلیت‌های استثنایی برنامه‌نویسی چند زبانه: عملکرد بهبود یافته سیستماتیک در Rust، Java، Golang، C++، Kotlin، Objective-C، TypeScript، JavaScript و بیشتر
- استدلال سطح o3: ترکیب استدلال عمیق با کارایی تا ۲۰ برابر بهتر
- داربست عامل/ابزار برجسته: عملکرد عالی در Claude Code، Cline، Kilo Code، Roo Code و BlackBox
- تفکر درهم‌تنیده (Interleaved Thinking): پشتیبانی بومی از استدلال بین تعاملات ابزار با بلوک‌های `thinking`
- پاسخ‌های مختصر و کارآمد: سرعت پاسخ بهبود یافته و کاهش مصرف توکن
- پنجره متن ۲۰۴K: پشتیبانی از مکالمات گسترده و پردازش اسناد
- حداکثر ۱۲۸K توکن خروجی: قابلیت تولید گسترده برای وظایف پیچیده
- سرعت خروجی: تقریبا ۶۰ توکن در ثانیه

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.03/۱م توکن | $0.375/۱م توکن | $1.20/۱م توکن |

**موارد استفاده:**

- وظایف کدنویسی پیچیده و مهندسی نرم‌افزار
- اتوماسیون عاملی و گردش‌های کاری استفاده از ابزار
- پروژه‌های برنامه‌نویسی چند زبانه
- بررسی و بازآرایی کد
- تولید مستندات فنی
- وظایف تحقیق و تحلیل

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.1",
    messages=[
        {
            "role": "user",
            "content": "یک خزنده وب همزمان در Rust با محدودیت نرخ پیاده‌سازی کن.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک خزنده وب همزمان در Rust با محدودیت نرخ پیاده‌سازی کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2.1-lightning

مدل `minimax-m2.1-lightning` نسخه سریع‌تر M2.1 است که برای سرعت بهینه‌سازی شده در حالی که قابلیت‌های استدلال قوی را حفظ می‌کند.

**ویژگی‌های کلیدی:**

- سرعت خروجی: تقریبا ۱۰۰ توکن در ثانیه (۶۰٪ سریع‌تر از M2.1)
- همان پنجره متن ۲۰۴K مانند M2.1
- بهینه‌سازی شده برای برنامه‌های حساس به تاخیر
- پشتیبانی کامل از فراخوانی ابزار و تابع
- حفظ کیفیت استدلال با توان عملیاتی بهبود یافته

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.03/۱م توکن | $0.375/۱م توکن | $2.40/۱م توکن |

**موارد استفاده:**

- کمک کد بلادرنگ و یکپارچه‌سازی IDE
- برنامه‌های چت تعاملی که نیاز به پاسخ‌های سریع دارند
- جلسات کدنویسی زنده و برنامه‌نویسی جفتی
- گردش‌های کاری عاملی حساس به زمان
- پردازش دسته‌ای با توان عملیاتی بالا

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.1-lightning",
    messages=[
        {
            "role": "user",
            "content": "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.1-lightning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2.5

مدل `minimax-m2.5` یکی از مدل‌های پرچم‌دار نسل قبل MiniMax است که برای بهره‌وری دنیای واقعی با عملکرد SOTA در کدنویسی، استفاده عاملی از ابزار و وظایف کار اداری طراحی شده است.

**ویژگی‌های کلیدی:**

- عملکرد SOTA در کدنویسی: ۸۰.۲٪ در SWE-Bench Verified، ۵۱.۳٪ در Multi-SWE-Bench
- جستجو و فراخوانی ابزار پیشرفته: ۷۶.۳٪ در BrowseComp با مدیریت زمینه
- ۳۷٪ سریع‌تر از M2.1: بهبود تجزیه وظیفه و کارایی توکن
- معماری Spec-Writing: مدل به طور فعال ویژگی‌ها، ساختار و طراحی UI را قبل از کدنویسی برنامه‌ریزی می‌کند
- ۱۰+ زبان برنامه‌نویسی: Go، C، C++، TypeScript، Rust، Kotlin، Python، Java، JavaScript، PHP، Lua، Dart، Ruby
- چرخه توسعه کامل: از طراحی سیستم 0-to-1 تا بررسی و آزمایش کد 90-to-100
- یکپارچه‌سازی کار اداری: همکاری عمیق با متخصصان مالی، حقوقی و علوم اجتماعی
- پنجره زمینه ۲۰۴K: پشتیبانی از مکالمات گسترده و پردازش اسناد
- سرعت خروجی: تقریبا ۵۰ توکن در ثانیه
- **استدلال داخلی**: محتوای تفکر در تگ‌های `<think>` قابل جداسازی با پارامتر `reasoning_split`

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.03/۱م توکن | $0.375/۱م توکن | $1.20/۱م توکن |

**موارد استفاده:**

- کدنویسی عاملی و مهندسی نرم‌افزار
- پروژه‌های برنامه‌نویسی چند زبانه
- وظایف جستجو و تحقیق پیچیده
- اتوماسیون کار اداری (Word، PowerPoint، Excel)
- مدل‌سازی و تحلیل مالی
- بررسی و بازآرایی کد

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.5",
    messages=[
        {
            "role": "user",
            "content": "یک خزنده وب همزمان با محدودیت نرخ در Rust با مدیریت خطای مناسب پیاده‌سازی کن.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک خزنده وب همزمان با محدودیت نرخ در Rust با مدیریت خطای مناسب پیاده‌سازی کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**محتوای استدلال:**

MiniMax M2.5 شامل قابلیت‌های استدلالی داخلی است. به طور پیش‌فرض، فرآیند تفکر مدل در تگ‌های `<think>` و `</think>` در محتوای پاسخ ظاهر می‌شود. شما می‌توانید از پارامتر `reasoning_split` برای جداسازی این محتوا در فیلد اختصاصی استفاده کنید.

```python
# استفاده از reasoning_split برای جداسازی محتوای تفکر
response = client.chat.completions.create(
    model="minimax-m2.5",
    messages=[{"role": "user", "content": "25 ضرب در 37 چند است؟"}],
    extra_body={"reasoning_split": True},
)

# دسترسی به محتوای استدلال جداشده
message = response.choices[0].message
print(f"استدلال: {message.reasoning_details}")  # فرآیند تفکر
print(f"پاسخ: {message.content}")  # فقط پاسخ نهایی
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="25 ضرب در 37 چند است؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


هنگام مدیریت تاریخچه مکالمه با فراخوانی ابزار، شیء پیام پاسخ کامل (شامل فیلد `tool_calls`) را برای حفظ زمینه اضافه کنید. برای جزئیات بیشتر درباره پارامتر `reasoning_split`، به [پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md#مدلهای-minimax-استدلال-m25) مراجعه کنید.

#### minimax-m2.5-lightning

مدل `minimax-m2.5-lightning` نسخه فوق‌سریع M2.5 است که برای سرعت بهینه‌سازی شده در حالی که قابلیت‌های یکسان را حفظ می‌کند.

**ویژگی‌های کلیدی:**

- سرعت خروجی: تقریبا ۱۰۰ توکن در ثانیه (۲ برابر سریع‌تر از سایر مدل‌های پیشرو)
- همان قابلیت‌های M2.5: هوش یکسان با توان عملیاتی بالاتر
- هم‌تراز با Claude Opus 4.6: مطابقت سرعت تکمیل با مدل‌های پیشرو
- عملیات کم‌هزینه: ۰.۳۰ دلار در ساعت با ۱۰۰ TPS عملیات مداوم
- پنجره زمینه ۲۰۴K
- پشتیبانی کامل از کش

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.03/۱م توکن | $0.375/۱م توکن | $2.40/۱م توکن |

**موارد استفاده:**

- کمک کد بلادرنگ و یکپارچه‌سازی IDE
- برنامه‌های چت تعاملی که نیاز به پاسخ‌های سریع دارند
- جلسات کدنویسی زنده و برنامه‌نویسی جفتی
- گردش‌های کاری عاملی حساس به زمان
- پردازش دسته‌ای با توان عملیاتی بالا

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.5-lightning",
    messages=[
        {
            "role": "user",
            "content": "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.5-lightning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2.7

مدل `minimax-m2.7` یکی از مدل‌های پرچم‌دار قبلی MiniMax است که دارای قابلیت‌های انقلابی خود-تکامل است و به اولین مدلی تبدیل شده که عمیقا در تکامل خود شرکت می‌کند. این مدل عملکرد پیشرو در کدنویسی، وظایف عاملی و اجرای مهارت‌های پیچیده را ارائه می‌دهد.

**ویژگی‌های کلیدی:**

- معماری خود-تکامل: اولین مدلی که عمیقا در تکامل خود شرکت می‌کند، خود را بازطراحی و بهبود می‌بخشد
- عملکرد SOTA در کدنویسی: ۵۶.۲۲٪ در بنچمارک SWE-Pro، پیشرو در بین تمام مدل‌های تجاری
- استدلال پیشرفته: مطابقت با مدل‌های پیشرو بدون زمان تفکر طولانی
- پشتیبانی از تیم‌های عامل: همکاری چند-عامل برای گردش‌های کاری عاملی پیچیده
- ۹۷٪ پیروی از مهارت: حفظ سازگاری در ۴۰+ تعریف مهارت پیچیده
- امتیاز VIBE-Pro: ۵۵.۶٪ برای کیفیت تولید مبتنی بر vibe
- Terminal Bench 2: امتیاز ۵۷.۰٪ در وظایف مبتنی بر ترمینال
- سرعت خروجی: تقریبا ۶۰ توکن در ثانیه
- **استدلال داخلی**: محتوای تفکر در تگ‌های `<think>` قابل جداسازی با پارامتر `reasoning_split`

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.06/۱م توکن | $0.375/۱م توکن | $1.20/۱م توکن |

**موارد استفاده:**

- کدنویسی عاملی پیچیده و توسعه نرم‌افزار
- گردش‌های کاری همکاری تیم چند-عامل
- توسعه سیستم‌های هوش مصنوعی خود-بهبود
- برنامه‌های پیشرفته پیروی از مهارت
- استقرارهای تولیدی با قابلیت اطمینان بالا
- اتوماسیون تحقیق و توسعه

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.7",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس برای ویرایشگر سند مشارکتی بلادرنگ با حل تعارض طراحی کن.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.7` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک معماری میکروسرویس برای ویرایشگر سند مشارکتی بلادرنگ با حل تعارض طراحی کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**محتوای استدلال:**

MiniMax M2.7 شامل قابلیت‌های استدلالی داخلی است. به طور پیش‌فرض، فرآیند تفکر مدل در تگ‌های `<think>` و `</think>` در محتوای پاسخ ظاهر می‌شود. شما می‌توانید از پارامتر `reasoning_split` برای جداسازی این محتوا در فیلد اختصاصی استفاده کنید.

```python
# استفاده از reasoning_split برای جداسازی محتوای تفکر
response = client.chat.completions.create(
    model="minimax-m2.7",
    messages=[
        {
            "role": "user",
            "content": "مصالحه‌های بین معماری‌های یکپارچه و میکروسرویس چیست؟",
        }
    ],
    extra_body={"reasoning_split": True},
)

# دسترسی به محتوای استدلال جداشده
message = response.choices[0].message
print(f"استدلال: {message.reasoning_details}")  # فرآیند تفکر
print(f"پاسخ: {message.content}")  # فقط پاسخ نهایی
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.7` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مصالحه‌های بین معماری‌های یکپارچه و میکروسرویس چیست؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2.7-highspeed

مدل `minimax-m2.7-highspeed` نسخه فوق‌سریع M2.7 است که برای حداکثر سرعت بهینه‌سازی شده در حالی که قابلیت‌های خود-تکامل یکسان را حفظ می‌کند.

**ویژگی‌های کلیدی:**

- سرعت خروجی: تقریبا ۱۰۰ توکن در ثانیه (سریع‌ترین در کلاس خود)
- همان قابلیت‌های M2.7: هوش خود-تکامل یکسان با توان عملیاتی بالاتر
- پشتیبانی از تیم‌های عامل: قابلیت‌های کامل همکاری چند-عامل با سرعت بالا
- ۹۷٪ پیروی از مهارت: حفظ سازگاری در ۴۰+ مهارت پیچیده
- عملیات کم‌تأخیر: ایده‌آل برای برنامه‌های تعاملی بلادرنگ
- پشتیبانی کامل از کش با قیمت‌گذاری بهینه

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.60/۱م توکن | $0.06/۱م توکن | $0.375/۱م توکن | $2.40/۱م توکن |

**موارد استفاده:**

- گردش‌های کاری عاملی بلادرنگ که نیاز به پاسخ فوری دارند
- دستیاران کدنویسی تعاملی و یکپارچه‌سازی IDE
- هماهنگی زنده تیم چند-عامل
- پردازش دسته‌ای با توان عملیاتی بالا
- برنامه‌های تولیدی حساس به زمان
- برنامه‌های چت جریانی

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.7-highspeed",
    messages=[
        {
            "role": "user",
            "content": "قضیه CAP و پیامدهای آن برای طراحی پایگاه داده توزیع‌شده را توضیح بده.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.7-highspeed` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="قضیه CAP و پیامدهای آن برای طراحی پایگاه داده توزیع‌شده را توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### minimax-m2

مدل `minimax-m2` مدل نسل قبلی با قابلیت‌های عاملی قوی است که گزینه‌ای مقرون به صرفه برای وظایف عمومی ارائه می‌دهد.

**ویژگی‌های کلیدی:**

- پنجره متن ۲۰۴K
- قابلیت‌های استدلال پیشرفته
- پشتیبانی از فراخوانی ابزار
- گزینه مقرون به صرفه برای برنامه‌های تولیدی
- عملکرد قوی در وظایف کدنویسی و استدلال

**قیمت‌گذاری:**

| ورودی | ورودی کش شده | ایجاد کش | خروجی |
|-------|--------------|----------|-------|
| $0.30/۱م توکن | $0.03/۱م توکن | $0.375/۱م توکن | $1.20/۱م توکن |

**موارد استفاده:**

- تولید و درک متن عمومی
- کمک کدنویسی و تولید کد
- ایجاد محتوا و خلاصه‌سازی
- پاسخ به سؤالات و تحلیل
- گردش‌های کاری عاملی با استفاده از ابزار

## روش‌های دسترسی SDK

مدل‌های MiniMax از طریق دو روش SDK قابل دسترسی هستند:

| SDK | آدرس پایه | اندپوینت | بهترین برای |
|-----|----------|----------|------------|
| OpenAI SDK | `https://api.avalai.ir/v1` | `/v1/chat/completions` | تکمیل چت استاندارد |
| Anthropic SDK | `https://api.avalai.ir` (بدون /v1) | `/v1/messages` | بلوک‌های thinking بومی، استفاده از ابزار |

## مثال‌های استفاده

### OpenAI SDK - استفاده پایه

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="minimax-m2.1",
    messages=[
        {
            "role": "user",
            "content": "یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### OpenAI SDK - فراخوانی تابع

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر، مثلا تهران",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "واحد دما",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="minimax-m2.1",
    messages=[{"role": "user", "content": "آب و هوای تهران چگونه است؟"}],
    tools=tools,
    tool_choice="auto",
)

print(response.choices[0].message)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="آب و هوای تهران چگونه است؟",
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


### Anthropic SDK - استفاده پایه

```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # توجه: بدون /v1
)

message = client.messages.create(
    model="minimax-m2.1",
    max_tokens=4096,
    messages=[
        {"role": "user", "content": "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن"}
    ],
)

print(message.content)
```

### Anthropic SDK - استفاده از ابزار با تفکر درهم‌تنیده

MiniMax M2.1 به صورت بومی از **تفکر درهم‌تنیده (Interleaved Thinking)** پشتیبانی می‌کند که به مدل اجازه می‌دهد بین هر دور تعامل با ابزار استدلال کند. قبل از هر استفاده از ابزار، مدل روی محیط فعلی و خروجی‌های ابزار تامل می‌کند تا اقدام بعدی را تصمیم بگیرد.

```python
import anthropic
import json

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # توجه: بدون /v1
)

# تعریف ابزار: استعلام آب و هوا
tools = [
    {
        "name": "get_weather",
        "description": "دریافت آب و هوای یک مکان، کاربر باید ابتدا مکان را مشخص کند.",
        "input_schema": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "شهر و کشور، مثلا تهران، ایران",
                }
            },
            "required": ["location"],
        },
    }
]


def send_messages(messages):
    response = client.messages.create(
        model="minimax-m2.1",
        max_tokens=4096,
        messages=messages,
        tools=tools,
    )
    return response


def process_response(response):
    thinking_blocks = []
    text_blocks = []
    tool_use_blocks = []

    for block in response.content:
        if block.type == "thinking":
            thinking_blocks.append(block)
            print(f"💭 تفکر>\n{block.thinking}\n")
        elif block.type == "text":
            text_blocks.append(block)
            print(f"💬 مدل>\t{block.text}")
        elif block.type == "tool_use":
            tool_use_blocks.append(block)
            print(
                f"🔧 ابزار>\t{block.name}({json.dumps(block.input, ensure_ascii=False)})"
            )

    return thinking_blocks, text_blocks, tool_use_blocks


# پرسش کاربر
messages = [{"role": "user", "content": "آب و هوای تهران چگونه است؟"}]
print(f"\n👤 کاربر>\t {messages[0]['content']}")

# مدل پاسخ اول را برمی‌گرداند (ممکن است شامل فراخوانی ابزار باشد)
response = send_messages(messages)
thinking_blocks, text_blocks, tool_use_blocks = process_response(response)

# اگر فراخوانی ابزار وجود دارد، ابزار را اجرا کن و مکالمه را ادامه بده
if tool_use_blocks:
    # ⚠️ مهم: پاسخ کامل دستیار را به تاریخچه پیام اضافه کن
    messages.append({"role": "assistant", "content": response.content})

    # اجرای ابزار و بازگرداندن نتیجه (شبیه‌سازی فراخوانی API آب و هوا)
    print(f"\n🔨 در حال اجرای ابزار: {tool_use_blocks[0].name}")
    tool_result = "24℃، آفتابی"
    print(f"📊 نتیجه ابزار: {tool_result}")

    # اضافه کردن نتیجه اجرای ابزار
    messages.append(
        {
            "role": "user",
            "content": [
                {
                    "type": "tool_result",
                    "tool_use_id": tool_use_blocks[0].id,
                    "content": tool_result,
                }
            ],
        }
    )

    # دریافت پاسخ نهایی
    final_response = send_messages(messages)
    process_response(final_response)
```

## تفکر درهم‌تنیده

قابلیت **تفکر درهم‌تنیده (Interleaved Thinking)** در MiniMax M2.1 به مدل اجازه می‌دهد بین تعاملات ابزار استدلال کند، که آن را برای گردش‌های کاری عاملی بسیار قدرتمند می‌سازد.

### نحوه کار

1. **قبل از استفاده از ابزار**: مدل روی محیط فعلی تامل می‌کند و تصمیم می‌گیرد کدام ابزار را فراخوانی کند
2. **بعد از نتیجه ابزار**: مدل خروجی ابزار را تحلیل می‌کند و اقدام بعدی را برنامه‌ریزی می‌کند
3. **زنجیره تفکر**: زنجیره استدلال کامل در طول چندین تعامل ابزار حفظ می‌شود

### بهترین شیوه‌ها

- **حفظ پاسخ کامل**: همیشه `response.content` کامل (شامل بلوک‌های thinking) را به تاریخچه پیام اضافه کنید
- **محتوا را تغییر ندهید**: بلوک‌های thinking را دست‌نخورده نگه دارید - آن‌ها تداوم استدلال را حفظ می‌کنند
- **از Anthropic SDK استفاده کنید**: برای پشتیبانی بومی از بلوک thinking، از Anthropic SDK با `base_url="https://api.avalai.ir"` استفاده کنید

### فرمت پاسخ

هنگام استفاده از Anthropic SDK، پاسخ‌ها شامل سه نوع بلوک هستند:

| نوع بلوک | توضیحات |
|----------|---------|
| `thinking` | فرآیند استدلال داخلی مدل |
| `text` | محتوای متنی خروجی مدل |
| `tool_use` | اطلاعات فراخوانی ابزار با نام تابع و آرگومان‌ها |

## مثال‌های JavaScript/TypeScript

### OpenAI SDK

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "minimax-m2.1",
  messages: [
    {
      role: "user",
      content: "یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
    },
  ],
});

console.log(response.choices[0].message.content);
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `minimax-m2.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک سیستم احراز هویت JWT در Node.js با توکن‌های تازه‌سازی پیاده‌سازی کن",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Anthropic SDK

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",  // توجه: بدون /v1
});

const message = await client.messages.create({
  model: "minimax-m2.1",
  max_tokens: 4096,
  messages: [
    { role: "user", content: "یک سیستم احراز هویت JWT در Node.js پیاده‌سازی کن" }
  ],
});

console.log(message.content);
```

## مقایسه مدل‌ها

| ویژگی | minimax-m2.1 | minimax-m2.1-lightning | minimax-m2 |
|-------|--------------|------------------------|------------|
| پنجره متن | تا ۱,۰۰۰,۰۰۰ توکن | ۲۰۴,۸۰۰ توکن | ۱,۰۰۰,۰۰۰ توکن | ۲۰۴,۸۰۰ توکن |
| ورودی چندوجهی | متن، تصویر، ویدیو | متن | متن | متن |
| فراخوانی ابزار | ✓ | ✓ | ✓ | ✓ |
| قیمت ورودی | $0.60/۱م (≤۵۱۲K) | $0.30/۱م | $0.30/۱م | $0.30/۱م |
| قیمت خروجی | $2.40/۱م (≤۵۱۲K) | $1.20/۱م | $1.20/۱م | $1.20/۱م |
| بهترین برای | کدنویسی پیشرو، زمینه ۱م، چندوجهی | خود-تکامل، تیم‌های عامل | SOTA کدنویسی، بهره‌وری | استدلال پیچیده |

## منابع مرتبط

- [اعلان پشتیبانی از ارائه‌دهنده MiniMax](fa/news/2025-12-28-minimax-provider-support-added.md)
- [مستندات رسمی MiniMax](https://platform.minimax.io/docs/guides/quickstart)
- [کتابخانه‌ها و SDK‌ها](fa/libraries.md)
- [قیمت‌گذاری](fa/pricing.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
