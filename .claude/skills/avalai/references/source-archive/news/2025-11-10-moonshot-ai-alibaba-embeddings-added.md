# ارائه‌دهنده Moonshot.ai و مدل‌های Embedding Alibaba اکنون در دسترس هستند

**تاریخ:** 1404-08-20 / (2025-11-10)

## خلاصه

AvalAI پشتیبانی از Moonshot.ai، یک ارائه‌دهنده جدید با ۱۰ مدل پیشرفته شامل سری قدرتمند Kimi با پنجره زمینه تا 128K و قابلیت‌های استدلال را معرفی می‌کند. علاوه بر این، ۴ مدل جدید embedding چندوجهی و متنی از Alibaba (Dashscope) را معرفی می‌کنیم که گزینه‌های شما را برای برنامه‌های کاربردی مبتنی بر بردار گسترش می‌دهد. همه مدل‌ها از طریق API یکپارچه ما با پشتیبانی از چندین نقطه پایانی در دسترس هستند.

---

## جزئیات

### Moonshot.ai

۱۰ مدل جدید از Moonshot.ai را معرفی می‌کنیم که شامل سری پیشرفته Kimi با پنجره‌های زمینه گسترده، قابلیت‌های بینایی، ویژگی‌های استدلال و پشتیبانی از فراخوانی ابزار است:

