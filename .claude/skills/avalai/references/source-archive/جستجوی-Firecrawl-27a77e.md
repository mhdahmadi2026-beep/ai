# جستجوی Firecrawl

AvalAI دسترسی به API جستجوی وب Firecrawl را فراهم می‌کند که قابلیت‌های جستجوی قدرتمند همراه با ویژگی‌های پیشرفته وب‌اسکرپینگ و استخراج محتوا را ارائه می‌دهد.

## ابزار جستجو

Firecrawl در ارائه نتایج جستجوی جامع با وب‌اسکرپینگ یکپارچه تخصص دارد و به شما امکان می‌دهد از منابع متعدد به طور همزمان جستجو کنید و محتوا استخراج نمایید.

### جستجوی Firecrawl

جستجوی پیشرفته وب با قابلیت‌های وب‌اسکرپینگ یکپارچه و پشتیبانی از چندین منبع.

| ویژگی      | جزئیات                                                     |
| ---------- | ---------------------------------------------------------- |
| شناسه ابزار | `firecrawl-search`                                         |
| اندپوینت   | `v1/search/firecrawl-search` یا `v1/search`              |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                     |
| قیمت‌گذاری | $0.008 به ازای هر کوئری                                    |
| قابلیت‌ها  | جستجوی چند منبعی، فیلتر دسته‌بندی، وب‌اسکرپینگ، جستجوی زمان‌بندی شده، هدف‌گیری جغرافیایی |
| نقاط قوت   | استخراج محتوا، فیلتر پیشرفته، انواع منابع متعدد             |
| بهترین برای | استخراج داده، تحقیق، جمع‌آوری محتوا، جستجوهای دارای اسکرپینگ |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search/firecrawl-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "artificial intelligence research",
    "max_results": 10,
    "sources": ["web", "news"],
    "categories": [{"type": "research"}],
    "scrapeOptions": {
      "formats": ["markdown"],
      "onlyMainContent": true,
      "removeBase64Images": true
    }
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "artificial intelligence research",
        "max_results": 10,
        "sources": ["web", "news"],
        "categories": [{"type": "research"}],
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "removeBase64Images": True,
        },
    },
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search/firecrawl-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "artificial intelligence research",
        max_results: 10,
        sources: ["web", "news"],
        categories: [{"type": "research"}],
        scrapeOptions: {
            formats: ["markdown"],
            onlyMainContent: true,
            removeBase64Images: true
        }
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```


## ویژگی‌ها

Firecrawl جستجوی وب را با قابلیت‌های قدرتمند اسکرپینگ ترکیب می‌کند:

### منابع متعدد

جستجو در منابع مختلف به طور همزمان:

- `web` - نتایج جستجوی وب (پیش‌فرض)
- `images` - نتایج جستجوی تصویر
- `news` - نتایج جستجوی اخبار با تاریخ

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "climate change",
        "sources": ["web", "news"],
        "max_results": 10,
    },
)
```

### فیلتر دسته‌بندی

فیلتر نتایج بر اساس دسته‌بندی‌های خاص:

- `github` - جستجو در مخازن، کد، مسائل و مستندات GitHub
- `research` - جستجو در وب‌سایت‌های آکادمیک و تحقیقاتی (arXiv، Nature، IEEE، PubMed و غیره)
- `pdf` - جستجو برای فایل‌های PDF

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "machine learning algorithms",
        "categories": [{"type": "github"}, {"type": "research"}],
        "max_results": 10,
    },
)
```

### جستجوی زمان‌بندی شده

از پارامتر `tbs` برای فیلتر بر اساس بازه‌های زمانی استفاده کنید:

- `qdr:h` - ساعت گذشته
- `qdr:d` - روز گذشته
- `qdr:w` - هفته گذشته
- `qdr:m` - ماه گذشته
- `qdr:y` - سال گذشته

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "AI news",
        "tbs": "qdr:m",  # ماه گذشته
        "max_results": 10,
    },
)
```

### اسکرپینگ محتوا

Firecrawl به طور خودکار محتوای کامل صفحه را برای نتایج جستجو زمانی که `scrapeOptions` مشخص شده است، اسکرپ می‌کند. به طور پیش‌فرض، LiteLLM فرمت markdown با فقط محتوای اصلی را درخواست می‌کند.

**گزینه‌های اسکرپینگ:**

- `formats` - فرمت محتوا (مثلا `["markdown"]`)
- `onlyMainContent` - فقط محتوای اصلی را استخراج کن (boolean)
- `removeBase64Images` - حذف تصاویر کدگذاری شده base64 (boolean)

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "Python best practices",
        "max_results": 5,
        "scrapeOptions": {
            "formats": ["markdown"],
            "onlyMainContent": True,
            "removeBase64Images": True,
        },
    },
)
```

### هدف‌گیری جغرافیایی

از پارامتر `location` برای نتایج هدف‌گیری شده جغرافیایی استفاده کنید. موقعیت باید در فرمت `"شهر،ایالت،کشور"` باشد:

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "restaurants",
        "location": "San Francisco,California,United States",
        "max_results": 10,
    },
)
```

### مدیریت URL نامعتبر

