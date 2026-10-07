---
title: "API مدل GPT Audio Mini، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل GPT Audio Mini در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_audio_input", "supports_audio_output", "supports_function_calling", "supports_native_streaming", "supports_parallel_function_calling", "supports_system_messages", "supports_tool_choice"], "citations": [], "evidence": null, "external": {"canonicalSlug": "openai/gpt-audio-mini", "contextLength": 128000, "defaultParameters": {"frequency_penalty": null, "temperature": null, "top_p": null}, "fetchedAt": "2026-07-31T06:13:12.364711Z", "instructionType": null, "maxCompletionTokens": 16384, "modelId": "openai/gpt-audio-mini", "pricing": {"completion": "0.0000024", "overrides": [], "prompt": "0.0000006"}, "reasoning": {"defaultEffort": null, "defaultEnabled": null, "mandatory": null, "supportedEfforts": []}, "stale": true, "tokenizer": "GPT", "url": "https://openrouter.ai/openai/gpt-audio-mini"}, "faq": [{"answer": "برای دسترسی به API مدل GPT Audio Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-audio-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل GPT Audio Mini در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل GPT Audio Mini در AvalAI برای هر یک میلیون توکن ورودی $0.60 و برای هر یک میلیون توکن خروجی $2.40 هزینه دارد.", "question": "هزینه API مدل GPT Audio Mini در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل GPT Audio Mini معادل $0.60 / 1M tokens برای ورودی و $2.40 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل GPT Audio Mini چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای GPT Audio Mini برابر 128,000 توکن است.", "question": "پنجره زمینه مدل GPT Audio Mini چقدر است؟"}, {"answer": "در سطح 5 مدل GPT Audio Mini در AvalAI تا 10,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل GPT Audio Mini در AvalAI چقدر است؟"}, {"answer": "مدل GPT Audio Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، خروجی صوتی، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، پیام‌های سیستمی، انتخاب ابزار.", "question": "مدل GPT Audio Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل GPT Audio Mini در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل GPT Audio Mini در AvalAI چه سطحی لازم است؟"}], "id": "GPT Audio Mini", "owner": "openai", "provider": "openai", "sourceId": "gpt-audio-mini", "specifications": {"inputCostPerToken": 6e-07, "maxInputTokens": 128000, "maxOutputTokens": 16384, "outputCostPerToken": 2.4e-06}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>OpenAI</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل GPT Audio Mini در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gpt-audio-mini</code>
    <button type="button" data-copy-model-id="gpt-audio-mini" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">GPT Audio Mini یک مدل هوش مصنوعی از OpenAI است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gpt-audio-mini">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.0000006">$0.60 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000024">$2.40 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>128,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>16,384 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-01-19</strong></div>
</div>

## استفاده از مدل هوش مصنوعی GPT Audio Mini

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gpt-audio-mini", "input": "Give a concise, practical solution."}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-audio-mini",
    input="Give a concise, practical solution.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-audio-mini",
  input: "Give a concise, practical solution.",
});

console.log(response.output_text);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- ورودی صوتی
- خروجی صوتی
- فراخوانی توابع
- پخش زنده
- فراخوانی موازی توابع
- پیام‌های سیستمی
- انتخاب ابزار

### Endpointها

- `/v1/chat/completions`
- `/v1/responses`
- `/v1/realtime`
- `/v1/batch`

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `frequency_penalty`
- `logit_bias`
- `logprobs`
- `max_tokens`
- `presence_penalty`
- `response_format`
- `seed`
- `stop`
- `structured_outputs`
- `temperature`
- `tool_choice`
- `tools`
- `top_logprobs`
- `top_p`

## محدودیت نرخ مدل GPT Audio Mini

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 1 | 10,000 |
| سطح 1 | 100 | 30,000 |
| سطح 2 | 1,000 | 450,000 |
| سطح 3 | 1,500 | 800,000 |
| سطح 4 | 3,500 | 2,000,000 |
| سطح 5 | 10,000 | 30,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000006">$0.60 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000006">$0.60 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000006330">$0.63 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000024">$2.40 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000024">$2.40 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000025320">$2.53 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>



<OpenRouterLivePanel />


## مدل‌های مرتبط

- [gpt-audio-mini-2025-10-06](/fa/models/gpt-audio-mini-2025-10-06)
- [gpt-audio-2025-08-28](/fa/models/gpt-audio-2025-08-28)
- [gpt-audio-1.5](/fa/models/gpt-audio-1.5)
- [GPT Audio](/fa/models/gpt-audio)

## پرسش‌های متداول

### چگونه به API مدل GPT Audio Mini در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل GPT Audio Mini یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-audio-mini` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل GPT Audio Mini در AvalAI چقدر است؟

API مدل GPT Audio Mini در AvalAI برای هر یک میلیون توکن ورودی $0.60 و برای هر یک میلیون توکن خروجی $2.40 هزینه دارد.

### هزینه توکن مدل GPT Audio Mini چقدر است؟

قیمت فعلی AvalAI برای مدل GPT Audio Mini معادل $0.60 / 1M tokens برای ورودی و $2.40 / 1M tokens برای خروجی است.

### پنجره زمینه مدل GPT Audio Mini چقدر است؟

حداکثر ورودی ثبت‌شده برای GPT Audio Mini برابر 128,000 توکن است.

### محدودیت نرخ مدل GPT Audio Mini در AvalAI چقدر است؟

در سطح 5 مدل GPT Audio Mini در AvalAI تا 10,000 درخواست در دقیقه و 30,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل GPT Audio Mini در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل GPT Audio Mini در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، خروجی صوتی، فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، پیام‌های سیستمی، انتخاب ابزار.

### برای استفاده از مدل GPT Audio Mini در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل GPT Audio Mini در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/openai/gpt-audio-mini) · آخرین بررسی: 2026-07-31
