---
hasH1: true
---

# مدل‌های DeepSeek

AvalAI دسترسی به مدل‌های DeepSeek را از طریق API یکپارچه فراهم می‌کند. برای یکپارچه‌سازی‌های جدید، از `deepseek-v4.1-flash` برای درک بومی تصویر، استدلال، کدنویسی و گردش‌کارهای ابزارمحور استفاده کنید.

## مدل‌های موجود

### deepseek-v4.1-flash

DeepSeek V4.1 Flash یک مدل ترکیب متخصصان با ۵۵۲ میلیارد پارامتر کل و معماری رمزگذار–رمزگشای علّی (causal encoder–decoder) است. برای پردازش ورودی ۸ میلیارد و برای تولید خروجی ۱۶ میلیارد پارامتر فعال دارد. این مدل از بینایی بومی، حالت‌های تفکری و غیرتفکری، فراخوانی ابزار و حافظه نهان پرامپت پشتیبانی می‌کند.

| ویژگی | جزئیات |
| --- | --- |
| شناسه مدل در AvalAI | `deepseek-v4.1-flash` |
| حداکثر توکن ورودی در فهرست AvalAI | 1,000,000 |
| حداکثر توکن خروجی در فهرست AvalAI | 393,216 (ارائه‌دهنده این مقدار را 384K می‌نامد) |
| پارامترهای کل / فعال | 552B کل؛ 8B فعال برای ورودی / 16B فعال برای خروجی |
| قابلیت‌ها | بینایی بومی، حالت تفکری / غیرتفکری، فراخوانی ابزار، خروجی JSON، حافظه نهان پرامپت |
| در دسترس از طریق | `v1/chat/completions`، `v1/messages`، `v1/responses` (پشتیبانی جزئی) |
| قیمت ورودی | $0.15 / 1M توکن |
| قیمت ورودی ذخیره‌شده | $0.003 / 1M توکن |
| قیمت خروجی | $0.60 / 1M توکن |

قیمت‌ها به دلار آمریکا هستند. **AvalAI همیشه همین تعرفه ثابت کم‌بار را اعمال می‌کند**: نیازی به زمان‌بندی درخواست‌ها نیست، قیمت در ساعات اوج دو برابر نمی‌شود و نباید مبالغ جدول را دوباره نصف کنید.

با Chat Completions شروع کنید:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4.1-flash",
    "messages": [
      {"role": "user", "content": "Review a database migration plan: identify failure modes and give a concise verification checklist."}
    ]
  }'
```

پشتیبانی Responses **جزئی** است و برابری کامل ابزارهای داخلی یا گردش‌کارهای دارای وضعیت ذخیره‌شده را تضمین نمی‌کند. پیش از تغییر نقطه پایانی، گردش‌کار دقیق خود، از جمله رفت‌وبرگشت ابزارها، قالب خروجی و ادامه مکالمه را بررسی کنید. مقدارهای مجاز تلاش استدلالی را از مدل‌های قدیمی به این مدل تعمیم ندهید.

### تغییر مسیر پیش‌روی V4-Pro

**از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC، درخواست‌های `deepseek-v4-pro` در AvalAI به `deepseek-v4.1-flash` هدایت خواهند شد و با تعرفه V4.1 Flash محاسبه می‌شوند.** در تاریخ ۱۴۰۵-۰۶-۲۰ / (2026-09-11) این تغییر هنوز انجام نشده است. از هم‌اکنون `deepseek-v4.1-flash` را انتخاب کنید و پیش از تغییر مسیر، پرامپت‌ها، ورودی‌های تصویری، چرخه‌های ابزار، بودجه خروجی، تأخیر و هزینه را آزمایش کنید.

DeepSeek مدل‌های قدیمی V4-Flash و V4-Flash-Vision-Exp را در سرویس مستقیم خود بازنشسته کرده است. این اعلامیه به‌تنهایی به معنی تغییر مسیرهای دیگری برای این شناسه‌ها در AvalAI نیست. [اعلامیه انتشار ۱۴۰۵-۰۶-۲۰ / (2026-09-11)](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md) را ببینید.

### نسخه‌های پیشین DeepSeek V4

اطلاعات V4-Flash در ادامه، مربوط به نسخه پیشین 0731 است؛ نه مشخصات V4.1 Flash یا اعلام تغییر مسیر جدید در AvalAI. مشخصات و قیمت‌های V4-Pro در ادامه به دوره پیش از تغییر مسیر در ۱۴۰۵-۰۶-۲۳ / (2026-09-14) مربوط‌اند.

### deepseek-v4-flash

**سابقه نسخه 0731:** مدل DeepSeek-V4-Flash-0731 با ۲۸۴ میلیارد پارامتر کل، ۱۳ میلیارد پارامتر فعال و ماژول رمزگشایی حدسی DSpark برای کدنویسی، کار با ترمینال، ابزارها و خودکارسازی عرضه شد. برای یکپارچه‌سازی‌های جدید، بخش V4.1 Flash در بالا را ببینید.

| ویژگی                | جزئیات                                                                                                                                             |
| -------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- |
| پنجره زمینه          | ۱ میلیون توکن                                                                                                                                      |
| حداکثر خروجی         | DeepSeek برای بارهای کاری محلی با reasoning سطح `high` و `max` تا ۳۸۴K را توصیه می‌کند؛ محدودیت فعلی route در AvalAI را از `/v1/models` بررسی کنید |
| پارامترها            | ۲۸۴ میلیارد کل / ۱۳ میلیارد فعال                                                                                                                   |
| نسخه backend         | DeepSeek-V4-Flash-0731 (خودکار؛ بدون تغییر شناسه مدل)                                                                                              |
| speculative decoding | ماژول DSpark متصل                                                                                                                                  |
| تلاش استدلالی        | `low`، `high` یا `max`                                                                                                                             |
| قیمت ورودی           | $0.22 / ۱ میلیون توکن                                                                                                                              |
| قیمت ورودی کش‌شده    | $0.007 / ۱ میلیون توکن                                                                                                                             |
| قیمت خروجی           | $0.66 / ۱ میلیون توکن                                                                                                                              |
| نقاط قوت             | کدنویسی بلندمدت، کار با ترمینال، استفاده از ابزار، اتوماسیون و اجرای عاملی اقتصادی                                                                 |
| بهترین برای          | برنامه‌های پرترافیک، عامل‌های کدنویسی، گردش‌کارهای ابزارمحور و تحلیل زمینه بزرگ                                                                    |
| ویژگی‌ها             | خروجی ساختاریافته ✓، فراخوانی ابزار ✓، کش پرامپت ✓، استریمینگ بومی ✓                                                                               |
| در دسترس از طریق     | `v1/chat/completions`                                                                                                                              |

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# شناسه پایدار به‌طور خودکار از DeepSeek-V4-Flash-0731 استفاده می‌کند.
response = client.chat.completions.create(
    model="deepseek-v4-flash",
    messages=[
        {
            "role": "user",
            "content": "علت ریشه‌ای این استقرار ناموفق را پیدا کن و امن‌ترین اصلاح را پیشنهاد بده.",
        }
    ],
    reasoning_effort="high",
)

print(response.choices[0].message.content)
```

