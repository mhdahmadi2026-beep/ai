# انتشار مدل‌های پایدار Gemini 2.5: معرفی نام‌های جدید مدل‌ها

**تاریخ:** 1404-04-08 / (2025-06-28)

## خلاصه

گوگل به طور رسمی مدل‌های پایدار سری Gemini 2.5 را منتشر کرد. نام‌های جدید مدل‌های پایدار [`gemini-2.5-flash`](fa/models/gemini-2.5-flash.md) و [`gemini-2.5-pro`](fa/models/gemini-2.5-pro.md) اکنون در دسترس قرار گرفته‌اند و جایگزین نسخه‌های پیش‌نمایش قبلی شده‌اند. علاوه بر این، مدل جدید [`gemma-3n-e2b-it`](fa/models/gemma-3n-e2b-it.md) به سری Gemma و مدل آزمایشی [`gemini-2.5-flash-lite-preview-06-17`](fa/models/gemini-2.5-flash-lite-preview-06-17.md) نیز اضافه شده‌اند.

---

## جزئیات

این به‌روزرسانی با انتشار مدل‌های پایدار، بهبودهای قابل توجهی را برای سری Gemini 2.5 به ارمغان می‌آورد. کاربران باید برای افزایش قابلیت اطمینان و بهبود عملکرد، از نسخه‌های پیش‌نمایش به نام‌های جدید مدل‌های پایدار مهاجرت کنند.

### مدل‌های پایدار گوگل Gemini 2.5

* **gemini-2.5-flash**: نسخه پایدار مدل سریع و کارآمد Gemini 2.5 گوگل که برای سرعت بهینه‌سازی شده و در عین حال خروجی‌های با کیفیت بالا ارائه می‌دهد. این مدل جایگزین نسخه‌های پیش‌نمایش شده و پایداری بهتری برای استفاده در تولید ارائه می‌دهد. [مستندات](fa/models/gemini-2.5-flash.md)

* **gemini-2.5-pro**: نسخه پایدار قدرتمندترین مدل Gemini 2.5 گوگل که استدلال پیشرفته و درک جامع زبان ارائه می‌دهد. این نسخه آماده تولید از مدل‌های پیش‌نمایش قبلی در دسترس است. [مستندات](fa/models/gemini-2.5-pro.md)

### راهنمای مهاجرت برای مدل‌های پیش‌نمایش

اگر در حال حاضر از نام‌های مدل پیش‌نمایش استفاده می‌کنید، لطفا کد خود را برای استفاده از نسخه‌های جدید پایدار به‌روزرسانی کنید:

#### مهاجرت Gemini 2.5 Pro
- **از:** `gemini-2.5-pro-preview-06-05` → **به:** `gemini-2.5-pro`
- **از:** `gemini-2.5-pro-preview-05-06` → **به:** `gemini-2.5-pro`

#### مهاجرت Gemini 2.5 Flash
- **از:** `gemini-2.5-flash-preview-04-17` → **به:** `gemini-2.5-flash`
- **از:** `gemini-2.5-flash-preview-05-20` → **به:** `gemini-2.5-flash`

### مدل جدید Gemma

* **gemma-3n-e2b-it**: یک اضافه جدید به سری Gemma با قابلیت‌های پیشرفته و عملکرد بهینه‌سازی شده برای وظایف پیروی از دستورالعمل. [مستندات](fa/models/gemma-3n-e2b-it.md)

### مدل آزمایشی جدید

* **gemini-2.5-flash-lite-preview-06-17**: نسخه آزمایشی سبک Gemini 2.5 Flash که برای برنامه‌های نیازمند زمان پاسخ سریع‌تر با نیازهای محاسباتی کاهش یافته طراحی شده است. [مستندات](fa/models/gemini-2.5-flash-lite-preview-06-17.md)

## مثال‌های استفاده

### استفاده از مدل‌های جدید پایدار Gemini 2.5

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از مدل پایدار Gemini 2.5 Flash
completion = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": "مزایای استفاده از نسخه‌های پایدار مدل نسبت به نسخه‌های پیش‌نمایش را توضیح دهید.",
        }
    ],
)

print(completion.choices[0].message.content)

# استفاده از مدل پایدار Gemini 2.5 Pro
completion = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[
        {
            "role": "user",
            "content": "تاثیر پایداری مدل هوش مصنوعی بر برنامه‌های تولیدی را تحلیل کنید.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// استفاده از مدل پایدار Gemini 2.5 Flash
const flashCompletion = await client.chat.completions.create({
  model: "gemini-2.5-flash",
  messages: [
    {
      role: "user",
      content:
        "مزایای استفاده از نسخه‌های پایدار مدل نسبت به نسخه‌های پیش‌نمایش را توضیح دهید.",
    },
  ],
});

console.log(flashCompletion.choices[0].message.content);

// استفاده از مدل پایدار Gemini 2.5 Pro
const proCompletion = await client.chat.completions.create({
  model: "gemini-2.5-pro",
  messages: [
    {
      role: "user",
      content:
        "تاثیر پایداری مدل هوش مصنوعی بر برنامه‌های تولیدی را تحلیل کنید.",
    },
  ],
});

console.log(proCompletion.choices[0].message.content);

```

### استفاده از مدل جدید Gemma

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gemma-3n-e2b-it",
    messages=[
        {
            "role": "user",
            "content": "توضیح مفصلی از مفاهیم یادگیری ماشین برای مبتدیان بنویسید.",
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
  model: "gemma-3n-e2b-it",
  messages: [
    {
      role: "user",
      content: "توضیح مفصلی از مفاهیم یادگیری ماشین برای مبتدیان بنویسید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات Gemini 2.5 Flash](fa/models/gemini-2.5-flash.md)
- [مستندات Gemini 2.5 Pro](fa/models/gemini-2.5-pro.md)
- [مستندات Gemma 3n E2B IT](fa/models/gemma-3n-e2b-it.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [مرجع API](fa/api-reference/introduction.md)