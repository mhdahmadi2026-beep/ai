---
hasH1: true
---

# عملکرد AvalAI

در این صفحه، عملکرد AvalAI را از چند زاویه بررسی می‌کنیم: میزان استفاده از cache پرامپت، تأخیر در مناطق مختلف، سرعت تولید توکن و شیوه درست اندازه‌گیری در محیط عملیاتی. تازه‌ترین آزمایش‌ها بالاتر آمده‌اند. این اعداد نتیجه چند اجرای مشخص‌اند و نباید آن‌ها را تضمین همیشگی سرویس در نظر گرفت.

## گزارش‌های ۱۴۰۵-۰۵-۲۳

### نتیجه‌های cache در هر دو endpoint متنی OpenAI

آخرین نسخه بنچمارک، درخواست واقع‌گرایانه تحلیل سند حقوقی را از طریق AvalAI و provider رسمی هر مدل روی `v1/chat/completions` و `v1/responses` می‌فرستد. دور اول cache هر سرویس را آماده می‌کند، runner به‌مدت 15 ثانیه صبر می‌کند و دورهای 2 تا 5 رفتار cache در حالت warm را می‌سنجند. یک درخواست فقط زمانی cache hit محسوب می‌شود که API تعداد توکن‌های cacheشده را گزارش کند—عمدتا با نسبت `usage.prompt_tokens_details.cached_tokens / usage.prompt_tokens`—نه بر اساس ترتیب درخواست، زمان پاسخ یا فرض ثابت بودن prefix.

این نتیجه‌ها مشاهدات یک اجرای مشخص با پنج دور paired و ترتیبی برای هر API و سه مدل `deepseek-v4-flash`، `glm-5.2` و `kimi-k3` هستند. داده‌ها رفتار مشاهده‌شده در همین اجرا را نشان می‌دهند و تضمین سطح سرویس نیستند.

### `deepseek-v4-flash`: مقایسه AvalAI و DeepSeek

هر دو سرویس در هر دو API تمام 5 درخواست را با موفقیت پاسخ دادند. AvalAI در همه دورها **99.9%** cache hit گزارش کرد (1,400 توکن از 1,401 توکن)، درحالی‌که DeepSeek به **95.1%** رسید (1,408 توکن از 1,480 توکن). بنابراین اختلاف warm در هر دو API به سود AvalAI **+4.8 واحد درصد** بود.

| سرویس | API | cache hit در حالت warm | میانگین latency | موفقیت |
| --- | --- | ---: | ---: | ---: |
| AvalAI | `v1/chat/completions` | **99.9%** | 1.704s | 5/5 |
| DeepSeek | `v1/chat/completions` | 95.1% | 6.201s | 5/5 |
| AvalAI | `v1/responses` | **99.9%** | 18.282s | 5/5 |
| DeepSeek | `v1/responses` | 95.1% | 6.444s | 5/5 |

![نسبت cache hit در هر دور Chat Completions برای DeepSeek Flash](/fa/_media/img/cache_hit_bar_deepseek-v4-flash_chat_completions_20260814_175107.png)

![میانگین تجمعی cache hit در Chat Completions برای DeepSeek Flash](/fa/_media/img/cache_hit_line_deepseek-v4-flash_chat_completions_20260814_175107.png)

![نسبت cache hit در هر دور Responses برای DeepSeek Flash](/fa/_media/img/cache_hit_bar_deepseek-v4-flash_responses_20260814_175107.png)

![میانگین تجمعی cache hit در Responses برای DeepSeek Flash](/fa/_media/img/cache_hit_line_deepseek-v4-flash_responses_20260814_175107.png)

### `glm-5.2`: مقایسه AvalAI و Z.AI

در `v1/chat/completions` هر دو سرویس تمام 5 درخواست را پاسخ دادند و به **99.9%** cache hit در حالت warm رسیدند. AvalAI در دورهای 2 تا 5 تعداد 1,409 توکن از 1,410 توکن و Z.AI تعداد 1,408 توکن از 1,410 توکن را cacheشده گزارش کرد. در `v1/responses`، AvalAI هر 5 درخواست را با موفقیت پاسخ داد و پس از دور آماده‌سازی به **99.9%** رسید. Z.AI برای هر پنج درخواست خطای `404 Not Found` برگرداند، زیرا base URL عمومی آزمایش‌شده این endpoint را ارائه نمی‌کند؛ این خطاها نتیجه دسترس‌پذیری endpoint هستند، نه درخواست‌های موفق با cache hit صفر درصد.

