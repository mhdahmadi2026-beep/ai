# groq

groq استنتاج فوق‌سریع برای مدل‌های هوش مصنوعی متن‌باز را از طریق معماری سخت‌افزاری تخصصی خود فراهم می‌کند. تمام مدل‌ها از طریق API یکپارچه AvalAI با عملکرد پیشرو و قیمت‌گذاری رقابتی در دسترس هستند.

## مدل‌های موجود

- [ایمنی و تعدیل محتوا](#مدلهای-ایمنی-و-تعدیل-محتوا)
  - [groq.llama-guard-4-12b](#groqllama-guard-4-12b) - تعدیل محتوای پیشرفته
  - [groq.llama-prompt-guard-2-22m](#groqllama-prompt-guard-2-22m) - تشخیص سبک تزریق پرامپت
  - [groq.llama-prompt-guard-2-86m](#groqllama-prompt-guard-2-86m) - تشخیص پیشرفته تزریق پرامپت
  
- [مدل‌های زبان بزرگ](#مدلهای-زبان-بزرگ)
  - [groq.llama-4-maverick-17b-128e-instruct](#groqllama-4-maverick-17b-128e-instruct) - Llama 4 پیشرفته با 128 متخصص
  - [groq.llama-4-scout-17b-16e-instruct](#groqllama-4-scout-17b-16e-instruct) - Llama 4 کارآمد با 16 متخصص
  - [groq.kimi-k2-instruct-0905](#groqkimi-k2-instruct-0905) - دنبال‌کننده دستورالعمل Kimi K2
  - [groq.gpt-oss-120b](#groqgpt-oss-120b) - GPT متن‌باز بزرگ (120B)
  - [groq.gpt-oss-20b](#groqgpt-oss-20b) - GPT متن‌باز کارآمد (20B)
  - [groq.gpt-oss-safeguard-20b](#groqgpt-oss-safeguard-20b) - GPT با ایمنی بهبودیافته (20B)
  - [groq.qwen3-32b](#groqqwen3-32b) - Qwen 3 چندزبانه (32B)

- [مدل‌های صوتی](#مدلهای-صوتی)
  - [groq.playai-tts](#groqplayai-tts) - تبدیل متن به گفتار با کیفیت بالا
  - [groq.playai-tts-arabic](#groqplayai-tts-arabic) - TTS بهینه‌شده برای عربی
  - [groq.whisper-large-v3](#groqwhisper-large-v3) - تشخیص گفتار پیشرفته
  - [groq.whisper-large-v3-turbo](#groqwhisper-large-v3-turbo) - تشخیص گفتار سریع‌تر

## ویژگی‌های کلیدی

- **استنتاج فوق‌سریع**: سرعت استنتاج پیشرو در صنعت که توسط سخت‌افزار سفارشی LPU™ (واحد پردازش زبان) groq پشتیبانی می‌شود
- **مدل‌های متن‌باز**: دسترسی به مدل‌های محبوب متن‌باز با عملکرد آماده برای تولید
- **قیمت‌گذاری رقابتی**: گزینه‌های مقرون‌به‌صرفه با پشتیبانی از کش پرامپت برای صرفه‌جویی بیشتر
- **قابلیت‌های متنوع**: از تعدیل ایمنی تا تولید متن چندزبانه و پردازش صوتی
- **آماده برای تولید**: قابلیت اطمینان و عملکرد سطح سازمانی

## پشتیبانی از نقطه پایانی API

| دسته مدل | v1/chat/completions | v1/audio/speech | v1/audio/transcriptions |
|----------|---------------------|-----------------|-------------------------|
| LLM و ایمنی | ✅ کامل | ❌ | ❌ |
| مدل‌های TTS | ❌ | ✅ کامل | ❌ |
| مدل‌های Whisper | ❌ | ❌ | ✅ کامل |

---

## مدل‌های ایمنی و تعدیل محتوا

### groq.llama-guard-4-12b

مدل تعدیل محتوای پیشرفته مبتنی بر Llama Guard 4 با 12 میلیارد پارامتر.

**قیمت‌گذاری:** 0.20 دلار/1م توکن ورودی، 0.10 دلار/1م ورودی کش‌شده، 0.20 دلار/1م توکن خروجی

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.llama-guard-4-12b",
    "messages": [
      {
        "role": "user",
        "content": "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]"
      }
    ]
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="groq.llama-guard-4-12b",
    messages=[
        {
            "role": "user",
            "content": "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "groq.llama-guard-4-12b",
  messages: [
    {
      role: "user",
      content: "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
    },
  ],
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `groq.llama-guard-4-12b` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
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
  instructions: "You are a helpful assistant.",
  input: "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
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
    "input": "بررسی کن که آیا این محتوا ایمن است: [محتوا برای تعدیل]",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### groq.llama-prompt-guard-2-22m

مدل سبک تشخیص تزریق پرامپت با 22 میلیون پارامتر.

**قیمت‌گذاری:** 0.03 دلار/1م توکن ورودی، 0.015 دلار/1م ورودی کش‌شده، 0.03 دلار/1م توکن خروجی

### groq.llama-prompt-guard-2-86m

مدل تشخیص پیشرفته تزریق پرامپت با 86 میلیون پارامتر.

**قیمت‌گذاری:** 0.04 دلار/1م توکن ورودی، 0.02 دلار/1م ورودی کش‌شده، 0.04 دلار/1م توکن خروجی

---

## مدل‌های زبان بزرگ

### groq.llama-4-maverick-17b-128e-instruct

مدل Llama 4 پیشرفته با 17 میلیارد پارامتر و 128 متخصص، بهینه‌شده برای استدلال پیچیده و دنبال کردن دستورالعمل‌ها.

**قیمت‌گذاری:** 0.20 دلار/1م توکن ورودی، 0.10 دلار/1م ورودی کش‌شده، 0.60 دلار/1م توکن خروجی

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.llama-4-maverick-17b-128e-instruct",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع Python برای محاسبه اعداد اول بنویس."
      }
    ]
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="groq.llama-4-maverick-17b-128e-instruct",
    messages=[
        {
            "role": "user",
            "content": "یک تابع Python برای محاسبه اعداد اول بنویس.",
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "groq.llama-4-maverick-17b-128e-instruct",
  messages: [
    {
      role: "user",
      content: "یک تابع Python برای محاسبه اعداد اول بنویس.",
    },
  ],
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `groq.llama-4-maverick-17b-128e-instruct` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع Python برای محاسبه اعداد اول بنویس.",
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
  instructions: "You are a helpful assistant.",
  input: "یک تابع Python برای محاسبه اعداد اول بنویس.",
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
    "input": "یک تابع Python برای محاسبه اعداد اول بنویس.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### groq.llama-4-scout-17b-16e-instruct

مدل Llama 4 کارآمد با 17 میلیارد پارامتر و 16 متخصص.

**قیمت‌گذاری:** 0.11 دلار/1م توکن ورودی، 0.055 دلار/1م ورودی کش‌شده، 0.34 دلار/1م توکن خروجی

### groq.kimi-k2-instruct-0905

مدل دنبال‌کننده دستورالعمل Kimi K2 بهینه‌شده برای دنبال کردن دستورالعمل‌های پیچیده.

**قیمت‌گذاری:** 1.00 دلار/1م توکن ورودی، 0.50 دلار/1م ورودی کش‌شده، 0.34 دلار/1م توکن خروجی

### groq.gpt-oss-120b

مدل GPT متن‌باز بزرگ با 120 میلیارد پارامتر.

**قیمت‌گذاری:** 0.15 دلار/1م توکن ورودی، 0.075 دلار/1م ورودی کش‌شده، 0.75 دلار/1م توکن خروجی

### groq.gpt-oss-20b

مدل GPT متن‌باز کارآمد با 20 میلیارد پارامتر.

**قیمت‌گذاری:** 0.075 دلار/1م توکن ورودی، 0.0375 دلار/1م ورودی کش‌شده، 0.30 دلار/1م توکن خروجی

### groq.gpt-oss-safeguard-20b

مدل GPT با ایمنی بهبودیافته با 20 میلیارد پارامتر و فیلتر محتوای داخلی.

**قیمت‌گذاری:** 0.075 دلار/1م توکن ورودی، 0.0375 دلار/1م ورودی کش‌شده، 0.30 دلار/1م توکن خروجی

### groq.qwen3-32b

مدل چندزبانه Qwen 3 با 32 میلیارد پارامتر، بهینه‌شده برای زبان‌های متعدد.

**قیمت‌گذاری:** 0.29 دلار/1م توکن ورودی، 0.145 دلار/1م ورودی کش‌شده، 0.59 دلار/1م توکن خروجی

---

## مدل‌های صوتی

### groq.playai-tts

سنتز گفتار با کیفیت بالا با صداهای طبیعی.

**قیمت‌گذاری:** 50.00 دلار/1م توکن ورودی پایه + 0.00005 دلار به ازای هر کاراکتر

**صداهای پشتیبانی شده:** Aaliyah-PlayAI, Adelaide-PlayAI, Angelo-PlayAI, Arista-PlayAI, Atlas-PlayAI, Basil-PlayAI, Briggs-PlayAI, Calum-PlayAI, Celeste-PlayAI, Cheyenne-PlayAI, Chip-PlayAI, Cillian-PlayAI, Deedee-PlayAI, Eleanor-PlayAI, Fritz-PlayAI, Gail-PlayAI, Indigo-PlayAI, Jennifer-PlayAI, Judy-PlayAI, Mamaw-PlayAI, Mason-PlayAI, Mikail-PlayAI, Mitch-PlayAI, Nia-PlayAI, Quinn-PlayAI, Ruby-PlayAI, Thunder-PlayAI

```bash
curl https://api.avalai.ir/v1/audio/speech \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "groq.playai-tts",
    "input": "سلام، این یک آزمایش از سیستم تبدیل متن به گفتار PlayAI است.",
    "voice": "Aaliyah-PlayAI"
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.audio.speech.create(
    model="groq.playai-tts",
    voice="Aaliyah-PlayAI",
    input="سلام، این یک آزمایش از سیستم تبدیل متن به گفتار PlayAI است.",
)

response.stream_to_file("output.mp3")

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const mp3 = await client.audio.speech.create({
  model: "groq.playai-tts",
  voice: "Aaliyah-PlayAI",
  input: "سلام، این یک آزمایش از سیستم تبدیل متن به گفتار PlayAI است.",
});

const buffer = Buffer.from(await mp3.arrayBuffer());
await fs.promises.writeFile("output.mp3", buffer);

```


### groq.playai-tts-arabic

سنتز گفتار بهینه‌شده برای زبان عربی.

**قیمت‌گذاری:** 50.00 دلار/1م توکن ورودی پایه + 0.00005 دلار به ازای هر کاراکتر

**صداهای پشتیبانی شده:** مشابه groq.playai-tts

### groq.whisper-large-v3

مدل تشخیص گفتار پیشرفته مبتنی بر Whisper Large v3 از OpenAI.

**قیمت‌گذاری:** 0.000031 دلار به ازای هر ثانیه صدا (0.00185 دلار به ازای هر دقیقه)

```bash
curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F file="@audio.mp3" \
  -F model="groq.whisper-large-v3"

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

with open("audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="groq.whisper-large-v3",
        file=audio_file,
    )

print(transcript.text)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
  model: "groq.whisper-large-v3",
  file: fs.createReadStream("audio.mp3"),
});

console.log(transcript.text);

```


### groq.whisper-large-v3-turbo

تشخیص گفتار سریع‌تر با حفظ دقت.

**قیمت‌گذاری:** 0.00001111 دلار به ازای هر ثانیه صدا (0.000067 دلار به ازای هر دقیقه)

---

## منابع مرتبط

- [اخبار پشتیبانی از ارائه‌دهنده groq](fa/news/2025-11-20-gemini-3-pro-image-groq-provider-added.md)
- [قیمت‌گذاری API](fa/pricing.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [راهنمای پردازش صوتی](fa/guides/audio-processing.md)
