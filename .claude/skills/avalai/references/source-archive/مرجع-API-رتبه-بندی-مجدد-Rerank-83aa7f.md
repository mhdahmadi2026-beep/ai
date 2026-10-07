# مرجع API رتبه‌بندی مجدد (Rerank)

API رتبه‌بندی مجدد به شما امکان می‌دهد ارتباط نتایج جستجو یا لیست اسناد را با مرتب‌سازی مجدد آنها بر اساس ارتباطشان با یک پرس‌وجوی معین بهبود بخشید. این ویژگی به ویژه برای برنامه‌هایی که به نتایج جستجوی بسیار مرتبط از مجموعه بزرگی از اسناد نیاز دارند، مفید است.

> **نکته مهم:** نقطه پایانی rerank توسط SDK رسمی OpenAI پشتیبانی نمی‌شود. شما باید مستقیما از روش HTTP یا REST API استفاده کنید، همانطور که در مثال‌های زیر نشان داده شده است.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/rerank
```

## بدنه درخواست (Request Body)

| پارامتر            | نوع     | الزامی | توضیحات                                                                                                 |
| ------------------ | ------- | ------ | ------------------------------------------------------------------------------------------------------- |
| `model`            | string  | بله    | شناسه مدلی که باید استفاده شود. از `cohere-rerank-v4.0-pro`، `cohere-rerank-v4.0-fast`، `cohere.rerank-v3-5:0` و `qwen3-rerank` پشتیبانی می‌کند. |
| `query`            | string  | بله    | پرس‌وجوی جستجو برای رتبه‌بندی اسناد.                                                                    |
| `documents`        | array   | بله    | آرایه‌ای از رشته‌ها یا اشیا که نشان‌دهنده اسناد برای رتبه‌بندی مجدد هستند.                             |
| `top_n`            | integer | خیر    | تعداد نتایج برتر برای برگرداندن. پیش‌فرض تمام اسناد است.                                                |
| `return_documents` | boolean | خیر    | اینکه آیا محتوای سند در پاسخ برگردانده شود. پیش‌فرض `true` است.                                         |
| `user`             | string  | خیر    | یک شناسه منحصر به فرد که نماینده کاربر نهایی شما است و می‌تواند به نظارت و شناسایی سو استفاده کمک کند. |

### فرمت سند (Document Format)

اسناد می‌توانند در دو فرمت ارائه شوند:

1. به عنوان رشته‌ها:

```json
"documents": [
    "متن سند 1",
    "متن سند 2",
    "متن سند 3"
  ]
```

2. به عنوان اشیا با شناسه:

```json
"documents": [
    {
      "id": "doc1",
      "text": "متن سند 1"
    },
    {
      "id": "doc2",
      "text": "متن سند 2"
    },
    {
      "id": "doc3",
      "text": "متن سند 3"
    }
  ]
```

## مثال‌ها

### رتبه‌بندی مجدد پایه

```bash
curl https://api.avalai.ir/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "cohere.rerank-v3-5:0",
 "query": "مزایای انرژی‌های تجدیدپذیر چیست؟",
 "documents": [
 "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
 "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
 "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
 "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند."
 ]
}'

```

```python
import requests
import json

API_KEY = "YOUR_AVALAI_API_KEY"
AVALAI_BASE_URL = "https://api.avalai.ir/v1"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

data = {
    "model": "cohere.rerank-v3-5:0",
    "query": "مزایای انرژی‌های تجدیدپذیر چیست؟",
    "documents": [
        "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
        "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
        "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
        "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
    ],
}

response = requests.post(f"{AVALAI_BASE_URL}/rerank", headers=headers, json=data)

if response.status_code == 200:
    reranked_documents = response.json().get("results")
    for doc in reranked_documents:
        print(
            f"ایندکس: {doc['index']}، امتیاز ارتباط: {doc['relevance_score']}، سند: {doc['document']['text']}"
        )
else:
    print(f"خطا: {response.status_code} - {response.text}")

```

```javascript
const fetch = require("node-fetch"); // یا از fetch مرورگر استفاده کنید

const API_KEY = process.env.AVALAI_API_KEY;
const AVALAI_BASE_URL = "https://api.avalai.ir/v1";

