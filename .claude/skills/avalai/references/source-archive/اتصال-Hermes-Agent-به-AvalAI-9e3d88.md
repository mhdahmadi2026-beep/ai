---
hasH1: true
---
# اتصال Hermes Agent به AvalAI

Hermes Agent می‌تواند از AvalAI به‌عنوان یک ارائه‌دهنده نام‌گذاری‌شده و سازگار با OpenAI استفاده کند، در حالی که ابزارها، نشست‌ها، درگاه‌ها و سرویس‌های کمکی Hermes جداگانه کنترل می‌شوند. این راهنما ابتدا مسیر سازگارتر را راه‌اندازی می‌کند، چت ساده را پیش از ابزارها می‌آزماید و سپس مرز قابلیت‌هایی را که به مسیر یا تنظیم جدا نیاز دارند توضیح می‌دهد.

> **اعتبارسنجی:** تنظیمات و برچسب‌های رابط این صفحه در **2026-08-06** با منابع رسمی عمومی بررسی شده‌اند. موجودی مدل‌ها ممکن است تغییر کند؛ پیش از راه‌اندازی، مدل انتخابی را در [فهرست مدل‌های AvalAI](/fa/models/) بررسی کنید.

## این یکپارچه‌سازی چیست

**بازبینی ۱۴۰۵-۰۶-۱۷ / (2026-09-08):** راهنمای رسمی جاری همچنان ارائه‌دهنده نام‌گذاری‌شده، `key_env`، `chat_completions` و `/model custom:<name>:<model>` را مستند می‌کند. برچسب Compose پایین همان نمونه بررسی‌شده قبلی است، نه ادعایی درباره جدیدترین انتشار. پس از بررسی اتصال، [تمرین محدود عامل برنامه‌نویسی](/fa/guides/coding-agent-workflows) را انجام دهید یا [گردش‌کار عملی انتخاب کنید](/fa/guides/ai-workflows).

مسیر درخواست چنین است:

**شما ←→ حلقه عامل و ابزارهای Hermes ←→ endpoint سازگار با OpenAI در AvalAI ←→ مدل انتخابی**

AvalAI درخواست مدل را احراز هویت می‌کند. در مقابل، Hermes به‌طور مستقل تعیین می‌کند عامل چه فایل‌هایی را بخواند یا تغییر دهد، چه فرمانی اجرا کند، به کدام شبکه دسترسی داشته باشد و چه درگاهی را منتشر کند. معتبر بودن کلید API، سیاست ناامن ابزار یا فایل‌سیستم را امن نمی‌کند.

این اتصال برای عامل ترمینالی یا پیام‌رسان با ابزار و نشست قابل ادامه مناسب است. اگر به ابزار عامل و نشست طولانی نیاز ندارید، یک کلاینت چت ساده انتخاب سبک‌تری است.

## پیش‌نیازها

- Linux، macOS یا Windows از طریق WSL2 مطابق نیازمندی‌های جاری Hermes.
- یک نسخه جدید Hermes Agent.
- کلید API اختصاصی AvalAI خارج از کنترل نسخه.
- مدلی با حداقل **64,000 توکن ورودی**؛ Hermes برای کار عامل با ابزار، Context کوچک‌تر را رد می‌کند.
- مدلی که همه قابلیت‌های مورد آزمون را داشته باشد. در این راهنما `gpt-5.4-mini` مدل نمونه است، زیرا فهرست فعلی Chat Completions، Responses، streaming، ابزارها، خروجی ساختاریافته، vision و 272,000 توکن ورودی را برای آن ثبت می‌کند.

برای Hermes یک کلید مستقل AvalAI بسازید تا لغو دسترسی و انتساب مصرف، برنامه‌های دیگر را تحت تأثیر قرار ندهد.

## بررسی AvalAI پیش از پیکربندی

پیش از تغییر Hermes این مقادیر را بررسی کنید:

| بررسی | مقدار لازم |
| --- | --- |
| URL پایه سازگار با OpenAI | `https://api.avalai.ir/v1` |
| مسیر سازگارتر | `/v1/chat/completions` |
| مسیر اختیاری Responses | `/v1/responses` |
| مدل نمونه | `gpt-5.4-mini` |
| حداقل Context در Hermes | 64,000 توکن ورودی |

شناسه مدل، مسیر API و قابلیت‌ها سه بررسی جدا هستند. دیده‌شدن مدل در `/v1/models` به معنی پشتیبانی آن از همه endpointها و ابزارها نیست.