> **سابقه ارتقا:** [اعلامیه ۱۴۰۵-۰۵-۱۲ / (2026-08-03)](fa/news/2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade.md) ارتقای خودکار به نسخه 0731 را ثبت کرده است و اعلام تغییر مسیر جدید V4.1 برای این شناسه در AvalAI نیست.

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-v4-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مزایای پنجره زمینه ۱ میلیون توکنی برای تحلیل اسناد را خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### deepseek-v4-pro

**فقط برای مراجعه به دوره پیش از تغییر مسیر:** مشخصات، قیمت‌ها و مثال زیر مربوط به DeepSeek-V4-Pro-0813 پیش از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC هستند. از آن زمان، `deepseek-v4-pro` از V4.1 Flash و تعرفه آن استفاده خواهد کرد، نه معماری یا قیمت‌های Pro در جدول زیر. برای یکپارچه‌سازی‌های جدید از `deepseek-v4.1-flash` استفاده کنید.

| ویژگی | جزئیات V4-Pro-0813 پیش از تغییر مسیر |
| --- | --- |
| پنجره زمینه | 1M توکن |
| حداکثر خروجی | 384K توکن (با نگارش ارائه‌دهنده) |
| پارامترها | 1.6T کل / 49B فعال |
| نسخه پردازش‌کننده | DeepSeek-V4-Pro-0813 |
| رمزگشایی حدسی | ماژول DSpark متصل |
| حالت | تفکری / غیرتفکری؛ تفکر به‌صورت پیش‌فرض فعال |
| تلاش استدلالی | `reasoning_effort: "high"` یا `"max"` (low/medium → high، xhigh → max) |
| قیمت ورودی | $0.66 / 1M توکن |
| قیمت ورودی ذخیره‌شده | $0.022 / 1M توکن |
| قیمت خروجی | $1.98 / 1M توکن |
| فیلد استدلال | `reasoning_content` |
| قابلیت‌ها | خروجی JSON، فراخوانی ابزار، تکمیل پیشوند چت (بتا) |
| نقطه پایانی ثبت‌شده | `v1/chat/completions` |

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# حالت تفکری با تلاش استدلالی بالا
response = client.chat.completions.create(
    model="deepseek-v4-pro",
    messages=[
        {
            "role": "user",
            "content": "یک معماری تحمل‌پذیر خطا برای یک پردازنده پرداخت جهانی با ۵۰٬۰۰۰ TPS طراحی کنید.",
        }
    ],
    reasoning_effort="high",
    extra_body={"thinking": {"type": "enabled"}},
)

print(response.choices[0].message.reasoning_content)
print(response.choices[0].message.content)
```

> **سابقه ارتقا:** [اعلامیه ۱۴۰۵-۰۵-۲۳ / (2026-08-14)](fa/news/2026-08-14-deepseek-v4-fixed-off-peak-pricing.md) ارتقا به نسخه 0813 را ثبت کرده است. تغییر مسیر پیش‌رو در ۱۴۰۵-۰۶-۲۳ / (2026-09-14) جایگزین اطلاعات پردازش‌کننده و قیمت‌گذاری آن خواهد شد.

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-v4-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک معماری تحمل‌پذیر خطا برای یک پردازنده پرداخت جهانی با ۵۰٬۰۰۰ TPS طراحی کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### نام‌های سازگار هدایت‌شده به DeepSeek V4

> **سازگاری:** AvalAI نام‌های مستعار موجود را طبق [سیاست سازگاری ۱۴۰۵-۰۵-۲۳ / (2026-08-14)](fa/news/2026-08-14-deepseek-v4-fixed-off-peak-pricing.md) حفظ می‌کند. جزئیات قدیمی زیر، همان سیاست و مشخصات V4 پیش از تغییر مسیر را ثبت می‌کنند و اعلام تغییر نام‌های مستعار دیگری نیستند. برای یکپارچه‌سازی‌های جدید از `deepseek-v4.1-flash` استفاده کنید.

### deepseek-chat

`deepseek-chat` اکنون به **`deepseek-v4-flash`** هدایت می‌شود (به‌صورت پیش‌فرض حالت غیرتفکری) و تعرفه ثابت V4-Flash را دارد.

| ویژگی | جزئیات |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| هدایت به | `deepseek-v4-flash` |
| پنجره زمینه | ۱ میلیون توکن (به ارث رسیده از V4-Flash) |
| حداکثر توکن خروجی | تا ۳۸۴ هزار |
| حالت | غیرتفکری به‌صورت پیش‌فرض |
| قیمت‌گذاری ورودی (cache miss) | $0.22 / ۱ میلیون توکن |
| قیمت‌گذاری ورودی (cache hit) | $0.007 / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | $0.66 / ۱ میلیون توکن |
| نقاط قوت | سریع، اقتصادی، استدلال نزدیک به V4-Pro، زمینه ۱ میلیونی، کارایی DSA |
| بهترین برای | یکپارچه‌سازی‌های موجود که به نام `deepseek-chat` متکی هستند |
| استدلال | استدلال CoT اختیاری از طریق `reasoning_effort` و کلید `thinking` |
| ویژگی‌ها | خروجی JSON ✓، فراخوانی ابزار ✓، تکمیل پیشوند چت (بتا) ✓، تکمیل FIM (بتا، فقط حالت غیرتفکری) ✓ |

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-chat` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### deepseek-reasoner

