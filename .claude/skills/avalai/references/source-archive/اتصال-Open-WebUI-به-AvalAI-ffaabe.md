---
hasH1: true
---
# اتصال Open WebUI به AvalAI

Open WebUI می‌تواند از AvalAI از طریق اتصال سازگار با OpenAI استفاده کند، در حالی که کشف مدل، RAG، تصویر و صدا در تنظیمات جداگانه هر قابلیت باقی می‌مانند. این راهنما ابتدا Chat Completions پایدار را راه‌اندازی می‌کند، Open Responses را experimental در نظر می‌گیرد و یک baseline کوچک Docker Compose با احراز هویت ارائه می‌دهد.

> **اعتبارسنجی:** برچسب‌های اتصال، پیش‌فرض حساب، قرارداد endpoint و مسیرهای کانتینر در **2026-08-06** با منابع رسمی Open WebUI بررسی شده‌اند. پیش از استقرار، [فهرست مدل AvalAI](/fa/models/) و release جاری Open WebUI را دوباره بررسی کنید.

## این یکپارچه‌سازی چیست

**بازبینی ۱۴۰۵-۰۶-۱۷ / (2026-09-08):** راهنمای جاری ارائه‌دهنده سازگار با OpenAI مسیر **Settings → Admin → Connections** و استفاده از **Model IDs (Filter)** هنگام خطای دریافت فهرست را توضیح می‌دهد. چت و دریافت فهرست مدل همچنان دو بررسی جدا هستند. کانتینر با نسخه ثابت پایین، نمونه بررسی‌شده قبلی است و توصیه به نسخه جاری نیست. پس از راه‌اندازی، پیش از اتصال داده واقعی شرکت، [پیش‌نویس پشتیبانی بدون کدنویسی](/fa/guides/ai-workflows) را امتحان کنید.

مسیر درخواست چنین است:

**کاربر مرورگر ←→ جریان مکالمه و task در Open WebUI ←→ اتصال پیکربندی‌شده AvalAI ←→ مدل انتخابی**

Open WebUI مالک کاربر، مکالمه، فایل، retrieval، ابزار، task model و تنظیم رسانه است. AvalAI درخواست‌های API ارسال‌شده از Open WebUI را احراز هویت می‌کند. کارکردن اتصال چت به‌تنهایی embeddings، تولید تصویر، speech یا transcription را پیکربندی نمی‌کند.

وقتی رابط چت self-hosted و چندکاربره می‌خواهید از این اتصال استفاده کنید. اگر به لایه حساب، مکالمه و retrieval در Open WebUI نیاز ندارید، برنامه خود را مستقیم به AvalAI متصل کنید.

## پیش‌نیازها

- Docker همراه Compose؛ Docker مسیر رسمی پیشنهادی برای بیشتر کاربران است.
- یک کلید API اختصاصی AvalAI.
- مدل چت جاری مانند `gpt-5.4-mini`.
- یک `WEBUI_SECRET_KEY` تصادفی و پایدار خارج از کنترل نسخه.
- برنامه مشخص برای حساب مدیر نخست و تأیید ثبت‌نام‌های بعدی پیش از انتشار سرویس.
- پشتیبانی شبکه از WebSocket تا چت streaming درست کار کند.

نخستین حساب ثبت‌شده روی volume داده تازه، Administrator می‌شود. ثبت‌نام‌های بعدی به‌صورت پیش‌فرض وضعیت Pending دارند و نیازمند تأیید مدیر هستند.

## بررسی AvalAI پیش از پیکربندی

پیش از افزودن اتصال این مقادیر را بررسی کنید:

| بررسی | مقدار لازم |
| --- | --- |
| URL پایه سازگار با OpenAI | `https://api.avalai.ir/v1` |
| مسیر اصلی لازم | `/v1/chat/completions` |
| مسیر پیشنهادی کشف مدل | `/v1/models` |
| مدل نمونه | `gpt-5.4-mini` |
| مسیر اختیاری experimental | `/v1/responses` |

Open WebUI اتصال را با فراخوانی `/models` و Bearer authentication بررسی می‌کند. اگر provider این مسیر را نداشته باشد، ممکن است verification شکست بخورد ولی Chat Completions کار کند. در این حالت به‌جای تغییر endpoint درست چت، **Model IDs (Filter)** را به‌کار ببرید.

AvalAI در حال حاضر از شناسه‌های `gpt-transcribe` و `gpt-live-transcribe` پشتیبانی نمی‌کند. در تنظیم صوت فقط مدل‌هایی را انتخاب کنید که اکنون برای `/v1/audio/transcriptions` فهرست شده‌اند.

