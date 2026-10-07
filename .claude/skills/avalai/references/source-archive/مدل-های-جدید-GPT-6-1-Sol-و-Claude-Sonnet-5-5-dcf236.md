---
hasH1: true
published: "2026-09-30"
description: "GPT-6.1 Sol و Claude Sonnet 5.5 در AvalAI در دسترس‌اند. پشتیبانی نقاط پایانی، قیمت توکن‌ها، کنترل استدلال و نکات مهاجرت را مقایسه کنید."
---

# مدل‌های جدید: GPT-6.1 Sol و Claude Sonnet 5.5

**تاریخ:** ۱۴۰۵-۰۷-۰۸ / (2026-09-30)

## خلاصه

GPT-6.1 Sol و Claude Sonnet 5.5 اکنون از سطح ۱ در AvalAI در دسترس‌اند. هر دو از Chat Completions و Messages به‌طور کامل پشتیبانی می‌کنند؛ پشتیبانی Responses برای GPT-6.1 Sol کامل و برای Sonnet 5.5 جزئی است. قیمت‌ها و نکات مهاجرت در ادامه آمده‌اند.

## جزئیات

### OpenAI: GPT-6.1 Sol

برای کدنویسی، تحلیل سند و کارهای حرفه‌ای که به استدلال با قیمت توکن کمتر از GPT-6 Astra نیاز دارند، از **`gpt-6.1-sol`** استفاده کنید.

- **محدودیت‌ها:** حداکثر ۹۲۲٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی؛ این‌ها سقف‌های جداگانه فهرست هستند و جمع آن‌ها ظرفیت تضمین‌شده درخواست نیست.
- **قابلیت‌ها:** ورودی متن و تصویر، خروجی متن، استدلال، ورودی PDF، فراخوانی تابع، خروجی ساختاریافته و حافظه نهان پرامپت. درک تصویر به معنای توانایی تولید تصویر نیست.
- **بهبودهای گزارش‌شده از سوی ارائه‌دهنده:** کدنویسی و کار با اسناد حرفه‌ای بهتر از GPT-6 Sol، بهبود ارزیابی‌های استفاده از رایانه و علوم، و خطاهای واقعیت‌محور کمتر در پرامپت‌های آزمایشی دشوار. OpenAI از عملکرد هم‌سطح Astra در DeepSWE v1.1 با حدود یک‌پنجم هزینه هر کار خبر می‌دهد؛ این نتیجه ارزیابی بالادستی است، نه تضمین AvalAI درباره تأخیر، هزینه هر کار یا امتیاز معیار.
- **خواندن حافظه نهان:** در بازه استاندارد، $0.10 به ازای هر میلیون توکن؛ ۹۵ درصد کمتر از نرخ ورودی استاندارد و نصف نرخ خواندن حافظه نهان GPT-6 Sol. قیمت ورودی و خروجی در همین بازه $2.00 و $10.00 است.
- **استدلال:** با درخواست ساده زیر شروع کنید. در Chat Completions از `reasoning_effort` و در Responses از `reasoning.effort` فقط با مقدارهایی استفاده کنید که برای مسیر شما تأیید شده‌اند؛ فراداده محلی مدل از `none` و `minimal` پشتیبانی نمی‌کند. مقدار پیش‌فرض تلاش مدل‌های قدیمی GPT را به این مدل تعمیم ندهید.

### Anthropic: Claude Sonnet 5.5

برای کارهای کدنویسی با دامنه مشخص، رفع اشکال، تهیه سند، صفحه گسترده، اسلاید و طراحی مشارکتی، از **`claude-sonnet-5-5`** استفاده کنید. این مدل مکمل Opus 5.5 است و برای پیچیده‌ترین کارهای باز، جایگزین آن محسوب نمی‌شود.