**سابقه سازگاری پیش از تغییر مسیر:** سیاست ۱۴۰۵-۰۵-۲۳ / (2026-08-14)، نام `deepseek-reasoner` را با تفکر پیش‌فرض فعال به `deepseek-v4-pro` هدایت می‌کند. مشخصات و قیمت‌های V4-Pro در ادامه مربوط به پیش از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC هستند و حفظ پردازش‌کننده یا تعرفه قدیمی Pro پس از تغییر مسیر اعلام‌شده را تضمین نمی‌کنند.

| ویژگی | جزئیات |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| هدایت به | `deepseek-v4-pro` |
| پنجره زمینه | ۱ میلیون توکن (به ارث رسیده از V4-Pro) |
| حداکثر توکن خروجی | تا ۳۸۴ هزار |
| حالت | تفکری به‌صورت پیش‌فرض (فعال) |
| تلاش استدلالی | `reasoning_effort: "high"` یا `"max"` |
| قیمت‌گذاری ورودی (cache miss) | $0.66 / ۱ میلیون توکن |
| قیمت‌گذاری ورودی (cache hit) | $0.022 / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | $1.98 / ۱ میلیون توکن |
| نقاط قوت | SOTA متن‌باز در کدنویسی عاملی، استدلال کلاس جهانی، دانش جهانی غنی |
| بهترین برای | یکپارچه‌سازی‌های موجود که به نام `deepseek-reasoner` متکی هستند |
| استدلال | فرآیند تفکر آشکار از طریق فیلد `reasoning_content` |
| ویژگی‌ها | خروجی JSON ✓، فراخوانی ابزار ✓، تکمیل پیشوند چت (بتا) ✓ |

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {
            "role": "user",
            "content": "این مسئله ریاضی پیچیده را گام به گام حل کنید: اگر قطاری ۱۲۰ مایل را در ۲ ساعت طی کند، سپس سرعت خود را ۲۵٪ افزایش دهد برای ۳ ساعت بعدی، در مجموع چه مسافتی طی کرده است؟",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-reasoner` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این مسئله ریاضی پیچیده را گام به گام حل کنید: اگر قطاری ۱۲۰ مایل را در ۲ ساعت طی کند، سپس سرعت خود را ۲۵٪ افزایش دهد برای ۳ ساعت بعدی، در مجموع چه مسافتی طی کرده است؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### deepseek-v3.2

DeepSeek-V3.2 از طریق Azure AI، هماهنگ کننده کارایی محاسباتی بالا با استدلال برتر و عملکرد عامل. دارای DeepSeek Sparse Attention (DSA) برای سناریوهای کارآمد با متن بلند.

| ویژگی | جزئیات |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| پنجره زمینه | ۱۲۸ هزار توکن |
| حداکثر توکن خروجی | محدودیت‌های خروجی استاندارد |
| ارائه‌دهنده | Azure AI |
| حالت | حالت غیرتفکری برای پاسخ‌های کارآمد |
| قیمت‌گذاری ورودی | $0.28 / ۱ میلیون توکن |
| قیمت‌گذاری ورودی (cache hit) | $0.028 / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | $0.42 / ۱ میلیون توکن |
| نقاط قوت | پاسخ‌های سریع، پردازش کارآمد، استفاده بهبود یافته از ابزار، عملکرد سطح GPT-5 |
| بهترین برای | گفتگوی عمومی، پاسخ‌های سریع، برنامه‌های پرحجم، وظایف عامل |
| استدلال | استدلال استاندارد بدون فرآیند تفکر آشکار |
| قابلیت‌ها | JSON Output ✓، Tool Calls ✓، Chat Prefix Completion (Beta) ✓ |
| در دسترس در | `v1/chat/completions`، `v1/completions`، `v1/responses`، `v1/messages` |

**مزایای میزبانی Azure AI:**
- **محدودیت‌های نرخ بهتر**: توان عملیاتی بالاتر نسبت به API مستقیم DeepSeek
- **تاخیر کمتر**: زمان پاسخ سریع‌تر از طریق زیرساخت جهانی Azure
- **قابلیت اطمینان بهتر**: دسترسی‌پذیری و عملکرد در سطح سازمانی

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-v3.2",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای پیاده‌سازی درخت جستجوی دودویی بنویس",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-v3.2` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع Python برای پیاده‌سازی درخت جستجوی دودویی بنویس",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### deepseek-v3.2-speciale

DeepSeek-V3.2-Speciale از طریق Azure AI، یک نوع با محاسبات بالا که از GPT-5 پیشی گرفته و مهارت استدلال هم‌سطح با Gemini-3.0-Pro را نشان می‌دهد. در المپیاد بین‌المللی ریاضی ۲۰۲۵ (IMO) و المپیاد بین‌المللی انفورماتیک (IOI) به عملکرد مدال طلا دست یافت.

| ویژگی | جزئیات |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| پنجره زمینه | ۱۲۸ هزار توکن |
| حداکثر توکن خروجی | محدودیت‌های خروجی گسترده برای استدلال |
| ارائه‌دهنده | Azure AI |
| حالت | حالت استدلال عمیق (تفکر) |
| قیمت‌گذاری ورودی | $0.28 / ۱ میلیون توکن |
| قیمت‌گذاری ورودی (cache hit) | $0.028 / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | $0.42 / ۱ میلیون توکن |
| نقاط قوت | استدلال سطح متخصص، عملکرد سطح المپیاد، پیشی از GPT-5 |
| بهترین برای | ریاضیات پیچیده، برنامه‌نویسی رقابتی، تحقیق، تحلیل عمیق |
| استدلال | تفکر گسترده با فرآیند استدلال آشکار |
| قابلیت‌ها | JSON Output ✓، Chat Prefix Completion (Beta) ✓ |
| فراخوانی ابزار | ✗ پشتیبانی نمی‌شود (فقط برای وظایف استدلال طراحی شده) |
| در دسترس در | `v1/chat/completions`، `v1/completions`، `v1/responses`، `v1/messages` |

**دستاوردهای کلیدی:**
- 🥇 عملکرد مدال طلا در المپیاد بین‌المللی ریاضی ۲۰۲۵ (IMO)
- 🥇 عملکرد مدال طلا در المپیاد بین‌المللی انفورماتیک (IOI)
- مهارت استدلال هم‌سطح با Gemini-3.0-Pro

**نکته مهم:** DeepSeek-V3.2-Speciale به طور انحصاری برای وظایف استدلال عمیق طراحی شده و از قابلیت فراخوانی ابزار پشتیبانی نمی‌کند.

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-v3.2-speciale",
    messages=[
        {
            "role": "user",
            "content": "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
        }
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-v3.2-speciale` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### deepseek-v3.1

DeepSeek-V3.1 از طریق Azure AI، دسترسی مستقیم به آخرین مدل با استفاده بهبود یافته از ابزار و قابلیت‌های عامل.

| ویژگی | جزئیات |
| ---------------------- | ------------------------------------------------------------------------------------------- |
| پنجره زمینه | ۱۲۸ هزار توکن |
| حداکثر توکن خروجی | محدودیت‌های خروجی استاندارد |
| ارائه‌دهنده | Azure AI |
| حالت | حالت غیرتفکری برای پاسخ‌های کارآمد |
| قیمت‌گذاری ورودی (cache hit) | $0.07 / ۱ میلیون توکن |
| قیمت‌گذاری ورودی (cache miss) | $0.27 / ۱ میلیون توکن |
| قیمت‌گذاری خروجی | $1.10 / ۱ میلیون توکن |
| نقاط قوت | پاسخ‌های سریع، پردازش کارآمد، استفاده بهبود یافته از ابزار، گردش‌کارهای عامل |
| بهترین برای | گفتگوی عمومی، پاسخ‌های سریع، برنامه‌های پرحجم، وظایف عامل |
| استدلال | استدلال استاندارد بدون فرآیند تفکر آشکار |
| در دسترس در | `v1/chat/completions`، `v1/responses`، `v1/messages` |

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-v3.1",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای تجزیه و تحلیل فایل‌های لاگ و استخراج الگوهای خطا ایجاد کنید",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-v3.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع Python برای تجزیه و تحلیل فایل‌های لاگ و استخراج الگوهای خطا ایجاد کنید",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## قابلیت‌های کلیدی

### استنتاج ترکیبی

DeepSeek-V3.2 قابلیت‌های استنتاج ترکیبی منحصر به فردی ارائه می‌دهد که به کاربران امکان انتخاب بین حالت‌های تفکری و غیرتفکری بسته به نیازهایشان را می‌دهد:

- **حالت غیرتفکری** (`deepseek-chat`): استنتاج متعادل در برابر طول - مدل روزانه شما با عملکرد سطح GPT-5
- **حالت تفکری** (`deepseek-reasoner`): قابلیت‌های استدلال حداکثری که رقیب Gemini-3.0-Pro است

### جزئیات API حالت تفکری

هنگام استفاده از حالت تفکری (`deepseek-reasoner`)، API دو فیلد محتوا برمی‌گرداند:

- **`reasoning_content`**: فرآیند استدلال زنجیره‌ای (CoT)
- **`content`**: پاسخ نهایی

**دسترسی به محتوای استدلال:**

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [
      {
        "role": "user",
        "content": "۹.۱۱ و ۹.۸، کدام بزرگتر است؟"
      }
    ]
  }'

# پاسخ شامل:
# - choices[0].message.reasoning_content: استدلال CoT
# - choices[0].message.content: پاسخ نهایی

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "۹.۱۱ و ۹.۸، کدام بزرگتر است؟"}],
)

# دسترسی به فرآیند استدلال
reasoning_content = response.choices[0].message.reasoning_content
# دسترسی به پاسخ نهایی
content = response.choices[0].message.content

print(f"استدلال: {reasoning_content}")
print(f"پاسخ: {content}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: [{ role: "user", content: "۹.۱۱ و ۹.۸، کدام بزرگتر است؟" }]
});

// دسترسی به فرآیند استدلال
const reasoningContent = response.choices[0].message.reasoning_content;
// دسترسی به پاسخ نهایی
const content = response.choices[0].message.content;

console.log(`استدلال: ${reasoningContent}`);
console.log(`پاسخ: ${content}`);

php=:<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => [
        ['role' => 'user', 'content' => '۹.۱۱ و ۹.۸، کدام بزرگتر است؟']
    ]
]);

// دسترسی به فرآیند استدلال
$reasoningContent = $response->choices[0]->message->reasoning_content ?? null;
// دسترسی به پاسخ نهایی
$content = $response->choices[0]->message->content;

echo "استدلال: " . $reasoningContent . "\n";
echo "پاسخ: " . $content . "\n";

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-reasoner` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="۹.۱۱ و ۹.۸، کدام بزرگتر است؟",
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
  input: "۹.۱۱ و ۹.۸، کدام بزرگتر است؟",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "۹.۱۱ و ۹.۸، کدام بزرگتر است؟",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مکالمات چند نوبتی

در مکالمات چند نوبتی با حالت تفکری:

- هر نوبت هم `reasoning_content` و هم `content` را خروجی می‌دهد
- **مهم**: هنگام ادامه مکالمه، فقط `content` از نوبت‌های قبلی را ارسال کنید، نه `reasoning_content`
- `reasoning_content` از نوبت‌های قبلی در زمینه متصل نمی‌شود

```language-selector
bash=:# نوبت ۱
RESPONSE=$(curl -s https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [
      {"role": "user", "content": "۱۵ + ۲۷ چند می‌شود؟"}
    ]
  }')

CONTENT=$(echo $RESPONSE | jq -r '.choices[0].message.content')

# نوبت ۲ - فقط content را ارسال کنید، نه reasoning_content
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d "{
    \"model\": \"deepseek-reasoner\",
    \"messages\": [
      {\"role\": \"user\", \"content\": \"۱۵ + ۲۷ چند می‌شود؟\"},
      {\"role\": \"assistant\", \"content\": \"$CONTENT\"},
      {\"role\": \"user\", \"content\": \"حالا آن را در ۲ ضرب کن.\"}
    ]
  }"

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# نوبت ۱
messages = [{"role": "user", "content": "۱۵ + ۲۷ چند می‌شود؟"}]
response = client.chat.completions.create(model="deepseek-reasoner", messages=messages)

reasoning_content = response.choices[0].message.reasoning_content
content = response.choices[0].message.content

# نوبت ۲ - فقط content را ارسال کنید، نه reasoning_content
messages.append({"role": "assistant", "content": content})
messages.append({"role": "user", "content": "حالا آن را در ۲ ضرب کن."})

response = client.chat.completions.create(model="deepseek-reasoner", messages=messages)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// نوبت ۱
let messages = [{ role: "user", content: "۱۵ + ۲۷ چند می‌شود؟" }];
let response = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: messages
});

const reasoningContent = response.choices[0].message.reasoning_content;
const content = response.choices[0].message.content;

// نوبت ۲ - فقط content را ارسال کنید، نه reasoning_content
messages.push({ role: "assistant", content: content });
messages.push({ role: "user", content: "حالا آن را در ۲ ضرب کن." });

response = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: messages
});

console.log(response.choices[0].message.content);

php=:<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// نوبت ۱
$messages = [['role' => 'user', 'content' => '۱۵ + ۲۷ چند می‌شود؟']];
$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => $messages
]);

$reasoningContent = $response->choices[0]->message->reasoning_content ?? null;
$content = $response->choices[0]->message->content;

// نوبت ۲ - فقط content را ارسال کنید، نه reasoning_content
$messages[] = ['role' => 'assistant', 'content' => $content];
$messages[] = ['role' => 'user', 'content' => 'حالا آن را در ۲ ضرب کن.'];

$response = $client->chat()->create([
    'model' => 'deepseek-reasoner',
    'messages' => $messages
]);

echo $response->choices[0]->message->content . "\n";

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-reasoner` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="حالا آن را در ۲ ضرب کن.",
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
  input: "حالا آن را در ۲ ضرب کن.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "حالا آن را در ۲ ضرب کن.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### تفکر در استفاده از ابزار

DeepSeek-V3.2 اولین مدل DeepSeek است که تفکر را مستقیما در استفاده از ابزار یکپارچه می‌کند:

- **پشتیبانی از حالت دوگانه**: پشتیبانی از استفاده از ابزار در هر دو حالت تفکری و غیرتفکری
- **داده‌های آموزش عامل**: سنتز داده‌های آموزش عامل گسترده شامل ۱۸۰۰+ محیط و ۸۵ هزار+ دستورالعمل پیچیده
- **استدلال بهبود یافته**: قابلیت بهبود یافته برای استدلال در تعاملات پیچیده با ابزار

**⚠️ بحرانی: فراخوانی ابزار با حالت تفکری**

هنگام استفاده از فراخوانی ابزار با حالت تفکری، **باید** `reasoning_content` را در درخواست‌های بعدی در همان نوبت به API برگردانید. عدم انجام این کار منجر به خطای ۴۰۰ می‌شود:

```
Missing reasoning_content field in the assistant message
```

**پیاده‌سازی صحیح فراخوانی ابزار:**

```language-selector
bash=:# توجه: فراخوانی ابزار با حالت تفکری نیاز به مدیریت دقیق reasoning_content دارد
# این یک مثال ساده است - برای پیاده‌سازی کامل به Python/JS مراجعه کنید

curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-reasoner",
    "messages": [
      {"role": "user", "content": "آب و هوای تهران امروز چطور است؟"}
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت آب و هوای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {"type": "string", "description": "نام شهر"}
            },
            "required": ["location"]
          }
        }
      }
    ]
  }'

# مهم: وقتی مدل tool_calls برمی‌گرداند، باید
# reasoning_content را در پیام دستیار هنگام ارسال نتایج ابزار درج کنید

python=:import json
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت آب و هوای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "نام شهر"},
                },
                "required": ["location"],
            },
        },
    },
]

messages = [{"role": "user", "content": "آب و هوای تهران امروز چطور است؟"}]

while True:
    response = client.chat.completions.create(
        model="deepseek-reasoner", messages=messages, tools=tools
    )

    message = response.choices[0].message
    reasoning_content = message.reasoning_content
    content = message.content
    tool_calls = message.tool_calls

    # اگر فراخوانی ابزار نداشتیم، پاسخ نهایی را داریم
    if not tool_calls:
        print(f"پاسخ نهایی: {content}")
        break

    # بحرانی: reasoning_content را هنگام اضافه کردن پیام دستیار درج کنید
    assistant_message = {
        "role": "assistant",
        "content": content or "",
        "tool_calls": [
            {
                "id": tc.id,
                "type": "function",
                "function": {
                    "name": tc.function.name,
                    "arguments": tc.function.arguments,
                },
            }
            for tc in tool_calls
        ],
    }

    # باید reasoning_content را اگر موجود بود درج کنید
    if reasoning_content:
        assistant_message["reasoning_content"] = reasoning_content

    messages.append(assistant_message)

    # پردازش فراخوانی‌های ابزار و اضافه کردن نتایج
    for tc in tool_calls:
        # پیاده‌سازی ابزار شما در اینجا
        tool_result = "آفتابی، ۱۵-۲۲ درجه سانتیگراد"  # نتیجه نمونه
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tc.id,
                "content": tool_result,
            }
        )

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت آب و هوای یک مکان",
            parameters: {
                type: "object",
                properties: {
                    location: { type: "string", description: "نام شهر" }
                },
                required: ["location"]
            }
        }
    }
];

let messages = [{ role: "user", content: "آب و هوای تهران امروز چطور است؟" }];

while (true) {
    const response = await client.chat.completions.create({
        model: "deepseek-reasoner",
        messages: messages,
        tools: tools
    });
    
    const message = response.choices[0].message;
    const reasoningContent = message.reasoning_content;
    const content = message.content;
    const toolCalls = message.tool_calls;
    
    // اگر فراخوانی ابزار نداشتیم، پاسخ نهایی را داریم
    if (!toolCalls) {
        console.log(`پاسخ نهایی: ${content}`);
        break;
    }
    
    // بحرانی: reasoning_content را هنگام اضافه کردن پیام دستیار درج کنید
    const assistantMessage = {
        role: "assistant",
        content: content || "",
        tool_calls: toolCalls.map(tc => ({
            id: tc.id,
            type: "function",
            function: {
                name: tc.function.name,
                arguments: tc.function.arguments
            }
        }))
    };
    
    // باید reasoning_content را اگر موجود بود درج کنید
    if (reasoningContent) {
        assistantMessage.reasoning_content = reasoningContent;
    }
    
    messages.push(assistantMessage);
    
    // پردازش فراخوانی‌های ابزار و اضافه کردن نتایج
    for (const tc of toolCalls) {
        // پیاده‌سازی ابزار شما در اینجا
        const toolResult = "آفتابی، ۱۵-۲۲ درجه سانتیگراد";  // نتیجه نمونه
        messages.push({
            role: "tool",
            tool_call_id: tc.id,
            content: toolResult
        });
    }
}

php=:<?php
require 'vendor/autoload.php';

use OpenAI;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$tools = [
    [
        'type' => 'function',
        'function' => [
            'name' => 'get_weather',
            'description' => 'دریافت آب و هوای یک مکان',
            'parameters' => [
                'type' => 'object',
                'properties' => [
                    'location' => ['type' => 'string', 'description' => 'نام شهر']
                ],
                'required' => ['location']
            ]
        ]
    ]
];

$messages = [['role' => 'user', 'content' => 'آب و هوای تهران امروز چطور است؟']];

while (true) {
    $response = $client->chat()->create([
        'model' => 'deepseek-reasoner',
        'messages' => $messages,
        'tools' => $tools
    ]);
    
    $message = $response->choices[0]->message;
    $reasoningContent = $message->reasoning_content ?? null;
    $content = $message->content;
    $toolCalls = $message->tool_calls ?? null;
    
    // اگر فراخوانی ابزار نداشتیم، پاسخ نهایی را داریم
    if (!$toolCalls) {
        echo "پاسخ نهایی: " . $content . "\n";
        break;
    }
    
    // بحرانی: reasoning_content را هنگام اضافه کردن پیام دستیار درج کنید
    $assistantMessage = [
        'role' => 'assistant',
        'content' => $content ?? '',
        'tool_calls' => array_map(function($tc) {
            return [
                'id' => $tc->id,
                'type' => 'function',
                'function' => [
                    'name' => $tc->function->name,
                    'arguments' => $tc->function->arguments
                ]
            ];
        }, $toolCalls)
    ];
    
    // باید reasoning_content را اگر موجود بود درج کنید
    if ($reasoningContent) {
        $assistantMessage['reasoning_content'] = $reasoningContent;
    }
    
    $messages[] = $assistantMessage;
    
    // پردازش فراخوانی‌های ابزار و اضافه کردن نتایج
    foreach ($toolCalls as $tc) {
        // پیاده‌سازی ابزار شما در اینجا
        $toolResult = "آفتابی، ۱۵-۲۲ درجه سانتیگراد";  // نتیجه نمونه
        $messages[] = [
            'role' => 'tool',
            'tool_call_id' => $tc->id,
            'content' => $toolResult
        ];
    }
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-reasoner` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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
    input="آب و هوای تهران امروز چطور است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const tools = [
  {
    type: "function",
    name: "get_current_weather",
    description: "Get the current weather in a given location.",
    parameters: {
      type: "object",
      properties: { location: { type: "string" } },
      required: ["location"],
      additionalProperties: false,
    },
  },
];

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "آب و هوای تهران امروز چطور است؟",
  tools,
});

