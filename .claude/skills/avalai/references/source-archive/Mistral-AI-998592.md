# Mistral AI

AvalAI دسترسی به سرویس‌های Mistral AI را از طریق API یکپارچه ما فراهم می‌کند. این صفحه جزئیات مدل‌های موجود Mistral AI، قابلیت‌های آن‌ها و موارد استفاده را شرح می‌دهد.

## مدل‌های موجود

### مدل‌های متن و چت

Mistral AI چندین مدل زبانی قدرتمند برای تولید متن و کاربردهای چت ارائه می‌دهد.

#### mistral-large-3

مدل `mistral-large-3` توانمندترین مدل Mistral AI تا به امروز است، یک مدل متن‌باز پیشرفته با معماری مخلوط-متخصصان پراکنده با ۴۱ میلیارد پارامتر فعال و ۶۷۵ میلیارد پارامتر کل. تحت مجوز Apache 2.0 منتشر شده است.

**ویژگی‌های کلیدی:**

- معماری مخلوط-متخصصان پراکنده (۴۱ میلیارد فعال / ۶۷۵ میلیارد کل پارامتر)
- منتشر شده تحت مجوز Apache 2.0 برای دسترسی کامل متن‌باز
- قابلیت‌های چندوجهی بومی با درک تصویر
- بهترین عملکرد در کلاس برای مکالمات چندزبانه در ۴۰+ زبان
- به برابری با بهترین مدل‌های متن‌باز تنظیم‌شده با دستورالعمل می‌رسد
- رتبه ۲ در دسته مدل‌های OSS غیر استدلالی در LMArena (رتبه ۶ کلی در میان مدل‌های OSS)
- چک‌پوینت بهینه‌شده در فرمت NVFP4 برای استقرار کارآمد
- قابلیت اجرا روی یک گره تک 8×A100 یا 8×H100 با استفاده از vLLM

**قیمت‌گذاری:**

| ورودی | ورودی کش‌شده | خروجی | هر صفحه |
|-------|--------------|--------|----------|
| $0.50/1M توکن | $0.05/1M توکن | $1.50/1M توکن | $0.001/صفحه |

**موارد استفاده:**

