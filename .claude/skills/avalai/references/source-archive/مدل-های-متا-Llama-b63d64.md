# مدل‌های متا (Llama)

AvalAI از طریق ادغام‌های مختلف با شرکا مانند AWS Bedrock و Google Vertex AI، دسترسی به خانواده قدرتمند مدل‌های Llama متا را فراهم می‌کند. این صفحه جزئیات برخی از مدل‌های رایج Llama موجود را شرح می‌دهد.

## سری Llama 3.1

سری Llama 3.1 پیشرفت‌های قابل توجهی در استدلال، تولید کد و پیروی از دستورالعمل‌ها، همراه با پنجره‌های زمینه بزرگ ارائه می‌دهد.

### Llama 3.1 405B Instruct

بزرگترین و توانمندترین مدل در سری Llama 3.1 که برای وظایف پیچیده استدلال و تولید طراحی شده است.

| ویژگی | جزئیات |
|-------------------|-----------------------------------------------------------------------|
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن ورودی، ۴٬۰۹۶ توکن خروجی |
| داده‌های آموزشی | تا مارس ۲۰۲۴ |
| قیمت‌گذاری ورودی | ~۵.۳۲ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| قیمت‌گذاری خروجی | ~۱۶.۰۰ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| نقاط قوت | عملکرد پیشرفته برای مدل‌های باز، برتری در استدلال، کد، ظرافت |
| بهترین برای | وظایف بسیار پیچیده، تحقیق، پرامپت‌های عملیاتی چالش‌برانگیز |

