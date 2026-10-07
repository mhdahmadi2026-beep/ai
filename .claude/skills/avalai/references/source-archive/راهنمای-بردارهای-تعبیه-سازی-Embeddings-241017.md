# راهنمای بردارهای تعبیه‌سازی (Embeddings)

Embeddingها متن را به بردار تبدیل می‌کنند تا برنامه شما معنی متن‌ها را مقایسه کند، نه فقط کلمه‌های مشترک را. از آن‌ها برای جستجوی معنایی، RAG، پیشنهاددهی، خوشه‌بندی، تشخیص تکراری‌ها، طبقه‌بندی و تشخیص ناهنجاری استفاده کنید.

> این راهنما با اقتباس از مستندات رسمی OpenAI درباره [Vector embeddings](https://developers.openai.com/api/docs/guides/embeddings)، با تغییرات endpoint، کلید API، availability مدل‌ها و راهنمای retrieval در AvalAI تهیه شده است.

## چه زمانی از Embedding استفاده کنیم؟

وقتی می‌خواهید قبل از فراخوانی مدل مولد، روی داده‌های خودتان lookup سریع انجام دهید از embedding استفاده کنید. یک جریان رایج در AvalAI:

1. سندها را به chunkهای پایدار تقسیم کنید.
2. هر chunk را با `/v1/embeddings` embed کنید.
3. بردارها را همراه metadata مثل `document_id`، URL منبع، مجوزها، زبان و زمان به‌روزرسانی ذخیره کنید.
4. query کاربر را با همان مدل و همان تعداد بعد embed کنید.
5. نزدیک‌ترین chunkها را با cosine similarity یا dot product بازیابی کنید.
6. بهترین snippetها را به `/v1/responses` یا `/v1/chat/completions` بدهید.

در یک vector index مدل‌ها یا تعداد ابعاد متفاوت را مخلوط نکنید. بردارهای query و سند باید با همان مدل embedding و همان dimensionality ساخته شوند.

پیش از ingest، قرارداد index را مشخص کنید: شناسه مدل، `dimensions`، metric فاصله، سیاست chunking، راهبرد زبان، فیلترهای metadata، قواعد نگهداری داده و trigger بازسازی embedding. تغییر هرکدام پس از launch معمولا به rebuild یا backfill بردارها نیاز دارد.

## انتخاب مدل و ابعاد

مدل‌های embedding فعلی AvalAI شامل مدل‌های سازگار با OpenAI مانند `text-embedding-3-small`، `text-embedding-3-large`، `text-embedding-ada-002` و گزینه‌های provider-specific از Gemini، Cohere، Alibaba، Cloudflare، BAAI و Nvidia NIM هستند. برای availability فعلی، [جزئیات مدل‌ها](fa/models/model-details.md) را ببینید.

فقط وقتی مدل انتخابی از بردار کوتاه‌تر پشتیبانی می‌کند از `dimensions` استفاده کنید. بردار کوچک‌تر هزینه ذخیره‌سازی، حافظه و جستجو را کم می‌کند، اما ممکن است کیفیت retrieval را کاهش دهد. اگر vector store شما سقف dimension دارد، ابعاد را هنگام ساخت embedding تنظیم کنید، نه اینکه بعدا بردار را دستی کوتاه کنید.

برای مدل‌های embedding نسل سوم OpenAI، اندازه پیش‌فرض بردار `1536` برای `text-embedding-3-small` و `3072` برای `text-embedding-3-large` است. این embeddingها به طول ۱ نرمال شده‌اند؛ بنابراین cosine similarity و dot product معمولا رتبه‌بندی یکسانی می‌دهند. برای تخمین توکن این مدل‌ها از `cl100k_base` استفاده کنید.

Embedding جایگزین داده تازه نیست. اگر کاربر درباره واقعیت‌های جدید یا خصوصی می‌پرسد، سندهای فعلی خودتان را embed و بازیابی کنید؛ به دانسته‌های داخلی مدل embedding تکیه نکنید.

API مرجع OpenAI ورودی خالی را نمی‌پذیرد و برای درخواست‌های embedding، محدودیت توکن وابسته به مدل را مستند می‌کند. در AvalAI محدودیت‌ها می‌توانند بر اساس provider، مدل، route و سطح حساب متفاوت باشند؛ بنابراین پیش از bulk backfill، [جزئیات مدل‌ها](fa/models/model-details.md)، [rate limitها](fa/guides/rate-limits.md) و یک dry run کوچک را بررسی کنید.

## هزینه، مقیاس و تازگی داده

هزینه درخواست‌های embedding معمولا بیشتر به توکن‌های ورودی و سپس هزینه ذخیره‌سازی/جستجو وابسته است. مقدار `usage.prompt_tokens` را برای محاسبه هزینه ingest لاگ کنید، بردار chunkهای بدون تغییر را cache کنید و به‌جای rebuild کامل index بعد از هر ویرایش سند، backfill تدریجی انجام دهید.

برای corpus بزرگ‌تر از یک مجموعه کوچک در حافظه، از vector database یا سرویس search برای K-nearest-neighbor lookup استفاده کنید. فیلترهای metadata را بیرون از فراخوانی مدل enforce کنید: اول tenant، permission، زبان، محصول، freshness و نوع سند را محدود کنید، سپس candidateهای باقی‌مانده را با similarity رتبه‌بندی کنید.

Embedding ابزار retrieval است، نه منبع واقعیت‌های تازه. مدل‌های OpenAI `text-embedding-3-*` برای similarity معنایی مفیدند، اما برنامه شما باید سندهای فعلی را بازیابی کند و از مدل مولد بخواهد بر اساس همان context پاسخ دهد.

## تنظیم جستجوی معنایی

جستجوی معنایی می‌تواند متن مرتبط را حتی وقتی query کاربر و سند کلمه‌های مشترک کمی دارند پیدا کند. برای نمونه، پرسشی مثل «انسان‌ها چه زمانی به ماه رسیدند؟» باید بتواند متنی درباره «اولین فرود روی ماه» را بازیابی کند، چون معنی دو عبارت نزدیک است.

در pipeline بازیابی سمت برنامه با AvalAI:

- **Queryهای مبهم را بازنویسی کنید** و به عبارت‌های کوتاه قابل جستجو تبدیل کنید، اما سؤال اصلی کاربر را برای فراخوانی نهایی مدل نگه دارید.
- **قبل از ranking فیلتر کنید**؛ با metadataهایی مثل tenant، زبان، محصول، نوع سند، مجوزها و تازگی داده.
- **`top_k` و thresholdها را تنظیم کنید** تا chunkهای کم‌اعتماد به‌عنوان evidence ضعیف وارد context مدل نشوند.
- **Semantic و keyword search را ترکیب کنید** وقتی ID دقیق، نام محصول، اصطلاح حقوقی یا تفاوت نگارش فارسی/انگلیسی اهمیت دارد.
- **تغییرات را با سؤال‌های برچسب‌خورده ارزیابی کنید** پیش از تغییر chunk size، overlap، مدل embedding، تعداد ابعاد یا منطق ranking.

برای الگوی کامل retrieval سمت برنامه و مسیر مهاجرت به retrieval میزبانی‌شده، [بازیابی](fa/guides/retrieval.md) را ببینید.

## ارزیابی کیفیت Retrieval

پیش از تغییر مدل embedding، `dimensions`، اندازه chunk، overlap، راهبرد زبان یا فرمول ranking، یک مجموعه کوچک retrieval با label بسازید. این کار الگوی semantic search در OpenAI را به gate تولیدی برای AvalAI تبدیل می‌کند:

| فیلد | کاربرد |
| --- | --- |
| `query` | سؤال طبیعی کاربر، همراه تفاوت‌های نگارشی فارسی/انگلیسی وقتی مهم است. |
| `must_include_doc_ids` | chunkها یا سندهایی که باید در نتیجه‌های برتر دیده شوند. |
| `forbidden_doc_ids` | chunkهای قدیمی، غیرمجاز یا گمراه‌کننده که نباید بازیابی شوند. |
| `filters` | فیلترهای tenant، permission، محصول، زبان یا freshness که باید قبل از ranking اعمال شوند. |
| `expected_answer_source` | passage منبعی که مدل مولد باید cite یا summarize کند. |

معیارهایی مثل `recall@k`، میانگین رتبه متقابل، latency، هزینه توکن و درصد پاسخ‌های grounded در sourceهای بازیابی‌شده را track کنید. این مجموعه را قبل و بعد از هر rebuild index اجرا کنید. برای محصول‌های دوزبانه، query فارسی روی محتوای فارسی، query انگلیسی روی محتوای انگلیسی، و queryهای mixed-language شبیه ترافیک واقعی پشتیبانی را وارد کنید.

## چک‌لیست موارد استفاده

راهنمای embedding شرکت OpenAI، embedding را یک نمایش عمومی برای ویژگی‌های متنی معرفی می‌کند. در پروژه‌های AvalAI، کاربردهای production رایج شامل این موارد است:

| مورد استفاده | الگوی عملی |
| --- | --- |
| جستجوی معنایی و RAG | chunkها را embed کنید، context مرتبط را بازیابی کنید و سپس با `/v1/responses` یا `/v1/chat/completions` پاسخ دهید. |
| پیشنهاددهی | آیتم‌ها را بر اساس شباهت برداری به یک آیتم مرجع یا پروفایل کاربر رتبه‌بندی کنید. |
| تشخیص تکراری‌ها | رکوردهای candidate را مقایسه کنید و همسایه‌های نزدیک بالاتر از threshold شباهت را علامت بزنید. |
| خوشه‌بندی | ticketها، reviewها یا گفت‌وگوهای پشتیبانی بدون label را پیش از خلاصه‌سازی گروه‌بندی کنید. |
| طبقه‌بندی سبک | labelها و متن ورودی را embed کنید، سپس نزدیک‌ترین label را انتخاب کنید یا یک classifier کوچک آموزش دهید. |
| تشخیص ناهنجاری | بردارهایی را که از خوشه معمول دور هستند برای بازبینی یا triage پیدا کنید. |
| جستجوی کد و مستندات | symbolها، خلاصه functionها و docs را embed کنید و در برابر سؤال طبیعی توسعه‌دهنده رتبه‌بندی کنید. |
| سنجش تنوع | توزیع شباهت‌ها را تحلیل کنید تا topicهای بیش‌ازحد تکراری، near-duplicateها یا gapهای corpus پیدا شوند. |
| feature encoding | از بردارها به‌عنوان ویژگی متن آزاد برای classifierها یا مدل‌های regression کوچک، وقتی label دارید، استفاده کنید. |

## مثال سریع

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.embeddings.create(
    model="text-embedding-3-small",
    input=[
        "AvalAI از APIهای سازگار با OpenAI پشتیبانی می‌کند.",
        "Embeddingها برای بازیابی سندهای مرتبط مفید هستند.",
    ],
    encoding_format="float",
)

vectors = [item.embedding for item in response.data]
print(len(vectors), len(vectors[0]))

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "text-embedding-3-small",
  input: [
    "AvalAI از APIهای سازگار با OpenAI پشتیبانی می‌کند.",
    "Embeddingها برای بازیابی سندهای مرتبط مفید هستند.",
  ],
  encoding_format: "float",
});

