---
title: "محدودیت نرخ API AvalAI، سطوح حساب و اعتبار رایگان ثبت‌نام"
description: "محدودیت نرخ و سطوح AvalAI را همراه با ۲۵٬۰۰۰ تومان اعتبار ثبت‌نام ایمیلی و مجموع ۲۰۰٬۰۰۰ تومان پس از تأیید تلفن بشناسید."
---

# محدودیت نرخ API AvalAI و سطوح حساب

این راهنما محدودیت‌های نرخ API AvalAI، سطوح حساب و نحوه دریافت تا **۲۰۰٬۰۰۰ تومان اعتبار رایگان ثبت‌نام** با تأیید شمارهٔ تلفن را توضیح می‌دهد.

## درک محدودیت‌های نرخ

محدودیت‌های نرخ، محدودیت‌هایی بر تعداد درخواست‌های API هستند که می‌توانید در یک دوره زمانی معین ارسال کنید. این محدودیت‌ها برای اطمینان از استفاده منصفانه از API و جلوگیری از سوء استفاده وضع شده‌اند. AvalAI محدودیت‌های نرخ را مشابه رویکرد OpenAI پیاده‌سازی می‌کند، با ارتقای خودکار سطح بر اساس استفاده شما.

## درک سطوح استفاده

AvalAI از یک سیستم سطح‌بندی استفاده می‌کند که در آن محدودیت‌های نرخ شما به‌صورت خودکار رشد می‌کنند — نخست با تأیید شمارهٔ تلفن و سپس از طریق شارژ تجمعی حساب. هیچ فرم درخواستی، دورهٔ انتظار یا تأیید دستی وجود ندارد: به‌محض اینکه شرایط یک سطح را برآورده کنید، محدودیت‌های جدید بلافاصله فعال می‌شوند.

### نحوه کار محدودیت‌های نرخ

محدودیت‌های نرخ به پنج روش اندازه‌گیری می‌شوند:
- **RPM** (درخواست در دقیقه)
- **RPD** (درخواست در روز)
- **TPM** (توکن در دقیقه)
- **TPD** (توکن در روز)
- **IPM** (تصویر در دقیقه)

شما می‌توانید به محدودیت‌های نرخ در هر یک از این معیارها برسید، بسته به اینکه کدام یک اول برسد. برای مثال، ممکن است ۲۰ درخواست با تنها ۱۰۰ توکن ارسال کنید و به محدودیت RPM خود برسید، حتی اگر به محدودیت TPM نرسیده باشید.

### شرایط سطوح

هر کاربری که در AvalAI ثبت‌نام کند بلافاصله می‌تواند از API استفاده کند. سطح شما بر اساس دو عامل تعیین می‌شود:

1. **روش تأیید حساب** — فقط با ایمیل، یا با شمارهٔ تلفن.
2. **مجموع شارژ تجمعی** — شارژها در طول عمر حسابتان روی هم انباشته می‌شوند.

| سطح | روش رسیدن به این سطح | اعتبار رایگان ثبت‌نام | محدودیت‌های نرخ |
|------|----------------------|-----------------------|-----------------|
| سطح پایه (Tier 0) | ثبت‌نام فقط با ایمیل | ۲۵٬۰۰۰ تومان | [محدودیت‌های نرخ سطح پایه](fa/rate-limits-tier0.md) را ببینید |
| سطح ۱ | ثبت‌نام با تلفن یا اتصال و تأیید آن در ادامه | در مجموع ۲۰۰٬۰۰۰ تومان | [محدودیت‌های نرخ سطح ۱](fa/rate-limits-tier1.md) را ببینید |
| سطح ۲ | مجموع شارژ معادل ۱۰ دلار | اعتبار ثبت‌نام تا زمان مصرف باقی می‌ماند | [محدودیت‌های نرخ سطح ۲](fa/rate-limits-tier2.md) را ببینید |
| سطح ۳ | مجموع شارژ معادل ۵۰ دلار | اعتبار ثبت‌نام تا زمان مصرف باقی می‌ماند | [محدودیت‌های نرخ سطح ۳](fa/rate-limits-tier3.md) را ببینید |
| سطح ۴ | مجموع شارژ معادل ۲۵۰ دلار | اعتبار ثبت‌نام تا زمان مصرف باقی می‌ماند | [محدودیت‌های نرخ سطح ۴](fa/rate-limits-tier4.md) را ببینید |
| سطح ۵ | مجموع شارژ معادل ۱٬۰۰۰ دلار | اعتبار ثبت‌نام تا زمان مصرف باقی می‌ماند | [محدودیت‌های نرخ سطح ۵](fa/rate-limits-tier5.md) را ببینید |

