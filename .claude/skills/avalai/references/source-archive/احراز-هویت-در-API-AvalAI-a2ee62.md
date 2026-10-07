# احراز هویت در API AvalAI

این راهنما نحوه احراز هویت با API AvalAI را توضیح می‌دهد.

## کلیدهای API

تمام درخواست‌ها به API AvalAI باید شامل یک کلید API باشند. کلیدهای API شما در [داشبورد AvalAI](https://chat.avalai.ir/platform/home) در دسترس هستند.

!> **هشدار امنیتی**: کلیدهای API خود را ایمن نگه دارید! آن‌ها را در کد سمت کلاینت یا مخازن عمومی قرار ندهید. کلیدهای API باید فقط در کد سمت سرور استفاده شوند.

## روش‌های احراز هویت

### احراز هویت با توکن Bearer

روش توصیه شده برای احراز هویت با API AvalAI استفاده از احراز هویت توکن Bearer در هدر `Authorization` است:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
"model": "gpt-5.6-luna",
"messages": [{"role": "user", "content": "Hello!"}]
}'
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Hello!",
    "instructions": "You are a helpful assistant."
  }'
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### کتابخانه‌های کلاینت

هنگام استفاده از کتابخانه‌های کلاینت، می‌توانید کلید API و URL پایه را در هنگام راه‌اندازی کلاینت پیکربندی کنید:

#### پایتون (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)
```

#### جاوااسکریپت/تایپ‌اسکریپت (JavaScript/TypeScript)

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY, // استفاده از متغیرهای محیطی
  baseURL: "https://api.avalai.ir/v1",
});
```

#### گو (Go)

```go
package main

import (
	"os"

	openai "github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)
	_ = client
}
```

## بهترین شیوه‌های کلید API

1. **هرگز کلیدهای API خود را به اشتراک نگذارید**: با کلیدهای API مانند رمزهای عبور رفتار کنید.
2. **از متغیرهای محیطی استفاده کنید**: کلیدهای API را به جای کدنویسی مستقیم، در متغیرهای محیطی ذخیره کنید.
3. **کلیدهای API جداگانه ایجاد کنید**: از کلیدهای API مختلف برای محیط‌های توسعه، آزمایش و تولید استفاده کنید.
4. **مجوزهای کلید API را محدود کنید**: کلیدهایی با حداقل مجوزهای مورد نیاز ایجاد کنید.
5. **کلیدهای API را به طور منظم تغییر دهید**: برای امنیت بیشتر، کلیدهای API خود را به صورت دوره‌ای بازسازی کنید.
6. **استفاده از کلید API را نظارت کنید**: به طور منظم استفاده از API خود را برای فعالیت‌های غیرمجاز بررسی کنید.

## کنترل‌های دسترسی Enterprise

مستندات RBAC و Admin API در OpenAI یک الگوی طراحی مفید است: مدیریت سطح سازمان را از دسترسی runtime سطح project جدا کنید، permissionها را از طریق group یا service account بدهید، و پیش از rollout گسترده با یک حساب غیر owner دسترسی را verify کنید. AvalAI همان APIهای مدیریت سازمان OpenAI را منتشر نکرده است؛ بنابراین این الگو را به کنترل‌های موجود در داشبورد AvalAI و IAM برنامه خودتان نگاشت کنید.

برای deploymentهای production روی AvalAI:

- وقتی isolation مهم است، برای هر environment، service، tenant یا reseller کلید جداگانه صادر کنید؛
- credentialهای admin، billing، support و model-serving را از هم جدا نگه دارید؛
- وقتی محدودسازی کلید در دسترس است، فقط routeها و مدل‌های لازم همان workload را مجاز کنید؛
- در هر access review، کلیدهای استفاده‌نشده، userهای قدیمی و secretهای قدیمی CI را حذف کنید؛
- ایجاد، حذف، rotation، تغییر rate-limit و تغییر permission کلیدها را در audit trail برنامه خودتان ثبت کنید.

## مرزهای اتوماسیون Admin

Admin APIهای OpenAI از کلید Admin API جداگانه استفاده می‌کنند و برای endpointهای عادی مدل معتبر نیستند. AvalAI در حال حاضر Admin API سازگار را مستند نکرده است؛ بنابراین متغیرهای محیطی admin-key مخصوص OpenAI را برای AvalAI تنظیم نکنید، routeهای مدیریت سازمان OpenAI را از طریق AvalAI فراخوانی نکنید، و فرض نکنید helperهای admin در SDK رسمی OpenAI کلیدهای AvalAI را مدیریت می‌کنند.

اتوماسیون مدیریت AvalAI را فقط از طریق dashboard/APIهای مستند AvalAI انجام دهید. اگر به invite کاربر، automation چرخه عمر کلید، تغییر rate limit یا export لاگ audit نیاز دارید، آن را workflow مدیریت platform بدانید و پیش از نوشتن script، route پشتیبانی‌شده AvalAI را تأیید کنید.

