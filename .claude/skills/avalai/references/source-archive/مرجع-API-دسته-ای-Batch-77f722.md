# مرجع API دسته‌ای (Batch)

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. برای workloadهای دسته‌ای فعلی، از [راهنمای پردازش دسته‌ای](fa/guides/batch-processing.md) و [درخواست‌های موازی سازگار با Rate Limit](fa/examples/rate_limit_safe_parallel_requests.md) استفاده کنید.

دسته‌های بزرگی از درخواست‌های API را برای پردازش ناهمزمان ایجاد کنید. الگوی OpenAI-compatible برای Batch API خروجی‌ها را در بازه ۲۴ ساعته برمی‌گرداند و برای کارهای آفلاین مناسب است که می‌توانند منتظر تکمیل ناهمزمان بمانند.

?> Batch API میزبانی‌شده در OpenAI برای حساب‌های OpenAI تخفیف ۵۰٪ و یک pool جدا با محدودیت بالاتر اعلام می‌کند. این شرایط تجاری مربوط به میزبانی OpenAI است و تا وقتی `/v1/batches` در AvalAI فعال و مستند نشده، تضمین AvalAI محسوب نمی‌شود. تا آن زمان، workerهای دسته‌ای سمت کلاینت از قیمت‌گذاری و محدودیت نرخ مسیر/مدل عادی AvalAI استفاده می‌کنند.

راهنمای مرتبط: [راهنمای پردازش دسته‌ای](fa/guides/batch-processing.md)

مثال‌های مرتبط:

- [درخواست‌های موازی سازگار با Rate Limit](fa/examples/rate_limit_safe_parallel_requests.md)
- [ارزیابی با Promptfoo و AvalAI](fa/examples/promptfoo_evals_with_avalai.md)

## گردش کار OpenAI-compatible

وقتی این endpoint در AvalAI فعال شود، از همان چرخه Batch API در OpenAI استفاده کنید:

1. یک فایل `.jsonl` با یک درخواست در هر خط آماده کنید.
2. فایل را با `purpose="batch"` از طریق [Files API](fa/api-reference/files.md) آپلود کنید.
3. با `input_file_id`، `endpoint` و `completion_window` یک batch بسازید.
4. شی batch را poll کنید تا به `completed`، `failed`، `expired` یا `cancelled` برسد.
5. `output_file_id` را برای ردیف‌های موفق دانلود کنید و `error_file_id` را برای ردیف‌های ناموفق یا منقضی‌شده بررسی کنید.

از `custom_id`های پایدار استفاده کنید، چون ترتیب ردیف‌های خروجی ممکن است با ترتیب ورودی یکی نباشد.

### محدودیت‌های برنامه‌ریزی

- هر فایل ورودی JSONL را به یک `endpoint` و یک `model` محدود کنید.
- مقدارهای `custom_id` باید یکتا باشند؛ ردیف‌های خروجی را با `custom_id` به ورودی وصل کنید، نه با شماره خط.
- مقدار `stream: true` نگذارید؛ خروجی batch در فایل‌های output و error نوشته می‌شود.
- محدودیت مرجع OpenAI برابر ۵۰٬۰۰۰ درخواست برای هر batch و ۲۰۰ مگابایت برای هر فایل ورودی است؛ محدودیت AvalAI در زمان rollout ممکن است کمتر باشد.
- تا وقتی AvalAI این موارد را برای `/v1/batches` مستند نکرده، تخفیف Batch، سیاست نگه‌داری فایل یا pool جداگانه محدودیت نرخ OpenAI را برای AvalAI فرض نکنید.
- برای `/v1/moderations` در هر ردیف `input` بگذارید. در moderation چندوجهی، برای کوچک ماندن JSONL از `image_url` به جای payloadهای بزرگ base64 استفاده کنید.
- برای `/v1/videos` روی بدنه JSON برنامه‌ریزی کنید: assetها را از قبل upload کنید و به جای multipart upload با file ID یا image URL پشتیبانی‌شده به آن‌ها ارجاع دهید.

