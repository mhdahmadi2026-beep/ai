# مدل‌های جدید اضافه شدند: Grok 4.20 پایدار، GPT-Image-2، سری Qwen3.6، Kimi K2.6 و Gemini Embedding 2

**تاریخ:** ۱۴۰۵-۰۲-۰۳ / (2026-04-23)

## خلاصه

 افزودن ده مدل جدید از پنج ارائه‌دهنده پیشرو را اعلام می‌کنیم: نسخه‌های پایدار `grok-4.20-reasoning` و `grok-4.20-non-reasoning` از X.AI، مدل نسل‌بعدی تولید تصویر `gpt-image-2` از OpenAI، مدل‌های چندوجهی بینایی‌-زبانی `qwen3.6-flash`، `qwen3.6-27b`، `qwen3.6-35b-a3b` و `qwen3.6-max-preview` از Alibaba، مدل متن‌باز عامل‌محور کدنویسی `kimi-k2.6` از Moonshot AI، و نخستین مدل تعبیه چندوجهی گوگل یعنی `gemini-embedding-2`.

---

## جزئیات

### X.AI (Grok)

نسخهٔ پایدار Grok 4.20 اکنون با هر دو نوع Reasoning و Non-Reasoning در دسترس است و فراتر از نسخه‌های بتای قبلی با حفظ همان پنجره زمینه ۲ میلیون توکنی و سرعت پیشرو در صنعت عرضه می‌شود.

#### grok-4.20-reasoning

[`grok-4.20-reasoning`](fa/providers/xai.md) نسخهٔ پایدار مدل پرچم‌دار Grok 4.20 Reasoning از X.AI است. این مدل سرعت پیشرو در صنعت، فراخوانی ابزار عامل‌محور، پایین‌ترین نرخ توهم در بازار و پایبندی دقیق به دستورالعمل‌ها برای پاسخ‌هایی پیوسته دقیق ارائه می‌دهد.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۲,۰۰۰,۰۰۰ توکن |
| قیمت ورودی | $2.00 / 1M توکن |
| قیمت ورودی کش‌شده | $0.20 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $6.00 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $4.00 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $0.40 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $12.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **حالت استدلال**: تفکر گسترده پیش از پاسخ‌گویی برای حل مسائل پیچیده
- **زمینه عظیم**: پنجره زمینه ۲ میلیون توکنی برای اسناد و مکالمات گسترده
- **پایین‌ترین نرخ توهم**: دقت و صحت پیشرو در صنعت
- **پایبندی دقیق به دستورالعمل**: پاسخ‌های پیوسته دقیق
- **فراخوانی توابع و خروجی ساختارمند**: پشتیبانی کامل از ابزارها و سیستم‌های خارجی

#### grok-4.20-non-reasoning

[`grok-4.20-non-reasoning`](fa/providers/xai.md) نسخهٔ پایدار non-reasoning است که برای پاسخ‌های سریع بدون تفکر گسترده بهینه‌سازی شده و برای برنامه‌های پرتوان و حساس به تأخیر ایده‌آل است.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۲,۰۰۰,۰۰۰ توکن |
| قیمت ورودی | $2.00 / 1M توکن |
| قیمت ورودی کش‌شده | $0.20 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $6.00 / 1M توکن |
| قیمت ورودی (بالای ۲۰۰K) | $4.00 / 1M توکن |
| ورودی کش‌شده (بالای ۲۰۰K) | $0.40 / 1M توکن |
| قیمت خروجی (بالای ۲۰۰K) | $12.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **استنتاج سریع**: بهینه‌سازی‌شده برای پاسخ‌های سریع بدون سربار استدلال
- **زمینه عظیم**: پنجره زمینه ۲ میلیون توکنی
- **توان بالا**: ایده‌آل برای برنامه‌های حساس به تأخیر
- **فراخوانی توابع و خروجی ساختارمند**: پشتیبانی کامل از ابزارها

### OpenAI

#### gpt-image-2

