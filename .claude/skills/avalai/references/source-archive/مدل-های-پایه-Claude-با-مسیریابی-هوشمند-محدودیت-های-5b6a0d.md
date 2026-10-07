# مدل‌های پایه Claude با مسیریابی هوشمند: محدودیت‌های نرخ بالاتر

**تاریخ:** 1404-09-07 / (2025-11-28)

## خلاصه

AvalAI فضای نام مدل‌های پایه Claude را با مسیریابی هوشمند در تمام ارائه‌دهندگان رسمی ابری Anthropic معرفی می‌کند. کاربران اکنون می‌توانند از طریق نام‌های ساده‌شده مدل (`claude-opus-4-5`، `claude-sonnet-4-5`، `claude-opus-4-1`، `claude-haiku-4-5`) به مدل‌های Claude دسترسی داشته باشند و به لطف توزیع هوشمند بار در Anthropic (Claude.ai)، AWS Bedrock، Google Cloud Platform و Microsoft Azure از محدودیت‌های نرخ بسیار بالاتری بهره‌مند شوند.

---

## جزئیات

### مسیریابی هوشمند برای مدل‌های Claude

ما دسترسی به فضای نام مدل‌های پایه Claude با قابلیت‌های مسیریابی هوشمند را اعلام می‌کنیم. این ویژگی به طور خودکار درخواست‌های API را در تمام ارائه‌دهندگان رسمی ابری Anthropic توزیع می‌کند و توان عملیاتی و محدودیت‌های نرخ بسیار بالاتری نسبت به دسترسی تک‌ارائه‌دهنده ارائه می‌دهد.

**ارائه‌دهندگان پشتیبانی شده:**

1. **Anthropic (Claude.ai)** - API مستقیم Anthropic
2. **AWS Bedrock** - سرویس‌های وب آمازون
3. **Google Cloud Platform (GCP)** - Vertex AI
4. **Microsoft Azure** - Azure AI

### نام‌های جدید مدل پایه

فضاهای نام مدل پایه زیر اکنون در دسترس هستند:

| مدل پایه | شناسه مدل AWS Bedrock | پنجره متنی |
|------------|---------------------|----------------|
| `claude-opus-4-5` | `anthropic.claude-opus-4-5-20251101-v1:0` | 200K توکن |
| `claude-sonnet-4-5` | `anthropic.claude-sonnet-4-5-20250929-v1:0` | 200K توکن |
| `claude-opus-4-1` | `anthropic.claude-opus-4-1-20250805-v1:0` | 200K توکن |
| `claude-haiku-4-5` | `anthropic.claude-haiku-4-5-20251001-v1:0` | 200K توکن |

### بهبود محدودیت‌های نرخ

مسیریابی هوشمند با توزیع بار در چندین ارائه‌دهنده ابری، محدودیت‌های نرخ بسیار بالاتری را امکان‌پذیر می‌کند. در اینجا مقایسه‌ای برای حساب‌های سطح 1 آورده شده است:

**مقایسه محدودیت‌های نرخ سطح 1:**

| مدل | فضای نام | درخواست/دقیقه | توکن/دقیقه |
|-------|-----------|--------------|------------|
| Claude Opus 4.5 | `anthropic.claude-opus-4-5-20251101-v1:0` (Bedrock) | 1 | 40,000 |
| Claude Opus 4.5 | `claude-opus-4-5` (پایه) | **10** | 30,000 |
| Claude Sonnet 4.5 | `anthropic.claude-sonnet-4-5-20250929-v1:0` (Bedrock) | 2 | 200,000 |
| Claude Sonnet 4.5 | `claude-sonnet-4-5` (پایه) | **25** | 30,000 |
| Claude Opus 4.1 | `anthropic.claude-opus-4-1-20250805-v1:0` (Bedrock) | 1 | 200,000 |
| Claude Opus 4.1 | `claude-opus-4-1` (پایه) | **5** | 30,000 |
| Claude Haiku 4.5 | `anthropic.claude-haiku-4-5-20251001-v1:0` (Bedrock) | 25 | 80,000 |
| Claude Haiku 4.5 | `claude-haiku-4-5` (پایه) | 25 | 50,000 |

**محدودیت‌های نرخ سطح 5 (سازمانی):**

| مدل پایه | درخواست/دقیقه | توکن/دقیقه |
|------------|--------------|------------|
| `claude-opus-4-5` | 1,500 | 4,000,000 |
| `claude-sonnet-4-5` | 1,500 | 4,000,000 |
| `claude-opus-4-1` | 1,500 | 4,000,000 |
| `claude-haiku-4-5` | 1,500 | 8,000,000 |

### قیمت‌گذاری

قیمت‌گذاری مدل پایه همانند قیمت‌گذاری اصلی مدل AWS Bedrock باقی می‌ماند:

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| `claude-opus-4-5` | 5.00 دلار/1M توکن | 1.50 دلار/1M توکن | 25.00 دلار/1M توکن |
| `claude-sonnet-4-5` | 3.00 دلار/1M توکن | 1.50 دلار/1M توکن | 15.00 دلار/1M توکن |
| `claude-opus-4-1` | 15.00 دلار/1M توکن | 7.50 دلار/1M توکن | 75.00 دلار/1M توکن |
| `claude-haiku-4-5` | 1.00 دلار/1M توکن | 0.50 دلار/1M توکن | 5.00 دلار/1M توکن |

