---
title: "API مدل Gemini 3.1 Pro Preview، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل Gemini 3.1 Pro Preview در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_audio_input", "supports_function_calling", "supports_native_streaming", "supports_pdf_input", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_system_messages", "supports_tool_choice", "supports_url_context", "supports_video_input", "supports_vision", "supports_web_search"], "citations": [], "evidence": null, "external": {"canonicalSlug": "google/gemini-3.1-pro-preview-20260219", "contextLength": 1048576, "defaultParameters": {"frequency_penalty": null, "presence_penalty": null, "repetition_penalty": null, "temperature": null, "top_k": null, "top_p": null}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 65536, "modelId": "google/gemini-3.1-pro-preview", "pricing": {"completion": "0.000012", "image": "0.000002", "input_cache_read": "0.0000002", "input_cache_write": "0.000000375", "overrides": [{"completion": "0.000018", "inputCacheRead": "0.0000004", "minPromptTokens": 200000, "prompt": "0.000004"}], "prompt": "0.000002", "web_search": "0.014"}, "reasoning": {"defaultEffort": "medium", "defaultEnabled": null, "mandatory": true, "supportedEfforts": ["high", "low", "medium"]}, "stale": false, "tokenizer": "Gemini", "url": "https://openrouter.ai/google/gemini-3.1-pro-preview"}, "faq": [{"answer": "برای دسترسی به API مدل Gemini 3.1 Pro Preview یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini-3.1-pro-preview` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل Gemini 3.1 Pro Preview در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل Gemini 3.1 Pro Preview در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $12.00 هزینه دارد.", "question": "هزینه API مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل Gemini 3.1 Pro Preview معادل $2.00 / 1M tokens برای ورودی و $12.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل Gemini 3.1 Pro Preview چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای Gemini 3.1 Pro Preview برابر 1,048,576 توکن است.", "question": "پنجره زمینه مدل Gemini 3.1 Pro Preview چقدر است؟"}, {"answer": "در سطح 5 مدل Gemini 3.1 Pro Preview در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟"}, {"answer": "مدل Gemini 3.1 Pro Preview در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، فراخوانی توابع، پخش زنده، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، زمینه از نشانی وب، ورودی ویدئو، بینایی، جست‌وجوی وب.", "question": "مدل Gemini 3.1 Pro Preview در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل Gemini 3.1 Pro Preview در AvalAI به سطح 1 یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل Gemini 3.1 Pro Preview در AvalAI چه سطحی لازم است؟"}], "id": "Gemini 3.1 Pro Preview", "owner": "google", "provider": "gemini", "sourceId": "gemini-3.1-pro-preview", "specifications": {"inputCostPerToken": 2e-06, "maxInputTokens": 1048576, "maxOutputTokens": 65536, "outputCostPerToken": 1.2e-05}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Google</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل Gemini 3.1 Pro Preview در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gemini-3.1-pro-preview</code>
    <button type="button" data-copy-model-id="gemini-3.1-pro-preview" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">Gemini 3.1 Pro Preview یک مدل هوش مصنوعی از Google است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gemini-3.1-pro-preview">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت ورودی</span><strong><span data-model-price data-price-per-token="0.000002">$2.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.000012">$12.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>1,048,576 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>65,536 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-02-19</strong></div>
</div>

## استفاده از مدل هوش مصنوعی Gemini 3.1 Pro Preview

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gemini-3.1-pro-preview", "messages": [{"role": "user", "content": "Give a concise, practical solution."}]}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gemini-3.1-pro-preview",
    messages=[{"role": "user", "content": "Give a concise, practical solution."}],
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gemini-3.1-pro-preview",
  messages: [{ role: "user", content: "Give a concise, practical solution." }],
});

console.log(response.choices[0].message.content);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- ورودی صوتی
- فراخوانی توابع
- پخش زنده
- ورودی PDF
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- پیام‌های سیستمی
- انتخاب ابزار
- زمینه از نشانی وب
- ورودی ویدئو
- بینایی
- جست‌وجوی وب

### Endpointها

- `/v1/chat/completions`
- `/v1/completions`
- `/v1/batch`

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `include_reasoning`
- `max_tokens`
- `reasoning`
- `reasoning_effort`
- `response_format`
- `seed`
- `stop`
- `structured_outputs`
- `temperature`
- `tool_choice`
- `tools`
- `top_p`

#### مقادیر تکمیلی تلاش استدلال

`high`, `low`, `medium`

## محدودیت نرخ مدل Gemini 3.1 Pro Preview

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح 1 | 10 | 500,000 |
| سطح 2 | 75 | 2,000,000 |
| سطح 3 | 250 | 4,000,000 |
| سطح 4 | 500 | 10,000,000 |
| سطح 5 | 10,000 | 20,000,000 |

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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.000002">$2.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.000002">$2.00 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.000002110">$2.11 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.000012">$12.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.000012">$12.00 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.000012660">$12.66 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>


<section class="model-benchmarks">
  <h2>عملکرد بنچمارک هم‌گروه</h2>
  <p>امتیازهای مستقل و دارای منبع؛ بدون امتیاز ترکیبی.</p>
  <article class="model-benchmark">
    <h3>شاخص عاملیت Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>8.2</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">8.2 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/google/gemini-3.1-pro-preview" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص کدنویسی Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>68.8</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">68.8 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/google/gemini-3.1-pro-preview" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
  <article class="model-benchmark">
    <h3>شاخص هوش Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>29.7</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">29.7 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/google/gemini-3.1-pro-preview" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
</section>

<OpenRouterLivePanel />


## مدل‌های مرتبط

- [gemini-3.1-flash-tts-preview](/fa/models/gemini-3.1-flash-tts-preview)
- [Gemini 3.1 Flash Lite Preview](/fa/models/gemini-3.1-flash-lite-preview)
- [Nano Banana 2 Lite (Gemini 3.1 Flash Lite Image)](/fa/models/gemini-3.1-flash-lite-image)
- [Gemini 3.1 Flash Lite](/fa/models/gemini-3.1-flash-lite)

## پرسش‌های متداول

### چگونه به API مدل Gemini 3.1 Pro Preview در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل Gemini 3.1 Pro Preview یک کلید API در داشبورد AvalAI بسازید و شناسه `gemini-3.1-pro-preview` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟

API مدل Gemini 3.1 Pro Preview در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $12.00 هزینه دارد.

### هزینه توکن مدل Gemini 3.1 Pro Preview چقدر است؟

قیمت فعلی AvalAI برای مدل Gemini 3.1 Pro Preview معادل $2.00 / 1M tokens برای ورودی و $12.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل Gemini 3.1 Pro Preview چقدر است؟

حداکثر ورودی ثبت‌شده برای Gemini 3.1 Pro Preview برابر 1,048,576 توکن است.

### محدودیت نرخ مدل Gemini 3.1 Pro Preview در AvalAI چقدر است؟

در سطح 5 مدل Gemini 3.1 Pro Preview در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل Gemini 3.1 Pro Preview در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل Gemini 3.1 Pro Preview در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: ورودی صوتی، فراخوانی توابع، پخش زنده، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، زمینه از نشانی وب، ورودی ویدئو، بینایی، جست‌وجوی وب.

### برای استفاده از مدل Gemini 3.1 Pro Preview در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل Gemini 3.1 Pro Preview در AvalAI به سطح 1 یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/google/gemini-3.1-pro-preview) · آخرین بررسی: 2026-09-30
