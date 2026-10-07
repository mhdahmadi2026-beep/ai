# مرجع API کاربر (User API)

API کاربر دسترسی برنامه‌نویسی به اطلاعات حساب، موجودی اعتبار و تاریخچه تراکنش‌ها را فراهم می‌کند. از این نقاط پایانی برای نظارت بر مصرف، پیگیری هزینه‌ها و دریافت داده‌های دقیق هزینه برای فراخوانی‌های API استفاده کنید.

## آدرس پایه (Base URL)

```
https://api.avalai.ir/user/v1
```

## نمای کلی

API کاربر امکانات زیر را به شما می‌دهد:

- **نظارت بر مصرف اعتبار** - بررسی موجودی باقیمانده و منابع اعتبار
- **پیگیری استفاده از API** - لیست و فیلتر تراکنش‌ها با پارامترهای انعطاف‌پذیر
- **تحلیل هزینه‌ها** - دریافت آمار تجمیعی بر اساس مدل، ارائه‌دهنده، روز یا کلید API
- **جستجوی تراکنش‌ها** - دریافت تراکنش‌های خاص با شناسه درخواست برای داده‌های دقیق هزینه

### نگهداری داده‌ها

> **مهم:** رکوردهای تراکنش حداقل به مدت **۹۰ روز** در دسترس هستند. تضمینی برای دسترسی به داده‌های تراکنش پس از ۳ ماه وجود ندارد. اگر نیاز به نگهداری داده‌های هزینه برای مدت طولانی‌تر دارید، لطفا جزئیات تراکنش را در پایگاه داده خود ذخیره کنید.

### ویژگی‌های کلیدی

| ویژگی | توضیحات |
|-------|---------|
| **داده‌های اعتبار بلادرنگ** | اطلاعات اعتبار همیشه به‌روز است |
| **فیلتر انعطاف‌پذیر** | فیلتر تراکنش‌ها بر اساس مدل، ارائه‌دهنده، بازه زمانی و موارد دیگر |
| **آمار تجمیعی** | دریافت داده‌های خلاصه گروه‌بندی شده بر اساس روز، مدل، ارائه‌دهنده یا کلید API |
| **جستجوی دسته‌ای** | دریافت تا ۱۰۰۰ تراکنش در یک درخواست |
| **پیگیری دقیق هزینه** | دریافت جزئیات دقیق هزینه برای هر درخواست API با شناسه درخواست |
| **نگهداری ۹۰ روزه** | رکوردهای تراکنش حداقل ۹۰ روز در دسترس هستند |

## احراز هویت

تمام نقاط پایانی API کاربر نیاز به احراز هویت با توکن Bearer و کلید API AvalAI دارند.

```bash
# تنظیم کلید API
export AVALAI_API_KEY="your-avalai-api-key"

# نمونه درخواست
curl -X GET "https://api.avalai.ir/user/v1/credit" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
from openai import OpenAI
import requests

# استفاده از requests برای API کاربر
api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

response = requests.get("https://api.avalai.ir/user/v1/credit", headers=headers)
print(response.json())

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const apiKey = process.env.AVALAI_API_KEY;

const response = await fetch("https://api.avalai.ir/user/v1/credit", {
  method: "GET",
  headers: {
    Authorization: `Bearer ${apiKey}`,
    "Content-Type": "application/json",
  },
});

const data = await response.json();
console.log(data);

```

```go
// مثال Go
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/credit", nil)
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}

```

```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$ch = curl_init();
curl_setopt($ch, CURLOPT_URL, 'https://api.avalai.ir/user/v1/credit');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
print_r($data);
?>

```


### خطاهای احراز هویت

| کد وضعیت | خطا | توضیحات |
|----------|-----|---------|
| 401 | `unauthorized` | کلید API موجود نیست یا نامعتبر است |
| 403 | `forbidden` | حساب کاربری معلق یا غیرفعال است |

## محدودیت نرخ (Rate Limiting)

نقاط پایانی `/user/v1` محدودیت نرخ را برای هر کاربر بر اساس سطح حساب اعمال می‌کنند.

### محدودیت نرخ `/user/v1` بر اساس سطح

| سطح حساب | محدودیت درخواست |
|-----------|-----------------|
| سطح پایه (سطح ۰) | ۳ درخواست در دقیقه |
| سطح ۱ | ۱۵ درخواست در دقیقه |
| سطح ۲ | ۵۰ درخواست در دقیقه |
| سطح ۳ | ۱۵۰ درخواست در دقیقه |
| سطح ۴ | ۳۵۰ درخواست در دقیقه |
| سطح ۵ | ۷۵۰ درخواست در دقیقه |

### هدرهای محدودیت نرخ

هر پاسخ شامل اطلاعات محدودیت نرخ است:

| هدر | توضیحات |
|-----|---------|
| `x-ratelimit-limit-requests` | حداکثر درخواست در دقیقه |
| `x-ratelimit-remaining-requests` | درخواست‌های باقیمانده در پنجره فعلی |
| `x-ratelimit-reset-requests` | ثانیه تا بازنشانی محدودیت نرخ |