| سرویس | API | cache hit در حالت warm | میانگین latency | موفقیت |
| --- | --- | ---: | ---: | ---: |
| AvalAI | `v1/chat/completions` | **99.9%** | 20.394s | 5/5 |
| Z.AI | `v1/chat/completions` | 99.9% | 4.971s | 5/5 |
| AvalAI | `v1/responses` | **99.9%** | 2.830s | 5/5 |
| Z.AI | `v1/responses` | در دسترس نیست | — | 0/5 |

![نسبت cache hit در هر دور Chat Completions برای GLM-5.2](/fa/_media/img/cache_hit_bar_glm-5.2_chat_completions_20260814_175704.png)

![میانگین تجمعی cache hit در Chat Completions برای GLM-5.2](/fa/_media/img/cache_hit_line_glm-5.2_chat_completions_20260814_175704.png)

![نسبت cache hit در هر دور Responses برای GLM-5.2](/fa/_media/img/cache_hit_bar_glm-5.2_responses_20260814_175704.png)

![میانگین تجمعی cache hit در Responses برای GLM-5.2](/fa/_media/img/cache_hit_line_glm-5.2_responses_20260814_175704.png)

### `kimi-k3`: مقایسه AvalAI و Moonshot AI

هر دو سرویس تمام 5 درخواست Chat Completions را پاسخ دادند و در تمام دورها **85.8%** cache hit گزارش کردند (1,280 توکن از 1,492 توکن). AvalAI در Responses نیز هر 5 درخواست را با **85.8%** cache hit پاسخ داد. API عمومی آزمایش‌شده Moonshot درخواست‌های `v1/responses` را نپذیرفت: چهار درخواست با خطای دسترسی و یک درخواست با خطای اتصال روبه‌رو شد. AvalAI همچنان درخواست Responses این مدل را می‌پذیرد و آن را در لایه مسیریابی داخلی به جریان سازگار بالادستی تبدیل می‌کند.

| سرویس | API | cache hit در حالت warm | میانگین latency | موفقیت |
| --- | --- | ---: | ---: | ---: |
| AvalAI | `v1/chat/completions` | **85.8%** | 4.187s | 5/5 |
| Moonshot AI | `v1/chat/completions` | 85.8% | 7.819s | 5/5 |
| AvalAI | `v1/responses` | **85.8%** | 4.401s | 5/5 |
| Moonshot AI | `v1/responses` | در دسترس نیست | — | 0/5 |

![نسبت cache hit در هر دور Chat Completions برای Kimi K3](/fa/_media/img/cache_hit_bar_kimi-k3_chat_completions_20260814_180128.png)

![میانگین تجمعی cache hit در Chat Completions برای Kimi K3](/fa/_media/img/cache_hit_line_kimi-k3_chat_completions_20260814_180128.png)

![نسبت cache hit در هر دور Responses برای Kimi K3](/fa/_media/img/cache_hit_bar_kimi-k3_responses_20260814_180128.png)

![میانگین تجمعی cache hit در Responses برای Kimi K3](/fa/_media/img/cache_hit_line_kimi-k3_responses_20260814_180128.png)

### روش اجرا و بازتولید

runner درخواست‌ها را به‌صورت ترتیبی—ابتدا AvalAI و سپس provider رسمی—ارسال می‌کند و برای دورهای Responses یک زنجیره مستقل `previous_response_id` برای هر سرویس می‌سازد. artifact مربوط به JSON، شیء کامل `usage` گزارش‌شده توسط provider را برای بررسی مستقل نگه می‌دارد؛ اما این مستندات عمدا هیچ مسیر محلی یا credential را منتشر نمی‌کنند.

```bash
python tests/benchmarks/test_cache_hit_ratio.py \
  --model deepseek-v4-flash --rounds 5 --prefix-tokens 2000 \
  --official-provider deepseek

python tests/benchmarks/test_cache_hit_ratio.py \
  --model glm-5.2 --rounds 5 --prefix-tokens 2000 \
  --official-provider zai

python tests/benchmarks/test_cache_hit_ratio.py \
  --model kimi-k3 --rounds 5 --prefix-tokens 2000 \
  --official-provider moonshot.ai
```

#### سورس کامل بنچمارک

