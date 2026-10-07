# Serper Search

AvalAI دسترسی به API جستجوی سریع و مبتنی بر نتایج Google در Serper را فراهم می‌کند؛ گزینه‌ای بسیار مقرون‌به‌صرفه برای جستجوی مستقیم وب در حجم بالا.

## ابزار جستجو

Serper در ارائه نتایج جستجوی Google با هزینه پایین تخصص دارد و کنترل‌های کاربردی برای موقعیت جغرافیایی، زبان، اصلاح خودکار، فیلتر زمانی و صفحه‌بندی ارائه می‌کند.

### Serper Search

جستجوی کم‌هزینه مبتنی بر Google با هدف‌گیری جغرافیایی و فیلترهای زمانی.

| ویژگی       | جزئیات                                                        |
| ----------- | ------------------------------------------------------------- |
| شناسه ابزار | `serper-search`                                               |
| اندپوینت    | `v1/search/serper-search` یا `v1/search`                    |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                        |
| قیمت‌گذاری  | $0.001 به ازای هر کوئری                                       |
| قابلیت‌ها    | جستجوی وب مبتنی بر Google، هدف‌گیری جغرافیایی، کنترل زبان، فیلتر زمانی، صفحه‌بندی |
| نقاط قوت    | کمترین هزینه جستجو، محلی‌سازی کاربردی، نتایج سریع            |
| بهترین برای | جستجوی پرحجم، نظارت بر قیمت، جستجوی محلی، پایش اخبار        |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search/serper-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI news",
    "max_results": 10,
    "gl": "uk",
    "hl": "en",
    "autocorrect": false,
    "tbs": "qdr:d",
    "page": 1
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/serper-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "latest AI news",
        "max_results": 10,
        # پارامترهای اختصاصی Serper
        "gl": "uk",  # کد کشور/موقعیت جغرافیایی
        "hl": "en",  # کد زبان
        "autocorrect": False,  # غیرفعال کردن اصلاح خودکار
        "tbs": "qdr:d",  # فیلتر زمانی: روز گذشته
        "page": 1,  # شماره صفحه
    },
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search/serper-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "latest AI news",
        max_results: 10,
        // پارامترهای اختصاصی Serper
        gl: "uk",              // کد کشور/موقعیت جغرافیایی
        hl: "en",              // کد زبان
        autocorrect: false,     // غیرفعال کردن اصلاح خودکار
        tbs: "qdr:d",          // فیلتر زمانی: روز گذشته
        page: 1                 // شماره صفحه
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```


## پارامترهای درخواست

Serper Search از پارامترهای زیر پشتیبانی می‌کند:

### پارامترهای استاندارد

| پارامتر              | نوع     | الزامی | توضیحات                                                      |
| -------------------- | ------- | ------ | ------------------------------------------------------------ |
| query                | string  | بله    | رشته کوئری جستجو                                             |
| max_results          | integer | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10                       |
| search_domain_filter | array   | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)            |
| max_tokens_per_page  | integer | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024        |
| country              | string  | خیر    | فیلتر کد کشور (برای مثال `US`، `GB`، `DE`)                  |
| location             | string  | خیر    | موقعیت جغرافیایی برای نتایج محلی (برای مثال `Berlin,Germany`) |

### پارامترهای اختصاصی Serper

| پارامتر | نوع | الزامی | توضیحات |
| ------- | --- | ------ | ------- |
| gl | string | خیر | کد کشور/موقعیت جغرافیایی برای نتایج محلی‌سازی‌شده (برای مثال `uk`، `us`، `de`) |
| hl | string | خیر | کد زبان نتایج (برای مثال `en`، `de`، `fa`) |
| autocorrect | boolean | خیر | فعال یا غیرفعال کردن اصلاح خودکار کوئری. برای غیرفعال کردن مقدار `false` قرار دهید |
| tbs | string | خیر | فیلتر جستجوی زمانی مانند `qdr:h`، `qdr:d`، `qdr:w`، `qdr:m` یا `qdr:y` |
| page | integer | خیر | شماره صفحه برای نتایج صفحه‌بندی‌شده |

## جستجوی مبتنی بر زمان

از پارامتر `tbs` برای فیلتر کردن نتایج بر اساس بازه زمانی استفاده کنید:

| مقدار | معنی |
| ----- | ---- |
| `qdr:h` | ساعت گذشته |
| `qdr:d` | روز گذشته |
| `qdr:w` | هفته گذشته |
| `qdr:m` | ماه گذشته |
| `qdr:y` | سال گذشته |

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/serper-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "AI product launches",
        "tbs": "qdr:d",  # روز گذشته
        "max_results": 10,
    },
)
```

## هدف‌گیری جغرافیایی

پارامترهای `country`، `location`، `gl` و `hl` را برای دریافت نتایج هدفمند جغرافیایی ترکیب کنید:

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/serper-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "restaurants",
        "country": "DE",
        "location": "Berlin,Germany",
        "gl": "de",
        "hl": "de",
        "max_results": 10,
    },
)
```

## فرمت پاسخ

جستجوهای Serper نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

```json
{
  "object": "search",
  "results": [
    {
      "title": "عنوان نتیجه",
      "url": "https://example.com/page",

      "snippet": "خلاصه‌ای از محتوای صفحه...",
      "date": "2024-01-15"
    }
  ]
}
```

## چه زمانی از Serper Search استفاده کنیم

از Serper Search استفاده کنید وقتی:

- به کم‌هزینه‌ترین گزینه جستجوی مستقیم وب با قیمت $0.001 به ازای هر کوئری نیاز دارید
- نتایج مبتنی بر Google را از طریق Search API یکپارچه AvalAI می‌خواهید
- به فیلترهای زمانی برای محتوای جدید، پایش اخبار یا مانیتورینگ نیاز دارید
- به جستجوی محلی با پارامترهای کشور، زبان و موقعیت نیاز دارید
- سیستم‌های پرحجم مانند نظارت بر قیمت، پایش بازار یا تجمیع جستجو می‌سازید

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
