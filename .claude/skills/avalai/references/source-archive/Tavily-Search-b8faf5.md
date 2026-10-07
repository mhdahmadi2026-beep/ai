# Tavily Search

AvalAI دسترسی به API جستجوی وب Tavily را فراهم می‌کند که قابلیت‌های جستجوی جامع با سطوح استاندارد و پیشرفته برای موارد استفاده مختلف ارائه می‌دهد.

## ابزارهای جستجو

Tavily در ارائه نتایج جستجوی با کیفیت بالای وب که برای برنامه‌های هوش مصنوعی و سیستم‌های RAG (Retrieval-Augmented Generation) بهینه شده‌اند، تخصص دارد.

### Tavily Search (استاندارد)

جستجوی وب استاندارد با پوشش جامع و نتایج با کیفیت.

| ویژگی       | جزئیات                                                        |
| ----------- | ------------------------------------------------------------- |
| شناسه ابزار | `tavily-search`                                               |
| اندپوینت    | `v1/search/tavily-search` یا `v1/search`                    |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                        |
| قیمت‌گذاری  | $0.008 به ازای هر کوئری                                       |
| قابلیت‌ها    | جستجوی وب، فیلتر دامنه، نتایج خاص کشور                       |
| نقاط قوت    | پوشش جامع وب، نتایج قابل اعتماد                              |
| بهترین برای | جستجوهای عمومی وب، برنامه‌های RAG، تحقیق                     |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search/tavily-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "latest AI developments 2024",
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/tavily-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "latest AI developments 2024", "max_results": 10},
)

results = response.json()
for result in results["results"]:
    print(f"{result['title']}: {result['url']}")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/search/tavily-search", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        query: "latest AI developments 2024",
        max_results: 10
    })
});

const data = await response.json();
data.results.forEach(result => {
    console.log(`${result.title}: ${result.url}`);
});

```


### Tavily Search Advanced

جستجوی پیشرفته با قابلیت‌های فیلترینگ پیشرفته و کیفیت عمیق‌تر نتایج.

| ویژگی       | جزئیات                                                               |
| ----------- | -------------------------------------------------------------------- |
| شناسه ابزار | `tavily-search-advanced`                                             |
| اندپوینت    | `v1/search/tavily-search-advanced` یا `v1/search`                  |
| حداکثر نتایج | 1-20 نتیجه در هر کوئری                                               |
| قیمت‌گذاری  | $0.016 به ازای هر کوئری                                              |
| قابلیت‌ها    | جستجوی پیشرفته وب، فیلترینگ بهبود یافته، تحلیل عمیق‌تر نتایج       |
| نقاط قوت    | نتایج با کیفیت بالاتر، فیلترینگ بهتر، محتوای دقیق‌تر               |
| بهترین برای | تحقیقات پیچیده، جستجوهای تخصصی، RAG با دقت بالا                    |

**نمونه استفاده:**

```bash
curl https://api.avalai.ir/v1/search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "tavily-search-advanced",
    "query": "machine learning research papers",
    "max_results": 10,
    "search_domain_filter": ["arxiv.org", "scholar.google.com"],
    "country": "united states"
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "tavily-search-advanced",
        "query": "machine learning research papers",
        "max_results": 10,
        "search_domain_filter": ["arxiv.org", "scholar.google.com"],
        "country": "united states",
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
        search_tool_name: "tavily-search-advanced",
        query: "machine learning research papers",
        max_results: 10,
        search_domain_filter: ["arxiv.org", "scholar.google.com"],
        country: "united states"
    })
});

const data = await response.json();

