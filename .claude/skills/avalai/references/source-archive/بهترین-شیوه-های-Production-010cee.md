# بهترین شیوه‌های Production

انتقال پروژه‌های هوش مصنوعی به Production با بهترین شیوه‌ها.

این راهنما مجموعه‌ای جامع از بهترین شیوه‌ها را برای کمک به انتقال از نمونه اولیه به مرحله استقرار ارائه می‌دهد. چه یک مهندس یادگیری ماشین باتجربه باشید و چه یک علاقه‌مند جدید، این راهنما باید ابزارهایی را که برای استفاده موفق از پلتفرم در یک محیط عملیاتی نیاز دارید در اختیار شما قرار دهد: از ایمن‌سازی دسترسی به API ما تا طراحی یک معماری قوی که می‌تواند حجم ترافیک بالا را مدیریت کند. از این راهنما برای کمک به توسعه یک برنامه برای استقرار برنامه خود به صورت هرچه روان‌تر و موثرتر استفاده کنید.

## راه‌اندازی سازمان شما

### کلیدهای API

API AvalAI از کلیدهای API برای احراز هویت استفاده می‌کند. از صفحه کلیدهای API خود بازدید کنید تا کلید API که در درخواست‌های خود استفاده خواهید کرد را دریافت کنید.

این یک روش نسبتا ساده برای کنترل دسترسی است، اما باید در ایمن نگه داشتن این کلیدها هوشیار باشید:

- **کلیدهای API خود را ایمن نگه دارید**: هرگز کلیدهای API خود را در کد سمت کلاینت یا مخازن عمومی افشا نکنید.
- **از متغیرهای محیطی استفاده کنید**: کلیدهای API خود را به جای کدگذاری سخت، در متغیرهای محیطی ذخیره کنید.
- **کلیدهای API جداگانه ایجاد کنید**: از کلیدهای API مختلف برای محیط‌های توسعه، آزمایش و عملیاتی استفاده کنید.
- **کلیدهای API را به طور منظم بچرخانید**: به طور دوره‌ای کلیدهای API خود را برای افزایش امنیت بازتولید کنید.

### مدیریت محدودیت‌های استفاده

برای نظارت بر استفاده خود، می‌توانید یک آستانه اطلاع‌رسانی در حساب خود تنظیم کنید تا پس از عبور از یک آستانه استفاده مشخص، هشدار ایمیلی دریافت کنید. همچنین می‌توانید یک بودجه ماهانه تعیین کنید. لطفا به پتانسیل ایجاد اختلال در برنامه/کاربران خود توسط بودجه ماهانه توجه داشته باشید. از داشبورد پیگیری استفاده برای نظارت بر استفاده از توکن خود در طول چرخه‌های صورتحساب فعلی و گذشته استفاده کنید.

### جداسازی staging و production

راهنمای production OpenAI توصیه می‌کند staging را از production جدا کنید تا تست‌ها نتوانند quota، هزینه یا داده مشتریان زنده را مختل کنند. همین الگو را در AvalAI هم اعمال کنید:

- برای توسعه محلی، staging و production از API key، project یا حساب جدا استفاده کنید.
- دسترسی production را فقط به سرویس‌ها و operatorهایی بدهید که واقعا نیاز دارند.
- در staging هشدارهای هزینه و rate limit پایین‌تری بگذارید تا تست‌های runaway با ایمنی fail شوند.
- model ID، route ارائه‌دهنده و feature flagها را در environment variable نگه دارید تا rollback به deploy کد نیاز نداشته باشد.
- قابلیت‌های وابسته به route مثل Response ذخیره‌شده، jobهای پس‌زمینه، ابزارهای hosted، پاک‌سازی Files API و sessionهای Realtime را پیش از وعده دادن رفتار production در staging تست کنید.

## مدیریت نسخه مدل

هنگام انتقال به محیط عملیاتی، مدیریت صحیح نسخه مدل برای پایداری و نگهداری بلندمدت بسیار حیاتی است.

### استفاده از فضای نام مدل‌های پایدار

> **بهترین شیوه:** همیشه از فضاهای نام مدل پایدار (stable) زمانی که در دسترس قرار می‌گیرند استفاده کنید. وقتی یک مدل پیش‌نمایش برای اولین بار معرفی می‌شود (مثلا `gemini-2.5-flash-image-preview`)، ممکن است بعدا به عنوان نسخه پایدار منتشر شود (مثلا `gemini-2.5-flash-image`). در چنین مواردی، در اسرع وقت به نسخه پایدار و غیر پیش‌نمایش مهاجرت کنید تا از پشتیبانی مداوم و عملکرد بهینه برخوردار شوید.

**چرا این مهم است:**
- مدل‌های پیش‌نمایش ممکن است با اطلاع‌رسانی محدود منسوخ شوند
- مدل‌های پایدار پشتیبانی بهتر و دوره‌های دسترسی طولانی‌تری دریافت می‌کنند
- سیستم‌های عملیاتی به رفتار قابل پیش‌بینی مدل نیاز دارند

**نکات پیاده‌سازی:**
- برای اطلاع از تغییرات چرخه حیات مدل، در [اعلانات منسوخ شدن](fa/deprecations.md) عضو شوید
- پیکربندی نام مدل را به عنوان متغیرهای محیطی برای به‌روزرسانی آسان پیاده‌سازی کنید
- قبل از ضرب‌الاجل منسوخ شدن مدل پیش‌نمایش، یک برنامه مهاجرت ایجاد کنید

```python
import os

# خوب: استفاده از متغیر محیطی برای به‌روزرسانی آسان مدل
MODEL_NAME = os.getenv("AI_MODEL", "gemini-2.5-flash-image")  # استفاده از نسخه پایدار

# از کدگذاری سخت مدل‌های پیش‌نمایش در محیط عملیاتی خودداری کنید
# بد: model = "gemini-2.5-flash-image-preview"  # مدل‌های پیش‌نمایش منسوخ می‌شوند
```

## محدودیت‌های نرخ

درک و مدیریت صحیح محدودیت‌های نرخ برای برنامه‌های عملیاتی ضروری است. برای اطلاعات جامع، [راهنمای محدودیت‌های نرخ](fa/rate-limits.md) را مشاهده کنید.

