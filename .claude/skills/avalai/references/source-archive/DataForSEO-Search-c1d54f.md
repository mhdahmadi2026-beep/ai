# DataForSEO Search

AvalAI دسترسی به API جستجوی مقرون به صرفه DataForSEO را فراهم می‌کند که نتایج جستجوی وب قابل اعتماد با ارزش عالی برای برنامه‌های پر حجم ارائه می‌دهد.

## ابزارهای جستجو

DataForSEO در ارائه داده‌های SEO و جستجو با تمرکز بر مقرون به صرفه بودن و قابلیت اطمینان تخصص دارد و آن را برای کسب‌وکارها و برنامه‌هایی که به جستجوهای مکرر نیاز دارند، ایده‌آل می‌کند.

### DataForSEO Search

موتور جستجوی مقرون به صرفه با نتایج قابل اعتماد و با کیفیت.

| ویژگی       | جزئیات                                                        |
| ----------- | ------------------------------------------------------------- |
| شناسه ابزار | `dataforseo-search`                                           |
| اندپوینت    | `v1/search/dataforseo-search` یا `v1/search`                |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                        |
| قیمت‌گذاری  | $0.003 به ازای هر کوئری                                       |
| قابلیت‌ها    | جستجوی وب، فیلتر دامنه، داده‌های SEO، نتایج قابل اعتماد      |
| نقاط قوت    | مقرون به صرفه، قابل اعتماد، مناسب برای حجم بالا              |
| بهترین برای | برنامه‌های پر حجم، پروژه‌های با بودجه محدود، ابزارهای SEO     |

**نمونه استفاده:**

```language-selector
bash=:curl https://api.avalai.ir/v1/search/dataforseo-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "web development trends 2024",
    "max_results": 10
  }'

python=:import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/dataforseo-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "web development trends 2024", "max_results": 10},
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

javascript=:const response = await fetch("https://api.avalai.ir/v1/search/dataforseo-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "web development trends 2024",
        max_results: 10
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```

## جستجوی پیشرفته با فیلترینگ

مقرون به صرفه بودن DataForSEO را با گزینه‌های فیلترینگ پیشرفته برای نتایج هدفمند ترکیب کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "dataforseo-search",
    "query": "SEO optimization techniques",
    "max_results": 15,
    "search_domain_filter": ["moz.com", "searchengineland.com", "semrush.com"],
    "country": "United States",
    "language_code": "en",
    "depth": 20,
    "device": "desktop",
    "os": "windows"
  }'

python=:import requests

response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "dataforseo-search",
        "query": "SEO optimization techniques",
        "max_results": 15,
        "search_domain_filter": ["moz.com", "searchengineland.com", "semrush.com"],
        # پارامترهای اختصاصی DataForSEO
        "country": "United States",  # نام کشور برای location_name
        "language_code": "en",  # کد زبان
        "depth": 20,  # تعداد نتایج (حداکثر 700)
        "device": "desktop",  # نوع دستگاه ('desktop', 'mobile', 'tablet')
        "os": "windows",  # سیستم عامل
    },
)

results = response.json()

javascript=:const response = await fetch("https://api.avalai.ir/v1/search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        search_tool_name: "dataforseo-search",
        query: "SEO optimization techniques",
        max_results: 15,
        search_domain_filter: ["moz.com", "searchengineland.com", "semrush.com"],
        // پارامترهای اختصاصی DataForSEO
        country: "United States",       // نام کشور برای location_name
        language_code: "en",            // کد زبان
        depth: 20,                      // تعداد نتایج (حداکثر 700)
        device: "desktop",              // نوع دستگاه ('desktop', 'mobile', 'tablet')
        os: "windows"                   // سیستم عامل
    })
});

const data = await response.json();

