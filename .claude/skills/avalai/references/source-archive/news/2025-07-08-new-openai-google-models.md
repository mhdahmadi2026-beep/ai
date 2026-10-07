# مدل‌های جدید اضافه شده: مدل‌های تحقیقاتی OpenAI و Google Imagen 4.0

**تاریخ:** 1404-04-17 / (2025-07-08)

## خلاصه

ما مجموعه مدل‌های خود را با مدل‌های تحقیقاتی قدرتمند جدید OpenAI و آخرین مدل‌های تولید تصویر Google Imagen 4.0 گسترش داده‌ایم. این اضافات شامل قابلیت‌های تحقیق عمیق پیشرفته و ابزارهای تولید تصویر پیشرفته برای بهبود برنامه‌های هوش مصنوعی شما می‌باشد.

---

## جزئیات

### مدل‌های تحقیقاتی OpenAI

ما با افتخار اضافه شدن آخرین مدل‌های تحقیقاتی OpenAI را اعلام می‌کنیم که برای استدلال پیچیده و وظایف تحقیق عمیق طراحی شده‌اند:

- **o3-pro**: پیشرفته‌ترین مدل استدلال OpenAI برای حل مسائل پیچیده و تحلیل
- **o3-deep-research**: قدرتمندترین مدل تحقیق عمیق ما که قادر به انجام وظایف تحقیقاتی پیچیده و چندمرحله‌ای با قابلیت جستجوی اینترنت است
- **o4-mini-deep-research**: مدل تحقیق عمیق سریع‌تر و مقرون‌به‌صرفه‌تر که برای وظایف تحقیقاتی پیچیده با تعادل عالی هزینه-عملکرد ایده‌آل است

#### نکات مهم استفاده از مدل‌های تحقیقاتی

تمام مدل‌های تحقیقاتی (`o3-deep-research`، `o4-mini-deep-research`، و `computer-use-preview`) **فقط از طریق endpoint مسیر v1/responses** قابل دسترسی هستند و نیاز به انتخاب ابزار دارند. هنگام استفاده از `search_context_size`، باید حداقل روی "medium" تنظیم شود تا عملکرد بهینه داشته باشد.

### مدل‌های Google Imagen 4.0

آخرین مدل‌های تولید تصویر Google اکنون در دسترس هستند و کیفیت و سرعت بهبود یافته‌ای ارائه می‌دهند:

- **imagen-4.0-ultra-generate-preview-06-06**: تولید تصویر با کیفیت فوق‌العاده بالا با جزئیات و واقع‌گرایی استثنایی
- **imagen-4.0-generate-preview-06-06**: تولید تصویر با کیفیت بالا برای کاربردهای حرفه‌ای
- **imagen-4.0-fast-generate-preview-06-06**: تولید تصویر سریع که برای سرعت بهینه‌سازی شده و در عین حال کیفیت را حفظ می‌کند

### نمونه‌های استفاده

#### مدل‌های تحقیقاتی (endpoint مسیر v1/responses)

```language-selector
python=:import requests

url = "https://api.avalai.ir/v1/responses"
headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer $AVALAI_API_KEY",
}

data = {
    "model": "o3-deep-research",
    "tools": [{"type": "web_search", "search_context_size": "medium"}],
    "input": "تحقیق درباره آخرین پیشرفت‌های محاسبات کوانتومی",
}

response = requests.post(url, headers=headers, json=data)
print(response.json())

javascript=:const response = await fetch('https://api.avalai.ir/v1/responses', {
 method: 'POST',
 headers: {
 'Content-Type': 'application/json',
 'Authorization': 'Bearer $AVALAI_API_KEY'
 },
 body: JSON.stringify({
 model: 'o3-deep-research',
 tools: [{ type: 'web_search_preview', search_context_size: 'medium' }],
 input: 'تحقیق درباره آخرین پیشرفت‌های محاسبات کوانتومی'
 })
});

const result = await response.json();
console.log(result);

bash=:curl -i https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "o3-deep-research",
 "tools": [{ "type": "web_search", "search_context_size": "medium"}],
 "input": "تحقیق درباره آخرین پیشرفت‌های محاسبات کوانتومی"
 }'

```

#### مدل‌های Google Imagen (Chat Completions استاندارد)

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="imagen-4.0-generate-preview-06-06",
    messages=[
        {
            "role": "user",
            "content": "تصویر زیبایی از منظره طبیعی با کوه‌ها و دریاچه در زمان غروب تولید کن",
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
  model: "imagen-4.0-generate-preview-06-06",
  messages: [
    {
      role: "user",
      content:
        "تصویر زیبایی از منظره طبیعی با کوه‌ها و دریاچه در زمان غروب تولید کن",
    },
  ],
});

console.log(response.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Google](fa/providers/google.md)
- [راهنمای Responses API](fa/guides/responses-vs-chat-completions.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [ابزارها و فراخوانی تابع](fa/guides/tools.md)