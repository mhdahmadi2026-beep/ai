# استفاده از API جستجوی v1/search

## مقدمه

API `v1/search` یک **endpoint اختصاصی جستجوی وب** است که دسترسی برنامه‌نویسی به موتورهای جستجو و ابزارهای متعدد را فراهم می‌کند. برخلاف جستجوی وب در chat completions (که پاسخ‌های LLM را با داده‌های بلادرنگ تقویت می‌کند)، API `v1/search` به طور مستقیم نتایج جستجوی ساختاریافته از ارائه‌دهندگان مختلف را بدون پردازش LLM برمی‌گرداند.

**تفاوت کلیدی:**
- **وب سرویس v1/search**: دسترسی مستقیم برنامه‌نویسی به جستجو ← بازگشت نتایج خام جستجو (URL‌ها، اسنیپت‌ها، متادیتا)
- **جستجوی وب در Chat Completions**: جستجوی تقویت‌شده با LLM ← بازگشت پاسخ‌های تولید شده توسط هوش مصنوعی با استنادات

> **مهم:** این متفاوت از [جستجوی وب در Chat Completions](fa/guides/tools-web-search.md) است که به مدل‌های زبانی امکان جستجوی وب را در طول مکالمات می‌دهد. اندپوینت `v1/search` یک API جستجوی وب مستقل است که نتایج جستجوی خام را برای استفاده برنامه‌نویسی برمی‌گرداند، در حالی که جستجوی وب در chat completions پاسخ‌های هوش مصنوعی را با داده‌های وب بلادرنگ تقویت می‌کند.

این باعث می‌شود API ‍‍‍`v1/search` برای برنامه‌هایی که به نتایج مستقیم جستجو، تجمیع داده، اتوماسیون تحقیق یا ساخت رابط‌های جستجوی سفارشی نیاز دارند، ایده‌آل باشد.

## ویژگی‌های کلیدی

- **10 ابزار جستجو** - دسترسی به Serper، Perplexity، Tavily، Firecrawl، Parallel AI، Exa AI، Google PSE و DataForSEO
- **فرمت API یکپارچه** - یک endpoint واحد با ساختار پاسخ سازگار با Perplexity
- **ارائه‌دهندگان متعدد** - انتخاب بهترین ابزار جستجو برای مورد استفاده و بودجه شما
- **نتایج ساختاریافته** - دریافت نتایج جستجوی سازماندهی‌شده با URL‌ها، اسنیپت‌ها و متادیتا
- **مقرون به صرفه** - پرداخت به ازای هر کوئری با قیمت‌گذاری از $0.001 تا $0.025
- **بدون پردازش LLM** - نتایج مستقیم جستجو بدون تفسیر هوش مصنوعی

## ابزارهای جستجوی موجود

| ابزار جستجو | ارائه‌دهنده | قیمت/کوئری | بهترین برای |
|------------|----------|-------------|----------|
| `serper-search` | Serper | $0.001 | کم‌هزینه‌ترین جستجوی مبتنی بر Google |
| `dataforseo-search` | DataForSEO | $0.003 | جستجوی عمومی مقرون به صرفه |
| `parallel_ai-search` | Parallel AI | $0.004 | جستجوی موازی سریع |
| `perplexity-search` | Perplexity | $0.005 | عملکرد متعادل |
| `tavily-search` | Tavily | $0.008 | جستجوی وب استاندارد |
| `firecrawl-search` | Firecrawl | $0.008 | جستجو با استخراج محتوا و اسکرپینگ |
| `parallel_ai-search-pro` | Parallel AI | $0.009 | جستجوی موازی پیشرفته |
| `tavily-search-advanced` | Tavily | $0.016 | جستجوی عمیق با تحلیل |
| `exa_ai-search` | Exa AI | $0.025 | جستجوی معنایی عصبی |

## استفاده پایه

### روش 1: مشخص کردن ابزار در URL

ساده‌ترین روش استفاده از API ‍‍‍`v1/search` شامل کردن نام ابزار جستجو مستقیما در URL است:

```bash
curl https://api.avalai.ir/v1/search/perplexity-search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "آخرین پیشرفت‌ها در محاسبات کوانتومی",
    "max_results": 5
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از کتابخانه requests برای فراخوانی مستقیم API
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/perplexity-search",
    headers={
        "Content-Type": "application/json",
        "Authorization": f"Bearer {client.api_key}",
    },
    json={"query": "آخرین پیشرفت‌ها در محاسبات کوانتومی", "max_results": 5},
)

results = response.json()
print(results)

```

```javascript
import fetch from 'node-fetch';

const response = await fetch('https://api.avalai.ir/v1/search/perplexity-search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'آخرین پیشرفت‌ها در محاسبات کوانتومی',
    max_results: 5
  })
});

const results = await response.json();
console.log(results);

```

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	requestBody, _ := json.Marshal(map[string]interface{}{
		"query":       "آخرین پیشرفت‌ها در محاسبات کوانتومی",
		"max_results": 5,
	})

	req, _ := http.NewRequest("POST",
		"https://api.avalai.ir/v1/search/perplexity-search",
		bytes.NewBuffer(requestBody))

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

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

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'query' => 'آخرین پیشرفت‌ها در محاسبات کوانتومی',
    'max_results' => 5
];

$ch = curl_init('https://api.avalai.ir/v1/search/perplexity-search');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$results = json_decode($response, true);
print_r($results);

```


### روش 2: مشخص کردن ابزار در بدنه درخواست

به طور جایگزین، می‌توانید ابزار جستجو را در بدنه درخواست با استفاده از endpoint پایه `v1/search` مشخص کنید:

```bash
curl https://api.avalai.ir/v1/search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "search_tool_name": "tavily-search",
    "query": "تاثیر تغییرات اقلیمی بر یخ‌های قطبی",
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={
        "search_tool_name": "tavily-search",
        "query": "تاثیر تغییرات اقلیمی بر یخ‌های قطبی",
        "max_results": 10,
    },
)

