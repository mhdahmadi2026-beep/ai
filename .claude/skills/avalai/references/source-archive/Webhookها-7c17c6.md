# Webhookها

Webhook به API اجازه می‌دهد وقتی وضعیت کارهای async تغییر می‌کند به برنامه شما اطلاع دهد. OpenAI برای eventهایی مثل `response.completed`، تکمیل Batch و به‌روزرسانی jobهای fine-tuning webhook مستند کرده است. در AvalAI، webhook میزبانی‌شده ارائه‌دهنده را وابسته به route و حساب بدانید؛ وقتی webhook میزبانی‌شده در دسترس نیست، از worker مالک job، webhook برنامه خودتان را ارسال کنید.

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

## چه زمانی استفاده کنیم

وقتی polling کافی نیست از webhook استفاده کنید:

- background Responses یا jobهای طولانی باید پس از پایان به backend خبر دهند؛
- workerهای Batch، eval یا data-enrichment به callback تکمیل نیاز دارند؛
- تولید ویدیو، fine-tuning یا پردازش فایل باید سرویس دیگری را بیدار کند؛
- resellerها نیاز دارند سیستم‌های downstream eventهای هزینه یا وضعیت job را دریافت کنند.

برای workflowهای فقط مرورگری، polling endpoint job خودتان را ترجیح دهید. Webhook برای اعلان server-to-server مناسب‌تر است.

## مرز Webhook میزبانی‌شده

اگر route AvalAI یا provider upstream شما webhook به سبک OpenAI ارائه می‌کند، این قواعد عملیاتی را در نظر بگیرید:

- یک endpoint عمومی HTTPS تنظیم کنید و فقط event typeهای لازم را subscribe کنید؛
- raw request body را برای verification امضا نگه دارید؛
- signing secret را پیش از هر side effect بررسی کنید؛
- سریع با `2xx` پاسخ دهید و پردازش سنگین را به worker منتقل کنید؛
- با event ID مثل header `webhook-id` یا `id` خود event deduplicate کنید؛
- هنگام شکست endpoint، retry با backoff را انتظار داشته باشید.

سیاست مرجع OpenAI تحویل‌های ناموفق webhook را تا ۷۲ ساعت retry می‌کند. برای AvalAI یا webhookهای provider-specific همین پنجره retry را فرض نکنید مگر اینکه آن route صریحا مستند کرده باشد.

### چک‌لیست پیکربندی و Headerها

در webhookهای میزبانی‌شده OpenAI، endpointها به‌صورت per-project در داشبورد provider تنظیم می‌شوند و signing secret فقط یک‌بار نمایش داده می‌شود. برای routeهای AvalAI، ابتدا بررسی کنید provider انتخابی برای حساب شما پیکربندی webhook میزبانی‌شده ارائه می‌کند یا نه. اگر ارائه نمی‌کند، از الگوی app-managed پایین با secret اختصاصی `AVALAI_WEBHOOK_SECRET` استفاده کنید.

وقتی داشبورد webhook میزبانی‌شده در دسترس است، فقط event typeهایی را subscribe کنید که worker شما واقعا مدیریت می‌کند، در کد allowlist نگه دارید، و پیش از فعال کردن side effectهای production یک test event از provider ارسال کنید. برای eventهای سازگار با OpenAI، کاتالوگ کامل eventها در API reference همان provider است؛ برای callbackهای app-managed در AvalAI، taxonomy کوچک و نسخه‌دار خودتان را تعریف کنید.

هنگام دریافت event سازگار با OpenAI، پیش از queue کردن کار این فیلدها را نگه دارید و log کنید:

| فیلد | چرا مهم است |
| --- | --- |
| `webhook-id` | شناسه پایدار delivery برای idempotency و جلوگیری از پردازش duplicate. |
| `webhook-timestamp` | همراه raw body برای شناسایی requestهای قدیمی یا replayشده استفاده می‌شود. |
| `webhook-signature` | ثابت می‌کند payload از دارنده signing secret آمده است. |
| `id` و `type` رویداد | به worker کمک می‌کند `response.completed`، `job.failed` یا eventهای سفارشی را امن route کند. |

اگر signing secret لو رفت، فورا آن را rotate کنید. هنگام rotation یک overlap window کوتاه پشتیبانی کنید که receiver هر دو secret قدیمی و جدید را بپذیرد، سپس بعد از drain شدن retryهای queueشده secret قدیمی را حذف کنید.

