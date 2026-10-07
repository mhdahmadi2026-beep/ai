# تولید و ویرایش تصاویر با مدل‌های Seedream

مدل‌های Seedream از ByteDance قابلیت‌های پیشرفته تولید تصویر را ارائه می‌دهند، از تولید متن-به-تصویر گرفته تا ویرایش پیشرفته تصویر-به-تصویر. این راهنما نحوه استفاده از تمام قابلیت‌های این مدل‌ها را از طریق API یکپارچه AvalAI نشان می‌دهد.

> **نکته مهم**: برای بهترین نتایج، توصیه می‌شود از پرامپت‌های انگلیسی استفاده کنید زیرا مدل‌های تولید تصویر معمولا برای زبان انگلیسی بهینه‌سازی شده‌اند. برای پشتیبانی فنی یا سوالات، با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

## مقدمه

مدل‌های Seedream با ویژگی‌های منحصر به فرد خود متمایز هستند:
- **استدلال زنجیره فکر** (5.0): تحلیل و بهینه‌سازی هوشمند پرامپت
- **زیبایی‌شناسی سبک MJ** (5.0): پشتیبانی داخلی از تولید به سبک Midjourney
- **تولید تصویر متوالی**: ایجاد دسته‌هایی از تصاویر مرتبط موضوعی
- **ترکیب چند تصویر**: ترکیب چندین تصویر مرجع با پرامپت‌های متنی
- **خروجی با وضوح بالا**: تولید تصاویر تا وضوح 4K
- **پشتیبانی جریانی**: تولید تصویر بلادرنگ با به‌روزرسانی‌های تدریجی
- **کنترل پیشرفته**: تنظیم دقیق تولید با پارامترهای تخصصی

## مدل‌های موجود

| مدل | قابلیت‌ها | بهترین کاربرد |
|-------|-------------|----------|
| `seedream-5-0-260128` | استدلال CoT، زیبایی‌شناسی سبک MJ، متن-به-تصویر، تصویر-به-تصویر، بهینه‌سازی هوشمند پرامپت | محتوای خلاقانه پرمیوم، تولید هنری، عکاسی حرفه‌ای |


## استفاده پایه

### تولید متن-به-تصویر

تولید تصاویر با کیفیت بالا از توضیحات متنی:

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید پایه متن-به-تصویر
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="اژدهای باشکوهی که در میان ابرها در غروب آفتاب پرواز می‌کند، سبک هنر دیجیتال، بسیار تفصیلی، نورپردازی سینمایی",
    size="2K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر تولید شده: {response.data[0].url}")
```

### ویرایش تصویر-به-تصویر

تبدیل تصاویر موجود با راهنمایی متنی:

```python
# ویرایش تصویر-به-تصویر
response = client.images.edit(
    model="seedream-5-0-260128",
    image=open("input_image.png", "rb"),
    prompt="این منظره را به شهری سایبرپانک با چراغ‌های نئون و ساختمان‌های آینده‌نگر تبدیل کن",
    size="2K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر ویرایش شده: {response.data[0].url}")
```

## ویژگی‌های پیشرفته

### تولید تصویر متوالی

ایجاد دسته‌هایی از تصاویر مرتبط موضوعی به‌طور خودکار:

```python
# تولید متوالی - اجازه به مدل برای تصمیم‌گیری درباره تعداد تصاویر
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="داستان جنگل جادویی در چهار فصل، هر کدام موجودات جادویی متفاوت و تغییرات جوی را نشان می‌دهد",
    size="2K",
    extra_body={
        "sequential_image_generation": "auto",
        "sequential_image_generation_options": {"max_images": 6},
        "watermark": False,
    },
)

print(f"{len(response.data)} تصویر تولید شد:")
for i, image in enumerate(response.data):
    print(f"تصویر {i+1}: {image.url}")
