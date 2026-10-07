# راه‌اندازی آزمایشیی API فایل‌ها - مدیریت فایل سازگار با OpenAI

**تاریخ:** ۱۴۰۴-۱۰-۱۱ / (2026-01-01)

## خلاصه

AvalAI اعلام می‌کند API فایل‌ها (`/v1/files`) اولین لایه سرویس بومی ما است که سیستم مدیریت فایل سازگار با OpenAI را ارائه می‌دهد. یک بار فایل‌ها را آپلود کنید و با `file_id` در چندین درخواست API به آنها ارجاع دهید، که سربار شبکه را کاهش داده و عملکرد را بهبود می‌بخشد. API فایل‌ها در طول دوره بتای ۶۰ روزه تا ۱۰ اسفند ۱۴۰۴ کاملا رایگان است.

---

## جزئیات

### API فایل‌ها چیست؟

API فایل‌ها اولین لایه سرویس بومی AvalAI است که یک سیستم مدیریت فایل سازگار با OpenAI ارائه می‌دهد. به جای ارسال فایل‌های کدگذاری شده با base64 یا URLها با هر درخواست API، می‌توانید:

1. **یک بار آپلود کنید، همه جا استفاده کنید** - یک فایل آپلود کنید تا `file_id` دریافت کنید، سپس در درخواست‌های بعدی به آن ارجاع دهید
2. **سربار شبکه را کاهش دهید** - دیگر نیازی به ارسال بارهای بزرگ base64 (که حدود ۳۳٪ سربار اضافه می‌کنند) با هر درخواست نیست
3. **عملکرد را بهبود دهید** - فایل‌ها در سمت سرور ذخیره و به صورت داخلی بازیابی می‌شوند، که تأخیر را کاهش می‌دهد
4. **سازگاری با نقاط پایانی متعدد** - از فایل‌های آپلود شده با `v1/chat/completions`، `v1/responses`، `v1/messages`، `v1/ocr` و `v1/images/edits` استفاده کنید

### برنامه بتای رایگان

> **🎉 رایگان برای ۶۰ روز**: تمام عملیات API فایل‌ها از ۱۱ دی ۱۴۰۴ تا ۱۰ اسفند ۱۴۰۴ کاملا **رایگان** است. از شما دعوت می نماییم که سرویس را تست کنید و درصورت بروز مشکل به [t.me/AvalAISupport](https://t.me/AvalAISupport) گزارش دهید.

### اهداف پشتیبانی شده فایل

| هدف | توضیحات |
|---------|-------------|
| `assistants` | برای استفاده در API دستیاران |
| `batch` | برای استفاده در API دسته‌ای |
| `fine-tune` | برای تنظیم دقیق مدل‌ها |
| `vision` | تصاویر برای تنظیم دقیق بینایی |
| `user_data` | نوع فایل انعطاف‌پذیر برای هر هدفی |
| `evals` | برای مجموعه داده‌های ارزیابی |
| `others` | مخصوص AvalAI: هدف عمومی برای هر مورد استفاده دیگر |

### محدودیت‌های نرخ بر اساس سطح

#### عملیات فایل (در دقیقه)

| سطح | آپلود | دانلود | حذف |
|------|---------|-----------|---------|
| ۰ (رایگان) | ۳ | ۵ | ۱۰ |
| ۱ | ۱۰ | ۱۰۰ | ۱۰۰ |
| ۲ | ۵۰ | ۲۵۰ | ۲۵۰ |
| ۳ | ۲۵۰ | ۵۰۰ | ۵۰۰ |
| ۴ | ۵۰۰ | ۱٬۰۰۰ | ۱٬۰۰۰ |
| ۵ | ۱٬۵۰۰ | ۲٬۰۰۰ | ۵٬۰۰۰ |

#### محدودیت‌های فضای ذخیره‌سازی

| سطح | حداکثر فضا |
|------|-------------|
| ۰ (رایگان) | ۲۵۰ مگابایت |
| ۱ | ۲ گیگابایت |
| ۲ | ۵ گیگابایت |
| ۳ | ۱۵ گیگابایت |
| ۴ | ۵۰ گیگابایت |
| ۵ | ۲۰۰ گیگابایت |

**حداکثر اندازه فایل**: ۱۲۸ مگابایت برای هر فایل (در طول بتا)

---

## نقاط پایانی API

API فایل‌ها ۵ نقطه پایانی ارائه می‌دهد:

| متد | نقطه پایانی | توضیحات |
|--------|----------|-------------|
| POST | `/v1/files` | آپلود یک فایل |
| GET | `/v1/files` | لیست تمام فایل‌ها |
| GET | `/v1/files/{file_id}` | دریافت متادیتای فایل |
| DELETE | `/v1/files/{file_id}` | حذف یک فایل |
| GET | `/v1/files/{file_id}/content` | دانلود محتوای فایل |

---

## مثال‌های درخواست/پاسخ API

### آپلود یک فایل

```bash
curl https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F purpose="user_data" \
  -F file="@document.pdf"
```

#### پاسخ

```json
{
  "id": "file-abc123def456",
  "object": "file",
  "bytes": 1024000,
  "created_at": 1735689600,
  "expires_at": null,
  "filename": "document.pdf",
  "purpose": "user_data"
}
```

### لیست فایل‌ها

```bash
curl https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

#### پاسخ

```json
{
  "object": "list",
  "data": [
    {
      "id": "file-abc123def456",
      "object": "file",
      "bytes": 1024000,
      "created_at": 1735689600,
      "expires_at": null,
      "filename": "document.pdf",
      "purpose": "user_data"
    }
  ]
}
```

### استفاده از فایل در تکمیل گفتگو

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {
            "type": "text",
            "text": "این سند درباره چیست؟"
          },
          {
            "type": "file",
            "file": {
              "file_id": "file-abc123def456"
            }
          }
        ]
      }
    ]
  }'
```

---

## مثال‌های استفاده از SDK

### آپلود و استفاده از یک فایل

```language-selector
bash=:# آپلود یک فایل
FILE_RESPONSE=$(curl -s https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F purpose="user_data" \
  -F file="@document.pdf")

FILE_ID=$(echo $FILE_RESPONSE | jq -r '.id')

# استفاده از فایل در تکمیل گفتگو
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-4o",
    "messages": [
      {
        "role": "user",
        "content": [
          {"type": "text", "text": "این سند را خلاصه کنید"},
          {"type": "file", "file": {"file_id": "'$FILE_ID'"}}
        ]
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

# آپلود یک فایل
file = client.files.create(file=open("document.pdf", "rb"), purpose="user_data")

print(f"فایل آپلود شد: {file.id}")

# استفاده از فایل در تکمیل گفتگو
response = client.chat.completions.create(
    model="gpt-4o",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این سند را خلاصه کنید"},
                {"type": "file", "file": {"file_id": file.id}},
            ],
        }
    ],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// آپلود یک فایل
const file = await client.files.create({
  file: fs.createReadStream("document.pdf"),
  purpose: "user_data",
});

console.log(`فایل آپلود شد: ${file.id}`);

// استفاده از فایل در تکمیل گفتگو
const response = await client.chat.completions.create({
  model: "gpt-4o",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این سند را خلاصه کنید" },
        { type: "file", file: { file_id: file.id } },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

### فایل با سیاست انقضا

```language-selector
bash=:# آپلود فایلی که بعد از ۲۴ ساعت منقضی می‌شود
curl https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F purpose="user_data" \
  -F file="@temp_document.pdf" \
  -F 'expires_after={"anchor":"created_at","seconds":86400}'

python=:# آپلود فایلی که بعد از ۲۴ ساعت منقضی می‌شود
file = client.files.create(
    file=open("temp_document.pdf", "rb"),
    purpose="user_data",
    expires_after={"anchor": "created_at", "seconds": 86400},  # ۲۴ ساعت
)

print(f"زمان انقضای فایل: {file.expires_at}")

javascript=:// آپلود فایلی که بعد از ۲۴ ساعت منقضی می‌شود
const file = await client.files.create({
  file: fs.createReadStream("temp_document.pdf"),
  purpose: "user_data",
  expires_after: {
    anchor: "created_at",
    seconds: 86400, // ۲۴ ساعت
  },
});

console.log(`زمان انقضای فایل: ${file.expires_at}`);

```

---

## چرا از API فایل‌ها استفاده کنیم؟

### قبل (بدون API فایل‌ها)

هر درخواست محتوای کامل فایل را ارسال می‌کند:

```python
# هر درخواست کل فایل کدگذاری شده با base64 را ارسال می‌کند
for question in questions:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_encoded_file}"  # حدود ۳۳٪ بزرگتر
                        },
                    },
                ],
            }
        ],
    )
