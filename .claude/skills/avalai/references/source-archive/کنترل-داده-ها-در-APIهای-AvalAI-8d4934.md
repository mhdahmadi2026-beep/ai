# کنترل داده‌ها در APIهای AvalAI

از این راهنما برای طراحی integrationهای امن از نظر حریم خصوصی در AvalAI استفاده کنید. این متن راهنماهای رسمی OpenAI درباره [کنترل داده‌ها](https://developers.openai.com/api/docs/guides/your-data)، [وضعیت مکالمه](https://developers.openai.com/api/docs/guides/conversation-state)، [پردازش پس‌زمینه](https://developers.openai.com/api/docs/guides/background) و [کش کردن پرامپت](https://developers.openai.com/api/docs/guides/prompt-caching) را برای gateway سازگار با OpenAI در AvalAI تطبیق می‌دهد.

سیاست API خود AvalAI در [سیاست حفظ حریم خصوصی](fa/safety/privacy-policy.md) و [سیاست محتوا](fa/safety/content-policy.md) توضیح داده شده است. از آنجا که AvalAI درخواست‌ها را به ارائه‌دهندگان بالادستی route می‌کند، همیشه بین **metadata سرویس AvalAI** و **application state سمت ارائه‌دهنده** تفاوت بگذارید.

## لایه‌های داده

| لایه | ممکن است شامل چه چیزی باشد | اقدام توسعه‌دهنده |
| --- | --- | --- |
| محتوای درخواست و پاسخ | prompt، پیام‌ها، خروجی ابزار، فایل، تصویر، صوت | فقط حداقل داده لازم برای انجام کار را ارسال کنید. |
| metadata سرویس AvalAI | مدل، route، مصرف token، هزینه، IP، request ID | logها را فقط برای billing، پشتیبانی، debug محدودیت نرخ و بررسی سوءاستفاده نگه دارید. |
| application state ارائه‌دهنده | Response ذخیره‌شده، فایل‌ها، batchها، vector storeها، jobهای پس‌زمینه | در صورت پشتیبانی از `store: false`، `expires_after`، API حذف یا state مدیریت‌شده در برنامه استفاده کنید. |
| ابزارها و سرویس‌های ثالث | جستجوی وب، سرورهای MCP، APIهای خارجی، سرویس‌های native ارائه‌دهنده | پیش از ارسال داده مشتری، سیاست نگه‌داری هر سرویس را بررسی کنید. |

## رفتارهای مرجع OpenAI برای تطبیق

رفتارهای منتشرشده OpenAI را به‌عنوان checklist استفاده کنید، سپس پیش از دادن تضمین نگه‌داری، route دقیق AvalAI و provider بالادستی را verify کنید:

OpenAI بین **logهای بررسی سوءاستفاده** و **application state** تفاوت می‌گذارد: logهای abuse monitoring ممکن است prompt، پاسخ و metadata ایمنی مشتق‌شده را برای اجرای policy نگه دارند، اما application state داده‌ای است که یک قابلیت برای انجام درخواست باید persist کند. در AvalAI همین مدل ذهنی را نگه دارید، اما آن را به route و provider انتخابی نگاشت کنید. metadata عملیاتی مانند `avalai-request-id`، مدل، usage، هزینه و error class را از محتوای مشتری جدا ذخیره کنید و logهای billing یا support را جای امنی برای prompt کامل فرض نکنید.

پیش‌فرض‌های مرجع OpenAI برای review ریسک عددهای مفیدی هستند، اما تضمین خودکار AvalAI نیستند: logهای abuse monitoring معمولا تا ۳۰ روز نگه‌داری می‌شوند، Responseهای ذخیره‌شده وقتی storage فعال است دست‌کم ۳۰ روز نگه‌داری می‌شوند، Responseهای background برای polling داده را کوتاه‌مدت نگه می‌دارند، و خروجی صوتی می‌تواند برای audio چندنوبتی state کوتاه‌عمر بسازد. Zero Data Retention و Modified Abuse Monitoring کنترل‌های تأییدشده حساب هستند؛ در رفتار ZDR OpenAI، `store` مثل `false` در نظر گرفته می‌شود، اما endpointهایی که به application state نیاز دارند ممکن است همچنان واجد شرایط نباشند. هر ادعای AvalAI را وابسته به route، provider و قرارداد همان مشتری بدانید.

| قابلیت | رفتار مرجع OpenAI | پیش‌فرض امن در AvalAI |
| --- | --- | --- |
| آموزش API | داده API برای آموزش مدل‌های OpenAI استفاده نمی‌شود مگر اینکه صریحا opt in شود. | سیاست آموزش provider بالادستی را فرض نکنید؛ قرارداد همان route را مستند کنید. |
| `/v1/responses` | Response ذخیره‌شده به‌صورت پیش‌فرض یا با `store: true` نگه‌داری می‌شود؛ `store: false` بازیابی بعدی را غیرفعال می‌کند. | مگر اینکه محصول به retrieval بعدی یا `previous_response_id` نیاز دارد، `store: false` بگذارید. |
| background mode | برای polling، داده Response را کوتاه‌مدت ذخیره می‌کند و به state ذخیره‌شده نیاز دارد. | فقط در صورت پشتیبانی route استفاده کنید؛ در غیر این صورت job async و فراخوانی stateless خودتان را اجرا کنید. |
| فایل‌ها و batchها | فایل‌های آپلودشده، batchها، evalها و artifactهای fine-tuning تا حذف یا انقضا persist می‌شوند. | در صورت پشتیبانی `expires_after` بگذارید و cleanup job زمان‌بندی کنید. |
| ابزارها و MCP | داده ارسال‌شده به ابزار remote یا سرور MCP تابع policy همان third party است. | هر tool call را انتقال داده به سرویس خارجی طبقه‌بندی کنید. |
| prompt caching | cache می‌تواند latency/cost را بهتر کند، اما مرز حذف یا حریم خصوصی نیست. | داده اختصاصی کاربر را بعد از prefix مشترک بگذارید و شناسه خام در cache key نفرستید. |

### کنترل‌های نگه‌داری عمومی نیستند

کنترل‌های Zero Data Retention و Modified Abuse Monitoring در OpenAI تنظیمات تاییدشده حساب هستند، نه flagهایی که هر endpoint به صورت خودکار رعایت کند. حتی اگر یک provider کنترل مشابهی ارائه دهد، بعضی قابلیت‌ها ممکن است همچنان application state بسازند، چون بدون آن کار نمی‌کنند: response ذخیره‌شده، polling پس‌زمینه، فایل‌ها، batchها، artifactهای eval، vector storeها، ابزارهای hosted، jobهای ویدیو یا tool callهای third-party. در deploymentهای AvalAI، retention را یک قرارداد per-route بدانید: پیش از پذیرش داده regulated یا وعده دادن timeline حذف، مدل، endpoint، provider و feature flagهای انتخابی را تایید کنید.

اگر طراحی privacy شما به رفتار stateless وابسته است، `store: false`، history مدیریت‌شده در برنامه، فایل‌های کوتاه‌عمر، cleanup job صریح و فراخوانی مستقل `/v1/moderations` را ترجیح دهید؛ این مسیرها application state کمتری می‌سازند.

### بررسی‌های مخصوص Responses برای نگه‌داری داده

برای workflowهای Responses، پیش از launch این سطح‌ها را review کنید:

- **Responseهای ذخیره‌شده:** وقتی یک route رفتار storage به سبک OpenAI را رعایت کند، Response ممکن است بعدا قابل retrieve باشد مگر اینکه `store: false` بگذارید؛ retention مرجع OpenAI برای Response ذخیره‌شده دست‌کم ۳۰ روز است. فقط برای featureهایی که به `previous_response_id`، polling، retrieval یا debugging با تأیید retention نیاز دارند از `store: true` استفاده کنید.
- **Background mode:** رفتار مرجع OpenAI برای امکان polling یا reconnect، داده Response را حدود ۱۰ دقیقه ذخیره می‌کند. در AvalAI، `background: true` را با طراحی‌های strict stateless یا zero-retention ناسازگار بدانید، مگر اینکه قرارداد route شما چیز دیگری بگوید.
- **خروجی صوتی:** workflowهای صوتی چندنوبتی ممکن است به application state کوتاه‌عمر نیاز داشته باشند تا turnهای بعدی بتوانند به audio تولیدشده ارجاع دهند؛ retention مرجع OpenAI برای این state یک ساعت است. نگه‌داری صوت را در data-flow diagram از نگه‌داری پاسخ متنی جدا کنید.
- **فشرده‌سازی:** فشرده‌سازی server-side برای حمل machine state opaque طراحی شده است. اگر route از `store: false` پشتیبانی می‌کند، compaction itemها را بیرون از policy نگه‌داری خودتان persist نکنید.
- **ابزارهای third-party:** سرورهای MCP remote، ابزارهای hosted code/shell، جستجوی زنده وب و connectorهای native provider می‌توانند تعهدات retention خارجی جداگانه بسازند. آن‌ها را data processor مستند کنید، نه پارامتر عادی مدل.

## پیش‌فرض Stateless

برای workflowهای جدید Responses API، مگر اینکه واقعا نیاز دارید پاسخ را بعدا بازیابی کنید، `store: false` را تنظیم کنید. اگر route انتخاب‌شده از `store` پشتیبانی نمی‌کند، رفتار را وابسته به ارائه‌دهنده بدانید و سیاست نگه‌داری برنامه خودتان را محافظه‌کارانه نگه دارید.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model=os.getenv("AVALAI_MODEL", "gpt-5.6-luna"),
    instructions="Answer using only the provided support policy.",
    input="Summarize the refund policy in two bullets.",
    store=False,
    safety_identifier="user_hash_8f3a2c",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: process.env.AVALAI_MODEL ?? "gpt-5.6-luna",
  instructions: "Answer using only the provided support policy.",
  input: "Summarize the refund policy in two bullets.",
  store: false,
  safety_identifier: "user_hash_8f3a2c",
});

