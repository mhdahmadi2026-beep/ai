# News 2025-10-20-advanced-tts-and-transcription-models-added: دسترسی به اطلاعات گوینده از بخش‌ها
URL: `https://docs.avalai.ir/fa/news/2025-10-20-advanced-tts-and-transcription-models-added`
**تاریخ:** 1404-07-28 / (2025-10-20)

# افزودن مدل‌های پیشرفته TTS و رونویسی

**تاریخ:** 1404-07-28 / (2025-10-20)

## خلاصه

ما افزودن قابلیت‌های پیشرفته تبدیل متن به گفتار و رونویسی به پلتفرم AvalAI را اعلام می‌کنیم. مدل‌های [`gemini-2.5-flash-tts`](fa/providers/google.md#gemini-25-flash-tts) و [`gemini-2.5-pro-tts`](fa/providers/google.md#gemini-25-pro-tts) گوگل اکنون از طریق اولین endpoint بومی Vertex AI ما [`v1/text:synthesize`](fa/api-reference/v1-text-synthesize.md) در کنار فرمت‌های سازگار با OpenAI در دسترس هستند. همچنین مدل [`gpt-4o-transcribe-diarize`](fa/providers/openai.md#gpt-4o-transcribe-diarize) OpenAI قابلیت‌های بهبود یافته رونویسی با شناسایی گوینده را ارائه می‌دهد.


## نمونه‌های درخواست/پاسخ API

### Gemini TTS از طریق Chat Completions

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-2.5-flash-tts",
    "messages": [
      {
        "role": "user",
        "content": "Say hello in a friendly and welcoming way"
      }
    ]
  }'
```

#### نمونه پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1729425000,
  "model": "gemini-2.5-flash-tts",
  "system_fingerprint": null,
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "//NExAASKAKgAQAAAP8A8A8AZ...[محتوای صوتی رمزگذاری شده base64 کوتاه شده]...",

        "thinking_blocks": [],
        "annotations": []
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 96,
    "total_tokens": 108,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": null,
      "text_tokens": 12,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0000966000",
    "irt": 11.08,
    "exchange_rate": 114600
  }
}
```

### Gemini TTS از طریق Audio Speech Endpoint

#### نمونه درخواست

```bash
curl -X POST https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-flash-tts",
    "input": "Hello! Welcome to AvalAI platform.",
    "voice": "alloy"
  }' \
  --output speech.mp3
```

### Gemini TTS از طریق Endpoint بومی Vertex AI

#### نمونه درخواست

```bash
curl -X POST https://api.avalai.ir/v1/text:synthesize \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "text": "Hello, this is a test of the text to speech system."
    },
    "voice": {
      "languageCode": "en-US",
      "name": "Kore",
      "model_name": "gemini-2.5-flash-tts"
    },
    "audioConfig": {
      "audioEncoding": "MP3"
    }
  }' \
  | jq -r '.audioContent' | base64 -d >output.mp3
```

#### نمونه پاسخ

```json
{
  "audioContent": "//NExAASKAKgAQAAAP8A8A...[صدای رمزگذاری شده base64]...",

  "timepoints": [],
  "audioConfig": {
    "audioEncoding": "MP3",
    "sampleRateHertz": 24000
  }
}
```

### GPT-4o رونویسی با شناسایی گوینده

#### نمونه درخواست

```bash
curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F file="@/path/to/audio.mp3" \
  -F model="gpt-4o-transcribe-diarize" \
  -F language="en" \
  -F response_format="verbose_json"
```

#### نمونه پاسخ

```json
{
  "task": "transcribe",
  "language": "english",
  "duration": 45.5,
  "text": "Speaker 1: Hello, welcome to the meeting. Speaker 2: Thank you, glad to be here. Speaker 1: Let's discuss the project timeline.",
  "segments": [
    {
      "id": 0,
      "seek": 0,
      "start": 0.0,
      "end": 2.5,
      "text": "Hello, welcome to the meeting.",
      "speaker": "SPEAKER_1",
      "tokens": [
        1234,
        5678
      ],
      "temperature": 0.0,
      "avg_logprob": -0.25,
      "compression_ratio": 1.2,
      "no_speech_prob": 0.01
    },
    {
      "id": 1,
      "seek": 0,
      "start": 2.5,
      "end": 5.0,
      "text": "Thank you, glad to be here.",
      "speaker": "SPEAKER_2",
      "tokens": [
        9876,
        5432
      ],
      "temperature": 0.0,
      "avg_logprob": -0.22,
      "compression_ratio": 1.1,
      "no_speech_prob": 0.02
    }
  ]
}
```

---

## نمونه‌های استفاده از SDK

### Gemini TTS با OpenAI SDK

```language-selector
bash=:curl -X POST https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-2.5-flash-tts",
    "input": "Hello! This is a test of the text to speech system.",
    "voice": "alloy"
  }' \
  --output speech.mp3

python=:from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AVALAI_API_KEY"), base_url="https://api.avalai.ir/v1"
)

response = client.audio.speech.create(
    model="gemini-2.5-flash-tts",
    voice="alloy",
    input="Hello! This is a test of the text to speech system.",
)

response.stream_to_file("speech.mp3")
print("Audio saved to speech.mp3")

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const response = await client.audio.speech.create({
    model: "gemini-2.5-flash-tts",
    voice: "alloy",
    input: "Hello! This is a test of the text to speech system.",
});

const buffer = Buffer.from(await response.arrayBuffer());
await fs.promises.writeFile("speech.mp3", buffer);
console.log("Audio saved to speech.mp3");

```

