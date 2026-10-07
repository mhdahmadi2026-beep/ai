# تولید تصاویر با مدل‌های GPT Image

## مقدمه

خانواده مدل‌های GPT Image نمایانگر مدل‌های تولید تصویر OpenAI هستند که درک پیشرفته زبان را با قابلیت‌های تولید تصویر پیشرفته ترکیب می‌کنند. این راهنما به شما نشان می‌دهد چگونه از این مدل‌ها از طریق API AvalAI برای تولید و ویرایش تصاویر استفاده کنید.

> **نکته مهم**: برای بهترین نتایج، توصیه می‌شود از پرامپت‌های انگلیسی استفاده کنید زیرا مدل‌های تولید تصویر معمولا برای زبان انگلیسی بهینه‌سازی شده‌اند. برای پشتیبانی فنی یا سوالات، با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

## گزینه‌های مدل

### GPT Image 2 (تازه‌ترین)
مدل نسل بعدی OpenAI برای تولید تصویر. این مدل با بهبودهای قابل توجهی نسبت به GPT Image 1.5 ارائه می‌شود:
- **بهترین پایبندی به prompt در رده خود** - درک برتر از پرامپت‌های چندبخشی و دقیق
- **وفاداری بصری بالاتر** - خروجی‌های واقع‌گرایانه‌تر با جزئیات ظریف‌تر
- **رندر متن قوی‌تر** - رندر دقیق تایپوگرافی، لوگو و علائم
- **هزینه خروجی پایین‌تر** - خروجی متن از $32.00/۱ میلیون به $10.00/۱ میلیون و خروجی تصویر از $32.00/۱ میلیون به $30.00/۱ میلیون در مقایسه با GPT Image 1.5 کاهش یافته است
- **پشتیبانی از دو endpoint** - با هر دو `v1/images/generations` و `v1/images/edits` کار می‌کند

**قیمت‌گذاری:** ورودی متن $5.00/۱ میلیون توکن، کش شده $1.25/۱ میلیون، خروجی متن $10.00/۱ میلیون، ورودی تصویر $8.00/۱ میلیون، ورودی تصویر کش شده $2.00/۱ میلیون، خروجی تصویر $30.00/۱ میلیون.

### GPT Image 1.5
مدل پیشرفته قبلی OpenAI برای تولید و ویرایش تصویر:
- **پایبندی بهبود یافته به prompt** - درک و اجرای بهتر پرامپت‌های دقیق
- **کیفیت بصری بهتر** - خروجی‌های با وفاداری بالاتر و واقع‌گرایانه‌تر
- **رندر متن بهتر** - توانایی بهبود یافته برای رندر دقیق متن در تصاویر
- **پشتیبانی از تولید و ویرایش** - با هر دو endpoint `v1/images/generations` و `v1/images/edits` کار می‌کند

**قیمت‌گذاری:** ورودی متن $5.00/1 میلیون توکن، کش شده $2.00/1 میلیون، خروجی متن $32.00/1 میلیون، ورودی تصویر $8.00/1 میلیون، خروجی تصویر $32.00/1 میلیون.

### GPT Image 1
مدل پرچمدار شناخته‌شده تولید تصویر که کیفیت خروجی بالا را با قابلیت‌های پیشرفته پیروی از دستورالعمل ارائه می‌دهد.

### GPT Image 1 Mini
یک نسخه مقرون به صرفه از GPT Image 1 که تولید تصویر سریع‌تر و مقرون به صرفه‌تر را با حفظ کیفیت بالای خروجی فراهم می‌کند. برای برنامه‌های با حجم بالا و نمونه‌سازی اولیه کامل است. **برای کاربران سطح 3، 4 و 5 در دسترس است.**