### پاسخ عبور از محدودیت نرخ

```json
{
  "error": "rate_limit_exceeded",
  "message": "Rate limit exceeded. Try again in 45 seconds."
}
```

---

## نقاط پایانی (Endpoints)

### GET /credit

دریافت موجودی اعتبار فعلی، محدودیت‌ها و منابع اعتبار.

**آدرس:** `GET https://api.avalai.ir/user/v1/credit`

#### درخواست

```bash
curl -X GET "https://api.avalai.ir/user/v1/credit" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
import requests

api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}"}

response = requests.get("https://api.avalai.ir/user/v1/credit", headers=headers)
credit_info = response.json()
print(f"اعتبار باقیمانده: {credit_info['remaining_irt']} تومان")
print(f"سطح حساب: {credit_info['account_tier']}")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const response = await fetch("https://api.avalai.ir/user/v1/credit", {
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
});

const creditInfo = await response.json();
console.log(`اعتبار باقیمانده: ${creditInfo.remaining_irt} تومان`);
console.log(`سطح حساب: ${creditInfo.account_tier}`);

```

```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

type CreditResponse struct {
	Limit        float64 `json:"limit"`
	RemainingIRT float64 `json:"remaining_irt"`
	AccountTier  int     `json:"account_tier"`
}

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/credit", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var credit CreditResponse
	json.NewDecoder(resp.Body).Decode(&credit)
	fmt.Printf("اعتبار باقیمانده: %.2f تومان\n", credit.RemainingIRT)
}

```

```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$ch = curl_init('https://api.avalai.ir/user/v1/credit');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . $apiKey]);

$response = curl_exec($ch);
curl_close($ch);

$credit = json_decode($response, true);
echo "اعتبار باقیمانده: " . $credit['remaining_irt'] . " تومان\n";
echo "سطح حساب: " . $credit['account_tier'] . "\n";
?>

```


#### پاسخ

```json
{
  "limit": 0.0,
  "remaining_irt": 742927.85,
  "remaining_unit": 0.0,
  "total_unit": 6.44622863340564,
  "exchange_rate": 115250,
  "account_tier": 5,
  "credit_sources": {
    "grants": [],
    "packages": [
      {
        "id": "25",
        "template_id": "d-o3050s",
        "name": "مدل‌های زبانی منتخب OpenAI روزانه پایه",
        "description": "٪۴۰ تخفیف در مدل‌های منتخب OpenAI",
        "amount_irt": "500000.00",
        "remaining_irt": "498447.15",
        "end_date": "2025-11-27T15:05:07.404882+00:00",
        "allowed_services": [
          "api"
        ],
        "scope_details": {
          "api": [
            "gpt-5-chat",
            "gpt-5-mini",
            "gpt-5.6-luna",
            "gpt-5.4-mini",
            "o4-mini",
            "o3-mini"
          ]
        }
      }
    ]
  }
}
```

#### فیلدهای پاسخ

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `limit` | float | حد کل اعتبار به تومان |
| `remaining_irt` | float | اعتبار باقیمانده به تومان |
| `remaining_unit` | float | اعتبار باقیمانده به واحد (دلار) |
| `total_unit` | float | کل اعتبار به واحد |
| `exchange_rate` | int | نرخ تبدیل فعلی تومان به واحد (دلار) |
| `account_tier` | int | سطح حساب (۰-۵)، بر محدودیت نرخ تاثیر می‌گذارد |
| `credit_sources` | object | جزئیات منابع اعتبار |
| `credit_sources.grants` | array | گرنت‌های فعال |
| `credit_sources.packages` | array | بسته‌های فعال |

#### فیلدهای منبع اعتبار

**گرنت:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه یکتای گرنت |
| `description` | string | توضیحات گرنت |
| `amount_irt` | string | مبلغ کل گرنت به تومان |
| `remaining_irt` | string | مبلغ باقیمانده به تومان |
| `end_date` | string | تاریخ انقضا (ISO 8601) |
| `allowed_services` | array | سرویس‌هایی که این گرنت برای آن‌ها قابل استفاده است |
| `scope_details` | object | محدودیت‌های مدل/ارائه‌دهنده |

**بسته:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه یکتای بسته |
| `template_id` | string | شناسه قالب بسته |
| `name` | string | نام بسته |
| `description` | string | توضیحات بسته |
| `amount_irt` | string | مبلغ کل بسته به تومان |
| `remaining_irt` | string | مبلغ باقیمانده به تومان |
| `end_date` | string | تاریخ انقضا (ISO 8601) |
| `allowed_services` | array | سرویس‌هایی که این بسته برای آن‌ها قابل استفاده است |
| `scope_details` | object | محدودیت‌های مدل/ارائه‌دهنده |

---

### GET /transactions

دریافت لیست صفحه‌بندی شده از تراکنش‌های API شما.

**آدرس:** `GET https://api.avalai.ir/user/v1/transactions`

#### پارامترهای کوئری