results = response.json()

# دسترسی به نتایج جستجو
for result in results.get("results", []):
    print(f"عنوان: {result['title']}")
    print(f"URL: {result['url']}")
    print(f"اسنیپت: {result['snippet']}")
    print("---")

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    search_tool_name: 'tavily-search',
    query: 'تاثیر تغییرات اقلیمی بر یخ‌های قطبی',
    max_results: 10
  })
});

const results = await response.json();

// پردازش نتایج
results.results?.forEach(result => {
  console.log(`عنوان: ${result.title}`);
  console.log(`URL: ${result.url}`);
  console.log(`اسنیپت: ${result.snippet}`);
  console.log('---');
});

```

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

type SearchRequest struct {
	SearchToolName string `json:"search_tool_name"`
	Query          string `json:"query"`
	MaxResults     int    `json:"max_results"`
}

type SearchResult struct {
	Title   string `json:"title"`
	URL     string `json:"url"`
	Snippet string `json:"snippet"`
}

type SearchResponse struct {
	Results []SearchResult `json:"results"`
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	searchReq := SearchRequest{
		SearchToolName: "tavily-search",
		Query:          "تاثیر تغییرات اقلیمی بر یخ‌های قطبی",
		MaxResults:     10,
	}

	requestBody, _ := json.Marshal(searchReq)

	req, _ := http.NewRequest("POST",
		"https://api.avalai.ir/v1/search",
		bytes.NewBuffer(requestBody))

	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)

	var searchResp SearchResponse
	json.Unmarshal(body, &searchResp)

	for _, result := range searchResp.Results {
		fmt.Printf("عنوان: %s\n", result.Title)
		fmt.Printf("URL: %s\n", result.URL)
		fmt.Printf("اسنیپت: %s\n", result.Snippet)
		fmt.Println("---")
	}
}

```

```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'search_tool_name' => 'tavily-search',
    'query' => 'تاثیر تغییرات اقلیمی بر یخ‌های قطبی',
    'max_results' => 10
];

$ch = curl_init('https://api.avalai.ir/v1/search');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$results = json_decode($response, true);

foreach ($results['results'] ?? [] as $result) {
    echo "عنوان: " . $result['title'] . "\n";
    echo "URL: " . $result['url'] . "\n";
    echo "اسنیپت: " . $result['snippet'] . "\n";
    echo "---\n";
}

```


## ویژگی‌های پیشرفته

### کنترل تعداد نتایج

تعداد نتایج دریافتی را با استفاده از پارامتر `max_results` مشخص کنید:

```bash
curl https://api.avalai.ir/v1/search/google_pse-search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "بهترین شیوه‌ها برای طراحی API",
    "max_results": 20
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/google_pse-search",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={"query": "بهترین شیوه‌ها برای طراحی API", "max_results": 20},
)

results = response.json()

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search/google_pse-search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'بهترین شیوه‌ها برای طراحی API',
    max_results: 20
  })
});

const results = await response.json();

```


### جستجوی Serper با فیلتر زمانی و هدف‌گیری جغرافیایی

از `serper-search` برای جستجوی کم‌هزینه مبتنی بر Google با پارامترهای اختصاصی Serper مانند `gl`، `hl`، `autocorrect`، `tbs` و `page` استفاده کنید:

```bash
curl https://api.avalai.ir/v1/search/serper-search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "restaurants",
    "max_results": 10,
    "gl": "uk",
    "hl": "en",
    "autocorrect": false,
    "tbs": "qdr:d",
    "page": 1,
    "country": "DE",
    "location": "Berlin,Germany"
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/serper-search",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={
        "query": "restaurants",
        "max_results": 10,
        # پارامترهای اختصاصی Serper
        "gl": "uk",  # کد کشور/موقعیت جغرافیایی
        "hl": "en",  # کد زبان
        "autocorrect": False,  # غیرفعال کردن اصلاح خودکار
        "tbs": "qdr:d",  # فیلتر زمانی: روز گذشته
        "page": 1,  # شماره صفحه
        # هدف‌گیری جغرافیایی
        "country": "DE",
        "location": "Berlin,Germany",
    },
)

results = response.json()

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search/serper-search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'restaurants',
    max_results: 10,
    // پارامترهای اختصاصی Serper
    gl: 'uk',              // کد کشور/موقعیت جغرافیایی
    hl: 'en',              // کد زبان
    autocorrect: false,    // غیرفعال کردن اصلاح خودکار
    tbs: 'qdr:d',          // فیلتر زمانی: روز گذشته
    page: 1,               // شماره صفحه
    // هدف‌گیری جغرافیایی
    country: 'DE',
    location: 'Berlin,Germany'
  })
});

const results = await response.json();

```


**مقادیر جستجوی زمانی:** `qdr:h` (ساعت گذشته)، `qdr:d` (روز گذشته)، `qdr:w` (هفته گذشته)، `qdr:m` (ماه گذشته) و `qdr:y` (سال گذشته).

### جستجوی خاص دامنه

از پارامتر `domains` برای محدود کردن نتایج جستجو به دامنه‌های خاص استفاده کنید:

```bash
curl https://api.avalai.ir/v1/search/tavily-search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "آموزش یادگیری ماشین",
    "domains": ["arxiv.org", "papers.nips.cc", "scholar.google.com"],
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/tavily-search",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={
        "query": "آموزش یادگیری ماشین",
        "domains": ["arxiv.org", "papers.nips.cc", "scholar.google.com"],
        "max_results": 10,
    },
)

results = response.json()

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search/tavily-search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'آموزش یادگیری ماشین',
    domains: ['arxiv.org', 'papers.nips.cc', 'scholar.google.com'],
    max_results: 10
  })
});

const results = await response.json();

```


