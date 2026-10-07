# News 2026-02-03-elevenlabs-provider-cloudflare-models-added: ارائه‌دهنده جدید: مدل‌های گفتاری ElevenLabs و ۱۲ مدل جدید هوش مصنوعی Cloudflare
URL: `https://docs.avalai.ir/fa/news/2026-02-03-elevenlabs-provider-cloudflare-models-added`
**تاریخ:** ۱۴۰۴-۱۱-۱۴ / (2026-02-03)

# ارائه‌دهنده جدید: مدل‌های گفتاری ElevenLabs و ۱۲ مدل جدید هوش مصنوعی Cloudflare

**تاریخ:** ۱۴۰۴-۱۱-۱۴ / (2026-02-03)

## خلاصه

AvalAI ارائه‌دهنده جدید ElevenLabs را با ۷ مدل گفتاری پیشرفته برای تبدیل متن به گفتار و گفتار به متن اضافه می‌کند. همچنین ۱۲ مدل جدید هوش مصنوعی Cloudflare شامل مدل‌های تولید تصویر FLUX، مدل‌های embedding و مدل‌های چت از ارائه‌دهندگان مختلف اکنون در دسترس است.


### Cloudflare AI - ۱۲ مدل جدید

مجموعه مدل‌های هوش مصنوعی Cloudflare را با ۱۲ مدل جدید در حوزه‌های تولید تصویر، embedding و چت گسترش داده‌ایم. [مستندات](fa/providers/cloudflare.md)

#### مدل‌های تولید تصویر (v1/images/generations)

پنج مدل جدید تولید تصویر اکنون در دسترس است:

| مدل | توضیحات | قیمت پایه (۱ مگاپیکسل) |
|-----|---------|------------------------|
| `cf.flux-2-klein-9b` | مدل FLUX 2 Klein با ۹ میلیارد پارامتر | $۰.۰۱۵/تصویر |
| `cf.flux-2-klein-4b` | مدل فشرده FLUX 2 Klein با ۴ میلیارد پارامتر | $۰.۰۱۰/تصویر |
| `cf.flux-2-dev` | مدل توسعه FLUX 2 | $۰.۰۱۰/تصویر |
| `cf.lucid-origin` | تولید تصویر Lucid Origin | $۰.۰۱۵/تصویر |
| `cf.phoenix-1.0` | تولید تصویر Phoenix 1.0 | $۰.۰۱۵/تصویر |

**قیمت‌گذاری بر اساس رزولوشن:**

| مدل | ۱ مگاپیکسل | ۲ مگاپیکسل | ۳ مگاپیکسل | ۴ مگاپیکسل |
|-----|------------|------------|------------|------------|
| `cf.flux-2-klein-9b` | $۰.۰۱۵ | $۰.۰۱۷ | $۰.۰۱۹ | $۰.۰۲۱ |
| `cf.flux-2-klein-4b` | $۰.۰۱۰ | $۰.۰۱۲ | $۰.۰۱۴ | $۰.۰۱۶ |
| `cf.flux-2-dev` | $۰.۰۱۰ | $۰.۰۱۱ | $۰.۰۱۲ | $۰.۰۱۳ |
| `cf.lucid-origin` | $۰.۰۱۵ | $۰.۰۱۷ | $۰.۰۱۹ | $۰.۰۲۱ |
| `cf.phoenix-1.0` | $۰.۰۱۵ | $۰.۰۱۷ | $۰.۰۱۹ | $۰.۰۲۱ |

#### مدل‌های Embedding (v1/embeddings)

سه مدل embedding جدید برای جستجوی معنایی و تحلیل متن:

| مدل | توضیحات | قیمت ورودی (دلار/۱م توکن) |
|-----|---------|---------------------------|
| `cf.qwen3-embedding-0.6b` | Qwen3 Embedding ۰.۶ میلیارد از Alibaba | $۰.۰۱۲ |
| `cf.plamo-embedding-1b` | PLaMo Embedding ۱ میلیارد از PFN | $۰.۰۱۹ |
| `cf.embeddinggemma-300m` | EmbeddingGemma ۳۰۰ میلیون از Google | $۰.۰۱۲ |