| پارامتر | نوع | پیش‌فرض | توضیحات |
|---------|-----|---------|---------|
| `hours_ago` | int | 24 | ساعت‌های قبل برای بررسی (۱-۷۲۰). اگر تاریخ‌ها ارائه شوند نادیده گرفته می‌شود. |
| `start_date` | string | - | تاریخ شروع (YYYY-MM-DD). نیاز به `end_date` دارد. |
| `end_date` | string | - | تاریخ پایان (YYYY-MM-DD). نیاز به `start_date` دارد. |
| `page` | int | 1 | شماره صفحه (۱-۱۰۰۰۰) |
| `page_size` | int | 100 | تعداد آیتم در هر صفحه (۱-۱۰۰۰) |
| `safety_identifier` | string | - | فیلتر بر اساس شناسه داخلی شما |
| `api_key_id` | int | - | فیلتر بر اساس شناسه کلید API خاص |
| `model` | string | - | فیلتر بر اساس نام مدل (تطابق جزئی) |
| `provider` | string | - | فیلتر بر اساس نام ارائه‌دهنده |
| `status_code` | int | - | فیلتر بر اساس کد وضعیت HTTP |
#### مثال‌ها

```bash
# ۲۴ ساعت گذشته (پیش‌فرض)
curl -X GET "https://api.avalai.ir/user/v1/transactions" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# ۷ روز گذشته
curl -X GET "https://api.avalai.ir/user/v1/transactions?hours_ago=168" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# بازه تاریخی مشخص
curl -X GET "https://api.avalai.ir/user/v1/transactions?start_date=2025-01-01&end_date=2025-01-07" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# فیلتر بر اساس مدل
curl -X GET "https://api.avalai.ir/user/v1/transactions?model=gpt-5.5&page_size=50" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
import requests

api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}"}

# ۲۴ ساعت گذشته (پیش‌فرض)
response = requests.get("https://api.avalai.ir/user/v1/transactions", headers=headers)

# با فیلترها
response = requests.get(
    "https://api.avalai.ir/user/v1/transactions",
    headers=headers,
    params={"model": "gpt-5.6-luna", "hours_ago": 168, "page_size": 50},  # ۷ روز گذشته
)

transactions = response.json()
for tx in transactions["transactions"]:
    print(f"{tx['id']}: {tx['model']} - {tx['tokens']['total']} توکن")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const apiKey = process.env.AVALAI_API_KEY;

// با فیلترها
const params = new URLSearchParams({
  model: "gpt-5.6-luna",
  hours_ago: "168",
  page_size: "50",
});

const response = await fetch(
  `https://api.avalai.ir/user/v1/transactions?${params}`,
  {
    headers: { Authorization: `Bearer ${apiKey}` },
  },
);

const data = await response.json();
data.transactions.forEach((tx) => {
  console.log(`${tx.id}: ${tx.model} - ${tx.tokens.total} توکن`);
});

```

```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"net/url"
	"os"
)

