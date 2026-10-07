# مرجع API بردارهای تعبیه‌سازی (Embeddings)

API بردارهای تعبیه‌سازی به شما امکان می‌دهد متن را به نمایش‌های برداری تبدیل کنید که می‌توانند برای جستجوی معنایی، خوشه‌بندی، طبقه‌بندی و سایر وظایف یادگیری ماشین استفاده شوند.

Embeddingها نزدیکی معنایی را حفظ می‌کنند: متن‌هایی با معنی مشابه بردارهایی نزدیک‌تر می‌گیرند و متن‌های نامرتبط از هم دورتر می‌شوند. از آن‌ها برای retrieval، پیشنهاددهی، تشخیص تکراری‌ها، تشخیص ناهنجاری، خوشه‌بندی و طبقه‌بندی سبک روی داده‌های خودتان استفاده کنید.

## گردش‌کار Embedding

1. **برای هر index یک مدل و اندازه ابعاد ثابت انتخاب کنید.** بردارهای query و سند باید با همان مدل و همان تعداد بعد ساخته شوند.
2. **متن ورودی را قبل از embedding نرمال و chunk کنید.** برای هر chunk شناسه پایدار نگه دارید تا سندهای بدون تغییر دوباره embed نشوند.
3. **بردارها را همراه metadata ذخیره کنید**؛ مثل URL منبع، شناسه سند، مجوزها، زبان و زمان آخرین به‌روزرسانی.
4. **با cosine similarity یا dot product جستجو کنید**؛ بسته به vector store خودتان. metric زمان index و query را یکسان نگه دارید.
5. **snippetهای بازیابی‌شده را به `/v1/responses` یا `/v1/chat/completions` بدهید** و از مدل نخواهید از حافظه حدس بزند. برای یک workflow کامل، [RAG دستی با Embeddings](/fa/examples/manual_rag_with_embeddings.md) را ببینید.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/embeddings
```

## بدنه درخواست (Request Body)

| پارامتر           | نوع             | الزامی | توضیحات                                                                                                     |
| ----------------- | --------------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| `model`           | string          | بله    | شناسه مدلی که باید استفاده شود. برای مدل‌های تعبیه‌سازی موجود به [مدل‌ها](fa/models/model-details.md) مراجعه کنید.      |
| `input`           | string or array | بله    | متنی که باید تعبیه‌سازی شود. می‌تواند یک رشته یا آرایه‌ای از رشته‌ها باشد.                                      |
| `encoding_format` | string          | خیر    | فرمتی که بردارهای تعبیه‌سازی باید در آن برگردانده شوند. می‌تواند "float" یا "base64" باشد. پیش‌فرض "float" است. |
| `dimensions`      | integer         | خیر    | تعداد ابعادی که بردارهای تعبیه‌سازی خروجی باید داشته باشند. فقط در برخی مدل‌ها پشتیبانی می‌شود.                 |
| `user`            | string          | خیر    | یک شناسه منحصر به فرد که نماینده کاربر نهایی شما است و می‌تواند به نظارت و شناسایی سو استفاده کمک کند.     |

### نکته‌های درخواست

- برای embedding چند متن مستقل در یک درخواست، آرایه‌ای از رشته‌ها را در `input` بفرستید. این قابلیت در خود Embeddings API پشتیبانی می‌شود و با Batch API میزبانی‌شده AvalAI فرق دارد.
- هزینه embedding را بر اساس ورودی‌ای که می‌فرستید برنامه‌ریزی کنید. پاسخ مدل‌های متنی سازگار با OpenAI مقدارهای `usage.prompt_tokens` و `usage.total_tokens` را برمی‌گرداند؛ قیمت‌گذاری AvalAI و routeهای provider-specific می‌توانند متفاوت باشند، پس پیش از backfill بزرگ [قیمت‌گذاری](/fa/pricing.md) را بررسی کنید.
- وقتی مدل انتخابی از بردار کوتاه‌تر پشتیبانی می‌کند، از `dimensions` استفاده کنید. بردار کوچک‌تر هزینه ذخیره‌سازی، حافظه و جستجو را کم می‌کند، اما ممکن است کیفیت retrieval را کاهش دهد.
- برای بیشتر vector databaseها و محاسبه similarity از `encoding_format: "float"` استفاده کنید. `base64` را فقط وقتی انتخاب کنید که pipeline شما مشخصا از انتقال فشرده سود می‌برد.
- قبل از embedding ورودی‌های خیلی بزرگ، تعداد توکن را بشمارید یا تخمین بزنید؛ [شمارش توکن](/fa/guides/token-counting.md) و context window مدل انتخابی را ببینید. برای مدل‌های OpenAI `text-embedding-3-*` از tokenizer نوع `cl100k_base` استفاده کنید.
- رشته خالی نفرستید. API مرجع OpenAI برای درخواست‌های embedding محدودیت‌های per-input و aggregate request را مستند می‌کند؛ در AvalAI این محدودیت‌ها می‌توانند بر اساس مدل، route provider و سطح حساب متفاوت باشند، پس ingestهای بزرگ را به batchهای محدود تقسیم کنید و chunkهای ناموفق را ایمن retry کنید.

## مثال‌ها

### تولید تعبیه‌سازی پایه

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "text-embedding-3-small",
  "input": "The food was delicious and the service was excellent."
}'

```

