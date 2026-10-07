# مدل‌های Z.AI

AvalAI دسترسی به خانواده مدل‌های GLM (General Language Model) از Z.AI را فراهم می‌کند که به خاطر عملکرد استثنایی کدنویسی، پردازش زمینه طولانی و قابلیت‌های جامع در حوزه‌های مختلف شناخته شده‌اند.

## GLM-5.3-Flash

پرچم‌دار چندوجهی و کارآمد Z.AI، توانمندی کدنویسی و عامل‌ها را با معماری ترکیب خبرگان ۳۲۰ میلیارد پارامتری ارائه می‌کند که برای هر توکن ۱۸ میلیارد پارامتر را فعال می‌سازد. طراحی ۴۵ لایه آن از توجه تنک و خطی ترکیبی بهره می‌برد تا هزینه استنتاج نسبت به مدل کامل GLM-5.3 کاهش یابد.

### glm-5.3-flash

GLM-5.3-Flash برای کدنویسی، درک چندوجهی، استفاده از ابزار و گردش‌کارهای عاملی طولانی طراحی شده است و هم‌زمان تأخیر و هزینه را در سطحی عملی نگه می‌دارد.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5.3-flash` |
| معماری | 320B پارامتر کل، 18B پارامتر فعال، ۴۵ لایه |
| پنجره زمینه | 991,000 توکن ورودی |
| حداکثر خروجی | 128,000 توکن |
| قابلیت‌ها | چت، درک چندوجهی، فراخوانی تابع، کش پرامپت، استدلال، انتخاب ابزار |
| قیمت تشویقی ورودی | $0.075 / ۱ میلیون توکن تا ۱۸ شهریور ۱۴۰۵ (September 9, 2026) |
| قیمت تشویقی ورودی کش‌شده | $0.015 / ۱ میلیون توکن تا ۱۸ شهریور ۱۴۰۵ (September 9, 2026) |
| قیمت تشویقی خروجی | $0.25 / ۱ میلیون توکن تا ۱۸ شهریور ۱۴۰۵ (September 9, 2026) |
| مناسب برای | کدنویسی عاملی، کار در مقیاس مخزن، اسناد تصویری، خودکارسازی ابزارمحور |
| در دسترس در | `v1/chat/completions`، `v1/messages`، `v1/responses` (پشتیبانی جزئی) |

**ویژگی‌های کلیدی:**
- **چندوجهی بومی**: نخستین مدل چندوجهی بومی در سری GLM-5 که با پیکره چندوجهی ۳۰ تریلیون توکنی آموزش دیده است
- **معماری کارآمد ترکیب خبرگان**: برای هر توکن 18B پارامتر از مجموع 320B پارامتر را در ۴۵ لایه فعال می‌کند
- **توجه کارآمد**: بنا بر گزارش Z.AI، در مقایسه با GLM-5.3 به ۳٫۰ برابر محاسبه کمتر برای توجه و KV cache با اندازه ۴٫۴ برابر کوچک‌تر نیاز دارد
- **زمینه طولانی**: حداکثر 991,000 توکن ورودی و 128,000 توکن خروجی را می‌پذیرد
- **وزن‌های باز**: استقرار مستقل با اکوسیستم‌هایی مانند SGLang، vLLM و TokenSpeed را پشتیبانی می‌کند

**نکات برجسته عملکرد به گزارش Z.AI:**

- Terminal Bench 2.1: امتیاز 84.3 در برابر 81.0 برای GLM-5.2
- DeepSWE v1.1: امتیاز 63.4 در برابر 46.2
- Toolathlon Verified: امتیاز 78.4 در برابر 59.9
- AutomationBench v1.0.6: امتیاز 48.8 در برابر 26.2

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.3-flash",
    "messages": [{"role": "user", "content": "این برنامه پیاده‌سازی را بررسی کن و خطرهای اصلی آن را مشخص کن."}]
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")
response = client.chat.completions.create(
    model="glm-5.3-flash",
    messages=[
        {
            "role": "user",
            "content": "این برنامه پیاده‌سازی را بررسی کن و خطرهای اصلی آن را مشخص کن.",
        }
    ],
)
print(response.choices[0].message.content)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});
const response = await client.chat.completions.create({
  model: "glm-5.3-flash",
  messages: [
    { role: "user", content: "این برنامه پیاده‌سازی را بررسی کن و خطرهای اصلی آن را مشخص کن." },
  ],
});
console.log(response.choices[0].message.content);

```


---

## GLM-5.3

جدیدترین مدل پرچم‌دار Z.AI برای کدنویسی پیچیده، وظایف عاملی بلندمدت و تحلیل امنیتی مجاز است. GLM-5.3 از همان مدل پایه GLM-5.2 استفاده می‌کند و بهبودهای آن حاصل آموزش تکمیلی گسترده‌تر روی محیط‌های بیشتر، وظایف متنوع‌تر و مسیرهای اجرایی طولانی‌تر است.

### glm-5.3

