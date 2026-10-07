---
hasH1: true
---
# اتصال 9Router به AvalAI

9Router می‌تواند AvalAI را به‌عنوان upstream سازگار با OpenAI ثبت کند، برای مدل‌ها prefix بسازد و آن‌ها را از یک gateway محلی سازگار با OpenAI در اختیار کلاینت قرار دهد. این راهنما ابتدا یک اتصال ساده می‌سازد، Chat Completions را از Responses جدا می‌کند و fallback و تبدیل درخواست را تا زمان اثبات مسیر مستقیم خاموش نگه می‌دارد.

> **اعتبارسنجی:** برچسب‌های عمومی، قرارداد environment و مسیرهای کانتینر در **2026-08-06** با منابع رسمی 9Router بررسی شده‌اند. پیش از استقرار، [فهرست مدل‌های AvalAI](/fa/models/) و release جاری upstream را دوباره بررسی کنید.

## این یکپارچه‌سازی چیست

**بازبینی ۱۴۰۵-۰۶-۱۷ / (2026-09-08):** راهنمای رسمی Docker و README همچنان درگاه `20128`، مقدار `DATA_DIR=/app/data` و تنظیمات جداگانه امضا و گذرواژه پیشخوان را مستند می‌کنند. پیکربندی ساده و تک‌سرویسی Compose پایین را حفظ کنید. تصویر با نسخه ثابت، نمونه بررسی‌شده قبلی است و توصیه به جدیدترین انتشار نیست. 9Router درخواست را مسیریابی می‌کند؛ ابزار و کار مناسب را در [گردش‌کارهای عملی هوش مصنوعی](/fa/guides/ai-workflows) انتخاب کنید.

مسیر درخواست چنین است:

**کلاینت سازگار با OpenAI ←→ gateway محلی `/v1` در 9Router ←→ provider node پیشونددار AvalAI ←→ AvalAI**

کلید AvalAI اتصال 9Router به AvalAI را احراز هویت می‌کند. کلید دیگری که در dashboard خود 9Router می‌سازید، کلاینت پایین‌دستی را برای اتصال به 9Router احراز هویت می‌کند. این دو اعتبارنامه را یکسان نگیرید و به‌جای هم نفرستید.

وقتی به gateway محلی، شناسه مدل پیشونددار، چند اتصال upstream، priority یا fallback کنترل‌شده نیاز دارید از 9Router استفاده کنید. اگر به این لایه مسیریابی نیاز ندارید، اتصال مستقیم به AvalAI ساده‌تر است.

## پیش‌نیازها

- Node.js 20+ و npm برای آزمون محلی، یا Docker همراه Compose برای اجرای پایدار.
- یک کلید API اختصاصی AvalAI.
- شناسه مدل جاری و endpoint پشتیبانی‌شده آن.
- گذرواژه قوی dashboard و مقدارهای تصادفی مستقل برای رازهای امضای 9Router.
- دسترسی محلی به `http://localhost:20128`؛ dashboard را پیش از تغییر اعتبارنامه منتشر نکنید.

مدل نمونه فعلی `gpt-5.4-mini` است. این مدل Chat Completions و Responses را دارد، اما در 9Router این دو نوع provider node جدا هستند.

## بررسی AvalAI پیش از پیکربندی

ابتدا این مقادیر را بررسی کنید:

| بررسی | مقدار لازم |
| --- | --- |
| URL پایه AvalAI | `https://api.avalai.ir/v1` |
| مسیر Chat | `/v1/chat/completions` |
| مسیر Responses | `/v1/responses` |
| مدل نمونه | `gpt-5.4-mini` |
| URL درگاه پس از راه‌اندازی | `http://localhost:20128/v1` |

موفقیت **Check** فقط کلید upstream، URL، نوع API و مدل اختیاری واردشده را در همان لحظه تأیید می‌کند. این کار اتصال API-key پایداری را که درخواست‌های بعدی استفاده می‌کنند نمی‌سازد.

AvalAI در حال حاضر از شناسه‌های `gpt-transcribe` و `gpt-live-transcribe` پشتیبانی نمی‌کند. اتصال صوتی باید مدلی را به‌کار ببرد که اکنون برای مسیر متناظر `/v1/audio/*` فهرست شده باشد.

## نصب 9Router

برای آزمون محلی، package رسمی npm را نصب کنید:

```bash
npm install -g 9router
9router
```

`http://localhost:20128` را باز کنید. برای نمونه عملیاتی، package سراسری را کنار بگذارید و از Compose دارای tag ثابت در ادامه استفاده کنید.

## اتصال AvalAI

