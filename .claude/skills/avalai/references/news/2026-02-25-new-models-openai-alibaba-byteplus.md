# News 2026-02-25-new-models-openai-alibaba-byteplus: Seedream 5.0 برای تولید تصویر
URL: `https://docs.avalai.ir/fa/news/2026-02-25-new-models-openai-alibaba-byteplus`
**تاریخ:** 1404-12-06 / (2026-02-25)

# مدل‌های جدید اضافه شدند: GPT-5.3-Codex، GPT-Audio-1.5، Qwen3.5 Flash، Qwen3-Coder-Next و Seedream 5.0

**تاریخ:** 1404-12-06 / (2026-02-25)

## خلاصه

ما دسترسی به شش مدل جدید از سه ارائه‌دهنده را اعلام می‌کنیم: GPT-5.3-Codex از OpenAI (قدرتمندترین مدل کدنویسی عاملی) و GPT-Audio-1.5 (بهترین مدل صوتی برای ورودی/خروجی صوتی)، Qwen3.5-Flash، Qwen3-Coder-Next و Qwen3.5-35B-A3B از Alibaba (مدل‌های کارآمد نسل جدید)، و Seedream 5.0 از BytePlus (تولید تصویر پیشرفته با استدلال زنجیره فکر). این مدل‌ها قابلیت‌های پیشرفته‌ای در کدنویسی عاملی، پردازش صوتی، استنتاج کارآمد و تولید تصویر ارائه می‌دهند.


## نمونه‌های درخواست/پاسخ API

### نمونه GPT-5.3-Codex

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.3-codex",
    "input": "این کدبیس را برای پیاده‌سازی تزریق پیش‌نیاز بازنویسی کن و پوشش تست جامع اضافه کن.",
    "reasoning": {"effort": "high"}
  }'
```

### نمونه GPT-Audio-1.5

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-1.5",
    "messages": [
      {
        "role": "user",
        "content": "یک داستان کوتاه درباره یک ربات که نقاشی یاد می‌گیرد برایم بگو."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }'
```

صدای بازگشتی به‌صورت Base64 در مسیر `choices[0].message.audio.data` قرار می‌گیرد. برای تبدیل آن به یک فایل MP3 قابل پخش مستقیم از ترمینال (به `jq` نیاز دارد)، یک دستور یک‌باره اجرا کنید:

```zsh
# macOS (zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-1.5",
    "messages": [
      {
        "role": "user",
        "content": "یک داستان کوتاه درباره یک ربات که نقاشی یاد می‌گیرد برایم بگو."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 -D > output.mp3

afplay output.mp3
```

```bash
# لینوکس (bash/zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-1.5",
    "messages": [
      {
        "role": "user",
        "content": "یک داستان کوتاه درباره یک ربات که نقاشی یاد می‌گیرد برایم بگو."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 --decode >output.mp3

ffplay -nodisp -autoexit output.mp3
```

