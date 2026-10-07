# تولید و ویرایش تصاویر با سری Nano Banana

## مقدمه

**Nano Banana** نام قابلیت‌های تولید تصویر بومی Gemini است. Gemini می‌تواند تصاویر را به صورت مکالمه‌ای با متن، تصاویر یا ترکیبی از هر دو تولید و پردازش کند. این امکان را به شما می‌دهد تا تصاویر بصری را با کنترل بی‌سابقه ایجاد، ویرایش و تکرار کنید.

خانواده Nano Banana شامل سه مدل متمایز است که از طریق AvalAI در دسترس هستند:

| مدل | شناسه | بهترین برای |
|-----|-------|-------------|
| **Nano Banana 2** | `gemini-3.1-flash-image` | پربازده، بهینه‌سازی شده برای سرعت، موارد استفاده توسعه‌دهندگان با حجم بالا |
| **Nano Banana Pro** | `gemini-3-pro-image` | تولید دارایی‌های حرفه‌ای، دستورالعمل‌های پیچیده، رندر متن با کیفیت بالا |
| **Nano Banana** | `gemini-2.5-flash-image` | سرعت و کارایی، حجم بالا، وظایف با تاخیر کم |

این راهنما هر سه مدل را پوشش می‌دهد و نشان می‌دهد چگونه از آن‌ها از طریق API AvalAI برای تولید، ویرایش و تبدیل تصاویر با زبان طبیعی استفاده کنید.

> **توجه:** اکنون هر سه مدل دارای نام مستعار پایدار هستند. توصیه می‌کنیم برای محیط‌های تولید از شناسه‌های پایدار (`gemini-2.5-flash-image`، `gemini-3.1-flash-image` و `gemini-3-pro-image`) استفاده کنید. شناسه‌های پیش‌نمایش متناظر (`gemini-2.5-flash-image-preview`، `gemini-3.1-flash-image-preview` و `gemini-3-pro-image-preview`) همچنان در دسترس هستند.

> **نکته مهم**: برای بهترین نتایج، توصیه می‌شود از پرامپت‌های انگلیسی استفاده کنید زیرا مدل‌های تولید تصویر معمولا برای زبان انگلیسی بهینه‌سازی شده‌اند. برای پشتیبانی فنی یا سوالات، با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

## ویژگی‌های کلیدی

- **تولید تصویر پیشرفته** - ایجاد تصاویر با کیفیت بالا و واقع‌گرایانه از دستورات متنی دقیق
- **ویرایش پیشرفته تصویر** - تبدیل تصاویر موجود با دستورالعمل‌های زبان طبیعی
- **ثبات شخصیت** - حفظ ظاهر ثابت سوژه‌ها در چندین تولید
- **ادغام چند تصویر** - ترکیب چندین تصویر ورودی در ترکیب‌بندی‌های منسجم
- **ویرایش مکالمه‌ای** - بهبود تکراری از طریق گفتگوی طبیعی
- **ادغام دانش جهانی** - استفاده از دانش Gemini برای تصاویر دقیق از نظر زمینه‌ای
- **تبدیل‌های مبتنی بر دستور** - انجام ویرایش‌های دقیق با دستورات متنی ساده

## تولید پایه تصویر

برای تولید یک تصویر با Gemini 2.5 Flash Image باید یک دستور متنی ارائه دهید که آنچه می‌خواهید ایجاد کنید را توصیف می‌کند. این مدل در درک توضیحات دقیق و ایجاد تصاویری که با دید شما مطابقت دارد، برتری دارد.

```python
from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تولید تصویر از متن
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند، نقاشی شده به سبک نقاشی منظره رمانتیک",
        }
    ],
    modalities=["image", "text"],
)

# Image is now available in the response
image_url = response.choices[0].message.images[0]["image_url"]["url"]
content = (
    response.choices[0].message.content.strip()
    if response.choices[0].message.content
    else None
)

# پردازش داده‌های تصویر برگشتی
header, base64_data = image_url.split(",", 1)
ext = header.split(";")[0].split("/")[1]  # مثل "png" یا "jpeg"

# رمزگشایی و ذخیره تصویر
image_bytes = base64.b64decode(base64_data)
filename = f"generated_image.{ext}"
with open(filename, "wb") as f:
    f.write(image_bytes)
print(f"✅ تصویر ذخیره شد به عنوان {filename}")

# چاپ هر پاسخ متنی که همراه تصویر آمده
if content:
    print(f"پاسخ مدل: {content}")

```

