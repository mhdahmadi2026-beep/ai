# مدل جدید اضافه شد: GPT Image 1 اکنون در دسترس است

**تاریخ:** 1404-02-06 (2025-04-26)

## خلاصه

AvalAI با افتخار از پشتیبانی مدل GPT Image 1 از OpenAI خبر می‌دهد، یک مدل قدرتمند جدید که درک پیشرفته زبان را با قابلیت‌های تولید تصویر پیشرفته ترکیب می‌کند. این مدل در دنبال کردن دستورالعمل‌های دقیق برتری دارد و تصاویر واقع‌گرایانه با کیفیت بالا تولید می‌کند که پیشرفت قابل توجهی نسبت به مدل‌های تصویری نسل قبلی محسوب می‌شود.

---

## جزئیات

### OpenAI

* **gpt-image-1**: یک مدل تولید تصویر همه‌کاره با قابلیت‌های برتر در پیروی از دستورالعمل‌ها و کیفیت خروجی واقع‌گرایانه. [مستندات](fa/examples/generate_images_with_gpt_image.md)

GPT Image 1 نشان‌دهنده پیشرفت قابل توجهی در فناوری تولید تصویر هوش مصنوعی است که دانش جهانی مدل‌های زبانی بزرگ را با توانایی‌های پیشرفته ایجاد تصویر ترکیب می‌کند. چه نیاز به تولید تصاویر کاملا جدید از توضیحات متنی داشته باشید و چه ویرایش تصاویر موجود، این مدل نتایج استثنایی در طیف گسترده‌ای از کاربردها ارائه می‌دهد.

[راهنمای جامع](fa/examples/generate_images_with_gpt_image.md) ما بر اساس [مثال رسمی OpenAI Cookbook](https://cookbook.openai.com/examples/generate_images_with_gpt_image) و با تطبیق برای پیاده‌سازی AvalAI تهیه شده است.

### ویژگی‌های کلیدی

* **پیروی برتر از دستورالعمل‌ها**: با ارائه متن‌های توضیحی دقیق، دقیقا آنچه می‌خواهید را ایجاد کنید
* **کیفیت واقع‌گرایانه**: تولید تصاویر با جزئیات و واقع‌گرایی چشمگیر
* **شخصی‌سازی انعطاف پذیر**: تنظیم کیفیت، اندازه، فشرده‌سازی و شفافیت پس‌زمینه
* **ویرایش پیشرفته**: ترکیب یا اصلاح تصاویر موجود با دستورالعمل‌های متنی
* **پشتیبانی از ماسک**: ویرایش بخش‌های خاصی از تصاویر در حین حفظ سایر قسمت‌ها

### مثال‌های استفاده

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید یک تصویر جدید
response = client.images.generate(
    model="gpt-image-1",
    prompt="تصویر واقع‌گرایانه از یک شهر آینده‌نگر با خودروهای پرنده و ساختمان‌های بلند شیشه‌ای",
    size="1024x1024",
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
  model: "gpt-image-1",
  prompt:
    "تصویر واقع‌گرایانه از یک شهر آینده‌نگر با خودروهای پرنده و ساختمان‌های بلند شیشه‌ای",
  size: "1024x1024",
  response_format: "url", // or b64_json
});

// دسترسی به URL تصویر
const imageUrl = response.data[0].url;
console.log(`Generated image URL: ${imageUrl}`);

```

### قابلیت‌های ویرایش تصویر

GPT Image 1 همچنین در ویرایش و ترکیب تصاویر موجود برتری دارد. می‌توانید تا 10 تصویر ورودی و دستورالعمل‌های دقیق برای چگونگی اصلاح یا ادغام آنها ارائه دهید.

```python
# ویرایش یک تصویر موجود
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-1",
        image=image_file,
        prompt="تغییر پس‌زمینه به غروب آفتاب در ساحل",
        response_format="url",  # or b64_json
    )
```

### ویرایش مبتنی بر ماسک

برای کنترل دقیق روی قسمت‌هایی از تصویر که اصلاح می‌شوند، می‌توانید یک ماسک با کانال آلفا ارائه دهید:

```python
# ویرایش با ماسک
with open("input_image.jpg", "rb") as image_file, open("mask.png", "rb") as mask_file:
    response = client.images.edit(
        model="gpt-image-1",
        image=image_file,
        mask=mask_file,
        prompt="اضافه کردن گل‌های رنگارنگ به منطقه باغ",
        response_format="url",  # or b64_json
    )
```

---

## لینک‌های مرتبط

* [راهنمای استفاده از GPT Image 1](fa/examples/generate_images_with_gpt_image.md)
* [راهنمای تولید تصویر](fa/guides/image-generation.md)
* [مرجع API OpenAI](fa/api-reference/images.md)
* [اطلاعات قیمت‌گذاری](fa/pricing.md)