> این راهنما با اقتباس از [OpenAI Cookbook](https://developers.openai.com/cookbook/) رسمی و [مخزن GitHub رسمی OpenAI Cookbook](https://github.com/openai/openai-cookbook)، به‌ویژه راهنمای prompting مدل‌های GPT Image، و با تغییرات endpoint و کلید API برای AvalAI تهیه شده است.

## ویژگی‌های کلیدی

- **پیروی پیشرفته از دستورالعمل‌ها** - با دستورات متنی دقیق، دقیقا آنچه می‌خواهید را ایجاد کنید
- **کیفیت واقع‌گرایانه** - تولید تصاویر با کیفیت بالا و جزئیات چشمگیر
- **شخصی‌سازی انعطاف پذیر** - تنظیم کیفیت، اندازه، فشرده‌سازی و شفافیت
- **ویرایش تصویر** - اصلاح تصاویر موجود یا ترکیب چندین تصویر
- **پشتیبانی از ماسک** - ویرایش بخش‌های خاصی از تصاویر در حین حفظ سایر قسمت‌ها
- **مسیر ابزار Responses** - وقتی route شما در AvalAI پشتیبانی کند، ابزار میزبانی‌شده `image_generation` را داخل `/v1/responses` برای تجربه‌های مکالمه‌ای و ویرایش چندمرحله‌ای فراخوانی کنید

## Playbook پرامپت‌نویسی برای production

گردش‌کارهای قابل اعتماد GPT Image معمولا از پرامپت‌هایی استفاده می‌کنند که شبیه brief کوتاه محصول یا خلاقه هستند. پرامپت را ساختاریافته بنویسید، کاربرد تصویر را مشخص کنید و جدا کنید چه چیزی باید تغییر کند و چه چیزهایی باید ثابت بمانند.

### قالب عمومی

```text
Goal: <این تصویر برای چه استفاده می‌شود>
Format: <photo, ad, slide, UI mockup, diagram, product shot>
Canvas: <اندازه، نسبت تصویر، جهت>
Subject: <موضوع اصلی، محصول، شخص یا interface>
Composition: <کادربندی، زاویه، جای‌گذاری، فضای خالی>
Style: <photorealistic, flat vector, editorial, 3D render, ...>
Text: "<متن دقیق داخل تصویر>", جای‌گذاری، تایپوگرافی، زبان
Constraints: no watermark, no extra text, preserve brand colors, keep layout clean
```

### متن داخل تصویر

متن دقیق را داخل کوتیشن بگذارید و جایگاه و hierarchy آن را مشخص کنید. برای labelهای کوچک، infographicهای شلوغ یا متن چندزبانه، از `quality="high"` شروع کنید.

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt=(
        "Goal: product launch slide. Format: clean 16:9 presentation slide. "
        "Canvas: 1536x1024. Subject: a modern analytics dashboard screenshot mockup. "
        'Text: headline exactly "Revenue Signals", subtitle exactly "Weekly pipeline health". '
        "Composition: headline top-left, dashboard centered, three metric callouts on the right. "
        "Style: polished SaaS product visual, crisp typography, restrained colors. "
        "Constraints: no extra words, no watermark, readable text."
    ),
    size="1536x1024",
    quality="high",
)
```

### بومی‌سازی تصویر

برای ترجمه یک design موجود، از مدل بخواهید layout را حفظ کند و فقط متن را جایگزین کند. این الگو برای تبلیغات، screenshotهای UI، packaging و infographic مفید است.

```text
Translate all visible English text into Persian.
Preserve the original layout, typography hierarchy, colors, icons, logo placement,
spacing, arrows, and image content. Do not add new claims or extra text.
```

### ویرایش دقیق

در ویرایش، تغییر موردنظر و invariantها را واضح بنویسید. این کار drift را در iterationهای بعدی کمتر می‌کند.

```text
Change only the chair color to matte black.
Keep the camera angle, room layout, lighting, shadows, wall color, floor texture,
table position, and all other objects exactly the same.
```

### ترکیب چند تصویر

به هر تصویر ورودی با شماره و نقش آن اشاره کنید.

```text
Image 1 is the product photo. Image 2 is the lifestyle background.
Place the product from Image 1 on the table in Image 2.
Match perspective, contact shadow, color temperature, and scale.
Preserve the product label exactly.
```

## تولید پایه تصویر

برای تولید یک تصویر با مدل‌های GPT Image، باید یک دستور متنی ارائه دهید که آنچه می‌خواهید ایجاد کنید را توصیف می‌کند. هرچه دستور شما دقیق‌تر باشد، نتایج بهتر خواهد بود. می‌توانید از [`gpt-image-2`](fa/providers/openai.md) برای تازه‌ترین و بهترین قابلیت‌ها، [`gpt-image-1.5`](fa/providers/openai.md) برای مدل پیشرفته قبلی، [`gpt-image-1`](fa/providers/openai.md) برای کیفیت بالا، یا [`gpt-image-1-mini`](fa/providers/openai.md) برای تولید مقرون به صرفه استفاده کنید.

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.images.generate(
    model="gpt-image-2",  # یا "gpt-image-1.5"، "gpt-image-1"، "gpt-image-1-mini"
    prompt="یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند",
    size="1024x1024",
    quality="medium",
)

image_base64 = response.data[0].b64_json
with open("mountain-lake.png", "wb") as image_file:
    image_file.write(base64.b64decode(image_base64))

```

