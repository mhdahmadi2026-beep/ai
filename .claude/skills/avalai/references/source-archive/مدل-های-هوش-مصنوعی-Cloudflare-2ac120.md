# مدل‌های هوش مصنوعی Cloudflare

سرویس Workers AI شرکت Cloudflare، دسترسی به مجموعه‌ای جامع از مدل‌های هوش مصنوعی را فراهم می‌کند که بر روی شبکه جهانی لبه (Edge) این شرکت اجرا می‌شوند. از طریق AvalAI، شما می‌توانید به ۳۳ مدل قدرتمند هوش مصنوعی Cloudflare با تاخیر کم و عملکرد بالا دسترسی داشته باشید و از زیرساخت توزیع‌شده Cloudflare برای استنتاج بهینه هوش مصنوعی بهره‌مند شوید.

## مدل‌های موجود

مدل‌های هوش مصنوعی Cloudflare طیف گسترده‌ای از دسته‌بندی‌ها و ارائه‌دهندگان را پوشش می‌دهند؛ از مدل‌های فشرده و کارآمد گرفته تا سیستم‌های استدلال در مقیاس بزرگ. تمامی این مدل‌ها برای استقرار در لبه شبکه بهینه‌سازی شده‌اند و عملکردی پایدار را در سراسر شبکه جهانی Cloudflare تضمین می‌کنند.

### مدل‌های Meta Llama

Cloudflare میزبان مجموعه‌ای کامل از مدل‌های Llama شرکت متا است؛ از جدیدترین نسخه یعنی Llama 4 Scout گرفته تا نسخه‌های گوناگون سری Llama 3.x.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.llama-4-scout-17b-16e-instruct` | ۱۷ میلیارد (۱۶ متخصص) | چندوجهی (متن و تصویر) | ۱۲۸ هزار |
| `cf.llama-3.3-70b-instruct-fp8-fast` | ۷۰ میلیارد (FP8) | استنتاج سریع، عمومی | ۱۲۸ هزار |
| `cf.llama-3.1-8b-instruct-fast` | ۸ میلیارد | مکالمه سریع چندزبانه | ۱۲۸ هزار |
| `cf.llama-3.1-8b-instruct-awq` | ۸ میلیارد (int4) | استنتاج بهینه | ۱۲۸ هزار |
| `cf.llama-3.1-8b-instruct-fp8` | ۸ میلیارد (FP8) | عملکرد متعادل | ۱۲۸ هزار |
| `cf.llama-3.1-8b-instruct` | ۸ میلیارد | مکالمه استاندارد | ۱۲۸ هزار |
| `cf.llama-3.1-70b-instruct` | ۷۰ میلیارد | استدلال پیچیده | ۱۲۸ هزار |
| `cf.llama-3.2-1b-instruct` | ۱ میلیارد | مکالمه فشرده | ۱۲۸ هزار |
| `cf.llama-3.2-3b-instruct` | ۳ میلیارد | وظایف مبتنی بر عامل (Agentic) | ۱۲۸ هزار |
| `cf.meta-llama-3-8b-instruct` | ۸ میلیارد | استدلال بهبودیافته | ۸ هزار |
| `cf.llama-3-8b-instruct-awq` | ۸ میلیارد (int4) | استقرار بهینه | ۸ هزار |
| `cf.llama-3-8b-instruct` | ۸ میلیارد | دستورالعمل استاندارد | ۸ هزار |
| `cf.llama-guard-3-8b` | ۸ میلیارد | ایمنی محتوا | ۸ هزار |

#### Llama 4 Scout - اوج قابلیت‌های چندوجهی

این جدیدترین عضو خانواده Llama، قابلیت‌های چندوجهی را به صورت بومی ارائه می‌دهد:

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# درک متن و تصویر
completion = client.chat.completions.create(
    model="cf.llama-4-scout-17b-16e-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این تصویر شامل چه چیزهایی است؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "data:image/jpeg;base64,..."},
                },
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.llama-4-scout-17b-16e-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


### مدل‌های Google Gemma

مدل‌های Gemma از گوگل، عملکردی فوق‌العاده را با قابلیت‌های چندزبانه و پشتیبانی از LoRA ترکیب می‌کنند.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.gemma-3-12b-it` | ۱۲ میلیارد | چندوجهی، بیش از ۱۴۰ زبان | ۱۲۸ هزار |
| `cf.gemma-7b-it-lora` | ۷ میلیارد | تنظیم دقیق (Fine-tuning) با LoRA | ۸ هزار |
| `cf.gemma-2b-it-lora` | ۲ میلیارد | LoRA فشرده | ۸ هزار |
| `cf.gemma-7b-it` | ۷ میلیارد | دستورالعمل عمومی | ۸ هزار |