const vectors = response.data.map((item) => item.embedding);
console.log(vectors.length, vectors[0].length);

bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-3-small",
    "input": [
      "AvalAI از APIهای سازگار با OpenAI پشتیبانی می‌کند.",
      "Embeddingها برای بازیابی سندهای مرتبط مفید هستند."
    ],
    "encoding_format": "float"
  }'

```

## نکته‌های Production

- برای chunkهای بدون تغییر، embedding را cache کنید؛ embedding دوباره در هر درخواست کند و پرهزینه است.
- شناسه chunkها را پایدار نگه دارید تا فقط سندهای تغییرکرده را به‌روزرسانی کنید.
- metadata مربوط به مجوزها را ذخیره کنید و نتیجه‌ها را قبل از ارسال context به مدل فیلتر کنید.
- برای embedding فوری چند متن از آرایه `input` استفاده کنید؛ از [پردازش دسته‌ای](fa/guides/batch-processing.md) فقط برای jobهای آفلاین و وقتی route پشتیبانی می‌کند استفاده کنید.
- قبل از embedding ورودی‌های بزرگ، توکن‌ها را بشمارید؛ [شمارش توکن](fa/guides/token-counting.md) را ببینید.
- بردارهای ذخیره‌شده را داده مشتق‌شده از کاربر بدانید. آن‌ها متن خوانا نیستند، اما می‌توانند الگوهای شباهت را آشکار کنند؛ پس همان tenant isolation، retention و deletion policy سندهای منبع را برای آن‌ها اعمال کنید.

## منابع مرتبط

- [مرجع API Embeddings](fa/api-reference/embeddings.md)
- [RAG دستی با Embeddings](fa/examples/manual_rag_with_embeddings.md)
- [راهنمای Retrieval](fa/guides/retrieval.md)
- [درخواست‌های موازی سازگار با Rate Limit](fa/examples/rate_limit_safe_parallel_requests.md)