## IP Allowlist و هویت شبکه

OpenAI برای محصولات مدیریت‌شده خودش، مانند ChatGPT integrations و Codex cloud، محدوده‌های IP خروجی منتشر می‌کند. این محدوده‌ها فقط traffic زیرساخت OpenAI را نشان می‌دهند، نه یک customer، workspace یا route مشخص AvalAI را. از IP rangeهای OpenAI برای احراز هویت traffic برنامه خودتان به AvalAI یا برای نمایش traffic providerهای AvalAI استفاده نکنید.

برای کنترل‌های شبکه:

- هر درخواست AvalAI را با `Authorization: Bearer $AVALAI_API_KEY` احراز هویت کنید؛
- در صورت امکان، خروجی serverها یا runnerهای CI خود را به `https://api.avalai.ir/v1` محدود کنید؛
- webhookها، ابزارها و callbackهای ورودی را با signature، OAuth، mTLS یا shared secret تأیید کنید، اگر سرویس بالادستی پشتیبانی می‌کند؛
- IP allowlistها را service-specific نگه دارید و وقتی provider rangeهای متغیر منتشر می‌کند، آن‌ها را خودکار refresh کنید.

## برنامه‌ریزی برای Server و Workload Identity

مستندات enterprise احراز هویت OpenAI الگوی workload identity federation را توضیح می‌دهد؛ در این الگو workloadهای قابل اعتماد cloud توکن‌های OIDC را با access token کوتاه‌عمر API عوض می‌کنند و نیازی به نگه‌داری کلید API بلندمدت ندارند. AvalAI در حال حاضر endpoint تبادل workload identity منتشر نکرده است، بنابراین این بخش را الگوی معماری بدانید، نه قابلیت فعلی AvalAI.

برای برنامه‌های production روی AvalAI امروز:

- `AVALAI_API_KEY` را فقط در secret store سمت server مثل secret manager cloud یا vault محرمانه CI نگه دارید،
- برای browser یا mobile از backend خودتان session token کوتاه‌عمر صادر کنید،
- وقتی isolation مهم است، برای هر service، environment و tenant کلید AvalAI جداگانه داشته باشید،
- `avalai-request-id`، endpoint، model و `safety_identifier` hashشده را log کنید تا requestها بدون افشای PII خام قابل audit باشند،
- اگر deployment، دستگاه کارمند، runner CI یا secret مخزن احتمالا لو رفته، کلیدها را فورا rotate کنید.

اگر AvalAI بعدا workload identity را اضافه کند، انتظار داشته باشید issuer قابل اعتماد را پیکربندی کنید، claimهای workload را به service account یا محدوده API key match کنید، حداقل permission لازم را بدهید، و خطاهای token exchange را جدا از خطاهای عادی API monitor کنید.

## شناسه‌های سازمانی

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

تا زمانی که routing سازمانی فعال نشده است، هدر سازمانی یا گزینه `organization` در SDK ارسال نکنید. برای جداسازی ترافیک و billing از کلیدهای API جداگانه، محیط‌های جدا، پروژه‌ها یا metadata فروشنده/کاربر در برنامه خودتان استفاده کنید.

## محدودیت نرخ

درخواست‌های API مشمول محدودیت نرخ هستند. هنگامی که از محدودیت‌های نرخ خود فراتر می‌روید، پاسخ 429 Too Many Requests دریافت خواهید کرد. برای اطلاعات بیشتر، به مستندات [محدودیت‌های نرخ](fa/guides/rate-limits.md) مراجعه کنید.

## مدیریت کلید API

می‌توانید کلیدهای API خود را در [داشبورد AvalAI](https://chat.avalai.ir/platform/home) مدیریت کنید:

1. ایجاد کلیدهای API جدید
2. حذف کلیدهای API موجود
3. مشاهده آمار استفاده از کلید API
4. تنظیم مجوزها و محدودیت‌ها برای کلیدهای API

## عیب‌یابی مشکلات احراز هویت

اگر با مشکلات احراز هویت مواجه هستید:

1. تایید کنید که از کلید API صحیح استفاده می‌کنید
2. بررسی کنید که کلید API فعال است و منقضی نشده است
3. اطمینان حاصل کنید که از روش احراز هویت صحیح استفاده می‌کنید
4. تایید کنید که کلید API مجوزهای لازم را دارد
5. محدودیت‌های نرخ خود را بررسی کنید تا مطمئن شوید از آن‌ها فراتر نرفته‌اید

اگر همچنان با مشکل مواجه هستید، با [پشتیبانی AvalAI](https://avalai.ir/contact-us-avalai) تماس بگیرید.