- **محدودیت‌ها:** حداکثر ۱٬۰۰۰٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی؛ برای استدلال و پاسخ نهایی فضای کافی در خروجی بگذارید.
- **قابلیت‌ها:** استدلال، درک تصویر و PDF، ابزارها، خروجی ساختاریافته و حافظه نهان پرامپت.
- **کارایی گزارش‌شده از سوی ارائه‌دهنده:** Anthropic از تولید خروجی بیش از ۳۰ درصد سریع‌تر و کاهش هزینه هر کار تا ۳۰ درصد نسبت به Sonnet 5، به‌دلیل مصرف توکن کمتر، خبر می‌دهد. این اعداد به نوع کار وابسته‌اند و حاصل اندازه‌گیری بالادستی هستند، نه تضمین سرویس AvalAI.
- **پیش‌فرض تلاش در محصولات متفاوت است:** Anthropic برای برنامه‌های Claude و Claude Code مقدار `medium` و برای Claude Platform مقدار `high` را مستند کرده است. پیش‌فرض API مدل Opus 5.5 را کپی نکنید. اگر رفتار قابل پیش‌بینی مهم است، سطح تلاش پشتیبانی‌شده را صریح انتخاب کنید.
- **مهاجرت از تفکر غیرفعال:** برنامه‌هایی که قبلاً تفکر را غیرفعال می‌کردند، باید پیش از ارتقا به تنظیم جدید `between_tools` منتقل شوند. این تنظیم تفکر ابتدای کار را غیرفعال نگه می‌دارد، نه همه تفکر را. [راهنمای مهاجرت Sonnet 5.5](https://platform.claude.com/docs/en/models/sonnet-5-5/migration-guide#turn-thinking-off) را دنبال کنید و به‌جای کپی بدنه قدیمیِ غیرفعال‌کردن تفکر، پشتیبانی تنظیم را در مسیر AvalAI خود بررسی کنید.
- **تفکر حفظ‌شده:** حفظ تفکر وابسته به حساب گسترش یافته است. بلوک‌های امضاشده تفکر و نوبت‌های کامل دستیار و ابزار را دست‌نخورده نگه دارید؛ پیش از انتقال گفت‌وگوها میان حساب‌ها، الزامات مهاجرت را بررسی کنید. [راهنمای حفظ تفکر Anthropic](https://platform.claude.com/docs/en/build-with-claude/preserved-thinking) را ببینید.
- **محدودیت‌های درخواست:** کنترل‌های نمونه‌گیری پشتیبانی‌نشده مانند `temperature` و `top_p`، پیش‌پرکردن پاسخ دستیار یا اجبار به استفاده از ابزار را ارسال نکنید. به‌جای کپی مقدار ثابت `budget_tokens`، تفکر تطبیقی را انتخاب کنید.

### پشتیبانی نقاط پایانی

| شناسه مدل | `v1/chat/completions` | `v1/messages` | `v1/responses` |
| --- | --- | --- | --- |
| `gpt-6.1-sol` | کامل | کامل | کامل |
| `claude-sonnet-5-5` | کامل | کامل | **جزئی** |

پشتیبانی جزئی Responses به معنای برابری کامل ابزارهای میزبانی‌شده، وضعیت ذخیره‌شده یا گردش‌کارهای پس‌زمینه نیست. برای کنترل‌های اختصاصی تفکر Sonnet و بلوک‌های گفت‌وگو، Messages را ترجیح دهید و قابلیت‌های موردنیاز خود را آزمایش کنید. در دسترس بودن نقطه پایانی به‌تنهایی دسترسی به Batch، Flex، Priority، Fast mode، ابزارهای استفاده از رایانه یا دیگر ابزارهای میزبانی‌شده ارائه‌دهنده را تأیید نمی‌کند. این اعلامیه شناسه مدل‌های موجود را به‌طور خودکار جایگزین نمی‌کند.

## قیمت‌گذاری

همه قیمت‌ها **به دلار آمریکا برای هر ۱ میلیون توکن** هستند و تعرفه AvalAI را نشان می‌دهند؛ از قیمت‌ها، زمان نگهداری حافظه نهان بالادستی را استنتاج نکنید.

### GPT-6.1 Sol

| طول کل ورودی درخواست | ورودی | ورودی کش‌شده | ورودی ایجاد کش | خروجی |
| --- | ---: | ---: | ---: | ---: |
| تا 272K توکن، شامل خود این مقدار | $2.00 | $0.10 | $2.50 | $10.00 |
| بیش از 272K توکن | $4.00 | $0.20 | $5.00 | $15.00 |

ورودی دقیقاً ۲۷۲ هزار توکنی در بازه پایین‌تر باقی می‌ماند. طول کل ورودی درخواست، بازه تعرفه را تعیین می‌کند و نرخ خروجی نیز از همین بازه پیروی می‌کند؛ نرخ بالاتر فقط روی توکن‌های مازاد بر ۲۷۲ هزار اعمال نمی‌شود.

### Claude Sonnet 5.5

| ورودی | ورودی کش‌شده | ورودی ایجاد کش | خروجی |
| ---: | ---: | ---: | ---: |
| $2.00 | $0.20 | $4.00 | $10.00 |

قیمت ایجاد حافظه نهان در AvalAI **$4.00** است، نه قیمت بالادستی $2.50 که در اعلامیه ارائه‌دهنده آمده است. از این نرخ، زمان نگهداری پنج‌دقیقه‌ای یا یک‌ساعته را نتیجه نگیرید. برای این مدل بازه قیمت جداگانه‌ای برای زمینه طولانی ثبت نشده است. محدودیت توان عملیاتی هر سطح حساب را در [فهرست قیمت‌گذاری](fa/pricing.md) ببینید.

## درخواست Chat Completions و مثال‌های SDK

کلید `AVALAI_API_KEY` را در محیط خود قرار دهید. برای هر دو مدل از همان پرامپت و ساختار درخواست استفاده کنید؛ هنگام ارزیابی Sonnet فقط شناسه مدل را تغییر دهید. در مثال‌ها عمداً کنترل نمونه‌گیری و تلاش استدلالی ارسال نشده است.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-6.1-sol",
    "messages": [{"role": "user", "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag."}]
  }'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
for model in ("gpt-6.1-sol", "claude-sonnet-5-5"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag.",
            }
        ],
    )
    print(model, response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
for (const model of ["gpt-6.1-sol", "claude-sonnet-5-5"]) {
  const response = await client.chat.completions.create({
    model,
    messages: [{ role: "user", content: "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag." }],
  });
  console.log(model, response.choices[0].message.content);
}

```

### پاسخ‌های آموزشی

این‌ها **نمونه آموزشی** هستند، نه پاسخ ثبت‌شده از API زنده. هر نمونه ۱۰۰ توکن ورودی بدون حافظه نهان و ۵۰ توکن خروجی قابل‌صورتحساب دارد؛ ابزاری استفاده نشده و نرخ تبدیل نمونه ۱۰۰٬۰۰۰ تومان به ازای هر دلار است. مصرف واقعی توکن، جزئیات توکن‌های استدلال، شناسه‌ها و نرخ تبدیل حساب متفاوت خواهند بود. هزینه نمونه برابر است با `(100 × $2 + 50 × $10) / 1,000,000 = $0.0007`، یعنی ۷۰ تومان با همین نرخ تبدیل نمونه.

```json
{
  "id": "chatcmpl-gpt-6-1-sol-example",
  "created": 1790726400,
  "object": "chat.completion",
  "model": "gpt-6.1-sol",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "Test both flag states, verify authentication and error handling, monitor the limited rollout, and confirm rollback restores the previous behavior."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 50,
    "total_tokens": 150,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "estimated_cost": {
    "unit": "0.0007000000",
    "irt": 70,
    "exchange_rate": 100000
  }
}
```

```json
{
  "id": "chatcmpl-claude-sonnet-5-5-example",
  "created": 1790726400,
  "object": "chat.completion",
  "model": "claude-sonnet-5-5",
  "choices": [
    {
      "index": 0,
      "finish_reason": "stop",
      "message": {
        "role": "assistant",
        "content": "Test both flag states, verify authentication and error handling, monitor the limited rollout, and confirm rollback restores the previous behavior."
      }
    }
  ],
  "usage": {
    "prompt_tokens": 100,
    "completion_tokens": 50,
    "total_tokens": 150,
    "prompt_tokens_details": {
      "cached_tokens": 0
    }
  },
  "estimated_cost": {
    "unit": "0.0007000000",
    "irt": 70,
    "exchange_rate": 100000
  }
}
```

## GPT-6.1 Sol با Responses

این درخواست ساده و بدون وضعیت ذخیره‌شده از نقطه پایانی کامل Responses برای GPT-6.1 Sol استفاده می‌کند. قابلیت‌های اضافی ابزار میزبانی‌شده یا وضعیت ذخیره‌شده را جداگانه آزمایش کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"gpt-6.1-sol","input":"Give a concise verification checklist for a feature-flagged API release."}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
response = client.responses.create(
    model="gpt-6.1-sol",
    input="Give a concise verification checklist for a feature-flagged API release.",
)
print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const response = await client.responses.create({
  model: "gpt-6.1-sol",
  input: "Give a concise verification checklist for a feature-flagged API release.",
});
console.log(response.output_text);

```

## Claude Sonnet 5.5 با SDK بومی Anthropic

در SDK Anthropic، آدرس پایه باید **فقط نشانی میزبان** باشد و به `/v1` ختم نشود. این مثال صریحاً تفکر تطبیقی و تلاش `high` را درخواست می‌کند؛ بدنه مهاجرت `between_tools` نیست. برای کارهای دشوارتر بودجه خروجی را افزایش دهید و برای نوبت‌های بعدی ابزار، محتوای کامل پاسخ را حفظ کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "x-api-key: $AVALAI_API_KEY" \
  -H "anthropic-version: 2023-06-01" \
  -H "Content-Type: application/json" \
  -d '{
    "model":"claude-sonnet-5-5",
    "max_tokens":4096,
    "thinking":{"type":"adaptive"},
    "output_config":{"effort":"high"},
    "messages":[{"role":"user","content":"Review this release plan and give a concise verification checklist: deploy an API behind a feature flag."}]
  }'