```python
# مثال پایتون (Python)
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input="The food was delicious and the service was excellent.",
)

embeddings = response.data[0].embedding
print(f"Length of embedding vector: {len(embeddings)}")
print(f"First few values: {embeddings[:5]}")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.embeddings.create({
  model: "text-embedding-3-small",
  input: "The food was delicious and the service was excellent."
});

const embeddings = response.data[0].embedding;
console.log(`Length of embedding vector: ${embeddings.length}`);
console.log(`First few values: ${embeddings.slice(0, 5)}`);

```

```go
// مثال گو (Go)
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateEmbeddings(
		context.Background(),
		openai.EmbeddingRequest{
			Model: openai.TextEmbeddingSmall,
			Input: []string{"The food was delicious and the service was excellent."},
		},
	)

	if err != nil {
		fmt.Printf("Embedding error: %v\n", err)
		return
	}

	embeddings := resp.Data[0].Embedding
	fmt.Printf("Length of embedding vector: %d\n", len(embeddings))
	fmt.Printf("First few values: %v\n", embeddings[:5])
}

```

```php
<?php
// مثال PHP برای Embeddings از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/embeddings';

$data = [
'model' => 'text-embedding-3-small',
'input' => 'The food was delicious and the service was excellent.' // متن ورودی به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
// در صورت نیاز پارامترهای دیگری مانند encoding_format، dimensions و غیره را اضافه کنید
// 'encoding_format' => 'float',
// 'dimensions' => 1024
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
  if (isset($responseData['data'][0]['embedding'])) {
    $embedding = $responseData['data'][0]['embedding'];
    echo "طول بردار تعبیه‌سازی: " . count($embedding) . "\n";
    echo "چند مقدار اول: [" . implode(', ', array_slice($embedding, 0, 5)) . "]\n";
  } else {
    echo "پاسخ دریافت شد:\n";
    print_r($responseData);
  }
}
?>

```


### چند ورودی در یک درخواست

Embeddings API از batching ورودی با ارسال آرایه‌ای از رشته‌ها در `input` پشتیبانی می‌کند. API میزبانی‌شده `/v1/batches` در AvalAI یک قابلیت جداگانه برای پردازش آفلاین است؛ وقتی یک پاسخ فوری شامل embedding چند متن می‌خواهید، از همین فرم آرایه‌ای استفاده کنید.

می‌توانید چندین متن را در یک درخواست واحد تعبیه‌سازی کنید:

```python
response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[
        "The food was delicious and the service was excellent.",
        "The restaurant was very expensive and the food was mediocre.",
        "I highly recommend this restaurant for its amazing atmosphere.",
    ],
)

# Process each embedding
for i, embedding in enumerate(response.data):
    print(f"Embedding {i}, length: {len(embedding.embedding)}")
```

### ابعاد سفارشی

وقتی مدل انتخابی از `dimensions` پشتیبانی می‌کند، اندازه هدف را هنگام ساخت embedding تعیین کنید تا همه بردارهای index شکل یکسان داشته باشند:

