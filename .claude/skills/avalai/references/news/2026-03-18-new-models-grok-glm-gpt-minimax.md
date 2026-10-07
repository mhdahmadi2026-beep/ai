# News 2026-03-18-new-models-grok-glm-gpt-minimax: استفاده از Grok 4.20 Beta
URL: `https://docs.avalai.ir/fa/news/2026-03-18-new-models-grok-glm-gpt-minimax`
**تاریخ:** ۱۴۰۴-۱۲-۲۷ / (2026-03-18)

# مدل‌های جدید اضافه شدند: Grok 4.20 Beta، GLM-5-Turbo، GPT-5.4 Mini/Nano و MiniMax M2.7

**تاریخ:** ۱۴۰۴-۱۲-۲۷ / (2026-03-18)

## خلاصه

ما افزودن هفت مدل جدید را اعلام می‌کنیم: Grok 4.20 Beta از X.AI (نسخه‌های استدلالی و غیراستدلالی) با سرعت پیشرو در صنعت و پنجره زمینه ۲ میلیون توکن، GLM-5-Turbo از Z.AI بهینه‌سازی شده برای سناریوهای عاملی OpenClaw، GPT-5.4 Mini و Nano از OpenAI برای کارهای حجم بالا با هزینه کارآمد، و M2.7 از MiniMax با قابلیت‌های خودتکاملی و عملکرد SOTA در کدنویسی.


## خلاصه قیمت‌گذاری

| مدل | ورودی (دلار/۱م توکن) | ورودی کش شده (دلار/۱م توکن) | خروجی (دلار/۱م توکن) |
|-----|----------------------|----------------------------|----------------------|
| `grok-4.20-beta-0309-reasoning` | $2.00 | $0.20 | $6.00 |
| `grok-4.20-beta-0309-non-reasoning` | $2.00 | $0.20 | $6.00 |
| `glm-5-turbo` | $1.32 | $0.264 | $4.40 |
| `gpt-5.4-mini` | $0.75 | $0.075 | $4.50 |
| `gpt-5.4-nano` | $0.20 | $0.02 | $1.25 |
| `minimax-m2.7` | $0.30 | $0.06 | $1.20 |
| `minimax-m2.7-highspeed` | $0.60 | $0.06 | $2.40 |

---

## نمونه درخواست و پاسخ API

### نمونه Grok 4.20 Beta Reasoning

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.20-beta-0309-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "یک استراتژی بازاریابی دیجیتال جامع برای یک استارتاپ فناوری طراحی کنید."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه GLM-5-Turbo با حالت تفکر

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "به عنوان یک متخصص بازاریابی، یک شعار جذاب برای پلتفرم باز Z.AI ایجاد کنید."
      }
    ],
    "thinking": {
      "type": "enabled"
    },
    "max_tokens": 4096,
    "temperature": 1.0
  }'
```

### نمونه GPT-5.4 Mini

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.4-mini",
    "messages": [
      {
        "role": "user",
        "content": "یک کلاینت API با محدودیت نرخ در پایتون با بازگشت نمایی پیاده‌سازی کنید."
      }
    ],
    "max_tokens": 4096
  }'
```

### نمونه GPT-5.4 Nano

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.4-nano",
    "messages": [
      {
        "role": "user",
        "content": "متن زیر را به عنوان مثبت، منفی یا خنثی طبقه‌بندی کنید: 'محصول خوب کار می‌کند اما ارسال کند بود.'"
      }
    ]
  }'
```

### نمونه MiniMax M2.7

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.7",
    "messages": [
      {
        "role": "user",
        "content": "یک هارنس عامل تحقیقاتی بسازید که بتواند خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی را مدیریت کند."
      }
    ],
    "max_tokens": 8192
  }'
```

---

## نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.4-mini",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت‌های کلیدی بین معماری میکروسرویس و مونولیتیک را توضیح دهید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از GPT-5.4 Mini
response = client.chat.completions.create(
    model="gpt-5.4-mini",
    messages=[
        {
            "role": "user",
            "content": "تفاوت‌های کلیدی بین معماری میکروسرویس و مونولیتیک را توضیح دهید.",
        }
    ],
)

print(response.choices[0].message.content)

# استفاده از Grok 4.20 Beta
response = client.chat.completions.create(
    model="grok-4.20-beta-0309-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک معماری سیستم توزیع‌شده با تحمل خطا طراحی کنید.",
        }
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از GPT-5.4 Mini
const response = await client.chat.completions.create({
  model: "gpt-5.4-mini",
  messages: [
    {
      role: "user",
      content: "تفاوت‌های کلیدی بین معماری میکروسرویس و مونولیتیک را توضیح دهید.",
    },
  ],
});

console.log(response.choices[0].message.content);

// استفاده از MiniMax M2.7
const m2Response = await client.chat.completions.create({
  model: "minimax-m2.7",
  messages: [
    {
      role: "user",
      content: "یک عامل بسازید که بتواند به طور خودمختار آزمایش‌های ML را مدیریت کند.",
    },
  ],
  max_tokens: 8192,
});

console.log(m2Response.choices[0].message.content);

```

---

## لینک‌های مستندات

- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [مستندات مدل‌های Z.AI](fa/providers/zai.md)
- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های MiniMax](fa/providers/minimax.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
