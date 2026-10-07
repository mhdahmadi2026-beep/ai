---
title: "API مدل gemini-3.8-flash-lite-tts، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل gemini-3.8-flash-lite-tts در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": [], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل gemini-3.8-flash-lite-tts یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini/gemini-3.8-flash-lite-tts` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل gemini-3.8-flash-lite-tts در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل gemini-3.8-flash-lite-tts در AvalAI برای هر یک میلیون توکن ورودی $0.50 و برای هر یک میلیون توکن خروجی $6.00 هزینه دارد.", "question": "هزینه API مدل gemini-3.8-flash-lite-tts در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل gemini-3.8-flash-lite-tts معادل $0.50 / 1M tokens برای ورودی و $6.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل gemini-3.8-flash-lite-tts چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای gemini-3.8-flash-lite-tts برابر 8,192 توکن است.", "question": "پنجره زمینه مدل gemini-3.8-flash-lite-tts چقدر است؟"}, {"answer": "در سطح 5 مدل gemini-3.8-flash-lite-tts در AvalAI تا 1,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل gemini-3.8-flash-lite-tts در AvalAI چقدر است؟"}, {"answer": "برای فراخوانی مدل gemini-3.8-flash-lite-tts در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل gemini-3.8-flash-lite-tts در AvalAI چه سطحی لازم است؟"}], "id": "gemini-3.8-flash-lite-tts", "owner": "google", "provider": "gemini", "sourceId": "gemini/gemini-3.8-flash-lite-tts", "specifications": {"inputCostPerToken": 5e-07, "maxInputTokens": 8192, "maxOutputTokens": 16384, "outputCostPerToken": 6e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Google</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل gemini-3.8-flash-lite-tts در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gemini/gemini-3.8-flash-lite-tts</code>
    <button type="button" data-copy-model-id="gemini/gemini-3.8-flash-lite-tts" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">gemini-3.8-flash-lite-tts یک مدل هوش مصنوعی از Google است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gemini-3.8-flash-lite-tts">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.000006">$6.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>8,192 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>16,384 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی gemini-3.8-flash-lite-tts

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gemini/gemini-3.8-flash-lite-tts", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini/gemini-3.8-flash-lite-tts",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini/gemini-3.8-flash-lite-tts",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- —

### Endpointها

- `/v1/audio/speech`

## محدودیت نرخ مدل gemini-3.8-flash-lite-tts

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 1 | 40,000 |
| سطح 1 | 25 | 1,000,000 |
| سطح 2 | 250 | 2,000,000 |
| سطح 3 | 500 | 3,000,000 |
| سطح 4 | 750 | 5,000,000 |
| سطح 5 | 1,000 | 10,000,000 |



## مدل‌های مرتبط

- [gemini-3.8-flash-tts](/fa/models/gemini-3.8-flash-tts)
- [Gemini 3.8 Flash](/fa/models/gemini-3.8-flash)
- [Gemini 3.7 Flash](/fa/models/gemini-3.7-flash)
- [Gemini 3.6 Flash](/fa/models/gemini-3.6-flash)

## پرسش‌های متداول

### چگونه به API مدل gemini-3.8-flash-lite-tts در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل gemini-3.8-flash-lite-tts یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini/gemini-3.8-flash-lite-tts` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل gemini-3.8-flash-lite-tts در AvalAI چقدر است؟

API مدل gemini-3.8-flash-lite-tts در AvalAI برای هر یک میلیون توکن ورودی $0.50 و برای هر یک میلیون توکن خروجی $6.00 هزینه دارد.

### هزینه توکن مدل gemini-3.8-flash-lite-tts چقدر است؟

قیمت فعلی AvalAI برای مدل gemini-3.8-flash-lite-tts معادل $0.50 / 1M tokens برای ورودی و $6.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل gemini-3.8-flash-lite-tts چقدر است؟

حداکثر ورودی ثبت‌شده برای gemini-3.8-flash-lite-tts برابر 8,192 توکن است.

### محدودیت نرخ مدل gemini-3.8-flash-lite-tts در AvalAI چقدر است؟

در سطح 5 مدل gemini-3.8-flash-lite-tts در AvalAI تا 1,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### برای استفاده از مدل gemini-3.8-flash-lite-tts در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل gemini-3.8-flash-lite-tts در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
