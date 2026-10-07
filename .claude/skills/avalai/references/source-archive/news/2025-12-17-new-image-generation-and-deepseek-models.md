# مدل‌های جدید اضافه شدند: GPT-Image-1.5، FLUX.2 Pro و DeepSeek-V3.2 روی Azure AI

**تاریخ:** ۱۴۰۴-۰۹-۲۶ / (2025-12-17)

## خلاصه

AvalAI چهار مدل جدید معرفی می‌کند: GPT-Image-1.5 از OpenAI با قابلیت‌های پیشرفته تولید تصویر، FLUX.2 Pro از Black Forest Labs با هوش بصری چندمرجعی، و مدل‌های DeepSeek-V3.2 میزبانی شده روی Azure AI با محدودیت‌های نرخ بهتر و تاخیر کمتر.

---

## جزئیات

### OpenAI - GPT-Image-1.5

GPT-Image-1.5 جدیدترین مدل تولید تصویر OpenAI است که بهبودهای قابل توجهی در واقع‌گرایی، دقت و قابلیت ویرایش نسبت به GPT-Image-1 ارائه می‌دهد. [مستندات](fa/providers/openai.md)

**قابلیت‌های کلیدی:**

- **فوتورئالیسم با وضوح بالا** با نورپردازی طبیعی، مواد دقیق و رندر رنگ غنی
- **توازن انعطاف‌پذیر کیفیت-تاخیر** برای تولید سریع‌تر در تنظیمات پایین‌تر
- **حفظ قوی چهره و هویت** برای ویرایش، سازگاری شخصیت و گردش‌های کاری چند مرحله‌ای
- **رندر متن قابل اعتماد** با حروف واضح، چیدمان یکپارچه و کنتراست قوی در تصاویر
- **بصری‌های ساختاریافته پیچیده** شامل اینفوگرافیک، نمودارها و ترکیبات چند پنلی
- **کنترل دقیق سبک و انتقال سبک** با حداقل پرامپت

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | تولید و ویرایش تصویر |
| ورودی | متن، تصویر |
| خروجی | تصویر، متن |
| اندپوینت‌های پشتیبانی | `v1/images/generations`، `v1/images/edits` |
| نقاط قوت | فوتورئالیسم پیشرفته، رندر متن، انتقال سبک |
| بهترین کاربرد | طراحی حرفه‌ای، خلاقیت‌های بازاریابی، اینفوگرافیک، موکاپ محصول |

> **💡 نکته زبان:** GPT-Image-1.5 از پرامپت‌های چندزبانه پشتیبانی می‌کند و با پرامپت‌های فارسی و انگلیسی به خوبی کار می‌کند.

**قیمت‌گذاری:**

| نوع توکن | قیمت به ازای ۱ میلیون توکن |
|----------|---------------------------|
| ورودی متن | $5.00 |
| ورودی متن کش شده | $2.00 |
| خروجی متن | $32.00 |
| ورودی تصویر | $8.00 |
| خروجی تصویر | $32.00 |

---

### Black Forest Labs - FLUX.2 Pro

FLUX.2 Pro مدل پیشرفته تولید تصویر Black Forest Labs است با هوش بصری چندمرجعی، جزئیات بی‌سابقه، دقت رنگ و استدلال فضایی. [مستندات](fa/providers/bfl.md)

**قابلیت‌های کلیدی:**

- **چندمرجعی**: ترکیب عناصر از حداکثر ۸ تصویر (API) با حفظ هویت در صحنه‌های پیچیده
- **فوتورئالیسم و جزئیات**: تولید تصاویر فوتورئالیستیک با جزئیات استثنایی
- **تایپوگرافی و متن**: تخصصی برای رندر متن و حفظ جزئیات کوچک
- **کنترل دقیق رنگ**: تطبیق دقیق رنگ هگز و پرامپت‌نویسی ساختاریافته
- **آماده تولید**: تولید تصویر با کیفیت بالا و درجه تولید در مقیاس

| ویژگی | جزئیات |
|-------|--------|
| نوع مدل | تولید تصویر |
| حداکثر رزولوشن | تا ۴ مگاپیکسل (4096x4096) |
| چندمرجعی | تا ۸ تصویر ورودی (API)، ۱۰ (playground) |
| اندپوینت‌های پشتیبانی | `v1/images/generations` |
| نقاط قوت | ترکیب چندمرجعی، دقت رنگ، تایپوگرافی |
| بهترین کاربرد | بازاریابی محصول، پلتفرم‌های خلاق، تصاویر غذا، فیلم‌سازی |

**قیمت‌گذاری:**