```python
response = client.embeddings.create(
    model="text-embedding-3-large",
    input="مستندات routing مدل در AvalAI را خلاصه کن.",
    dimensions=1024,
    encoding_format="float",
)

vector = response.data[0].embedding
print(len(vector))

```

```javascript
const response = await client.embeddings.create({
  model: "text-embedding-3-large",
  input: "مستندات routing مدل در AvalAI را خلاصه کن.",
  dimensions: 1024,
  encoding_format: "float",
});

const vector = response.data[0].embedding;
console.log(vector.length);

```

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "text-embedding-3-large",
    "input": "مستندات routing مدل در AvalAI را خلاصه کن.",
    "dimensions": 1024,
    "encoding_format": "float"
  }'

```


اگر ناچارید بردارها را بعد از تولید کوتاه کنید، قبل از مقایسه آن‌ها را نرمال کنید. روش پیشنهادی استفاده از پارامتر API است، چون ابعاد تولید، ذخیره‌سازی و search را صریح نگه می‌دارد.

## فرمت پاسخ (Response Format)

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "embedding": [
        0.0023064255,
        -0.009327292,
        -0.0028842222,
        ...
      ],
      "index": 0
    }
  ],
  "model": "text-embedding-3-small",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  }
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر  | نوع    | توضیحات                                       |
| -------- | ------ | --------------------------------------------- |
| `object` | string | نوع شی، که همیشه "list" است.                 |
| `data`   | array  | آرایه‌ای از اشیا تعبیه‌سازی.                     |
| `model`  | string | مدلی که برای تولید تعبیه‌سازی استفاده شده است. |
| `usage`  | object | یک شی حاوی اطلاعات استفاده از توکن.          |

### شی تعبیه‌سازی (Embedding Object)

| پارامتر     | نوع     | توضیحات                                                                                     |
| ----------- | ------- | ------------------------------------------------------------------------------------------- |
| `object`    | string  | نوع شی، که همیشه "embedding" است.                                                          |
| `embedding` | array   | بردار تعبیه‌سازی که آرایه‌ای از اعداد اعشاری است. طول این آرایه به مدل استفاده شده بستگی دارد. |
| `index`     | integer | شاخص تعبیه‌سازی در آرایه ورودی.                                                                 |

### شی استفاده (Usage Object)

| پارامتر         | نوع     | توضیحات                                                                    |
| --------------- | ------- | -------------------------------------------------------------------------- |
| `prompt_tokens` | integer | تعداد توکن‌های استفاده شده در ورودی.                                       |
| `total_tokens`  | integer | تعداد کل توکن‌های استفاده شده (برای تعبیه‌سازی‌ها برابر با prompt_tokens است). |

## پرسش‌های متداول

### چطور K نزدیک‌ترین بردار را سریع بازیابی کنیم؟

وقتی داده از یک مجموعه کوچک در حافظه بزرگ‌تر می‌شود، از vector database یا سرویس search استفاده کنید. هر بردار را همراه source ID، metadata مربوط به tenant و permission، زبان، زمان و نوع سند ذخیره کنید تا پیش از similarity search فیلتر deterministic داشته باشید.

### کدام تابع فاصله مناسب‌تر است؟

Cosine similarity یک پیش‌فرض امن است. embeddingهای متنی OpenAI به طول ۱ نرمال شده‌اند؛ بنابراین cosine similarity و Euclidean distance معمولا رتبه‌بندی یکسانی می‌دهند و برای این بردارهای نرمال‌شده می‌توانید از dot product به‌عنوان مسیر سریع‌ترِ معادل cosine استفاده کنید.

### آیا embeddingها از رویدادهای جدید خبر دارند؟

Embedding را به‌عنوان پایگاه دانش factual استفاده نکنید. مدل‌های `text-embedding-3-large` و `text-embedding-3-small` برای دانستن رویدادهای جدید طراحی نشده‌اند؛ سندهای عمومی یا خصوصی فعلی خودتان را embed کنید و هنگام پاسخ‌گویی بازیابی کنید.

### آیا می‌توان embeddingها را ذخیره یا share کرد؟

Embeddingها را داده مشتق‌شده از کاربر بدانید. متن خوانا نیستند، اما می‌توانند الگوهای similarity یا عضویت در corpus را آشکار کنند؛ پس همان سیاست retention، deletion، access control و tenant isolation سندهای منبع را روی آن‌ها هم اعمال کنید.

## مدل‌های موجود

AvalAI در حال حاضر این شناسه‌های مدل با mode برابر `embedding` را ارائه می‌کند. برای آخرین محدودیت‌ها و هزینه‌ها، [جزئیات مدل‌ها](/fa/models/model-details.md)، [قیمت‌گذاری](/fa/pricing.md) و صفحه‌های rate limit را ببینید.

| ارائه‌دهنده | مدل | اندازه بردار / پنجره ورودی | نکته |
| ----------- | ---- | --------------------------- | ---- |
| OpenAI | `text-embedding-3-large` | 3072 بعد؛ 8191 توکن ورودی | embedding متنی OpenAI با ابعاد بالاتر؛ از بردار کوتاه‌تر با `dimensions` پشتیبانی می‌کند. |
| OpenAI | `text-embedding-3-small` | 1536 بعد؛ 8191 توکن ورودی | embedding متنی بهینه OpenAI برای search، clustering، classification و recommendation. |
| OpenAI | `text-embedding-ada-002` | 1536 بعد؛ 8191 توکن ورودی | مدل legacy سازگار با OpenAI برای indexهای موجود. |
| Google | `gemini-embedding-2` | تا 3072 بعد؛ 8192 توکن ورودی | embedding چندوجهی Gemini برای workflowهای متن، تصویر، صدا، ویدیو و PDF در routeهای پشتیبانی‌شده. |
| Google | `gemini-embedding-001` | تا 3072 بعد؛ 2048 توکن ورودی | مدل embedding Gemini با کنترل‌های task-specific از طریق پارامترهای provider-specific. |
| Cohere | `embed-v-4-0` | تا 3072 بعد؛ 128k توکن ورودی | Cohere Embed v4 از طریق Azure AI؛ از ورودی متن و تصویر روی `/v1/embeddings` پشتیبانی می‌کند. |
| Cohere | `cohere.embed-v4:0` | تا 1536 بعد؛ 128k توکن ورودی | Cohere Embed v4 از طریق AWS Bedrock برای workflowهای retrieval چندوجهی. |
| Cohere | `cohere.embed-multilingual-v3` | 1024 بعد؛ پنجره ورودی provider | embedding چندزبانه Cohere برای جستجو و طبقه‌بندی بین‌زبانی. |
| Alibaba | `text-embedding-v4` | 2048 بعد؛ 1024 توکن ورودی | جدیدترین embedding متنی Qwen برای semantic search و RAG. |
| Alibaba | `text-embedding-v3` | 1024 بعد؛ 1024 توکن ورودی | embedding متنی چندزبانه Qwen برای indexهای متنی موجود. |
| Alibaba | `tongyi-embedding-vision-plus` | 1152 بعد؛ 1024 توکن ورودی | embedding چندوجهی برای retrieval بین متن، تصویر و ویدیو. |
| Alibaba | `tongyi-embedding-vision-flash` | 768 بعد؛ 1024 توکن ورودی | embedding چندوجهی سریع‌تر برای search بین‌وجهی کم‌تاخیرتر. |
| Cloudflare | `cf.plamo-embedding-1b` | اندازه بردار provider؛ 4096 توکن ورودی | مدل embedding PLaMo از مسیر Cloudflare. |
| Cloudflare | `cf.embeddinggemma-300m` | اندازه بردار provider؛ 2048 توکن ورودی | مدل embedding فشرده مبتنی بر Gemma برای search سبک. |
| Nvidia NIM | `nvidia_nim.nv-embedqa-e5-v5` | اندازه بردار provider | مدل embedding میزبانی‌شده در NIM برای retrieval پرسش‌وپاسخ. |
| Nvidia NIM | `nvidia_nim.nv-embed-v1` | اندازه بردار provider | مدل embedding عمومی میزبانی‌شده در NIM. |
| BAAI از طریق Nvidia NIM | `nvidia_nim.bge-m3` | اندازه بردار provider | مدل embedding چندزبانه BGE از مسیر Nvidia NIM. |

## شباهت و فاصله

برای retrieval، query را با همان مدل و همان تعداد بعدی embed کنید که برای سندهای ذخیره‌شده استفاده کرده‌اید، سپس سندها را بر اساس شباهت برداری رتبه‌بندی کنید. cosine similarity یک پیش‌فرض خوب است؛ embeddingهای OpenAI به طول ۱ نرمال شده‌اند، بنابراین برای آن مدل‌ها dot product و cosine similarity معمولا رتبه‌بندی یکسانی می‌دهند. اگر بعد از تولید، بردارها را دستی کوتاه می‌کنید، پیش از ذخیره یا مقایسه آن‌ها را نرمال کنید.

Embeddingهای providerها یا ابعاد مختلف را در یک index مخلوط نکنید مگر اینکه vector store و مجموعه ارزیابی شما کیفیت رتبه‌بندی را تأیید کند. برای workflowهای retrieval مهم، یک eval کوچک با جواب‌های برچسب‌خورده نگه دارید تا تغییر مدل، chunking و dimensions را ایمن مقایسه کنید.

بردارهای ذخیره‌شده داده مشتق‌شده هستند. همان سیاست tenant isolation، retention، deletion و access control سندهای منبع را برای بردارها و metadata مربوط به آن‌ها هم اعمال کنید.

## موارد استفاده رایج

### جستجوی معنایی (Semantic Search)

از بردارهای تعبیه‌سازی می‌توان برای یافتن اسناد مشابه از نظر معنایی استفاده کرد:

```python
import os
import numpy as np
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


