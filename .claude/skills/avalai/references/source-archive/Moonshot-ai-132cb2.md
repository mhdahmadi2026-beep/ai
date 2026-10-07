# Moonshot.ai

Moonshot.ai مدل‌های پیشرفته هوش مصنوعی را از طریق سری Kimi خود ارائه می‌دهد که شامل پنجره‌های زمینه گسترده، قابلیت‌های بینایی، ویژگی‌های استدلال و پشتیبانی جامع از فراخوانی ابزار است. همه مدل‌ها برای مکالمات چینی و انگلیسی بهینه شده‌اند و از فرمت SDK OpenAI پشتیبانی می‌کنند.


## مدل‌های موجود

- [kimi-k3](#kimi-k3) - پرچم‌دار جدید Moonshot AI با ۲٫۸ تریلیون پارامتر، بینایی بومی، استدلال همیشه‌فعال و زمینه ۱ میلیون توکنی
- [kimi-k2.7-code](#kimi-k27-code) - جدیدترین مدل کدنویسی متن‌باز با مهندسی نرم‌افزار SOTA و قابلیت‌های عاملی
- [kimi-k2.7-code-highspeed](#kimi-k27-code-highspeed) - نسخه پرسرعت K2.7 Code برای بارهای کاری کدنویسی با تأخیر پایین
- [kimi-k2.6](#kimi-k26) - مدل متن‌باز با کدنویسی SOTA، اجرای long-horizon و Agent Swarm
- [kimi-k2.5](#kimi-k25) - قوی‌ترین مدل چندوجهی متن‌باز با قابلیت‌های ازدحام عامل
- [kimi-k2-thinking](#kimi-k2-thinking) - مدل استدلال عاملی پرچمدار با قابلیت‌های استدلال عمیق
- [kimi-k2-0711-preview](#kimi-k2-0711-preview) - پیش‌نمایش مدل K2 نسل بعدی
- [kimi-latest](#kimi-latest) - نام مستعاری که اکنون به `kimi-k3` اشاره می‌کند
- [kimi-thinking-preview](#kimi-thinking-preview) - مدل استدلال پیشرفته با زنجیره تفکر
- [moonshot-v1-8k](#moonshot-v1-8k) - مدل مقرون به صرفه با زمینه 8K
- [moonshot-v1-8k-vision-preview](#moonshot-v1-8k-vision-preview) - مدل با قابلیت بینایی 8K
- [moonshot-v1-32k](#moonshot-v1-32k) - مدل متعادل با زمینه 32K
- [moonshot-v1-32k-vision-preview](#moonshot-v1-32k-vision-preview) - مدل با قابلیت بینایی 32K
- [moonshot-v1-128k](#moonshot-v1-128k) - مدل گسترده با زمینه 128K
- [moonshot-v1-128k-vision-preview](#moonshot-v1-128k-vision-preview) - مدل با قابلیت بینایی 128K
- [moonshot-v1-auto](#moonshot-v1-auto) - انتخاب خودکار مدل

## پشتیبانی نقطه پایانی API

| مدل | v1/chat/completions | v1/messages | v1/responses |
|-------|---------------------|-------------|--------------|
| `kimi-k3` / `kimi-latest` | ✅ کامل | ✅ کامل | ⚠️ جزئی |
| سایر مدل‌های Moonshot | ✅ کامل | ⚠️ جزئی | ⚠️ جزئی |

## ویژگی‌های کلیدی

- **پنجره‌های زمینه گسترده**: تا ۱ میلیون توکن با `kimi-k3` برای اسناد، کدبیس‌ها و مکالمات طولانی
- **قابلیت‌های بینایی**: `kimi-k3` درک بصری بومی دارد و مدل‌های قدیمی vision-preview نیز ورودی تصویر را می‌پذیرند
- **استفاده از ابزار (فراخوانی تابع)**: همه مدل‌ها از حداکثر ۱۲۸ ابزار در هر درخواست پشتیبانی می‌کنند
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته از طریق پارامتر `response_format`
- **حالت جزئی**: امکان پیش‌پر کردن پاسخ‌های دستیار برای کنترل بهتر خروجی
- **کش کردن پرامپت**: همه مدل‌ها از ورودی کش شده برای صرفه‌جویی قابل توجه در هزینه پشتیبانی می‌کنند
- **پشتیبانی دوزبانه**: بهینه‌سازی شده برای مکالمات چینی و انگلیسی

---

## kimi-k3

**توانمندترین مدل پرچم‌دار Moonshot AI**

Kimi K3 یک مدل پراکنده Mixture-of-Experts با ۲٫۸ تریلیون پارامتر است که با Kimi Delta Attention و Attention Residuals ساخته شده است. این مدل زمینه ۱ میلیون توکنی، درک بصری بومی، استدلال همیشه‌فعال، کدنویسی بلندمدت، کار دانشی، خروجی ساختاریافته و استفاده از ابزار را ترکیب می‌کند. نام مستعار `kimi-latest` اکنون به این مدل اشاره می‌کند.

### ویژگی‌ها

- **زمینه ۱ میلیون توکنی**: پردازش اسناد طولانی، کدبیس‌های بزرگ و مکالمات گسترده
- **استدلال همیشه‌فعال**: به‌صورت پیش‌فرض از `reasoning_effort: "max"` استفاده می‌کند
- **بینایی بومی**: درک تصویر و بازخورد بصری در کنار متن
- **کدنویسی بلندمدت**: مناسب وظایف مهندسی در مقیاس ریپو و استفاده مداوم از ابزار
- **خروجی ساختاریافته**: پشتیبانی از JSON Schema سخت‌گیرانه
- **فراخوانی ابزار**: پشتیبانی از ابزارهای سفارشی و گردش‌کارهای چندمرحله‌ای
- **کش خودکار پرامپت**: استفاده مجدد از پیشوندهای بدون تغییر، بدون شناسه کش یا پارامتر اضافی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $3.00 به ازای 1M توکن |
| توکن‌های ورودی کش‌شده | $0.30 به ازای 1M توکن |
| توکن‌های خروجی | $15.00 به ازای 1M توکن |


### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
|----------|---------|
| `v1/chat/completions` | ✅ کامل |
| `v1/messages` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k3",
    "messages": [{"role": "user", "content": "برای مهاجرت یک مونولیت بزرگ Python برنامه طراحی کن."}],
    "reasoning_effort": "max",
    "max_completion_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")
response = client.chat.completions.create(
    model="kimi-k3",
    messages=[
        {
            "role": "user",
            "content": "برای مهاجرت یک مونولیت بزرگ Python برنامه طراحی کن.",
        }
    ],
    reasoning_effort="max",
    max_completion_tokens=8192,
)
print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const response = await client.chat.completions.create({
  model: "kimi-k3",
  messages: [{ role: "user", content: "برای مهاجرت یک مونولیت بزرگ Python برنامه طراحی کن." }],
  reasoning_effort: "max",
  max_completion_tokens: 8192,
});
console.log(response.choices[0].message.content);

```

---

## kimi-k2.7-code

**کدنویسی متن‌باز SOTA — مهندسی نرم‌افزار و گردش‌کارهای عاملی**

Kimi K2.7 Code جدیدترین مدل متن‌باز Moonshot AI است که به‌طور ویژه برای مهندسی نرم‌افزار و کدنویسی عاملی ساخته شده است. این مدل نتایج state-of-the-art را در معیارهای کدنویسی و عاملی ارائه می‌دهد و قابلیت اطمینان چندمرحله‌ای قدرتمندی برای تولید full-stack، وظایف سطح ریپو و استفاده از ابزار در افق بلند دارد. این مدل از طریق ارائه‌دهنده API شرکت Fireworks.ai سرویس‌دهی می‌شود.

### ویژگی‌ها

- **کدنویسی SOTA**: عملکرد پیشرو در مهندسی نرم‌افزار در وظایف فرانت‌اند و بک‌اند
- **گردش‌کارهای عاملی**: اجرای چندمرحله‌ای قابل اطمینان با استفاده از ابزار برای کارهای سطح ریپو و full-stack
- **اجرای Long-Horizon**: مدیریت وظایف پیچیده و چندمرحله‌ای با قابلیت اطمینان بالا
- **فراخوانی توابع**: پشتیبانی کامل از فراخوانی توابع
- **زمینه گسترده**: پنجره زمینه ۲۶۲٬۱۴۴ توکنی برای کدبیس‌های بزرگ و جلسات طولانی

### قیمت‌گذاری

| نوع | هزینه |
|-----|-------|
| توکن‌های ورودی | $0.95 در هر 1M توکن |
| توکن‌های ورودی کش‌شده | $0.19 در هر 1M توکن |
| توکن‌های خروجی | $4.00 در هر 1M توکن |


### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
|----------|---------|
| `v1/chat/completions` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

### موارد استفاده

- تولید برنامه‌های وب full-stack
- درک و بازآرایی کد در سطح ریپو
- گردش‌کارهای کدنویسی عاملی با استفاده از ابزار در چند مرحله
- جایگزین کدنویسی متن‌باز کم‌هزینه و باکیفیت

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.7-code",
    "messages": [
      {
        "role": "user",
        "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن."
      }
    ],
    "max_tokens": 8192
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2.7-code",
    messages=[
        {
            "role": "user",
            "content": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
        },
    ],
    max_tokens=8192,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k2.7-code",
  messages: [
    {
      role: "user",
      content: "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
    },
  ],
  max_tokens: 8192,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2.7-code` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
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
  input: "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک REST API در FastAPI با احراز هویت JWT و مدل‌های SQLAlchemy پیاده‌سازی کن.",
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

## kimi-k2.7-code-highspeed

**کدنویسی با تأخیر پایین — نسخه پرسرعت K2.7 Code**

Kimi K2.7 Code Highspeed یک نسخه سرویس‌دهی پرسرعت از Kimi K2.7 Code است که برای بارهای کاری کدنویسی با تأخیر پایین، جایی که زمان پاسخ سریع‌تر اهمیت دارد، بهینه شده است. این مدل همان قابلیت‌های مهندسی نرم‌افزار و عاملی را حفظ می‌کند و در عین حال توان عملیاتی را در اولویت قرار می‌دهد، با قیمت هر توکن بالاتر که مسیر سرویس‌دهی پرسرعت اختصاصی را منعکس می‌کند. این مدل از طریق ارائه‌دهنده API شرکت Fireworks.ai سرویس‌دهی می‌شود.

### ویژگی‌ها

- **سرویس‌دهی پرسرعت**: بهینه‌شده برای پاسخ‌های با تأخیر پایین در سناریوهای کدنویسی تعاملی
- **کدنویسی SOTA**: همان عملکرد پیشرو مهندسی نرم‌افزار مانند K2.7 Code
- **گردش‌کارهای عاملی**: اجرای چندمرحله‌ای قابل اطمینان با استفاده از ابزار
- **فراخوانی توابع**: پشتیبانی کامل از فراخوانی توابع
- **زمینه گسترده**: پنجره زمینه ۲۶۲٬۱۴۴ توکنی

### قیمت‌گذاری

| نوع | هزینه |
|-----|-------|
| توکن‌های ورودی | $1.90 در هر 1M توکن |
| توکن‌های ورودی کش‌شده | $0.38 در هر 1M توکن |
| توکن‌های خروجی | $8.00 در هر 1M توکن |


### پشتیبانی نقطه پایانی

| نقطه پایانی | پشتیبانی |
|----------|---------|
| `v1/chat/completions` | ✅ کامل |
| `v1/responses` | ⚠️ جزئی |

### موارد استفاده

- دستیارهای IDE تعاملی که به زمان پاسخ سریع نیاز دارند
- گردش‌کارهای کدنویسی عاملی حساس به تأخیر
- تولید و تکمیل کد بلادرنگ

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.7-code-highspeed",
    "messages": [
      {
        "role": "user",
        "content": "یک هوک جستجوی debounced در React با TypeScript بنویس."
      }
    ],
    "max_tokens": 4096
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2.7-code-highspeed",
    messages=[
        {
            "role": "user",
            "content": "یک هوک جستجوی debounced در React با TypeScript بنویس.",
        },
    ],
    max_tokens=4096,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k2.7-code-highspeed",
  messages: [
    {
      role: "user",
      content: "یک هوک جستجوی debounced در React با TypeScript بنویس.",
    },
  ],
  max_tokens: 4096,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2.7-code-highspeed` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک هوک جستجوی debounced در React با TypeScript بنویس.",
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
  input: "یک هوک جستجوی debounced در React با TypeScript بنویس.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک هوک جستجوی debounced در React با TypeScript بنویس.",
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

## kimi-k2.6

**از کد تا خلق، از یک به چندین — کدنویسی SOTA با اجرای Long-Horizon**

Kimi K2.6 مدل کدنویسی متن‌باز قبلی Moonshot است و برای بارهای کاری جدید کدنویسی عاملی، Kimi K2.7 Code جایگزین پیشنهادی آن است. این مدل همچنان برای کدنویسی state-of-the-art، اجرای long-horizon و قابلیت‌های Agent Swarm کاربرد دارد و بر پایه K2.5 ساخته شده و قابلیت اطمینان چندمرحله‌ای قوی‌تر، تولید full-stack، قابلیت استفاده مجدد Document-to-Skills، Claw Groups (پیش‌نمایش) و Kimi Slides را دارد.

### ویژگی‌ها

- **کدنویسی SOTA**: دستورالعمل‌ها را به رابط‌های فرانت‌اند در سطح Awwwards با خطوط تمیز، انیمیشن‌ها و تعاملات تبدیل می‌کند
- **تولید Full-Stack**: وب‌سایت‌های کامل کارآمد با احراز هویت، تعاملات و عملیات پایگاه داده را از یک دستورالعمل می‌سازد
- **اجرای Long-Horizon**: وظایف پیچیده و چندمرحله‌ای را با قابلیت اطمینان بالاتر و تغییرات غیرضروری کمتر مدیریت می‌کند
- **Agent Swarm**: هماهنگی چندین عامل به‌صورت موازی برای جستجو، تحقیق، تحلیل، نگارش بلند و تولید محتوای چندفرمتی
- **Document to Skills**: تبدیل اسناد باکیفیت به مهارت‌های قابل استفاده مجدد که در وظایف آینده به‌کار می‌آیند
- **Claw Groups (پیش‌نمایش)**: جریان کاری چندعاملی با یک هماهنگ‌کننده که وظایف و پیش‌نیاز‌ها را مدیریت می‌کند
- **Kimi Slides**: تولید ارائه‌های آماده تولید از دستورالعمل‌ها یا ورودی‌های چندفرمتی
- **فراخوانی توابع**: پشتیبانی کامل از فراخوانی توابع

### قیمت‌گذاری

| نوع | هزینه |
|-----|-------|
| توکن‌های ورودی | $0.95 در هر 1M توکن |
| توکن‌های ورودی کش‌شده | $0.16 در هر 1M توکن |
| توکن‌های خروجی | $4.00 در هر 1M توکن |


### موارد استفاده

- تولید برنامه‌های وب full-stack با UI تمیز و احراز هویت
- جریان‌های کاری عامل‌محور long-horizon (تحقیق، تحلیل، تولید خلاقانه)
- هماهنگی چندعاملی از طریق Claw Groups برای پروژه‌های پیچیده
- تولید ارائه‌های آماده تولید با Kimi Slides
- تبدیل Document-to-Skills برای الگوهای قابل استفاده مجدد
- استراتژی بازار و تولید محتوای چندفرمتی

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
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

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2.6",
    messages=[
        {
            "role": "user",
            "content": "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI.",
        },
    ],
    max_tokens=8192,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k2.6",
  messages: [
    {
      role: "user",
      content: "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI.",
    },
  ],
  max_tokens: 8192,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2.6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI.",
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
  input: "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Build a full-stack task management web application with user authentication, real-time updates, and a clean modern UI.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## kimi-k2.5

**قوی‌ترین مدل چندوجهی متن‌باز با هوش عاملی بصری**

Kimi K2.5 قوی‌ترین مدل متن‌باز Moonshot AI تا به امروز است که بر اساس Kimi K2 با آموزش مداوم بر روی تقریبا 15 تریلیون توکن ترکیبی بصری و متنی ساخته شده است. به عنوان یک مدل چندوجهی بومی، K2.5 قابلیت‌های **کدنویسی و بینایی** پیشرفته و یک الگوی **ازدحام عامل** خودهدایت ارائه می‌دهد.

### ویژگی‌ها

- **هوش عاملی بصری**: قابلیت‌های چندوجهی بومی با کدنویسی و بینایی پیشرفته
- **ازدحام عامل**: هدایت تا 100 زیرعامل، اجرای گردش‌های کاری موازی با تا 1500 فراخوانی ابزار
- **کدنویسی با بینایی**: برتری در توسعه فرانت‌اند، تولید کد از ویدیو، و اشکال‌زدایی بصری
- **اجرای 4.5 برابر سریع‌تر**: ازدحام عامل زمان اجرا را در مقایسه با تنظیم تک‌عاملی کاهش می‌دهد
- **پشتیبانی چند نقطه پایانی**: در هر دو نقطه پایانی `v1/chat/completions` و `v1/responses` موجود است
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | ۰.۶۶ دلار به ازای ۱ میلیون توکن |
| توکن‌های ورودی کش‌شده | ۰.۱۱ دلار به ازای ۱ میلیون توکن |
| توکن‌های خروجی | ۳.۳۰ دلار به ازای ۱ میلیون توکن |

### موارد استفاده

- توسعه فرانت‌اند پیچیده با چیدمان‌های تعاملی و انیمیشن‌های غنی
- تولید کد از ویدیو و اشکال‌زدایی بصری
- گردش‌های کاری چند عاملی با اجرای موازی
- وظایف استدلال تصویر و ویدیو
- وظایف کدنویسی پیشرفته با درک بصری
- برنامه‌های عامل خودمختار

### نمونه

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2.5",
    "messages": [
      {
        "role": "user",
        "content": "یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید."
      }
    ],
    "max_tokens": 8000
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2.5",
    messages=[
        {
            "role": "user",
            "content": "یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید.",
        },
    ],
    max_tokens=8000,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k2.5",
  messages: [
    {
      role: "user",
      content: "یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید.",
    },
  ],
  max_tokens: 8000,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2.5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید.",
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
  input: "یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک صفحه فرود واکنش‌گرا با انیمیشن‌های فعال‌شده با اسکرول ایجاد کنید.",
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

## kimi-k2-thinking

**مدل استدلال عاملی پرچم‌دار نسل قبل Moonshot AI با قابلیت‌های استدلال عمیق**

[`kimi-k2-thinking`](fa/news/2025-11-18-new-models-gemini-3-pro-kimi-k2-thinking.md) یک مدل پرچم‌دار نسل قبل Moonshot AI برای استدلال عاملی چندمنظوره، استدلال عمیق و استفاده از ابزار چندمرحله‌ای است. این مدل همچنان برای مسائل بسیار پیچیده‌ای که از زنجیره‌های استدلال گسترده و فراخوانی‌های متوالی ابزار بهره می‌برند کاربردی است.

### ویژگی‌ها

- **استدلال عمیق**: قابلیت‌های استدلال گسترده با فیلد `reasoning_content`
- **استفاده از ابزار چند مرحله‌ای**: طراحی شده برای انجام استدلال عمیق در فراخوانی‌های متعدد ابزار
- **عملکرد عاملی**: برتری در برنامه‌ریزی و اجرای وظایف چند مرحله‌ای پیچیده
- **حل مسئله پیشرفته**: قادر به مقابله با سخت‌ترین مسائل از طریق استدلال گام به گام
- **پنجره زمینه**: پشتیبانی زمینه بزرگ برای تحلیل جامع مسائل
- **دمای توصیه شده**: 1.0 برای عملکرد بهینه
- **max_tokens توصیه شده**: ≥ 16,000 برای اطمینان از بازگشت کامل reasoning_content
- **استریمینگ توصیه شده**: فعال‌سازی `stream: true` برای تجربه کاربری بهتر و جلوگیری از مشکلات timeout
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری
- **بدون آموزش بر روی داده‌های مشتری**: تمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | ۰.۶۶ دلار به ازای ۱ میلیون توکن |
| توکن‌های ورودی کش‌شده | ۰.۱۶۵ دلار به ازای ۱ میلیون توکن |
| توکن‌های خروجی | ۲.۷۵ دلار به ازای ۱ میلیون توکن |
| زمینه جستجو | ۰.۰۰۵ دلار به ازای هر پرس‌وجو |

### موارد استفاده

- وظایف استدلال و حل مسئله پیچیده
- گردش‌های کاری عاملی چند مرحله‌ای با استفاده از ابزار
- برنامه‌ریزی استراتژیک و تصمیم‌گیری
- تحقیق و تحلیل پیشرفته
- تولید کد با استدلال عمیق
- مکالمات پیچیده چند نوبتی که نیاز به حفظ زمینه دارند

### نکات مهم پیاده‌سازی

برای نتایج بهینه با [`kimi-k2-thinking`](fa/news/2025-11-18-new-models-gemini-3-pro-kimi-k2-thinking.md):

1. **شامل کردن زمینه استدلال کامل**: همیشه کل فیلد `reasoning_content` از پاسخ‌های قبلی را در ورودی خود قرار دهید. مدل تصمیم می‌گیرد که کدام بخش‌ها برای استدلال بیشتر ضروری هستند.

2. **تنظیم max_tokens کافی**: از `max_tokens ≥ 16,000` استفاده کنید تا اطمینان حاصل شود که `reasoning_content` و محتوای نهایی کامل بدون کوتاه شدن برگردانده می‌شوند.

3. **استفاده از دمای توصیه شده**: `temperature = 1.0` را تنظیم کنید تا بهترین عملکرد از مدل دریافت کنید.

4. **فعال‌سازی استریمینگ**: از `stream = true` برای تجربه کاربری بهتر و جلوگیری از مشکلات network-timeout استفاده کنید، زیرا پاسخ‌های استدلال می‌توانند بزرگتر از تکمیل‌های معمولی باشند.

5. **دسترسی به reasoning_content**: در SDK OpenAI، از `hasattr(obj, "reasoning_content")` برای بررسی وجود فیلد استفاده کنید و از `getattr(obj, "reasoning_content")` برای دریافت مقدار آن استفاده کنید. فیلد `reasoning_content` در همان سطح فیلد `content` ظاهر می‌شود.

### نمونه

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2-thinking",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI با قابلیت‌های استدلال پیشرفته."
      },
      {
        "role": "user",
        "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید."
      }
    ],
    "max_tokens": 16000,
    "temperature": 1.0,
    "stream": true
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2-thinking",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI با قابلیت‌های استدلال پیشرفته.",
        },
        {
            "role": "user",
            "content": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
        },
    ],
    max_tokens=16000,
    temperature=1.0,
)

# دسترسی به محتوای استدلال در صورت وجود
message = response.choices[0].message
if hasattr(message, "reasoning_content"):
    reasoning = getattr(message, "reasoning_content")
    print("استدلال:", reasoning)

print("پاسخ:", message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "kimi-k2-thinking",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI با قابلیت‌های استدلال پیشرفته.",
    },
    {
      role: "user",
      content: "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
    },
  ],
  max_tokens: 16000,
  temperature: 1.0,
});

// دسترسی به محتوای استدلال در صورت وجود
const message = response.choices[0].message;
if ("reasoning_content" in message) {
  console.log("استدلال:", message.reasoning_content);
}

console.log("پاسخ:", message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2-thinking` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
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
  input: "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک استراتژی جامع بازاریابی دیجیتال برای یک استارتاپ فناوری طراحی کنید.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### نمونه فراخوانی ابزار چند مرحله‌ای

```python
from openai import OpenAI
import json

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# تعریف ابزارها برای استفاده توسط مدل
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت اطلاعات آب و هوای فعلی",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "نام شهر"}
                },
                "required": ["location"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "web_search",
            "description": "جستجوی اطلاعات در وب",
            "parameters": {
                "type": "object",
                "properties": {
                    "query": {"type": "string", "description": "پرس‌وجوی جستجو"}
                },
                "required": ["query"],
            },
        },
    },
]

messages = [
    {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی با دسترسی به ابزارها برای جمع‌آوری اطلاعات.",
    },
    {
        "role": "user",
        "content": "آب و هوای توکیو چگونه است و اخبار اخیر درباره پیشرفت‌های هوش مصنوعی پیدا کنید؟",
    },
]

# مکالمه چند نوبتی با فراخوانی ابزار
max_iterations = 10
for iteration in range(max_iterations):
    response = client.chat.completions.create(
        model="kimi-k2-thinking",
        messages=messages,
        tools=tools,
        max_tokens=16000,
        temperature=1.0,
    )

    message = response.choices[0].message

    # نمایش استدلال در صورت وجود
    if hasattr(message, "reasoning_content"):
        reasoning = getattr(message, "reasoning_content")
        print(f"\\n=== استدلال (تکرار {iteration + 1}) ===")
        print(reasoning[:200] + "..." if len(reasoning) > 200 else reasoning)

    # اضافه کردن پیام دستیار به تاریخچه (حفظ reasoning_content)
    messages.append(message)

    # اگر فراخوانی ابزار نباشد، مکالمه کامل است
    if not message.tool_calls:
        print("\\n=== پاسخ نهایی ===")
        print(message.content)
        break

    # مدیریت فراخوانی ابزارها
    print(f"\\nمدل {len(message.tool_calls)} ابزار را فراخوانی کرد")
    for tool_call in message.tool_calls:
        func_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)

        print(f"  - {func_name}({args})")

        # شبیه‌سازی اجرای ابزار (با فراخوانی‌های واقعی ابزار جایگزین کنید)
        if func_name == "get_weather":
            result = f"آب و هوا در {args['location']}: آفتابی، ۲۲ درجه سانتیگراد"
        elif func_name == "web_search":
            result = f"نتایج جستجو برای '{args['query']}': [اخبار اخیر هوش مصنوعی...]"
        else:
            result = "ابزار یافت نشد"

        # اضافه کردن نتیجه ابزار به پیام‌ها
        messages.append(
            {
                "role": "tool",
                "tool_call_id": tool_call.id,
                "name": func_name,
                "content": result,
            }
        )
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2-thinking` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="آب و هوای توکیو چگونه است و اخبار اخیر درباره پیشرفت‌های هوش مصنوعی پیدا کنید؟",
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


---


## kimi-k2-0711-preview

**پیش‌نمایش مدل K2 نسل بعدی با عملکرد بهبود یافته**

انتشار پیش‌نمایش مدل نسل بعدی K2 از Moonshot که عملکرد و کارایی بهبود یافته نسبت به نسخه‌های قبلی را ارائه می‌دهد.

### ویژگی‌ها

- **پنجره زمینه**: 128K توکن
- **دمای توصیه شده**: 0.6
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری
- **عدم آموزش بر روی داده‌های مشتری**: متمرکز بر حریم خصوصی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $0.60 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $2.50 به ازای 1M توکن |

### موارد استفاده

- وظایف استدلال پیچیده
- مکالمات چند مرحله‌ای
- تحلیل و خلاصه‌سازی اسناد
- تولید محتوای فنی

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-k2-0711-preview",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "مفهوم کش کردن پرامپت را توضیح دهید."
      }
    ],
    "temperature": 0.6
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-k2-0711-preview",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            "role": "user",
            "content": "مفهوم کش کردن پرامپت را توضیح دهید.",
        },
    ],
    temperature=0.6,
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "kimi-k2-0711-preview",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
    },
    {
      role: "user",
      content: "مفهوم کش کردن پرامپت را توضیح دهید.",
    }
  ],
  temperature: 0.6,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-k2-0711-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="مفهوم کش کردن پرامپت را توضیح دهید.",
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
  input: "مفهوم کش کردن پرامپت را توضیح دهید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "مفهوم کش کردن پرامپت را توضیح دهید.",
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

## kimi-latest

**نام مستعار پایدار برای Kimi K3**

`kimi-latest` اکنون به `kimi-k3` اشاره می‌کند. ادغام‌های موجود می‌توانند بدون تغییر نام مدل از همین alias استفاده کنند و درخواست‌ها با قابلیت‌ها و قیمت Kimi K3 اجرا می‌شوند. برای استقرارهای قابل بازتولید، شناسه صریح `kimi-k3` را به‌کار ببرید.

### ویژگی‌ها

- **پنجره زمینه**: ۱ میلیون توکن
- **استدلال همیشه‌فعال**: پشتیبانی از `reasoning_effort: "max"`
- **نسخه‌سازی خودکار**: در حال حاضر به `kimi-k3` اشاره می‌کند
- **بینایی بومی**: پشتیبانی از درک چندوجهی تصویر
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $3.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.30 به ازای 1M توکن |
| توکن‌های خروجی | $15.00 به ازای 1M توکن |

### موارد استفاده

- مکالمات عمومی
- تولید و ویرایش محتوا
- کمک و اشکال‌زدایی کد
- پاسخ به سؤالات

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید."
      }
    ],
    "reasoning_effort": "max"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            "role": "user",
            "content": "یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید.",
        },
    ],
    reasoning_effort="max",
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "kimi-latest",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
    },
    {
      role: "user",
      content: "یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید.",
    }
  ],
  reasoning_effort: "max",
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API (پشتیبانی `kimi-latest` / Kimi K3 جزئی است)</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="kimi-latest",
    instructions="You are a helpful assistant.",
    input="یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "kimi-latest",
  instructions: "You are a helpful assistant.",
  input: "یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک تابع Python برای محاسبه اعداد فیبوناچی بنویسید.",
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

## kimi-thinking-preview

**مدل استدلال پیشرفته با قابلیت‌های زنجیره تفکر**

یک مدل استدلال تخصصی که استدلال زنجیره‌ای تفکر (CoT) را برای حل مسائل پیچیده چند مرحله‌ای و تحلیل اعمال می‌کند.

### ویژگی‌ها

- **مدل استدلال**: قابلیت‌های زنجیره تفکر (CoT)
- **پنجره زمینه**: 128K توکن
- **دمای توصیه شده**: 1.0
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **فرآیند تفکر قابل مشاهده**: نمایش استدلال گام به گام

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $30.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $30.00 به ازای 1M توکن |

### موارد استفاده

- حل مسائل پیچیده
- وظایف استدلال چند مرحله‌ای
- برنامه‌ریزی و تحلیل استراتژیک
- مسائل ریاضی و منطقی
- طراحی معماری سیستم

### مثال

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-thinking-preview",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید."
      }
    ],
    "temperature": 1.0,
    "max_tokens": 4096
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="kimi-thinking-preview",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {
            "role": "user",
            "content": "یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید.",
        },
    ],
    temperature=1.0,
    max_tokens=4096,
)

