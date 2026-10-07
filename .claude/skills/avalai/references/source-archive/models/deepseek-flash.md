---
title: "API مدل deepseek-flash، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل deepseek-flash در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_assistant_prefill", "supports_function_calling", "supports_native_streaming", "supports_parallel_function_calling", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_system_messages", "supports_tool_choice", "supports_vision"], "citations": [], "evidence": null, "external": null, "faq": [{"answer": "برای دسترسی به API مدل deepseek-flash یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل deepseek-flash در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل deepseek-flash در AvalAI برای هر یک میلیون توکن ورودی $0.30 و برای هر یک میلیون توکن خروجی $1.20 هزینه دارد.", "question": "هزینه API مدل deepseek-flash در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل deepseek-flash معادل $0.30 / 1M tokens برای ورودی و $1.20 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل deepseek-flash چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای deepseek-flash برابر 1,000,000 توکن است.", "question": "پنجره زمینه مدل deepseek-flash چقدر است؟"}, {"answer": "در سطح 5 مدل deepseek-flash در AvalAI تا 10,000 درخواست در دقیقه و 50,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل deepseek-flash در AvalAI چقدر است؟"}, {"answer": "مدل deepseek-flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پیش‌پرکردن پاسخ دستیار، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی.", "question": "مدل deepseek-flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل deepseek-flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل deepseek-flash در AvalAI چه سطحی لازم است؟"}], "id": "deepseek-flash", "owner": "deepseek", "provider": "deepseek", "sourceId": "deepseek-flash", "specifications": {"inputCostPerToken": 3e-07, "maxInputTokens": 1000000, "maxOutputTokens": 393216, "outputCostPerToken": 1.2e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>DeepSeek</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل deepseek-flash در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">deepseek-flash</code>
    <button type="button" data-copy-model-id="deepseek-flash" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">deepseek-flash یک مدل هوش مصنوعی از DeepSeek است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=deepseek-flash">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000003">$0.30 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000012">$1.20 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>1,000,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>393,216 توکن</strong></div>
</div>

## استفاده از مدل هوش مصنوعی deepseek-flash

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "deepseek-flash", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="deepseek-flash",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-flash",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- پیش‌پرکردن پاسخ دستیار
- فراخوانی توابع
- پخش زنده
- فراخوانی موازی توابع
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- پیام‌های سیستمی
- انتخاب ابزار
- بینایی

### Endpointها

- `/v1/chat/completions`

## محدودیت نرخ مدل deepseek-flash

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 50 | 1,000,000 |
| سطح 2 | 500 | 4,000,000 |
| سطح 3 | 1,500 | 8,000,000 |
| سطح 4 | 2,500 | 8,000,000 |
| سطح 5 | 10,000 | 50,000,000 |



## مدل‌های مرتبط

- [DeepSeek V4.1 Flash](/fa/models/deepseek-v4.1-flash)
- [DeepSeek V4 Pro 0423](/fa/models/deepseek-v4-pro)
- [DeepSeek V4 Flash 0423](/fa/models/deepseek-v4-flash)
- [deepseek-v3.2-speciale](/fa/models/deepseek-v3.2-speciale)

## پرسش‌های متداول

### چگونه به API مدل deepseek-flash در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل deepseek-flash یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل deepseek-flash در AvalAI چقدر است؟

API مدل deepseek-flash در AvalAI برای هر یک میلیون توکن ورودی $0.30 و برای هر یک میلیون توکن خروجی $1.20 هزینه دارد.

### هزینه توکن مدل deepseek-flash چقدر است؟

قیمت فعلی AvalAI برای مدل deepseek-flash معادل $0.30 / 1M tokens برای ورودی و $1.20 / 1M tokens برای خروجی است.

### پنجره زمینه مدل deepseek-flash چقدر است؟

حداکثر ورودی ثبت‌شده برای deepseek-flash برابر 1,000,000 توکن است.

### محدودیت نرخ مدل deepseek-flash در AvalAI چقدر است؟

در سطح 5 مدل deepseek-flash در AvalAI تا 10,000 درخواست در دقیقه و 50,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل deepseek-flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل deepseek-flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: پیش‌پرکردن پاسخ دستیار، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی.

### برای استفاده از مدل deepseek-flash در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل deepseek-flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
