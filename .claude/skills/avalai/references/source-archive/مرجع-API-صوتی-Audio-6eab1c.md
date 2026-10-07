---
hasH1: true
---

# مرجع API صوتی (Audio)

از endpointهای صوتی AvalAI برای رونویسی گفتار، ترجمه گفتار به انگلیسی، تولید صدای گفتاری، یا افزودن ورودی/خروجی صوتی مستقیم به جریان Chat Completions استفاده کنید. AvalAI با SDKهای سازگار با OpenAI کار می‌کند؛ کافی است `base_url` / `baseURL` را روی `https://api.avalai.ir/v1` بگذارید و با `AVALAI_API_KEY` احراز هویت کنید.

راهنماهای مرتبط: [پردازش صوت](fa/guides/audio-processing.md)، [Realtime و صوت زنده](fa/guides/realtime-audio.md)، [تبدیل گفتار به متن](fa/guides/speech-to-text.md)، [تبدیل متن به گفتار](fa/guides/text-to-speech.md)، [Responses در برابر Chat Completions](fa/guides/responses-vs-chat-completions.md)

## انتخاب مسیر صوتی

| هدف | مسیر AvalAI | چه زمانی استفاده شود |
| --- | --- | --- |
| تولید صدای گفتاری از متن | `POST /v1/audio/speech` | متن نهایی آماده است و خروجی فایل صوتی یا پاسخ قابل پخش می‌خواهید. |
| رونویسی یا ترجمه فایل صوتی | `POST /v1/audio/transcriptions`، `POST /v1/audio/translations` | یک فایل صوتی محدود یا upload دارید. |
| ورودی/خروجی صوتی مستقیم در چت | `POST /v1/chat/completions` با مدل صوتی | به `input_audio`، `modalities` یا `message.audio` در همان فراخوانی مدل نیاز دارید. |
| گردش‌کار صوتی Responses-first | `/v1/audio/transcriptions` → `/v1/responses` → `/v1/audio/speech` | می‌خواهید از reasoning، ابزارها، خروجی ساختاریافته یا state در Responses کنار صوت استفاده کنید. |
| مکالمه زنده کم‌تاخیر | [مرجع معماری Realtime](fa/guides/realtime-audio.md) | مستندات Realtime OpenAI برای طراحی معماری مفید است؛ مگر اینکه route زنده برای حساب شما فعال شده باشد، از endpointهای request-based پشتیبانی‌شده AvalAI استفاده کنید. |

> راهنمای فعلی OpenAI بین Audio APIهای request-based و Realtime sessionها تفاوت می‌گذارد. APIهای request-based برای فایل‌ها و تولید گفتار ساده‌ترند؛ Realtime برای رویدادهای صوتی زنده و کم‌تاخیر است. مثال‌های AvalAI در این صفحه روی مسیرهای پشتیبانی‌شده request-based و Chat Completions تمرکز دارند.

## تبدیل متن به گفتار (TTS)

### Endpoint

```http
POST https://api.avalai.ir/v1/audio/speech
```

### بدنه درخواست