```javascript
import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// تولید تصویر از متن
const response = await client.chat.completions.create({
 model: "gemini-2.5-flash-image",
 messages: [{
 role: "user",
 content: "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند، نقاشی شده به سبک نقاشی منظره رمانتیک"
 }],
 modalities: ["image", "text"],
});

// Image is now available in the response
const imageUrl = response.choices[0].message.images[0].image_url.url;
const content = response.choices[0].message.content ? response.choices[0].message.content.trim() : null;

// پردازش داده‌های تصویر برگشتی
const [header, base64Data] = imageUrl.split(",", 2);
const ext = header.split(";")[0].split("/")[1];

// رمزگشایی و ذخیره تصویر
const imageBytes = Buffer.from(base64Data, 'base64');
const filename = `generated_image.${ext}`;
fs.writeFileSync(filename, imageBytes);
console.log(`✅ تصویر ذخیره شد به عنوان ${filename}`);

// چاپ هر پاسخ متنی که همراه تصویر آمده
if (content) {
 console.log(`پاسخ مدل: ${content}`);
}

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند، نقاشی شده به سبک نقاشی منظره رمانتیک",
                },
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند، نقاشی شده به سبک نقاشی منظره رمانتیک" },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند، نقاشی شده به سبک نقاشی منظره رمانتیک"
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## ویرایش و تبدیل تصویر

Gemini 2.5 Flash Image در ویرایش تصاویر موجود بر اساس دستورالعمل‌های زبان طبیعی برتری دارد. می‌توانید تصاویر مرجع ارائه دهید و از مدل بخواهید تغییرات یا تبدیل‌های خاصی انجام دهد.

### ویرایش پایه تصویر به تصویر

```python
# تبدیل تصویر به تصویر
prompt = (
    "این تصویر را به سبک انیمه Studio Ghibli با رنگ‌های پرجنب و جو و حال جادویی تبدیل کن"
)
image_url = "https://example.com/your-image.jpg"

# استفاده از URL تصویر
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": prompt},
            {"type": "image_url", "image_url": {"url": image_url}},
        ],
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)

# پردازش پاسخ مشابه تولید متن به تصویر
image_url = response.choices[0].message.images[0]["image_url"]["url"]
content = (
    response.choices[0].message.content.strip()
    if response.choices[0].message.content
    else None
)
# ... (همان کد پردازش بالا)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### استفاده از تصاویر کدگذاری شده Base64

برای سازگاری بهتر و هنگام کار با تصاویر محلی، می‌توانید تصاویر را به عنوان base64 کدگذاری کنید:

```python
import base64


def encode_image(image_path):
    """کدگذاری تصویر به رشته base64"""
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


# بارگذاری و کدگذاری تصویر شما
image_path = "path/to/your/image.jpg"
base64_image = encode_image(image_path)

# ایجاد پیام با تصویر base64
messages = [
    {
        "role": "user",
        "content": [
            {
                "type": "text",
                "text": "پس‌زمینه را به محیط ساحل گرمسیری تغییر بده در حالی که سوژه بدون تغییر باقی بماند",
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
            },
        ],
    }
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## قابلیت‌های پیشرفته

### ثبات شخصیت

یکی از ویژگی‌های برجسته Gemini 2.5 Flash Image حفظ ثبات شخصیت در چندین تولید است. می‌توانید یک شخصیت ایجاد کنید و سپس آن‌ها را در سناریوهای مختلف قرار دهید در حالی که ظاهرشان حفظ می‌شود.

```python
# ابتدا، یک شخصیت ایجاد کنید
character_prompt = "یک پرتره واقع‌گرایانه از یک زن جوان با موهای فرفری قرمز، چشمان سبز، پوشیده کت جین آبی ایجاد کن. او لبخند دوستانه و کک و مک دارد."

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[{"role": "user", "content": character_prompt}],
    modalities=["image", "text"],
)

