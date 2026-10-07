# API سنتز متن - Endpoint بومی Vertex AI

endpoint [`v1/text:synthesize`](fa/api-reference/v1-text-synthesize.md) قابلیت‌های بومی تبدیل متن به گفتار Vertex AI را از طریق پلتفرم AvalAI فراهم می‌کند. این اولین endpoint بومی Vertex AI ما است که دسترسی کامل به ویژگی‌های پیشرفته TTS Google Cloud از جمله سنتز چند گوینده، پیکربندی‌های صدای سفارشی و کنترل دقیق صدا را ارائه می‌دهد.

## نمای کلی

این endpoint تولید تبدیل متن به گفتار با کیفیت بالا را با استفاده از مدل‌های Gemini TTS گوگل ([`gemini-2.5-flash-tts`](fa/providers/google.md#gemini-25-flash-tts) و [`gemini-2.5-pro-tts`](fa/providers/google.md#gemini-25-pro-tts)) با فرمت و ویژگی‌های بومی Vertex AI امکان‌پذیر می‌سازد.

**ویژگی‌های کلیدی:**
- فرمت بومی API Vertex AI
- 30+ صدای طبیعی
- 100+ زبان و لهجه
- پرامپت‌های استایل برای کنترل لحن
- مکالمات چند گوینده
- پشتیبانی از فرمت‌های صوتی متعدد
- کنترل پیشرفته آهنگ

## Endpoint

```
POST https://api.avalai.ir/v1/text:synthesize
```

## احراز هویت

کلید API AvalAI خود را در هدر Authorization قرار دهید:

```bash
Authorization: Bearer YOUR_AVALAI_API_KEY
```

## فرمت درخواست

### درخواست پایه

```json
{
  "input": {
    "text": "سلام، این یک تست سیستم تبدیل متن به گفتار است."
  },
  "voice": {
    "languageCode": "fa-IR",
    "name": "Kore",
    "model_name": "gemini-2.5-flash-tts"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
```

### درخواست با پرامپت استایل

```json
{
  "input": {
    "prompt": "متن زیر را با لحنی هیجان‌زده و پرانرژی بگویید",
    "text": "به آینده هوش مصنوعی خوش آمدید!"
  },
  "voice": {
    "languageCode": "fa-IR",
    "name": "Puck",
    "model_name": "gemini-2.5-pro-tts"
  },
  "audioConfig": {
    "audioEncoding": "MP3"
  }
}
```

### درخواست چند گوینده

```json
{
  "input": {
    "text": "سام: سلام! باب: سلام، حال شما چطور است؟ سام: عالی هستم، ممنون!"
  },
  "voice": {
    "languageCode": "fa-IR",
    "model_name": "gemini-2.5-pro-tts",
    "multiSpeakerVoiceConfig": {
      "speakerVoiceConfigs": [
        {
          "speakerAlias": "سام",
          "speakerId": "Kore"
        },
        {
          "speakerAlias": "باب",
          "speakerId": "Charon"
        }
      ]
    }
  },
  "audioConfig": {
    "audioEncoding": "LINEAR16",
    "sampleRateHertz": 24000
  }
}
```

## پارامترهای درخواست

### input (الزامی)

متن ورودی برای سنتز. می‌تواند شامل پرامپت استایل اختیاری باشد.

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `text` | string | بله | متن برای سنتز (حداکثر ۴۰۰۰ بایت در زمان نگارش) |
| `prompt` | string | خیر | دستورالعمل‌های استایل برای نحوه گفتن متن (حداکثر ۴۰۰۰ بایت در زمان نگارش) |

> **توجه:** حداکثر محدودیت کاراکتر در زمان نگارش این مستندات تقریبا 4,000 بایت است. این محدودیت ممکن است در طول زمان تغییر کند. برای اطلاعات به‌روز در مورد محدودیت‌های کاراکتر و سایر قیدها، لطفا به [مستندات رسمی Google Cloud Text-to-Speech](https://docs.cloud.google.com/text-to-speech/docs/gemini-tts) مراجعه کنید.

### voice (الزامی)

پیکربندی صدا برای سنتز.

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `languageCode` | string | بله | کد زبان BCP-47 (مثلا "en-US"، "fa-IR") |
| `name` | string | خیر | نام صدا (مثلا "Kore"، "Puck"، "Charon") |
| `model_name` | string | بله | مدل مورد استفاده: `gemini-2.5-flash-tts` یا `gemini-2.5-pro-tts` |
| `multiSpeakerVoiceConfig` | object | خیر | پیکربندی برای سنتز چند گوینده |

#### multiSpeakerVoiceConfig

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `speakerVoiceConfigs` | array | بله | آرایه‌ای از پیکربندی‌های گوینده |

هر پیکربندی گوینده شامل:

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `speakerAlias` | string | بله | شناسه گوینده در متن (مثلا "سام"، "باب") |
| `speakerId` | string | بله | نام صدا برای این گوینده |

### audioConfig (الزامی)

پیکربندی خروجی صوتی.

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `audioEncoding` | string | بله | فرمت صدا: `MP3`، `LINEAR16`، `OGG_OPUS`، `MULAW`، `ALAW` |
| `sampleRateHertz` | integer | خیر | نرخ نمونه‌برداری در Hz (۱۶۰۰۰، ۲۴۰۰۰، یا ۴۸۰۰۰ برای LINEAR16) |

## فرمت پاسخ

### پاسخ موفق

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

### فیلدهای پاسخ

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `audioContent` | string | داده صوتی رمزگذاری شده Base64 |
| `timepoints` | array | اطلاعات زمان‌بندی برای کلمات/واج‌ها (در صورت درخواست) |
| `audioConfig` | object | پیکربندی صوتی استفاده شده برای سنتز |

## صداهای موجود

Gemini 2.5 TTS از 30+ صدای با کیفیت بالا پشتیبانی می‌کند. صداهای رایج شامل:

| نام صدا | توضیحات | بهترین برای |
|---------|---------|-------------|
| Kore | خنثی، متعادل | کاربرد عمومی، حرفه‌ای |
| Charon | عمیق، طنین‌انداز | معتبر، روایت |
| Fenrir | کیفیت داستان‌گویی | کتاب‌های صوتی، روایت‌ها |
| Aoede | قوی، معتبر | رهبری، اعلان‌ها |
| Puck | روشن، پرانرژی | محتوای شاد، تبلیغات |
| Zephyr | نرم، حرفه‌ای | تجاری، ارائه‌ها |

## پشتیبانی زبان

این endpoint از 100+ زبان پشتیبانی می‌کند از جمله:

**در دسترس عمومی:**
- انگلیسی (آمریکا، بریتانیا، هند، استرالیا)
- اسپانیایی (اسپانیا، مکزیک، آمریکای لاتین)
- فرانسوی (فرانسه، کانادا)
- آلمانی، ایتالیایی، پرتغالی (برزیل، پرتغال)
- عربی، هندی، ژاپنی، کره‌ای، چینی (ماندارین)
- فارسی (ایران)، ترکی، روسی، اوکراینی
- و خیلی بیشتر...

برای لیست کامل، [Gemini 2.5 Flash TTS](fa/providers/google.md#gemini-25-flash-tts) را ببینید.

## فرمت‌های صوتی

### رمزگذاری‌های پشتیبانی شده

| فرمت | نوع MIME | مورد استفاده | کیفیت |
|------|----------|---------------|--------|
| MP3 | audio/mpeg | کاربرد عمومی، وب | خوب، فایل‌های کوچک |
| LINEAR16 | audio/L16 | کیفیت بالا، ویرایش | بهترین، فایل‌های بزرگ‌تر |
| OGG_OPUS | audio/ogg | استریمینگ، وب | خوب، کارآمد |
| MULAW | audio/basic | تلفنی | پایین‌تر، سازگار |
| ALAW | audio/x-alaw-basic | تلفنی | پایین‌تر، سازگار |

### نرخ نمونه‌برداری

- **MP3/OGG_OPUS**: خودکار (معمولا ۲۴kHz)
- **LINEAR16**: ۱۶۰۰۰، ۲۴۰۰۰، یا ۴۸۰۰۰ Hz (با `sampleRateHertz` مشخص کنید)
- **MULAW/ALAW**: ۸۰۰۰ Hz

## نمونه‌های استفاده

### نمونه‌های cURL

#### سنتز پایه

```bash
curl -X POST https://api.avalai.ir/v1/text:synthesize \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "text": "سلام، این یک تست است."
    },
    "voice": {
      "languageCode": "fa-IR",
      "name": "Kore",
      "model_name": "gemini-2.5-flash-tts"
    },
    "audioConfig": {
      "audioEncoding": "MP3"
    }
  }' \
  | jq -r '.audioContent' | base64 -d >output.mp3
```

#### با پرامپت استایل

```bash
curl -X POST https://api.avalai.ir/v1/text:synthesize \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": {
      "prompt": "متن زیر را با لحنی کنجکاوانه بگویید",
      "text": "خب، پس... درباره این موضوع هوش مصنوعی به من بگویید."
    },
    "voice": {
      "languageCode": "fa-IR",
      "name": "Puck",
      "model_name": "gemini-2.5-pro-tts"
    },
    "audioConfig": {
      "audioEncoding": "LINEAR16",
      "sampleRateHertz": 24000
    }
  }' \
  | jq -r '.audioContent' | base64 -d >output.wav
```

### Python با Google Cloud SDK

```python
from google.cloud import texttospeech
import os

# پیکربندی کلاینت
client = texttospeech.TextToSpeechClient(
    transport="rest",
    client_options={
        "api_endpoint": "https://api.avalai.ir",
        "api_key": os.getenv("AVALAI_API_KEY"),
    },
)

# آماده‌سازی درخواست
synthesis_input = texttospeech.SynthesisInput(
    text="سلام! این یک تست سیستم تبدیل متن به گفتار است."
)

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR", name="Kore", model_name="gemini-2.5-flash-tts"
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

# سنتز گفتار
response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

# ذخیره در فایل
with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
    print("محتوای صوتی در output.mp3 نوشته شد")
```

### Python با پرامپت استایل

```python
from google.cloud import texttospeech
import os

client = texttospeech.TextToSpeechClient(
    transport="rest",
    client_options={
        "api_endpoint": "https://api.avalai.ir",
        "api_key": os.getenv("AVALAI_API_KEY"),
    },
)

synthesis_input = texttospeech.SynthesisInput(
    text="به آینده هوش مصنوعی خوش آمدید!",
    prompt="متن زیر را با لحنی هیجان‌زده و پرانرژی بگویید",
)

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR", name="Puck", model_name="gemini-2.5-pro-tts"
)

audio_config = texttospeech.AudioConfig(audio_encoding=texttospeech.AudioEncoding.MP3)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("output.mp3", "wb") as out:
    out.write(response.audio_content)
```

### مکالمه چند گوینده

```python
synthesis_input = texttospeech.SynthesisInput(
    text="Sam: سلام! Bob: سلام، حال شما چطور است؟ Sam: عالی هستم، ممنون!"
)

voice = texttospeech.VoiceSelectionParams(
    language_code="fa-IR",
    model_name="gemini-2.5-pro-tts",
    multi_speaker_voice_config=texttospeech.MultiSpeakerVoiceConfig(
        speaker_voice_configs=[
            texttospeech.MultispeakerPrebuiltVoice(
                speaker_alias="Sam", speaker_id="Kore"  # must be English
            ),
            texttospeech.MultispeakerPrebuiltVoice(
                speaker_alias="Bob", speaker_id="Charon"  # must be English
            ),
        ]
    ),
)

audio_config = texttospeech.AudioConfig(
    audio_encoding=texttospeech.AudioEncoding.LINEAR16, sample_rate_hertz=24000
)

response = client.synthesize_speech(
    input=synthesis_input, voice=voice, audio_config=audio_config
)

with open("conversation.wav", "wb") as out:
    out.write(response.audio_content)
```

## پاسخ‌های خطا

### خطاهای رایج

| کد وضعیت | خطا | توضیحات |
|---------|-----|---------|
| 400 | Bad Request | فرمت یا پارامترهای درخواست نامعتبر |
| 401 | Unauthorized | کلید API نامعتبر یا وجود ندارد |
| 413 | Request Entity Too Large | متن از محدودیت‌های حجم تجاوز می‌کند |
| 429 | Too Many Requests | محدودیت نرخ فراتر رفته |
| 500 | Internal Server Error | خطای سمت سرور |

### فرمت پاسخ خطا

```json
{
  "error": {
    "code": 400,
    "message": "متن از حداکثر طول ۹۰۰ بایت تجاوز می‌کند",
    "status": "INVALID_
    ARGUMENT"
  }
}
```

## بهترین روش‌ها

### مدیریت طول متن

```python
def split_text(text, max_bytes=900):
    """تقسیم متن به قطعات کمتر از max_bytes."""
    chunks = []
    current = ""
    for word in text.split():
        test = f"{current} {word}".strip()
        if len(test.encode("utf-8")) <= max_bytes:
            current = test
        else:
            chunks.append(current)
            current = word
    if current:
        chunks.append(current)
    return chunks


# استفاده برای متن طولانی
long_text = "متن بسیار طولانی شما اینجا..."
chunks = split_text(long_text)
for i, chunk in enumerate(chunks):
    # سنتز هر قطعه
    pass
```

### تطبیق زبان

همیشه اطمینان حاصل کنید که `languageCode` با زبان متن شما مطابقت دارد:

```python
# برای انگلیسی
voice = {"name": "Kore", "languageCode": "en-US"}

# برای فارسی
voice = {"name": "Kore", "languageCode": "fa-IR"}

# برای اسپانیایی
voice = {"name": "Kore", "languageCode": "es-ES"}
```

### انتخاب مدل

- **از [`gemini-2.5-flash-tts`](fa/providers/google.md#gemini-25-flash-tts) استفاده کنید** برای:
  - برنامه‌های با حجم بالا
  - تبدیل ساده متن به گفتار
  - موارد استفاده حساس به هزینه

- **از [`gemini-2.5-pro-tts`](fa/providers/google.md#gemini-25-pro-tts) استفاده کنید** برای:
  - پرامپت‌های استایل پیچیده
  - مکالمات چند گوینده
  - نیازهای کیفیت پریمیوم

## قیمت‌گذاری

### gemini-2.5-flash-tts
- ورودی: ۰.۵۰ دلار / ۱ میلیون توکن (کاراکتر)
- ورودی کش شده: ۰.۲۵ دلار / ۱ میلیون توکن
- خروجی صوتی: ۱۰.۰۰ دلار / ۱ میلیون توکن (۳۲ توکن در ثانیه صدا)

### gemini-2.5-pro-tts
- ورودی: ۱.۰۰ دلار / ۱ میلیون توکن (کاراکتر)
- ورودی کش شده: ۰.۵۰ دلار / ۱ میلیون توکن
- خروجی: ۲۰.۰۰ دلار / ۱ میلیون توکن (۳۲ توکن در ثانیه صدا)

**نمونه محاسبه هزینه:**
- ۳۰ ثانیه صدا = ۳۰ × ۳۲ = ۹۶۰ توکن صوتی
- ۱۰۰ کاراکتر ورودی = ۱۰۰ توکن ورودی
- مجموع برای نسخه فلش: $0.00005 (ورودی) + $0.0096 (خروجی) ≈ $0.00965

## مستندات مرتبط

- [مدل Gemini 2.5 Flash TTS](fa/providers/google.md#gemini-25-flash-tts)
- [مدل Gemini 2.5 Pro TTS](fa/providers/google.md#gemini-25-pro-tts)
- [API Audio Speech (سازگار با OpenAI)](fa/api-reference/audio.md)
- [API Chat Completions](fa/api-reference/chat.md)
- [راهنمای پردازش صوت](fa/guides/audio-processing.md)
- [اخبار: افزودن مدل‌های پیشرفته TTS](fa/news/2025-10-20-advanced-tts-and-transcription-models-added.md)
- [مستندات رسمی Vertex AI](https://cloud.google.com/text-to-speech/docs/gemini-tts)