| پارامتر | نوع | الزامی | نکته‌ها |
| --- | --- | --- | --- |
| `model` | string | بله | شناسه‌های پشتیبانی‌شده شامل `gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`, `gemini-3.1-flash-tts-preview`, `gpt-4o-mini-tts`، `tts-1`، `tts-1-hd`، `gemini-2.5-pro-tts`، `gemini-2.5-flash-tts`، `gemini-2.5-pro-preview-tts`، `gemini-2.5-flash-preview-tts`، `eleven_v3`، `eleven_multilingual_v2`، `eleven_turbo_v2`، `eleven_turbo_v2_5`، `eleven_flash_v2`، `eleven_flash_v2_5`، `groq.playai-tts` و `groq.playai-tts-arabic` هستند. برای وضعیت فعلی به [جزئیات مدل‌ها](fa/models/model-details.md) مراجعه کنید. |
| `input` | string | بله | متنی که باید به گفتار تبدیل شود. TTS سازگار با OpenAI تا ۴٬۰۹۶ کاراکتر را در هر درخواست می‌پذیرد؛ routeهای provider-specific ممکن است محدودیت متفاوت داشته باشند، پس متن‌های طولانی را بر اساس پاراگراف یا scene تقسیم کنید. |
| `voice` | string or object | بله | صداهای OpenAI شامل `alloy`، `ash`، `ballad`، `coral`، `echo`، `fable`، `nova`، `onyx`، `sage`، `shimmer`، `verse`، `marin` و `cedar` هستند؛ وقتی کیفیت صدا مهم است ابتدا `marin` یا `cedar` را ارزیابی کنید. مدل‌های ارائه‌دهندگان دیگر ممکن است صدای متفاوت داشته باشند. Gemini 3.8 شیء صدای آماده مانند `{"name":"Zephyr","languageCode":"en-US"}` را می‌پذیرد؛ این شیء یک صدای آماده را انتخاب می‌کند و به معنای ساخت یا شبیه‌سازی صدای شخصی نیست. |
| `instructions` | string | خیر | راهنمای سبک و لحن برای مدل‌های سازگار مثل `gpt-4o-mini-tts`؛ همه مدل‌ها آن را پشتیبانی نمی‌کنند و در رفتار مرجع OpenAI برای `tts-1` / `tts-1-hd` پشتیبانی نمی‌شود. |
| `response_format` | string | خیر | پیش‌فرض `mp3` است. فرمت‌های رایج: `mp3`، `opus`، `aac`، `flac`، `wav`، `pcm`. برای پخش کم‌تاخیرتر از `wav` یا `pcm` استفاده کنید.  پیش‌فرض و قالب‌های مجاز به مدل و مسیر بستگی دارد؛ برای ذخیره MP3، مقدار `mp3` را صریح بفرستید. مدل `gemini-3.1-flash-tts-preview` به `pcm` نیاز دارد. |
| `speed` | number | خیر | سرعت پخش، اگر مدل انتخابی پشتیبانی کند. Speech سازگار با OpenAI مقدار `0.25` تا `4.0` را می‌پذیرد و پیش‌فرض `1.0` است. |
| `stream_format` | string | خیر | قالب envelope برای streaming، اگر پشتیبانی شود. مقدارهای سازگار با OpenAI شامل `audio` و `sse` هستند؛ `sse` برای `tts-1` / `tts-1-hd` پشتیبانی نمی‌شود. |

### تولید گفتار پایه

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-4o-mini-tts",
    "voice": "coral",
    "input": "امروز روز خوبی برای ساختن چیزی است که مردم دوستش داشته باشند.",
    "instructions": "با لحنی گرم و مطمئن صحبت کن."
  }' \
  --output avalai_speech.mp3

python=:import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

speech_path = Path("avalai_speech.mp3")

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input="امروز روز خوبی برای ساختن چیزی است که مردم دوستش داشته باشند.",
    instructions="با لحنی گرم و مطمئن صحبت کن.",
) as response:
    response.stream_to_file(speech_path)

print(f"Saved {speech_path}")

javascript=:import fs from "node:fs/promises";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const audio = await client.audio.speech.create({
  model: "gpt-4o-mini-tts",
  voice: "coral",
  input: "امروز روز خوبی برای ساختن چیزی است که مردم دوستش داشته باشند.",
  instructions: "با لحنی گرم و مطمئن صحبت کن.",
});

await fs.writeFile("avalai_speech.mp3", Buffer.from(await audio.arrayBuffer()));

```

### تبدیل متن به گفتار با Gemini 3.8

برای کاربردهای جدید تبدیل متن به گفتار، `gemini-3.8-flash-tts` را برای کیفیت خلاقانه، اجرای احساسی، لهجه‌های منطقه‌ای و ثبات گفت‌وگوهای طولانی انتخاب کنید. برای توان عملیاتی بالا، تأخیر کم و خواندن متن‌های روزمره، `gemini-3.8-flash-lite-tts` مناسب‌تر است. هر دو مدل **متن دریافت می‌کنند و صوت تولید می‌کنند**؛ برای رونویسی، گفت‌وگو با ورودی صوتی، Live API یا استدلال طراحی نشده‌اند.

AvalAI این مدل‌های TTS را فقط از طریق روش‌های بومی `/v1beta/models`، مسیر `/v1/chat/completions` و مسیر `/v1/audio/speech` ارائه می‌دهد. آن‌ها را به `/v1/responses`، `/v1/messages` یا مسیر قدیمی `/v1/text:synthesize` نفرستید. ابتدا پاسخ را با یک مدل گفت‌وگومحور یا استدلالی جداگانه بنویسید و سپس متن نهایی را به TTS بدهید.

```bash
curl --fail-with-body -sS https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "voice": {"name": "Zephyr", "languageCode": "en-US"},
    "input": "Welcome to AvalAI. This voice was generated by AI.",
    "response_format": "mp3"
  }' \
  --output speech.mp3
