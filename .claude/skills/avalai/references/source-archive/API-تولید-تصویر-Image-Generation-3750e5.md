---
hasH1: true
---

# API تولید تصویر (Image Generation)

API تولید تصویر به شما امکان می‌دهد با استفاده از مدل‌های هوش مصنوعی از ارائه‌دهندگان مختلف از طریق پلتفرم AvalAI، تصاویر را ایجاد و ویرایش کنید.

برای گردش‌کارهای مکالمه‌ای یا چندمرحله‌ای تصویر، AvalAI می‌تواند ابزارهای تولید تصویر سبک OpenAI در Responses را هم ارائه کند، اگر مدل و route انتخابی از آن پشتیبانی کنند. endpointهای این صفحه را مسیر مستقیم و قابل‌حمل در نظر بگیرید و قبل از انتقال flow تصویر به `/v1/responses`، [مسیر مهاجرت تصویر](fa/guides/image-generation.md#مسیر-مهاجرت-ابزار-تصویر-در-responses) را ببینید.

## تازه‌ترین مدل‌های تصویر OpenAI

برای تولید و ویرایش سریع‌تر، `gpt-image-2.5-flare` را به‌عنوان انتخاب پیش‌فرض عمومی به کار ببرید. برای ویرایش دقیق‌تر تصاویر حرفه‌ای محصول و طرح‌های تبلیغاتی، با پذیرش زمان تولید طولانی‌تر، `gpt-image-2.5-sunburst` را انتخاب کنید. هر دو از `/v1/images/generations` و `/v1/images/edits` پشتیبانی می‌کنند.

به گفته OpenAI، نورپردازی، بافت‌ها، حفظ سوژه مرجع، ویرایش هدفمند و ثبات در ویرایش‌های چندمرحله‌ای بهبود یافته‌اند. این ارائه‌دهنده از کاهش زمان تولید Flare تا ۵۰٪ نسبت به GPT Image 2 خبر می‌دهد؛ این ادعا تضمین زمان پاسخ در AvalAI نیست. برای ویرایش‌های پیاپی، هر خروجی را ذخیره کنید و در درخواست بعدی به‌عنوان تصویر منبع بفرستید؛ در هر مرحله مشخص کنید چه چیزهایی باید بدون تغییر بمانند.

هیچ‌یک از این دو شناسه تصویر را در فیلد `model` مسیر `/v1/responses` قرار ندهید. ابزارهای میزبانی‌شده تصویر در Responses به یک مدل متنی با پشتیبانی جداگانه نیاز دارند. Sketch و قالب‌های آماده ChatGPT جزو قابلیت‌های API در AvalAI نیستند. [خبر معرفی مدل‌ها](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md) را ببینید.

### GPT-6 Sol، GPT-6 Luna و Grok 4.7

مدل‌های `gpt-6-sol` و `gpt-6-luna` از OpenAI و `grok-4.7` از xAI از درک تصویر و استدلال پشتیبانی می‌کنند، اما **مدل تولید تصویر نیستند**. این شناسه‌ها را به‌عنوان مدل تصویر به `v1/images/generations` یا `v1/images/edits` نفرستید. برای تولید و ویرایش مستقیم، مدل‌های اختصاصی مانند `gpt-image-2.5-flare` یا `gpt-image-2.5-sunburst` را به کار ببرید.

Sol و Luna در `v1/chat/completions`، `v1/messages` و `v1/responses` پشتیبانی کامل دارند. پشتیبانی Grok 4.7 در Chat Completions و Messages کامل و در `v1/responses` **جزئی** است. هیچ‌یک از این اعلام‌های پشتیبانی نقطه پایانی به‌تنهایی دسترسی به ابزار میزبانی‌شده `image_generation` را تأیید نمی‌کند؛ مدل، مسیر و حساب انتخابی را جداگانه بررسی کنید. پشتیبانی جزئی Grok به معنی برابری کامل ابزارهای میزبانی‌شده یا گردش‌کارهای دارای وضعیت ذخیره‌شده نیست.

برای گردش‌کاری قابل انتقال، از مدل استدلالی بخواهید تصویر مرجع را تحلیل کند یا شرح متنی آماده کند؛ سپس برنامه شما API اختصاصی تصویر را با یک مدل تصویر فراخوانی کند. [خبر مدل‌های جدید](fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added.md) و [راهنمای تولید تصویر](fa/guides/image-generation.md) را ببینید.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/images/generations
```

## بدنه درخواست (Request Body)

| پارامتر           | نوع     | الزامی | توضیحات                                                                                                      |
| ----------------- | ------- | ------ | ------------------------------------------------------------------------------------------------------------ |
| `model`           | string  | بله    | شناسه مدل انتخابی، مانند `gpt-image-2.5-flare` یا `gpt-image-2.5-sunburst`. |
| `prompt`          | string  | بله    | توصیف متنی تصویر یا تصاویر مورد نظر. در مدل‌های GPT Image، وقتی چیدمان، متن یا دقت ویرایش مهم است، شرح ساختاریافته‌ای از نتیجه دلخواه بنویسید. |
| `n`               | integer | خیر    | تعداد تصاویری که باید تولید شود. پیش‌فرض ۱ است.                                                              |
| `size`            | string  | خیر    | اندازه تصاویر تولید شده. اندازه‌های رایج OpenAI شامل `1024x1024`، `1024x1536` و `1536x1024` است؛ `gpt-image-2` از اندازه‌های سفارشی معتبر هم پشتیبانی می‌کند. |
| `quality`         | string  | خیر    | تنظیم کیفیت وابسته به مدل. مدل‌های GPT Image در صورت پشتیبانی از `low`، `medium`، `high` یا `auto` استفاده می‌کنند. فقط GPT Image 2.5 Flare و Sunburst دو گزینه اضافی `xhigh` و `max` را نیز می‌پذیرند؛ این مقادیر را به مدل‌های قدیمی نفرستید. |
| `style`           | string  | خیر    | تنظیم سبک وابسته به مدل. برخی مدل‌های قدیمی تصویر مقدارهایی مثل `vivid` یا `natural` را پشتیبانی می‌کنند. |
| `response_format` | string  | خیر    | مدل‌های قدیمی تصویر ممکن است `url` یا `b64_json` را پشتیبانی کنند. مدل‌های GPT Image داده Base64 برمی‌گردانند؛ مقدار `data[0].b64_json` را decode و ذخیره کنید. |
| `output_format`   | string  | خیر    | فرمت فایل خروجی GPT Image در صورت پشتیبانی route: `png`، `jpeg` یا `webp`. |
| `output_compression` | integer | خیر | سطح فشرده‌سازی برای خروجی JPEG/WebP در صورت پشتیبانی. |
| `background`      | string  | خیر    | نحوه پس‌زمینه در صورت پشتیبانی. تا وقتی مدل انتخابی خروجی شفاف را تأیید نکرده، `auto` یا `opaque` را نگه دارید. |
| `moderation`      | string  | خیر    | سطح moderation برای GPT Image در صورت ارائه route. برای production مقدار `auto` را نگه دارید؛ `low` فقط پس از review ایمنی استفاده شود. |
| `stream`          | boolean | خیر    | در صورت پشتیبانی route، تولید تصویر را به‌صورت streaming فعال می‌کند. |
| `partial_images`  | integer | خیر    | تعداد تصویرهای preview جزئی هنگام streaming، در صورت پشتیبانی route. routeهای سبک GPT Image معمولا مقدار `0` تا `3` را می‌پذیرند. |
| `user`            | string  | خیر    | یک شناسه منحصر به فرد که نماینده کاربر نهایی شما است و می‌تواند به نظارت و شناسایی سو استفاده کمک کند.       |

### نکته‌های خروجی، streaming و هزینه

- routeهای سبک GPT Image داده تصویر را در `data[0].b64_json` به‌صورت Base64 برمی‌گردانند؛ آن را decode و bytes را ذخیره کنید. routeهای قدیمی یا provider-specific ممکن است وقتی `response_format: "url"` را پشتیبانی کنند URL برگردانند.
- usage تولید تصویر می‌تواند شامل `input_tokens`، `output_tokens` و جزئیات image token باشد. اندازه، کیفیت، تصویرهای ورودی و previewهای جزئی روی هزینه و latency اثر می‌گذارند؛ پیش از workflowهای حجیم یا high-resolution قیمت‌گذاری AvalAI را بررسی کنید.
- streaming تولید تصویر در routeهای پشتیبانی‌شده Image API eventهایی مثل `image_generation.partial_image` و event نهایی `image_generation.completed` برمی‌گرداند. `partial_images` تعداد previewهای درخواستی را کنترل می‌کند، اما اگر تصویر نهایی سریع آماده شود ممکن است previewهای کمتری دریافت کنید.
- برای `gpt-image-2` مقدار `background` را `auto` یا `opaque` نگه دارید؛ background شفاف پشتیبانی نمی‌شود مگر اینکه route انتخابی AvalAI صریحا آن را مستند کرده باشد.
- وقتی حجم فایل و latency مهم است از `jpeg` یا `webp` همراه `output_compression` استفاده کنید. وقتی خروجی lossless یا alpha لازم دارید و مدل شفافیت را پشتیبانی می‌کند از `png` استفاده کنید.

## مثال‌ها

### تولید تصویر پایه

برای الگوهای پرامپت production، متن داخل تصویر، بومی‌سازی، compositing و ویرایش دقیق، [ساخت تصویر با GPT Image](fa/examples/generate_images_with_gpt_image.md) را ببینید. آن راهنما محتوای رسمی OpenAI Cookbook برای GPT Image را برای AvalAI تطبیق می‌دهد.

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-image-2.5-flare",
  "prompt": "A cute baby sea otter floating on its back in the ocean",
  "n": 1,
  "size": "1024x1024",
  "quality": "medium"
}' | jq -r '.data[0].b64_json' | base64 --decode >sea-otter.png

python=:# مثال پایتون (Python)
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.images.generate(
    model="gpt-image-2.5-flare",
    prompt="A cute baby sea otter floating on its back in the ocean",
    n=1,
    size="1024x1024",
    quality="medium",
)

image_base64 = response.data[0].b64_json
with open("sea-otter.png", "wb") as image_file:
    image_file.write(base64.b64decode(image_base64))

javascript=:// مثال جاوااسکریپت (JavaScript)
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "gpt-image-2.5-flare",
  prompt: "A cute baby sea otter floating on its back in the ocean",
  n: 1,
  size: "1024x1024",
  quality: "medium",
});

const imageBase64 = response.data[0].b64_json;
fs.writeFileSync("sea-otter.png", Buffer.from(imageBase64, "base64"));

```

### مثال ابزار تصویر در Responses

فقط وقتی مدل و حساب AvalAI انتخابی شما از ابزار میزبانی‌شده `image_generation` پشتیبانی می‌کند از `/v1/responses` استفاده کنید. برای تولید و ویرایش تک‌مرحله‌ای، Image API مستقیم بالا مسیر قابل‌حمل‌تر است.

```language-selector
python=:import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="Generate a friendly mascot for an API documentation site.",
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

if image_calls:
    with open("docs-mascot.png", "wb") as image_file:
        image_file.write(base64.b64decode(image_calls[0].result))

javascript=:import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "Generate a friendly mascot for an API documentation site.",
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

if (imageCall) {
  fs.writeFileSync("docs-mascot.png", Buffer.from(imageCall.result, "base64"));
}

```

#### گزینه‌های ابزار Responses

| پارامتر | نوع | توضیحات |
| ------- | --- | ------- |
| `type` | string | باید `image_generation` باشد. |
| `action` | string | اختیاری. `auto` اجازه می‌دهد مدل انتخاب کند؛ `generate` تولید تصویر جدید را اجباری می‌کند؛ `edit` وقتی تصویر در context است ویرایش را اجباری می‌کند. |
| `size` | string | ابعاد تصویر، مثل `1024x1024`، `1024x1536`، `1536x1024` یا اندازه دیگری که route پشتیبانی کند. |
| `quality` | string | کیفیت رندر، معمولا `low`، `medium`، `high` یا `auto` در صورت پشتیبانی. |
| `output_format` | string | فرمت خروجی در صورت پشتیبانی: `png`، `jpeg` یا `webp`. |
| `output_compression` | integer | سطح فشرده‌سازی برای خروجی JPEG/WebP در صورت پشتیبانی. |
| `background` | string | تا وقتی مدل انتخابی خروجی transparent را تأیید نکرده، `auto` یا `opaque` را استفاده کنید. |
| `partial_images` | integer | تعداد previewهای تدریجی هنگام streaming، معمولا `0` تا `3` در صورت پشتیبانی. |
| `input_image_mask` | object | شی mask برای ویرایش تصویر در Responses، معمولا file ID، در صورت پشتیبانی. |

## پارامترهای اختصاصی ارائه‌دهنده (Provider-Specific Parameters)

هنگام استفاده از مدل‌های تولید یا ویرایش تصویر غیر OpenAI (مانند Black Forest Labs، Alibaba، BytePlus یا مدل‌های Google)، ممکن است نیاز به ارسال پارامترهای اختصاصی ارائه‌دهنده داشته باشید که مستقیما توسط SDK OpenAI پشتیبانی نمی‌شوند. از پارامتر [`extra_body`](fa/guides/provider-specific-params.md) برای ارسال این پارامترهای اضافی استفاده کنید.

### استفاده از extra_body برای پارامترهای اختصاصی ارائه‌دهنده

سیستم به طور خودکار پارامترهای اختصاصی ارائه‌دهنده را به ارائه‌دهنده مناسب نگاشت می‌کند زیرا اینها پارامترهای استاندارد OpenAI نیستند.

#### پارامترهای اختصاصی ارائه‌دهنده رایج

در اینجا چند نمونه از پارامترهای اختصاصی ارائه‌دهنده برای مدل‌های تصویری پشتیبانی‌شده مثل **Black Forest Labs (BFL)**، **Alibaba**، **BytePlus** و **Google** آورده شده است:

- `output_format` - تعیین فرمت خروجی برای تصویر تولید شده
- `aspect_ratio` - کنترل نسبت ابعاد تصاویر تولید شده
- `prompt_upsampling` - فعال یا غیرفعال کردن بهبود پرامپت
- `safety_tolerance` - تنظیم فیلتر ایمنی محتوا
- `samples` - تعداد نمونه‌های تولیدی
- `extras` - گزینه‌های اضافی مخصوص مدل
- `image_strength` - کنترل قدرت تولید تصویر به تصویر
- `init_image_mode` - تنظیم حالت مقداردهی اولیه برای ویرایش تصویر
- `init_image` - ارائه تصویر اولیه برای ویرایش

### مثال با پارامترهای اختصاصی ارائه‌دهنده

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# استفاده از مدل Black Forest Labs با پارامترهای اختصاصی ارائه‌دهنده
response = client.images.generate(
    model="flux-1.1-pro",
    prompt="اژدهای باشکوهی که در میان ابرها پرواز می‌کند",
    size="1024x1024",
    extra_body={
        "aspect_ratio": "16:9",
        "output_format": "png",
        "safety_tolerance": 2,
        "prompt_upsampling": True,
    },
    response_format="b64_json",  # not supporting 'url'
)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// استفاده از مدل Black Forest Labs با پارامترهای اختصاصی ارائه‌دهنده
const response = await client.images.generate({
 model: "flux-1.1-pro",
 prompt: "اژدهای باشکوهی که در میان ابرها پرواز می‌کند",
 size: "1024x1024",
 // @ts-expect-error extra_body is a provider-specific parameter
 extra_body: {
 aspect_ratio: "16:9",
 output_format: "png",
 safety_tolerance: 2,
 prompt_upsampling: true
 },
 response_format: "b64_json", // not supporting 'url'
});

```

### مدل‌های تصویر Alibaba Qwen

مدل‌های تصویر Qwen از هم فرمت OpenAI SDK و هم فرمت بومی Alibaba Dashscope پشتیبانی می‌کنند و حداکثر انعطاف‌پذیری را برای توسعه‌دهندگان فراهم می‌کنند.

```language-selector
python=:import os
from openai import OpenAI
import requests

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# تولید متن-به-تصویر با استفاده از فرمت OpenAI SDK
response = client.images.generate(
    model="qwen-image",
    prompt="منظره آرام کوهستانی با دریاچه شفاف که قله‌های برفی را منعکس می‌کند",
    size="1328x1328",
    n=1,
    response_format="url",  # or b64_json
)

print(f"URL تصویر تولید شده: {response.data[0].url}")

# ویرایش تصویر با استفاده از فرمت OpenAI SDK
with open("input_image.jpg", "rb") as image_file:
    edit_response = requests.post(
        "https://api.avalai.ir/v1/images/edits",
        headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}"},
        files={"image": image_file},
        data={
            "model": "qwen-image-edit",
            "prompt": "آسمان را به غروب دراماتیک با رنگ‌های نارنجی و بنفش تغییر دهید",
        },
    )

