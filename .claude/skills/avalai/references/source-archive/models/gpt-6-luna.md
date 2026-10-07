---
title: "API مدل GPT-6 Luna، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل GPT-6 Luna در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_function_calling", "supports_native_streaming", "supports_parallel_function_calling", "supports_pdf_input", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_system_messages", "supports_tool_choice", "supports_vision", "supports_web_search"], "citations": [], "evidence": null, "external": {"canonicalSlug": "openai/gpt-6-luna-20260922", "contextLength": 1050000, "defaultParameters": {"frequency_penalty": null, "presence_penalty": null, "repetition_penalty": null, "temperature": null, "top_k": null, "top_p": null}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 128000, "modelId": "openai/gpt-6-luna", "pricing": {"completion": "0.0000005", "input_cache_read": "0.00000001", "input_cache_write": "0.000000125", "overrides": [{"completion": "0.00000075", "inputCacheRead": "0.00000002", "inputCacheWrite": "0.00000025", "minPromptTokens": 272000, "prompt": "0.0000002"}], "prompt": "0.0000001", "web_search": "0.01"}, "reasoning": {"defaultEffort": "medium", "defaultEnabled": true, "mandatory": false, "supportedEfforts": ["high", "low", "max", "medium", "none", "xhigh"]}, "stale": false, "tokenizer": "GPT", "url": "https://openrouter.ai/openai/gpt-6-luna"}, "faq": [{"answer": "برای دسترسی به API مدل GPT-6 Luna یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-6-luna` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل GPT-6 Luna در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل GPT-6 Luna در AvalAI برای هر یک میلیون توکن ورودی $0.10 و برای هر یک میلیون توکن خروجی $0.50 هزینه دارد.", "question": "هزینه API مدل GPT-6 Luna در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل GPT-6 Luna معادل $0.10 / 1M tokens برای ورودی و $0.50 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل GPT-6 Luna چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای GPT-6 Luna برابر 922,000 توکن است.", "question": "پنجره زمینه مدل GPT-6 Luna چقدر است؟"}, {"answer": "در سطح 5 مدل GPT-6 Luna در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل GPT-6 Luna در AvalAI چقدر است؟"}, {"answer": "مدل GPT-6 Luna در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی، جست‌وجوی وب.", "question": "مدل GPT-6 Luna در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل GPT-6 Luna در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل GPT-6 Luna در AvalAI چه سطحی لازم است؟"}], "id": "GPT-6 Luna", "owner": "openai", "provider": "openai", "sourceId": "gpt-6-luna", "specifications": {"inputCostPerToken": 1e-07, "maxInputTokens": 922000, "maxOutputTokens": 128000, "outputCostPerToken": 5e-07}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>OpenAI</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل GPT-6 Luna در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">gpt-6-luna</code>
    <button type="button" data-copy-model-id="gpt-6-luna" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">GPT-6 Luna مدل کم‌هزینه OpenAI از نسل GPT-6 برای استدلال پرتعداد، کدنویسی و گردش‌کارهای حرفه‌ای روزمره است. AvalAI از Chat Completions، Messages و Responses پشتیبانی می‌کند؛ ابزارهای میزبانی‌شده به پشتیبانی جداگانه مسیر نیاز دارند.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=gpt-6-luna">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.0000005">$0.50 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>922,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>128,000 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-09-22</strong></div>
</div>

## استفاده از مدل هوش مصنوعی GPT-6 Luna

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "gpt-6-luna", "input": "Give a concise, practical solution."}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-luna",
    input="Give a concise, practical solution.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-6-luna",
  input: "Give a concise, practical solution.",
});

console.log(response.output_text);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## مناسب برای

- پشتیبانی و خلاصه‌سازی در حجم بالا
- گردش‌کارهای کدنویسی حساس به هزینه
- وظایف دارای زمینه تکراری با حافظه نهان پرامپت

## قابلیت‌ها و endpointها

- فراخوانی توابع
- پخش زنده
- فراخوانی موازی توابع
- ورودی PDF
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- پیام‌های سیستمی
- انتخاب ابزار
- بینایی
- جست‌وجوی وب

### Endpointها

- `/v1/chat/completions`
- `/v1/messages`
- `/v1/responses`

### پارامترهای مدل از منابع شخص ثالث

داده مرجع شخص ثالث پشتیبانی endpointهای AvalAI را تغییر نمی‌دهد؛ قابلیت‌ها و endpointهای بالا را مبنا قرار دهید.

