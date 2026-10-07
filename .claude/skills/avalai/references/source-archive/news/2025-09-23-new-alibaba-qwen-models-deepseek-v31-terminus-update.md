# مدل‌های جدید Alibaba Qwen، به‌روزرسانی DeepSeek-V3.1-Terminus، مدل‌های X.AI Grok-4-Fast و بهبود تولید تصویر

**تاریخ:** 1404-07-01 / (2025-09-23)

## خلاصه

AvalAI اعلام می‌کند که 8 مدل جدید متنی چت Alibaba با پشتیبانی جامع endpoint، 2 مدل پیشرفته تولید تصویر Qwen با سازگاری دوگانه SDK، مدل‌های جدید استدلال Grok-4-Fast X.AI با پنجره زمینه 2M، و ارتقاء خودکار backend به DeepSeek-V3.1-Terminus برای بهبود سازگاری زبان و عملکرد agent اضافه شده‌اند.

---

## جزئیات

ما گسترش قابل توجهی در ارائه مدل‌های هوش مصنوعی خود با مدل‌های متنی جدید Alibaba، قابلیت‌های پیشرفته تولید تصویر، مدل‌های استدلال مقرون‌به‌صرفه جدید X.AI، و بهبود عملکرد DeepSeek از طریق بهبودهای خودکار backend اعلام می‌کنیم.

### ارتقاء خودکار DeepSeek-V3.1-Terminus

DeepSeek به طور خودکار زیرساخت backend خود را به DeepSeek-V3.1-Terminus ارتقا داده است. کاربران [`deepseek-chat`](fa/models/deepseek-chat.md) و [`deepseek-reasoner`](fa/models/deepseek-reasoner.md) به طور خودکار از این بهبودها بدون تغییر نام مدل بهره‌مند خواهند شد.

#### DeepSeek

- **deepseek-chat**: اکنون توسط backend DeepSeek-V3.1-Terminus با سازگاری زبان بهبود یافته و قابلیت‌های agent پشتیبانی می‌شود
- **deepseek-reasoner**: اکنون توسط backend DeepSeek-V3.1-Terminus با ثبات استدلال بهبود یافته پشتیبانی می‌شود

**بهبودهای کلیدی:**
- **سازگاری زبان**: کاهش مخلوط شدن چینی/انگلیسی و حذف مشکلات کاراکترهای تصادفی
- **عملکرد Agent**: قابلیت‌های قوی‌تر Code Agent و Search Agent
- **ثبات خروجی**: خروجی‌های قابل اعتمادتر و سازگارتر در benchmarkها
- **طول Context**: 128K توکن
- **قیمت‌گذاری**: ورودی (cache hit) $0.07/1M توکن، ورودی (cache miss) $0.56/1M توکن، خروجی $1.68/1M توکن

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-chat",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع Python برای تجزیه و تحلیل پیچیدگی کد ایجاد کن"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای تجزیه و تحلیل پیچیدگی کد ایجاد کن",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
    model: "deepseek-reasoner",
    messages: [
        {
            role: "user",
            content: "دلیل انتخاب یک الگوریتم خاص را توضیح دهید",
        },
    ],
});

console.log(response.choices[0].message.content);

```

### مدل‌های جدید متنی چت Alibaba

ما 8 مدل جدید Alibaba (Dashscope) را با پشتیبانی از چندین endpoint شامل `v1/completions`، [`v1/chat/completions`](fa/api-reference/chat.md)، و پشتیبانی جزئی در [`v1/messages`](fa/api-reference/messages.md) اضافه کرده‌ایم.

#### Alibaba

- **qwen-flash**: مدل با عملکرد بالا بهینه شده برای سرعت و کارایی با قیمت‌گذاری طبقه‌بندی شده
- **qwen-flash-2025-07-28**: نسخه تاریخ‌دار qwen-flash با قابلیت‌ها و قیمت‌گذاری یکسان
- **qwen-plus-2025-09-11**: مدل بهبود یافته با قابلیت‌های استدلال بهتر
- **qwen3-next-80b-a3b-thinking**: مدل استدلال پیشرفته با فرآیند تفکر قابل مشاهده
- **qwen3-next-80b-a3b-instruct**: مدل پیروی از دستورالعمل بهینه شده برای پاسخ‌های مستقیم
- **qwen3-coder-flash**: مدل تخصصی کدنویسی با طبقه‌بندی قیمت آگاه از context
- **qwen3-coder-flash-2025-07-28**: نسخه تاریخ‌دار qwen3-coder-flash
- **qwen-plus-2025-07-28**: نسخه قبلی qwen-plus با عملکرد تثبیت شده

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی Cache شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| qwen-flash | $0.05/1M | $0.025/1M | $0.40/1M | بالای 256K: ورودی $0.25/1M، خروجی $2.00/1M |
| qwen-plus-2025-09-11 | $0.40/1M | $0.20/1M | $4.00/1M | - |
| qwen3-next-80b-a3b-thinking | $0.144/1M | $0.072/1M | $1.434/1M | - |
| qwen3-next-80b-a3b-instruct | $0.144/1M | $0.072/1M | $0.574/1M | - |
| qwen3-coder-flash | $0.30/1M | $0.10/1M | $1.50/1M | قیمت‌گذاری طبقه‌ای بالای 32K، 128K، 256K |

```language-selector
bash=:# استفاده از qwen-flash برای وظایف عمومی
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-flash",
    "messages": [
      {
        "role": "user",
        "content": "مزایای کلیدی cloud computing را خلاصه کن"
      }
    ]
  }'

