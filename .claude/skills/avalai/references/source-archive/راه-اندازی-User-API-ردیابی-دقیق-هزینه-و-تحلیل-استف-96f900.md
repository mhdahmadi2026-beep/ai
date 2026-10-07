# راه‌اندازی User API: ردیابی دقیق هزینه و تحلیل استفاده

**تاریخ:** 1404-09-06 / (2025-11-27)

راه‌اندازی User API در آدرس `https://api.avalai.ir/user/v1` را اعلام می‌کنیم که ردیابی دقیق هزینه، تاریخچه تراکنش‌ها و تحلیل استفاده را فراهم می‌کند. این API جدید نیاز حیاتی به صورتحساب دقیق و مدیریت هزینه را برطرف می‌کند، به‌ویژه برای فروشندگان و سازمان‌های بزرگ که نیاز به نظارت دقیق بر استفاده دارند.

---

## نمای کلی

User API چهار endpoint اختصاصی برای مدیریت جامع حساب و ردیابی هزینه معرفی می‌کند. برخلاف فیلد `estimated_cost` در پاسخ‌های API (که تضمین نمی‌شود و ممکن است همیشه موجود نباشد)، User API داده‌های هزینه دقیق 100٪ را ظرف 30 ثانیه پس از هر فراخوانی API فراهم می‌کند.

### قابلیت‌های کلیدی

- **ردیابی دقیق هزینه**: دریافت هزینه دقیق برای هر فراخوانی API با استفاده از [`x-request-id`](fa/api-reference/response-headers.md#x-request-id) از هدرهای پاسخ
- **تاریخچه تراکنش‌ها**: لیست تمام تراکنش‌ها با فیلتر پیشرفته بر اساس مدل، ارائه‌دهنده، بازه زمانی
- **تحلیل استفاده**: خلاصه‌های دقیق گروه‌بندی شده بر اساس مدل، ارائه‌دهنده، تاریخ یا ساعت
- **پردازش دسته‌ای**: جستجوی تا 1000 شناسه تراکنش در یک درخواست
- **رد تراکنش کامل**: جزئیات کامل تراکنش‌ها برای انطباق و صورتحساب

---

## نقاط پایانی API

### آدرس پایه

```
https://api.avalai.ir/user/v1
```

### نقاط پایانی موجود

| نقطه پایانی | متد | هدف |
|----------|--------|---------|
| `/transactions` | GET | لیست تراکنش‌ها با فیلتر |
| `/transactions/lookup` | POST | دریافت هزینه دقیق با شناسه تراکنش |
| `/transactions/summary` | GET | تحلیل و خلاصه استفاده |
| `/health` | GET | وضعیت سلامت API |

---

## موارد استفاده

### برای فروشندگان

فروشندگان اکنون می‌توانند بر اساس هزینه‌های واقعی به مشتریان صورتحساب دقیق صادر کنند:

**مشکل حل‌شده**: فیلد `estimated_cost` در پاسخ‌های API برای صورتحساب قابل اعتماد نیست:
- تضمین نمی‌شود که موجود باشد
- ممکن است هزینه‌های نهایی را منعکس نکند
- می‌تواند باعث اختلاف در صورتحساب شود

**راه‌حل**: از endpoint `/transactions/lookup` در User API با [`x-request-id`](fa/api-reference/response-headers.md#x-request-id) از هدرهای پاسخ برای دریافت هزینه دقیق تضمین‌شده ظرف 30 ثانیه استفاده کنید.

**گردش کار**:
1. فراخوانی API از طرف مشتری
2. دریافت [`x-request-id`](fa/api-reference/response-headers.md#x-request-id) از هدرهای پاسخ
3. ذخیره شناسه درخواست با رکورد مشتری
4. پس از 30 ثانیه، جستجوی هزینه دقیق
5. صورتحساب دقیق به مشتری

### برای سازمان‌های بزرگ

سازمان‌ها قابلیت تخصیص دقیق هزینه و تسویه حساب دقیق به دست می‌آورند:

- **ردیابی چند مستاجری**: ردیابی هزینه‌ها بر اساس بخش یا پروژه با استفاده از `safety_identifier`
- **بازیابی دسته‌ای هزینه**: پردازش میلیون‌ها درخواست با جستجوی دسته‌ای
- **تحلیل لحظه‌ای**: نظارت بر الگوهای هزینه و بهینه‌سازی استفاده
- **انطباق**: رد تراکنش کامل برای گزارش‌دهی مالی

### برای توسعه‌دهندگان

همه توسعه‌دهندگان از نظارت دقیق استفاده بهره‌مند می‌شوند:

- **مدیریت بودجه**: ردیابی هزینه‌ها در برابر بودجه‌های تخصیص‌یافته
- **بهینه‌سازی هزینه**: شناسایی الگوهای پرهزینه و بهینه‌سازی prompt‌ها
- **اشکال‌زدایی**: ارتباط هزینه‌ها با درخواست‌های خاص برای عیب‌یابی

---

## شروع سریع

### مرحله 1: یک فراخوانی API انجام دهید

هر پاسخ API شامل هدر [`x-request-id`](fa/api-reference/response-headers.md#x-request-id) است:

```bash
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "سلام!"}]
  }'
```

**هدرهای پاسخ**:
```
HTTP/2 200
date: Wed, 27 Nov 2025 09:24:15 GMT
content-type: application/json
x-ratelimit-limit-requests: 30000
x-ratelimit-remaining-requests: 29999
x-request-id: 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a
```

### مرحله 2: جستجوی هزینه دقیق

تا 30 ثانیه صبر کنید، سپس هزینه دقیق را بازیابی کنید:

```bash
curl "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]
  }'
```

**پاسخ**:
```json
{
  "transactions": [
    {
      "id": "019ac4a0-a8f4-7041-845f-3ea8f15dcf1a",
      "created_at": "2025-11-26T20:06:22.555Z",
      "requested_at": "2025-11-26T20:00:15.228Z",
      "safety_identifier": null,
      "model": "gpt-4o-mini",
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
              "gpt-5-mini",
              "gpt-5-nano",
              "o4-mini",
              "o3-mini",
              "o1",
              "gpt-4.1",
              "gpt-4.1-mini",
              "gpt-4.1-nano",
              "gpt-4o",
              "gpt-4o-mini",
              "gpt-4o-transcribe",
              "gpt-4o-mini-transcribe",
              "gpt-4o-mini-tts"
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

---

## نمونه‌های کد

### Python: ردیابی هزینه فروشندگان

```language-selector
bash=:# مرحله 1: فراخوانی API برای مشتری
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini",
    "messages": [{"role": "user", "content": "سلام!"}],
    "safety_identifier": "customer-12345"
  }'

# مرحله 2: 30 ثانیه صبر کنید، سپس هزینه را جستجو کنید
sleep 30

curl "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]
  }'

python=:import requests
import time

# مرحله 1: فراخوانی API برای مشتری
response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "gpt-4o-mini",
        "messages": [{"role": "user", "content": "سلام!"}],
        "safety_identifier": "customer-12345",
    },
)