[`gpt-image-2`](fa/providers/openai.md) مدل نسل‌بعدی تولید تصویر OpenAI است که دقت و کنترل بیشتر، رندرینگ قدرتمندتر متن چندزبانه، پیچیدگی سبک‌شناختی و واقع‌گرایی، هوشمندی ارتقایافته نسبت به دنیای واقعی، و پشتیبانی از نسبت ابعاد انعطاف‌پذیر را ارائه می‌دهد. این مدل هم روی اندپوینت `v1/images/generations` و هم `v1/images/edits` در دسترس است.

| ویژگی | جزئیات |
|-------|--------|
| قیمت ورودی متنی | $5.00 / 1M توکن |
| قیمت ورودی تصویری | $8.00 / 1M توکن |
| ورودی متنی کش‌شده | $1.25 / 1M توکن |
| ورودی تصویری کش‌شده | $2.00 / 1M توکن |
| قیمت خروجی متنی | $10.00 / 1M توکن |
| قیمت خروجی تصویری | $30.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر |
| روش‌های خروجی | تصویر، متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/images/generations`, `v1/images/edits` |

**ویژگی‌های کلیدی:**
- **دقت و کنترل بیشتر**: بهبود چشم‌گیر دقت تولید تصویر و پایبندی به جزئیات دستورالعمل
- **رندرینگ متن چندزبانه**: عملکرد قوی در خطوط جهانی از جمله ژاپنی، عربی، کره‌ای، دوناگری، سیریلیک، بنگالی، یونانی، چینی و لاتین
- **پیچیدگی سبک‌شناختی و واقع‌گرایی**: وفاداری بالاتر در عکاسی، تصویرسازی، مانگا، پیکسل‌آرت و دیگر سبک‌های بصری
- **نسبت ابعاد انعطاف‌پذیر**: فرمت‌های افقی، مربعی و عمودی برای کاربردهایی از بنر تا صفحات موبایل
- **حالت تفکر**: استفاده از استدلال برای تحقیق، تبدیل ورودی‌ها و تولید دارایی‌های بصری منسجم از ابتدا تا انتها
- **ویرایش تصویر**: پشتیبانی از هر دو اندپوینت تولید و ویرایش برای جریان‌های کاری کامل تصویر

**نام‌های مستعار:** `gpt-image-2-2026-04-21`

### Alibaba (سری Qwen3.6)

چهار مدل جدید از سری Qwen3.6 اکنون در دسترس هستند و بهبودهای قابل‌توجهی در کدنویسی عامل‌محور، استدلال STEM، هوشمندی فضایی و تشخیص اشیا نسبت به نسل Qwen3.5 ارائه می‌دهند.

#### qwen3.6-flash

[`qwen3.6-flash`](fa/providers/alibaba.md) مدل Flash بینایی‌-زبانی بومی Qwen3.6 است با پنجره زمینه ۱ میلیون توکنی و بهبود چشم‌گیر در کدنویسی عامل‌محور، استدلال ریاضی و هوشمندی فضایی نسبت به qwen3.5-flash.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۱,۰۰۰,۰۰۰ توکن (قیمت‌گذاری رده‌یک ۲۵۶K) |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.25 / 1M توکن |
| قیمت ورودی (بالای ۲۵۶K) | $1.00 / 1M توکن |
| ورودی ساخت کش | $0.3125 / 1M توکن |
| ورودی ساخت کش (بالای ۲۵۶K) | $1.25 / 1M توکن |
| قیمت ورودی کش‌شده | $0.025 / 1M توکن (۹۰٪ کاهش هزینه) |
| ورودی کش‌شده (بالای ۲۵۶K) | $0.10 / 1M توکن |
| قیمت خروجی | $1.50 / 1M توکن |
| قیمت خروجی (بالای ۱۲۸K) | $4.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بینایی‌-زبانی بومی**: پردازش بومی متن، تصویر و ویدیو
- **پنجره زمینه ۱M**: زمینه گسترده برای اسناد و مکالمات طولانی
- **کدنویسی عامل‌محور**: به‌طور قابل‌توجه از Qwen3.5-Flash در معیارهای code-agent بهتر عمل می‌کند
- **هوشمندی فضایی**: بهبود چشم‌گیر در مکان‌یابی و تشخیص اشیا
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`
- **پشتیبانی ابزار**: فراخوانی توابع، خروجی ساختارمند و جستجوی وب

