# افزودن مدل‌های جدید Cohere: Rerank v4 و Azure Embed v4

**تاریخ:** 1403-09-23 / (2025-12-14)

## خلاصه

مدل‌های جدید Rerank v4 از Cohere (نسخه‌های Pro و Fast) برای رتبه‌بندی مجدد جستجوی معنایی پیشرفته، و مدل embedding جدید `embed-v-4-0` روی زیرساخت Azure AI services با محدودیت نرخ تا 30 برابر بیشتر نسبت به endpoint استاندارد Cohere اضافه شده‌اند.

---

## جزئیات

### مدل‌های Cohere Rerank v4

مدل‌های Rerank v4 از Cohere پیشرفت قابل توجهی در رتبه‌بندی مجدد جستجوی معنایی هستند و پنجره context به اندازه 32,768 توکن ارائه می‌دهند—تقریبا 8 برابر بزرگتر از نسخه‌های قبلی. هر دو مدل از بیش از 100 زبان پشتیبانی می‌کنند و داده‌های ساختاریافته فرمت شده به صورت رشته‌های YAML را مدیریت می‌کنند.

- **[Cohere Rerank v4 Pro](fa/providers/cohere.md)** (`cohere-rerank-v4.0-pro`): مدل رتبه‌بندی مجدد با بالاترین کیفیت برای بارهای کاری production که به حداکثر دقت مرتبط‌سازی نیاز دارند. [مستندات مدل](fa/providers/cohere.md)

- **[Cohere Rerank v4 Fast](fa/providers/cohere.md)** (`cohere-rerank-v4.0-fast`): یک مدل رتبه‌بندی مجدد مقرون به صرفه که برای برنامه‌های با توان عملیاتی بالا با حداقل تاخیر بهینه‌سازی شده است. [مستندات مدل](fa/providers/cohere.md)

**ویژگی‌های کلیدی:**
- **پنجره Context بزرگ**: 32,768 توکن در هر سند (8 برابر بزرگتر از v3.5)
- **پشتیبانی چندزبانه**: پشتیبانی از بیش از 100 زبان
- **داده‌های ساختاریافته**: پشتیبانی بومی از اسناد ساختاریافته فرمت YAML
- **ظرفیت سند بالا**: پردازش تا 10,000 سند در هر درخواست
- **امتیازات نرمال‌شده**: امتیازات مرتبط‌سازی در بازه [0, 1] برای تفسیر آسان
- **پشتیبانی Endpoint**: در دسترس در v1/rerank

**قیمت‌گذاری:**

| مدل | هزینه هر کوئری |
|-------|----------------|
| cohere-rerank-v4.0-pro | $0.0025/کوئری |
| cohere-rerank-v4.0-fast | $0.002/کوئری |

### نمونه‌های API Rerank

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "cohere-rerank-v4.0-pro",
    "query": "پایتخت ایالات متحده کجاست؟",
    "documents": [
      "کارسون سیتی پایتخت ایالت نوادا در آمریکاست.",
      "واشنگتن دی‌سی پایتخت ایالات متحده است. این یک منطقه فدرال است.",
      "مجازات اعدام از قبل از تشکیل کشور در ایالات متحده وجود داشته است."
    ],
    "top_n": 3
  }'
```

#### نمونه پاسخ

```json
{
  "id": "rerank-abc123xyz",
  "results": [
    {
      "index": 1,
      "relevance_score": 0.943264
    },
    {
      "index": 0,
      "relevance_score": 0.590401
    },
    {
      "index": 2,
      "relevance_score": 0.466457
    }
  ],
  "usage": {
    "search_units": 1
  },
  "estimated_cost": {
    "unit": "0.0025000000",
    "irt": 286.5,
    "exchange_rate": 114600
  }
}
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "cohere-rerank-v4.0-pro",
    "query": "یادگیری ماشین چیست؟",
    "documents": [
      "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
      "یادگیری عمیق از شبکه‌های عصبی با لایه‌های زیاد استفاده می‌کند.",
      "هوای امروز آفتابی با آسمان صاف است."
    ],
    "top_n": 2
  }'

python=:from openai import OpenAI
import requests

api_key = "your-avalai-api-key"

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "cohere-rerank-v4.0-pro",
        "query": "یادگیری ماشین چیست؟",
        "documents": [
            "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
            "یادگیری عمیق از شبکه‌های عصبی با لایه‌های زیاد استفاده می‌کند.",
            "هوای امروز آفتابی با آسمان صاف است.",
        ],
        "top_n": 2,
    },
)

print(response.json())

javascript=:const response = await fetch("https://api.avalai.ir/v1/rerank", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        model: "cohere-rerank-v4.0-pro",
        query: "یادگیری ماشین چیست؟",
        documents: [
            "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
            "یادگیری عمیق از شبکه‌های عصبی با لایه‌های زیاد استفاده می‌کند.",
            "هوای امروز آفتابی با آسمان صاف است."
        ],
        top_n: 2
    })
});

