# مدل جدید اضافه شد: GPT Image 1 Mini اکنون در دسترس است

**تاریخ:** 1404-07-16 (2025-10-08)

## خلاصه

AvalAI از پشتیبانی مدل GPT Image 1 Mini از OpenAI خبر می‌دهد، یک نسخه مقرون به صرفه از GPT Image 1 که تولید تصویر سریع‌تر و مقرون به صرفه‌تر را با حفظ کیفیت بالای خروجی ارائه می‌دهد. این مدل همان درک پیشرفته زبان و قابلیت‌های تولید تصویر GPT Image 1 را با هزینه قابل توجهی کمتر فراهم می‌کند و برای برنامه‌های با حجم بالا ایده‌آل است.

---

## جزئیات

### OpenAI

* **gpt-image-1-mini**: یک مدل تولید تصویر مقرون به صرفه با قابلیت‌های پیشرفته در پیروی از دستورالعمل‌ها و کیفیت خروجی واقع‌گرایانه با قیمت کاهش یافته. [مستندات](fa/examples/generate_images_with_gpt_image.md)

GPT Image 1 Mini همان فناوری قدرتمند تولید تصویر GPT Image 1 را ارائه می‌دهد اما با بهینه‌سازی برای مقرون به صرفه بودن. این مدل برای برنامه‌هایی که نیاز به تولید تصویر با حجم بالا، نمونه‌سازی اولیه یا سناریوهایی که قیمت کاهش یافته مزایای قابل توجهی ارائه می‌دهد در حالی که همچنان نتایج عالی ارائه می‌دهد، کامل است.

### ویژگی‌های کلیدی

* **مقرون به صرفه**: قیمت قابل توجهی کمتر در مقایسه با GPT Image 1
* **ورودی چندوجهی**: قبول ورودی‌های متنی و تصویری برای موارد استفاده متنوع
* **گزینه‌های کیفیت**: پشتیبانی از حالت‌های تولید با کیفیت پایین، متوسط و بالا
* **اندازه‌های انعطاف‌پذیر**: گزینه‌های رزولوشن متعدد شامل 1024x1024، 1024x1536 و 1536x1024
* **ویرایش پیشرفته**: ترکیب یا اصلاح تصاویر موجود با دستورالعمل‌های متنی
* **پشتیبانی از ماسک**: ویرایش بخش‌های خاصی از تصاویر در حین حفظ سایر قسمت‌ها

### دسترسی

GPT Image 1 Mini برای کاربران **سطح 3، 4 و 5** در AvalAI در دسترس است.

### جزئیات قیمت‌گذاری

GPT Image 1 Mini قیمت قابل توجهی کاهش یافته در مقایسه با GPT Image 1 ارائه می‌دهد:

| نوع توکن | قیمت به ازای 1 میلیون توکن |
|----------|----------------------------|
| ورودی متنی | $5.00 |
| ورودی متنی کش شده | $1.25 |
| ورودی تصویری | $10.00 |
| ورودی تصویری کش شده | $2.50 |
| خروجی تصویری | $40.00 |

**قیمت‌گذاری تولید تصویر:**

| کیفیت | اندازه | قیمت به ازای هر تصویر |
|--------|---------|----------------------|
| پایین | 1024x1024 | $0.011 |
| پایین | 1024x1536 / 1536x1024 | $0.016 |
| متوسط | 1024x1024 | $0.042 |
| متوسط | 1024x1536 / 1536x1024 | $0.063 |
| بالا | 1024x1024 | $0.036 |
| بالا | 1024x1536 / 1536x1024 | $0.052 |

### مثال‌های استفاده از GPT Image 1 Mini

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-1-mini",
    "prompt": "تصویر واقع‌گرایانه از یک شهر آینده‌نگر با خودروهای پرنده و ساختمان‌های بلند شیشه‌ای",
    "size": "1024x1024",
    "quality": "high",
    "response_format": "url"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید یک تصویر جدید
response = client.images.generate(
    model="gpt-image-1-mini",
    prompt="تصویر واقع‌گرایانه از یک شهر آینده‌نگر با خودروهای پرنده و ساختمان‌های بلند شیشه‌ای",
    size="1024x1024",
    quality="high",
    response_format="url",  # or b64_json
)

# دسترسی به URL تصویر
image_url = response.data[0].url
print(f"Generated image URL: {image_url}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تولید یک تصویر جدید
const response = await client.images.generate({
  model: "gpt-image-1-mini",
  prompt: "تصویر واقع‌گرایانه از یک شهر آینده‌نگر با خودروهای پرنده و ساختمان‌های بلند شیشه‌ای",
  size: "1024x1024",
  quality: "high",
  response_format: "url", // or b64_json
});

// دسترسی به URL تصویر
const imageUrl = response.data[0].url;
console.log(`Generated image URL: ${imageUrl}`);

```

### ویرایش تصویر با GPT Image 1 Mini

GPT Image 1 Mini همچنین از قابلیت‌های ویرایش تصویر پشتیبانی می‌کند:

```language-selector
bash=:curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F model="gpt-image-1-mini" \
  -F image="@input_image.jpg" \
  -F prompt="تغییر پس‌زمینه به ساحل گرمسیری" \
  -F response_format="url"

python=:# ویرایش یک تصویر موجود
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-1-mini",
        image=image_file,
        prompt="تغییر پس‌زمینه به ساحل گرمسیری",
        response_format="url",  # or b64_json
    )

edited_image_url = response.data[0].url
print(f"Edited image URL: {edited_image_url}")

javascript=:import fs from "fs";

// ویرایش یک تصویر موجود
const response = await client.images.edit({
  model: "gpt-image-1-mini",
  image: fs.createReadStream("input_image.jpg"),
  prompt: "تغییر پس‌زمینه به ساحل گرمسیری",
  response_format: "url", // or b64_json
});

const editedImageUrl = response.data[0].url;
console.log(`Edited image URL: ${editedImageUrl}`);

```

### ویرایش مبتنی بر ماسک

برای کنترل دقیق روی قسمت‌هایی از تصویر که اصلاح می‌شوند:

```python
# ویرایش با ماسک
with open("input_image.jpg", "rb") as image_file, open("mask.png", "rb") as mask_file:
    response = client.images.edit(
        model="gpt-image-1-mini",
        image=image_file,
        mask=mask_file,
        prompt="اضافه کردن گل‌های رنگارنگ به ناحیه ماسک شده",
        response_format="url",  # or b64_json
    )
```

### اندپوینت‌های پشتیبانی شده

GPT Image 1 Mini در اندپوینت‌های زیر در دسترس است:

* **v1/images/generations** - برای تولید مستقیم تصویر
* **v1/images/edits** - برای ویرایش تصاویر موجود

---

## لینک‌های مرتبط

* [راهنمای استفاده از GPT Image 1](fa/examples/generate_images_with_gpt_image.md)
* [راهنمای تولید تصویر](fa/guides/image-generation.md)
* [مستندات مدل‌های OpenAI](fa/providers/openai.md)
* [اطلاعات قیمت‌گذاری](fa/pricing.md)