#### qwen3.6-27b

[`qwen3.6-27b`](fa/providers/alibaba.md) مدل متراکم بینایی‌-زبانی بومی ۲۷ میلیارد پارامتری Qwen3.6 است که بر پایه معماری 3.5-27B ساخته شده و بهبودهای کلیدی در کدنویسی عامل‌محور، استدلال STEM و قابلیت‌های عامل بصری ارائه می‌دهد.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۲۵۶,۰۰۰ توکن |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.60 / 1M توکن |
| قیمت ورودی کش‌شده | $0.06 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $3.60 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بینایی‌-زبانی بومی**: پردازش بومی متن، تصویر و ویدیو
- **پنجره زمینه ۲۵۶K**: زمینه گسترده برای وظایف پیچیده
- **استدلال STEM ارتقایافته**: مهارت‌های بهبودیافته استدلال ریاضی و کدنویسی
- **عوامل بصری**: پیشرفت در درک ویدیو، OCR اسناد و قابلیت‌های عامل بصری
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

#### qwen3.6-35b-a3b

[`qwen3.6-35b-a3b`](fa/providers/alibaba.md) مدل بینایی‌-زبانی بومی ۳۵B-A3B از Qwen3.6 است که بر پایه معماری ترکیبی متشکل از توجه خطی با چارچوب ترکیب پراکنده متخصصان (sparse MoE) برای راندمان استنتاج بالاتر ساخته شده است.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۲۵۶,۰۰۰ توکن |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $0.248 / 1M توکن |
| قیمت ورودی کش‌شده | $0.025 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت خروجی | $1.485 / 1M توکن |
| روش‌های ورودی | متن، تصویر، ویدیو |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **معماری ترکیبی**: توجه خطی همراه با MoE پراکنده برای راندمان بالاتر
- **کدنویسی عامل‌محور بهبودیافته**: عملکرد به‌مراتب بهتر code-agent
- **هوشمندی فضایی**: پیشرفت در مکان‌یابی و تشخیص اشیا
- **مقرون‌به‌صرفه**: قیمت‌گذاری بسیار پایین به لطف فعال‌سازی پراکنده کارآمد
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

#### qwen3.6-max-preview

[`qwen3.6-max-preview`](fa/providers/alibaba.md) بزرگ‌ترین و توانمندترین نوع سری Qwen3.6 است که در حالت پیش‌نمایش با قابلیت‌های صرفا متنی ارائه می‌شود. این مدل شامل vibe coding پیشرفته، اجرای کارآمد عامل کدنویسی و بازیابی دانش long-tail ارتقایافته است.

| ویژگی | جزئیات |
|-------|--------|
| پنجره زمینه | ۲۵۶,۰۰۰ توکن (قیمت‌گذاری رده‌یک ۱۲۸K) |
| حداکثر خروجی | ۶۴K توکن |
| قیمت ورودی | $1.30 / 1M توکن |
| قیمت ورودی (بالای ۱۲۸K) | $2.00 / 1M توکن |
| ورودی ساخت کش | $1.625 / 1M توکن |
| ورودی ساخت کش (بالای ۱۲۸K) | $2.50 / 1M توکن |
| قیمت ورودی کش‌شده | $0.13 / 1M توکن (۹۰٪ کاهش هزینه) |
| ورودی کش‌شده (بالای ۱۲۸K) | $0.20 / 1M توکن |
| قیمت خروجی | $7.80 / 1M توکن |
| قیمت خروجی (بالای ۱۲۸K) | $12.00 / 1M توکن |
| روش‌های ورودی | متن |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **بزرگ‌ترین مدل Qwen3.6**: توانمندترین نوع در سری Qwen3.6
- **Vibe Coding ارتقایافته**: توسعه فرانت‌اند قوی‌تر و اجرای عامل کدنویسی
- **دانش Long-Tail**: بازیابی دانش ارتقایافته برای موضوعات تخصصی
- **پنجره زمینه ۲۵۶K**: زمینه گسترده برای وظایف پیچیده
- **تفکر عمیق**: حالت استدلال اختیاری از طریق `enable_thinking`