for (const item of response.output) {
  if (item.type === "function_call") {
    console.log(item.name, item.arguments);
  }
}
console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "آب و هوای تهران امروز چطور است؟",
    "tools": [
      {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string"
            }
          },
          "required": [
            "location"
          ],
          "additionalProperties": false
        }
      }
    ]
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**نکات مهم برای فراخوانی ابزار:**

1. در یک نوبت واحد (هنگام پردازش فراخوانی‌های ابزار)، همیشه `reasoning_content` را در پیام‌های دستیار درج کنید
2. هنگام شروع نوبت جدید کاربر، می‌توانید `reasoning_content` را از تاریخچه پاک کنید تا پهنای باند ذخیره شود
3. شیء `response.choices[0].message` شامل تمام فیلدهای لازم است - می‌توانید آن را مستقیما به messages اضافه کنید

### مهارت‌های عامل بهبود یافته

DeepSeek-V3.2 دارای بهبودهای قابل توجه در قابلیت‌های عامل است:

- **استفاده از ابزار**: قابلیت بهبود یافته برای استفاده از ابزارها و API های خارجی با یکپارچه‌سازی تفکر
- **وظایف چندمرحله‌ای**: عملکرد بهتر در گردش‌های کاری عامل پیچیده و چندمرحله‌ای
- **فراخوانی تابع**: قابلیت‌های بهبود یافته فراخوانی تابع برای ادغام با سیستم‌های خارجی