توانمندترین مدل کدنویسی Z.AI که برای انجام کارهای مهندسی گسترده از برنامه‌ریزی و پیاده‌سازی تا آزمایش و راستی‌آزمایی طراحی شده است. تفکر همیشه فعال است و توسعه‌دهندگان می‌توانند سطح استدلال `low`، `high` یا `max` را انتخاب کنند.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5.3` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی ساختاریافته، استدلال، تفکر اجباری |
| قیمت ورودی | ۱.۴۰ دلار / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | ۰.۲۶ دلار / ۱ میلیون توکن |
| قیمت خروجی | ۴.۴۰ دلار / ۱ میلیون توکن |
| نقاط قوت | کدنویسی پیشرو، عامل‌های بلندمدت، تحلیل آسیب‌پذیری، استفاده از ابزار |
| مناسب برای | کدنویسی عاملی، مهندسی در مقیاس مخزن، خودکارسازی بلندمدت، پژوهش امنیتی مجاز |
| در دسترس در | `v1/chat/completions`، `v1/messages`، `v1/responses` (پشتیبانی جزئی) |

**ویژگی‌های کلیدی:**
- **کدنویسی قوی‌تر**: Z.AI بهبود ۵۰٪ نسبت به GLM-5.2 را در معیار داخلی Z.ai Code Bench گزارش می‌کند
- **مهندسی بلندمدت**: گردش‌کارهای گسترده شامل برنامه‌ریزی، پیاده‌سازی، آزمایش، ارزیابی و راستی‌آزمایی را انجام می‌دهد
- **تحلیل امنیت سایبری**: کشف بهتر آسیب‌پذیری و استدلال درباره زنجیره بهره‌برداری برای محیط‌های مجاز
- **تفکر اجباری**: مقدار `thinking.type` باید `enabled` باشد و غیرفعال‌کردن تفکر پشتیبانی نمی‌شود
- **سطح استدلال**: مقدارهای `low`، `high` و `max` را می‌پذیرد؛ مقدار پیش‌فرض `max` است و برای کدنویسی پیشنهاد می‌شود
- **زمینه بزرگ**: حداکثر ۱M توکن ورودی و ۱۲۸K توکن خروجی

**نکات برجسته عملکرد به گزارش Z.AI:**

- Terminal-Bench 3.0: امتیاز 28.3 در برابر 4.6 برای GLM-5.2
- DeepSWE v1.1: امتیاز 66.9 در برابر 46.2
- Agents' Last Exam: امتیاز 28.5 در برابر 23.8
- CyberGym: امتیاز 84.5 در برابر 77.2
- ExploitBench: امتیاز 54.4 در برابر 24.4

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.3",
    "messages": [
      {
        "role": "user",
        "content": "برای بازآرایی مرحله‌ای این مخزن برنامه‌ریزی کن و مراحل راستی‌آزمایی و بازگشت را نیز بنویس."
      }
    ],
    "thinking": {"type": "enabled"},
    "reasoning_effort": "max"
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5.3",
    messages=[
        {
            "role": "user",
            "content": "برای بازآرایی مرحله‌ای این مخزن برنامه‌ریزی کن و مراحل راستی‌آزمایی و بازگشت را نیز بنویس.",
        }
    ],
    extra_body={
        "thinking": {"type": "enabled"},
        "reasoning_effort": "max",
    },
)

print(response.choices[0].message.content)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "glm-5.3",
  messages: [
    {
      role: "user",
      content: "برای بازآرایی مرحله‌ای این مخزن برنامه‌ریزی کن و مراحل راستی‌آزمایی و بازگشت را نیز بنویس.",
    },
  ],
  thinking: { type: "enabled" },
  reasoning_effort: "max",
});

console.log(response.choices[0].message.content);

```


> **الزام مهاجرت:** درخواست‌هایی که `thinking.type: "disabled"` می‌فرستند با GLM-5.3 با خطا روبه‌رو می‌شوند. مقدار را به `enabled` تغییر دهید و اگر سبک‌ترین سطح استدلال را می‌خواهید، `reasoning_effort: "low"` را به کار ببرید.

---

## GLM-5.2

جدیدترین مدل پرچمدار Z.AI برای مهندسی عاملی که GLM-5.1 را با پنجره زمینه گسترش‌یافته ۱ میلیون توکنی و قابلیت اطمینان بهبودیافته در افق بلند توسعه می‌دهد. GLM-5.2 بر پایه‌های قدرتمند کدنویسی و عاملی سری GLM-5 ساخته شده و در عین حال مدیریت زمینه را برای بارهای کاری سطح ریپو و سنگین از نظر اسناد مقیاس‌پذیر می‌کند.

### glm-5.2

توانمندترین مدل GLM از Z.AI که برای مهندسی نرم‌افزار پیچیده، استدلال با زمینه طولانی و گردش‌کارهای عاملی پایدار طراحی شده است. GLM-5.2 عملکرد کدنویسی پیشرو را با پنجره زمینه بزرگ مناسب برای کدبیس‌های چند فایلی و جلسات عاملی طولانی ترکیب می‌کند.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5.2` |
| پنجره زمینه | ۱٬۰۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، تفکر عمیق |
| قیمت ورودی | ۱.۴۰ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۲۶ دلار / ۱ میلیون توکن (۸۱٪ کاهش هزینه) |
| قیمت خروجی | ۴.۴۰ دلار / ۱ میلیون توکن |
| نقاط قوت | کدنویسی پیشرو، زمینه ۱ میلیون توکنی، مهندسی عاملی افق بلند |
| بهترین استفاده | کدنویسی عاملی، وظایف سطح ریپو، استدلال با زمینه طولانی، مهندسی نرم‌افزار پیچیده |
| در دسترس در | `v1/chat/completions`، `v1/responses` (پشتیبانی جزئی) |

**ویژگی‌های کلیدی:**
- **پنجره زمینه ۱ میلیون توکنی**: مدیریت کدبیس‌های سطح ریپو و بارهای کاری سنگین از نظر اسناد در یک درخواست
- **عملکرد کدنویسی پیشرو**: نتایج پیشرفته در معیارهای مهندسی نرم‌افزار و عاملی
- **بهینه‌سازی افق بلند**: حفظ بهینه‌سازی مولد در جلسات چندمرحله‌ای طولانی
- **بازبینی خود**: بازنگری استدلال و تجدیدنظر در استراتژی از طریق تکرار مکرر
- **قابلیت‌های پیشرفته**: حالت تفکر، جریان‌سازی، فراخوانی تابع، کش زمینه، خروجی ساختاریافته، پشتیبانی MCP

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5.2",
    messages=[
        {
            "role": "user",
            "content": "این کدبیس چند فایلی بزرگ را برای افزودن یک لایه کش بازنویسی کن و برنامه مهاجرت را توضیح بده.",
        }
    ],
    max_tokens=8192,
    temperature=0.6,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5.2` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این کدبیس چند فایلی بزرگ را برای افزودن یک لایه کش بازنویسی کن و برنامه مهاجرت را توضیح بده.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-5.1

مدل پرچمدار نسل جدید Z.AI برای مهندسی عاملی، با قابلیت‌های کدنویسی به طور قابل توجهی قوی‌تر از نسخه قبلی. GLM-5.1 عملکرد پیشرو را در SWE-Bench Pro (۵۸.۴٪) به دست می‌آورد و با فاصله زیادی از GLM-5 در NL2Repo و Terminal-Bench 2.0 پیشتاز است.

### glm-5.1

