# افزودن مدل جدید X.AI: Grok-4

**تاریخ:** 1404-04-23 / (2025-07-14)

## خلاصه

مدل پیشرفته Grok-4، پرچمدار X.AI، اکنون به پلتفرم AvalAI راه یافته است. این مدل با توانایی‌های بی‌نظیر در پردازش زبان طبیعی، تحلیل ریاضیات و استدلال پیچیده، به‌عنوان یک راه‌حل جامع هوش مصنوعی، استانداردهای جدیدی برای کاربردهای متنوع تعریف می‌کند.

---

## جزئیات

### X.AI

- **grok-4**: جدیدترین و بهترین مدل پرچمدار X.AI که عملکرد استثنایی در زمینه‌های زبان طبیعی، ریاضیات و استدلال ارائه می‌دهد. این مدل همه‌کاره به عنوان راه‌حل مناسب برای کاربردهای جامع هوش مصنوعی عمل می‌کند. [مستندات](fa/models/grok-4.md)

### ویژگی‌های کلیدی

**قابلیت‌های پیشرفته:**
- **فراخوانی تابع (Function Calling)**: اتصال مدل به ابزارها و سیستم‌های خارجی برای عملکرد بهتر
- **خروجی‌های ساختاریافته (Structured Outputs)**: ارائه پاسخ‌ها در قالب‌های خاص و سازمان‌یافته برای یکپارچگی بهتر
- **استدلال (Reasoning)**: مدل قبل از پاسخ دادن فکر می‌کند و پاسخ‌های دقیق‌تر و منطقی‌تری ارائه می‌دهد
- **پنجره زمینه بزرگ**: پنجره زمینه 256,000 توکن برای مدیریت مکالمات و اسناد گسترده

**مشخصات عملکرد:**
- **نام‌های مدل**: `grok-4-0709`، `grok-4`، `grok-4-latest`
- **پنجره زمینه**: 256,000 توکن

### قیمت‌گذاری

- **ورودی**: 3.00 دلار به ازای هر میلیون توکن
- **ورودی کش‌ شده**: 0.75 دلار به ازای هر میلیون توکن (75% کاهش هزینه)
- **خروجی**: 15.00 دلار به ازای هر میلیون توکن

قیمت‌گذاری ورودی کش‌ شده می‌تواند هزینه‌های شما را به طور قابل توجهی کاهش دهد، به خصوص هنگام کار با محتوای تکراری یا مکالمات طولانی.

### نمونه‌های استفاده

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="grok-4",
    messages=[
        {
            "role": "user",
            "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید و یک مثال ریاضی ارائه دهید.",
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
  model: "grok-4",
  messages: [
    {
      role: "user",
      content:
        "محاسبات کوانتومی را به زبان ساده توضیح دهید و یک مثال ریاضی ارائه دهید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### نمونه فراخوانی تابع

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تعریف تابعی برای فراخوانی توسط مدل
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculate_math",
            "description": "انجام محاسبات ریاضی",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": "عبارت ریاضی برای ارزیابی",
                    }
                },
                "required": ["expression"],
            },
        },
    }
]

completion = client.chat.completions.create(
    model="grok-4",
    messages=[{"role": "user", "content": "15 ضرب در 23 به علاوه 47 چقدر می‌شود؟"}],
    tools=tools,
    tool_choice="auto",
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تعریف تابعی برای فراخوانی توسط مدل
const tools = [
  {
    type: "function",
    function: {
      name: "calculate_math",
      description: "انجام محاسبات ریاضی",
      parameters: {
        type: "object",
        properties: {
          expression: {
            type: "string",
            description: "عبارت ریاضی برای ارزیابی",
          },
        },
        required: ["expression"],
      },
    },
  },
];

const completion = await client.chat.completions.create({
  model: "grok-4",
  messages: [
    {
      role: "user",
      content: "15 ضرب در 23 به علاوه 47 چقدر می‌شود؟",
    },
  ],
  tools: tools,
  tool_choice: "auto",
});

console.log(completion.choices[0].message.content);

```

### موارد استفاده

Grok-4 در کاربردهای مختلف عملکرد بی‌نظیری دارد:

- **استدلال پیچیده**: حل مسائل پیشرفته و تحلیل منطقی
- **محاسبات ریاضی**: استدلال و محاسبات ریاضی پیچیده
- **وظایف زبان طبیعی**: تولید متن باکیفیت، خلاصه‌سازی و تحلیل
- **تولید کد**: کمک در برنامه‌نویسی و توضیح کد
- **تحقیق و تحلیل**: وظایف تحقیقاتی عمیق با استدلال جامع
- **نوشتن خلاقانه**: تولید محتوا با درک پیشرفته زبان

---

## لینک‌های مرتبط

- [مستندات مدل Grok-4](fa/models/grok-4.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [مستندات محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [مرجع API](fa/api-reference/)