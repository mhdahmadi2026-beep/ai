# مدل GPT-5 Pro اکنون در دسترس است

**تاریخ:** 1404-07-14 / (2025-10-06)

## خلاصه

ما افزودن GPT-5 Pro، پیشرفته‌ترین مدل استدلالی OpenAI را اعلام می‌کنیم که اکنون در AvalAI برای کاربران سطح 2، 3، 4 و 5 در دسترس است. GPT-5 Pro هوش سطح تخصصی را با قابلیت‌های استدلال گسترده برای پاسخ‌های جامع و دقیق در وظایف پیچیده در زمینه‌های کدنویسی، ریاضیات، نوشتن، بهداشت و موارد دیگر ارائه می‌دهد.

---

## جزئیات

### OpenAI

* **gpt-5-pro**: پیشرفته‌ترین مدل استدلالی OpenAI با قابلیت‌های تفکر گسترده، تولید پاسخ‌های هوشمندانه‌تر و دقیق‌تر برای مسائل پیچیده. در دسترس کاربران سطح 2 به بالا. [مستندات](fa/providers/openai.md)

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 400,000 توکن برای مدیریت مکالمات و اسناد گسترده
- **حداکثر توکن خروجی**: 272,000 توکن برای پاسخ‌های جامع
- **قابلیت‌های پیشرفته**: فراخوانی تابع، خروجی‌های ساختاریافته، جستجوی وب، جستجوی فایل، تولید تصویر، پشتیبانی MCP
- **پشتیبانی استدلال**: استدلال با تلاش بالا با فرآیند تفکر قابل مشاهده برای حل مسائل پیچیده
- **پشتیبانی نقطه پایانی**: منحصرا از طریق API v1/responses در دسترس است
- **تاریخ قطع دانش**: 30 سپتامبر 2024

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | خروجی |
|-------|-------|--------|
| gpt-5-pro | $15.00/1M توکن | $120.00/1M توکن |

**توجه:** GPT-5 Pro برای وظایف پیچیده و سطح تخصصی که نیاز به استدلال گسترده دارند طراحی شده است. برخی درخواست‌ها ممکن است چندین دقیقه طول بکشد. این مدل به طور پیش‌فرض با تلاش استدلال بالا کار می‌کند و منحصرا در API Responses برای فعال‌سازی تعاملات چندنوبتی و ویژگی‌های پیشرفته در دسترس است.

### مثال استفاده

#### API Responses پایه

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-pro",
    "input": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن."
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.responses.create(
    model="gpt-5-pro",
    input="یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
)

print(response.output_text)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5-pro",
  input: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
});

console.log(response.output_text);

```

#### با جستجوی وب

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-pro",
    "tools": [{"type": "web_search"}],
    "input": "اخبار مثبت امروز چه بود؟"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.responses.create(
    model="gpt-5-pro",
    tools=[{"type": "web_search"}],
    input="اخبار مثبت امروز چه بود؟",
)

print(response.output_text)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5-pro",
  tools: [{ type: "web_search" }],
  input: "اخبار مثبت امروز چه بود؟",
});

console.log(response.output_text);

```

### ویژگی‌های پیشرفته

#### مثال فراخوانی تابع

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5-pro",
    "input": "هوای نیویورک چطور است؟",
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات هوای فعلی",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات هوای فعلی",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    }
                },
                "required": ["location"],
            },
        },
    }
]

response = client.responses.create(
    model="gpt-5-pro",
    input="هوای نیویورک چطور است؟",
    tools=tools,
    tool_choice="auto",
)

print(response.output_text)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات هوای فعلی",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر",
                    }
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.responses.create({
  model: "gpt-5-pro",
  input: "هوای نیویورک چطور است؟",
  tools: tools,
  tool_choice: "auto",
});

console.log(response.output_text);

```

### نسخه‌های مدل

GPT-5 Pro نسخه‌بندی snapshot را برای قفل کردن رفتار خاص مدل فراهم می‌کند:

- **gpt-5-pro**: آخرین نسخه (به طور خودکار به‌روزرسانی می‌شود)
- **gpt-5-pro-2025-10-06**: snapshot ثابت از 6 اکتبر 2025

### نکات برجسته عملکرد

GPT-5 Pro عملکرد پیشرفته‌ای را در چندین حوزه نشان می‌دهد:

- **ریاضیات**: 94.6% در AIME 2025 (با ابزار)
- **کدنویسی**: 74.9% در SWE-bench Verified
- **چندوجهی**: 84.2% در حل مسائل بصری سطح کالج MMMU
- **بهداشت**: 46.2% در مکالمات چالش‌برانگیز HealthBench Hard
- **علوم**: 88.4% در سؤالات سطح دکترا GPQA Diamond (با استدلال گسترده)

این مدل در حل مسائل پیچیده برتری دارد و عملکرد سطح تخصصی را در کدنویسی، ریاضیات، نوشتن، بهداشت، ادراک بصری و پیروی از دستورالعمل‌ها نشان می‌دهد.

---

## لینک‌های مرتبط

* [مستندات مدل‌های OpenAI](fa/providers/openai.md)
* [راهنمای API Responses](fa/guides/responses-vs-chat-completions.md)
* [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
* [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
* [مستندات محدودیت‌های نرخ](fa/guides/rate-limits.md)