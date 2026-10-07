# RAG دستی با Embeddings

Retrieval-Augmented Generation یا RAG به مدل کمک می‌کند از روی اسناد خودتان پاسخ بدهد. ابزارهای hosted مثل file search می‌توانند معماری را ساده‌تر کنند، اما اگر کنترل کامل روی ذخیره‌سازی، فیلتر، امتیازدهی یا قابلیت‌های هنوز فعال‌نشده AvalAI می‌خواهید، می‌توانید یک pipeline کوچک RAG را با embeddings و Responses API بسازید.

> این راهنما با اقتباس از [OpenAI Cookbook رسمی](https://developers.openai.com/cookbook)، به‌ویژه نمونه‌های [پرسش و پاسخ با embeddings](https://github.com/openai/openai-cookbook/blob/main/examples/Question_answering_using_embeddings.ipynb) و [file search با Responses](https://github.com/openai/openai-cookbook/blob/main/examples/File_Search_Responses.ipynb)، همراه با تغییرات لازم برای endpoint و کلید API در AvalAI تهیه شده است.

## چه چیزی می‌سازید

این مثال چند متن سیاست پشتیبانی را index می‌کند، برای آن‌ها embedding می‌سازد، مرتبط‌ترین متن‌ها را برای سوال کاربر پیدا می‌کند و از مدل می‌خواهد فقط بر اساس context بازیابی‌شده پاسخ دهد.

این روش دستی مناسب است اگر:

- می‌خواهید از database یا سرویس search خودتان استفاده کنید.
- قبل از generation به فیلتر deterministic نیاز دارید.
- می‌خواهید کیفیت retrieval را مستقیم ارزیابی کنید.
- hosted vector store یا file search برای endpoint انتخابی شما در دسترس نیست.

## نگاشت این روش به File Search میزبانی‌شده

الگوی File Search میزبانی‌شده در OpenAI از Responses API به‌همراه vector storeهای مدیریت‌شده توسط ارائه‌دهنده استفاده می‌کند: فایل‌ها را upload می‌کنید، یک vector store می‌سازید، فایل‌ها را به آن وصل می‌کنید، تا وضعیت indexing برابر `completed` شود صبر می‌کنید، سپس `/v1/responses` را با ابزار `file_search` فراخوانی می‌کنید و آیتم‌های خروجی `file_search_call` و `message` را بررسی می‌کنید. در AvalAI، File Search و APIهای vector store میزبانی‌شده هنوز در حال توسعه هستند، بنابراین همین مفاهیم را فعلا به‌صورت دستی پیاده‌سازی کنید:

| مفهوم در File Search میزبانی‌شده | معادل دستی در AvalAI امروز |
| --------------------------------- | --------------------------- |
| `vector_store`                    | جدول database، object store، FAISS/Milvus/Pinecone index یا سرویس search خودتان |
| `vector_store.file`               | یک chunk با `id` پایدار، نام فایل منبع، attributes، متن و embedding |
| `max_num_results`                 | مقدار `k` در retrieval و سقف بودجه توکن context |
| `filters` / `attributes`          | فیلتر SQL/search که قبل از شباهت برداری اعمال می‌شود |
| `include` search results          | لاگ کردن chunk ID، score، filename و متن‌های بازیابی‌شده |
| `file_citation`                   | source IDهایی که به مدل می‌گویید در پاسخ نهایی cite کند |

## کنترل‌های Retrieval که بهتر است نگه دارید

این کنترل‌ها از retrieval میزبانی‌شده حتی در یک pipeline دستی کوچک هم مفید هستند:

- **بازنویسی query**: پرسش‌های مبهم کاربر را قبل از embedding به queryهای کوتاه‌تر و قابل جستجو تبدیل کنید.
- **retrieval ترکیبی**: شباهت برداری dense را با keyword/BM25 برای نام محصول، شناسه دقیق و اصطلاحات policy ترکیب کنید.
- **فیلتر metadata**: قبل از ranking بر اساس tenant، region، محصول، permission، تاریخ یا نوع سند فیلتر کنید.
- **آستانه score**: chunkهای کم‌ارتباط را حذف کنید تا context ضعیف وارد prompt نشود.
- **استراتژی chunking**: بر اساس heading یا بخش معنایی خرد کنید، overlap محدود نگه دارید و metadata منبع را حفظ کنید.
- **ارزیابی**: پیش از تغییر chunk size یا `k`، معیارهای `Recall@k`، `MRR` و grounded بودن پاسخ را بسنجید.

retrieval اسناد و حافظه کاربر به سیاست‌های نوشتن متفاوتی نیاز دارند. برای الگویی با scope جداگانه tenant، کاربر و عامل که فقط اطلاعات تاییدشده و قابل استفاده مجدد را ذخیره می‌کند، [حافظه پایدار عامل با Embeddings](fa/examples/durable_agent_memory.md) را ببینید.

## مثال کامل Python

پیش‌نیاز‌ها را نصب کنید:

```bash
pip install openai numpy
export AVALAI_API_KEY="your-avalai-api-key"
```

فایل `rag_demo.py` را بسازید:

```python
import os
from dataclasses import dataclass

import numpy as np
from openai import OpenAI

EMBEDDING_MODEL = "text-embedding-3-small"
GENERATION_MODEL = "gpt-5.6-luna"
MIN_RETRIEVAL_SCORE = 0.2

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


@dataclass
class Document:
    id: str
    title: str
    text: str
    embedding: list[float] | None = None


documents = [
    Document(
        id="refunds",
        title="Refund policy",
        text=(
            "Customers can request a refund within 14 days of purchase if usage "
            "is below 10 percent of the purchased credit package."
        ),
    ),
    Document(
        id="rate-limits",
        title="Rate limit policy",
        text=(
            "Rate limits are tier based. Higher tiers increase requests per minute "
            "and tokens per minute. Applications should retry 429 errors with backoff."
        ),
    ),
    Document(
        id="keys",
        title="API key handling",
        text=(
            "API keys must be stored in environment variables or secret managers. "
            "Never expose keys in browser code, mobile apps, logs, or public repositories."
        ),
    ),
]


def embed_texts(texts: list[str]) -> list[list[float]]:
    response = client.embeddings.create(
        model=EMBEDDING_MODEL,
        input=texts,
    )
    return [item.embedding for item in response.data]


def cosine_similarity(a: list[float], b: list[float]) -> float:
    va = np.array(a)
    vb = np.array(b)
    return float(np.dot(va, vb) / (np.linalg.norm(va) * np.linalg.norm(vb)))


def index_documents() -> None:
    embeddings = embed_texts([doc.text for doc in documents])
    for doc, embedding in zip(documents, embeddings):
        doc.embedding = embedding


def retrieve(query: str, k: int = 2) -> list[tuple[Document, float]]:
    query_embedding = embed_texts([query])[0]
    scored = [
        (doc, cosine_similarity(query_embedding, doc.embedding))
        for doc in documents
        if doc.embedding is not None
    ]
    ranked = sorted(scored, key=lambda item: item[1], reverse=True)
    return [(doc, score) for doc, score in ranked if score >= MIN_RETRIEVAL_SCORE][:k]


def answer_with_context(question: str) -> str:
    matches = retrieve(question)
    context = "\n\n".join(
        f"[{doc.id}] {doc.title}\n{doc.text}" for doc, score in matches
    )

    response = client.responses.create(
        model=GENERATION_MODEL,
        instructions=(
            "Answer only from the provided context. If the context is not enough, "
            "say that the documentation does not contain the answer. Cite source IDs."
        ),
        input=f"Context:\n{context}\n\nQuestion: {question}",
    )
    return response.output_text


if __name__ == "__main__":
    index_documents()
    question = "How should my app react when it gets rate limited?"
    print(answer_with_context(question))
```

اجرا:

```bash
python rag_demo.py
```

## نسخه JavaScript

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const EMBEDDING_MODEL = "text-embedding-3-small";
const GENERATION_MODEL = "gpt-5.6-luna";
const MIN_RETRIEVAL_SCORE = 0.2;

const documents = [
  {
    id: "refunds",
    title: "Refund policy",
    text: "Customers can request a refund within 14 days of purchase if usage is below 10 percent of the purchased credit package.",
  },
  {
    id: "rate-limits",
    title: "Rate limit policy",
    text: "Rate limits are tier based. Higher tiers increase requests per minute and tokens per minute. Applications should retry 429 errors with backoff.",
  },
  {
    id: "keys",
    title: "API key handling",
    text: "API keys must be stored in environment variables or secret managers. Never expose keys in browser code, mobile apps, logs, or public repositories.",
  },
];

async function embedTexts(texts) {
  const response = await client.embeddings.create({
    model: EMBEDDING_MODEL,
    input: texts,
  });
  return response.data.map((item) => item.embedding);
}

function cosineSimilarity(a, b) {
  const dot = a.reduce((sum, value, index) => sum + value * b[index], 0);
  const normA = Math.sqrt(a.reduce((sum, value) => sum + value * value, 0));
  const normB = Math.sqrt(b.reduce((sum, value) => sum + value * value, 0));
  return dot / (normA * normB);
}

async function retrieve(question, k = 2) {
  const documentEmbeddings = await embedTexts(documents.map((doc) => doc.text));
  const queryEmbedding = (await embedTexts([question]))[0];

  return documents
    .map((doc, index) => ({
      ...doc,
      score: cosineSimilarity(queryEmbedding, documentEmbeddings[index]),
    }))
    .sort((a, b) => b.score - a.score)
    .filter((doc) => doc.score >= MIN_RETRIEVAL_SCORE)
    .slice(0, k);
}

async function answerWithContext(question) {
  const matches = await retrieve(question);
  const context = matches
    .map((doc) => `[${doc.id}] ${doc.title}\n${doc.text}`)
    .join("\n\n");

  const response = await client.responses.create({
    model: GENERATION_MODEL,
    instructions:
      "Answer only from the provided context. If the context is not enough, say that the documentation does not contain the answer. Cite source IDs.",
    input: `Context:\n${context}\n\nQuestion: ${question}`,
  });

  return response.output_text;
}

console.log(
  await answerWithContext("How should my app react when it gets rate limited?"),
);
```

## اجزای پایه با cURL

با cURL می‌توانید هر مرحله را جداگانه تست کنید.

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "text-embedding-3-small",
    "input": [
      "Rate limits are tier based. Applications should retry 429 errors with backoff.",
      "API keys must be stored in environment variables or secret managers."
    ]
  }'

curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "Answer only from the provided context and cite source IDs.",
    "input": "Context:\n[rate-limits] Rate limits are tier based. Applications should retry 429 errors with backoff.\n\nQuestion: How should my app react when it gets rate limited?"
  }'
```

## بررسی کیفیت Retrieval

تا زمان شکست generation صبر نکنید. از همان ابتدا retrieval را با این معیارها بسنجید:

- برای هر سوال تست، document ID مورد انتظار را ذخیره کنید.
- `Recall@k` را محاسبه کنید: آیا سند مورد انتظار در top `k` دیده می‌شود؟
- `MRR` را محاسبه کنید: اولین سند درست چقدر بالا رتبه گرفته است؟
- IDهای بازیابی‌شده را کنار هر پاسخ تولیدی لاگ کنید.
- قبل از افزایش `k`، matchهای کم‌امتیاز را بازبینی کنید؛ context بیشتر همیشه پاسخ بهتر نمی‌سازد.

## بهترین شیوه‌ها

- اسناد بلند را بر اساس بخش و heading خرد کنید، نه فقط تعداد کاراکتر.
- source IDها را پایدار نگه دارید تا citationهای تولیدشده قابل استفاده بمانند.
- metadata را کنار هر chunk ذخیره کنید تا بتوانید قبل از retrieval فیلتر کنید.
- فقط وقتی vector store شما بردارهای کوتاه‌تر می‌خواهد از پارامتر `dimensions` استفاده کنید؛ تعداد ابعاد را بین documentها و queryها یکسان نگه دارید.
- context بازیابی‌شده را قبل از سوال کاربر قرار دهید و chunkها را واضح جدا کنید.
- از مدل بخواهید اگر context کافی نیست، صریح بگوید.
- embedding اسناد بدون تغییر را cache کنید؛ embedding گرفتن در هر request کند و پرهزینه است.

## لینک‌های مرتبط

- [مرجع Embeddings API](fa/api-reference/embeddings.md)
- [مرجع Responses API](fa/api-reference/responses.md)
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