# Function to compute cosine similarity
def cosine_similarity(a, b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))


# Create embeddings for a query and documents
query = "delicious pasta"
documents = [
    "The restaurant serves amazing Italian food.",
    "The new smartphone has excellent battery life.",
    "Their pasta dishes are incredibly tasty and authentic.",
]

# Get query embedding
query_response = client.embeddings.create(model="text-embedding-3-small", input=query)
query_embedding = query_response.data[0].embedding

# Get document embeddings
doc_response = client.embeddings.create(model="text-embedding-3-small", input=documents)
doc_embeddings = [item.embedding for item in doc_response.data]

# Compute similarities
similarities = [
    cosine_similarity(query_embedding, doc_embedding)
    for doc_embedding in doc_embeddings
]

# Print results
for i, similarity in enumerate(similarities):
    print(f"Document {i}: Similarity = {similarity:.4f}")
    print(f"Text: {documents[i]}")
```

### طبقه‌بندی متن (Text Classification)

از بردارهای تعبیه‌سازی می‌توان با مدل‌های یادگیری ماشین سنتی برای طبقه‌بندی استفاده کرد:

```python
import os
from sklearn.linear_model import LogisticRegression
import numpy as np
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# Sample training data
texts = [
    "I love this product, it's amazing!",
    "This is the best purchase I've ever made.",
    "I'm very disappointed with the quality.",
    "This product is terrible, don't buy it.",
]
labels = [1, 1, 0, 0]  # 1 for positive, 0 for negative

