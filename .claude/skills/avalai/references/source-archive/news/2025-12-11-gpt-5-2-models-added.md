# مدل‌های جدید اضافه شد: GPT-5.2 و GPT-5.2 Pro

**تاریخ:** 1404-09-20 / (2025-12-11)

## خلاصه

جدیدترین مدل‌های پرچمدار OpenAI یعنی GPT-5.2 و GPT-5.2 Pro اکنون در AvalAI در دسترس هستند. GPT-5.2 برای وظایف کدنویسی و عاملی در صنایع مختلف طراحی شده و دارای بهبود در هوش عمومی، پیروی از دستورالعمل‌ها و قابلیت‌های چندوجهی است. GPT-5.2 Pro پاسخ‌های هوشمندتر و دقیق‌تری برای وظایف حرفه‌ای پیچیده ارائه می‌دهد و رکوردهای جدیدی در معیارهای کار دانشی، کدنویسی، علم و ریاضیات ثبت کرده است.

---

## جزئیات

### OpenAI

ما دسترسی به **GPT-5.2** (`gpt-5.2`) و **GPT-5.2 Pro** (`gpt-5.2-pro`)، پیشرفته‌ترین مدل‌های OpenAI برای کار دانشی حرفه‌ای و عامل‌های بلندمدت را اعلام می‌کنیم. [مستندات](fa/providers/openai.md)

#### GPT-5.2

GPT-5.2 بهترین مدل چندمنظوره OpenAI است که برای وظایف کدنویسی و عاملی در صنایع مختلف بهینه‌سازی شده است.

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 400,000 توکن ورودی، 128,000 حداکثر توکن خروجی
- **تاریخ دانش**: 31 اوت 2025
- **ورودی/خروجی**: پشتیبانی از ورودی و خروجی متن و تصویر
- **استدلال پیشرفته**: تلاش استدلال قابل تنظیم (none، low، medium، high، xhigh)
- **قابلیت‌های بهبود یافته**: هوش عمومی، پیروی از دستورالعمل، دقت، کارایی توکن، چندوجهی، بینایی، تولید کد، فراخوانی ابزار، مدیریت زمینه
- **پشتیبانی نقطه پایانی**: در دسترس در v1/chat/completions، v1/responses و موارد دیگر

#### GPT-5.2 Pro

GPT-5.2 Pro توانمندترین نسخه GPT-5.2 است که پاسخ‌های هوشمندتر و دقیق‌تری برای مسائل دشوار تولید می‌کند.

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 400,000 توکن ورودی، 128,000 حداکثر توکن خروجی
- **تاریخ دانش**: 31 اوت 2025
- **ورودی/خروجی**: ورودی متن و تصویر، خروجی متن
- **تفکر گسترده**: تلاش استدلال پشتیبانی از medium، high، xhigh
- **دسترسی API**: فقط Responses API (v1/responses)
- **عملکرد**: رکورد جدید در GDPval (74.1%)، GPQA Diamond (93.2%)، ARC-AGI-1 Verified (90.5%)

**توجه:** GPT-5.2 Pro برای مسائل دشوار طراحی شده و برخی درخواست‌ها ممکن است چندین دقیقه طول بکشد. از حالت پس‌زمینه برای جلوگیری از وقفه زمانی استفاده کنید.

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5.2 | 1.75 دلار/1M توکن | 0.175 دلار/1M توکن | 14.00 دلار/1M توکن |
| gpt-5.2-pro | 21.00 دلار/1M توکن | - | 168.00 دلار/1M توکن |

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست GPT-5.2

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "یک الگوریتم برای بهینه‌سازی برنامه‌ریزی مسیر برای سرویس تحویل طراحی کنید."
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1733936400,
  "model": "gpt-5.2",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "در اینجا یک الگوریتم بهینه‌سازی مسیر با استفاده از ترکیبی از تکنیک‌ها آورده شده است...\n\n## مرور کلی الگوریتم\n\n1. **خوشه‌بندی**: گروه‌بندی تحویل‌ها بر اساس نزدیکی جغرافیایی با استفاده از k-means\n2. **بهینه‌سازی TSP**: اعمال الگوریتم ژنتیک برای هر خوشه\n3. **مسیریابی مجدد پویا**: تنظیم بلادرنگ بر اساس داده‌های ترافیک\n\n