# مرحله 2: دریافت x-request-id
request_id = response.headers.get("x-request-id")
print(f"شناسه درخواست: {request_id}")

# مرحله 3: انتظار برای پردازش هزینه
time.sleep(30)

# مرحله 4: جستجوی هزینه دقیق
cost_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"transaction_ids": [request_id]},
)

transaction = cost_response.json()["transactions"][0]
cost_usd = float(transaction["cost"]["total_cost_usd"])
print(f"هزینه دقیق: ${cost_usd:.6f}")

javascript=:// مرحله 1: فراخوانی API برای مشتری
const response = await fetch("https://api.avalai.ir/v1/chat/completions", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "gpt-4o-mini",
    messages: [{role: "user", content: "سلام!"}],
    safety_identifier: "customer-12345"
  })
});

// مرحله 2: دریافت x-request-id
const requestId = response.headers.get("x-request-id");
console.log(`شناسه درخواست: ${requestId}`);

// مرحله 3: انتظار برای پردازش هزینه
await new Promise(resolve => setTimeout(resolve, 30000));

// مرحله 4: جستجوی هزینه دقیق
const costResponse = await fetch("https://api.avalai.ir/user/v1/transactions/lookup", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    transaction_ids: [requestId]
  })
});

const data = await costResponse.json();
const transaction = data.transactions[0];
const costUsd = parseFloat(transaction.cost.total_cost_usd);
console.log(`هزینه دقیق: $${costUsd.toFixed(6)}`);

```

### سازمان‌ها: بازیابی دسته‌ای هزینه

```language-selector
bash=:# لیست تراکنش‌های اخیر
curl "https://api.avalai.ir/user/v1/transactions?limit=100&created_after=2025-11-27T00:00:00Z" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# جستجوی چندین تراکنش
curl "https://api.avalai.ir/user/v1/transactions/lookup" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "transaction_ids": [
      "019ac4a0-a8f4-7041-845f-3ea8f15dcf1a",
      "019ac4a0-b2c3-7d4e-9f0a-1b2c3d4e5f6a",
      "019ac4a0-c3d4-8e5f-a0b1-2c3d4e5f6a7b"
    ]
  }'

python=:import requests

# لیست تراکنش‌های اخیر
list_response = requests.get(
    "https://api.avalai.ir/user/v1/transactions",
    headers={"Authorization": f"Bearer {api_key}"},
    params={"limit": 100, "created_after": "2025-11-27T00:00:00Z"},
)

transactions = list_response.json()["transactions"]
transaction_ids = [t["id"] for t in transactions]

# جستجوی دسته‌ای (تا 1000 شناسه)
cost_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"transaction_ids": transaction_ids},
)

# محاسبه هزینه کل
total_cost = sum(
    float(t["cost"]["total_cost_usd"]) for t in cost_response.json()["transactions"]
)
print(f"هزینه کل: ${total_cost:.6f}")

