---
title: "API مدل DeepSeek V3، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل DeepSeek V3 در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_native_streaming", "supports_parallel_function_calling", "supports_prompt_caching", "supports_response_schema", "supports_system_messages", "supports_tool_choice"], "citations": [], "evidence": null, "external": {"canonicalSlug": "deepseek/deepseek-chat-v3", "contextLength": 163840, "defaultParameters": {}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 16000, "modelId": "deepseek/deepseek-chat", "pricing": {"completion": "0.0000010287", "overrides": [], "prompt": "0.0000002574"}, "reasoning": {"defaultEffort": null, "defaultEnabled": null, "mandatory": null, "supportedEfforts": []}, "stale": false, "tokenizer": "DeepSeek", "url": "https://openrouter.ai/deepseek/deepseek-chat"}, "faq": [{"answer": "برای دسترسی به API مدل DeepSeek V3 یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-chat` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل DeepSeek V3 در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل DeepSeek V3 در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.", "question": "هزینه API مدل DeepSeek V3 در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل DeepSeek V3 معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل DeepSeek V3 چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای DeepSeek V3 برابر 131,072 توکن است.", "question": "پنجره زمینه مدل DeepSeek V3 چقدر است؟"}, {"answer": "در سطح 5 مدل DeepSeek V3 در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل DeepSeek V3 در AvalAI چقدر است؟"}, {"answer": "مدل DeepSeek V3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار.", "question": "مدل DeepSeek V3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل DeepSeek V3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل DeepSeek V3 در AvalAI چه سطحی لازم است؟"}], "id": "DeepSeek V3", "owner": "deepseek", "provider": "deepseek", "sourceId": "deepseek-chat", "specifications": {"inputCostPerToken": 2.8e-07, "maxInputTokens": 131072, "maxOutputTokens": 8192, "outputCostPerToken": 4.2e-07}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>DeepSeek</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل DeepSeek V3 در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">deepseek-chat</code>
    <button type="button" data-copy-model-id="deepseek-chat" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">DeepSeek V3 یک مدل هوش مصنوعی از DeepSeek است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=deepseek-chat">مقایسه مدل</a>
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
<div class="model-fact"><span>حداکثر خروجی</span><strong>8,192 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2024-12-26</strong></div>
<div class="model-fact"><span>پایان دانش</span><strong>2024-07-31</strong></div>
</div>

## استفاده از مدل هوش مصنوعی DeepSeek V3

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "deepseek-chat", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "deepseek-chat",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- فراخوانی توابع
- پخش زنده
- فراخوانی موازی توابع
- کش کردن پرامپت
- خروجی ساختاریافته
- پیام‌های سیستمی
- انتخاب ابزار

### Endpointها

- `/v1/chat/completions`

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `frequency_penalty`
- `logit_bias`
- `max_tokens`
- `min_p`
- `presence_penalty`
- `repetition_penalty`
- `response_format`
- `seed`
- `stop`
- `structured_outputs`
- `temperature`
- `tool_choice`
- `tools`
- `top_k`
- `top_p`

## محدودیت نرخ مدل DeepSeek V3

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 3 | 40,000 |
| سطح 1 | 250 | 500,000 |
| سطح 2 | 500 | 2,000,000 |
| سطح 3 | 1,500 | 4,000,000 |
| سطح 4 | 2,500 | 8,000,000 |
| سطح 5 | 5,000 | 15,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.00000028">$0.28 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000002574">$0.26 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000002715570">$0.27 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.00000042">$0.42 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000010287">$1.03 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000010852785">$1.09 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>



<OpenRouterLivePanel />


## مدل‌های مرتبط

- [deepseek-coder](/fa/models/deepseek-coder)
- [DeepSeek V4.1 Flash](/fa/models/deepseek-v4.1-flash)
- [DeepSeek V4 Pro 0423](/fa/models/deepseek-v4-pro)
- [DeepSeek V4 Flash 0423](/fa/models/deepseek-v4-flash)

## پرسش‌های متداول

### چگونه به API مدل DeepSeek V3 در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل DeepSeek V3 یک کلید API در داشبورد AvalAI بسازید و شناسه `deepseek-chat` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل DeepSeek V3 در AvalAI چقدر است؟

API مدل DeepSeek V3 در AvalAI برای هر یک میلیون توکن ورودی $0.28 و برای هر یک میلیون توکن خروجی $0.42 هزینه دارد.

### هزینه توکن مدل DeepSeek V3 چقدر است؟

قیمت فعلی AvalAI برای مدل DeepSeek V3 معادل $0.28 / 1M tokens برای ورودی و $0.42 / 1M tokens برای خروجی است.

### پنجره زمینه مدل DeepSeek V3 چقدر است؟

حداکثر ورودی ثبت‌شده برای DeepSeek V3 برابر 131,072 توکن است.

### محدودیت نرخ مدل DeepSeek V3 در AvalAI چقدر است؟

در سطح 5 مدل DeepSeek V3 در AvalAI تا 5,000 درخواست در دقیقه و 15,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل DeepSeek V3 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل DeepSeek V3 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، کش کردن پرامپت، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار.

### برای استفاده از مدل DeepSeek V3 در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل DeepSeek V3 در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/deepseek/deepseek-chat) · آخرین بررسی: 2026-09-30