# این تصویر شخصیت را ذخیره کنید، سپس از آن به عنوان مرجع برای ظاهر ثابت استفاده کنید
# در دستورات بعدی، می‌توانید به این شخصیت اشاره کنید:
consistency_prompt = "همان شخص از تصویر قبلی را نشان بده که حالا در خیابان شلوغ شهر در شب ایستاده، با نورهای نئون که روی سنگفرش خیس منعکس می‌شود"
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Describe this image.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### ادغام چند تصویر

ترکیب چندین تصویر برای ایجاد ترکیب‌بندی‌های جدید:

```python
# ترکیب دو تصویر
fusion_prompt = "این دو تصویر را ترکیب کن: شخص تصویر اول را در مکان زیبای تصویر دوم قرار بده، مطمئن شو که نورپردازی و جو و حال به طور طبیعی با هم تطبیق داشته باشند"

# می‌توانید چندین تصویر را در آرایه محتوا قرار دهید
messages = [
    {
        "role": "user",
        "content": [
            {"type": "text", "text": fusion_prompt},
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image1}"},
            },
            {
                "type": "image_url",
                "image_url": {"url": f"data:image/jpeg;base64,{base64_image2}"},
            },
        ],
    }
]
```

### ویرایش مکالمه‌ای تصویر

می‌توانید با مدل مکالمه کنید تا تصاویرتان را به صورت تکراری بهبود دهید:

```python
# شروع با تولید تصویر اولیه
messages = [
    {"role": "user", "content": "یک فضای داخلی کافه‌ای دنج با نورپردازی گرم ایجاد کن"}
]

response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)

# پاسخ مدل را اضافه کنید تا مکالمه ادامه یابد
messages.append({"role": "assistant", "content": response.choices[0].message.content})

# حالا بهبودها را انجام دهید
messages.append(
    {
        "role": "user",
        "content": "نورپردازی را گرم‌تر کن و چند گیاه نزدیک پنجره‌ها اضافه کن",
    }
)

# مکالمه را برای بهبودهای بیشتر ادامه دهید
refined_response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=messages,
    modalities=["image", "text"],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="نورپردازی را گرم‌تر کن و چند گیاه نزدیک پنجره‌ها اضافه کن",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## بهترین شیوه‌های مهندسی دستور

### 1. دقیق و جزئی باشید

مدل به توضیحات دقیق که شامل موارد زیر است به خوبی پاسخ می‌دهد:
- **مشخصات سبک**: "واقع‌گرایانه"، "نقاشی رنگ روغن"، "هنر دیجیتال"، "سبک Studio Ghibli"
- **جزئیات نورپردازی**: "نورپردازی ساعت طلایی"، "سایه‌های دراماتیک"، "نور ملایم پراکنده"
- **عناصر ترکیب‌بندی**: "قانون سوم"، "پرتره نزدیک"، "نمای گسترده منظره"
- **پارامترهای فنی**: "عمق میدان کم"، "کنتراست بالا"، "رنگ‌های پرجنب و جو"

```python
detailed_prompt = """
یک پرتره واقع‌گرایانه از یک صنعتگر مسن در کارگاهش ایجاد کن.
نورپردازی: نور گرم و طلایی که از پنجره غبارآلود می‌تابد و سایه‌های دراماتیک ایجاد می‌کند.
ترکیب‌بندی: نمای نزدیک متمرکز بر دستان کهنه‌اش که روی تکه چوبی کار می‌کند.
سبک: سبک عکاسی مستند با بافت‌های غنی و جزئیات بالا.
حال و هوا: تاملی و آرام، نشان‌دهنده زیبایی صنعتگری سنتی.
"""
```

### 2. سبک‌های هنری را مشخص کنید

```python
style_examples = [
    "به سبک شب پرستاره ون گوگ با ضربه قلم‌های چرخان",
    "به عنوان یک طراحی خطی مینیمالیستی با اشکال هندسی تمیز",
    "به سبک پوسترهای تبلیغاتی قدیمی دهه 1950",
    "به عنوان هنر دیجیتال سایبرپانک با رنگ‌های نئون و عناصر آینده‌نگرانه",
    "به سبک چاپ‌های چوبی ژاپنی با رنگ‌های پررنگ و خطوط تمیز",
]
```

### 3. از زمینه مرجع استفاده کنید

هنگام ویرایش تصاویر، زمینه واضحی در مورد آنچه باید تغییر کند و آنچه باید یکسان بماند ارائه دهید:

```python
editing_prompt = """
این تصویر پرتره را با تغییرات زیر تبدیل کن:
- پس‌زمینه را به محیط کتابخانه با قفسه‌های کتاب تغییر بده
- ژست و بیان چهره شخص را دقیقا همان نگه دار
- نورپردازی را تنظیم کن تا با نورپردازی گرم و محیطی کتابخانه تطبیق داشته باشد
- همان سطح جزئیات و کیفیت واقع‌گرایانه را حفظ کن
"""
```

### 4. از دانش جهانی استفاده کنید

Gemini 2.5 Flash Image می‌تواند از دانش خود در مورد مکان‌های واقعی، دوره‌های تاریخی و زمینه‌های فرهنگی استفاده کند:

```python
knowledge_prompt = """
یک صحنه تاریخی دقیق از بازار اروپایی قرون وسطی در قرن چهاردهم ایجاد کن.
شامل لباس‌های مناسب دوره، معماری و فعالیت‌های زندگی روزانه باشد.
تاجران در حال فروش کالا، مردم با لباس‌های اصیل قرون وسطایی و ساختمان‌های معمولی قرون وسطی را نشان بده.
از نظر تاریخی دقیق باشد در حالی که زیبایی هنری را حفظ کند.
"""
```

## مشخصات فنی

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `gemini-2.5-flash-image` |
| پنجره زمینه | 32,768 توکن (ورودی) |
| حداکثر توکن‌های خروجی | 32,768 توکن |
| ورودی‌های پشتیبانی شده | تصاویر و متن |
| خروجی‌های پشتیبانی شده | تصاویر و متن |
| قیمت‌گذاری ورودی | $0.30 / 1M توکن |
| قیمت‌گذاری خروجی | $2.50 / 1M توکن (متن)، $30.00 / 1M توکن (تولید تصویر) |
| قطع دانش | ژوئن 2025 |

### استفاده از تنظیمات اختصاصی Gemini (generationConfig)

هنگام استفاده از مدل‌های Nano Banana (`gemini-2.5-flash-image`، `gemini-3.1-flash-image` و `gemini-3-pro-image`) از طریق endpoint سازگار با OpenAI (`v1/chat/completions`)، می‌توانید تنظیمات اختصاصی Gemini (پارامترهای غیر OpenAI) را از طریق دیکشنری `extra_body` ارسال کنید. این به شما امکان می‌دهد از ویژگی‌های بومی Gemini مانند `aspectRatio` و `imageSize` در حین استفاده از رابط آشنای SDK OpenAI بهره‌مند شوید.

> **توجه:** کاربران همچنین می‌توانند از [API بومی Gemini (v1beta)](fa/api-reference/v1beta.md) برای دسترسی به Gemini از طریق schema API بومی و SDK رسمی گوگل برای کنترل کامل پارامترها استفاده کنند.

**پارامترهای پشتیبانی شده imageConfig:**

| پارامتر | نوع | توضیحات | مقادیر پشتیبانی شده | مدل‌های پشتیبانی شده |
|---------|-----|---------|---------------------|---------------------|
| `aspectRatio` | string | نسبت ابعاد تصویر | "1:1", "2:3", "3:2", "3:4", "4:3", "4:5", "5:4", "9:16", "16:9", "21:9" | `gemini-2.5-flash-image`, `gemini-3.1-flash-image`, `gemini-3-pro-image` |
| `imageSize` | string | اندازه تصویر خروجی | "1K", "2K", "4K" | `gemini-3.1-flash-image`, `gemini-3-pro-image` |

#### Gemini 2.5 Flash Image (Nano Banana) با نسبت ابعاد

```python
from openai import OpenAI
import base64

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# تولید تصویر با نسبت ابعاد سفارشی با استفاده از extra_body
response = client.chat.completions.create(
    model="gemini-2.5-flash-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a sunset beach scene",
                },
            ],
        }
    ],
    modalities=["image", "text"],
    extra_body={"generationConfig": {"imageConfig": {"aspectRatio": "16:9"}}},
)