| مؤلفه | قیمت |
|-------|------|
| تصویر تولید شده (۱ مگاپیکسل) | $0.03 |
| هر مگاپیکسل اضافی | $0.015 |
| تصویر مرجع (به ازای مگاپیکسل) | $0.015 |

**نکات قیمت‌گذاری:**
- ۱ مگاپیکسل = ۱۰۲۴x۱۰۲۴ پیکسل
- رزولوشن به مگاپیکسل بعدی گرد می‌شود
- تصاویر بزرگتر از ۴ مگاپیکسل به ۴ مگاپیکسل تغییر اندازه می‌دهند

> **⚠️ نکته مهم زبان:** FLUX.2 Pro برای پرامپت‌های انگلیسی بهینه شده است. برای بهترین نتایج، از پرامپت‌های انگلیسی هنگام تولید تصویر با مدل‌های FLUX استفاده کنید. پرامپت‌های غیرانگلیسی ممکن است نتایج ناسازگار تولید کنند.

---

### DeepSeek - DeepSeek-V3.2 و DeepSeek-V3.2-Speciale (از طریق Azure AI)

مدل‌های DeepSeek-V3.2 اکنون از طریق Azure AI در دسترس هستند و محدودیت‌های نرخ بهتر و تاخیر کمتر نسبت به دسترسی مستقیم API DeepSeek ارائه می‌دهند. [مستندات](fa/providers/deepseek.md)

**DeepSeek-V3.2** کارایی محاسباتی بالا را با استدلال برتر و عملکرد عامل هماهنگ می‌کند و از DeepSeek Sparse Attention (DSA) برای سناریوهای کارآمد با متن بلند استفاده می‌کند.

**DeepSeek-V3.2-Speciale** یک نوع با محاسبات بالا است که از GPT-5 پیشی گرفته و مهارت استدلال هم‌سطح با Gemini-3.0-Pro را نشان می‌دهد. این مدل در المپیاد بین‌المللی ریاضی ۲۰۲۵ (IMO) و المپیاد بین‌المللی انفورماتیک (IOI) به عملکرد مدال طلا دست یافت.

| ویژگی | DeepSeek-V3.2 | DeepSeek-V3.2-Speciale |
|-------|---------------|------------------------|
| ارائه‌دهنده | Azure AI | Azure AI |
| پنجره متن | ۱۲۸K توکن | ۱۲۸K توکن |
| حالت | بدون تفکر (کارآمد) | استدلال عمیق (تفکر) |
| فراخوانی ابزار | ✓ پشتیبانی می‌شود | ✗ پشتیبانی نمی‌شود |
| نقاط قوت | پاسخ سریع، پردازش کارآمد | استدلال سطح متخصص، عملکرد سطح المپیاد |
| بهترین کاربرد | چت عمومی، وظایف عاملی | ریاضیات پیچیده، برنامه‌نویسی رقابتی، تحقیق |
| اندپوینت‌های پشتیبانی | `v1/chat/completions`، `v1/completions`، `v1/responses`، `v1/messages` | `v1/chat/completions`، `v1/completions`، `v1/responses`، `v1/messages` |

**قیمت‌گذاری (هر دو مدل):**

| نوع توکن | قیمت به ازای ۱ میلیون توکن |
|----------|---------------------------|
| ورودی | $0.28 |
| ورودی کش شده | $0.028 |
| خروجی | $0.42 |

**مزایای میزبانی Azure AI:**

- **محدودیت‌های نرخ بهتر**: توان عملیاتی بالاتر نسبت به API مستقیم DeepSeek
- **تاخیر کمتر**: زمان پاسخ سریع‌تر از طریق زیرساخت جهانی Azure
- **قابلیت اطمینان بهتر**: دسترسی‌پذیری و عملکرد در سطح سازمانی

---

## مثال‌های درخواست/پاسخ API

### تولید تصویر GPT-Image-1.5

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-1.5",
    "prompt": "یک عکس کاندید فوتورئالیستیک از یک ملوان سالخورده ایستاده روی یک قایق ماهیگیری کوچک با پوست آفتاب‌زده و خالکوبی‌های سنتی",
    "size": "1024x1024",
    "quality": "high",
    "n": 1,
    "response_format": "b64_json"
  }'
```

**پاسخ نمونه:**

```json
{
  "created": 1765933200,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQA...[TRUNCATED]",
      "revised_prompt": "یک عکس کاندید فوتورئالیستیک..."
    }
  ],
  "usage": {
    "prompt_tokens": 45,
    "completion_tokens": 1024,
    "total_tokens": 1069
  },
  "estimated_cost": {
    "unit": "0.0328800000",
    "irt": 4321.08,
    "exchange_rate": 131400
  }
}
```

### ویرایش تصویر GPT-Image-1.5

```bash
curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gpt-image-1.5" \
  -F "image=@input_image.png" \
  -F "prompt=آن را شبیه یک عصر زمستانی با بارش برف کن" \
  -F "size=1024x1024"
