# پشتیبانی از پلتفرم Nvidia NIM اضافه شد: مدل‌های Open Weight متمرکز بر تحقیق

**تاریخ:** 1404-09-01 / (2025-11-22)

## خلاصه

ما پشتیبانی از پلتفرم Nvidia NIM را اعلام می‌کنیم که دسترسی به مدل‌های open-weight بهینه‌شده برای تحقیق و ارزیابی را فراهم می‌کند. این مدل‌ها با قیمت‌گذاری مناسب برای تحقیق (1/10 نرخ‌های تولید) و محدودیت‌های نرخ طراحی‌شده برای استفاده آکادمیک و آزمایشی ارائه می‌شوند. پلتفرم شامل 20 مدل است که embedding، reranking، تولید متن و قابلیت‌های بینایی از ارائه‌دهندگانی مانند Meta، Google، Nvidia و Alibaba را پوشش می‌دهد.

---

## جزئیات

### پلتفرم Nvidia NIM

Nvidia NIM (Nvidia Inference Microservices) دسترسی به مدل‌های open-weight را فراهم می‌کند که برای محققان، دانشجویان و توسعه‌دهندگانی که قابلیت‌های AI را بررسی می‌کنند ایده‌آل هستند. این مدل‌ها در پلتفرم Nvidia به صورت رایگان با محدودیت‌های نرخ بسیار پایین ارائه می‌شوند، و ما دسترسی به آن‌ها را با قیمت‌گذاری مناسب برای تحقیق (تقریبا 1/10 نرخ مدل‌های تولید) فراهم می‌کنیم.

**نکته مهم:** این‌ها مدل‌های متمرکز بر تحقیق هستند، نه سرویس‌های عملیاتی. آن‌ها برای موارد زیر طراحی شده‌اند:
- تحقیقات آکادمیک و آزمایشی
- ارزیابی و معیارسنجی مدل
- اهداف آموزشی
- توسعه اثبات مفهوم (proof-of-concept)

برای بارهای کاری تولیدی، توصیه می‌کنیم از نسخه‌های production-grade موجود از سایر ارائه‌دهندگان استفاده کنید (مثلا Groq برای مدل‌های Llama).

### مدل‌های موجود

#### مدل‌های Embedding

