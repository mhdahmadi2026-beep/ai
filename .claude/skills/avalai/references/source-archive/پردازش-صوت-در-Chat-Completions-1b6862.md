---
hasH1: true
---

# پردازش صوت در Chat Completions

این مثال نشان می‌دهد چگونه از endpoint سازگار با OpenAI یعنی `/v1/chat/completions` در AvalAI همراه با مدل‌های صوتی استفاده کنید. وقتی مدل باید `input_audio` بپذیرد یا `message.audio` را مستقیم برگرداند، Chat Completions را نگه دارید. وقتی به reasoning روی transcript، ابزارها، خروجی ساختاریافته یا state قبل از تولید گفتار نیاز دارید، از مسیر مهاجرت Responses استفاده کنید.

مستندات مرتبط: [API صوتی](fa/api-reference/audio.md)، [راهنمای پردازش صوت](fa/guides/audio-processing.md)، [Responses در برابر Chat Completions](fa/guides/responses-vs-chat-completions.md)

## مدل‌های صوتی Chat

| مدل | مناسب برای |
| --- | --- |
| `gpt-audio-1.5` | گفت‌وگوهای صوتی با کیفیت بالاتر و زمینه طولانی‌تر. |
| `gpt-audio` | گردش‌کارهای متعادل با ورودی/خروجی صوتی. |
| `gpt-audio-mini` | توسعه کم‌هزینه، ربات‌های پشتیبانی و قابلیت‌های صوتی پرترافیک. |

قبل از استقرار، [جزئیات مدل‌ها](fa/models/model-details.md) را بررسی کنید؛ چون دسترسی endpoint می‌تواند به tier حساب و route ارائه‌دهنده وابسته باشد.

## الگوی ۱: تولید پاسخ گفتاری از متن

وقتی کاربر متن می‌فرستد و می‌خواهید مدل هم متن و هم صدا برگرداند، از این الگو استفاده کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-audio-mini",
    "modalities": ["text", "audio"],
    "audio": { "voice": "alloy", "format": "wav" },
    "messages": [
      {
        "role": "system",
        "content": "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار."
      },
      {
        "role": "user",
        "content": "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند."
      }
    ]
  }'

python=:import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

completion = client.chat.completions.create(
    model="gpt-audio-mini",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "wav"},
    messages=[
        {
            "role": "system",
            "content": "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار.",
        },
        {
            "role": "user",
            "content": "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند.",
        },
    ],
)

message = completion.choices[0].message
print(message.content)

if message.audio:
    with open("answer.wav", "wb") as output:
        output.write(base64.b64decode(message.audio.data))

javascript=:import fs from "node:fs/promises";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "gpt-audio-mini",
  modalities: ["text", "audio"],
  audio: { voice: "alloy", format: "wav" },
  messages: [
    {
      role: "system",
      content: "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار.",
    },
    {
      role: "user",
      content: "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند.",
    },
  ],
});

const message = completion.choices[0].message;
console.log(message.content);

if (message.audio?.data) {
  await fs.writeFile("answer.wav", Buffer.from(message.audio.data, "base64"));
}

```

صدای بازگشتی به‌صورت Base64 در مسیر `choices[0].message.audio.data` قرار می‌گیرد. برای تبدیل آن به یک فایل قابل پخش مستقیم از ترمینال (به `jq` نیاز دارد)، خروجی `mp3` بخواهید و یک دستور یک‌باره اجرا کنید:

```zsh
# macOS (zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-mini",
    "modalities": ["text", "audio"],
    "audio": { "voice": "alloy", "format": "mp3" },
    "messages": [
      {
        "role": "system",
        "content": "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار."
      },
      {
        "role": "user",
        "content": "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند."
      }
    ]
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 -D > answer.mp3

afplay answer.mp3
```

```bash
# لینوکس (bash/zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio-mini",
    "modalities": ["text", "audio"],
    "audio": { "voice": "alloy", "format": "mp3" },
    "messages": [
      {
        "role": "system",
        "content": "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار."
      },
      {
        "role": "user",
        "content": "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند."
      }
    ]
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 --decode >answer.mp3

ffplay -nodisp -autoexit answer.mp3
```

```powershell
# ویندوز (PowerShell)
$response = curl.exe -sS "https://api.avalai.ir/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:AVALAI_API_KEY" `
  -d '{
    "model": "gpt-audio-mini",
    "modalities": ["text", "audio"],
    "audio": { "voice": "alloy", "format": "mp3" },
    "messages": [
      {
        "role": "system",
        "content": "تو یک دستیار صوتی دوستانه هستی. پاسخ‌ها را کوتاه نگه دار."
      },
      {
        "role": "user",
        "content": "در یک پاراگراف توضیح بده صورت‌حساب AvalAI چگونه کار می‌کند."
      }
    ]
  }' | ConvertFrom-Json

[IO.File]::WriteAllBytes(
  (Join-Path $PWD "answer.mp3"),
  [Convert]::FromBase64String($response.choices[0].message.audio.data)
)

Start-Process .\answer.mp3
```

