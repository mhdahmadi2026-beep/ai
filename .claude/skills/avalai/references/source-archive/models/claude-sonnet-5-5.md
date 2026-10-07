---
title: "API مدل Claude Sonnet 5.5، قیمت و پنجره زمینه"
description: "راهنمای دسترسی به API مدل Claude Sonnet 5.5 در AvalAI؛ قیمت، پنجره زمینه، قابلیت‌ها، endpointها و محدودیت نرخ را بررسی کنید."
pageType: "model"
generator: "avalai-model-pages@2"
componentData: {"model": {"available": true, "capabilities": ["supports_adaptive_thinking", "supports_anthropic_compaction", "supports_computer_use", "supports_function_calling", "supports_max_reasoning_effort", "supports_mid_conversation_system", "supports_native_structured_output", "supports_output_config", "supports_pdf_input", "supports_prompt_caching", "supports_reasoning", "supports_response_schema", "supports_tool_choice", "supports_vision", "supports_web_search", "supports_xhigh_reasoning_effort"], "citations": [], "evidence": null, "external": {"canonicalSlug": "anthropic/claude-sonnet-5.5-20260928", "contextLength": 1000000, "defaultParameters": {}, "fetchedAt": "2026-09-30T08:49:02.612598Z", "instructionType": null, "maxCompletionTokens": 128000, "modelId": "anthropic/claude-sonnet-5.5", "pricing": {"completion": "0.00001", "input_cache_read": "0.0000002", "input_cache_write": "0.0000025", "overrides": [], "prompt": "0.000002", "web_search": "0.01"}, "reasoning": {"defaultEffort": "high", "defaultEnabled": null, "mandatory": true, "supportedEfforts": ["high", "low", "max", "medium", "xhigh"]}, "stale": false, "tokenizer": "Claude", "url": "https://openrouter.ai/anthropic/claude-sonnet-5.5"}, "faq": [{"answer": "برای دسترسی به API مدل Claude Sonnet 5.5 یک کلید API در داشبورد AvalAI بسازید و شناسه `claude-sonnet-5-5` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.", "question": "چگونه به API مدل Claude Sonnet 5.5 در AvalAI دسترسی پیدا کنم؟"}, {"answer": "API مدل Claude Sonnet 5.5 در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.", "question": "هزینه API مدل Claude Sonnet 5.5 در AvalAI چقدر است؟"}, {"answer": "قیمت فعلی AvalAI برای مدل Claude Sonnet 5.5 معادل $2.00 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.", "question": "هزینه توکن مدل Claude Sonnet 5.5 چقدر است؟"}, {"answer": "حداکثر ورودی ثبت‌شده برای Claude Sonnet 5.5 برابر 1,000,000 توکن است.", "question": "پنجره زمینه مدل Claude Sonnet 5.5 چقدر است؟"}, {"answer": "در سطح 5 مدل Claude Sonnet 5.5 در AvalAI تا 150 درخواست در دقیقه و 8,000,000 توکن در دقیقه را پشتیبانی می‌کند.", "question": "محدودیت نرخ مدل Claude Sonnet 5.5 در AvalAI چقدر است؟"}, {"answer": "مدل Claude Sonnet 5.5 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: تفکر تطبیقی، Anthropic compaction، کنترل رایانه، فراخوانی توابع، Max reasoning effort، پیام سیستمی میان گفت‌وگو، خروجی ساختاریافته، Output config، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب، Xhigh reasoning effort.", "question": "مدل Claude Sonnet 5.5 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟"}, {"answer": "برای فراخوانی مدل Claude Sonnet 5.5 در AvalAI به سطح 1 یا بالاتر نیاز دارید.", "question": "برای استفاده از مدل Claude Sonnet 5.5 در AvalAI چه سطحی لازم است؟"}], "id": "Claude Sonnet 5.5", "owner": "anthropic", "provider": "anthropic", "sourceId": "claude-sonnet-5-5", "specifications": {"inputCostPerToken": 2e-06, "maxInputTokens": 1000000, "maxOutputTokens": 128000, "outputCostPerToken": 1e-05}}}
---