```javascript
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "gpt-image-2", // یا "gpt-image-1.5"، "gpt-image-1"، "gpt-image-1-mini"
  prompt:
    "یک تصویر واقع‌گرایانه از منظره کوهستانی با دریاچه‌ای که غروب آفتاب را منعکس می‌کند",
  size: "1024x1024",
  quality: "medium",
});

const imageBase64 = response.data[0].b64_json;
fs.writeFileSync("mountain-lake.png", Buffer.from(imageBase64, "base64"));

```


## ابزار تصویر در Responses (وابسته به route)

برای کارهای تک‌مرحله‌ای تصویر، `/v1/images/generations` را پیش‌فرض نگه دارید. وقتی مدل و حساب AvalAI شما صریحا از ابزار میزبانی‌شده `image_generation` پشتیبانی می‌کند و تصویر بخشی از مکالمه، agent flow یا ویرایش چندنوبتی است، از `/v1/responses` استفاده کنید.

در فیلد `model` از یک مدل متنی سازگار با Responses استفاده کنید و رفتار تصویر را داخل تنظیمات tool بگذارید. `action: "generate"` تولید تصویر جدید را اجباری می‌کند، `action: "edit"` را فقط وقتی استفاده کنید که تصویر ورودی در context وجود دارد، و `action: "auto"` اجازه می‌دهد مدل تصمیم بگیرد. اگر روی routeهای پشتیبانی‌شده باید حتما فراخوانی تصویر انجام شود، `tool_choice: { type: "image_generation" }` را اضافه کنید؛ در غیر این صورت مدل می‌تواند پاسخ متنی بدهد.

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Draw a clean product hero image of a matte black smart speaker on a walnut desk.",
    tools=[
        {
            "type": "image_generation",
            "action": "generate",
            "size": "1024x1024",
            "quality": "medium",
        }
    ],
)

image_calls = [item for item in response.output if item.type == "image_generation_call"]

if not image_calls:
    raise RuntimeError("No image was generated; use /v1/images/generations instead.")

with open("responses-product-hero.png", "wb") as image_file:
    image_file.write(base64.b64decode(image_calls[0].result))

print("Revised prompt:", getattr(image_calls[0], "revised_prompt", None))

```

```javascript
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input:
    "Draw a clean product hero image of a matte black smart speaker on a walnut desk.",
  tools: [
    {
      type: "image_generation",
      action: "generate",
      size: "1024x1024",
      quality: "medium",
    },
  ],
});

const imageCall = response.output.find(
  (item) => item.type === "image_generation_call"
);

if (!imageCall) {
  throw new Error("No image was generated; use /v1/images/generations instead.");
}

fs.writeFileSync(
  "responses-product-hero.png",
  Buffer.from(imageCall.result, "base64")
);

console.log("Revised prompt:", imageCall.revised_prompt);

