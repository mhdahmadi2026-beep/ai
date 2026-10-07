# بهترین شیوه‌های استفاده از API AvalAI

از این صفحه به‌عنوان چک‌لیست سریع production برای ساخت روی API سازگار با OpenAI در AvalAI استفاده کنید. این راهنما نکات رسمی OpenAI درباره production، deployment، prompting، safety و accuracy را برای `https://api.avalai.ir/v1` تطبیق می‌دهد.

برای جزئیات اجرایی، از راهنماهای تخصصی زیر شروع کنید و این صفحه را تنها منبع تصمیم‌گیری در نظر نگیرید.

## نقشه مطالعه پیشنهادی

| هدف | از اینجا شروع کنید | دلیل |
| --- | --- | --- |
| انتشار قابلیت AI جدید | [چک‌لیست استقرار API](fa/guides/deployment-checklist.md) | راه‌اندازی Responses-first، effort استدلال، verbosity، cache، job پس‌زمینه و workflowهای طولانی. |
| آماده‌سازی production | [بهترین شیوه‌های استقرار](fa/guides/production-best-practices.md) | مقیاس‌پذیری، observability، محدودیت نرخ، کنترل هزینه، امنیت و نظم release. |
| بهبود کیفیت پرامپت | [مهندسی پرامپت](fa/guides/prompt-engineering.md) | دستورالعمل‌ها، مثال‌ها، قالب خروجی، حلقه ارزیابی و تشخیص زمان عبور از prompt-only fixes. |
| کاهش هزینه یا تأخیر | [بهینه‌سازی هزینه](fa/guides/cost-optimization.md)، [بهینه‌سازی تأخیر](fa/guides/latency-optimization.md) | routing مدل، بودجه توکن، streaming، caching، batching و service tierها. |
| افزایش دقت واقعی | [بهینه‌سازی دقت LLM](fa/guides/optimizing-llm-accuracy.md)، [ارزیابی‌ها](fa/guides/evals.md) | قبل از تغییر prompt، retrieval، fine-tuning یا model، eval اجرا کنید. |
| مدیریت ریسک ایمنی | [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md)، [چک‌های ایمنی](fa/guides/safety-checks.md)، [Red Teaming](fa/guides/red-teaming.md) | شناسه کاربر، moderation، approval ابزار و آزمون ریسک پیش از release. |

## استفاده اصلی از API

- **برای کار جدید با Responses شروع کنید:** برای state، ابزارها، reasoning، خروجی ساختاریافته و رفتارهای جدید مدل از `/v1/responses` شروع کنید. `/v1/chat/completions` را برای integrationهای پایدار موجود و مدل‌هایی نگه دارید که فقط سازگاری chat دارند.
- **secretها را سمت server نگه دارید:** `AVALAI_API_KEY` را از environment variable یا secret manager بخوانید. کلید بلندمدت را در browser، mobile، repo عمومی، log یا screenshot قرار ندهید.
- **محدودیت نرخ را زود طراحی کنید:** headerهای پاسخ را مانیتور کنید، exponential backoff همراه jitter بگذارید و batching یا background processing را فقط وقتی به throughput کمک می‌کند استفاده کنید.
- **برای debug کافی log کنید:** request ID، مدل، provider، endpoint، latency، تعداد retry، status، usage و شناسه tenant/user را ثبت کنید. secret یا داده شخصی غیرضروری را log نکنید.
- **ورودی و خروجی را validate کنید:** schema، محدودیت اندازه، نوع فایل، moderation و allowlist ابزارها را پیش از عملیات پرهزینه یا پرریسک اعمال کنید.

## انتخاب مدل و API