<a class="model-back-link" href="/fa/models/">بازگشت به کاوشگر مدل‌ها</a>
<section class="model-page-hero">
  <div class="model-page-hero__identity">
    <span>Anthropic</span>
    <span class="badge badge-success">در AvalAI در دسترس است</span>
  </div>
  <h1>دسترسی به API مدل Claude Sonnet 5.5 در AvalAI</h1>
  <div class="model-page-hero__model-id">
    <code dir="ltr">claude-sonnet-5-5</code>
    <button type="button" data-copy-model-id="claude-sonnet-5-5" aria-label="کپی شناسه مدل">
      <svg data-copy-icon viewBox="0 0 24 24" aria-hidden="true"><rect x="9" y="9" width="13" height="13" rx="2"></rect><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path></svg>
    </button>
  </div>
  <p class="model-page-hero__summary">Claude Sonnet 5.5 یک مدل هوش مصنوعی از Anthropic است که از طریق API سازگار با OpenAI در AvalAI در دسترس است.</p>
  <div class="model-page-hero__actions">
    <a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ورود به داشبورد</a>
    <a class="model-action model-action--secondary" href="/fa/models/compare?models=claude-sonnet-5-5">مقایسه مدل</a>
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
<div class="model-fact"><span>قیمت خروجی</span><strong><span data-model-price data-price-per-token="0.00001">$10.00 / 1M tokens</span></strong></div>
<div class="model-fact"><span>پنجره زمینه</span><strong>1,000,000 توکن</strong></div>
<div class="model-fact"><span>حداکثر خروجی</span><strong>128,000 توکن</strong></div>
<div class="model-fact"><span>تاریخ انتشار</span><strong>2026-09-28</strong></div>
</div>

## استفاده از مدل هوش مصنوعی Claude Sonnet 5.5

کلید API را در متغیر محیطی نگه دارید و درخواست را از کد سمت سرور ارسال کنید.

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model": "claude-sonnet-5-5", "input": "Give a concise, practical solution."}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="claude-sonnet-5-5",
    input="Give a concise, practical solution.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "claude-sonnet-5-5",
  input: "Give a concise, practical solution.",
});

console.log(response.output_text);