- **[kimi-k2-0711-preview](fa/providers/moonshotai.md#kimi-k2-0711-preview)**: نسخه پیش‌نمایش نسل بعدی مدل K2 با عملکرد و کارایی بهبود یافته. طول پنجره زمینه 128K.

- **[kimi-latest](fa/providers/moonshotai.md#kimi-latest)**: آخرین مدل پایدار Kimi با انتخاب خودکار نسخه و بهینه‌سازی. طول پنجره زمینه 128K.

- **[kimi-thinking-preview](fa/providers/moonshotai.md#kimi-thinking-preview)**: مدل استدلال پیشرفته با قابلیت‌های زنجیره‌ای تفکر (Chain-of-Thought) برای حل مسائل پیچیده چند مرحله‌ای. طول پنجره زمینه 128K.

- **[moonshot-v1-8k](fa/providers/moonshotai.md#moonshot-v1-8k)**: مدل مقرون به صرفه برای مکالمات کوتاه‌تر. طول پنجره زمینه 8K.

- **[moonshot-v1-8k-vision-preview](fa/providers/moonshotai.md#moonshot-v1-8k-vision-preview)**: مدل با قابلیت بینایی برای وظایف چندوجهی. طول پنجره زمینه 8K.

- **[moonshot-v1-32k](fa/providers/moonshotai.md#moonshot-v1-32k)**: مدل متعادل برای مکالمات با طول متوسط. طول پنجره زمینه 32K.

- **[moonshot-v1-32k-vision-preview](fa/providers/moonshotai.md#moonshot-v1-32k-vision-preview)**: مدل با قابلیت بینایی و زمینه گسترده. طول پنجره زمینه 32K.

- **[moonshot-v1-128k](fa/providers/moonshotai.md#moonshot-v1-128k)**: مدل با زمینه گسترده برای پردازش اسناد. طول پنجره زمینه 128K.

- **[moonshot-v1-128k-vision-preview](fa/providers/moonshotai.md#moonshot-v1-128k-vision-preview)**: مدل با قابلیت بینایی و حداکثر پنجره زمینه. طول پنجره زمینه 128K.

- **[moonshot-v1-auto](fa/providers/moonshotai.md#moonshot-v1-auto)**: به طور خودکار بهترین مدل را بر اساس ورودی شما انتخاب می‌کند. تا 128K طول پنجره زمینه.

**ویژگی‌های کلیدی:**
- **پنجره‌های زمینه گسترده**: 8K تا 128K توکن برای مدیریت مکالمات و اسناد گسترده
- **قابلیت‌های بینایی**: مدل‌های vision-preview از تصاویر کدگذاری شده Base64 و URL‌های تصویر پشتیبانی می‌کنند
- **مدل‌های استدلال**: [`kimi-thinking-preview`](fa/providers/moonshotai.md#kimi-thinking-preview) استدلال زنجیره‌ای تفکر را برای تحلیل پیچیده فراهم می‌کند
- **استفاده از ابزار (فراخوانی تابع)**: همه مدل‌ها از فراخوانی تابع با حداکثر ۱۲۸ ابزار در هر درخواست پشتیبانی می‌کنند
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته از طریق پارامتر `response_format`
- **حالت جزئی**: امکان پیش‌پر کردن پاسخ‌های دستیار برای کنترل بهتر خروجی
- **انتخاب خودکار**: [`moonshot-v1-auto`](fa/providers/moonshotai.md#moonshot-v1-auto) به طور هوشمند بهترین مدل را مسیریابی می‌کند
- **کش کردن پرامپت**: همه مدل‌ها از ورودی کش شده برای صرفه‌جویی قابل توجه در هزینه توکن‌های تکراری پشتیبانی می‌کنند
- **سازگاری با OpenAI**: پشتیبانی کامل از SDK و فرمت API OpenAI

**پشتیبانی نقطه پایانی:**
- **پشتیبانی کامل**: [`v1/chat/completions`](fa/guides/text-generation.md)
- **پشتیبانی جزئی**: [`v1/messages`](fa/guides/responses-vs-chat-completions.md)، [`v1/responses`](fa/guides/responses-vs-chat-completions.md)

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| kimi-k2-0711-preview | $0.60/1M توکن | $0.15/1M توکن | $2.50/1M توکن |
| kimi-latest | $0.20/1M توکن | $0.15/1M توکن | $5.00/1M توکن |
| kimi-thinking-preview | $30.00/1M توکن | $0.15/1M توکن | $30.00/1M توکن |
| moonshot-v1-8k | $0.20/1M توکن | $0.15/1M توکن | $2.00/1M توکن |
| moonshot-v1-8k-vision-preview | $0.20/1M توکن | $0.15/1M توکن | $2.00/1M توکن |
| moonshot-v1-32k | $1.00/1M توکن | $0.15/1M توکن | $3.00/1M توکن |
| moonshot-v1-32k-vision-preview | $1.00/1M توکن | $0.15/1M توکن | $3.00/1M توکن |
| moonshot-v1-128k | $2.00/1M توکن | $0.15/1M توکن | $5.00/1M توکن |
| moonshot-v1-128k-vision-preview | $2.00/1M توکن | $0.15/1M توکن | $5.00/1M توکن |
| moonshot-v1-auto | $2.00/1M توکن | $0.15/1M توکن | $5.00/1M توکن |

**هزینه‌های اضافی:**
- فراخوانی ابزار جستجوی وب: $0.005 به ازای هر فراخوانی (هنگام استفاده از ابزارهای جستجوی وب خارجی)


### مدل‌های Embedding Alibaba (Dashscope)

۴ مدل embedding جدید از Alibaba Dashscope را معرفی می‌کنیم که شامل قابلیت‌های چندوجهی است:

- **[tongyi-embedding-vision-plus](fa/providers/alibaba.md#tongyi-embedding-vision-plus)**: مدل embedding چندوجهی پیشرفته با پشتیبانی از متن، تصویر و ویدیو. ۱,۱۵۲ بعد، محدودیت متن ۱,۰۲۴ توکن.

- **[tongyi-embedding-vision-flash](fa/providers/alibaba.md#tongyi-embedding-vision-flash)**: مدل embedding چندوجهی سریع بهینه‌شده برای سرعت. ۷۶۸ بعد، محدودیت متن ۱,۰۲۴ توکن.

- **[text-embedding-v4](fa/providers/alibaba.md#text-embedding-v4)**: آخرین نسل مدل embedding متنی با ابعاد قابل تنظیم (۶۴-۲,۰۴۸). از دستورالعمل‌های کار، بردارهای پراکنده و پردازش دسته‌ای پشتیبانی می‌کند.

- **[text-embedding-v3](fa/providers/alibaba.md#text-embedding-v3)**: نسل قبلی مدل embedding متنی با عملکرد اثبات شده. ابعاد قابل تنظیم (۵۱۲-۱,۰۲۴).

**ویژگی‌های کلیدی:**
- **پشتیبانی چندوجهی**: مدل‌های بینایی از ورودی‌های متنی، تصویری و ویدیویی پشتیبانی می‌کنند
- **ابعاد قابل تنظیم**: مدل‌های متنی از چندین گزینه بعدی پشتیبانی می‌کنند
- **سازگاری با OpenAI**: با OpenAI SDK از طریق نقطه پایانی [`v1/embeddings`](fa/guides/retrieval.md) کار می‌کند
- **پشتیبانی از API بومی**: همچنین فرمت پاسخ بومی Alibaba را برای ویژگی‌های پیشرفته بازمی‌گرداند
- **دستورالعمل‌های کار**: [`text-embedding-v4`](fa/providers/alibaba.md#text-embedding-v4) از بهینه‌سازی کار سفارشی پشتیبانی می‌کند
- **بردارهای پراکنده**: [`text-embedding-v4`](fa/providers/alibaba.md#text-embedding-v4) می‌تواند هم بردارهای متراکم و هم پراکنده تولید کند

**موارد استفاده:**
- بازیابی متقابل (متن به تصویر، تصویر به ویدیو)
- محاسبه شباهت معنایی
- طبقه‌بندی و خوشه‌بندی محتوا
- جستجوی تصویر مبتنی بر متن
- تحلیل محتوای ویدیو

برای پارامترهای API بومی Alibaba با OpenAI SDK، از فیلد [`extra_body`](fa/guides/provider-specific-params.md) برای ارسال پارامترهای غیر OpenAI استفاده کنید.

### نمونه‌های درخواست/پاسخ API

#### نمونه درخواست - گفتگوی Moonshot.ai

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."
      }
    ],
    "temperature": 0.6
  }'
```

#### نمونه پاسخ - گفتگوی Moonshot.ai

```json
{
  "id": "cmpl-moonshot-1234567890",
  "created": 1762123456,
  "model": "kimi-latest",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "محاسبات کوانتومی یک رویکرد انقلابی برای محاسبات است که از اصول مکانیک کوانتومی بهره می‌برد...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 245,
    "prompt_tokens": 18,
    "total_tokens": 263,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 18,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0013474000",
    "irt": 154.36,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست - استدلال Moonshot.ai

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-thinking-preview",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کنید"
      }
    ],
    "temperature": 1.0,
    "max_tokens": 4096
  }'
```

#### نمونه درخواست - Embedding متنی Alibaba

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "text-embedding-v4",
    "input": "یادگیری ماشین در حال تحول فناوری است",
    "dimensions": 1024
  }'
```

#### نمونه پاسخ - Embedding متنی Alibaba

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        -0.026611328125,
        -0.016571044921875,
        -0.02227783203125,
        0.0156707763671875,
        "...[مجموعا ۱۰۲۴ بعد]"
      ]
    }
  ],
  "model": "text-embedding-v4",
  "usage": {
    "prompt_tokens": 8,
    "total_tokens": 8
  },
  "estimated_cost": {
    "unit": "0.0000005600",
    "irt": 0.06,
    "exchange_rate": 114600
  }
}
```

#### نمونه درخواست - Embedding چندوجهی Alibaba

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "tongyi-embedding-vision-plus",
    "input": {
      "contents": [
        {"text": "یک غروب زیبا بر فراز کوه‌ها"},
        {"image": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"}
      ]
    }
  }'
```

### نمونه‌های استفاده از SDK

#### تکمیل گفتگوهای Moonshot.ai

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "اصول کلیدی معماری پایدار چیست؟"
      }
    ],
    "temperature": 0.6
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            "role": "user",
            "content": "اصول کلیدی معماری پایدار چیست؟",
        },
    ],
    temperature=0.6,
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "kimi-latest",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
    },
    {
      role: "user",
      content: "اصول کلیدی معماری پایدار چیست؟",
    },
  ],
  temperature: 0.6,
});

console.log(completion.choices[0].message.content);

```

#### مدل بینایی Moonshot.ai

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H
"Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "moonshot-v1-8k-vision-preview",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "در این تصویر چه چیزی است؟"
          },
          {
            "type": "image_url",
            "image_url": {
              "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
            }
          }
        ]
      }
    ]
  }'

python=:completion = client.chat.completions.create(
    model="moonshot-v1-8k-vision-preview",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی است؟"},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
                    },
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:const completion = await client.chat.completions.create({
  model: "moonshot-v1-8k-vision-preview",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "در این تصویر چه چیزی است؟" },
        {
          type: "image_url",
          image_url: { url: "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png" },
        },
      ],
    },
  ],
});

console.log(completion.choices[0].message.content);

```

#### Embedding‌های متنی Alibaba

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "text-embedding-v4",
    "input": "پردازش زبان طبیعی به رایانه‌ها امکان درک متن را می‌دهد",
    "dimensions": 1024
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="text-embedding-v4",
    input="پردازش زبان طبیعی به رایانه‌ها امکان درک متن را می‌دهد",
    dimensions=1024,
)