### برنامه‌ریزی وضعیت و callback

AvalAI در حال حاضر webhook میزبانی‌شده برای Batch ارائه نمی‌کند. اگر قبل از فعال شدن `/v1/batches` به اعلان تکمیل نیاز دارید، job را از طریق worker خودتان اجرا کنید و بعد از ذخیره نتیجه‌ها webhook برنامه خودتان را ارسال کنید. برای idempotency از شناسه event پایدار استفاده کنید، payloadهای callback را با secret امضا کنید، و receiverها را طوری طراحی کنید که قبل از انجام کار سنگین سریع با `2xx` تأیید کنند. برای الگوی receiver، [Webhookها](/fa/guides/webhooks.md) را ببینید.

Responses در حالت background در OpenAI یک الگوی async جدا برای یک پاسخ طولانی است، نه جایگزین ردیف‌های Batch. اگر AvalAI در آینده background Responses را ارائه کند، انتظار داشته باشید شی Response را تا خروج از وضعیت‌های `queued` یا `in_progress` poll کنید؛ تا آن زمان، این رفتار را در جدول job خودتان مدل کنید.

### راهنمای عملی وضعیت‌های Batch

وضعیت‌ها را فقط label نمایشی ندانید؛ آن‌ها stateهای workflow هستند:

| وضعیت | معنی | برنامه شما چه کند |
| --- | --- | --- |
| `validating` | فایل ورودی پیش از شروع اجرا بررسی می‌شود. | با backoff به polling ادامه دهید؛ پیشرفت validation را فقط به operatorها نشان دهید. |
| `failed` | فایل ورودی validation را پاس نکرده است. | retry همان فایل را متوقف کنید، `errors` یا `error_file_id` را بررسی کنید، ردیف‌های JSONL را اصلاح کنید و batch جدید بسازید. |
| `in_progress` | ردیف‌ها در حال اجرا هستند. | polling را ادامه دهید؛ کامل بودن فایل‌های خروجی را فرض نکنید. |
| `finalizing` | اجرا تمام شده و فایل‌های نتیجه آماده می‌شوند. | polling را ادامه دهید و storage دانلود فایل‌های output و error را آماده کنید. |
| `completed` | فایل‌های نتیجه آماده‌اند. | `output_file_id` را دانلود کنید، ردیف‌ها را با `custom_id` پردازش کنید و metadata batch را archive کنید. |
| `expired` | بازه ۲۴ ساعته قبل از تکمیل همه ردیف‌ها تمام شده است. | ردیف‌های کامل‌شده را نگه دارید، ردیف‌های منقضی‌شده را در فایل خطا بررسی کنید و فقط `custom_id`های ناتمام را دوباره ارسال کنید. |
| `cancelling` | لغو در حال انجام است و بعضی کارهای در حال اجرا ممکن است هنوز تمام شوند. | مصرف‌کننده‌های downstream را متوقف کنید و منتظر `cancelled` بمانید. |
| `cancelled` | لغو کامل شده است. | نتیجه‌های جزئی را دانلود کنید، ردیف‌های ناتمام را cancelled علامت بزنید و از پردازش دوباره ردیف‌های کامل‌شده جلوگیری کنید. |

برای fallback مبتنی بر worker خودتان، همین state machine را mirror کنید. این کار مهاجرت آینده به `/v1/batches` میزبانی‌شده را بدون تغییر گزارش‌گیری downstream ساده‌تر می‌کند.

## ایجاد دسته

```
POST https://api.avalai.ir/v1/batches
```

یک دسته را از یک فایل آپلود شده از درخواست‌ها ایجاد و اجرا می‌کند.

### بدنه درخواست (Request Body)