### TTS پیشرفته با پرامپت‌های استایل

```language-selector
bash=:curl -X POST https://api.avalai.ir/v1/text:synthesize \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "Say the following in an excited and energetic way",
      "text": "Welcome to the future of AI!"
    },
    "voice": {
      "languageCode": "en-US",
      "name": "Puck",
      "model_name": "gemini-2.5-pro-tts"
    },
    "audioConfig": {
      "audioEncoding": "MP3"
    }
  }' \
  | jq -r '.audioContent' | base64 -d >output.mp3

python=:from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient(
    transport="rest",
    client_options={
        "api_endpoint": "https://api.avalai.ir",
        "api_key": os.getenv("AVALAI_API_KEY"),
    },
)

synthesis_input = texttospeech.SynthesisInput(
    text="Welcome to the future of AI!",
    prompt="Say the following in an excited and energetic way",
)

voice = texttospeech.VoiceSelectionParams(
    language_code="en-US", name="Puck", model_name="gemini-2.5-pro-tts"
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("Audio saved to output.mp3")

javascript=:import fetch from "node-fetch";
import fs from "fs";

const response = await fetch("https://api.avalai.ir/v1/text:synthesize", {
    method: "POST",
    headers: {
        "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
        "Content-Type": "application/json"
    },
    body: JSON.stringify({
        input: {
            prompt: "Say the following in an excited and energetic way",
            text: "Welcome to the future of AI!"
        },
        voice: {
            languageCode: "en-US",
            name: "Puck",
            model_name: "gemini-2.5-pro-tts"
        },
        audioConfig: {
            audioEncoding: "MP3"
        }
    })
});

const data = await response.json();
const audioBuffer = Buffer.from(data.audioContent, "base64");
await fs.promises.writeFile("output.mp3", audioBuffer);
console.log("Audio saved to output.mp3");

```

### GPT-4o رونویسی با شناسایی گوینده

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F file="@/path/to/audio.mp3" \
  -F model="gpt-4o-transcribe-diarize" \
  -F response_format="verbose_json"

python=:from openai import OpenAI
import os

client = OpenAI(
    api_key=os.getenv("AVALAI_API_KEY"), base_url="https://api.avalai.ir/v1"
)

with open("/path/to/audio.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-transcribe-diarize",
        file=audio_file,
        response_format="verbose_json",
    )

# دسترسی به اطلاعات گوینده از بخش‌ها
for segment in transcript.segments:
    print(f"{segment.speaker}: {segment.text}")

javascript=:import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
    file: fs.createReadStream("/path/to/audio.mp3"),
    model: "gpt-4o-transcribe-diarize",
    response_format: "verbose_json",
});

// دسترسی به اطلاعات گوینده از بخش‌ها
transcript.segments.forEach(segment => {
    console.log(`${segment.speaker}: ${segment.text}`);
});

```

---

## موارد استفاده

### برنامه‌های تبدیل متن به گفتار

**تولید محتوا:**
- روایت کتاب‌های صوتی با صداهای چندین شخصیت
- تولید پادکست از محتوای نوشتاری
- محتوای آموزشی با روایت جذاب

**دسترسی‌پذیری:**
- صفحه‌خوان‌ها با صداهای طبیعی
- توضیحات صوتی برای محتوای بصری
- سرویس‌های دسترسی‌پذیری چند زبانه

**سازمانی:**
- سیستم‌های IVR با پاسخ‌های پویا
- اعلان‌ها و هشدارهای صوتی
- پاسخ‌های صوتی خدمات مشتری

### رونویسی با شناسایی گوینده

**تحلیل جلسات:**
- رونویسی خودکار و نسبت دادن مشارکت‌های گوینده
- تولید خلاصه جلسات با زمینه گوینده
- پیگیری مشارکت فردی و زمان صحبت

**خدمات مشتری:**
- تحلیل تعاملات مشتری-نماینده
- تضمین کیفیت با معیارهای خاص گوینده
- نظارت بر انطباق با انتساب دقیق

**تولید محتوا:**
- رونویسی مصاحبه با برچسب‌های گوینده
- پس از تولید و ویرایش پادکست
- تولید زیرنویس برای محتوای چند گوینده

---

## لینک‌های مرتبط

- [مستندات مدل‌های Google](fa/providers/google.md)
- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مرجع API Vertex AI Text:Synthesize](fa/api-reference/v1-text-synthesize.md)
- [مرجع API Audio](fa/api-reference/audio.md)
- [مرجع API Chat Completions](fa/api-reference/chat.md)
- [راهنمای پردازش صوت](fa/guides/audio-processing.md)
- [مستندات Vertex AI](https://cloud.google.com/text-to-speech/docs/gemini-tts)