# Get embeddings for training data
response = client.embeddings.create(model="text-embedding-3-small", input=texts)
embeddings = [item.embedding for item in response.data]

# Train a classifier
classifier = LogisticRegression()
classifier.fit(embeddings, labels)

# Classify new text
new_texts = ["I really enjoy using this.", "This doesn't work as advertised."]
new_response = client.embeddings.create(model="text-embedding-3-small", input=new_texts)
new_embeddings = [item.embedding for item in new_response.data]

# Predict
predictions = classifier.predict(new_embeddings)
for text, prediction in zip(new_texts, predictions):
    sentiment = "positive" if prediction == 1 else "negative"
    print(f"Text: '{text}' - Predicted sentiment: {sentiment}")
```

## تعبیه‌سازی‌ گوگل Gemini

مدل‌های تعبیه‌سازی Gemini گوگل ویژگی‌های پیشرفته‌ای از جمله بهینه‌سازی خاص وظیفه، کنترل انعطاف‌پذیر ابعاد و عملکرد برتر برای وظایف مختلف NLP ارائه می‌دهند. AvalAI از تعبیه‌سازی‌ Gemini از طریق رویکردهای سازگار با OpenAI و SDK بومی Google GenAI پشتیبانی می‌کند.

### استفاده از تعبیه‌سازی‌ Gemini با طرحواره OpenAI

می‌توانید از تعبیه‌سازی‌ Gemini از طریق نقطه پایانی استاندارد `v1/embeddings` با پارامترهای اضافی در `extra_body` برای ویژگی‌های پیشرفته استفاده کنید:

#### تعبیه‌سازی پایه Gemini

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# تعبیه‌سازی پایه Gemini
response = client.embeddings.create(
    model="gemini-embedding-001",
    input="روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد",
)

embedding = response.data[0].embedding
print(f"ابعاد تعبیه‌سازی: {len(embedding)}")
print(f"چند مقدار اول: {embedding[:5]}")

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تعبیه‌سازی پایه Gemini
const response = await client.embeddings.create({
    model: "gemini-embedding-001",
    input: "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد",
});

const embedding = response.data[0].embedding;
console.log(`ابعاد تعبیه‌سازی: ${embedding.length}`);
console.log(`چند مقدار اول: ${embedding.slice(0, 5)}`);

```

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-001",
    "input": "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد"
  }'