javascript=:// لیست تراکنش‌های اخیر
const listResponse = await fetch(
  "https://api.avalai.ir/user/v1/transactions?limit=100&created_after=2025-11-27T00:00:00Z",
  {
    headers: {
      "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`
    }
  }
);

const data = await listResponse.json();
const transactionIds = data.transactions.map(t => t.id);

// جستجوی دسته‌ای (تا 1000 شناسه)
const costResponse = await fetch("https://api.avalai.ir/user/v1/transactions/lookup", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    transaction_ids: transactionIds
  })
});

const costData = await costResponse.json();

// محاسبه هزینه کل
const totalCost = costData.transactions.reduce(
  (sum, t) => sum + parseFloat(t.cost.total_cost_usd),
  0
);
console.log(`هزینه کل: $${totalCost.toFixed(6)}`);

```

---

## ویژگی‌های پیشرفته

### فیلتر تراکنش‌ها

فیلتر تراکنش‌ها بر اساس معیارهای متعدد:

```bash
curl "https://api.avalai.ir/user/v1/transactions?model=gpt-4o&provider=openai&created_after=2025-11-27T00:00:00Z&limit=50" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

**پاسخ**:
```json
{
  "transactions": [
    {
      "id": "019ac4a0-a8f4-7041-845f-3ea8f15dcf1a",
      "created_at": "2025-11-27T09:24:18.129Z",
      "requested_at": "2025-11-27T09:24:14.709Z",
      "safety_identifier": null,
      "model": "gpt-4o-mini-2024-07-18",
      "provider": "openai",
      "status_code": 200,
      "stream": false,
      "tokens": {
        "total": 17,
        "prompt": 8,
        "completion": 9,
        "reasoning": 0,
        "cached": 0
      }
    }
  ],
  "total": 1,
  "page": 1,
  "page_size": 100,
  "has_more": false
}
```

### تحلیل استفاده

دریافت آمار استفاده تجمیع‌شده:

```bash
# خلاصه روزانه بر اساس مدل
curl "https://api.avalai.ir/user/v1/transactions/summary?group_by=day" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

**پاسخ**:
```json
{
  "period": {
    "start": "2025-11-26T14:34:35.797Z",
    "end": "2025-11-27T14:34:35.797Z"
  },
  "totals": {
    "transactions": 16071,
    "tokens": {
      "total": 389932376,
      "prompt": 363975518,
      "completion": 25956858,
      "reasoning": 4976660,
      "cached": 104316078
    },
    "cost": {
      "unit": "883.58715766",
      "paid_unit": "883.40514018",
      "paid_irt": "0",
      "paid_grant_irt": "1000000.00"
    }
  },
  "breakdown": [
    {
      "period": "2025-11-27",
      "transactions": 9636,
      "tokens": {
        "total": 218301310,
        "prompt": 203319110,
        "completion": 14982200
      }
    },
    {
      "period": "2025-11-26",
      "transactions": 6435,
      "tokens": {
        "total": 171631066,
        "prompt": 160656408,
        "completion": 10974658
      }
    }
  ],
  "by_model": null,
  "by_safety_identifier": null,
  "by_provider": null,
  "by_api_key": null
}
```

### شناسه‌های سفارشی

برچسب‌گذاری درخواست‌ها برای ردیابی بخشی:

```bash
curl "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o",
    "messages": [{"role": "user", "content": "این داده‌ها را تحلیل کن"}],
    "safety_identifier": "dept-analytics-project-x"
  }'
```

سپس فیلتر بر اساس شناسه:

```bash
curl "https://api.avalai.ir/user/v1/transactions?safety_identifier=dept-analytics-project-x" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

---

## راهنمای مهاجرت

### از estimated_cost به User API

**قبل** (غیرقابل اعتماد):
```python
response = client.chat.completions.create(...)
# estimated_cost ممکن است موجود نباشد!
cost = (
    response.estimated_cost.get("unit") if hasattr(response, "estimated_cost") else None
)
```

**بعد** (تضمین‌شده):
```python
response = client.chat.completions.create(...)
request_id = response.headers.get("x-request-id")

# 30 ثانیه صبر کنید
time.sleep(30)

# دریافت هزینه دقیق تضمین‌شده
cost_data = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"transaction_ids": [request_id]},
).json()

cost = float(cost_data["transactions"][0]["cost"]["total_cost_usd"])
```

---

## لینک‌های مرتبط

- [مرجع User API](fa/api-reference/user.md) - مستندات کامل API
- [راهنمای هدرهای پاسخ](fa/api-reference/response-headers.md) - درک [`x-request-id`](fa/api-reference/response-headers.md#x-request-id) و محدودیت‌های نرخ
- [راهنمای ردیابی هزینه فروشندگان](fa/resellers/cost-tracking-guide.md) - راهنمای گام به گام پیاده‌سازی
- [راهنمای استفاده سازمانی](fa/resellers/enterprise-guide.md) - الگوهای پیشرفته برای مقیاس
- [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md) - درک محدودیت‌های نرخ API