### استدلال پیشرفته

حالت تفکری ارائه می‌دهد:

- **تحلیل گام به گام**: تجزیه واضح مسائل پیچیده
- **استدلال شفاف**: فرآیندهای تفکر آشکار برای درک بهتر
- **عملکرد مدال طلا**: DeepSeek-V3.2-Speciale نتایج سطح طلا در IMO، CMO، فینال جهانی ICPC و IOI 2025 کسب کرده است

### بنچمارک‌های عملکرد (بر اساس ادعاهای DeepSeek)

DeepSeek-V3.2 بهبودهای قابل توجهی در معیارهای کلیدی نشان می‌دهد:

- **سطح GPT-5**: حالت غیرتفکری عملکردی در سطح GPT-5 ارائه می‌دهد
- **رقیب Gemini-3.0-Pro**: حالت تفکری رقیب قابلیت‌های Gemini-3.0-Pro است
- **استدلال چندمرحله‌ای**: قابلیت بهبود یافته برای جستجو و تحلیل پیچیده

## راهنمای انتخاب مدل

یکپارچه‌سازی‌های جدید را با `deepseek-v4.1-flash` آغاز کنید. حالت‌های تفکری و غیرتفکری را برای وظیفه خود ارزیابی کنید و بینایی بومی و فراخوانی ابزار را با ورودی‌های واقعی آزمایش کنید. به‌جای محدودیت‌های قدیمی نام‌های مستعار، سقف ۱٬۰۰۰٬۰۰۰ توکن ورودی و ۳۹۳٬۲۱۶ توکن خروجی ثبت‌شده در فهرست را در نظر بگیرید. کاربران V4-Pro باید آزمایش‌های مهاجرت را پیش از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC تکمیل کنند.