## گردش‌کارهای Reasoning و Agentic

برای workloadهای جدید سری GPT-5 و agentic، از [Responses API](fa/api-reference/responses.md) شروع کنید مگر اینکه در حال نگهداری یک ادغام موجود Chat Completions باشید. کیفیت reasoning، orchestration ابزارها، خروجی ساختاریافته، prompt caching و مدیریت state زمانی بهتر عمل می‌کنند که با هم طراحی شوند.

### چک‌لیست Production

- **state مناسب را انتخاب کنید:** برای flowهای چندنوبتی ساده از `previous_response_id`، برای flowهای stateless یا حساس به compliance از ارسال دستی itemها، و برای عامل‌های طولانی‌مدت از فشرده‌سازی context استفاده کنید.
- **instructionهای state را صریح نگه دارید:** هنگام استفاده از `previous_response_id`، `instructions` ثابت را در هر درخواست دوباره بفرستید و فقط وقتی policy نگهداری داده اجازه می‌دهد `store: true` استفاده کنید.
- **reasoning را آگاهانه تنظیم کنید:** GPT-5.5 به‌صورت پیش‌فرض `medium` است؛ `reasoning.effort` را روی کمترین سطحی بگذارید که evalها را پاس می‌کند و `high` یا `xhigh` را برای تصمیم‌هایی نگه دارید که latency و هزینه token بیشتر توجیه دارد.
- **طول پاسخ را جداگانه کنترل کنید:** به جای اینکه فرض کنید reasoning بیشتر یعنی پاسخ طولانی‌تر، از `text.verbosity`، محدودیت کلمه، تعداد بخش، عرض جدول یا دستور JSON-only استفاده کنید.
- **برای قرارداد خروجی از schema استفاده کنید، نه فقط prose:** [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md) با `text.format` را به توصیف JSON فقط در prompt ترجیح دهید.
- **context قابل cache را ثابت نگه دارید:** policy یا context محصول طولانی و قابل استفاده مجدد را ابتدای درخواست بگذارید، facts پویای کاربر را نزدیک انتها قرار دهید، و برای الگوهای ترافیک تکراری از `prompt_cache_key` ثابت استفاده کنید.
- **توضیح ابزارها را مثل interface بنویسید:** مشخص کنید هر ابزار چه کاری انجام می‌دهد، چه زمانی فراخوانی می‌شود، ورودی‌های الزامی چیست، چه side effectهایی دارد، retry چه زمانی امن است و خطاهای رایج چیست.
- **پیشرفت را در UX نشان دهید:** برای flowهای tool-heavy از preamble یا status کوتاه استفاده کنید تا کاربر قبل از پاسخ نهایی بداند دستیار چه چیزی را بررسی می‌کند.

هنگام مهاجرت promptهای قدیمی به GPT-5.5، با کوچک‌ترین promptی شروع کنید که قرارداد محصول را حفظ می‌کند. outcome، معیار موفقیت، side effectهای مجاز، قوانین evidence و شکل خروجی را نگه دارید؛ guidance مرحله‌به‌مرحله قدیمی را حذف کنید مگر اینکه همان فرایند دقیق لازم باشد.

### قابلیت‌های پیشرفته Responses را در staging gate کنید

چک‌لیست استقرار OpenAI منبع خوبی برای اهرم‌های پیشرفته production است، اما AvalAI درخواست‌ها را بین چند provider route می‌کند. قابلیت‌های hosted را تا زمانی که همان endpoint، مدل و provider را در staging تست نکرده‌اید، وابسته به route فرض کنید.

| قابلیت | زمان استفاده | چک release در AvalAI |
| --- | --- | --- |
| `tool_search` / ابزار deferred | اپلیکیشن catalog ابزار بزرگی دارد | اگر discovery میزبانی‌شده فعال نیست، ابزارها را قبل از فراخوانی AvalAI در خود اپلیکیشن فیلتر کنید. |
| ابزارهای hosted | به web search، file search، اجرای کد، تولید تصویر یا workflowهای شبیه computer-use نیاز دارید | ابتدا endpointهای مستند AvalAI را ترجیح دهید؛ ابزارهای hosted بومی provider را قبل از اتکا verify کنید. |
| Compaction | agentهای طولانی state مهم را زیر logهای قدیمی یا trace ابزارها گم می‌کنند | فقط در صورت پشتیبانی از compaction میزبانی‌شده استفاده کنید؛ در غیر این صورت summary مدیریت‌شده در app بسازید که decisionها، IDها و taskهای باز را نگه دارد. |
| `reasoning.encrypted_content` | به continuity استدلال بدون ذخیره state نیاز دارید | reasoning itemهای برگشتی را در صورت وجود دقیقا round-trip کنید؛ آن‌ها را parse یا rewrite نکنید. |
| `background: true` | کار ممکن است از یک request معمولی طولانی‌تر شود یا به polling نیاز دارد | مگر اینکه route انتخابی Responses پشتیبانی background میزبانی‌شده را ثابت کند، از jobهای app-managed استفاده کنید. |
| WebSocket mode | agent ابزارمحور در چندین turn ادامه پیدا می‌کند | مگر اینکه staging پشتیبانی WebSocket و مسیر recovery را ثابت کند، HTTP همراه `previous_response_id` یا replay دستی را نگه دارید. |

چک‌لیست go/no-go عمیق‌تر را در [چک‌لیست استقرار API](fa/guides/deployment-checklist.md) نگه دارید و قابلیت‌های hosted پشتیبانی‌نشده را به‌عنوان تصمیم محصول صریح ثبت کنید، نه فرض پنهان.

### Observability

`avalai-request-id`، مدل، endpoint، service tier، latency، input tokens، output tokens، cached input tokens، تعداد tool callها و وضعیت نهایی را log کنید. برای workflowهای زنجیره‌ای Responses، هم response ID فعلی و هم state strategy استفاده‌شده را ثبت کنید تا تیم پشتیبانی بتواند خطاها را بدون حدس درباره مسیر context بازتولید کند.

### انتشار مطمئن: eval، guardrail و rollout

قبل از اینکه تغییر prompt، مدل، schema ابزار یا منطق retrieval وارد production شود، معیار انتشار را قابل اندازه‌گیری و تکرارپذیر کنید:

- **KPI و SLO تعریف کنید:** دقت task، کیفیت refusal، نرخ hallucination، نرخ موفقیت tool، latency صدک ۹۵، هزینه token و نرخ خطا را از logها دنبال کنید، نه از review حسی.
- **golden eval set نگه دارید:** ورودی‌های نماینده کاربران، رفتار مورد انتظار، rubricهای pass/fail و edge caseهای شناخته‌شده را در repo ذخیره کنید؛ تا زمانی که hosted eval endpointهای AvalAI فعال شوند، برای اجراهای محلی و CI از [ارزیابی‌ها](fa/guides/evals.md) و [ارزیابی با Promptfoo و AvalAI](fa/examples/promptfoo_evals_with_avalai.md) استفاده کنید.
- **graderهای خودکار را کالیبره کنید:** LLM-as-judge یا graderهای rubric-based را فقط بعد از مقایسه با labelهای انسانی وارد CI کنید؛ برای تصمیم‌های safety، مالی، حقوقی، پزشکی، حذف داده و سایر اقدامات high-impact همچنان human review بگذارید.
- **guardrail را در مرز درست قرار دهید:** ورودی کاربر را قبل از کار پرهزینه، argumentهای ابزار را قبل از side effect، خروجی نهایی را قبل از تحویل، و اقداماتی را که state تولیدی را تغییر می‌دهند با approval انسانی بررسی کنید. [workflow عاملی با guardrail](fa/examples/agentic_guardrails_schema_workflow.md) را ببینید.
- **rollout تدریجی داشته باشید:** نسخه فعلی مدل و prompt را pin کنید، candidate را با A/B یا canary traffic اجرا کنید، metricهای eval و production را کنار هم ببینید و مسیر rollback آماده داشته باشید.

eval را بخشی از توسعه بدانید، نه چک‌لیست روز انتشار. قبل از اصلاح prompt، شکست‌های production را به dataset اضافه کنید تا همان bug دوباره بی‌صدا برنگردد.

### استراتژی‌های کلیدی محدودیت نرخ

- **پیاده‌سازی عقب‌نشینی نمایی**: هنگامی که به محدودیت‌های نرخ برخورد می‌کنید، از عقب‌نشینی نمایی برای تلاش مجدد درخواست‌ها استفاده کنید.
- **نظارت بر استفاده خود**: به طور منظم استفاده از API خود را بررسی کنید تا از مشکلات غیرمنتظره محدودیت نرخ جلوگیری کنید.
- **در صورت امکان درخواست‌ها را دسته‌بندی کنید**: برای عملیاتی مانند تعبیه‌سازی‌‌ها، چندین ورودی را در یک درخواست واحد دسته‌بندی کنید.
- **استفاده از هدرهای پاسخ**: برای مدیریت پیشگیرانه نرخ درخواست‌ها، هدرهای محدودیت نرخ را نظارت کنید.

### استفاده از هدرهای پاسخ برای مدیریت محدودیت نرخ

هر پاسخ API شامل هدرهایی است که اطلاعات ارزشمندی درباره وضعیت محدودیت نرخ شما ارائه می‌دهند. از این هدرها برای پیاده‌سازی محدودیت نرخ پیشگیرانه در برنامه خود استفاده کنید. برای مستندات دقیق، [هدرهای پاسخ](fa/api-reference/response-headers.md) را مشاهده کنید.