print(response.data[0].embedding)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "text-embedding-v4",
  input: "پردازش زبان طبیعی به رایانه‌ها امکان درک متن را می‌دهد",
  dimensions: 1024,
});

console.log(response.data[0].embedding);

```

#### Embedding‌های چندوجهی Alibaba با پارامترهای بومی

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "tongyi-embedding-vision-plus",
    "input": {
      "contents": [
        {"text": "تصویر محصول برای جستجو"},
        {"image": "https://example.com/product.jpg"}
      ]
    }
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از extra_body برای پارامترهای بومی Alibaba
response = client.embeddings.create(
    model="tongyi-embedding-vision-plus",
    input="placeholder",  # مورد نیاز OpenAI SDK
    extra_body={
        "input": {
            "contents": [
                {"text": "تصویر محصول برای جستجو"},
                {"image": "https://example.com/product.jpg"},
            ]
        }
    },
)

print(response.data[0].embedding)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از پارامترهای غیراستاندارد
const response = await client.embeddings.create({
  model: "tongyi-embedding-vision-plus",
  input: "placeholder", // مورد نیاز OpenAI SDK
  // فرمت بومی Alibaba در بدنه درخواست
  input: {
    contents: [
      { text: "تصویر محصول برای جستجو" },
      { image: "https://example.com/product.jpg" }
    ]
  }
});

console.log(response.data[0].embedding);

```