- `include_reasoning`
- `max_completion_tokens`
- `max_tokens`
- `reasoning`
- `reasoning_effort`
- `response_format`
- `seed`
- `structured_outputs`
- `tool_choice`
- `tools`

#### مقادیر تکمیلی تلاش استدلال

`high`, `low`, `max`, `medium`, `none`, `xhigh`

## محدودیت نرخ مدل GPT-6 Luna

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح پایه | 1 | 10,000 |
| سطح 1 | 50 | 500,000 |
| سطح 2 | 150 | 2,000,000 |
| سطح 3 | 250 | 4,000,000 |
| سطح 4 | 1,500 | 8,000,000 |
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
      <tr><td>قیمت ورودی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000001">$0.10 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000001">$0.10 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000001055">$0.11 / 1M tokens</span></td></tr>
      <tr><td>قیمت ورودی (بیش از 272,000 توکن)</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000002">$0.20 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000002">$0.20 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000002110">$0.21 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000005">$0.50 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.0000005">$0.50 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.0000005275">$0.53 / 1M tokens</span></td></tr>
      <tr><td>قیمت خروجی (بیش از 272,000 توکن)</td><td dir="ltr"><span data-model-price data-price-per-token="0.00000075">$0.75 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.00000075">$0.75 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.00000079125">$0.79 / 1M tokens</span></td></tr>
    </tbody>
  </table>
  <p><small>قیمت AvalAI نهایی و بدون کارمزد پلتفرم است. قیمت مؤثر OpenRouter با افزودن کارمزد ۵٫۵٪ خرید اعتبار به بالاترین نرخ گزارش‌شده مدل (از جمله نرخ زمینه طولانی) محاسبه شده است. OpenRouter هنگام خرید اعتبار ۵٫۵٪ کارمزد دریافت می‌کند (حداقل ۰٫۸۰ دلار)؛ بنابراین خریدهای کوچک ممکن است هزینه مؤثر بیشتری داشته باشند. <a href="https://openrouter.ai/docs/faq" target="_blank" rel="noopener noreferrer">OpenRouter FAQ</a></small></p>
</section>


<section class="model-benchmarks">
  <h2>عملکرد بنچمارک هم‌گروه</h2>
  <p>امتیازهای مستقل و دارای منبع؛ بدون امتیاز ترکیبی.</p>
  <article class="model-benchmark">
    <h3>شاخص هوش Artificial Analysis</h3>
    <div class="model-benchmark__score" dir="ltr">
      <strong>37.3</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">37.3 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/openai/gpt-6-luna" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
</section>

<OpenRouterLivePanel />


## مدل‌های مرتبط

- [GPT-6 Sol](/fa/models/gpt-6-sol)
- [GPT-6 Astra](/fa/models/gpt-6-astra)
- [GPT-5.6 Luna](/fa/models/gpt-5.6-luna)
- [GPT-6.1 Sol](/fa/models/gpt-6.1-sol)

## پرسش‌های متداول

### چگونه به API مدل GPT-6 Luna در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل GPT-6 Luna یک کلید API در داشبورد AvalAI بسازید و شناسه `gpt-6-luna` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل GPT-6 Luna در AvalAI چقدر است؟

API مدل GPT-6 Luna در AvalAI برای هر یک میلیون توکن ورودی $0.10 و برای هر یک میلیون توکن خروجی $0.50 هزینه دارد.

### هزینه توکن مدل GPT-6 Luna چقدر است؟

قیمت فعلی AvalAI برای مدل GPT-6 Luna معادل $0.10 / 1M tokens برای ورودی و $0.50 / 1M tokens برای خروجی است.

### پنجره زمینه مدل GPT-6 Luna چقدر است؟

حداکثر ورودی ثبت‌شده برای GPT-6 Luna برابر 922,000 توکن است.

### محدودیت نرخ مدل GPT-6 Luna در AvalAI چقدر است؟

در سطح 5 مدل GPT-6 Luna در AvalAI تا 10,000 درخواست در دقیقه و 20,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل GPT-6 Luna در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل GPT-6 Luna در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: فراخوانی توابع، پخش زنده، فراخوانی موازی توابع، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، پیام‌های سیستمی، انتخاب ابزار، بینایی، جست‌وجوی وب.

### برای استفاده از مدل GPT-6 Luna در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل GPT-6 Luna در AvalAI به سطح پایه (سطح ۰) یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/openai/gpt-6-luna) · آخرین بررسی: 2026-09-30