python=:import os
from anthropic import Anthropic

client = Anthropic(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir"
)
response = client.messages.create(
    model="claude-sonnet-5-5",
    max_tokens=4096,
    thinking={"type": "adaptive"},
    output_config={"effort": "high"},
    messages=[
        {
            "role": "user",
            "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag.",
        }
    ],
)
for block in response.content:
    if block.type == "text":
        print(block.text)

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir" });
const response = await client.messages.create({
  model: "claude-sonnet-5-5",
  max_tokens: 4096,
  thinking: { type: "adaptive" },
  output_config: { effort: "high" },
  messages: [{ role: "user", content: "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag." }],
});
for (const block of response.content) {
  if (block.type === "text") console.log(block.text);
}

```

## چک‌لیست یکپارچه‌سازی

۱. شناسه صریح مدل را انتخاب کنید و دسترسی سطح ۱ را بررسی کنید؛ این اعلامیه نام مستعار یا هدایت خودکار ایجاد نمی‌کند.
۲. پیش از تغییر ترافیک محیط تولید، کیفیت خروجی، چرخه ابزار، اسکیما، تأخیر و مصرف توکن را با کارهای خود دوباره آزمایش کنید.
۳. کنترل‌های قدیمی پشتیبانی‌نشده را حذف کنید. برای گردش‌کارهای Sonnet با تفکر غیرفعال، مهاجرت `between_tools` و الزامات حفظ تفکر وابسته به حساب را دنبال کنید.
۴. زمینه کامل دستیار و ابزار را حفظ کنید، برای استدلال فضای کافی در خروجی قابل‌صورتحساب بگذارید و به‌جای زنجیره تفکر پنهان، نتیجه یا دلیل کوتاه بخواهید.
۵. میزان استفاده از حافظه نهان و هزینه واقعی صورتحساب را پایش کنید؛ آستانه ۲۷۲ هزار توکنی GPT-6.1 Sol و نرخ ایجاد حافظه نهان Sonnet در AvalAI بر برآورد اثر می‌گذارند.

## مستندات مرتبط

- [مدل‌های OpenAI](fa/providers/openai.md#gpt-6-1-sol) و [مرجع GPT-6.1 Sol](fa/models/gpt-6.1-sol.md)
- [مدل‌های Anthropic](fa/providers/anthropic.md#claude-sonnet-5-5) و [مرجع Sonnet 5.5](fa/models/claude-sonnet-5-5.md)
- [Chat Completions](fa/api-reference/chat.md)، [Messages](fa/api-reference/messages.md) و [Responses](fa/api-reference/responses.md)
- [راهنمای استدلال](fa/guides/reasoning.md) و [قیمت‌گذاری](fa/pricing.md)
