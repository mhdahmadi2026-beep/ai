---
title: "API مدل Kimi Latest، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل Kimi Latest در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_tool_choice", "supports_vision"], "citations": [], "evidence": null, "external": {"canonicalSlug": "~moonshotai/kimi-latest", "contextLength": 1048576, "defaultParameters": {"frequency_penalty": null, "presence_penalty": null, "repetition_penalty": null, "temperature": null, "top_k": null, "top_p": 0.95}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 943718, "modelId": "~moonshotai/kimi-latest", "pricing": {"completion": "0.0000091343", "input_cache_read": "0.0000004", "overrides": [], "prompt": "0.0000003654"}, "reasoning": {"defaultEffort": "max", "defaultEnabled": true, "mandatory": false, "supportedEfforts": ["high", "low", "max"]}, "stale": false, "tokenizer": "Router", "url": "https://openrouter.ai/~moonshotai/kimi-latest"}, "faq": [{"answer": "برای دسترسی به API مدل Kimi Latest یک کلید API در داشبورد AvalAI بسازید و شناسه `openrouter/~moonshotai/kimi-latest` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل Kimi Latest در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل Kimi Latest در AvalAI برای هر یک میلیون توکن ورودی $3.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.", "question": "هزینه API مدل Kimi Latest در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل Kimi Latest معادل $3.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل Kimi Latest چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای Kimi Latest برابر 1,048,576 توکن است.", "question": "پنجره زمینه مدل Kimi Latest چقدر است؟"}, {"answer": "در سطح 5 مدل Kimi Latest در AvalAI تا 5,000 درخواست در دقیقه و 3,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل Kimi Latest در AvalAI چقدر است؟"}, {"answer": "مدل Kimi Latest در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی.", "question": "مدل Kimi Latest در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل Kimi Latest در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل Kimi Latest در AvalAI چه سطحی لازم است؟"}], "id": "Kimi Latest", "owner": "moonshot", "provider": "moonshot", "sourceId": "openrouter/~moonshotai/kimi-latest", "specifications": {"inputCostPerToken": 3e-06, "maxInputTokens": 1048576, "maxOutputTokens": 943718, "outputCostPerToken": 1.5e-05}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Moonshot</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل Kimi Latest در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">openrouter/~moonshotai/kimi-latest</code>
    <button type="button" data-copy-model-id="openrouter/~moonshotai/kimi-latest" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">Kimi Latest یک مدل هوش مصنوعی از Moonshot است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=kimi-latest">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.000003">$3.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.000015">$15.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>1,048,576 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>943,718 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-04-27</strong></div>
</div>

## استفاده از مدل هوش مصنوعی Kimi Latest

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "openrouter/~moonshotai/kimi-latest", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="openrouter/~moonshotai/kimi-latest",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "openrouter/~moonshotai/kimi-latest",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- انتخاب ابزار
- بینایی

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `frequency_penalty`
- `include_reasoning`
- `logit_bias`
- `logprobs`
- `max_tokens`
- `min_p`
- `presence_penalty`
- `reasoning`
- `reasoning_effort`
- `repetition_penalty`
- `response_format`
- `seed`
- `stop`
- `structured_outputs`
- `temperature`
- `tool_choice`
- `tools`
- `top_k`
- `top_logprobs`
- `top_p`

#### مقادیر تکمیلی تلاش استدلال

`high`, `low`, `max`

## محدودیت نرخ مدل Kimi Latest

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 50 | 200,000 |
| سطح 2 | 100 | 500,000 |
| سطح 3 | 250 | 1,000,000 |
| سطح 4 | 500 | 2,000,000 |
| سطح 5 | 5,000 | 3,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.000003">$3.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000003654">$0.37 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000003854970">$0.39 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.000015">$15.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000091343">$9.13 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000096366865">$9.64 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>



<OpenRouterLivePanel />


## مدل‌های مرتبط

- [Kimi K3](/fa/models/kimi-k3)
- [kimi-k2.7-code-highspeed](/fa/models/kimi-k2.7-code-highspeed)
- [Kimi K2.7 Code](/fa/models/kimi-k2.7-code)
- [Kimi K2.6](/fa/models/kimi-k2.6)

## پرسش‌های متداول

### چگونه به API مدل Kimi Latest در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل Kimi Latest یک کلید API در داشبورد AvalAI بسازید و شناسه `openrouter/~moonshotai/kimi-latest` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل Kimi Latest در AvalAI چقدر است؟

API مدل Kimi Latest در AvalAI برای هر یک میلیون توکن ورودی $3.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.

### هزینه توکن مدل Kimi Latest چقدر است؟

قیمت فعلی AvalAI برای مدل Kimi Latest معادل $3.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل Kimi Latest چقدر است؟

حداکثر ورودی ثبت‌شده برای Kimi Latest برابر 1,048,576 توکن است.

### محدودیت نرخ مدل Kimi Latest در AvalAI چقدر است؟

در سطح 5 مدل Kimi Latest در AvalAI تا 5,000 درخواست در دقیقه و 3,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل Kimi Latest در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل Kimi Latest در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی.

### برای استفاده از مدل Kimi Latest در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل Kimi Latest در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/~moonshotai/kimi-latest) · آخرین بررسی: 2026-09-30
