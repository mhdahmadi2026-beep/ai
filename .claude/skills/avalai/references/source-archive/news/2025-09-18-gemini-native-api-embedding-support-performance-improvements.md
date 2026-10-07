# گسترش API بومی Gemini: پشتیبانی از تعبیه‌سازی و بهبود عملکرد

**Date:** 1404-06-28 / (2025-09-18)

## خلاصه

AvalAI با افزودن پشتیبانی جامع از تعبیه‌سازی از طریق نقطه پایانی جدید `embedContent` API بومی Gemini `v1beta` را گسترش می‌دهد، ویژگی‌های بهینه‌سازی خاص وظیفه را معرفی می‌کند و بهبودهای عملکرد API شامل افزایش نرخ موفقیت و کاهش تاخیر را به عنوان بخشی از تلاش‌های بهبود عملکرد مداوم ما ارائه می‌دهد.

---

## جزئیات

ما بهبودهایی را در API بومی Gemini `v1beta` اعلام می‌کنیم که قابلیت‌های تعبیه‌سازی را گسترش می‌دهد و در عین حال عملکرد بهبود یافته‌ای را در سراسر پلتفرم ما ارائه می‌دهد.

### پشتیبانی از تعبیه‌سازی API بومی Gemini

ما پشتیبانی جامع از تعبیه‌سازی را به API بومی Gemini `v1beta` اضافه کرده‌ایم که به توسعه‌دهندگان امکان استفاده از مدل‌های تعبیه‌سازی پیشرفته گوگل را از طریق رویکردهای سازگار با OpenAI و SDK بومی Google GenAI می‌دهد.

#### نقطه پایانی جدید embedContent

- **gemini-embedding-001**: مدل تعبیه‌سازی اصلی گوگل با بهینه‌سازی خاص وظیفه پیشرفته و کنترل انعطاف‌پذیر ابعاد. [مستندات](fa/providers/google.md)

**ویژگی‌های کلیدی:**
- **نقطه پایانی**: `/v1beta/models/{model}:embedContent`
- **حداکثر توکن‌های ورودی**: ۲٬۰۴۸ توکن
- **ابعاد خروجی**: انعطاف‌پذیر ۱۲۸-۳۰۷۲ (توصیه‌شده: ۷۶۸، ۱۵۳۶، ۳۰۷۲)
- **قیمت‌گذاری ورودی**: ۰.۱۵ دلار / ۱ میلیون توکن
- **قیمت‌گذاری خروجی**: ۰.۰۷۵ دلار / ۱ میلیون توکن
- **انواع وظایف**: `SEMANTIC_SIMILARITY،` `CLASSIFICATION،` `CLUSTERING،` `RETRIEVAL_DOCUMENT،` `RETRIEVAL_QUERY،` `CODE_RETRIEVAL_QUERY،` `QUESTION_ANSWERING،` `FACT_VERIFICATION`
- **ویژگی‌های پیشرفته**: یادگیری نمایش ماتریوشکا (MRL) برای ابعاد انعطاف‌پذیر
- **در دسترس در**: [`/v1beta/models`](fa/api-reference/v1beta.md)، [`v1/embeddings`](fa/api-reference/embeddings.md)

```language-selector
python=:from google import genai
from google.genai import types

client = genai.Client(
    api_key="your-avalai-api-key",
    http_options={"api_version": "v1beta", "base_url": "https://api.avalai.ir"},
)

# تولید تعبیه‌سازی پایه
result = client.models.embed_content(
    model="gemini-embedding-001", contents="معنای زندگی چیست؟"
)

print(f"ابعاد تعبیه‌سازی: {len(result.embeddings[0].values)}")

# استفاده پیشرفته با نوع وظیفه و ابعاد سفارشی
result = client.models.embed_content(
    model="gemini-embedding-001",
    contents=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    config=types.EmbedContentConfig(
        task_type="SEMANTIC_SIMILARITY", output_dimensionality=768
    ),
)

for i, embedding in enumerate(result.embeddings):
    print(f"تعبیه‌سازی {i}: {len(embedding.values)} بعد")

javascript=:import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
    apiKey: process.env.AVALAI_API_KEY,
    httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}}
});

// تولید تعبیه‌سازی پایه
const response = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: "معنای زندگی چیست؟"
});

console.log(`ابعاد تعبیه‌سازی: ${response.embeddings[0].values.length}`);

// استفاده پیشرفته با نوع وظیفه
const advancedResponse = await ai.models.embedContent({
    model: "gemini-embedding-001",
    contents: [
        "معنای زندگی چیست؟",
        "هدف وجود چیست؟"
    ],
    taskType: "SEMANTIC_SIMILARITY",
    outputDimensionality: 768
});

console.log(`${advancedResponse.embeddings.length} تعبیه‌سازی تولید شد`);

bash=:# تعبیه‌سازی پایه با API بومی
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

### پشتیبانی بهبود یافته از تعبیه‌سازی سازگار با OpenAI

علاوه بر پشتیبانی از API بومی، ما نقطه پایانی تعبیه‌سازی سازگار با OpenAI خود را با قابلیت‌های کامل تعبیه‌سازی Gemini بهبود داده‌ایم:

```language-selector
python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