### کنترل عمق جستجو (Tavily پیشرفته)

برای تحلیل عمیق‌تر جستجو، از `tavily-search-advanced` با کنترل عمق جستجو استفاده کنید:

```bash
curl https://api.avalai.ir/v1/search/tavily-search-advanced \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "تحلیل جامع روندهای انرژی تجدیدپذیر",
    "search_depth": "advanced",
    "max_results": 15
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/tavily-search-advanced",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={
        "query": "تحلیل جامع روندهای انرژی تجدیدپذیر",
        "search_depth": "advanced",
        "max_results": 15,
    },
)

results = response.json()

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search/tavily-search-advanced', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'تحلیل جامع روندهای انرژی تجدیدپذیر',
    search_depth: 'advanced',
    max_results: 15
  })
});

const results = await response.json();

```


### جستجوی معنایی عصبی (Exa AI)

برای قابلیت‌های جستجوی معنایی/عصبی، از Exa AI استفاده کنید:

```bash
curl https://api.avalai.ir/v1/search/exa_ai-search \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "query": "استارت‌آپ‌های نوآورانه در حال کار بر روی کشاورزی پایدار",
    "max_results": 10
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/search/exa_ai-search",
    headers={"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"},
    json={
        "query": "استارت‌آپ‌های نوآورانه در حال کار بر روی کشاورزی پایدار",
        "max_results": 10,
    },
)

results = response.json()

# Exa AI نتایج معنایی مرتبط ارائه می‌دهد
for result in results.get("results", []):
    print(f"URL مرتبط: {result['url']}")
    print(f"زمینه: {result['snippet']}")

```

```javascript
const response = await fetch('https://api.avalai.ir/v1/search/exa_ai-search', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
  },
  body: JSON.stringify({
    query: 'استارت‌آپ‌های نوآورانه در حال کار بر روی کشاورزی پایدار',
    max_results: 10
  })
});

const results = await response.json();

// پردازش نتایج معنایی مرتبط
results.results?.forEach(result => {
  console.log(`URL مرتبط: ${result.url}`);
  console.log(`زمینه: ${result.snippet}`);
});

‍‍‍‍

```


## موارد استفاده

### 1. اتوماسیون تحقیق

اتوماسیون تحقیق با جمع‌آوری اطلاعات از ابزارهای جستجوی متعدد:

```bash
# جستجو در چندین ارائه‌دهنده
curl https://api.avalai.ir/v1/search/dataforseo-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "دستورالعمل‌های اخلاقی هوش مصنوعی", "max_results": 5}'

curl https://api.avalai.ir/v1/search/exa_ai-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "دستورالعمل‌های اخلاقی هوش مصنوعی", "max_results": 5}'

```

```python
import requests
import asyncio
import aiohttp


async def search_multiple_providers(query):
    """جستجو همزمان در چندین ارائه‌دهنده"""
    api_key = "your-avalai-api-key"

    search_tools = [
        "serper-search",
        "dataforseo-search",
        "parallel_ai-search",
        "exa_ai-search",
    ]

    async with aiohttp.ClientSession() as session:
        tasks = []
        for tool in search_tools:
            url = f"https://api.avalai.ir/v1/search/{tool}"
            headers = {
                "Content-Type": "application/json",
                "Authorization": f"Bearer {api_key}",
            }
            data = {"query": query, "max_results": 5}

            tasks.append(session.post(url, json=data, headers=headers))

        responses = await asyncio.gather(*tasks)
        results = []
        for response in responses:
            results.append(await response.json())

        return results


# استفاده از تابع
results = asyncio.run(search_multiple_providers("دستورالعمل‌های اخلاقی هوش مصنوعی"))

# تجمیع و حذف تکراری نتایج
all_urls = set()
for provider_results in results:
    for result in provider_results.get("results", []):
        all_urls.add(result["url"])

print(f"{len(all_urls)} منبع منحصر به فرد پیدا شد")

```

```javascript
import fetch from 'node-fetch';

async function searchMultipleProviders(query) {
  const apiKey = process.env.AVALAI_API_KEY;
  
  const searchTools = [
    'serper-search',
    'dataforseo-search',
    'parallel_ai-search',
    'exa_ai-search'
  ];
  
  const promises = searchTools.map(tool =>
    fetch(`https://api.avalai.ir/v1/search/${tool}`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${apiKey}`
      },
      body: JSON.stringify({ query, max_results: 5 })
    }).then(r => r.json())
  );
  
  const results = await Promise.all(promises);
  
  // تجمیع و حذف تکراری
  const allUrls = new Set();
  results.forEach(providerResults => {
    providerResults.results?.forEach(result => {
      allUrls.add(result.url);
    });
  });
  
  console.log(`${allUrls.size} منبع منحصر به فرد پیدا شد`);
  return results;
}

// استفاده از تابع
const results = await searchMultipleProviders(
  'دستورالعمل‌های اخلاقی هوش مصنوعی'
);

```


### 2. مقایسه و نظارت بر قیمت

ساخت سیستم نظارت بر قیمت با استفاده از ابزارهای جستجوی مقرون به صرفه:

```bash
# استفاده از DataForSEO برای نظارت مقرون به صرفه بر قیمت
curl https://api.avalai.ir/v1/search/dataforseo-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "قیمت iPhone 15 Pro Max",
    "max_results": 20
  }'

```

```python
import requests
import re
from datetime import datetime


def monitor_prices(product_query):
    """نظارت بر قیمت‌های یک محصول در فروشگاه‌های مختلف"""
    response = requests.post(
        "https://api.avalai.ir/v1/search/dataforseo-search",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"query": product_query, "max_results": 20},
    )

    results = response.json()

    prices = []
    for result in results.get("results", []):
        # استخراج قیمت از اسنیپت (مثال ساده‌شده)
        snippet = result.get("snippet", "")
        price_match = re.search(r"\$[\d,]+(?:\.\d{2})?", snippet)

        if price_match:
            prices.append(
                {
                    "url": result["url"],
                    "title": result["title"],
                    "price": price_match.group(),
                    "timestamp": datetime.now().isoformat(),
                }
            )

    return prices


