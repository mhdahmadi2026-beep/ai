# Perplexity

Perplexity دو نوع سرویس ارائه می‌دهد:

1. **مدل‌های LLM**: مدل‌های پیشرفته هوش مصنوعی با یکپارچگی جستجوی وب بلادرنگ، استدلال زنجیره‌ای و قابلیت‌های تحقیق جامع
2. **سرویس جستجو** (`perplexity-search`): دسترسی مستقیم به قابلیت‌های جستجوی Perplexity از طریق [`v1/search`](fa/examples/using_v1_search.md) بدون نیاز به LLM

همه مدل‌های LLM درک قدرتمند زبان را با جستجوی وب زنده ترکیب می‌کنند تا پاسخ‌های مستند و دارای استناد ارائه دهند.

در داده فعلی AvalAI، مدل‌های Sonar را برای قابلیت‌های native Perplexity مانند `citations`، `search_results` و `search_context_size` از مسیر `/v1/chat/completions` فراخوانی کنید. مثال‌های Responses پایین صفحه الگوی مهاجرت هستند؛ فقط وقتی از آن‌ها استفاده کنید که مدل یا route انتخابی شما صراحتا از `/v1/responses` پشتیبانی کند.

## مدل‌های موجود

- [sonar](#sonar) - پاسخ‌های سریع با نتایج جستجوی قابل اعتماد
- [sonar-pro](#sonar-pro) - جستجوی پیشرفته با نتایج بهبود یافته
- [sonar-reasoning](#sonar-reasoning) - استدلال سریع با جستجوی بلادرنگ
- [sonar-reasoning-pro](#sonar-reasoning-pro) - استدلال پیشرفته با جستجوی جامع
- [sonar-deep-research](#sonar-deep-research) - تحقیق جامع در صدها منبع
- [perplexity-search](#api-جستجوی-مستقیم-بدون-llm) - جستجوی مستقیم بدون پاسخ LLM

## پشتیبانی از نقاط پایانی API

| قابلیت | endpoint پیشنهادی | نکته |
| --- | --- | --- |
| پاسخ‌های native مدل‌های Perplexity | `/v1/chat/completions` | بهترین مسیر برای مدل‌های Sonar، citationها، metadata جستجو و فیلدهای اختصاصی Perplexity. |
| workflowهای متنی به سبک Responses | `/v1/responses` | فقط با مدل یا route پشتیبانی‌شده استفاده کنید؛ `messages` را به `input` منتقل کنید و `output_text` را بخوانید. |
| فقط جستجوی مستقیم | `/v1/search` | برای گرفتن نتایج جستجو بدون متن تولیدشده از `perplexity-search` استفاده کنید. |

---

## sonar

**پاسخ‌های سریع با نتایج جستجوی قابل اعتماد**

یک مدل جستجوی سبک و مقرون به صرفه که برای پاسخ‌های سریع و مستند با جستجوی وب بلادرنگ بهینه شده است.

### ویژگی‌ها

- **مدل غیراستدلالی**: برای سرعت و مستقیم بودن بهینه شده
- **پنجره زمینه**: 128K توکن
- **جستجوی وب بلادرنگ**: جستجوی زنده با استنادات و ابرداده
- **مقرون به صرفه**: قیمت‌گذاری متوازن برای استفاده عمومی
- **بدون آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $1.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.50 به ازای 1M توکن |
| توکن‌های خروجی | $1.00 به ازای 1M توکن |
| زمینه جستجو (کم) | $5 به ازای 1K درخواست |
| زمینه جستجو (متوسط) | $8 به ازای 1K درخواست |
| زمینه جستجو (زیاد) | $12 به ازای 1K درخواست |

### موارد استفاده

- جستجوهای سریع و بررسی صحت اطلاعات
- خلاصه اخبار و رویدادهای جاری
- وظایف پرسش و پاسخ ساده
- تعاریف و توضیحات

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
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

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="sonar",
    messages=[{"role": "user", "content": "آخرین اخبار در تحقیقات هوش مصنوعی چیست؟"}],
)

print(response.choices[0].message.content)
print(f"استنادات: {response.citations}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "sonar",
  messages: [
    { role: "user", content: "آخرین اخبار در تحقیقات هوش مصنوعی چیست؟" }
  ]
});

console.log(response.choices[0].message.content);
console.log("استنادات:", response.citations);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `sonar` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="آخرین اخبار در تحقیقات هوش مصنوعی چیست؟",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "آخرین اخبار در تحقیقات هوش مصنوعی چیست؟",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "آخرین اخبار در تحقیقات هوش مصنوعی چیست؟",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## sonar-pro

**جستجوی پیشرفته با نتایج جستجوی بهبود یافته**

یک مدل جستجوی پیشرفته طراحی شده برای پرس‌وجوهای پیچیده که 2 برابر بیشتر از Sonar استاندارد نتایج جستجو با درک عمیق‌تر محتوا ارائه می‌دهد.

### ویژگی‌ها

- **مدل غیراستدلالی**: بازیابی اطلاعات پیشرفته
- **پنجره زمینه**: 200K توکن
- **نتایج جستجوی بهبود یافته**: 2 برابر بیشتر از Sonar
- **بهینه‌سازی پرس‌وجوهای پیچیده**: طراحی شده برای سؤالات چند مرحله‌ای
- **بدون آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $3.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $1.50 به ازای 1M توکن |
| توکن‌های خروجی | $15.00 به ازای 1M توکن |
| زمینه جستجو (کم) | $6 به ازای 1K درخواست |
| زمینه جستجو (متوسط) | $10 به ازای 1K درخواست |
| زمینه جستجو (زیاد) | $14 به ازای 1K درخواست |

### موارد استفاده

- سؤالات تحقیقاتی پیچیده
- تحلیل تطبیقی در چندین منبع
- ترکیب اطلاعات و گزارش‌دهی دقیق
- تحلیل عمیق بازار

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-pro",
    "messages": [
      {
        "role": "user",
        "content": "موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="sonar-pro",
    messages=[
        {
            "role": "user",
            "content": "موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید",
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "sonar-pro",
  messages: [
    { role: "user", content: "موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید" }
  ]
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `sonar-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "موقعیت رقابتی موتورهای جستجوی هوش مصنوعی در سال 2025 را تحلیل کنید",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## sonar-reasoning

**استدلال سریع با جستجوی بلادرنگ**

یک مدل متمرکز بر استدلال که استدلال زنجیره‌ای (CoT) را برای تحلیل ساختاری با جستجوی وب بلادرنگ اعمال می‌کند.

### ویژگی‌ها

- **مدل استدلالی**: قابلیت‌های زنجیره‌ای تفکر (CoT)
- **پنجره زمینه**: 128K توکن
- **استدلال سریع**: بهینه شده برای حل سریع مسئله
- **جستجوی وب بلادرنگ**: جستجوی زنده یکپارچه
- **بدون آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $1.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.50 به ازای 1M توکن |
| توکن‌های خروجی | $5.00 به ازای 1M توکن |
| زمینه جستجو (کم) | $5 به ازای 1K درخواست |
| زمینه جستجو (متوسط) | $8 به ازای 1K درخواست |
| زمینه جستجو (زیاد) | $14 به ازای 1K درخواست |

### موارد استفاده

- حل مسئله چند مرحله‌ای
- تحلیل منطقی و استدلال ساختاری
- برنامه‌ریزی استراتژیک و تصمیم‌گیری
- عیب‌یابی فنی با تحقیق

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید"
      }
    ],
    "max_tokens": 2048
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="sonar-reasoning",
    messages=[
        {
            "role": "user",
            "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید",
        }
    ],
    max_tokens=2048,
)

# مدل فرآیند استدلال زنجیره‌ای خود را نشان می‌دهد
print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "sonar-reasoning",
  messages: [
    { role: "user", content: "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید" }
  ],
  max_tokens: 2048
});

// مدل فرآیند استدلال زنجیره‌ای خود را نشان می‌دهد
console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `sonar-reasoning` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## sonar-reasoning-pro

**استدلال پیشرفته با جستجوی جامع**

استدلال زنجیره‌ای پیشرفته با 2 برابر نتایج جستجوی بیشتر برای وظایف تحلیل چند مرحله‌ای پیچیده.

### ویژگی‌ها

- **مدل استدلالی پیشرفته**: قابلیت‌های CoT بهبود یافته
- **پنجره زمینه**: 128K توکن
- **نتایج جستجوی بهبود یافته**: 2 برابر بیشتر از sonar-reasoning
- **وظایف چند مرحله‌ای پیچیده**: بهینه شده برای تحلیل عمیق
- **بدون آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $2.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $1.00 به ازای 1M توکن |
| توکن‌های خروجی | $8.00 به ازای 1M توکن |
| زمینه جستجو (کم) | $6 به ازای 1K درخواست |
| زمینه جستجو (متوسط) | $10 به ازای 1K درخواست |
| زمینه جستجو (زیاد) | $14 به ازای 1K درخواست |

### موارد استفاده

- تحلیل و استدلال چند مرحله‌ای پیچیده
- تحقیق پیشرفته با استدلال عمیق
- تصمیم‌گیری استراتژیک با تحلیل جامع
- تجزیه مسائل پیچیده

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-reasoning-pro",
    "messages": [
      {
        "role": "user",
        "content": "یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید"
      }
    ],
    "max_tokens": 4096
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="sonar-reasoning-pro",
    messages=[
        {
            "role": "user",
            "content": "یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید",
        }
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "sonar-reasoning-pro",
  messages: [
    { role: "user", content: "یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید" }
  ],
  max_tokens: 4096
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `sonar-reasoning-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک نقشه راه محصول دقیق برای یک پلتفرم مبتنی بر هوش مصنوعی توسعه دهید",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## sonar-deep-research

**تحقیق جامع در صدها منبع**

تحلیل موضوعی در سطح تخصصی با تولید گزارش دقیق، پشتیبانی از استناد و قابلیت‌های تحقیق جامع.

### ویژگی‌ها

- **مدل تحقیق عمیق**: تحقیق جامع چند منبعی
- **پنجره زمینه**: 128K توکن
- **تولید گزارش**: گزارش‌های دقیق و ساختاریافته
- **استنادات پیشرفته**: توکن‌های استناد برای ارجاع
- **توکن‌های استدلال**: قیمت‌گذاری جداگانه برای فرآیند استدلال
- **بدون آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $2.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $1.00 به ازای 1M توکن |
| توکن‌های خروجی | $8.00 به ازای 1M توکن |
| توکن‌های استدلال | $3.00 به ازای 1M توکن |
| توکن‌های استناد | $2.00 به ازای 1M توکن |
| پرس‌وجوی جستجو | $0.005 به ازای هر پرس‌وجو |
| زمینه جستجو (همه سطوح) | $5 به ازای 1K درخواست |

### موارد استفاده

- تحقیقات آکادمیک و گزارش‌های جامع
- تحلیل بازار و اطلاعات رقابتی
- بررسی دقیق و تحقیقات تحقیقی
- محتوای بلند با استنادات گسترده

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "sonar-deep-research",
    "messages": [
      {
        "role": "user",
        "content": "تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید"
      }
    ],
    "max_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="sonar-deep-research",
    messages=[
        {
            "role": "user",
            "content": "تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید",
        }
    ],
    max_tokens=8192,
)

print(response.choices[0].message.content)
# دسترسی به استنادات دقیق
print(f"استنادات: {response.citations}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response
 = await client.chat.completions.create({
  model: "sonar-deep-research",
  messages: [
    { role: "user", content: "تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید" }
  ],
  max_tokens: 8192
});

console.log(response.choices[0].message.content);
// دسترسی به استنادات دقیق
console.log("استنادات:", response.citations);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `sonar-deep-research` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "تحقیق جامع در مورد کاربردهای محاسبات کوانتومی در کشف دارو انجام دهید",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## API جستجوی مستقیم (بدون LLM)

علاوه بر استفاده از مدل‌های Perplexity از طریق تکمیل چت، می‌توانید مستقیما از طریق نقطه پایانی API [`v1/search`](fa/guides/tools-web-search.md) بدون فراخوانی LLM به قابلیت‌های جستجوی Perplexity دسترسی داشته باشید. این زمانی مفید است که فقط به نتایج جستجوی خام نیاز دارید.

### نام ابزار جستجو

از `perplexity-search` به عنوان شناسه ابزار جستجو استفاده کنید.

### نمونه درخواست (گزینه 1: ابزار جستجو در URL)

```bash
curl https://api.avalai.ir/v1/search/perplexity-search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "query": "آخرین پیشرفت‌های هوش مصنوعی 2024",
    "max_results": 5,
    "search_domain_filter": ["arxiv.org", "nature.com"],
    "country": "US"
  }'
```

### نمونه درخواست (گزینه 2: ابزار جستجو در بدنه)

```bash
curl https://api.avalai.ir/v1/search \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "search_tool_name": "perplexity-search",
    "query": "آخرین پیشرفت‌های هوش مصنوعی 2024",
    "max_results": 5
  }'
```

### پارامترها

- **`query`** (ضروری): رشته پرس‌وجوی جستجو
- **`max_results`** (اختیاری): حداکثر تعداد نتایج برای بازگشت
- **`search_domain_filter`** (اختیاری): آرایه دامنه‌ها برای فیلتر کردن نتایج
- **`country`** (اختیاری): کد کشور برای نتایج محلی‌سازی شده

برای اطلاعات بیشتر در مورد API جستجو، به [مستندات API جستجو](fa/news/2025-10-26-search-api-launched.md) مراجعه کنید.

---

## منابع مرتبط

- [راهنمای تولید متن](fa/guides/text-generation.md)
- [ابزارهای جستجوی وب](fa/guides/tools-web-search.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [پاسخ‌های جریانی](fa/guides/streaming-responses.md)
- [اخبار: افزودن مدل‌های Perplexity](fa/news/2025-10-26-perplexity-sonar-models-added.md)