print(f"تصویر ویرایش شده: {edit_response.json()}")

# استفاده از فرمت بومی Dashscope برای پارامترهای پیشرفته
dashscope_response = requests.post(
    "https://api.avalai.ir/v1/images/generations",
    headers={
        "Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "model": "qwen-image",
        "input": {
            "messages": [
                {
                    "role": "user",
                    "content": [
                        {
                            "text": "عکس پرتره حرفه‌ای از یک فرد تجاری مطمئن در محیط اداری مدرن"
                        }
                    ],
                }
            ]
        },
        "parameters": {
            "size": "1328*1328",
            "prompt_extend": True,
            "watermark": False,
            "negative_prompt": "تار، کیفیت پایین، تحریف شده",
        },
    },
)

print(f"نتیجه فرمت Dashscope: {dashscope_response.json()}")

javascript=:import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// تولید متن-به-تصویر با استفاده از فرمت OpenAI SDK
const response = await client.images.generate({
    model: "qwen-image",
    prompt: "منظره شهری آینده‌نگرانه با ماشین‌های پرنده و چراغ‌های نئون",
    size: "1664x928", // نسبت ابعاد 16:9
    n: 1,
    response_format: "url", // or b64_json
});

console.log(`URL تصویر تولید شده: ${response.data[0].url}`);