async function rerankDocuments() {
  const data = {
    model: "cohere.rerank-v3-5:0",
    query: "مزایای انرژی‌های تجدیدپذیر چیست؟",
    documents: [
      "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
      "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
      "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
      "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
    ],
  };

  try {
    const response = await fetch(`${AVALAI_BASE_URL}/rerank`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const responseData = await response.json();
      const rerankedDocuments = responseData.results;
      rerankedDocuments.forEach((doc) => {
        console.log(
          `ایندکس: ${doc.index}، امتیاز ارتباط: ${doc.relevance_score}، سند: ${doc.document.text}`,
        );
      });
    } else {
      console.error(`خطا: ${response.status} - ${await response.text()}`);
    }
  } catch (error) {
    console.error("درخواست ناموفق بود:", error);
  }
}

rerankDocuments();

```

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

type RerankRequest struct {
	Model     string   `json:"model"`
	Query     string   `json:"query"`
	Documents []string `json:"documents"`
	TopN      int      `json:"top_n,omitempty"`
}

type Document struct {
	Text string `json:"text"`
}

type Result struct {
	Index          int      `json:"index"`
	RelevanceScore float64  `json:"relevance_score"`
	Document       Document `json:"document"`
}

type RerankResponse struct {
	Results []Result `json:"results"`
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("لطفا متغیر محیطی AVALAI_API_KEY را تنظیم کنید")
		return
	}

	baseURL := "https://api.avalai.ir/v1"

	reqBody := RerankRequest{
		Model: "cohere.rerank-v3-5:0",
		Query: "مزایای انرژی‌های تجدیدپذیر چیست؟",
		Documents: []string{
			"منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
			"سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
			"سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
			"پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
		},
	}

	jsonData, err := json.Marshal(reqBody)
	if err != nil {
		fmt.Printf("خطا در تبدیل درخواست: %v\n", err)
		return
	}

	req, err := http.NewRequest("POST", baseURL+"/rerank", bytes.NewBuffer(jsonData))
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}

	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("خطا در ارسال درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode != 200 {
		fmt.Printf("خطا: %d - %s\n", resp.StatusCode, string(body))
		return
	}

	var rerankResp RerankResponse
	err = json.Unmarshal(body, &rerankResp)
	if err != nil {
		fmt.Printf("خطا در تجزیه پاسخ: %v\n", err)
		return
	}

	for _, result := range rerankResp.Results {
		fmt.Printf("ایندکس: %d، امتیاز ارتباط: %.4f، سند: %s\n",
			result.Index, result.RelevanceScore, result.Document.Text)
	}
}

```

```php
<?php
// مثال PHP برای Rerank از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/rerank';

$data = [
 'model' => 'cohere.rerank-v3-5:0',
 'query' => 'مزایای انرژی‌های تجدیدپذیر چیست؟',
 'documents' => [
 'منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.',
 'سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.',
 'سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.',
 'پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.'
 ]
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey,
 'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
 echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
 echo "خطای HTTP: " . $httpcode . "\n";
 echo $response;
} else {
 $responseData = json_decode($response, true);
 if (isset($responseData['results'])) {
 foreach ($responseData['results'] as $result) {
 echo "ایندکس: " . $result['index'] .
 "، امتیاز ارتباط: " . $result['relevance_score'] .
 "، سند: " . $result['document']['text'] . "\n";
 }
 } else {
 echo "پاسخ دریافت شد:\n";
 print_r($responseData);
 }
}
?>

```


### رتبه‌بندی مجدد پیشرفته با اشیا سند و نتایج Top-N

```python
import requests
import json

API_KEY = "YOUR_AVALAI_API_KEY"
AVALAI_BASE_URL = "https://api.avalai.ir/v1"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

data = {
    "model": "cohere.rerank-v3-5:0",
    "query": "راه‌حل‌های تغییرات آب و هوایی",
    "documents": [
        {
            "id": "doc1",
            "text": "انرژی خورشیدی می‌تواند انتشار کربن را به طور قابل توجهی کاهش دهد.",
        },
        {"id": "doc2", "text": "خودروهای برقی در حال مقرون به صرفه‌تر شدن هستند."},
        {"id": "doc3", "text": "تلاش‌های جنگل‌کاری به جذب CO2 از جو کمک می‌کند."},
        {"id": "doc4", "text": "شیوه‌های کشاورزی پایدار انتشار متان را کاهش می‌دهند."},
        {
            "id": "doc5",
            "text": "ساختمان‌های بهینه انرژی می‌توانند نیازهای گرمایش و سرمایش را کاهش دهند.",
        },
    ],
    "top_n": 3,  # فقط 3 نتیجه مرتبط‌ترین را برگردان
}

response = requests.post(f"{AVALAI_BASE_URL}/rerank", headers=headers, json=data)

if response.status_code == 200:
    reranked_documents = response.json().get("results")
    print(f"{len(reranked_documents)} سند مرتبط‌ترین:")
    for doc in reranked_documents:
        print(
            f"شناسه: {doc['document'].get('id', 'N/A')}، امتیاز: {doc['relevance_score']:.4f}"
        )
        print(f"متن: {doc['document']['text']}\n")
else:
    print(f"خطا: {response.status_code} - {response.text}")
```