```python
import requests


def make_api_request_with_rate_limit_monitoring(prompt):
    response = requests.post(
        "https://api.avalai.ir/v1/chat/completions",
        headers={"Authorization": f"Bearer {api_key}"},
        json={
            "model": "gpt-5.6-luna",
            "messages": [{"role": "user", "content": prompt}],
        },
    )

    # نظارت پیشگیرانه بر محدودیت‌های نرخ
    remaining_requests = int(response.headers.get("x-ratelimit-remaining-requests", 0))
    remaining_tokens = int(response.headers.get("x-ratelimit-remaining-tokens", 0))
    reset_time = response.headers.get("x-ratelimit-reset-requests", "")

    # پیاده‌سازی عقب‌نشینی پیشگیرانه هنگام نزدیک شدن به محدودیت‌ها
    if remaining_requests < 100:
        print(
            f"⚠️ درخواست‌ها کم است: {remaining_requests} باقی‌مانده، بازنشانی در {reset_time}"
        )
        time.sleep(1)  # توقف کوتاه برای جلوگیری از رسیدن به محدودیت‌ها

    return response
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### محدودیت‌های نرخ بر اساس سطح

محدودیت‌های نرخ شما به سطح حساب شما (0-5) بستگی دارد. سطوح بالاتر محدودیت‌های بالاتری دارند و ارتقا به‌محض احراز شرایط به‌صورت خودکار انجام می‌شود:

| سطح | شرایط و اعتبار رایگان ثبت‌نام |
|------|--------------------------------|
| سطح پایه (Tier 0) | ثبت‌نام فقط با ایمیل؛ شامل ۲۵٬۰۰۰ تومان اعتبار فعال‌سازی رایگان |
| سطح ۱ | ثبت‌نام با تلفن تأییدشده برای دریافت مجموع ۲۰۰٬۰۰۰ تومان، یا افزودن تلفن تأییدشده به حساب ایمیلی برای دریافت ۱۷۵٬۰۰۰ تومان دیگر؛ بدون نیاز به شارژ |
| سطح 2 | مجموع شارژ معادل ۱۰ دلار |
| سطح 3 | مجموع شارژ معادل ۵۰ دلار |
| سطح 4 | مجموع شارژ معادل ۲۵۰ دلار |
| سطح 5 | مجموع شارژ معادل ۱٬۰۰۰ دلار |

پاداش تلفن، مجموع اعتبار رایگان ثبت‌نام را به **۲۰۰٬۰۰۰ تومان** می‌رساند و ۲۰۰٬۰۰۰ تومان جداگانه علاوه بر اعتبار ایمیل نیست. برای محدودیت‌های نرخ دقیق هر مدل، [مستندات محدودیت‌های نرخ](fa/rate-limits.md) را مشاهده کنید.

## مقیاس‌پذیری معماری راه‌حل شما

هنگام طراحی برنامه یا سرویس خود برای مرحله استقرار که از API ما استفاده می‌کند، مهم است که در نظر بگیرید چگونه برای پاسخگویی به تقاضاهای ترافیک مقیاس‌پذیر خواهید بود. چند حوزه کلیدی وجود دارد که باید در نظر بگیرید، صرف نظر از ارائه دهنده خدمات ابری انتخابی شما:

### مقیاس‌پذیری افقی

ممکن است بخواهید برنامه خود را به صورت افقی گسترش دهید تا درخواست‌هایی را که از منابع مختلف به برنامه شما می‌آیند پاسخ دهید. این می‌تواند شامل استقرار سرورها یا کانتینرهای اضافی برای توزیع بار باشد. اگر این نوع مقیاس‌پذیری را انتخاب می‌کنید، مطمئن شوید که معماری شما برای مدیریت چندین گره طراحی شده است و مکانیزم‌هایی برای متعادل کردن بار بین آنها دارید.

### مقیاس‌پذیری عمودی

گزینه دیگر، مقیاس‌پذیری عمودی برنامه شماست، یعنی می‌توانید منابع در دسترس یک گره را افزایش دهید. این شامل ارتقا قابلیت‌های سرور شما برای مدیریت بار اضافی خواهد بود. اگر این نوع مقیاس‌پذیری را انتخاب می‌کنید، مطمئن شوید که برنامه شما برای استفاده از این منابع اضافی طراحی شده است.

### کش کردن

با ذخیره‌سازی داده‌هایی که مکررا به آنها دسترسی می‌شود، می‌توانید زمان پاسخگویی را بدون نیاز به تماس‌های مکرر با API ما بهبود بخشید. برنامه شما باید طوری طراحی شود که در صورت امکان از داده‌های کش شده استفاده کند و در صورت اضافه شدن اطلاعات جدید، کش را نامعتبر کند. چند روش مختلف برای انجام این کار وجود دارد. به عنوان مثال، می‌توانید داده‌ها را در یک پایگاه داده، سیستم فایل یا کش حافظه ذخیره کنید، بسته به اینکه چه چیزی برای برنامه شما منطقی‌تر است.

### متعادل‌سازی بار

تکنیک‌های متعادل‌سازی بار را در نظر بگیرید تا اطمینان حاصل کنید که درخواست‌ها به طور یکنواخت بین سرورهای در دسترس شما توزیع می‌شوند. این می‌تواند شامل استفاده از یک متعادل‌کننده بار در مقابل سرورهای شما یا استفاده از DNS round-robin باشد. متعادل‌سازی بار به بهبود عملکرد و کاهش گلوگاه‌ها کمک می‌کند.

## بهبود تاخیرها

تاخیر، زمانی است که برای پردازش یک درخواست و بازگشت پاسخ صرف می‌شود. در این بخش، برخی از عواملی را که بر تاخیر مدل‌های تولید متن تاثیر می‌گذارند بررسی می‌کنیم و پیشنهاداتی برای کاهش آن ارائه می‌دهیم.

تاخیر یک درخواست تکمیل عمدتا تحت تاثیر دو عامل قرار دارد: مدل و تعداد توکن‌های تولید شده. چرخه عمر یک درخواست تکمیل به شکل زیر است:

1. **شبکه**: تاخیر از کاربر نهایی به API
2. **سرور**: زمان پردازش توکن‌های پرامپت
3. **سرور**: زمان نمونه‌برداری/تولید توکن‌ها
4. **شبکه**: تاخیر از API به کاربر نهایی

بخش عمده تاخیر معمولا از مرحله تولید توکن ناشی می‌شود.

> **شهود**: توکن‌های پرامپت تاخیر بسیار کمی به تماس‌های تکمیل اضافه می‌کنند. زمان تولید توکن‌های تکمیل بسیار طولانی‌تر است، زیرا توکن‌ها یکی یکی تولید می‌شوند. طول‌های تولید طولانی‌تر به دلیل تولید مورد نیاز برای هر توکن، تاخیر را انباشته می‌کنند.

### هفت اهرم کاهش تاخیر

از این اهرم‌های برگرفته از مستندات OpenAI به عنوان چک‌لیست عملیاتی برای workloadهای AvalAI استفاده کنید:

1. **پردازش سریع‌تر توکن‌ها:** وظایف ساده را پس از پاس کردن evalها به مدل‌های کوچک‌تر یا کم‌تاخیرتر route کنید.
2. **تولید توکن‌های کمتر:** بودجه پاسخ را صریح تعیین کنید و برای Responses از `max_output_tokens` و برای Chat Completions از `max_completion_tokens` استفاده کنید.
3. **استفاده از توکن‌های ورودی کمتر:** context مربوط به RAG را هرس کنید، HTML را پاک‌سازی کنید، تاریخچه تکراری را حذف کنید و پیشوند قابل reuse را cache-friendly نگه دارید.
4. **ارسال درخواست‌های کمتر:** وقتی مراحل به round trip جداگانه نیاز ندارند، آن‌ها را در یک structured response ترکیب کنید.
5. **موازی‌سازی:** classification، retrieval، moderation و enrichment مستقل را هم‌زمان اجرا کنید و همچنان محدودیت نرخ را رعایت کنید.
6. **کم کردن حس انتظار کاربر:** خروجی را stream کنید، chunkها را پردازش کنید و به جای spinner خالی، وضعیت ابزار یا workflow را نشان دهید.
7. **LLM را پیش‌فرض نکنید:** confirmationهای محدود را hard-code کنید، پاسخ‌های رایج را از قبل بسازید یا برای metricها و search resultها از UI اختصاصی استفاده کنید.

ابتدا کاهش توکن‌های خروجی را اولویت دهید. در بسیاری از workloadهای متنی، کوتاه‌تر کردن خروجی قابل مشاهده اثر latency بیشتری نسبت به حذف تعداد کمی از توکن‌های prompt دارد.

### عوامل رایج تاثیرگذار بر تاخیر

#### انتخاب مدل

API ما مدل‌های مختلفی با سطوح متفاوتی از پیچیدگی و عمومیت ارائه می‌دهد. قدرتمندترین مدل‌ها می‌توانند تکمیل‌های پیچیده‌تر و متنوع‌تری تولید کنند، اما پردازش پرس و جوی شما نیز زمان بیشتری می‌برد. مدل‌های کوچکتر می‌توانند چت تکمیلی سریع‌تر و ارزان‌تری تولید کنند، اما ممکن است نتایجی تولید کنند که برای پرس و جوی شما کمتر دقیق یا مرتبط باشند. می‌توانید مدلی را انتخاب کنید که بهترین تناسب را با مورد استفاده شما و تعادل بین سرعت، هزینه و کیفیت داشته باشد.

#### تعداد توکن‌های تکمیلی

درخواست تعداد زیادی از توکن‌های تکمیلی تولید شده می‌تواند منجر به افزایش تاخیر شود:

- **توکن‌های حداکثر کمتر**: برای درخواست‌هایی با تعداد تولید توکن مشابه، آنهایی که پارامتر `max_tokens` کمتری دارند، تاخیر کمتری دارند.
- **شامل توالی‌های توقف**: برای جلوگیری از تولید توکن‌های غیرضروری، یک توالی توقف اضافه کنید.
- **تولید تکمیل‌های کمتر**: در صورت امکان، مقادیر `n` و `best_of` را کاهش دهید.

برای integrationهای جدید Responses API، از `max_output_tokens` استفاده کنید؛ برای Chat Completions، در صورت پشتیبانی `max_completion_tokens` را ترجیح دهید. مثال‌های قدیمی `max_tokens` را الگوی سازگاری برای مدل‌ها یا SDKهای قدیمی‌تر بدانید.

> **هشدار برای مدل‌های reasoning:** این سقف‌ها می‌توانند علاوه بر پاسخ قابل مشاهده، شامل توکن‌های reasoning پنهان نیز باشند و سهم تضمین‌شده‌ای برای متن نهایی نیستند. اگر reasoning تمام بودجه را مصرف کند، Responses ممکن است `status: "incomplete"`، مقدار `incomplete_details.reason: "max_output_tokens"` و خروجی متنی خالی برگرداند. در Chat Completions نیز ممکن است `finish_reason: "length"` دریافت کنید. مقدار `usage.output_tokens_details.reasoning_tokens` را بررسی کنید؛ سپس سقف را افزایش دهید، در صورت پشتیبانی `reasoning.effort` را روی `low` یا `none` بگذارید، task را ساده یا تقسیم کنید و برای پاسخ نهایی حاشیه امن نگه دارید. بخش [استدلال: تخصیص فضا برای استدلال](fa/guides/reasoning.md#تخصیص-فضا-برای-استدلال) را ببینید.

#### جریان‌سازی

تنظیم `stream: true` در یک درخواست باعث می‌شود مدل به محض در دسترس بودن توکن‌ها شروع به بازگرداندن آنها کند، به جای اینکه منتظر تولید کامل توالی توکن‌ها باشد. این زمان دریافت همه توکن‌ها را تغییر نمی‌دهد، اما زمان اولین توکن را برای برنامه‌ای که می‌خواهیم پیشرفت جزئی را نشان دهیم یا می‌خواهیم تولیدات را متوقف کنیم، کاهش می‌دهد. این می‌تواند تجربه کاربری بهتری باشد و بهبود UX محسوب می‌شود، بنابراین ارزش آزمایش با جریان‌سازی را دارد.

### پاسخ‌های جریانی (Streaming)

برای تجربه کاربری بهتر، از پاسخ‌های جریانی استفاده کنید:

```language-selector
python=:import os
import sys
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": "داستانی درباره یک کاوشگر فضایی بنویس"}],
    stream=True,
)

