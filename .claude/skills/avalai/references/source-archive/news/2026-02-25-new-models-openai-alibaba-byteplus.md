# مدل‌های جدید اضافه شدند: GPT-5.3-Codex، GPT-Audio-1.5، Qwen3.5 Flash، Qwen3-Coder-Next و Seedream 5.0

**تاریخ:** 1404-12-06 / (2026-02-25)

## خلاصه

ما دسترسی به شش مدل جدید از سه ارائه‌دهنده را اعلام می‌کنیم: GPT-5.3-Codex از OpenAI (قدرتمندترین مدل کدنویسی عاملی) و GPT-Audio-1.5 (بهترین مدل صوتی برای ورودی/خروجی صوتی)، Qwen3.5-Flash، Qwen3-Coder-Next و Qwen3.5-35B-A3B از Alibaba (مدل‌های کارآمد نسل جدید)، و Seedream 5.0 از BytePlus (تولید تصویر پیشرفته با استدلال زنجیره فکر). این مدل‌ها قابلیت‌های پیشرفته‌ای در کدنویسی عاملی، پردازش صوتی، استنتاج کارآمد و تولید تصویر ارائه می‌دهند.

---

## جزئیات

### OpenAI

#### GPT-5.3-Codex

**GPT-5.3-Codex** (`gpt-5.3-codex`) قدرتمندترین مدل کدنویسی عاملی OpenAI تا به امروز است. این مدل پیشرفت‌های عملکرد کدنویسی GPT-5.2-Codex و قابلیت‌های استدلال GPT-5.2 را در یک مدل ترکیب می‌کند و ۲۵٪ سریع‌تر است. [مستندات](fa/providers/openai.md)

**ویژگی‌های کلیدی:**

- **کدنویسی پیشرفته**: رکوردهای جدید صنعت در SWE-Bench Pro و Terminal-Bench
- **پنجره متنی 400K**: مدیریت کدبیس‌های بزرگ و مستندات گسترده
- **حداکثر 128K توکن خروجی**: تولید راه‌حل‌های کد جامع
- **پشتیبانی از توکن استدلال**: سطوح تلاش قابل تنظیم (کم، متوسط، زیاد، خیلی زیاد)
- **پشتیبانی از بینایی**: پردازش تصاویر برای درک کد بصری
- **همکاری تعاملی**: ارائه به‌روزرسانی‌های مکرر در طول کارهای طولانی
- **خودبهبودی**: اولین مدلی که در ایجاد خودش نقش داشته
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/responses`

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| gpt-5.3-codex | $1.75/1M توکن | $0.175/1M توکن | $14.00/1M توکن |

#### GPT-Audio-1.5

**GPT-Audio-1.5** (`gpt-audio-1.5`) بهترین مدل صوتی OpenAI برای ورودی/خروجی صوتی با Chat Completions است. این مدل برای تعامل بلادرنگ با تاخیر کم و گفتار طبیعی بهینه شده است. [مستندات](fa/providers/openai.md)

**ویژگی‌های کلیدی:**

- **ورودی/خروجی چندوجهی**: ورودی‌های متنی و صوتی، خروجی‌های متنی و صوتی
- **تاخیر کم**: بهینه شده برای هوش مصنوعی مکالماتی بلادرنگ
- **گفتار طبیعی**: خروجی صوتی روان‌تر و مکالماتی‌تر
- **فراخوانی تابع**: پشتیبانی از برنامه‌های تعاملی مبتنی بر ابزار
- **پنجره متنی 128K**: مدیریت مکالمات گسترده
- **حداکثر 16K توکن خروجی**: تولید پاسخ‌های جامع
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`

**قیمت‌گذاری:**

| مدل | ورودی متنی | ورودی کش شده | ورودی صوتی | خروجی متنی | خروجی صوتی |
|-------|------------|--------------|-------------|-------------|--------------|
| gpt-audio-1.5 | $2.50/1M توکن | $1.25/1M توکن | $32.00/1M توکن | $10.00/1M توکن | $64.00/1M توکن |

### Alibaba (Qwen)

#### Qwen3.5-Flash

**Qwen3.5-Flash** (`qwen3.5-flash`) نسخه میزبانی شده Qwen3.5-35B-A3B با ویژگی‌های تولیدی شامل طول متن ۱ میلیون توکن و ابزارهای داخلی رسمی است. این مدل برای کارایی استنتاج بسیار بالا با استفاده از معماری ترکیبی طراحی شده است. [مستندات](fa/providers/alibaba.md)

**ویژگی‌های کلیدی:**