### Moonshot AI

#### kimi-k2.6

[`kimi-k2.6`](fa/providers/moonshotai.md) جدیدترین مدل متن‌باز Moonshot AI است که با کدنویسی state-of-the-art، اجرای long-horizon و قابلیت‌های Agent Swarm ارائه می‌شود. این مدل بر پایه K2.5 ساخته شده و قابلیت اطمینان چندمرحله‌ای قوی‌تر، قابلیت full-stack، و Document-to-Skills قابل استفاده مجدد را دارد.

| ویژگی | جزئیات |
|-------|--------|
| قیمت ورودی | $0.95 / 1M توکن |
| قیمت ورودی کش‌شده | $0.16 / 1M توکن |
| قیمت خروجی | $4.00 / 1M توکن |
| روش‌های ورودی | متن، تصویر |
| روش‌های خروجی | متن |
| اندپوینت‌های پشتیبانی‌شده | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **کدنویسی SOTA**: دستورالعمل‌ها را به رابط‌های فرانت‌اند در سطح Awwwards با خطوط تمیز، انیمیشن‌ها و تعاملات تبدیل می‌کند
- **تولید Full-Stack**: وب‌سایت‌های کامل کارآمد با احراز هویت، تعاملات و عملیات پایگاه داده را از یک دستورالعمل می‌سازد
- **اجرای Long-Horizon**: وظایف پیچیده و چندمرحله‌ای را با قابلیت اطمینان بالاتر و تغییرات غیرضروری کمتر مدیریت می‌کند
- **Agent Swarm**: هماهنگی چندین عامل به‌صورت موازی برای جستجو، تحقیق، تحلیل، نگارش بلند و تولید محتوای چندفرمتی
- **Document to Skills**: تبدیل اسناد باکیفیت به مهارت‌های قابل استفاده مجدد که در وظایف آینده به‌کار می‌آیند
- **Claw Groups (پیش‌نمایش)**: جریان کاری جدید چندعاملی با یک هماهنگ‌کننده که وظایف و پیش‌نیاز‌ها را مدیریت می‌کند
- **Kimi Slides**: تولید ارائه‌های آماده تولید از دستورالعمل‌ها یا ورودی‌های چندفرمتی


### Google

#### gemini-embedding-2

[`gemini-embedding-2`](fa/providers/google.md) نخستین مدل تعبیه چندوجهی گوگل در Gemini API است. این مدل متن، تصویر، ویدیو، صوت و اسناد را در یک فضای تعبیه یکپارچه نگاشت می‌کند و جستجو، طبقه‌بندی و خوشه‌بندی میان‌وجهی در بیش از ۱۰۰ زبان را امکان‌پذیر می‌سازد.

| ویژگی | جزئیات |
|-------|--------|
| قیمت ورودی متنی | $0.20 / 1M توکن |
| ورودی متنی کش‌شده | $0.02 / 1M توکن (۹۰٪ کاهش هزینه) |
| قیمت ورودی تصویری | $0.45 / 1M توکن |
| قیمت ورودی صوتی | $6.50 / 1M توکن |
| قیمت ورودی ویدیویی | $12.00 / 1M توکن |
| قیمت خروجی | $0.15 / 1M توکن |
| محدودیت توکن ورودی | ۸,۱۹۲ توکن |
| ابعاد خروجی | انعطاف‌پذیر (۱۲۸ تا ۳۰۷۲، پیش‌فرض ۳۰۷۲، پیشنهادی ۷۶۸/۱۵۳۶/۳۰۷۲) |
| روش‌های ورودی | متن، تصویر، صوت، ویدیو، PDF |
| روش‌های خروجی | Embeddings |
| اندپوینت‌های پشتیبانی‌شده | `v1/embeddings`, `v1beta/models/{model}:embedContent` (Gemini بومی) |