```

### بعد (با API فایل‌ها)

یک بار آپلود کنید، با شناسه ارجاع دهید:

```python
# یک بار آپلود کنید
file = client.files.create(file=open("document.pdf", "rb"), purpose="user_data")

# در چندین درخواست با شناسه ارجاع دهید - بدون بارهای بزرگ
for question in questions:
    response = client.chat.completions.create(
        model="gpt-4o",
        messages=[
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": question},
                    {"type": "file", "file": {"file_id": file.id}},  # فقط یک رشته کوتاه
                ],
            }
        ],
    )
```

---

## ذخیره‌سازی و امنیت

### زیرساخت ذخیره‌سازی

فایل‌ها در ارائه‌دهندگان ابری سطح سازمانی ذخیره می‌شوند:
- **AWS S3**
- **Google Cloud Platform (GCP)**
- **Cloudflare**

### ملاحظات امنیتی

- فایل‌ها با اقدامات امنیتی سطح سازمانی ذخیره می‌شوند
- فایل‌ها بدون رمزنگاری در حالت استراحت ذخیره می‌شوند (استاندارد صنعت برای فایل‌های پرتکرار، مشابه سایر ارائه‌دهندگان)
- دسترسی توسط کلید API شما کنترل می‌شود - فقط شما می‌توانید به فایل‌های خود دسترسی داشته باشد

### برنامه پاداش باگ

اگر یک آسیب‌پذیری امنیتی کشف کردید، لطفا گزارش دهید به:
- **ایمیل**: security@avalai.ir
- **پاداش باگ** برای مسائل امنیتی بحرانی که می‌توانند داده‌های کاربران را در خطر قرار دهند در دسترس است

---

## لینک‌های مرتبط

- [مرجع API فایل‌ها](fa/api-reference/files.md) - مستندات کامل API با تمام نقاط پایانی
- [راهنمای ورودی‌های فایل](fa/guides/file-inputs.md) - درباره روش‌های مختلف ارسال فایل‌ها بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - محدودیت‌های نرخ مبتنی بر سطح را درک کنید
- [API تکمیل گفتگو](fa/api-reference/chat.md) - از فایل‌ها در تکمیل گفتگو استفاده کنید
- [API تشخیص متن](fa/api-reference/ocr.md) - پردازش اسناد با OCR

---

## پشتیبانی

برای سؤالات یا مشکلات مربوط به بتای API فایل‌ها:
- **تلگرام**: [t.me/AvalAISupport](https://t.me/AvalAISupport)
- **مستندات**: [مرجع API فایل‌ها](fa/api-reference/files.md)
