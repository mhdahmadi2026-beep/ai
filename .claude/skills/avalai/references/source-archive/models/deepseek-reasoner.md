---
title: "API مدل deepseek-reasoner، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل deepseek-reasoner در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_native_streaming", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_system_messages"], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل deepseek-reasoner یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-reasoner` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل deepseek-reasoner در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل deepseek-reasoner در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.", "question": "هزینه API مدل deepseek-reasoner در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل deepseek-reasoner معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل deepseek-reasoner چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای deepseek-reasoner برابر 131,072 توکن است.", "question": "پنجره زمینه مدل deepseek-reasoner چقدر است؟"}, {"answer": "در سطح 5 مدل deepseek-reasoner در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل deepseek-reasoner در AvalAI چقدر است؟"}, {"answer": "مدل deepseek-reasoner در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پخش زنده، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی.", "question": "مدل deepseek-reasoner در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل deepseek-reasoner در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل deepseek-reasoner در AvalAI چه سطحی لازم است؟"}], "id": "deepseek-reasoner", "owner": "deepseek", "provider": "deepseek", "sourceId": "deepseek-reasoner", "specifications": {"inputCostPerToken": 2.8e-07, "maxInputTokens": 131072, "maxOutputTokens": 65536, "outputCostPerToken": 4.2e-07}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>DeepSeek</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل deepseek-reasoner در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">deepseek-reasoner</code>
    <button type="button" data-copy-model-id="deepseek-reasoner" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">deepseek-reasoner یک مدل هوش مصنوعی از DeepSeek است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=deepseek-reasoner">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.00000028">$0.28 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.00000042">$0.42 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>131,072 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>65,536 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی deepseek-reasoner

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "deepseek-reasoner", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-reasoner",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- پخش زنده
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- پیام‌های سیستمی

### Endpointها

- `/v1/chat/completions`

## محدودیت نرخ مدل deepseek-reasoner

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 250 | 500,000 |
| سطح 2 | 500 | 3,000,000 |
| سطح 3 | 1,500 | 4,000,000 |
| سطح 4 | 2,500 | 8,000,000 |
| سطح 5 | 5,000 | 15,000,000 |



## مدل‌های مرتبط

- [DeepSeek V4.1 Flash](/fa/models/deepseek-v4.1-flash)
- [DeepSeek V4 Pro 0423](/fa/models/deepseek-v4-pro)
- [DeepSeek V4 Flash 0423](/fa/models/deepseek-v4-flash)
- [deepseek-v3.2-speciale](/fa/models/deepseek-v3.2-speciale)

## پرسش‌های متداول

### چگونه به API مدل deepseek-reasoner در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل deepseek-reasoner یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-reasoner` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل deepseek-reasoner در AvalAI چقدر است؟

API مدل deepseek-reasoner در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.

### هزینه توکن مدل deepseek-reasoner چقدر است؟

قیمت فعلی AvalAI برای مدل deepseek-reasoner معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.

### پنجره زمینه مدل deepseek-reasoner چقدر است؟

حداکثر ورودی ثبت‌شده برای deepseek-reasoner برابر 131,072 توکن است.

### محدودیت نرخ مدل deepseek-reasoner در AvalAI چقدر است؟

در سطح 5 مدل deepseek-reasoner در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل deepseek-reasoner در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل deepseek-reasoner در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پخش زنده، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی.

### برای استفاده از مدل deepseek-reasoner در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل deepseek-reasoner در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