**ویژگی‌های کلیدی:**
- **نخستین تعبیه چندوجهی**: فضای تعبیه یکپارچه در سراسر متن، تصویر، ویدیو، صوت و PDF
- **جستجوی میان‌وجهی**: مقایسه و بازیابی محتوا در وجه‌های مختلف در همان فضای برداری
- **بیش از ۱۰۰ زبان**: پشتیبانی گسترده چندزبانه برای برنامه‌های بین‌المللی
- **یادگیری بازنمایی Matryoshka (MRL)**: ابعاد خروجی انعطاف‌پذیر (۱۲۸–۳۰۷۲) بدون افت کیفیت
- **نرمال‌سازی مجدد خودکار**: ابعاد برش‌داده‌شده (مانند ۷۶۸، ۱۵۳۶) برای شباهت دقیق به‌طور خودکار نرمال می‌شوند
- **تجمیع تعبیه**: یک تعبیه تجمیع‌شده واحد برای ورودی‌های چندبخشی (متن + تصویر و غیره)
- **دستورالعمل وظیفه**: درج انواع وظیفه مستقیما در دستورالعمل‌ها (مثلا `task: search result | query: ...`) برای عملکرد بهینه
- **روش‌های پشتیبانی‌شده**: متن (۸,۱۹۲ توکن)، تصاویر (PNG/JPEG، حداکثر ۶)، صوت (MP3/WAV، حداکثر ۱۸۰ ثانیه)، ویدیو (MP4/MOV، حداکثر ۱۲۰ ثانیه، ۳۲ فریم)، PDF (حداکثر ۶ صفحه)
- **پشتیبانی دوگانه API**: در دسترس در هم اندپوینت سازگار با OpenAI یعنی `v1/embeddings` و هم اندپوینت بومی Gemini یعنی `v1beta/models/{model}:embedContent`

**نام‌های مستعار:** `gemini-embedding-2-preview`

---

## خلاصه قیمت‌گذاری

| مدل | ورودی ($/1M توکن) | ورودی کش‌شده ($/1M توکن) | خروجی ($/1M توکن) |
|-----|-------------------|-------------------------|-------------------|
| `grok-4.20-reasoning` | $2.00 | $0.20 | $6.00 |
| `grok-4.20-non-reasoning` | $2.00 | $0.20 | $6.00 |
| `gpt-image-2` (متن) | $5.00 | $1.25 | $10.00 |
| `gpt-image-2` (تصویر) | $8.00 | $2.00 | $30.00 |
| `qwen3.6-flash` | $0.25 | $0.025 | $1.50 |
| `qwen3.6-27b` | $0.60 | $0.06 | $3.60 |
| `qwen3.6-35b-a3b` | $0.248 | $0.025 | $1.485 |
| `qwen3.6-max-preview` | $1.30 | $0.13 | $7.80 |
| `kimi-k2.6` | $0.95 | $0.16 | $4.00 |
| `gemini-embedding-2` (متن) | $0.20 | $0.02 | $0.15 |

---

## نمونه‌های درخواست/پاسخ API

### نمونه Grok 4.20 Reasoning

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "grok-4.20-reasoning",
    "messages": [
      {
        "role": "user",
        "content": "Design a fault-tolerant distributed system architecture for a global payment platform."
      }
    ],
    "max_tokens": 4096
  }'