### ساخت provider node

1. **Providers** را باز کنید.
2. **Add OpenAI Compatible** را انتخاب کنید.
3. **Name** را `AvalAI` بگذارید.
4. **Prefix** را `avalai` بگذارید. این prefix بخشی از همه شناسه‌های مدل پایین‌دستی می‌شود.
5. برای اتصال نخست **Chat Completions** را انتخاب کنید. فقط وقتی مدل از `/v1/responses` پشتیبانی می‌کند، node جدا با **Responses API** بسازید.
6. **Base URL** را `https://api.avalai.ir/v1` قرار دهید.
7. کلید AvalAI را در **API Key (for Check)** وارد کنید.
8. در صورت نیاز `gpt-5.4-mini` را در **Model ID (optional)** وارد کنید.
9. **Check** را بزنید، نتیجه را بررسی و node را بسازید.

کلید validation عمداً موقت است. مرحله بعد را نیز انجام دهید.

### افزودن اتصال پایدار upstream

provider جدید AvalAI و کارت **Connections** را باز و **Add Connection** را انتخاب کنید. این مقادیر را وارد کنید:

- **Name:** نامی مانند `AvalAI production`؛
- **API Key:** کلید اختصاصی AvalAI؛
- **Priority:** برای نخستین و تنها اتصال مقدار `1`؛
- **Proxy Pool:** جز در نیاز بازبینی‌شده پراکسی خروجی، مقدار `None`.

**Validate** و سپس **Save** را انتخاب کنید. پیش از افزودن کلید دوم، round-robin یا fallback، فعال بودن اتصال را بررسی کنید.

### درک شناسه مدل پیشونددار

با prefix برابر `avalai`، شناسه مدل در gateway برابر `avalai/gpt-5.4-mini` است، نه شناسه خام AvalAI. در dashboard یک کلید پایین‌دستی 9Router بسازید و فهرست محلی مدل را ببینید:

```bash
curl http://localhost:20128/v1/models \
  -H "Authorization: Bearer replace-with-9router-key"
```

کلاینت، کلید 9Router را به localhost می‌فرستد؛ سپس 9Router کلید ذخیره‌شده AvalAI را به upstream می‌فرستد.

## تأیید نخستین جریان

هنگام اعتبارسنجی فقط یک اتصال فعال AvalAI داشته باشید و fallback را خاموش کنید:

```bash
curl -N http://localhost:20128/v1/chat/completions \
  -H "Authorization: Bearer replace-with-9router-key" \
  -H "Content-Type: application/json" \
  -H "X-9Router-Token-Saver: off" \
  -d '{
    "model": "avalai/gpt-5.4-mini",
    "messages": [{"role": "user", "content": "Reply with exactly: AvalAI via 9Router"}],
    "stream": true
  }'
```

این لایه‌ها را جداگانه بررسی کنید:

1. **Check** مربوط به provider node موفق است.
2. اتصال پایدار وضعیت active دارد.
3. `/v1/models` مدل پیشونددار را نشان می‌دهد.
4. درخواست streaming در Chat Completions خروجی مدل مورد انتظار را برمی‌گرداند.
5. فقط بعد از آن token saver، rewrite، round-robin، proxy pool یا fallback را فعال کنید.
6. برای Responses همین فرایند را با node مستقل **Responses API** و درخواست `/v1/responses` تکرار کنید.

هدر `X-9Router-Token-Saver: off` برای یک درخواست diagnostic همه token saverها را دور می‌زند و مشکل protocol در upstream را از مشکل transformation جدا می‌کند.

## قابلیت‌های پشتیبانی‌شده

node عمومی مدل زبانی فقط نوع API انتخاب‌شده هنگام ساخت همان node را پوشش می‌دهد.

