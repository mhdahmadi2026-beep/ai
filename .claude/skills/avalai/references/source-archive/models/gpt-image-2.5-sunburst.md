---
title: "API مدل gpt-image-2.5-sunburst، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل gpt-image-2.5-sunburst در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_pdf_input", "supports_vision"], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل gpt-image-2.5-sunburst یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-image-2.5-sunburst` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل gpt-image-2.5-sunburst در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل gpt-image-2.5-sunburst در AvalAI برای هر یک میلیون توکن ورودی $5.00 و برای هر یک میلیون توکن خروجی — هزینه دارد.", "question": "هزینه API مدل gpt-image-2.5-sunburst در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل gpt-image-2.5-sunburst معادل $5.00 / 1M tokens برای ورودی و — برای خروجی است.", "question": "هزینه توکن مدل gpt-image-2.5-sunburst چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای gpt-image-2.5-sunburst برابر — توکن است.", "question": "پنجره زمینه مدل gpt-image-2.5-sunburst چقدر است؟"}, {"answer": "در سطح 5 مدل gpt-image-2.5-sunburst در AvalAI تا 250 درخواست در دقیقه و 1,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل gpt-image-2.5-sunburst در AvalAI چقدر است؟"}, {"answer": "مدل gpt-image-2.5-sunburst در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی PDF، بینایی.", "question": "مدل gpt-image-2.5-sunburst در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل gpt-image-2.5-sunburst در AvalAI به سطح 1 یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل gpt-image-2.5-sunburst در AvalAI چه سطحی لازم است؟"}], "id": "gpt-image-2.5-sunburst", "owner": "openai", "provider": "openai", "sourceId": "gpt-image-2.5-sunburst", "specifications": {"inputCostPerToken": 5e-06, "maxInputTokens": null, "maxOutputTokens": null, "outputCostPerToken": null}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>OpenAI</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل gpt-image-2.5-sunburst در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gpt-image-2.5-sunburst</code>
    <button type="button" data-copy-model-id="gpt-image-2.5-sunburst" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">gpt-image-2.5-sunburst یک مدل هوش مصنوعی از OpenAI است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gpt-image-2.5-sunburst">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.000005">$5.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong>—</strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>— توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>— توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی gpt-image-2.5-sunburst

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gpt-image-2.5-sunburst", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-image-2.5-sunburst",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-image-2.5-sunburst",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- ورودی PDF
- بینایی

### Endpointها

- `/v1/images/generations`
- `/v1/images/edits`

## محدودیت نرخ مدل gpt-image-2.5-sunburst

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح 1 | 1 | 40,000 |
| سطح 2 | 5 | 500,000 |
| سطح 3 | 50 | 1,000,000 |
| سطح 4 | 100 | 4,000,000 |
| سطح 5 | 250 | 1,000,000 |



## مدل‌های مرتبط

- [gpt-image-2.5-flare](/fa/models/gpt-image-2.5-flare)
- [gpt-image-2](/fa/models/gpt-image-2)
- [gpt-image-1.5](/fa/models/gpt-image-1.5)
- [gpt-image-1-mini](/fa/models/gpt-image-1-mini)

## پرسش‌های متداول

### چگونه به API مدل gpt-image-2.5-sunburst در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل gpt-image-2.5-sunburst یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-image-2.5-sunburst` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل gpt-image-2.5-sunburst در AvalAI چقدر است؟

API مدل gpt-image-2.5-sunburst در AvalAI برای هر یک میلیون توکن ورودی $5.00 و برای هر یک میلیون توکن خروجی — هزینه دارد.

### هزینه توکن مدل gpt-image-2.5-sunburst چقدر است؟

قیمت فعلی AvalAI برای مدل gpt-image-2.5-sunburst معادل $5.00 / 1M tokens برای ورودی و — برای خروجی است.

### پنجره زمینه مدل gpt-image-2.5-sunburst چقدر است؟

حداکثر ورودی ثبت‌شده برای gpt-image-2.5-sunburst برابر — توکن است.

### محدودیت نرخ مدل gpt-image-2.5-sunburst در AvalAI چقدر است؟

در سطح 5 مدل gpt-image-2.5-sunburst در AvalAI تا 250 درخواست در دقیقه و 1,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل gpt-image-2.5-sunburst در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل gpt-image-2.5-sunburst در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی PDF، بینایی.

### برای استفاده از مدل gpt-image-2.5-sunburst در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل gpt-image-2.5-sunburst در AvalAI به سطح 1 یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
