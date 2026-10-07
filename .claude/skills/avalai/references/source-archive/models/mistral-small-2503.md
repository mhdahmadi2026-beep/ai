---
title: "API مدل mistral-small-2503، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل mistral-small-2503 در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_tool_choice", "supports_vision"], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل mistral-small-2503 یک کلید API در داشبورد AvalAI بسازید و شناسه `azure_ai/mistral-small-2503` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل mistral-small-2503 در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل mistral-small-2503 در AvalAI برای هر یک میلیون توکن ورودی $0.10 و برای هر یک میلیون توکن خروجی $0.30 هزینه دارد.", "question": "هزینه API مدل mistral-small-2503 در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل mistral-small-2503 معادل $0.10 / 1M tokens برای ورودی و $0.30 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل mistral-small-2503 چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای mistral-small-2503 برابر 128,000 توکن است.", "question": "پنجره زمینه مدل mistral-small-2503 چقدر است؟"}, {"answer": "در سطح 5 مدل mistral-small-2503 در AvalAI تا 1,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل mistral-small-2503 در AvalAI چقدر است؟"}, {"answer": "مدل mistral-small-2503 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، انتخاب ابزار، بینایی.", "question": "مدل mistral-small-2503 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل mistral-small-2503 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل mistral-small-2503 در AvalAI چه سطحی لازم است؟"}], "id": "mistral-small-2503", "owner": "google", "provider": "vertex_ai", "sourceId": "azure_ai/mistral-small-2503", "specifications": {"inputCostPerToken": 1e-07, "maxInputTokens": 128000, "maxOutputTokens": 128000, "outputCostPerToken": 3e-07}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Vertex Ai</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل mistral-small-2503 در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">azure_ai/mistral-small-2503</code>
    <button type="button" data-copy-model-id="azure_ai/mistral-small-2503" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">mistral-small-2503 یک مدل هوش مصنوعی از Google است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=mistral-small-2503">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000001">$0.10 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000003">$0.30 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>128,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>128,000 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی mistral-small-2503

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "azure_ai/mistral-small-2503", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="azure_ai/mistral-small-2503",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "azure_ai/mistral-small-2503",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- انتخاب ابزار
- بینایی

## محدودیت نرخ مدل mistral-small-2503

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 150 | 1,000,000 |
| سطح 2 | 250 | 2,000,000 |
| سطح 3 | 500 | 3,000,000 |
| سطح 4 | 750 | 5,000,000 |
| سطح 5 | 1,000 | 10,000,000 |



## مدل‌های مرتبط

- [veo-3.1-generate-preview](/fa/models/veo-3.1-generate-preview)
- [veo-3.1-generate-001](/fa/models/veo-3.1-generate-001)
- [veo-3.1-fast-generate-preview](/fa/models/veo-3.1-fast-generate-preview)
- [veo-3.1-fast-generate-001](/fa/models/veo-3.1-fast-generate-001)

## پرسش‌های متداول

### چگونه به API مدل mistral-small-2503 در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل mistral-small-2503 یک کلید API در داشبورد AvalAI بسازید و شناسه `azure_ai/mistral-small-2503` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل mistral-small-2503 در AvalAI چقدر است؟

API مدل mistral-small-2503 در AvalAI برای هر یک میلیون توکن ورودی $0.10 و برای هر یک میلیون توکن خروجی $0.30 هزینه دارد.

### هزینه توکن مدل mistral-small-2503 چقدر است؟

قیمت فعلی AvalAI برای مدل mistral-small-2503 معادل $0.10 / 1M tokens برای ورودی و $0.30 / 1M tokens برای خروجی است.

### پنجره زمینه مدل mistral-small-2503 چقدر است؟

حداکثر ورودی ثبت‌شده برای mistral-small-2503 برابر 128,000 توکن است.

### محدودیت نرخ مدل mistral-small-2503 در AvalAI چقدر است؟

در سطح 5 مدل mistral-small-2503 در AvalAI تا 1,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل mistral-small-2503 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل mistral-small-2503 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، انتخاب ابزار، بینایی.

### برای استفاده از مدل mistral-small-2503 در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل mistral-small-2503 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