```python\nfrom sklearn.cluster import KMeans\nimport numpy as np\n\nclass DeliveryOptimizer:\n    def __init__(self, deliveries, num_vehicles):\n        self.deliveries = deliveries\n        self.num_vehicles = num_vehicles\n    \n    def cluster_deliveries(self):\n        coords = np.array([(d.lat, d.lng) for d in self.deliveries])\n        kmeans = KMeans(n_clusters=self.num_vehicles)\n        return kmeans.fit_predict(coords)\n```\n\nاین رویکرد مسافت کل سفر را تقریبا 30% نسبت به مسیریابی ساده کاهش می‌دهد.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 320,
    "prompt_tokens": 18,
    "total_tokens": 338,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 18,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0048115000",
    "irt": 551.24,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست GPT-5.2 Pro (Responses API)

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.2-pro",
    "input": "یک معماری سیستم توزیع‌شده جامع با توجه به تحمل خطا و مقیاس‌پذیری برای یک پلتفرم معاملات مالی طراحی کنید.",
    "reasoning": {
      "effort": "high"
    }
  }'
```

### نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "messages": [
      {
        "role": "user",
        "content": "یک کامپوننت React با TypeScript برای داشبورد نمایش داده‌ها بسازید."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gpt-5.2",
    messages=[
        {
            "role": "user",
            "content": "یک کامپوننت React با TypeScript برای داشبورد نمایش داده‌ها بسازید.",
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
  model: "gpt-5.2",
  messages: [
    {
      role: "user",
      content: "یک کامپوننت React با TypeScript برای داشبورد نمایش داده‌ها بسازید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### ویژگی‌های پیشرفته

#### کنترل تلاش استدلال

GPT-5.2 از تلاش استدلال قابل تنظیم برای تعادل بین سرعت و کیفیت پشتیبانی می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.2",
    "input": "این اثبات ریاضی پیچیده را مرحله به مرحله حل کنید.",
    "reasoning": {
      "effort": "high"
    }
  }'

python=:response = client.responses.create(
    model="gpt-5.2",
    input="این اثبات ریاضی پیچیده را مرحله به مرحله حل کنید.",
    reasoning={"effort": "high"},
)

print(response.output)

javascript=:const response = await client.responses.create({
    model: "gpt-5.2",
    input: "این اثبات ریاضی پیچیده را مرحله به مرحله حل کنید.",
    reasoning: { effort: "high" },
});

console.log(response.output);

```

#### فراخوانی تابع

GPT-5.2 در فراخوانی تابع با دقت بهبود یافته عملکرد عالی دارد:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.2",
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
    model="gpt-5.2",
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
    model: "gpt-5.2",
    messages: [{role: "user", content: "آب و هوای فعلی سانفرانسیسکو چطور است و آیا باید چتر همراه ببرم؟"}],
    tools: tools,
    tool_choice: "auto",
});

```

### موارد استفاده

GPT-5.2 و GPT-5.2 Pro به ویژه برای موارد زیر مناسب هستند:

- **مهندسی نرم‌افزار**: تولید کد، دیباگ، بازسازی، پیاده‌سازی ویژگی‌ها
- **گردش‌های کاری عاملی**: وظایف خودگردان طولانی‌مدت با اجرای چند مرحله‌ای
- **کار دانشی حرفه‌ای**: صفحه‌گسترده‌ها، ارائه‌ها، گزارش‌ها، تحلیل اسناد
- **حل مسائل پیچیده**: طراحی معماری، برنامه‌ریزی سیستم، تحلیل استراتژیک
- **تحقیقات علمی**: ریاضیات پیشرفته، فیزیک، شیمی، سوالات زیست‌شناسی
- **وظایف زمینه طولانی**: تحلیل اسناد با پنجره زمینه 400K توکن
- **وظایف چندوجهی**: تحلیل مبتنی بر بینایی، درک تصویر، تعامل با رابط کاربری

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای استدلال](fa/guides/reasoning.md)
- [مرجع Responses API](fa/api-reference/responses.md)
