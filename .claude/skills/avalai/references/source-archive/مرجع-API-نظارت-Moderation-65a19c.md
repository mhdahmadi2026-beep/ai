# مرجع API نظارت (Moderation)

API نظارت به شما کمک می‌کند محتوای بالقوه مضر در ورودی کاربر یا خروجی مدل را شناسایی کنید. از آن برای طبقه‌بندی متن مستقل و، با `omni-moderation-latest`، ورودی‌های تصویری استفاده کنید. نتیجه را به عنوان سیگنال خط‌مشی برای فیلتر، صف بررسی، مداخله حساب یا ارجاع انسانی در نظر بگیرید، نه یک سیستم ایمنی کامل به تنهایی.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/moderations
```

## انتخاب گردش‌کار

| گردش‌کار | چه زمانی استفاده شود | endpoint یا پارامتر |
|----------|----------------------|---------------------|
| طبقه‌بندی ورودی مستقل | وقتی بدون تولید پاسخ، برای متن یا تصویر سیگنال خط‌مشی لازم دارید | `POST /v1/moderations` |
| moderation خروجی تولیدشده | وقتی هم برای درخواست و هم برای پاسخ تولیدشده امتیاز moderation لازم دارید | `moderation: {"model": "omni-moderation-latest"}` در درخواست‌های پشتیبانی‌شده `/v1/responses` یا `/v1/chat/completions` |
| بررسی و ارجاع | وقتی audit trail پایدار یا صف بررسی انسانی لازم دارید | `flagged`، `categories`، `category_scores`، `category_applied_input_types`، `request_id` و `safety_identifier` hashشده خودتان را ذخیره کنید |

## بدنه درخواست (Request Body)

| پارامتر | نوع | الزامی | توضیحات |
|-----------|------|----------|-------------|
| `input` | string، array، یا آرایه content item | بله | متنی که باید طبقه‌بندی شود. با `omni-moderation-latest`، ورودی می‌تواند شامل آیتم‌های متن و تصویر URL باشد. |
| `model` | string | خیر | مدل نظارت. مدل‌های فعلی AvalAI شامل `omni-moderation-latest`، `omni-moderation-2024-09-26`، `text-moderation-latest`، `text-moderation-stable` و `cf.llama-guard-3-8b` هستند. |

?> `omni-moderation-latest` از متن و تصویر پشتیبانی می‌کند، اما صوت را طبقه‌بندی نمی‌کند. محدودیت مرجع OpenAI برای تصویرهای moderation برابر 20 مگابایت است؛ پیش از اتکا به این سقف در production، محدودیت مسیر AvalAI و ارائه‌دهنده را بررسی کنید.

## مثال‌ها

### درخواست نظارت پایه

```bash
curl https://api.avalai.ir/v1/moderations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "omni-moderation-latest",
    "input": "می‌خواهم آن‌ها را بکشم."
}'
```

### مثال پایتون (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.moderations.create(
    model="omni-moderation-latest",
    input="می‌خواهم آن‌ها را بکشم.",
)

# بررسی اینکه آیا متن پرچم‌گذاری شده است
if response.results[0].flagged:
    print("این محتوا پرچم‌گذاری شد!")

# بررسی دسته‌بندی‌های خاص
categories = response.results[0].categories
for category, flagged in categories.items():
    if flagged:
        print(f"محتوا برای {category} پرچم‌گذاری شد")
```

### مثال جاوااسکریپت (JavaScript)

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.moderations.create({
  model: "omni-moderation-latest",
  input: "می‌خواهم آن‌ها را بکشم.",
});

// بررسی اینکه آیا متن پرچم‌گذاری شده است
if (response.results[0].flagged) {
  console.log("این محتوا پرچم‌گذاری شد!");
}

// بررسی دسته‌بندی‌های خاص
const categories = response.results[0].categories;
for (const [category, flagged] of Object.entries(categories)) {
  if (flagged) {
    console.log(`محتوا برای ${category} پرچم‌گذاری شد`);
  }
}
```

### نظارت متن و تصویر

وقتی لازم است متن و تصویر URL را در یک درخواست طبقه‌بندی کنید، از `omni-moderation-latest` استفاده کنید:

```bash
curl https://api.avalai.ir/v1/moderations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "omni-moderation-latest",
    "input": [
      { "type": "text", "text": "بررسی کن آیا این محتوا ایمن است." },
      {
        "type": "image_url",
        "image_url": {
          "url": "https://example.com/image.png"
        }
      }
    ]
  }'