### راهنمای مهاجرت

مهاجرت به فضاهای نام مدل پایه ساده است - فقط نام مدل را در فراخوانی‌های API خود به‌روزرسانی کنید:

**قبل (فضای نام AWS Bedrock):**
```python
model = "anthropic.claude-opus-4-5-20251101-v1:0"
```

**بعد (فضای نام مدل پایه):**
```python
model = "claude-opus-4-5"
```

هیچ تغییر کد دیگری لازم نیست. رابط API، فرمت پاسخ و تمام قابلیت‌ها یکسان باقی می‌مانند.

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5",
    "messages": [
      {
        "role": "user",
        "content": "مزایای معماری چند ابری برای بارهای کاری هوش مصنوعی را توضیح بده."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1732789200,
  "model": "claude-opus-4-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "معماری چند ابری برای بارهای کاری هوش مصنوعی چندین مزیت کلیدی ارائه می‌دهد:\n\n1. **دسترسی‌پذیری بالا**: توزیع بارهای کاری در چندین ارائه‌دهنده ابری افزونگی را تضمین می‌کند و زمان خرابی را به حداقل می‌رساند.\n\n2. **بهینه‌سازی محدودیت نرخ**: با مسیریابی درخواست‌ها به چندین ارائه‌دهنده، می‌توانید توان عملیاتی مجموع بالاتری نسبت به آنچه هر ارائه‌دهنده به تنهایی ارائه می‌دهد، به دست آورید.\n\n3. **بهینه‌سازی هزینه**: ارائه‌دهندگان مختلف ممکن است قیمت‌گذاری بهتری برای مناطق یا الگوهای استفاده خاص ارائه دهند.\n\n4. **استقلال از فروشنده**: اجتناب از پیش‌نیاز به یک ارائه‌دهنده واحد، انعطاف‌پذیری و قدرت مذاکره را افزایش می‌دهد.\n\n5. **پوشش جغرافیایی**: دسترسی به مراکز داده در مناطق مختلف، تاخیر را برای برنامه‌های جهانی بهبود می‌بخشد.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 150,
    "prompt_tokens": 18,
    "total_tokens": 168,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 18,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0038400000",
    "irt": 440.06,
    "exchange_rate": 114600
  }
}
```

### نمونه‌های استفاده از SDK

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای جستجوی دودویی بنویس."
      }
    ]
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از فضای نام مدل پایه برای مسیریابی هوشمند
completion = client.chat.completions.create(
    model="claude-opus-4-5",  # مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای جستجوی دودویی بنویس.",
        }
    ],
)

print(completion.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از فضای نام مدل پایه برای مسیریابی هوشمند
const completion = await client.chat.completions.create({
  model: "claude-opus-4-5",  // مسیریابی هوشمند در تمام ارائه‌دهندگان Anthropic
  messages: [
    {
      role: "user",
      content: "یک تابع پایتون برای جستجوی دودویی بنویس.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```


### استفاده از SDK Anthropic

فضاهای نام مدل پایه با SDK رسمی Anthropic نیز پشتیبانی می‌شوند:

```bash
curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-5",
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "مسیریابی هوشمند در معماری ابری را توضیح بده."
      }
    ]
  }'

```

```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key", base_url="https://api.avalai.ir"
)

message = client.messages.create(
    model="claude-opus-4-5",  # مسیریابی هوشمند فعال
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": "مسیریابی هوشمند در معماری ابری را توضیح بده.",
        }
    ],
)

print(message.content[0].text)

```

```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const message = await client.messages.create({
  model: "claude-opus-4-5",  // مسیریابی هوشمند فعال
  max_tokens: 1024,
  messages: [
    {
      role: "user",
      content: "مسیریابی هوشمند در معماری ابری را توضیح بده.",
    },
  ],
});

console.log(message.content[0].text);

```


### سازگاری پس‌رو

فضاهای نام مدل AWS Bedrock همچنان به طور کامل پشتیبانی می‌شوند. اگر دسترسی مستقیم به Bedrock را ترجیح می‌دهید، می‌توانید به استفاده از شناسه‌های کامل مدل ادامه دهید:

- `anthropic.claude-opus-4-5-20251101-v1:0`
- `anthropic.claude-sonnet-4-5-20250929-v1:0`
- `anthropic.claude-opus-4-1-20250805-v1:0`
- `anthropic.claude-haiku-4-5-20251001-v1:0`

با این حال، توصیه می‌کنیم به فضاهای نام مدل پایه مهاجرت کنید تا از محدودیت‌های نرخ بالاتر و دسترسی‌پذیری بهبود یافته از طریق مسیریابی هوشمند بهره‌مند شوید.

---

## لینک‌های مرتبط

- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [مستندات محدودیت‌های نرخ](fa/rate-limits.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [بهترین شیوه‌های تولید](fa/guides/production-best-practices.md)