```

### ترکیب چند تصویر

ترکیب چندین تصویر مرجع برای ایجاد چیزی جدید:

```python
# ترکیب چند تصویر
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="طراحی معماری مدرن که این سبک‌های مختلف را به‌طور هماهنگ ترکیب می‌کند",
    extra_body={
        "image": [
            "https://example.com/gothic-cathedral.jpg",
            "https://example.com/modern-skyscraper.jpg",
            "https://example.com/traditional-japanese-temple.jpg",
        ],
        "sequential_image_generation": "disabled",
        "size": "2K",
        "watermark": False,
    },
)

print(f"معماری ترکیبی: {response.data[0].url}")
```

### تولید جریانی

دریافت به‌روزرسانی‌های بلادرنگ در حین تولید تصاویر:

```python
import requests
import json


def stream_image_generation():
    url = "https://api.avalai.ir/v1/images/generations"
    headers = {
        "Authorization": "Bearer your-avalai-api-key",
        "Content-Type": "application/json",
    }

    data = {
        "model": "seedream-5-0-260128",
        "prompt": "مجموعه‌ای از آثار هنری مفهومی برای بازی فانتزی، نشان دادن محیط‌ها و شخصیت‌های مختلف",
        "size": "2K",
        "stream": True,
        "sequential_image_generation": "auto",
        "sequential_image_generation_options": {"max_images": 5},
        "watermark": False,
    }

    response = requests.post(url, headers=headers, json=data, stream=True)

    for line in response.iter_lines():
        if line:
            try:
                chunk = json.loads(line.decode("utf-8").replace("data: ", ""))
                if "data" in chunk:
                    for image in chunk["data"]:
                        if "url" in image:
                            print(f"تصویر جدید آماده: {image['url']}")
                            print(f"اندازه: {image.get('size', 'نامشخص')}")
            except json.JSONDecodeError:
                continue


# اجرای تولید جریانی
stream_image_generation()
```

## کنترل وضوح و کیفیت

### تولید با وضوح بالا

تولید تصاویر در وضوح‌های مختلف:

```python
# تولید با وضوح 4K بالا
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="پرتره فوق‌العاده تفصیلی از شخصیت سایبرپانک با تقویت‌های مکانیکی پیچیده، نورپردازی عکاسی حرفه‌ای، کیفیت 8K",
    size="4K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر 4K: {response.data[0].url}")
print(f"اندازه واقعی: {response.data[0].size}")
```

### نسبت‌های ابعاد سفارشی

تولید تصاویر با ابعاد خاص:

```python
# نسبت ابعاد سفارشی - نمای پهن سینمایی
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="نمای پهن سینمایی از نبرد کشتی فضایی در اعماق فضا، مقیاس حماسی، نورپردازی دراماتیک",
    size="3024x1296",  # نسبت ابعاد 21:9
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر سینمایی: {response.data[0].url}")

# جهت عمودی
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="برج بلند فانتزی که به ابرها می‌رسد، ترکیب‌بندی عمودی، معماری تفصیلی",
    size="1440x2560",  # نسبت ابعاد 9:16
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر عمودی: {response.data[0].url}")
```

## کاربردهای خلاقانه

### انتقال سبک و جلوه‌های هنری

```python
# مثال انتقال سبک
response = client.images.edit(
    model="seedream-5-0-260128",
    image=open("input_image.png", "rb"),
    prompt="این عکس را به سبک نقاشی ون گوگ با ضربه‌های قلم‌موی چرخان و رنگ‌های پرجنب‌وجوش تبدیل کن",
    size="2K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"سبک ون گوگ: {response.data[0].url}")

# تنوع‌های سبک متعدد
response = client.images.edit(
    model="seedream-5-0-260128",
    image=open("input_image.png", "rb"),
    prompt="تنوع‌های هنری این پرتره در سبک‌های مختلف: نقاشی روغن، آبرنگ، هنر دیجیتال، و طراحی با مداد",
    size="2K",
    extra_body={
        "sequential_image_generation": "auto",
        "sequential_image_generation_options": {"max_images": 4},
        "watermark": False,
    },
)

print(f"{len(response.data)} تنوع سبک تولید شد:")
for i, image in enumerate(response.data):
    print(f"سبک {i+1}: {image.url}")
```

### تجسم محصولات

```python
# تولید نمونه محصول
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="گوشی هوشمند شیک مدرن روی میز کار مینیمالیست، عکاسی حرفه‌ای محصول، پس‌زمینه تمیز، نورپردازی استودیو",
    size="2K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"نمونه محصول: {response.data[0].url}")

# زاویه‌های متعدد محصول
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="عکس‌های حرفه‌ای محصول از ساعت لوکس از زاویه‌های مختلف: نمای جلو، نمای کناری، نمای پشت، و عکس روی مچ دست",
    size="2K",
    extra_body={
        "sequential_image_generation": "auto",
        "sequential_image_generation_options": {"max_images": 4},
        "watermark": False,
    },
)