# تعبیه‌سازی پیشرفته Gemini با نوع وظیفه و ابعاد سفارشی
response = client.embeddings.create(
    model="gemini-embedding-001",
    input=["معنای زندگی چیست؟", "هدف وجود چیست؟", "چگونه کیک درست کنم؟"],
    extra_body={"task_type": "SEMANTIC_SIMILARITY", "output_dimensionality": 768},
)

# محاسبه شباهت کسینوسی
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

embeddings = [item.embedding for item in response.data]
embeddings_matrix = np.array(embeddings)
similarity_matrix = cosine_similarity(embeddings_matrix)

print(f"شباهت بین دو متن اول: {similarity_matrix[0, 1]:.4f}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تعبیه‌سازی پیشرفته Gemini با نوع وظیفه
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

```

### نتایج تلاش‌های بهبود عملکرد

به عنوان بخشی از تلاش‌های بهبود پیوسته عملکرد، که ماه گذشته آغاز شد، ما بهبودهای قابل توجهی را در پایداری سرویس API و عملکرد ارائه داده‌ایم:

**بهبودهای عملکرد:**
- **بهبود نرخ موفقیت**: بهبود نرخ موفقیت API در تمام نقاط پایانی
- **کاهش تاخیر**: کاهش متوسط تاخیر پاسخ برای عملیات تعبیه‌سازی
- **پایداری اتصال**: بهبود مدیریت اتصال و مدیریت خطا
- **بهینه‌سازی توان عملیاتی**: افزایش ظرفیت مدیریت درخواست‌های همزمان به میزان ۷۰٪
- **بازیابی خطا**: بهبود مکانیسم‌های تلاش مجدد خودکار و تنزل تدریجی

**سرویس‌های تحت تاثیر:**
- [`v1/embeddings`](fa/api-reference/embeddings.md) - بهبود عملکرد تولید تعبیه‌سازی
- [`/v1beta/models`](fa/api-reference/v1beta.md) - بهبود قابلیت اطمینان API بومی Gemini
- [`v1/chat/completions`](fa/api-reference/chat.md) - بهینه‌سازی پردازش جریانی و دسته‌ای
- [`v1/responses`](fa/api-reference/responses.md) - بهبود پایداری تولید پاسخ

### ویژگی‌های تعبیه‌سازی پیشرفته

پیاده‌سازی تعبیه‌سازی Gemini ما شامل ویژگی‌های پیشرفته برای عملکرد بهینه است:

**بهینه‌سازی خاص وظیفه:**
- **`SEMANTIC_SIMILARITY`**: بهینه‌سازی شده برای سیستم‌های توصیه و تشخیص تکراری
- **`CLASSIFICATION`**: بهبود یافته برای تحلیل احساسات و تشخیص اسپم
- **`CLUSTERING`**: بهبود یافته برای سازماندهی اسناد و تحقیقات بازار
- **`RETRIEVAL_DOCUMENT`**: بهینه‌سازی شده برای سیستم‌های RAG و موتورهای جستجو
- **`RETRIEVAL_QUERY`**: بهبود یافته برای برنامه‌های جستجوی سفارشی
- **`CODE_RETRIEVAL_QUERY`**: تخصصی شده برای جستجوی کد و جستجوی مستندات
- **`QUESTION_ANSWERING`**: بهینه‌سازی شده برای چت‌بات‌ها و سیستم‌های FAQ
- **`FACT_VERIFICATION`**: بهبود یافته برای سیستم‌های تایید خودکار

**کنترل انعطاف‌پذیر ابعاد:**
- پشتیبانی از ۱۲۸-۳۰۷۲ بعد با یادگیری نمایش ماتریوشکا (MRL)
- ابعاد توصیه‌شده: ۷۶۸، ۱۵۳۶، ۳۰۷۲ برای عملکرد بهینه
- نرمال‌سازی خودکار برای ۳۰۷۲ بعد
- راهنمایی نرمال‌سازی دستی برای ابعاد کوچک‌تر

---

## لینک‌های مرتبط

- [مستندات مدل‌های گوگل](fa/providers/google.md) - راهنمای کامل مدل‌ها و تعبیه‌سازی‌ Gemini
- [مرجع API تعبیه‌سازی](fa/api-reference/embeddings.md) - مستندات نقطه پایانی تعبیه‌سازی سازگار با OpenAI
- [مرجع API v1beta](fa/api-reference/v1beta.md) - مستندات API بومی Gemini با نقطه پایانی embedContent
- [پشتیبانی از API بومی Gemini](fa/news/2025-07-22-native-gemini-api-support-now-available.md) - اعلامیه قبلی پشتیبانی از API بومی
- [بهبودهای عملکرد جریانی](fa/news/2025-09-14-deepseek-v3-1-grok-code-fast-1-streaming-improvements.md) - اعلامیه قبلی بهبود عملکرد