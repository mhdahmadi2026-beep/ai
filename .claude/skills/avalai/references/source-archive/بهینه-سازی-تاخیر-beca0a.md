# بهینه‌سازی تاخیر

این راهنما اصول اساسی بهبود تاخیر در انواع مختلف کاربردهای مرتبط با LLM را پوشش می‌دهد. این تکنیک‌ها از همکاری با طیف وسیعی از مشتریان و توسعه‌دهندگان در برنامه‌های عملیاتی به دست آمده است.

## هفت اصل برای بهینه‌سازی تاخیر

1. [پردازش سریع‌تر توکن‌ها](#پردازش-سریعتر-توکنها)
2. [تولید توکن‌های کمتر](#تولید-توکنهای-کمتر)
3. [استفاده از توکن‌های ورودی کمتر](#استفاده-از-توکنهای-ورودی-کمتر)
4. [ارسال درخواست‌های کمتر](#ارسال-درخواستهای-کمتر)
5. [موازی‌سازی](#موازیسازی)
6. [کاهش زمان انتظار کاربران](#کاهش-زمان-انتظار-کاربران)
7. [عدم استفاده پیش‌فرض از LLM](#عدم-استفاده-پیشفرض-از-llm)

## چک‌لیست کاهش latency در AvalAI

قبل از بازنویسی یک integration فعال، این موارد را بررسی کنید:

| اهرم | چه زمانی استفاده کنیم | راهنمای AvalAI |
| --- | --- | --- |
| مدل کوچک‌تر | کار محدود، تکراری یا قابل‌راستی‌آزمایی است | قبل از ارسال همه مراحل به مدل پرچم‌دار، `gpt-5.4-mini`، `gpt-5.4-nano` یا یک مدل سریع provider-specific را امتحان کنید. |
| بودجه خروجی | پاسخ می‌تواند کوتاه یا ساختاریافته باشد | در `/v1/responses` از `text.verbosity` و `max_output_tokens` استفاده کنید؛ در `/v1/chat/completions` از `max_completion_tokens` استفاده کنید؛ `max_tokens` را فقط برای مثال‌های قدیمی نگه دارید. |
| تلاش استدلالی | مدل reasoning زمان زیادی صرف تفکر می‌کند | GPT-5.5 به‌صورت پیش‌فرض `medium` است؛ قبل از `none` مقدار `low` را تست کنید و فقط وقتی evalها بهبود کیفیت را ثابت کردند به `high`/`xhigh` بروید. |
| کش پرامپت | درخواست‌های زیادی instruction، schema یا prefix مشترک دارند | متن مشترک را در ابتدای prompt بگذارید، بخش‌های پویا را عقب‌تر ببرید، و `prompt_cache_key` را فقط وقتی route/model پشتیبانی می‌کند بفرستید. |
| سطح سرویس | بین هزینه و سرعت انتخاب می‌کنید | برای فراخوانی‌های production حساس به latency از `service_tier: "default"` استفاده کنید. `flex` را فقط برای jobهای حساس به هزینه و قابل‌تحمل نسبت به کندی یا کمبود ظرفیت به‌کار ببرید. |
| Streaming | کاربر می‌تواند خروجی جزئی را مصرف کند | برای کاهش time-to-first-token و نمایش پیشرفت واقعی، پاسخ را stream کنید. |

هم **زمان رسیدن اولین token** و هم **زمان رسیدن آخرین token** را اندازه‌گیری کنید. تغییری که latency تکمیل کامل را کم می‌کند، اگر UI stream یا progress نشان ندهد، هنوز ممکن است برای کاربر کند به نظر برسد.

برای GPT-5.5 و مدل‌های OpenAI دارای reasoning، انتخاب مدل، `reasoning.effort` و `text.verbosity` را knobهای جدا بدانید. درخواست با reasoning بالا و پاسخ نهایی کوتاه می‌تواند مفید باشد، اما همچنان توکن reasoning پنهان و زمان بیشتری مصرف می‌کند. برای baseline کیفیت از `medium` شروع کنید، برای flowهای تعاملی `low` را مقایسه کنید، و `none` را برای classification، retrieval یا formatting ساده بدون برنامه‌ریزی چندمرحله‌ای نگه دارید.

برای بیشتر برنامه‌های AvalAI به این ترتیب بهینه‌سازی کنید:

1. **اول توکن‌های خروجی را کم کنید.** خروجی قابل‌مشاهده و توکن‌های reasoning معمولا بیش از توکن‌های prompt روی latency اثر می‌گذارند.
2. **کوچک‌ترین مدلی را استفاده کنید که evalهای شما را پاس می‌کند.** قبل از فرستادن همه گام‌ها به مدل پرچم‌دار، instruction روشن‌تر، few-shot example یا fine-tuning را امتحان کنید.
3. **فراخوانی‌های مستقل را ترکیب یا موازی کنید.** round tripهای متوالی API مستقیما تاخیر قابل‌مشاهده برای کاربر ایجاد می‌کنند.
4. **prefixهای ثابت را cache-friendly کنید.** instruction مشترک، schema ابزارها و متن policy را اول بگذارید؛ snippetهای RAG و state پویا را عقب‌تر بیاورید.
5. **وقتی کد deterministic بهتر است، از LLM استفاده نکنید.** confirmationها را hard-code کنید، lookupهای ساده را با search/filtering معمولی انجام دهید و داده ساختاریافته را با UI component نشان دهید، نه prose تولیدشده.

## قبل از بهینه‌سازی اندازه‌گیری کنید

قبل از تغییر prompt یا مدل، یک trace پایه ثبت کنید. برای هر درخواست این موارد را log کنید:

- `avalai-request-id`، endpoint، provider، مدل، service tier و اینکه درخواست stream شده یا نه؛
- زمان رسیدن اولین byte، زمان رسیدن اولین token و زمان رسیدن آخرین token؛
- input tokens، output tokens، reasoning tokens و cached-tokenها وقتی در دسترس‌اند؛
- تعداد retry، خطاهای rate limit، provider fallback و status نهایی؛
- زمان انتظار قابل‌مشاهده برای کاربر، شامل queueing، retrieval، rendering و buffering سمت کلاینت.

سپس هر بار فقط یک بهینه‌سازی را مقایسه کنید. مدل کوچک‌تر ممکن است final-token latency را کم کند، در حالی که streaming latency ادراک‌شده را بدون کاهش زمان کل compute بهتر می‌کند. هر دو مفیدند، اما جداگانه اندازه‌گیری‌شان کنید.

## نقشه bottleneck به اهرم بهینه‌سازی

قبل از تغییر prompt، از trace پایه استفاده کنید تا کندترین لایه را پیدا کنید. این کار باعث می‌شود بهینه‌سازی latency متمرکز بماند و وقتی مشکل اصلی retrieval، rendering یا orchestration متوالی است، بی‌دلیل مدل را عوض نکنید.

| bottleneck | نشانه رایج | اولین اهرم در AvalAI |
| --- | --- | --- |
| compute مدل کند است | زمان final-token طولانی، تعداد reasoning-token بالا یا استفاده از مدل پرچم‌دار برای کار ساده | مدل کوچک‌تر را امتحان کنید، `reasoning.effort` را پایین بیاورید یا classification ساده را از generation سخت جدا کنید. |
| خروجی خیلی طولانی است | output token بالا یا JSON/آرگومان‌های function طولانی | `text.verbosity` را کم کنید، `max_output_tokens`/`max_completion_tokens` را محدود کنید، نام فیلدها را کوتاه کنید یا به‌جای prose، ID ساختاریافته برگردانید. |
| prompt خیلی بزرگ است | input token بالا همراه با `cached_tokens` پایین | context مربوط به RAG را کوتاه کنید، HTML را پاک‌سازی کنید، prefix ثابت را اول بگذارید و `prompt_cache_key` را فقط وقتی route پشتیبانی می‌کند اضافه کنید. |
| round tripها زیادند | چند `avalai-request-id` متوالی برای یک action کاربر | مراحل را در یک پاسخ ساختاریافته ترکیب کنید، فراخوانی‌های مستقل را موازی کنید یا برای branchهای احتمالا امن speculative execution به‌کار ببرید. |
| UI خالی به نظر می‌رسد | time-to-first-token کند یا نبود progress هنگام tool/retrieval | پاسخ را stream کنید، مراحل tool/retrieval را نشان دهید و post-processing سمت backend را قبل از ارسال به UI به chunk تبدیل کنید. |
| LLM لازم نیست | خروجی محدود و تکراری در درخواست‌های مشابه | confirmationها را hard-code کنید، variantها را precompute کنید، از search/filtering استفاده کنید یا metricها را با UI component نمایش دهید. |

## پردازش سریع‌تر توکن‌ها

**سرعت استنتاج** به نرخ پردازش توکن‌ها توسط LLM اشاره دارد که اغلب با توکن در دقیقه (TPM) یا توکن در ثانیه (TPS) اندازه‌گیری می‌شود.

عامل اصلی تاثیرگذار بر سرعت استنتاج **اندازه مدل** است – مدل‌های کوچکتر معمولا سریع‌تر اجرا می‌شوند (و ارزان‌تر هستند)، و در صورت استفاده صحیح می‌توانند حتی از مدل‌های بزرگتر عملکرد بهتری داشته باشند. برای حفظ کیفیت بالای عملکرد با مدل‌های کوچکتر:

* از پرامپت طولانی‌تر و با جزئیات بیشتر استفاده کنید
* مثال‌های few-shot بیشتری اضافه کنید
* fine-tuning / distillation را در نظر بگیرید

به عنوان مثال، می‌توانید از `gpt-5.4-mini` یا `claude-haiku-4-5` برای پاسخ‌های سریع‌تر استفاده کنید، زمانی که برای کار مناسب هستند.

Predicted Outputs هم زمانی می‌تواند زمان inference را کاهش دهد که بخش بزرگی از پاسخ متنی از قبل مشخص است؛ مثلا ویرایش فایل. وقتی می‌توانید draft نزدیک به خروجی مورد انتظار بدهید، راهنمای [خروجی‌های پیش‌بینی‌شده](fa/guides/predicted-outputs.md) را ببینید.

```python
# استفاده از مدل کوچکتر با پرامپت دقیق‌تر
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "system",
            "content": "شما یک دستیار مفید هستید که پاسخ‌های مختصر و دقیق ارائه می‌دهد.",
        },
        {
            "role": "user",
            "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید، با تمرکز بر کیوبیت‌ها و برهم‌نهی. یک تشبیه که درک آن را آسان کند، ارائه دهید.",
        },
    ],
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

response = client.responses.create(
    model="gpt-5.4-mini",
    instructions="You are a helpful assistant.",
    input="محاسبات کوانتومی را به زبان ساده توضیح دهید، با تمرکز بر کیوبیت‌ها و برهم‌نهی. یک تشبیه که درک آن را آسان کند، ارائه دهید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## تولید توکن‌های کمتر

تولید توکن‌ها معمولا مرحله با بیشترین تاخیر هنگام استفاده از LLM است. به عنوان یک قاعده کلی، **کاهش ۵۰٪ از توکن‌های خروجی می‌تواند تاخیر را حدود ۵۰٪ کاهش دهد**. در مدل‌های reasoning، توکن‌های reasoning پنهان هم بودجه خروجی و زمان مصرف می‌کنند، حتی اگر به کاربر نمایش داده نشوند.

برای کاهش اندازه خروجی:

* برای **زبان طبیعی**، از مدل بخواهید مختصر باشد ("زیر ۲۰ کلمه" یا "بسیار مختصر باشید")
* برای **خروجی ساختاریافته**، نحو خروجی خود را به حداقل برسانید: نام توابع را کوتاه کنید، آرگومان‌های نام‌دار را حذف کنید، پارامترها را ادغام کنید
* در `/v1/responses` از `max_output_tokens`، در `/v1/chat/completions` از `max_completion_tokens`، یا در صورت پشتیبانی از `stop`/stop sequence برای پایان دادن زودهنگام به تولید استفاده کنید

در JSONهای میانی حساس به latency، هر نام فیلد بخشی از خروجی است. قراردادهای
API عمومی را خوانا نگه دارید، اما برای فیلدهای داخلی reasoning یا routing از
نام‌های کوتاه‌تر استفاده کنید: `message_is_conversation_continuation` می‌تواند
`cont` شود، `response_requirements` می‌تواند `reqs` شود، و توضیح‌ها به‌جای
تولید در هر پاسخ داخل prompt یا کامنت schema قرار بگیرند. قبل از استفاده از
schema فشرده در قرارداد customer-facing، آن را با eval اعتبارسنجی کنید.

```python
# درخواست پاسخ مختصر
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "system",
            "content": "شما یک دستیار مفید هستید که پاسخ‌های بسیار مختصر، زیر ۵۰ کلمه ارائه می‌دهد.",
        },
        {"role": "user", "content": "نظریه نسبیت را توضیح دهید"},
    ],
    max_completion_tokens=100,
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

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="شما یک دستیار مفید هستید که پاسخ‌های بسیار مختصر، زیر ۵۰ کلمه ارائه می‌دهد.",
    input="نظریه نسبیت را توضیح دهید",
    max_output_tokens=100,
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## استفاده از توکن‌های ورودی کمتر

اگرچه کاهش توکن‌های ورودی منجر به کاهش تاخیر می‌شود، اما تاثیر آن کمتر قابل توجه است – **کاهش ۵۰٪ از پرامپت شما ممکن است تنها منجر به بهبود ۱-۵٪ در تاخیر شود**. این تکنیک‌ها را هنگام کار با متن‌های بزرگ در نظر بگیرید:

* fine-tuning مدل برای جایگزینی دستورالعمل‌ها/مثال‌های طولانی
* فیلتر کردن متن ورودی (هرس نتایج RAG، پاکسازی HTML)
* به حداکثر رساندن پیشوند مشترک پرامپت با قرار دادن بخش‌های پویا در انتهای پرامپت

برای ترافیک production تکراری، prefix پایدار معمولا از حذف وسواس‌گونه چند کلمه مهم‌تر است. دستورالعمل‌های ثابت، JSON schema و متن policy را قبل از تاریخچه گفتگو یا snippetهای retrieval قرار دهید تا caching سمت provider بتواند prefix را دوباره استفاده کند. اگر route پشتیبانی می‌کند، برای هر workload یا پیکربندی assistant یک `prompt_cache_key` پایدار بفرستید؛ شناسه خام کاربر را cache key نکنید.

```python
# مثالی از فیلتر کردن متن ورودی
def filter_relevant_context(query, documents, max_tokens=2000):
    # مرتب‌سازی اسناد بر اساس ارتباط با پرسش
    sorted_docs = sort_by_relevance(query, documents)

    # انتخاب فقط مرتبط‌ترین اسناد تا حداکثر توکن مشخص شده
    filtered_docs = []
    token_count = 0

    for doc in sorted_docs:
        doc_tokens = count_tokens(doc)
        if token_count + doc_tokens <= max_tokens:
            filtered_docs.append(doc)
            token_count += doc_tokens
        else:
            break

    return filtered_docs
```

## ارسال درخواست‌های کمتر

هر درخواست API تاخیر رفت و برگشت ایجاد می‌کند. به جای درخواست‌های متوالی، ترکیب چندین مرحله در یک پرامپت واحد را در نظر بگیرید:

```python
# به جای درخواست‌های جداگانه برای خلاصه‌سازی و ترجمه
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "system",
            "content": "شما دو وظیفه انجام خواهید داد: ۱) خلاصه کردن متن، و ۲) ترجمه خلاصه به اسپانیایی. نتایج را در قالب JSON با فیلدهای 'summary' و 'translation' برگردانید.",
        },
        {"role": "user", "content": "متن برای پردازش: " + long_article},
    ],
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

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="شما دو وظیفه انجام خواهید داد: ۱) خلاصه کردن متن، و ۲) ترجمه خلاصه به اسپانیایی. نتایج را در قالب JSON با فیلدهای 'summary' و 'translation' برگردانید.",
    input="متن برای پردازش: " + long_article,
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## موازی‌سازی

برای مراحل غیر متوالی، فراخوانی‌های API را موازی کنید:

در production، parallelism را با محدودیت concurrency و retry همراه کنید. Tierهای rate limit در AvalAI بر اساس مدل و endpoint متفاوت‌اند؛ بنابراین parallelism محدود امن‌تر از اجرای همزمان همه سندهاست. برای کارهای آفلاین، وقتی throughput از latency تعاملی مهم‌تر است، Batch API را در نظر بگیرید.

```python
import asyncio
import os
from openai import AsyncOpenAI


async def process_documents(documents):
    client = AsyncOpenAI(
        api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
    )

    async def process_document(doc):
        response = await client.chat.completions.create(
            model="gpt-5.4-mini",
            messages=[
                {"role": "system", "content": "سند زیر را خلاصه کنید:"},
                {"role": "user", "content": doc},
            ],
        )
        return response.choices[0].message.content

    # پردازش همه اسناد به صورت موازی
    tasks = [process_document(doc) for doc in documents]
    return await asyncio.gather(*tasks)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import asyncio
import os
from openai import AsyncOpenAI


async def process_documents(documents):
    client = AsyncOpenAI(
        api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
    )

    async def process_document(doc):
        response = await client.responses.create(
            model="gpt-5.4-mini",
            instructions="سند زیر را خلاصه کنید:",
            input=doc,
        )
        return response.output_text

    tasks = [process_document(doc) for doc in documents]
    return await asyncio.gather(*tasks)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای مراحل متوالی، اجرای حدسی را در نظر بگیرید، به ویژه زمانی که یک نتیجه محتمل‌تر است:

1. مرحله 1 و مرحله 2 را همزمان شروع کنید (مثلا، بررسی محتوای ورودی و تولید داستان)
2. نتیجه مرحله 1 را تایید کنید
3. اگر نتیجه مطابق انتظار نبود، مرحله 2 را لغو کنید (و در صورت لزوم دوباره تلاش کنید)

در production، هنگام استفاده از speculative execution هر دو request ID را ثبت
کنید و مسیر cancel/discard را صریح نگه دارید. مثلا اگر درخواست moderation
ورودی fail شد، generation از قبل شروع‌شده را discard کنید، آن را برای کاربر
stream نکنید و tokenهای هدررفته را در dashboard هزینه حساب کنید.

## کاهش زمان انتظار کاربران

تفاوت بین انتظار و مشاهده پیشرفت قابل توجه است:

* **جریان‌سازی (Streaming)**: بلافاصله شروع به نمایش پاسخ در حین تولید آن کنید
* **تکه‌بندی (Chunking)**: خروجی را در تکه‌ها برای نمایش بلادرنگ پردازش کنید
* **نمایش مراحل**: فرآیندهای چند مرحله‌ای را به کاربران نشان دهید
* **حالت‌های بارگذاری**: از نشانگرهای چرخشی و نوارهای پیشرفت استفاده کنید

```python
import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

# پخش جریانی پاسخ به کاربر
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {"role": "user", "content": "یک داستان کوتاه درباره یک مسافر زمان بنویس."}
    ],
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
    input="یک داستان کوتاه درباره یک مسافر زمان بنویس.",
    stream=True,
)

for event in stream:
    if event.type == "response.output_text.delta":
        sys.stdout.write(event.delta)
        sys.stdout.flush()
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## عدم استفاده پیش‌فرض از LLM

LLM‌ها بسیار قدرتمند و همه‌کاره هستند، اما همیشه کارآمدترین راه‌حل نیستند. این جایگزین‌ها را در نظر بگیرید:

* **کدنویسی سخت (Hard-coding)**: برای خروجی‌های محدود مانند پیام‌های تایید
* **پیش‌محاسبه**: برای سناریوهای ورودی محدود
* **استفاده از رابط کاربری**: برای معیارهای خلاصه شده یا نتایج جستجو
* **بهینه‌سازی سنتی**: جستجوی دودویی، کش کردن، جداول هش و غیره

```python
# مثالی از استفاده از کش برای پرسش‌های متداول
response_cache = {}


def get_response(query):
    # بررسی وجود پاسخ در کش
    if query in response_cache:
        return response_cache[query]

    # در صورت عدم وجود، تولید پاسخ جدید
    response = client.chat.completions.create(
        model="gpt-5.6-luna", messages=[{"role": "user", "content": query}]
    )

    # ذخیره پاسخ در کش برای استفاده‌های آینده
    response_text = response.choices[0].message.content
    response_cache[query] = response_text

    return response_text
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

response_cache = {}


def get_response(query):
    if query in response_cache:
        return response_cache[query]

    response = client.responses.create(model="gpt-5.6-luna", input=query)
    response_cache[query] = response.output_text
    return response.output_text
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مثال: بهینه‌سازی یک ربات پشتیبانی مشتری

بیایید یک معماری نمونه برای ربات پشتیبانی مشتری را تحلیل کنیم و اصول بهینه‌سازی تاخیر را اعمال کنیم.

### معماری اولیه

معماری اولیه شامل موارد زیر است:
1. کاربر پیامی ارسال می‌کند
2. پیام به یک پرسش خودکفا تبدیل می‌شود
3. تعیین می‌کنیم آیا به اطلاعات اضافی نیاز است یا خیر
4. بازیابی انجام می‌شود
5. دستیار درباره پرسش و نتایج جستجو استدلال می‌کند
6. پاسخ به کاربر ارسال می‌شود

### بهینه‌سازی‌های اعمال شده

1. **ترکیب مراحل**: ادغام متن‌سازی پرسش و بررسی بازیابی برای ارسال درخواست‌های کمتر
2. **استفاده از مدل‌های کوچک‌تر**: تغییر به یک مدل کوچک‌تر یا fine-tuned برای وظایف تعریف‌شده دقیق
3. **موازی‌سازی**: اجرای همزمان بررسی‌های بازیابی و مراحل استدلال
4. **کوتاه کردن نام فیلدها**: کاهش توکن‌های خروجی با استفاده از نام‌های فیلد JSON مختصرتر

این بهینه‌سازی‌ها می‌توانند latency را کم کنند و کیفیت را حفظ کنند، اما آن‌ها را با traceهای واقعی خودتان اعتبارسنجی کنید. قبل از rollout در production، first-token latency، final-token latency، تعداد tokenهای خروجی، نرخ retry و زمان قابل‌مشاهده برای کاربر را پیگیری کنید.

## منابع مرتبط

- [مهندسی پرامپت](fa/guides/prompt-engineering)
- [کش کردن پرامپت](fa/guides/prompt-caching)
- [خروجی‌های پیش‌بینی‌شده](fa/guides/predicted-outputs)
- [شمارش توکن](fa/guides/token-counting)
- [پاسخ‌های جریانی](fa/guides/streaming-responses)
- [انتخاب مدل](fa/guides/model-selection)