```


#### ویژگی‌های پیشرفته با انواع وظایف

تعبیه‌سازی‌ Gemini از بهینه‌سازی خاص وظیفه و ابعاد سفارشی پشتیبانی می‌کنند:

```python
# تعبیه‌سازی پیشرفته Gemini با نوع وظیفه و ابعاد سفارشی
response = client.embeddings.create(
    model="gemini-embedding-001",
    input=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    extra_body={"task_type": "SEMANTIC_SIMILARITY", "output_dimensionality": 768},
)

# محاسبه شباهت کسینوسی بین تعبیه‌سازی‌‌ها
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings = [item.embedding for item in response.data]
embeddings_matrix = np.array(embeddings)
similarity_matrix = cosine_similarity(embeddings_matrix)

print(f"شباهت بین دو متن اول: {similarity_matrix[0, 1]:.4f}")
print(f"شباهت بین متن اول و سوم: {similarity_matrix[0, 2]:.4f}")

# نرمال‌سازی تعبیه‌سازی‌‌ها برای ابعاد < 3072 (توصیه می‌شود)
if len(embeddings[0]) < 3072:
    normalized_embeddings = []
    for embedding in embeddings:
        embedding_array = np.array(embedding)
        normalized = embedding_array / np.linalg.norm(embedding_array)
        normalized_embeddings.append(normalized)
    print("تعبیه‌سازی‌‌ها برای عملکرد بهینه نرمال‌سازی شدند")

```

```javascript
// تعبیه‌سازی پیشرفته Gemini با نوع وظیفه و ابعاد سفارشی
const response = await client.embeddings.create({
    model: "gemini-embedding-001",
    input: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟",
        "چگونه کیک درست کنم؟"
    ],
    // @ts-expect-error extra_body is a provider-specific parameter
    extra_body: {
        task_type: "SEMANTIC_SIMILARITY",
        output_dimensionality: 768
    }
});

const embeddings = response.data.map(item => item.embedding);
console.log(`${embeddings.length} تعبیه‌سازی با ${embeddings[0].length} بعد تولید شد`);

// محاسبه شباهت ساده ضرب داخلی (برای تعبیه‌سازی‌ نرمال‌شده)
function dotProduct(a, b) {
    return a.reduce((sum, val, i) => sum + val * b[i], 0);
}

const similarity = dotProduct(embeddings[0], embeddings[1]);
console.log(`شباهت بین دو متن اول: ${similarity.toFixed(4)}`);

```

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-001",
    "input": ["معنای زندگی چیست؟", "هدف وجود چیست؟"],
    "extra_body": {
      "task_type": "SEMANTIC_SIMILARITY",
      "output_dimensionality": 768
    }
  }'

```


#### انواع وظایف پشتیبانی‌شده