func main() {
	baseURL := "https://api.avalai.ir/user/v1/transactions"
	params := url.Values{}
	params.Add("model", "gpt-5.6-luna")
	params.Add("hours_ago", "168")
	params.Add("page_size", "50")

	req, _ := http.NewRequest("GET", baseURL+"?"+params.Encode(), nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("تعداد کل تراکنش‌ها: %v\n", result["total"])
}

```

```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

$params = http_build_query([
    'model' => 'gpt-5.6-luna',
    'hours_ago' => 168,
    'page_size' => 50
]);

$ch = curl_init('https://api.avalai.ir/user/v1/transactions?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . $apiKey]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
foreach ($data['transactions'] as $tx) {
    echo $tx['id'] . ': ' . $tx['model'] . ' - ' . $tx['tokens']['total'] . " توکن\n";
}
?>

```


#### پاسخ

```json
{
  "transactions": [
    {
      "id": "019ac1c0-9ff3-7663-b0b9-fbcf2461939a",
      "created_at": "2025-11-26T20:06:23.442Z",
      "requested_at": "2025-11-26T20:00:18.031Z",
      "safety_identifier": null,
      "model": "gpt-5.4-mini",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {
        "total": 30,
        "prompt": 10,
        "completion": 20,
        "reasoning": 0,
        "cached": 0
      }
    }
  ],
  "total": 100,
  "page": 1,
  "page_size": 100,
  "has_more": false
}
```

#### فیلدهای تراکنش

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه یکتای تراکنش (UUID v7) - همان هدر `avalai-request-id` |
| `created_at` | string | زمان پردازش هزینه تراکنش - زمانی که تراکنش پردازش شده و هزینه آن محاسبه شده (ISO 8601) |
| `requested_at` | string | زمان شروع درخواست (ISO 8601) |
| `model` | string | مدل استفاده شده (مثلا "gpt-5.4") |
| `provider` | string | نام ارائه‌دهنده (مثلا "openai", "anthropic") |
| `status_code` | int | کد وضعیت HTTP پاسخ |
| `stream` | bool | آیا درخواست از استریمینگ استفاده کرده |
| `tokens.total` | int | کل توکن‌های استفاده شده |
| `tokens.prompt` | int | توکن‌های ورودی |
| `tokens.completion` | int | توکن‌های خروجی |
| `tokens.reasoning` | int | توکن‌های استدلال (مدل‌های o1/o3) |
| `tokens.cached` | int | توکن‌های کش شده (کش پرامپت) |
| `safety_identifier` | string | شناسه داخلی شما (در صورت ارائه) |

---

### POST /transactions/lookup

جستجوی تراکنش‌های خاص با UUID آن‌ها. این نقطه پایانی کلیدی برای **پیگیری دقیق هزینه** است - از `avalai-request-id` در هدرهای پاسخ API برای دریافت جزئیات دقیق هزینه استفاده کنید.

**آدرس:** `POST https://api.avalai.ir/user/v1/transactions/lookup`

> **مهم برای نمایندگان فروش:** این نقطه پایانی **هزینه دقیق** هر درخواست API را برمی‌گرداند که ۱۰۰٪ دقیق است و حداکثر ۳۰ ثانیه پس از اتمام درخواست در دسترس است. برای یک گردش کار کامل به [راهنمای پیگیری هزینه نمایندگان](fa/resellers/cost-tracking-guide.md) مراجعه کنید.

#### دریافت شناسه درخواست از SDK ها

هنگام استفاده از SDK های رسمی مانند OpenAI Python SDK، هدر `avalai-request-id` به طور خودکار ذخیره شده و از طریق شیء پاسخ در دسترس قرار می‌گیرد. در اینجا نحوه دسترسی به آن در SDK های مختلف آمده است:

**پایتون (OpenAI SDK)**

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[{"role": "user", "content": "سلام!"}],
)

# دسترسی به شناسه درخواست از شیء پاسخ
request_id = response._request_id
print(f"شناسه درخواست: {request_id}")

# اکنون می‌توانید از این request_id برای جستجوی هزینه تراکنش استفاده کنید
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


> **توجه:** ویژگی `_request_id` در تمام اشیاء پاسخ برگردانده شده توسط OpenAI SDK هنگام پیکربندی با آدرس پایه AvalAI در دسترس است. این شامل پاسخ‌های chat completions، embeddings، تصاویر و سایر نقاط پایانی می‌شود.

**سایر SDK ها**

برای SDK در زبان‌های دیگر، معمولا باید مستقیما به هدرهای پاسخ دسترسی پیدا کنید:

| SDK | روش دسترسی به شناسه درخواست |
|-----|----------------------------|
| پایتون (OpenAI) | `response._request_id` |
| پایتون (requests) | `response.headers.get("avalai-request-id")` |
| جاوااسکریپت (fetch) | `response.headers.get("avalai-request-id")` |
| Go (net/http) | `resp.Header.Get("avalai-request-id")` |
| PHP (curl) | استخراج از هدرهای پاسخ |

#### بدنه درخواست

| فیلد | نوع | الزامی | توضیحات |
|------|-----|--------|---------|
| `transaction_ids` | array | بله | لیست UUID تراکنش‌ها (۱-۱۰۰۰) |

#### مثال

```bash
# ابتدا یک فراخوانی API انجام دهید و هدر avalai-request-id را ذخیره کنید
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.4-mini",
    "messages": [{"role": "user", "content": "سلام!"}]
  }'

# هدرهای پاسخ شامل موارد زیر خواهد بود:
# avalai-request-id: 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a

# سپس تراکنش را جستجو کنید (حداکثر ۳۰ ثانیه صبر کنید برای پردازش)
curl -X POST "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]
  }'

```

```python
# مثال پایتون (Python)
import requests
import time

api_key = "your-avalai-api-key"
headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}

# مرحله ۱: یک فراخوانی API انجام دهید و avalai-request-id را ذخیره کنید
response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers=headers,
    json={"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام!"}]},
)

# دریافت شناسه درخواست از هدرهای پاسخ
request_id = response.headers.get("avalai-request-id")
print(f"شناسه درخواست: {request_id}")

# مرحله ۲: صبر کنید برای پردازش (حداکثر ۳۰ ثانیه)
time.sleep(5)  # معمولا خیلی زودتر در دسترس است

# مرحله ۳: جستجوی تراکنش برای هزینه دقیق
lookup_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers=headers,
    json={"transaction_ids": [request_id]},
)

transaction = lookup_response.json()
if transaction["summary"]["found"] > 0:
    tx = transaction["transactions"][0]
    print(f"هزینه دقیق: {tx['cost']['unit']} دلار")
    print(f"هزینه دقیق: {tx['cost']['paid_irt']} تومان")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const apiKey = process.env.AVALAI_API_KEY;
const headers = {
  Authorization: `Bearer ${apiKey}`,
  "Content-Type": "application/json",
};

// مرحله ۱: یک فراخوانی API انجام دهید و avalai-request-id را ذخیره کنید
const chatResponse = await fetch("https://api.avalai.ir/v1/chat/completions", {
  method: "POST",
  headers,
  body: JSON.stringify({
    model: "gpt-5.4-mini",
    messages: [{ role: "user", content: "سلام!" }],
  }),
});

// دریافت شناسه درخواست از هدرهای پاسخ
const requestId = chatResponse.headers.get("avalai-request-id");
console.log(`شناسه درخواست: ${requestId}`);

// مرحله ۲: صبر کنید برای پردازش
await new Promise((resolve) => setTimeout(resolve, 5000));

// مرحله ۳: جستجوی تراکنش برای هزینه دقیق
const lookupResponse = await fetch(
  "https://api.avalai.ir/user/v1/transactions/lookup",
  {
    method: "POST",
    headers,
    body: JSON.stringify({ transaction_ids: [requestId] }),
  },
);

const data = await lookupResponse.json();
if (data.summary.found > 0) {
  const tx = data.transactions[0];
  console.log(`هزینه دقیق: ${tx.cost.unit} دلار`);
  console.log(`هزینه دقیق: ${tx.cost.paid_irt} تومان`);
}

```

```go
// مثال Go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"time"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// مرحله ۱: یک فراخوانی API انجام دهید
	chatBody, _ := json.Marshal(map[string]interface{}{
		"model":    "gpt-5.4-mini",
		"messages": []map[string]string{{"role": "user", "content": "سلام!"}},
	})

	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(chatBody))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, _ := (&http.Client{}).Do(req)
	requestID := resp.Header.Get("avalai-request-id")
	resp.Body.Close()
	fmt.Printf("شناسه درخواست: %s\n", requestID)

	// مرحله ۲: صبر کنید برای پردازش
	time.Sleep(5 * time.Second)

	// مرحله ۳: جستجوی تراکنش
	lookupBody, _ := json.Marshal(map[string]interface{}{
		"transaction_ids": []string{requestID},
	})

	req, _ = http.NewRequest("POST", "https://api.avalai.ir/user/v1/transactions/lookup", bytes.NewBuffer(lookupBody))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, _ = (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("نتیجه: %+v\n", result)
}

```

```php
<?php
// مثال PHP
$apiKey = getenv('AVALAI_API_KEY');

// مرحله ۱: یک فراخوانی API انجام دهید و avalai-request-id را ذخیره کنید
$ch = curl_init('https://api.avalai.ir/v1/chat/completions');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HEADER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'model' => 'gpt-5.4-mini',
    'messages' => [['role' => 'user', 'content' => 'سلام!']]
]));

$response = curl_exec($ch);
$headerSize = curl_getinfo($ch, CURLINFO_HEADER_SIZE);
$headers = substr($response, 0, $headerSize);
curl_close($ch);

// استخراج avalai-request-id از هدرها
preg_match('/avalai-request-id:\s*([^\r\n]+)/i', $headers, $matches);
$requestId = trim($matches[1] ?? '');
echo "شناسه درخواست: $requestId\n";

// مرحله ۲: صبر کنید برای پردازش
sleep(5);

// مرحله ۳: جستجوی تراکنش
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/lookup');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
    'Content-Type: application/json'
]);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode([
    'transaction_ids' => [$requestId]
]));

$lookupResponse = curl_exec($ch);
curl_close($ch);

$data = json_decode($lookupResponse, true);
if ($data['summary']['found'] > 0) {
    $tx = $data['transactions'][0];
    echo "هزینه دقیق: " . $tx['cost']['unit'] . " دلار\n";
    echo "هزینه دقیق: " . $tx['cost']['paid_irt'] . " تومان\n";
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
    model="gpt-5.4-mini",
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
  model: "gpt-5.4-mini",
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
    "model": "gpt-5.4-mini",
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


#### پاسخ

**مثال ۱: پرداخت از موجودی UNIT (بدون بسته اعتباری)**

```json
{
  "transactions": [
    {
      "id": "019ac4a0-a8f4-7041-845f-3ea8f15dcf1a",
      "created_at": "2025-11-27T09:24:18.129Z",
      "requested_at": "2025-11-27T09:24:14.709Z",
      "safety_identifier": null,
      "model": "gpt-5.4-mini-2026-03-17",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {
        "total": 17,
        "prompt": 8,
        "completion": 9,
        "reasoning": 0,
        "cached": 0,
        "prompt_details": {
          "text_tokens": 8,
          "audio_tokens": 0,
          "image_tokens": 0,
          "cached_tokens": 0,
          "audio_input_duration": 0,
          "cache_creation_tokens": 0
        },
        "completion_details": {
          "text_tokens": 9,
          "audio_tokens": 0,
          "image_tokens": 0,
          "reasoning_tokens": 0,
          "audio_output_duration": 0,
          "accepted_prediction_tokens": 0,
          "rejected_prediction_tokens": 0
        }
      },
      "ip_address": "192.168.1.1",
      "tools": {},
      "api_key_suffix": "...6I20",
      "cost": {
        "unit": "0.00000660",
        "paid_unit": "0.00000660",
        "paid_irt": "0",
        "paid_grant_irt": "0",
        "source": "credit",
        "currency": "UNIT"
      },
      "grants": [],
      "packages": []
    }
  ],
  "summary": {
    "requested": 1,
    "found": 1,
    "not_found_ids": []
  }
}
```

**مثال ۲: پرداخت از بسته اعتباری**

```json
{
  "transactions": [
    {
      "id": "019ac1c0-9518-7931-bf77-518cfbdd89f0",
      "created_at": "2025-11-26T20:06:22.555Z",
      "requested_at": "2025-11-26T20:00:15.228Z",
      "safety_identifier": null,
      "model": "gpt-5.4-mini",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {
        "total": 30,
        "prompt": 10,
        "completion": 20,
        "reasoning": 0,
        "cached": 0,
        "prompt_details": {
          "text_tokens": 10,
          "audio_tokens": 0,
          "image_tokens": 0,
          "cached_tokens": 0,
          "audio_input_duration": 0,
          "cache_creation_tokens": 0
        },
        "completion_details": {
          "text_tokens": 20,
          "audio_tokens": 0,
          "image_tokens": 0,
          "reasoning_tokens": 0,
          "audio_output_duration": 0,
          "accepted_prediction_tokens": 0,
          "rejected_prediction_tokens": 0
        }
      },
      "ip_address": "192.168.1.1",
      "tools": {},
      "api_key_suffix": "...jCqw",
      "cost": {
        "unit": "0.00001350",
        "paid_unit": "0.00001350",
        "paid_irt": "0.00",
        "paid_grant_irt": "1.55",
        "source": "credit_package",
        "currency": "UNIT"
      },
      "grants": [],
      "packages": [
        {
          "id": "1234",
          "template_id": "d-o3050s",
          "name": "مدل‌های زبانی منتخب OpenAI روزانه پایه",
          "amount_irt": "500000.00",
          "remaining_irt": "498447.15",
          "allowed_services": [
            "api"
          ],
          "scope_details": {
            "api": [
              "gpt-5-chat",
              "gpt-5.6-luna",
              "gpt-5.4-mini"
            ]
          },
          "end_date": "2025-11-27T15:05:07.404Z"
        }
      ]
    }
  ],
  "summary": {
    "requested": 1,
    "found": 1,
    "not_found_ids": []
  }
}
```

#### فیلدهای پاسخ

**شیء اصلی:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `transactions` | array | آرایه‌ای از اشیاء تراکنش |
| `summary` | object | خلاصه درخواست جستجو |

**شیء تراکنش:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه یکتای تراکنش (UUID v7) - همان هدر `avalai-request-id` |
| `created_at` | string | زمان پردازش هزینه تراکنش (ISO 8601) |
| `requested_at` | string | زمان شروع درخواست (ISO 8601) |
| `safety_identifier` | string\|null | شناسه داخلی شما (در صورت ارائه) |
| `model` | string | مدل استفاده شده (مثلا "gpt-5.4-mini-2026-03-17") |
| `provider` | string | نام ارائه‌دهنده (مثلا "openai", "anthropic") |
| `status_code` | int | کد وضعیت HTTP پاسخ |
| `stream` | bool | آیا درخواست از استریمینگ استفاده کرده |
| `tokens` | object | جزئیات استفاده توکن |
| `ip_address` | string | آدرس IP درخواست |
| `tools` | object | ابزارها/توابع استفاده شده در درخواست |
| `api_key_suffix` | string | ۴ کاراکتر آخر کلید API استفاده شده |
| `cost` | object | جزئیات هزینه |
| `grants` | array | گرنت‌های استفاده شده برای این تراکنش |
| `packages` | array | بسته‌های استفاده شده برای این تراکنش |

**شیء توکن‌ها:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `total` | int | کل توکن‌های استفاده شده |
| `prompt` | int | توکن‌های ورودی |
| `completion` | int | توکن‌های خروجی |
| `reasoning` | int | توکن‌های استدلال (مدل‌های o1/o3) |
| `cached` | int | توکن‌های کش شده (کش پرامپت) |
| `prompt_details` | object | جزئیات توکن‌های ورودی |
| `completion_details` | object | جزئیات توکن‌های خروجی |

**شیء جزئیات ورودی:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `text_tokens` | int | توکن‌های متنی در ورودی |
| `audio_tokens` | int | توکن‌های صوتی در ورودی |
| `image_tokens` | int | توکن‌های تصویری در ورودی |
| `cached_tokens` | int | توکن‌های کش شده در ورودی |
| `audio_input_duration` | int | مدت زمان ورودی صوتی به ثانیه |
| `cache_creation_tokens` | int | توکن‌های استفاده شده برای ایجاد کش |

**شیء جزئیات خروجی:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `text_tokens` | int | توکن‌های متنی در خروجی |
| `audio_tokens` | int | توکن‌های صوتی در خروجی |
| `image_tokens` | int | توکن‌های تصویری در خروجی |
| `reasoning_tokens` | int | توکن‌های استدلال در خروجی |
| `audio_output_duration` | int | مدت زمان خروجی صوتی به ثانیه |
| `accepted_prediction_tokens` | int | توکن‌های پیش‌بینی پذیرفته شده |
| `rejected_prediction_tokens` | int | توکن‌های پیش‌بینی رد شده |

**شیء هزینه:**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `unit` | string | کل هزینه به دلار/واحد |
| `paid_unit` | string | هزینه پرداخت شده به دلار/واحد |
| `paid_irt` | string | هزینه پرداخت شده به تومان (از موجودی) |
| `paid_grant_irt` | string | هزینه پوشش داده شده توسط گرنت‌ها/بسته‌ها |
| `source` | string | منبع پرداخت: `credit`، `credit_package`، `grant`، یا `balance` |
| `currency` | string | نوع ارز (همیشه "UNIT") |

---

### GET /transactions/summary

دریافت خلاصه تراکنش‌ها بر اساس مدل، ارائه‌دهنده، یا تاریخ. مفید برای گزارش‌دهی و تحلیل.

**آدرس:** `GET https://api.avalai.ir/user/v1/transactions/summary`

#### پارامترهای Query

| پارامتر | نوع | پیش‌فرض | توضیحات |
|---------|-----|---------|---------|
| `hours_ago` | int | 24 | ساعت‌های قبل برای بررسی (۱-۷۲۰) |
| `start_date` | string | - | تاریخ شروع (YYYY-MM-DD) |
| `end_date` | string | - | تاریخ پایان (YYYY-MM-DD) |
| `group_by` | string | model | گروه‌بندی بر اساس: model، provider، date، hour |

#### مثال‌ها

**گروه‌بندی بر اساس مدل (پیش‌فرض):**

```bash
curl -X GET "https://api.avalai.ir/user/v1/transactions/summary" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
import requests

response = requests.get(
    "https://api.avalai.ir/user/v1/transactions/summary",
    headers={"Authorization": f"Bearer {api_key}"},
)
print(response.json())

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const response = await fetch(
  "https://api.avalai.ir/user/v1/transactions/summary",
  {
    headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
  },
);
console.log(await response.json());

```

```go
// مثال Go
package main

import (
	"encoding/json"
	"fmt"
	"net/http"
	"os"
)

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)
	fmt.Printf("%+v\n", result)
}

```

```php
<?php
// مثال PHP
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
curl_close($ch);

print_r(json_decode($response, true));
?>

```


**پاسخ (group_by=model):**

```json
{
  "summary": [
    {
      "model": "gpt-5.6-luna",
      "count": 150,
      "total_tokens": 45000,
      "total_cost_unit": "0.450000",
      "total_cost_irt": "51862.50"
    },
    {
      "model": "gpt-5.4-mini",
      "count": 500,
      "total_tokens": 75000,
      "total_cost_unit": "0.0375",
      "total_cost_irt": "4321.88"
    }
  ],
  "period": {
    "start": "2025-11-26T00:00:00.000Z",
    "end": "2025-11-27T00:00:00.000Z",
    "hours": 24
  }
}
```

**گروه‌بندی بر اساس ارائه‌دهنده:**

```bash
curl -X GET "https://api.avalai.ir/user/v1/transactions/summary?group_by=provider" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
response = requests.get(
    "https://api.avalai.ir/user/v1/transactions/summary",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"group_by": "provider"},
)

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const response = await fetch(
  "https://api.avalai.ir/user/v1/transactions/summary?group_by=provider",
  {
    headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
  },
);

```

```go
// مثال Go
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=provider", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

```

```php
<?php
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?group_by=provider');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);
$response = curl_exec($ch);
?>

```


**پاسخ (group_by=provider):**

```json
{
  "summary": [
    {
      "provider": "openai",
      "count": 450,
      "total_tokens": 85000,
      "total_cost_unit": "0.425000",
      "total_cost_irt": "48987.50"
    },
    {
      "provider": "anthropic",
      "count": 200,
      "total_tokens": 35000,
      "total_cost_unit": "0.0625",
      "total_cost_irt": "7196.88"
    }
  ],
  "period": {
    "start": "2025-11-26T00:00:00.000Z",
    "end": "2025-11-27T00:00:00.000Z",
    "hours": 24
  }
}
```

**گروه‌بندی بر اساس تاریخ:**

```bash
curl -X GET "https://api.avalai.ir/user/v1/transactions/summary?group_by=date&hours_ago=168" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
response = requests.get(
    "https://api.avalai.ir/user/v1/transactions/summary",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"group_by": "date", "hours_ago": 168},  # ۷ روز
)

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const response = await fetch(
  "https://api.avalai.ir/user/v1/transactions/summary?group_by=date&hours_ago=168",
  {
    headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
  },
);

```

```go
// مثال Go
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=date&hours_ago=168", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

```

```php
<?php
$params = http_build_query(['group_by' => 'date', 'hours_ago' => 168]);
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);
?>

```


**پاسخ (group_by=date):**

```json
{
  "summary": [
    {
      "date": "2025-11-26",
      "count": 650,
      "total_tokens": 120000,
      "total_cost_unit": "0.487500",
      "total_cost_irt": "56184.38"
    },
    {
      "date": "2025-11-25",
      "count": 580,
      "total_tokens": 105000,
      "total_cost_unit": "0.420000",
      "total_cost_irt": "48405.00"
    }
  ],
  "period": {
    "start": "2025-11-20T00:00:00.000Z",
    "end": "2025-11-27T00:00:00.000Z",
    "hours": 168
  }
}
```

**گروه‌بندی بر اساس ساعت:**

```bash
curl -X GET "https://api.avalai.ir/user/v1/transactions/summary?group_by=hour&hours_ago=24" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python) - تحلیل الگوهای ساعتی
response = requests.get(
    "https://api.avalai.ir/user/v1/transactions/summary",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"group_by": "hour", "hours_ago": 24},
)

data = response.json()
for hour_data in data["summary"]:
    print(
        f"ساعت {hour_data['hour']}: {hour_data['count']} درخواست، {hour_data['total_cost_unit']} دلار"
    )

```

```javascript
// مثال جاوااسکریپت (JavaScript) - نمودار هزینه ساعتی
const response = await fetch(
  "https://api.avalai.ir/user/v1/transactions/summary?group_by=hour&hours_ago=24",
  {
    headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
  },
);

const data = await response.json();
data.summary.forEach((hour) => {
  console.log(`ساعت ${hour.hour}: ${hour.count} درخواست`);
});

```

```go
// مثال Go - گزارش تفصیلی ساعتی
req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/transactions/summary?group_by=hour&hours_ago=24", nil)
req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

resp, _ := (&http.Client{}).Do(req)
defer resp.Body.Close()

var result map[string]interface{}
json.NewDecoder(resp.Body).Decode(&result)

```

```php
<?php
// مثال PHP - تحلیل الگوی استفاده
$params = http_build_query(['group_by' => 'hour', 'hours_ago' => 24]);
$ch = curl_init('https://api.avalai.ir/user/v1/transactions/summary?' . $params);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
$data = json_decode($response, true);

foreach ($data['summary'] as $hour) {
    echo "ساعت {$hour['hour']}: {$hour['count']} درخواست\n";
}
?>

```


**پاسخ (group_by=hour):**

```json
{
  "summary": [
    {
      "hour": "2025-11-26T14:00:00.000Z",
      "count": 45,
      "total_tokens": 8500,
      "total_cost_unit": "0.0425",
      "total_cost_irt": "4896.88"
    },
    {
      "hour": "2025-11-26T15:00:00.000Z",
      "count": 52,
      "total_tokens": 9800,
      "total_cost_unit": "0.049",
      "total_cost_irt": "5643.50"
    }
  ],
  "period": {
    "start": "2025-11-26T00:00:00.000Z",
    "end": "2025-11-27T00:00:00.000Z",
    "hours": 24
  }
}
```

---

### GET /health

بررسی وضعیت سلامت User API.

**آدرس:** `GET https://api.avalai.ir/user/v1/health`

#### درخواست

```bash
curl -X GET "https://api.avalai.ir/user/v1/health" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
# مثال پایتون (Python)
import requests

response = requests.get(
    "https://api.avalai.ir/user/v1/health",
    headers={"Authorization": f"Bearer {api_key}"},
)
print(response.json())

```

```javascript
// مثال جاوااسکریپت (JavaScript)
const response = await fetch("https://api.avalai.ir/user/v1/health", {
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}` },
});
console.log(await response.json());