```python
response = client.chat.completions.create(
    # نام مدل ممکن است بر اساس ارائه دهنده متفاوت باشد، به عنوان مثال 'meta.llama3-1-405b-instruct-v1:0' در Bedrock
    model="meta.llama3-1-405b-instruct-v1:0",
    messages=[
        {"role": "system", "content": "شما یک معمار خبره هستید."},
        {
            "role": "user",
            "content": "یک معماری پایدار و مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک جهانی طراحی کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `meta.llama3-1-405b-instruct-v1:0` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک معماری پایدار و مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک جهانی طراحی کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Llama 3.1 70B Instruct

تعادل قوی بین عملکرد و کارایی، مناسب برای طیف گسترده‌ای از وظایف سخت.

| ویژگی | جزئیات |
|-------------------|-----------------------------------------------------------------------|
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن ورودی، ۲٬۰۴۸ توکن خروجی |
| داده‌های آموزشی | تا مارس ۲۰۲۴ |
| قیمت‌گذاری ورودی | ~۰.۹۹ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| قیمت‌گذاری خروجی | ~۰.۹۹ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| نقاط قوت | عملکرد عالی نسبت به اندازه‌اش، پیروی قوی از دستورالعمل |
| بهترین برای | برنامه‌های چت پیچیده، تولید محتوا، سیستم‌های RAG |

```python
response = client.chat.completions.create(
    # نام مدل ممکن است متفاوت باشد، به عنوان مثال 'meta.llama3-1-70b-instruct-v1:0' در Bedrock
    model="meta.llama3-1-70b-instruct-v1:0",
    messages=[
        {"role": "system", "content": "شما یک دستیار هوش مصنوعی مفید هستید."},
        {
            "role": "user",
            "content": "مدل‌های Llama 3.1 70B و 8B را مقایسه و تفاوت‌هایشان را بیان کنید.",
        },
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `meta.llama3-1-70b-instruct-v1:0` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مدل‌های Llama 3.1 70B و 8B را مقایسه و تفاوت‌هایشان را بیان کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Llama 3.1 8B Instruct

کوچکترین مدل در سری Llama 3.1، بهینه‌شده برای سرعت و کارایی در وظایف کمتر پیچیده.

| ویژگی | جزئیات |
|-------------------|-----------------------------------------------------------------------|
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن ورودی، ۲٬۰۴۸ توکن خروجی |
| داده‌های آموزشی | تا مارس ۲۰۲۴ |
| قیمت‌گذاری ورودی | ~۰.۲۲ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| قیمت‌گذاری خروجی | ~۰.۲۲ دلار / ۱ میلیون توکن (از طریق Bedrock) |
| نقاط قوت | بسیار سریع و مقرون به صرفه، مناسب برای وظایف ساده‌تر |
| بهترین برای | ربات‌های چت ساده، خلاصه‌سازی، طبقه‌بندی، تولید محتوای سبک |

```python
response = client.chat.completions.create(
    # نام مدل ممکن است متفاوت باشد، به عنوان مثال 'meta.llama3-1-8b-instruct-v1:0' در Bedrock
    model="meta.llama3-1-8b-instruct-v1:0",
    messages=[
        {"role": "user", "content": "پایتخت فرانسه کجاست؟"},
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `meta.llama3-1-8b-instruct-v1:0` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="پایتخت فرانسه کجاست؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## سری Llama 3.2 (پیش‌نمایش)

سری Llama 3.2 قابلیت‌های جدیدی از جمله بینایی و بهبودهای عملکردی بیشتری را معرفی می‌کند. در دسترس بودن ممکن است در ابتدا محدود باشد.

### Llama 3.2 90B Vision Instruct

یک مدل چندوجهی بزرگ که قابلیت‌های متنی قوی را با درک بینایی ترکیب می‌کند.

| ویژگی | جزئیات |
|-------------------|-----------------------------------------------------------------------|
| پنجره زمینه | ۱۲۸٬۰۰۰ توکن ورودی، ۲٬۰۴۸ توکن خروجی |
| داده‌های آموزشی | آخرین داده‌های موجود (تخمینی) |
| قیمت‌گذاری ورودی | (قیمت ارائه دهنده را بررسی کنید، به عنوان مثال Vertex AI) |
| قیمت‌گذاری خروجی | (قیمت ارائه دهنده را بررسی کنید، به عنوان مثال Vertex AI) |
| نقاط قوت | ورودی چندوجهی (متن و تصویر)، استدلال قوی |
| بهترین برای | برنامه‌هایی که نیاز به درک همزمان متن و تصویر دارند |

```python
# ساختار مثال - فراخوانی‌های API خاص ممکن است بر اساس ارائه دهنده متفاوت باشد
response = client.chat.completions.create(
    model="llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این تصویر را توصیف کنید."},
                {"type": "image_url", "image_url": {"url": "..."}},
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `llama-4-scout-17b-16e-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


## سری Llama 4 Scout (پیش‌نمایش از طریق Together AI)

سری Llama 4 Scout مدل‌های آزمایشی هستند که بر روی قابلیت‌های خاص یا بهبود کارایی تمرکز دارند.

### Llama 4 Scout 17B 128e Instruct FP8

یک مدل آزمایشی که احتمالا از دقت FP8 برای بهبود کارایی استفاده می‌کند.

| ویژگی | جزئیات |
| ----------------------- | -------------------------------------- |
| ارائه دهنده | Together AI |
| مالک | Meta |
| پنجره زمینه | (جزئیات ارائه دهنده را بررسی کنید) |
| قیمت‌گذاری ورودی | (جزئیات ارائه دهنده را از طریق AvalAI بررسی کنید) |
| قیمت‌گذاری خروجی | (جزئیات ارائه دهنده را از طریق AvalAI بررسی کنید) |
| حداکثر درخواست/دقیقه | ۵۰.۰ |
| حداکثر توکن/دقیقه | ۴۰۰٬۰۰۰.۰ |
| نقاط قوت | آزمایشی، کارایی بالقوه بالا |
| بهترین برای | تست معماری‌ها/فرمت‌های جدید مدل |
| شناسه مدل (مثال) | `together_ai/meta-llama/llama-4-scout-17b-128e-instruct-fp8` |

```python
# مثال استفاده از Llama 4 Scout 17B FP8 از طریق Together AI
response = client.chat.completions.create(
    model="llama-4-scout-17b-128e-instruct-fp8",
    messages=[{"role": "user", "content": "مزایای بالقوه استنتاج FP8 چیست؟"}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `llama-4-scout-17b-128e-instruct-fp8` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مزایای بالقوه استنتاج FP8 چیست؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Llama 4 Scout 17B 16e Instruct

یک مدل آزمایشی دیگر از سری Scout.

| ویژگی | جزئیات |
| ----------------------- | -------------------------------------- |
| ارائه دهنده | Together AI |
| مالک | Meta |
| پنجره زمینه | (جزئیات ارائه دهنده را بررسی کنید) |
| قیمت‌گذاری ورودی | (جزئیات ارائه دهنده را از طریق AvalAI بررسی کنید) |
| قیمت‌گذاری خروجی | (جزئیات ارائه دهنده را از طریق AvalAI بررسی کنید) |
| حداکثر درخواست/دقیقه | ۵۰.۰ |
| حداکثر توکن/دقیقه | ۴۰۰٬۰۰۰.۰ |
| نقاط قوت | آزمایشی |
| بهترین برای | تست قابلیت‌های جدید مدل |
| شناسه مدل (مثال) | `together_ai/meta-llama/llama-4-scout-17b-16e-instruct` |

```python
# مثال استفاده از Llama 4 Scout 17B 16e از طریق Together AI
response = client.chat.completions.create(
    model="llama-4-scout-17b-16e-instruct",
    messages=[
        {"role": "user", "content": "ویژگی‌های کلیدی سری Llama 4 Scout را خلاصه کنید."}
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `llama-4-scout-17b-16e-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="ویژگی‌های کلیدی سری Llama 4 Scout را خلاصه کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مدل‌های Llama قبلی

نسخه‌های قدیمی‌تر مانند Llama 3 (8B، 70B) و Llama 2 (7B، 13B، 70B) نیز از طریق ارائه‌دهندگان مختلف قابل دسترسی از طریق AvalAI در دسترس هستند، اغلب با قیمت‌های پایین‌تر اما با پنجره‌های زمینه کوچکتر و عملکرد بالقوه پایین‌تر در مقایسه با Llama 3.1/3.2. برای جزئیات به مستندات ارائه دهنده خاص که از طریق AvalAI پیوند داده شده است، مراجعه کنید.

## استفاده از مدل‌های Meta از طریق AvalAI

با استفاده از نقاط پایانی استاندارد API AvalAI و کتابخانه‌های سازگار با OpenAI به مدل‌های Llama که توسط شرکایی مانند Bedrock یا Vertex AI میزبانی می‌شوند، دسترسی پیدا کنید. اطمینان حاصل کنید که از شناسه مدل صحیح همانطور که توسط ادغام AvalAI خاص ارائه شده است، استفاده می‌کنید.

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

# مثال استفاده از مدل Llama 3.1 (شناسه به ارائه دهنده بستگی دارد)
response = client.chat.completions.create(
    model="meta.llama3-1-70b-instruct-v1:0",  # شناسه مثال Bedrock
    messages=[{"role": "user", "content": "درباره مدل‌های Llama به من بگو."}],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `meta.llama3-1-70b-instruct-v1:0` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="درباره مدل‌های Llama به من بگو.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## منابع مرتبط

- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API تعبیه‌سازی](fa/api-reference/embeddings.md)
- [مرجع API آوا](fa/api-reference/audio.md)
- [مرجع API نظارت](fa/api-reference/moderation.md)
- [احراز هویت](fa/api-reference/authentication.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
