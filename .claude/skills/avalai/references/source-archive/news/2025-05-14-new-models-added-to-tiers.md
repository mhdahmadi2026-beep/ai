# افزودن مدل‌های o1-pro و o3 به سطوح دسترسی AvalAI

**تاریخ:** 1404-02-25 (2025-05-14)

## خلاصه

ما مفتخریم که دسترسی به مدل‌های قدرتمند استدلالی OpenAI، o1-pro و o3، را در چندین سطح دسترسی پلتفرم AvalAI اعلام کنیم. مدل o1-pro اکنون برای کاربران در سطوح دسترسی 4 و 5 قابل دسترسی است، در حالی که مدل o3 در سطوح دسترسی 3، 4 و 5 در دسترس است. این بروزرسانی، ارائه مدل‌های پیشرفته استدلالی ما را گسترش می‌دهد و گزینه‌های بیشتری برای وظایف پیچیده که نیازمند تحلیل عمیق متن و تصاویر هستند، فراهم می‌کنند.

---

## جزئیات

### مدل OpenAI o3

مدل o3، قدرتمندترین مدل استدلالی OpenAI است که استاندارد جدیدی برای وظایف ریاضی، علمی، کدنویسی و استدلال تصویری تعیین می‌کند. این مدل در نگارش فنی و پیروی از دستورالعمل‌ها برتری دارد و آن را برای سناریوهای حل مسائل پیچیده ایده‌آل می‌سازد.

**ویژگی‌های کلیدی:**

- قابلیت‌های استدلال استثنایی در تمام حوزه‌ها
- پنجره زمینه 200,000 توکنی
- حداکثر 100,000 توکن خروجی
- تاریخ قطع دانش: 31 مه 2024
- پشتیبانی از ورودی‌های متنی و تصویری
- خروجی به فرمت متن

**دسترسی در سطوح:**

- سطح 3
- سطح 4
- سطح 5

### مدل OpenAI o1-pro

مدل o1-pro نسخه‌ای از o1 با قدرت محاسباتی بیشتر برای پاسخ‌های بهتر است. این مدل با یادگیری تقویتی آموزش دیده تا قبل از پاسخ دادن فکر کند و استدلال‌های پیچیده انجام دهد، با استفاده از منابع محاسباتی اضافی برای تفکر عمیق‌تر و ارائه پاسخ‌های به طور مداوم بهتر.

**ویژگی‌های کلیدی:**

- قابلیت‌های استدلال بالاتر
- پنجره زمینه 200,000 توکنی
- حداکثر 100,000 توکن خروجی
- تاریخ قطع دانش: 30 سپتامبر 2023
- پشتیبانی از ورودی‌های متنی و تصویری
- خروجی به فرمت متن

**دسترسی در سطوح:**

- سطح 4
- سطح 5

### نمونه استفاده

شما می‌توانید به این مدل‌ها از طریق نقاط پایانی استاندارد API ما دسترسی پیدا کنید. در اینجا نمونه‌هایی از نحوه استفاده از آنها آورده شده است:

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# Using the o3 model
completion = client.chat.completions.create(
    model="o3",
    messages=[
        {
            "role": "user",
            "content": "Explain quantum computing principles and their potential impact on cryptography.",
        }
    ],
)

print(completion.choices[0].message.content)

# Using the o1-pro model
completion = client.chat.completions.create(
    model="o1-pro",
    messages=[
        {
            "role": "user",
            "content": "Analyze the implications of quantum computing on modern encryption standards.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// Using the o3 model
async function useO3Model() {
  const completion = await client.chat.completions.create({
    model: "o3",
    messages: [
      {
        role: "user",
        content:
          "Explain quantum computing principles and their potential impact on cryptography.",
      },
    ],
  });

  console.log(completion.choices[0].message.content);
}

// Using the o1-pro model
async function useO1ProModel() {
  const completion = await client.chat.completions.create({
    model: "o1-pro",
    messages: [
      {
        role: "user",
        content:
          "Analyze the implications of quantum computing on modern encryption standards.",
      },
    ],
  });

  console.log(completion.choices[0].message.content);
}

useO3Model();
useO1ProModel();

```

## پیوندهای مرتبط

* [فهرست مدل‌ها](fa/models/index.md)
* [مرجع API Chat Completions](fa/api-reference/chat.md)
* [راهنمای انتخاب مدل](fa/guides/model-selection.md)