```

### نظارت خروجی تولیدشده

نقاط پایانی تولید سازگار با OpenAI ممکن است از شیء سطح بالای `moderation` پشتیبانی کنند تا امتیازهای نظارت ورودی مدل و خروجی تولیدشده را کنار پاسخ برگردانند. وقتی پشتیبانی AvalAI برای route انتخابی شما فعال باشد، `moderation: {"model": "omni-moderation-latest"}` را به `/v1/responses` یا `/v1/chat/completions` بفرستید؛ در غیر این صورت، پیش و/یا پس از تولید، `/v1/moderations` را جداگانه فراخوانی کنید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="یک کاربر درخواست دستورالعمل آسیب‌زا دارد. کوتاه رد کن و مسیر امن پیشنهاد بده.",
    moderation={"model": "omni-moderation-latest"},
)

input_moderation = response.moderation.input
output_moderation = response.moderation.output

print(input_moderation.flagged)
print(output_moderation.flagged)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input:
    "یک کاربر درخواست دستورالعمل آسیب‌زا دارد. کوتاه رد کن و مسیر امن پیشنهاد بده.",
  moderation: { model: "omni-moderation-latest" },
});

console.log(response.moderation.input.flagged);
console.log(response.moderation.output.flagged);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "یک کاربر درخواست دستورالعمل آسیب‌زا دارد. کوتاه رد کن و مسیر امن پیشنهاد بده.",
    "moderation": { "model": "omni-moderation-latest" }
  }'

```


?> نتایج inline moderation را پیش از نمایش متن تولیدشده به کاربر بررسی کنید. در پاسخ‌های streamشده، امتیازهای moderation پس از کامل شدن کل خروجی آماده می‌شوند، نه همراه deltaهای جزئی.

### چند ورودی در یک درخواست

می‌توانید چند متن مستقل را در یک درخواست `/v1/moderations` بررسی کنید. این الگو با API ناهمگام `/v1/batch` متفاوت است.

```python
response = client.moderations.create(
    model="omni-moderation-latest",
    input=[
        "می‌خواهم آن‌ها را بکشم.",
        "امروز هوا خوب است.",
        "قصد دارم به خودم آسیب بزنم.",
    ],
)

# پردازش هر نتیجه
for i, result in enumerate(response.results):
    print(f"متن {i+1}: {'پرچم‌گذاری شده' if result.flagged else 'پرچم‌گذاری نشده'}")
```

## فرمت پاسخ (Response Format)