console.log(response.output_text);

```

در Chat Completions فقط نوبت‌هایی را دوباره بفرستید که برای پاسخ لازم هستند و اگر policy اجازه می‌دهد، حافظه بلندمدت مکالمه را در پایگاه‌داده خودتان نگه دارید. به‌صورت پیش‌فرض prompt کامل را log نکنید.

برای reasoning چندنوبتی stateless، بدون ذخیره Response object هم می‌توانید continuity لازم را حفظ کنید: encrypted reasoning items را درخواست کنید و itemهای `response.output` برگشتی را در history خودتان replay کنید.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

history = [{"role": "user", "content": "Draft a two-step migration plan."}]

response = client.responses.create(
    model=os.getenv("AVALAI_MODEL", "gpt-5.6-luna"),
    input=history,
    store=False,
    include=["reasoning.encrypted_content"],
)

history += response.output
history.append({"role": "user", "content": "Now make it safer for production."})

follow_up = client.responses.create(
    model=os.getenv("AVALAI_MODEL", "gpt-5.6-luna"),
    input=history,
    store=False,
    include=["reasoning.encrypted_content"],
)

print(follow_up.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const history = [{ role: "user", content: "Draft a two-step migration plan." }];

const response = await client.responses.create({
  model: process.env.AVALAI_MODEL ?? "gpt-5.6-luna",
  input: history,
  store: false,
  include: ["reasoning.encrypted_content"],
});

history.push(...response.output);
history.push({ role: "user", content: "Now make it safer for production." });

const followUp = await client.responses.create({
  model: process.env.AVALAI_MODEL ?? "gpt-5.6-luna",
  input: history,
  store: false,
  include: ["reasoning.encrypted_content"],
});

console.log(followUp.output_text);

```