پیشرفته‌ترین مدل Z.AI که عملکرد SOTA را در وظایف مهندسی نرم‌افزار پیچیده به دست می‌آورد و از همه مدل‌ها از جمله GPT-5.4 و Claude Opus 4.6 در SWE-Bench Pro پیشی می‌گیرد.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5.1` |
| پنجره زمینه | ۲۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸٬۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، تفکر عمیق |
| قیمت ورودی | ۱.۵۴ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۲۸۶ دلار / ۱ میلیون توکن (۸۱٪ کاهش هزینه) |
| قیمت خروجی | ۴.۸۴ دلار / ۱ میلیون توکن |
| نقاط قوت | SOTA در SWE-Bench Pro (۵۸.۴٪)، بهینه‌سازی افق بلند، مهندسی عاملی |
| بهترین استفاده | کدنویسی عاملی، مهندسی نرم‌افزار پیچیده، وظایف سطح ریپو |
| در دسترس در | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **پیشرو در SWE-Bench Pro**: عملکرد ۵۸.۴٪، پیشتاز از همه مدل‌ها از جمله GPT-5.4 و Claude Opus 4.6
- **بهینه‌سازی افق بلند**: حفظ بهینه‌سازی مولد در بیش از ۶۰۰ تکرار با بیش از ۶۰۰۰ فراخوانی ابزار
- **بازبینی خود**: بازنگری استدلال و تجدیدنظر در استراتژی از طریق تکرار مکرر
- **حل مسائل پیچیده**: تجزیه مسائل پیچیده، اجرای آزمایش‌ها، خواندن نتایج و شناسایی موانع با دقت
- **قابلیت‌های پیشرفته**: حالت تفکر، جریان‌سازی، فراخوانی تابع، کش زمینه، خروجی ساختاریافته، پشتیبانی MCP

**عملکرد معیار:**
- SWE-Bench Pro: ۵۸.۴٪ (SOTA)
- NL2Repo: ۴۲.۷٪
- Terminal-Bench 2.0: ۶۳.۵٪
- AIME 2026: ۹۵.۳٪
- GPQA-Diamond: ۸۶.۲٪
- HLE (با ابزار): ۵۲.۳٪

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5.1",
    messages=[
        {
            "role": "user",
            "content": "یک پایگاه داده وکتور با خوشه‌بندی IVF و امتیازدهی u8 برای جستجوی نزدیک‌ترین همسایه پیاده‌سازی کن.",
        }
    ],
    max_tokens=8192,
    temperature=0.6,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5.1` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک پایگاه داده وکتور با خوشه‌بندی IVF و امتیازدهی u8 برای جستجوی نزدیک‌ترین همسایه پیاده‌سازی کن.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-5v-Turbo

مدل بینایی چندحالتی Z.AI که برای وظایف درک بصری با توان بالا بهینه‌سازی شده است.

### glm-5v-turbo

مدل بینایی-زبان Z.AI برای پردازش و تحلیل تصاویر با دقت بالا، با پشتیبانی از چندین تصویر در یک درخواست.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5v-turbo` |
| پنجره زمینه | ۲۰۰٬۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸٬۰۰۰ توکن |
| قابلیت‌ها | چت، بینایی، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت ورودی | ۱.۲۰ دلار / ۱ میلیون توکن |
| قیمت ورودی کش شده | ۰.۲۴ دلار / ۱ میلیون توکن (۸۰٪ کاهش هزینه) |
| قیمت خروجی | ۴.۰۰ دلار / ۱ میلیون توکن |
| نقاط قوت | درک بینایی، پشتیبانی چند تصویر، توان بالا |
| بهترین استفاده | تحلیل تصویر، پرسش و پاسخ بصری، درک اسناد، وظایف چندحالتی |
| در دسترس در | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **درک بینایی**: پردازش و تحلیل تصاویر با دقت بالا
- **پشتیبانی چند تصویر**: مدیریت چندین تصویر در یک درخواست
- **توان بالا**: بهینه‌سازی شده برای پردازش بصری سریع
- **کش زمینه**: ۸۰٪ کاهش هزینه در ورودی‌های کش شده
- **فراخوانی تابع**: پشتیبانی کامل از ابزار با ورودی‌های بصری
- **جریان‌سازی**: پاسخ‌های جریانی بلادرنگ

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5v-turbo",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "چه اشیائی در این تصویر می‌بینید؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/image.jpg"},
                },
            ],
        }
    ],
    max_tokens=2048,
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5v-turbo` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
            ],
        }
    ],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-5

مدل پایه پرچمدار Z.AI که برای مهندسی عامل‌محور طراحی شده، قادر به ارائه بهره‌وری قابل اعتماد در مهندسی سیستم‌های پیچیده و وظایف عامل‌محور بلندمدت است. GLM-5 عملکرد SOTA را در کدنویسی و قابلیت‌های عامل‌محور در میان مدل‌های open-weight به دست می‌آورد.

### glm-5

