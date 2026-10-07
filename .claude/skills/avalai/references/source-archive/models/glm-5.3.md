---
title: "API مدل GLM 5.3، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل GLM 5.3 در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_prompt_caching", "supports_reasoning", "supports_tool_choice"], "citations": [], "evidence": null, "external": {"canonicalSlug": "z-ai/glm-5.3-20260816", "contextLength": 1048576, "defaultParameters": {"temperature": 1, "top_p": 0.95}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 943717, "modelId": "z-ai/glm-5.3", "pricing": {"completion": "0.0000044", "input_cache_read": "0.00000026", "overrides": [], "prompt": "0.0000014"}, "reasoning": {"defaultEffort": "max", "defaultEnabled": true, "mandatory": true, "supportedEfforts": ["high", "low", "max"]}, "stale": false, "tokenizer": "Other", "url": "https://openrouter.ai/z-ai/glm-5.3"}, "faq": [{"answer": "برای دسترسی به API مدل GLM 5.3 یک کلید API در داشبورد AvalAI بسازید و شناسه `glm-5.3` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل GLM 5.3 در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل GLM 5.3 در AvalAI برای هر یک میلیون توکن ورودی $1.40 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.", "question": "هزینه API مدل GLM 5.3 در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل GLM 5.3 معادل $1.40 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل GLM 5.3 چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای GLM 5.3 برابر 991,000 توکن است.", "question": "پنجره زمینه مدل GLM 5.3 چقدر است؟"}, {"answer": "در سطح 5 مدل GLM 5.3 در AvalAI تا 1,500 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل GLM 5.3 در AvalAI چقدر است؟"}, {"answer": "مدل GLM 5.3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، انتخاب ابزار.", "question": "مدل GLM 5.3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل GLM 5.3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل GLM 5.3 در AvalAI چه سطحی لازم است؟"}], "id": "GLM 5.3", "owner": "zai", "provider": "zai", "sourceId": "glm-5.3", "specifications": {"inputCostPerToken": 1.4e-06, "maxInputTokens": 991000, "maxOutputTokens": 128000, "outputCostPerToken": 4.4e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Zai</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل GLM 5.3 در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">glm-5.3</code>
    <button type="button" data-copy-model-id="glm-5.3" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">GLM 5.3 یک مدل هوش مصنوعی از Zai است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=glm-5.3">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000014">$1.40 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>991,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>128,000 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-08-18</strong></div>
</div>

## استفاده از مدل هوش مصنوعی GLM 5.3

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "glm-5.3", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="glm-5.3",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "glm-5.3",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- کش کردن پرامپت
- استدلال
- انتخاب ابزار

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `frequency_penalty`
- `include_reasoning`
- `logit_bias`
- `logprobs`
- `max_tokens`
- `min_p`
- `parallel_tool_calls`
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

## محدودیت نرخ مدل GLM 5.3

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 25 | 10,000,000 |
| سطح 2 | 250 | 4,000,000 |
| سطح 3 | 500 | 8,000,000 |
| سطح 4 | 750 | 10,000,000 |
| سطح 5 | 1,500 | 30,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000014">$1.40 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000014">$1.40 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000014770">$1.48 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000044">$4.40 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000046420">$4.64 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>


<section class="model-benchmarks">
  <h2>عملکرد بنچمارک هم‌گروه</h2>
  <p>امتیازهای مستقل و دارای منبع؛ بدون امتیاز ترکیبی.</p>
  <article class="model-benchmark">
    <h3>شاخص عاملیت Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>53.1</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">53.1 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/z-ai/glm-5.3" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص کدنویسی Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>74.8</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">74.8 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/z-ai/glm-5.3" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص هوش Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>44.8</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">44.8 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/z-ai/glm-5.3" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
</section>

<OpenRouterLivePanel />


## مدل‌های مرتبط

- [GLM 5.3 Flash](/fa/models/glm-5.3-flash)
- [GLM 5.2](/fa/models/glm-5.2)
- [GLM 5.1](/fa/models/glm-5.1)

## پرسش‌های متداول

### چگونه به API مدل GLM 5.3 در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل GLM 5.3 یک کلید API در داشبورد AvalAI بسازید و شناسه `glm-5.3` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل GLM 5.3 در AvalAI چقدر است؟

API مدل GLM 5.3 در AvalAI برای هر یک میلیون توکن ورودی $1.40 و برای هر یک میلیون توکن خروجی $4.40 هزینه دارد.

### هزینه توکن مدل GLM 5.3 چقدر است؟

قیمت فعلی AvalAI برای مدل GLM 5.3 معادل $1.40 / 1M tokens برای ورودی و $4.40 / 1M tokens برای خروجی است.

### پنجره زمینه مدل GLM 5.3 چقدر است؟

حداکثر ورودی ثبت‌شده برای GLM 5.3 برابر 991,000 توکن است.

### محدودیت نرخ مدل GLM 5.3 در AvalAI چقدر است؟

در سطح 5 مدل GLM 5.3 در AvalAI تا 1,500 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل GLM 5.3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل GLM 5.3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، کش کردن پرامپت، استدلال، انتخاب ابزار.

### برای استفاده از مدل GLM 5.3 در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل GLM 5.3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/z-ai/glm-5.3) · آخرین بررسی: 2026-09-30
