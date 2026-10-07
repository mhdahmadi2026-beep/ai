# اعلان منسوخ شدن مدل‌های گوگل جمینای

**تاریخ:** 1404-07-05 / (2025-09-27)

## خلاصه

گوگل چندین مدل جمینای را از طریق API رسمی خود منسوخ کرده است. این مدل‌ها دیگر برای درخواست‌های جدید در دسترس نخواهند بود و پیاده‌سازی‌های موجود باید به گزینه‌های پشتیبانی شده مهاجرت کنند تا از ادامه ارائه خدمات اطمینان حاصل کنند.

---

## جزئیات

### مدل‌های منسوخ شده

مدل‌های گوگل جمینای زیر به طور رسمی توسط API جمینای گوگل منسوخ شده‌اند و دیگر از طریق AvalAI در دسترس نیستند:

#### مدل‌های اصلی جمینای
- **gemini-pro** - مدل عمومی قدیمی
- **gemini-1.5-pro** - مدل نسل قبلی پرو
- **gemini-1.5-pro-002** - نسخه خاص
- **gemini-1.5-pro-001** - نسخه خاص
- **gemini-1.5-pro-latest** - اشاره‌گر آخرین نسخه (منسوخ شده)

#### نسخه‌های آزمایشی
- **gemini-1.5-pro-exp-0801** - نسخه آزمایشی آگوست 2024
- **gemini-1.5-pro-exp-0827** - نسخه آزمایشی 27 آگوست 2024
- **gemini-2.0-flash-exp** - مدل آزمایشی Flash 2.0
- **gemini-exp-1114** - مدل آزمایشی 14 نوامبر
- **gemini-exp-1206** - مدل آزمایشی 6 دسامبر

#### مدل‌های Flash
- **gemini-1.5-flash-latest** - اشاره‌گر آخرین مدل flash
- **gemini-1.5-flash-8b** - مدل flash با 8 میلیارد پارامتر
- **gemini-1.5-flash-8b-exp-0924** - نسخه آزمایشی flash 24 سپتامبر
- **gemini-1.5-flash-exp-0827** - نسخه آزمایشی flash 27 آگوست
- **gemini-1.5-flash-8b-exp-0827** - نسخه آزمایشی flash 8B 27 آگوست

### تاثیر بر کاربران

- **تاثیر فوری**: این مدل‌ها دیگر درخواست‌های جدید را نمی‌پذیرند
- **پیاده‌سازی‌های موجود**: هر برنامه‌ای که از این نام‌های مدل استفاده کند، پاسخ خطا دریافت خواهد کرد
- **پاسخ‌های API**: درخواست‌های ارسالی به مدل‌های منسوخ شده، پیام‌های خطای مناسب مبنی بر عدم دسترسی مدل را برمی‌گردانند

### مسیر مهاجرت توصیه شده

کاربران باید به مدل‌های گوگل جمینای پشتیبانی شده فعلی که از طریق AvalAI در دسترس هستند مهاجرت کنند. لطفا برای آخرین مدل‌های جمینای موجود و قابلیت‌های آن‌ها به مستندات مدل ما مراجعه کنید.

**مدل‌های پایدار فعلی:**
- **gemini-2.0-flash** - مدل flash نسل 2.0
- **gemini-2.0-flash-lite** - نسخه سبک flash نسل 2.0
- **gemini-2.5-pro** - مدل پرو نسل 2.5
- **gemini-2.5-flash** - مدل flash نسل 2.5
- **gemini-2.5-flash-lite** - نسخه سبک flash نسل 2.5

**مراحل مهاجرت:**

1. **شناسایی استفاده**: پیاده‌سازی‌های فعلی خود را بررسی کنید تا مشخص کنید کدام مدل‌های منسوخ شده را استفاده می‌کنید
2. **انتخاب جایگزین**: از میان مدل‌های جمینای پشتیبانی شده فعلی بر اساس نیازهای موردی خود انتخاب کنید
3. **به‌روزرسانی کد**: پارامتر مدل در فراخوانی‌های API خود را برای استفاده از نام‌های مدل جدید تغییر دهید
4. **تست یکپارچگی**: تایید کنید که برنامه‌های شما با مدل‌های جدید به درستی کار می‌کنند
5. **نظارت بر عملکرد**: اطمینان حاصل کنید که مدل‌های جایگزین نیازهای عملکرد و کیفیت شما را برآورده می‌کنند

### مثال مهاجرت

اگر از یک مدل منسوخ شده استفاده می‌کردید، پیاده‌سازی خود را به‌روزرسانی کنید:

```language-selector
bash=:# قبل (منسوخ شده)
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-1.5-pro-latest",
    "messages": [
      {
        "role": "user",
        "content": "پرامپت شما اینجا."
      }
    ]
  }'

# بعد (استفاده از مدل پشتیبانی شده فعلی)
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-pro",
    "messages": [
      {
        "role": "user",
        "content": "پرامپت شما اینجا."
      }
    ]
  }'

python=:# قبل (منسوخ شده)
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="gemini-1.5-pro-latest",  # منسوخ شده
    messages=[
        {
            "role": "user",
            "content": "پرامپت شما اینجا.",
        }
    ],
)

# بعد (استفاده از مدل پشتیبانی شده فعلی)
completion = client.chat.completions.create(
    model="gemini-2.5-pro",  # پشتیبانی شده فعلی
    messages=[
        {
            "role": "user",
            "content": "پرامپت شما اینجا.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:// قبل (منسوخ شده)
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "gemini-1.5-pro-latest", // منسوخ شده
  messages: [
    {
      role: "user",
      content: "پرامپت شما اینجا.",
    },
  ],
});

// بعد (استفاده از مدل پشتیبانی شده فعلی)
const completion = await client.chat.completions.create({
  model: "gemini-2.5-pro", // پشتیبانی شده فعلی
  messages: [
    {
      role: "user",
      content: "پرامپت شما اینجا.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### پشتیبانی و کمک

اگر برای مهاجرت به کمک نیاز دارید یا سؤالاتی درباره مدل‌های جایگزین دارید:

- مستندات مدل فعلی ما را برای مدل‌های جمینای موجود بررسی کنید
- برای راهنمایی مهاجرت با تیم پشتیبانی ما تماس بگیرید
- صفحه وضعیت API ما را برای آخرین به‌روزرسانی‌های دسترسی مدل بررسی کنید

---

## لینک‌های مرتبط

- [مستندات مدل‌های موجود](fa/models/index.md)
- [راهنمای مدل‌ها](fa/guides/model-selection.md)
- [مرجع API - تکمیل چت](fa/api-reference/chat.md)
- [بهترین شیوه‌های مهاجرت](fa/guides/best-practices.md)
- [راهنمای مدیریت خطا](fa/guides/error-handling.md)
