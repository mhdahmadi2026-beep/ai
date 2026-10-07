# Exa AI Search

AvalAI دسترسی به موتور جستجوی عصبی Exa AI را فراهم می‌کند که برای کوئری‌های معنایی بهینه شده و نتایج بسیار مرتبط را بر اساس معنا به جای صرف کلمات کلیدی ارائه می‌دهد.

## ابزارهای جستجو

Exa AI در فناوری جستجوی عصبی تخصص دارد و از مدل‌های پیشرفته هوش مصنوعی برای درک هدف کوئری و ارائه نتایج معنایی مرتبط استفاده می‌کند.

### Exa AI Search

موتور جستجوی عصبی بهینه شده برای درک معنایی و ارتباط.

| ویژگی       | جزئیات                                                               |
| ----------- | -------------------------------------------------------------------- |
| شناسه ابزار | `exa_ai-search`                                                      |
| اندپوینت    | `v1/search/exa_ai-search` یا `v1/search`                           |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                               |
| قیمت‌گذاری  | $0.025 به ازای هر کوئری                                              |
| قابلیت‌ها    | جستجوی معنایی، درک عصبی، نتایج آگاه از زمینه                        |
| نقاط قوت    | درک معنایی برتر، آگاهی از زمینه، قدرت گرفته از هوش مصنوعی          |
| بهترین برای | کوئری‌های پیچیده، تحقیق، برنامه‌های جستجوی معنایی                  |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search/exa_ai-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest breakthroughs in quantum computing",
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/exa_ai-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "latest breakthroughs in quantum computing", "max_results": 10},
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search/exa_ai-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "latest breakthroughs in quantum computing",
        max_results: 10
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```


## جستجوی معنایی با فیلتر دامنه

جستجوی عصبی Exa AI در درک کوئری‌های پیچیده عالی است و می‌تواند با فیلترینگ دامنه برای نتایج هدفمند ترکیب شود.

```bash
curl https://api.avalai.ir/v1/search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "exa_ai-search",
    "query": "machine learning research papers",
    "max_results": 10,
    "search_domain_filter": ["arxiv.org", "paperswithcode.com", "scholar.google.com"]
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "exa_ai-search",
        "query": "machine learning research papers",
        "max_results": 10,
        "search_domain_filter": [
            "arxiv.org",
            "paperswithcode.com",
            "scholar.google.com",
        ],
    },
)

results = response.json()

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        search_tool_name: "exa_ai-search",
        query: "machine learning research papers",
        max_results: 10,
        search_domain_filter: ["arxiv.org", "paperswithcode.com", "scholar.google.com"]
    })
});

const data = await response.json();

```


## پارامترهای درخواست

جستجوی Exa AI از پارامترهای زیر پشتیبانی می‌کند:

| پارامتر              | نوع     | الزامی | توضیحات                                                      |
| -------------------- | ------- | ------ | ------------------------------------------------------------ |
| query                | string  | بله    | رشته کوئری جستجو                                             |
| max_results          | integer | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10                       |
| search_domain_filter | array   | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)            |
| max_tokens_per_page  | integer | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024        |
| country              | string  | خیر    | فیلتر کد کشور (مثلا "US"، "GB"، "DE")                       |

## فرمت پاسخ

جستجوهای Exa AI نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

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

## استفاده از Exa AI Search از طریق AvalAI

به جستجوی عصبی Exa AI با استفاده از اندپوینت Search API AvalAI دسترسی پیدا کنید. می‌توانید ابزار را در مسیر URL یا در بدنه درخواست مشخص کنید.

```python
import requests

# گزینه 1: ابزار در URL
response = requests.post(
    "https://api.avalai.ir/v1/search/exa_ai-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "artificial intelligence safety research", "max_results": 10},
)

# گزینه 2: ابزار در بدنه
response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "exa_ai-search",
        "query": "deep learning architectures for NLP",
        "max_results": 10,
        "search_domain_filter": ["arxiv.org", "proceedings.mlr.press"],
    },
)

results = response.json()
```

## چه زمانی از Exa AI Search استفاده کنیم

**از Exa AI Search استفاده کنید** وقتی:
- به درک معنایی کوئری‌های پیچیده نیاز دارید
- هدف کوئری مهم‌تر از تطبیق دقیق کلمات کلیدی است
- در حال ساخت برنامه‌های تحقیق یا کشف دانش هستید
- به رتبه‌بندی ارتباط مبتنی بر هوش مصنوعی نیاز دارید
- با محتوای فنی یا تخصصی کار می‌کنید
- زمینه و معنا برای کیفیت نتایج حیاتی است

## مزایای کلیدی

1. **درک معنایی**: فراتر از تطبیق کلمات کلیدی برای درک هدف کوئری می‌رود
2. **رتبه‌بندی عصبی**: امتیازدهی ارتباط مبتنی بر هوش مصنوعی برای کیفیت بهتر نتایج
3. **آگاهی از زمینه**: روابط و زمینه را در کوئری‌ها درک می‌کند
4. **بهینه شده برای تحقیق**: به ویژه برای جستجوهای آکادمیک و فنی موثر است
5. **کیفیت بر حجم**: تمرکز بر نتایج بسیار مرتبط به جای حجم

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
- [مستندات رسمی Exa AI](https://docs.exa.ai)