```json
{
  "id": "modr-5MWoLO",
  "model": "omni-moderation-latest",
  "results": [
    {
      "flagged": true,
      "categories": {
        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "illicit": false,
        "illicit/violent": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": false,
        "violence": true
      },
      "category_scores": {
        "sexual": 3.6988e-06,
        "hate": 0.0034766977,
        "harassment": 0.0124246953,
        "self-harm": 2.0235e-06,
        "illicit": 0.0005227032,
        "illicit/violent": 3.682979e-07,
        "sexual/minors": 3.01e-08,
        "hate/threatening": 0.0017639078,
        "violence/graphic": 2.49108e-05,
        "self-harm/intent": 5.447e-07,
        "self-harm/instructions": 8.4e-09,
        "harassment/threatening": 0.0058918546,
        "violence": 0.9223177433
      },
      "category_applied_input_types": {
        "sexual": [
          "text"
        ],
        "hate": [
          "text"
        ],
        "harassment": [
          "text"
        ],
        "self-harm": [
          "text"
        ],
        "illicit": [
          "text"
        ],
        "illicit/violent": [
          "text"
        ],
        "sexual/minors": [
          "text"
        ],
        "hate/threatening": [
          "text"
        ],
        "violence/graphic": [
          "text"
        ],
        "self-harm/intent": [
          "text"
        ],
        "self-harm/instructions": [
          "text"
        ],
        "harassment/threatening": [
          "text"
        ],
        "violence": [
          "text"
        ]
      }
    }
  ]
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر | نوع | توضیحات |
|-----------|------|-------------|
| `id` | string | شناسه منحصر به فرد برای درخواست نظارت. |
| `model` | string | مدلی که برای نظارت محتوا استفاده شده است. |
| `results` | array | آرایه‌ای از نتایج نظارت، یکی برای هر ورودی. |

### شی نتیجه نظارت (Moderation Result Object)

| پارامتر | نوع | توضیحات |
|-----------|------|-------------|
| `flagged` | boolean | آیا مدل محتوا را بالقوه مضر طبقه‌بندی کرده است. این فیلد را به عنوان سیگنال اولیه استفاده کنید. |
| `categories` | object | پرچم‌های بولی به ازای هر دسته‌بندی. از آن‌ها برای مسیریابی، لاگ، ارجاع و تصمیم‌های بررسی استفاده کنید. |
| `category_scores` | object | امتیاز اطمینان هر دسته‌بندی از 0 تا 1. آستانه‌های سفارشی ممکن است با ارتقای مدل‌ها نیاز به تنظیم دوباره داشته باشند. |
| `category_applied_input_types` | object | نوع ورودی که هر امتیاز دسته‌بندی به آن اعمال شده است، مثل `text` یا `image`. |

### دسته‌بندی‌ها (Categories)

| دسته‌بندی | توضیحات | ورودی‌ها |
|----------|-------------|----------|
| `sexual` | محتوایی با هدف برانگیختگی جنسی یا ترویج خدمات جنسی، به جز زمینه‌های آموزشی یا سلامت | متن و تصویر |
| `sexual/minors` | محتوای جنسی شامل فرد زیر 18 سال | فقط متن |
| `hate` | محتوایی که نفرت بر اساس هویت محافظت‌شده را بیان، تحریک یا ترویج می‌کند | فقط متن |
| `hate/threatening` | محتوای نفرت‌انگیز که شامل خشونت یا آسیب جدی علیه گروه هدف است | فقط متن |
| `harassment` | محتوایی که زبان آزاردهنده علیه یک هدف را بیان یا ترویج می‌کند | فقط متن |
| `harassment/threatening` | آزار که شامل خشونت یا آسیب جدی است | فقط متن |
| `illicit` | دستورالعمل، راهنمایی یا تسهیل ارتکاب اعمال غیرقانونی | فقط متن |
| `illicit/violent` | محتوای غیرقانونی که با خشونت یا سلاح نیز مرتبط است | فقط متن |
| `self-harm` | محتوایی که خودآزاری را ترویج، تشویق یا تصویر می‌کند | متن و تصویر |
| `self-harm/intent` | محتوایی که گوینده در آن قصد خودآزاری را بیان می‌کند | متن و تصویر |
| `self-harm/instructions` | دستورالعمل یا تشویق برای خودآزاری | متن و تصویر |
| `violence` | محتوایی که مرگ، خشونت یا آسیب فیزیکی را نشان می‌دهد | متن و تصویر |
| `violence/graphic` | تصویرسازی گرافیکی مرگ، خشونت یا آسیب فیزیکی | متن و تصویر |

## مدل‌های موجود

| مدل | توضیحات | قیمت‌گذاری |
|-------|-------------|---------|
| `omni-moderation-latest` | جدیدترین مدل OpenAI برای نظارت متن و تصویر | رایگان |
| `omni-moderation-2024-09-26` | snapshot ثابت مدل omni moderation شرکت OpenAI | رایگان |
| `text-moderation-latest` | alias جدید متن‌محور OpenAI برای moderation | رایگان |
| `text-moderation-stable` | alias پایدار متن‌محور OpenAI برای moderation | رایگان |
| `cf.llama-guard-3-8b` | مدل Llama Guard میزبانی‌شده روی Cloudflare برای moderation | صفحه قیمت‌گذاری را ببینید |

## بهترین شیوه‌های پیاده‌سازی

### فیلتر کردن محتوا

یک رویکرد لایه‌ای برای فیلتر کردن محتوا پیاده‌سازی کنید:

1. **فیلتر قبل از ارسال**: فیلترهای سمت کلاینت را قبل از ارسال محتوا به API اعمال کنید
2. **نظارت API**: از API نظارت برای تشخیص دقیق‌تر استفاده کنید
3. **بررسی انسانی**: برای موارد مرزی، فرآیندهای بررسی انسانی را پیاده‌سازی کنید

### آستانه‌های دسته‌بندی

آستانه‌های امتیاز دسته‌بندی را بر اساس الزامات برنامه خود سفارشی کنید:

```python
def is_content_allowed(result, custom_thresholds=None):
    thresholds = {
        "sexual": 0.5,
        "hate": 0.5,
        "harassment": 0.5,
        "self-harm": 0.5,
        "illicit": 0.5,
        "illicit/violent": 0.5,
        "sexual/minors": 0.1,  # آستانه سخت‌گیرانه‌تر
        "hate/threatening": 0.5,
        "violence/graphic": 0.5,
        "self-harm/intent": 0.5,
        "self-harm/instructions": 0.5,
        "harassment/threatening": 0.5,
        "violence": 0.5,
    }

    if custom_thresholds:
        thresholds.update(custom_thresholds)

    scores = result.category_scores
    if hasattr(scores, "model_dump"):
        scores = scores.model_dump()

    for category, threshold in thresholds.items():
        if scores.get(category, 0) >= threshold:
            return False

    return True
