# افزودن مدل‌های جدید به پلتفرم AvalAI

**تاریخ:** 1404-02-05

## خلاصه

خرسندیم افزودن چندین مدل جدید به پلتفرم AvalAI را اعلام کنیم. این به‌روزرسانی گزینه‌های متنوعی را برای وظایف مختلف از جمله استدلال پیشرفته، پردازش کارآمد و قابلیت‌های تخصصی در اختیار شما قرار می‌دهد و شامل مدل‌هایی از OpenAI و Google است.

---

## جزئیات

مدل‌های زیر اکنون از طریق API پلتفرم AvalAI در دسترس هستند:

### OpenAI

* **o4-mini**: نسخه کارآمدتر از جدیدترین مدل o4 شرکت OpenAI که تعادل عالی بین عملکرد و سرعت را ارائه می‌دهد. [مستندات](fa/models/o4-mini.md)
* **o3**: مدل قدرتمند همه‌منظوره OpenAI با قابلیت‌های استدلال پیشرفته. [مستندات](fa/models/o3.md)
* **gpt-4.1-nano**: کوچک‌ترین و کارآمدترین مدل در خانواده GPT-4.1، ایده‌آل برای برنامه‌هایی که نیازمند پاسخ‌های سریع و مصرف منابع کمتر هستند. [مستندات](fa/models/gpt-4.1-nano.md)
* **gpt-4.1-mini**: مدل متوسط GPT-4.1 که تعادل خوبی بین عملکرد و کارایی ارائه می‌دهد. [مستندات](fa/models/gpt-4.1-mini.md)
* **gpt-4.1**: مدل پرچمدار GPT-4.1 از OpenAI، با قابلیت‌های پیشرفته استدلال، دانش و پیروی از دستورالعمل‌ها. [مستندات](fa/models/gpt-4.1.md)

### مدل‌های Google

* **gemini-2.5-flash-preview-04-17**: نسخه پیش‌نمایش از جدیدترین مدل Gemini 2.5 Flash گوگل، بهینه‌سازی شده برای سرعت در عین حفظ عملکرد قوی. [مستندات](fa/models/gemini-2.5-flash-preview-04-17.md)
* **gemini-2.5-pro-preview-03-25**: مدل قدرتمند Gemini 2.5 Pro گوگل در نسخه پیش‌نمایش، با قابلیت‌های پیشرفته استدلال و دانش. [مستندات](fa/models/gemini-2.5-pro-preview-03-25.md)


استفاده از این مدل‌ها از هم‌اکنون از طریق نقاط پایانی استاندارد API ما امکان‌پذیر است. برای مشاهده شناسه‌های دقیق مدل و نمونه کدهای کاربردی، لطفا به مستندات مربوطه مراجعه نمایید.

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="o4-mini",
    messages=[
        {
            "role": "user",
            "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید.",
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
  model: "o4-mini",

  messages: [
    {
      role: "user",
      content: "محاسبات کوانتومی را به زبان ساده توضیح دهید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

---

## پیوندهای مرتبط

* [فهرست مدل‌ها](fa/models/index.md)
* [مرجع API Chat Completions](fa/api-reference/chat.md)
* [راهنمای انتخاب مدل](fa/guides/model-selection.md)