| وضعیت | قابلیت | انتظار درست |
| --- | --- | --- |
| Direct | کشف مدل | 9Router فهرست routeشده و پیشونددار را در `/v1/models` محلی منتشر می‌کند. |
| Direct | Chat Completions | **Chat Completions** را انتخاب و `/v1/chat/completions` محلی را فراخوانی کنید. |
| Direct | Responses | **Responses API** را در node جدا انتخاب کنید؛ مدل AvalAI نیز باید این مسیر را داشته باشد. |
| Model/route dependent | Streaming | مدل، مسیر upstream، adapter در 9Router و کلاینت پایین‌دستی باید framing یکسان داشته باشند. |
| Model/route dependent | ابزار و خروجی ساختاریافته | به پشتیبانی مدل و عبور سازگار `tools`، `tool_choice` و schema وابسته است. |
| Model/route dependent | Vision و ورودی تصویر | به مدل vision در AvalAI و کلاینتی با شکل multimodal درست نیاز دارد. |
| Separate configuration | Embeddings | اتصال **Self-hosted Embedding** را با پایه `https://api.avalai.ir/v1`، کلید ذخیره‌شده و مدلی مانند `text-embedding-v4` بسازید. |
| Separate configuration | گفتار به متن | اتصال **Self-hosted STT** را با URL کامل `https://api.avalai.ir/v1/audio/transcriptions` و مدل transcription جاری بسازید. |
| Separate configuration | متن به گفتار | اتصال **Self-hosted TTS** را با ریشه `https://api.avalai.ir` بسازید تا adapter مسیر `/v1/audio/speech` را اضافه کند؛ سپس مدل speech جاری را انتخاب کنید. |
| Separate configuration | جست‌وجوی وب | provider جست‌وجوی 9Router و مسیر جست‌وجوی خود مدل دو تنظیم جدا هستند؛ مشخص کنید کلاینت کدام را فراخوانی می‌کند. |
| Unsupported or unvalidated | تولید تصویر، Realtime و ویدیو از node عمومی | صرف سازگاری OpenAI برای این نگاشت‌ها کافی نیست؛ این مسیرها از node زبانی استنباط نشدند. |

نام‌های **Self-hosted STT**، **Self-hosted TTS** و **Self-hosted Embedding** نوع provider در 9Router هستند. فیلدهای URL و key آن‌ها مسیر مستند OpenAI-shaped را در اختیار می‌گذارند، اما در این راهنما درخواست رسانه‌ای credentialed از AvalAI اجرا نشده است.

## اجرا با Docker Compose

image رسمی چندمعماری است. یک release بررسی‌شده را ثابت کنید، dashboard را به loopback محدود کنید، `/app/data` را پایدار نگه دارید و sidecar اختیاری Headroom را از نمونه پایه حذف کنید:

```yaml [compose.yaml]
services:
  9router:
    image: decolua/9router:v0.5.35
    container_name: 9router
    restart: unless-stopped
    ports:
      - "127.0.0.1:20128:20128"
    volumes:
      - 9router-data:/app/data
    env_file:
      - .env
    environment:
      DATA_DIR: /app/data
      PORT: "20128"
      HOSTNAME: 0.0.0.0
      NODE_ENV: production
      ENABLE_REQUEST_LOGS: "false"

volumes:
  9router-data:
```

یک `.env` نادیده‌گرفته‌شده با mode برابر `0600` بسازید. هر راز را مستقل تولید کنید و متن نمونه را به‌عنوان مقدار واقعی به‌کار نبرید:

```dotenv
JWT_SECRET=replace-with-an-independent-random-value
INITIAL_PASSWORD=replace-with-a-strong-dashboard-password
API_KEY_SECRET=replace-with-an-independent-random-value
MACHINE_ID_SALT=replace-with-an-independent-random-value
DATA_DIR=/app/data
ENABLE_REQUEST_LOGS=false
AUTH_COOKIE_SECURE=false
REQUIRE_API_KEY=true
```

مقدار fallback رسمی برای `INITIAL_PASSWORD` تنظیم‌نشده برابر `123456` است و ناامن محسوب می‌شود. متغیر را پیش از نخستین اجرا تنظیم کنید و نمونه‌ای با این fallback را منتشر نکنید. وقتی dashboard از HTTPS ارائه می‌شود، `AUTH_COOKIE_SECURE=true` را تنظیم کنید.

نمونه دارای tag ثابت را اجرا و بررسی کنید:

```bash
chmod 600 .env
docker compose config --quiet
docker compose up -d
docker compose logs --tail=100 9router
```

این baseline، Headroom، پراکسی خروجی یا reverse proxy اجرا نمی‌کند. آن‌ها را فقط پس از کارکرد مسیر مستقیم AvalAI و بازبینی مرز امنیتی اضافه کنید.

## بهره‌برداری امن

- پورت `20128` را روی loopback یا شبکه خصوصی نگه دارید، مگر ingress موجود با TLS و احراز هویت داشته باشید.
- ورود dashboard، کلید پایین‌دستی gateway و کلید upstream AvalAI را جدا نگه دارید.
- برای workload حساس `ENABLE_REQUEST_LOGS=false` را حفظ کنید. debug log می‌تواند prompt، response، header، فایل و داده شخصی داشته باشد.
- برای هر استقرار یک کلید AvalAI مستقل داشته باشید و مصرف provider را پایش کنید. عدد هزینه در dashboard فقط برآورد نمایشی است و رکورد صورتحساب AvalAI نیست.
- هنگام عیب‌یابی token saver و rewrite را خاموش و سپس یکی‌یکی فعال کنید.
- volume را محافظت کنید؛ SQLite، backup، certificate، log، تنظیم runtime، credential ذخیره‌شده provider و کلید پایین‌دستی در آن قرار دارد.