## چه زمانی State ذخیره‌شده مفید است؟

برخی قابلیت‌ها برای عملکرد بهتر به state ذخیره‌شده نیاز دارند:

- **`previous_response_id` و شیءهای conversation:** برای workflowهای چندنوبتی مفید هستند، اما برای داده‌های حساس یا regulated، replay دستی همراه با `store: false` را ترجیح دهید.
- **پردازش پس‌زمینه:** background mode مرجع OpenAI برای polling، داده Response را کوتاه‌مدت ذخیره می‌کند و به state ذخیره‌شده نیاز دارد. در AvalAI فقط وقتی route انتخابی پشتیبانی می‌کند از `background: true` میزبانی‌شده استفاده کنید؛ در غیر این صورت job table خودتان و فراخوانی stateless مدل را به‌کار ببرید.
- **Files API:** برای فایل‌های موقت `expires_after` بگذارید و وقتی دیگر به فایل نیاز ندارید DELETE را فراخوانی کنید.
- **Batch، evalها، fine-tuning و vector storeها:** datasetهای آپلودشده و artifactهای تولیدشده را تا زمان حذف یا انقضای provider، persistent فرض کنید.

## کش کردن پرامپت و حریم خصوصی

Prompt caching یک بهینه‌سازی است، نه مرز کنترل داده. با دقت از آن استفاده کنید:

- متن policy پایدار و schema ابزارها را ابتدا، و جزئیات اختصاصی کاربر را انتهای prompt قرار دهید.
- از `prompt_cache_key` برای bucket کردن workload استفاده کنید، نه به‌عنوان شناسه خام کاربر.
- `prompt_cache_key` را از `safety_identifier` جدا نگه دارید.
- `prompt_cache_retention` را فقط وقتی استفاده کنید که مدل، route و حساب انتخابی از آن پشتیبانی کنند.
- برای نیازهای سخت‌گیرانه نگه‌داری، بررسی کنید provider از cache در حافظه یا cache extended استفاده می‌کند.
- برای مدل‌های خانواده OpenAI که به extended prompt caching نیاز دارند، `prompt_cache_retention: "in_memory"` را تنظیم نکنید مگر اینکه route انتخابی AvalAI صریحا پشتیبانی آن را مستند کرده باشد.

OpenAI مستند کرده که extended prompt caching در مدل‌های پشتیبانی‌شده می‌تواند key/value tensorهای مدل را تا ۲۴ ساعت نگه دارد؛ در AvalAI فعال بودن این قابلیت به route بالادستی وابسته است. بدون تأیید provider، به مشتریان تضمین cache-retention ندهید.

## بهداشت فایل و ابزار

- URL عمومی را فقط برای سندهای عمومی به‌کار ببرید؛ برای سندهای خصوصی از Base64 یا Files API استفاده کنید.
- اگر فایل نیاز به استفاده مجدد ندارد، پس از پردازش آن را حذف کنید.
- ورودی‌های تصویر و فایل را سطح نگه‌داری ویژه بدانید: scannerهای ایمنی بالادستی ممکن است رسانه flag شده را حتی با فعال بودن کنترل‌های سخت‌گیرانه‌تر برای بازبینی دستی نگه دارند.
- secretها، credentialها، اطلاعات پرداخت، private keyها و PII نامرتبط را پیش از فراخوانی مدل حذف یا redact کنید.
- argumentهای ابزار را پیش از اجرا و خروجی ابزار را پیش از بازگرداندن به مدل validate کنید.
- پیش از تغییر حساب، ارسال پیام، حذف داده، پرداخت یا فراخوانی سیستم خارجی، approval انسانی بگیرید.
- جستجوی وب زنده، سرورهای Remote MCP، ابزارهای hosted code/shell و connectorهای native ارائه‌دهنده را پردازش خارجی یا provider-managed طبقه‌بندی کنید. فقط وقتی route انتخابی AvalAI صریحا پشتیبانی می‌کند از حالت‌های جستجوی offline/cache-only استفاده کنید، و فرض نکنید نگه‌داری، residency، HIPAA یا شرایط BAA سرویس‌های ثالث با policy AvalAI یکی است.

## Data Residency و Routeهای منطقه‌ای