از `ignoreInvalidURLs` برای حذف URLهای نامعتبر از نتایج استفاده کنید:

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "web development tutorials",
        "ignoreInvalidURLs": True,
        "max_results": 10,
    },
)
```

## عملگرهای کوئری پشتیبانی شده

Firecrawl از عملگرهای جستجوی پیشرفته پشتیبانی می‌کند:

| عملگر | عملکرد | مثال |
|-------|--------|------|
| `""` | تطابق غیر فازی یک رشته متن | `"Firecrawl"` |
| `-` | حذف کلمات کلیدی خاص | `-bad`، `-site:example.com` |
| `site:` | فقط نتایج از یک وب‌سایت مشخص | `site:firecrawl.dev` |
| `inurl:` | فقط نتایجی که شامل یک کلمه در URL هستند | `inurl:firecrawl` |
| `allinurl:` | فقط نتایجی که شامل چند کلمه در URL هستند | `allinurl:git firecrawl` |
| `intitle:` | فقط نتایج با یک کلمه در عنوان | `intitle:Firecrawl` |
| `allintitle:` | فقط نتایج با چند کلمه در عنوان | `allintitle:firecrawl playground` |
| `related:` | فقط نتایج مرتبط با یک دامنه خاص | `related:firecrawl.dev` |

**مثال:**

```python
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": 'site:github.com "machine learning" -deprecated',
        "max_results": 10,
    },
)
```

## پارامترهای درخواست

جستجوی Firecrawl از پارامترهای زیر پشتیبانی می‌کند:

| پارامتر                | نوع     | الزامی | توضیحات                                              |
| ---------------------- | ------- | ------ | ---------------------------------------------------- |
| `query`                | string  | بله    | رشته کوئری جستجو                                     |
| `max_results`          | integer | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10              |
| `sources`              | array   | خیر    | منابع جستجو: `["web", "news", "images"]`            |
| `categories`           | array   | خیر    | فیلترهای دسته‌بندی: `[{"type": "github"}, {"type": "research"}, {"type": "pdf"}]` |
| `tbs`                  | string  | خیر    | جستجوی زمان‌بندی شده (مثلا `"qdr:m"` برای ماه گذشته) |
| `location`             | string  | خیر    | موقعیت جغرافیایی (مثلا `"San Francisco,California,United States"`) |
| `country`              | string  | خیر    | فیلتر کد کشور (مثلا `"US"`، `"GB"`، `"DE"`)       |
| `ignoreInvalidURLs`    | boolean | خیر    | حذف URLهای نامعتبر از نتایج                         |
| `scrapeOptions`        | object  | خیر    | پیکربندی اسکرپینگ برای محتوای نتایج                 |
| `scrapeOptions.formats` | array  | خیر    | فرمت‌های محتوا: `["markdown"]`                      |
| `scrapeOptions.onlyMainContent` | boolean | خیر | فقط محتوای اصلی را استخراج کن            |
| `scrapeOptions.removeBase64Images` | boolean | خیر | حذف تصاویر کدگذاری شده base64        |
| `search_domain_filter` | array   | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)   |
| `max_tokens_per_page`  | integer | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024 |

## فرمت پاسخ

جستجوهای Firecrawl نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

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

## استفاده از جستجوی Firecrawl از طریق AvalAI

با استفاده از اندپوینت API جستجوی AvalAI به جستجوی Firecrawl دسترسی پیدا کنید. می‌توانید ابزار را در مسیر URL یا در بدنه درخواست مشخص کنید.

```python
import requests

# گزینه 1: ابزار در URL
response = requests.post(
    "https://api.avalai.ir/v1/search/firecrawl-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "query": "latest AI developments",
        "sources": ["web", "news"],
        "max_results": 10,
    },
)

# گزینه 2: ابزار در بدنه با تمام گزینه‌های پیشرفته
response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "firecrawl-search",
        "query": "machine learning research",
        # پارامترهای اختصاصی Firecrawl
        "sources": ["web", "news"],  # جستجو در منابع متعدد
        "categories": [
            {"type": "github"},
            {"type": "research"},
        ],  # فیلتر بر اساس دسته‌بندی
        "tbs": "qdr:m",  # جستجوی زمان‌بندی شده (ماه گذشته)
        "location": "San Francisco,California,United States",  # هدف‌گیری جغرافیایی
        "ignoreInvalidURLs": True,  # حذف URLهای نامعتبر
        "scrapeOptions": {  # گزینه‌های اسکرپینگ برای نتایج
            "formats": ["markdown"],
            "onlyMainContent": True,
            "removeBase64Images": True,
        },
        "max_results": 10,
    },
)

results = response.json()
```

## موارد استفاده

**از جستجوی Firecrawl استفاده کنید** زمانی که:

- نیاز به استخراج و پردازش محتوای کامل صفحه دارید
- جستجو در انواع منابع متعدد (وب، اخبار، تصاویر)
- فیلتر بر اساس دسته‌بندی‌های خاص (GitHub، مقالات تحقیقاتی، PDFها)
- انجام جستجوهای حساس به زمان
- هدف‌گیری جغرافیایی نتایج جستجو
- استفاده از عملگرهای جستجوی پیشرفته
- ساخت برنامه‌های استخراج داده یا وب‌اسکرپینگ
- جمع‌آوری محتوا از منابع متعدد

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
