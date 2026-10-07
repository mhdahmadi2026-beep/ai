# یکپارچه‌سازی AvalAI با Claude Code

Claude Code عامل کدنویسی قدرتمند Anthropic در ترمینال است که می‌تواند کدبیس شما را بخواند، فایل‌ها را ویرایش کند و دستورات ترمینال را اجرا کند. به‌صورت پیش‌فرض Claude Code به API خود Anthropic متصل می‌شود، اما با چند متغیر محیطی می‌توانید آن را مستقیما به AvalAI متصل کنید و از کلید API AvalAI خود استفاده کنید.

Claude Code برای قابلیت‌های عاملی خود به **فراخوانی ابزار (Tool Calling)** وابسته است. AvalAI به‌صورت بومی از [Messages API (`v1/messages`)](fa/api-reference/messages.md) سازگار با Anthropic پشتیبانی می‌کند—همان نقطه پایانی که Claude Code از آن استفاده می‌کند—بنابراین برای مدل‌های Claude و بسیاری از مدل‌های دیگر، به LiteLLM، پراکسی یا لایه ترجمه نیاز ندارید.

?> **💰 پیشنهاد ویژه:** با [بسته‌های اعتباری اختصاصی](fa/credit-packages.md) AvalAI، **تا ۷۰٪ اعتبار بیشتر** دریافت کنید یا از **تا ۴۰٪ تخفیف ویژه** در خریدهای خود بهره‌مند شوید. این پیشنهادها به شما کمک می‌کنند بودجه توسعه هوش مصنوعی خود را به بهترین شکل مدیریت کنید!

## چرا AvalAI را با Claude Code یکپارچه کنیم؟

اتصال Claude Code به AvalAI قابلیت‌های قدرتمندی را به ترمینال شما اضافه می‌کند:

* **استفاده از یک کلید AvalAI:** Claude Code را بدون نیاز به حساب جداگانه Anthropic، با کلید API AvalAI اجرا کنید
* **دسترسی به بیش از 410 مدل:** از Claude Opus 4.8، Claude 5 Sonnet و Claude Haiku 4.5 استفاده کنید؛ همچنین بسیاری از مدل‌های متن‌باز و شخص ثالث مانند GLM-5.2، Kimi K2.7 Code، Gemini 3.1 Pro و GPT-5.5 از طریق همان نقطه پایانی سازگار با Anthropic در دسترس هستند
* **کدنویسی کاملا عاملی:** کد تولید کنید، بازسازی انجام دهید، اشکال‌زدایی کنید، دستورات را اجرا کنید و فایل‌ها را مستقیما از CLI ویرایش کنید
* **API سازگار با Anthropic:** AvalAI نقطه پایانی سازگار با Anthropic را ارائه می‌دهد، بنابراین Claude Code فقط با چند متغیر محیطی کار می‌کند
* **مقرون‌به‌صرفه بودن:** از قیمت‌گذاری رقابتی AvalAI که با نرخ‌های ارائه‌دهندگان اصلی همسو است بهره‌مند شوید
* **انعطاف‌پذیری:** بهترین مدل را برای هر کار انتخاب کنید—استدلال عمیق، کدنویسی سریع یا توسعه مقرون‌به‌صرفه

## دریافت کلید API از AvalAI (راهنمای گام به گام)

برای دریافت کلید API خود، این مراحل را دنبال کنید:

1. **ایجاد حساب کاربری AvalAI:**
   اگر هنوز حساب کاربری ندارید، به [داشبورد AvalAI](https://chat.avalai.ir/platform/home) مراجعه کرده و ثبت‌نام کنید.

2. **ورود به بخش کلیدهای API:**
   پس از ورود، به بخش «کلیدهای API» در داشبورد بروید.

3. **ایجاد کلید جدید:**
   روی دکمه «ساخت کلید جدید» یا «Create secret key» کلیک کنید.

4. **نام‌گذاری کلید (اختیاری):**
   برای مدیریت بهتر، نامی مانند «Claude Code Development» برای کلید خود انتخاب کنید.

5. **کپی و ذخیره‌سازی کلید API:**
   کلید تولیدشده فقط یک بار نمایش داده می‌شود. **مهم:** آن را فورا کپی کرده و در جای امن نگه دارید؛ به دلایل امنیتی امکان مشاهده دوباره کلید کامل وجود ندارد.

## نصب Claude Code

اگر هنوز Claude Code را نصب نکرده‌اید، ابتدا CLI را نصب کنید.

در macOS، Linux یا WSL از نصب‌کننده رسمی استفاده کنید:

```bash
curl -fsSL https://claude.ai/install.sh | bash
```

در Windows، ابتدا Node.js نسخه 18 یا بالاتر را نصب کنید، سپس PowerShell را با دسترسی Administrator باز کنید و Claude Code را با npm نصب کنید:

```powershell
npm install -g @anthropic-ai/claude-code
```

در macOS، Linux یا WSL هم اگر npm را ترجیح می‌دهید می‌توانید از همین دستور استفاده کنید.

نصب را بررسی کنید:

```bash
claude --version
```

## پیکربندی Claude Code برای AvalAI (روش مستقیم و توصیه‌شده)

Claude Code پیکربندی ارائه‌دهنده را از متغیرهای محیطی می‌خواند. از آنجا که AvalAI به‌صورت بومی [Messages API (`v1/messages`)](fa/api-reference/messages.md) سازگار با Anthropic را ارائه می‌دهد، می‌توانید Claude Code را بدون پراکسی یا لایه ترجمه مستقیما به AvalAI متصل کنید.

متغیرهای زیر را در ترمینال تنظیم کنید:

**macOS / Linux (bash یا zsh):**

```bash
export ANTHROPIC_BASE_URL="https://api.avalai.ir"
export ANTHROPIC_AUTH_TOKEN="your-avalai-api-key"
export ANTHROPIC_MODEL="claude-opus-5"
export ANTHROPIC_SMALL_FAST_MODEL="claude-haiku-4-5"
```

عملکرد هر متغیر:

* **`ANTHROPIC_BASE_URL`** — درخواست‌های Claude Code را به نقطه پایانی سازگار با Anthropic در AvalAI هدایت می‌کند (`https://api.avalai.ir`).
* **`ANTHROPIC_AUTH_TOKEN`** — کلید API AvalAI شماست. Claude Code آن را به‌عنوان توکن احراز هویت ارسال می‌کند.
* **`ANTHROPIC_MODEL`** — مدل اصلی Claude Code برای استدلال و کدنویسی.
* **`ANTHROPIC_SMALL_FAST_MODEL`** — مدل کوچک‌تر و سریع‌تر برای وظایف سبک پس‌زمینه مانند خلاصه‌سازی یا تولید عنوان. انتخاب مدل اقتصادی در این بخش به کاهش هزینه کمک می‌کند.

?> **نکته امنیتی:** کلید را در فایل‌های پروژه ذخیره نکنید. از متغیر محیطی مانند `ANTHROPIC_AUTH_TOKEN` استفاده کنید و هرگز کلید API خود را در سیستم کنترل نسخه ثبت نکنید.

### دائمی کردن تنظیمات

برای جلوگیری از وارد کردن دوباره متغیرها در هر ترمینال جدید، آن‌ها را به فایل پیکربندی شل اضافه کنید.

1. فایل پیکربندی Zsh را باز کنید (شل پیش‌فرض در macOS):

   ```bash
nano ~/.zshrc
```

2. در انتهای فایل، تنظیمات AvalAI را اضافه کنید:

   ```bash
# AvalAI configuration for Claude Code
export ANTHROPIC_BASE_URL="https://api.avalai.ir"
export ANTHROPIC_AUTH_TOKEN="your-avalai-api-key"
export ANTHROPIC_MODEL="claude-opus-5"
export ANTHROPIC_SMALL_FAST_MODEL="claude-haiku-4-5"
```

3. برای ذخیره `Ctrl + O` و سپس `Enter` را بزنید، و برای خروج `Ctrl + X` را فشار دهید.

4. تغییرات را در ترمینال فعلی اعمال کنید:

   ```bash
source ~/.zshrc
```

> **نکته:** اگر از bash استفاده می‌کنید، همین خطوط را به `~/.bashrc` یا `~/.bash_profile` اضافه کرده و سپس دستور مناسب مانند `source ~/.bashrc` را اجرا کنید.

**Windows (PowerShell):**

یک پنجره PowerShell جدید باز کنید و متغیرها را برای همان نشست تنظیم کنید:

```powershell
$env:ANTHROPIC_BASE_URL = "https://api.avalai.ir"
$env:ANTHROPIC_AUTH_TOKEN = "your-avalai-api-key"
$env:ANTHROPIC_API_KEY = $env:ANTHROPIC_AUTH_TOKEN
$env:ANTHROPIC_MODEL = "claude-opus-5"
$env:ANTHROPIC_SMALL_FAST_MODEL = "claude-haiku-4-5"
```

!> **نکته اجرای اول در Windows:** در نصب تازه روی Windows، اگر فقط `ANTHROPIC_AUTH_TOKEN` تنظیم شده باشد، Claude Code ممکن است هنوز صفحه ورود Anthropic را در مرورگر باز کند. تنظیم `ANTHROPIC_API_KEY` با همان کلید AvalAI باعث می‌شود Claude Code هنگام راه‌اندازی یک کلید API سفارشی را تشخیص دهد. وقتی Claude Code پرسید آیا می‌خواهید از کلید API سفارشی شناسایی‌شده استفاده کنید، گزینه **Yes** را انتخاب کنید.

برای دائمی کردن تنظیمات در Windows، از API متغیرهای محیطی کاربر در PowerShell استفاده کنید؛ سپس PowerShell را ببندید و دوباره باز کنید:

```powershell
[Environment]::SetEnvironmentVariable("ANTHROPIC_BASE_URL", "https://api.avalai.ir", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_AUTH_TOKEN", "your-avalai-api-key", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_API_KEY", "your-avalai-api-key", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_MODEL", "claude-opus-5", "User")
[Environment]::SetEnvironmentVariable("ANTHROPIC_SMALL_FAST_MODEL", "claude-haiku-4-5", "User")
```

پس از باز کردن دوباره PowerShell، بررسی کنید که Windows مقادیر را می‌بیند:

```powershell
echo $env:ANTHROPIC_BASE_URL
echo $env:ANTHROPIC_AUTH_TOKEN
echo $env:ANTHROPIC_API_KEY
```

### روش جایگزین: فایل تنظیمات پروژه یا کاربر

به‌جای متغیرهای محیطی، می‌توانید همین تنظیمات را در فایل تنظیمات Claude Code قرار دهید. فایل `~/.claude/settings.json` (سطح کاربر) یا `.claude/settings.json` (سطح پروژه) را ایجاد یا ویرایش کنید:

```json
{
  "env": {
    "ANTHROPIC_BASE_URL": "https://api.avalai.ir",

    "ANTHROPIC_AUTH_TOKEN": "your-avalai-api-key",
    "ANTHROPIC_API_KEY": "your-avalai-api-key",
    "ANTHROPIC_MODEL": "claude-opus-5",
    "ANTHROPIC_SMALL_FAST_MODEL": "claude-haiku-4-5"
  }
}
```

!> **مهم:** اگر فایل پروژه‌ای `.claude/settings.json` را در Git ثبت می‌کنید، کلید واقعی API را داخل آن قرار ندهید. کلید را در متغیر محیطی نگه دارید و فایل تنظیمات را برای مقادیر غیرحساس مانند `ANTHROPIC_BASE_URL` و نام مدل‌ها استفاده کنید.

## اجرای Claude Code

پس از تنظیم متغیرهای محیطی، Claude Code را از دایرکتوری پروژه اجرا کنید:

```bash
cd /path/to/your/project
claude
```

در PowerShell ویندوز، از مسیرهای ویندوزی استفاده کنید:

```powershell
cd C:\path\to\your\project
claude
```

Claude Code یک نشست تعاملی را با استفاده از نقطه پایانی AvalAI و مدلی که انتخاب کرده‌اید شروع می‌کند. برای بررسی اتصال، یک درخواست ساده را امتحان کنید:

```text
درباره این پروژه به من بگو
```

اگر پاسخ عادی دریافت کردید، یکپارچه‌سازی شما فعال است! 🎉

### بررسی پیکربندی فعال

داخل نشست Claude Code می‌توانید وضعیت فعلی را بررسی یا مدل را تغییر دهید:

* **`/status`** — نشان می‌دهد کدام نقطه پایانی API و کدام مدل‌ها نشست فعلی را سرویس‌دهی می‌کنند.
* **`/model`** — مدل‌های در دسترس را نمایش می‌دهد یا مدل نشست فعلی را تغییر می‌دهد.

### تغییر موقت مدل

می‌توانید مدل را فقط برای یک اجرا تغییر دهید، بدون اینکه فایل‌های شل را ویرایش کنید:

```bash
# اجرای نشست با یک مدل مشخص
claude --model claude-sonnet-5

# یا تنظیم inline برای یک اجرا
ANTHROPIC_MODEL="claude-opus-5" claude
```

## استفاده از مدل‌های سایر ارائه‌دهندگان

Claude Code به مدل‌های Claude محدود نیست. از آنجا که بسیاری از مدل‌های AvalAI از طریق [Messages API (`v1/messages`)](fa/api-reference/messages.md) نیز ارائه می‌شوند، می‌توانید مقدار `ANTHROPIC_MODEL` را به مدل‌های متن‌باز و شخص ثالث هم تغییر دهید—بدون پراکسی.

```bash
# مدل‌های متن‌باز
export ANTHROPIC_MODEL="glm-5.2"
export ANTHROPIC_MODEL="kimi-k2.7-code"

# Google Gemini
export ANTHROPIC_MODEL="gemini-3.1-pro-preview"

# OpenAI
export ANTHROPIC_model="gpt-5.6-luna"
```

!> **نکته سازگاری:** بیشتر مدل‌های AvalAI روی نقطه پایانی `v1/messages` کار می‌کنند، اما سازگاری کامل برای تک‌تک مدل‌ها تضمین نمی‌شود—برخی مدل‌ها ممکن است فرمت Messages یا ساختار Tool Calling آن را کامل پشتیبانی نکنند. اگر مدل خاصی با Claude Code درست کار نکرد، لطفا با [پشتیبانی AvalAI](https://chat.avalai.ir/platform/home) تماس بگیرید تا برای سازگار کردن آن با Messages endpoint کمک کنیم.

?> **مشاهده مدل‌های جدید:** برای دیدن جدیدترین مدل‌های اضافه‌شده و شناسه آن‌ها، [اخبار AvalAI](fa/news/index.md) را بررسی کنید.

## آیا به پراکسی یا LiteLLM نیاز دارم؟

**خیر.** AvalAI به‌صورت بومی [Messages API (`v1/messages`)](fa/api-reference/messages.md) سازگار با Anthropic را ارائه می‌دهد؛ یعنی همان نقطه پایانی که Claude Code با آن کار می‌کند. بنابراین برای مدل‌های پشتیبانی‌شده، روش مستقیم بالا ساده‌ترین و توصیه‌شده‌ترین راه است.

پراکسی ترجمه فقط زمانی مطرح می‌شود که بخواهید Claude Code را با مدلی اجرا کنید که فقط فرمت OpenAI Chat Completions را پشتیبانی می‌کند و اصلا با Anthropic Messages API سازگار نیست. از آنجا که AvalAI مدل‌های Claude و بسیاری از مدل‌های دیگر را روی endpoint بومی Messages ارائه می‌دهد، معمولا نیازی به این پیچیدگی ندارید.

?> **توصیه:** از روش مستقیم استفاده کنید: `ANTHROPIC_BASE_URL` را روی `https://api.avalai.ir` و `ANTHROPIC_AUTH_TOKEN` را روی کلید AvalAI خود قرار دهید.

## انتخاب مدل مناسب

AvalAI دسترسی به بیش از 410 مدل را فراهم می‌کند. در ادامه چند پیشنهاد برای وظایف کدنویسی با Claude Code آمده است:

### برای تولید کد پیچیده و استدلال
* **Claude Opus 4.8** (`claude-opus-4-8`) - بهترین گزینه برای استدلال پیچیده و کدبیس‌های بزرگ
* **Claude 5 Sonnet** (`claude-sonnet-5`) - تعادل عالی بین سرعت و کیفیت
* **GPT-5.5** (`gpt-5.5`) - عالی برای حل مسائل پیشرفته

### برای کدنویسی عاملی سریع و کارآمد
* **Claude Haiku 4.5** (`claude-haiku-4-5`) - سریع و کارآمد؛ گزینه مناسب برای نقش `ANTHROPIC_SMALL_FAST_MODEL`
* **Claude 5 Sonnet** (`claude-sonnet-5`) - عملکرد قوی برای کدنویسی روزمره
* **Kimi K2.7 Code** (`kimi-k2.7-code`) - مدل متن‌باز قدرتمند برای گردش‌کارهای عاملی

### برای توسعه مقرون‌به‌صرفه
* **GLM-5.2** (`glm-5.2`) - مدل متن‌باز توانمند با هزینه کمتر
* **Gemini 3.1 Pro** (`gemini-3.1-pro-preview`) - سریع، چندوجهی و اقتصادی

?> **نکته:** یک مدل اصلی قدرتمند (`ANTHROPIC_MODEL`) را با یک مدل کوچک و اقتصادی (`ANTHROPIC_SMALL_FAST_MODEL`) ترکیب کنید تا بین کیفیت و هزینه تعادل برقرار شود. Claude Code وظایف سبک پس‌زمینه را خودکار به مدل کوچک‌تر می‌فرستد.

## نکات و بهترین شیوه‌ها

* **ذخیره‌سازی امن:** با کلید API AvalAI مثل رمز عبور رفتار کنید. آن را از متغیر محیطی بخوانید و هرگز در Git ثبت نکنید.
* **مدل کوچک و سریع:** مقدار `ANTHROPIC_SMALL_FAST_MODEL` را روی مدلی اقتصادی مثل `claude-haiku-4-5` بگذارید تا وظایف پس‌زمینه ارزان‌تر انجام شوند.
* **نقاط بازگشت Git:** Claude Code می‌تواند کدبیس شما را تغییر دهد. قبل و بعد از هر وظیفه، checkpoint یا commit ایجاد کنید تا در صورت نیاز تغییرات را برگردانید.
* **فایل CLAUDE.md:** یک فایل `CLAUDE.md` به مخزن اضافه کنید تا راهنمایی ثابت درباره دستورات ساخت، قراردادها و انتظارات پروژه به Claude Code بدهید.
* **محدودیت‌های نرخ:** به [محدودیت‌های نرخ](fa/guides/rate-limits.md) AvalAI توجه کنید. بیشتر وظایف کدنویسی در محدوده باقی می‌مانند، اما در اجراهای عاملی بزرگ مراقب باشید.
* **پایش هزینه:** مصرف خود را از داشبورد AvalAI پیگیری کنید تا هزینه‌ها را کنترل و انتخاب مدل را بهینه کنید.

## عیب‌یابی

* **خطای کلید API نامعتبر / احراز هویت:**
    - بررسی کنید متغیر `ANTHROPIC_AUTH_TOKEN` تنظیم شده باشد: در macOS/Linux دستور `echo $ANTHROPIC_AUTH_TOKEN` و در PowerShell دستور `echo $env:ANTHROPIC_AUTH_TOKEN` را اجرا کنید.
    - در اولین اجرای Windows، متغیر `ANTHROPIC_API_KEY` را هم با دستور `echo $env:ANTHROPIC_API_KEY` بررسی کنید؛ این کار مانع برگشت Claude Code به جریان ورود مرورگری Anthropic می‌شود.
    - پس از تنظیم متغیر، ترمینال را مجددا باز کنید یا `source ~/.zshrc` را اجرا کنید.
    - مطمئن شوید کلید در داشبورد AvalAI فعال است.

* **درخواست‌ها هنوز به Anthropic ارسال می‌شوند:**
    - مطمئن شوید `ANTHROPIC_BASE_URL` دقیقا `https://api.avalai.ir` باشد (در روش مستقیم، `/v1` اضافه نکنید).
    - داخل Claude Code دستور `/status` را اجرا کنید تا endpoint فعال را ببینید.
    - اگر قبلا با حساب Anthropic وارد شده‌اید، از آن خارج شوید تا Claude Code از متغیرهای محیطی استفاده کند.

* **مشکلات اتصال:**
    - اتصال اینترنت خود را بررسی کنید.
    - مطمئن شوید هیچ فایروال یا پراکسی دسترسی به `https://api.avalai.ir` را مسدود نمی‌کند.

* **خطای یافت نشدن مدل (Model Not Found):**
    - شناسه مدل را بررسی کنید (به [نمای کلی مدل‌های AvalAI](fa/models/model-details.md) مراجعه کنید).
    - یک مدل رایج مانند `claude-opus-4-8` یا `claude-sonnet-5` را امتحان کنید.
    - برای مدل‌های جدید، [اخبار AvalAI](fa/news/index.md) را ببینید.

* **خرابی Tool Calling یا اقدامات عاملی:**
    - مطمئن شوید مدل انتخابی از Tool Calling پشتیبانی می‌کند.
    - مدل‌های Claude در AvalAI از Tool Calling روی [Messages API](fa/api-reference/messages.md) پشتیبانی می‌کنند.
    - اگر مدل غیر Claude خاصی درست کار نمی‌کند، با [پشتیبانی AvalAI](https://chat.avalai.ir/platform/home) تماس بگیرید تا سازگاری آن با `v1/messages` بررسی شود.

* **خطاهای محدودیت نرخ:**
    - [محدودیت‌های نرخ](fa/guides/rate-limits.md) مربوط به سطح (Tier) خود را بررسی کنید.
    - کمی صبر کنید و دوباره تلاش کنید، یا برای محدودیت‌های بالاتر ارتقای سطح را در نظر بگیرید.

## نتیجه‌گیری

یکپارچه‌سازی AvalAI با Claude Code سریع و ساده است: کافی است `ANTHROPIC_BASE_URL` را روی AvalAI بگذارید، کلید AvalAI خود را در `ANTHROPIC_AUTH_TOKEN` تنظیم کنید و مدل‌های دلخواه را انتخاب کنید. از آنجا که AvalAI به‌صورت بومی از `v1/messages` پشتیبانی می‌کند، برای استفاده معمول به پراکسی یا LiteLLM نیاز ندارید.

با این تنظیمات می‌توانید قابلیت‌های عاملی Claude Code را در ترمینال خود، همراه با قیمت‌گذاری رقابتی AvalAI و دسترسی به بیش از 410 مدل، استفاده کنید.

## منابع مرتبط

- [مرجع API AvalAI: مقدمه](fa/api-reference/introduction.md)
- [Messages API سازگار با Anthropic در AvalAI](fa/api-reference/messages.md)
- [نمای کلی مدل‌های AvalAI](fa/models/model-details.md)
- [اخبار و مدل‌های جدید](fa/news/index.md)
- [راهنمای محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [یکپارچه‌سازی AvalAI با OpenAI Codex](fa/guides/setup-codex.md)
- [یکپارچه‌سازی AvalAI با افزونه‌های VSCode](fa/guides/setup-vscode.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [مستندات رسمی Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview)