# استفاده از qwen3-coder-flash برای وظایف کدنویسی
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-coder-flash",
    "messages": [
      {
        "role": "user",
        "content": "یک interface TypeScript برای سیستم مدیریت کاربر بنویس"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از qwen-flash برای وظایف عمومی
response = client.chat.completions.create(
    model="qwen-flash",
    messages=[
        {
            "role": "user",
            "content": "مزایای کلیدی cloud computing را خلاصه کن",
        }
    ],
)

print(response.choices[0].message.content)

# استفاده از qwen3-coder-flash برای وظایف کدنویسی
coding_response = client.chat.completions.create(
    model="qwen3-coder-flash",
    messages=[
        {
            "role": "user",
            "content": "یک interface TypeScript برای سیستم مدیریت کاربر بنویس",
        }
    ],
)

print(coding_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// استفاده از qwen3-next-80b-a3b-thinking برای وظایف استدلال
const response = await client.chat.completions.create({
    model: "qwen3-next-80b-a3b-thinking",
    messages: [
        {
            role: "user",
            content: "مزایا و معایب معماری microservices را تجزیه و تحلیل کن",
        },
    ],
});

console.log(response.choices[0].message.content);

```

### مدل‌های جدید تولید تصویر Qwen

ما دو مدل پیشرفته تصویر با پشتیبانی دوگانه SDK معرفی کرده‌ایم که با schema OpenAI و schema بومی Alibaba Dashscope در [`v1/images/generations`](fa/api-reference/images.md) و [`v1/images/edits`](fa/api-reference/images.md) سازگار هستند.

#### مدل‌های تصویر Alibaba

- **qwen-image**: تولید پیشرفته متن-به-تصویر با بازنویسی هوشمند prompt و پارامترهای قابل تنظیم
- **qwen-image-edit**: قابلیت‌های پیچیده ویرایش تصویر با پشتیبانی ورودی چند تصویری

**قیمت‌گذاری:**
- **qwen-image**: $0.035 به ازای هر تصویر تولید شده
- **qwen-image-edit**: $0.045 به ازای هر تصویر ویرایش شده

**ویژگی‌های کلیدی:**
- **گزینه‌های رزولوشن**: نسبت‌های مختلف ابعاد (1:1، 4:3، 3:4، 16:9، 9:16)
- **بهبود Prompt**: بازنویسی هوشمند prompt برای نتایج بهتر
- **پشتیبانی دوگانه SDK**: سازگار با OpenAI SDK و API بومی Dashscope
- **پارامترهای پیشرفته**: promptهای منفی، کنترل watermark، پشتیبانی seed

```language-selector
bash=:# تولید متن-به-تصویر با فرمت OpenAI
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-image",
    "prompt": "منظره آرام کوهستانی با دریاچه شفاف که قله‌های برفی را منعکس می‌کند",
    "size": "1328x1328",
    "n": 1
  }'

# ویرایش تصویر
curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=qwen-image-edit" \
  -F "image=@input_image.jpg" \
  -F "prompt=آسمان را به غروب دراماتیک با رنگ‌های نارنجی و بنفش تغییر دهید"

# استفاده از فرمت بومی Dashscope
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-image",
    "input": {
      "messages": [
        {
          "role": "user",
          "content": [
            {
              "text": "عکس پرتره حرفه‌ای از یک فرد تجاری مطمئن در محیط اداری مدرن"
            }
          ]
        }
      ]
    },
    "parameters": {
      "size": "1328*1328",
      "prompt_extend": true,
      "watermark": false
    }
  }'

python=:# استفاده از فرمت OpenAI SDK
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید متن-به-تصویر
response = client.images.generate(
    model="qwen-image",
    prompt="منظره آرام کوهستانی با دریاچه شفاف که قله‌های برفی را منعکس می‌کند",
    size="1328x1328",
    n=1,
    response_format="url",  # or b64_json
)

print(response.data[0].url)

# ویرایش تصویر
import requests

with open("input_image.jpg", "rb") as image_file:
    response = requests.post(
        "https://api.avalai.ir/v1/images/edits",
        headers={"Authorization": f"Bearer {api_key}"},
        files={"image": image_file},
        data={
            "model": "qwen-image-edit",
            "prompt": "آسمان را به غروب دراماتیک با رنگ‌های نارنجی و بنفش تغییر دهید",
        },
    )

print(response.json())

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تولید متن-به-تصویر
const response = await client.images.generate({
    model: "qwen-image",
    prompt: "منظره شهری آینده‌نگرانه با ماشین‌های پرنده و چراغ‌های نئون",
    size: "1664x928", // نسبت ابعاد 16:9
    n: 1,
    response_format: "url", // or b64_json
});

console.log(response.data[0].url);

// استفاده از فرمت بومی Dashscope
const dashscopeResponse = await fetch("https://api.avalai.ir/v1/images/generations", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        model: "qwen-image",
        input: {
            messages: [
                {
                    role: "user",
                    content: [
                        {
                            text: "عکس پرتره حرفه‌ای از یک فرد تجاری مطمئن در محیط اداری مدرن"
                        }
                    ]
                }
            ]
        },
        parameters: {
            size: "1328*1328",
            prompt_extend: true,
            watermark: false
        }
    })
});