نسخه کامل و اصلاح‌شده اسکریپت از هر دو API، زنجیره مستقل Responses برای هر سرویس، شکل‌های مختلف `usage` در APIهای سازگار با OpenAI و Anthropic، تشخیص خودکار provider و aliasها، محافظ stream در برابر توقف، artifactهای JSON و نمودارهای جداگانه هر endpoint پشتیبانی می‌کند. کلیدهای API از flagها یا environment variableهای استاندارد خوانده می‌شوند و هرگز داخل artifact نوشته نمی‌شوند.

<details>
<summary>نمایش سورس کامل بنچمارک</summary>

<<< ../tests/benchmarks/test_cache_hit_ratio.py{python}

</details>

### دامنه و محدودیت‌ها

این سه آزمایش پنج‌دوره‌ای در تاریخ ۱۴۰۵-۰۵-۲۳ مشاهده شده‌اند. خطای Responses در provider رسمی یعنی endpoint موردنظر در API عمومی آزمایش‌شده در دسترس نبوده است؛ این خطا نباید به‌عنوان cache hit صفر درصد برای یک درخواست موفق تفسیر شود. latency تحت‌تأثیر شرایط مدل و شبکه است و یک درخواست کند می‌تواند میانگین پنج‌دوره‌ای را به‌شکل محسوسی تغییر دهد. برنامه باید در صورت cache miss نیز درست کار کند و نباید affinity را جایگزین state مکالمه بداند. برای جزئیات پیاده‌سازی، [راهنمای cache پرامپت](/fa/guides/prompt-caching.md) را ببینید.

## راهنمای بهینه‌سازی عملکرد

### بهتر کردن cache-hit ratio

- instructions ثابت، متن policy، schema ابزارها، تصاویر و مثال‌های قابل reuse را ابتدا و context پویا و timestampها را انتها قرار دهید.
- prefix را از نظر byte کاملا یکسان نگه دارید و `usage.prompt_tokens_details.cached_tokens` یا فیلد native ارائه‌دهنده را بررسی کنید.
- درخواست‌های warm را جدا از priming مقایسه کنید و مدل، route، نسخه prompt، request ID و timestampها را ثبت کنید.

### کاهش latency و افزایش throughput

- با کوچک‌ترین مدلی شروع کنید که evalهای شما را پاس می‌کند و مدل‌های reasoning بزرگ‌تر را برای تصمیم‌های سخت نگه دارید.
- خروجی را با `max_output_tokens` برای `/v1/responses` یا `max_completion_tokens` برای `/v1/chat/completions` محدود کنید.
- خروجی کاربرمحور را stream کنید، فقط کارهای مستقل را موازی اجرا کنید و connectionهای HTTP را reuse کنید.
- فراخوانی‌های غیرضروری مدل را حذف و مراحل نزدیک را در صورت امکان در یک structured response ترکیب کنید.

### اندازه‌گیری رفتار production

TTFT/TTFB، latency کل، مدل، endpoint، توکن‌های input/output/cacheشده، request ID، status و تعداد retry/fallback را log کنید. به‌جای اتکا به یک میانگین، p50، p90 و p95 را گزارش کنید. این صفحه را کنار [بهینه‌سازی latency](/fa/guides/latency-optimization.md) و [بهینه‌سازی هزینه](/fa/guides/cost-optimization.md) بخوانید.

## بنچمارک‌های latency منطقه‌ای

مطالعه‌های latency زیر از دامنه اصلی AvalAI یعنی `api.avalai.ir` استفاده کردند و برای مقایسه یکسان زیرساخت اصلی، Guardrail غیرفعال بود. Guardrail برای بیشتر اپلیکیشن‌ها توصیه می‌شود، اما در این تست‌های تاریخی حدود 200 تا 300 میلی‌ثانیه latency اضافه می‌کرد. دامنه جایگزین اتصال یعنی `api.avalapis.ir` ذاتا latency بیشتری دارد و در این تست‌ها استفاده نشد.

AvalAI connectionهای پایدار و connection poolهای provider را نگه می‌دارد و بهینه‌سازی پردازش درخواست، شبکه و فراخوانی تکراری سربار پلتفرم را کم می‌کند. موقعیت جغرافیایی، بار مدل، طول خروجی، تنظیمات امنیتی و شرایط شبکه همچنان بر هر اندازه‌گیری اثر دارند.

## جدیدترین latency منطقه‌ای - ۲۰-۰۷-۱۴۰۴

### عملکرد مرکز داده اروپا (EU) - ۲۰-۰۷-۱۴۰۴

