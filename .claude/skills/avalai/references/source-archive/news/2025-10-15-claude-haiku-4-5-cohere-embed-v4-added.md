# افزودن مدل‌های پایدار جدید: Claude Haiku 4.5 و Cohere Embed v4

**تاریخ:** 1404-07-24 / (2025-10-15)

## خلاصه

دو مدل پایدار جدید به AvalAI اضافه شده‌اند: Claude Haiku 4.5 از Anthropic که یک مدل کدنویسی با کارایی بالا است و قابلیت‌های نزدیک به مرزهای دانش را با سرعت استثنایی و هزینه بهینه ارائه می‌دهد، و Embed v4 از Cohere که یک مدل embedding پیشرفته با پشتیبانی از متن، تصویر و محتوای ترکیبی با پنجره context به اندازه 128k است.

---

## جزئیات

### Anthropic

- **[Claude Haiku 4.5](fa/providers/anthropic.md)** (‍‍‍‍`claude-haiku-4-5`): یک مدل کوچک قدرتمند که عملکرد کدنویسی نزدیک به مرزهای دانش را با یک سوم هزینه و بیش از دو برابر سرعت Claude Sonnet 4 ارائه می‌دهد. ایده‌آل برای برنامه‌های بلادرنگ، دستیارهای چت، ایجنت‌های خدمات مشتری، وایب کُدینگ  و گردش‌کارهای ایجنتی. [مستندات مدل](fa/providers/anthropic.md)

**ویژگی‌های کلیدی:**
- **کارایی بالا**: قابلیت‌های کدنویسی معادل Claude Sonnet 4 با عملکرد برتر در استفاده از کامپیوتر
- **سرعت استثنایی**: تا 4-5 برابر سریعتر از Sonnet 4.5 برای نمونه‌سازی سریع و هماهنگی چند-ایجنته
- **بهینه‌سازی هزینه**: ارائه عملکرد مدل premium با کم‌ترین هزینه
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته، استفاده از کامپیوتر و پشتیبانی از بینایی
- **پنجره Context**: 200k توکن برای مکالمات گسترده و پردازش اسناد
- **پشتیبانی Endpoint**: در دسترس در v1/chat/completions و v1/messages

**قیمت‌گذاری:**

| مدل | ورودی | خروجی |
|-------|-------|--------|
| claude-haiku-4-5-20251001-v1:0 | $1.00/1M توکن | $5.00/1M توکن |

### نمونه درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-haiku-4-5",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای محاسبه دنباله فیبوناچی با استفاده از memoization بنویس."
      }
    ],
    "max_tokens": 1024
  }'
```

#### نمونه پاسخ

```json
{
  "id": "msg_01ABC123xyz",
  "created": 1729026000,
  "model": "claude-haiku-4-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "این یک تابع کارآمد پایتون برای محاسبه اعداد فیبوناچی با استفاده از memoization است:\n\n
```python\ndef fibonacci(n, memo={}):\n    if n in memo:\n        return memo[n]\n    if n <= 1:\n        return n\n    memo[n] = fibonacci(n-1, memo) + fibonacci(n-2, memo)\n    return memo[n]\n\n# مثال استفاده\nfor i in range(10):\n    print(f\"F({i}) = {fibonacci(i)}\")\n```\n\nاین پیاده‌سازی از دیکشنری برای ذخیره مقادیر محاسبه شده استفاده می‌کند و پیچیدگی زمانی را از O(2^n) به O(n) کاهش می‌دهد.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 145,
    "prompt_tokens": 23,
    "total_tokens": 168,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 23,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0007480000",
    "irt": 85.72,
    "exchange_rate": 114600
  }
}
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-haiku-4-5",
    "messages": [
      {
        "role": "user",
        "content": "به من در دیباگ کردن این کد پایتون کمک کن."
      }
    ],
    "max_tokens": 2048
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="claude-haiku-4-5",
    messages=[
        {
            "role": "user",
            "content": "به من در دیباگ کردن این کد پایتون کمک کن.",
        }
    ],
    max_tokens=2048,
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "claude-haiku-4-5",
  messages: [
    {
      role: "user",
      content: "به من در دیباگ کردن این کد پایتون کمک کن.",
    },
  ],
  max_tokens: 2048,
});

console.log(completion.choices[0].message.content);

```

### Cohere

- **[Cohere Embed v4](fa/providers/cohere.md)** (`cohere.embed-v4:0`): یک مدل embedding پیشرفته که از متن، تصاویر و محتوای ترکیبی (از جمله PDF) پشتیبانی می‌کند. ایده‌آل برای جستجوی معنایی، تولید افزوده با بازیابی (RAG)، طبقه‌بندی اسناد و تطبیق شباهت. [مستندات مدل](fa/providers/cohere.md)

**ویژگی‌های کلیدی:**
- **پشتیبانی چندوجهی**: پردازش متن، تصاویر و اسناد ترکیبی متن/تصویر
- **ابعاد منعطف**: انتخاب از 256، 512، 1024 یا 1536 (پیش‌فرض) بعد خروجی
- **پنجره Context بزرگ**: 128k توکن برای پردازش اسناد گسترده
- **معیارهای شباهت متعدد**: پشتیبانی از Cosine Similarity، Dot Product Similarity و Euclidean Distance
- **پردازش PDF**: پشتیبانی بومی برای embedding اسناد PDF
- **پشتیبانی Endpoint**: در دسترس در v1/embeddings

### نمونه‌های API Embedding

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "cohere.embed-v4:0",
    "input": "هوش مصنوعی در حال تغییر نحوه کار و زندگی ماست.",
    "encoding_format": "float"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="cohere.embed-v4:0",
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
  model: "cohere.embed-v4:0",
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
  "model": "cohere.embed-v4:0",
  "usage": {
    "prompt_tokens": 12,
    "total_tokens": 12
  },
  "estimated_cost": {
    "unit": "0.0000120000",
    "irt": 1.38,
    "exchange_rate": 114600
  }
}
```

---

## موارد استفاده

### Claude Haiku 4.5
- **برنامه‌های بلادرنگ**: دستیارهای چت و خدمات مشتری با تاخیر کم
- **گردش‌کارهای کدنویسی**: برنامه‌نویسی جفتی، بررسی کد و نمونه‌سازی سریع
- **سیستم‌های ایجنتی**: هماهنگی چند-ایجنته با اجرای موازی وظایف
- **استفاده از کامپیوتر**: گردش‌کارهای خودکار که نیاز به تعامل با رابط‌های کامپیوتر دارند
- **برنامه‌های حساس به هزینه**: استقرارهای production که به هوش بالا در مقیاس نیاز دارند

### Cohere Embed v4
- **جستجوی معنایی**: ساخت سیستم‌های جستجوی هوشمند با درک زمینه‌ای
- **سیستم‌های RAG**: تقویت مدل‌های زبانی با بازیابی اسناد مرتبط
- **طبقه‌بندی اسناد**: دسته‌بندی و سازماندهی مجموعه‌های بزرگ اسناد
- **تطبیق شباهت**: یافتن محتوای مشابه در مجموعه‌داده‌های متن و تصویر
- **پردازش PDF**: استخراج و embedding اطلاعات از اسناد PDF

---

## لینک‌های مرتبط

- [مستندات مدل‌های Anthropic](fa/providers/anthropic.md)
- [مستندات مدل‌های Cohere](fa/providers/cohere.md)
- [راهنمای API Embeddings](fa/guides/retrieval.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md)
