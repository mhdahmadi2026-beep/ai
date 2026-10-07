# مدل‌های Perplexity Sonar اکنون در دسترس هستند

**تاریخ:** 1404-08-04 / (2025-10-26)

## خلاصه

AvalAI اکنون از ۵ مدل جدید Perplexity Sonar با قابلیت‌های پیشرفته جستجوی وب و استدلال پشتیبانی می‌کند. این مدل‌ها یکپارچگی جستجوی وب بلادرنگ، استدلال زنجیره‌ای (Chain-of-Thought) و قابلیت‌های تحقیق جامع را از طریق API یکپارچه ما با پشتیبانی از چندین نقطه پایانی از جمله [`v1/chat/completions`](fa/guides/text-generation.md)، [`v1/completions`](fa/guides/text-generation.md)، [`v1/messages`](fa/guides/responses-vs-chat-completions.md) و [`v1/responses`](fa/guides/responses-vs-chat-completions.md) فراهم می‌کنند.

---

## جزئیات

### Perplexity

۵ مدل جدید از Perplexity را معرفی می‌کنیم که تولید متن مبتنی بر هوش مصنوعی را با جستجوی وب بلادرنگ و قابلیت‌های استدلال ترکیب می‌کنند:

- **[sonar](fa/providers/perplexity.md#sonar)**: پاسخ‌های سریع با نتایج جستجوی قابل اعتماد. یک مدل جستجوی سبک و مقرون به صرفه که برای پاسخ‌های سریع و مستند با جستجوی وب بلادرنگ بهینه شده است. طول پنجره زمینه 128K.

- **[sonar-pro](fa/providers/perplexity.md#sonar-pro)**: جستجوی پیشرفته با نتایج جستجوی بهبود یافته. یک مدل جستجوی پیشرفته طراحی شده برای پرس‌وجوهای پیچیده که 2 برابر بیشتر از Sonar استاندارد نتایج جستجو ارائه می‌دهد. طول پنجره زمینه 200K.

- **[sonar-reasoning](fa/providers/perplexity.md#sonar-reasoning)**: استدلال سریع با جستجوی بلادرنگ. یک مدل متمرکز بر استدلال که استدلال زنجیره‌ای (CoT) را برای تحلیل ساختاری با جستجوی وب اعمال می‌کند. طول پنجره زمینه 128K.

- **[sonar-reasoning-pro](fa/providers/perplexity.md#sonar-reasoning-pro)**: استدلال پیشرفته با جستجوی جامع. استدلال زنجیره‌ای پیشرفته با 2 برابر نتایج جستجوی بیشتر برای تحلیل چند مرحله‌ای پیچیده. طول پنجره زمینه 128K.

- **[sonar-deep-research](fa/providers/perplexity.md#sonar-deep-research)**: تحقیق جامع در صدها منبع. تحلیل موضوعی در سطح تخصصی با تولید گزارش دقیق و پشتیبانی از استناد. طول پنجره زمینه 128K.

**ویژگی‌های کلیدی:**
- **جستجوی وب بلادرنگ**: همه مدل‌ها جستجوی وب زنده را با استنادات و ابرداده نتایج جستجو یکپارچه می‌کنند
- **استدلال زنجیره‌ای**: مدل‌های استدلال از حل مسئله ساختاری با فرآیندهای تفکر دقیق پشتیبانی می‌کنند
- **پنجره‌های زمینه انعطاف‌پذیر**: طول زمینه 128K-200K برای مدیریت اسناد گسترده
- **چندین نقطه پایانی API**: پشتیبانی کامل از v1/chat/completions و v1/completions؛ پشتیبانی جزئی از v1/messages و v1/responses
- **پشتیبانی از استناد**: تولید خودکار استناد با URL‌های منبع و ابرداده نتایج جستجو
- **گزینه‌های مقرون به صرفه**: سطوح قیمت‌گذاری مختلف از توکن‌های ورودی رایگان تا قابلیت‌های تحقیق عمیق پرمیوم

**جزئیات قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی | قیمت‌گذاری ویژه |
|-------|-------|--------------|--------|-----------------|
| sonar | $1.00/1M توکن | $0.50/1M توکن | $1.00/1M توکن | $5-$12 به ازای 1K درخواست (زمینه جستجو) |
| sonar-pro | $3.00/1M توکن | $1.50/1M توکن | $15.00/1M توکن | $6-$14 به ازای 1K درخواست (زمینه جستجو) |
| sonar-reasoning | $1.00/1M توکن | $0.50/1M توکن | $5.00/1M توکن | $5-$12 به ازای 1K درخواست (زمینه جستجو) |
| sonar-reasoning-pro | $2.00/1M توکن | $1.00/1M توکن | $8.00/1M توکن | $6-$14 به ازای 1K درخواست (زمینه جستجو) |
| sonar-deep-research | $2.00/1M توکن | $1.00/1M توکن | $8.00/1M توکن | $3.00/1M توکن استدلال، $2.00/1M توکن استناد، $0.005 به ازای هر پرس‌وجوی جستجو |

**توجه:** قیمت‌گذاری زمینه جستجو بر اساس پیچیدگی پرس‌وجو (کم/متوسط /زیاد) متفاوت است و به ازای هر 1K درخواست محاسبه می‌شود.

### نمونه درخواست/پاسخ API

#### نمونه درخواست - Sonar

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar",
    "messages": [
      {
        "role": "user",
        "content": "آخرین اخبار در تحقیقات هوش مصنوعی چیست؟"
      }
    ]
  }'
```

#### نمونه پاسخ - Sonar

```json
{
  "id": "80cff570-614d-4344-8cd4-9f78af816a3d",
  "created": 1761492286,
  "model": "sonar",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "آخرین اخبار در تحقیقات هوش مصنوعی برای سال 2025 پیشرفت‌های چشمگیری را برجسته می‌کند...",
        "role": "assistant",
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 592,
    "prompt_tokens": 9,
    "total_tokens": 601,
    "completion_tokens_details": null,
    "prompt_tokens_details": null,
    "cost": {
      "input_tokens_cost": 0.0,
      "output_tokens_cost": 0.001,
      "request_cost": 0.005,
      "total_cost": 0.006
    },
    "search_context_size": "low"
  },
  "citations": [
    "https://news.microsoft.com/source/features/ai/6-ai-trends-youll-see-more-of-in-2025/",

    "https://news.stanford.edu/artificial-intelligence",

    "https://www.artificialintelligence-news.com"

  ],
  "search_results": [
    {
      "title": "6 AI trends you'll see more of in 2025 - Microsoft Source",
      "url": "https://news.microsoft.com/source/features/ai/6-ai-trends-youll-see-more-of-in-2025/",

      "date": "2024-12-05",
      "last_updated": "2025-10-26",
      "snippet": "در سال 2025، هوش مصنوعی از یک ابزار برای کار و خانه به بخشی جدایی ناپذیر از هر دو تبدیل خواهد شد...",
      "source": "web"
    }
  ],
  "estimated_cost": {
    "unit": "0.0006010000",
    "irt": 65.03,
    "exchange_rate": 108200
  }
}
```

#### نمونه درخواست - Sonar Reasoning

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید"
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
    "model": "sonar",
    "messages": [
      {
        "role": "user",
        "content": "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="sonar",
    messages=[
        {
            "role": "user",
            "content": "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
        }
    ],
)

print(completion.choices[0].message.content)
# دسترسی به استنادات و نتایج جستجو
print(completion.citations)
print(completion.search_results)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "sonar",
  messages: [
    {
      role: "user",
      content: "آخرین پیشرفت‌ها در محاسبات کوانتومی چیست؟",
    },
  ],
});

console.log(completion.choices[0].message.content);
// دسترسی به استنادات و نتایج جستجو
console.log(completion.citations);
console.log(completion.search_results);

```

### استفاده از مدل‌های استدلال

برای مدل‌های استدلال مانند [`sonar-reasoning`](fa/providers/perplexity.md#sonar-reasoning) و [`sonar-reasoning-pro`](fa/providers/perplexity.md#sonar-reasoning-pro)، مدل فرآیند تفکر خود را نشان می‌دهد:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "چشم‌انداز رقابتی موتورهای جستجوی هوش مصنوعی را تحلیل کنید"
      }
    ],
    "max_tokens": 2048
  }'

python=:response = client.chat.completions.create(
    model="sonar-reasoning",
    messages=[
        {
            "role": "user",
            "content": "چشم‌انداز رقابتی موتورهای جستجوی هوش مصنوعی را تحلیل کنید",
        }
    ],
    max_tokens=2048,
)

# مدل فرآیند استدلال زنجیره‌ای خود را نشان خواهد داد
print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
    model: "sonar-reasoning",
    messages: [
        {
            role: "user",
            content: "چشم‌انداز رقابتی موتورهای جستجوی هوش مصنوعی را تحلیل کنید",
        },
    ],
    max_tokens: 2048,
});