# نظارت بر قیمت آیفون
iphone_prices = monitor_prices("قیمت iPhone 15 Pro Max")

for item in iphone_prices:
    print(f"{item['title']}: {item['price']}")
    print(f"URL: {item['url']}\n")

```

```javascript
async function monitorPrices(productQuery) {
  const response = await fetch('https://api.avalai.ir/v1/search/dataforseo-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
    },
    body: JSON.stringify({
      query: productQuery,
      max_results: 20
    })
  });
  
  const results = await response.json();
  
  const prices = [];
  results.results?.forEach(result => {
    // استخراج قیمت از اسنیپت
    const priceMatch = result.snippet?.match(/\$[\d,]+(?:\.\d{2})?/);
    
    if (priceMatch) {
      prices.push({
        url: result.url,
        title: result.title,
        price: priceMatch[0],
        timestamp: new Date().toISOString()
      });
    }
  });
  
  return prices;
}

// نظارت بر قیمت محصولات
const iphonePrices = await monitorPrices('قیمت iPhone 15 Pro Max');

iphonePrices.forEach(item => {
  console.log(`${item.title}: ${item.price}`);
  console.log(`URL: ${item.url}\n`);
});

```


### 3. تجمیع اخبار

تجمیع اخبار از منابع متعدد با استفاده از ابزارهای جستجوی سریع:

```bash
# استفاده از Parallel AI برای تجمیع سریع اخبار
curl https://api.avalai.ir/v1/search/parallel_ai-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "آخرین اخبار تکنولوژی",
    "max_results": 15
  }'

```

```python
import requests
from datetime import datetime


def aggregate_news(topic, max_results=15):
    """تجمیع مقالات خبری در مورد یک موضوع خاص"""
    response = requests.post(
        "https://api.avalai.ir/v1/search/parallel_ai-search",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"query": f"{topic} اخبار", "max_results": max_results},
    )

    results = response.json()

    articles = []
    for result in results.get("results", []):
        articles.append(
            {
                "title": result["title"],
                "url": result["url"],
                "snippet": result["snippet"],
                "fetched_at": datetime.now().isoformat(),
            }
        )

    return articles


# تجمیع اخبار تکنولوژی
tech_news = aggregate_news("هوش مصنوعی")

print(f"{len(tech_news)} مقاله پیدا شد:\n")
for article in tech_news[:5]:  # نمایش 5 مورد اول
    print(f"📰 {article['title']}")
    print(f"   {article['snippet'][:100]}...")
    print(f"   {article['url']}\n")

```

```javascript
async function aggregateNews(topic, maxResults = 15) {
  const response = await fetch('https://api.avalai.ir/v1/search/parallel_ai-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
    },
    body: JSON.stringify({
      query: `${topic} اخبار`,
      max_results: maxResults
    })
  });
  
  const results = await response.json();
  
  const articles = results.results?.map(result => ({
    title: result.title,
    url: result.url,
    snippet: result.snippet,
    fetchedAt: new Date().toISOString()
  })) || [];
  
  return articles;
}

// تجمیع اخبار هوش مصنوعی
const aiNews = await aggregateNews('هوش مصنوعی');

console.log(`${aiNews.length} مقاله پیدا شد:\n`);
aiNews.slice(0, 5).forEach(article => {
  console.log(`📰 ${article.title}`);
  console.log(`   ${article.snippet.substring(0, 100)}...`);
  console.log(`   ${article.url}\n`);
});

```


### 4. تحقیقات آکادمیک

جستجوی منابع آکادمیک با استفاده از فیلتر دامنه خاص:

```bash
# جستجوی مقالات آکادمیک با استفاده از Tavily با فیلتر دامنه
curl https://api.avalai.ir/v1/search/tavily-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "پیشرفت محاسبات کوانتومی 2024",
    "domains": ["arxiv.org", "nature.com", "science.org", "scholar.google.com"],
    "max_results": 15
  }'

```

```python
import requests


def search_academic_papers(query, domains=None):
    """جستجوی مقالات آکادمیک از منابع معتبر"""
    if domains is None:
        domains = [
            "arxiv.org",
            "nature.com",
            "science.org",
            "scholar.google.com",
            "ieee.org",
            "acm.org",
        ]

    response = requests.post(
        "https://api.avalai.ir/v1/search/tavily-search",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"query": query, "domains": domains, "max_results": 15},
    )

    results = response.json()

    papers = []
    for result in results.get("results", []):
        papers.append(
            {
                "title": result["title"],
                "url": result["url"],
                "abstract": result["snippet"],
                "source": result["url"].split("/")[2],  # استخراج دامنه
            }
        )

    return papers


# جستجوی مقالات محاسبات کوانتومی
papers = search_academic_papers("پیشرفت محاسبات کوانتومی 2024")

print(f"{len(papers)} مقاله آکادمیک پیدا شد:\n")
for paper in papers:
    print(f"📄 {paper['title']}")
    print(f"   منبع: {paper['source']}")
    print(f"   {paper['url']}\n")

```

```javascript
async function searchAcademicPapers(query, domains = null) {
  if (!domains) {
    domains = [
      'arxiv.org',
      'nature.com',
      'science.org',
      'scholar.google.com',
      'ieee.org',
      'acm.org'
    ];
  }
  
  const response = await fetch('https://api.avalai.ir/v1/search/tavily-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
    },
    body: JSON.stringify({
      query,
      domains,
      max_results: 15
    })
  });
  
  const results = await response.json();
  
  const papers = results.results?.map(result => ({
    title: result.title,
    url: result.url,
    abstract: result.snippet,
    source: new URL(result.url).hostname
  })) || [];
  
  return papers;
}