```

متن انگلیسی نمونه با `languageCode: "en-US"` هماهنگ است. چون خروجی با پسوند MP3 ذخیره می‌شود، `response_format: "mp3"` را صریح تعیین کرده‌ایم. برای توان عملیاتی بالاتر، فقط مقدار `model` را به `gemini-3.8-flash-lite-tts` تغییر دهید. برای کنترل گوینده و سبک در هر نوبت و رمزگشایی خروجی بومی بر اساس نوع MIME، [نمونه TTS بومی](fa/api-reference/v1beta.md#gemini-38-native-text-to-speech) را ببینید.

### نکته‌های TTS

- برای سازگاری با ادغام‌های قدیمی، `tts-1` و `tts-1-hd` را نگه دارید؛ وقتی کنترل سبک غنی‌تر می‌خواهید از `gpt-4o-mini-tts` استفاده کنید.
- فهرست صداها به خانواده مدل وابسته است. `tts-1` و `tts-1-hd` مجموعه voice کوچک‌تری نسبت به `gpt-4o-mini-tts` دارند؛ اگر یک voice خطا داد، از voice مستند همان ارائه‌دهنده استفاده کنید.
- به کاربران نهایی شفاف بگویید صدایی که می‌شنوند با هوش مصنوعی تولید شده است.
- ساخت custom voice در مستندات OpenAI یک قابلیت account-specific/provider-specific است، نه endpoint پیش‌فرض AvalAI. برای هر workflow ارائه‌دهنده که صدا را ضبط یا clone می‌کند، consent record نگه دارید.
- برای متن‌های طولانی، متن را بخش‌بندی کنید و فایل‌های صوتی برگشتی را در برنامه خود به هم بچسبانید.

## تبدیل گفتار به متن: رونویسی

### Endpoint

```http
POST https://api.avalai.ir/v1/audio/transcriptions
```

### بدنه درخواست

| پارامتر | نوع | الزامی | نکته‌ها |
| --- | --- | --- | --- |
| `file` | file | بله | فایل صوتی upload شده. برای مدل‌های رونویسی سازگار با OpenAI، فایل‌ها را حداکثر حدود ۲۵ مگابایت نگه دارید و از فرمت‌هایی مثل `flac`، `mp3`، `mp4`، `mpeg`، `mpga`، `m4a`، `ogg`، `wav` یا `webm` استفاده کنید. برای فایل‌های بزرگ‌تر، آن‌ها را تقسیم یا فشرده کنید. |
| `model` | string | بله | شناسه‌های پشتیبانی‌شده شامل `whisper-1`، `gpt-4o-transcribe`، `gpt-4o-mini-transcribe`، `gpt-4o-transcribe-diarize`، `scribe_v1`، `scribe_v2`، `groq.whisper-large-v3` و `groq.whisper-large-v3-turbo` هستند. |
| `language` | string | خیر | راهنمای اختیاری زبان با قالب ISO-639-1، مثل `en` یا `fa`، اگر مدل پشتیبانی کند. تعیین زبان ورودی می‌تواند دقت و latency را بهتر کند. |
| `prompt` | string | خیر | متن زمینه برای املای درست، واژگان خاص یا سبک. همه مدل‌های رونویسی آن را پشتیبانی نمی‌کنند؛ مدل diarization در OpenAI از `prompt` پشتیبانی نمی‌کند. |
| `response_format` | string | خیر | پیش‌فرض `json` است. `whisper-1` از `json`، `text`، `srt`، `verbose_json` و `vtt` پشتیبانی می‌کند؛ مدل‌های GPT-4o معمولا `json` یا `text` دارند؛ diarization می‌تواند `diarized_json` داشته باشد. |
| `timestamp_granularities[]` | array | خیر | timestamp کلمه یا segment برای مدل‌های سازگار، مخصوصا `whisper-1` همراه با `verbose_json`؛ timestamp کلمه می‌تواند latency اضافه کند و این گزینه برای مدل diarization در OpenAI در دسترس نیست. |
| `stream` | boolean | خیر | eventهای transcript را برای مدل‌های غیر Whisper سازگار stream می‌کند. انتظار `transcript.text.delta` و در پایان `transcript.text.done` داشته باشید؛ در حالت diarization ممکن است `transcript.text.segment` هم دریافت کنید. `whisper-1` در OpenAI از رونویسی stream شده پشتیبانی نمی‌کند. فقط وقتی route زنده برای حساب شما فعال است، سراغ Realtime بروید. |
| `chunking_strategy` | string یا object | خیر | در OpenAI برای diarization ورودی‌های طولانی‌تر از ۳۰ ثانیه لازم است. مگر اینکه تنظیم VAD اختصاصی ارائه‌دهنده نیاز دارید، از `"auto"` استفاده کنید. |
| `include[]` | array | خیر | با `response_format="json"` روی مدل‌های GPT-4o transcription سازگار، از `include[]=logprobs` برای دیدن confidence توکن‌ها استفاده کنید. برای `whisper-1` یا مدل diarization OpenAI پشتیبانی نمی‌شود. |
| `temperature` | number | خیر | دمای نمونه‌گیری از `0` تا `1`، اگر پشتیبانی شود. مقدار کمتر deterministicتر است؛ `0` اجازه می‌دهد سرویس براساس آستانه‌های log probability تنظیم کند. |
| `known_speaker_names[]` / `known_speaker_references[]` | array | خیر | نگاشت اختیاری نام گوینده برای routeهای diarization سازگار. OpenAI تا ۴ گوینده را پشتیبانی می‌کند؛ referenceها باید clipهای ۲ تا ۱۰ ثانیه‌ای و به صورت data URL باشند. |

### رونویسی فایل صوتی

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@meeting.mp3" \
  -F model="gpt-4o-transcribe" \
  -F response_format="text"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("meeting.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=audio_file,
        response_format="text",
        prompt="نام محصول‌ها شامل AvalAI، Qwen، Grok، Claude و Gemini است.",
    )

print(transcript)

javascript=:import fs from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
  model: "gpt-4o-transcribe",
  file: fs.createReadStream("meeting.mp3"),
  response_format: "text",
  prompt: "نام محصول‌ها شامل AvalAI، Qwen، Grok، Claude و Gemini است.",
});

console.log(transcript);

```