این تست از یک ماشین مجازی در یک مرکز داده Azure در اتحادیه اروپا انجام شد و عملکرد AvalAI را با فراخوانی مستقیم API OpenAI از همان مکان مقایسه می‌کند.

**محیط تست:**
* **مدل:** `gpt-4o-mini`
* **ارائه دهنده ابری:** Microsoft Azure
* **سخت‌افزار:** 4GB RAM، 2 vCPUs
* **مکان:** اروپا

#### نتایج عملکرد اروپا

| معیار | AvalAI (gpt-4o-mini) | OpenAI (gpt-4o-mini) |
| ------------------------ | -------------------- | -------------------- |
| **میانگین TTFB (ثانیه)** | 0.435 | 0.717 |
| **میانه TTFB (ثانیه)** | 0.393 | 0.685 |
| **صدک ۹۵ TTFB (ثانیه)** | 0.605 | 1.032 |
| **میانگین توکن در ثانیه**| 24.5 | 13.8 |
| **نرخ موفقیت** | 100.00% | 100.00% |

![مقایسه عملکرد API در اروپا](_media/img/api_performance_comparison_20251012_a.png ':size=1000')

#### تحلیل

نتایج خودگویاست: **AvalAI اکنون ۳۹٪ سریع‌تر از دسترسی مستقیم به OpenAI** از مرکز داده اروپایی ما است. میانه TTFB ما ۰.۳۹۳ ثانیه در مقایسه با ۰.۶۸۵ ثانیه OpenAI، به همراه توان عملیاتی توکن ۷۷٪ بالاتر (۲۴.۵ در مقابل ۱۳.۸ توکن/ثانیه)، نشان می‌دهد که یک پلتفرم API یکپارچه با معماری خوب می‌تواند از دسترسی مستقیم به ارائه‌دهنده بهتر عمل کند.

این مزیت عملکردی از اتصالات پایدار ما به زیرساخت OpenAI و مدیریت بهینه‌شده درخواست‌های ما ناشی می‌شود. درحالی‌که کاربران فردی باید اتصالات را برقرار کرده و سربار را با هر درخواست مدیریت کنند، سیستم با ترافیک بالای ما اتصالات گرم و مسیرهای بهینه‌شده به تمام ارائه‌دهندگان را حفظ می‌کند. بهینه‌سازی‌های اخیر زیرساخت ما هر سربار داخلی را بیشتر کاهش داده است که منجر به عملکرد برتری شده که در این بنچمارک‌ها نشان داده شده است.

---

### عملکرد مرکز داده خاورمیانه (ME) - ۲۰-۰۷-۱۴۰۴

این تست از یک ماشین مجازی در یک مرکز داده Arvancloud در خاورمیانه انجام شد و عملکرد AvalAI را با فراخوانی مستقیم API OpenAI از همان مکان مقایسه می‌کند.

**محیط تست:**
* **مدل:** `gpt-4o-mini`
* **ارائه دهنده ابری:** Arvancloud
* **سخت‌افزار:** 4GB RAM، 2 vCPUs
* **مکان:** خاورمیانه

#### نتایج عملکرد خاورمیانه

| معیار | AvalAI (gpt-4o-mini) | OpenAI (gpt-4o-mini) |
| ------------------------ | -------------------- | -------------------- |
| **میانگین TTFB (ثانیه)** | 0.703 | 1.246 |
| **میانه TTFB (ثانیه)** | 0.668 | 1.048 |
| **صدک ۹۵ TTFB (ثانیه)**| 0.947 | 2.309 |
| **میانگین توکن در ثانیه**| 14.9 | 8.4 |
| **نرخ موفقیت** | 100.00% | 100.00% |

![مقایسه عملکرد API در خاورمیانه](_media/img/api_performance_comparison_20251012_b.png ':size=1000')

#### تحلیل

مزیت عملکردی حتی برای کاربران خاورمیانه نیز برجسته‌تر است: **AvalAI ۴۴٪ زمان پاسخ سریع‌تر** با میانه TTFB ۰.۶۶۸ ثانیه در مقایسه با ۱.۰۴۸ ثانیه OpenAI ارائه می‌دهد. توان عملیاتی توکن ۷۷٪ بالاتر است (۱۴.۹ در مقابل ۸.۴ توکن/ثانیه) که تجربه بسیار بهتری برای استقرارهای منطقه‌ای فراهم می‌کند.