| پارامتر             | نوع    | الزامی | توضیحات                                                                                                                                                                                                                                                                                                              |
| ------------------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input_file_id`     | string | بله    | شناسه یک فایل آپلود شده که حاوی درخواست‌ها برای دسته جدید است. فایل ورودی شما باید به صورت [فایل JSONL](#شی-ورودی-درخواست) فرمت‌بندی شده باشد و باید با هدف `batch` آپلود شود. فایل می‌تواند تا ۵۰٬۰۰۰ درخواست داشته باشد و حجم آن تا ۲۰۰ مگابایت باشد. برای نحوه آپلود فایل به [آپلود فایل](files.md) مراجعه کنید. |
| `endpoint`          | string | بله    | نقطه‌پایانی که برای همه درخواست‌های دسته استفاده می‌شود. هدف‌های OpenAI-compatible شامل `/v1/responses`، `/v1/chat/completions`، `/v1/embeddings`، `/v1/completions` (قدیمی)، `/v1/moderations`، `/v1/images/generations`، `/v1/images/edits` و `/v1/videos` هستند. دسترسی AvalAI ممکن است در زمان rollout محدودتر باشد. دسته‌های `/v1/embeddings` همچنین به حداکثر ۵۰٬۰۰۰ ورودی embedding در همه درخواست‌های دسته محدود هستند. |
| `completion_window` | string | بله    | بازه زمانی که دسته باید در آن پردازش شود. در حال حاضر فقط `24h` پشتیبانی می‌شود.                                                                                                                                                                                                                                     |
| `metadata`          | map    | خیر    | مجموعه‌ای از ۱۶ جفت کلید-مقدار که می‌توان به یک شی پیوست کرد. این می‌تواند برای ذخیره اطلاعات اضافی در مورد شی در قالبی ساختاریافته مفید باشد. کلیدها رشته‌هایی با حداکثر طول ۶۴ کاراکتر هستند. مقادیر رشته‌هایی با حداکثر طول ۵۱۲ کاراکتر هستند.                                                                  |
| `output_expires_after` | object | خیر | سیاست انقضای اختیاری برای فایل‌های خروجی و خطا، وقتی route انتخابی از آن پشتیبانی کند. از همان شکل `anchor: "created_at"` و `seconds` در [انقضای Files API](fa/api-reference/files.md?id=شی-سیاست-انقضا-expiration-policy-object) استفاده کنید و فایل‌های نتیجه مهم را پیش از انقضا دانلود کنید. |

### مثال درخواست

```bash
curl https://api.avalai.ir/v1/batches \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
  "input_file_id": "file-abc123",
  "endpoint": "/v1/chat/completions",
  "completion_window": "24h",
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "کار ارزیابی شبانه"
  }
}'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

batch = client.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/chat/completions",
    completion_window="24h",
    metadata={
        "customer_id": "user_123456789",
        "batch_description": "کار ارزیابی شبانه",
    },
)
print(batch)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function main() {
  const batch = await client.batches.create({
    input_file_id: "file-abc123",
    endpoint: "/v1/chat/completions",
    completion_window: "24h",
    metadata: {
      customer_id: "user_123456789",
      batch_description: "کار ارزیابی شبانه",
    },
  });
  console.log(batch);
}
main();

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

برای اجرای batch با شکل Responses، batch را با `endpoint: "/v1/responses"` بسازید و فایل ورودی را با ردیف‌های `/v1/responses` آماده کنید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

batch = client.batches.create(
    input_file_id="file-abc123",
    endpoint="/v1/responses",
    completion_window="24h",
    metadata={"batch_description": "ارزیابی شبانه Responses"},
)

print(batch)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const batch = await client.batches.create({
  input_file_id: "file-abc123",
  endpoint: "/v1/responses",
  completion_window: "24h",
  metadata: {
    batch_description: "ارزیابی شبانه Responses",
  },
});

console.log(batch);

```

```bash
curl https://api.avalai.ir/v1/batches \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "input_file_id": "file-abc123",
    "endpoint": "/v1/responses",
    "completion_window": "24h",
    "metadata": {
      "batch_description": "ارزیابی شبانه Responses"
    }
  }'