# دسترسی به تصویر تولید شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر تولید شده: {image_url}")

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// تولید تصویر با نسبت ابعاد سفارشی با استفاده از extra_body
const response = await client.chat.completions.create({
    model: "gemini-2.5-flash-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "text",
                    text: "Generate a sunset beach scene"
                }
            ]
        }
    ],
    modalities: ["image", "text"],
    extra_body: {
        generationConfig: {
            imageConfig: {
                aspectRatio: "16:9"
            }
        }
    }
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر تولید شده: ${imageUrl}`);
}

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### Gemini 3 Pro Image Preview (Nano Banana Pro) با نسبت ابعاد و اندازه تصویر

مدل `gemini-3-pro-image` (Nano Banana Pro) از هر دو پارامتر `aspectRatio` و `imageSize` پشتیبانی می‌کند و به شما امکان تولید تصاویر با رزولوشن تا 4K را می‌دهد:

```python
from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

# تولید تصویر 4K با نسبت ابعاد سفارشی
response = client.chat.completions.create(
    model="gemini-3-pro-image",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "Generate a sunset beach scene",
                },
            ],
        }
    ],
    modalities=["image", "text"],
    extra_body={
        "generationConfig": {
            "imageConfig": {
                "aspectRatio": "16:9",
                "imageSize": "4k",  # توسط gemini-3.1-flash-image و gemini-3-pro-image پشتیبانی می‌شود
            }
        }
    },
)

# دسترسی به تصویر تولید شده
if response.choices[0].message.images:
    image_url = response.choices[0].message.images[0]["image_url"]["url"]
    print(f"URL تصویر 4K تولید شده: {image_url}")

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

// تولید تصویر 4K با نسبت ابعاد سفارشی
const response = await client.chat.completions.create({
    model: "gemini-3-pro-image",
    messages: [
        {
            role: "user",
            content: [
                {
                    type: "text",
                    text: "Generate a sunset beach scene"
                }
            ]
        }
    ],
    modalities: ["image", "text"],
    extra_body: {
        generationConfig: {
            imageConfig: {
                aspectRatio: "16:9",
                imageSize: "4k"  // توسط gemini-3.1-flash-image و gemini-3-pro-image پشتیبانی می‌شود
            }
        }
    }
});

if (response.choices[0].message.images) {
    const imageUrl = response.choices[0].message.images[0].image_url.url;
    console.log(`URL تصویر 4K تولید شده: ${imageUrl}`);
}

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
      ],
    },
  ],
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**نمونه cURL:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-3-pro-image",
    "messages": [
      {
        "role": "user",
        "content": "Generate a sunset beach scene"
      }
    ],
    "modalities": ["image", "text"],
    "extra_body": {
      "generationConfig": {
        "imageConfig": {
          "aspectRatio": "16:9",
          "imageSize": "4k"
        }
      }
    }
  }'
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-3-pro-image` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Generate a sunset beach scene",
    "instructions": "You are a helpful assistant."
  }'
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای اطلاعات بیشتر در مورد پارامترهای اختصاصی ارائه‌دهنده، به [راهنمای پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md) مراجعه کنید.

### فرمت خروجی تصویر

تصاویر به عنوان URL‌های داده کدگذاری شده base64 در پاسخ متنی برگردانده می‌شوند. فرمت:
```
data:image/[format];base64,[base64-encoded-image-data]
```

که `[format]` معمولا `png` یا `jpeg` است.

## رسیدگی به خطا و عیب‌یابی

### مسائل رایج و راه‌حل‌ها

1. **هیچ تصویری در پاسخ نیست**: بررسی کنید که `modalities=["image", "text"]` را در درخواست خود گنجانده‌اید.

2. **خطاهای رمزگشایی Base64**: مطمئن شوید که URL داده را به درستی تقسیم می‌کنید و فقط بخش base64 را استخراج می‌کنید.

3. **مسائل کیفیت تصویر**: سعی کنید در دستورات خود در مورد کیفیت، سبک و جزئیات فنی مورد نظر دقیق‌تر باشید.

```python
def safe_extract_image(response):
    """استخراج و ذخیره ایمن تصویر از پاسخ مدل"""
    try:
        if (
            not hasattr(response.choices[0].message, "images")
            or not response.choices[0].message.images
        ):
            print("هیچ تصویری در پاسخ یافت نشد")
            return None

        image_url = response.choices[0].message.images[0]["image_url"]["url"]

        header, base64_data = image_url.split(",", 1)
        ext = header.split(";")[0].split("/")[1]

        image_bytes = base64.b64decode(base64_data)
        filename = f"generated_image.{ext}"

        with open(filename, "wb") as f:
            f.write(image_bytes)

            print(f"✅ تصویر ذخیره شد به عنوان {filename}")
            return filename

    except Exception as e:
        print(f"خطا در پردازش تصویر: {e}")
        return None