- وظایف استدلال و تحلیل پیچیده
- مکالمات و تولید محتوای چندزبانه
- درک و پردازش اسناد
- تولید کد و وظایف فنی
- برنامه‌های تحقیقاتی و سازمانی
- گردش‌های کاری عاملی و استفاده از ابزار

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="mistral-large-3",
    messages=[
        {
            "role": "user",
            "content": "پیامدهای محاسبات کوانتومی بر رمزنگاری مدرن را تحلیل کنید.",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `mistral-large-3` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="پیامدهای محاسبات کوانتومی بر رمزنگاری مدرن را تحلیل کنید.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### codestral-2501

مدل `codestral-2501` یک مدل تخصصی ۲۲ میلیارد پارامتری است که برای تولید کد در بیش از ۸۰ زبان برنامه‌نویسی طراحی شده است. این مدل استاندارد جدیدی برای عملکرد و قابلیت‌های تولید کد تعیین می‌کند.

**ویژگی‌های کلیدی:**

- تسلط بر بیش از ۸۰ زبان برنامه‌نویسی از جمله Python، Java، C، C++، JavaScript، Bash، Swift، Fortran و بسیاری دیگر
- تکمیل توابع کدنویسی، نوشتن تست‌ها و پر کردن کد ناقص با استفاده از مکانیسم پر کردن میانی (fill-in-the-middle)
- پنجره زمینه ۳۲ هزار توکنی برای تکمیل و درک کد طولانی
- عملکرد برتر در معیارهای سنجش شامل HumanEval، MBPP، CruxEval و RepoBench
- برتری در تولید SQL و وظایف برنامه‌نویسی چندزبانه
- قابلیت‌های پیشرفته پر کردن میانی برای ویرایش و تکمیل کد

**موارد استفاده:**

- توسعه نرم‌افزار و تولید کد
- ایجاد و خودکارسازی تست
- تکمیل کد در محیط‌های توسعه یکپارچه (IDE) و محیط‌های توسعه
- تولید مستندات فنی
- ترجمه کد بین زبان‌های برنامه‌نویسی
- اشکال‌زدایی و بهینه‌سازی کد

#### mistral-small-2503

مدل `mistral-small-2503` یک مدل زبانی همه‌کاره و کارآمد است که برای وظایف تولید و درک متن عمومی طراحی شده است. این مدل تعادل خوبی بین عملکرد و کارایی محاسباتی ارائه می‌دهد.

**ویژگی‌های کلیدی:**

- بهینه‌سازی شده برای وظایف زبانی عمومی
- پشتیبانی از پنجره زمینه ۱ میلیون توکنی
- عملکرد کارآمد برای وظایف زبانی روزمره
- قابلیت‌های متعادل در استدلال، تولید محتوا و درک متن
- گزینه مقرون به صرفه برای کاربردهای تولیدی

**موارد استفاده:**

- تولید محتوا و خلاصه‌سازی
- پاسخگویی به سؤالات و بازیابی اطلاعات
- طبقه‌بندی و تحلیل متن
- کاربردهای هوش مصنوعی مکالمه‌ای
- پردازش و درک اسناد

### مدل‌های OCR

#### mistral-ocr-4-0

مدل `mistral-ocr-4-0` جدیدترین مدل استخراج و درک سند Mistral AI است. این مدل متن Markdown را همراه با bounding box، طبقه‌بندی نوع بلوک و اطلاعات confidence درون‌خطی برمی‌گرداند و از ۱۷۰ زبان در ۱۰ گروه زبانی پشتیبانی می‌کند.

`mistral-ocr-latest` اکنون به `mistral-ocr-4-0` اشاره می‌کند و از همان قیمت‌گذاری استفاده می‌کند؛ بنابراین ادغام‌های موجود مبتنی بر alias لازم نیست فورا تغییر کنند. برای workflowهای قابل بازتولید، شناسه نسخه‌دار را به‌کار ببرید.

**ویژگی‌های کلیدی:**

- ارائه bounding box برای هایلایت موضعی، citation و گردش‌کارهای redaction
- طبقه‌بندی بلوک‌هایی مانند عنوان، جدول، معادله و امضا
- ارائه اطلاعات confidence درون‌خطی برای اعتبارسنجی و بازبینی انسانی
- حفظ ساختار سند در قالب Markdown برای RAG و pipelineهای ایندکس‌گذاری
- پشتیبانی از ۱۷۰ زبان در ۱۰ گروه زبانی
- پذیرش فرمت‌های متداول از جمله PDF، DOC، PPT، OpenDocument و تصویر
- پشتیبانی از annotation ساختاریافته Document AI در همان endpoint OCR
- مناسب برای semantic chunking، جستجوی سازمانی، پردازش فرم، فاکتور و workflowهای انطباق

**قیمت‌گذاری:**

- استخراج OCR: مبلغ $0.004 به ازای هر صفحه ($4 برای ۱٬۰۰۰ صفحه)
- annotation سند یا تصویر: مبلغ $0.005 به ازای هر صفحه annotation‌شده ($5 برای ۱٬۰۰۰ صفحه)

**انواع فایل‌های پشتیبانی شده:**

- اسناد PDF (تا 50 مگابایت و 1000 صفحه)
- تصاویر در فرمت‌های PNG، JPEG، WEBP و GIF غیر متحرک

## نحوه استفاده

برخلاف سایر مدل‌های سازگار با OpenAI، مدل‌های Mistral AI از ساختار نقطه پایانی متفاوتی بدون بخش مسیر "/v1" استفاده می‌کنند.

### مثال‌های پردازش OCR

#### استفاده از URL برای پردازش PDF

```python
from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا 100 صفحه
)

print(ocr_response)
```

#### استفاده از PDF با کدگذاری Base64

```python
import base64
from mistralai import Mistral

# خواندن و کدگذاری فایل PDF
with open("document.pdf", "rb") as f:
    pdf_data = f.read()

base64_pdf = base64.b64encode(pdf_data).decode("utf-8")
document_url = f"data:application/pdf;base64,{base64_pdf}"

# پردازش PDF کدگذاری شده
client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {"type": "document_url", "document_url": document_url}

ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا 100 صفحه
)

print(ocr_response)
```

#### پردازش صفحات خاص

```python
from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

# پردازش فقط صفحات 0، 1 و 5
ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
    pages=[0, 1, 5],  # فقط پردازش صفحات خاص
)

print(ocr_response)
```

#### مثال JavaScript

```javascript
import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-4-0",
  document: documentParam,
  pages: Array.from({ length: 100 }, (_, i) => i), // پردازش تا 100 صفحه
});

console.log(ocrResponse);
```

### درک سند

مدل `mistral-ocr-4-0` همچنین می‌تواند با مدل‌های زبانی ترکیب شود تا امکان تعامل زبان طبیعی با محتوای سند را فراهم کند. این به شما امکان می‌دهد با پرسیدن سؤالات به زبان طبیعی، اطلاعات و بینش‌ها را از اسناد استخراج کنید.

#### پاسخگویی به سؤالات از مقالات علمی

```python
from mistralai import Mistral
from mistralai.models.chat import ChatMessage

# راه‌اندازی کلاینت
client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# ابتدا سند را با OCR پردازش کنید
document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
    pages=[0, 1, 2],  # پردازش 3 صفحه اول
)

# ایجاد یک پیام با متن و سند
document_content = (
    ocr_response.pages[0].text
    + "\n"
    + ocr_response.pages[1].text
    + "\n"
    + ocr_response.pages[2].text
)
message = f"""
لطفا این مقاله علمی را تحلیل کنید و بر اساس محتوای آن به سؤالات پاسخ دهید:

{document_content}
"""

# ارسال درخواست
messages = [
    ChatMessage(role="user", content=message),
]

chat_response = client.chat(
    model="mistral-large-latest",
    messages=messages,
)

print(chat_response.choices[0].message.content)

# پرسیدن سؤالات خاص درباره سند
question = "دستاورد اصلی این مقاله چیست؟"
messages = [
    ChatMessage(role="user", content=message),
    ChatMessage(role="assistant", content=chat_response.choices[0].message.content),
    ChatMessage(role="user", content=question),
]

chat_response = client.chat(
    model="mistral-large-latest",
    messages=messages,
)

print(f"سؤال: {question}\nپاسخ: {chat_response.choices[0].message.content}")
```

#### استخراج اطلاعات از رسیدها

```python
from mistralai import Mistral
from mistralai.models.chat import ChatMessage

# راه‌اندازی کلاینت
client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش تصویر رسید
document_param = {
    "type": "document_url",
    "document_url": "https://example.com/receipt.jpg",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
)

# ایجاد یک پیام با متن و تصویر
message = f"""
اطلاعات زیر را از این رسید استخراج کنید:
1. نام فروشگاه
2. تاریخ خرید
3. مبلغ کل
4. لیست اقلام خریداری شده با قیمت‌ها

محتوای رسید:
{ocr_response.pages[0].text}
"""

# ارسال درخواست
messages = [
    ChatMessage(role="user", content=message),
]

chat_response = client.chat(
    model="mistral-large-latest",
    messages=messages,
)

print(chat_response.choices[0].message.content)
```

قابلیت‌های کلیدی:

- پاسخگویی به سؤالات در مورد محتوای خاص سند
- استخراج اطلاعات و خلاصه‌سازی
- تجزیه و تحلیل سند و ارائه بینش‌ها
- پرس و جوهای چند سندی و مقایسه‌ها
- پاسخ‌های آگاه از زمینه که کل سند را در نظر می‌گیرند
- گزینه‌های خروجی ساختاریافته برای پردازش پایین‌دستی

### موارد استفاده کلیدی

Mistral OCR امکان طیف گسترده‌ای از کاربردهای پردازش اسناد را فراهم می‌کند:

- **تحقیقات علمی**: تبدیل مقالات علمی با فرمول‌ها و نمودارهای پیچیده به فرمت‌های آماده هوش مصنوعی
- **حفظ میراث تاریخی**: دیجیتال‌سازی اسناد و آثار تاریخی برای دسترسی گسترده‌تر
- **خدمات مشتری**: تبدیل مستندات و راهنماها به پایگاه‌های دانش نمایه‌شده
- **آموزش**: تبدیل یادداشت‌های سخنرانی و ارائه‌ها به محتوای قابل جستجو
- **حقوقی**: پردازش پرونده‌های نظارتی و اسناد حقوقی
- **مهندسی**: استخراج اطلاعات از متون فنی و نقشه‌ها

## منابع مرتبط

- [اعلام OCR 4](fa/news/2026-07-17-kimi-k3-mistral-ocr-4-added.md)
- [راهنمای پردازش سند](fa/guides/pdf-files.md)
- [پردازش اسناد با Mistral OCR](fa/examples/processing_documents_with_mistral_ocr.md)