```


- ایجاد batch همچنان از `/v1/batches` انجام می‌شود؛ فقط مقدار `endpoint` به `/v1/responses` تغییر می‌کند.
- در هر ردیف JSONL، `messages` به `input` و راهنمایی system/developer به `instructions` یا آیتم `developer` منتقل می‌شود.
- در ردیف‌های خروجی، متن تولیدشده را از بدنه Responses بخوانید؛ معمولا `body.output_text`.

</details>
<!-- responses-equivalent:end -->


### بازگشتی‌ها (Returns)

شی [دسته](#شی-دسته) ایجاد شده.

## بازیابی دسته

```
GET https://api.avalai.ir/v1/batches/{batch_id}
```

یک دسته را بازیابی می‌کند.

### پارامترهای مسیر (Path Parameters)

| پارامتر    | نوع    | الزامی | توضیحات                            |
| ---------- | ------ | ------ | ---------------------------------- |
| `batch_id` | string | بله    | شناسه دسته‌ای که باید بازیابی شود. |

### مثال درخواست

```bash
curl https://api.avalai.ir/v1/batches/batch_abc123 \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

### بازگشتی‌ها (Returns)

شی [دسته](#شی-دسته) مطابق با شناسه مشخص شده.

## لغو دسته

```
POST https://api.avalai.ir/v1/batches/{batch_id}/cancel
```

یک دسته در حال پیشرفت را لغو می‌کند. دسته به مدت ۱۰ دقیقه در وضعیت `cancelling` خواهد بود، قبل از اینکه به `cancelled` تغییر کند، جایی که نتایج جزئی (در صورت وجود) در فایل خروجی در دسترس خواهد بود.

### پارامترهای مسیر (Path Parameters)

| پارامتر    | نوع    | الزامی | توضیحات                        |
| ---------- | ------ | ------ | ------------------------------ |
| `batch_id` | string | بله    | شناسه دسته‌ای که باید لغو شود. |

### مثال درخواست

```bash
curl https://api.avalai.ir/v1/batches/batch_abc123/cancel \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -X POST
```

### بازگشتی‌ها (Returns)

شی [دسته](#شی-دسته) لغو شده.

## لیست دسته‌ها

```
GET https://api.avalai.ir/v1/batches
```

دسته‌های سازمان شما را لیست می‌کند.

### پارامترهای کوئری (Query Parameters)

| پارامتر | نوع     | الزامی | توضیحات                                                                                            |
| ------- | ------- | ------ | -------------------------------------------------------------------------------------------------- |
| `after` | string  | خیر    | یک نشانگر برای استفاده در صفحه‌بندی. `after` یک شناسه شی است که مکان شما را در لیست تعریف می‌کند. |
| `limit` | integer | خیر    | محدودیتی برای تعداد اشیا بازگردانده شده. محدودیت می‌تواند بین ۱ تا ۱۰۰ باشد و پیش‌فرض ۲۰ است.     |

### مثال درخواست

```bash
curl "https://api.avalai.ir/v1/batches?limit=2" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

### بازگشتی‌ها (Returns)

لیستی از اشیا [دسته](#شی-دسته) صفحه‌بندی شده.

## شی دسته

| پارامتر             | نوع             | توضیحات                                                                                                           |
| ------------------- | --------------- | ----------------------------------------------------------------------------------------------------------------- |
| `id`                | string          | شناسه، که می‌تواند در نقاط پایانی API ارجاع داده شود.                                                             |
| `object`            | string          | نوع شی، که همیشه `batch` است.                                                                                    |
| `endpoint`          | string          | نقطه‌پایانی API AvalAI که توسط دسته استفاده می‌شود.                                                               |
| `errors`            | object or null  | حاوی جزئیات در مورد خطاها در صورت وقوع در طول پردازش دسته است.                                                    |
| `input_file_id`     | string          | شناسه فایل ورودی برای دسته.                                                                                       |
| `completion_window` | string          | بازه زمانی که دسته باید در آن پردازش شود.                                                                         |
| `status`            | string          | وضعیت فعلی دسته (مثلا `validating`, `in_progress`, `completed`, `failed`, `cancelling`, `cancelled`, `expired`). |
| `output_file_id`    | string or null  | شناسه فایل حاوی خروجی‌های درخواست‌های با موفقیت اجرا شده.                                                         |
| `error_file_id`     | string or null  | شناسه فایل حاوی خروجی‌های درخواست‌های با خطا.                                                                     |
| `created_at`        | integer         | زمان یونیکس (به ثانیه) برای زمان ایجاد دسته.                                                                      |
| `in_progress_at`    | integer or null | زمان یونیکس (به ثانیه) برای زمان شروع پردازش دسته.                                                                |
| `expires_at`        | integer or null | زمان یونیکس (به ثانیه) برای زمان انقضای دسته.                                                                     |
| `finalizing_at`     | integer or null | زمان یونیکس (به ثانیه) برای زمان شروع نهایی‌سازی دسته.                                                            |
| `completed_at`      | integer or null | زمان یونیکس (به ثانیه) برای زمان تکمیل دسته.                                                                      |
| `failed_at`         | integer or null | زمان یونیکس (به ثانیه) برای زمان شکست دسته.                                                                       |
| `expired_at`        | integer or null | زمان یونیکس (به ثانیه) برای زمان انقضای دسته.                                                                     |
| `cancelling_at`     | integer or null | زمان یونیکس (به ثانیه) برای زمان شروع لغو دسته.                                                                   |
| `cancelled_at`      | integer or null | زمان یونیکس (به ثانیه) برای زمان لغو دسته.                                                                        |
| `request_counts`    | object          | تعداد درخواست‌ها برای وضعیت‌های مختلف در دسته (`total`, `completed`, `failed`).                                   |
| `metadata`          | map             | مجموعه‌ای از جفت‌های کلید-مقدار پیوست شده به شی.                                                                 |

### مثال شی دسته

```json
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/chat/completions",
  "errors": null,
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "completed",
  "output_file_id": "file-cvaTdG",
  "error_file_id": "file-HOWS94",
  "created_at": 1711471533,
  "in_progress_at": 1711471538,
  "expires_at": 1711557933,
  "finalizing_at": 1711493133,
  "completed_at": 1711493163,
  "failed_at": null,
  "expired_at": null,
  "cancelling_at": null,
  "cancelled_at": null,
  "request_counts": {
    "total": 100,
    "completed": 95,
    "failed": 5
  },
  "metadata": {
    "customer_id": "user_123456789",
    "batch_description": "کار ارزیابی شبانه"
  }
}
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی batch روی `/v1/responses` تنظیم می‌شود، شی batch همان فیلدهای چرخه عمر را دارد؛ فقط `endpoint` و شکل بدنه ردیف‌های خروجی متفاوت است.

```json
{
  "id": "batch_abc123",
  "object": "batch",
  "endpoint": "/v1/responses",
  "input_file_id": "file-abc123",
  "completion_window": "24h",
  "status": "completed",
  "output_file_id": "file-cvaTdG",
  "error_file_id": null
}
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## فایل‌های نتیجه و انقضا

وقتی batch به وضعیت `completed` می‌رسد، از `output_file_id` همراه [Files API](fa/api-reference/files.md) برای دانلود نتیجه‌های موفق استفاده کنید. ردیف‌هایی که در validation، انقضا یا اجرا شکست بخورند، در صورت وجود در `error_file_id` نوشته می‌شوند. اگر `output_expires_after` را تنظیم می‌کنید، نتیجه‌های پایدار را پیش از انقضای فایل‌های خروجی در storage خودتان کپی کنید.

ممکن است ترتیب خروجی با ترتیب ورودی متفاوت باشد، بنابراین همیشه ردیف‌ها را با `custom_id` به هم وصل کنید. اگر batch قبل از پایان همه ردیف‌ها منقضی شود، ردیف‌های کامل‌شده همچنان در دسترس می‌مانند و ردیف‌های ناتمام به‌عنوان خطا گزارش می‌شوند.

## شی ورودی درخواست

ساختار هر خط در فایل ورودی JSONL.

| پارامتر     | نوع    | الزامی | توضیحات                                                                                                                                                        |
| ----------- | ------ | ------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `custom_id` | string | بله    | یک شناسه برای هر درخواست که توسط توسعه‌دهنده ارائه می‌شود و برای تطبیق خروجی‌ها با ورودی‌ها استفاده می‌شود. باید برای هر درخواست در یک دسته منحصر به فرد باشد. |
| `method`    | string | بله    | متد HTTP که برای درخواست استفاده می‌شود. در حال حاضر فقط `POST` پشتیبانی می‌شود.                                                                               |
| `url`       | string | بله    | URL نسبی API AvalAI که برای درخواست استفاده می‌شود (مثلا `/v1/chat/completions` یا `/v1/responses`).                                                        |
| `body`      | object | بله    | بدنه درخواست برای فراخوانی API (مثلا پارامترها برای تکمیل چت).                                                                                                |

همه ردیف‌های یک فایل ورودی را روی یک endpoint و یک مدل نگه دارید. مقدار `stream: true` نگذارید؛ نتایج batch بعد از پردازش از طریق فایل خروجی تحویل داده می‌شوند.

### مثال خط ورودی

```json
{
  "custom_id": "request-1",
  "method": "POST",
  "url": "/v1/chat/completions",
  "body": {
    "model": "gpt-5.4-mini",
    "messages": [
      {
        "role": "system",
        "content": "شما یک دستیار مفید هستید."
      },
      {
        "role": "user",
        "content": "۲+۲ چند می‌شود؟"
      }
    ]
  }
}
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، از این شکل خط استفاده کنید. `messages` به `input` منتقل می‌شود، پیام سیستمی به `instructions` می‌رود و متن نهایی از `response.output_text` داخل بدنه پاسخ خوانده می‌شود.

```json
{
  "custom_id": "request-1",
  "method": "POST",
  "url": "/v1/responses",
  "body": {
    "model": "gpt-5.4-mini",
    "input": "۲+۲ چند می‌شود؟",
    "instructions": "You are a helpful assistant."
  }
}
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## شی خروجی درخواست

ساختار هر خط در فایل(های) خروجی JSONL.

| پارامتر     | نوع            | توضیحات                                                                                            |
| ----------- | -------------- | -------------------------------------------------------------------------------------------------- |
| `id`        | string         | شناسه درخواست دسته.                                                                                |
| `custom_id` | string         | شناسه ارائه شده توسط توسعه‌دهنده از فایل ورودی.                                                    |
| `response`  | object or null | شی پاسخ از فراخوانی API در صورت موفقیت آمیز بودن. شامل `status_code`, `request_id`, و `body` است. |
| `error`     | object or null | جزئیات در مورد خطا در صورت شکست درخواست.                                                           |

### مثال خط خروجی (موفقیت)

```json
{
  "id": "batch_req_wnaDys",
  "custom_id": "request-2",
  "response": {
    "status_code": 200,
    "request_id": "req_c187b3",
    "body": {
      "id": "chatcmpl-9758Iw",
      "object": "chat.completion",
      "created": 1711475054,
      "model": "gpt-5.4-mini",
      "choices": [
        {
          "index": 0,
          "message": {
            "role": "assistant",
            "content": "۲ + ۲ برابر است با ۴."
          },
          "finish_reason": "stop"
        }
      ],
      "usage": {
        "prompt_tokens": 24,
        "completion_tokens": 15,
        "total_tokens": 39
      },
      "system_fingerprint": null
    }
  },
  "error": null
}
```

### مثال خط خروجی (خطا)

```json
{
  "id": "batch_req_abcxyz",
  "custom_id": "request-3",
  "response": null,
  "error": {
    "code": "invalid_request_error",
    "message": "شناسه مدل نامعتبر ارائه شده است."
  }
}
```