## فرمت پاسخ (Response Format)

```json
{
  "results": [
    {
      "index": 0,
      "relevance_score": 0.9876,
      "document": {
        "text": "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند."
      }
    },
    {
      "index": 2,
      "relevance_score": 0.8765,
      "document": {
        "text": "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود."
      }
    },
    {
      "index": 1,
      "relevance_score": 0.7654,
      "document": {
        "text": "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند."
      }
    },
    {
      "index": 3,
      "relevance_score": 0.6543,
      "document": {
        "text": "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند."
      }
    }
  ]
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر   | نوع   | توضیحات                                                                 |
| --------- | ----- | ----------------------------------------------------------------------- |
| `results` | array | آرایه‌ای از اشیا نتیجه، مرتب شده بر اساس امتیاز ارتباط به ترتیب نزولی. |

### شی نتیجه (Result Object)

| پارامتر           | نوع     | توضیحات                                                                                               |
| ----------------- | ------- | ----------------------------------------------------------------------------------------------------- |
| `index`           | integer | شاخص سند در آرایه ورودی اصلی.                                                                         |
| `relevance_score` | float   | امتیازی بین 0 و 1 که نشان‌دهنده ارتباط سند با پرس‌وجو است. مقادیر بالاتر نشان‌دهنده ارتباط بیشتر است. |
| `document`        | object  | شی سند حاوی متن و هر شناسه اصلی در صورت ارائه.                                                       |

## مدل‌های موجود

در حال حاضر، AvalAI از مدل‌های رتبه‌بندی مجدد زیر پشتیبانی می‌کند:

| ارائه دهنده | مدل | پنجره زمینه | قیمت‌گذاری | توضیحات |
| ----------- | --- | ----------- | --------- | ------- |
| Cohere | cohere-rerank-v4.0-pro | ۳۲,۷۶۸ توکن | $۰.۰۰۲۵/کوئری | مدل رتبه‌بندی با بالاترین کیفیت و پنجره زمینه ۸ برابر بزرگتر. پشتیبانی از بیش از ۱۰۰ زبان و اسناد YAML. |
| Cohere | cohere-rerank-v4.0-fast | ۳۲,۷۶۸ توکن | $۰.۰۰۲/کوئری | مدل رتبه‌بندی مقرون به صرفه برای برنامه‌های با توان عملیاتی بالا. پشتیبانی از بیش از ۱۰۰ زبان. |
| Cohere | cohere.rerank-v3-5:0 | ۴,۰۹۶ توکن | $۱.۰۰/۱K واحد | نسل قبلی مدل رتبه‌بندی مجدد. |

## موارد استفاده رایج

### بهبود سیستم‌های RAG

رتبه‌بندی مجدد به ویژه برای سیستم‌های تولید افزوده بازیابی (RAG) ارزشمند است، جایی که کیفیت اسناد بازیابی شده به طور مستقیم بر خروجی نهایی تاثیر می‌گذارد:

```python
import requests
from openai import OpenAI

# مرحله 1: بازیابی اسناد کاندید (مثال ساده شده)
candidate_documents = [
    "توافق پاریس یک معاهده بین‌المللی در مورد تغییرات آب و هوایی است.",
    "گرم شدن کره زمین باعث افزایش سطح آب دریاها در سراسر جهان می‌شود.",
    "منابع انرژی تجدیدپذیر شامل انرژی خورشیدی، بادی و برق‌آبی می‌شود.",
    "خودروهای برقی نسبت به خودروهای بنزینی آلایندگی کمتری تولید می‌کنند.",
    "فناوری‌های جذب کربن می‌توانند به کاهش انتشار گازهای گلخانه‌ای کمک کنند.",
]

# مرحله 2: رتبه‌بندی مجدد اسناد بر اساس پرس‌وجو
query = "چگونه می‌توانیم انتشار کربن را کاهش دهیم؟"
rerank_data = {
    "model": "cohere.rerank-v3-5:0",
    "query": query,
    "documents": candidate_documents,
}

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json=rerank_data,
)