```


## شخصی‌سازی گزینه‌های خروجی

مدل‌های GPT Image چندین گزینه برای شخصی‌سازی تصاویر تولید شده ارائه می‌دهند:

### اندازه تصویر

می‌توانید اندازه تصویر تولید شده را با استفاده از پارامتر `size` مشخص کنید:

- `1024x1024` (مربع)
- `1024x1536` (عمودی)
- `1536x1024` (افقی)
- `auto` (پیش‌فرض)

`gpt-image-2` از اندازه‌های سفارشی انعطاف‌پذیر هم پشتیبانی می‌کند، به شرطی که ابعاد معتبر باشند و نسبت تصویر بیش از حد کشیده نباشد. برای اطمینان production، ابتدا از `1024x1024`، `1024x1536`، `1536x1024` یا `2560x1440` شروع کنید و سپس خروجی‌های بزرگ‌تر را تست کنید.

برای اندازه‌های سفارشی `gpt-image-2`، قبل از ارسال درخواست این چک‌لیست را بررسی کنید:

- بلندترین ضلع `3840px` یا کمتر باشد.
- هر دو بعد مضرب `16px` باشند.
- نسبت ضلع بلند به ضلع کوتاه بیشتر از `3:1` نباشد.
- مجموع پیکسل‌ها بین `655,360` و `8,294,400` باشد.
- خروجی‌های بزرگ‌تر از `2560x1440` از نظر latency، هزینه و ثبات بصری روی route AvalAI شما تست شده باشند.

```python
# استفاده از GPT Image 2 برای خروجی افقی با کیفیت بالا
response = client.images.generate(
    model="gpt-image-2",
    prompt="یک پرتره با سبک پیکسل آرت از یک گربه با عینک آفتابی",
    size="1536x1024",  # جهت افقی
)

# استفاده از GPT Image 1 Mini برای تولید مقرون به صرفه
response = client.images.generate(
    model="gpt-image-1-mini",
    prompt="یک پرتره با سبک پیکسل آرت از یک گربه با عینک آفتابی",
    size="1024x1536",  # جهت عمودی
    quality="high",  # مشخص کردن سطح کیفیت
)
```

### کیفیت تصویر

کیفیت تصویر تولید شده را با استفاده از پارامتر `quality` کنترل کنید:

- `low` - تولید سریع‌تر اما کیفیت پایین‌تر
- `medium` - تعادل بین کیفیت و سرعت
- `high` - بالاترین کیفیت اما تولید کندتر
- `auto` (پیش‌فرض)

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="یک تصویر با جزئیات از یک قلعه فانتزی",
    quality="high",  # بالاترین کیفیت
)
```

### فرمت خروجی و فشرده‌سازی

می‌توانید فرمت خروجی و سطح فشرده‌سازی را مشخص کنید:

```python
response = client.images.generate(
    model="gpt-image-2",
    prompt="یک طراحی لوگوی مینیمالیستی با اشکال هندسی",
    output_format="jpeg",
    output_compression=75,  # سطح فشرده‌سازی (0-100)
)
```

### پس‌زمینه شفاف

پس‌زمینه شفاف به مدل و route انتخابی وابسته است. راهنمای فعلی OpenAI برای `gpt-image-2` مقدار `background="transparent"` را پشتیبانی‌شده نمی‌داند؛ بنابراین تا وقتی route AvalAI شما پشتیبانی شفافیت را برای مدل انتخابی تأیید نکرده، `background="auto"` یا `background="opaque"` را نگه دارید. اگر مدل انتخابی شفافیت را پشتیبانی کند، از فرمتی با کانال alpha مانند `png` یا `webp` استفاده کنید.

```python
response = client.images.generate(
    model="gpt-image-1",
    prompt="A 3D rendered icon of a rocket, isolated with no visible background",
    output_format="png",
    background="transparent",
)
```

## ویرایش تصاویر

مدل‌های GPT Image می‌توانند تصاویر موجود را بر اساس دستورالعمل‌های متنی اصلاح کنند. برای ویرایش‌های production که هویت، labelها، layout یا fidelity مهم است، `gpt-image-2` را ترجیح دهید.

برای فراخوانی مستقیم HTTP REST API، اندپوینت ویرایش `https://api.avalai.ir/v1/images/edits` است.

برای `gpt-image-2`، پارامتر `input_fidelity` را ارسال نکنید؛ راهنمای فعلی OpenAI می‌گوید این مدل ورودی‌های تصویری را به‌صورت خودکار با fidelity بالا پردازش می‌کند. در routeهای قدیمی‌تر که `input_fidelity` را ارائه می‌کنند، برای چهره‌ها، لوگوها، بسته‌بندی، screenshotهای UI یا ویرایش‌هایی که حفظ جزئیات متمایز مهم است از `high` استفاده کنید.

### ویرایش پایه تصویر

```python
# باز کردن یک تصویر موجود - استفاده از GPT Image 2
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-2",
        image=image_file,
        prompt=(
            "Change only the background to a tropical beach. "
            "Keep the person, pose, clothing, lighting direction, and camera angle the same."
        ),
    )

edited_image_base64 = response.data[0].b64_json

# استفاده از GPT Image 1 Mini برای ویرایش مقرون به صرفه
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-1-mini",
        image=image_file,
        prompt="تغییر پس‌زمینه به یک ساحل گرمسیری",
    )
```