این‌ها دستورهای یک‌باره ترمینال هستند و نیازی نیست چیزی به `.zshrc`، `.bashrc` یا پروفایل PowerShell اضافه شود.



### تبدیل متن به گفتار با Gemini 3.8

برای کاربردهای جدید تبدیل متن به گفتار، `gemini-3.8-flash-tts` را برای کیفیت خلاقانه، اجرای احساسی، لهجه‌های منطقه‌ای و ثبات گفت‌وگوهای طولانی انتخاب کنید. برای توان عملیاتی بالا، تأخیر کم و خواندن متن‌های روزمره، `gemini-3.8-flash-lite-tts` مناسب‌تر است. هر دو مدل **متن دریافت می‌کنند و صوت تولید می‌کنند**؛ برای رونویسی، گفت‌وگو با ورودی صوتی، Live API یا استدلال طراحی نشده‌اند.

AvalAI این مدل‌های TTS را فقط از طریق روش‌های بومی `/v1beta/models`، مسیر `/v1/chat/completions` و مسیر `/v1/audio/speech` ارائه می‌دهد. آن‌ها را به `/v1/responses`، `/v1/messages` یا مسیر قدیمی `/v1/text:synthesize` نفرستید. ابتدا پاسخ را با یک مدل گفت‌وگومحور یا استدلالی جداگانه بنویسید و سپس متن نهایی را به TTS بدهید.

```bash
curl --fail-with-body -sS https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "messages": [{"role": "user", "content": "Have a wonderful day!"}],
    "modalities": ["audio"],
    "audio": {"voice": "Zephyr", "format": "pcm16"}
  }' \
  --output chat-speech.json

python3 - <<'PYTHON'
import base64
import json
from pathlib import Path

response = json.loads(Path("chat-speech.json").read_text())
data = response["choices"][0]["message"]["audio"]["data"]
Path("speech.pcm").write_bytes(base64.b64decode(data, validate=True))
PYTHON

ffmpeg -f s16le -ar 24000 -ac 1 -i speech.pcm speech.wav
```

این درخواست متن داده‌شده را می‌خواند؛ به پرسش پاسخ نمی‌دهد و ورودی صوتی نمی‌پذیرد. در Chat، داده Base64 در `choices[0].message.audio.data` قرار دارد، نه `message.content`. خروجی درخواستی `pcm16`، صوت PCM علامت‌دار ۱۶ بیتی با ترتیب little-endian، نرخ ۲۴٬۰۰۰ هرتز و یک کانال است و هدر ندارد؛ آن را در فایل خام ذخیره و با پارامترهای ورودی صریح تبدیل کنید. از `.content` به‌عنوان مسیر جایگزین استفاده نکنید و عبارت `DEPRECATED` را از Base64 حذف نکنید. پاسخ بومی غیرجریانی ۳٫۸ به‌طور پیش‌فرض WAV است؛ پیش از افزودن هدر، `mimeType` را بررسی کنید. برای `speechMetadata` هر بخش بومی و مهاجرت از `gemini-3.1-flash-tts-preview` / `gemini-2.5-flash-tts` / `gemini-2.5-pro-tts`، [راهنمای تبدیل متن به گفتار](fa/guides/text-to-speech.md#migrate-to-gemini-38-tts) را ببینید.

## الگوی ۲: ارسال ورودی صوتی به مدل

وقتی مدل باید مستقیم روی صوت reasoning انجام دهد، از `input_audio` استفاده کنید. فایل صوتی را متناسب با محدودیت مدل و request کوتاه نگه دارید.

```language-selector
python=:import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("customer_question.wav", "rb") as audio_file:
    audio_b64 = base64.b64encode(audio_file.read()).decode("utf-8")

completion = client.chat.completions.create(
    model="gpt-audio-mini",
    modalities=["text", "audio"],
    audio={"voice": "coral", "format": "wav"},
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "مشتری چه سوالی می‌پرسد؟ کوتاه پاسخ بده."},
                {
                    "type": "input_audio",
                    "input_audio": {"data": audio_b64, "format": "wav"},
                },
            ],
        }
    ],
)

print(completion.choices[0].message.content)

javascript=:import fs from "node:fs/promises";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const audioB64 = (await fs.readFile("customer_question.wav")).toString("base64");

const completion = await client.chat.completions.create({
  model: "gpt-audio-mini",
  modalities: ["text", "audio"],
  audio: { voice: "coral", format: "wav" },
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "مشتری چه سوالی می‌پرسد؟ کوتاه پاسخ بده." },
        {
          type: "input_audio",
          input_audio: { data: audioB64, format: "wav" },
        },
      ],
    },
  ],
});

console.log(completion.choices[0].message.content);

```

## الگوی ۳: ادامه گفت‌وگوی صوتی

برای گفت‌وگوهای کوتاه، transcript متنی را در برنامه خود نگه دارید و turnهای قبلی کاربر/دستیار را در `messages` بفرستید. بایت‌های صوتی را جداگانه ذخیره کنید؛ فقط وقتی مدل باید دوباره خود صوت را بررسی کند، صوت را دوباره ارسال کنید.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

messages = [
    {"role": "system", "content": "تو یک دستیار پشتیبانی صوتی و مختصر هستی."},
    {"role": "user", "content": "آیا می‌توانم SDKهای OpenAI را با AvalAI استفاده کنم؟"},
]

first = client.chat.completions.create(
    model="gpt-audio-mini",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "mp3"},
    messages=messages,
)