مدل پرچمدار Z.AI که هم‌ترازی عملکرد با Claude Opus 4.5 را در وظایف مهندسی نرم‌افزار به دست می‌آورد، با بالاترین امتیازات در میان مدل‌های open-weight در SWE-bench Verified و Terminal Bench 2.0.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5` |
| پنجره زمینه | ۲۰۰,۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸,۰۰۰ توکن |
| قابلیت‌ها | گفتگو، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، تفکر عمیق |
| قیمت ورودی | $1.10 / 1M توکن |
| قیمت ورودی کش‌شده | $0.22 / 1M توکن (۸۰٪ کاهش هزینه) |
| قیمت خروجی | $3.52 / 1M توکن |
| نقاط قوت | کدنویسی SOTA، مهندسی عامل‌محور، عملکرد سطح Claude Opus 4.5 |
| مناسب برای | کدنویسی عامل‌محور، وظایف عامل‌محور بلندمدت، مهندسی نرم‌افزار، طراحی سیستم پیچیده |
| در دسترس در | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **مهندسی عامل‌محور**: طراحی شده برای مهندسی سیستم‌های پیچیده و وظایف عامل‌محور بلندمدت
- **عملکرد SOTA در کدنویسی**: امتیاز 77.8 در SWE-bench Verified، 56.2 در Terminal Bench 2.0 (بالاترین در میان مدل‌های open-weight)
- **سطح Claude Opus 4.5**: هم‌ترازی عملکرد در وظایف مهندسی نرم‌افزار
- **مقیاس مدل بزرگتر**: 744 میلیارد پارامتر (40 میلیارد فعال) با 28.5T داده پیش‌آموزش
- **توجه پراکنده**: DeepSeek Sparse Attention برای بهره‌وری بهبود یافته
- **قابلیت‌های پیشرفته**: حالت تفکر، جریان، فراخوانی تابع، کش زمینه، خروجی ساختاریافته

**نکات برجسته عملکرد:**

GLM-5 عملکرد پیشگامانه‌ای به دست می‌آورد:
- عملکرد بهتر از Gemini 3.0 Pro در کدنویسی کلی
- دستیابی به SOTA در میان مدل‌های open-weight در SWE-bench Verified و τ²-Bench
- برتری در توسعه فرانت‌اند، مهندسی سیستم‌های بک‌اند، و وظایف اجرای بلندمدت
- برنامه‌ریزی بلندمدت عامل‌محور خودکار، بازسازی بک‌اند، و اشکال‌زدایی عمیق

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5",
    "messages": [
      {
        "role": "user",
        "content": "معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن."
      }
    ],
    "max_tokens": 8192,
    "temperature": 0.6
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5",
    messages=[
        {
            "role": "user",
            "content": "معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن.",
        }
    ],
    max_tokens=8192,
    temperature=0.6,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-5",
    messages: [
        {
            role: "user",
            content: "معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن."
        }
    ],
    max_tokens: 8192,
    temperature: 0.6
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "معماری میکروسرویس‌ها را برای پلتفرم تجارت الکترونیک با سرویس‌های مدیریت سفارش، موجودی و پرداخت طراحی و پیاده‌سازی کن.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**حالت تفکر عمیق:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5",
    "messages": [
      {
        "role": "user",
        "content": "این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده."
      }
    ],
    "thinking": {
      "type": "enabled",
      "budget_tokens": 15000
    },
    "max_tokens": 16384
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5",
    messages=[
        {
            "role": "user",
            "content": "این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده.",
        }
    ],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 15000}},
    max_tokens=16384,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-5",
    messages: [
        {
            role: "user",
            content: "این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده."
        }
    ],
    thinking: {
        type: "enabled",
        budget_tokens: 15000
    },
    max_tokens: 16384
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "این کدبیس پیچیده را تحلیل کن و بهبودهای معماری را برای نگهداری و مقیاس‌پذیری بهتر پیشنهاد بده.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-5-Turbo

مدل پایه Z.AI که عمیقا برای سناریوهای عاملی OpenClaw بهینه‌سازی شده است. این مدل از مرحله آموزش به طور خاص برای نیازمندی‌های اصلی وظایف OpenClaw بهینه‌سازی شده و قابلیت‌های کلیدی مانند فراخوانی ابزار، پیروی از دستورات، وظایف زمان‌بندی‌شده و پایدار، و اجرای زنجیره بلند را تقویت کرده است.

### glm-5-turbo

مدل بهبود یافته ClawBench که برای گردش‌های کاری عاملی دنیای واقعی طراحی شده، با قابلیت‌های برتر فراخوانی ابزار، پیروی از دستورات و اجرای زنجیره بلند.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-5-turbo` |
| پنجره زمینه | ۲۰۰,۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸,۰۰۰ توکن |
| قابلیت‌ها | گفتگو، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، حالت تفکر، MCP |
| قیمت ورودی | $1.32 / 1M توکن |
| قیمت ورودی کش‌شده | $0.264 / 1M توکن (۸۰٪ کاهش هزینه) |
| قیمت خروجی | $4.40 / 1M توکن |
| نقاط قوت | بومی OpenClaw، فراخوانی ابزار دقیق، پیروی از دستورات، اجرای زنجیره بلند |
| مناسب برای | گردش‌های کاری عاملی، برنامه‌های سنگین ابزار، وظایف زمان‌بندی‌شده، اتوماسیون چند مرحله‌ای |
| در دسترس در | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **مدل بومی OpenClaw**: ساخته شده به طور سیستماتیک برای گردش‌های کاری عاملی دنیای واقعی از داده‌های آموزشی تا اهداف بهینه‌سازی
- **فراخوانی ابزار—فراخوانی دقیق**: قابلیت تقویت‌شده برای فراخوانی ابزارها و مهارت‌های مختلف خارجی با ثبات و قابلیت اطمینان بیشتر در وظایف چند مرحله‌ای
- **پیروی از دستورات—تجزیه پیشرفته**: قابلیت‌های درک و تجزیه قوی‌تر برای دستورات پیچیده، چندلایه و زنجیره بلند
- **وظایف زمان‌بندی‌شده و پایدار**: بهینه‌سازی شده برای تریگرهای زمان‌بندی‌شده، اجرای مداوم و وظایف طولانی‌مدت با درک بهتر ابعاد زمانی
- **زنجیره‌های بلند با توان بالا**: کارایی اجرا و ثبات پاسخ بهبود یافته برای توان داده بالا و زنجیره‌های منطقی بلند
- **حالت تفکر**: حالت‌های تفکر متعدد برای سناریوهای مختلف
- **خروجی جریانی**: پاسخ‌های جریانی بلادرنگ برای تجربه تعامل کاربر بهتر
- **کش زمینه**: مکانیزم کش هوشمند برای بهینه‌سازی عملکرد در مکالمات طولانی
- **خروجی ساختاریافته**: پشتیبانی از JSON و سایر قالب‌های خروجی ساختاریافته
- **پشتیبانی MCP**: یکپارچه‌سازی انعطاف‌پذیر ابزارها و منابع داده MCP خارجی

**عملکرد ZClawBench:**

