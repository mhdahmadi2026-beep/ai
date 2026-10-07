# مدل جدید اضافه شد: Claude Opus 4.5

**تاریخ:** 1404-09-04 / (2025-11-25)

## خلاصه

مدل Claude Opus 4.5 از شرکت Anthropic اکنون در AvalAI در دسترس است. این مدل عملکرد پیشرفته‌ای در کدنویسی، عامل‌های هوش مصنوعی و استفاده از رایانه ارائه می‌دهد، با بهبود قابل توجه کارایی و کاهش 80 درصدی قیمت نسبت به مدل‌های قبلی Opus. این مدل با استفاده از توکن‌های بسیار کمتر، نتایج بهتری در معیارهای کدنویسی و وظایف استدلال پیچیده به دست می‌آورد.

---

## جزئیات

### Anthropic

ما دسترسی به **Claude Opus 4.5** (‍‍‍‍`claude-opus-4-5`)، جدیدترین و قدرتمندترین مدل Anthropic را اعلام می‌کنیم. این نسخه پیشرفت قابل توجهی در قابلیت‌های هوش مصنوعی برای مهندسی نرم‌افزار، جریان‌های کاری عاملی و حل مسائل پیچیده را نشان می‌دهد. [مستندات](fa/models/claude-opus-4.md)

**ویژگی‌های کلیدی:**

- **کدنویسی پیشرفته**: رهبری در SWE-bench Verified و دستیابی به عملکرد برتر در 7 از 8 زبان برنامه‌نویسی در SWE-bench Multilingual
- **کارایی بهبود یافته**: استفاده از 48-76 درصد توکن کمتر نسبت به مدل‌های قبلی با حفظ یا بهبود عملکرد
- **قابلیت‌های عاملی پیشرفته**: عملکرد عالی در وظایف خودگردان طولانی‌مدت با استدلال پایدار و اجرای چند مرحله‌ای
- **امنیت بهبود یافته**: مقاوم‌ترین مدل هم‌راستا شده از Anthropic با مقاومت برتر در برابر حملات تزریق پرامپت
- **کنترل تلاش**: پارامتر تلاش جدید به توسعه‌دهندگان اجازه می‌دهد برای سرعت/هزینه یا حداکثر قابلیت بهینه‌سازی کنند
- **پنجره متنی**: 200K توکن برای مدیریت مکالمات و اسناد گسترده
- **پشتیبانی نقاط پایانی**: در دسترس در v1/chat/completions (پشتیبانی کامل)، v1/messages (پشتیبانی کامل) و v1/responses (پشتیبانی جزئی)
- **قیمت‌گذاری**: 5/25 دلار به ازای هر میلیون توکن (کاهش 80 درصدی نسبت به قیمت‌گذاری قبلی Opus)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| claude-opus-4-5 | 5.00 دلار/1M توکن | 1.50 دلار/1M توکن | 25.00 دلار/1M توکن |

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست (v1/chat/completions)

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5", # دسترسی در سطح کاربری ۱ و بالاتر
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون بنویس که به طور کارآمد اعداد اول را با استفاده از الگوریتم غربال اراتوستن پیدا کند."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1732532400,
  "model": "claude-opus-4-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا یک پیاده‌سازی کارآمد از غربال اراتوستن آورده شده است:\n\n
```python\ndef sieve_of_eratosthenes(limit):\n    \"\"\"Find all prime numbers up to limit using Sieve of Eratosthenes.\"\"\"\n    if limit < 2:\n        return []\n    \n    # Initialize boolean array\n    is_prime = [True] * (limit + 1)\n    is_prime[0] = is_prime[1] = False\n    \n    # Sieve process\n    for i in range(2, int(limit**0.5) + 1):\n        if is_prime[i]:\n            # Mark multiples as composite\n            for j in range(i*i, limit + 1, i):\n                is_prime[j] = False\n    \n    # Return list of primes\n    return [num for num in range(limit + 1) if is_prime[num]]\n```\n\nاین پیاده‌سازی دارای پیچیدگی زمانی O(n log log n) و پیچیدگی فضایی O(n) است.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 245,
    "prompt_tokens": 28,
    "total_tokens": 273,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0062650000",
    "irt": 717.85,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست (v1/messages - فرمت بومی Anthropic)