messages.append({"role": "assistant", "content": first.choices[0].message.content})
messages.append({"role": "user", "content": "base URL را هم نشان بده."})

second = client.chat.completions.create(
    model="gpt-audio-mini",
    modalities=["text", "audio"],
    audio={"voice": "alloy", "format": "mp3"},
    messages=messages,
)

print(second.choices[0].message.content)

```

<!-- responses-equivalent:start -->
<details>
<summary>مسیر مهاجرت به Responses API</summary>

برای صوت مستقیم، `input_audio` و `message.audio` فعلا به Chat Completions تعلق دارند. وقتی workflow از Responses سود می‌برد، آن را به چند مرحله request-based تقسیم کنید:

1. صوت کاربر را با `/v1/audio/transcriptions` به متن تبدیل کنید.
2. transcript را به `/v1/responses` بفرستید.
3. متن نهایی را از `response.output_text` بخوانید.
4. صدا را با `/v1/audio/speech` بسازید.

```language-selector
python=:import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("customer_question.wav", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-transcribe",
        file=audio_file,
        response_format="text",
    )

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="تو یک دستیار پشتیبانی مختصر هستی. برای پخش صوتی پاسخ بده.",
    input=transcript,
)

with client.audio.speech.with_streaming_response.create(
    model="gpt-audio-1.5",
    voice="coral",
    input=response.output_text,
) as speech:
    speech.stream_to_file(Path("response.mp3"))

javascript=:import fs from "node:fs";
import fsp from "node:fs/promises";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
  model: "gpt-transcribe",
  file: fs.createReadStream("customer_question.wav"),
  response_format: "text",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "تو یک دستیار پشتیبانی مختصر هستی. برای پخش صوتی پاسخ بده.",
  input: transcript,
});

const speech = await client.audio.speech.create({
  model: "gpt-audio-1.5",
  voice: "coral",
  input: response.output_text,
});

await fsp.writeFile("response.mp3", Buffer.from(await speech.arrayBuffer()));

```

وقتی به قابلیت‌هایی مثل tool call، structured outputs، `previous_response_id` یا manual Item replay نیاز دارید، از این مسیر مهاجرت استفاده کنید. وقتی خروجی صوتی مستقیم مدل قابلیت اصلی است، Chat Completions را نگه دارید.

</details>
<!-- responses-equivalent:end -->

## نکته‌های فرمت و تأخیر

- وقتی تأخیر پخش مهم است، در Chat Completions از `wav` یا `pcm16` استفاده کنید؛ نام قالب خام در `/v1/audio/speech` برابر `pcm` است.
- برای فایل‌های کم‌حجم و سازگاری گسترده، `mp3` مناسب است.
- هنگام توسعه `gpt-audio-mini` را ترجیح دهید؛ وقتی کیفیت یا context مهم‌تر است به `gpt-audio` یا `gpt-audio-1.5` بروید.
- در گفت‌وگوهای چندمرحله‌ای، همان audio bytes را مدام نفرستید؛ transcript را نگه دارید و فقط وقتی مدل باید دوباره صوت را بررسی کند، صوت را ارسال کنید.
- برای ذخیره‌های طولانی، به جای base64 کردن صوت داخل Chat Completions از `/v1/audio/transcriptions` و chunking استفاده کنید.

## عیب‌یابی

| نشانه | راه‌حل |
| --- | --- |
| پاسخ صوتی برنگشت | `"audio"` را در `modalities` بگذارید و object `audio` را با `voice` و `format` تنظیم کنید. |
| `input_audio` رد شد | مطمئن شوید مدل انتخابی ورودی صوتی را پشتیبانی می‌کند و `format` با بایت‌های encode شده سازگار است. |
| payload خیلی بزرگ است | برای فایل‌ها از `/v1/audio/transcriptions` استفاده کنید، صوت را فشرده کنید یا ذخیره‌های طولانی را تقسیم کنید. |
| مدل صوت قبلی را به یاد نمی‌آورد | transcript متنی را ذخیره و ارسال کنید؛ فرض نکنید صوت خام بین requestها باقی می‌ماند. |
| ابزارها یا خروجی ساختاریافته نیاز دارید | از مسیر مهاجرت Responses استفاده کنید و متن نهایی را با `/v1/audio/speech` به صدا تبدیل کنید. |
