---
hasH1: true
published: "2026-09-30"
description: "Gemini 3.8 Flash TTS و Flash-Lite TTS در AvalAI در دسترس‌اند. کاربردهای خلاقانه و پرحجم، قیمت تشویقی و نکات مهاجرت صوتی را مقایسه کنید."
---

# مدل‌های Gemini 3.8 Flash و Flash-Lite TTS در دسترس‌اند

**تاریخ:** ۱۴۰۵-۰۷-۰۸ / (2026-09-30)

## خلاصه

Gemini 3.8 Flash TTS و Flash-Lite TTS در AvalAI در دسترس‌اند. برای روایت خلاقانه Flash و برای تولید پرحجم Lite را انتخاب کنید؛ هر دو فارسی دارند. قیمت تشویقی تا ۱۰ دی ۱۴۰۵ برقرار است؛ نکات درخواست ساختاریافته و مهاجرت قالب صوت در ادامه آمده‌اند.

## جزئیات

### انتخاب مدل مناسب تبدیل متن به گفتار Google

| مدل | کاربرد مناسب | زبان‌ها |
| --- | --- | --- |
| [`gemini-3.8-flash-tts`](fa/models/gemini-3.8-flash-tts.md) | روایت خلاقانه، کتاب صوتی، اجرای بیانگر، لهجه‌های منطقه‌ای، گفت‌وگوی پیچیده و حفظ هویت صدا در نوبت‌های طولانی | 130، از جمله فارسی |
| [`gemini-3.8-flash-lite-tts`](fa/models/gemini-3.8-flash-lite-tts.md) | تولید پرحجم، زنجیره پردازش عامل صوتی، خواندن متن با صدا و گفتار روزمره تک‌گوینده | 101، از جمله فارسی |

هر دو مدل **متن می‌گیرند و صوت تولید می‌کنند** و ساختار درخواست بومی یکسانی دارند. توصیف توان عملیاتی و تأخیر Lite، راهنمای ارائه‌دهنده است، نه تضمین عملکرد اندازه‌گیری‌شده در AvalAI. در زنجیره پردازش عامل صوتی، یک مدل جداگانه پاسخ را آماده می‌کند و مدل تبدیل متن به گفتار، متن نهایی را می‌خواند؛ این مدل‌ها برای گفت‌وگو با ورودی صوتی یا استدلال نیستند.

### نقاط پایانی پشتیبانی‌شده در AvalAI

هر دو مدل در AvalAI **فقط** از روش‌های بومی `/v1beta/models`، مسیر `/v1/chat/completions` و مسیر `/v1/audio/speech` پشتیبانی می‌کنند. مثال بومی زیر از `:generateContent` استفاده می‌کند.

Gemini 3.8 TTS را به Responses، Messages، مسیر قدیمی Vertex یعنی `/v1/text:synthesize`، Live یا Interactions نفرستید. نقاط پایانی بالادستی فهرست گسترده صداها، طراحی صدا و بازتولید صدا برای این مدل‌ها در AvalAI ارائه نمی‌شوند؛ مستندات بالادستی Batch، Flex یا Priority نیز به معنای در دسترس بودن آن‌ها در AvalAI نیست. مثال‌ها فقط از صداهای آماده استفاده می‌کنند.

Google سقف **۸٬۱۹۲ توکن ورودی و ۱۶٬۳۸۴ توکن خروجی را به‌عنوان محدودیت سرویس‌دهی Gemini API** اعلام کرده است؛ این اعداد تضمین پنجره زمینه یا سهمیه حساب AvalAI نیستند. برای اطلاعات مرجع مسیریابی، سقف‌های منتشرشده، دسترسی و توان عملیاتی هر سطح حساب، [فهرست مدل‌های AvalAI](fa/models/model-details.md) را ببینید؛ داده‌های آن را با محدودیت‌های بالادستی جایگزین نکنید.

## قیمت‌گذاری

