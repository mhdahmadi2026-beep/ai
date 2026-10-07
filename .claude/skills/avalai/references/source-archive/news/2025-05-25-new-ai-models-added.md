# مدل‌های جدید هوش مصنوعی اضافه شدند: Codestral، Gemma 3 و Imagen 4.0

**تاریخ:** 1404-03-05 / (2025-05-25)

## خلاصه

چندین مدل قدرتمند جدید هوش مصنوعی به پلتفرم AvalAI اضافه شده‌اند. این به‌روزرسانی شامل Codestral-2501 از Mistral AI برای تولید کد پیشرفته، خانواده مدل‌های Gemma 3 از Google با قابلیت‌های چندرسانه‌ای، و جدیدترین مدل‌های تولید تصویر Imagen 4.0 از Google است. این تغییرات به طور قابل توجهی قابلیت‌های پلتفرم ما را برای تولید کد، پردازش متن چندزبانه و ایجاد تصاویر با کیفیت بالا گسترش می‌دهند.

---

## جزئیات

این به‌روزرسانی چندین مدل پیشرفته هوش مصنوعی را به پلتفرم AvalAI می‌آورد و خدمات ما را در چندین حوزه تقویت می‌کند. موارد جدید عبارتند از:

### Mistral AI

* **codestral-2501**: یک مدل قدرتمند با ۲۲ میلیارد پارامتر که برای تولید کد در بیش از ۸۰ زبان برنامه‌نویسی تخصصی شده است. این مدل در تکمیل توابع کدنویسی، نوشتن تست‌ها و تکمیل کد ناقص با استفاده از مکانیسم پر کردن میانی (fill-in-the-middle) برتری دارد. این مدل از زبان‌های Python، Java، C، C++، JavaScript، Bash، Swift، Fortran و بسیاری دیگر پشتیبانی می‌کند. [مستندات](fa/models/codestral-2501.md)

### گوگل جما

* **gemma-3-1b-it**: یک مدل سبک فقط متنی با آموزش دستورالعمل، مناسب برای برنامه‌های با منابع محاسباتی محدود در عین ارائه عملکرد مطلوب. [مستندات](fa/models/gemma-3-1b-it.md)
* **gemma-3-4b-it**: یک مدل چندرسانه‌ای متعادل که از ورودی‌های متن و تصویر با پنجره زمینه ۱۲۸ هزار توکنی پشتیبانی می‌کند. [مستندات](fa/models/gemma-3-4b-it.md)
* **gemma-3-12b-it**: یک مدل چندرسانه‌ای قدرتمندتر با قابلیت‌های استدلال پیشرفته و پشتیبانی از بیش از ۱۴۰ زبان. [مستندات](fa/models/gemma-3-12b-it.md)
* **gemma-3-27b-it**: بزرگترین مدل Gemma 3، با ارائه عملکرد برتر برای وظایف پیچیده با ورودی‌های تصویر و متن. [مستندات](fa/models/gemma-3-27b-it.md)
* **gemma-3n-e4b-it**: یک مدل تخصصی کارآمد با ۴ میلیارد پارامتر که برای موارد استفاده خاص بهینه‌سازی شده است. [مستندات](fa/models/gemma-3n-e4b-it.md)

### گوگل Imagen

* **imagen-4.0-generate-preview-05-20**: جدیدترین نسخه پیش‌نمایش مدل تولید تصویر Imagen 4.0 از گوگل. [مستندات](fa/models/imagen-4.0-generate-preview-05-20.md)
* **imagen-4.0-ultra-generate-exp-05-20**: نسخه آزمایشی با کیفیت فوق‌العاده بالای Imagen 4.0 برای تولید تصاویر فوق‌العاده دقیق و واقع‌گرایانه. [مستندات](fa/models/imagen-4.0-ultra-generate-exp-05-20.md)
* **imagen-3.0-generate-002**: نسخه به‌روزرسانی شده Imagen 3.0 با قابلیت‌های پیشرفته تولید تصویر. [مستندات](fa/models/imagen-3.0-generate-002.md)
* **imagen-3.0-generate-001**: مدل پایه Imagen 3.0 برای تولید تصاویر با کیفیت بالا. [مستندات](fa/models/imagen-3.0-generate-001.md)
* **imagen-3.0-fast-generate-001**: نسخه سریع‌تر Imagen 3.0 که برای کاهش تاخیر با حفظ کیفیت خوب بهینه‌سازی شده است. [مستندات](fa/models/imagen-3.0-fast-generate-001.md)

### امبدینگ‌ها

* **gemini-embedding-exp-03-07**: مدل آزمایشی امبدینگ Gemini از گوگل برای ایجاد نمایش‌های برداری با کیفیت بالا از متن. [مستندات](fa/models/gemini-embedding-exp-03-07.md)

## مثال‌های استفاده

### استفاده از Codestral برای تولید کد

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="codestral-2501",
    messages=[
        {
            "role": "user",
            "content": "یک تابع پایتون بنویس که بررسی کند آیا یک رشته پالیندروم است یا خیر.",
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
  model: "codestral-2501",
  messages: [
    {
      role: "user",
      content:
        "یک تابع پایتون بنویس که بررسی کند آیا یک رشته پالیندروم است یا خیر.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### استفاده از مدل‌های Gemma 3 برای وظایف چندرسانه‌ای

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemma-3-12b-it",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چه چیزی وجود دارد؟"},
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

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemma-3-12b-it",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "در این تصویر چه چیزی وجود دارد؟" },
        {
          type: "image_url",
          image_url: { url: "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png" },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

### تولید تصاویر با Imagen 4.0

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="imagen-4.0-generate-preview-05-20",
    prompt="یک شهر آینده‌نگر با ماشین‌های پرنده و باغ‌های عمودی روی آسمان‌خراش‌ها",
    n=1,
    size="1024x1024",
    response_format="url",  # or b64_json
)

image_url = response.data[0].url
print(f"آدرس تصویر تولید شده: {image_url}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "imagen-4.0-generate-preview-05-20",
  prompt:
    "یک شهر آینده‌نگر با ماشین‌های پرنده و باغ‌های عمودی روی آسمان‌خراش‌ها",
  n: 1,
  size: "1024x1024",
  response_format: "url", // or b64_json
});

const imageUrl = response.data[0].url;
console.log(`آدرس تصویر تولید شده: ${imageUrl}`);

```

### ایجاد امبدینگ‌ها با Gemini

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    input="روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد", model="gemini-embedding-exp-03-07"
)

embeddings = response.data[0].embedding
print(f"بردار امبدینگ (۵ مقدار اول): {embeddings[:5]}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  input: "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد",
  model: "gemini-embedding-exp-03-07",
});

const embeddings = response.data[0].embedding;
console.log(`بردار امبدینگ (۵ مقدار اول): ${embeddings.slice(0, 5)}`);

```

---

## لینک‌های مرتبط

- [مستندات Codestral](fa/models/codestral-2501.md)
- [راهنمای تولید تصویر Imagen 4.0](fa/guides/image-generation.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [مرجع API](fa/api-reference/introduction.md)