GLM-5-Turbo بهبودهای قابل توجهی نسبت به GLM-5 در سناریوهای OpenClaw ارائه می‌دهد:
- عملکرد بهتر از چندین مدل پیشرو در دسته‌های وظایف کلیدی متعدد
- پوشش راه‌اندازی محیط، توسعه نرم‌افزار، بازیابی اطلاعات، تحلیل داده و ایجاد محتوا
- مدیریت ۳۰-۵۰٪ گردش‌های کاری عامل تحقیقاتی به طور خودمختار

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "به عنوان یک متخصص بازاریابی، لطفا یک شعار جذاب برای محصول من ایجاد کنید."
      },
      {
        "role": "assistant",
        "content": "البته، برای ایجاد یک شعار جذاب، لطفا بیشتر در مورد محصولتان بگویید."
      },
      {
        "role": "user",
        "content": "پلتفرم باز Z.AI"
      }
    ],
    "max_tokens": 4096,
    "temperature": 1.0
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5-turbo",
    messages=[
        {
            "role": "user",
            "content": "به عنوان یک متخصص بازاریابی، لطفا یک شعار جذاب برای محصول من ایجاد کنید.",
        },
        {
            "role": "assistant",
            "content": "البته، برای ایجاد یک شعار جذاب، لطفا بیشتر در مورد محصولتان بگویید.",
        },
        {
            "role": "user",
            "content": "پلتفرم باز Z.AI",
        },
    ],
    max_tokens=4096,
    temperature=1.0,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-5-turbo",
    messages: [
        {
            role: "user",
            content: "به عنوان یک متخصص بازاریابی، لطفا یک شعار جذاب برای محصول من ایجاد کنید."
        },
        {
            role: "assistant",
            content: "البته، برای ایجاد یک شعار جذاب، لطفا بیشتر در مورد محصولتان بگویید."
        },
        {
            role: "user",
            content: "پلتفرم باز Z.AI"
        }
    ],
    max_tokens: 4096,
    temperature: 1.0
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5-turbo` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="پلتفرم باز Z.AI",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "پلتفرم باز Z.AI",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "پلتفرم باز Z.AI",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**حالت تفکر:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5-turbo",
    "messages": [
      {
        "role": "user",
        "content": "یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند."
      }
    ],
    "thinking": {
      "type": "enabled"
    },
    "stream": true,
    "max_tokens": 4096,
    "temperature": 1.0
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5-turbo",
    messages=[
        {
            "role": "user",
            "content": "یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند.",
        }
    ],
    extra_body={"thinking": {"type": "enabled"}},
    stream=True,
    max_tokens=4096,
    temperature=1.0,
)

for chunk in response:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-5-turbo",
    messages: [
        {
            role: "user",
            content: "یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند."
        }
    ],
    thinking: {
        type: "enabled"
    },
    stream: true,
    max_tokens: 4096,
    temperature: 1.0
});

for await (const chunk of response) {
    if (chunk.choices[0]?.delta?.content) {
        process.stdout.write(chunk.choices[0].delta.content);
    }
}

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-5-turbo` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک هارنس عامل تحقیقاتی طراحی کنید که از خطوط لوله داده، محیط‌های آموزش و همکاری بین تیمی پشتیبانی کند.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-4.7

جدیدترین مدل در سری GLM که عمق استدلال برابر با o3 را با کارایی تا ۲۰ برابر بهتر ترکیب می‌کند و در کدنویسی و وظایف عاملی برتری دارد.

### glm-4.7

پیشرفته‌ترین مدل Z.AI که عمق استدلال برابر با o3 را با کارایی استثنایی ترکیب می‌کند و عملکرد برتر در کدنویسی، ریاضیات و گردش‌های کاری عامل‌محور ارائه می‌دهد.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-4.7` |
| پنجره زمینه | ۲۰۰,۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸,۰۰۰ توکن |
| قابلیت‌ها | گفتگو، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، تفکر عمیق |
| قیمت ورودی | $0.60 / 1M توکن |
| قیمت ورودی کش‌شده | $0.11 / 1M توکن (۸۲٪ کاهش هزینه) |
| قیمت خروجی | $2.20 / 1M توکن |
| نقاط قوت | استدلال سطح o3، کارایی ۲۰ برابر، کدنویسی برتر، گردش‌های کاری عامل‌محور |
| مناسب برای | کدنویسی پیچیده، اتوماسیون عامل‌محور، حل مسائل ریاضی، برنامه‌نویسی رقابتی |
| در دسترس در | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |

**ویژگی‌های کلیدی:**
- **استدلال سطح o3**: دستیابی به عمق استدلال برابر با o3 در بنچمارک‌های چالش‌برانگیز
- **کارایی ۲۰ برابر**: ارائه کارایی تا ۲۰ برابر بهتر با هزینه ۵۰٪ کمتر نسبت به رقبا
- **کدنویسی برتر**: عملکرد بهتر از Claude Sonnet 4 و GPT-4.1 در وظایف کدنویسی
- **حالت تفکر عمیق**: پشتیبانی از حالت `hard_thinking_low` برای وظایف استدلال پیچیده
- **یکپارچه‌سازی سیستم اجرا**: پشتیبانی بومی برای گردش‌های کاری عامل‌محور با اجرای کد
- **زمینه گسترده**: پنجره زمینه ۲۰۰K توکن با ظرفیت خروجی ۱۲۸K توکن

**نکات برجسته عملکرد:**

GLM-4.7 عملکرد پیشگامانه‌ای به دست می‌آورد:
- برابری با o3 در بنچمارک‌های استدلال (AIME 2025، GPQA Diamond)
- عملکرد بهتر از Claude Sonnet 4 و GPT-4.1 در وظایف کدنویسی
- عملکرد استثنایی در LiveCodeBench و SWE-Bench
- کارایی تا ۲۰ برابر بیشتر نسبت به مدل‌های رقیب

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7",
    "messages": [
      {
        "role": "user",
        "content": "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو."
      }
    ],
    "max_tokens": 4096,
    "temperature": 0.6
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.7",
    messages=[
        {
            "role": "user",
            "content": "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو.",
        }
    ],
    max_tokens=4096,
    temperature=0.6,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.7",
    messages: [
        {
            role: "user",
            content: "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو."
        }
    ],
    max_tokens: 4096,
    temperature: 0.6
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.7` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن، شامل عملیات درج، حذف و جستجو.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**حالت تفکر عمیق:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7",
    "messages": [
      {
        "role": "user",
        "content": "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد"
      }
    ],
    "thinking": {
      "type": "enabled",
      "budget_tokens": 10000
    },
    "max_tokens": 8192
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.7",
    messages=[
        {
            "role": "user",
            "content": "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
        }
    ],
    extra_body={"thinking": {"type": "enabled", "budget_tokens": 10000}},
    max_tokens=8192,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.7",
    messages: [
        {
            role: "user",
            content: "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد"
        }
    ],
    thinking: {
        type: "enabled",
        budget_tokens: 10000
    },
    max_tokens: 8192
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.7` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "این مسئله IMO را حل کن: همه اعداد صحیح مثبت n را پیدا کن به طوری که n^2 + 1 بر n^3 + n + 1 بخش‌پذیر باشد",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## سری GLM-4.7-Flash

سری GLM-4.7-Flash قدرت GLM-4.7 را در بسته‌های کوچک‌تر، سریع‌تر و ارزان‌تر ارائه می‌دهد. این مدل‌ها در معیارهای اصلی مانند SWE-bench Verified و τ²-Bench به امتیازات SOTA متن‌باز در میان مدل‌های با اندازه مشابه دست یافته‌اند.

### glm-4.7-flashx

سریع‌ترین مدل در خانواده GLM-4.7، بهینه‌سازی شده برای برنامه‌های حساس به سرعت در عین حفظ قابلیت‌های برنامه‌نویسی عالی.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-4.7-flashx` |
| پنجره متن | ۲۰۰,۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸,۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت ورودی | $۰.۰۷۷ / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | $۰.۰۱۱ / ۱ میلیون توکن (۸۶٪ کاهش هزینه) |
| قیمت خروجی | $۰.۴۴ / ۱ میلیون توکن |
| نقاط قوت | استنتاج سریع، مقرون‌به‌صرفه، کدنویسی عالی |
| بهترین برای | برنامه‌های با توان عملیاتی بالا، پاسخ‌های سریع، استقرارهای حساس به هزینه |
| دسترسی در | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |

**ویژگی‌های کلیدی:**
- **SOTA متن‌باز**: دستیابی به امتیازات پیشرفته در میان مدل‌های با اندازه مشابه در SWE-bench Verified و τ²-Bench
- **توسعه برتر**: عملکرد عالی در هر دو وظایف توسعه فرانت‌اند و بک‌اند
- **استنتاج سریع**: بهینه‌سازی شده برای سرعت با تأخیر پاسخ کمتر
- **مقرون‌به‌صرفه**: قیمت‌گذاری به طور قابل توجهی کمتر از مدل کامل GLM-4.7

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7-flashx",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند."
      }
    ],
    "max_tokens": 2048,
    "temperature": 0.7
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.7-flashx",
    messages=[
        {
            "role": "user",
            "content": "یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند.",
        }
    ],
    max_tokens=2048,
    temperature=0.7,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.7-flashx",
    messages: [
        {
            role: "user",
            content: "یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند."
        }
    ],
    max_tokens: 2048,
    temperature: 0.7
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.7-flashx` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک تابع TypeScript بنویس که یک ابزار debounce با تایپ مناسب پیاده‌سازی کند.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

### glm-4.7-flash

مدلی متعادل با عملکرد عالی و کارایی بهبود یافته نسبت به مدل کامل GLM-4.7، به ویژه قوی برای وظایف توسعه، ترجمه و پردازش متن طولانی.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-4.7-flash` |
| پنجره متن | ۲۰۰,۰۰۰ توکن |
| حداکثر خروجی | ۱۲۸,۰۰۰ توکن |
| قابلیت‌ها | چت، فراخوانی تابع، خروجی‌های ساختاریافته |
| قیمت ورودی | $۰.۰۷ / ۱ میلیون توکن |
| قیمت ورودی کش‌شده | $۰.۰۱ / ۱ میلیون توکن (۸۶٪ کاهش هزینه) |
| قیمت خروجی | $۰.۴۰ / ۱ میلیون توکن |
| نقاط قوت | عملکرد متعادل، عالی برای توسعه، ترجمه |
| بهترین برای | توسعه فرانت‌اند/بک‌اند، نوشتن چینی، ترجمه، پردازش متن طولانی |
| دسترسی در | `v1/chat/completions`، `v1/responses` (جزئی)، `v1/messages` (جزئی) |

**ویژگی‌های کلیدی:**
- **کاربردهای متنوع**: عالی برای نوشتن چینی، ترجمه، پردازش متن طولانی و تعاملات نقش‌آفرینی
- **زیبایی‌شناسی فرانت‌اند برتر**: تولید صفحات وب، ارائه‌ها و پوسترهای بصری برتر
- **مقرون‌به‌صرفه**: قیمت‌گذاری تقریبا ۹۰٪ کمتر از مدل کامل GLM-4.7 در عین حفظ کیفیت
- **متن گسترده**: پنجره متن ۲۰۰ هزار توکن با ظرفیت خروجی ۱۲۸ هزار توکن

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.7-flash",
    "messages": [
      {
        "role": "user",
        "content": "یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن."
      }
    ],
    "max_tokens": 4096,
    "temperature": 0.7
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.7-flash",
    messages=[
        {
            "role": "user",
            "content": "یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن.",
        }
    ],
    max_tokens=4096,
    temperature=0.7,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.7-flash",
    messages: [
        {
            role: "user",
            content: "یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن."
        }
    ],
    max_tokens: 4096,
    temperature: 0.7
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.7-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک صفحه لندینگ مدرن و واکنش‌گرا برای یک محصول SaaS با بخش هیرو و جدول قیمت‌گذاری طراحی کن.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


---

## GLM-4.6

جدیدترین نسخه در سری GLM که پیشرفت‌های جامع در کدنویسی، استدلال، نوشتن و برنامه‌های عامل‌محور دست یافته است.

### glm-4.6

مدل پرچمدار Z.AI که عملکرد برتر در وظایف واقعی کدنویسی ارائه می‌دهد و قابلیت‌هایی برابر با Claude Sonnet 4 نشان می‌دهد.

| ویژگی | جزئیات |
| -------------- | ---------------------------------------------------------------- |
| شناسه مدل | `glm-4.6` |
| پنجره زمینه | 200,000 توکن |
| حداکثر خروجی | 128,000 توکن |
| قابلیت‌ها | گفتگو، فراخوانی تابع، خروجی‌های ساختاریافته، استدلال، جستجوی وب |
| قیمت ورودی | $0.60 / 1M توکن |
| قیمت ورودی کش‌شده | $0.11 / 1M توکن (82٪ کاهش هزینه) |
| قیمت خروجی | $2.20 / 1M توکن |
| قیمت جستجوی وب | $0.01 / فراخوانی |
| نقاط قوت | کدنویسی برتر، پردازش زمینه طولانی، استدلال، گردکارهای عامل‌محور |
| مناسب برای | ابزارهای کدنویسی هوش مصنوعی، دفتر هوشمند، تولید محتوا، ترجمه، شخصیت‌های مجازی |
| در دسترس در | `v1/chat/completions` |