```

## پارامترهای درخواست

جستجوی DataForSEO از پارامترهای زیر پشتیبانی می‌کند:

### پارامترهای استاندارد

| پارامتر              | نوع     | الزامی | توضیحات                                                      |
| -------------------- | ------- | ------ | ------------------------------------------------------------ |
| query                | string  | بله    | رشته کوئری جستجو                                             |
| max_results          | integer | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10                       |
| search_domain_filter | array   | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)            |
| max_tokens_per_page  | integer | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024        |

### پارامترهای اختصاصی DataForSEO (پیشرفته)

| پارامتر              | نوع     | الزامی | توضیحات                                                      |
| -------------------- | ------- | ------ | ------------------------------------------------------------ |
| country              | string  | خیر    | نام کشور برای موقعیت مکانی (مثلا "United States"، "United Kingdom"، "Germany"). به عنوان `location_name` در API DataForSEO استفاده می‌شود. |
| language_code        | string  | خیر    | کد زبان برای نتایج (مثلا "en"، "de"، "fr")                   |
| depth                | integer | خیر    | تعداد نتایج جستجو برای دریافت (حداکثر 700)                  |
| device               | string  | خیر    | نوع دستگاه برای شبیه‌سازی: `desktop`، `mobile`، یا `tablet` |
| os                   | string  | خیر    | سیستم عامل برای شبیه‌سازی (مثلا "windows"، "macos"، "android"، "ios") |

برای اطلاعات بیشتر در مورد پارامترهای موجود، به [مستندات رسمی DataForSEO](https://docs.dataforseo.com) مراجعه کنید.

## فرمت پاسخ

جستجوهای DataForSEO نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

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

## استفاده از DataForSEO Search از طریق AvalAI

به API جستجوی DataForSEO با استفاده از اندپوینت Search API AvalAI دسترسی پیدا کنید. می‌توانید ابزار را در مسیر URL یا در بدنه درخواست مشخص کنید.

```python
import requests

# گزینه 1: ابزار در URL
response = requests.post(
    "https://api.avalai.ir/v1/search/dataforseo-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "content marketing strategies", "max_results": 10},
)

# گزینه 2: ابزار در بدنه با پارامترهای پیشرفته
response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "dataforseo-search",
        "query": "link building best practices",
        "max_results": 20,
        "country": "United States",
        "language_code": "en",
        "device": "desktop",
    },
)

results = response.json()
```

## چه زمانی از DataForSEO Search استفاده کنیم

**از DataForSEO Search استفاده کنید** وقتی:
- کارایی هزینه اولویت اصلی است ($0.003 به ازای هر کوئری)
- در حال پردازش حجم بالایی از کوئری‌های جستجو هستید
- به نتایج قابل اعتماد و ثابت نیاز دارید
- در حال ساخت ابزارهای SEO یا پلتفرم‌های تحلیلی هستید
- اجرای جستجوهای خودکار یا نظارت
- محدودیت‌های بودجه قابل توجه است
- کیفیت جستجوی استاندارد نیازهای شما را برآورده می‌کند

## مزایای کلیدی

1. **مقرون به صرفه**: با $0.003 به ازای هر کوئری، تعادل خوبی بین قیمت و قابلیت‌های فیلترینگ ارائه می‌دهد
2. **مناسب برای حجم بالا**: عالی برای برنامه‌هایی که به جستجوهای مکرر نیاز دارند
3. **نتایج قابل اعتماد**: نتایج جستجوی ثابت و با کیفیت
4. **متمرکز بر SEO**: بهینه شده برای برنامه‌های SEO و داده‌های وب
5. **ارزش عالی**: تعادل عالی بین هزینه و کیفیت

## موارد استفاده

- **ابزارهای SEO**: ساخت ابزارهای ردیابی رتبه، تحقیق کلمات کلیدی، یا تحلیل رقبا
- **جمع‌آوری محتوا**: جمع‌آوری منظم محتوا از منابع متعدد
- **تحقیق بازار**: نظارت بر روندها و رقبا در مقیاس بزرگ
- **نظارت خودکار**: راه‌اندازی جستجوهای منظم برای هشدارها یا ردیابی
- **برنامه‌های پر حجم**: هر برنامه‌ای که به جستجوهای مکرر نیاز دارد و هزینه اهمیت دارد

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
- [مستندات رسمی DataForSEO](https://docs.dataforseo.com)