```

**نمونه پاسخ:**

```json
{
  "id": "chatcmpl-grok420-abc123",
  "created": 1776321600,
  "model": "grok-4.20-reasoning",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "A fault-tolerant global payment platform should adopt a multi-region active-active architecture...",
        "role": "assistant",
        "thinking_blocks": [
          {
            "type": "thinking",
            "thinking": "Let me break down the requirements: global reach, fault tolerance, payment-grade reliability..."
          }
        ],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1420,
    "prompt_tokens": 25,
    "total_tokens": 1445,
    "prompt_tokens_details": {
      "cached_tokens": 0,
      "text_tokens": 25
    }
  },
  "estimated_cost": {
    "unit": "0.0085700000",
    "irt": 982.13,
    "exchange_rate": 114600
  }
}
```

### نمونه تولید GPT-Image-2

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "A modernist editorial poster titled \"Typography\" that celebrates global scripts including Japanese, Arabic, Korean, and Latin letterforms, in red, blue, and black tones.",
    "size": "1024x1024",
    "n": 1
  }'
```

**نمونه پاسخ:**

```json
{
  "created": 1776321700,
  "data": [
    {
      "b64_json": "iVBORw0KGgoAAAANSUhEUgAABAAAAAQACAIAAADwf7zU...[TRUNCATED]",
      "revised_prompt": "A modernist editorial poster..."
    }
  ],
  "usage": {
    "input_tokens": 32,
    "input_tokens_details": {
      "text_tokens": 32,
      "image_tokens": 0
    },
    "output_tokens": 4160,
    "total_tokens": 4192
  },
  "estimated_cost": {
    "unit": "0.1249600000",
    "irt": 14320.22,
    "exchange_rate": 114600
  }
}
```

### نمونه ویرایش GPT-Image-2

```bash
curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gpt-image-2" \
  -F "image=@input.png" \
  -F "prompt=Add a gold Art Deco frame and soft sunrise lighting" \
  -F "size=1024x1024"
```

### نمونه Qwen3.6-Flash با حالت تفکر

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.6-flash",
    "messages": [
      {
        "role": "user",
        "content": "Implement a binary search tree in Python with insert, delete, and in-order traversal methods."
      }
    ],
    "extra_body": {
      "enable_thinking": true
    },
    "stream": true
  }'
```

### نمونه Qwen3.6-Max-Preview

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.6-max-preview",
    "messages": [
      {
        "role": "user",
        "content": "Build a polished Next.js landing page for a SaaS product with hero, features, testimonials, and pricing sections."
      }
    ],
    "max_tokens": 8192
  }'
```

### نمونه Agent Swarm در Kimi K2.6

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.6",
    "messages": [
      {
        "role": "user",
        "content": "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI."
      }
    ],
    "max_tokens": 8192
  }'
```

### نمونه Gemini Embedding 2 (متن)

```bash
curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-2",
    "input": "task: search result | query: What is the meaning of life?",
    "dimensions": 768
  }'
```

**نمونه پاسخ:**

```json
{
  "object": "list",
  "data": [
    {
      "object": "embedding",
      "index": 0,
      "embedding": [
        0.0123,
        -0.0456,
        0.0789,
        "...[TRUNCATED 768 values]"
      ]
    }
  ],
  "model": "gemini-embedding-2",
  "usage": {
    "prompt_tokens": 14,
    "total_tokens": 14
  },
  "estimated_cost": {
    "unit": "0.0000028000",
    "irt": 0.32,
    "exchange_rate": 114600
  }
}
```

### Gemini Embedding 2 چندوجهی از طریق اندپوینت سازگار با OpenAI

اندپوینت `v1/embeddings` ورودی‌های چندوجهی (تصاویر، صوت، ویدیو) را به‌صورت URI‌های `data:` در آرایه `input` می‌پذیرد:

```bash
# متن + تصویر (base64 data URI) از طریق اندپوینت سازگار با OpenAI
curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "input": [
      "The food was delicious and the waiter...",
      "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAAgAAAAIAQMAAAD+wSzIAAAABlBMVEX///+/v7+jQ3Y5AAAADklEQVQI12P4AIX8EAgALgAD/aNpbtEAAAAASUVORK5CYII"
    ],
    "model": "gemini-embedding-2"
  }'