#### مدل‌های تکمیل چت (v1/chat/completions, v1/responses)

چهار مدل چت جدید با پشتیبانی جزئی از v1/responses:

| مدل | صاحب | ورودی (دلار/۱م) | ورودی کش شده (دلار/۱م) | خروجی (دلار/۱م) |
|-----|------|-----------------|------------------------|-----------------|
| `cf.qwen3-30b-a3b-fp8` | Alibaba | $۰.۰۵۱ | $۰.۰۲۵ | $۰.۳۴ |
| `cf.granite-4.0-h-micro` | IBM | $۰.۰۱۷ | $۰.۰۰۸ | $۰.۱۱ |
| `cf.gpt-oss-120b` | OpenAI | $۰.۳۵ | $۰.۱۷۵ | $۰.۷۵ |
| `cf.gpt-oss-20b` | OpenAI | $۰.۲۰ | $۰.۱۰ | $۰.۳۰ |

---

## مثال‌های درخواست/پاسخ API

### مثال تبدیل متن به گفتار ElevenLabs

```bash
curl https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "eleven_flash_v2_5",
    "input": "روباه قهوه‌ای سریع از روی سگ تنبل پرید.",
    "voice": "coral"
  }' \
  --output speech.mp3
```

### مثال رونویسی ElevenLabs

```bash
curl https://api.avalai.ir/v1/audio/transcriptions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F file=@audio.mp3 \
  -F model=scribe_v2
```

**نمونه پاسخ:**

```json
{
  "text": "روباه قهوه‌ای سریع از روی سگ تنبل پرید.",
  "task": "transcribe",
  "language": "fa",
  "duration": 2.5,
  "words": [
    {"word": "روباه", "start": 0.0, "end": 0.25},
    {"word": "قهوه‌ای", "start": 0.25, "end": 0.45},
    ...
  ]
}
```

### مثال تولید تصویر Cloudflare

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "cf.flux-2-klein-9b",
    "prompt": "یک شهر آینده‌نگر در غروب خورشید با ماشین‌های پرنده",
    "n": 1,
    "size": "1024x1024"
  }'
```

### مثال Embedding Cloudflare

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "cf.qwen3-embedding-0.6b",
    "input": "یادگیری ماشین به کامپیوترها امکان یادگیری از داده‌ها را می‌دهد."
  }'
```

---

## مقایسه قیمت‌ها

### مدل‌های TTS ElevenLabs

| مدل | هزینه/ثانیه | بهترین برای |
|-----|-------------|-------------|
| `eleven_flash_v2_5` | $۰.۰۰۲۵ | برنامه‌های بلادرنگ، تأخیر کم |
| `eleven_turbo_v2_5` | $۰.۰۰۲۵ | تعادل کیفیت و سرعت |
| `eleven_multilingual_v2` | $۰.۰۰۵ | بالاترین کیفیت، دامنه احساسی |

### مدل‌های تصویر Cloudflare

| مدل | به ازای تصویر (۱ مگاپیکسل) | بهترین برای |
|-----|---------------------------|-------------|
| `cf.flux-2-klein-4b` | $۰.۰۱۰ | تولید مقرون‌به‌صرفه |
| `cf.flux-2-dev` | $۰.۰۱۰ | توسعه و آزمایش |
| `cf.flux-2-klein-9b` | $۰.۰۱۵ | خروجی با کیفیت بالاتر |

---

## منابع مرتبط

- [مستندات مدل‌های ElevenLabs](fa/providers/elevenlabs.md)
- [مستندات مدل‌های Cloudflare](fa/providers/cloudflare.md)
- [مرجع API صوتی](fa/api-reference/audio.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API Embeddings](fa/api-reference/embeddings.md)
- [مستندات رسمی ElevenLabs API](https://elevenlabs.io/docs/api-reference)
