# مدل‌های جدید اضافه شدند: مدل‌های تبدیل متن به گفتار Gemini و Mistral Small

**تاریخ:** 1404-03-09 / (2025-05-29)

## خلاصه
از اضافه شدن سه مدل قدرتمند جدید به پلتفرم AvalAI با هدف ارتقای قابلیت‌های پردازش زبان طبیعی و تولید صدای با کیفیت بالا خبر می‌دهیم. این به‌روزرسانی شامل مدل‌های پیشرفته تبدیل متن به گفتار Gemini 2.5 Pro Preview TTS و Gemini 2.5 Flash Preview TTS از شرکت Google، و همچنین مدل جدید mistral-small-2503 از Mistral است. با این بروزرسانی پلتفرم AvalAI قادر است تجربه‌ای بی‌نظیر در زمینه تولید صدای طبیعی و پردازش زبان ارائه دهد.

---

## جزئیات

این به‌روزرسانی چندین مدل پیشرفته هوش مصنوعی را به پلتفرم AvalAI می‌آورد و خدمات ما را در چندین حوزه تقویت می‌کند. موارد جدید عبارتند از:

### گوگل Gemini

* **gemini-2.5-pro-preview-tts**: مدل پیشرفته تبدیل متن به گفتار گوگل با قابلیت‌های تولید صدای با کیفیت بالا، پشتیبانی از خروجی تک گوینده و چند گوینده. [مستندات](fa/models/gemini-2.5-pro-preview-tts.md)
* **gemini-2.5-flash-preview-tts**: نسخه سریع‌تر مدل TTS Gemini، بهینه‌سازی شده برای کاهش تاخیر در عین حفظ کیفیت عالی صدا. [مستندات](fa/models/gemini-2.5-flash-preview-tts.md)

### Mistral AI

* **mistral-small-2503**: جدیدترین مدل زبانی کوچک Mistral که تعادل عالی بین عملکرد و کارایی ارائه می‌دهد. [مستندات](fa/models/mistral-small-2503@001.md)

### ویژگی‌های Gemini TTS

مدل‌های جدید Gemini TTS چندین قابلیت قدرتمند ارائه می‌دهند:

* **صدای تک گوینده و چند گوینده**: تولید صدا با یک صدا یا ایجاد مکالمات بین چندین گوینده
* **کنترل سبک از طریق پرامپت**: کنترل سبک، لحن، لهجه و سرعت با استفاده از پرامپت‌های زبان طبیعی
* **۳۰ گزینه صدا**: انتخاب از میان ۳۰ گزینه صدای متنوع با ویژگی‌های مختلف
* **پشتیبانی از ۲۴ زبان**: تشخیص خودکار زبان با پشتیبانی از ۲۴ زبان
* **پنجره زمینه ۳۲ هزار توکنی**: پردازش متن‌های طولانی‌تر با پنجره زمینه بزرگ
* **پشتیبانی از استریمینگ**: استریم پاسخ‌های صوتی برای تعاملات روان‌تر

## مثال‌های استفاده

### تبدیل متن به گفتار تک گوینده با Gemini

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "gemini-2.5-flash-preview-tts",
 "messages": [{
 "role": "user",
 "content": "روز بسیار خوبی داشته باشید!"
 }],
 "modalities": ["audio"],
 "audio": {
 "voice": "Kore",
 "format": "pcm16"
 }
}'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-2.5-flash-preview-tts",
    messages=[{"role": "user", "content": "روز بسیار خوبی داشته باشید!"}],
    modalities=["audio"],  # الزامی برای مدل‌های TTS
    audio={"voice": "Kore", "format": "pcm16"},  # الزامی: باید "pcm16" باشد
)

# تبدیل پاسخ به دیکشنری
response_dict = response.model_dump()
audio_data_base64 = response_dict["choices"][0]["message"]["audio"]["data"]
# رمزگشایی داده‌های صوتی base64 به داده‌های باینری
audio_data = base64.b64decode(audio_data_base64)

# ذخیره صدا در یک فایل
with open("output.wav", "wb") as file:
    file.write(audio_data)

javascript=:import { OpenAI } from "openai";
import * as fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-2.5-flash-preview-tts",
  messages: [
    {
      role: "user",
      content: "با لحن شاد بگو: روز بسیار خوبی داشته باشید!",
    },
  ],
  modalities: ["audio"], // الزامی برای مدل‌های TTS
  audio: {
    voice: "Kore",
    format: "pcm16", // الزامی: باید "pcm16" باشد
  },
});

// استخراج داده‌های صوتی از پاسخ
const responseObj = response.toJSON();
const audioDataBase64 = responseObj.choices[0].message.audio.data;
const buffer = Buffer.from(audioDataBase64, "base64");
await fs.promises.writeFile("output.wav", buffer);