AvalAI در حال حاضر از شناسه‌های `gpt-transcribe` و `gpt-live-transcribe` پشتیبانی نمی‌کند. نمونه‌های upstream با این شناسه‌ها را وارد Hermes نکنید.

## نصب Hermes

[راهنمای رسمی نصب Hermes](https://hermes-agent.nousresearch.com/docs/getting-started/installation) را دنبال کنید. پس از نصب، CLI و پوشه تنظیمات را بررسی کنید:

```bash
hermes --version
hermes doctor
```

راز ارائه‌دهنده را در اسکریپت محلی پروژه نگذارید. Hermes رازها را در `~/.hermes/.env` و تنظیمات غیرمحرمانه را در `~/.hermes/config.yaml` نگه می‌دارد.

## اتصال AvalAI

### راه‌اندازی تعاملی پیشنهادی

بیرون از نشست فعال، `hermes model` را اجرا و **Custom endpoint (self-hosted / VLLM / etc.)** را انتخاب کنید. مقادیر زیر را وارد کنید:

| فیلد Hermes | مقدار |
| --- | --- |
| API base URL | `https://api.avalai.ir/v1` |
| API key | کلید اختصاصی AvalAI |
| Model | `gpt-5.4-mini` |
| API mode / transport | `chat_completions` |
| Context length | `272000` |

Wizard تنظیم ارائه‌دهنده را پایدار می‌کند. ابتدا `chat_completions` را انتخاب کنید، چون مسیر سازگارتر است.

### پیکربندی نام‌گذاری‌شده و قابل ممیزی

فقط راز را در `~/.hermes/.env` نگه دارید:

```dotenv
AVALAI_API_KEY=replace-with-your-avalai-key
```

سپس `providers.avalai` را در `~/.hermes/config.yaml` تعریف کنید:

```yaml
providers:
  avalai:
    api: https://api.avalai.ir/v1
    key_env: AVALAI_API_KEY
    transport: chat_completions
    default_model: gpt-5.4-mini
    models:
      gpt-5.4-mini:
        context_length: 272000
        supports_vision: true
```

فیلد `key_env` به Hermes می‌گوید راز در کدام متغیر قرار دارد. مقدار inline برای `api_key` را در `config.yaml`، پشتیبان، تصویر یا گزارش اشتراکی قرار ندهید.

### Transport اختیاری Responses

وقتی آگاهانه می‌خواهید Hermes درخواست Responses بفرستد، یک ارائه‌دهنده نام‌گذاری‌شده جدا بسازید. فقط پس از مشاهده `/v1/responses` برای مدل در فهرست جاری AvalAI، transport را تغییر دهید:

```yaml
providers:
  avalai-responses:
    api: https://api.avalai.ir/v1
    key_env: AVALAI_API_KEY
    transport: codex_responses
    default_model: gpt-5.4-mini
    models:
      gpt-5.4-mini:
        context_length: 272000
        supports_vision: true
```

`codex_responses` نام transport در Hermes است؛ این نام ثابت نمی‌کند همه مدل‌ها یا سرورهای سازگار با OpenAI از Responses پشتیبانی می‌کنند.

## تأیید نخستین جریان

لایه‌ها را به ترتیب بررسی کنید:

1. ابتدا diagnostic را اجرا و خطای تنظیم را برطرف کنید.
2. Hermes را اجرا و provider و model را در banner آغازین تأیید کنید.
3. یک درخواست ساده و سپس پرسش دومی وابسته به پاسخ نخست بفرستید.
4. اگر مدل از function calling پشتیبانی می‌کند، یک کار فقط‌خواندنی امن مانند فهرست‌کردن پوشه جاری بخواهید. آزمون را با نوشتن فایل یا تغییر shell شروع نکنید.
5. خارج شوید و نشست را ادامه دهید.
6. فقط پس از کارکرد مسیر پیش‌فرض، تغییر مدل داخل نشست را آزمایش کنید.

```bash
hermes doctor
hermes
hermes --continue
```

داخل نشست فعال، `/model custom:avalai:gpt-5.4-mini` ارائه‌دهنده نام‌گذاری‌شده را انتخاب می‌کند. برای افزودن یا تغییر provider از `hermes model` در ترمینال استفاده کنید؛ `/model` فقط میان providerهای از پیش پیکربندی‌شده جابه‌جا می‌شود.

## قابلیت‌های پشتیبانی‌شده

وضعیت، مسیر Hermes تا AvalAI را توصیف می‌کند و وعده‌ای برای همه مدل‌ها نیست.

| وضعیت | قابلیت | انتظار درست |
| --- | --- | --- |
| Direct | Chat Completions | ارائه‌دهنده سفارشی می‌تواند درخواست `/v1/chat/completions` بفرستد؛ از این مسیر شروع کنید. |
| Model/route dependent | Responses | `codex_responses` را فقط با مدل تأییدشده برای `/v1/responses` به‌کار ببرید. |
| Model/route dependent | Streaming | Hermes و مدل انتخابی باید رویدادهای stream مورد انتظار را حفظ کنند. |
| Model/route dependent | System messages و sampling | پارامتر پشتیبانی‌نشده ممکن است همچنان رد یا نادیده گرفته شود. |
| Model/route dependent | ابزار و خروجی ساختاریافته | به function calling مدل، schema سازگار و مجوز ابزار Hermes وابسته است. |
| Model/route dependent | Vision و ورودی تصویر | `supports_vision: true` را فقط برای مدل vision تأییدشده در فهرست تنظیم کنید. |
| Unsupported or unvalidated | Embeddings و RAG از provider اصلی | ارائه‌دهنده inference اصلی Hermes محل تنظیم embeddings نیست. |
| Separate configuration | تولید تصویر | ابزار تصویر یا Tool Gateway در Hermes backend و اعتبارنامه جدا دارد. |
| Separate configuration | گفتار به متن و متن به گفتار | ابزارهای صوتی و transcription سرویس کمکی هستند و از provider چت نتیجه نمی‌شوند. |
| Separate configuration | جست‌وجوی وب و اتوماسیون مرورگر | backend و مجوز ابزارهای Hermes از احراز هویت مدل AvalAI جدا هستند. |
| Unsupported or unvalidated | صدای Realtime و ویدیو | نگاشت مستند و تأییدشده‌ای از provider نام‌گذاری‌شده برای این مسیرها پیدا نشد. |

مدل‌های کمکی ممکن است به‌صورت پیش‌فرض به مدل اصلی هدایت شوند، اما vision analysis، خلاصه‌سازی وب، تولید تصویر، صدا، مرورگر، حافظه و gateway پیام‌رسان می‌توانند پیکربندی و صورتحساب جدا داشته باشند. پیش از فرض استفاده از کلید AvalAI، provider فعال هرکدام را بررسی کنید.

## اجرا با Docker Compose

Hermes یک `Dockerfile` و `docker-compose.yml` رسمی منتشر می‌کند. به‌جای تعریف image غیررسمی، از همان فایل‌ها در tag بررسی‌شده استفاده کنید. tag تأییدشده این راهنما `v2026.8.3` است:

```bash
git clone https://github.com/NousResearch/hermes-agent.git
cd hermes-agent
git checkout v2026.8.3
HERMES_UID="$(id -u)" HERMES_GID="$(id -g)" docker compose up -d --build
docker compose exec gateway hermes doctor
docker compose logs --tail=100 gateway dashboard
```

فایل رسمی Compose:

- source بررسی‌شده را به image محلی `hermes-agent` تبدیل می‌کند؛
- مسیر `~/.hermes` میزبان را برای تنظیمات و نشست پایدار روی `/opt/data` mount می‌کند؛
- کاربر سرویس را با `HERMES_UID` و `HERMES_GID` هماهنگ می‌کند؛
- dashboard را با host networking به `127.0.0.1` محدود می‌کند؛
- API server سازگار با OpenAI را تا زمان تنظیم هر دو متغیر `API_SERVER_HOST` و `API_SERVER_KEY` خاموش نگه می‌دارد.

Dashboard را با `--insecure --host 0.0.0.0` منتشر نکنید. برای مدیریت راه‌دور از SSH tunnel یا ingress موجود با TLS و احراز هویت استفاده کنید. gateway پیام‌رسان را پیش از تعریف allowlist صریح کاربران فعال نکنید.

## بهره‌برداری امن

- فقط workspace ضروری را mount کنید. Hermes مستقل از احراز هویت مدل می‌تواند ابزار اجرا و فایل تغییر دهد.
- `~/.hermes/.env`، auth store، داده نشست و پشتیبان‌ها را فقط برای مالک سرویس خوانا نگه دارید.
- Dashboard و gateway را خصوصی نگه دارید. اگر API server را فعال می‌کنید، یک `API_SERVER_KEY` قوی و مستقل بسازید.
- مجوز ترمینال، مرورگر، شبکه و پیام‌رسان را جداگانه بازبینی و ابزار غیرضروری را خاموش کنید.
- Authorization header، prompt، response، محتوای فایل و داده شخصی را از diagnostic حذف کنید.
- مصرف و محدودیت نرخ AvalAI را پایش کنید؛ retry و مدل کمکی می‌تواند بیش از turn قابل‌مشاهده درخواست بسازد.

پیش از ارتقا، سرویس‌ها را متوقف کنید، از همه پوشه داده Hermes پشتیبان بگیرید و revision جاری را ثبت کنید:

```bash
docker compose stop
git rev-parse HEAD
tar -czf hermes-data-backup.tgz -C "$HOME" .hermes
docker compose start
```

برای ارتقا، tag بررسی‌شده را checkout و image را rebuild کنید. برای rollback، سرویس را متوقف کنید، به revision ثبت‌شده بازگردید، دوباره build کنید و فقط در صورت نیاز migration داده، پشتیبان را بازیابی کنید. بازیابی را پیش از اتکا روی یک کپی جدا آزمایش کنید.

## عیب‌یابی

| نشانه | نخست کدام لایه را بررسی کنیم | اقدام امن بعدی |
| --- | --- | --- |
| `401` یا `403` | `AVALAI_API_KEY`، مالکیت فایل یا دسترسی حساب | `hermes doctor` را اجرا و `key_env` را بدون چاپ راز بررسی کنید. |
| `404` | URL پایه یا transport | `/v1` را حفظ و جز در مدل Responses از `chat_completions` استفاده کنید. |
| مدل پیدا نمی‌شود | شناسه دقیق و provider نام‌گذاری‌شده | `/v1/models` و `/model custom:avalai:...` را بررسی کنید. |
| خطای Context در شروع | metadata کوچک‌تر از 64K | مدل بزرگ‌تر انتخاب یا `context_length` تأییدشده را اصلاح کنید. |
| tool call به‌شکل متن دیده می‌شود | سازگاری مدل و schema ابزار | function calling را تأیید و آزمون را به یک ابزار فقط‌خواندنی محدود کنید. |
| چت کار می‌کند اما vision نه | `supports_vision`، شکل ورودی یا routing کمکی | فهرست مدل و provider فعال vision را بررسی کنید. |
| stream خالی یا خراب | ناسازگاری Chat و Responses یا proxy buffering | به چت ساده بدون stream برگردید و لایه‌ها را یکی‌یکی فعال کنید. |
| نشست ادامه پیدا نمی‌کند | مسیر داده یا مالکیت volume | mount شدن `~/.hermes` روی `/opt/data` و دسترسی UID را بررسی کنید. |
| فایل‌های کانتینر root-owned هستند | نگاشت UID/GID یا entrypoint تغییرکرده | از Compose رسمی استفاده کنید و زنجیره `/init` را جایگزین نکنید. |

## راهنماهای مرتبط AvalAI و منابع رسمی

AvalAI:

- [مقدمه API](/fa/api-reference/introduction)
- [فهرست مدل‌ها](/fa/models/)
- [انتخاب مدل](/fa/guides/model-selection)
- [فراخوانی تابع](/fa/guides/function-calling)
- [Vision](/fa/guides/vision)
- [محدودیت نرخ](/fa/guides/rate-limits)
- [بهترین شیوه‌های استقرار](/fa/guides/production-best-practices)

Hermes Agent:

- [مخزن رسمی](https://github.com/NousResearch/hermes-agent)
- [Quickstart](https://hermes-agent.nousresearch.com/docs/getting-started/quickstart)
- [Installation](https://hermes-agent.nousresearch.com/docs/getting-started/installation)
- [AI providers and custom endpoints](https://hermes-agent.nousresearch.com/docs/integrations/providers)

## مرز اعتبارسنجی

این راهنما در **2026-08-06** از روی منابع بررسی شد. Markdown، برابری تنظیمات، پیوندها و رفتار سایت ایستا را می‌توان محلی اعتبارسنجی کرد. در این کار از کلید AvalAI استفاده نشد، Hermes نصب نشد، کانتینر build یا اجرا نشد، درخواست پولی ارسال نشد، gateway منتشر نشد، پشتیبان بازیابی نشد و شبکه production آزموده نشد. پیش از اجرای فرمان‌ها روی سامانه عملیاتی، release جاری upstream و فهرست مدل را دوباره بررسی کنید.