// جستجوی مقالات محاسبات کوانتومی
const papers = await searchAcademicPapers('پیشرفت محاسبات کوانتومی 2024');

console.log(`${papers.length} مقاله آکادمیک پیدا شد:\n`);
papers.forEach(paper => {
  console.log(`📄 ${paper.title}`);
  console.log(`   منبع: ${paper.source}`);
  console.log(`   ${paper.url}\n`);
});

```


### 5. هوش رقابتی

استفاده از جستجوی معنایی Exa AI برای تحلیل رقابتی:

```bash
# استفاده از Exa AI برای جستجوی معنایی شرکت/رقبا
curl https://api.avalai.ir/v1/search/exa_ai-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "شرکت‌های در حال توسعه عامل‌های هوش مصنوعی برای اتوماسیون سازمانی",
    "max_results": 10
  }'

```

```python
import requests


def competitive_intelligence(query, max_results=10):
    """جمع‌آوری اطلاعات رقابتی با استفاده از جستجوی معنایی"""
    response = requests.post(
        "https://api.avalai.ir/v1/search/exa_ai-search",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"query": query, "max_results": max_results},
    )

    results = response.json()

    competitors = []
    for result in results.get("results", []):
        competitors.append(
            {
                "company": result["title"],
                "url": result["url"],
                "description": result["snippet"],
            }
        )

    return competitors


# یافتن رقبا در حوزه عامل‌های هوش مصنوعی
competitors = competitive_intelligence(
    "شرکت‌های در حال توسعه عامل‌های هوش مصنوعی برای اتوماسیون سازمانی"
)

print(f"{len(competitors)} شرکت مرتبط پیدا شد:\n")
for comp in competitors:
    print(f"🏢 {comp['company']}")
    print(f"   {comp['description'][:150]}...")
    print(f"   {comp['url']}\n")

```

```javascript
async function competitiveIntelligence(query, maxResults = 10) {
  const response = await fetch('https://api.avalai.ir/v1/search/exa_ai-search', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
    },
    body: JSON.stringify({
      query,
      max_results: maxResults
    })
  });
  
  const results = await response.json();
  
  const competitors = results.results?.map(result => ({
    company: result.title,
    url: result.url,
    description: result.snippet
  })) || [];
  
  return competitors;
}

// یافتن رقبا در حوزه عامل‌های هوش مصنوعی
const competitors = await competitiveIntelligence(
  'شرکت‌های در حال توسعه عامل‌های هوش مصنوعی برای اتوماسیون سازمانی'
);

console.log(`${competitors.length} شرکت مرتبط پیدا شد:\n`);
competitors.forEach(comp => {
  console.log(`🏢 ${comp.company}`);
  console.log(`   ${comp.description.substring(0, 150)}...`);
  console.log(`   ${comp.url}\n`);
});

```


## درک فرمت پاسخ

API ‍‍‍`v1/search` نتایج را در فرمت سازگار با Perplexity برمی‌گرداند:

```json
{
  "results": [
    {
      "title": "عنوان مقاله",
      "url": "https://example.com/article",

      "snippet": "متن پیش‌نمایش از مقاله...",
      "published_date": "2024-10-26",
      "author": "نام نویسنده"
    }
  ],
  "query": "کوئری جستجوی شما",
  "search_tool": "perplexity-search"
}
```

### پردازش نتایج

```python
import requests
import json


def process_search_results(query, search_tool="perplexity-search"):
    """پردازش و ساختاردهی نتایج جستجو"""
    response = requests.post(
        f"https://api.avalai.ir/v1/search/{search_tool}",
        headers={
            "Content-Type": "application/json",
            "Authorization": f"Bearer {api_key}",
        },
        json={"query": query, "max_results": 10},
    )

    data = response.json()

    # استخراج و ساختاردهی نتایج
    processed = {
        "query": data.get("query", query),
        "tool_used": data.get("search_tool", search_tool),
        "total_results": len(data.get("results", [])),
        "results": [],
    }

    for result in data.get("results", []):
        processed["results"].append(
            {
                "title": result.get("title", ""),
                "url": result.get("url", ""),
                "snippet": result.get("snippet", "")[:200],  # کوتاه‌سازی
                "published": result.get("published_date", "نامشخص"),
            }
        )

    return processed


# استفاده از تابع
results = process_search_results("راه‌حل‌های تغییرات اقلیمی")

print(f"کوئری: {results['query']}")
print(f"ابزار: {results['tool_used']}")
print(f"پیدا شد: {results['total_results']} نتیجه\n")

for i, result in enumerate(results["results"][:5], 1):
    print(f"{i}. {result['title']}")
    print(f"   {result['snippet']}")
    print(f"   {result['url']}\n")

```

```javascript
async function processSearchResults(query, searchTool = 'perplexity-search') {
  const response = await fetch(`https://api.avalai.ir/v1/search/${searchTool}`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
      'Authorization': `Bearer ${process.env.AVALAI_API_KEY}`
    },
    body: JSON.stringify({
      query,
      max_results: 10
    })
  });
  
  const data = await response.json();
  
  // استخراج و ساختاردهی نتایج
  const processed = {
    query: data.query || query,
    toolUsed: data.search_tool || searchTool,
    totalResults: data.results?.length || 0,
    results: data.results?.map(result => ({
      title: result.title || '',
      url: result.url || '',
      snippet: (result.snippet || '').substring(0, 200),
      published: result.published_date || 'نامشخص'
    })) || []
  };
  
  return processed;
}

// استفاده از تابع
const results = await processSearchResults('راه‌حل‌های تغییرات اقلیمی');

console.log(`ابزار: ${results.toolUsed}`);
console.log(`پیدا شد: ${results.totalResults} نتیجه\n`);