## اطلاعات قیمت‌گذاری

همه قیمت‌های زیر به دلار آمریکا برای هر ۱ میلیون توکن هستند. AvalAI تعرفه ثابت کم‌بار را در تمام ساعات ارائه می‌کند؛ درخواست‌ها را برای تخفیف زمان‌بندی نکنید و این قیمت‌ها را دوباره نصف نکنید.

| مدل / دوره | ورودی ذخیره‌شده | ورودی | خروجی |
| --- | ---: | ---: | ---: |
| `deepseek-v4.1-flash` | $0.003 | $0.15 | $0.60 |
| `deepseek-v4-pro` پیش از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC | $0.022 | $0.66 | $1.98 |
| `deepseek-v4-pro` از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC، با هدایت به V4.1 Flash | $0.003 | $0.15 | $0.60 |

تعرفه ورودی ذخیره‌شده برای توکن‌هایی اعمال می‌شود که در حافظه نهان موجودند؛ سایر توکن‌های ورودی با تعرفه ورودی محاسبه می‌شوند. قیمت‌های پیشین V4-Flash در بخش سابقه انتشار بالا ثبت شده‌اند. [اعلامیه انتشار و مهاجرت](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md) را ببینید.

## بهترین شیوه‌ها برای مدل‌های DeepSeek

