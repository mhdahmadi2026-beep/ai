---
title: "API مدل gpt-4o-transcribe، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل gpt-4o-transcribe در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": [], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل gpt-4o-transcribe یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-4o-transcribe` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل gpt-4o-transcribe در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل gpt-4o-transcribe در AvalAI برای هر یک میلیون توکن ورودی $2.50 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.", "question": "هزینه API مدل gpt-4o-transcribe در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل gpt-4o-transcribe معادل $2.50 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل gpt-4o-transcribe چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای gpt-4o-transcribe برابر 16,000 توکن است.", "question": "پنجره زمینه مدل gpt-4o-transcribe چقدر است؟"}, {"answer": "در سطح 5 مدل gpt-4o-transcribe در AvalAI تا 10,000 درخواست در دقیقه و 6,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل gpt-4o-transcribe در AvalAI چقدر است؟"}, {"answer": "برای فراخوانی مدل gpt-4o-transcribe در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل gpt-4o-transcribe در AvalAI چه سطحی لازم است؟"}], "id": "gpt-4o-transcribe", "owner": "openai", "provider": "openai", "sourceId": "gpt-4o-transcribe", "specifications": {"inputCostPerToken": 2.5e-06, "maxInputTokens": 16000, "maxOutputTokens": 2000, "outputCostPerToken": 1e-05}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>OpenAI</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل gpt-4o-transcribe در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gpt-4o-transcribe</code>
    <button type="button" data-copy-model-id="gpt-4o-transcribe" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">gpt-4o-transcribe یک مدل هوش مصنوعی از OpenAI است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gpt-4o-transcribe">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000025">$2.50 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.00001">$10.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>16,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>2,000 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی gpt-4o-transcribe

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gpt-4o-transcribe", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-4o-transcribe",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-4o-transcribe",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- —

### Endpointها

- `/v1/audio/transcriptions`

## محدودیت نرخ مدل gpt-4o-transcribe

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 500 | 200,000 |
| سطح 2 | 1,500 | 350,000 |
| سطح 3 | 3,500 | 2,000,000 |
| سطح 4 | 5,000 | 4,000,000 |
| سطح 5 | 10,000 | 6,000,000 |



## مدل‌های مرتبط

- [gpt-4o-transcribe-diarize](/fa/models/gpt-4o-transcribe-diarize)
- [gpt-4o-mini-transcribe](/fa/models/gpt-4o-mini-transcribe)
- [GPT-4o-mini (2024-07-18)](/fa/models/gpt-4o-mini-2024-07-18)
- [GPT-4o-mini](/fa/models/gpt-4o-mini)

## پرسش‌های متداول

### چگونه به API مدل gpt-4o-transcribe در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل gpt-4o-transcribe یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-4o-transcribe` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل gpt-4o-transcribe در AvalAI چقدر است؟

API مدل gpt-4o-transcribe در AvalAI برای هر یک میلیون توکن ورودی $2.50 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.

### هزینه توکن مدل gpt-4o-transcribe چقدر است؟

قیمت فعلی AvalAI برای مدل gpt-4o-transcribe معادل $2.50 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل gpt-4o-transcribe چقدر است؟

حداکثر ورودی ثبت‌شده برای gpt-4o-transcribe برابر 16,000 توکن است.

### محدودیت نرخ مدل gpt-4o-transcribe در AvalAI چقدر است؟

در سطح 5 مدل gpt-4o-transcribe در AvalAI تا 10,000 درخواست در دقیقه و 6,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### برای استفاده از مدل gpt-4o-transcribe در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل gpt-4o-transcribe در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
