# News 2026-04-25-gpt-5-5-model-added: مدل پرچمدار جدید اضافه شد: GPT-5.5
URL: `https://docs.avalai.ir/fa/news/2026-04-25-gpt-5-5-model-added`
**تاریخ:** ۱۴۰۵-۰۲-۰۵ / (2026-04-25)

# مدل پرچمدار جدید اضافه شد: GPT-5.5

**تاریخ:** ۱۴۰۵-۰۲-۰۵ / (2026-04-25)

## خلاصه

جدیدترین مدل پرچمدار OpenAI یعنی **GPT-5.5** اکنون در AvalAI از طریق هر دو Responses API (`v1/responses`) و Chat Completions API (`v1/chat/completions`) در دسترس است. GPT-5.5 عملکردی در سطح جدیدترین فناوری در کدنویسی عاملی، کار دانشی، استفاده از کامپیوتر و تحقیقات علمی ارائه می‌دهد، در حالی که تأخیر به ازای هر توکن را در سطح قابل مقایسه با GPT-5.4 حفظ می‌کند.


### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست Chat Completions

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {
        "role": "user",
        "content": "این تابع پایتون را به نسخه async اصطلاحی بازنویسی کن و مزایا و معایب را توضیح بده."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc789",
  "created": 1777881600,
  "model": "gpt-5.5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا بازنویسی async اصطلاحی با استفاده از asyncio.gather برای I/O همزمان، همراه با مدیریت صریح لغو و توضیح مختصر مزایا و معایب در مقایسه با نسخه همزمان ارائه شده است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 412,
    "prompt_tokens": 28,
    "total_tokens": 440,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 28,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0124000000",
    "irt": 1420.8,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست Responses API

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "input": "این گزارش مالی فصلی را تحلیل کن و سه عامل ریسک مهم را همراه با شواهد پشتیبان استخراج کن.",
    "reasoning": {
      "effort": "high"
    }
  }'
```

---

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {
        "role": "user",
        "content": "یک محدودکننده نرخ توزیع‌شده طراحی کن که در برابر خرابی بخشی از نودها مقاوم باشد."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5.5",
    messages=[
        {
            "role": "user",
            "content": "یک محدودکننده نرخ توزیع‌شده طراحی کن که در برابر خرابی بخشی از نودها مقاوم باشد.",
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
  model: "gpt-5.5",
  messages: [
    {
      role: "user",
      content: "یک محدودکننده نرخ توزیع‌شده طراحی کن که در برابر خرابی بخشی از نودها مقاوم باشد.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

### ویژگی‌های پیشرفته

#### کنترل تلاش استدلال

GPT-5.5 از تلاش استدلال قابل تنظیم پشتیبانی می‌کند تا بتوانید به ازای هر درخواست، میان تأخیر و عمق پاسخ تعادل برقرار کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "input": "مرحله به مرحله اثبات کن که مجموع دو عدد صحیح فرد، زوج است.",
    "reasoning": {
      "effort": "high"
    }
  }'

python=:response = client.responses.create(
    model="gpt-5.5",
    input="مرحله به مرحله اثبات کن که مجموع دو عدد صحیح فرد، زوج است.",
    reasoning={"effort": "high"},
)

print(response.output)

javascript=:const response = await client.responses.create({
    model: "gpt-5.5",
    input: "مرحله به مرحله اثبات کن که مجموع دو عدد صحیح فرد، زوج است.",
    reasoning: { effort: "high" },
});

console.log(response.output);

```

#### فراخوانی تابع

GPT-5.5 استفاده از ابزار را قوی‌تر کرده است، مدت زمان طولانی‌تری روی وظیفه متمرکز می‌ماند و در گردش‌های کاری عاملی، ابزارها را مطمئن‌تر انتخاب می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.5",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوای توکیو چطور است و آیا باید ژاکت همراه ببرم؟"
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
    model="gpt-5.5",
    messages=[
        {
            "role": "user",
            "content": "آب و هوای توکیو چطور است و آیا باید ژاکت همراه ببرم؟",
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
    model: "gpt-5.5",
    messages: [{role: "user", content: "آب و هوای توکیو چطور است و آیا باید ژاکت همراه ببرم؟"}],
    tools: tools,
    tool_choice: "auto",
});

```

---

### نکات برجسته معیارها

GPT-5.5 به نتایج جدیدی در سطح جدیدترین فناوری در کدنویسی، کار دانشی و استفاده از ابزار رسیده است:

| معیار | GPT-5.5 | GPT-5.4 |
|-----------|---------|---------|
| Terminal-Bench 2.0 | **۸۲.۷٪** | ۷۵.۱٪ |
| Expert-SWE (داخلی) | **۷۳.۱٪** | ۶۸.۵٪ |
| GDPval (برد یا تساوی) | **۸۴.۹٪** | ۸۳.۰٪ |
| OSWorld-Verified | **۷۸.۷٪** | ۷۵.۰٪ |
| Tau2-bench Telecom | **۹۸.۰٪** | ۹۲.۸٪ |
| Toolathlon | **۵۵.۶٪** | ۵۴.۶٪ |
| BrowseComp | **۸۴.۴٪** | ۸۲.۷٪ |
| FrontierMath Tier 1–3 | **۵۱.۷٪** | ۴۷.۶٪ |
| FrontierMath Tier 4 | **۳۵.۴٪** | ۲۷.۱٪ |
| CyberGym | **۸۱.۸٪** | ۷۹.۰٪ |
| ARC-AGI-2 (Verified) | **۸۵.۰٪** | ۷۳.۳٪ |

GPT-5.5 همچنین بازیابی زمینه طولانی قدرتمندی ارائه می‌دهد و در OpenAI MRCR v2 (8-needle، ۵۱۲K–۱M) امتیاز ۷۴.۰٪ کسب کرده، در مقابل ۳۶.۶٪ برای GPT-5.4.

---

### موارد استفاده

GPT-5.5 به ویژه برای موارد زیر مناسب است:

- **کدنویسی عاملی**: وظایف مهندسی خودگردان طولانی‌مدت، بازسازی چندفایلی، دیباگ در کدبیس‌های بزرگ
- **کار دانشی**: مدل‌سازی صفحه‌گسترده، تحقیق عملیاتی، تولید اسناد و اسلاید
- **استفاده از کامپیوتر**: کار با نرم‌افزار، پیمایش رابط‌های کاربری و هماهنگی میان ابزارها
- **تحقیقات علمی**: بیوانفورماتیک، زیست‌شناسی کمی، ریاضیات و تحلیل داده چندمرحله‌ای
- **تحلیل مالی و حقوقی**: خلاصه‌سازی گزارش، امتیازدهی ریسک، بررسی قرارداد
- **وظایف زمینه طولانی**: تحلیل اسناد و استدلال روی کدبیس با پنجره ورودی ۱ میلیون توکن

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [مرجع Responses API](fa/api-reference/responses.md)