results.results.slice(0, 5).forEach((result, i) => {
  console.log(`${i + 1}. ${result.title}`);
  console.log(`   ${result.snippet}`);
  console.log(`   ${result.url}\n`);
});

```


## مقایسه: API ‍‍‍`v1/search` در برابر جستجوی وب داخل مدل

AvalAI هم API خام جستجو و هم جستجوی داخل مدل را پشتیبانی می‌کند. این دو را ابزارهای متفاوت بدانید، نه جایگزین مستقیم یکدیگر.

| ویژگی | API `/v1/search` | ابزار Responses `web_search` | مدل‌های search در Chat Completions |
| --- | --- | --- | --- |
| **خروجی** | نتایج خام: URL، snippet و متادیتای ارائه‌دهنده | پاسخ تولیدشده توسط AI همراه citation و متادیتای منبع اختیاری | پاسخ تولیدشده توسط AI همراه citation |
| **پردازش** | بدون synthesis توسط LLM | مدل تصمیم می‌گیرد چه زمانی و چگونه جستجو کند، مگر اینکه `tool_choice` اجباری شود | مدل تخصصی قبل از پاسخ جستجو می‌کند |
| **بهترین کاربرد** | crawling، monitoring، aggregation و ranking سفارشی | assistantها، Q&A، تحقیق و تولید گزارش | یکپارچه‌سازی‌های موجود Chat Completions |
| **کنترل‌ها** | پارامترهای خاص ارائه‌دهنده | `search_context_size`، متادیتای منابع، فیلتر دامنه و کنترل دسترسی زنده در صورت پشتیبانی | محدودتر از ابزارهای Responses |
| **مسیر مهاجرت** | برای pipelineهای داده خام نگه دارید | برای پاسخ‌های جدید تولیدشده توسط مدل ترجیح دهید | فقط وقتی باید Chat Completions حفظ شود نگه دارید |

### چه زمانی از `/v1/search` استفاده کنیم

وقتی به دسترسی مستقیم به نتایج جستجو بدون تفسیر مدل، چند URL برای پردازش پایین‌دستی، aggregation کم‌تاخیر یا قابلیت‌های خاص ارائه‌دهنده‌هایی مثل `serper-search`، `tavily-search`، `exa_ai-search` یا `dataforseo-search` نیاز دارید، از `/v1/search` استفاده کنید.

### چه زمانی از Responses `web_search` استفاده کنیم

وقتی برنامه باید در زبان طبیعی پاسخ دهد، منابع را در متن cite کند، در صورت نیاز بیشتر جستجو کند یا جستجو را با reasoning، structured output، function calling یا conversation state ترکیب کند، از Responses `web_search` استفاده کنید.

### چه زمانی Chat Completions search را نگه داریم

مثال‌های Chat Completions search را برای یکپارچه‌سازی‌های موجود و مدل‌های search پشتیبانی‌شده در AvalAI که در `data/models.json` هستند نگه دارید. برای کار جدید، Responses `web_search` را ترجیح دهید چون کنترل ابزار غنی‌تر و مسیر مهاجرت روشن‌تری دارد.

**مثال تفاوت:**

```bash
# API /v1/search - بازگشت نتایج خام جستجو
curl https://api.avalai.ir/v1/search/perplexity-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"query": "محاسبات کوانتومی چیست؟", "max_results": 5}'

# بازگشت: URL، عنوان، snippet و متادیتای ارائه‌دهنده

# Responses web_search - بازگشت پاسخ AI همراه citation
curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "tools": [{"type": "web_search", "search_context_size": "medium"}],
    "include": ["web_search_call.action.sources"],
    "input": "محاسبات کوانتومی چیست؟ با منابع به‌روز توضیح بده."
  }'

# بازگشت: پاسخ ترکیبی همراه annotationهای citation و متادیتای منابع

# Chat Completions search - برای یکپارچه‌سازی‌های پشتیبانی‌شده موجود نگه دارید
curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-search-preview",
    "messages": [{"role": "user", "content": "محاسبات کوانتومی چیست؟"}]
  }'

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه Responses API همراه ابزار `web_search`</summary>

برای پاسخ‌های جدیدی که مدل با جستجوی وب تولید می‌کند، از این نسخه استفاده کنید. `messages` به `input` منتقل می‌شود، دسترسی وب در `tools` اعلام می‌شود و متن نهایی از `response.output_text` خوانده می‌شود؛ برای جزئیات `web_search_call` و `url_citation`، `response.output` را بررسی کنید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    tools=[{"type": "web_search", "search_context_size": "medium"}],
    include=["web_search_call.action.sources"],
    input="محاسبات کوانتومی چیست؟ با منابع به‌روز توضیح بده.",
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
  tools: [{ type: "web_search", search_context_size: "medium" }],
  include: ["web_search_call.action.sources"],
  input: "محاسبات کوانتومی چیست؟ با منابع به‌روز توضیح بده.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "tools": [{"type": "web_search", "search_context_size": "medium"}],
    "include": ["web_search_call.action.sources"],
    "input": "محاسبات کوانتومی چیست؟ با منابع به‌روز توضیح بده."
  }'

```


- Chat `messages` → Responses `input`
- مدل search در Chat → مدل پشتیبان Responses همراه `tools: [{"type": "web_search"}]`
- `choices[0].message.content` → `response.output_text`
- برای `web_search_call`، `message`، `url_citation` و متادیتای اختیاری `sources`، `response.output` را بررسی کنید.

</details>
<!-- responses-equivalent:end -->

## بهترین شیوه‌ها

### 1. انتخاب ابزار جستجوی مناسب

ابزارهای جستجو را بر اساس نیازهای خود انتخاب کنید:

- **برنامه‌های با کمترین هزینه**: از `serper-search` استفاده کنید ($0.001/کوئری)
- **برنامه‌های حساس به هزینه**: از `dataforseo-search` استفاده کنید ($0.003/کوئری)
- **جستجوی عمومی وب**: از `perplexity-search` یا `google_pse-search` استفاده کنید ($0.005/کوئری)
- **جستجوی معنایی/عصبی**: از `exa_ai-search` استفاده کنید ($0.025/کوئری)
- **تحقیق عمیق**: از `tavily-search-advanced` استفاده کنید ($0.016/کوئری)
- **جستجوی موازی سریع**: از `parallel_ai-search` یا `parallel_ai-search-pro` استفاده کنید

### 2. بهینه‌سازی تعداد نتایج

تعادل بین هزینه و جامعیت:

```python
# برای جستجوهای سریع
response = search("query", max_results=5)  # ارزان‌تر، سریع‌تر