## نصب Open WebUI

یک پوشه کاری خصوصی و فایل `.env` نادیده‌گرفته‌شده با راز پایدار بسازید. سپس image پایدار بررسی‌شده را با storage پایدار اجرا کنید:

```dotenv
WEBUI_AUTH=True
WEBUI_SECRET_KEY=replace-with-an-independent-random-value
```

```bash
chmod 600 .env
docker volume create open-webui
docker run -d --name open-webui --restart unless-stopped \
  -p 127.0.0.1:3000:8080 \
  --env-file .env \
  -v open-webui:/app/backend/data \
  ghcr.io/open-webui/open-webui:v0.11.0
docker logs --tail=100 open-webui
```

`http://localhost:3000` را باز کنید، ابتدا حساب مدیر مورد نظر را بسازید و پیش از افزودن credential ارائه‌دهنده، ماندگاری volume پس از restart را بررسی کنید.

## اتصال AvalAI

با حساب Administrator وارد شوید و این مسیر دقیق را دنبال کنید:

**Admin Settings → Connections → OpenAI → Add Connection**

این مقادیر را وارد کنید:

| فیلد | مقدار |
| --- | --- |
| URL | `https://api.avalai.ir/v1` |
| API Key | کلید اختصاصی AvalAI |
| Model IDs (Filter) | اگر discovery کار می‌کند خالی؛ در غیر این صورت `gpt-5.4-mini` |

اتصال را ذخیره کنید و toggle فعال/غیرفعال آن را روشن نگه دارید. فیلتر دستی مدل یک allowlist و fallback برای discovery است و قابلیت واقعی مدل را تغییر نمی‌دهد.

### ابتدا Chat Completions

اتصال اصلی سازگار با OpenAI به Chat Completions نیاز دارد. `gpt-5.4-mini` را انتخاب، یک prompt ساده بفرستید و پیش از فعال‌کردن ابزار یا پیوست فایل، streaming را بررسی کنید.

### Open Responses جدا و experimental است

Open WebUI پشتیبانی Open Responses را experimental معرفی می‌کند. آن را جدا از اتصال پایدار Chat Completions پیکربندی و آزمایش کنید. Open WebUI و مدل AvalAI هر دو باید شکل درخواست و stream را پشتیبانی کنند؛ آن را جایگزین مستقیم اتصال چت موجود فرض نکنید.

## تأیید نخستین جریان

هر لایه را جداگانه بررسی کنید:

1. سلامت کانتینر و mount شدن `/app/backend/data` را بررسی کنید.
2. مطمئن شوید نخستین حساب مورد نظر دسترسی Administrator دارد.
3. ذخیره و فعال بودن اتصال AvalAI را بررسی کنید.
4. مطمئن شوید discovery کار می‌کند یا `gpt-5.4-mini` با **Model IDs (Filter)** دیده می‌شود.
5. یک چت تازه بدون ابزار و فایل شروع و درخواست متن ساده ارسال کنید.
6. نمایش تدریجی خروجی streaming را بررسی کنید.
7. turn دوم وابسته به پاسخ اول بفرستید.
8. فقط پس از آن ابزار، vision، RAG، تصویر، STT یا TTS را جداگانه آزمایش کنید.

اگر چت ساده شکست می‌خورد، هنوز retrieval یا media را عیب‌یابی نکنید. ابتدا سلامت کانتینر، احراز هویت، انتخاب مدل، شکل endpoint و streaming را از هم جدا کنید.

## قابلیت‌های پشتیبانی‌شده

اتصال اصلی و تنظیمات مخصوص قابلیت، surfaceهای جدا هستند.