- **معماری ترکیبی**: شبکه‌های دلتای دروازه‌ای + ترکیب پراکنده متخصصان برای استنتاج با توان بالا
- **چندوجهی بومی**: پردازش متن، تصاویر و ویدیوها به صورت بومی
- **پنجره متنی ۱ میلیون توکن**: متن گسترده برای محتوای طولانی
- **۲۰۱ زبان**: پشتیبانی گسترده از زبان‌ها و گویش‌ها
- **ابزارهای داخلی**: پشتیبانی رسمی از استفاده تطبیقی ابزار برای جریان‌های کاری عاملی
- **پشتیبانی از ایجاد کش**: کشینگ کارآمد با قیمت‌گذاری سطحی

**قیمت‌گذاری:**

| مدل | ورودی | ایجاد کش | ورودی کش شده | خروجی |
|-------|-------|----------------|--------------|--------|
| qwen3.5-flash | $0.10/1M توکن | $0.125/1M توکن | $0.01/1M توکن | $0.40/1M توکن |

#### Qwen3-Coder-Next

**Qwen3-Coder-Next** (`qwen3-coder-next`) یک مدل متن‌باز ۸۰ میلیارد پارامتری Mixture-of-Experts است که به طور خاص برای عامل‌های کدنویسی و توسعه محلی با تنها ۳ میلیارد پارامتر فعال طراحی شده است. [مستندات](fa/providers/alibaba.md)

**ویژگی‌های کلیدی:**

- **فوق‌العاده کارآمد**: ۸۰ میلیارد کل / ۳ میلیارد فعال - عملکرد قابل مقایسه با مدل‌های ۱۰-۲۰ برابر بزرگتر
- **قابلیت‌های عاملی پیشرفته**: عملکرد عالی در استدلال طولانی‌مدت، استفاده پیچیده از ابزار و بازیابی از خطا
- **پنجره متنی 256K**: تحلیل مخازن کد بزرگ
- **یکپارچگی IDE**: ادغام یکپارچه با پلتفرم‌های CLI/IDE (Claude Code، Qwen Code، Cline، Trae و غیره)
- **حالت غیر فکری**: بهینه شده برای تولید کد سریع و بلادرنگ

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| qwen3-coder-next | $0.30/1M توکن | $0.15/1M توکن | $1.50/1M توکن |

#### Qwen3.5-35B-A3B

**Qwen3.5-35B-A3B** (`qwen3.5-35b-a3b`) نسخه متن‌باز Qwen3.5-Flash است، با ۳۵ میلیارد پارامتر کل و ۳ میلیارد فعال برای استنتاج کارآمد. [مستندات](fa/providers/alibaba.md)

**ویژگی‌های کلیدی:**

- **معماری ترکیبی**: شبکه‌های دلتای دروازه‌ای + MoE پراکنده برای استنتاج کارآمد
- **بینایی-زبان بومی**: پایه چندوجهی یکپارچه
- **متن بومی 262K**: قابل گسترش تا ۱ میلیون توکن
- **کدنویسی قوی**: ۶۹.۲٪ در SWE-bench Verified
- **قابلیت‌های عاملی**: ۸۱.۲٪ در TAU2-Bench

**قیمت‌گذاری:**

| مدل | ورودی | ورودی کش شده | خروجی |
|-------|-------|--------------|--------|
| qwen3.5-35b-a3b | $0.25/1M توکن | $0.12/1M توکن | $2.00/1M توکن |

### BytePlus (ByteDance)

#### Seedream 5.0

**Seedream 5.0** (`seedream-5-0-260128`) جدیدترین مدل تولید تصویر با کارایی بالای ByteDance با استدلال زنجیره فکر برای بهبود منطق فضایی و انطباق با فیزیک است. [مستندات](fa/providers/byteplus.md)

**ویژگی‌های کلیدی:**

- **استدلال هوشمند**: زنجیره فکر (CoT) برای بهبود منطق فضایی و انطباق با فیزیک
- **متن فعال وب**: اتصال به جستجوهای زنده وب برای رویدادها و محصولات فعلی
- **ویرایش چندمرحله‌ای**: ویرایش مکالماتی تصویر با تنظیمات تکراری
- **رندر متن بهبود یافته**: قابلیت‌های بهبود یافته برای رندر متن در تصاویر (پوسترها، لوگوها) به چندین زبان
- **وضوح بالا**: تولید تصاویر تا وضوح 4K
- **یکپارچگی دسته‌ای**: حفظ بهتر موضوع و چیدمان در تولیدات متعدد
- **تولید سریع**: ۲-۳ ثانیه در هر تصویر
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/images/generations` و `v1/images/edit`

**قیمت‌گذاری:**

| مدل | خروجی |
|-------|--------|
| seedream-5-0-260128 | $35.00/1M توکن (~$0.035 در هر تصویر) |

---

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