# برای تحقیق جامع
response = search("query", max_results=20)  # کامل‌تر

# توجه: اکثر ارائه‌دهندگان از 1-20 نتیجه در هر کوئری پشتیبانی می‌کنند
```

### 3. پیاده‌سازی کش

کش کردن نتایج جستجو برای کاهش هزینه‌ها:

```python
import requests
from functools import lru_cache
from datetime import datetime, timedelta


class SearchCache:
    def __init__(self, api_key):
        self.api_key = api_key
        self.cache = {}

    def search(
        self,
        query,
        search_tool="dataforseo-search",
        max_results=10,
        cache_duration=3600,
    ):
        """جستجو با کش (cache_duration به ثانیه)"""
        cache_key = f"{search_tool}:{query}:{max_results}"

        # بررسی کش
        if cache_key in self.cache:
            cached_data, timestamp = self.cache[cache_key]
            if datetime.now() - timestamp < timedelta(seconds=cache_duration):
                print(f"✓ استفاده از نتایج کش شده برای: {query}")
                return cached_data

        # انجام جستجو
        print(f"🔍 در حال جستجو: {query}")
        response = requests.post(
            f"https://api.avalai.ir/v1/search/{search_tool}",
            headers={
                "Content-Type": "application/json",
                "Authorization": f"Bearer {self.api_key}",
            },
            json={"query": query, "max_results": max_results},
        )

        results = response.json()

        # به‌روزرسانی کش
        self.cache[cache_key] = (results, datetime.now())

        return results


# استفاده
cache = SearchCache(api_key="your-avalai-api-key")

# فراخوانی اول - انجام جستجو
results1 = cache.search("پیشرفت‌های هوش مصنوعی", cache_duration=1800)  # کش برای 30 دقیقه

# فراخوانی دوم - استفاده از کش
results2 = cache.search(
    "پیشرفت‌های هوش مصنوعی", cache_duration=1800
)  # بدون فراخوانی API
```

### 4. مدیریت خطاها به درستی

پیاده‌سازی منطق تلاش مجدد و مدیریت خطا:

```python
import requests
from time import sleep


def robust_search(query, search_tool="perplexity-search", max_retries=3):
    """جستجو با منطق تلاش مجدد و مدیریت خطا"""
    for attempt in range(max_retries):
        try:
            response = requests.post(
                f"https://api.avalai.ir/v1/search/{search_tool}",
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
                json={"query": query, "max_results": 10},
                timeout=30,
            )

            response.raise_for_status()  # خطا برای 4xx/5xx

            return response.json()

        except requests.exceptions.Timeout:
            print(f"تایم‌اوت در تلاش {attempt + 1}/{max_retries}")
            if attempt < max_retries - 1:
                sleep(2**attempt)  # backoff نمایی

        except requests.exceptions.RequestException as e:
            print(f"خطا در تلاش {attempt + 1}/{max_retries}: {str(e)}")
            if attempt < max_retries - 1:
                sleep(2**attempt)
            else:
                raise

    return None


# استفاده
results = robust_search("محاسبات کوانتومی")
if results:
    print(f"{len(results.get('results', []))} نتیجه پیدا شد")
else:
    print("جستجو پس از تلاش‌های مجدد ناموفق بود")
```

### 5. پردازش دسته‌ای

پردازش کارآمد چندین کوئری:

```python
import asyncio
import aiohttp


async def batch_search(queries, search_tool="dataforseo-search", max_results=10):
    """جستجوی همزمان چندین کوئری"""
    async with aiohttp.ClientSession() as session:
        tasks = []

        for query in queries:
            task = session.post(
                f"https://api.avalai.ir/v1/search/{search_tool}",
                json={"query": query, "max_results": max_results},
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {api_key}",
                },
            )
            tasks.append(task)

        responses = await asyncio.gather(*tasks, return_exceptions=True)

        results = []
        for i, response in enumerate(responses):
            if isinstance(response, Exception):
                print(f"خطا برای کوئری '{queries[i]}': {str(response)}")
                results.append(None)
            else:
                results.append(await response.json())

        return results


# استفاده
queries = [
    "روندهای هوش مصنوعی 2024",
    "اخبار محاسبات کوانتومی",
    "پیشرفت‌های انرژی تجدیدپذیر",
]

results = asyncio.run(batch_search(queries))

for query, result in zip(queries, results):
    if result:
        print(f"✓ {query}: {len(result.get('results', []))} نتیجه")
    else:
        print(f"✗ {query}: ناموفق")
```

## قیمت‌گذاری و بهینه‌سازی هزینه

### هزینه به ازای هر کوئری

| ابزار جستجو | هزینه | درخواست به ازای هر $1 |
|------------|------|-----------------|
| serper-search | $0.001 | ~1000 |
| dataforseo-search | $0.003 | ~333 |
| parallel_ai-search | $0.004 | ~250 |
| perplexity-search | $0.005 | ~200 |
| google_pse-search | $0.005 | ~200 |
| tavily-search | $0.008 | ~125 |
| parallel_ai-search-pro | $0.009 | ~111 |
| tavily-search-advanced | $0.016 | ~62 |
| exa_ai-search | $0.025 | ~40 |

### استراتژی‌های بهینه‌سازی هزینه

1. **استفاده از ابزارهای ارزان‌تر برای جستجوهای پرحجم**:

```python
# برای نظارت بر قیمت (حجم بالا)
   tool = "serper-search"  # $0.001/کوئری

   # برای تحلیل معنایی (حجم کم، کیفیت بالا)
   tool = "exa_ai-search"  # $0.025/کوئری