```

### تولید تصویر FLUX.2 Pro

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "flux.2-pro",
    "prompt": "یک هدشات حرفه‌ای از یک زن تاجر مطمئن در یک دفتر مدرن، نورپردازی طبیعی نرم، عمق میدان کم",
    "size": "1024x1024",
    "n": 1,
    "response_format": "b64_json"
  }'
```

**پاسخ نمونه:**

```json
{
  "created": 1765933200,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQA...[TRUNCATED]"
    }
  ],
  "estimated_cost": {
    "unit": "0.0300000000",
    "irt": 3942.0,
    "exchange_rate": 131400
  }
}
```

### تکمیل چت DeepSeek-V3.2

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v3.2",
    "messages": [
      {
        "role": "user",
        "content": "درهم‌تنیدگی کوانتومی را به زبان ساده توضیح بده"
      }
    ]
  }'
```

**پاسخ نمونه:**

```json
{
  "id": "chatcmpl-abc123",
  "created": 1765933200,
  "model": "deepseek-v3.2",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "درهم‌تنیدگی کوانتومی پدیده‌ای است که در آن دو یا چند ذره به گونه‌ای به هم متصل می‌شوند که حالت کوانتومی هر ذره را نمی‌توان به طور مستقل توصیف کرد...",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 245,
    "prompt_tokens": 12,
    "total_tokens": 257
  },
  "estimated_cost": {
    "unit": "0.0001063800",
    "irt": 13.98,
    "exchange_rate": 131400
  }
}
```

### استدلال DeepSeek-V3.2-Speciale

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v3.2-speciale",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد"
      }
    ],
    "max_tokens": 4096
  }'
```

---

## مثال‌های استفاده از SDK

### GPT-Image-1.5

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-1.5",
    "prompt": "یک اینفوگرافیک دقیق که نحوه کار دستگاه قهوه‌ساز را توضیح می‌دهد ایجاد کن",
    "size": "1024x1024",
    "quality": "high",
    "n": 1,
    "response_format": "b64_json"
  }'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="gpt-image-1.5",
    prompt="یک اینفوگرافیک دقیق که نحوه کار دستگاه قهوه‌ساز را توضیح می‌دهد ایجاد کن",
    size="1024x1024",
    quality="high",
    n=1,
    response_format="b64_json",
)

# ذخیره تصویر
img_data = base64.b64decode(response.data[0].b64_json)
with open("infographic.png", "wb") as f:
    f.write(img_data)

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "gpt-image-1.5",
  prompt: "یک اینفوگرافیک دقیق که نحوه کار دستگاه قهوه‌ساز را توضیح می‌دهد ایجاد کن",
  size: "1024x1024",
  quality: "high",
  n: 1,
  response_format: "b64_json",
});

// ذخیره تصویر
const imgData = Buffer.from(response.data[0].b64_json, "base64");
fs.writeFileSync("infographic.png", imgData);

```

### FLUX.2 Pro

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "flux.2-pro",
    "prompt": "یک منظره کوهستانی آرام در غروب خورشید با دریاچه انعکاسی",
    "size": "1024x1024",
    "n": 1,
    "response_format": "b64_json"
  }'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="flux.2-pro",
    prompt="یک منظره کوهستانی آرام در غروب خورشید با دریاچه انعکاسی",
    size="1024x1024",
    n=1,
    response_format="b64_json",
)

# ذخیره تصویر
img_data = base64.b64decode(response.data[0].b64_json)
with open("landscape.png", "wb") as f:
    f.write(img_data)

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "flux.2-pro",
  prompt: "یک منظره کوهستانی آرام در غروب خورشید با دریاچه انعکاسی",
  size: "1024x1024",
  n: 1,
  response_format: "b64_json",
});

// ذخیره تصویر
const imgData = Buffer.from(response.data[0].b64_json, "base64");
fs.writeFileSync("landscape.png", imgData);

```

### DeepSeek-V3.2 (Azure AI)

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v3.2",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی بنویس"
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="deepseek-v3.2",
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی بنویس",
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
  model: "deepseek-v3.2",
  messages: [
    {
      role: "user",
      content: "یک تابع پایتون برای پیاده‌سازی درخت جستجوی دودویی بنویس",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Black Forest Labs](fa/providers/bfl.md)
- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API - تصاویر](fa/api-reference/images.md)
- [قیمت‌گذاری](fa/pricing.md)