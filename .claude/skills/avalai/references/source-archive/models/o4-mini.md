---
title: "API مدل o4 Mini، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل o4 Mini در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_pdf_input", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_tool_choice", "supports_vision", "supports_web_search"], "citations": [], "evidence": null, "external": {"canonicalSlug": "openai/o4-mini-2025-04-16", "contextLength": 200000, "defaultParameters": {}, "fetchedAt": "2026-07-31T06:13:12.364711Z", "instructionType": null, "maxCompletionTokens": 100000, "modelId": "openai/o4-mini", "pricing": {"completion": "0.0000044", "input_cache_read": "0.000000275", "overrides": [], "prompt": "0.0000011", "web_search": "0.01"}, "reasoning": {"defaultEffort": null, "defaultEnabled": null, "mandatory": false, "supportedEfforts": []}, "stale": true, "tokenizer": "GPT", "url": "https://openrouter.ai/openai/o4-mini"}, "faq": [{"answer": "برای دسترسی به API مدل o4 Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `o4-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل o4 Mini در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل o4 Mini در AvalAI برای هر یک میلیون توکن ورودی $1.10 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.", "question": "هزینه API مدل o4 Mini در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل o4 Mini معادل $1.10 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل o4 Mini چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای o4 Mini برابر 200,000 توکن است.", "question": "پنجره زمینه مدل o4 Mini چقدر است؟"}, {"answer": "در سطح 5 مدل o4 Mini در AvalAI تا 1,500 درخواست در دقیقه و 1,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل o4 Mini در AvalAI چقدر است؟"}, {"answer": "مدل o4 Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب.", "question": "مدل o4 Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل o4 Mini در AvalAI به سطح 1 یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل o4 Mini در AvalAI چه سطحی لازم است؟"}], "id": "o4 Mini", "owner": "openai", "provider": "openai", "sourceId": "o4-mini", "specifications": {"inputCostPerToken": 1.1e-06, "maxInputTokens": 200000, "maxOutputTokens": 100000, "outputCostPerToken": 4.4e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>OpenAI</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل o4 Mini در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">o4-mini</code>
    <button type="button" data-copy-model-id="o4-mini" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">o4 Mini یک مدل هوش مصنوعی از OpenAI است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=o4-mini">مقایسه مدل</a>
  </div>
</section>

<div class="model-price-scale" data-model-price-scale="million">
  <span class="model-price-scale__label">مقیاس نمایش قیمت</span>
  <div class="model-price-scale__options" role="group" aria-label="مقیاس نمایش قیمت">
    <button class="model-price-scale__button" type="button" data-price-scale-toggle="million" aria-pressed="true">هر ۱ میلیون توکن</button>
    <button class="model-price-scale__button" type="button" data-price-scale-toggle="thousand" aria-pressed="false">هر ۱ هزار توکن</button>
  </div>
</div>

<div class="model-fact-grid">
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000011">$1.10 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>200,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>100,000 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2025-04-16</strong></div>
<div class="model-fact"><span>پایان دانش</span><strong>2024-06-30</strong></div>
</div>

## استفاده از مدل هوش مصنوعی o4 Mini

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "o4-mini", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="o4-mini",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "o4-mini",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- ورودی PDF
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- انتخاب ابزار
- بینایی
- جست‌وجوی وب

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `include_reasoning`
- `max_tokens`
- `reasoning`
- `response_format`
- `seed`
- `structured_outputs`
- `tool_choice`
- `tools`

## محدودیت نرخ مدل o4 Mini

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح 1 | 100 | 450,000 |
| سطح 2 | 250 | 100,000 |
| سطح 3 | 500 | 200,000 |
| سطح 4 | 1,000 | 4,000,000 |
| سطح 5 | 1,500 | 1,000,000 |

<section class="model-price-compare">
  <h2>قیمت AvalAI و بازار مرجع</h2>
  <table class="model-price-compare__table">
    <thead>
      <tr>
        <th rowspan="2" scope="col">نقش توکن</th>
        <th class="model-price-compare__avalai-heading" rowspan="2" scope="col" dir="rtl"><span>قیمت نهایی AvalAI</span><small>کارمزد پلتفرم ۰٪</small></th>
        <th class="model-price-compare__source-heading" colspan="3" scope="colgroup" dir="rtl">جزئیات هزینه OpenRouter</th>
      </tr>
      <tr>
        <th scope="col" dir="rtl">نرخ مدل</th><th scope="col" dir="rtl">کارمزد خرید اعتبار</th><th scope="col" dir="rtl">هزینه مؤثر OpenRouter پس از کارمزد</th>
      </tr>
    </thead>
    <tbody>
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000011">$1.10 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000011">$1.10 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000011605">$1.16 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000046420">$4.64 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>



<OpenRouterLivePanel />


## مدل‌های مرتبط

- [o4-mini-2025-04-16](/fa/models/o4-mini-2025-04-16)
- [omni-moderation-latest](/fa/models/omni-moderation-latest)
- [omni-moderation-2024-09-26](/fa/models/omni-moderation-2024-09-26)
- [o3-pro-2025-06-10](/fa/models/o3-pro-2025-06-10)

## پرسش‌های متداول

### چگونه به API مدل o4 Mini در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل o4 Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `o4-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل o4 Mini در AvalAI چقدر است؟

API مدل o4 Mini در AvalAI برای هر یک میلیون توکن ورودی $1.10 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.

### هزینه توکن مدل o4 Mini چقدر است؟

قیمت فعلی AvalAI برای مدل o4 Mini معادل $1.10 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.

### پنجره زمینه مدل o4 Mini چقدر است؟

حداکثر ورودی ثبت‌شده برای o4 Mini برابر 200,000 توکن است.

### محدودیت نرخ مدل o4 Mini در AvalAI چقدر است؟

در سطح 5 مدل o4 Mini در AvalAI تا 1,500 درخواست در دقیقه و 1,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل o4 Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل o4 Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب.

### برای استفاده از مدل o4 Mini در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل o4 Mini در AvalAI به سطح 1 یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/openai/o4-mini) · آخرین بررسی: 2026-07-31
