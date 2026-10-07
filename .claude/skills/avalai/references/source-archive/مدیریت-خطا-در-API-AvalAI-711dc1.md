# مدیریت خطا در API AvalAI

این راهنما اطلاعات جامعی در مورد مدیریت خطاها هنگام استفاده از API AvalAI ارائه می‌دهد.

## درک خطاهای API

هنگامی که یک درخواست API با شکست مواجه می‌شود، AvalAI یک کد وضعیت HTTP به همراه یک پاسخ JSON که شامل اطلاعات دقیق خطا است، برمی‌گرداند. درک این خطاها و پیاده‌سازی مدیریت خطای مناسب برای ساخت برنامه‌های پایدار ضروری است.

### فرمت پاسخ خطا

```json
{
  "error": {
    "message": "Incorrect API key provided: aa-JEa8wq. You can find your API key at https://chat.avalai.ir/platform/api-keys.",

    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_api_key",
    "solution": "If your API key was recently created, please wait up to 60 seconds for it to activate. Otherwise, verify you're using the correct key and that it hasn't been revoked. You can manage your API keys at https://chat.avalai.ir/platform/api-keys.",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### فیلدهای رایج در پاسخ‌های خطا

| فیلد | توضیحات |
|-------|-------------|
| `message` | توضیحی قابل خواندن توسط انسان از خطا |
| `type` | نوع خطای بازگردانده شده |
| `param` | پارامتری که باعث خطا شده است (در صورت وجود) |
| `code` | کد خطای خاص (در صورت وجود) |
| `solution` | راه‌حل پیشنهادی برای رفع خطا (در صورت وجود) |
| `request_id` | شناسه منحصربه‌فرد درخواست برای پیگیری و عیب‌یابی |

### استفاده از شناسه درخواست (Request ID) برای پشتیبانی

هر پاسخ خطا شامل فیلد یکتای `request_id` است که برای عیب‌یابی و دریافت کمک از پشتیبانی استفاده می‌شود. پاسخ‌های موفق نیز هدر `avalai-request-id` دارند. اگر `X-Client-Request-Id` می‌فرستید، آن را کنار شناسه درخواست AvalAI ثبت کنید تا حتی در timeoutها هم بتوانید درخواست را correlate کنید.

وقتی queue، سیستم trace یا فرایند پشتیبانی مشتری شما پیش از برگشت API به یک شناسه پایدار نیاز دارد، از `X-Client-Request-Id` استفاده کنید. برای هر درخواست منطقی مقدار جدید بسازید، آن را فقط ASCII نگه دارید، طول آن را زیر ۵۱۲ کاراکتر نگه دارید، و فقط هنگام retry همان عملیات idempotent دوباره از همان مقدار استفاده کنید. اگر timeout یا خطای شبکه اجازه خواندن `avalai-request-id` را ندهد، client request ID بهترین handle ارتباطی است که هنوز در اختیار شماست.

اگر خطایی را نمی‌توانید حل کنید، این بسته اطلاعاتی را برای پشتیبانی آماده کنید:

- `request_id` یا `avalai-request-id`
- مقدار اختیاری `X-Client-Request-Id` اگر برنامه شما آن را فرستاده است
- مدل، endpoint، وضعیت HTTP، timestamp و timezone
- metadata امن درخواست مثل تعداد توکن، اندازه فایل یا تعداد retry
- متن کامل `message`، `type`، `code` و `param`

API key، secret خام کاربر، فایل خصوصی یا prompt کامل را ارسال نکنید مگر اینکه پشتیبانی صراحتا نمونه redacted بخواهد.

## کدهای وضعیت HTTP

AvalAI از کدهای وضعیت استاندارد HTTP برای نشان دادن موفقیت یا شکست درخواست‌های API استفاده می‌کند:

### 2xx - موفقیت

| کد وضعیت | توضیحات |
|-------------|-------------|
| 200 | OK - درخواست موفقیت‌آمیز بود |
| 201 | Created - منبع با موفقیت ایجاد شد |
| 204 | No Content - درخواست موفقیت‌آمیز بود، اما محتوایی برای بازگرداندن وجود ندارد |

### 4xx - خطاهای کلاینت

| کد وضعیت | توضیحات |
|-------------|-------------|
| 400 | Bad Request - درخواست نادرست یا نامعتبر بود |
| 401 | Unauthorized - احراز هویت ناموفق بود یا ارائه نشده بود |
| 403 | Forbidden - کاربر احراز هویت شده به منبع درخواستی دسترسی ندارد |
| 404 | Not Found - منبع درخواستی وجود ندارد |
| 409 | Conflict - درخواست با وضعیت فعلی منبع تداخل دارد |
| 422 | Unprocessable Entity - درخواست به خوبی فرمت‌بندی شده بود اما حاوی خطاهای معنایی است |
| 429 | Too Many Requests - از محدودیت نرخ فراتر رفته است |

### 5xx - خطاهای سرور

| کد وضعیت | توضیحات |
|-------------|-------------|
| 500 | Internal Server Error - خطای غیرمنتظره‌ای در سرور رخ داد |
| 502 | Bad Gateway - سرور پاسخ نامعتبری از سرور بالادستی دریافت کرد |
| 503 | Service Unavailable - سرور به طور موقت در دسترس نیست |
| 504 | Gateway Timeout - سرور در انتظار پاسخ از سرور بالادستی زمانش تمام شد |

## کلاس‌های خطای SDK

SDKهای سازگار با OpenAI علاوه بر کدهای وضعیت HTTP، exceptionهای typed هم برمی‌گردانند. برای branch کردن منطق از این کلاس‌ها استفاده کنید، اما همچنان `request_id` / `avalai-request-id` AvalAI را log کنید؛ این شناسه‌ها برای پشتیبانی و lookup هزینه نمایندگان authoritative هستند.

| کلاس خطای SDK | علت رایج | راهنمای retry |
| --- | --- | --- |
| `APIConnectionError` | مشکل شبکه، proxy، TLS، egress کانتینر یا firewall پیش از رسیدن درخواست به API. | فقط بعد از بررسی سلامت شبکه با backoff retry کنید؛ اگر ادامه داشت پیام connectivity بدهید. |
| `APITimeoutError` | درخواست بیش از حد طول کشیده یا connection پیش از تکمیل بسته شده است. | کارهای idempotent را از state مشخص retry کنید؛ روی هر تلاش `X-Client-Request-Id` بفرستید. |
| `AuthenticationError` | API key وجود ندارد، نامعتبر است، فعال نشده یا revoke شده است. | retry نکنید؛ credential را اصلاح یا rotate کنید. |
| `BadRequestError` | JSON نامعتبر، فیلد الزامی missing، parameter ناسازگار یا input خراب. | بدون تغییر retry نکنید؛ request را با مستندات endpoint تطبیق دهید. |
| `PermissionDeniedError` | key، حساب، tier یا permission مدل اجازه عملیات را نمی‌دهد. | بدون تغییر retry نکنید؛ دسترسی مدل و tier حساب را بررسی کنید. |
| `NotFoundError` | مدل، فایل، batch، response یا resource ID پیدا نشده است. | IDها و سازگاری route را پیش از retry بررسی کنید. |
| `ConflictError` | resource قابل تغییر همزمان تغییر کرده یا در state ناسازگار است. | state را دوباره بخوانید و فقط update مورد نظر را retry کنید. |
| `RateLimitError` | محدودیت request، token، project یا ظرفیت provider رسیده است. | `Retry-After` را رعایت کنید، concurrency یا token را کم کنید و با jitter retry کنید. |
| `InternalServerError` | خطای موقت سرور یا provider upstream. | با backoff نمایی سقف‌دار retry کنید؛ اگر workflow اجازه می‌دهد failover کنید. |
| `UnprocessableEntityError` | request از نظر syntax درست است اما قابل پردازش نیست. | معمولا input را اصلاح کنید یا مدل/route دیگری امتحان کنید؛ blind retry نکنید. |

### ماتریس تصمیم retry

| وضعیت | اقدام |
| --- | --- |
| `429`، `500`، `502`، `503`، `504`، timeout یا قطع connection | با backoff نمایی سقف‌دار، jitter و حداکثر تعداد تلاش retry کنید. |
| هدر `Retry-After` وجود دارد | حداقل همان مقدار صبر کنید و سپس تلاش بعدی را انجام دهید. |
| `400`، `401`، `403`، `404`، `422`، policy error یا unsupported model | بدون تغییر retry نکنید؛ request، key، route، model یا دسترسی حساب را اصلاح کنید. |
| streaming وسط خروجی قطع می‌شود | خروجی partial را نگه دارید و از conversation یا job state مشخص retry کنید. |
| بعد از retryها همچنان شکست می‌خورد | متوقف شوید، شناسه‌ها و metadata امن را log کنید و مسیر fallback یا بررسی انسانی را فعال کنید. |

## انواع خطاهای رایج

### خطاهای احراز هویت (401)

#### `invalid_api_key`
کلید API نامعتبر، منقضی شده، یا معلق است.

```json
{
  "error": {
    "message": "Incorrect API key provided: aa-JEa8wq. You can find your API key at https://chat.avalai.ir/platform/api-keys.",

    "type": "invalid_request_error",
    "param": null,
    "code": "invalid_api_key",
    "solution": "If your API key was recently created, please wait up to 60 seconds for it to activate. Otherwise, verify you're using the correct key and that it hasn't been revoked.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای درخواست نامعتبر (400)

#### `invalid_request_format`
درخواست نادرست یا فاقد پارامترهای مورد نیاز است.

```json
{
  "error": {
    "message": "Your request was malformed or missing some required parameters, such as a token or an input.",
    "type": "invalid_request_format",
    "param": null,
    "code": "invalid_request_format",
    "solution": "Check the https://docs.avalai.ir for the specific API method you are calling and make sure you are sending valid and complete parameters.",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `context_window_exceeded`
طول ورودی از حداکثر پنجره زمینه مدل فراتر رفته است.

```json
{
  "error": {
    "message": "This model's maximum context length is exceeded. Please reduce the length of your prompt or completion.",
    "type": "context_window_exceeded",
    "param": "messages",
    "code": "context_window_exceeded",
    "solution": "The input is too long for this model. Try reducing the length of your input or using a model with a larger context window.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `unsupported_model`
مدل درخواستی برای این endpoint پشتیبانی نمی‌شود.

```json
{
  "error": {
    "message": "The requested model text-embedding-3-small is not supported for '/chat/completions' path. Please use a compatible model.",
    "type": "unsupported_model",
    "param": "model",
    "code": "unsupported_model",
    "solution": "Please check the documentation to see which models are available for this specific endpoint.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `content_policy_violation`
محتوا سیاست‌های حفاظتی را نقض می‌کند.

```json
{
  "error": {
    "message": "Your request was rejected as a result of our safety system. Your prompt may contain text that is not allowed by our safety system.",
    "type": "content_policy_violation",
    "param": null,
    "code": "content_policy_violation",
    "solution": "Please review our content policy guidelines and modify your request to comply with our safety requirements.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای دسترسی (403)

#### `model_access_denied`
به مدل درخواستی دسترسی ندارید.

```json
{
  "error": {
    "message": "model gpt-5.5 does not exists or you don't have access to it, for more information check https://chat.avalai.ir/platform/limits",

    "type": "model_access_denied",
    "param": null,
    "code": "model_access_denied",
    "solution": "Please check https://chat.avalai.ir/platform/limits",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `insufficient_tier`
سطح حساب شما برای دسترسی به این مدل کافی نیست.

```json
{
  "error": {
    "message": "model gpt-5.5 does not exists or you don't have access to it, for more information check https://chat.avalai.ir/platform/limits",

    "type": "insufficient_tier",
    "param": null,
    "code": "insufficient_tier",
    "solution": "Please check https://chat.avalai.ir/platform/limits",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای منابع (404)

#### `resource_not_found`
منبع درخواستی وجود ندارد.

```json
{
  "error": {
    "message": "Requested resource gpt-5 does not exist. for more information check https://chat.avalai.ir/platform/limits",

    "type": "not_found",
    "param": null,
    "code": "resource_not_found",
    "solution": "Please check https://chat.avalai.ir/platform/limits",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای محدودیت نرخ (429)

#### `rate_limit_exceeded`
از محدودیت نرخ درخواست فراتر رفته‌اید.

```json
{
  "error": {
    "message": "Rate limit reached for requests.",
    "type": "rate_limit_exceeded",
    "param": null,
    "code": "rate_limit_exceeded",
    "solution": "Pace your requests or upgrade to higher levels. Read the Rate limit guide at https://chat.avalai.ir/platform/limits",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `quota_exceeded`
اعتبار حساب شما تمام شده است.

```json
{
  "error": {
    "message": "You exceeded your current quota, please check your plan and billing details.",
    "type": "quota_exceeded",
    "param": null,
    "code": "quota_exceeded",
    "solution": "Please check your credit balance at https://chat.avalai.ir/platform/billing",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `insufficient_quota`
اعتبار حساب شما برای تکمیل این درخواست کافی نیست.

```json
{
  "error": {
    "message": "You have insufficient credit to complete this request. Your remaining balance of 0.001 UNIT(s) does not cover the estimated cost.",
    "type": "insufficient_quota",
    "param": null,
    "code": "insufficient_quota",
    "solution": "Please check your credit balance at https://chat.avalai.ir/platform/billing. You may need to add more credits to continue using the service.",

    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای سرور (500)

#### `internal_server_error`
خطای غیرمنتظره در سرور رخ داده است.

```json
{
  "error": {
    "message": "The server encountered an unexpected condition that prevented it from fulfilling the request. Please try again later.",
    "type": "internal_server_error",
    "param": null,
    "code": "internal_server_error",
    "solution": "This is usually a temporary issue on our side. Please retry your request after a brief wait.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `provider_server_error`
خطا در پردازش درخواست توسط ارائه‌دهنده API.

```json
{
  "error": {
    "message": "Error processing your request by the API provider. Please try again later.",
    "type": "provider_server_error",
    "param": null,
    "code": "provider_server_error",
    "solution": "The API provider encountered an error. This could be temporary. Please retry your request.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

### خطاهای عدم دسترسی سرویس (503)

#### `service_unavailable`
سرویس به طور موقت در دسترس نیست.

```json
{
  "error": {
    "message": "The server is currently unable to handle the request due to a temporary overload or maintenance of the server. Please try again later.",
    "type": "service_unavailable",
    "param": null,
    "code": "service_unavailable",
    "solution": "The service is temporarily unavailable. This could be due to high demand or planned maintenance.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

#### `model_overloaded`
مدل درخواستی در حال حاضر دارای بار زیاد است.

```json
{
  "error": {
    "message": "The model gpt-5.5 is currently overloaded. please try again later.",
    "type": "model_overloaded",
    "param": "model",
    "code": "model_overloaded",
    "solution": "The specific model you requested is experiencing high demand. Please try again shortly, or consider using an alternative model.",
    "request_id": "01994ea4-2038-7192-8997-3a3d05ef98d4"
  }
}
```

برای خطاهای overload یا سبک `slow_down`، concurrency را به آخرین سطح پایدار قبلی کاهش دهید، چند دقیقه ثابت نگه دارید، سپس به‌تدریج افزایش دهید. retry loop به‌تنهایی می‌تواند overload را بدتر کند اگر همه workerها هم‌زمان بیدار شوند؛ backoff را با کنترل concurrency در سطح queue ترکیب کنید.

### خطاهای حالت WebSocket در Responses

هنگام استفاده از `/v1/responses` در حالت WebSocket، خطاهای state اتصال را جدا از پاسخ‌های HTTP معمولی مدیریت کنید:

| خطا | معنی | بازیابی |
| --- | --- | --- |
| `previous_response_not_found` | سرور نمی‌تواند `previous_response_id` را از state موجود resolve کند. | با context کامل ورودی retry کنید و `previous_response_id` را `null` بگذارید. |
| `websocket_connection_limit_reached` | connection وب‌سوکت به بیشینه طول عمر خود رسیده است. | یک WebSocket جدید باز کنید و از آخرین state پایدار ادامه دهید. |

checkpointهای conversation را بیرون از socket ذخیره کنید تا reconnect بدون پیش‌نیاز به state حافظه‌ای client امن ادامه پیدا کند.

## بهترین شیوه‌های مدیریت خطا

### پیاده‌سازی منطق تلاش مجدد

برای خطاهای گذرا (مانند 429, 500, 502, 503, 504)، منطق تلاش مجدد را با عقب‌نشینی نمایی پیاده‌سازی کنید. retry را هدفمند نگه دارید:

- خطاهای `429`، `500`، `502`، `503` و `504` را با عقب‌نشینی نمایی سقف‌دار و jitter دوباره تلاش کنید.
- اگر پاسخ `Retry-After` دارد، همان مقدار را رعایت کنید؛ تلاش‌های ناموفق هم از بودجه rate limit مصرف می‌کنند.
- خطاهای احراز هویت، مجوز، اعتبارسنجی، policy یا منبع پیدا نشد را کورکورانه retry نکنید.
- `avalai-request-id`، مدل، route، status code، تعداد retry، latency و metadata امن درخواست را log کنید.
- برای streaming، در صورت قطع میانه جریان، خروجی partial را نگه دارید و از یک state مشخص گفتگو دوباره تلاش کنید.

#### مثال ها

```python
import os
import time
import random
from openai import OpenAI, APIError, RateLimitError

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def make_api_request_with_retry(func, max_retries=5, initial_delay=1, max_delay=60):
    """ارسال درخواست API با منطق retry و عقب‌نشینی نمایی."""
    num_retries = 0
    delay = initial_delay
    last_error = None

    while True:
        try:
            return func()
        except RateLimitError as e:
            last_error = e
            retry_after = int(e.headers.get("retry-after", 0)) if e.headers else 0
            delay = max(retry_after, delay)
        except APIError as e:
            if not (e.status_code and 500 <= e.status_code < 600):
                raise
            last_error = e

        if num_retries >= max_retries:
            raise last_error

        sleep_time = delay + random.uniform(0, 0.5 * delay)
        time.sleep(sleep_time)
        num_retries += 1
        delay = min(delay * 2, max_delay)


# مثال استفاده
def get_chat_completion():
    return client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": "سلام!"}],
    )


try:
    response = make_api_request_with_retry(get_chat_completion)
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Failed after multiple retries: {e}")

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function makeApiRequestWithRetry(
  func,
  maxRetries = 5,
  initialDelay = 1000,
  maxDelay = 60000,
) {
  let numRetries = 0;
  let delay = initialDelay;

  while (true) {
    try {
      return await func();
    } catch (error) {
      // مدیریت خطاهای محدودیت نرخ
      if (error.status === 429) {
        const retryAfter = error.headers?.["retry-after"]
          ? parseInt(error.headers["retry-after"]) * 1000
          : 0;
        delay = Math.max(retryAfter, delay);
      }
      // برای خطاهای کلاینت غیر از 429 تلاش مجدد نکنید
      else if (!error.status || error.status < 500) {
        throw error;
      }

      if (numRetries >= maxRetries) {
        throw error;
      }

      // عقب‌نشینی نمایی با لرزش (jitter)
      const jitter = Math.random() * 0.5 * delay;
      const sleepTime = delay + jitter;
      await new Promise((resolve) => setTimeout(resolve, sleepTime));

      numRetries += 1;
      delay = Math.min(delay * 2, maxDelay);
    }
  }
}

// مثال استفاده
async function getChatCompletion() {
  return client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: "سلام!" }],
  });
}

async function main() {
  try {
    const response = await makeApiRequestWithRetry(getChatCompletion);
    console.log(response.choices[0].message.content);
  } catch (error) {
    console.error("Failed after multiple retries: ", error);
  }
}

main();

```

```bash
#!/bin/bash

# تابع ارسال درخواست API با منطق تلاش مجدد
function make_api_request_with_retry {
  local max_retries=5
  local initial_delay=1
  local max_delay=60
  local num_retries=0
  local delay=$initial_delay

  while true; do
    # ارسال درخواست API
    response=$(curl -s -w "%{http_code}" https://api.avalai.ir/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $AVALAI_API_KEY" \
      -d '{
    "model": "gpt-5.6-luna",
    "messages": [{"role": "user", "content": "سلام!"}]
  }')

    http_code=${response: -3}
    content=${response:0:${#response}-3}

    # بررسی پاسخ
    if [[ $http_code -eq 200 ]]; then
      echo "$content"
      return 0
    elif [[ $http_code -eq 429 ]]; then
      # خطای محدودیت نرخ
      retry_after=$(echo "$content" | grep -o '"retry_after":[0-9]*' | grep -o '[0-9]*')
      if [[ -n $retry_after ]]; then
        delay=$retry_after
      fi
    elif [[ $http_code -lt 500 ]]; then
      # برای خطاهای کلاینت غیر از 429 تلاش مجدد نکنید
      echo "خطای کلاینت: $http_code - $content" >&2
      return 1
    fi

    # بررسی تعداد تلاش‌های مجدد
    if [[ $num_retries -ge $max_retries ]]; then
      echo "حداکثر تلاش‌های مجدد انجام شد: $content" >&2
      return 1
    fi

    # عقب‌نشینی نمایی با لرزش (jitter)
    jitter=$(awk -v delay="$delay" 'BEGIN {srand(); print rand() * 0.5 * delay}')
    sleep_time=$(awk -v delay="$delay" -v jitter="$jitter" 'BEGIN {print delay + jitter}')

    echo "تلاش مجدد در $sleep_time ثانیه..." >&2
    sleep $sleep_time

    num_retries=$((num_retries + 1))
    delay=$((delay < max_delay / 2 ? delay * 2 : max_delay))
  done
}

# استفاده از تابع
result=$(make_api_request_with_retry)
status=$?

if [[ $status -eq 0 ]]; then
  echo "پاسخ دریافت شد:"
  echo "$result" | grep -o '"content":"[^"]*"' | cut -d'"' -f4
else
  echo "خطا در ارسال درخواست: $result"
fi

```

```go
package main

import (
	"context"
	"fmt"
	"io"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/openai/openai-go"
)

// تابع ارسال درخواست API با منطق تلاش مجدد
func makeApiRequestWithRetry(ctx context.Context, fn func() (interface{}, error), maxRetries int, initialDelay, maxDelay time.Duration) (interface{}, error) {
	var numRetries int
	delay := initialDelay

	for {
		// ارسال درخواست API
		result, err := fn()
		if err == nil {
			return result, nil
		}

		// بررسی نوع خطا
		var retryAfter time.Duration
		var shouldRetry bool

		// بررسی خطای محدودیت نرخ
		if apiErr, ok := err.(*openai.APIError); ok {
			if apiErr.HTTPStatusCode == http.StatusTooManyRequests {
				shouldRetry = true
				// استخراج هدر retry-after
				if apiErr.Header != nil {
					if retryAfterStr := apiErr.Header.Get("retry-after"); retryAfterStr != "" {
						if retryAfterSec, err := strconv.Atoi(retryAfterStr); err == nil {
							retryAfter = time.Duration(retryAfterSec) * time.Second
						}
					}
				}
			} else if apiErr.HTTPStatusCode >= 500 {
				// تلاش مجدد برای خطاهای سرور
				shouldRetry = true
			}
		}

		// اگر نباید تلاش مجدد کنیم یا به حداکثر تلاش‌ها رسیده‌ایم
		if !shouldRetry || numRetries >= maxRetries {
			return nil, err
		}

		// استفاده از بیشترین مقدار بین تاخیر فعلی و retry-after
		if retryAfter > delay {
			delay = retryAfter
		}

		// عقب‌نشینی نمایی با لرزش (jitter)
		jitter := time.Duration(rand.Float64() * 0.5 * float64(delay))
		sleepTime := delay + jitter

		fmt.Fprintf(os.Stderr, "تلاش مجدد در %v...\n", sleepTime)

		// انتظار قبل از تلاش مجدد
		select {
		case <-time.After(sleepTime):
		case <-ctx.Done():
			return nil, ctx.Err()
		}

		// افزایش شمارنده و تاخیر
		numRetries++
		delay = time.Duration(math.Min(float64(delay*2), float64(maxDelay)))
	}
}

func main() {
	// تنظیم کلاینت
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// تعریف تابع ارسال درخواست
	getChatCompletion := func() (interface{}, error) {
		return client.CreateChatCompletion(
			context.Background(),
			openai.ChatCompletionRequest{
				model: "gpt-5.6-luna",
				Messages: []openai.ChatCompletionMessage{
					{
						Role:    "user",
						Content: "سلام!",
					},
				},
			},
		)
	}

	// ارسال درخواست با منطق تلاش مجدد
	ctx := context.Background()
	result, err := makeApiRequestWithRetry(ctx, getChatCompletion, 5, 1*time.Second, 60*time.Second)

	if err != nil {
		fmt.Fprintf(os.Stderr, "خطا پس از چندین تلاش: %v\n", err)
		os.Exit(1)
	}

	// نمایش پاسخ
	if resp, ok := result.(openai.ChatCompletionResponse); ok {
		fmt.Println(resp.Choices[0].Message.Content)
	} else {
		fmt.Fprintf(os.Stderr, "نوع پاسخ نامعتبر\n")
	}
}

```

```php
<?php
require 'vendor/autoload.php';

/**
* تابع ارسال درخواست API با منطق تلاش مجدد عقب‌نشینی نمایی
*/
function makeApiRequestWithRetry($func, $maxRetries = 5, $initialDelay = 1, $maxDelay = 60) {
  $numRetries = 0;
  $delay = $initialDelay;

  while (true) {
    try {
      return $func();
    } catch (\Exception $e) {
      // بررسی خطای محدودیت نرخ
      $isRateLimitError = false;
      $retryAfter = 0;

      if (method_exists($e, 'getResponse')) {
        $response = $e->getResponse();
        if ($response && $response->getStatusCode() === 429) {
          $isRateLimitError = true;
          $headers = $response->getHeaders();
          if (isset($headers['Retry-After'][0])) {
            $retryAfter = (int)$headers['Retry-After'][0];
          }
        }
      }

      // برای خطاهای کلاینت غیر از محدودیت نرخ تلاش مجدد نکنید
      $statusCode = method_exists($e, 'getCode') ? $e->getCode() : 0;
      if (!$isRateLimitError && ($statusCode < 500 || $statusCode === 0)) {
        throw $e;
      }

      if ($numRetries >= $maxRetries) {
        throw $e;
      }

      // تنظیم تاخیر بر اساس هدر retry-after
      if ($retryAfter > 0) {
        $delay = max($retryAfter, $delay);
      }

      // عقب‌نشینی نمایی با لرزش (jitter)
      $jitter = mt_rand() / mt_getrandmax() * 0.5 * $delay;
      $sleepTime = $delay + $jitter;

      error_log("تلاش مجدد در {$sleepTime} ثانیه...");
      sleep($sleepTime);

      $numRetries++;
      $delay = min($delay * 2, $maxDelay);
    }
  }
}

// تنظیم کلاینت
$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

// تعریف تابع ارسال درخواست
$getChatCompletion = function() use ($client) {
  return $client->chat()->create([
  'model' => 'gpt-5.6-luna',
  'messages' => [
  ['role' => 'user', 'content' => 'سلام!'],
  ],
  ]);
};

// استفاده از تابع با منطق تلاش مجدد
try {
  $response = makeApiRequestWithRetry($getChatCompletion);
  echo $response->choices[0]->message->content;
} catch (\Exception $e) {
  echo "خطا پس از چندین تلاش: " . $e->getMessage();
}
?>

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
    input="سلام!",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "سلام!",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "سلام!",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مدیریت انواع خطاهای خاص

مدیریت خاصی را برای انواع خطاهای مختلف پیاده‌سازی کنید:

```python
import os
from openai import (
    OpenAI,
    APIError,
    RateLimitError,
    AuthenticationError,
    PermissionDeniedError,
)

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

try:
    response = client.chat.completions.create(
        model="gpt-5.6-luna", messages=[{"role": "user", "content": "سلام!"}]
    )
except AuthenticationError as e:
    print(f"Authentication error: {e}. Please check your API key.")
except PermissionDeniedError as e:
    print(f"Permission error: {e}. Please check your access permissions.")
except RateLimitError as e:
    print(
        f"Rate limit exceeded: {e}. Please try again later or reduce request frequency."
    )
    # پیاده‌سازی منطق تلاش مجدد با عقب‌نشینی نمایی
except APIError as e:
    if e.status_code == 404:
        print(f"Resource not found: {e}. Please check the requested resource exists.")
    elif e.status_code == 400:
        print(f"Bad request: {e}. Please check your request parameters.")
    elif 500 <= e.status_code < 600:
        print(f"Server error: {e}. Please try again later.")
    else:
        print(f"API error: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
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


### اعتبارسنجی ورودی قبل از ارسال

پارامترهای ورودی را قبل از ارسال درخواست‌ها برای جلوگیری از خطاهای قابل پیش‌بینی اعتبارسنجی کنید:

```python
def validate_chat_completion_params(model, messages, temperature=None):
    errors = []

    # اعتبارسنجی مدل
    if not model:
        errors.append("پارامتر مدل الزامی است")

    # اعتبارسنجی پیام‌ها
    if not messages:
        errors.append("آرایه پیام‌ها الزامی است و نمی‌تواند خالی باشد")
    else:
        for i, msg in enumerate(messages):
            if "role" not in msg:
                errors.append(f"پیام در اندیس {i} فاقد 'role' است")
            if (
                "content" not in msg
                and "function_call" not in msg
                and "tool_calls" not in msg
            ):
                errors.append(
                    f"پیام در اندیس {i} فاقد 'content' یا فراخوانی تابع/ابزار است"
                )

    # اعتبارسنجی دما
    if temperature is not None and (temperature < 0 or temperature > 2):
        errors.append("دما باید بین ۰ و ۲ باشد")

    return errors


# مثال استفاده
model = "gpt-5.6-luna"
messages = [{"role": "user", "content": "سلام!"}]
temperature = 0.7

validation_errors = validate_chat_completion_params(model, messages, temperature)
if validation_errors:
    print("Validation errors:", validation_errors)
# مدیریت خطاهای اعتبارسنجی
else:
    # ادامه با فراخوانی API
    response = client.chat.completions.create(
        model=model, messages=messages, temperature=temperature
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
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="سلام!",
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


### پیاده‌سازی قطع‌کننده‌های مدار (Circuit Breakers)

برای برنامه‌های عملیاتی، الگوی قطع‌کننده مدار را برای جلوگیری از شکست‌های آبشاری پیاده‌سازی کنید:

```python
import time
from functools import wraps


class CircuitBreaker:
    def __init__(self, failure_threshold=5, recovery_timeout=30, name="default"):
        self.failure_threshold = failure_threshold
        self.recovery_timeout = recovery_timeout
        self.name = name
        self.failures = 0
        self.last_failure_time = None
        self.state = "CLOSED"  # CLOSED, OPEN, HALF-OPEN

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            if self.state == "OPEN":
                if time.time() - self.last_failure_time > self.recovery_timeout:
                    self.state = "HALF-OPEN"
                    self.failures = 0  # Reset failures when entering HALF-OPEN state
                else:
                    raise Exception(
                        f"Circuit breaker '{self.name}' is OPEN. Retry after {self.recovery_timeout - (time.time() - self.last_failure_time):.1f} seconds"
                    )

            try:
                result = func(*args, **kwargs)
                if self.state == "HALF-OPEN":
                    self.state = "CLOSED"
                    self.failures = 0
                return result
            except Exception as e:
                self.failures += 1
                self.last_failure_time = time.time()
                if self.failures >= self.failure_threshold:
                    self.state = "OPEN"
                raise Exception(
                    f"Circuit breaker '{self.name}' error: {str(e)}. Failures: {self.failures}/{self.failure_threshold}"
                )

        return wrapper


# Usage example
@CircuitBreaker(failure_threshold=3, recovery_timeout=60, name="chat_completions")
def get_chat_completion(prompt):
    return client.chat.completions.create(
        model="gpt-4",  # Fixed model name from "gpt-5.6-luna" to "gpt-4"
        messages=[{"role": "user", "content": prompt}],
    )


# Example usage with better error handling
def main():
    try:
        response = get_chat_completion("سلام!")
        print(response.choices[0].message.content)
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gpt-4` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


### ثبت وقایع و نظارت

ثبت وقایع و نظارت جامعی را برای پیگیری خطاهای API پیاده‌سازی کنید:

```python
import json
import logging
import os
from openai import OpenAI, APIError

# پیکربندی ثبت وقایع
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    handlers=[logging.FileHandler("api_errors.log"), logging.StreamHandler()],
)
logger = logging.getLogger("avalai_api")

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def log_api_request(method, endpoint, params, response=None, error=None):
    """ثبت جزئیات درخواست API."""
    log_data = {
        "method": method,
        "endpoint": endpoint,
        "params": params,
    }

    if response:
        log_data["status_code"] = 200
        log_data["response_id"] = getattr(response, "id", None)
        logger.info(f"API Request Successful: {json.dumps(log_data)}")

    if error:
        log_data["error_type"] = getattr(error, "type", type(error).__name__)
        log_data["error_message"] = str(error)
        log_data["status_code"] = getattr(error, "status_code", None)
        logger.error(f"API Request Failed: {json.dumps(log_data)}")

    # مثال استفاده
    try:
        params = {
            "model": "gpt-5.6-luna",
            "messages": [{"role": "user", "content": "سلام!"}],
        }

        response = client.chat.completions.create(**params)
        log_api_request("POST", "/chat/completions", params, response=response)
        print(response.choices[0].message.content)
    except APIError as e:
        log_api_request("POST", "/chat/completions", params, error=e)
        raise
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


## مدیریت پاسخ‌های جریانی (Streaming)

هنگام استفاده از پاسخ‌های جریانی، مدیریت خطای مناسب را پیاده‌سازی کنید:

```python
import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

partial_output = []

try:
    stream = client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": "یک داستان کوتاه درباره ربات بنویس."}],
        stream=True,
    )

    for chunk in stream:
        content = chunk.choices[0].delta.content
        if content:
            partial_output.append(content)
            sys.stdout.write(content)
            sys.stdout.flush()

except Exception as e:
    print(f"\nخطا هنگام streaming: {e}")
    # partial_output را نگه دارید تا بتوانید از state مشخص retry کنید.
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
    input="یک داستان کوتاه درباره ربات بنویس.",
    stream=True,
)

partial_output = []
try:
    for event in response:
        if event.type == "response.output_text.delta":
            partial_output.append(event.delta)
            print(event.delta, end="", flush=True)
except Exception as e:
    print(f"\nخطا هنگام streaming: {e}")
    # partial_output را ذخیره کنید و از state مشخص retry کنید.
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## مدیریت خطا در برنامه‌های عملیاتی

برای برنامه‌های عملیاتی، پیاده‌سازی این شیوه‌های اضافی را در نظر بگیرید:

1. **مدیریت خطای متمرکز**: یک سیستم مدیریت خطای متمرکز برای پردازش و پاسخ مداوم به خطاها ایجاد کنید.
2. **گزارش‌دهی خطا**: با سرویس‌های گزارش‌دهی خطا مانند Sentry یا Rollbar برای پیگیری و تحلیل خطاها ادغام شوید.
3. **بررسی‌های سلامت**: بررسی‌های سلامت را برای نظارت بر در دسترس بودن API پیاده‌سازی کنید.
4. **مکانیسم‌های جایگزین**: مکانیسم‌های جایگزینی را برای ویژگی‌های حیاتی در صورت عدم دسترسی به API توسعه دهید.
5. **پیام‌های خطای کاربرپسند**: پیام‌های خطای فنی را به زبان کاربرپسند ترجمه کنید.

## خطاهای رایج و راه‌حل‌ها

| کد خطا | نوع خطا | علل احتمالی | راه‌حل‌ها |
|---------|----------|----------------|-----------|
| `invalid_api_key` | احراز هویت | کلید API نامعتبر، منقضی یا معلق شده | کلید API خود را در https://chat.avalai.ir/platform/api-keys بررسی کنید |
| `invalid_request_format` | درخواست نامعتبر | درخواست نادرست یا فاقد پارامترهای مورد نیاز | مستندات API را در https://docs.avalai.ir بررسی کنید |
| `context_window_exceeded` | درخواست نامعتبر | ورودی بیش از حد طولانی برای پنجره زمینه مدل | طول ورودی را کاهش دهید یا مدلی با پنجره زمینه بزرگتر استفاده کنید |
| `unsupported_model` | درخواست نامعتبر | مدل برای این endpoint پشتیبانی نمی‌شود | لیست مدل‌های پشتیبانی شده را در مستندات بررسی کنید |
| `content_policy_violation` | درخواست نامعتبر | محتوا سیاست‌های امنیتی را نقض می‌کند | پرامپت خود را برای مطابقت با سیاست‌های محتوا اصلاح کنید |
| `model_access_denied` | دسترسی | به مدل درخواستی دسترسی ندارید | وضعیت حساب خود را در https://chat.avalai.ir/platform/limits بررسی کنید |
| `insufficient_tier` | دسترسی | سطح حساب برای این مدل کافی نیست | حساب خود را ارتقا دهید یا از مدل مناسب سطح خود استفاده کنید |
| `resource_not_found` | منبع یافت نشد | منبع یا مدل درخواستی وجود ندارد | نام مدل را برای اشتباهات تایپی بررسی کنید |
| `rate_limit_exceeded` | محدودیت نرخ | درخواست‌های بیش از حد در مدت زمان کوتاه | منطق تلاش مجدد با عقب‌نشینی نمایی پیاده‌سازی کنید |
| `quota_exceeded` | محدودیت نرخ | سهمیه حساب تمام شده است | موجودی حساب را در https://chat.avalai.ir/platform/billing بررسی کنید |
| `insufficient_quota` | محدودیت نرخ | اعتبار کافی برای تکمیل درخواست نیست | اعتبار حساب خود را شارژ کنید |
| `internal_server_error` | خطای سرور | خطای غیرمنتظره در سرور | کمی صبر کنید و دوباره تلاش کنید |
| `provider_server_error` | خطای سرور | خطا در ارائه‌دهنده API | از مدل دیگری استفاده کنید یا بعدا تلاش کنید |
| `service_unavailable` | سرویس در دسترس نیست | سرویس موقتا در دسترس نیست | کمی صبر کنید و دوباره تلاش کنید |
| `model_overloaded` | سرویس در دسترس نیست | مدل دارای بار زیاد است | از مدل جایگزین استفاده کنید یا بعدا تلاش کنید |

### نکات مهم برای عیب‌یابی

1. **همیشه شناسه درخواست (request_id) را ذخیره کنید** - این شناسه برای پیگیری مسائل با تیم پشتیبانی ضروری است
2. **پیام‌های خطا را کامل بخوانید** - اکثر پیام‌های خطا شامل راهنمایی‌های مفیدی برای حل مسئله هستند
3. **فیلد solution را بررسی کنید** - بسیاری از خطاها شامل راه‌حل‌های پیشنهادی هستند
4. **در صورت نیاز با پشتیبانی تماس بگیرید** - support@avalai.ir با ذکر شناسه درخواست

## نتیجه‌گیری

مدیریت خطای مناسب برای ساخت برنامه‌های پایدار با API AvalAI ضروری است. با پیاده‌سازی استراتژی‌های ذکر شده در این راهنما، می‌توانید برنامه‌های مقاوم‌تری ایجاد کنید که به خوبی خطاها را مدیریت کرده و تجربه کاربری بهتری را ارائه می‌دهند.

به یاد داشته باشید که انواع و کدهای خطای خاص ممکن است با توسعه API در طول زمان تکامل یابند. همیشه برای آخرین اطلاعات در مورد مدیریت خطا به به‌روزترین مستندات مراجعه کنید.