```

## مقایسه با سایر مدل‌ها

### Gemini 2.5 Flash Image در مقابل GPT Image 1

| ویژگی | Gemini 2.5 Flash Image | GPT Image 1 |
|---------|-------------------------------|-------------|
| **نقاط قوت** | ثبات شخصیت، ویرایش مکالمه‌ای، ادغام دانش جهانی | پیروی پیشرفته از دستورالعمل، پشتیبانی از ماسک، گزینه‌های اندازه متعدد |
| **کیفیت تصویر** | پیشرفته، امتیاز بالا | کیفیت بالا، واقع‌گرایانه |
| **رویکرد ویرایش** | مکالمه زبان طبیعی | کنترل مستقیم پارامتر |
| **پشتیبانی چند تصویر** | قابلیت‌های ادغام عالی | تا 10 تصویر ورودی |
| **رابط API** | تکمیل چت با modalities | اندپوینت اختصاصی تصاویر |

### چه زمانی Gemini 2.5 Flash Image را انتخاب کنیم

- **ثبات شخصیت** در چندین تصویر
- **گردش کار ویرایش مکالمه‌ای**
- **پروژه‌های ادغام چند تصویر**
- **کاربردهای آموزشی** با استفاده از دانش جهانی
- **بهبود تکراری** از طریق گفتگو
- **تبدیل سبک** با دقت فرهنگی/تاریخی

## محدودیت‌ها و ملاحظات

- **ارائه متن**: مانند اکثر مدل‌های تولید تصویر، متن درون تصاویر ممکن است ناسازگار باشد
- **صحنه‌های پیچیده**: صحنه‌های بسیار دقیق با عناصر زیاد ممکن است به طور کامل ارائه نشوند
- **فرمت پاسخ**: تصاویر در پاسخ‌های متنی تعبیه‌سازی می‌شوند به جای URL‌های جداگانه
- **زمان پردازش**: تولید با کیفیت بالا ممکن است بیشتر از مدل‌های ساده‌تر طول بکشد
- **پنجره زمینه**: محدود به 32,768 توکن برای ورودی و خروجی

## نتیجه‌گیری

Gemini 2.5 Flash Image نشان‌دهنده پیشرفت قابل توجهی در تولید و ویرایش تصویر هوش مصنوعی است و قابلیت‌های قدرتمندی برای ایجاد و تبدیل تصاویر از طریق زبان طبیعی ارائه می‌دهد. ویژگی‌های برجسته آن—ثبات شخصیت، ویرایش مکالمه‌ای و ادغام دانش جهانی—آن را به ویژه برای متخصصان خلاق، مربیان و توسعه‌دهندگانی که برنامه‌های متمرکز بر تصویر می‌سازند، ارزشمند می‌کند.

قابلیت مدل برای حفظ ثبات در تولیدها و درک دستورالعمل‌های ویرایش پیچیده از طریق گفتگو، امکانات جدیدی را برای گردش کارهای خلاقانه با کمک هوش مصنوعی باز می‌کند. چه در حال تولید آثار هنری اصلی، ویرایش عکس‌های موجود یا ایجاد محتوای تصویری آموزشی باشید، Gemini 2.5 Flash Image ابزارهایی را برای زنده کردن دید شما فراهم می‌کند.

برای اطلاعات بیشتر در مورد تولید تصویر با AvalAI، لطفا به [راهنمای تولید تصویر](fa/guides/image-generation.md) و [مستندات مدل‌های گوگل](fa/providers/google.md) ما مراجعه کنید.