| وضعیت | قابلیت | انتظار درست |
| --- | --- | --- |
| Direct | کشف مدل | `/v1/models` پیشنهاد می‌شود و **Model IDs (Filter)** fallback دستی است. |
| Direct | Chat Completions | اتصال اصلی OpenAI به `/v1/chat/completions` نیاز دارد. |
| Model/route dependent | Open Responses | پشتیبانی Open WebUI experimental است و مدل AvalAI باید `/v1/responses` داشته باشد. |
| Model/route dependent | Streaming | Open WebUI، مدل AvalAI و proxy موجود باید stream و رفتار WebSocket را حفظ کنند. |
| Model/route dependent | ابزار و خروجی ساختاریافته | به پشتیبانی مدل، `tools` و `tool_choice` سازگار و tool mode مناسب در Open WebUI وابسته است. |
| Model/route dependent | Vision و ورودی تصویر | به مدل vision در AvalAI و مسیر attachment درست در Open WebUI نیاز دارد. |
| Separate configuration | Embeddings و RAG | تنظیم **Documents** برای embedding را با `https://api.avalai.ir/v1`، کلید اختصاصی و مدلی مانند `text-embedding-v4` پیکربندی کنید. Retrieval همچنین به extraction، chunking، storage و permission وابسته است. |
| Separate configuration | تولید تصویر | تنظیم **Images** را برای `/v1/images/generations` و مدل جاری مانند `gpt-image-2` انجام دهید؛ این تنظیم از چت به ارث نمی‌رسد. |
| Separate configuration | گفتار به متن | تنظیم transcription در **Audio** را برای `/v1/audio/transcriptions` و مدلی مانند `gpt-transcribe` انجام دهید. |
| Separate configuration | متن به گفتار | تنظیم speech در **Audio** را برای `/v1/audio/speech` و مدلی مانند `gpt-audio-1.5` انجام دهید. |
| Separate configuration | جست‌وجوی وب و ابزار برنامه | این موارد ابزار Open WebUI یا درخواست مخصوص مدل با permission و احتمال درخواست اضافی هستند. |
| Unsupported or unvalidated | صدای Realtime و ویدیو | نگاشت مستند و تأییدشده‌ای از اتصال اصلی OpenAI به AvalAI برای این قابلیت‌ها پیدا نشد. |

Open WebUI ممکن است برای title، tag، پیشنهاد follow-up، task model، ابزار، embedding یا media درخواست اضافه بفرستد. حتی وقتی رابط فقط یک turn کاربر نشان می‌دهد، این درخواست‌ها می‌توانند quota مصرف کنند.

## اجرا با Docker Compose

برای نمونه پایدار، از یک سرویس دارای tag ثابت، یک volume، یک پورت خصوصی و فایل راز پایدار استفاده کنید:

```yaml [compose.yaml]
services:
  open-webui:
    image: ghcr.io/open-webui/open-webui:v0.11.0
    container_name: open-webui
    restart: unless-stopped
    ports:
      - "127.0.0.1:3000:8080"
    volumes:
      - open-webui:/app/backend/data
    env_file:
      - .env
    environment:
      WEBUI_AUTH: "True"
      WEBUI_SECRET_KEY: ${WEBUI_SECRET_KEY}

volumes:
  open-webui:
```

بدون افزودن Ollama یا sidecar دیگر، تنظیم را اعتبارسنجی و اجرا کنید:

```bash
chmod 600 .env
docker compose config --quiet
docker compose up -d
docker compose logs --tail=100 open-webui
```

برای استقرار قابل بازتولید از tagهای شناور `:main` یا `:latest` استفاده نکنید. هنگام اعتبارسنجی این صفحه، `v0.11.0` release پایدار جاری بود؛ پیش از تغییر، release note و migration را بررسی کنید.

احراز هویت را روشن نگه دارید. Quick Start رسمی هشدار می‌دهد که `WEBUI_AUTH=False` انتخاب یک‌طرفه میان single-user و multi-account است و برای نمونه اشتراکی مناسب نیست.

## بهره‌برداری امن

- پورت `3000` را روی loopback یا شبکه خصوصی نگه دارید. اگر reverse proxy موجود آن را منتشر می‌کند، TLS همراه احراز هویت بخواهید و WebSocket upgrade را حفظ کنید.
- پیش از دعوت کاربران، Administrator مورد نظر را ثبت کنید. ثبت‌نام را محدود و هر حساب Pending را بازبینی کنید.
- `WEBUI_SECRET_KEY` را هنگام بازسازی کانتینر ثابت نگه دارید؛ تغییر یا حذف آن کاربر را خارج و session پایدار را مختل می‌کند.
- اگر لغو و انتساب مصرف جدا می‌خواهید، برای chat، embeddings یا media کلیدهای AvalAI جدا استفاده کنید.
- تاریخچه مکالمه، فایل آپلودی، index بازیابی، credential ارائه‌دهنده و رکورد کاربر در `/app/backend/data` را حساس بدانید.
- کلید API، Authorization header، prompt، response، فایل آپلودی و داده شخصی را از log و support bundle حذف کنید.

پیش از ارتقا از volume متوقف‌شده پشتیبان بگیرید:

```bash
docker compose stop open-webui
mkdir -p backup/open-webui-data
docker cp open-webui:/app/backend/data/. backup/open-webui-data/
docker compose start open-webui
```