for chunk in response:
    if chunk.choices[0].delta.content:
        sys.stdout.write(chunk.choices[0].delta.content)
        sys.stdout.flush()

javascript=:const { OpenAI } = require("openai");

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function streamResponse() {
  const stream = await client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [
      { role: "user", content: "داستانی درباره یک کاوشگر فضایی بنویس" },
    ],
    stream: true,
  });

  for await (const chunk of stream) {
    if (chunk.choices[0]?.delta?.content) {
      process.stdout.write(chunk.choices[0].delta.content);
    }
  }
}

streamResponse();

go=:package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(
		os.Getenv("AVALAI_API_KEY"),
		openai.WithBaseURL("https://api.avalai.ir/v1"),
	)

	req := openai.ChatCompletionRequest{
		model: "gpt-5.6-luna",
		Messages: []openai.ChatCompletionMessage{
			{
				Role:    "user",
				Content: "داستانی درباره یک کاوشگر فضایی بنویس",
			},
		},
		Stream: true,
	}

	stream, err := client.CreateChatCompletionStream(context.Background(), req)
	if err != nil {
		fmt.Printf("Stream error: %v\n", err)
		os.Exit(1)
	}
	defer stream.Close()

	for {
		response, err := stream.Recv()
		if err != nil {
			break
		}
		if len(response.Choices) > 0 && response.Choices[0].Delta.Content != "" {
			fmt.Print(response.Choices[0].Delta.Content)
		}
	}
}

php=:<?php
require 'vendor/autoload.php';

$client = OpenAI::client(getenv('AVALAI_API_KEY'), [
 'base_url' => 'https://api.avalai.ir/v1',
]);

$stream = $client->chat()->createStreamed([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => 'داستانی درباره یک کاوشگر فضایی بنویس'],
 ],
]);

foreach ($stream as $response) {
 if ($response->choices[0]->delta->content) {
 echo $response->choices[0]->delta->content;
 ob_flush();
 flush();
 }
}
?>

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="داستانی درباره یک کاوشگر فضایی بنویس",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "داستانی درباره یک کاوشگر فضایی بنویس",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "داستانی درباره یک کاوشگر فضایی بنویس",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پردازش ناهمزمان

برای وظایف طولانی‌مدت، پردازش ناهمزمان را پیاده‌سازی کنید:

```language-selector
python=:import asyncio
import os
from openai import AsyncOpenAI

client = AsyncOpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


async def generate_response(prompt):
    response = await client.chat.completions.create(
        model="gpt-5.6-luna", messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content


async def process_batch(prompts):
    tasks = [generate_response(prompt) for prompt in prompts]
    return await asyncio.gather(*tasks)


# استفاده
results = asyncio.run(process_batch(["سلام", "حالت چطوره؟", "هوا چطوره؟"]))

javascript=:const { OpenAI } = require("openai");

const client = new OpenAI({
  apiKey: "AVALAI_API_KEY",
  baseURL: "https://api.avalai.ir/v1",
});

async function generateResponse(prompt) {
  const response = await client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: prompt }],
  });
  return response.choices[0].message.content;
}

async function processBatch(prompts) {
  const promises = prompts.map((prompt) => generateResponse(prompt));
  return await Promise.all(promises);
}

// استفاده
processBatch(["سلام", "حالت چطوره؟", "هوا چطوره؟"])
  .then((results) => console.log(results))
  .catch((error) => console.error(error));

go=:package main

import (
	"context"
	"fmt"
	"sync"

	"github.com/openai/openai-go"
)

func generateResponse(client *openai.Client, prompt string, wg *sync.WaitGroup, results map[int]string, index int) {
	defer wg.Done()

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    "user",
					Content: prompt,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	results[index] = resp.Choices[0].Message.Content
}

func main() {
	client := openai.NewClient(
		"AVALAI_API_KEY",
		openai.WithBaseURL("https://api.avalai.ir/v1"),
	)

	prompts := []string{"سلام", "حالت چطوره؟", "هوا چطوره؟"}
	results := make(map[int]string)

	var wg sync.WaitGroup
	for i, prompt := range prompts {
		wg.Add(1)
		go generateResponse(client, prompt, &wg, results, i)
	}

	wg.Wait()

	for i := 0; i < len(prompts); i++ {
		fmt.Printf("نتیجه %d: %s\n", i, results[i])
	}
}

php=:<?php
require 'vendor/autoload.php';

$client = OpenAI::client('AVALAI_API_KEY', [
 'base_url' => 'https://api.avalai.ir/v1',
]);

function generateResponse($client, $prompt) {
 $response = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => $prompt],
 ],
 ]);

 return $response->choices[0]->message->content;
}

$prompts = ["سلام", "حالت چطوره؟", "هوا چطوره؟"];
$results = [];

// استفاده از درخواست‌های موازی با وعده‌ها
$promises = [];
foreach ($prompts as $index => $prompt) {
 $promises[$index] = new Promise(function($resolve, $reject) use ($client, $prompt) {
 try {
 $result = generateResponse($client, $prompt);
 $resolve($result);
 } catch (Exception $e) {
 $reject($e);
 }
 });
}

$results = Promise\all($promises)->wait();
print_r($results);
?>

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "Write a one-sentence summary of AvalAI.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Write a one-sentence summary of AvalAI.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## بهینه‌سازی هزینه

برای نظارت بر هزینه‌های خود، می‌توانید یک آستانه اطلاع‌رسانی در حساب خود تنظیم کنید تا پس از عبور از یک آستانه استفاده مشخص، هشدار ایمیلی دریافت کنید. همچنین می‌توانید یک بودجه ماهانه تعیین کنید. لطفا به پتانسیل ایجاد اختلال در برنامه/کاربران خود توسط بودجه ماهانه توجه داشته باشید. از داشبورد پیگیری استفاده برای نظارت بر استفاده از توکن خود در طول چرخه‌های صورتحساب فعلی و گذشته استفاده کنید.

### استفاده از User API برای ردیابی هزینه

برای بارهای کاری عملیاتی، [User API](fa/api-reference/user.md) دسترسی برنامه‌ریزی شده برای ردیابی استفاده و هزینه‌ها فراهم می‌کند:

- **جستجوی تراکنش**: از نقطه پایانی `/user/v1/transactions/lookup` با `avalai-request-id` از هدرهای پاسخ برای دریافت جزئیات دقیق هزینه هر تماس API استفاده کنید
- **نظارت بر موجودی**: موجودی فعلی خود را به صورت برنامه‌ریزی شده جستجو کنید تا هشدارهای بودجه را پیاده‌سازی کنید
- **تحلیل استفاده**: الگوهای استفاده را در طول زمان ردیابی کنید تا هزینه‌ها را بهینه کرده و ظرفیت را برنامه‌ریزی کنید

```python
import requests
import time

# مرحله 1: تماس API و گرفتن avalai-request-id
response = requests.post(
    "https://api.avalai.ir/v1/chat/completions",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"model": "gpt-5.6-luna", "messages": [{"role": "user", "content": "سلام!"}]},
)
request_id = response.headers.get("avalai-request-id")

# مرحله 2: انتظار برای پردازش (معمولا در عرض چند ثانیه در دسترس است)
time.sleep(5)

# مرحله 3: دریافت هزینه دقیق با استفاده از User API
cost_response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={"Authorization": f"Bearer {api_key}"},
    json={"transaction_ids": [request_id]},
)
cost_data = cost_response.json()
print(f"هزینه درخواست: {cost_data}")
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="سلام!",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای فروشندگان و کاربران سازمانی، [راهنمای ردیابی هزینه فروشندگان](fa/resellers/cost-tracking-guide.md) را برای الگوهای استفاده پیشرفته مشاهده کنید.

### استفاده از توکن

یکی از چالش‌های انتقال نمونه اولیه خود به تولید، بودجه‌بندی هزینه‌های مرتبط با اجرای برنامه شماست. AvalAI یک مدل قیمت‌گذاری پرداخت به ازای استفاده ارائه می‌دهد، با قیمت‌هایی به ازای هر 1,000 توکن (تقریبا معادل 750 کلمه). برای تخمین هزینه‌های خود، باید استفاده از توکن را پیش‌بینی کنید. عواملی مانند سطوح ترافیک، تناوب تعامل کاربران با برنامه شما و میزان داده‌هایی که پردازش خواهید کرد را در نظر بگیرید.

> **بودجه را فقط بر اساس متن قابل مشاهده تعیین نکنید.** در همه ارائه‌دهندگان و مدل‌ها، توکن‌های پنهان `reasoning_tokens` با نرخ توکن خروجی مدل انتخابی محاسبه می‌شوند. وقتی `usage.output_tokens` از قبل آنها را شامل می‌شود، `usage.output_tokens_details.reasoning_tokens` فقط تفکیک این مقدار است: هزینه خروجی را به صورت `output_tokens * output_price` محاسبه کنید، نه `(output_tokens + reasoning_tokens) * output_price`. اگر route خروجی قابل مشاهده و reasoning را جدا گزارش می‌کند، هزینه هر دو مقدار را با همان نرخ توکن خروجی محاسبه کنید.

