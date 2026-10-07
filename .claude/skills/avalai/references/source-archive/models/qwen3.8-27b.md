---
title: "API مدل Qwen3.8 27B، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل Qwen3.8 27B در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_prompt_caching", "supports_vision"], "citations": [], "evidence": null, "external": {"canonicalSlug": "qwen/qwen3.8-27b-20260814", "contextLength": 1000000, "defaultParameters": {"temperature": 1, "top_k": 20, "top_p": 0.95}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 131072, "modelId": "qwen/qwen3.8-27b", "pricing": {"completion": "0.000003", "input_cache_read": "0.000000085", "overrides": [], "prompt": "0.00000042"}, "reasoning": {"defaultEffort": "xhigh", "defaultEnabled": true, "mandatory": false, "supportedEfforts": ["low", "medium", "xhigh"]}, "stale": false, "tokenizer": "Qwen", "url": "https://openrouter.ai/qwen/qwen3.8-27b"}, "faq": [{"answer": "برای دسترسی به API مدل Qwen3.8 27B یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.8-27b` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل Qwen3.8 27B در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل Qwen3.8 27B در AvalAI برای هر یک میلیون توکن ورودی $0.50 و برای هر یک میلیون توکن خروجی $2.00 هزینه دارد.", "question": "هزینه API مدل Qwen3.8 27B در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل Qwen3.8 27B معادل $0.50 / 1M tokens برای ورودی و $2.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل Qwen3.8 27B چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای Qwen3.8 27B برابر 262,144 توکن است.", "question": "پنجره زمینه مدل Qwen3.8 27B چقدر است؟"}, {"answer": "در سطح 5 مدل Qwen3.8 27B در AvalAI تا 1,500 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل Qwen3.8 27B در AvalAI چقدر است؟"}, {"answer": "مدل Qwen3.8 27B در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: کش کردن پرامپت، بینایی.", "question": "مدل Qwen3.8 27B در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل Qwen3.8 27B در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل Qwen3.8 27B در AvalAI چه سطحی لازم است؟"}], "id": "Qwen3.8 27B", "owner": "alibaba", "provider": "dashscope", "sourceId": "qwen3.8-27b", "specifications": {"inputCostPerToken": 5e-07, "maxInputTokens": 262144, "maxOutputTokens": null, "outputCostPerToken": 2e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Dashscope</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل Qwen3.8 27B در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">qwen3.8-27b</code>
    <button type="button" data-copy-model-id="qwen3.8-27b" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">Qwen3.8 27B یک مدل هوش مصنوعی از Alibaba است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=qwen3.8-27b">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000005">$0.50 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.000002">$2.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>262,144 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>— توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-08-14</strong></div>
</div>

## استفاده از مدل هوش مصنوعی Qwen3.8 27B

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "qwen3.8-27b", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-27b",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3.8-27b",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- کش کردن پرامپت
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
- `top_a`
- `top_k`
- `top_logprobs`
- `top_p`

#### مقادیر تکمیلی تلاش استدلال

`low`, `medium`, `xhigh`

## محدودیت نرخ مدل Qwen3.8 27B

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 20 | 500,000 |
| سطح 2 | 150 | 2,000,000 |
| سطح 3 | 350 | 4,000,000 |
| سطح 4 | 750 | 8,000,000 |
| سطح 5 | 1,500 | 20,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000005">$0.50 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.00000042">$0.42 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.00000044310">$0.44 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.000002">$2.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.000003">$3.00 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.000003165">$3.17 / 1M tokens</span></td></tr>
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
      <strong>45.8</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">45.8 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/qwen/qwen3.8-27b" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص کدنویسی Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>68.1</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">68.1 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/qwen/qwen3.8-27b" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص هوش Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>33.7</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">33.7 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/qwen/qwen3.8-27b" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
</section>

<OpenRouterLivePanel />


## مدل‌های مرتبط

- [Qwen3.8 2.4T A95B](/fa/models/qwen3.8-2.4t-a95b)
- [Qwen3.8 Max](/fa/models/qwen3.8-max)
- [Qwen3.8 Flash](/fa/models/qwen3.8-flash)
- [Qwen3.7 Plus](/fa/models/qwen3.7-plus)

## پرسش‌های متداول

### چگونه به API مدل Qwen3.8 27B در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل Qwen3.8 27B یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.8-27b` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل Qwen3.8 27B در AvalAI چقدر است؟

API مدل Qwen3.8 27B در AvalAI برای هر یک میلیون توکن ورودی $0.50 و برای هر یک میلیون توکن خروجی $2.00 هزینه دارد.

### هزینه توکن مدل Qwen3.8 27B چقدر است؟

قیمت فعلی AvalAI برای مدل Qwen3.8 27B معادل $0.50 / 1M tokens برای ورودی و $2.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل Qwen3.8 27B چقدر است؟

حداکثر ورودی ثبت‌شده برای Qwen3.8 27B برابر 262,144 توکن است.

### محدودیت نرخ مدل Qwen3.8 27B در AvalAI چقدر است؟

در سطح 5 مدل Qwen3.8 27B در AvalAI تا 1,500 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل Qwen3.8 27B در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل Qwen3.8 27B در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: کش کردن پرامپت، بینایی.

### برای استفاده از مدل Qwen3.8 27B در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل Qwen3.8 27B در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/qwen/qwen3.8-27b) · آخرین بررسی: 2026-09-30