این‌ها **تعرفه AvalAI به دلار آمریکا برای هر ۱ میلیون توکن** هستند. ورودی و ورودی کش‌شده به توکن‌های متن و خروجی به توکن‌های صوت تولیدشده اشاره دارند، نه ثانیه یا تعرفه ثابت هر فایل.

### نرخ تشویقی: از ۸ مهر تا پایان ۱۰ دی ۱۴۰۵ (2026-09-30 تا 2026-12-31)

| مدل | ورودی | ورودی کش‌شده | خروجی صوتی |
| --- | ---: | ---: | ---: |
| `gemini-3.8-flash-tts` | $0.50 | $0.125 | $9.00 |
| `gemini-3.8-flash-lite-tts` | $0.50 | $0.125 | $6.00 |

### نرخ استاندارد: از ۱۱ دی ۱۴۰۵ (2027-01-01)

| مدل | ورودی | ورودی کش‌شده | خروجی صوتی |
| --- | ---: | ---: | ---: |
| `gemini-3.8-flash-tts` | $1.00 | $0.25 | $18.00 |
| `gemini-3.8-flash-lite-tts` | $1.00 | $0.25 | $12.00 |

نرخ فعلی مدل‌ها را در [فهرست قیمت‌گذاری](fa/pricing.md) ببینید. این قیمت‌ها زمان نگهداری حافظه نهان، سطح حساب خاص یا سهمیه توان عملیاتی را مشخص نمی‌کنند.

## فهرست بررسی مهاجرت

۱. برای جایگزینی `gemini-3.1-flash-tts-preview`، Lite را برای توان عملیاتی و Flash را برای کار خلاقانه انتخاب کنید. هنگام مهاجرت از `gemini-2.5-flash-tts`، `gemini-2.5-pro-tts`، `gemini-2.5-flash-preview-tts` یا `gemini-2.5-pro-preview-tts` نیز همین معیار را به کار ببرید. در یکپارچه‌سازی‌های قدیمی Vertex، نقطه پایانی و ساختار درخواست را تغییر دهید، نه فقط شناسه مدل؛ این اعلامیه درخواست‌های موجود را خودکار به مسیر جدید هدایت نمی‌کند.
۲. متن را **رونویسی عین‌به‌عین گفتار** در نظر بگیرید. دستورهای بیان مانند `Say cheerfully:` یا نام گوینده مانند `Speaker 1:` را داخل متن گفتار نگذارید؛ ممکن است خوانده شوند. در درخواست بومی، برای هر بخش متن، شیء `speechMetadata` با نام‌گذاری camelCase و فیلدهای `speaker` و `style` قرار دهید. هر بخش چندگوینده باید نام یکی از گویندگان تنظیم‌شده را داشته باشد. دستورهای مستمر بیان را در `style` بگذارید و برچسب‌هایی مانند `<laugh>`، `<sigh>` و `<short pause>` را به رویدادهای صوتی لحظه‌ای محدود کنید.
۳. پاسخ بومی تک‌درخواستی نسخه ۳.۸ به‌طور پیش‌فرض **WAV با نوع `audio/wav` و هدر RIFF** است، برخلاف PCM بدون هدر در نسخه‌های قدیمی. مقدار `inlineData.mimeType` را بررسی کنید: بایت‌های WAV را مستقیم بنویسید و فقط برای PCM خام هدر بسازید. هدر دوم WAV اضافه نکنید و قالب را از نام فایل حدس نزنید.
۴. Chat Completions از `audio.format` و Speech از `response_format` استفاده می‌کند. مثال Chat صریحاً `pcm16` می‌خواهد و فقط `choices[0].message.audio.data` را رمزگشایی می‌کند. از `message.content` به‌عنوان مسیر جایگزین صوت استفاده نکنید و پیشوند دلخواه از Base64 حذف نکنید.
۵. مدل `gemini-3.1-flash-tts-preview` **فقط PCM16** را پشتیبانی می‌کند. برای درخواست قدیمی Speech، مقدار `response_format: "pcm"` را بفرستید، PCM خام ذخیره کنید و با `ffmpeg -f s16le -ar 24000 -ac 1 -i legacy-speech.pcm legacy-speech.mp3` آن را تبدیل کنید. ذخیره PCM خام با پسوند MP3، آن را به MP3 تبدیل نمی‌کند.