// مدل فرآیند استدلال زنجیره‌ای خود را نشان خواهد داد
console.log(response.choices[0].message.content);

```

### پشتیبانی از نقاط پایانی API

**پشتیبانی کامل:**
- [`v1/chat/completions`](fa/guides/text-generation.md): پشتیبانی کامل از همه مدل‌های Perplexity Sonar
- [`v1/completions`](fa/guides/text-generation.md): پشتیبانی از فرمت تکمیل متن

**پشتیبانی جزئی:**
- [`v1/messages`](fa/guides/responses-vs-chat-completions.md): پیام‌های سبک Anthropic
- [`v1/responses`](fa/guides/responses-vs-chat-completions.md): فرمت پاسخ‌ها

### موارد استفاده بر اساس مدل

**Sonar**: جستجوهای سریع، بررسی صحت اطلاعات، خلاصه اخبار، پرسش و پاسخ ساده

**Sonar Pro**: سؤالات تحقیقاتی پیچیده، تحلیل تطبیقی، ترکیب اطلاعات

**Sonar Reasoning**: حل مسئله چند مرحله‌ای، تحلیل منطقی، برنامه‌ریزی استراتژیک

**Sonar Reasoning Pro**: تحلیل پیشرفته چند مرحله‌ای، وظایف استدلال عمیق، تصمیم‌گیری جامع

**Sonar Deep Research**: تحقیقات آکادمیک، تحلیل بازار، بررسی دقیق، تحقیقات تحقیقی

**Sonar Medium Chat**: مکالمات تعاملی، عملکرد متوازن هزینه برای وظایف جستجو

**Sonar Medium Online**: برنامه‌های حجم بالا که هزینه‌های توکن باید به حداقل برسند

---

## پیوندهای مرتبط

- [مستندات مدل‌های Perplexity](fa/providers/perplexity.md)
- [راهنمای تولید متن](fa/guides/text-generation.md)
- [ابزارهای جستجوی وب](fa/guides/tools-web-search.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [مرجع API - تکمیل چت](fa/guides/text-generation.md)
- [پاسخ‌های جریانی](fa/guides/streaming-responses.md)