```

2. **پیاده‌سازی جستجوی سطح‌بندی شده**:

```python
def tiered_search(query):
    # ابتدا کم‌هزینه‌ترین ابزار را امتحان کنید
    results = search(query, "serper-search", max_results=5)

    # اگر راضی‌کننده نیست، از ابزار پریمیوم استفاده کنید
    if not is_satisfactory(results):
        results = search(query, "exa_ai-search", max_results=10)

    return results
```

3. **نظارت و تحلیل هزینه‌ها**:

```python
import csv
   from datetime import datetime
   
   class CostTracker:
       COSTS = {
           "serper-search": 0.001,
           "dataforseo-search": 0.003,
           "parallel_ai-search": 0.004,
           "perplexity-search": 0.005,
           "google_pse-search": 0.005,
           "tavily-search": 0.008,
           "parallel_ai-search-pro": 0.009,
           "tavily-search-advanced": 0.016,
           "exa_ai-search": 0.025,
       }
       
       def __init__(self, log_file="search_costs.csv"):
           self.log_file = log_file
           self.total_cost = 0
           self.query_count = 0
       
       def log_search(self, search_tool, query):
           cost = self.COSTS.get(search_tool, 0)
           self.total_cost += cost
           self.query_count += 1
           
           with open(self.log_file, 'a', newline='') as f:
               writer = csv.writer(f)
               writer.writerow([
                   datetime.now().isoformat(),
                   search_tool,
                   query,
                   cost,
                   self.total_cost
               ])
           
           return cost
       
       def get_summary(self):
           return {
               'total_queries': self.query_count,
               'total_cost': f"${self.total_cost:.4f}",
               'avg_cost': f"${self.total_cost/self.query_count:.4f}" if self.query_count > 0 else "$0"
           }
   
   # استفاده
   tracker = CostTracker()
   
   # انجام جستجوها
   tracker.log_search("serper-search", "کوئری 1")
   tracker.log_search("dataforseo-search", "کوئری 2")
   tracker.log_search("perplexity-search", "کوئری 3")
   tracker.log_search("exa_ai-search", "کوئری 4")
   
   print(tracker.get_summary())
```

## محدودیت‌های نرخ و سهمیه

API ‍‍‍`v1/search` از محدودیت‌های سطح حساب AvalAI شما پیروی می‌کند. برای محدودیت‌های نرخ خاص سطح به [صفحه قیمت‌گذاری](fa/pricing.md) مراجعه کنید.

## مدیریت خطا

پاسخ‌های خطای رایج:

```json
{
  "error": {
    "message": "Invalid API key",
    "type": "authentication_error",
    "code": "invalid_api_key"
  }
}
```

```json
{
  "error": {
    "message": "Rate limit exceeded",
    "type": "rate_limit_error",
    "code": "rate_limit_exceeded"
  }
}
```

```json
{
  "error": {
    "message": "Invalid search tool",
    "type": "invalid_request_error",
    "code": "invalid_search_tool"
  }
}
```

## عیب‌یابی

### نتایج خالی

اگر نتایج خالی دریافت می‌کنید:

1. فرمت کوئری را بررسی کنید
2. ابزار جستجوی متفاوتی را امتحان کنید
3. پارامتر `max_results` را تنظیم کنید
4. تایید کنید که کوئری به زبان انگلیسی است (برخی ابزارها با کوئری‌های انگلیسی بهتر کار می‌کنند)

### خطاهای تایم‌اوت

برای مشکلات تایم‌اوت:

1. تعداد `max_results` را کاهش دهید
2. از ابزارهای جستجوی سریع‌تر استفاده کنید (`serper-search`، `parallel_ai-search`، `dataforseo-search`)
3. منطق تلاش مجدد با backoff نمایی را پیاده‌سازی کنید
4. تقسیم جستجوهای بزرگ به دسته‌های کوچک‌تر را در نظر بگیرید

### مدیریت هزینه

برای مدیریت مؤثر هزینه‌ها:

1. از کش برای کوئری‌های تکراری استفاده کنید
2. با ابزارهای جستجوی ارزان‌تر شروع کنید
3. حذف تکراری کوئری را پیاده‌سازی کنید
4. استفاده را با ردیابی هزینه زیر نظر بگیرید
5. هشدارهای بودجه را در برنامه خود تنظیم کنید

## مستندات مرتبط

- [مرجع API جستجو](fa/api-reference/search.md) - مشخصات کامل API
- [جستجوی وب در Chat Completions](fa/examples/web_search_capabilities.md) - جستجوی تقویت‌شده با LLM
- [ارائه‌دهندگان جستجو](fa/models/index.md) - اطلاعات تفصیلی ارائه‌دهنده
- [قیمت‌گذاری](fa/pricing.md) - اطلاعات هزینه و سطح

## نتیجه‌گیری

API v1/search دسترسی برنامه‌نویسی قدرتمند به موتورهای جستجوی متعدد را از طریق یک رابط یکپارچه فراهم می‌کند. با انتخاب ابزار جستجوی مناسب برای مورد استفاده خود و پیاده‌سازی بهترین شیوه‌ها برای کش و مدیریت خطا، می‌توانید برنامه‌های قدرتمند جستجومحور و مقرون به صرفه بسازید.

برای سؤالات یا پشتیبانی، به [مستندات](fa/index.md) ما مراجعه کنید یا با پشتیبانی تماس بگیرید.