**Embeddingهای مبتنی بر Llama:**
- **nvidia_nim.llama-3.2-nemoretriever-300m-embed-v1**: مدل embedding فشرده (300M پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.2-nemoretriever-300m-embed-v2**: مدل embedding فشرده به‌روزشده - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.2-nemoretriever-1b-vlm-embed-v1**: مدل embedding vision-language (1B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.2-nv-embedqa-1b-v2**: embeddings متمرکز بر پرسش و پاسخ - [مستندات](fa/providers/nvidianim.md)

**Embeddingهای عمومی:**
- **nvidia_nim.nv-embedqa-e5-v5**: معماری E5 برای وظایف پرسش و پاسخ - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.nv-embed-v1**: مدل embedding همه‌منظوره - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.bge-m3**: مدل embedding چندزبانه BAAI - [مستندات](fa/providers/nvidianim.md)

#### مدل‌های Reranking

- **nvidia_nim.llama-3.2-nemoretriever-500m-rerank-v2**: مدل reranking فشرده (500M پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.2-nv-rerankqa-1b-v2**: reranking متمرکز بر پرسش و پاسخ (1B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.nv-rerankqa-mistral-4b-v3**: reranking مبتنی بر Mistral (4B پارامتر) - [مستندات](fa/providers/nvidianim.md)

#### مدل‌های تولید متن

**مدل‌های تخصصی:**
- **nvidia_nim.nemotron-parse**: تجزیه و استخراج اسناد - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.nvidia-nemotron-nano-9b-v2**: مدل تولید فشرده (9B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.eurollm-9b-instruct**: مدل دستوری متمرکز بر اروپا - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.gemma-3-1b-it**: مدل دستوری فشرده Google - [مستندات](fa/providers/nvidianim.md)

**مدل‌های پیشرفته:**
- **nvidia_nim.gpt-oss-20b**: معماری GPT متن‌باز (20B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.gpt-oss-120b**: GPT بزرگ متن‌باز (120B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.qwen3-next-80b-a3b-thinking**: مدل استدلال Alibaba (80B پارامتر) - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-4-scout-17b-16e-instruct**: نسخه کارآمد Llama از Meta - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.1-nemotron-ultra-253b-v1**: مدل Nemotron فوق‌العاده بزرگ - [مستندات](fa/providers/nvidianim.md)
- **nvidia_nim.llama-3.3-nemotron-super-49b-v1.5**: نسخه بهینه‌شده Nemotron - [مستندات](fa/providers/nvidianim.md)

#### مدل‌های بینایی

- **nvidia_nim.nemotron-nano-12b-v2-vl**: مدل vision-language برای وظایف مالتی‌مودال - [مستندات](fa/providers/nvidianim.md)

### محدودیت‌های نرخ

تمام مدل‌های Nvidia NIM محدودیت‌های نرخ زیر را بر اساس سطح شما دارند:

| سطح | محدودیت نرخ |
|------|------------|
| پایه | 3 (فراخوانی / دقیقه) |
| سطح ۱ | 5 (فراخوانی / دقیقه) |
| سطح ۲ | 10 (فراخوانی / دقیقه) |
| سطح ۳ | 15 (فراخوانی / دقیقه) |
| سطح ۴ | 20 (فراخوانی / دقیقه) |
| سطح ۵ | 30 (فراخوانی / دقیقه) |

**توجه:** این محدودیت‌های نرخ برای تحقیق و آزمایش طراحی شده‌اند. برای بارهای کاری تولیدی که نیاز به توان عملیاتی بالاتر دارند، استفاده از معادل‌های production-grade از سایر ارائه‌دهندگان را در نظر بگیرید.

### مقایسه قیمت‌گذاری

مدل‌های Nvidia NIM با قیمت تقریبا 1/10 معادل‌های تولیدی ارائه می‌شوند. به عنوان مثال:

**قیمت‌گذاری تحقیق در مقابل تولید:**

| مدل | ارائه‌دهنده | ورودی ($/1M) | ورودی کش‌شده ($/1M) | خروجی ($/1M) |
|-------|----------|--------------|---------------------|---------------|
| llama-4-scout-17b-16e-instruct | Nvidia NIM (تحقیق) | $0.027 | $0.014 | $0.085 |
| llama-4-scout-17b-16e-instruct | Groq (تولید) | $0.11 | $0.055 | $0.34 |

این ساختار قیمت‌گذاری مدل‌های Nvidia NIM را برای تحقیق، ارزیابی و یادگیری مقرون‌به‌صرفه می‌کند.

### نمونه درخواست/پاسخ API

#### نمونه مدل Embedding

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "nvidia_nim.nv-embed-v1",
    "input": "پردازش زبان طبیعی به ماشین‌ها امکان درک زبان انسان را می‌دهد"
  }'
```

#### نمونه تولید متن

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "nvidia_nim.llama-3.3-nemotron-super-49b-v1.5",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت بین یادگیری با ناظر و بدون ناظر را توضیح دهید."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "your-avalai-api-key",
  "created": 1732262400,
  "model": "nvidia_nim.llama-3.3-nemotron-super-49b-v1.5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "یادگیری با ناظر از داده‌های برچسب‌دار استفاده می‌کند که مدل از جفت‌های ورودی-خروجی یاد می‌گیرد، مانند آموزش مدل برای تشخیص گربه با نشان دادن تصاویر برچسب‌دار شده به عنوان 'گربه' یا 'نه گربه'. یادگیری بدون ناظر با داده‌های بدون برچسب کار می‌کند و الگوها را به طور مستقل پیدا می‌کند، مانند گروه‌بندی مشتریان مشابه بدون دسته‌بندی‌های از پیش تعریف‌شده. تفاوت کلیدی این است که یادگیری با ناظر یک 'معلم' دارد که پاسخ‌های صحیح را ارائه می‌دهد، در حالی که یادگیری بدون ناظر ساختار را به تنهایی کشف می‌کند.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 85,
    "prompt_tokens": 18,
    "total_tokens": 103,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 18,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000273000",
    "irt": 3.13,
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
    "model": "nvidia_nim.nvidia-nemotron-nano-9b-v2",
    "messages": [
      {
        "role": "user",
        "content": "کاربردهای transformers در NLP چیست؟"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="nvidia_nim.nvidia-nemotron-nano-9b-v2",
    messages=[
        {
            "role": "user",
            "content": "کاربردهای transformers در NLP چیست؟",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "nvidia_nim.nvidia-nemotron-nano-9b-v2",
  messages: [
    {
      role: "user",
      content: "کاربردهای transformers در NLP چیست؟",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### نمونه Reranking

```language-selector
bash=:curl https://api.avalai.ir/v1/rerank \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "nvidia_nim.nv-rerankqa-mistral-4b-v3",
    "query": "یادگیری ماشین چیست؟",
    "documents": [
      "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
      "Python یک زبان برنامه‌نویسی محبوب است.",
      "یادگیری عمیق از شبکه‌های عصبی با چندین لایه استفاده می‌کند."
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# توجه: استفاده از requests برای endpoint rerank
import requests

response = requests.post(
    "https://api.avalai.ir/v1/rerank",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "nvidia_nim.nv-rerankqa-mistral-4b-v3",
        "query": "یادگیری ماشین چیست؟",
        "documents": [
            "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
            "Python یک زبان برنامه‌نویسی محبوب است.",
            "یادگیری عمیق از شبکه‌های عصبی با چندین لایه استفاده می‌کند.",
        ],
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
        model: "nvidia_nim.nv-rerankqa-mistral-4b-v3",
        query: "یادگیری ماشین چیست؟",
        documents: [
            "یادگیری ماشین زیرمجموعه‌ای از هوش مصنوعی است.",
            "Python یک زبان برنامه‌نویسی محبوب است.",
            "یادگیری عمیق از شبکه‌های عصبی با چندین لایه استفاده می‌کند."
        ]
    })
});

const result = await response.json();
console.log(result);

```

### موارد استفاده

**تحقیق و آکادمیک:**
- معیارسنجی عملکرد مدل در معماری‌های مختلف
- پروژه‌های آموزشی و درسی
- توسعه و آزمایش الگوریتم
- بازتولید و اعتبارسنجی مقالات

**توسعه و نمونه‌سازی:**
- توسعه اثبات مفهوم
- بررسی ویژگی‌ها قبل از استقرار تولید
- ارزیابی مدل مقرون‌به‌صرفه
- تست یکپارچه‌سازی

**توصیه نمی‌شود برای:**
- برنامه‌های تولیدی که نیاز به در دسترس بودن بالا دارند
- سرویس‌ها با ترافیک کاربر قابل توجه
- برنامه‌های حیاتی
- سیستم‌های زمان واقعی که نیاز به تاخیر کم در مقیاس دارند

---

## لینک‌های مرتبط

- [مستندات مدل‌های Nvidia NIM](fa/providers/nvidianim.md)
- [مرجع API: Chat Completions](fa/api-reference/messages.md)
- [مرجع API: Embeddings](fa/api-reference/embeddings.md)
- [مرجع API: Rerank](fa/api-reference/rerank.md)
- [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [قیمت‌گذاری](fa/pricing.md)