```

<p class="model-quickstart-actions"><a class="model-action model-action--primary" href="https://chat.avalai.ir/platform/home" target="_blank" rel="noopener noreferrer">ساخت کلید API</a><a class="model-action model-action--secondary" href="/fa/quickstart">راهنمای شروع سریع</a></p>

## قابلیت‌ها و endpointها

- تفکر تطبیقی
- Anthropic compaction
- کنترل رایانه
- فراخوانی توابع
- Max reasoning effort
- پیام سیستمی میان گفت‌وگو
- خروجی ساختاریافته
- Output config
- ورودی PDF
- کش کردن پرامپت
- استدلال
- خروجی ساختاریافته
- انتخاب ابزار
- بینایی
- جست‌وجوی وب
- Xhigh reasoning effort

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
- `stop`
- `structured_outputs`
- `temperature`
- `tool_choice`
- `tools`
- `verbosity`

#### مقادیر تکمیلی تلاش استدلال

`high`, `low`, `max`, `medium`, `xhigh`

## محدودیت نرخ مدل Claude Sonnet 5.5

| Tier | RPM | TPM |
| ---: | ---: | ---: |
| سطح 1 | 2 | 30,000 |
| سطح 2 | 25 | 800,000 |
| سطح 3 | 50 | 120,000 |
| سطح 4 | 100 | 2,000,000 |
| سطح 5 | 150 | 8,000,000 |

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
      <tr><td>قیمت خروجی</td><td dir="ltr"><span data-model-price data-price-per-token="0.00001">$10.00 / 1M tokens</span></td><td dir="ltr"><span data-model-price data-price-per-token="0.00001">$10.00 / 1M tokens</span></td><td dir="ltr">۵٫۵٪</td><td dir="ltr"><span data-model-price data-price-per-token="0.00001055">$10.55 / 1M tokens</span></td></tr>
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
      <strong>56</strong><span>index</span>
    </div>
    <table class="model-benchmark__table">
      <thead><tr>
        <th>امتیاز</th><th>رتبه هم‌گروه</th><th>جهت</th><th>منبع و تاریخ</th>
      </tr></thead>
      <tbody><tr>
        <td dir="ltr">56 index</td><td>داده قابل مقایسه موجود نیست</td><td>بیشتر بهتر است</td><td><a href="https://openrouter.ai/anthropic/claude-sonnet-5.5" target="_blank" rel="noopener noreferrer">OpenRouter</a> · <span dir="ltr">2026-09-30</span></td>
      </tr></tbody>
    </table>
  </article>
</section>

<OpenRouterLivePanel />


## مدل‌های مرتبط

- [Claude Sonnet 5](/fa/models/claude-sonnet-5)
- [Claude Sonnet 4.6](/fa/models/claude-sonnet-4-6)
- [anthropic.claude-sonnet-4-5-20250929-v1:0](/fa/models/claude-sonnet-4-5-20250929-v1-0)
- [Claude Sonnet 4.5](/fa/models/claude-sonnet-4-5)

## پرسش‌های متداول

### چگونه به API مدل Claude Sonnet 5.5 در AvalAI دسترسی پیدا کنم؟

برای دسترسی به API مدل Claude Sonnet 5.5 یک کلید API در داشبورد AvalAI بسازید و شناسه `claude-sonnet-5-5` را به یکی از endpointهای پشتیبانی‌شده ارسال کنید.

### هزینه API مدل Claude Sonnet 5.5 در AvalAI چقدر است؟

API مدل Claude Sonnet 5.5 در AvalAI برای هر یک میلیون توکن ورودی $2.00 و برای هر یک میلیون توکن خروجی $10.00 هزینه دارد.

### هزینه توکن مدل Claude Sonnet 5.5 چقدر است؟

قیمت فعلی AvalAI برای مدل Claude Sonnet 5.5 معادل $2.00 / 1M tokens برای ورودی و $10.00 / 1M tokens برای خروجی است.

### پنجره زمینه مدل Claude Sonnet 5.5 چقدر است؟

حداکثر ورودی ثبت‌شده برای Claude Sonnet 5.5 برابر 1,000,000 توکن است.

### محدودیت نرخ مدل Claude Sonnet 5.5 در AvalAI چقدر است؟

در سطح 5 مدل Claude Sonnet 5.5 در AvalAI تا 150 درخواست در دقیقه و 8,000,000 توکن در دقیقه را پشتیبانی می‌کند.

### مدل Claude Sonnet 5.5 در AvalAI از چه قابلیت‌هایی پشتیبانی می‌کند؟

مدل Claude Sonnet 5.5 در AvalAI از این قابلیت‌ها پشتیبانی می‌کند: تفکر تطبیقی، Anthropic compaction، کنترل رایانه، فراخوانی توابع، Max reasoning effort، پیام سیستمی میان گفت‌وگو، خروجی ساختاریافته، Output config، ورودی PDF، کش کردن پرامپت، استدلال، خروجی ساختاریافته، انتخاب ابزار، بینایی، جست‌وجوی وب، Xhigh reasoning effort.

### برای استفاده از مدل Claude Sonnet 5.5 در AvalAI چه سطحی لازم است؟

برای فراخوانی مدل Claude Sonnet 5.5 در AvalAI به سطح 1 یا بالاتر نیاز دارید.

<span id="منابع-و-تازگی-داده" aria-hidden="true"></span>

## داده‌های شخص ثالث و تازگی

- قیمت، دسترسی، endpoint و محدودیت نرخ: داده‌های ساختاریافته AvalAI (مرجع اصلی)
- [بازار OpenRouter](https://openrouter.ai/anthropic/claude-sonnet-5.5) · آخرین بررسی: 2026-09-30