const result = await response.json();
console.log(result);

```

### Azure Embed v4 (محدودیت نرخ بالا)

- **[Embed v4 (Azure)](fa/providers/cohere.md)** (`embed-v-4-0`): جدیدترین مدل embedding از Cohere که از طریق زیرساخت Azure AI services ارائه می‌شود و محدودیت نرخ تا 30 برابر بیشتر و پایداری بهبودیافته نسبت به endpoint استاندارد `cohere.embed-v4:0` فراهم می‌کند. [مستندات مدل](fa/providers/cohere.md)

**ویژگی‌های کلیدی:**
- **محدودیت نرخ بالا**: تا 30 برابر توان عملیاتی بیشتر نسبت به endpoint استاندارد Cohere embed
- **پشتیبانی چندوجهی**: پردازش متن و تصاویر
- **ابعاد منعطف**: انتخاب از 256، 512، 1024 یا 1536 (پیش‌فرض) بعد خروجی
- **پنجره Context بزرگ**: 128k توکن برای پردازش اسناد گسترده
- **پایداری بهبودیافته**: زیرساخت Azure قابلیت اطمینان درجه سازمانی فراهم می‌کند
- **کیفیت مدل یکسان**: کیفیت embedding مشابه با `cohere.embed-v4:0`
- **پشتیبانی Endpoint**: در دسترس در v1/embeddings

**قیمت‌گذاری:**

| مدل | ورودی متن | ورودی تصویر |
|-------|------------|-------------|
| embed-v-4-0 | $0.12/1M توکن | $0.47/1M توکن |

### نمونه‌های API Embedding

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "embed-v-4-0",
    "input": "هوش مصنوعی در حال تغییر نحوه کار و زندگی ماست.",
    "encoding_format": "float"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="embed-v-4-0",
    input="هوش مصنوعی در حال تغییر نحوه کار و زندگی ماست.",
    encoding_format="float",
)

print(response.data[0].embedding[:10])  # ده بعد اول

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "embed-v-4-0",
  input: "هوش مصنوعی در حال تغییر نحوه کار و زندگی ماست.",
  encoding_format: "float"
});

console.log(response.data[0].embedding.slice(0, 10));  // ده بعد اول

```

#### نمونه پاسخ Embedding

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0.0234375,
        -0.015625,
        0.0456789,
        -0.0123456,
        0.0678901,
        "...[مجموعا 1536 بعد]"
      ]
    }
  ],
  "model": "embed-v-4-0",
  "usage": {
    "prompt_tokens": 12,
    "total_tokens": 12
  },
  "estimated_cost": {
    "unit": "0.0000014400",
    "irt": 0.17,
    "exchange_rate": 114600
  }
}
```

---

## موارد استفاده

### Cohere Rerank v4
- **سیستم‌های RAG**: بهبود کیفیت بازیابی با رتبه‌بندی مجدد اسناد بازیابی شده قبل از ارسال به LLMها
- **جستجوی معنایی**: افزایش مرتبط‌سازی نتایج جستجو برای برنامه‌های جستجوی سازمانی
- **پردازش اسناد**: رتبه‌بندی مجدد اسناد طولانی با پنجره context گسترش یافته 32k
- **جستجوی چندزبانه**: ساخت سیستم‌های جستجو با پشتیبانی از بیش از 100 زبان
- **جستجوی داده‌های ساختاریافته**: رتبه‌بندی مجدد اسناد ساختاریافته فرمت YAML

### Azure Embed v4 (embed-v-4-0)
- **برنامه‌های با توان عملیاتی بالا**: ایده‌آل برای سیستم‌های production که به نرخ درخواست بالای ثابت نیاز دارند
- **RAG سازمانی**: ساخت سیستم‌های RAG قابل اطمینان با تولید embedding پایدار
- **پردازش دسته‌ای**: پردازش کارآمد مجموعه‌های بزرگ اسناد
- **جستجوی چندوجهی**: ایجاد سیستم‌های جستجو با ترکیب محتوای متن و تصویر
- **برنامه‌های بلادرنگ**: مناسب برای برنامه‌هایی که به embeddingهای با تاخیر کم در مقیاس نیاز دارند

---

## نکته مهاجرت

اگر در حال حاضر از `cohere.embed-v4:0` استفاده می‌کنید، می‌توانید به راحتی به `embed-v-4-0` برای محدودیت نرخ بالاتر تغییر دهید. هر دو مدل embeddingهای یکسان تولید می‌کنند و سازگاری با پایگاه‌داده‌های بردار و برنامه‌های موجود را تضمین می‌کنند.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Cohere](fa/providers/cohere.md)
- [مرجع API Rerank](fa/api-reference/rerank.md)
- [مرجع API Embeddings](fa/api-reference/embeddings.md)
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md)
- [راهنمای بازیابی](fa/guides/retrieval.md)