# مدل فرآیند استدلال زنجیره‌ای تفکر خود را نشان خواهد داد
print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "kimi-thinking-preview",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
    },
    {
      role: "user",
      content: "یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید.",
    }
  ],
  temperature: 1.0,
  max_tokens: 4096,
});

// مدل فرآیند استدلال زنجیره‌ای تفکر خود را نشان خواهد داد
console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-thinking-preview` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید.",
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
  input: "یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک طرح پایگاه داده مقیاس‌پذیر برای یک پلتفرم رسانه اجتماعی طراحی کنید.",
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

## moonshot-v1-8k

**مدل مقرون به صرفه برای مکالمات کوتاه‌تر**

یک مدل مقرون به صرفه با پنجره زمینه 8K، ایده‌آل برای مکالمات کوتاه‌تر و وظایف سریع.

### ویژگی‌ها

- **پنجره زمینه**: 8K توکن
- **دمای توصیه شده**: 0.6
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری
- **مقرون به صرفه**: قیمت‌گذاری پایین‌تر برای برنامه‌های هوشمند هزینه

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $0.20 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $2.00 به ازای 1M توکن |

### موارد استفاده

- سؤال و جواب سریع
- تولید محتوای کوتاه
- قطعه‌های کد ساده
- خلاصه‌های مختصر

---

## moonshot-v1-8k-vision-preview

**مدل با قابلیت بینایی برای وظایف چندوجهی**

یک مدل با زمینه 8K و قابلیت‌های بینایی که از درک تصویر از طریق تصاویر کدگذاری شده Base64 و URL‌ها پشتیبانی می‌کند.

### ویژگی‌ها

- **پنجره زمینه**: 8K توکن
- **دمای توصیه شده**: 0.6
- **قابلیت‌های بینایی**: پشتیبانی از تصاویر JPG، PNG، BMP
- **ورودی تصویر**: پشتیبانی از کدگذاری Base64 و URL
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $0.20 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $2.00 به ازای 1M توکن |

### موارد استفاده

- توضیح و تحلیل تصویر
- پاسخ به سؤالات بصری
- درک اسناد با تصاویر
- تحلیل تصاویر محصول

---

## moonshot-v1-32k

**مدل متعادل برای مکالمات با طول متوسط**

یک مدل متعادل با پنجره زمینه 32K، مناسب برای مکالمات با طول متوسط و پردازش اسناد.

### ویژگی‌ها

- **پنجره زمینه**: 32K توکن
- **دمای توصیه شده**: 0.6
- **فراخوانی ابزار**: ت
ا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری
- **عملکرد متعادل**: ترکیب خوبی از ظرفیت و هزینه

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $1.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $3.00 به ازای 1M توکن |

### موارد استفاده

- تحلیل اسناد با طول متوسط
- مکالمات چند مرحله‌ای
- بررسی و توضیح کد
- خلاصه‌سازی محتوا

---

## moonshot-v1-32k-vision-preview

**مدل با قابلیت بینایی و زمینه گسترده**

یک مدل با زمینه 32K و قابلیت‌های بینایی، مناسب برای وظایف چندوجهی که به زمینه بیشتری نیاز دارند.

### ویژگی‌ها

- **پنجره زمینه**: 32K توکن
- **دمای توصیه شده**: 0.6
- **قابلیت‌های بینایی**: پشتیبانی از تصاویر JPG، PNG، BMP
- **ورودی تصویر**: پشتیبانی از کدگذاری Base64 و URL
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $1.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $3.00 به ازای 1M توکن |

### موارد استفاده

- تحلیل بصری پیچیده با زمینه
- درک اسناد چند صفحه‌ای
- تولید محتوای بصری
- کمک تحقیقاتی مبتنی بر تصویر

---

## moonshot-v1-128k

**مدل با زمینه گسترده برای پردازش اسناد**

یک مدل با پنجره زمینه گسترده 128K، ایده‌آل برای پردازش اسناد طولانی و مکالمات گسترده.

### ویژگی‌ها

- **پنجره زمینه**: 128K توکن
- **دمای توصیه شده**: 0.6
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: صرفه‌جویی قابل توجه در اسناد بزرگ
- **ظرفیت گسترده**: مدیریت محتوا به طول کتاب

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $2.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $5.00 به ازای 1M توکن |

### موارد استفاده

- تحلیل و خلاصه‌سازی اسناد طولانی
- مقالات تحقیقاتی گسترده
- درک پایگاه کد
- پردازش محتوای به طول کتاب
- تاریخچه مکالمه گسترده

---

## moonshot-v1-128k-vision-preview

**مدل با قابلیت بینایی و حداکثر پنجره زمینه**

مدل بینایی پرچمدار با پنجره زمینه 128K که از وظایف چندوجهی پیچیده با زمینه گسترده پشتیبانی می‌کند.

### ویژگی‌ها

- **پنجره زمینه**: 128K توکن
- **دمای توصیه شده**: 0.6
- **قابلیت‌های بینایی**: پشتیبانی از تصاویر JPG، PNG، BMP
- **ورودی تصویر**: پشتیبانی از کدگذاری Base64 و URL
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **حداکثر ظرفیت**: بزرگترین زمینه برای وظایف بینایی

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $2.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $5.00 به ازای 1M توکن |

### موارد استفاده

- تحلیل اسناد بصری پیچیده
- درک چند تصویری
- تفسیر نمودارهای فنی
- تحقیق بصری با زمینه گسترده

---

## moonshot-v1-auto

**انتخاب خودکار مدل بر اساس ورودی**

یک مدل مسیریابی هوشمند که به طور خودکار بهترین مدل را بر اساس ورودی شما انتخاب می‌کند و عملکرد و هزینه را متعادل می‌سازد.

### ویژگی‌ها

- **پنجره زمینه**: تا 128K توکن (بسته به مدل انتخاب شده)
- **دمای توصیه شده**: 0.6
- **مسیریابی هوشمند**: به طور خودکار بهترین مدل را انتخاب می‌کند
- **فراخوانی ابزار**: تا ۱۲۸ تابع در هر درخواست
- **حالت JSON**: پشتیبانی از خروجی ساختاریافته
- **کش کردن پرامپت**: کاهش هزینه برای محتوای تکراری
- **بهینه‌سازی هزینه**: عملکرد و کارایی را متعادل می‌کند

### قیمت‌گذاری

| نوع | هزینه |
|------|------|
| توکن‌های ورودی | $2.00 به ازای 1M توکن |
| توکن‌های ورودی کش شده | $0.15 به ازای 1M توکن |
| توکن‌های خروجی | $5.00 به ازای 1M توکن |

**توجه**: قیمت‌گذاری حداکثر ظرفیت مدل را نشان می‌دهد. هزینه‌های واقعی ممکن است کمتر باشد اگر یک مدل کوچکتر به طور خودکار انتخاب شود.

### موارد استفاده

- مکالمات با طول متغیر
- انواع مختلف وظایف
- برنامه‌های نیازمند بهینه‌سازی هزینه
- کمک هوش مصنوعی همه‌منظوره

---

## ویژگی‌های پیشرفته

### فراخوانی تابع (استفاده از ابزار)

همه مدل‌های Moonshot.ai از فراخوانی تابع با حداکثر ۱۲۸ ابزار در هر درخواست پشتیبانی می‌کنند.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "آب و هوای پاریس چگونه است؟"
      }
    ],
    "tools": [
      {
        "type": "function",
        "function": {
          "name": "get_weather",
          "description": "دریافت آب و هوای فعلی برای یک مکان",
          "parameters": {
            "type": "object",
            "properties": {
              "location": {
                "type": "string",
                "description": "نام شهر"
              },
              "unit": {
                "type": "string",
                "enum": ["celsius", "fahrenheit"]
              }
            },
            "required": ["location"]
          }
        }
      }
    ],
    "temperature": 0.6
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "دریافت آب و هوای فعلی برای یک مکان",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {"type": "string", "description": "نام شهر"},
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]

response = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {"role": "user", "content": "آب و هوای پاریس چگونه است؟"},
    ],
    tools=tools,
    temperature=0.6,
)

print(response.choices[0].message)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const tools = [
  {
    type: "function",
    function: {
      name: "get_weather",
      description: "دریافت آب و هوای فعلی برای یک مکان",
      parameters: {
        type: "object",
        properties: {
          location: { type: "string", description: "نام شهر" },
          unit: { type: "string", enum: ["celsius", "fahrenheit"] },
        },
        required: ["location"],
      },
    },
  }
];

const response = await client.chat.completions.create({
  model: "kimi-latest",
  messages: [
    { role: "system", content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI." },
    { role: "user", content: "آب و هوای پاریس چگونه است؟" },
  ],
  tools: tools,
  temperature: 0.6,
});

console.log(response.choices[0].message);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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
    input="آب و هوای پاریس چگونه است؟",
    tools=tools,
)

for item in response.output:
    if item.type == "function_call":
        print(item.name, item.arguments)
print(response.output_text)

javascript=:import OpenAI from "openai";

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
  input: "آب و هوای پاریس چگونه است؟",
  tools,
});

for (const item of response.output) {
  if (item.type === "function_call") {
    console.log(item.name, item.arguments);
  }
}
console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "آب و هوای پاریس چگونه است؟",
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


### حالت JSON

خروجی JSON ساختاریافته را با تنظیم پارامتر `response_format` فعال کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید. اطلاعات کاربر را به صورت JSON استخراج کنید."
      },
      {
        "role": "user",
        "content": "نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم."
      }
    ],
    "response_format": {"type": "json_object"},
    "temperature": 0.6
  }'

python=:response = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید. اطلاعات کاربر را به صورت JSON استخراج کنید.",
        },
        {
            "role": "user",
            "content": "نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم.",
        },
    ],
    response_format={"type": "json_object"},
    temperature=0.6,
)

print(response.choices[0].message.content)

javascript=:const response = await client.chat.completions.create({
  model: "kimi-latest",
  messages: [
    {
      role: "system",
      content: "شما Kimi هستید. اطلاعات کاربر را به صورت JSON استخراج کنید.",
    },
    {
      role: "user",
      content: "نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم.",
    },
  ],
  response_format: { type: "json_object" },
  temperature: 0.6,
});

console.log(response.choices[0].message.content);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم.",
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
  input: "نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "نام من جان است، ۳۰ ساله هستم و در نیویورک زندگی می‌کنم.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پاسخ‌های جریانی

جریان را برای تولید توکن بلادرنگ فعال کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "kimi-latest",
    "messages": [
      {
        "role": "system",
        "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI."
      },
      {
        "role": "user",
        "content": "یک داستان کوتاه درباره هوش مصنوعی بنویسید."
      }
    ],
    "stream": true,
    "temperature": 0.6
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

stream = client.chat.completions.create(
    model="kimi-latest",
    messages=[
        {
            "role": "system",
            "content": "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI.",
        },
        {"role": "user", "content": "یک داستان کوتاه درباره هوش مصنوعی بنویسید."},
    ],
    stream=True,
    temperature=0.6,
)

for chunk in stream:
    if chunk.choices[0].delta.content is not None:
        print(chunk.choices[0].delta.content, end="")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const stream = await client.chat.completions.create({
  model: "kimi-latest",
  messages: [
    { role: "system", content: "شما Kimi هستید، یک دستیار هوش مصنوعی ارائه شده توسط Moonshot AI." },
    { role: "user", content: "یک داستان کوتاه درباره هوش مصنوعی بنویسید." },
  ],
  stream: true,
  temperature: 0.6,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `kimi-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
    input="یک داستان کوتاه درباره هوش مصنوعی بنویسید.",
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
  input: "یک داستان کوتاه درباره هوش مصنوعی بنویسید.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک داستان کوتاه درباره هوش مصنوعی بنویسید.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## بهترین شیوه‌ها