**ویژگی‌های کلیدی:**
- **پنجره زمینه گسترده**: 200K توکن (گسترش یافته از 128K) برای مدیریت وظایف پیچیده عامل‌محور
- **عملکرد برتر کدنویسی**: عملکرد بهتر از Claude Sonnet 4 در تست‌های واقعی کدنویسی در محیط Claude Code
- **استدلال پیشرفته**: حالت تفکر داخلی با پارامتر `thinking` برای حل مسئله بهبود یافته
- **کارایی توکن**: بیش از 30٪ کارآمدتر از نسخه قبلی GLM-4.5
- **استفاده از ابزار**: پشتیبانی بومی برای فراخوانی ابزار در حین استنتاج
- **یکپارچه‌سازی جستجوی وب**: قابلیت‌های جستجوی وب داخلی برای اطلاعات به‌روز
- **فراخوانی تابع**: اتصال مدل به ابزارها و سیستم‌های خارجی
- **خروجی‌های ساختاریافته**: بازگرداندن پاسخ‌ها در قالب‌های خاص و سازمان‌یافته

**نکات برجسته عملکرد:**

GLM-4.6 عملکردی برابر با Claude Sonnet 4/Claude Sonnet 4.6 در 8 معیار معتبر از جمله موارد زیر به دست می‌آورد:
- AIME 25
- GPQA
- LCB v6
- HLE
- SWE-Bench Verified

در 74 تست واقعی کدنویسی در محیط Claude Code، GLM-4.6 عملکرد برتری نسبت به Claude Sonnet 4 و سایر مدل‌ها نشان می‌دهد، با شفافیت در تمام مسیرهای تست (در دسترس عموم در https://huggingface.co/datasets/zai-org/CC-Bench-trajectories).

**استفاده پایه:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.6",
    "messages": [
      {
        "role": "user",
        "content": "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن."
      }
    ],
    "max_tokens": 4096,
    "temperature": 0.6
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن.",
        }
    ],
    max_tokens=4096,
    temperature=0.6,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.6",
    messages: [
        {
            role: "user",
            content: "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن."
        }
    ],
    max_tokens: 4096,
    temperature: 0.6
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک نوار ناوبری واکنش‌گرا با منوهای کشویی با استفاده از React و Tailwind CSS ایجاد کن.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**حالت استدلال با پارامتر Thinking:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.6",
    "messages": [
      {
        "role": "user",
        "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن."
      }
    ],
    "thinking": {
      "type": "enabled"
    },
    "max_tokens": 4096,
    "temperature": 0.6
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
        }
    ],
    extra_body={"thinking": {"type": "enabled"}},
    max_tokens=4096,
    temperature=0.6,
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
    model: "glm-4.6",
    messages: [
        {
            role: "user",
            content: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن."
        }
    ],
    thinking: {
        type: "enabled"
    },
    max_tokens: 4096,
    temperature: 0.6
});

console.log(response.choices[0].message.content);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک معماری میکروسرویس مقیاس‌پذیر برای یک پلتفرم تجارت الکترونیک طراحی کن.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


**مثال فراخوانی تابع:**

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-4.6",
    "messages": [
      {
        "role": "user",
        "content": "آب و هوای نیویورک چطور است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت اطلاعات فعلی آب و هوا",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "tool_choice": "auto"
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات فعلی آب و هوا",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "نام شهر",
                    }
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[{"role": "user", "content": "آب و هوای نیویورک چطور است؟"}],
    tools=tools,
    tool_choice="auto",
)

print(response.choices[0].message)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1"
});

const tools = [
    {
        type: "function",
        function: {
            name: "get_weather",
            description: "دریافت اطلاعات فعلی آب و هوا",
            parameters: {
                type: "object",
                properties: {
                    location: {
                        type: "string",
                        description: "نام شهر",
                    }
                },
                required: ["location"],
            },
        },
    }
];

const response = await client.chat.completions.create({
    model: "glm-4.6",
    messages: [{role: "user", content: "آب و هوای نیویورک چطور است؟"}],
    tools: tools,
    tool_choice: "auto",
});

console.log(response.choices[0].message);

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
            "type": "object",
            "properties": {"location": {"type": "string"}},
            "required": ["location"],
            "additionalProperties": False,
        },
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input="آب و هوای نیویورک چطور است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const tools = [
  {
    type: "function",
    name: "get_current_weather",
    description: "Get the current weather in a given location.",
    parameters: {
      type: "object",
      properties: { location: { type: "string" } },
      required: ["location"],
      additionalProperties: false,
    },
  },
];

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "آب و هوای نیویورک چطور است؟",
  tools,
});

for (const item of response.output) {
  if (item.type === "function_call") {
    console.log(item.name, item.arguments);
  }
}
console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "آب و هوای نیویورک چطور است؟",
    "tools": [
      {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "parameters": {
          "type": "object",
          "properties": {
            "location": {
              "type": "string"
            }
          },
          "required": [
            "location"
          ],
          "additionalProperties": false
        }
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## موارد استفاده

### کدنویسی هوش مصنوعی

GLM-4.6 از زبان‌های برنامه‌نویسی اصلی از جمله Python، JavaScript و Java پشتیبانی می‌کند و زیبایی‌شناسی و طرح‌بندی منطقی برتر در کد فرانت‌اند ارائه می‌دهد. به طور بومی وظایف متنوع عامل را با قابلیت‌های بهبود یافته برنامه‌ریزی خودمختار و فراخوانی ابزار مدیریت می‌کند و در موارد زیر برتری دارد:

- تجزیه وظیفه
- همکاری بین ابزاری
- تنظیمات پویا
- گردکارهای توسعه پیچیده
- یکپارچه‌سازی IDE (Claude Code، Cline، OpenCode، Roo Code، Kilo Code)

**مثال:**

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "این تابع Python را برای کارآمدتر شدن بازسازی کن:\n\ndef find_duplicates(arr):\n    result = []\n    for i in range(len(arr)):\n        for j in range(i+1, len(arr)):\n            if arr[i] == arr[j] and arr[i] not in result:\n                result.append(arr[i])\n    return result",
        }
    ],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Explain how AvalAI provides a unified API for this request.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### دفتر هوشمند