const result = await dashscopeResponse.json();
console.log(result);

```

### مدل‌های جدید X.AI Grok-4-Fast

ما دو مدل جدید استدلال X.AI را با قابلیت‌های پیشرفته و قیمت‌گذاری مقرون‌به‌صرفه اضافه کرده‌ایم که برای وظایف پیچیده استدلال و تحلیل طراحی شده‌اند.

#### X.AI

- **grok-4-fast-reasoning**: مدل استدلال پیشرفته با قابلیت‌های تحلیل عمیق و حل مسئله پیچیده
- **grok-4-fast-non-reasoning**: مدل سریع برای وظایف عمومی چت و تولید محتوا بدون فرآیند استدلال

**ویژگی‌های کلیدی:**
- **پنجره زمینه**: 2M توکن برای هر دو مدل
- **قابلیت‌های پیشرفته**: پشتیبانی از function calling، structured outputs، و vision
- **عملکرد بهینه**: سرعت بالا با حفظ کیفیت خروجی
- **قیمت‌گذاری مقرون‌به‌صرفه**: بهینه شده برای استفاده در مقیاس بزرگ

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | خروجی | پنجره زمینه |
|------|-------|--------|-------------|
| grok-4-fast-reasoning | $0.40/1M توکن | $1.60/1M توکن | 2M توکن |
| grok-4-fast-non-reasoning | $0.40/1M توکن | $1.60/1M توکن | 2M توکن |

```language-selector
bash=:# استفاده از grok-4-fast-reasoning برای وظایف استدلال
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-fast-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید"
      }
    ],
    "max_tokens": 2048
  }'

# استفاده از grok-4-fast-non-reasoning برای چت عمومی
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4-fast-non-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "آخرین روندهای هوش مصنوعی در سال 2025 را خلاصه کنید"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از grok-4-fast-reasoning برای تحلیل پیچیده
response = client.chat.completions.create(
    model="grok-4-fast-reasoning",
    messages=[
        {
            "role": "user",
            "content": "مزایا و معایب پیاده‌سازی معماری microservices را تحلیل کنید و یک roadmap مهاجرت ارائه دهید",
        }
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)

# استفاده از grok-4-fast-non-reasoning برای تولید محتوا
content_response = client.chat.completions.create(
    model="grok-4-fast-non-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک مقاله وبلاگ در مورد مزایای کار از راه دور بنویسید",
        }
    ],
)

print(content_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// استفاده از grok-4-fast-reasoning برای حل مسئله
const reasoningResponse = await client.chat.completions.create({
    model: "grok-4-fast-reasoning",
    messages: [
        {
            role: "user",
            content: "یک سیستم توصیه‌گر برای پلتفرم e-commerce طراحی کنید که از machine learning استفاده می‌کند",
        },
    ],
    max_tokens: 2048,
});

console.log(reasoningResponse.choices[0].message.content);

// استفاده از grok-4-fast-non-reasoning برای پاسخ سریع
const quickResponse = await client.chat.completions.create({
    model: "grok-4-fast-non-reasoning",
    messages: [
        {
            role: "user",
            content: "بهترین practices برای امنیت API چیست؟",
        },
    ],
});

console.log(quickResponse.choices[0].message.content);

```

### پشتیبانی API Endpoint

**مدل‌های متنی چت در دسترس در:**
- `v1/completions` - endpoint تکمیل متن
- [`v1/chat/completions`](fa/api-reference/chat.md) - endpoint تکمیل چت  
- [`v1/messages`](fa/api-reference/messages.md) - endpoint پیام‌های سازگار با Anthropic (پشتیبانی جزئی)

**مدل‌های تصویر در دسترس در:**
- [`v1/images/generations`](fa/api-reference/images.md) - endpoint تولید تصویر
- [`v1/images/edits`](fa/api-reference/images.md) - endpoint ویرایش تصویر

هم فرمت OpenAI SDK و هم فرمت بومی Alibaba Dashscope برای حداکثر انعطاف‌پذیری پشتیبانی می‌شوند.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [مستندات رسمی Alibaba Dashscope](https://modelstudio.console.alibabacloud.com/?tab=doc#/doc/?type=model&url=2840914)
- [مستندات رسمی X.AI](https://docs.x.ai/)