## نمونه درخواست و پاسخ API

متغیر `AVALAI_API_KEY` را در محیط تنظیم کنید. درخواست‌های زیر به‌صورت محلی بررسی شده‌اند و **در API اجرا نشده‌اند**؛ کلید معتبر یا پاسخ زنده API در دسترس نبود. همه پاسخ‌های نمایش‌داده‌شده **نمونه توضیحی (ILLUSTRATIVE) با ساختار حداقلی** هستند، نه پاسخ کامل مشاهده‌شده؛ هیچ تعداد توکن، هزینه یا اندازه‌گیری تأخیری ساخته نشده است.

### Speech: ذخیره MP3 با درخواست صریح قالب

```language-selector
bash=:curl --fail-with-body -sS https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "voice": {"name": "Zephyr", "languageCode": "en-US"},
    "input": "Welcome to AvalAI. This voice was generated by AI.",
    "response_format": "mp3"
  }' \
  --dump-header speech-headers.txt \
  --output speech.mp3

```

متن انگلیسی با `languageCode: "en-US"` هماهنگ است. برای Lite فقط شناسه مدل را به `gemini-3.8-flash-lite-tts` تغییر دهید. پیش از پخش، وضعیت واقعی HTTP و Content-Type را در هدرهای ذخیره‌شده بررسی کنید؛ بدنه درخواست ناموفق، صوت نیست.

**پاسخ توضیحی — ILLUSTRATIVE:** بدنه دودویی MP3 با Content-Type صوتی، نه شیء JSON حاوی Base64. هدرهای واقعی را برای فراداده احتمالی صورتحساب بررسی کنید؛ فرض نکنید پاسخ دودویی دارای فیلدهای JSON مانند `usage` یا `estimated_cost` است.

### مسیر بومی: فراداده گوینده و سبک برای هر بخش

```language-selector
bash=:curl --fail-with-body -sS \
  https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "contents": [{
      "role": "user",
      "parts": [
        {"text": "Welcome to AvalAI.", "speechMetadata": {"speaker": "Host", "style": "Warm and welcoming."}},
        {"text": "Have a wonderful day!", "speechMetadata": {"speaker": "Guest", "style": "Cheerful and relaxed."}}
      ]
    }],
    "generationConfig": {
      "responseModalities": ["AUDIO"],
      "speechConfig": {
        "multiSpeakerVoiceConfig": {
          "speakerVoiceConfigs": [
            {"speaker": "Host", "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Zephyr"}}},
            {"speaker": "Guest", "voiceConfig": {"prebuiltVoiceConfig": {"voiceName": "Puck"}}}
          ]
        }
      }
    }
  }' \
  --output native-speech.json

jq 'walk(if type == "object" and has("inlineData") then .inlineData |= (if has("data") then del(.data) else . end) else . end)' native-speech.json

```

**پاسخ کامل واقعی** را بررسی کنید؛ از جمله همه گزینه‌ها، `usageMetadata` یا `usage` و `estimated_cost` در صورت وجود. دستور نمایش فقط داده صوتی Base64 بخش‌های بومی را حذف می‌کند و همه فیلدهای دیگر را نگه می‌دارد؛ JSON ذخیره‌شده دست‌نخورده می‌ماند.

**ساختار حداقلی توضیحی — ILLUSTRATIVE؛ داده صوتی کوتاه شده و فیلدهای صورتحساب به‌جای ساختن مقادیر حذف شده‌اند:**

```json
{
  "candidates": [
    {
      "content": {
        "role": "model",
        "parts": [
          {
            "inlineData": {
              "mimeType": "audio/wav",
              "data": "[BASE64_AUDIO]"
            }
          }
        ]
      }
    }
  ]
}
```

پاسخ واقعی ذخیره‌شده را رمزگشایی کنید، نه مقدار نمایشی مثال:

```python
import base64
import json
import wave
from pathlib import Path

response = json.loads(Path("native-speech.json").read_text())
parts = response["candidates"][0]["content"]["parts"]
audio_parts = [part["inlineData"] for part in parts if "inlineData" in part]
if not audio_parts:
    raise ValueError("No audio returned; inspect the full response")

for index, audio in enumerate(audio_parts):
    data = base64.b64decode(audio["data"], validate=True)
    mime_type = audio["mimeType"].split(";", 1)[0].strip().lower()
    filename = f"speech-{index}.wav"
    if mime_type == "audio/wav":
        # فایل WAV هدر RIFF دارد؛ دوباره برای آن هدر نسازید.
        Path(filename).write_bytes(data)
    elif mime_type == "audio/l16":
        # قالب PCM16 خام Gemini: تک‌کاناله، 24000 هرتز و دو بایت برای هر نمونه.
        with wave.open(filename, "wb") as output:
            output.setnchannels(1)
            output.setsampwidth(2)
            output.setframerate(24000)
            output.writeframes(data)
    else:
        raise ValueError(f"Unsupported audio MIME type: {audio['mimeType']}")
```

رمزگشا به‌جای حدس‌زدن، نوع MIME ناشناخته را رد می‌کند. اگر پاسخ پارامترهای PCM متفاوتی دارد، رمزگشا را با همان پارامترها هماهنگ کنید و تنظیم تک‌کاناله ۲۴ کیلوهرتز این مثال را تحمیل نکنید.

### Chat Completions: درخواست صریح PCM16 و تبدیل صوت خام

برای کنترل دقیق بیان در هر نوبت، از درخواست بومی بالا استفاده کنید؛ متن این درخواست Chat فقط شامل گفتار است.

```language-selector
bash=:curl --fail-with-body -sS https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-lite-tts",
    "messages": [{"role": "user", "content": "Welcome to AvalAI. This voice was generated by AI."}],
    "modalities": ["text", "audio"],
    "audio": {"voice": "Zephyr", "format": "pcm16"}
  }' \
  --output chat-speech.json

jq 'walk(if type == "object" and has("audio") and (.audio | type) == "object" then .audio |= (if has("data") then del(.data) else . end) else . end)' chat-speech.json

python3 - <<'PY'
import base64
import json
from pathlib import Path

response = json.loads(Path("chat-speech.json").read_text())
data = response["choices"][0]["message"]["audio"]["data"]
Path("chat-speech.pcm").write_bytes(base64.b64decode(data, validate=True))
PY

ffmpeg -f s16le -ar 24000 -ac 1 -i chat-speech.pcm chat-speech.wav

```

JSON کامل واقعی را بررسی کنید؛ از جمله `usage` و `estimated_cost` در صورت بازگردانده‌شدن. دستور نمایش فقط داده صوتی Base64 را حذف می‌کند و فیلدهای صورتحساب و سایر فیلدهای پاسخ را نگه می‌دارد. دستور تبدیل، PCM16 درخواستی را صریحاً صوت خام علامت‌دار ۱۶بیتی با ترتیب بایت little-endian، نرخ ۲۴ کیلوهرتز و یک کانال در نظر می‌گیرد؛ نام فایل به‌تنهایی این پارامترها را به رمزگشا نمی‌دهد.

**ساختار حداقلی توضیحی — ILLUSTRATIVE؛ پاسخ مشاهده‌شده نیست:**

```json
{
  "choices": [
    {
      "message": {
        "role": "assistant",
        "audio": {
          "data": "[BASE64_AUDIO]"
        }
      }
    }
  ]
}
```

## پیوندهای مرتبط

- [مرجع مدل Flash TTS](fa/models/gemini-3.8-flash-tts.md)
- [مرجع مدل Flash-Lite TTS](fa/models/gemini-3.8-flash-lite-tts.md)
- [راهنمای تبدیل متن به گفتار و مهاجرت](fa/guides/text-to-speech.md)
- [API بومی Gemini](fa/api-reference/v1beta.md#gemini-38-native-text-to-speech)
- [قیمت‌گذاری AvalAI](fa/pricing.md)
