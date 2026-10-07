# Parallel AI Search

AvalAI دسترسی به قابلیت‌های پردازش جستجوی موازی سریع Parallel AI را فراهم می‌کند که نسخه‌های استاندارد و حرفه‌ای را برای نیازهای عملکردی مختلف ارائه می‌دهد.

## ابزارهای جستجو

Parallel AI در پردازش جستجوی موازی سریع تخصص دارد و نتایج سریع را از طریق جستجوهای همزمان کارآمد ارائه می‌دهد.

### Parallel AI Search (استاندارد)

پردازش جستجوی موازی سریع با قیمت‌گذاری مقرون به صرفه.

| ویژگی       | جزئیات                                                        |
| ----------- | ------------------------------------------------------------- |
| شناسه ابزار | `parallel_ai-search`                                          |
| اندپوینت    | `v1/search/parallel_ai-search` یا `v1/search`               |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                        |
| قیمت‌گذاری  | $0.004 به ازای هر کوئری                                       |
| قابلیت‌ها    | پردازش جستجوی موازی، فیلتر دامنه، نتایج سریع                 |
| نقاط قوت    | مقرون به صرفه، پردازش سریع، عملکرد قابل اعتماد              |
| بهترین برای | برنامه‌های جستجوی با حجم بالا، پروژه‌های با بودجه محدود     |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search/parallel_ai-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "artificial intelligence trends",
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/parallel_ai-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "artificial intelligence trends", "max_results": 10},
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search/parallel_ai-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "artificial intelligence trends",
        max_results: 10
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```


### Parallel AI Search Pro

نسخه پیشرفته با ویژگی‌های اضافی و نتایج با کیفیت بالاتر.

| ویژگی       | جزئیات                                                               |
| ----------- | -------------------------------------------------------------------- |
| شناسه ابزار | `parallel_ai-search-pro`                                             |
| اندپوینت    | `v1/search/parallel_ai-search-pro` یا `v1/search`                  |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                               |
| قیمت‌گذاری  | $0.009 به ازای هر کوئری                                              |
| قابلیت‌ها    | جستجوی موازی پیشرفته، فیلترینگ بهبود یافته، نتایج ممتاز             |
| نقاط قوت    | نتایج با کیفیت بالاتر، دقت بهتر، ویژگی‌های پیشرفته                  |
| بهترین برای | برنامه‌های تولیدی، پروژه‌های کیفیت‌محور                             |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "parallel_ai-search-pro",
    "query": ["AI developments", "machine learning trends"],
    "max_results": 5,
    "processor": "pro",
    "max_chars_per_result": 500
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "parallel_ai-search-pro",
        "query": ["AI developments", "machine learning trends"],
        "max_results": 5,
        # پارامترهای اختصاصی Parallel AI
        "processor": "pro",  # 'base' یا 'pro'
        "max_chars_per_result": 500,  # حداکثر کاراکتر در هر نتیجه
    },
)

results = response.json()
print(f"Total results: {len(results['results'])}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        search_tool_name: "parallel_ai-search-pro",
        query: ["AI developments", "machine learning trends"],
        max_results: 5,
        // پارامترهای اختصاصی Parallel AI
        processor: "pro",                 // 'base' یا 'pro'
        max_chars_per_result: 500         // حداکثر کاراکتر در هر نتیجه
    })
});

const data = await response.json();
console.log(`Total results: ${data.results.length}`);

```


## پارامترهای درخواست

تمام ابزارهای جستجوی Parallel AI از پارامترهای زیر پشتیبانی می‌کنند:

### پارامترهای استاندارد

| پارامتر              | نوع            | الزامی | توضیحات                                                      |
| -------------------- | -------------- | ------ | ------------------------------------------------------------ |
| query                | string or array | بله   | رشته کوئری جستجو یا آرایه‌ای از رشته‌ها                      |
| max_results          | integer        | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10                       |
| search_domain_filter | array          | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)            |
| max_tokens_per_page  | integer        | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024        |
| country              | string         | خیر    | فیلتر کد کشور (مثلا "US"، "GB"، "DE")                       |

### پارامترهای اختصاصی Parallel AI (پیشرفته)

| پارامتر              | نوع            | الزامی | توضیحات                                                      |
| -------------------- | -------------- | ------ | ------------------------------------------------------------ |
| processor            | string         | خیر    | نوع پردازشگر: `base` (استاندارد) یا `pro` (کیفیت بالاتر)   |
| max_chars_per_result | integer        | خیر    | حداکثر کاراکتر در هر خلاصه نتیجه                            |

## فرمت پاسخ

تمام جستجوهای Parallel AI نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

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

## استفاده از Parallel AI Search از طریق AvalAI

به ابزارهای جستجوی Parallel AI با استفاده از اندپوینت Search API AvalAI دسترسی پیدا کنید. می‌توانید ابزار را در مسیر URL یا در بدنه درخواست مشخص کنید.

```python
import requests

# گزینه 1: ابزار در URL
response = requests.post(
    "https://api.avalai.ir/v1/search/parallel_ai-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "latest technology news", "max_results": 10},
)

# گزینه 2: ابزار در بدنه با پارامترهای پیشرفته
response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "parallel_ai-search-pro",
        "query": ["AI trends", "ML innovations", "tech startups"],
        "max_results": 5,
        # پارامترهای اختصاصی Parallel AI
        "processor": "pro",  # 'base' یا 'pro'
        "max_chars_per_result": 500,  # حداکثر کاراکتر در هر نتیجه
    },
)

results = response.json()
```

## انتخاب بین استاندارد و Pro

**از Parallel AI Search (استاندارد) استفاده کنید** وقتی:
- به نتایج جستجوی سریع و مقرون به صرفه نیاز دارید
- در حال پردازش حجم بالای کوئری‌های جستجو هستید
- بودجه اولویت اصلی است
- کیفیت استاندارد نیازهای شما را برآورده می‌کند

**از Parallel AI Search Pro استفاده کنید** وقتی:
- به نتایج با کیفیت بالاتر و دقیق‌تر نیاز دارید
- در حال اجرای برنامه‌های تولیدی هستید
- کیفیت و قابلیت اطمینان اولویت دارند
- به ویژگی‌های پیشرفته نیاز دارید

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