| مورد استفاده | شروع پیشنهادی | نکته |
| --- | --- | --- |
| دستیارهای عمومی | `gpt-5.5`, `gpt-5.4-mini`, `gpt-5.4-nano` | بر اساس کیفیت، latency و هزینه route کنید. در مدل‌های سازگار با Responses از `text.verbosity` برای کنترل طول پاسخ استفاده کنید. |
| استدلال پیچیده | `gpt-5.5`, `gpt-5.4-pro` و گزینه‌های reasoning | `reasoning.effort` را بر اساس task تنظیم کنید؛ تا وقتی eval نشان نداده از بیشترین effort استفاده نکنید. |
| تولید کد | `gpt-5.3-codex`, `gpt-5.5`, `claude-opus-4-8`, `kimi-k2.7-code` | برای workflowهای کدنویسی APIمحور Responses را ترجیح دهید؛ برای agentهای ویرایش repo راهنماهای Codex را ببینید. |
| پشتیبانی سریع یا routing | مدل‌های کوچک‌تر GPT، Claude Haiku، Gemini Flash یا Qwen Flash | پرامپت را کوتاه نگه دارید، خروجی را محدود کنید و فقط وقتی UX بهتر می‌شود stream کنید. |
| Retrieval و جستجو | `/v1/embeddings` همراه `/v1/responses` | امروز retrieval را سمت برنامه بسازید؛ File Search را تا زمان فعال شدن hosted support مرجع طراحی بدانید. |
| تصویر، صوت، ویدیو | راهنماهای API اختصاصی | از [تصاویر](fa/api-reference/images.md)، [صوت](fa/api-reference/audio.md) و [ویدیو](fa/api-reference/videos.md) شروع کنید. |

## پیش‌فرض‌های پرامپت‌نویسی

- رفتار پایدار را در `instructions` برای Responses یا پیام system/developer برای Chat Completions بگذارید.
- task، مخاطب، محدودیت‌ها و قالب خروجی را صریح بنویسید.
- فقط context مرتبط بدهید؛ به جای چسباندن کل knowledge base از retrieval یا file input استفاده کنید.
- وقتی کد پایین‌دست به fieldهای دقیق وابسته است، structured outputs یا function tools را ترجیح دهید.
- پیش از تغییر model، reasoning effort یا fine-tuning، پرامپت را با مثال‌های نماینده ارزیابی کنید.

## قواعد Production همسو با OpenAI

- **Responses را دفاعی parse کنید:** برای متن ساده از `response.output_text` استفاده کنید، اما وقتی درخواست می‌تواند tool call، refusal، annotation، فایل، تصویر یا metadata مربوط به reasoning برگرداند، `response.output` را بر اساس `type` بررسی کنید.
- **پرامپت‌ها را در کد version کنید:** prompt builderها، schemaها، مثال‌ها و fixtureهای eval را در version control نگه دارید. برای deploymentهای AvalAI به prompt objectهای hosted تکیه نکنید مگر اینکه route صریحا پشتیبانی و تست شده باشد.
- **JSON نهایی را از آرگومان ابزار جدا کنید:** برای پاسخ typed به کاربر از Structured Outputs و برای actionهای برنامه از function calling استفاده کنید. در هر دو حالت نتیجه را دوباره در کد server validate کنید.
- **قرارداد ابزار را strict نگه دارید:** `strict: true`، `additionalProperties: false` و فهرست fieldهای required را تنظیم کنید و برای مقدارهای اختیاری از union شامل `null` استفاده کنید. برای write، پرداخت یا approval، `parallel_tool_calls: false` بگذارید.
- **state را آگاهانه حفظ کنید:** در Responses وقتی retention قابل قبول است از `previous_response_id` استفاده کنید؛ در غیر این صورت فقط آیتم‌های خروجی لازم را replay کنید، از جمله `call_id`های متناظر برای نتیجه ابزار.
- **برای کار طولانی progress نشان دهید:** وقتی task از retrieval، ابزارها یا background processing استفاده می‌کند، پیش از پاسخ نهایی یک preamble یا event کوتاه stream کنید تا کاربر بداند درخواست در حال پیشروی است.

## موارد استفاده خاص

### تکمیل چت

- **حفظ تاریخچه مکالمه**: تاریخچه مکالمه مرتبط را برای زمینه شامل کنید.
- **محدود کردن طول مکالمه**: مکالمات بسیار طولانی توکن‌های بیشتری مصرف می‌کنند و می‌توانند منجر به از دست دادن زمینه شوند.
- **استفاده از function calling برای actionها**: وقتی مدل باید کد شما را فراخوانی کند از function calling استفاده کنید. وقتی خود پاسخ نهایی باید JSON باشد، [Structured Outputs](fa/guides/structured-outputs.md) مناسب‌تر است.

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
        "function": {
            "name": "get_weather",
            "description": "دریافت وضعیت آب و هوای فعلی در یک مکان معین.",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "شهر و ایالت، مثلا San Francisco, CA",
                    }
                },
                "required": ["location"],
                "additionalProperties": False,
            },
            "strict": True,
        },
    }
]

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": "هوای بوستون چطور است؟"}],
    tools=tools,
    parallel_tool_calls=False,
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

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
        "strict": True,
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="هوای بوستون چطور است؟",
    tools=tools,
    parallel_tool_calls=False,
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