```

### تبدیل متن به گفتار چند گوینده با Gemini

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "gemini-2.5-pro-preview-tts",
 "messages": [{
 "role": "user",
 "content": "مکالمه زیر را بین Joe و Jane تبدیل به TTS کن:\nJoe: چه خبر؟\nJane: بد نیستم، تو چطوری؟"
 }],
 "modalities": ["audio"],
 "audio": {
 "voice": "Kore",
 "format": "pcm16"
 }
}'

python=:from openai import OpenAI
import base64

# توجه: قابلیت چند گوینده هنوز در دسترس نیست
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-2.5-pro-preview-tts",
    messages=[
        {
            "role": "user",
            "content": "مکالمه زیر را بین Joe و Jane تبدیل به TTS کن:\nJoe: چه خبر؟\nJane: بد نیستم، تو چطوری؟",
        }
    ],
    modalities=["audio"],  # الزامی برای مدل‌های TTS
    audio={"voice": "Kore", "format": "pcm16"},  # الزامی: باید "pcm16" باشد
    # در آینده، پشتیبانی چند گوینده اضافه خواهد شد
)

# تبدیل پاسخ به دیکشنری
response_dict = response.model_dump()
audio_data_base64 = response_dict["choices"][0]["message"]["audio"]["data"]
# رمزگشایی داده‌های صوتی base64 به داده‌های باینری
audio_data = base64.b64decode(audio_data_base64)

# ذخیره صدا در یک فایل
with open("conversation.wav", "wb") as file:
    file.write(audio_data)

javascript=:import { OpenAI } from "openai";
import * as fs from "fs";

// توجه: قابلیت چند گوینده هنوز در دسترس نیست
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-2.5-pro-preview-tts",
  messages: [
    {
      role: "user",
      content:
        "مکالمه زیر را بین Joe و Jane تبدیل به TTS کن:\nJoe: چه خبر؟\nJane: بد نیستم، تو چطوری؟",
    },
  ],
  modalities: ["audio"], // الزامی برای مدل‌های TTS
  audio: {
    voice: "Kore",
    format: "pcm16", // الزامی: باید "pcm16" باشد
  },
  // در آینده، پشتیبانی چند گوینده اضافه خواهد شد
});

// استخراج داده‌های صوتی از پاسخ
const responseObj = response.toJSON();
const audioDataBase64 = responseObj.choices[0].message.audio.data;
const buffer = Buffer.from(audioDataBase64, "base64");
await fs.promises.writeFile("conversation.wav", buffer);

```

### استفاده از مدل Mistral Small

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="mistral-small-2503@001",
    messages=[
        {
            "role": "user",
            "content": "مفهوم شبکه‌های عصبی را به زبان ساده توضیح دهید.",
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "mistral-small-2503@001",
  messages: [
    {
      role: "user",
      content: "مفهوم شبکه‌های عصبی را به زبان ساده توضیح دهید.",
    },
  ],
});

console.log(completion.choices[0].message.content);

```

### کنترل سبک گفتار با پرامپت‌ها

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "gemini-2.5-pro-preview-tts",
 "messages": [{
 "role": "user",
 "content": "با لحن ترسناک و آهسته بگو: در تاریکی شب، سایه‌ها به حرکت در می‌آیند..."
 }],
 "modalities": ["audio"],
 "audio": {
 "voice": "Enceladus",
 "format": "pcm16"
 }
}'

python=:from openai import OpenAI
import base64

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gemini-2.5-pro-preview-tts",
    messages=[
        {
            "role": "user",
            "content": "با لحن ترسناک و آهسته بگو: در تاریکی شب، سایه‌ها به حرکت در می‌آیند...",
        }
    ],
    modalities=["audio"],  # الزامی برای مدل‌های TTS
    audio={"voice": "Enceladus", "format": "pcm16"},  # الزامی: باید "pcm16" باشد
)

# تبدیل پاسخ به دیکشنری
response_dict = response.model_dump()
audio_data_base64 = response_dict["choices"][0]["message"]["audio"]["data"]
# رمزگشایی داده‌های صوتی base64 به داده‌های باینری
audio_data = base64.b64decode(audio_data_base64)

# ذخیره صدا در یک فایل
with open("spooky.wav", "wb") as file:
    file.write(audio_data)

javascript=:import { OpenAI } from "openai";
import * as fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-2.5-pro-preview-tts",
  messages: [
    {
      role: "user",
      content:
        "با لحن ترسناک و آهسته بگو: در تاریکی شب، سایه‌ها به حرکت در می‌آیند...",
    },
  ],
  modalities: ["audio"], // الزامی برای مدل‌های TTS
  audio: {
    voice: "Enceladus",
    format: "pcm16", // الزامی: باید "pcm16" باشد
  },
});

// استخراج داده‌های صوتی از پاسخ
const responseObj = response.toJSON();
const audioDataBase64 = responseObj.choices[0].message.audio.data;
const buffer = Buffer.from(audioDataBase64, "base64");
await fs.promises.writeFile("spooky.wav", buffer);

```

---

## لینک‌های مرتبط

- [راهنمای تبدیل متن به گفتار](fa/guides/text-to-speech.md)
- [راهنمای پردازش صوتی](fa/guides/audio-processing.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [مرجع API](fa/api-reference/audio.md)