**نکات کاربردی:**

- 🎁 **با شمارهٔ تلفن ثبت‌نام و آن را تأیید کنید تا ۲۰۰٬۰۰۰ تومان اعتبار رایگان API بگیرید.** هیچ شارژی لازم نیست.
- ✉️ **می‌توانید با ایمیل شروع کنید.** ثبت‌نام فقط با ایمیل، بلافاصله **۲۵٬۰۰۰ تومان** اعتبار رایگان در سطح پایه ارائه می‌دهد.
- 📱 **بعدا تلفن را اضافه و تأیید کنید تا ۱۷۵٬۰۰۰ تومان دیگر بگیرید.** با این کار مجموع اعتبار رایگان حساب ایمیلی به همان **۲۰۰٬۰۰۰ تومان** می‌رسد و حساب فورا به سطح ۱ ارتقا می‌یابد. پاداش تلفن، مجموع را به ۲۰۰٬۰۰۰ تومان می‌رساند و ۲۰۰٬۰۰۰ تومان جداگانه علاوه بر اعتبار ایمیل نیست.
- ⚡ **ارتقای سطح، خودکار و آنی است** — به‌محض رسیدن به آستانهٔ بعدی، بدون نیاز به تیکت پشتیبانی یا انتظار، سطح شما ارتقا می‌یابد.
- 💳 **شارژها تجمعی محاسبه می‌شوند.** سطوح ۲ به بالا بر اساس مجموع شارژ تاریخی حساب شما تعیین می‌شوند، نه موجودی فعلی، و **هیچ اعتباری بابت ارتقا کسر نمی‌شود** — تمام اعتبار شما برای استفاده از API باقی می‌ماند.
- 💱 شارژها به ریال انجام می‌شوند و معادل دلاری آن برای تعیین سطح، بر اساس نرخ ارز نمایش‌داده‌شده در [chat.avalai.ir/platform](https://chat.avalai.ir/platform) محاسبه می‌شود. (اعتبار تومانی به‌صورت خودکار به تتر تبدیل نمی‌شود و فقط معادل آن برای محاسبهٔ سطح دسترسی بررسی می‌گردد. در صورت تمایل می‌توانید با کسر ۳٪ کارمزد، اعتبار تومانی خود را در [chat.avalai.ir/platform/billing/credit](https://chat.avalai.ir/platform/billing/credit) به معادل تتر تبدیل کنید.)
- 📈 **هیچ سقف هزینهٔ ماهانه‌ای وجود ندارد** — هر زمان نیاز داشتید می‌توانید از کل موجودی اعتبار خود استفاده کنید.
- 🤖 هر سطح دسترسی به مدل‌های بیشتر و محدودیت‌های نرخ بالاتر برای هر مدل فراهم می‌کند. محدودیت‌ها برای هر مدل و در سطح سازمان تعریف می‌شوند.

برای محدودیت‌های نرخ دقیق هر مدل در سطح خود، از صفحات مخصوص هر سطح که در بالا لینک شده‌اند دیدن کنید.

## محدودیت‌های نرخ API فایل‌ها

[API فایل‌ها](fa/api-reference/files.md) (`/v1/files`) محدودیت‌های نرخ جداگانه‌ای برای عملیات فایل دارد. این محدودیت‌ها بر اساس سطح است و در هر دقیقه اعمال می‌شود.

> **🎉 برنامه بتای رایگان**: تمام عملیات v1/files از **۱۱ دی ۱۴۰۴** تا **۱۰ اسفند ۱۴۰۴** (۶۰ روز) کاملا **رایگان** است. ما شما را تشویق می‌کنیم که تست کنید و هرگونه مشکل را به [t.me/AvalAISupport](https://t.me/AvalAISupport) گزارش دهید.

### محدودیت‌های نرخ عملیات فایل (در دقیقه)

| سطح | آپلود | دانلود | حذف |
|------|---------|-----------|---------|
| ۰ (رایگان) | ۳ | ۵ | ۱۰ |
| ۱ | ۱۰ | ۱۰۰ | ۱۰۰ |
| ۲ | ۵۰ | ۲۵۰ | ۲۵۰ |
| ۳ | ۲۵۰ | ۵۰۰ | ۵۰۰ |
| ۴ | ۵۰۰ | ۱٬۰۰۰ | ۱٬۰۰۰ |
| ۵ | ۱٬۵۰۰ | ۲٬۰۰۰ | ۵٬۰۰۰ |

### محدودیت‌های فضای ذخیره‌سازی بر اساس سطح

هر سطح یک محدودیت کل فضای ذخیره‌سازی دارد. پس از اتمام، آپلودها مسدود می‌شوند تا فضای ذخیره‌سازی را با حذف فایل‌ها آزاد کنید یا به سطح بالاتر ارتقا دهید.

| سطح | حداکثر فضا |
|------|-------------|
| ۰ (رایگان) | ۲۵۰ مگابایت |
| ۱ | ۲ گیگابایت |
| ۲ | ۵ گیگابایت |
| ۳ | ۱۵ گیگابایت |
| ۴ | ۵۰ گیگابایت |
| ۵ | ۲۰۰ گیگابایت |

**محدودیت اندازه فایل**: حداکثر اندازه آپلود **۱۲۸ مگابایت** برای هر فایل است (در طول بتا).

برای مستندات کامل API فایل‌ها شامل نقاط پایانی، مثال‌های کد و اهداف پشتیبانی شده فایل، به [مرجع API فایل‌ها](fa/api-reference/files.md) مراجعه کنید.

## هدرهای محدودیت نرخ

هنگامی که درخواست‌های API ارسال می‌کنید، هدرهای پاسخ شامل اطلاعاتی در مورد وضعیت فعلی محدودیت نرخ شما هستند:

| هدر | توضیحات |
|--------|-------------|
| `x-ratelimit-limit-requests` | حداکثر تعداد درخواست‌های مجاز در پنجره زمانی فعلی |
| `x-ratelimit-remaining-requests` | تعداد درخواست‌های باقی‌مانده در پنجره زمانی فعلی |
| `x-ratelimit-reset-requests` | زمانی که پنجره محدودیت نرخ فعلی بازنشانی می‌شود  |
| `x-ratelimit-limit-tokens` | حداکثر تعداد توکن‌های مجاز در پنجره زمانی فعلی |
| `x-ratelimit-remaining-tokens` | تعداد توکن‌های باقی‌مانده در پنجره زمانی فعلی |
| `x-ratelimit-reset-tokens` | زمانی که پنجره محدودیت نرخ توکن بازنشانی می‌شود  |

## ابعاد دیگر محدودیت که باید پایش کنید

APIهای سازگار با OpenAI می‌توانند هم‌زمان بیش از یک limiter را روی یک درخواست اعمال کنند. AvalAI محدودیت‌های منتشرشده سطح و هر مدل را در صفحات tier تولیدشده نشان می‌دهد، اما کلاینت production باید برای الگوهای زیر هم آماده باشد، هرجا route انتخابی آن‌ها را پشتیبانی کند:

- **دامنه سازمان و مدل:** محدودیت‌ها معمولا در سطح organization و مدل اعمال می‌شوند. اگر چند سرویس از یک کلید یا سازمان AvalAI استفاده کنند، همان ظرفیت را مشترک مصرف می‌کنند.
- **pool مشترک مدل‌ها:** aliasها یا variantهای نزدیک یک provider ممکن است از یک pool مشترک مصرف کنند. برای ظرفیت‌سنجی از model ID دقیق و صفحات tier استفاده کنید و فرض نکنید تغییر به مدل sibling سهمیه تازه می‌سازد.
- **درخواست‌های long-context:** promptهای بسیار بزرگ می‌توانند در providerهای upstream محدودیت کمتر یا جداگانه داشته باشند. کار را تقسیم کنید، history را compact کنید، یا به‌جای ارسال همان context بزرگ در هر turn از retrieval استفاده کنید.
- **محدودیت صف Batch:** پشتیبانی Batch API میزبانی‌شده در AvalAI در حال توسعه است، اما الگوی OpenAI توکن‌های ورودی queueشده را تا زمان تکمیل job برای همان مدل حساب می‌کند. برای workloadهای فعلی AvalAI، صف سمت کلاینت را هم بر اساس تعداد درخواست و هم تخمین تعداد توکن محدود کنید.
- **هدرهای project-token:** بعضی routeهای سازگار با OpenAI ممکن است هدرهایی مثل `x-ratelimit-limit-project-tokens` برگردانند. اگر این هدرها وجود داشتند، آن‌ها را جدا از هدرهای token سطح سازمان پایش کنید.
- **محدودیت‌های ingestion یا storage:** routeهای فایل، vector store، تصویر، صوت و ابزارهای میزبانی‌شده آینده می‌توانند محدودیت‌های مخصوص خودشان را داشته باشند. فقط به محدودیت token چت تکیه نکنید و مستندات endpoint مربوط را ببینید.
- **سقف محصولی برای هر کاربر:** برای اپلیکیشن‌های عمومی، سقف روزانه یا ماهانه داخلی و review دستی برای automation غیرعادی اضافه کنید. این کار از tier AvalAI شما در برابر یک account سوءاستفاده‌گر یا buggy محافظت می‌کند.

## مدیریت خطاهای محدودیت نرخ

هنگامی که از محدودیت نرخ فراتر می‌روید، API کد وضعیت 429 Too Many Requests را به همراه اطلاعاتی در مورد زمان تلاش مجدد برمی‌گرداند:

```json
{
  "error": {
    "message": "Rate limit exceeded for requests. Please try again in 30s.",
    "type": "rate_limit_error",
    "param": null,
    "code": "rate_limit_exceeded"
  }
}
```

پاسخ ممکن است شامل هدر `Retry-After` باشد که تعداد ثانیه‌هایی را که باید قبل از تلاش مجدد صبر کنید، نشان می‌دهد:

```
Retry-After: 30
```

## بهترین شیوه‌ها برای مدیریت محدودیت‌های نرخ

### پیاده‌سازی عقب‌نشینی نمایی (Exponential Backoff)

هنگامی که با خطای محدودیت نرخ مواجه می‌شوید، از عقب‌نشینی نمایی برای تلاش مجدد درخواست استفاده کنید. jitter تصادفی اضافه کنید تا همه کلاینت‌ها هم‌زمان retry نکنند، اگر `Retry-After` وجود دارد آن را رعایت کنید، و پس از سقف مشخصی از تلاش‌ها متوقف شوید چون درخواست‌های ناموفق هم از محدودیت دقیقه‌ای مصرف می‌کنند.

#### مثال پایتون

```language-selector
python=:import os
import time
import random
from openai import OpenAI, RateLimitError

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def make_request_with_backoff(func, max_retries=5, initial_delay=1, max_delay=60):
    """ارسال درخواست API با عقب‌نشینی نمایی برای خطاهای rate limit."""
    num_retries = 0
    delay = initial_delay

    while True:
        try:
            return func()
        except RateLimitError as e:
            if num_retries >= max_retries:
                raise

            retry_after = int(e.headers.get("retry-after", 0)) if e.headers else 0
            delay = max(retry_after, delay)

            sleep_time = delay + random.uniform(0, 0.5 * delay)
            print(f"Rate limit exceeded. Retrying in {sleep_time:.2f} seconds...")
            time.sleep(sleep_time)
            num_retries += 1
            delay = min(delay * 2, max_delay)


# مثال استفاده
def get_completion():
    return client.chat.completions.create(
        model="gpt-5.6-luna", messages=[{"role": "user", "content": "سلام!"}]
    )


try:
    response = make_request_with_backoff(get_completion)
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Failed after multiple retries: {e}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function makeRequestWithBackoff(
  func,
  maxRetries = 5,
  initialDelay = 1000,
  maxDelay = 60000,
) {
  let numRetries = 0;
  let delay = initialDelay;

  while (true) {
    try {
      return await func();
    } catch (error) {
      if (error.status !== 429 || numRetries >= maxRetries) {
        throw error;
      }

      // دریافت هدر retry-after در صورت وجود
      const retryAfter = error.headers?.["retry-after"]
        ? parseInt(error.headers["retry-after"]) * 1000
        : 0;
      delay = Math.max(retryAfter, delay);

      // عقب‌نشینی نمایی با لرزش (jitter)
      const jitter = Math.random() * 0.5 * delay;
      const sleepTime = delay + jitter;
      console.log(
        `Rate limit exceeded. Retrying in ${sleepTime / 1000} seconds...`,
      );
      await new Promise((resolve) => setTimeout(resolve, sleepTime));

      numRetries += 1;
      delay = Math.min(delay * 2, maxDelay);
    }
  }
}

// مثال استفاده
async function getCompletion() {
  return client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: "سلام!" }],
  });
}

async function main() {
  try {
    const response = await makeRequestWithBackoff(getCompletion);
    console.log(response.choices[0].message.content);
  } catch (error) {
    console.error(`Failed after multiple retries: ${error}`);
  }
}

main();

bash=:#!/bin/bash

# تابع ارسال درخواست با عقب‌نشینی نمایی برای خطاهای محدودیت نرخ
function make_request_with_backoff {
  local max_retries=5
  local initial_delay=1
  local max_delay=60
  local num_retries=0
  local delay=$initial_delay

  while true; do
    # ارسال درخواست API
    response=$(curl -s -w "%{http_code}" https://api.avalai.ir/v1/chat/completions \
      -H "Content-Type: application/json" \
      -H "Authorization: Bearer $AVALAI_API_KEY" \
      -d '{
    "model": "gpt-5.6-luna",
    "messages": [{"role": "user", "content": "سلام!"}]
  }')

    http_code=${response: -3}
    content=${response:0:${#response}-3}

    # بررسی پاسخ
    if [[ $http_code -eq 200 ]]; then
      echo "$content"
      return 0
    elif [[ $http_code -eq 429 ]]; then
      # خطای محدودیت نرخ
      retry_after=$(echo "$content" | grep -o '"retry_after":[0-9]*' | grep -o '[0-9]*')

      # اگر حداکثر تلاش‌ها انجام شده است، خروج با خطا
      if [[ $num_retries -ge $max_retries ]]; then
        echo "حداکثر تلاش‌های مجدد انجام شد: $content" >&2
        return 1
      fi

      # تنظیم تاخیر بر اساس هدر retry-after
      if [[ -n $retry_after ]]; then
        delay=$retry_after
      fi

      # عقب‌نشینی نمایی با لرزش (jitter)
      jitter=$(awk -v delay="$delay" 'BEGIN {srand(); print rand() * 0.5 * delay}')
      sleep_time=$(awk -v delay="$delay" -v jitter="$jitter" 'BEGIN {print delay + jitter}')

      echo "محدودیت نرخ فراتر رفت. تلاش مجدد در $sleep_time ثانیه..." >&2
      sleep $sleep_time

      num_retries=$((num_retries + 1))
      delay=$((delay < max_delay / 2 ? delay * 2 : max_delay))
    else
      # سایر خطاها
      echo "خطا: $http_code - $content" >&2
      return 1
    fi
  done
}

# استفاده از تابع
echo "ارسال درخواست به API..."
result=$(make_request_with_backoff)
status=$?

if [[ $status -eq 0 ]]; then
  echo "پاسخ دریافت شد:"
  echo "$result" | grep -o '"content":"[^"]*"' | cut -d'"' -f4
else
  echo "خطا در ارسال درخواست: $result"
fi

go=:package main

import (
	"context"
	"fmt"
	"math"
	"math/rand"
	"net/http"
	"os"
	"strconv"
	"time"

	"github.com/openai/openai-go"
)

// تابع ارسال درخواست با عقب‌نشینی نمایی برای خطاهای محدودیت نرخ
func makeRequestWithBackoff(ctx context.Context, fn func() (interface{}, error), maxRetries int, initialDelay, maxDelay time.Duration) (interface{}, error) {
	var numRetries int
	delay := initialDelay

	for {
		// ارسال درخواست API
		result, err := fn()
		if err == nil {
			return result, nil
		}

		// بررسی خطای محدودیت نرخ
		var retryAfter time.Duration
		var isRateLimitError bool

		if apiErr, ok := err.(*openai.APIError); ok {
			isRateLimitError = apiErr.HTTPStatusCode == http.StatusTooManyRequests

			// استخراج هدر retry-after
			if isRateLimitError && apiErr.Header != nil {
				if retryAfterStr := apiErr.Header.Get("retry-after"); retryAfterStr != "" {
					if retryAfterSec, err := strconv.Atoi(retryAfterStr); err == nil {
						retryAfter = time.Duration(retryAfterSec) * time.Second
					}
				}
			}
		}

		// اگر خطای محدودیت نرخ نیست یا به حداکثر تلاش‌ها رسیده‌ایم
		if !isRateLimitError || numRetries >= maxRetries {
			return nil, err
		}

		// استفاده از بیشترین مقدار بین تاخیر فعلی و retry-after
		if retryAfter > delay {
			delay = retryAfter
		}

		// عقب‌نشینی نمایی با لرزش (jitter)
		jitter := time.Duration(rand.Float64() * 0.5 * float64(delay))
		sleepTime := delay + jitter

		fmt.Fprintf(os.Stderr, "محدودیت نرخ فراتر رفت. تلاش مجدد در %v...\n", sleepTime)

		// انتظار قبل از تلاش مجدد
		select {
		case <-time.After(sleepTime):
		case <-ctx.Done():
			return nil, ctx.Err()
		}

		// افزایش شمارنده و تاخیر
		numRetries++
		delay = time.Duration(math.Min(float64(delay*2), float64(maxDelay)))
	}
}

func main() {
	// تنظیم کلاینت
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	// تعریف تابع ارسال درخواست
	getCompletion := func() (interface{}, error) {
		return client.CreateChatCompletion(
			context.Background(),
			openai.ChatCompletionRequest{
				model: "gpt-5.6-luna",
				Messages: []openai.ChatCompletionMessage{
					{
						Role:    "user",
						Content: "سلام!",
					},
				},
			},
		)
	}

	// ارسال درخواست با منطق تلاش مجدد
	ctx := context.Background()
	result, err := makeRequestWithBackoff(ctx, getCompletion, 5, 1*time.Second, 60*time.Second)

	if err != nil {
		fmt.Fprintf(os.Stderr, "خطا پس از چندین تلاش: %v\n", err)
		os.Exit(1)
	}

	// نمایش پاسخ
	if resp, ok := result.(openai.ChatCompletionResponse); ok {
		fmt.Println(resp.Choices[0].Message.Content)
	} else {
		fmt.Fprintf(os.Stderr, "نوع پاسخ نامعتبر\n")
	}
}

php=:<?php
require 'vendor/autoload.php';

/**
* تابع ارسال درخواست با عقب‌نشینی نمایی برای خطاهای محدودیت نرخ
*/
function makeRequestWithBackoff($func, $maxRetries = 5, $initialDelay = 1, $maxDelay = 60) {
  $numRetries = 0;
  $delay = $initialDelay;

  while (true) {
    try {
      return $func();
    } catch (\Exception $e) {
      // بررسی آیا خطای محدودیت نرخ است
      $isRateLimitError = false;
      $retryAfter = 0;

      if (method_exists($e, 'getResponse')) {
        $response = $e->getResponse();
        if ($response && $response->getStatusCode() === 429) {
          $isRateLimitError = true;
          $headers = $response->getHeaders();
          if (isset($headers['Retry-After'][0])) {
            $retryAfter = (int)$headers['Retry-After'][0];
          }
        }
      }

      // اگر خطای محدودیت نرخ نیست یا به حداکثر تلاش‌ها رسیده‌ایم
      if (!$isRateLimitError || $numRetries >= $maxRetries) {
        throw $e;
      }

      // تنظیم تاخیر بر اساس هدر retry-after
      if ($retryAfter > 0) {
        $delay = max($retryAfter, $delay);
      }

      // عقب‌نشینی نمایی با لرزش (jitter)
      $jitter = mt_rand() / mt_getrandmax() * 0.5 * $delay;
      $sleepTime = $delay + $jitter;

      echo "محدودیت نرخ فراتر رفت. تلاش مجدد در {$sleepTime} ثانیه...\n";
      sleep($sleepTime);

      $numRetries++;
      $delay = min($delay * 2, $maxDelay);
    }
  }
}

// تنظیم کلاینت
$apiKey = getenv('AVALAI_API_KEY');
$client = OpenAI::client($apiKey, [
'base_url' => 'https://api.avalai.ir/v1',
]);

// تعریف تابع ارسال درخواست
$getCompletion = function() use ($client) {
  return $client->chat()->create([
  'model' => 'gpt-5.6-luna',
  'messages' => [
  ['role' => 'user', 'content' => 'سلام!'],
  ],
  ]);
};

// استفاده از تابع با منطق تلاش مجدد
try {
  $response = makeRequestWithBackoff($getCompletion);
  echo $response->choices[0]->message->content . "\n";
} catch (\Exception $e) {
  echo "خطا پس از چندین تلاش: " . $e->getMessage() . "\n";
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
    input="سلام!",
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
  input: "سلام!",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "سلام!",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پیاده‌سازی محدودیت نرخ در سمت خودتان

به طور فعال نرخ درخواست خود را محدود کنید تا از برخورد به محدودیت‌های نرخ API جلوگیری کنید:

#### مثال پایتون با الگوریتم سطل توکن (Token Bucket)

```python
import time
import threading


class TokenBucket:
    """الگوریتم سطل توکن برای محدودیت نرخ."""

    def __init__(self, tokens_per_second, max_tokens):
        self.tokens_per_second = tokens_per_second
        self.max_tokens = max_tokens
        self.tokens = max_tokens
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def get_token(self, tokens=1):
        """دریافت توکن از سطل. در صورت موجود بودن توکن‌ها True و در غیر این صورت False برمی‌گرداند."""
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def _refill(self):
        """پر کردن مجدد سطل توکن بر اساس زمان سپری شده."""
        now = time.time()
        elapsed = now - self.last_refill_time
        new_tokens = elapsed * self.tokens_per_second
        if new_tokens > 0:
            self.tokens = min(self.tokens + new_tokens, self.max_tokens)
            self.last_refill_time = now

        # مثال استفاده
        # ایجاد یک محدود کننده نرخ با ۱۰ درخواست در ثانیه، حداکثر انفجار ۵۰
        rate_limiter = TokenBucket(10, 50)

    def make_api_request():
        if not rate_limiter.get_token():
            # توکن موجود نیست، باید صبر کرد
            print("Rate limit reached, waiting...")
            while not rate_limiter.get_token():
                time.sleep(0.1)

        # حالا یک توکن داریم، درخواست API را ارسال کنید
        try:
            response = client.chat.completions.create(
                model="gpt-5.6-luna", messages=[{"role": "user", "content": "سلام!"}]
            )
            return response
        except Exception as e:
            print(f"API request failed: {e}")
            return None
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


### در صورت امکان درخواست‌ها را دسته‌بندی کنید

برای عملیاتی مانند تعبیه‌سازی‌‌ها، چندین ورودی را در یک درخواست واحد دسته‌بندی کنید:

```python
# به جای ارسال ۱۰ درخواست جداگانه
texts = [
    "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد.",
    "پنج جادوگر بوکسور به سرعت می‌پرند.",
    # ... ۸ متن دیگر
]

# ارسال یک درخواست دسته‌ای واحد
response = client.embeddings.create(model="text-embedding-3-small", input=texts)

# پردازش همه تعبیه‌سازی‌‌ها به یکباره
embeddings = [item.embedding for item in response.data]
```

### نظارت بر استفاده خود

استفاده از API خود را برای جلوگیری از خطاهای غیرمنتظره محدودیت نرخ پیگیری کنید:

```python
def track_usage(response):
    """پیگیری استفاده از API از هدرهای پاسخ."""
    headers = response.headers

    # محدودیت‌های نرخ مبتنی بر درخواست
    requests_limit = int(headers.get("x-ratelimit-limit-requests", 0))
    requests_remaining = int(headers.get("x-ratelimit-remaining-requests", 0))
    requests_reset = int(headers.get("x-ratelimit-reset-requests", 0))

    # محدودیت‌های نرخ مبتنی بر توکن
    tokens_limit = int(headers.get("x-ratelimit-limit-tokens", 0))
    tokens_remaining = int(headers.get("x-ratelimit-remaining-tokens", 0))
    tokens_reset = int(headers.get("x-ratelimit-reset-tokens", 0))

    # محاسبه درصد استفاده
    requests_usage_pct = (
        100 - (requests_remaining / requests_limit * 100) if requests_limit else 0
    )
    tokens_usage_pct = (
        100 - (tokens_remaining / tokens_limit * 100) if tokens_limit else 0
    )

    print(
        f"Requests: {requests_remaining}/{requests_limit} ({requests_usage_pct:.1f}% used)"
    )
    print(f"Tokens: {tokens_remaining}/{tokens_limit} ({tokens_usage_pct:.1f}% used)")

    # هشدار در صورت بالا بودن استفاده
    if requests_usage_pct > 80 or tokens_usage_pct > 80:
        print("WARNING: API usage is high!")

    return {
        "requests": {
            "limit": requests_limit,
            "remaining": requests_remaining,
            "reset": requests_reset,
            "usage_pct": requests_usage_pct,
        },
        "tokens": {
            "limit": tokens_limit,
            "remaining": tokens_remaining,
            "reset": tokens_reset,
            "usage_pct": tokens_usage_pct,
        },
    }


# مثال استفاده
response = client.chat.completions.create(
    model="gpt-5.6-luna", messages=[{"role": "user", "content": "سلام!"}]
)

usage_stats = track_usage(response)
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


### پیاده‌سازی صف یا Token Bucket درخواست

برای برنامه‌های با حجم بالا، یک token bucket یا صف درخواست پیاده‌سازی کنید:

```python
import time
import threading


class TokenBucket:
    """الگوریتم token bucket برای محدودسازی نرخ."""

    def __init__(self, tokens_per_second, max_tokens):
        self.tokens_per_second = tokens_per_second
        self.max_tokens = max_tokens
        self.tokens = max_tokens
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def get_token(self, tokens=1):
        """اگر token کافی وجود دارد True برمی‌گرداند."""
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def _refill(self):
        """بر اساس زمان سپری‌شده tokenها را دوباره پر می‌کند."""
        now = time.time()
        elapsed = now - self.last_refill_time
        new_tokens = elapsed * self.tokens_per_second
        if new_tokens > 0:
            self.tokens = min(self.tokens + new_tokens, self.max_tokens)
            self.last_refill_time = now


def make_api_request(client):
    """ارسال درخواست API با محدودسازی نرخ."""
    if not rate_limiter.get_token():
        print("Rate limit reached, waiting...")
        while not rate_limiter.get_token():
            time.sleep(0.1)

    try:
        response = client.chat.completions.create(
            model="gpt-5.6-luna",
            messages=[{"role": "user", "content": "سلام!"}],
        )
        return response
    except Exception as e:
        print(f"API request failed: {e}")
        return None


# مثال استفاده: ۱۰ درخواست در ثانیه با burst حداکثر ۵۰
rate_limiter = TokenBucket(10, 50)
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


## استراتژی‌های محدودیت نرخ برای سناریوهای مختلف

### برنامه‌های تعاملی

برای برنامه‌های دارای تعامل کاربر:

1. **پیاده‌سازی throttling سمت کلاینت** برای جلوگیری از ارسال بیش از حد درخواست توسط کاربران
2. **نمایش نشانگرهای بارگذاری** برای ارائه بازخورد در طول فراخوانی‌های API
3. **کش کردن پاسخ‌ها** برای پرس‌وجوهای رایج برای کاهش فراخوانی‌های API

### پردازش دسته‌ای

!> ویژگی پیاده‌سازی نشده!
Batch API میزبانی‌شده در AvalAI در حال توسعه است. برای workloadهای دسته‌ای فعلی، از concurrency کنترل‌شده سمت کلاینت همراه با retry استفاده کنید.

برای برنامه‌های پردازش دسته‌ای:

1. **زمان‌بندی کارها در ساعات کم‌بار** برای جلوگیری از مشکلات محدودیت نرخ
2. **پردازش در دسته‌های کوچکتر** برای توزیع درخواست‌ها در طول زمان
3. **پیاده‌سازی منطق تلاش مجدد با افزایش تاخیر** بین دسته‌ها

برای الگوهای اقتباس‌شده از Cookbook و سازگار با AvalAI، [پردازش دسته‌ای](fa/guides/batch-processing.md) و [درخواست‌های موازی سازگار با Rate Limit](fa/examples/rate_limit_safe_parallel_requests.md) را ببینید.

### سیستم‌های با دسترسی‌پذیری بالا

برای سیستم‌هایی که نیاز به دسترسی‌پذیری بالا دارند:

1. **پیاده‌سازی چندین کلید API** با متعادل‌سازی بار
2. **تنظیم مکانیسم‌های جایگزین** برای زمانی که به محدودیت‌های نرخ می‌رسید
3. **حفظ بودجه توکن/درخواست** برای اطمینان از اولویت عملیات حیاتی

## ارتقا محدودیت‌های نرخ شما

اگر به‌طور مداوم به محدودیت‌های نرخ برخورد می‌کنید، سریع‌ترین راه‌ها برای افزایش ظرفیت شما این‌هاست:

1. **شمارهٔ تلفن خود را تأیید کنید** تا فورا از سطح پایه به سطح ۱ ارتقا یابید — بدون نیاز به هیچ شارژی.
2. **حساب خود را شارژ کنید** تا به سطح ۲ و سطوح بالاتر برسید. سطوح بر اساس شارژ تجمعی محاسبه می‌شوند، پس هر شارژی شما را به ارتقای بعدی نزدیک‌تر می‌کند.
3. **پیاده‌سازی خود را بهینه کنید** تا فراخوانی‌های غیرضروری API کاهش یابد (دسته‌بندی درخواست‌ها، کش‌کردن پاسخ‌ها و انتخاب اندازهٔ مدل مناسب همگی کمک می‌کنند).
4. **سطح فعلی و پیشرفت خود را** در هر زمان از داشبورد حساب کاربری خود بررسی کنید.

ارتقای سطح به‌محض عبور از آستانهٔ بعدی، به‌صورت خودکار و آنی انجام می‌شود — بدون تیکت پشتیبانی، بدون انتظار — و **تمام اعتبار شما پس از هر ارتقا برای استفاده از API باقی می‌ماند**.

## نتیجه‌گیری

مدیریت مؤثر محدودیت نرخ برای ساخت برنامه‌های قابل اعتماد با API AvalAI ضروری است. با پیاده‌سازی استراتژی‌های ذکر شده در این راهنما، می‌توانید اختلالات ناشی از محدودیت نرخ را به حداقل برسانید و تجربه روانی را برای کاربران خود تضمین کنید.

به یاد داشته باشید که محدودیت‌های نرخ ممکن است با تکامل API در طول زمان تغییر کنند. همیشه برای آخرین اطلاعات در مورد محدودیت‌های نرخ به به‌روزترین مستندات مراجعه کنید.
