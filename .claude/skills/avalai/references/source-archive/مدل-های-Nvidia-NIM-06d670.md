# مدل‌های Nvidia NIM

AvalAI دسترسی به پلتفرم Nvidia NIM (Nvidia Inference Microservices) را فراهم می‌کند که مدل‌های open-weight بهینه‌شده برای تحقیق و ارزیابی را ارائه می‌دهد. این مدل‌ها با قیمت‌گذاری مناسب برای تحقیق (تقریبا 1/10 نرخ‌های تولید) ارائه می‌شوند و برای تحقیقات آکادمیک، ارزیابی مدل و اهداف آموزشی ایده‌آل هستند.

## اطلاعیه مهم

**این‌ها مدل‌های متمرکز بر تحقیق هستند، نه سرویس‌های عملیاتی .** آن‌ها برای موارد زیر طراحی شده‌اند:
- تحقیقات آکادمیک و آزمایشی
- ارزیابی و معیارسنجی مدل
- پروژه‌های آموزشی و درسی
- توسعه اثبات مفهوم

برای بارهای کاری تولیدی که نیاز به دسترسی و توان عملیاتی بالا دارند، توصیه می‌کنیم از نسخه‌های production-grade از سایر ارائه‌دهندگان استفاده کنید (مثلا Groq برای مدل‌های Llama).

## مدل‌های موجود

### مدل‌های Embedding

Nvidia NIM چندین مدل embedding برای وظایف مختلف درک متن ارائه می‌دهد که شامل مدل‌های مبتنی بر Llama (300M تا 1B پارامتر) و مدل‌های عمومی مانند `nv-embed-v1` و `bge-m3` چندزبانه است. تمام مدل‌های embedding با قیمت $0.002 / 1M توکن ارائه می‌شوند.

### مدل‌های Reranking

مدل‌های reranking برای بهبود نتایج جستجو با امتیازدهی مجدد طراحی شده‌اند. مدل‌های موجود شامل `llama-3.2-nemoretriever-500m-rerank-v2` (500M)، `llama-3.2-nv-rerankqa-1b-v2` (1B) و `nv-rerankqa-mistral-4b-v3` (4B) هستند. تمام مدل‌های reranking $0.0002 به ازای هر کوئری هزینه دارند.

### مدل‌های تولید متن

پلتفرم Nvidia NIM طیف وسیعی از مدل‌های تولید متن ارائه می‌دهد:

**مدل‌های تخصصی:**
- `nemotron-parse`: تجزیه و استخراج اسناد ($0.01/$0.06 per 1M)
- `nvidia-nemotron-nano-9b-v2`: تولید عمومی 9B ($0.004/$0.016 per 1M)
- `eurollm-9b-instruct`: متمرکز بر زبان‌های اروپایی ($0.022/$0.022 per 1M)
- `gemma-3-1b-it`: مدل فشرده Google ($0.001/$0.005 per 1M)

**مدل‌های پیشرفته:**
- `gpt-oss-20b` و `gpt-oss-120b`: معماری GPT متن‌باز
- `qwen3-next-80b-a3b-thinking`: مدل استدلال Alibaba
- `llama-4-scout-17b-16e-instruct`: نسخه کارآمد Llama از Meta
- `llama-3.1-nemotron-ultra-253b-v1`: مدل فوق‌العاده بزرگ
- `llama-3.3-nemotron-super-49b-v1.5`: تعادل بین عملکرد و هزینه

### مدل بینایی

`nemotron-nano-12b-v2-vl`: مدل vision-language برای وظایف مالتی‌مودال مانند توضیح تصویر و پرسش و پاسخ بصری.

## مقایسه قیمت‌گذاری

مدل‌های Nvidia NIM با قیمت تقریبا 1/10 معادل‌های تولیدی ارائه می‌شوند:

| ارائه‌دهنده | مدل | ورودی | خروجی |
|----------|-------|-------|--------|
| Nvidia NIM (تحقیق) | llama-4-scout-17b-16e-instruct | $0.027/1M | $0.085/1M |
| Groq (تولید) | llama-4-scout-17b-16e-instruct | $0.11/1M | $0.34/1M |

## مدل‌های تولیدی NVIDIA (از طریق Fireworks.ai)

علاوه بر مدل‌های NIM تحقیق‌محور بالا، AvalAI یک مدل تولیدی Nemotron از NVIDIA را که از طریق پلتفرم Fireworks.ai سرویس‌دهی می‌شود ارائه می‌دهد. برخلاف مدل‌های تحقیقاتی NIM، این مدل برای بارهای کاری تولیدی با محدودیت‌های نرخ استاندارد در نظر گرفته شده است.

**nemotron-3-ultra**