### ترکیب چندین تصویر

می‌توانید تا 10 تصویر ورودی برای ترکیب یا مرجع ارائه دهید:

```python
with open("image1.jpg", "rb") as img1, open("image2.jpg", "rb") as img2:
    response = client.images.edit(
        model="gpt-image-2",
        image=[img1, img2],
        prompt=(
            "Image 1 is the person. Image 2 is the setting. "
            "Place the person from Image 1 naturally into Image 2. "
            "Match perspective, lighting, scale, and shadows."
        ),
    )
```

## استفاده از ماسک برای ویرایش دقیق

برای کنترل دقیق‌تر روی بخش‌هایی از تصویر که اصلاح می‌شوند، می‌توانید یک ماسک با کانال آلفا ارائه دهید:

```python
with open("input_image.jpg", "rb") as image_file, open("mask.png", "rb") as mask_file:
    response = client.images.edit(
        model="gpt-image-2",
        image=image_file,
        mask=mask_file,
        prompt="اضافه کردن گل‌های رنگارنگ به منطقه ماسک شده",
    )
```

## تصویرهای جزئی در Streaming (وابسته به route)

اگر route انتخابی AvalAI از streaming تصویر پشتیبانی کند، با `partial_images` می‌توانید هنگام رندر شدن خروجی نهایی preview تدریجی نشان دهید. تصویرهای جزئی را فقط preview بدانید؛ asset نهایی را از پاسخ کامل ذخیره کنید.

```python
import base64

stream = client.images.generate(
    model="gpt-image-2",
    prompt="A cinematic river made of white owl feathers in a quiet winter forest",
    stream=True,
    partial_images=2,
)

for event in stream:
    if event.type == "image_generation.partial_image":
        with open(f"river-partial-{event.partial_image_index}.png", "wb") as file:
            file.write(base64.b64decode(event.b64_json))
```

### ایجاد ماسک با کانال آلفا

اگر نیاز به ایجاد یک ماسک با کانال آلفا از یک تصویر سیاه و سفید دارید:

```python
from PIL import Image
from io import BytesIO

# بارگذاری ماسک سیاه و سفید به عنوان تصویر خاکستری
mask = Image.open("bw_mask.png").convert("L")

# تبدیل به RGBA و استفاده از خود ماسک برای کانال آلفا
mask_rgba = mask.convert("RGBA")
mask_rgba.putalpha(mask)

# ذخیره ماسک با کانال آلفا
mask_rgba.save("mask_with_alpha.png", "PNG")
```

## محاسبه هزینه GPT Image 2 برای ویرایش تصویر

وقتی تصاویر را با `gpt-image-2` از طریق `v1/images/edits` ویرایش می‌کنید، صورتحساب کاملا مبتنی بر توکن است. هیچ هزینه ثابتی برای هر ویرایش وجود ندارد: شما برای توکن‌های متن پرامپت، توکن‌های تصویر هر تصویر مرجعی که آپلود می‌کنید و توکن‌های تصویر خروجی که مدل برمی‌گرداند پرداخت می‌کنید. مقادیر `quality` و `size` که درخواست می‌دهید توکن‌های تصویر خروجی را تعیین می‌کنند که معمولا بیشترین سهم را در هزینه ویرایش دارند.

### هزینه‌های تقریبی هر تصویر بر اساس کیفیت و رزولوشن

GPT Image 2 از صورتحساب کاملا مبتنی بر توکن استفاده می‌کند. ارقام زیر تخمین‌های ماشین‌حساب از ابزار محاسبه هزینه تولید تصویر OpenAI هستند، نه نرخ‌های ثابت. هزینه واقعی بسته به پیچیدگی پرامپت، اندازه تصویر و اینکه آیا تصاویر مرجع شامل شده‌اند متفاوت است.

**کیفیت پایین (تقریبی):**

| رزولوشن | هزینه تقریبی هر تصویر |
| ------------------------ | ---------------------- |
| 1024x1024 (مربع)         | ~$0.008 |
| 1024x1536 (عمودی)        | ~$0.012 |
| 1536x1024 (افقی)         | ~$0.012 |