### معنای تحویل و تست محلی

Receiverها را برای تحویل **at-least-once** طراحی کنید: تحویل موفق یعنی endpoint شما `2xx` برگردانده، نه اینکه کار downstream کامل شده است. پیش از queue کردن کار کند، event ID و payload خامِ verifyشده را ذخیره کنید، وقتی `webhook-id` وجود دارد آن را idempotency key بگیرید، و deliveryهای تکراری را بی‌خطر کنید. redirectهای `3xx` را failure بدانید؛ URL عمومی HTTPS نهایی را مستقیم configure کنید.

برای توسعه local، receiver را از طریق public tunnel مثل ngrok، محیط توسعه cloud، یا endpoint موقت serverless در دسترس بگذارید. `localhost` ساده نمی‌تواند webhook ارائه‌دهنده را دریافت کند.

یک contract روشن برای receiver تعریف کنید:

| حالت | رفتار receiver |
| --- | --- |
| event معتبر و جدید | event را ذخیره کنید، کار را queue کنید و فوری `2xx` برگردانید. |
| `webhook-id` یا event `id` تکراری | بدون تکرار side effectها `2xx` برگردانید. |
| امضای نامعتبر یا timestamp قدیمی | `400` برگردانید و payload را parse یا queue نکنید. |
| خرابی موقت database یا queue | فقط وقتی می‌خواهید sender بعدا retry کند `5xx` برگردانید. |

### ماتریس Route کردن Eventها

نام eventهای webhook را یک contract برای route کردن بدانید، نه فقط log. Handler را کوچک نگه دارید: امضا را verify کنید، delivery را deduplicate کنید، event را ذخیره کنید، و action مخصوص همان route را queue کنید.

| خانواده Event | اقدام معمول | پیش از `2xx` ذخیره کنید |
| --- | --- | --- |
| `response.completed` | Response را retrieve کنید، خروجی نهایی را استخراج کنید، و رکورد conversation یا job را به‌روزرسانی کنید. | `response_id`، شناسه ارتباط با کاربر/job، status خروجی. |
| شکست یا لغو Response | job را terminal علامت بزنید، error code امن ذخیره کنید، و تصمیم بگیرید app باید با request جدید retry کند یا نه. | `response_id`، terminal status، تصمیم retry. |
| تکمیل Batch یا eval | result file یا report را بگیرید، dashboardها را به‌روزرسانی کنید، و به سیستم‌های downstream اطلاع دهید. | شناسه‌های batch/eval، result file ID، counterهای تجمیعی. |
| تکمیل fine-tuning | قبل از فعال کردن traffic، state نهایی job و شناسه مدل را دریافت کنید. | fine-tuning job ID، model ID، validation status. |
| تکمیل ویدیو یا رسانه | asset تولیدشده یا دلیل شکست را بگیرید، سپس URLهای polling موقت را expire کنید. | media job ID، asset URL یا storage key، status. |
| callback هزینه یا reseller | usage را reconcile کنید، billing idempotent انجام دهید، و اعلان مشتری را emit کنید. | request/job ID، مقدار usage، ledger transaction ID. |

برای eventهای میزبانی‌شده OpenAI، فقط به event typeهای دقیقی subscribe کنید که app شما مدیریت می‌کند. برای eventهای app-managed در AvalAI، وقتی مشتریان خارجی به schema وابسته شدند از namespace نسخه‌دار مثل `job.completed.v1` استفاده کنید.

## Receiver سازگار با OpenAI

وقتی sender از فرمت Standard Webhooks مورد استفاده OpenAI پیروی می‌کند، به جای verification دستی، از helperهای SDK یا کتابخانه‌های Standard Webhooks استفاده کنید. این helperها raw body، headerها، timestamp و signature را پیش از برگرداندن event اعتبارسنجی می‌کنند. این الگو را فقط برای routeهایی به‌کار ببرید که signing secret سازگار را صریحا ارائه می‌کنند.