```

### مرزهای Moderation

- در درخواست‌های tool calling، moderation می‌تواند argumentهای tool call و خروجی tool را وقتی در محتوای گفتگو آمده‌اند پوشش دهد.
- moderation نام tool، توضیحات tool، schemaهای tool یا schemaهای response format را بررسی نمی‌کند.
- در generation به صورت stream، deltaهای جزئی را تا رسیدن نتیجه نهایی moderation، moderationنشده در نظر بگیرید.
- inline moderation ممکن است برای مرحله input یا output یک شیء خطا برگرداند؛ در production پیش از خواندن category score نوع نتیجه را بررسی کنید.

### مدیریت مثبت کاذب (False Positives)

برای کاهش مثبت کاذب، موارد زیر را در نظر بگیرید:

1. استفاده از امتیازات دسته‌بندی به جای فقط فیلد `flagged`
2. پیاده‌سازی بررسی ثانویه برای موارد مرزی
3. نگهداری یک لیست مجاز برای محتوای امن شناخته شده که ممکن است پرچم‌گذاری شود

### پردازش چندورودی

برای کارایی، چندین مورد محتوا را در یک درخواست واحد دسته‌بندی کنید:

```python
def moderate_batch(texts, batch_size=25):
    results = []

    # پردازش در دسته‌ها برای جلوگیری از رسیدن به محدودیت‌های درخواست
    for i in range(0, len(texts), batch_size):
        batch = texts[i : i + batch_size]
        response = client.moderations.create(
            model="omni-moderation-latest",
            input=batch,
        )
        results.extend(response.results)

    return results
```

برای صف‌های آفلاین بزرگ، فقط زمانی از [Batch API](fa/api-reference/batch.md) ناهمگام استفاده کنید که `/v1/moderations` برای حساب و workload شما فعال باشد.

## مدیریت خطا (Error Handling)

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات |
|-------------|-------------|
| 400 | درخواست بد - درخواست شما نامعتبر است. |
| 401 | غیرمجاز - کلید API شما اشتباه است. |
| 403 | ممنوع - شما اجازه دسترسی به این منبع را ندارید. |
| 404 | یافت نشد - منبع مشخص شده یافت نشد. |
| 429 | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید. |
| 500 | خطای داخلی سرور - مشکلی در سرور ما وجود داشت. |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## ملاحظات خط‌مشی محتوا

هنگام پیاده‌سازی نظارت محتوا، موارد زیر را در نظر بگیرید:

1. **شفافیت**: کاربران را در مورد خط‌مشی‌های نظارت محتوای خود مطلع کنید
2. **فرآیند تجدیدنظر**: راهی برای کاربران فراهم کنید تا نسبت به تصمیمات نظارت اعتراض کنند
3. **زمینه فرهنگی**: آگاه باشید که نظارت محتوا ممکن است در فرهنگ‌ها و مناطق مختلف متفاوت باشد
4. **به‌روزرسانی‌های منظم**: سیستم‌های نظارت خود را با تکامل زبان به‌روز نگه دارید

## منابع مرتبط

- [مدل‌ها](fa/models/model-details.md) - درباره مدل‌های نظارت موجود بیاموزید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