```

```bash
# متن + صوت (base64 data URI) از طریق اندپوینت سازگار با OpenAI
AUDIO_PATH="./speech.mp3"
AUDIO_BASE64="$(base64 -i "$AUDIO_PATH" | tr -d '\n')"

cat >/tmp/embeddings-audio.json <<EOF
{
  "input": [
    "The food was delicious and the waiter...",
    "data:audio/mpeg;base64,${AUDIO_BASE64}"
  ],
  "model": "gemini-embedding-2"
}
EOF

curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer ${AVALAI_API_KEY}" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/embeddings-audio.json
```

```bash
# متن + ویدیو (base64 data URI) از طریق اندپوینت سازگار با OpenAI
VIDEO_PATH="./sample_video.mp4"
VIDEO_BASE64="$(base64 -i "$VIDEO_PATH" | tr -d '\n')"

cat >/tmp/embeddings-video.json <<EOF
{
  "input": [
    "The food was delicious and the waiter...",
    "data:video/mp4;base64,${VIDEO_BASE64}"
  ],
  "model": "gemini-embedding-2"
}
EOF

curl -i "https://api.avalai.ir/v1/embeddings" \
  -H "Authorization: Bearer ${AVALAI_API_KEY}" \
  -H "Content-Type: application/json" \
  --data-binary @/tmp/embeddings-video.json
```

### Gemini Embedding 2 از طریق API بومی Gemini (`v1beta`)

`gemini-embedding-2` همچنین از طریق اندپوینت بومی Gemini یعنی `v1beta/models/{model}:embedContent` در دسترس است که بخش‌های `inline_data` را برای تصاویر، صوت، ویدیو و PDF می‌پذیرد.

**تعبیه متن (API بومی):**

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  -d '{
    "model": "gemini-embedding-2",
    "content": {
      "parts": [{
        "text": "What is the meaning of life?"
      }]
    }
  }'
```

**تعبیه تصویر (API بومی):**

```bash
IMG_PATH="./sample_image.jpg"
# macOS: IMG_BASE64="$(base64 -i "$IMG_PATH" | tr -d '\n')"
IMG_BASE64=$(base64 -w0 "${IMG_PATH}")

cat >/tmp/payload.json <<EOF
{
  "content": {
    "parts": [
      {
        "inline_data": {
          "mime_type": "image/png",
          "data": "${IMG_BASE64}"
        }
      }
    ]
  }
}
EOF

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  --data-binary @/tmp/payload.json
```

**تعبیه صوت (API بومی):**

```bash
AUDIO_PATH="./speech.mp3"
AUDIO_BASE64="$(base64 -i "$AUDIO_PATH" | tr -d '\n')"

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  -d '{
    "content": {
      "parts": [{
        "inline_data": {
          "mime_type": "audio/mpeg",
          "data": "'"${AUDIO_BASE64}"'"
        }
      }]
    }
  }'
```

**تعبیه ویدیو (API بومی):**

```bash
VIDEO_PATH="./sample_video.mp4"
VIDEO_BASE64="$(base64 -i "$VIDEO_PATH" | tr -d '\n')"

curl -sS "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: ${AVALAI_API_KEY}" \
  --data-binary @- <<EOF
{
  "content": {
    "parts": [
      {
        "inline_data": {
          "mime_type": "video/mp4",
          "data": "${VIDEO_BASE64}"
        }
      }
    ]
  }
}
EOF
```

**تجمیع متن + تصویر (API بومی):**

```bash
curl "https://api.avalai.ir/v1beta/models/gemini-embedding-2:embedContent" \
  -H "Content-Type: application/json" \
  -H "x-goog-api-key: $AVALAI_API_KEY" \
  -d '{
    "content": {
      "parts": [
        {"text": "An image of a dog"},
        {
          "inline_data": {
            "mime_type": "image/png",
            "data": "iVBORw0KGgo...[TRUNCATED]"
          }
        }
      ]
    }
  }'
```