```python
import os
from flask import Flask, Response, request
from openai import InvalidWebhookSignatureError, OpenAI

app = Flask(__name__)
client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
webhook_secret = os.environ["AVALAI_OR_PROVIDER_WEBHOOK_SECRET"]


@app.post("/webhooks/openai-style")
def receive_openai_style_webhook():
    try:
        event = client.webhooks.unwrap(
            request.data,
            request.headers,
            secret=webhook_secret,
        )
    except InvalidWebhookSignatureError:
        return Response("invalid signature", status=400)

    delivery_id = request.headers.get("webhook-id") or event.id

    # Store delivery_id before enqueueing work so retries are safe.
    print("verified event:", delivery_id, event.type, event.data)
    return Response(status=200)

```

```javascript
import express from "express";
import OpenAI from "openai";

const app = express();
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});
const webhookSecret = process.env.AVALAI_OR_PROVIDER_WEBHOOK_SECRET;

app.use("/webhooks/openai-style", express.text({ type: "application/json" }));

app.post("/webhooks/openai-style", async (req, res) => {
  try {
    const event = await client.webhooks.unwrap(req.body, req.headers, {
      secret: webhookSecret,
    });

    const deliveryId = req.header("webhook-id") ?? event.id;

    // Store deliveryId before enqueueing work so retries are safe.
    console.log("verified event:", deliveryId, event.type, event.data);
    return res.sendStatus(200);
  } catch (error) {
    if (error instanceof OpenAI.InvalidWebhookSignatureError) {
      return res.status(400).send("invalid signature");
    }
    throw error;
  }
});

app.listen(8000, () => console.log("Webhook receiver listening on :8000"));

```


پیش از verification از `express.json()` یا هر parser دیگری که payload را تغییر می‌دهد استفاده نکنید. اگر route از schema امضای متفاوتی استفاده می‌کند، دقیقا headerها و canonical payload همان provider را دنبال کنید.

برای `response.completed`، payload رویداد معمولا شامل Response ID است. receiver را سریع نگه دارید: event را verify کنید، ID آن را ذخیره کنید، `2xx` برگردانید، و یک worker پاسخ نهایی را retrieve کند.

```python
# این بخش را بعد از verify شدن webhook در queue worker اجرا کنید.
response_id = event.data.id
response = client.responses.retrieve(response_id)
print(response.output_text)

```

```javascript
// این بخش را بعد از verify شدن webhook در queue worker اجرا کنید.
const responseId = event.data.id;
const response = await client.responses.retrieve(responseId);
console.log(response.output_text);

```


## الگوی Webhook مدیریت‌شده در برنامه

برای jobهای async امن در AvalAI، worker شما پس از ذخیره نتیجه نهایی یک callback امضاشده ارسال کند. Receiver امضا را verify می‌کند، event ID را deduplicate می‌کند، event را ذخیره می‌کند و قبل از کار سنگین `2xx` برمی‌گرداند.

```python
import hashlib
import hmac
import json
import os
import time
from flask import Flask, Response, request

app = Flask(__name__)
WEBHOOK_SECRET = os.environ["AVALAI_WEBHOOK_SECRET"].encode()
WEBHOOK_TOLERANCE_SECONDS = 300
seen_event_ids = set()


def verify_signature(raw_body: bytes, timestamp: str, signature: str) -> bool:
    try:
        event_time = int(timestamp)
    except ValueError:
        return False

    if abs(time.time() - event_time) > WEBHOOK_TOLERANCE_SECONDS:
        return False

    signed_payload = timestamp.encode() + b"." + raw_body
    expected = hmac.new(WEBHOOK_SECRET, signed_payload, hashlib.sha256).hexdigest()
    return hmac.compare_digest(signature, f"v1={expected}")


@app.post("/webhooks/avalai-jobs")
def receive_job_webhook():
    raw_body = request.get_data()
    event_id = request.headers.get("webhook-id", "")
    timestamp = request.headers.get("webhook-timestamp", "")
    signature = request.headers.get("webhook-signature", "")

    if not verify_signature(raw_body, timestamp, signature):
        return Response("invalid signature", status=400)

    event = json.loads(raw_body)
    event_id = event_id or event.get("id", "")
    if not event_id:
        return Response("missing event id", status=400)

    if event_id in seen_event_ids:
        return Response(status=200)

    seen_event_ids.add(event_id)

    # Persist event first, then enqueue slow processing.
    print("Received event:", event["type"], event["data"]["job_id"])
    return Response(status=200)


if __name__ == "__main__":
    app.run(port=8000)

```