### تعبیه‌سازی‌‌ها (Embeddings)

- **نرمال‌سازی بردارها**: برای مقایسه شباهت، بردارهای تعبیه‌سازی را نرمال‌سازی کنید.
- **استفاده از کاهش ابعاد**: برای تجسم، از تکنیک‌هایی مانند t-SNE یا UMAP استفاده کنید.
- **قطعه‌بندی را در نظر بگیرید**: برای اسناد طولانی، قطعه‌بندی متن به بخش‌های کوچکتر را در نظر بگیرید.

```python
import numpy as np


# نرمال‌سازی بردارها
def normalize(v):
    norm = np.linalg.norm(v)
    if norm == 0:
        return v
    return v / norm


# محاسبه شباهت کسینوسی
def cosine_similarity(a, b):
    return np.dot(a, b)
```

### تولید تصویر

- **جزئی و مشخص باشید**: پرامپت‌های دقیقی را برای نتایج بهتر تولید تصویر ارائه دهید.
- **سبک و رسانه را مشخص کنید**: اطلاعاتی در مورد سبک هنری یا رسانه مورد نظر را شامل کنید.
- **روی پرامپت‌ها تکرار کنید**: پرامپت‌ها را بر اساس نتایج تولید شده اصلاح کنید.

پرامپت خوب:
```
نقاشی دیجیتال دقیق از یک شهر آینده‌نگر در غروب آفتاب، با ماشین‌های پرنده، آسمان‌خراش‌های شیشه‌ای بلند با باغ‌ها، و تبلیغات هولوگرافیک، به سبک هنر سایبرپانک
```

پرامپت کمتر مؤثر:
```
یک شهر آینده‌نگر
```

## بهینه‌سازی هزینه

### استفاده از توکن

- **نظارت بر استفاده از توکن**: استفاده از توکن خود را پیگیری کنید تا از هزینه‌های غیرمنتظره جلوگیری کنید.
- **بهینه‌سازی طول پرامپت**: پرامپت‌ها را مختصر نگه دارید و در عین حال زمینه لازم را فراهم کنید.
- **در صورت امکان از مدل‌های کوچکتر استفاده کنید**: برای وظایف ساده‌تر، مدل‌های کوچکتر می‌توانند مقرون به صرفه‌تر باشند.
- **درخواست‌ها را دسته‌بندی کنید**: هنگام پردازش چندین ورودی، آن‌ها را در یک درخواست واحد دسته‌بندی کنید.

### کش کردن (Caching)

- **پاسخ‌ها را کش کنید**: برای درخواست‌های یکسان یا مشابه، کش کردن را برای جلوگیری از فراخوانی‌های API اضافی پیاده‌سازی کنید.
- **TTL را پیاده‌سازی کنید**: زمان مناسب برای ماندگاری (TTL) را برای پاسخ‌های کش شده بر اساس مورد استفاده خود تنظیم کنید.

```python
import hashlib
import json
from functools import lru_cache


@lru_cache(maxsize=100)
def get_embedding_cached(text, model="text-embedding-3-small"):
    # ایجاد هش از متن و مدل برای استفاده به عنوان کلید کش
    cache_key = hashlib.md5((text + model).encode()).hexdigest()

    # بررسی کنید که آیا نتیجه کش شده داریم
    # (در یک پیاده‌سازی واقعی، یک پایگاه داده یا سرویس کش را بررسی می‌کنید)

    # اگر در کش نیست، API را فراخوانی کنید
    response = client.embeddings.create(model=model, input=text)

    embedding = response.data[0].embedding

    # ذخیره در کش
    # (در یک پیاده‌سازی واقعی، در یک پایگاه داده یا سرویس کش ذخیره می‌کنید)

    return embedding
```

## ملاحظات امنیتی

### فیلتر کردن محتوا

- **فیلتر کردن محتوا را پیاده‌سازی کنید**: از نقاط پایانی نظارت برای فیلتر کردن محتوای نامناسب استفاده کنید.
- **خط‌مشی‌های استفاده مناسب را تنظیم کنید**: خط‌مشی‌های استفاده واضحی را برای برنامه خود تعریف کنید.

### حریم خصوصی داده‌های کاربر