#### Gemma 3 - چندوجهی پیشرفته

```python
# Gemma 3 با پنجره زمینه گسترده
completion = client.chat.completions.create(
    model="cf.gemma-3-12b-it",
    messages=[
        {
            "role": "user",
            "content": "این سند را تحلیل کرده و خلاصه‌ای جامع از آن ارائه دهید.",
        }
    ],
    max_tokens=2048,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.gemma-3-12b-it` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این سند را تحلیل کرده و خلاصه‌ای جامع از آن ارائه دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدل‌های Mistral AI

جدیدترین مدل‌های Mistral با درک بصری بهبودیافته و پنجره زمینه گسترده‌تر.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.mistral-small-3.1-24b-instruct` | ۲۴ میلیارد | بینایی + متن، فراخوانی توابع | ۱۲۸ هزار |

#### Mistral Small 3.1 - تقویت‌شده با بینایی

```python
# فراخوانی توابع به همراه قابلیت‌های بصری
completion = client.chat.completions.create(
    model="cf.mistral-small-3.1-24b-instruct",
    messages=[
        {
            "role": "user",
            "content": "این نمودار را تحلیل کرده و معیارهای کلیدی آن را استخراج کنید.",
        }
    ],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "extract_metrics",
                "description": "استخراج معیارهای عددی از داده‌ها",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "metrics": {"type": "array", "items": {"type": "number"}}
                    },
                },
            },
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.mistral-small-3.1-24b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این نمودار را تحلیل کرده و معیارهای کلیدی آن را استخراج کنید.",
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


### مدل‌های Qwen