### تشخیص گوینده (Diarization)

وقتی به segmentهای دارای برچسب گوینده نیاز دارید، از `gpt-4o-transcribe-diarize` استفاده کنید. `response_format` را `diarized_json` بگذارید و برای فایل‌های طولانی‌تر از ۳۰ ثانیه `chunking_strategy: "auto"` تنظیم کنید. در مستندات فعلی OpenAI این مدل فقط از مسیر `/v1/audio/transcriptions` در دسترس است، نه Realtime.

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@meeting.wav" \
  -F model="gpt-4o-transcribe-diarize" \
  -F response_format="diarized_json" \
  -F chunking_strategy="auto"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("meeting.wav", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-transcribe-diarize",
        file=audio_file,
        response_format="diarized_json",
        chunking_strategy="auto",
    )

for segment in transcript.segments:
    print(segment.speaker, segment.start, segment.end, segment.text)

```

### رویدادهای streaming رونویسی

برای فایل‌های ضبط‌شده، روی مدل‌های GPT-4o transcription سازگار `stream=true` بگذارید تا متن هر بخش به‌محض آماده شدن برسد. این eventها را مدیریت کنید:

- `transcript.text.delta`: متن partial رونویسی. در جریان diarization ممکن است `segment_id` داشته باشد، اما برچسب گوینده بعدا نهایی می‌شود.
- `transcript.text.done`: متن نهایی رونویسی و metadata استفاده.
- `transcript.text.segment`: segment نهایی diarization با `speaker`، `start`، `end` و `text`.

اگر confidence scoring برای QA یا صف بازبینی مهم است، روی مدل‌های GPT-4o transcription سازگار `include[]=logprobs` را همراه `response_format="json"` بفرستید. برای `whisper-1` streaming را فعال نکنید؛ به‌جای آن از chunkهای فایل یا route زنده Realtime استفاده کنید.

## تبدیل گفتار به متن: ترجمه

### Endpoint

```http
POST https://api.avalai.ir/v1/audio/translations
```

endpoint ترجمه، صوت پشتیبانی‌شده را می‌گیرد و متن انگلیسی برمی‌گرداند. مگر اینکه حساب شما مدل ترجمه صوتی دیگری داشته باشد، از `whisper-1` استفاده کنید.

### بدنه درخواست

| پارامتر | نوع | الزامی | نکته‌ها |
| --- | --- | --- | --- |
| `file` | file | بله | فایل صوتی upload شده در فرمت‌هایی مثل `flac`، `mp3`، `mp4`، `mpeg`، `mpga`، `m4a`، `ogg`، `wav` یا `webm`. برای مسیرهای سازگار با OpenAI فایل را حداکثر حدود ۲۵ مگابایت نگه دارید. |
| `model` | string | بله | endpoint ترجمه OpenAI از `whisper-1` پشتیبانی می‌کند؛ فقط وقتی AvalAI برای حساب شما route ترجمه صوتی دیگری فعال کرده باشد از مدل دیگر استفاده کنید. |
| `prompt` | string | خیر | راهنمای زمینه‌ای اختیاری. تا حد ممکن با زبان صوت ورودی هماهنگ باشد. |
| `response_format` | string | خیر | پیش‌فرض `json` است. فرمت‌های رایج سازگار با OpenAI شامل `json`، `text`، `srt`، `verbose_json` و `vtt` هستند. |
| `temperature` | number | خیر | دمای نمونه‌گیری از `0` تا `1`، اگر پشتیبانی شود. مقدار کمتر deterministicتر است. |

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/translations \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F file="@german.mp3" \
  -F model="whisper-1"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("german.mp3", "rb") as audio_file:
    translation = client.audio.translations.create(
        model="whisper-1",
        file=audio_file,
    )

print(translation.text)

```