print(f"{len(response.data)} زاویه محصول تولید شد:")
for i, image in enumerate(response.data):
    print(f"زاویه {i+1}: {image.url}")
```

### طراحی شخصیت و هنر مفهومی

```python
# تنوع‌های طراحی شخصیت
response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="طراحی شخصیت فانتزی: جادوگر قدرتمند با قابلیت‌های جادویی منحصر به فرد، نشان دادن تنوع‌های لباس و ژست‌های مختلف",
    size="2K",
    extra_body={
        "sequential_image_generation": "auto",
        "sequential_image_generation_options": {"max_images": 6},
        "watermark": False,
    },
)

print(f"تنوع‌های شخصیت: {len(response.data)} طراحی")
for i, image in enumerate(response.data):
    print(f"طراحی {i+1}: {image.url}")
```

## نمونه‌های JavaScript/Node.js

### استفاده پایه با Node.js

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

async function generateImage() {
    try {
        const response = await client.images.generate({
            model: "seedream-5-0-260128",
            prompt: "غروب زیبا روی منظره کوهستانی، واقع‌گرایانه، جزئیات بالا",
            size: "2K",
            response_format: "url",
            // @ts-expect-error extra_body is a provider-specific parameter
            extra_body: {
                "sequential_image_generation": "disabled",
                "watermark": false
            }
        });

        console.log("تصویر تولید شده:", response.data[0].url);
        return response.data[0].url;
    } catch (error) {
        console.error("خطا در تولید تصویر:", error);
    }
}

generateImage();
```

### تولید متوالی با Node.js

```javascript
async function generateImageSeries() {
    try {
        const response = await client.images.generate({
            model: "seedream-5-0-260128",
            prompt: "داستان تایم‌لپس شهر از طلوع تا نیمه‌شب، نشان دادن تغییر جو و نورپردازی",
            size: "2K",
            // @ts-expect-error extra_body is a provider-specific parameter
            extra_body: {
                "sequential_image_generation": "auto",
                "sequential_image_generation_options": {
                    "max_images": 8
                },
                "watermark": false
            }
        });

        console.log(`${response.data.length} تصویر در سری تولید شد:`);
        response.data.forEach((image, index) => {
            console.log(`زمان ${index + 1}: ${image.url}`);
        });

        return response.data;
    } catch (error) {
        console.error("خطا در تولید سری تصاویر:", error);
    }
}

generateImageSeries();
```

## تماس‌های مستقیم API

### استفاده از cURL

```bash
# تولید پایه متن-به-تصویر
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "seedream-5-0-260128",
    "prompt": "منظره شهری آینده‌نگر در شب با ماشین‌های پرنده و چراغ‌های نئون",
    "sequential_image_generation": "disabled",
    "response_format": "url",
    "size": "2K",
    "watermark": false
  }'

# تولید متوالی
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "seedream-5-0-260128",
    "prompt": "مجموعه‌ای از موجودات فانتزی در زیستگاه‌های طبیعی‌شان",
    "sequential_image_generation": "auto",
    "sequential_image_generation_options": {
      "max_images": 5
    },
    "response_format": "url",
    "size": "2K",
    "watermark": false
  }'

# ویرایش تصویر
curl https://api.avalai.ir/v1/images/edits \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "seedream-5-0-260128",
    "image": "https://example.com/input-image.jpg",
    "prompt": "عناصر جادویی و نورپردازی فانتزی به این صحنه اضافه کن",
    "sequential_image_generation": "disabled",
    "response_format": "url",
    "size": "2K",
    "watermark": false
  }'
```