> **یادداشت**: زمانی که چندین بخش در یک درخواست واحد ارائه می‌شوند، `gemini-embedding-2` یک تعبیه تجمیع‌شده واحد برمی‌گرداند. اگر به تعبیه‌های جداگانه برای هر ورودی نیاز دارید، از Batch API یا درخواست‌های متعدد استفاده کنید.

---

## نمونه‌های استفاده از SDK

### Chat Completions (Grok، Qwen، Kimi)

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.6",
    "messages": [
      {
        "role": "user",
        "content": "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form."
      }
    ]
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# Using Kimi K2.6 for full-stack coding
response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {
            "role": "user",
            "content": "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form.",
        }
    ],
)

print(response.choices[0].message.content)

# Using Grok 4.20 Reasoning
response = client.chat.completions.create(
    model="grok-4.20-reasoning",
    messages=[
        {
            "role": "user",
            "content": "Design a fault-tolerant distributed system architecture.",
        }
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)

# Using Qwen3.6-Flash with thinking mode
response = client.chat.completions.create(
    model="qwen3.6-flash",
    messages=[
        {
            "role": "user",
            "content": "Explain quantum entanglement with practical implications.",
        }
    ],
    extra_body={"enable_thinking": True},
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// Using Kimi K2.6
const kimiResponse = await client.chat.completions.create({
  model: "kimi-k2.6",
  messages: [
    {
      role: "user",
      content: "Build a minimalist personal portfolio website with a hero section, projects grid, and contact form.",
    },
  ],
});

console.log(kimiResponse.choices[0].message.content);

// Using Qwen3.6-Max-Preview
const qwenResponse = await client.chat.completions.create({
  model: "qwen3.6-max-preview",
  messages: [
    {
      role: "user",
      content: "Build a polished Next.js landing page for a SaaS product.",
    },
  ],
  max_tokens: 8192,
});

console.log(qwenResponse.choices[0].message.content);

```

### تولید تصویر (GPT-Image-2)

```language-selector
bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-image-2",
    "prompt": "A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
    "size": "1024x1024",
    "n": 1
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="gpt-image-2",
    prompt="A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
    size="1024x1024",
    n=1,
)

print(response.data[0].b64_json[:100] + "...")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
  model: "gpt-image-2",
  prompt: "A Bauhaus-inspired poster with bold typography and geometric shapes in red, blue, and black.",
  size: "1024x1024",
  n: 1,
});

console.log(response.data[0].b64_json.slice(0, 100) + "...");

```

### Embeddings (Gemini Embedding 2)

```language-selector
bash=:curl https://api.avalai.ir/v1/embeddings \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemini-embedding-2",
    "input": "task: search result | query: What is the meaning of life?",
    "dimensions": 768
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.embeddings.create(
    model="gemini-embedding-2",
    input="task: search result | query: What is the meaning of life?",
    dimensions=768,
)

print(f"Embedding length: {len(response.data[0].embedding)}")
print(f"First 5 values: {response.data[0].embedding[:5]}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.embeddings.create({
  model: "gemini-embedding-2",
  input: "task: search result | query: What is the meaning of life?",
  dimensions: 768,
});

console.log(`Embedding length: ${response.data[0].embedding.length}`);
console.log(`First 5 values:`, response.data[0].embedding.slice(0, 5));

```

---

## لینک‌های مستندات

- [مستندات مدل‌های X.AI](fa/providers/xai.md)
- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مستندات مدل‌های Moonshot AI](fa/providers/moonshotai.md)
- [مستندات مدل‌های Google](fa/providers/google.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API گفتگو](fa/api-reference/chat.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [مرجع API Embeddings](fa/api-reference/embeddings.md)
- [مرجع API بومی Gemini v1beta](fa/api-reference/v1beta.md)