مدل پرچمدار بزرگ‌مقیاس Nemotron از NVIDIA برای استدلال پیچیده و گردش‌کارهای عاملی که روی Fireworks.ai میزبانی می‌شود.

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `nemotron-3-ultra` |
| مالک | NVIDIA |
| ارائه‌دهنده API | Fireworks.ai |
| قیمت ورودی | $0.60 / 1M توکن |
| قیمت ورودی کش‌شده | $0.12 / 1M توکن |
| قیمت خروجی | $2.40 / 1M توکن |
| در دسترس در | `v1/chat/completions`، `v1/responses` (جزئی) |
| بهترین استفاده | استدلال پیچیده، گردش‌کارهای عاملی، تولید متن باکیفیت |

برای مستندات کامل، نمونه‌های استفاده و فراخوانی تابع، به [صفحه ارائه‌دهنده Fireworks.ai](fa/providers/fireworksai.md#nemotron-3-ultra) مراجعه کنید.

## محدودیت‌های نرخ

| سطح | محدودیت نرخ |
|------|------------|
| پایه | 3 RPM |
| سطح ۱ | 5 RPM |
| سطح ۲ | 10 RPM |
| صطح ۳ | 15 RPM |
| صطح ۴ | 20 RPM |
| صطح ۵ | 30 RPM |

## نمونه‌های استفاده

### Embedding

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="nvidia_nim.nv-embed-v1",
    input="پردازش زبان طبیعی به ماشین‌ها امکان درک زبان انسان را می‌دهد",
)

print(response.data[0].embedding[:5])
```

### تولید متن

```python
response = client.chat.completions.create(
    model="nvidia_nim.llama-3.3-nemotron-super-49b-v1.5",
    messages=[
        {
            "role": "user",
            "content": "تفاوت بین یادگیری با ناظر و بدون ناظر را توضیح دهید.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `nvidia_nim.llama-3.3-nemotron-super-49b-v1.5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="تفاوت بین یادگیری با ناظر و بدون ناظر را توضیح دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### Reranking

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "nvidia_nim.nv-rerankqa-mistral-4b-v3",
        "query": "یادگیری ماشین چیست؟",
        "documents": [
            "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
            "Python یک زبان برنامه‌نویسی محبوب است.",
            "یادگیری عمیق از شبکه‌های عصبی استفاده می‌کند.",
        ],
    },
)
```

### مدل بینایی

```python
import base64


def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


base64_image = encode_image("path/to/image.jpg")

response = client.chat.completions.create(
    model="nvidia_nim.nemotron-nano-12b-v2-vl",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی وجود دارد؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `nvidia_nim.nemotron-nano-12b-v2-vl` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


## موارد استفاده

### تحقیق و آکادمیک
- معیارسنجی عملکرد مدل
- پروژه‌های آموزشی و درسی
- توسعه الگوریتم و آزمایش
- بازتولید و اعتبارسنجی مقالات

### توسعه و نمونه‌سازی
- توسعه اثبات مفهوم
- بررسی ویژگی‌ها قبل از تولید
- ارزیابی مدل مقرون‌به‌صرفه
- تست یکپارچه‌سازی

### توصیه نمی‌شود برای
- برنامه‌های تولیدی با نیاز به دسترسی بالا
- سرویس‌ها با ترافیک کاربر قابل توجه
- برنامه‌های حیاتی
- سیستم‌های زمان واقعی

## بهترین شیوه‌ها

1. **مدیریت محدودیت نرخ**: درخواست‌های خود را در محدوده سطح برنامه‌ریزی کنید
2. **بهینه‌سازی هزینه**: در صورت امکان از ورودی‌های کش‌شده استفاده کنید
3. **انتخاب مدل**: کوچکترین مدلی که نیازهای شما را برآورده می‌کند انتخاب کنید
4. **ارزیابی**: قبل از در نظر گرفتن گزینه‌های تولیدی، آزمایش کامل انجام دهید
5. **استراتژی پشتیبان**: گزینه‌های تولیدی را برای مقیاس‌پذیری شناسایی کنید

## انتقال به تولید

هنگامی که آماده انتقال از تحقیق به تولید هستید:

1. **شناسایی گزینه‌های تولیدی**:
   - مدل‌های Llama → Groq، Together AI یا Fireworks AI
   - مدل‌های Qwen → Alibaba DashScope
   - مدل‌های عمومی → APIهای مستقیم ارائه‌دهنده

2. **مقایسه عملکرد**: معیارسنجی در مقابل نسخه‌های تولیدی
3. **تجزیه و تحلیل هزینه**: محاسبه هزینه‌های تولید در مقابل قیمت‌گذاری تحقیق
4. **برنامه‌ریزی محدودیت نرخ**: اطمینان از تامین نیازهای شما توسط محدودیت‌های تولید

## منابع مرتبط

- [اخبار پشتیبانی از پلتفرم Nvidia NIM](fa/news/2025-11-22-nvidia-nim-platform-support-added.md)
- [مرجع API: Chat Completions](fa/api-reference/messages.md)
- [مرجع API: Embeddings](fa/api-reference/embeddings.md)
- [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [قیمت‌گذاری](fa/pricing.md)