### پرامپت‌نویسی مؤثر

دستورالعمل‌های واضح و مشخص ارائه دهید. برای وظایف استدلالی، هنگام استفاده از `deepseek-reasoner` صراحتا تحلیل گام به گام درخواست کنید.

### دستورالعمل‌های سیستم

از نقش `system` به طور مؤثر برای راهنمایی رفتار مدل و سبک پاسخ به طور مداوم در هر دو مدل استفاده کنید.

### Temperature و Top_P

`temperature` و `top_p` را برای کنترل تصادفی تنظیم کنید. مقادیر پایین‌تر (مثل temp=0.2) خروجی‌های قطعی‌تری تولید می‌کنند، در حالی که مقادیر بالاتر (مثل temp=0.8) خلاقیت را تشویق می‌کنند.

## استفاده از مدل‌های DeepSeek از طریق AvalAI

همه مدل‌های DeepSeek از طریق نقاط پایانی استاندارد API AvalAI، با استفاده از کتابخانه‌های کلاینت سازگار با OpenAI قابل دسترسی هستند:

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید API واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # نقطه پایانی API AvalAI
)

# از هر مدل DeepSeek با شناسه AvalAI آن استفاده کنید
response = client.chat.completions.create(
    model="deepseek-chat",  # یا "deepseek-reasoner"
    messages=[{"role": "user", "content": "سلام!"}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `deepseek-chat` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


## نکات مهم

### مسیریابی مدل

برای یکپارچه‌سازی‌های جدید از `deepseek-v4.1-flash` استفاده کنید. جدول زیر نگاشت‌های حفظ‌شده در سیاست سازگاری AvalAI در ۱۴۰۵-۰۵-۲۳ / (2026-08-14) را ثبت می‌کند و اعلام تغییر مسیر نام‌های مستعار دیگری نیست. مسیر صریح `deepseek-v4-pro` در ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC به V4.1 Flash تغییر خواهد کرد.

| شناسه مدل | مدل پایه V4 |
| --- | --- |
| `deepseek-chat` | `deepseek-v4-flash` |
| `deepseek-coder` | `deepseek-v4-flash` |
| `deepseek-reasoner` | `deepseek-v4-pro` |
| `deepseek-v3-0324` | `deepseek-v4-pro` |
| `deepseek-r1-0528` | `deepseek-v4-pro` |
| `deepseek-v3.1` | `deepseek-v4-pro` |

طبق سیاست سازگاری، تعرفه ثابت مدل مقصد اعمال می‌شود. جزئیات V4-Pro در این صفحه را اطلاعات دوره پیش از تغییر مسیر بدانید. برای مدل‌های خارج از این جدول، از جمله `deepseek-v3.2` و `deepseek-v3.2-speciale`، تغییر دیگری در اینجا اعلام نشده است.

### پنجره زمینه

مدل‌های پایه DeepSeek V4 (`deepseek-v4-flash` و `deepseek-v4-pro`) پنجره زمینه **۱ میلیون توکنی** دارند. شناسه‌های هدایت‌شده قابلیت‌ها و محدودیت‌های عملیاتی route مقصد خود را به ارث می‌برند؛ مقدار جاری را از `/v1/models` بررسی کنید.

### پشتیبانی از فراخوانی تابع

DeepSeek-V3.1 از فراخوانی تابع از طریق Beta API پشتیبانی می‌کند که ادغام با ابزارها و خدمات خارجی را امکان‌پذیر می‌سازد.

## تفاوت‌ها با خانواده‌های مدل دیگر

در حالی که AvalAI یک API یکپارچه ارائه می‌دهد، مدل‌های DeepSeek ویژگی‌های منحصر به فردی دارند:

1. **استدلال ترکیبی**: تمایز منحصر به فرد حالت تفکری/غیرتفکری، قابل تنظیم از طریق `extra_body={"thinking": {"type": ...}}`
2. **DeepSeek Sparse Attention (DSA)**: فشرده‌سازی توکنی برای مدیریت کارآمد زمینه ۱ میلیون توکنی
3. **تفکر در استفاده از ابزار**: اولین خانواده که تفکر را مستقیما در استفاده از ابزار یکپارچه می‌کند
4. **تمرکز بر عامل**: به طور خاص برای وظایف عامل با ادغام عمیق با Claude Code، OpenClaw و OpenCode بهینه‌سازی شده
5. **شفافیت استدلال**: فرآیندهای تفکر آشکار از طریق فیلد `reasoning_content` در حالت تفکری
6. **عملکرد رقابتی (V4)**: V4-Pro به SOTA متن‌باز در کدنویسی عاملی دست یافته؛ V4-Flash کیفیت نزدیک به V4-Pro را با کسری از هزینه ارائه می‌دهد (بر اساس بنچمارک‌های DeepSeek)

## نسخه‌بندی مدل

- **`deepseek-v4.1-flash`**: شناسه صریح پیشنهادی AvalAI برای یکپارچه‌سازی‌های جدید، با بینایی بومی و حالت‌های تفکری / غیرتفکری.
- **`deepseek-v4-pro`**: پیش از ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC از V4-Pro-0813 استفاده می‌کند؛ از آن زمان به V4.1 Flash هدایت خواهد شد و تعرفه V4.1 Flash را خواهد داشت.
- **`deepseek-v4-flash`**: شناسه نسل پیشین V4؛ بازنشستگی در سرویس مستقیم ارائه‌دهنده به‌تنهایی تغییر مسیر جدید در AvalAI را تأیید نمی‌کند.
- نام‌های مستعار موجود همچنان زیر پوشش سیاست سازگاری AvalAI در ۱۴۰۵-۰۵-۲۳ / (2026-08-14) هستند. اطلاعات زنده مسیرها را از `/v1/models` بررسی کنید؛ پشتیبانی تأییدشده نقاط پایانی مدل‌های جدید در بالا آمده است، حتی اگر فیلدهای نقاط پایانی در فهرست ناقص باشند.

## قیمت‌گذاری

برای تعرفه V4.1 Flash و قیمت‌های V4-Pro پیش و پس از تغییر مسیر، [اطلاعات قیمت‌گذاری](#اطلاعات-قیمت‌گذاری) بالا را ببینید. تعرفه‌های اعلام‌شده DeepSeek در AvalAI در تمام ساعات ثابت‌اند.

- [جزئیات مدل](fa/models/model-details.md)
- [قیمت‌گذاری AvalAI](fa/pricing.md)

## منابع مرتبط

- [API تکمیل گفتگو](fa/api-reference/chat.md) - نحوه استفاده از مدل‌های گفتگو
- [احراز هویت](fa/api-reference/authentication.md) - نحوه احراز هویت با API AvalAI
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - اطلاعات در مورد محدودیت‌های نرخ API
- [مدیریت خطا](fa/guides/error-handling.md) - نحوه مدیریت خطاها هنگام استفاده از API
- [فراخوانی تابع](fa/guides/function-calling.md) - راهنمای استفاده از فراخوانی تابع با مدل‌های DeepSeek
- [راهنمای استدلال](fa/guides/reasoning.md) - بهترین شیوه‌ها برای وظایف استدلال