**کیفیت متوسط (تقریبی):**

| رزولوشن | هزینه تقریبی هر تصویر |
| ------------------------ | ---------------------- |
| 1024x1024 (مربع)         | ~$0.032 |
| 1024x1536 (عمودی)        | ~$0.048 |
| 1536x1024 (افقی)         | ~$0.048 |

**کیفیت بالا (تقریبی):**

| رزولوشن | هزینه تقریبی هر تصویر |
| ------------------------ | ---------------------- |
| 1024x1024 (مربع)         | ~$0.125 |
| 1024x1536 (عمودی)        | ~$0.187 |
| 1536x1024 (افقی)         | ~$0.187 |

این تخمین‌ها فقط توکن‌های تصویر خروجی را پوشش می‌دهند که با نرخ خروجی تصویر GPT Image 2 معادل $30.00 / ۱ میلیون توکن محاسبه می‌شوند. ویرایش‌ها هزینه توکن‌های متن پرامپت شما ($5.00 / ۱ میلیون) و توکن‌های ورودی تصویر برای هر تصویر مرجعی که آپلود می‌کنید ($8.00 / ۱ میلیون، یا $2.00 / ۱ میلیون در حالت کش شده) را نیز اضافه می‌کنند. همیشه برای تخمین دقیق هزینه، از ماشین‌حساب رسمی تولید تصویر OpenAI با پرامپت و تنظیمات خاص خود استفاده کنید.

### هر تنظیم کیفیت دقیقا چه چیزی تولید می‌کند

تنظیمات کیفیت صرفا یک درجه‌بندی بین بدتر و بهتر نیستند. هر سطح برای موارد استفاده مشخصی مناسب است و انتخاب سطح درست تاثیر مستقیمی بر هزینه‌های ماهانه دارد:

- **کیفیت پایین:** تولید سریع‌تر با کمترین هزینه. برای پیش‌نویس‌ها، دارایی‌های دیجیتال کوچک و pipelineهای خودکار که کنترل هزینه از جزئیات ظریف مهم‌تر است مناسب است.
- **کیفیت متوسط:** برای بیشتر تولیدات بازاریابی و محتوا مناسب است: تصاویر شبکه‌های اجتماعی، گرافیک‌های تحریریه، mockup محصول و دارایی‌های کمپین. در اکثر زمینه‌ها برای انتشار حرفه‌ای کافی است.
- **کیفیت بالا:** برای دارایی‌های نهایی production طراحی شده که دقت در سطح پیکسل اهمیت دارد: عکاسی محصول شاخص، مواد چاپی با رزولوشن بالا، طراحی بسته‌بندی و mockupهای دقیق UI.

### نکات عملی کنترل هزینه برای ویرایش

- برای iteration و پاس‌های پیش‌نمایش از `quality="low"` استفاده کنید، سپس فقط ویرایش نهایی تاییدشده را با `quality="high"` مجددا اجرا کنید.
- تصاویر مرجع را در کوچک‌ترین رزولوشنی نگه دارید که همچنان جزئیاتی را که باید حفظ شوند نگه می‌دارد؛ هر تصویر آپلودشده توکن‌های ورودی تصویر اضافه می‌کند.
- در جایی که route شما پشتیبانی می‌کند، تصاویر مرجع تکراری را کش کنید تا ورودی تصویر از $8.00 / ۱ میلیون به $2.00 / ۱ میلیون منتقل شود.
- برای ویرایش‌هایی که به کادربندی عمودی یا افقی نیاز ندارند، خروجی `1024x1024` را ترجیح دهید، زیرا خروجی‌های مربع در هر سطح کیفیت کمترین توکن‌های تصویر خروجی را دارند.

## انتخاب مدل GPT Image

### از GPT Image 2 استفاده کنید وقتی:

- یک گردش‌کار جدید تصویر می‌سازید
- بهترین prompt adherence و fidelity بصری را می‌خواهید
- تصویر شامل متن خوانا، UI، label، logo یا infographic است
- ویرایش باید identity، layout، label محصول یا perspective دوربین را حفظ کند
- کاهش retry از کمترین هزینه واحدی مهم‌تر است

### از GPT Image 1.5 یا GPT Image 1 استفاده کنید وقتی:

- یک گردش‌کار قدیمی و validate شده دارید و مهاجرت کنترل‌شده می‌خواهید
- موقتا به backward compatibility نیاز دارید تا خروجی‌ها را مقایسه کنید

### از GPT Image 1 Mini استفاده کنید وقتی:

- به تولید تصویر مقرون به صرفه نیاز دارید
- با برنامه‌های با حجم بالا کار می‌کنید
- در حال نمونه‌سازی یا تکرار ایده‌ها هستید
- نیازهای کیفیتی بالا هستند اما به حداکثر مطلق نیاز ندارید

برای بیشتر کارهای production جدید، از `gpt-image-2` شروع کنید و برای draft سریع از `quality="low"`، برای استفاده عمومی از `quality="medium"` و برای assetهای نهایی، متنی یا حساس به جزئیات از `quality="high"` استفاده کنید.

## بهترین شیوه‌ها برای مدل‌های GPT Image

1. **در دستورات خود دقیق و جزئی باشید** - مدل به توضیحات دقیق، از جمله سبک، نورپردازی، ترکیب‌بندی و جزئیات موضوع به خوبی پاسخ می‌دهد.

2. **سبک مورد نظر را به صراحت مشخص کنید** - به عنوان مثال، "واقع‌گرایانه"، "نقاشی رنگ روغن"، "هنر دیجیتال"، "طراحی با مداد" و غیره.

3. **در صورت امکان از تصاویر مرجع استفاده کنید** - هنگام ویرایش یا تلاش برای دستیابی به یک سبک خاص، ارائه تصاویر مرجع می‌تواند به هدایت مدل کمک کند.

4. **با تنظیمات کیفیت آزمایش کنید** - بر اساس نیازهای خود برای سرعت در مقابل جزئیات، تنظیمات کیفیت مختلف را امتحان کنید.

5. **از ماسک و invariantها برای کنترل دقیق استفاده کنید** - وقتی فقط یک بخش از تصویر را تغییر می‌دهید، در صورت امکان mask بدهید و دقیق بنویسید چه چیزهایی نباید تغییر کنند.

6. **پرامپت بازنویسی‌شده را بررسی کنید** - وقتی `revised_prompt` وجود دارد، آن را ذخیره کنید تا تیم پشتیبانی بتواند بازنویسی prompt و خروجی‌های غیرمنتظره را debug کند.

7. **state تصویر را برای flowهای Responses نگه دارید** - قبل از follow-up، مسیر فایل ذخیره‌شده، file ID، مقدار `previous_response_id` یا شناسه `image_generation_call` را نگه دارید.

## محدودیت‌ها

- مدل ممکن است گاهی تصاویری تولید کند که دقیقا با دستور شما مطابقت ندارد
- صحنه‌های بسیار پیچیده با چندین عنصر ممکن است به طور کامل ارائه نشوند
- ارائه متن در تصاویر ممکن است ناسازگار یا نادرست باشد
- هنگام استفاده از ماسک‌ها، ممکن است برخی نشت‌ها فراتر از مرزهای ماسک رخ دهد
- پرامپت‌های پیچیده ممکن است از درخواست‌های متنی کندتر باشند؛ برای queue و loading state مناسب طراحی کنید
- پس‌زمینه شفاف به مدل وابسته است و در حال حاضر برای `gpt-image-2` پشتیبانی نمی‌شود
- برای iterationهای اولیه از `quality="low"` یا GPT Image 1 Mini استفاده کنید، سپس برای خروجی نهایی و حساس به متن یا fidelity از `gpt-image-2` با `quality="high"` استفاده کنید

## نتیجه‌گیری

مدل‌های GPT Image ابزارهای قدرتمندی برای تولید و ویرایش تصویر با پرامپت متنی ساده هستند. برای گردش‌کارهای جدید AvalAI، `gpt-image-2` بهترین پیش‌فرض است: پرامپت‌های دقیق را بهتر دنبال می‌کند، برای briefهای بصری production مناسب‌تر است و در متن، layout، mockup محصول و ویرایش دقیق عملکرد قوی‌تری دارد.

برای اطلاعات بیشتر در مورد تولید تصویر با AvalAI، لطفا به [راهنمای تولید تصویر](fa/guides/image-generation.md) ما مراجعه کنید.