**یک چارچوب مفید برای تفکر درباره کاهش هزینه‌ها، در نظر گرفتن هزینه‌ها به عنوان تابعی از تعداد توکن‌ها و هزینه هر توکن است.** با استفاده از این چارچوب، دو مسیر بالقوه برای کاهش هزینه‌ها وجود دارد:

- **کاهش هزینه هر توکن**: برای برخی وظایف از مدل‌های کوچکتر استفاده کنید تا هزینه‌ها را کاهش دهید.
- **کاهش تعداد توکن‌های مورد نیاز**: از پرامپت‌های کوتاه‌تر استفاده کنید، مدل‌ها را فاین‌تیون کنید یا پرس‌وجوهای رایج کاربران را کش کنید تا نیازی به پردازش مجدد آنها نباشد.

برای اندازه‌گیری هزینه واقعی، به جای تخمین کاراکتری، از `usage` پاسخ، [User API](fa/api-reference/user.md) و [Models API](fa/api-reference/models.md) استفاده کنید. برای تخمین پیش از ارسال با متن، تصویر، فایل و ابزارها، [راهنمای شمارش توکن](fa/guides/token-counting.md) را دنبال کنید؛ قبل از ساخت کنترل‌های production روی `POST /v1/responses/input_tokens` بررسی کنید این route برای مسیر AvalAI شما فعال است.

- **نظارت بر استفاده از توکن**: استفاده از توکن خود را پیگیری کنید تا از هزینه‌های غیرمنتظره جلوگیری کنید.
- **بهینه‌سازی طول پرامپت**: پرامپت‌ها را مختصر نگه دارید و در عین حال زمینه لازم را فراهم کنید.
- **در صورت امکان از مدل‌های کوچکتر استفاده کنید**: برای وظایف ساده‌تر، مدل‌های کوچکتر می‌توانند مقرون به صرفه‌تر باشند.
- **درخواست‌ها را دسته‌بندی کنید**: هنگام پردازش چندین ورودی، آن‌ها را در یک درخواست واحد دسته‌بندی کنید.
- **پیشوندهای ثابت را کش کنید**: هر جا پشتیبانی می‌شود از prompt caching استفاده کنید و سپس `cached_tokens` و قیمت‌گذاری ورودی کش‌شده را در گزارش‌های usage/cost دنبال کنید.
- **حالت‌های async را آگاهانه انتخاب کنید**: batch یا پردازش کم‌اولویت را فقط برای workloadهایی به کار ببرید که نتیجه دیرتر یا ظرفیت مقطعی را تحمل می‌کنند.

## استراتژی MLOps

با انتقال نمونه اولیه خود به تولید، ممکن است بخواهید یک استراتژی MLOps توسعه دهید. MLOps (عملیات یادگیری ماشین) به فرآیند مدیریت چرخه عمر کامل مدل‌های یادگیری ماشین شما اشاره دارد، از جمله هر مدلی که ممکن است با استفاده از API ما فاین‌تیون کنید. هنگام طراحی استراتژی MLOps خود، چندین حوزه وجود دارد که باید در نظر بگیرید:

### مدیریت داده و مدل

مدیریت داده‌های مورد استفاده برای آموزش یا فاین‌تیون مدل شما و ردیابی نسخه‌ها و تغییرات. این شامل:

- نسخه‌بندی مجموعه داده‌های خود
- ردیابی تبدیل‌های داده
- حفظ بررسی‌های کیفیت داده
- مستندسازی منابع داده و مراحل پیش‌پردازش

### نظارت بر مدل

ردیابی عملکرد مدل شما در طول زمان و تشخیص هرگونه مشکل یا تخریب احتمالی:

- راه‌اندازی نظارت بر دقت و عملکرد مدل
- ایجاد هشدارها برای تخریب عملکرد
- ردیابی الگوهای استفاده از مدل
- نظارت بر انحراف مفهوم یا انحراف داده

### نظارت بر وضعیت سرویس

وضعیت دسترسی سرویس AvalAI را نظارت کنید و در به‌روزرسانی‌های وضعیت عضو شوید:

- **صفحه وضعیت**: برای بررسی وضعیت فعلی سرویس از [status.avalai.ir](https://status.avalai.ir) بازدید کنید
- **اشتراک در به‌روزرسانی‌ها**: در صفحه وضعیت عضو شوید تا اعلانات مربوط به تعمیر و نگهداری برنامه‌ریزی شده، حوادث و به‌روزرسانی‌های سرویس دریافت کنید
- **یکپارچه‌سازی بررسی‌های سلامت**: پیاده‌سازی بررسی‌های سلامت در برنامه خود را در نظر بگیرید که دسترسی API را قبل از عملیات حیاتی تایید می‌کند

### بازآموزی مدل

اطمینان از به‌روز بودن مدل شما با تغییرات داده یا نیازهای در حال تکامل:

- ایجاد معیارهایی برای زمان بازآموزی مدل‌ها
- خودکارسازی فرآیند بازآموزی در صورت امکان
- اعتبارسنجی مدل‌های بازآموزی شده قبل از استقرار
- حفظ تاریخچه نسخه‌های مدل

### استقرار مدل

خودکارسازی فرآیند استقرار مدل شما و مصنوعات مرتبط در محیط عملیاتی:

- پیاده‌سازی خطوط لوله CI/CD برای استقرار مدل
- ایجاد رویه‌های بازگشت برای استقرارهای ناموفق
- آزمایش مدل‌ها در محیط‌های مرحله‌بندی قبل از محیط عملیاتی
- مستندسازی پیکربندی‌های استقرار

تفکر در مورد این جنبه‌های برنامه شما به اطمینان از مرتبط ماندن و عملکرد خوب مدل شما در طول زمان کمک می‌کند.

## امنیت و انطباق

با انتقال نمونه اولیه خود به تولید، باید الزامات امنیتی و انطباقی را که ممکن است برای برنامه شما اعمال شود، ارزیابی و برطرف کنید. این شامل بررسی داده‌هایی است که مدیریت می‌کنید، درک نحوه پردازش داده‌ها توسط API ما و تعیین مقرراتی است که باید رعایت کنید.

### فیلتر کردن محتوا

- **پیاده‌سازی فیلتر کردن محتوا**: از نقاط پایانی تعدیل برای فیلتر کردن محتوای نامناسب استفاده کنید.
- **تنظیم سیاست‌های استفاده مناسب**: سیاست‌های استفاده واضحی را برای برنامه خود تعریف کنید.

### حریم خصوصی داده‌های کاربر

- **به حداقل رساندن اشتراک‌گذاری داده‌ها**: فقط داده‌های ضروری کاربر را با API به اشتراک بگذارید.
- **اطلاع‌رسانی به کاربران**: در مورد نحوه استفاده از داده‌های کاربر با مدل‌های هوش مصنوعی شفاف باشید.
- **پیاده‌سازی سیاست‌های نگهداری داده‌ها**: سیاست‌های واضحی برای مدت زمان ذخیره داده‌های کاربر تعریف کنید.

### ردیابی سوءاستفاده با Safety Identifier

برای محصولاتی که کاربران نهایی جداگانه با مدل تعامل دارند، در routeهای پشتیبانی‌شده یک `safety_identifier` پایدار و حفظ‌کننده حریم خصوصی بفرستید. این مقدار به تیم شما کمک می‌کند الگوی سوءاستفاده را به یک کاربر نهایی نسبت دهد، بدون اینکه داده شخصی خام داخل درخواست قرار بگیرد.

- **ابتدا هویت کاربر را hash کنید:** مقدار را از شناسه داخلی کاربر، username یا email با hash یک‌طرفه بسازید؛ برای previewهای ناشناس از session ID مبهم استفاده کنید.
- **cache key را دوباره استفاده نکنید:** `safety_identifier` را از `prompt_cache_key` جدا نگه دارید، چون اولی برای ردیابی سوءاستفاده است و دومی برای bucket کردن workload یا cache.
- **در هر سطح جداگانه بفرستید:** safety identifier به‌صورت خودکار بین APIها یا sessionها منتقل نمی‌شود؛ پس وقتی route انتخابی AvalAI پشتیبانی می‌کند، همان مقدار پایدار را در هر درخواست مرتبط Responses، Chat Completions، Messages یا session realtime بفرستید.
- **metadata را امن log کنید:** شناسه hash‌شده را همراه `avalai-request-id`، مدل، route و نتیجه moderation ثبت کنید، اما prompt کامل را فقط وقتی نگه دارید که policy نگه‌داری شما صریحا اجازه می‌دهد.

برای مثال‌هایی که `safety_identifier` را همراه `store: false` استفاده می‌کنند، [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md) و [کنترل داده‌ها](fa/guides/data-controls.md) را ببینید.

### مدیریت خطا

- **خطاها را به خوبی مدیریت کنید**: مدیریت خطای مناسب را برای کدهای وضعیت HTTP مختلف پیاده‌سازی کنید.
- **خطاهای API را ثبت کنید**: گزارش‌هایی از خطاهای API برای اهداف اشکال‌زدایی و نظارت نگه دارید.
- **پیام‌های خطای کاربرپسند ارائه دهید**: خطاهای API را به پیام‌های معنی‌دار برای کاربران نهایی ترجمه کنید.

برخی از حوزه‌های رایجی که باید در نظر بگیرید شامل ذخیره‌سازی داده‌ها، انتقال داده‌ها و نگهداری داده‌ها است. همچنین ممکن است لازم باشد از حفاظت‌های حریم خصوصی داده‌ها مانند رمزگذاری یا ناشناس‌سازی در صورت امکان استفاده کنید. علاوه بر این، باید از بهترین شیوه‌ها برای کدنویسی ایمن مانند پاکسازی ورودی و مدیریت صحیح خطا پیروی کنید.

## ملاحظات تجاری

با انتقال پروژه‌های هوش مصنوعی از نمونه اولیه به مرحله استقرار، مهم است که در نظر بگیرید چگونه یک محصول عالی با هوش مصنوعی بسازید و چگونه این به کسب و کار اصلی شما مرتبط می‌شود. در اینجا برخی از ملاحظات کلیدی تجاری آورده شده است:

- **تعریف معیارهای موفقیت واضح**: KPI ها را برای اندازه‌گیری تاثیر پیاده‌سازی هوش مصنوعی خود ایجاد کنید
- **همسویی با اهداف تجاری**: اطمینان حاصل کنید که پروژه هوش مصنوعی شما مستقیما از استراتژی کلی کسب و کار شما پشتیبانی می‌کند
- **در نظر گرفتن پذیرش کاربر**: برای آموزش کاربر و مدیریت تغییر برنامه‌ریزی کنید
- **ایجاد حلقه‌های بازخورد**: مکانیزم‌هایی برای جمع‌آوری بازخورد کاربر و بهبود برنامه خود ایجاد کنید
- **برنامه‌ریزی برای مقیاس‌پذیری**: در نظر بگیرید که مدل کسب و کار شما چگونه با افزایش استفاده مقیاس‌پذیر خواهد بود

## منابع مرتبط

- [چک‌لیست استقرار API](fa/guides/deployment-checklist.md)
- [کنترل داده‌ها](fa/guides/data-controls.md)
- [احراز هویت API](fa/api-reference/authentication.md)
- [User API](fa/api-reference/user.md)
- [محدودیت‌های نرخ](fa/rate-limits.md)
- [هدرهای پاسخ](fa/api-reference/response-headers.md)
- [منسوخ شدن‌ها](fa/deprecations.md)
- [مدیریت خطا](fa/guides/error-handling.md)
- [پاسخ‌های جریانی](fa/guides/streaming-responses.md)
- [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md)
- [ارزیابی با Promptfoo و AvalAI](fa/examples/promptfoo_evals_with_avalai.md)
- [Agentic Guardrails با Schema Workflow](fa/examples/agentic_guardrails_schema_workflow.md)
- [درخواست‌های موازی امن برای محدودیت نرخ](fa/examples/rate_limit_safe_parallel_requests.md)
- [فاین‌تیونینگ](fa/guides/fine-tuning.md)
- [وضعیت سرویس](https://status.avalai.ir)