```


## پارامترهای درخواست

تمام ابزارهای جستجوی Tavily از پارامترهای زیر پشتیبانی می‌کنند:

| پارامتر              | نوع     | الزامی | توضیحات                                                      |
| -------------------- | ------- | ------ | ------------------------------------------------------------ |
| query                | string  | بله    | رشته کوئری جستجو                                             |
| max_results          | integer | خیر    | حداکثر تعداد نتایج (1-20). پیش‌فرض: 10                       |
| search_domain_filter | array   | خیر    | لیست دامنه‌ها برای فیلتر نتایج (حداکثر 20 دامنه)            |
| max_tokens_per_page  | integer | خیر    | حداکثر توکن‌ها در هر صفحه برای پردازش. پیش‌فرض: 1024        |
| country              | string  | خیر    | نام کشور برای اولویت‌دهی به نتایج جستجو (فقط زمانی که topic برابر general باشد). مقادیر مجاز شامل: `afghanistan`, `albania`, `algeria`, `andorra`, `angola`, `argentina`, `armenia`, `australia`, `austria`, `azerbaijan`, `bahamas`, `bahrain`, `bangladesh`, `barbados`, `belarus`, `belgium`, `belize`, `benin`, `bhutan`, `bolivia`, `bosnia and herzegovina`, `botswana`, `brazil`, `brunei`, `bulgaria`, `burkina faso`, `burundi`, `cambodia`, `cameroon`, `canada`, `cape verde`, `central african republic`, `chad`, `chile`, `china`, `colombia`, `comoros`, `congo`, `costa rica`, `croatia`, `cuba`, `cyprus`, `czech republic`, `denmark`, `djibouti`, `dominican republic`, `ecuador`, `egypt`, `el salvador`, `equatorial guinea`, `eritrea`, `estonia`, `ethiopia`, `fiji`, `finland`, `france`, `gabon`, `gambia`, `georgia`, `germany`, `ghana`, `greece`, `guatemala`, `guinea`, `haiti`, `honduras`, `hungary`, `iceland`, `india`, `indonesia`, `iran`, `iraq`, `ireland`, `israel`, `italy`, `jamaica`, `japan`, `jordan`, `kazakhstan`, `kenya`, `kuwait`, `kyrgyzstan`, `latvia`, `lebanon`, `lesotho`, `liberia`, `libya`, `liechtenstein`, `lithuania`, `luxembourg`, `madagascar`, `malawi`, `malaysia`, `maldives`, `mali`, `malta`, `mauritania`, `mauritius`, `mexico`, `moldova`, `monaco`, `mongolia`, `montenegro`, `morocco`, `mozambique`, `myanmar`, `namibia`, `nepal`, `netherlands`, `new zealand`, `nicaragua`, `niger`, `nigeria`, `north korea`, `north macedonia`, `norway`, `oman`, `pakistan`, `panama`, `papua new guinea`, `paraguay`, `peru`, `philippines`, `poland`, `portugal`, `qatar`, `romania`, `russia`, `rwanda`, `saudi arabia`, `senegal`, `serbia`, `singapore`, `slovakia`, `slovenia`, `somalia`, `south africa`, `south korea`, `south sudan`, `spain`, `sri lanka`, `sudan`, `sweden`, `switzerland`, `syria`, `taiwan`, `tajikistan`, `tanzania`, `thailand`, `togo`, `trinidad and tobago`, `tunisia`, `turkey`, `turkmenistan`, `uganda`, `ukraine`, `united arab emirates`, `united kingdom`, `united states`, `uruguay`, `uzbekistan`, `venezuela`, `vietnam`, `yemen`, `zambia`, `zimbabwe`. برای اطلاعات بیشتر به [مستندات رسمی Tavily](https://docs.tavily.com/documentation/api-reference/endpoint/search) مراجعه کنید. |

## فرمت پاسخ

تمام جستجوهای Tavily نتایج را در فرمت پاسخ استاندارد جستجو برمی‌گردانند:

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

## استفاده از Tavily Search از طریق AvalAI

به ابزارهای جستجوی Tavily با استفاده از اندپوینت Search API AvalAI دسترسی پیدا کنید. می‌توانید ابزار را در مسیر URL یا در بدنه درخواست مشخص کنید.

```python
import requests

# گزینه 1: ابزار در URL
response = requests.post(
    "https://api.avalai.ir/v1/search/tavily-search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={"query": "artificial intelligence trends", "max_results": 10},
)

# گزینه 2: ابزار در بدنه
response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "search_tool_name": "tavily-search-advanced",
        "query": "artificial intelligence trends",
        "max_results": 10,
        "search_domain_filter": ["techcrunch.com", "wired.com"],
    },
)

results = response.json()
```

## انتخاب بین استاندارد و پیشرفته

**از Tavily Search (استاندارد) استفاده کنید** وقتی:
- به نتایج جستجوی عمومی وب نیاز دارید
- کارایی هزینه اولویت است
- کیفیت جستجوی استاندارد نیازهای شما را برآورده می‌کند
- در حال ساخت برنامه‌های RAG عمومی هستید

**از Tavily Search Advanced استفاده کنید** وقتی:
- به نتایج با کیفیت بالاتر و دقیق‌تر نیاز دارید
- در حال انجام تحقیقات تخصصی یا پیچیده هستید
- به قابلیت‌های فیلترینگ پیشرفته نیاز دارید
- دقت مهم‌تر از هزینه است

## منابع مرتبط

- [مرجع API جستجو](fa/api-reference/search.md)
- [اعلامیه Search API](fa/news/2025-10-26-search-api-launched.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [احراز هویت](fa/api-reference/authentication.md)
