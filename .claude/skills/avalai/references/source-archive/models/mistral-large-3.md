---
title: "API مدل mistral-large-3، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل mistral-large-3 در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_tool_choice"], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل mistral-large-3 یک کلید API در داشبورد AvalAI بسازید و شناسه `mistral-large-3` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل mistral-large-3 در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل mistral-large-3 در AvalAI برای هر یک میلیون توکن ورودی $5.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.", "question": "هزینه API مدل mistral-large-3 در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل mistral-large-3 معادل $5.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل mistral-large-3 چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای mistral-large-3 برابر 256,000 توکن است.", "question": "پنجره زمینه مدل mistral-large-3 چقدر است؟"}, {"answer": "در سطح 5 مدل mistral-large-3 در AvalAI تا 2,500 درخواست در دقیقه و 8,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل mistral-large-3 در AvalAI چقدر است؟"}, {"answer": "مدل mistral-large-3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، انتخاب ابزار.", "question": "مدل mistral-large-3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل mistral-large-3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل mistral-large-3 در AvalAI چه سطحی لازم است؟"}], "id": "mistral-large-3", "owner": "mistral ai", "provider": "azure", "sourceId": "mistral-large-3", "specifications": {"inputCostPerToken": 5e-06, "maxInputTokens": 256000, "maxOutputTokens": 256000, "outputCostPerToken": 1.5e-05}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Azure</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل mistral-large-3 در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">mistral-large-3</code>
    <button type="button" data-copy-model-id="mistral-large-3" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">mistral-large-3 یک مدل هوش مصنوعی از Mistral Ai است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=mistral-large-3">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.000015">$15.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>256,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>256,000 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی mistral-large-3

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "mistral-large-3", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="mistral-large-3",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "mistral-large-3",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- انتخاب ابزار

## محدودیت نرخ مدل mistral-large-3

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 1 | 10,000 |
| سطح 1 | 150 | 450,000 |
| سطح 2 | 500 | 800,000 |
| سطح 3 | 750 | 2,000,000 |
| سطح 4 | 1,500 | 4,000,000 |
| سطح 5 | 2,500 | 8,000,000 |



## مدل‌های مرتبط

- [mistral-ocr-latest](/fa/models/mistral-ocr-latest)
- [mistral-ocr-4-0](/fa/models/mistral-ocr-4-0)
- [mistral-ocr-2512](/fa/models/mistral-ocr-2512)
- [cf.mistral-small-3.1-24b-instruct](/fa/models/cf.mistral-small-3.1-24b-instruct)

## پرسش‌های متداول

### چگونه به API مدل mistral-large-3 در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل mistral-large-3 یک کلید API در داشبورد AvalAI بسازید و شناسه `mistral-large-3` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل mistral-large-3 در AvalAI چقدر است؟

API مدل mistral-large-3 در AvalAI برای هر یک میلیون توکن ورودی $5.00 و برای هر یک میلیون توکن خروجی $15.00 هزینه دارد.

### هزینه توکن مدل mistral-large-3 چقدر است؟

قیمت فعلی AvalAI برای مدل mistral-large-3 معادل $5.00 / 1M tokens برای ورودی و $15.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل mistral-large-3 چقدر است؟

حداکثر ورودی ثبت‌شده برای mistral-large-3 برابر 256,000 توکن است.

### محدودیت نرخ مدل mistral-large-3 در AvalAI چقدر است؟

در سطح 5 مدل mistral-large-3 در AvalAI تا 2,500 درخواست در دقیقه و 8,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل mistral-large-3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل mistral-large-3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، انتخاب ابزار.

### برای استفاده از مدل mistral-large-3 در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل mistral-large-3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