```

```go
// مثال Go
package main

import (
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	req, _ := http.NewRequest("GET", "https://api.avalai.ir/user/v1/health", nil)
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, _ := (&http.Client{}).Do(req)
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	fmt.Println(string(body))
}

```

```php
<?php
// مثال PHP
$ch = curl_init('https://api.avalai.ir/user/v1/health');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, ['Authorization: Bearer ' . getenv('AVALAI_API_KEY')]);

$response = curl_exec($ch);
curl_close($ch);

print_r(json_decode($response, true));
?>

```


#### پاسخ

```json
{
  "status": "healthy",
  "timestamp": "2025-11-27T09:30:00.000Z"
}
```

---

## مدیریت خطا

API کاربر از کدهای وضعیت HTTP استاندارد استفاده کرده و پاسخ‌های خطای JSON برمی‌گرداند.

### فرمت پاسخ خطا

```json
{
  "error": "error_code",
  "message": "توضیحات خطا به زبان قابل فهم"
}
```

### خطاهای رایج

| کد وضعیت | کد خطا | توضیحات |
|----------|--------|---------|
| 400 | `bad_request` | پارامترهای درخواست نامعتبر |
| 401 | `unauthorized` | کلید API موجود نیست یا نامعتبر است |
| 403 | `forbidden` | حساب کاربری معلق یا غیرفعال است |
| 404 | `not_found` | منبع یافت نشد |
| 429 | `rate_limit_exceeded` | درخواست‌های بیش از حد |
| 500 | `internal_error` | خطای سرور |

---

## منابع مرتبط

- [هدرهای پاسخ](fa/api-reference/response-headers.md) - اطلاعات درباره `avalai-request-id` و هدرهای محدودیت نرخ
- [راهنمای پیگیری هزینه نمایندگان](fa/resellers/cost-tracking-guide.md) - راهنمای گام به گام برای پیگیری دقیق هزینه
- [محدودیت نرخ](fa/guides/rate-limits.md) - درک محدودیت نرخ و سطوح
- [احراز هویت](fa/api-reference/authentication.md) - مدیریت کلید API
- [تکمیل گفتگو](fa/api-reference/chat.md) - مستندات نقطه پایانی اصلی API