به طور قابل توجهی کیفیت ارائه را در ایجاد PowerPoint و سناریوهای اتوماسیون اداری افزایش می‌دهد. طرح‌بندی‌های زیباشناختی پیشرفته با ساختارهای منطقی واضح تولید می‌کند در حالی که یکپارچگی محتوا و دقت بیان را حفظ می‌کند، که آن را برای موارد زیر ایده‌آل می‌کند:

- سیستم‌های اتوماسیون اداری
- ابزارهای ارائه هوش مصنوعی
- تولید اسناد
- ایجاد گزارش

### ترجمه و برنامه‌های بین زبانی

کیفیت ترجمه برای زبان‌های متعدد (فرانسوی، روسی، ژاپنی، کره‌ای) و زمینه‌های غیررسمی بهینه‌سازی شده است، به ویژه مناسب برای:

- محتوای رسانه‌های اجتماعی
- توضیحات تجارت الکترونیک
- ترجمه درام کوتاه
- خدمات فرامرزی
- ارتباطات سازمانی جهانی

انسجام معنایی و ثبات سبکی را در متون طولانی حفظ می‌کند در حالی که به سازگاری سبک برتر و بیان بومی‌سازی شده دست می‌یابد.

### تولید محتوا

از تولید محتوای متنوع از جمله موارد زیر پشتیبانی می‌کند:

- رمان‌ها و نوشتار خلاق
- فیلمنامه‌ها و سناریوها
- متن‌نویسی بازاریابی
- پست‌های وبلاگ و مقالات

بیان طبیعی را از طریق گسترش زمینه‌ای و تنظیم احساسی به دست می‌آورد.

### شخصیت‌های مجازی

لحن و رفتار ثابت را در مکالمات چند دوره‌ای حفظ می‌کند، ایده‌آل برای:

- انسان‌های مجازی
- برنامه‌های هوش مصنوعی اجتماعی
- شخصیت‌بخشی برند
- ربات‌های خدمات مشتری
- داستان‌سرایی تعاملی

تعاملات را با ثبات شخصیت گرم‌تر و معتبرتر می‌کند.

### جستجوی هوشمند و تحقیق عمیق

درک قصد کاربر، بازیابی ابزار و یکپارچه‌سازی نتایج را بهبود می‌بخشد. مدل:

- نتایج جستجوی دقیق را برمی‌گرداند
- پیامدها را به طور عمیق ترکیب می‌کند
- از سناریوهای تحقیق عمیق پشتیبانی می‌کند
- پاسخ‌های بینشی با یکپارچه‌سازی جستجوی وب به قیمت $0.01 به ازای هر فراخوانی ارائه می‌دهد

**مثال جستجوی وب:**

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[
        {
            "role": "user",
            "content": "آخرین پیشرفت‌ها در محاسبات کوانتومی تا سال 2025 چیست؟",
        }
    ],
    extra_body={"web_search": True},
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="آخرین پیشرفت‌ها در محاسبات کوانتومی تا سال 2025 چیست؟",
    tools=[{"type": "web_search"}],
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## پارامترهای کلیدی

### thinking

حالت استدلال مدل را کنترل می‌کند. هنگامی که فعال است، مدل فرآیند تفکر خود را قبل از ارائه پاسخ نهایی نشان می‌دهد.

```python
{"thinking": {"type": "enabled"}}  # یا "disabled"
```

### web_search

قابلیت‌های جستجوی وب را برای بازیابی اطلاعات به‌روز فعال می‌کند. هر فراخوانی جستجو $0.01 هزینه دارد.

```python
{"web_search": True}  # یا False
```

### temperature

تصادفی بودن را در تولید خروجی کنترل می‌کند (0-2). مقادیر پایین‌تر خروجی را متمرکزتر و قطعی‌تر می‌کنند.

```python
{"temperature": 0.6}  # پیش‌فرض: 0.6
```

### max_tokens

حداکثر تعداد توکن‌ها برای تولید در پاسخ (تا 128K).

```python
{"max_tokens": 4096}  # بر اساس نیازهای شما تنظیم کنید
```

## بهترین شیوه‌ها

1. **استفاده از حالت استدلال برای وظایف پیچیده**: پارامتر `thinking` را برای حل مسئله پیچیده، طراحی معماری و وظایف برنامه‌ریزی استراتژیک فعال کنید.

2. **استفاده از زمینه طولانی**: از پنجره زمینه 200K توکن برای پردازش پایگاه‌های کد بزرگ، اسناد گسترده یا مکالمات چند دوره‌ای استفاده کنید.

3. **بهینه‌سازی با ورودی کش‌شده**: از ذخیره‌سازی پرامپت برای کاهش هزینه‌ها تا 82٪ برای زمینه تکراری استفاده کنید.

4. **فعال‌سازی جستجوی وب در صورت نیاز**: جستجوی وب را برای وظایفی که نیاز به اطلاعات فعلی دارند فعال کنید، اما به هزینه $0.01 به ازای هر فراخوانی توجه کنید.

5. **فراخوانی تابع برای یکپارچه‌سازی‌ها**: از فراخوانی تابع برای اتصال GLM-4.6 با ابزارها، پایگاه‌های داده و APIهای خارجی استفاده کنید.

6. **کنترل دما**: از دماهای پایین‌تر (0.3-0.6) برای کدنویسی و وظایف تحلیلی، دماهای بالاتر (0.7-1.0) برای محتوای خلاق استفاده کنید.

7. **خروجی‌های ساختاریافته**: از قابلیت‌های خروجی ساختاریافته برای تجزیه پاسخ قابل پیش‌بینی، فرمت‌های خروجی خاص را درخواست کنید.

## استفاده از مدل‌های Z.AI از طریق AvalAI

با استفاده از نقاط پایانی استاندارد API AvalAI و کتابخانه‌های سازگار با OpenAI به مدل‌های GLM دسترسی پیدا کنید.

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-4.6",
    messages=[{"role": "user", "content": "یک هایکو درباره هوش مصنوعی بنویس."}],
)

print(response.choices[0].message.content)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `glm-4.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک هایکو درباره هوش مصنوعی بنویس.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## منابع مرتبط

- [مستندات رسمی Z.AI](https://docs.z.ai/)
- [API تکمیل گفتگو](fa/api-reference/chat.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [راهنمای خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/guides/rate-limits.md)
- [بهترین شیوه‌ها برای تولید](fa/guides/production-best-practices.md)