## بهترین شیوه‌ها

### مهندسی پرامپت

1. **مشخص و تفصیلی باشید**

```python
# پرامپت خوب
prompt = "کشتی هوایی استیم‌پانک که در میان ابرهای طوفانی پرواز می‌کند، جزئیات برنج و مس، طراحی دوران ویکتوریا، نورپردازی دراماتیک با رعد و برق، اجزای مکانیکی بسیار تفصیلی، ترکیب‌بندی سینمایی"

# پرامپت کم‌تاثیر
prompt = "کشتی هوایی جالب"
```

2. **مشخصات فنی را شامل کنید**

```python
prompt = "عکاسی حرفه‌ای محصول از ساعت لوکس، لنز ماکرو، نورپردازی استودیو، پس‌زمینه سفید، کیفیت تجاری، وضوح بالا، فوکوس تیز"
```

3. **سبک هنری را مشخص کنید**

```python
prompt = "نقاشی دیجیتال به سبک هنر مفهومی، تکنیک مت پینتینگ، رندرینگ واقع‌گرایانه، ترند در ArtStation"
```

### بهینه‌سازی عملکرد

1. **وضوح مناسب را انتخاب کنید**

```python
# برای استفاده وب
size = "1K"  # تولید سریع‌تر

# برای چاپ یا کار تفصیلی
size = "4K"  # کیفیت بالاتر، تولید آهسته‌تر
```

2. **از جریان برای تولید دسته‌ای استفاده کنید**

```python
# فعال‌سازی جریان برای چندین تصویر
extra_body = {"stream": True, "sequential_image_generation": "auto"}
```

3. **اندازه دسته‌ها را بهینه کنید**

```python
# تعادل بین کارایی و استفاده از منابع
sequential_image_generation_options = {
    "max_images": 5  # نقطه بهینه برای اکثر موارد استفاده
}
```

## مدیریت خطا

```python
import time
from openai import OpenAI


def robust_image_generation(prompt, max_retries=3):
    client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

    for attempt in range(max_retries):
        try:
            response = client.images.generate(
                model="seedream-5-0-260128",
                prompt=prompt,
                size="2K",
                response_format="url",
                extra_body={
                    "sequential_image_generation": "disabled",
                    "watermark": False,
                },
            )

            # بررسی موفقیت تولید
            if response.data and response.data[0].url:
                return response.data[0].url
            else:
                raise Exception("هیچ URL تصویری در پاسخ وجود ندارد")

        except Exception as e:
            print(f"تلاش {attempt + 1} ناموفق: {str(e)}")
            if attempt < max_retries - 1:
                time.sleep(2**attempt)  # تاخیر نمایی
            else:
                raise e


# استفاده
try:
    image_url = robust_image_generation("نقاشی منظره زیبا")
    print(f"تولید موفق: {image_url}")
except Exception as e:
    print(f"تولید تصویر پس از همه تلاش‌ها ناموفق: {e}")
```

## نتیجه‌گیری

Seedream 5.0 قابلیت‌های بی‌نظیری را برای تولید و ویرایش تصویر ارائه می‌دهد. ویژگی‌های منحصر به فرد آن مانند تولید متوالی، ترکیب چند تصویر و پشتیبانی جریانی آن را برای کاربردهای خلاقانه و تجاری ایده‌آل می‌کند. با پیروی از نمونه‌ها و بهترین شیوه‌های این راهنما، می‌توانید تمام قدرت این مدل پیشرفته را از طریق API یکپارچه AvalAI به کار بگیرید.

## منابع مرتبط

- [مستندات مدل‌های BytePlus](fa/providers/byteplus.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API](fa/api-reference/images.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