مدل‌های Qwen از شرکت Alibaba که برای استدلال، تولید کد و embedding تخصصی شده‌اند.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.qwq-32b` | ۳۲ میلیارد | استدلال پیشرفته | ۳۲ هزار |
| `cf.qwen2.5-coder-32b-instruct` | ۳۲ میلیارد | تولید کد | ۱۲۸ هزار |
| `cf.qwen3-30b-a3b-fp8` | ۳۰ میلیارد (FP8) | چت، عملکرد متعادل | ۱۲۸ هزار |
| `cf.qwen3-embedding-0.6b` | ۰.۶ میلیارد | embedding متن | - |

#### QwQ - مدل استدلالگر

```python
# وظایف نیازمند استدلال پیشرفته
completion = client.chat.completions.create(
    model="cf.qwq-32b",
    messages=[
        {
            "role": "user",
            "content": "این مسئله پیچیده ریاضی را گام به گام حل کنید: اگر قطاری ۱۲۰ کیلومتر را در ۲ ساعت طی کند و سپس سرعت خود را ۲۰٪ افزایش دهد، چقدر زمان برای طی کردن ۱۸۰ کیلومتر بعدی نیاز دارد؟",
        }
    ],
    temperature=0.1,  # دمای پایین‌تر برای وظایf استدلالی
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.qwq-32b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این مسئله پیچیده ریاضی را گام به گام حل کنید: اگر قطاری ۱۲۰ کیلومتر را در ۲ ساعت طی کند و سپس سرعت خود را ۲۰٪ افزایش دهد، چقدر زمان برای طی کردن ۱۸۰ کیلومتر بعدی نیاز دارد؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### Qwen2.5-Coder - متخصص برنامه‌نویسی

```python
# تولید و توضیح کد
completion = client.chat.completions.create(
    model="cf.qwen2.5-coder-32b-instruct",
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی به همراه عملیات درج، جستجو و حذف بنویسید.",
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.qwen2.5-coder-32b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی به همراه عملیات درج، جستجو و حذف بنویسید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدل‌های DeepSeek

مدل‌های استدلال تقطیر شده از DeepSeek که عملکردی رقابتی ارائه می‌دهند.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.deepseek-r1-distill-qwen-32b` | ۳۲ میلیارد | استدلال، عملکرد بهتر از o1-mini | ۱۲۸ هزار |

### مدل‌های متن‌باز OpenAI

مدل‌های متن‌باز OpenAI که روی شبکه لبه Cloudflare در دسترس هستند.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.gpt-oss-120b` | ۱۲۰ میلیارد | استدلال در مقیاس بزرگ | ۱۲۸ هزار |
| `cf.gpt-oss-20b` | ۲۰ میلیارد | عمومی کارآمد | ۱۲۸ هزار |

### مدل‌های NVIDIA Nemotron

جدیدترین مدل‌های Nemotron از NVIDIA با معماری ترکیبی LatentMoE.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.nemotron-3-120b-a12b` | ۱۲۰ میلیارد (۱۲ میلیارد فعال) | گردش‌های کاری عاملی، استدلال زمینه بلند | ۱ میلیون |

#### Nemotron-3-120B-A12B - برتری عاملی

Nemotron-3-Super-120B-A12B از NVIDIA یک مدل زبانی بزرگ است که برای ارائه قابلیت‌های قوی عاملی، استدلال و مکالمه طراحی شده است. این مدل از معماری ترکیبی LatentMoE با لایه‌های متناوب Mamba-2 و MoE با پیش‌بینی چند توکن (MTP) برای تولید متن سریع‌تر استفاده می‌کند.

| ویژگی | جزئیات |
|-------|--------|
| کل پارامترها | ۱۲۰ میلیارد (۱۲ میلیارد فعال) |
| معماری | LatentMoE - ترکیب Mamba-2 + MoE + Attention |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن |
| قیمت ورودی | ۰.۵۰ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۰۵ دلار / ۱ میلیون توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | ۱.۵۰ دلار / ۱ میلیون توکن |
| زبان‌های پشتیبانی‌شده | انگلیسی، فرانسوی، آلمانی، ایتالیایی، ژاپنی، اسپانیایی، چینی |
| بهترین استفاده | گردش‌های کاری عاملی، استدلال زمینه بلند، اتوماسیون تیکت IT |

**ویژگی‌های کلیدی:**
- **پنجره زمینه ۱ میلیون**: طول زمینه پیشرو در صنعت برای اسناد گسترده
- **استدلال قابل تنظیم**: فعال یا غیرفعال کردن حالت استدلال از طریق الگوی چت
- **پیش‌بینی چند توکن**: لایه‌های MTP برای تولید متن سریع‌تر
- **استفاده از ابزار و RAG**: عالی برای فراخوانی ابزار و تولید مبتنی بر بازیابی
- **مقرون‌به‌صرفه**: فقط ۱۲ میلیارد پارامتر فعال برای کارایی استثنایی

**نکات برجسته معیار:**
- SWE-Bench (OpenHands): ۶۰.۴۷٪
- AIME 2025: ۹۰.۲۱٪
- HMMT Feb 2025 (با ابزار): ۹۴.۷۳٪
- LiveCodeBench: ۸۱.۱۹٪

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استدلال زمینه بلند با Nemotron
completion = client.chat.completions.create(
    model="cf.nemotron-3-120b-a12b",
    messages=[
        {
            "role": "user",
            "content": "این کدبیس گسترده را تحلیل کن و بهبودهای معماری برای مقیاس‌پذیری بهتر پیشنهاد بده.",
        }
    ],
    temperature=1.0,  # تنظیم پیشنهادی برای Nemotron
    top_p=0.95,
)

print(completion.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.nemotron-3-120b-a12b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این کدبیس گسترده را تحلیل کن و بهبودهای معماری برای مقیاس‌پذیری بهتر پیشنهاد بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدل‌های IBM Granite

مدل‌های Granite از IBM برای کاربردهای سازمانی.

| مدل | پارامترها | تخصص | پنجره زمینه (Context) |
|-----|----------|-------|-----------------------|
| `cf.granite-4.0-h-micro` | Micro | چت سازمانی کارآمد | ۱۲۸ هزار |

### مدل‌های تولید تصویر

Cloudflare AI مدل‌های قدرتمند تولید تصویر را از طریق نقطه پایانی `v1/images/generations` ارائه می‌دهد.

| مدل | توضیحات | قیمت پایه (۱ مگاپیکسل) |
|-----|---------|------------------------|
| `cf.flux-2-klein-9b` | مدل FLUX 2 Klein با ۹ میلیارد پارامتر | $۰.۰۱۵/تصویر |
| `cf.flux-2-klein-4b` | مدل فشرده FLUX 2 Klein با ۴ میلیارد پارامتر | $۰.۰۱۰/تصویر |
| `cf.flux-2-dev` | مدل توسعه FLUX 2 | $۰.۰۱۰/تصویر |
| `cf.lucid-origin` | تولید تصویر Lucid Origin | $۰.۰۱۵/تصویر |
| `cf.phoenix-1.0` | تولید تصویر Phoenix 1.0 | $۰.۰۱۵/تصویر |

#### مثال تولید تصویر

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر با FLUX 2 Klein
response = client.images.generate(
    model="cf.flux-2-klein-9b",
    prompt="یک شهر آینده‌نگر در غروب خورشید با ماشین‌های پرنده",
    n=1,
    size="1024x1024",
)

print(response.data[0].url)
```

### مدل‌های Embedding

Cloudflare AI مدل‌های embedding را برای جستجوی معنایی و تحلیل متن از طریق نقطه پایانی `v1/embeddings` ارائه می‌دهد.

| مدل | صاحب | توضیحات | قیمت ورودی (دلار/۱م توکن) |
|-----|------|---------|---------------------------|
| `cf.qwen3-embedding-0.6b` | Alibaba | Qwen3 Embedding ۰.۶ میلیارد | $۰.۰۱۲ |
| `cf.plamo-embedding-1b` | PFN | PLaMo Embedding ۱ میلیارد | $۰.۰۱۹ |
| `cf.embeddinggemma-300m` | Google | EmbeddingGemma ۳۰۰ میلیون | $۰.۰۱۲ |

#### مثال Embedding

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید embedding
response = client.embeddings.create(
    model="cf.qwen3-embedding-0.6b",
    input="یادگیری ماشین به کامپیوترها امکان یادگیری از داده‌ها را می‌دهد.",
)

embedding = response.data[0].embedding
print(f"ابعاد embedding: {len(embedding)}")
```

## پارامترهای کلیدی

مدل‌های Cloudflare از پارامترهای استاندارد سازگار با OpenAI پشتیبانی می‌کنند:

| پارامتر | توضیحات | مقدار پیش‌فرض | محدوده |
|---------|---------|---------------|---------|
| `temperature` | میزان خلاقیت پاسخ را کنترل می‌کند | 0.7 | 0.0 تا 2.0 |
| `max_tokens` | حداکثر طول پاسخ تولیدی | 2048 | 1 تا 4096 |
| `top_p` | نمونه‌گیری هسته‌ای (Nucleus sampling) | 1.0 | 0.0 تا 1.0 |
| `frequency_penalty` | جریمه تکرار کلمات | 0.0 | -2.0 تا 2.0 |
| `presence_penalty` | جریمه تکرار موضوعات | 0.0 | -2.0 تا 2.0 |

## نقاط پایانی (Endpoints) API

مدل‌های Cloudflare بسته به نوع مدل از طریق نقاط پایانی مختلف در AvalAI قابل دسترسی هستند:

- **تکمیل چت (Chat Completions)**: [`v1/chat/completions`](fa/api-reference/chat.md) (پشتیبانی کامل)
- **پاسخ‌ها (Responses)**: [`v1/responses`](fa/api-reference/responses.md) (پشتیبانی جزئی)
- **Embeddings**: [`v1/embeddings`](fa/api-reference/embeddings.md) (مدل‌های embedding)
- **تولید تصویر**: [`v1/images/generations`](fa/api-reference/images.md) (مدل‌های تصویر)

## مثال‌های کاربردی

### تولید متن ساده

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="cf.llama-3.1-8b-instruct",
    messages=[
        {"role": "system", "content": "شما یک دستیار هوشمند و مفید هستید."},
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده شرح دهید."},
    ],
    temperature=0.7,
    max_tokens=1024,
)

print(completion.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.llama-3.1-8b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="محاسبات کوانتومی را به زبان ساده شرح دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### دریافت پاسخ به صورت جریانی (Streaming)

```python
# استفاده از Streaming برای دریافت پاسخ‌های آنی
stream = client.chat.completions.create(
    model="cf.llama-3.3-70b-instruct-fp8-fast",
    messages=[
        {
            "role": "user",
            "content": "داستان کوتاهی درباره آینده هوش مصنوعی و بشریت بنویسید.",
        }
    ],
    stream=True,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.llama-3.3-70b-instruct-fp8-fast` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="داستان کوتاهی درباره آینده هوش مصنوعی و بشریت بنویسید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### فراخوانی توابع (Function Calling)

```python
# فراخوانی توابع با مدل‌های پشتیبانی‌کننده
completion = client.chat.completions.create(
    model="cf.mistral-small-3.1-24b-instruct",
    messages=[{"role": "user", "content": "آب و هوای تهران الان چطور است؟"}],
    tools=[
        {
            "type": "function",
            "function": {
                "name": "get_weather",
                "description": "دریافت اطلاعات آب و هوای یک شهر",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "city": {"type": "string", "description": "نام شهر"}
                    },
                    "required": ["city"],
                },
            },
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.mistral-small-3.1-24b-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="آب و هوای تهران الان چطور است؟",
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


## بهترین شیوه‌ها (Best Practices)

### انتخاب مدل مناسب

- **برای سرعت**: از مدل‌های کوانتیزه‌شده FP8 یا AWQ مانند `cf.llama-3.3-70b-instruct-fp8-fast` استفاده کنید.
- **برای استدلال**: مدل‌های `cf.qwq-32b` یا `cf.deepseek-r1-distill-qwen-32b` گزینه‌های بهتری هستند.
- **برای کدنویسی**: از مدل تخصصی `cf.qwen2.5-coder-32b-instruct` استفاده کنید.
- **برای کاربردهای چندوجهی**: مدل‌های `cf.llama-4-scout-17b-16e-instruct` یا `cf.gemma-3-12b-it` را انتخاب کنید.
- **برای بهینه‌سازی مصرف**: مدل‌های فشرده مانند `cf.llama-3.2-1b-instruct` را امتحان کنید.

### بهینه‌سازی عملکرد

1. **کوانتیزه‌سازی مناسب**: مدل‌های FP8 تعادل خوبی بین سرعت و کیفیت برقرار می‌کنند.
2. **بهره‌گیری از شبکه لبه**: این مدل‌ها به دلیل اجرا بر روی شبکه جهانی Cloudflare، تاخیر بسیار کمی دارند.
3. **مدیریت زمینه**: از پنجره زمینه گسترده (تا ۱۲۸ هزار توکن) به شکل بهینه استفاده کنید.
4. **پاسخ جریانی**: برای بهبود تجربه کاربری در اپلیکیشن‌های تعاملی، قابلیت Streaming را فعال کنید.

### ایمنی محتوا

برای کنترل و نظارت بر محتوا، از مدل `cf.llama-guard-3-8b` استفاده کنید:

```python
# بررسی ایمنی محتوا
safety_check = client.chat.completions.create(
    model="cf.llama-guard-3-8b",
    messages=[{"role": "user", "content": "پیام کاربر برای بررسی از نظر ایمنی"}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cf.llama-guard-3-8b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="پیام کاربر برای بررسی از نظر ایمنی",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## استفاده از مدل‌های Cloudflare از طریق AvalAI

مدل‌های هوش مصنوعی Cloudflare به صورت یکپارچه با API واحد AvalAI ادغام شده‌اند. تمامی این مدل‌ها از رابط استاندارد سازگار با OpenAI استفاده می‌کنند، که این امر جابجایی بین مدل‌های مختلف Cloudflare یا ترکیب آن‌ها با سایر ارائه‌دهندگان را بسیار ساده می‌سازد.

### احراز هویت

```python
client = OpenAI(
    api_key="your-avalai-api-key",  # کلید API شما در AvalAI
    base_url="https://api.avalai.ir/v1",  # نقطه پایانی AvalAI
)
```

### محدودیت‌های نرخ استفاده (Rate Limits)

مدل‌های Cloudflare از سیاست‌های استاندارد محدودیت نرخ در AvalAI پیروی می‌کنند. برای اطلاع از محدودیت‌های سطح کاربری خود، به [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md) مراجعه کنید.

## منابع مرتبط

- [مستندات API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [راهنمای فراخوانی توابع](fa/guides/function-calling.md)
- [راهنمای قابلیت‌های بصری](fa/guides/vision.md)
- [راهنمای دریافت پاسخ جریانی](fa/guides/streaming-responses.md)
- [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [راهنمای بهترین شیوه‌ها](fa/guides/best-practices.md)