```powershell
# ویندوز (PowerShell)
$response = curl.exe -sS "https://api.avalai.ir/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:AVALAI_API_KEY" `
  -d '{
    "model": "gpt-audio-1.5",
    "messages": [
      {
        "role": "user",
        "content": "یک داستان کوتاه درباره یک ربات که نقاشی یاد می‌گیرد برایم بگو."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' | ConvertFrom-Json

[IO.File]::WriteAllBytes(
  (Join-Path $PWD "output.mp3"),
  [Convert]::FromBase64String($response.choices[0].message.audio.data)
)

Start-Process .\output.mp3
```

این‌ها دستورهای یک‌باره ترمینال هستند و نیازی نیست چیزی به `.zshrc`، `.bashrc` یا پروفایل PowerShell اضافه شود.

### نمونه Qwen3.5-Flash

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.5-flash",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس جامع برای پلتفرم تجارت الکترونیک طراحی کن."
      }
    ],
    "extra_body": {"enable_thinking": false}
  }'
```

### نمونه Qwen3-Coder-Next

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3-coder-next",
    "messages": [
      {
        "role": "user",
        "content": "الگوریتم مرتب‌سازی سریع با مدیریت خطای جامع بنویس."
      }
    ],
    "max_tokens": 4096,
    "temperature": 1.0,
    "extra_body": {"enable_thinking": false}
  }'
```

### نمونه Seedream 5.0

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "seedream-5-0-260128",
    "prompt": "عکاسی حرفه‌ای محصول از ساعت لوکس با متن PREMIUM QUALITY، نورپردازی دراماتیک، وضوح 4K",
    "size": "4K",
    "response_format": "url",
    "sequential_image_generation": "disabled",
    "watermark": false
  }'
```

---

## نمونه‌های استفاده از SDK

```language-selector
bash=:# GPT-5.3-Codex از طریق API پاسخ‌ها
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.3-codex",
    "input": "یک REST API برای سیستم مدیریت وظایف طراحی و پیاده‌سازی کن.",
    "reasoning": {"effort": "medium"}
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# GPT-5.3-Codex برای کدنویسی عاملی
response = client.responses.create(
    model="gpt-5.3-codex",
    input="یک REST API برای سیستم مدیریت وظایف طراحی و پیاده‌سازی کن.",
    reasoning={"effort": "medium"},
)

print(response.output_text)

# Qwen3.5-Flash برای کارهای عمومی
completion = client.chat.completions.create(
    model="qwen3.5-flash",
    messages=[
        {
            "role": "user",
            "content": "محاسبات کوانتومی را به زبان ساده توضیح بده.",
        }
    ],
    extra_body={"enable_thinking": False},
)

print(completion.choices[0].message.content)

# Seedream 5.0 برای تولید تصویر
image_response = client.images.generate(
    model="seedream-5-0-260128",
    prompt="منظره شهری آینده‌نگرانه در غروب خورشید با ماشین‌های پرنده",
    size="4K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر تولید شده: {image_response.data[0].url}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// GPT-5.3-Codex برای کدنویسی عاملی
const response = await client.responses.create({
  model: "gpt-5.3-codex",
  input: "یک REST API برای سیستم مدیریت وظایف طراحی و پیاده‌سازی کن.",
  reasoning: { effort: "medium" },
});

console.log(response.output_text);

// Qwen3-Coder-Next برای کارهای کدنویسی
const completion = await client.chat.completions.create({
  model: "qwen3-coder-next",
  messages: [
    {
      role: "user",
      content: "درخت جستجوی دودویی با عملیات درج، حذف و جستجو پیاده‌سازی کن.",
    },
  ],
  max_tokens: 4096,
  temperature: 1.0,
});

console.log(completion.choices[0].message.content);

// Seedream 5.0 برای تولید تصویر
const imageResponse = await client.images.generate({
  model: "seedream-5-0-260128",
  prompt: "منظره شهری آینده‌نگرانه در غروب خورشید با ماشین‌های پرنده",
  size: "4K",
  response_format: "url",
});

console.log(`تصویر تولید شده: ${imageResponse.data[0].url}`);

```

---

## موارد استفاده

### GPT-5.3-Codex
- **کدنویسی عاملی**: کارهای توسعه خودگردان طولانی‌مدت
- **بازنویسی کدبیس بزرگ**: مدیریت تغییرات پیچیده چند فایلی
- **توسعه وب**: ساخت برنامه‌های کامل با بازی‌ها و ویژگی‌های تعاملی
- **دیباگ**: تشخیص و رفع خودکار مشکلات کد
- **تسریع تحقیقات**: تسریع جریان‌های کاری توسعه

### GPT-Audio-1.5
- **عامل‌های صوتی**: ساخت ربات‌های صوتی واکنش‌گرا و شبیه انسان
- **ترجمه بلادرنگ**: ترجمه زنده کارآمد
- **دستیاران تعاملی**: رابط‌های مکالماتی با تاخیر کم
- **پشتیبانی مشتری**: خدمات مشتری طبیعی مبتنی بر صدا

### Qwen3.5-Flash و Qwen3.5-35B-A3B
- **کارهای متن طولانی**: پردازش اسناد و مکالمات گسترده
- **عامل‌های چندوجهی**: درک بینایی و متن در جریان‌های کاری یکپارچه
- **برنامه‌های چندزبانه**: پشتیبانی از ۲۰۱ زبان و گویش
- **استنتاج مقرون‌به‌صرفه**: خروجی‌های با کیفیت بالا با حداقل محاسبات

### Qwen3-Coder-Next
- **توسعه محلی**: کمک کدنویسی کارآمد بر روی سخت‌افزار مصرفی
- **یکپارچگی IDE**: تولید کد بلادرنگ در محیط‌های توسعه
- **جریان‌های کاری عاملی**: استفاده از ابزار و بازیابی از خطا برای کارهای پیچیده
- **بررسی کد**: تحلیل مخازن بزرگ با متن 256K

### Seedream 5.0
- **تجارت الکترونیک**: تجسم محصول با رندر متن
- **بازاریابی**: بصری‌های حرفه‌ای با تایپوگرافی بهبود یافته
- **رندر معماری**: بافت‌های مواد دقیق و نورپردازی
- **نمونه‌های UI/UX**: پروتوتایپ‌های طراحی با کنترل دقیق

---

## لینک‌های مرتبط

- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مستندات مدل‌های BytePlus](fa/providers/byteplus.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [API تولید تصویر](fa/api-reference/images.md)
- [مرجع API صوتی](fa/api-reference/audio.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/pricing.md)