- **به اشتراک‌گذاری داده‌ها را به حداقل برسانید**: فقط داده‌های کاربر ضروری را با API به اشتراک بگذارید.
- **به کاربران اطلاع دهید**: در مورد نحوه استفاده از داده‌های کاربر با مدل‌های هوش مصنوعی شفاف باشید.
- **خط‌مشی‌های نگهداری داده‌ها را پیاده‌سازی کنید**: خط‌مشی‌های واضحی را برای مدت زمان ذخیره داده‌های کاربر تعریف کنید.

## آزمایش و ارزیابی

### ارزیابی خروجی‌های مدل

- **معیارهای ارزیابی را تعریف کنید**: معیارهای واضحی را برای ارزیابی عملکرد مدل ایجاد کنید.
- **ارزیابی انسانی انجام دهید**: برای وظایف ذهنی، ارزیابی انسانی را شامل کنید.
- **از آزمایش خودکار استفاده کنید**: آزمایش‌های خودکار را برای ارزیابی سازگار پیاده‌سازی کنید.

### آزمایش A/B

- **نسخه‌های مدل را مقایسه کنید**: مدل‌ها یا پرامپت‌های مختلف را با کاربران واقعی آزمایش کنید.
- **معیارهای کلیدی را اندازه‌گیری کنید**: معیارهایی مانند رضایت کاربر، نرخ تکمیل وظیفه و غیره را پیگیری کنید.

## معماری برنامه

### پردازش ناهمزمان

برای وظایف طولانی‌مدت، پردازش ناهمزمان را پیاده‌سازی کنید:

```python
import asyncio
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


async def generate_response(prompt):
    response = await client.chat.completions.create(
        model="gpt-5.6-luna", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


async def process_batch(prompts):
    tasks = [generate_response(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)


# استفاده
results = asyncio.run(process_batch(["سلام", "حالت چطوره؟", "هوا چطوره؟"]))
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

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


### پاسخ‌های جریانی (Streaming)

برای تجربه کاربری بهتر، از پاسخ‌های جریانی استفاده کنید:

```python
from openai import OpenAI
import os
import sys

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": "داستانی درباره یک کاوشگر فضایی بنویس"}],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content:
        sys.stdout.write(chunk.choices[0].delta.content)
        sys.stdout.flush()
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

stream = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="داستانی درباره یک کاوشگر فضایی بنویس",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        sys.stdout.write(event.delta)
        sys.stdout.flush()
    elif event.type == "response.completed":
        break
    elif event.type in {"response.failed", "error"}:
        raise RuntimeError(event)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## دریافت کمک با استفاده از مستندات

**💡 نکته کاربردی:** می‌توانید آدرس هر صفحه از مستندات docs.avalai.ir را کپی کرده و مستقیما در پیام خود در [chat.avalai.ir](https://chat.avalai.ir) (پلتفرم چت AvalAI) قرار دهید. وقتی آدرس مستندات را در پیام خود وارد می‌کنید، مدل‌های هوش مصنوعی می‌توانند به محتوای آن صفحه دسترسی داشته باشند و به شما کمک کنند:

- از هر مدلی بخواهید بخش‌های خاص مستندات را توضیح دهد
- در رفع اشکال با استفاده از مستندات مربوطه کمک بگیرید
- نمونه‌های پیاده‌سازی بر اساس مستندات درخواست کنید
- مفاهیم پیچیده را با پرسش و پاسخ تعاملی روشن کنید

کافیست آدرس صفحه مستندات را همراه با سؤال خود در پیام چت وارد کنید و مدل آن مستندات را دریافت کرده و برای کمک به شما استفاده می‌کند. این امکان با ترکیب مستندات جامع ما با کمک هوش مصنوعی، اشکال‌زدایی و پیاده‌سازی سریع‌تر را فراهم می‌کند.

## نتیجه‌گیری

پیروی از این بهترین شیوه‌ها به شما کمک می‌کند تا برنامه‌های مؤثرتر، کارآمدتر و ایمن‌تری با API AvalAI بسازید. با کسب تجربه در پلتفرم، شیوه‌های اضافی متناسب با موارد استفاده خاص خود را توسعه خواهید داد.

به یاد داشته باشید که حوزه هوش مصنوعی به سرعت در حال تحول است، بنابراین به‌روز ماندن با آخرین مدل‌ها، تکنیک‌ها و بهترین شیوه‌ها برای نتایج بهینه ضروری است.