```javascript
import crypto from "node:crypto";
import express from "express";

const app = express();
const webhookSecret = Buffer.from(process.env.AVALAI_WEBHOOK_SECRET, "utf8");
const webhookToleranceSeconds = 300;
const seenEventIds = new Set();

app.use("/webhooks/avalai-jobs", express.raw({ type: "application/json" }));

function verifySignature(rawBody, timestamp, signature) {
  const eventTime = Number(timestamp);
  if (!Number.isFinite(eventTime)) {
    return false;
  }

  if (Math.abs(Date.now() / 1000 - eventTime) > webhookToleranceSeconds) {
    return false;
  }

  const expected =
    "v1=" +
    crypto
      .createHmac("sha256", webhookSecret)
      .update(`${timestamp}.`)
      .update(rawBody)
      .digest("hex");

  if (signature.length !== expected.length) {
    return false;
  }

  return crypto.timingSafeEqual(Buffer.from(signature), Buffer.from(expected));
}

app.post("/webhooks/avalai-jobs", (req, res) => {
  const eventId = req.header("webhook-id") ?? "";
  const timestamp = req.header("webhook-timestamp") ?? "";
  const signature = req.header("webhook-signature") ?? "";

  if (!verifySignature(req.body, timestamp, signature)) {
    return res.status(400).send("invalid signature");
  }

  const event = JSON.parse(req.body.toString("utf8"));
  const dedupeId = eventId || event.id;
  if (!dedupeId) {
    return res.status(400).send("missing event id");
  }

  if (seenEventIds.has(dedupeId)) {
    return res.sendStatus(200);
  }

  seenEventIds.add(dedupeId);

  // Persist event first, then enqueue slow processing.
  console.log("Received event:", event.type, event.data.job_id);
  return res.sendStatus(200);
});

app.listen(8000, () => console.log("Webhook receiver listening on :8000"));

```


در production برای `seen_event_ids` از storage پایدار استفاده کنید؛ set در حافظه فقط برای مثال local است.

## شکل Event

payloadهای webhook برنامه را کوچک و پایدار نگه دارید:

```json
{
  "object": "event",
  "id": "evt_job_01J...",
  "type": "job.completed",
  "created_at": 1760000000,
  "data": {
    "job_id": "job_abc123",
    "response_id": "resp_abc123",
    "status": "completed"
  }
}
```

Event typeهای پیشنهادی:

| Event | کاربرد |
| --- | --- |
| `job.completed` | پاسخ نهایی، shard batch، گزارش یا asset رسانه آماده است. |
| `job.failed` | worker پس از retryها شکست خورده؛ error code امن اضافه کنید. |
| `job.cancelled` | کاربر یا سیستم پیش از تکمیل job را لغو کرده است. |
| `cost.available` | usage قابل billing برای reseller یا chargeback آماده است. |

## چک‌لیست Sender

- برای هر delivery یک event ID یکتا بسازید.
- `timestamp.raw_body` را با secret امضا کنید و `webhook-signature` را بفرستید.
- deliveryهای timeout یا `5xx` را با exponential backoff retry کنید.
- تا ابد retry نکنید؛ expiration window و dead-letter queue تعریف کنید.
- API key، secret خام کاربر یا خروجی حجیم مدل را در webhook payload قرار ندهید.

## چک‌لیست Receiver

- raw request body را برای verification نگه دارید.
- امضای نامعتبر را پیش از parsing یا side effect رد کنید.
- timestampهای قدیمی را رد کنید تا ریسک replay کمتر شود.
- با event ID deduplicate کنید.
- سریع با `2xx` پاسخ دهید و کار کند را queue کنید.
- event ID، request ID، job ID، status و نتیجه signature verification را log کنید.
- اگر signing secret لو رفت آن را rotate کنید و برای migration یک overlap window کوتاه پشتیبانی کنید.
- برای تست local از public tunnel یا محیط توسعه cloud استفاده کنید؛ webhook به `localhost` ساده نمی‌رسد.
- redirect را failure بدانید؛ URL عمومی HTTPS نهایی را مستقیم configure کنید.

## منابع مرتبط

- [پردازش پس‌زمینه](/fa/guides/background-processing.md)
- [پردازش دسته‌ای](/fa/guides/batch-processing.md)
- [تنظیم دقیق](/fa/guides/fine-tuning.md)
- [هدرهای پاسخ](/fa/api-reference/response-headers.md)
- [راهنمای ردیابی هزینه برای فروشندگان](/fa/resellers/cost-tracking-guide.md)