# مرحله 3: استخراج مرتبط‌ترین اسناد
reranked_docs = []
if response.status_code == 200:
    results = response.json().get("results")
    reranked_docs = [
        result["document"]["text"] for result in results[:2]
    ]  # 2 مورد مرتبط‌ترین

# مرحله 4: استفاده از اسناد رتبه‌بندی شده در پرامپت مدل زبانی
client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

context = "\n".join(reranked_docs)
prompt = f"بر اساس اطلاعات زیر:\n\n{context}\n\nبه این سؤال پاسخ دهید: {query}"

completion = client.chat.completions.create(
    model="gpt-5.6-luna", messages=[{"role": "user", "content": prompt}]
)

print(completion.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `cohere.rerank-v3-5:0` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Summarize the uploaded file."},
                {"type": "input_file", "file_id": "file_abc123"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### بهبود نتایج جستجو

رتبه‌بندی مجدد می‌تواند با در نظر گرفتن معنای معنایی فراتر از تطبیق کلیدواژه، ارتباط جستجو را به طور قابل توجهی بهبود بخشد:

```python
# تابع جستجوی ساده که اسنادی را که حاوی هر یک از عبارات پرس‌وجو هستند برمی‌گرداند
def keyword_search(query, documents):
    query_terms = query.lower().split()
    results = []
    for doc in documents:
        if any(term in doc.lower() for term in query_terms):
            results.append(doc)
    return results


# مجموعه اسناد
documents = [
    "الگوریتم‌های یادگیری ماشین به مجموعه داده‌های بزرگ برای آموزش نیاز دارند.",
    "شبکه‌های عصبی زیرمجموعه‌ای از مدل‌های یادگیری ماشین هستند.",
    "یادگیری عمیق وظایف بینایی کامپیوتری را متحول کرده است.",
    "پیش‌پردازش داده‌ها یک مرحله مهم در هر جریان کاری (RAG) یادگیری ماشین است.",
    "یادگیری انتقالی به مدل‌ها اجازه می‌دهد از دانش شبکه‌های از پیش آموزش‌دیده استفاده کنند.",
    "یادگیری نظارت‌شده از داده‌های برچسب‌گذاری شده برای آموزش مدل‌های پیش‌بینی استفاده می‌کند.",
    "یادگیری بدون نظارت الگوهایی را در داده‌های بدون برچسب پیدا می‌کند.",
    "یادگیری تقویتی عامل‌ها را از طریق مکانیسم‌های پاداش آموزش می‌دهد.",
]

# پرس‌وجوی کاربر
query = "شبکه‌های عصبی چگونه از داده‌ها یاد می‌گیرند؟"

# مرحله 1: دریافت نتایج اولیه با تطبیق ساده کلیدواژه
initial_results = keyword_search(query, documents)
print("نتایج جستجوی کلیدواژه اولیه:")
for i, doc in enumerate(initial_results):
    print(f"{i+1}. {doc}")

# مرحله 2: رتبه‌بندی مجدد نتایج برای بهبود ارتباط
rerank_data = {
    "model": "cohere.rerank-v3-5:0",
    "query": query,
    "documents": initial_results,
}

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"},
    json=rerank_data,
)

# مرحله 3: نمایش نتایج رتبه‌بندی شده
print("\nنتایج رتبه‌بندی شده:")
if response.status_code == 200:
    results = response.json().get("results")
    for i, result in enumerate(results):
        print(f"{i+1}. [{result['relevance_score']:.4f}] {result['document']['text']}")
```

## مدیریت خطا (Error Handling)

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات                                                        |
| -------- | -------------------------------------------------------------- |
| 400      | درخواست بد - درخواست شما نامعتبر است.                          |
| 401      | غیرمجاز - کلید API شما اشتباه است.                             |
| 403      | ممنوع - شما اجازه دسترسی به این منبع را ندارید.                |
| 404      | یافت نشد - منبع مشخص شده یافت نشد.                             |
| 429      | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید. |
| 500      | خطای داخلی سرور - مشکلی در سرور ما وجود داشت.                  |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## منابع مرتبط

- [مدل‌های Cohere](fa/providers/cohere.md) - درباره مدل‌های Cohere موجود بیاموزید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md) - درباره بهینه‌سازی سیستم‌های RAG بیاموزید
