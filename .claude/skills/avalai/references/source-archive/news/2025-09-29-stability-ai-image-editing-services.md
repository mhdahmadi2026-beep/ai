# سرویس‌های ویرایش تصویر Stability AI اکنون در دسترس است

**تاریخ:** ۱۴۰۴-۰۷-۰۷ / (2025-09-29)

## خلاصه

ما اعلام می‌کنیم که ۹ سرویس تخصصی ویرایش تصویر Stability AI از طریق نقطه دسترسی `v1/images/edits` در دسترس است. این ابزارهای حرفه‌ای امکان ویرایش دقیق تصاویر شامل inpainting (پر کردن نواحی خالی)، جایگزینی اشیاء، حذف پس‌زمینه و قابلیت‌های انتقال سبک را فراهم می‌کند.

**به‌روزرسانی مهم:** مدل `stability.sd3-large-v1:0` منسوخ شده است. لطفا برای ادامه دسترسی به قابلیت‌های Stable Diffusion با کیفیت بالا به `stability.sd3-5-large-v1:0` مهاجرت کنید.

---

## جزئیات

### سرویس‌های ویرایش تصویر Stability AI

AvalAI اکنون دسترسی به ۹ سرویس تخصصی ویرایش تصویر از Stability AI را فراهم می‌کند که برای تسریع گردش‌کارهای خلاقانه حرفه‌ای طراحی شده‌اند. این سرویس‌ها از فناوری‌های پیشرفته هوش مصنوعی برای امکان ویرایش و دستکاری دقیق تصاویر با کیفیت حرفه‌ای استفاده می‌کنند.

> **⚠️ نکته مهم:** تمام مدل‌های Stability AI تنها از prompts انگلیسی پشتیبانی می‌کنند. در صورت ارسال پرامپ فارسی، فراخوانی با خطای ۴۰۰ مواجه خواهد شد.

#### سرویس‌های جدید Stability (۹ مدل)

**سرویس‌های ویرایش (Edit Services):**
- **stability.stable-image-inpaint-v1:0** - پر کردن هوشمندانه نواحی پوشیده شده با محتوای مناسب
- **stability.stable-image-search-recolor-v1:0** - تغییر رنگ اشیاء خاص با استفاده از prompts طبیعی
- **stability.stable-image-search-replace-v1:0** - جایگزینی اشیاء درون تصاویر با استفاده از prompts توصیفی
- **stability.stable-image-erase-object-v1:0** - حذف عناصر ناخواسته با حفظ سازگاری پس‌زمینه
- **stability.stable-image-remove-background-v1:0** - جدا کردن سوژه‌ها از پس‌زمینه با دقت

**سرویس‌های کنترل (Control Services):**
- **stability.stable-image-control-sketch-v1:0** - تولید تصاویر دقیق از طرح‌های خام
- **stability.stable-image-control-structure-v1:0** - حفظ ترکیب ساختاری با تغییر سبک بصری
- **stability.stable-image-style-guide-v1:0** - تولید محتوای جدید با پیروی از مرجع سبک بصری خاص
- **stability.stable-style-transfer-v1:0** - اعمال سبک‌های هنری از تصاویر مرجع به محتوای هدف

### ویژگی‌های کلیدی

- **کیفیت حرفه‌ای**: قابلیت‌های ویرایش تصویر سطح سازمانی
- **سازگاری با OpenAI SDK**: کار یکپارچه با کتابخانه‌های موجود OpenAI client
- **پارامترهای پیشرفته**: تنظیم دقیق نتایج با style presets، control strength و negative prompts
- **فرمت‌های ورودی متعدد**: پشتیبانی از تصاویر، ماسک‌ها و مراجع سبک
- **مقرون به صرفه**: قیمت‌گذاری رقابتی در ۰.۰۴۰ دلار به ازای هر تصویر ویرایش شده

### پشتیبانی Endpoint

تمام سرویس‌ها از طریق endpoint استاندارد ویرایش تصویر در دسترس هستند:

```
POST https://api.avalai.ir/v1/images/edits
```

### نمونه‌های استفاده

#### Inpainting پایه (پر کردن نواحی خالی)

```language-selector
bash=:curl -X POST https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=stability.stable-image-inpaint-v1:0" \
  -F "image=@input-image-inpaint.jpg" \
  -F "mask=@mask-image-inpaint.png" \
  -F "prompt=artificer of time and space"

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# توجه: از prompt انگلیسی استفاده کنید
with open("input-image-inpaint.jpg", "rb") as img, open(
    "mask-image-inpaint.png", "rb"
) as msk:
    response = client.images.edit(
        model="stability.stable-image-inpaint-v1:0",
        image=img,
        mask=msk,
        prompt="artificer of time and space",  # prompt انگلیسی
        extra_body={
            "style_preset": "photographic",
            "negative_prompt": "blurry, low quality",
        },
        response_format="url",  # or b64_json
    )

print(f"تصویر ویرایش شده: {response.data[0].url}")

javascript=:import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// توجه: از prompt انگلیسی استفاده کنید
const response = await client.images.edit({
    model: "stability.stable-image-inpaint-v1:0",
    image: fs.createReadStream("input-image-inpaint.jpg"),
    mask: fs.createReadStream("mask-image-inpaint.png"),
    prompt: "artificer of time and space", // prompt انگلیسی
    extra_body: {
        style_preset: "photographic",
        negative_prompt: "blurry, low quality"
    },
    response_format="url", # or b64_json
});

console.log(`تصویر ویرایش شده: ${response.data[0].url}`);

```