// استفاده از فرمت بومی Dashscope برای پارامترهای پیشرفته
const dashscopeResponse = await fetch("https://api.avalai.ir/v1/images/generations", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        model: "qwen-image",
        input: {
            messages: [
                {
                    role: "user",
                    content: [
                        {
                            text: "صحنه جنگل جادویی با قارچ‌های درخشان و چراغ‌های پری"
                        }
                    ]
                }
            ]
        },
        parameters: {
            size: "1328*1328",
            prompt_extend: true,
            watermark: false,
            negative_prompt: "تاریک، غمگین، ترسناک"
        }
    })
});

const result = await dashscopeResponse.json();
console.log("نتیجه فرمت Dashscope:", result);

```

#### پارامترهای اختصاصی مدل Qwen

هنگام استفاده از فرمت بومی Dashscope، می‌توانید به پارامترهای اضافی دسترسی داشته باشید:

- `prompt_extend` - فعال‌سازی بازنویسی هوشمند prompt برای نتایج بهتر
- `watermark` - کنترل اضافه کردن watermark Qwen-Image
- `negative_prompt` - مشخص کردن آنچه که نمی‌خواهید در تصویر باشد
- `size` - پشتیبانی از نسبت‌های مختلف ابعاد (1328×1328، 1664×928، 1472×1140، 1140×1472، 928×1664)
- `seed` - تنظیم seed تصادفی برای نتایج قابل تکرار

> **نکته:** پارامترهای خاص موجود به ارائه‌دهنده مدل بستگی دارد. برای فهرست کامل پارامترها به مستندات مدل‌های فردی مراجعه کنید. سیستم به طور خودکار نگاشت این پارامترها به فرمت API ارائه‌دهنده مناسب را انجام می‌دهد.

## فرمت پاسخ (Response Format)

routeهای GPT Image داده تصویر را به‌صورت Base64 برمی‌گردانند. مقدار `data[0].b64_json` را decode و bytes را ذخیره کنید:

```json
{
  "created": 1589478378,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEU...",
      "revised_prompt": "یک بچه سمور دریایی بامزه با خز قهوه‌ای، که در آب اقیانوس آبی شفاف به پشت شناور است. پنجه‌های کوچک سمور در حالی که با آرامش استراحت می‌کند، قابل مشاهده است، با امواج ملایم اطراف آن زیر آسمان روشن."
    }
  ]
}
```

برخی مدل‌های قدیمی تصویر یا routeهای ارائه‌دهنده ممکن است وقتی `response_format` برابر `url` باشد URL برگردانند:

```json
{
  "created": 1589478378,
  "data": [
    {
      "url": "https://avalai-generated-images.storage.googleapis.com/image1.png",

      "revised_prompt": "یک بچه سمور دریایی بامزه با خز قهوه‌ای، که در آب اقیانوس آبی شفاف به پشت شناور است. پنجه‌های کوچک سمور در حالی که با آرامش استراحت می‌کند، قابل مشاهده است، با امواج ملایم اطراف آن زیر آسمان روشن."
    }
  ]
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر   | نوع     | توضیحات                              |
| --------- | ------- | ------------------------------------ |
| `created` | integer | زمان یونیکس (به ثانیه) ایجاد تصاویر. |
| `data`    | array   | آرایه‌ای از اشیا تصویر.              |

### شی تصویر (Image Object)

| پارامتر          | نوع    | توضیحات                                                                                                     |
| ---------------- | ------ | ----------------------------------------------------------------------------------------------------------- |
| `b64_json`       | string | داده تصویر کدگذاری‌شده با Base64. برای routeهای سبک GPT Image وجود دارد. |
| `url`            | string | URL تصویر تولید شده. فقط وقتی route یا مدل انتخابی خروجی URL را پشتیبانی کند وجود دارد. |
| `revised_prompt` | string | پرامپتی که برای تولید تصویر استفاده شده است، که ممکن است برای نتایج بهتر اصلاح شده باشد.                    |

## ویرایش تصویر (Image Editing)

AvalAI از قابلیت‌های جامع ویرایش تصویر از طریق نقطه پایانی زیر پشتیبانی می‌کند:

```
POST https://api.avalai.ir/v1/images/edits
```

این به شما امکان می‌دهد با ارائه فایل تصویر و یک پرامپت توصیفی برای تغییرات مورد نظر، یک تصویر موجود را ویرایش کنید.

### بدنه درخواست (Multipart یا JSON)

| پارامتر           | نوع     | الزامی | توضیحات                                                                                                       |
| ----------------- | ------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| `model`           | string  | بله    | شناسه مدلی که برای ویرایش استفاده می‌شود (مدل‌های پشتیبانی شده را در زیر ببینید).                             |
| `image`           | file یا file[] | برای multipart بله | فایل یا فایل‌های منبع برای ویرایش در `multipart/form-data`. الزامات به مدل وابسته است؛ routeهای GPT Image می‌توانند یک یا چند تصویر منبع بپذیرند. |
| `images`          | array   | برای درخواست JSON بله | referenceهای تصویر منبع برای درخواست‌های JSON سبک GPT Image. هر item یک object با دقیقا یکی از `image_url` یا `file_id` است؛ `image_url` می‌تواند URL کامل یا data URL با Base64 باشد. routeهای GPT Image در صورت فعال بودن می‌توانند تا 16 تصویر ورودی بپذیرند. |
| `mask`            | file یا object | خیر | ماسک اختیاری. در درخواست multipart فایل بفرستید، و در درخواست JSON یک object با دقیقا یکی از `image_url` یا `file_id` بفرستید. برای masking سبک GPT Image، ابعاد ماسک را با تصویر منبع یکسان نگه دارید و در صورت نیاز alpha channel داشته باشید. |
| `prompt`          | string  | بله    | توضیح متنی تصویر نهایی مورد نظر. کل تصویر نهایی را توصیف کنید، نه فقط بخش تغییر. |
| `n`               | integer | خیر    | تعداد تصاویر ویرایش شده که باید تولید شود. پیش‌فرض ۱ است.                                                     |
| `size`            | string  | خیر    | اندازه تصویر ویرایش‌شده. اندازه‌های پشتیبانی‌شده به مدل وابسته است. |
| `quality`         | string  | خیر    | کیفیت GPT Image در صورت پشتیبانی: `low`، `medium`، `high` یا `auto`. مدل‌های GPT Image 2.5 Flare و Sunburst از `xhigh` و `max` نیز پشتیبانی می‌کنند؛ این دو گزینه برای مدل‌های قدیمی GPT Image نیستند. |
| `response_format` | string  | خیر    | مدل‌های قدیمی تصویر ممکن است `url` یا `b64_json` را پشتیبانی کنند. routeهای GPT Image داده Base64 برمی‌گردانند. |
| `output_format`   | string  | خیر    | فرمت فایل خروجی در صورت پشتیبانی: `png`، `jpeg` یا `webp`. |
| `output_compression` | integer | خیر | سطح فشرده‌سازی برای خروجی JPEG/WebP در صورت پشتیبانی. |
| `stream`          | boolean | خیر    | در صورت پشتیبانی route، streaming ویرایش تصویر را فعال می‌کند. |
| `partial_images`  | integer | خیر    | تعداد previewهای تدریجی هنگام streaming، در صورت پشتیبانی. |
| `input_fidelity`  | string  | خیر    | حفظ جزئیات ورودی برای مدل/routeهایی که پشتیبانی می‌کنند. برای `gpt-image-2` ارسال نکنید، چون ورودی‌های تصویری را خودکار با fidelity بالا پردازش می‌کند. |
| `user`            | string  | خیر    | یک شناسه منحصر به فرد که نماینده کاربر نهایی شما است و می‌تواند به نظارت و شناسایی سو استفاده کمک کند.        |

### قیمت‌گذاری GPT Image 2.5 و برآورد خروجی

هر دو مدل `gpt-image-2.5-flare` و `gpt-image-2.5-sunburst` از نرخ‌های تأییدشده زیر در AvalAI استفاده می‌کنند؛ واحد قیمت دلار آمریکا به‌ازای هر ۱ میلیون توکن است:

| نوع مصرف | قیمت |
| --- | ---: |
| ورودی متن | $5.00 |
| ورودی تصویر | $8.00 |
| ورودی متن ذخیره‌شده در حافظه نهان | $1.25 |
| ورودی تصویر ذخیره‌شده در حافظه نهان | $2.00 |
| خروجی متن | $0.00 |
| خروجی تصویر | $30.00 |

| کیفیت | برآورد سهم خروجی هر تصویر 1024x1024 در هر دو مدل (دلار آمریکا) |
| --- | ---: |
| `low` | $0.00588 |
| `medium` | $0.01317 |
| `high` | $0.05268 |
| `xhigh` | $0.09366 |
| `max` | $0.21072 |

این برآوردها **فقط توکن‌های تصویر خروجی** را پوشش می‌دهند، نه کل هزینه تولید یا ویرایش. هزینه متن پرامپت و توکن‌های ورودی همه تصاویر مرجع را نیز اضافه کنید؛ نرخ حافظه نهان فقط برای ورودی واجد شرایط اعمال می‌شود. برای پیش‌نویس از `low` و برای استفاده عمومی از `medium` استفاده کنید. برای تصاویر نهایی، `high`، `xhigh` و `max` را با توجه به کیفیت مورد نیاز، زمان و بودجه مقایسه کنید. دو سطح اضافی `xhigh` و `max` مخصوص این مدل‌های GPT Image 2.5 هستند.

### قیمت‌گذاری و محاسبه هزینه ویرایش با GPT Image 2

ویرایش‌هایی که با `gpt-image-2` روی `v1/images/edits` انجام می‌شوند، به‌جای هزینه ثابت برای هر ویرایش، صورتحساب کاملا مبتنی بر توکن دارند. هزینه کل از اجزای زیر تشکیل می‌شود:

```text
هزینه تخمینی ویرایش = هزینه توکن‌های متن پرامپت
                     + هزینه توکن‌های ورودی همه تصاویر مرجع
                     + هزینه توکن‌های تصویر خروجی
```

متن پرامپت با نرخ $5.00 / ۱ میلیون توکن، ورودی تصویر با نرخ $8.00 / ۱ میلیون توکن ($2.00 / ۱ میلیون در حالت کش شده) و خروجی تصویر با نرخ $30.00 / ۱ میلیون توکن محاسبه می‌شود. مقادیر درخواستی `quality` و `size` تعداد توکن‌های تصویر خروجی را کنترل می‌کنند و هر تصویر منبع یا مرجع نیز توکن‌های ورودی تصویر را اضافه می‌کند.

#### هزینه‌های تقریبی هر تصویر بر اساس کیفیت و رزولوشن

جدول زیر **هزینه تخمینی تصویر خروجی** را بر اساس ماشین‌حساب هزینه تولید تصویر OpenAI نشان می‌دهد. این مقادیر نرخ ثابت نیستند و هزینه متن پرامپت یا توکن‌های ورودی تصاویر مرجع را شامل نمی‌شوند. هزینه واقعی ویرایش با پیچیدگی پرامپت، اندازه خروجی و تعداد و ابعاد تصاویر مرجع تغییر می‌کند.

| کیفیت | 1024x1024 (مربع) | 1024x1536 (عمودی) | 1536x1024 (افقی) |
| ------- | ------------------ | -------------------- | --------------------- |
| پایین   | ~$0.008            | ~$0.012              | ~$0.012               |
| متوسط   | ~$0.032            | ~$0.048              | ~$0.048               |
| بالا    | ~$0.125            | ~$0.187              | ~$0.187               |

برای برآورد دقیق، همیشه از ماشین‌حساب رسمی تولید تصویر OpenAI با پرامپت، تصاویر مرجع، کیفیت و رزولوشن خاص خود استفاده کنید.

#### هر تنظیم کیفیت چه چیزی تولید می‌کند

- **پایین:** تولید سریع‌تر با کمترین هزینه. برای پیش‌نویس‌ها، دارایی‌های دیجیتال کوچک و pipelineهای خودکاری مناسب است که کنترل هزینه در آن‌ها از جزئیات ظریف مهم‌تر است.
- **متوسط:** برای بیشتر تولیدات بازاریابی و محتوا، از جمله تصاویر شبکه‌های اجتماعی، گرافیک‌های تحریریه، mockup محصول و دارایی‌های کمپین مناسب است. در اکثر زمینه‌ها برای انتشار حرفه‌ای کافی است.
- **بالا:** برای دارایی‌های نهایی production طراحی شده که دقت در سطح پیکسل اهمیت دارد؛ از جمله عکاسی شاخص محصول، مواد چاپی با رزولوشن بالا، طراحی بسته‌بندی و mockupهای دقیق UI.

در workflowهای ویرایش حساس به هزینه، iterationها را با `quality="low"` انجام دهید و فقط نتیجه تاییدشده را با `quality="high"` رندر کنید. برای راهنمایی بیشتر درباره کنترل هزینه، به [تولید تصاویر با GPT Image](fa/examples/generate_images_with_gpt_image.md) مراجعه کنید.

### فرمت‌های درخواست و ماسک‌ها

- برای upload فایل محلی از `multipart/form-data` استفاده کنید: تصویرهای منبع را با `image` / `image[]` و ماسک اختیاری را به‌صورت فایل binary بفرستید.
- برای editهای JSON سبک GPT Image از `application/json` استفاده کنید: تصویرهای منبع را در `images` به‌صورت objectهایی بفرستید که دقیقا یکی از `image_url` یا `file_id` را دارند. `image_url` می‌تواند URL کامل یا data URL با Base64 مثل `data:image/png;base64,...` باشد.
- ماسک‌های JSON را به‌صورت object با دقیقا یکی از `image_url` یا `file_id` بفرستید؛ مثلا `{ "image_url": "data:image/png;base64,..." }` یا `{ "file_id": "file_..." }`.
- در ویرایش با mask، ماسک و تصویر منبع باید format و ابعاد یکسان داشته باشند. ماسک‌های سبک GPT Image باید alpha channel داشته باشند؛ ناحیه‌های transparent مشخص می‌کنند مدل کجا اجازه ویرایش دارد.
- برای `gpt-image-2`، `input_fidelity` را ارسال نکنید؛ مدل ورودی‌های تصویری را خودکار با fidelity بالا پردازش می‌کند. در routeهای قدیمی‌تر که این پارامتر را ارائه می‌کنند، برای چهره، لوگو، بسته‌بندی محصول، screenshot و ویرایش‌های حساس به جزئیات از fidelity بالا استفاده کنید.
- ویرایش streaming در routeهای پشتیبانی‌شده eventهایی مثل `image_edit.partial_image` و `image_edit.completed` برمی‌گرداند. تصویرهای جزئی را preview بدانید و خروجی final completed را به‌عنوان asset production ذخیره کنید.

### مدل‌های پشتیبانی شده برای ویرایش تصویر

مدل‌های زیر از نقطه پایانی `v1/images/edits` پشتیبانی می‌کنند:

#### مدل‌های OpenAI

- **gpt-image-2.5-flare** - تازه‌ترین انتخاب پیش‌فرض عمومی برای تولید و ویرایش سریع‌تر تصویر
- **gpt-image-2.5-sunburst** - تازه‌ترین گزینه حرفه‌ای برای ویرایش دقیق‌تر با زمان تولید طولانی‌تر
- **gpt-image-2** - مدل نسل قبلی GPT Image برای گردش‌کارهای موجود و آزموده‌شده
- **gpt-image-1.5** - مدل پیشرفته قبلی GPT Image برای workflowهای موجود و validate شده
- **gpt-image-1** - مدل تولید و ویرایش تصویر GPT Image
- **gpt-image-1-mini** - مدل کم‌هزینه‌تر GPT Image برای draft و ideation پرترافیک

#### مدل‌های Black Forest Labs

- **flux.1-kontext-pro** - مدل پیشرفته FLUX با قابلیت‌های ویرایش حرفه‌ای

#### مدل‌های Google

- **gemini-3.1-flash-image** (نانو بنانا ۲) - مدل پرچمدار تصویر گوگل؛ برای گردش‌کارهای ویرایش تصویر-به-تصویر از طریق `v1/chat/completions` یا `v1beta/` استفاده کنید. تمام مدل‌های `imagen-*` منسوخ شده و از فهرست حذف شده‌اند.

### ویرایش با GPT Image 2.5 Sunburst و curl

مقدار `AVALAI_API_KEY` را تنظیم کنید و تصویر منبع محلی را با نام `input_image.png` آماده کنید. این مثال multipart به curl، jq و base64 نیاز دارد. Flare نیز از همین نقطه پایانی پشتیبانی می‌کند؛ برای مقایسه نتایج، فقط شناسه مدل را تغییر دهید.

```bash
curl --fail-with-body https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gpt-image-2.5-sunburst" \
  -F "image=@input_image.png" \
  -F "prompt=Change only the background to warm white. Keep the product, logo, texture, camera angle, and composition unchanged." \
  -F "size=1024x1024" \
  -F "quality=high" \
  -F "n=1" >sunburst-response.json \
  && jq -er '.data[0].b64_json' sunburst-response.json | base64 --decode >sunburst-edit.png
```

### مثال ویرایش تصویر

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# ویرایش تصویر موجود
with open("input_image.png", "rb") as image_file:
    response = client.images.edit(
        model="gpt-image-2",
        image=image_file,
        prompt="رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
        size="1024x1024",
        n=1,
    )

# ذخیره تصویر ویرایش شده
import base64

edited_image = base64.b64decode(response.data[0].b64_json)
with open("edited_image.png", "wb") as f:
    f.write(edited_image)

print("✅ تصویر ویرایش شد و با نام edited_image.png ذخیره شد")

javascript=:import fs from 'fs';
import OpenAI from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// ویرایش تصویر موجود
const imageFile = fs.createReadStream("input_image.png");
const response = await client.images.edit({
 model: "gpt-image-2",
 image: imageFile,
 prompt: "رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
 size: "1024x1024",
 n: 1,
});

// ذخیره تصویر ویرایش شده
const imageBase64 = response.data[0].b64_json;
fs.writeFileSync("edited_image.png", Buffer.from(imageBase64, "base64"));

console.log("✅ تصویر ویرایش شد و با نام edited_image.png ذخیره شد");

```

### ویرایش تصویر با ورودی Base64 (بدون SDK)

اگر در محیطی کار می‌کنید که SDK OpenAI در دسترس نیست، می‌توانید `v1/images/edits` را مستقیم از طریق HTTP صدا بزنید. برای درخواست‌های JSON ویرایش سبک GPT Image، تصویر منبع را به data URL با Base64 (`data:{mime_type};base64,{encoded_data}`) تبدیل کنید و طبق [فرمت‌های درخواست بالا](#فرمتهای-درخواست-و-ماسکها)، آن را در آرایه `images` با یک object شامل `image_url` بفرستید. این schema مورد انتظار برای referenceهای تصویری JSON است؛ `image_url` می‌تواند URL عمومی HTTPS هم باشد و برای تصویرهای آپلودشده از Files API می‌توانید `file_id` بفرستید. بسته به route، تصویر ویرایش‌شده ممکن است در `data[0].b64_json`، به‌صورت data URL با Base64 در `data[0].url` یا به‌صورت URL قابل دانلود برگردد؛ قبل از ذخیره bytes همه شکل‌های پشتیبانی‌شده را handle کنید.

```language-selector
bash=:# تصویر منبع را Base64 encode کنید (در Linux برای حذف line break از `base64 -w 0` استفاده کنید)
IMAGE_BASE64=$(base64 -i input_image.png | tr -d '\n')

curl https://api.avalai.ir/v1/images/edits \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-image-2",
  "prompt": "رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
  "images": [
    { "image_url": "data:image/png;base64,'"$IMAGE_BASE64"'" }
  ],
  "size": "1024x1024",
  "n": 1
}' | jq -r '
  .data[0]
  | if .b64_json then .b64_json
    elif (.url // "" | startswith("data:")) then (.url | split(",")[1])
    else error("response did not include b64_json or a data URL")
    end
' | base64 --decode >edited_image.png

python=:import base64
import os

import requests


def save_image_result(image, output_path):
    """Save an image result that may contain b64_json, a data URL, or a URL."""
    if image.get("b64_json"):
        image_bytes = base64.b64decode(image["b64_json"])
    elif image.get("url", "").startswith("data:"):
        _, encoded = image["url"].split(",", 1)
        image_bytes = base64.b64decode(encoded)
    elif image.get("url"):
        image_response = requests.get(image["url"], timeout=120)
        image_response.raise_for_status()
        image_bytes = image_response.content
    else:
        raise ValueError(f"No image payload found in response item: {image}")

    with open(output_path, "wb") as f:
        f.write(image_bytes)


# تصویر منبع را به data URL با Base64 تبدیل کنید
with open("input_image.png", "rb") as image_file:
    image_base64 = base64.b64encode(image_file.read()).decode("utf-8")

response = requests.post(
    "https://api.avalai.ir/v1/images/edits",
    headers={
        "Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={
        "model": "gpt-image-2",
        "prompt": "رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید",
        "images": [{"image_url": f"data:image/png;base64,{image_base64}"}],
        "size": "1024x1024",
        "n": 1,
    },
)
response.raise_for_status()

save_image_result(response.json()["data"][0], "edited_image.png")

print("✅ تصویر ویرایش شد و با نام edited_image.png ذخیره شد")

```

اگر route انتخابی فقط `multipart/form-data` را پشتیبانی می‌کند، به‌جای Base64 فایل خام را upload کنید — در curl از `-F "image=@input_image.png"` استفاده کنید و در Python `requests`، file handle باز را با `files={"image": image_file}` مثل مثال Qwen بالا بفرستید. data URLهای Base64 فقط برای درخواست‌های ویرایش JSON کاربرد دارند.

## تغییرات تصویر (Image Variations)

AvalAI در حال حاضر مدل variation پشتیبانی‌شده‌ای را در `data/models.json` فهرست نمی‌کند. این endpoint را placeholder سازگاری در نظر بگیرید و برای workflowهای شبیه variation از `v1/images/edits` همراه تصویر منبع یا از `v1/images/generations` با brief دقیق تصویر منبع استفاده کنید.

```
POST https://api.avalai.ir/v1/images/variations
```

## مدل‌های موجود

AvalAI از مدل‌های مختلف تولید و ویرایش تصویر از ارائه‌دهندگان مختلف پشتیبانی می‌کند:

### مدل‌های تولید تصویر

| ارائه دهنده       | مدل                            | توضیحات                                                                   | نقاط پایانی پشتیبانی شده                     |
| ----------------- | ------------------------------ | ------------------------------------------------------------------------- | -------------------------------------------- |
| BytePlus          | seedream-5-0-260128            | پیشرفته‌ترین مدل Seedream با استدلال زنجیره فکر (CoT)، زیبایی‌شناسی سبک MJ و بهینه‌سازی هوشمند prompt | `v1/images/generations`, `v1/images/edits` |
| BytePlus          | seedream-4-5-251128            | مدل Seedream جدید با حالت‌های تولید پیشرفته، پایبندی بهتر به prompt و قابلیت‌های ویرایش چندتصویری | `v1/images/generations`, `v1/images/edits` |
| OpenAI | gpt-image-2.5-flare | تازه‌ترین انتخاب پیش‌فرض عمومی برای تولید و ویرایش سریع‌تر | `/v1/images/generations`, `/v1/images/edits` |
| OpenAI | gpt-image-2.5-sunburst | تازه‌ترین مدل حرفه‌ای برای ویرایش دقیق‌تر با زمان تولید طولانی‌تر | `/v1/images/generations`, `/v1/images/edits` |
| OpenAI | gpt-image-2 | مدل نسل قبلی با پیروی دقیق از پرامپت و قابلیت ویرایش | `v1/images/generations`, `v1/images/edits` |
| OpenAI | gpt-image-1.5 | مدل پیشرفته نسل قبلی برای تولید و ویرایش تصویر | `v1/images/generations`, `v1/images/edits` |
| OpenAI            | gpt-image-1                    | مدل پیشرفته تولید و ویرایش تصویر OpenAI (فقط سطح 3، 4، 5)                  | `v1/images/generations`, `v1/images/edits` |
| OpenAI            | gpt-image-1-mini               | نسخه مقرون به صرفه GPT Image 1 برای برنامه‌های با حجم بالا (فقط سطح 3، 4، 5) | `v1/images/generations`, `v1/images/edits` |
| Black Forest Labs | flux.2-pro                     | پیشرفته‌ترین مدل FLUX با کیفیت تصویر برتر و قیمت‌گذاری بر اساس مگاپیکسل | `v1/images/generations`                     |
| Black Forest Labs | flux-1.1-pro                   | مدل پیشرفته FLUX                                                          | `v1/images/generations`                     |
| Black Forest Labs | flux.1-kontext-pro             | مدل پیشرفته FLUX با قابلیت‌های ویرایش حرفه‌ای                             | `v1/images/generations`                     |
| Google            | gemini-2.5-flash-image | Nano Banana - مدل پایدار و پیشرفته تولید تصویر با قابلیت‌های تبدیل متن به تصویر و تصویر به تصویر | `v1/chat/completions`                       |
| Google            | gemini-3-pro-image | Nano Banana Pro (پایدار) - تولید تصویر درجه حرفه‌ای برای دارایی‌های برند، کیفیت فتورئالیستیک | `v1/chat/completions`، `v1beta/`                       |
| Google            | gemini-3.1-flash-image | Nano Banana 2 (پایدار) - تولید تصویر پرچمدار با کارایی بالا با رزولوشن تا 4K، رندرینگ متن پیشرفته | `v1/chat/completions`، `v1beta/`                       |
| Google            | gemini-3.1-flash-lite-image | Nano Banana 2 Lite - متخصص کارایی با تاخیر زیر ۲ ثانیه و تولید مقرون‌به‌صرفه در رزولوشن 1K | `v1/chat/completions`، `v1beta/`                       |
| Google            | gemini-3-pro-image-preview | نام مستعار پیش‌نمایش قدیمی Nano Banana Pro؛ برای یکپارچه‌سازی‌های تولیدی جدید از `gemini-3-pro-image` استفاده کنید | `v1/chat/completions`                       |
| Google            | gemini-3.1-flash-image-preview | نام مستعار پیش‌نمایش قدیمی Nano Banana 2؛ برای یکپارچه‌سازی‌های تولیدی جدید از `gemini-3.1-flash-image` استفاده کنید | `v1/chat/completions`                       |
| Google            | imagen-4.0-ultra-generate-001  | ❌ **منسوخ شده و حذف شده** - تولید تصویر با کیفیت فوق‌العاده بالا. به `gemini-3-pro-image` مهاجرت کنید | حذف شده |
| Google            | imagen-4.0-generate-001        | ❌ **منسوخ شده و حذف شده** - تولید تصویر حرفه‌ای با کیفیت بالا. به `gemini-3.1-flash-image` مهاجرت کنید | حذف شده |
| Google            | imagen-4.0-fast-generate-001   | ❌ **منسوخ شده و حذف شده** - تولید تصویر سریع. به `gemini-3.1-flash-image` مهاجرت کنید | حذف شده |
| Google            | imagen-3.0-generate-002        | ❌ **منسوخ شده و حذف شده** - نسخه به‌روز Imagen 3.0. به `gemini-3.1-flash-image` مهاجرت کنید | حذف شده |
| Google            | imagen-3.0-generate-001        | ❌ **منسوخ شده و حذف شده** - مدل Imagen 3.0 گوگل برای تولید و ویرایش تصویر. به `gemini-3.1-flash-image` مهاجرت کنید | حذف شده |
| Google            | imagen-3.0-fast-generate-001   | ❌ **منسوخ شده و حذف شده** - نسخه سریع Imagen 3.0. به `gemini-3.1-flash-image` مهاجرت کنید | حذف شده |
| Alibaba           | qwen-image-3.0-pro             | تولید و ویرایش حرفه‌ای؛ $0.04 در ۱K/حدود ۱ MP، $0.075 در ۲ تا ۴ MP و $0.003 برای هر تصویر مرجع | `v1/images/generations`, `v1/images/edits` |
| Alibaba           | qwen-image-3.0                 | تولید و ویرایش عمومی؛ $0.04 در ۱K/حدود ۱ MP، $0.075 در ۲ تا ۴ MP و $0.003 برای هر تصویر مرجع | `v1/images/generations`, `v1/images/edits` |
| Alibaba           | qwen-image-2.0-pro             | تولید تصویر حرفه‌ای با تایپوگرافی پیشرفته و رزولوشن بومی ۲K                | `v1/images/generations`                     |
| Alibaba           | qwen-image-2.0                 | تولید و ویرایش یکپارچه با رزولوشن بومی ۲K و فوتورئالیسم                    | `v1/images/generations`, `v1/images/edits`  |
| Alibaba           | z-image-turbo                  | تولید تصویر فوق‌سریع با حالت Thinking برای کیفیت بهتر                      | `v1/images/generations`                     |
| Alibaba           | qwen-image                     | تولید پیشرفته متن-به-تصویر با بهبود هوشمند prompt                        | `v1/images/generations`                     |
| Cloudflare        | cf.flux-2-klein-9b             | FLUX 2 Klein 9B - تولید تصویر با کیفیت بالا                               | `v1/images/generations`                     |
| Cloudflare        | cf.flux-2-klein-4b             | FLUX 2 Klein 4B - تولید تصویر سریع                                        | `v1/images/generations`                     |
| Cloudflare        | cf.flux-2-dev                  | FLUX 2 Dev - نسخه توسعه با ویژگی‌های انعطاف‌پذیر                           | `v1/images/generations`                     |
| Cloudflare        | cf.lucid-origin                | Lucid Origin - تولید تصویر خلاقانه و هنری                                 | `v1/images/generations`                     |
| Cloudflare        | cf.phoenix-1.0                 | Phoenix 1.0 - تعادل بین کیفیت و سرعت                                      | `v1/images/generations`                     |

### مدل‌های ویرایش تصویر

| ارائه دهنده       | مدل                               | توضیحات                                                            | نقاط پایانی پشتیبانی شده |
| ----------------- | --------------------------------- | ------------------------------------------------------------------ | ------------------------ |
| OpenAI | gpt-image-2.5-flare | تازه‌ترین انتخاب پیش‌فرض عمومی برای ویرایش سریع‌تر | `/v1/images/edits` |
| OpenAI | gpt-image-2.5-sunburst | تازه‌ترین گزینه حرفه‌ای برای ویرایش دقیق‌تر با زمان تولید طولانی‌تر | `/v1/images/edits` |
| OpenAI | gpt-image-2 | مدل نسل قبلی برای ویرایش تصویر | `v1/images/edits` |
| OpenAI | gpt-image-1.5 | مدل پیشرفته نسل قبلی برای ویرایش تصویر | `v1/images/edits` |
| OpenAI            | gpt-image-1                       | مدل پیشرفته تولید و ویرایش تصویر OpenAI (فقط سطح 3، 4، 5)         | `v1/images/edits`       |
| OpenAI            | gpt-image-1-mini                  | نسخه مقرون به صرفه GPT Image 1 برای برنامه‌های با حجم بالا (فقط سطح 3، 4، 5) | `v1/images/edits`       |
| Black Forest Labs | flux.1-kontext-pro                | مدل پیشرفته FLUX با قابلیت‌های ویرایش حرفه‌ای                      | `v1/images/edits`       |
| Google            | gemini-3.1-flash-image            | نانو بنانا ۲ - مدل پرچمدار ویرایش تصویر گوگل (جایگزین مسیرهای حذف‌شده `imagen-*`)؛ از طریق `v1/chat/completions` یا `v1beta/` استفاده کنید | `v1/chat/completions`, `v1beta/` |
| Alibaba           | qwen-image-3.0-pro                | ویرایش حرفه‌ای با هزینه $0.003 برای هر تصویر مرجع/ورودی             | `v1/images/edits`       |
| Alibaba           | qwen-image-3.0                    | ویرایش عمومی با هزینه $0.003 برای هر تصویر مرجع/ورودی                | `v1/images/edits`       |
| Alibaba           | qwen-image-2.0-pro                | ویرایش حرفه‌ای با خطای تایپوگرافی نزدیک به صفر در بیش از ۴۰ زبان   | `v1/images/edits`       |
| Alibaba           | qwen-image-2.0                    | تولید و ویرایش یکپارچه با خروجی فوتورئالیستیک حرفه‌ای              | `v1/images/edits`       |
| Alibaba           | qwen-image-edit-plus              | ویرایش پیشرفته تصویر با کیفیت بهبودیافته و پشتیبانی چند تصویری      | `v1/images/generations`, `v1/images/edits` |
| Alibaba           | qwen-image-edit                   | ویرایش پیچیده تصویر با پشتیبانی ورودی چند تصویری                   | `v1/images/edits`       |

## مدیریت خطا (Error Handling)

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات                                                                  |
| -------- | ------------------------------------------------------------------------ |
| 400      | درخواست بد - درخواست شما نامعتبر است (مثلا پرامپت بیش از حد طولانی است). |
| 401      | غیرمجاز - کلید API شما اشتباه است.                                       |
| 403      | ممنوع - شما اجازه دسترسی به این منبع را ندارید.                          |
| 404      | یافت نشد - منبع مشخص شده یافت نشد.                                       |
| 429      | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید.           |
| 500      | خطای داخلی سرور - مشکلی در سرور ما وجود داشت.                            |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

برای خطاهای مخصوص تصویر که با اصلاح ورودی قابل‌حل هستند، بدون تغییر prompt، mask یا تصویر منبع retry خودکار انجام ندهید. خطاهای moderation ممکن است با `error.code = "moderation_blocked"` برگردند و گاهی `moderation_details` اختیاری داشته باشند:

- `moderation_stage`: یکی از `input`، `output` یا `unknown`
- `categories`: برچسب‌های عمومی و کلی مانند `harassment`، `self-harm`، `sexual` یا `violence`

این جزئیات را برای log توسعه‌دهنده و support نگه دارید، اما پیام کاربر نهایی را عمومی، کوتاه و قابل‌اقدام بنویسید.

## نظارت محتوا (Content Moderation)

تمام درخواست‌های تولید تصویر مشمول نظارت محتوا هستند. promptها یا خروجی‌هایی که خط‌مشی محتوا را نقض کنند رد می‌شوند. routeهای سبک GPT Image ممکن است پارامتر `moderation` را ارائه کنند؛ برای production مقدار `auto` را نگه دارید و `low` را فقط پس از review ایمنی استفاده کنید. برای اطلاعات بیشتر، به راهنمای [خط‌مشی محتوا](fa/safety/content-policy.md) مراجعه کنید.

## منابع مرتبط

- [مدل‌ها](fa/models/model-details.md) - درباره مدل‌های تولید تصویر موجود بیاموزید
- [ساخت تصویر با GPT Image](fa/examples/generate_images_with_gpt_image.md) - الگوهای prompt و ویرایش اقتباس‌شده از Cookbook برای `gpt-image-2`
- [راهنمای تولید تصویر](fa/guides/image-generation.md) - انتخاب مدل و پارامترهای مخصوص ارائه‌دهنده
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