کنترل‌های data residency در OpenAI در سطح project تنظیم می‌شوند و برای endpointها، مدل‌ها و تنظیمات حساب واجد شرایط از دامنه‌های API منطقه‌ای استفاده می‌کنند. وقتی از طریق AvalAI فراخوانی می‌کنید، فرض نکنید دامنه‌های منطقه‌ای OpenAI، تنظیمات Zero Data Retention یا تضمین‌های پردازش منطقه‌ای به‌صورت خودکار روی route انتخابی AvalAI اعمال می‌شوند.

برای deploymentهای regulated، پیش از launch یک رکورد شواهد برای route ارائه‌دهنده نگه دارید:

- endpoint انتخابی AvalAI، provider، model ID و service tier؛
- اینکه customer content فقط در region لازم ذخیره می‌شود، در همان region پردازش می‌شود یا global route می‌شود؛
- اینکه prompt caching، jobهای پس‌زمینه، Files API، ابزارها، web search، تولید ویدیو یا connectorهای native ارائه‌دهنده خارج از model call اصلی application state می‌سازند یا نه؛
- اینکه حساب مشتری برای همان route قرارداد data-processing، residency، BAA/HIPAA یا enterprise retention امضاشده دارد یا نه؛
- رفتار fallback اگر route منطقه‌ای ترجیحی در دسترس نباشد.

Residency را از کنترل‌های امنیتی جدا نگه دارید. رمزنگاری، `store: false`، moderation، prompt caching و data residency مسائل متفاوتی را حل می‌کنند و باید مستقل از هم verify شوند.

## مدیریت کلید سازمانی و BYOK

OpenAI برای application stateهای واجد شرایط Enterprise Key Management (EKM) را مستند کرده است؛ در این حالت کلیدها از سیستم‌های مدیریت کلید خارجی پشتیبانی‌شده sync می‌شوند. وقتی از طریق AvalAI یا provider بالادستی دیگری به مدل‌ها دسترسی دارید، فرض نکنید این کنترل‌های OpenAI به‌صورت خودکار اعمال می‌شوند.

برای نیازهای customer-managed encryption:

- بررسی کنید route دقیق AvalAI، provider، endpoint و نوع artifact ذخیره‌شده از BYOK/EKM پشتیبانی می‌کند یا نه؛
- مشخص کنید کدام state پوشش داده می‌شود: Responseهای ذخیره‌شده، آبجکت‌های Files API، vector storeها، batchها، evalها، artifactهای fine-tuning، containerهای ابزار hosted یا logهای provider؛
- مسیر خطا را برای endpointی که با policy مدیریت کلید مشتری سازگار نیست تعریف کنید؛
- حتی اگر provider برای application state خودش EKM ارائه کند، رمزنگاری سمت برنامه را برای دیتابیس‌ها، logها، queueها و object storage خودتان نگه دارید.

## چک‌لیست Production

- برای هر route که محتوای مشتری می‌گیرد، data-flow diagram بسازید.
- مشخص کنید هر درخواست از `store`، `previous_response_id`، background mode، Files API، Batch API، ابزارها یا جستجوی خارجی استفاده می‌کند یا نه.
- ثبت کنید application state سمت provider تحت customer-managed encryption پوشش داده می‌شود یا باید برای آن workflow از آن اجتناب شود.
- مقدار `safety_identifier` را hash پایدار یا شناسه opaque بگذارید؛ ایمیل، تلفن یا username خام نفرستید.
- `avalai-request-id`، مدل، route، token usage، latency و error class را بدون ذخیره کامل محتوای مشتری log کنید.
- قبل از پذیرش داده regulated یا حساس، رفتار نگه‌داری provider را برای همان مدل و endpoint بررسی کنید.

## راهنماهای مرتبط

- [سیاست حفظ حریم خصوصی](fa/safety/privacy-policy.md)
- [سیاست محتوا](fa/safety/content-policy.md)
- [وضعیت مکالمه](fa/guides/conversation-state.md)
- [پردازش پس‌زمینه](fa/guides/background-processing.md)
- [کش کردن پرامپت](fa/guides/prompt-caching.md)
- [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md)
- [API فایل‌ها](fa/api-reference/files.md)