tag فعلی image را ثبت کنید. برای ارتقا release note را بخوانید، فقط tag ثابت را تغییر دهید، `docker compose config --quiet` را اجرا و سرویس را با همان volume و secret بازسازی کنید. برای rollback ابتدا tag پیشین را برگردانید. داده را فقط در حالت توقف سرویس و پس از بررسی سازگاری migration روی یک کپی بازیابی کنید.

## عیب‌یابی

| نشانه | نخست کدام لایه را بررسی کنیم | اقدام امن بعدی |
| --- | --- | --- |
| verification اتصال `400`، `401` یا `403` می‌دهد | `/v1/models`، Bearer key یا رفتار discovery ارائه‌دهنده | URL پایه درست را نگه دارید و اگر فقط discovery شکست خورد شناسه دقیق را به **Model IDs (Filter)** اضافه کنید. |
| چت `401`/`403` می‌دهد | کلید ذخیره‌شده AvalAI و toggle اتصال | کلید اختصاصی را دوباره ذخیره و فعال بودن اتصال را بررسی کنید. |
| چت `404` می‌دهد | نبود `/v1`، مدل اشتباه یا ناسازگاری Responses و Chat | از `https://api.avalai.ir/v1` و Chat Completions پایدار شروع کنید. |
| مدل دیده نمی‌شود | Filter، tier حساب یا catalog قدیمی | یک شناسه جاری را به **Model IDs (Filter)** اضافه و چت تازه باز کنید. |
| چت ساده کار می‌کند اما ابزار نه | Function calling، tool mode یا schema | پشتیبانی مدل را بررسی و آزمون را به یک ابزار محدود کنید. |
| Vision شکست می‌خورد | قابلیت مدل یا مسیر attachment | مدل vision تأییدشده در catalog را با یک تصویر کوچک بیازمایید. |
| RAG شکست می‌خورد | تنظیم embedding، extractor، chunk، permission یا storage | پیش از re-index یک سند کوچک، embeddings را جداگانه آزمایش کنید. |
| تصویر یا صدا شکست می‌خورد | engine، URL، key یا مدل مخصوص قابلیت | تنظیم **Images** یا **Audio** را بررسی کنید؛ credential چت کافی نیست. |
| خروجی streaming نیست | رفتار WebSocket/SSE در proxy یا route اشتباه | ابتدا روی loopback آزمایش، سپس buffering و upgrade در proxy را بررسی کنید. |
| پس از restart کاربران خارج می‌شوند | `WEBUI_SECRET_KEY` حذف یا تغییر کرده است | secret پایدار اصلی را از محل امن بازیابی کنید. |
| داده پس از restart حذف می‌شود | volume مربوط به `/app/backend/data` وجود ندارد | پیش از بازسازی کانتینر mount volume نام‌دار را بررسی کنید. |

## راهنماهای مرتبط AvalAI و منابع رسمی

AvalAI:

- [مقدمه API](/fa/api-reference/introduction)
- [فهرست مدل‌ها](/fa/models/)
- [انتخاب مدل](/fa/guides/model-selection)
- [Embeddings](/fa/guides/embeddings)
- [تولید تصویر](/fa/guides/image-generation)
- [گفتار به متن](/fa/guides/speech-to-text)
- [متن به گفتار](/fa/guides/text-to-speech)
- [محدودیت نرخ](/fa/guides/rate-limits)
- [بهترین شیوه‌های استقرار](/fa/guides/production-best-practices)

Open WebUI:

- [مخزن رسمی](https://github.com/open-webui/open-webui)
- [Quick Start](https://docs.openwebui.com/getting-started/quick-start/)
- [Connect a Provider](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/)
- [OpenAI-Compatible Providers](https://docs.openwebui.com/getting-started/quick-start/connect-a-provider/starting-with-openai-compatible/)

## مرز اعتبارسنجی

این راهنما در **2026-08-06** از روی منابع بررسی شد. Markdown، پیوند route، برابری locale، syntax فایل Compose دارای tag ثابت و رفتار سایت buildشده را می‌توان محلی اعتبارسنجی کرد. در این کار Open WebUI دانلود یا اجرا نشد، Administrator ثبت نشد، کلید AvalAI ذخیره نشد، درخواست زنده چت یا media ارسال نشد، WebSocket از proxy عبور داده نشد، backup بازیابی نشد و شبکه production آزموده نشد. پیش از استفاده عملیاتی، release جاری و routeهای مدل را دوباره بررسی کنید.