### استفاده از مدل استدلال

مدل [`kimi-thinking-preview`](fa/providers/moonshotai.md#kimi-thinking-preview) استدلال زنجیره‌ای تفکر را برای حل مسائل پیچیده فراهم می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-thinking-preview",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "مبادلات بین معماری یکپارچه و میکروسرویس‌ها را تحلیل کنید"
      }
    ],
    "temperature": 1.0,
    "max_tokens": 4096
  }'

python=:response = client.chat.completions.create(
    model="kimi-thinking-preview",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            "role": "user",
            "content": "مبادلات بین معماری یکپارچه و میکروسرویس‌ها را تحلیل کنید",
        },
    ],
    temperature=1.0,
    max_tokens=4096,
)

# مدل فرآیند استدلال خود را نشان خواهد داد
print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
    model: "kimi-thinking-preview",
    messages: [
        {
            role: "system",
            content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            role: "user",
            content: "مبادلات بین معماری یکپارچه و میکروسرویس‌ها را تحلیل کنید",
        },
    ],
    temperature: 1.0,
    max_tokens: 4096,
});

// مدل فرآیند استدلال خود را نشان خواهد داد
console.log(response.choices[0].message.content);

```

### نمونه فراخوانی تابع

مدل‌های Moonshot.ai از فراخوانی تابع پیشرفته با حداکثر ۱۲۸ ابزار در هر درخواست پشتیبانی می‌کنند:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "آب و هوای توکیو چگونه است؟"
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
                "enum": ["celsius", "fahrenheit"]
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "temperature": 0.6
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
                    },
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {"role": "user", "content": "آب و هوای توکیو چگونه است؟"},
    ],
    tools=tools,
    temperature=0.6,
)

print(response.choices[0].message)

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
                    },
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "kimi-latest",
    messages: [
        {
            role: "system",
            content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        { role: "user", content: "آب و هوای توکیو چگونه است؟" },
    ],
    tools: tools,
    temperature: 0.6,
});

console.log(response.choices[0].message);

```

### ویژگی‌های پیشرفته Embedding متنی

مدل [`text-embedding-v4`](fa/providers/alibaba.md#text-embedding-v4) از ویژگی‌های پیشرفته از طریق API بومی پشتیبانی می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "text-embedding-v4",
    "input": "مقالات تحقیقاتی درباره یادگیری ماشین",
    "dimensions": 1024,
    "text_type": "query",
    "instruct": "با توجه به یک پرس‌وجوی مقاله تحقیقاتی، مقالات تحقیقاتی مرتبط را بازیابی کنید"
  }'

python=:response = client.embeddings.create(
    model="text-embedding-v4",
    input="مقالات تحقیقاتی درباره یادگیری ماشین",
    dimensions=1024,
    extra_body={
        "text_type": "query",
        "instruct": "با توجه به یک پرس‌وجوی مقاله تحقیقاتی، مقالات تحقیقاتی مرتبط را بازیابی کنید",
    },
)

print(response.data[0].embedding)

javascript=:const response = await client.embeddings.create({
  model: "text-embedding-v4",
  input: "مقالات تحقیقاتی درباره یادگیری ماشین",
  dimensions: 1024,
  extra_body: {
    text_type: "query",
    instruct: "با توجه به یک پرس‌وجوی مقاله تحقیقاتی، مقالات تحقیقاتی مرتبط را بازیابی کنید"
  }
});

console.log(response.data[0].embedding);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های Moonshot.ai](fa/providers/moonshotai.md)
- [مستندات مدل‌های Alibaba (Dashscope)](fa/providers/alibaba.md)
- [راهنمای تولید متن](fa/guides/text-generation.md)
- [راهنمای Embedding و بازیابی](fa/guides/retrieval.md)
- [پارامترهای خاص ارائه‌دهنده](fa/guides/provider-specific-params.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای قابلیت‌های بینایی](fa/guides/vision.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)