```bash
curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -d '{
    "model": "claude-opus-4-5", # دسترسی در سطح کاربری ۱ و بالاتر
    "max_tokens": 1024,
    "messages": [
      {
        "role": "user",
        "content": "مفهوم تزریق پیش‌نیاز در طراحی نرم‌افزار را توضیح بده."
      }
    ]
  }'
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5",
    "messages": [
      {
        "role": "user",
        "content": "به من کمک کن این کد را دیباگ کنم و پیشنهادات بهبود بده."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-AvalAI-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="claude-opus-4-5",
    messages=[
        {
            "role": "user",
            "content": "به من کمک کن این کد را دیباگ کنم و پیشنهادات بهبود بده.",
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
  model: "claude-opus-4-5",
  messages: [
    {
      role: "user",
      content: "به من کمک کن این کد را دیباگ کنم و پیشنهادات بهبود بده.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### ویژگی‌های پیشرفته

#### نمونه فراخوانی تابع (Function Calling)

Claude Opus 4.5 در فراخوانی تابع با دقت بهبود یافته و خطاهای کمتر عملکرد عالی دارد:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوای فعلی سانفرانسیسکو چطور است و آیا باید چتر همراه ببرم؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"],
                "description": "واحد دما"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

python=:tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    },
                    "unit": {
                        "type": "string",
                        "enum": ["celsius", "fahrenheit"],
                        "description": "واحد دما",
                    },
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="claude-opus-4-5",
    messages=[
        {
            "role": "user",
            "content": "آب و هوای فعلی سانفرانسیسکو چطور است و آیا باید چتر همراه ببرم؟",
        }
    ],
    tools=tools,
    tool_choice="auto",
)

javascript=:const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات آب و هوای فعلی برای یک مکان",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر",
                    },
                    unit: {
                        type: "string",
                        enum: ["celsius", "fahrenheit"],
                        description: "واحد دما",
                    }
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "claude-opus-4-5",
    messages: [{role: "user", content: "آب و هوای فعلی سانفرانسیسکو چطور است و آیا باید چتر همراه ببرم؟"}],
    tools: tools,
    tool_choice: "auto",
});

```

#### نمونه استدلال پیچیده

برای وظایف که نیاز به تحلیل عمیق و استدلال چند مرحله‌ای دارند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-4-5",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک که روزانه 1 میلیون تراکنش را مدیریت می‌کند طراحی کن. شاردینگ پایگاه داده، استراتژی‌های کش و تحمل خطا را در نظر بگیر."
      }
    ],
    "max_tokens": 4096
  }'

python=:response = client.chat.completions.create(
    model="claude-opus-4-5",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک که روزانه 1 میلیون تراکنش را مدیریت می‌کند طراحی کن. شاردینگ پایگاه داده، استراتژی‌های کش و تحمل خطا را در نظر بگیر.",
        }
    ],
    max_tokens=4096,
)

# Claude Opus 4.5 برنامه‌ریزی معماری دقیق با ملاحظات عملی ارائه می‌دهد
print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
    model: "claude-opus-4-5",
    messages: [
        {
            role: "user",
            content: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک که روزانه 1 میلیون تراکنش را مدیریت می‌کند طراحی کن. شاردینگ پایگاه داده، استراتژی‌های کش و تحمل خطا را در نظر بگیر.",
        },
    ],
    max_tokens: 4096,
});

// Claude Opus 4.5 برنامه‌ریزی معماری دقیق با ملاحظات عملی ارائه می‌دهد
console.log(response.choices[0].message.content);

```

### موارد استفاده

Claude Opus 4.5 به ویژه برای موارد زیر مناسب است:

- **مهندسی نرم‌افزار**: تولید کد، بازسازی، دیباگ و بررسی کد
- **جریان‌های کاری عاملی**: وظایف خودگردان طولانی‌مدت با اجرای چند مرحله‌ای
- **استفاده از رایانه**: اتوماسیون صفحه‌گسترده، مدیریت وظایف مرورگر و عملیات دسکتاپ
- **حل مسائل پیچیده**: طراحی معماری، برنامه‌ریزی سیستم و تحلیل استراتژیک
- **پردازش اسناد**: تحلیل اسناد گسترده با پنجره متنی 200K توکن
- **وظایف تحقیقاتی**: تحلیل عمیق که نیاز به استدلال پایدار در چندین مرحله دارد

---

## لینک‌های مرتبط

- [مستندات مدل Claude Opus 4](fa/models/claude-opus-4.md)
- [نمای کلی مدل‌های Anthropic](fa/providers/anthropic.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/pricing.md)
- [بهترین شیوه‌های مهندسی پرامپت](fa/guides/prompt-engineering.md)