## صوت در Chat Completions

مدل‌های صوتی مانند `gpt-audio-1.5`، `gpt-audio` و `gpt-audio-mini` از ورودی و/یا خروجی صوتی مستقیم در `/v1/chat/completions` پشتیبانی می‌کنند. وقتی به `message.audio` یا `input_audio` مستقیم نیاز دارید، همین مسیر را نگه دارید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-audio-mini",
    "modalities": ["text", "audio"],
    "audio": { "voice": "alloy", "format": "wav" },
    "messages": [
      { "role": "user", "content": "سیاست بازپرداخت ما را با لحنی دوستانه توضیح بده." }
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
        {"role": "user", "content": "سیاست بازپرداخت ما را با لحنی دوستانه توضیح بده."}
    ],
)

audio_data = completion.choices[0].message.audio.data
with open("reply.wav", "wb") as output:
    output.write(base64.b64decode(audio_data))

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
      { "role": "user", "content": "سیاست بازپرداخت ما را با لحنی دوستانه توضیح بده." }
    ]
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 -D > reply.mp3

afplay reply.mp3
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
      { "role": "user", "content": "سیاست بازپرداخت ما را با لحنی دوستانه توضیح بده." }
    ]
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 --decode >reply.mp3

ffplay -nodisp -autoexit reply.mp3
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
      { "role": "user", "content": "سیاست بازپرداخت ما را با لحنی دوستانه توضیح بده." }
    ]
  }' | ConvertFrom-Json

[IO.File]::WriteAllBytes(
  (Join-Path $PWD "reply.mp3"),
  [Convert]::FromBase64String($response.choices[0].message.audio.data)
)