پیش از ارتقا، سرویس را متوقف و داده پایدار را از کانتینر متوقف‌شده کپی کنید:

```bash
docker compose stop 9router
mkdir -p backup/9router-data
docker cp 9router:/app/data/. backup/9router-data/
docker compose start 9router
```

tag فعلی image را ثبت کنید. برای ارتقا فقط tag بررسی‌شده را تغییر دهید، `docker compose config --quiet` را اجرا و سرویس را با همان volume بازسازی کنید. برای rollback ابتدا tag قبلی را برگردانید. SQLite را فقط در حالت توقف سرویس و از backup آزموده‌شده بازیابی کنید.

## عیب‌یابی

| نشانه | نخست کدام لایه را بررسی کنیم | اقدام امن بعدی |
| --- | --- | --- |
| **Check** در provider مقدار `401`/`403` می‌دهد | کلید AvalAI در فیلد validation موقت | کلید upstream اختصاصی را بدون افشا بررسی کنید. |
| `/v1` محلی مقدار `401`/`403` می‌دهد | کلید پایین‌دستی 9Router | کلید کپی‌شده از 9Router را بفرستید، نه کلید AvalAI. |
| **Check** موفق است اما درخواست شکست می‌خورد | اتصال پایدار وجود ندارد یا inactive است | کلید را در **Connections** اضافه، validate و save کنید. |
| مدل پیدا نمی‌شود | prefix یعنی `avalai/` یا نوع API اشتباه است | `/v1/models` محلی را ببینید و شناسه دقیق آن را استفاده کنید. |
| `404` در upstream | URL پایه یا route ناسازگار | `https://api.avalai.ir/v1` را حفظ و Chat را با Responses جابه‌جا نکنید. |
| stream متوقف یا خروجی عوض می‌شود | token saver، rewrite، fallback یا proxy | یک درخواست با `X-9Router-Token-Saver: off` بفرستید و transformationها را خاموش کنید. |
| Embeddings مقدار `404` می‌دهد | `/v1` در base URL نیست | برای **Self-hosted Embedding** از `https://api.avalai.ir/v1` استفاده کنید. |
| مسیر STT/TTS دوبار اضافه می‌شود | شکل full URL و server root اشتباه است | STT URL کامل transcription و TTS ریشه سرور را می‌گیرد. |
| state پس از restart حذف می‌شود | volume مربوط به `/app/data` یا `DATA_DIR` اشتباه است | `DATA_DIR=/app/data` و mount volume نام‌دار را بررسی کنید. |
| dashboard هزینه زیاد نشان می‌دهد | estimate با billing اشتباه شده است | منبع مصرف و قیمت AvalAI را بررسی کنید؛ estimate در 9Router invoice نیست. |

## راهنماهای مرتبط AvalAI و منابع رسمی

AvalAI:

- [مقدمه API](/fa/api-reference/introduction)
- [فهرست مدل‌ها](/fa/models/)
- [انتخاب مدل](/fa/guides/model-selection)
- [Embeddings](/fa/guides/embeddings)
- [گفتار به متن](/fa/guides/speech-to-text)
- [متن به گفتار](/fa/guides/text-to-speech)
- [محدودیت نرخ](/fa/guides/rate-limits)
- [بهترین شیوه‌های استقرار](/fa/guides/production-best-practices)

9Router:

- [مخزن رسمی](https://github.com/decolua/9router)
- [راهنمای رسمی Docker](https://github.com/decolua/9router/blob/master/DOCKER.md)
- [قرارداد environment](https://github.com/decolua/9router/blob/master/.env.example)

## مرز اعتبارسنجی

این راهنما در **2026-08-06** از روی منابع بررسی شد. برچسب provider، شکل route، tag انتشار، برابری Markdown و syntax فایل Compose را می‌توان بدون credential بررسی کرد. در این کار 9Router نصب نشد، image دانلود یا اجرا نشد، provider node ساخته نشد، کلید AvalAI ذخیره نشد، درخواست زنده ارسال نشد، fallback آزموده نشد، SQLite بازیابی نشد و gateway production منتشر نشد. پیش از استفاده عملیاتی، release upstream و مسیرهای جاری AvalAI را دوباره اعتبارسنجی کنید.