### انتخاب مدل مناسب

- **وظایف سریع**: از [`moonshot-v1-8k`](#moonshot-v1-8k) برای مکالمات کوتاه مقرون به صرفه استفاده کنید
- **استفاده عمومی**: از [`kimi-latest`](#kimi-latest) برای عملکرد متعادل و به‌روزرسانی‌های خودکار استفاده کنید
- **وظایف بینایی**: از مدل‌های vision-preview برای درک تصویر استفاده کنید
- **استدلال پیچیده**: از [`kimi-thinking-preview`](#kimi-thinking-preview) برای مسائل چند مرحله‌ای استفاده کنید
- **اسناد طولانی**: از مدل‌های 128K برای زمینه گسترده استفاده کنید
- **نیازهای انعطاف‌پذیر**: از [`moonshot-v1-auto`](#moonshot-v1-auto) برای بهینه‌سازی خودکار استفاده کنید

### تنظیمات دما

- **توصیه شده برای اکثر مدل‌ها**: 0.6
- **توصیه شده برای مدل‌های استدلال**: 1.0
- **مقادیر پایین‌تر (0.2-0.4)**: خروجی‌های قطعی‌تر و متمرکزتر
- **مقادیر بالاتر (0.8-1.0)**: خروجی‌های خلاقانه‌تر و متنوع‌تر

### بهینه‌سازی هزینه

- **از کش کردن پرامپت استفاده کنید**: هزینه‌ها را به طور قابل توجهی در محتوای تکراری کاهش می‌دهد
- **پنجره زمینه مناسب را انتخاب کنید**: اگر 8K کافی است از 128K استفاده نکنید
- **moonshot-v1-auto را در نظر بگیرید**: به طور خودکار هزینه و عملکرد را متعادل می‌کند
- **از قیمت‌گذاری ورودی کش شده بهره ببرید**: $0.15 به ازای 1M توکن در مقابل هزینه‌های ورودی استاندارد

## منابع مرتبط

- [راهنمای تولید متن](fa/guides/text-generation.md)
- [راهنمای قابلیت‌های بینایی](fa/guides/vision.md)
- [راهنمای فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
- [راهنمای کش کردن پرامپت](fa/guides/prompt-caching.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [اخبار: افزودن ارائه‌دهنده Moonshot.ai](fa/news/2025-11-10-moonshot-ai-alibaba-embeddings-added.md)