#### تغییر رنگ اشیاء (Object Recoloring)

```language-selector
bash=:curl -X POST https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=stability.stable-image-search-recolor-v1:0" \
  -F "image=@input-search-recolor.jpg" \
  -F "prompt=red jacket" \
  -F "select_prompt=jacket"

python=:# تغییر رنگ اشیاء خاص
with open("input-search-recolor.jpg", "rb") as img:
    response = client.images.edit(
        model="stability.stable-image-search-recolor-v1:0",
        image=img,
        prompt="red jacket",  # رنگ/سبک جدید (انگلیسی)
        extra_body={
            "select_prompt": "jacket",  # چه چیزی را تغییر رنگ دهیم (انگلیسی)
            "style_preset": "photographic",
        },
        response_format="url",  # or b64_json
    )

print(f"تصویر تغییر رنگ یافته: {response.data[0].url}")

javascript=:const response = await client.images.edit({
    model: "stability.stable-image-search-recolor-v1:0",
    image: fs.createReadStream("input-search-recolor.jpg"),
    prompt: "red jacket", // رنگ جدید (انگلیسی)
    extra_body: {
        select_prompt: "jacket", // شیء مورد نظر (انگلیسی)
        style_preset: "photographic"
    }
});

```

### نمونه نتایج

| سرویس | تصویر ورودی | تصویر خروجی |
|---------|--------|--------|
| **Inpaint** | ![ورودی](../_media/img/input-image-inpaint.jpg ':size=1000') | ![خروجی](../_media/img/output-image-inpaint.jpg ':size=1000') |
| **Search & Recolor** | ![ورودی](../_media/img/input-search-recolor.jpg ':size=1000') | ![خروجی](../_media/img/output-search-recolor.jpg ':size=1000') |
| **Remove Background** | ![ورودی](../_media/img/input-remove-background.jpg ':size=1000') | ![خروجی](../_media/img/output-remove-background.jpg ':size=1000') |
| **Control Sketch** | ![ورودی](../_media/img/input-control-sketch.jpg ':size=1000') | ![خروجی](../_media/img/output-control-sketch.jpg ':size=1000') |

### پارامترهای پیشرفته

تمام سرویس‌ها از پارامترهای پیشرفته برای تنظیم دقیق نتایج پشتیبانی می‌کنند:

- **Style Presets**: `photographic`، `cinematic`، `digital-art`، `anime` و موارد دیگر
- **Control Strength**: تنظیم تاثیر تصاویر ورودی (۰.۰-۱.۰)
- **Negative Prompts**: مشخص کردن عناصر ناخواسته (به انگلیسی)
- **Seed Values**: تضمین نتایج قابل تکرار
- **Output Formats**: پشتیبانی از PNG، JPEG، WebP

### مدیریت خطا

```language-selector
python=:try:
    response = client.images.edit(
        model="stability.stable-image-inpaint-v1:0",
        image=image_file,
        prompt="Your English prompt here",  # حتما انگلیسی
        response_format="url",  # or b64_json
    )
    print(f"موفقیت: {response.data[0].url}")
except Exception as e:
    if "filter_reason" in str(e):
        print("محتوا فیلتر شد. prompt متفاوتی امتحان کنید.")
    elif "invalid_prompts" in str(e):
        print("prompt نامعتبر شناسایی شد.")
    else:
        print(f"خطای API: {e}")

```

### قیمت‌گذاری

| دسته سرویس | هزینه به ازای هر تصویر | بهترین برای |
|------------------|----------------|----------|
| **سرویس‌های تخصصی تصویر** | ۰.۰۴۰ دلار | کارهای حرفه‌ای ویرایش تصویر |

### مرجع فنی

این پیاده‌سازی‌ها از الگوهای مستندات رسمی AWS Bedrock Stability AI پیروی می‌کنند. برای مشخصات فنی دقیق، به [مستندات AWS Bedrock Stability AI Image Services](https://docs.aws.amazon.com/bedrock/latest/userguide/stable-image-services.html) مراجعه کنید.

---

## لینک‌های مرتبط

- [مرجع API تولید تصویر](fa/api-reference/images.md) - مستندات کامل API
- [راهنمای تولید تصویر](fa/guides/image-generation.md) - راهنمای جامع استفاده
- [نمونه‌های ویرایش تصویر Stability AI](fa/examples/stability_ai_image_editing.md) - راهنمای‌های دقیق
- [پارامترهای خاص ارائه‌دهنده](fa/guides/provider-specific-params.md) - استفاده از پارامترهای پیشرفته