Start-Process .\reply.mp3
```

این‌ها دستورهای یک‌باره ترمینال هستند و نیازی نیست چیزی به `.zshrc`، `.bashrc` یا پروفایل PowerShell اضافه شود.



<!-- responses-equivalent:start -->
<details>
<summary>مسیر مهاجرت به Responses: متن را رونویسی یا تولید کنید و سپس با `/v1/audio/speech` صدا بسازید.</summary>

Responses API برای گردش‌کارهای جدید متنی، reasoning، ابزارها و state پیشنهاد می‌شود؛ اما وقتی به `input_audio` یا `message.audio` مستقیم نیاز دارید، مسیر صوتی Chat Completions را نگه دارید. برای یک جریان صوتی Responses-first:

1. صوت کاربر را با `/v1/audio/transcriptions` رونویسی کنید.
2. transcript را به `/v1/responses` بفرستید.
3. متن نهایی را از `response.output_text` بخوانید.
4. خروجی گفتاری را با `/v1/audio/speech` بسازید.

```language-selector
python=:import os
from pathlib import Path
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("question.mp3", "rb") as audio_file:
    transcript = client.audio.transcriptions.create(
        model="gpt-4o-transcribe",
        file=audio_file,
        response_format="text",
    )

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="برای یک دستیار پشتیبانی صوتی، واضح و کوتاه پاسخ بده.",
    input=transcript,
)

with client.audio.speech.with_streaming_response.create(
    model="gpt-4o-mini-tts",
    voice="coral",
    input=response.output_text,
) as speech:
    speech.stream_to_file(Path("answer.mp3"))

javascript=:import fs from "node:fs";
import fsp from "node:fs/promises";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = await client.audio.transcriptions.create({
  model: "gpt-4o-transcribe",
  file: fs.createReadStream("question.mp3"),
  response_format: "text",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "برای یک دستیار پشتیبانی صوتی، واضح و کوتاه پاسخ بده.",
  input: transcript,
});

const speech = await client.audio.speech.create({
  model: "gpt-4o-mini-tts",
  voice: "coral",
  input: response.output_text,
});

await fsp.writeFile("answer.mp3", Buffer.from(await speech.arrayBuffer()));

```

</details>
<!-- responses-equivalent:end -->

## مدیریت خطا

| وضعیت | علت رایج | راه‌حل |
| --- | --- | --- |
| `400` | پارامتر پشتیبانی‌نشده برای مدل انتخابی | فیلدهای خاص مدل مثل `instructions`، timestamp، diarization یا audio modalities را حذف یا اصلاح کنید. |
| `401` | API key نامعتبر یا خالی | `AVALAI_API_KEY` را تنظیم کنید و کلیدها را hard-code نکنید. |
| `413` | فایل صوتی بیش از حد بزرگ است | فایل را فشرده، تقسیم یا کوتاه‌تر کنید. |
| `415` | نوع رسانه پشتیبانی نمی‌شود | برای مدل‌های رونویسی سازگار با OpenAI از فرمت‌هایی مثل `flac`، `mp3`، `mp4`، `mpeg`، `mpga`، `m4a`، `ogg`، `wav` یا `webm` استفاده کنید. |
| `429` | عبور از rate limit | با backoff تلاش مجدد کنید و محدودیت tier خود را بررسی کنید. |

## بهترین شیوه‌ها

- برای رونویسی با کیفیت بالاتر از `gpt-4o-transcribe` یا `gpt-4o-mini-transcribe` استفاده کنید؛ `whisper-1` را برای سازگاری گسترده، timestamp و ترجمه نگه دارید.
- فقط وقتی برچسب گوینده نیاز دارید، `gpt-4o-transcribe-diarize` را انتخاب کنید.
- وقتی برای صف بازبینی یا QA به confidence نیاز دارید، روی مدل‌های GPT-4o transcription سازگار از `include[]=logprobs` استفاده کنید.
- برای TTS قابل کنترل، `gpt-4o-mini-tts` را ترجیح دهید؛ `tts-1` و `tts-1-hd` را برای ادغام‌های موجود نگه دارید.
- برای تماس‌های مستقیم صوت-به-صوت یا متن-به-صوت از Chat Completions استفاده کنید.
- برای reasoning روی transcript، ابزارها، خروجی ساختاریافته و state چندمرحله‌ای از Responses استفاده کنید و سپس متن نهایی را به TTS بدهید.
- شناسه مدل، latency، اندازه upload و فرمت پاسخ را برای عیب‌یابی و بررسی هزینه log کنید.
- وقتی تصمیم‌ها و action itemهای downstream به evidence قابل اعتبارسنجی از transcript نیاز دارند، از [تحلیل هوشمند جلسه با تفکیک گوینده](fa/examples/speaker_aware_meeting_intelligence.md) استفاده کنید.