موقعیت استراتژیک زیرساخت ما و مسیرهای مسیریابی بهینه‌شده، به همراه اتصالات پایدار به ارائه‌دهندگان و بهینه‌سازی‌های اخیر، عملکرد استثنایی را برای کاربران در این منطقه ارائه می‌دهد. فاصله عملکردی در مقایسه با دسترسی مستقیم به OpenAI از زمان بنچمارک‌های خردادماه به‌طور قابل‌توجهی افزایش یافته است که تاثیر تلاش‌های بهینه‌سازی ما را نشان می‌دهد.

---

## عملکرد تاریخی - خرداد ۱۴۰۴

برای شفافیت و نمایش بهبود مستمر ما، نتایج بنچمارک قبلی خود را از خرداد ۱۴۰۴ حفظ می‌کنیم. این نتایج تاریخی نقطه شروع قبل از ابتکار بهینه‌سازی اخیر ما را نشان می‌دهند.

### عملکرد مرکز داده اروپا (EU) - تاریخ ۲۲-۰۳-۱۴۰۴

**محیط تست:**
* **مدل:** `gpt-4o-mini`
* **ارائه دهنده ابری:** Microsoft Azure
* **مکان:** اروپا

#### نتایج عملکرد اروپا (تاریخی)

| معیار | AvalAI (gpt-4o-mini) | OpenAI (gpt-4o-mini) |
| ------------------------ | -------------------- | -------------------- |
| **میانگین TTFB (ثانیه)** | 0.728 | 0.531 |
| **میانه TTFB (ثانیه)** | 0.683 | 0.510 |
| **صدک ۹۵ TTFB (ثانیه)** | 1.056 | 0.740 |
| **میانگین توکن در ثانیه**| 15.9 | 18.9 |
| **نرخ موفقیت** | 100.00% | 100.00% |

![مقایسه عملکرد API در اروپا - خرداد ۱۴۰۴](_media/img/api_performance_comparison_53111243.png ':size=1000')

#### تحلیل تاریخی

در خرداد ۱۴۰۴، AvalAI سربار تاخیر جزئی در حدود ۲۰۰ میلی‌ثانیه نسبت به فراخوانی مستقیم OpenAI از مراکز داده Azure نشان داد. این امر با توجه به میزبانی اصلی OpenAI بر روی زیرساخت Azure قابل انتظار بود. خدمات ارزش‌افزوده‌ای که ما ارائه می‌دادیم—مسیریابی API یکپارچه، لایه‌های امنیتی قوی و پشتیبانی از چند ارائه‌دهنده—با این سربار جزئی همراه بود.

### عملکرد مرکز داده خاورمیانه (ME) - تاریخ ۲۲-۰۳-۱۴۰۴

**محیط تست:**
* **مدل:** `gpt-4o-mini`
* **ارائه دهنده ابری:** Arvancloud
* **مکان:** خاورمیانه

#### نتایج عملکرد خاورمیانه (تاریخی)

| معیار | AvalAI (gpt-4o-mini) | OpenAI (gpt-4o-mini) |
| ------------------------ | -------------------- | -------------------- |
| **میانگین TTFB (ثانیه)** | 0.993 | 1.095 |
| **میانه TTFB (ثانیه)** | 0.929 | 0.951 |
| **صدک ۹۵ TTFB (ثانیه)**| 1.479 | 1.386 |
| **میانگین توکن در ثانیه**| 11.4 | 9.6 |
| **نرخ موفقیت** | 100.00% | 100.00% |

![مقایسه عملکرد API در خاورمیانه - خرداد ۱۴۰۴](_media/img/api_performance_comparison_53111244.png ':size=1000')

#### تحلیل تاریخی

حتی در خرداد ۱۴۰۴، AvalAI عملکرد رقابتی را برای کاربران خاورمیانه با تاخیر کمتر و توان عملیاتی بالاتر نسبت به دسترسی مستقیم به OpenAI ارائه می‌داد. نتایج مهرماه ما بهبودهای قابل‌توجه بیشتری را از تلاش‌های بهینه‌سازی ما نشان می‌دهد.

---

## بازتولید نتایج latency منطقه‌ای

ما به شفافیت کامل اعتقاد داریم. شما می‌توانید از اسکریپت پایتون زیر برای اجرای این تست‌های عملکردی خودتان استفاده کنید و نتایج ما را تایید کنید.