| نوع وظیفه | توضیحات | بهترین برای |
|-----------|-------------|----------|
| `SEMANTIC_SIMILARITY` | بهینه‌سازی شده برای اندازه‌گیری شباهت متن | سیستم‌های توصیه، تشخیص تکراری |
| `CLASSIFICATION` | بهینه‌سازی شده برای وظایف طبقه‌بندی متن | تحلیل احساسات، تشخیص اسپم |
| `CLUSTERING` | بهینه‌سازی شده برای گروه‌بندی متن‌های مشابه | سازماندهی اسناد، تحقیقات بازار |
| `RETRIEVAL_DOCUMENT` | بهینه‌سازی شده برای نمایه‌سازی اسناد | سیستم‌های RAG، موتورهای جستجو |
| `RETRIEVAL_QUERY` | بهینه‌سازی شده برای پرس‌وجوهای جستجو | برنامه‌های جستجوی سفارشی |
| `CODE_RETRIEVAL_QUERY` | بهینه‌سازی شده برای پرس‌وجوهای جستجوی کد | جستجوی کد، جستجوی مستندات |
| `QUESTION_ANSWERING` | بهینه‌سازی شده برای سیستم‌های پرسش و پاسخ | چت‌بات‌ها، سیستم‌های FAQ |
| `FACT_VERIFICATION` | بهینه‌سازی شده برای بررسی حقایق | سیستم‌های تایید خودکار |

### استفاده از API بومی Gemini

همچنین می‌توانید از تعبیه‌سازی‌ Gemini از طریق نقطه پایانی SDK بومی Google GenAI برای دسترسی کامل به ویژگی‌های خاص Gemini استفاده کنید:

```python
import os
from google import genai

client = genai.Client(
    api_key=os.environ["AVALAI_API_KEY"],
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# تعبیه‌سازی پایه با API بومی
result = client.models.embed_content(
    model="gemini-embedding-001", contents="معنای زندگی چیست؟"
)

embedding = result.embeddings[0]
print(f"ابعاد تعبیه‌سازی: {len(embedding.values)}")
print(f"چند مقدار اول: {embedding.values[:5]}")

# استفاده پیشرفته با نوع وظیفه و ابعاد سفارشی
from google.genai import types

result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY", output_dimensionality=768
    ),
)

# محاسبه شباهت‌ها با استفاده از تعبیه‌سازی‌‌ها
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings_matrix = np.array([emb.values for emb in result.embeddings])
similarity_matrix = cosine_similarity(embeddings_matrix)

print(f"شباهت بین 'معنای زندگی' و 'هدف وجود': {similarity_matrix[0, 1]:.4f}")
print(f"شباهت بین 'معنای زندگی' و 'درست کردن کیک': {similarity_matrix[0, 2]:.4f}")

```

```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

// تعبیه‌سازی پایه با API بومی
const response = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: "معنای زندگی چیست؟"
});

const embedding = response.embeddings[0];
console.log(`ابعاد تعبیه‌سازی: ${embedding.values.length}`);
console.log(`چند مقدار اول: ${embedding.values.slice(0, 5)}`);

// استفاده پیشرفته با نوع وظیفه و ابعاد سفارشی
const advancedResponse = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟",
        "چگونه کیک درست کنم؟"
    ],
    taskType: "SEMANTIC_SIMILARITY",
    outputDimensionality: 768
});

console.log(`${advancedResponse.embeddings.length} تعبیه‌سازی تولید شد`);

```

```bash
# تعبیه‌سازی پایه با API بومی
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {"parts": [{"text": "معنای زندگی چیست؟"}]}
    ]
  }'

# استفاده پیشرفته با نوع وظیفه و ابعاد سفارشی
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-001:embedContent" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "contents": [
      {"parts": [{"text": "معنای زندگی چیست؟"}]},
      {"parts": [{"text": "هدف وجود چیست؟"}]}
    ],
    "embedding_config": {
      "task_type": "SEMANTIC_SIMILARITY",
      "output_dimensionality": 768
    }
  }'

```


### فرمت پاسخ تعبیه‌سازی Gemini (API بومی)

هنگام استفاده از API بومی Gemini، فرمت پاسخ با طرحواره OpenAI متفاوت است:

```json
{
  "embeddings": [
    {
      "values": [
        0.0023064255,
        -0.009327292,
        -0.0028842222,
        ...
      ]
    }
  ]
}
```

### کنترل ابعاد خروجی

تعبیه‌سازی‌ Gemini از یادگیری نمایش ماتریوشکا (MRL) پشتیبانی می‌کنند که امکان استفاده از ابعاد کوچک‌تر بدون از دست دادن کیفیت قابل توجه را فراهم می‌کند:

- **۳۰۷۲ بعد**: ظرفیت کامل مدل (پیش‌فرض، از قبل نرمال‌سازی شده)
- **۱۵۳۶ بعد**: عملکرد متعادل و کارایی
- **۷۶۸ بعد**: کارآمد با عملکرد خوب
- **۵۱۲ بعد**: فشرده با عملکرد قابل قبول
- **۲۵۶ بعد**: بسیار فشرده
- **۱۲۸ بعد**: حداقل اندازه

> **مهم**: برای ابعاد غیر از ۳۰۷۲، باید تعبیه‌سازی‌‌ها را برای عملکرد بهینه شباهت معنایی نرمال‌سازی کنید:

```python
import numpy as np


# نرمال‌سازی تعبیه‌سازی‌‌ها برای ابعاد < ۳۰۷۲
def normalize_embedding(embedding):
    embedding_array = np.array(embedding)
    return embedding_array / np.linalg.norm(embedding_array)


# مثال استفاده
if len(embedding) < 3072:
    normalized_embedding = normalize_embedding(embedding)
```

### مثال سیستم RAG با تعبیه‌سازی‌ Gemini

در اینجا مثال کاملی از استفاده از تعبیه‌سازی‌ Gemini برای سیستم تولید تقویت‌شده بازیابی (RAG) آورده شده است:

```python
import os
import numpy as np
from openai import OpenAI
from sklearn.metrics.pairwise import cosine_similarity

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# پایگاه دانش نمونه
documents = [
    "پاریس پایتخت فرانسه است و به خاطر برج ایفل مشهور است.",
    "توکیو پایتخت ژاپن است و به خاطر فناوری و فرهنگش معروف است.",
    "لندن پایتخت انگلستان است و خانه بیگ بن می‌باشد.",
    "برلین پایتخت آلمان است و به خاطر تاریخ غنی‌اش شناخته می‌شود.",
    "رم پایتخت ایتالیا است و به خاطر کولوسئوم مشهور است.",
]

# ایجاد تعبیه‌سازی برای پایگاه دانش با استفاده از نوع وظیفه RETRIEVAL_DOCUMENT
doc_response = client.embeddings.create(
    model="gemini-embedding-001",
    input=documents,
    extra_body={"task_type": "RETRIEVAL_DOCUMENT", "output_dimensionality": 768},
)

doc_embeddings = np.array([item.embedding for item in doc_response.data])

# نرمال‌سازی تعبیه‌سازی‌‌ها برای محاسبه شباهت بهینه
doc_embeddings = doc_embeddings / np.linalg.norm(doc_embeddings, axis=1, keepdims=True)


def search_knowledge_base(query, top_k=2):
    # ایجاد تعبیه‌سازی پرس‌وجو با استفاده از نوع وظیفه RETRIEVAL_QUERY
    query_response = client.embeddings.create(
        model="gemini-embedding-001",
        input=query,
        extra_body={"task_type": "RETRIEVAL_QUERY", "output_dimensionality": 768},
    )

    query_embedding = np.array(query_response.data[0].embedding)
    query_embedding = query_embedding / np.linalg.norm(query_embedding)

    # محاسبه شباهت‌ها
    similarities = cosine_similarity([query_embedding], doc_embeddings)[0]

    # دریافت top-k اسناد مشابه
    top_indices = np.argsort(similarities)[-top_k:][::-1]

    results = []
    for idx in top_indices:
        results.append({"document": documents[idx], "similarity": similarities[idx]})

    return results


# مثال استفاده
query = "پایتخت فرانسه کجاست؟"
results = search_knowledge_base(query)

print(f"پرس‌وجو: {query}")
for i, result in enumerate(results):
    print(f"{i+1}. {result['document']} (شباهت: {result['similarity']:.4f})")
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

- [مدل‌ها](fa/models/model-details.md) - درباره مدل‌های تعبیه‌سازی موجود بیاموزید
- [RAG دستی با Embeddings](fa/examples/manual_rag_with_embeddings.md) - الگوی retrieval اقتباس‌شده از Cookbook با embeddings در AvalAI
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md) - راهنمای طراحی برای گردش‌کارهای retrieval
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
