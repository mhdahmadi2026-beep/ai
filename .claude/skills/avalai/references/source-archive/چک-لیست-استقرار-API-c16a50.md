# چک‌لیست استقرار API

قبل از انتشار یک اپلیکیشن مبتنی بر AvalAI در production از این چک‌لیست استفاده کنید. این راهنما [چک‌لیست رسمی استقرار API](https://developers.openai.com/api/docs/guides/deployment-checklist) و [بهترین شیوه‌های production](https://developers.openai.com/api/docs/guides/production-best-practices) از OpenAI را برای base URL سازگار با OpenAI در AvalAI، سطح‌های rate limit، routing ارائه‌دهندگان و مستندات دوزبانه تطبیق می‌دهد.

## ۱. سطح API را انتخاب کنید

- **برای workflowهای جدید متن، reasoning، structured output و ابزارمحور، در صورت پشتیبانی مدل از `/v1/responses` شروع کنید.**
- **برای integrationهای موجود یا مدل‌هایی که فقط سازگاری Chat دارند، `/v1/chat/completions` را نگه دارید.**
- **مسیر migration را مستند کنید:** `messages` → `input`، promptهای system/developer → `instructions`، `max_completion_tokens` → `max_output_tokens` و `choices[0].message.content` → `response.output_text`.
- **Model IDها را در config pin کنید:** برای هر release مقدارهای `AVALAI_MODEL`، `AVALAI_BASE_URL=https://api.avalai.ir/v1` و label نسخه prompt را مشخص کنید.

!> ویژگی‌های hosted در Responses مثل ابزارهای hosted، jobهای پس‌زمینه، compaction، انتقال reasoning رمزگذاری‌شده یا WebSocket mode ممکن است در AvalAI به route و مدل وابسته باشند. آیتم چک‌لیست را نگه دارید، اما rollout را فقط بعد از مشاهده رفتار واقعی همان provider/model در staging انجام دهید.

قبل از launch، برای هر route مدل یک capability matrix کوچک نگه دارید: `/v1/responses`، streaming، `reasoning.effort`، `text.verbosity`، `previous_response_id`، `prompt_cache_key`، tool calling، jobهای پس‌زمینه و ادامه با WebSocket. هر «بله» باید request ID در staging داشته باشد و هر «نه» باید fallback مستند داشته باشد.

## ۲. کیفیت، هزینه و تأخیر را تنظیم کنید

| اهرم | کاربرد | راهنمای AvalAI |
| --- | --- | --- |
| `reasoning.effort` | عمق reasoning | کمترین effortی را انتخاب کنید که [evalها](fa/guides/evals.md) را پاس می‌کند؛ effort بالا را برای تصمیم‌های پیچیده نگه دارید. |
| `text.verbosity` | طول پاسخ | پاسخ production را کوتاه نگه دارید مگر اینکه UX توضیح کامل بخواهد. |
| `max_output_tokens` / `max_completion_tokens` | بودجه مشترک خروجی و reasoning | برای همه درخواست‌ها سقف بگذارید، اما برای پاسخ قابل مشاهده حاشیه امن نگه دارید؛ reasoning می‌تواند تمام سقف را مصرف کند و پاسخ ناقص بدون متن بسازد. برای تمام شدن بودجه با دلیل `max_output_tokens` یا `length` alert بگذارید و سقف را همراه با `reasoning.effort` تنظیم کنید. |
| `prompt_cache_key` | context تکراری | context پایدار محصول/خط‌مشی را ابتدا و context پویای کاربر را انتها نگه دارید؛ برای tenantها یا workflowهای نامرتبط یک cache key بیش‌ازحد داغ نسازید. |
| `phase` پیام assistant | agentهای طولانی‌مدت | هنگام replay تاریخچه assistant، تفاوت `phase: "commentary"` و `phase: "final_answer"` را حفظ کنید. |
| `tool_search` / ابزار deferred | tool catalog بزرگ | namespaceهای کوچک‌تر و lazy loading ابزار را ترجیح دهید؛ توضیح namespace را کوتاه نگه دارید و قواعد استفاده دقیق را داخل تعریف deferred ابزار بگذارید. |
| Compaction | مکالمه‌های طولانی | اگر hosted compaction فعال است از آن استفاده کنید؛ در غیر این صورت state را در app خلاصه کنید بدون از دست دادن decisionها، IDها و taskهای باز. |
| `reasoning.encrypted_content` | ادامه reasoning بدون ذخیره state | reasoning itemهای برگشتی provider را در صورت پشتیبانی دقیقا round-trip کنید؛ آن‌ها را parse یا rewrite نکنید. |
| Streaming | کاهش حس انتظار | پاسخ قابل مشاهده را stream کنید و برای flowهای ابزارمحور status نشان دهید. |
| پردازش پس‌زمینه | resumability | برای کارهای طولانی از jobهای app-managed استفاده کنید مگر اینکه background Responses hosted برای route شما فعال باشد؛ حالت background میزبانی‌شده معمولا به state ذخیره‌شده پاسخ نیاز دارد. |
| WebSocket mode | flowهای چندمرحله‌ای و ابزارمحور | فقط وقتی استفاده کنید که staging پشتیبانی route را ثابت کرده باشد؛ هر connection بهتر است یک workflow در حال اجرا داشته باشد و برای کار موازی connection جدا بگیرید. |

برای قابلیت‌های وابسته به route یا نیازمند فعال‌سازی، پیش از انتشار قرارداد
release را بنویسید:

- **Tool search:** ابزارها را بر اساس intent گروه‌بندی کنید، namespaceها را
  کوچک نگه دارید و توضیح namespace را کوتاه بنویسید. اگر `tool_search` یا
  `defer_loading` میزبانی‌شده برای route شما فعال نیست، تعریف ابزارها را قبل
  از ارسال request به AvalAI در اپلیکیشن فیلتر کنید.
- **Compaction:** اگر compaction میزبانی‌شده در دسترس است، خروجی compactشده
  را بدون تغییر forward کنید؛ آن را state ماشینی بدانید، نه خلاصه انسانی قابل
  ویرایش. اگر در دسترس نیست، decisionها، IDها، نتیجه ابزارها و taskهای باز را
  در summary مدیریت‌شده توسط اپلیکیشن حفظ کنید.
- **Prompt caching:** policy، schema و تعریف ابزارهای پایدار را ابتدای prompt
  نگه دارید، برای هر workload یا tenant از `prompt_cache_key` opaque استفاده
  کنید، و شناسه خام کاربر یا یک cache key جهانی بیش‌ازحد شلوغ نسازید.
- **Background jobs:** روی همان route بررسی کنید که آیا `background: true` به
  state ذخیره‌شده پاسخ نیاز دارد یا نه. اگر privacy posture شما رفتار
  zero-retention می‌خواهد، queue و worker مدیریت‌شده توسط اپلیکیشن را ترجیح
  دهید.
- **WebSocket mode:** فقط برای workflowهای طولانی و tool-heavy استفاده کنید،
  آن هم بعد از اینکه staging رفتار reconnect، cancel، timeout و fallback به
  HTTP را ثابت کرد.

## ۳. Credential و هویت کاربر را امن کنید

- `AVALAI_API_KEY` را در secret manager یا متغیر محیطی ذخیره کنید؛ آن را در کد browser/mobile قرار ندهید.
- برای development، staging و production کلید یا project جدا داشته باشید.
- کلید لو رفته را فورا rotate کنید و مالک rotation را مشخص کنید.
- برای محصولات دارای کاربر نهایی، `safety_identifier` hashشده ارسال کنید تا بررسی سوءاستفاده بدون ذخیره هویت خام انجام شود.
- حتی وقتی guardrail فعال است، password، API key، private key یا داده غیرضروری مشتری را به مدل نفرستید.

## ۴. دسترسی و عملیات را قفل کنید

مستندات OpenAI درباره RBAC، Admin API، workload identity و IP egress الگوهای عملیاتی خوبی می‌دهند، اما قابلیت‌های حساب AvalAI ممکن است متفاوت باشد. آن‌ها را به‌عنوان checklist استفاده کنید و هر مورد را پیش از launch با داشبورد AvalAI، قرارداد reseller یا پشتیبانی حساب verify کنید.

- **حداقل دسترسی:** دسترسی admin انسانی را از API key زمان اجرا جدا کنید. وقتی allowlist پروژه/مدل در دسترس است، کلید production را فقط به routeها و مدل‌هایی محدود کنید که اپلیکیشن واقعا نیاز دارد.
- **مرز پروژه:** محیط‌های experiment، staging، production و reseller/customer را در project یا account جدا نگه دارید تا فایل‌ها، هزینه، rate limit و logها با هم مخلوط نشوند.
- **Credential سرویس:** برای سرورها و CI، اگر در دسترس است از workload credential یا service account استفاده کنید. اگر هنوز از مقدارهای طولانی‌عمر `AVALAI_API_KEY` استفاده می‌کنید، آن‌ها را طبق برنامه و بعد از هر incident rotate کنید.
- **حاکمیت مدل:** برای هر محیط allowlist مدل‌های تاییدشده نگه دارید و مدل‌های آزمایشی را تا زمان پاس شدن بررسی privacy، cost، latency و eval از workloadهای regulated دور نگه دارید.
- **عملیات هزینه و rate limit:** مالک budget alert، تغییر quota و escalation محدودیت نرخ را مشخص کنید. هر درخواست افزایش limit باید به شواهد `avalai-request-id` و ترافیک مورد انتظار وصل باشد.
- **قابلیت audit:** تغییر کلیدها، routing، model allowlist، نسخه prompt، تنظیمات data-retention و budgetهای reseller را با هویت تغییر‌دهنده log کنید. اگر plan حساب اجازه می‌دهد audit eventها را export یا archive کنید.
- **کنترل شبکه:** IP allowlist فقط ترافیک یک شبکه عملیاتی را شناسایی می‌کند، نه کاربر authenticateشده را. حتی وقتی allowlist فعال است، authentication درخواست، mTLS/OAuth برای ابزارها و webhookهای امضاشده را حفظ کنید.

### CI/CD و Workload Identity

مستندات [workload identity federation](https://developers.openai.com/api/docs/guides/workload-identity-federation) در OpenAI یک الگوی production قوی نشان می‌دهد: workloadهای مورد اعتماد در CI/CD یا runtime به‌جای نگه‌داری API key بلندمدت، token هویتی خارجی را با access token کوتاه‌عمر exchange می‌کنند. AvalAI ممکن است همین endpoint تبادل token یا مدل service-account mapping را برای همه حساب‌ها expose نکند؛ بنابراین اصل طراحی را تطبیق دهید، نه API callهای مخصوص OpenAI را.

برای deploymentهای AvalAI این الگو را استفاده کنید:

- **تا حد امکان دسترسی keyless بسازید:** بگذارید GitHub Actions، Kubernetes، AWS، Azure، GCP یا SPIFFE با OIDC/workload identity به secret manager خودتان authenticate کند و `AVALAI_API_KEY` را درست هنگام اجرای job دریافت کند.
- **Claimها را دقیق match کنید:** issuer، audience، repository، branch/ref، environment، workflow، namespace یا service account را محدود کنید. mapping سازمانی گسترده نسازید و هرگز به pull requestهای fork نامطمئن credential production ندهید.
- **Identityها را جدا کنید:** برای CI، staging، runtime production، jobهای billing نمایندگان فروش و data backfill credential جدا داشته باشید. pipeline build نباید همان key اپلیکیشن live کاربرمحور را استفاده کند.
- **Tokenها را کوتاه‌عمر نگه دارید:** اگر پلتفرم شما secret موقت صادر می‌کند، فقط هنگام شروع job آن را exchange کنید، در logها mask کنید، و پس از incident کلید زیربنایی AvalAI را revoke یا rotate کنید.
- **Mappingها را audit کنید:** انتقال repository، branch protection، approvalهای environment، چرخش JWKS/key و workflowهای غیرفعال را review کنید؛ mapping هویتی قدیمی می‌تواند به مسیر دسترسی production تبدیل شود.

اگر AvalAI در آینده workload identity یا service-account mapping بومی اضافه کند، همان سطح امنیت را حفظ کنید: claim matching دقیق، least privilege، محیط‌های جدا، token کوتاه‌عمر و alert برای exchangeهای failed یا غیرمنتظره.

## ۵. Safety Gate اضافه کنید

- ورودی و خروجی پرریسک را با [`/v1/moderations`](fa/api-reference/moderation.md) بررسی کنید.
- خروجی‌های ساختاریافته را قبل از استفاده در سیستم downstream با schema اعتبارسنجی کنید.
- argumentهای ابزار را قبل از اجرا و خروجی ابزار را پیش از بازگرداندن به مدل validate کنید.
- برای refund، delete، write، shell command، اقدام مالی، تصمیم پزشکی/حقوقی/امنیتی و سایر side effectها approval انسانی بگذارید.
- برای prompt injection، سوءاستفاده از ابزار، نشت داده و فشار روی مرزهای policy، [تست‌های red-team](fa/guides/red-teaming.md) اجرا کنید.

## ۶. Evals و Rollout را آماده کنید

- یک golden dataset در repo نگه دارید که promptهای نماینده، edge caseها، رفتار مورد انتظار و rubricهای pass/fail را پوشش دهد.
- هر pull request که prompt، model ID، retrieval، ابزار، moderation یا routing را تغییر می‌دهد باید smoke eval سریع اجرا کند.
- پیش از launch، suite کامل را با [ارزیابی با Promptfoo و AvalAI](fa/examples/promptfoo_evals_with_avalai.md) یا runner CI خود اجرا کنید.
- تغییر را با traffic کوچک canary کنید، metricهای production را با نتایج eval مقایسه کنید و rollback config آماده داشته باشید.
- هر failure production را پیش از اصلاح prompt به eval set اضافه کنید.
- workflowهای long-context را در چند اندازه context اعتبارسنجی کنید تا regressionهای «گم شدن در میانه» پیش از launch دیده شوند.

## ۷. Scale و Rate Limit را مدیریت کنید

- برای محدودیت‌های تولیدشده فعلی بر اساس tier و مدل، صفحه [محدودیت‌های نرخ](fa/rate-limits.md) را بخوانید.
- برای خطای `429` و خطاهای گذرای `5xx`، exponential backoff همراه jitter پیاده‌سازی کنید.
- `x-ratelimit-*`، `avalai-request-id`، latency، token usage و وضعیت نهایی را در logها دنبال کنید.
- برای embeddings و کارهای batch-safe، اگر تعداد request را کم می‌کند و output token را زیاد نمی‌کند، batching انجام دهید.
- برای workloadهای bursty از queue و برای flowهای طولانی از workerهای app-managed استفاده کنید.

## ۸. Production را Observe کنید

به‌اندازه‌ای context log کنید که بتوان failure را بدون افشای secret بازتولید کرد:

- route، model، provider، service tier، نسخه prompt و نسخه deployment
- `avalai-request-id`، response ID، latency، retryها، حالت streaming و وضعیت نهایی
- input token، output token، cached token و هزینه تخمینی
- نام tool callها، argumentهای validateشده، وضعیت نتیجه و تصمیم‌های approval
- نتیجه moderation، hash مربوط به `safety_identifier` و دلیل failure در red-team/eval

## ۹. بازبینی Go/No-Go

فقط وقتی ship کنید که پاسخ همه پرسش‌ها «بله» باشد:

- آیا اپلیکیشن از API surface و model config مورد نظر استفاده می‌کند؟
- آیا API keyها، user IDها و logها از نظر حریم خصوصی امن هستند؟
- آیا access controlها، model allowlistها، مالک‌های هزینه و audit logها آماده‌اند؟
- آیا evalها، red-team testها و schema checkها پاس شده‌اند؟
- آیا مسیرهای rate limit، timeout، retry و rollback تست شده‌اند؟
- آیا تیم پشتیبانی می‌تواند گزارش کاربر را از `avalai-request-id` تا نسخه prompt و route مدل دنبال کند؟
- آیا UX درباره محدودیت‌های AI، مسیر review و تصمیم‌های unsafe-content شفاف است؟

## راهنماهای مرتبط

- [بهترین شیوه‌های Production](fa/guides/production-best-practices.md)
- [Responses در مقابل Chat Completions](fa/guides/responses-vs-chat-completions.md)
- [کنترل داده‌ها](fa/guides/data-controls.md)
- [محدودیت‌های نرخ](fa/rate-limits.md)
- [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md)
- [Red Teaming برای اپلیکیشن‌های هوش مصنوعی](fa/guides/red-teaming.md)
- [بهینه‌سازی هزینه](fa/guides/cost-optimization.md)