**توجه**: درحالی‌که این بنچمارک‌ها با استفاده از مدل **`gpt-4o-mini`** انجام شده‌اند، بهبودهای عملکردی برای تمام مدل‌های موجود در پلتفرم ما اعمال می‌شود. شما می‌توانید هر مدلی از انتخاب خود را با استفاده از این اسکریپت تست کنید تا ببینید AvalAI برای مورد استفاده خاص شما چگونه عمل می‌کند.

لطفا اطمینان حاصل کنید که کتابخانه‌های لازم (`requests`، `numpy`، `matplotlib`، `seaborn`، `tabulate`، `tqdm`) را نصب کرده‌اید.

```python
import os
import requests
import time
import numpy as np
import matplotlib.pyplot as plt
import json
from tabulate import tabulate
from tqdm import tqdm
from datetime import datetime
import seaborn as sns


def test_api_performance(
    api_name, api_url, api_key, model, num_requests=10, prompt="Say hi"
):
    """Test API performance and collect comprehensive metrics"""
    headers = {"Content-Type": "application/json", "Authorization": f"Bearer {api_key}"}
    data = {"model": model, "messages": [{"role": "user", "content": prompt}]}

    ttfb_times = []
    total_times = []
    token_counts = []
    tokens_per_second = []
    errors = 0

    print(f"Testing {api_name} API with {num_requests} requests...")
    for _ in tqdm(range(num_requests)):
        try:
            start_time = time.time()
            response = requests.post(
                api_url, headers=headers, json=data, timeout=(10, 30)
            )
            response_time = time.time()

            # Process the response
            response_json = response.json()
            end_time = time.time()

            # Calculate metrics
            ttfb = response_time - start_time
            total_time = end_time - start_time

            # Try to get token count if available
            try:
                usage = response_json.get("usage", {})
                total_tokens = usage.get("total_tokens", 0)
                completion_tokens = usage.get("completion_tokens", 0)
                token_counts.append(total_tokens)

                # Calculate tokens per second (using completion tokens)
                if completion_tokens > 0 and total_time > 0:
                    tokens_per_second.append(completion_tokens / total_time)
                else:
                    tokens_per_second.append(0)
            except Exception as e:
                token_counts.append(0)
                tokens_per_second.append(0)

            ttfb_times.append(ttfb)
            total_times.append(total_time)

            # Add a small delay to avoid rate limiting
            time.sleep(0.5)

        except Exception as e:
            print(f"Error on request: {e}")
            errors += 1

    return {
        "name": api_name,
        "url": api_url,
        "model": model,
        "average_ttfb": np.mean(ttfb_times) if ttfb_times else None,
        "median_ttfb": np.median(ttfb_times) if ttfb_times else None,
        "p95_ttfb": np.percentile(ttfb_times, 95) if ttfb_times else None,
        "average_total": np.mean(total_times) if total_times else None,
        "median_total": np.median(total_times) if total_times else None,
        "p95_total": np.percentile(total_times, 95) if total_times else None,
        "ttfb_times": ttfb_times,
        "total_times": total_times,
        "token_counts": token_counts,
        "avg_tokens": (
            np.mean(token_counts) if token_counts and any(token_counts) else None
        ),
        "tokens_per_second": tokens_per_second,
        "avg_tokens_per_second": (
            np.mean([t for t in tokens_per_second if t > 0])
            if tokens_per_second and any(tokens_per_second)
            else None
        ),
        "median_tokens_per_second": (
            np.median([t for t in tokens_per_second if t > 0])
            if tokens_per_second and any(tokens_per_second)
            else None
        ),
        "success_rate": (
            len(ttfb_times) / (len(ttfb_times) + errors)
            if (len(ttfb_times) + errors) > 0
            else 0
        ),
        "error_count": errors,
    }


def print_comparison_table(results_avalai, results_openai):
    """Print comparison table between two APIs"""
    headers = [
        "Metric",
        f"AvalAI ({results_avalai['model']})",
        f"OpenAI ({results_openai['model']})",
    ]

    data = [
        [
            "Average TTFB (s)",
            f"{results_avalai['average_ttfb']:.3f}",
            f"{results_openai['average_ttfb']:.3f}",
        ],
        [
            "Median TTFB (s)",
            f"{results_avalai['median_ttfb']:.3f}",
            f"{results_openai['median_ttfb']:.3f}",
        ],
        [
            "95th Percentile TTFB (s)",
            f"{results_avalai['p95_ttfb']:.3f}",
            f"{results_openai['p95_ttfb']:.3f}",
        ],
        [
            "Average Total Time (s)",
            f"{results_avalai['average_total']:.3f}",
            f"{results_openai['average_total']:.3f}",
        ],
        [
            "Median Total Time (s)",
            f"{results_avalai['median_total']:.3f}",
            f"{results_openai['median_total']:.3f}",
        ],
        [
            "95th Percentile Total (s)",
            f"{results_avalai['p95_total']:.3f}",
            f"{results_openai['p95_total']:.3f}",
        ],
        [
            "Success Rate",
            f"{results_avalai['success_rate']:.2%}",
            f"{results_openai['success_rate']:.2%}",
        ],
    ]

    # Add token metrics if available
    if (
        results_avalai["avg_tokens"] is not None
        and results_openai["avg_tokens"] is not None
    ):
        data.append(
            [
                "Avg Tokens per Response",
                f"{results_avalai['avg_tokens']:.1f}",
                f"{results_openai['avg_tokens']:.1f}",
            ]
        )

    # Add tokens per second metrics if available
    if (
        results_avalai["avg_tokens_per_second"] is not None
        and results_openai["avg_tokens_per_second"] is not None
    ):
        data.append(
            [
                "Avg Tokens per Second",
                f"{results_avalai['avg_tokens_per_second']:.1f}",
                f"{results_openai['avg_tokens_per_second']:.1f}",
            ]
        )
        data.append(
            [
                "Median Tokens per Second",
                f"{results_avalai['median_tokens_per_second']:.1f}",
                f"{results_openai['median_tokens_per_second']:.1f}",
            ]
        )

    print("\nAPI Performance Comparison:")
    print(tabulate(data, headers=headers, tablefmt="grid"))


def plot_comparison(results_avalai, results_openai, output_file=None):
    """Create improved visualization plots for API comparison"""
    # Set the style
    sns.set(style="whitegrid")

    # Create figure with subplots - adding a third subplot for tokens per second
    fig, axes = plt.subplots(3, 1, figsize=(12, 15))

    # Define metrics to plot
    metrics = [
        ("ttfb_times", "Time to First Byte (s)"),
        ("total_times", "Total Request Time (s)"),
        ("tokens_per_second", "Tokens per Second"),
    ]

    # Define colors for each API
    colors = {"AvalAI": "#3498db", "OpenAI": "#2ecc71"}

    for i, (metric, title) in enumerate(metrics):
        # Create violin plots with individual points
        ax = axes[i]

        # Prepare data for plotting
        data_to_plot = []
        labels = []

        for result, label in [(results_avalai, "AvalAI"), (results_openai, "OpenAI")]:
            # Filter out zeros for tokens per second
            if metric == "tokens_per_second":
                data_to_plot.append([t for t in result[metric] if t > 0])
            else:
                data_to_plot.append(result[metric])
            labels.append(f"{label}\n({result['model']})")

        # Create violin plot
        parts = ax.violinplot(data_to_plot, showmeans=True, showmedians=True)

        # Customize violin plots
        for pc, color_key in zip(parts["bodies"], colors.keys()):
            pc.set_facecolor(colors[color_key])
            pc.set_alpha(0.7)

        # Add boxplot inside violin
        bp = ax.boxplot(
            data_to_plot,
            positions=range(1, len(data_to_plot) + 1),
            widths=0.15,
            patch_artist=True,
            showfliers=False,
        )

        # Customize boxplots
        for box, color_key in zip(bp["boxes"], colors.keys()):
            box.set(color="black", linewidth=1.5)
            box.set(facecolor="white")

        # Add scatter points with jitter
        for j, data in enumerate(
            [
                (
                    results_avalai[metric]
                    if metric != "tokens_per_second"
                    else [t for t in results_avalai[metric] if t > 0]
                ),
                (
                    results_openai[metric]
                    if metric != "tokens_per_second"
                    else [t for t in results_openai[metric] if t > 0]
                ),
            ]
        ):
            # Add jitter to x position
            x = np.random.normal(j + 1, 0.05, size=len(data))
            ax.scatter(
                x,
                data,
                alpha=0.4,
                s=20,
                color=list(colors.values())[j],
                edgecolor="white",
                linewidth=0.5,
            )

        # Set labels and title
        ax.set_title(title, fontsize=14, fontweight="bold")
        if metric == "tokens_per_second":
            ax.set_ylabel("Tokens/second", fontsize=12)
        else:
            ax.set_ylabel("Time (seconds)", fontsize=12)
        ax.set_xticks(range(1, len(labels) + 1))
        ax.set_xticklabels(labels, fontsize=12)

        # Add horizontal grid lines
        ax.yaxis.grid(True, linestyle="--", alpha=0.7)

        # Add stats as text
        for j, (result, label) in enumerate(
            [(results_avalai, "AvalAI"), (results_openai, "OpenAI")]
        ):
            if metric == "tokens_per_second":
                if result["avg_tokens_per_second"] is not None:
                    stats = (
                        f"Mean: {result['avg_tokens_per_second']:.1f}\n"
                        f"Median: {result['median_tokens_per_second']:.1f}"
                    )
                    max_val = (
                        max([t for t in result[metric] if t > 0])
                        if any(t > 0 for t in result[metric])
                        else 0
                    )
                    ax.annotate(
                        stats,
                        xy=(j + 1, max_val * 1.05),
                        ha="center",
                        va="bottom",
                        fontsize=10,
                        bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.7),
                    )
            else:
                stats = (
                    f"Mean: {result[f'average_{metric.split("_")[0]}']:.3f}s\n"
                    f"Median: {result[f'median_{metric.split("_")[0]}']:.3f}s\n"
                    f"95th: {result[f'p95_{metric.split("_")[0]}']:.3f}s"
                )
                ax.annotate(
                    stats,
                    xy=(j + 1, result[f'p95_{metric.split("_")[0]}'] * 1.05),
                    ha="center",
                    va="bottom",
                    fontsize=10,
                    bbox=dict(boxstyle="round,pad=0.5", fc="white", alpha=0.7),
                )

    # Add title and timestamp
    plt.suptitle(
        f"API Performance Comparison: AvalAI vs OpenAI", fontsize=16, fontweight="bold"
    )
    plt.figtext(
        0.5,
        0.01,
        f'Generated on {datetime.now().strftime("%Y-%m-%d %H:%M:%S")}',
        ha="center",
        fontsize=10,
    )

    plt.tight_layout(rect=[0, 0.03, 1, 0.97])

    if output_file:
        plt.savefig(output_file, dpi=300, bbox_inches="tight")
        print(f"Plot saved to {output_file}")
    else:
        plt.show()


def save_results(results_avalai, results_openai, filename):
    """Save results to JSON file"""
    # Convert numpy arrays to lists for JSON serialization
    results_avalai_copy = results_avalai.copy()
    results_openai_copy = results_openai.copy()

    for key in ["ttfb_times", "total_times", "token_counts"]:
        if key in results_avalai_copy:
            results_avalai_copy[key] = [float(x) for x in results_avalai_copy[key]]
        if key in results_openai_copy:
            results_openai_copy[key] = [float(x) for x in results_openai_copy[key]]

    data = {
        "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
        "results": {"avalai": results_avalai_copy, "openai": results_openai_copy},
    }

    with open(filename, "w") as f:
        json.dump(data, f, indent=2)

    print(f"Results saved to {filename}")


def main():
    # API configuration
    model_name = "gpt-4o-mini"

    url_avalai = "https://api.avalai.ir/v1/chat/completions"
    api_key_avalai = os.getenv("AVALAI_API_KEY")  # Replace with actual key

    url_openai = "https://api.openai.com/v1/chat/completions"
    api_key_openai = os.getenv("OPENAI_API_KEY")  # Replace with actual key

    # Number of requests to make for each API
    num_requests = 60

    # Test prompt
    prompt = "Say hi"

    # Run the tests
    results_avalai = test_api_performance(
        "AvalAI", url_avalai, api_key_avalai, model_name, num_requests, prompt
    )
    results_openai = test_api_performance(
        "OpenAI", url_openai, api_key_openai, model_name, num_requests, prompt
    )

    # Print comparison table
    print_comparison_table(results_avalai, results_openai)

    # Generate visualization
    plot_comparison(results_avalai, results_openai, "api_performance_comparison.png")

    # Save results
    save_results(results_avalai, results_openai, "api_performance_results.json")


if __name__ == "__main__":
    main()
```

## منابع مرتبط

- [راهنماها: بهینه‌سازی تاخیر](fa/guides/latency-optimization.md)
- [راهنماها: شمارش توکن](fa/guides/token-counting.md)
- [راهنماها: کش کردن پرامپت](fa/guides/prompt-caching.md)
- [راهنماها: محدودیت‌های نرخ](fa/guides/rate-limits.md)
