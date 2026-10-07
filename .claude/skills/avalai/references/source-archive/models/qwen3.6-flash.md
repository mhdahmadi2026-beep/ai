---
title: "API مدل Qwen3.6 Flash، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل Qwen3.6 Flash در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_reasoning", "supports_tool_choice", "supports_video_input", "supports_vision"], "citations": [], "evidence": null, "external": {"canonicalSlug": "qwen/qwen3.6-flash", "contextLength": 1000000, "defaultParameters": {}, "fetchedAt": "2026-07-31T06:13:12.364711Z", "instructionType": null, "maxCompletionTokens": 65536, "modelId": "qwen/qwen3.6-flash", "pricing": {"completion": "0.000001125", "input_cache_write": "0.000000234375", "overrides": [{"completion": "0.000003", "inputCacheWrite": "0.0000009375", "minPromptTokens": 256000, "prompt": "0.00000075"}], "prompt": "0.0000001875"}, "reasoning": {"defaultEffort": null, "defaultEnabled": null, "mandatory": false, "supportedEfforts": []}, "stale": true, "tokenizer": "Qwen3", "url": "https://openrouter.ai/qwen/qwen3.6-flash"}, "faq": [{"answer": "برای دسترسی به API مدل Qwen3.6 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.6-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل Qwen3.6 Flash در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل Qwen3.6 Flash در AvalAI برای هر یک میلیون توکن ورودی — و برای هر یک میلیون توکن خروجی — هزینه دارد.", "question": "هزینه API مدل Qwen3.6 Flash در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل Qwen3.6 Flash معادل — برای ورودی و — برای خروجی است.", "question": "هزینه توکن مدل Qwen3.6 Flash چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای Qwen3.6 Flash برابر 991,000 توکن است.", "question": "پنجره زمینه مدل Qwen3.6 Flash چقدر است؟"}, {"answer": "در سطح 5 مدل Qwen3.6 Flash در AvalAI تا 10,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل Qwen3.6 Flash در AvalAI چقدر است؟"}, {"answer": "مدل Qwen3.6 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.", "question": "مدل Qwen3.6 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل Qwen3.6 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل Qwen3.6 Flash در AvalAI چه سطحی لازم است؟"}], "id": "Qwen3.6 Flash", "owner": "alibaba", "provider": "dashscope", "sourceId": "qwen3.6-flash", "specifications": {"inputCostPerToken": null, "maxInputTokens": 991000, "maxOutputTokens": 64000, "outputCostPerToken": null}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Dashscope</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل Qwen3.6 Flash در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">qwen3.6-flash</code>
    <button type="button" data-copy-model-id="qwen3.6-flash" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">Qwen3.6 Flash یک مدل هوش مصنوعی از Alibaba است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=qwen3.6-flash">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong>—</strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong>—</strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>991,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>64,000 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-04-27</strong></div>
</div>

## استفاده از مدل هوش مصنوعی Qwen3.6 Flash

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "qwen3.6-flash", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.6-flash",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3.6-flash",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- استدلال
- انتخاب ابزار
- ورودی ویدئو
- بینایی

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `frequency_penalty`
- `include_reasoning`
- `logprobs`
- `max_tokens`
- `presence_penalty`
- `reasoning`
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

## محدودیت نرخ مدل Qwen3.6 Flash

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 100 | 1,000,000 |
| سطح 2 | 750 | 2,000,000 |
| سطح 3 | 1,500 | 4,000,000 |
| سطح 4 | 3,500 | 8,000,000 |
| سطح 5 | 10,000 | 10,000,000 |


<OpenRouterLivePanel />


## مدل‌های مرتبط

- [Qwen3.6 Plus](/fa/models/qwen3.6-plus)
- [Qwen3.6 Max Preview](/fa/models/qwen3.6-max-preview)
- [Qwen3.6 35B A3B](/fa/models/qwen3.6-35b-a3b)
- [Qwen3.6 27B](/fa/models/qwen3.6-27b)

## پرسش‌های متداول

### چگونه به API مدل Qwen3.6 Flash در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل Qwen3.6 Flash یک کلید API در داشبورد AvalAI بسازید و شناسه `qwen3.6-flash` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل Qwen3.6 Flash در AvalAI چقدر است؟

API مدل Qwen3.6 Flash در AvalAI برای هر یک میلیون توکن ورودی — و برای هر یک میلیون توکن خروجی — هزینه دارد.

### هزینه توکن مدل Qwen3.6 Flash چقدر است؟

قیمت فعلی AvalAI برای مدل Qwen3.6 Flash معادل — برای ورودی و — برای خروجی است.

### پنجره زمینه مدل Qwen3.6 Flash چقدر است؟

حداکثر ورودی ثبت‌شده برای Qwen3.6 Flash برابر 991,000 توکن است.

### محدودیت نرخ مدل Qwen3.6 Flash در AvalAI چقدر است؟

در سطح 5 مدل Qwen3.6 Flash در AvalAI تا 10,000 درخواست در دقیقه و 10,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل Qwen3.6 Flash در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل Qwen3.6 Flash در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، استدلال، انتخاب ابزار، ورودی ویدئو، بینایی.

### برای استفاده از مدل Qwen3.6 Flash در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل Qwen3.6 Flash در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/qwen/qwen3.6-flash) · آخرین بررسی: 2026-07-31
