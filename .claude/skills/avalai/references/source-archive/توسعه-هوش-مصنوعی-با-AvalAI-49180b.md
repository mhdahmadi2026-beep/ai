---
hasH1: true
description: "توسعه هوش مصنوعی با AvalAI با استفاده از API سازگار با OpenAI، مثال‌های قابل اجرا، راهنماهای پیاده‌سازی و مرجع مدل‌ها و قیمت‌گذاری"
---

# توسعه هوش مصنوعی با AvalAI

<div class="docs-home-intro">
  <p class="docs-home-lead">با یک درخواست واقعی شروع کنید و سپس مسیر مستنداتی را دنبال کنید که با محصول شما هماهنگ است. AvalAI با یک آدرس پایه واحد در کلاینت‌های سازگار با OpenAI کار می‌کند.</p>
  <div class="docs-home-actions">
    <a class="is-primary" href="/fa/quickstart">شروع راه‌اندازی سریع</a>
    <a href="/fa/api-reference/introduction">مشاهده مرجع API</a>
  </div>
</div>

<!-- avalai-search-discovery:start -->

کاربران ممکن است AvalAI را با املاهای رایج «اول ai» یا «اول ای آی» و یا «هوش مصنوعی اول» پیدا کنند؛ نام رسمی در مستندات همیشه به همین شکل نوشته می‌شود.

<!-- avalai-search-discovery:end -->

<section class="docs-first-request" aria-labelledby="first-request-title">
  <div class="docs-first-request-steps">
    <h2 id="first-request-title">اولین درخواست خود را ارسال کنید</h2>
    <p>با Responses API مطمئن شوید کلید، کلاینت و مدل به‌درستی با هم کار می‌کنند.</p>
    <ol role="list">
      <li><strong>یک کلید API بسازید</strong><span><a href="https://chat.avalai.ir/platform/home">داشبورد AvalAI را باز کنید</a>، یک کلید پروژه بسازید و آن را فقط در سرور نگه دارید.</span></li>
      <li><strong>یک کلاینت نصب کنید</strong><span>از SDK سازگار با OpenAI برای Python یا JavaScript استفاده کنید یا همان درخواست را با cURL بفرستید.</span></li>
      <li><strong>درخواست Responses را اجرا کنید</strong><span>متغیر <code>AVALAI_API_KEY</code> را تنظیم کنید، مثال را اجرا کنید و <code>response.output_text</code> را بخوانید.</span></li>
    </ol>
  </div>
  <div class="docs-first-request-code">

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-6-astra",
  input: "Give me one practical idea for a developer tool.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-6-astra",
    "input": "Give me one practical idea for a developer tool."
  }'

```


  </div>
</section>

<section class="docs-task-paths" aria-labelledby="task-paths-title">
  <div class="docs-section-heading">
    <h2 id="task-paths-title">مسیر مناسب کار خود را انتخاب کنید</h2>
    <p>مستقیم به API و راهنماهای مرتبط با نیاز خود بروید.</p>
  </div>
  <div class="docs-task-path-list">
    <a class="docs-task-path" href="/fa/api-reference/responses"><span><strong>متن و استدلال</strong><span>پاسخ‌های حالت‌مند، خروجی ساختاریافته و گردش‌کارهای استدلالی بسازید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-task-path" href="/fa/api-reference/images"><span><strong>تصویر و بینایی</strong><span>محتوای تصویری را تولید، ویرایش و تحلیل کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-task-path" href="/fa/api-reference/audio"><span><strong>صوت و گفتار</strong><span>صوت را رونویسی کنید و خروجی گفتاری بسازید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-task-path" href="/fa/guides/tools"><span><strong>ابزارها و بازیابی</strong><span>مدل‌ها را به توابع، فایل‌ها، جست‌وجو و داده‌های برنامه متصل کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
  </div>
</section>

<section class="docs-models-pricing" aria-labelledby="models-pricing-title">
  <div class="docs-section-heading">
    <h2 id="models-pricing-title">مدل مناسب و هزینه آن را پیدا کنید</h2>
    <p>ابتدا قابلیت‌های مستندشده را مقایسه کنید و سپس قیمت فعلی ورودی و خروجی را ببینید.</p>
  </div>
  <div class="docs-home-link-rows">
    <a class="docs-home-link-row" href="/fa/news/2026-09-30-gemini-3-8-tts-models-added"><span><strong>جدید: Gemini 3.8 Flash و Flash-Lite TTS</strong><span>Flash را برای روایت خلاقانه، لهجه‌ها و پایداری گفتار طولانی و Lite را برای زنجیره پردازش عامل صوتی پرحجم و خواندن متن با صدا انتخاب کنید. هر دو فارسی دارند؛ نرخ تشویقی توکن تا ۱۰ دی ۱۴۰۵ (2026-12-31) و نکات درخواست ساختاریافته و مهاجرت قالب صوت را ببینید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added"><span><strong>جدید: GPT-6.1 Sol و Claude Sonnet 5.5</strong><span>از سطح ۱ با <code>gpt-6.1-sol</code> یا <code>claude-sonnet-5-5</code> گردش‌کارهای کدنویسی و اسنادی بسازید. هر دو از Chat Completions و Messages کامل پشتیبانی می‌کنند؛ Responses برای Sol کامل و برای Sonnet جزئی است. نرخ استاندارد هر میلیون توکن ورودی ۲ دلار و خروجی ۱۰ دلار است؛ قیمت حافظه نهان و مهاجرت تفکر Sonnet را مقایسه کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-24-claude-opus-5-5-added"><span><strong>پرچم‌دار جدید Anthropic: Claude Opus 5.5</strong><span>از <code>claude-opus-5-5</code> برای کدنویسی طولانی‌مدت و کار دانشی با تفکر تطبیقی همیشه‌فعال، پنجره ورودی یک‌میلیون‌توکنی و پشتیبانی کامل Chat Completions، Messages و Responses استفاده کنید. از سطح ۱ در دسترس است؛ قیمت هر یک میلیون توکن ورودی ۴ دلار و خروجی ۲۰ دلار است.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added"><span><strong>جدید: GPT-6 Sol، GPT-6 Luna و Grok 4.7</strong><span>از <code>gpt-6-sol</code> و <code>gpt-6-luna</code> از OpenAI برای استدلال کم‌هزینه، یا از <code>grok-4.7</code> از xAI برای کدنویسی طولانی‌مدت و کار دانشی استفاده کنید. هر سه از Chat Completions و Messages پشتیبانی می‌کنند؛ پشتیبانی Responses برای Sol و Luna کامل و برای Grok جزئی است.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added"><span><strong>جدید: GPT Image 2.5، DeepSeek V4.1 Flash و Grok 4.6</strong><span>با Flare یا Sunburst تصویر بسازید و ویرایش کنید و با DeepSeek V4.1 Flash یا Grok 4.6 عامل‌های استدلالی بسازید. تعرفه کم‌بار DeepSeek شبانه‌روزی است؛ پیش از تغییر مسیریابی V4-Pro در ۲۳ شهریور (2026-09-14) مهاجرت کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-05-gpt-6-astra-added"><span><strong>پرچم‌دار جدید OpenAI: GPT-6 Astra</strong><span>از <code>gpt-6-astra</code> برای کارهای دشوار رایانه‌ای، مهندسی نرم‌افزار، حرفه‌ای، علمی، امنیت سایبری و زمینه بلند با پشتیبانی کامل Chat Completions، Messages و Responses استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-02-claude-fable-5-1-added"><span><strong>پرچم‌دار جدید Anthropic: Claude Fable 5.1</strong><span>از <code>claude-fable-5-1</code> برای کدنویسی پیشرفته، پژوهش، کار دانشی و عامل‌های طولانی‌مدت با پنجره ورودی ۱M، تفکر تطبیقی همیشه‌فعال و هزینه کمتر خواندن از کش استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added"><span><strong>مدل‌های جدید Alibaba: Qwen3.8-27B و Qwen3.8-Flash</strong><span>از <code>qwen3.8-flash</code> برای گردش‌کارهای کم‌هزینه بینایی و عامل‌ها، یا از <code>qwen3.8-27b</code> برای استدلال بینایی-زبان متراکم و فشرده با کنترل انعطاف‌پذیر تفکر استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-08-26-glm-5-3-flash-added"><span><strong>پرچم‌دار جدید Z.AI: GLM-5.3-Flash</strong><span>از <code>glm-5.3-flash</code> برای گردش‌کارهای چندوجهی کدنویسی و عامل‌ها با ۳۲۰B پارامتر کل، ۱۸B پارامتر فعال، پنجره ورودی ۹۹۱K و قیمت تشویقی تا ۱۸ شهریور ۱۴۰۵ استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-08-18-glm-5-3-added"><span><strong>پرچم‌دار Z.AI: GLM-5.3</strong><span>گردش‌کارهای پیچیده کدنویسی و عامل‌های بلندمدت را با تفکر اجباری، سطح استدلال انتخابی و پنجره زمینه ۱ میلیون توکنی بسازید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-08-15-qwen3-8-open-weight-and-qwen-image-3-added"><span><strong>مدل‌های جدید Alibaba: مدل وزن‌باز Qwen3.8 و Qwen Image 3</strong><span>از qwen3.8-2.4t-a95b برای workloadهای متنی با تفکر اجباری یا از qwen-image-3.0-pro و qwen-image-3.0 برای تولید و ویرایش تصویر استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/news/2026-09-03-gemini-3-8-flash-added"><span><strong>مدل جدید: Gemini 3.8 Flash</strong><span>عامل‌های کدنویسی بلندمدت و گردش‌کارهای مبتنی بر ابزار را با نرخ تشویقی تا ۱۰ دی ۱۴۰۵ (December 31, 2026) بسازید. نام مستعار <code>gemini-flash-latest</code> اکنون به این مدل اشاره می‌کند.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/models/muse-glimmer-30b"><span><strong>جدید: Muse Glimmer 30B</strong><span>از مدل چندوجهی و عاملی Meta روی Fireworks.ai برای reasoning، ابزار، کدنویسی و کار چندزبانه استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/models/nemotron-3.5-lightning"><span><strong>جدید: Nemotron 3.5 Lightning</strong><span>از مدل کارآمد NVIDIA با ۳۰B پارامتر کل و ۳B فعال برای reasoning، کدنویسی، RAG و عامل‌ها استفاده کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/guides/prompt-caching"><span><strong>بهبود چشمگیر مسیریابی cache</strong><span>مسیریابی هر کاربر و مدل اکنون آخرین زیرساخت موفق را در یک بازه sticky و rolling پانزده‌دقیقه‌ای ترجیح می‌دهد.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/models/index"><span><strong>مرور مدل‌ها</strong><span>خانواده مدل، نوع ورودی و خروجی، طول زمینه و نقاط پایانی پشتیبانی‌شده را مقایسه کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
    <a class="docs-home-link-row" href="/fa/pricing"><span><strong>بررسی قیمت‌گذاری</strong><span>پیش از انتخاب مدل برای محیط تولید، قیمت فعلی توکن و رسانه را ببینید.</span></span><span class="docs-row-arrow" aria-hidden="true">←</span></a>
  </div>
</section>

<section class="docs-popular-guides" aria-labelledby="popular-guides-title">
  <div class="docs-section-heading">
    <h2 id="popular-guides-title">راهنماهای محبوب و کارهای رایج توسعه‌دهندگان</h2>
    <p>پس از یک درخواست موفق، رفتار قابل اتکای برنامه را پیاده‌سازی کنید.</p>
  </div>
  <div class="docs-guide-links">
    <a href="/fa/guides/structured-outputs"><strong>بازگرداندن داده ساختاریافته</strong><span>پاسخ را به اسکیمایی محدود کنید که برنامه بتواند اعتبارسنجی کند.</span></a>
    <a href="/fa/guides/function-calling"><strong>فراخوانی توابع برنامه</strong><span>به مدل اجازه درخواست ابزار بدهید و اجرای آن را در کد کنترل کنید.</span></a>
    <a href="/fa/guides/streaming-responses"><strong>پخش جریانی پاسخ</strong><span>هم‌زمان با رسیدن رویدادهای پاسخ، خروجی مفید را نمایش دهید.</span></a>
    <a href="/fa/guides/production-best-practices"><strong>آماده‌سازی برای محیط تولید</strong><span>امنیت، پایداری، تاخیر و هزینه را از قبل برنامه‌ریزی کنید.</span></a>
  </div>
</section>

<section class="docs-support-status" aria-labelledby="support-status-title">
  <div class="docs-section-heading">
    <h2 id="support-status-title">پشتیبانی و وضعیت سرویس</h2>
    <p>برای حساب کاربری یا یکپارچه‌سازی خود کمک بگیرید یا بررسی کنید آیا رویداد فعالی روی درخواست‌ها اثر می‌گذارد.</p>
  </div>
  <div class="docs-home-link-rows">
    <a class="docs-home-link-row" href="https://chat.avalai.ir/platform/support/create-ticket"><span><strong>ایجاد تیکت پشتیبانی</strong><span>جزئیات درخواست و زمینه خطا را برای بررسی پشتیبانی ارسال کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">↖</span></a>
    <a class="docs-home-link-row" href="https://status.avalai.ir"><span><strong>مشاهده وضعیت سرویس</strong><span>وضعیت فعلی سرویس‌ها و رخدادهای اخیر را بررسی کنید.</span></span><span class="docs-row-arrow" aria-hidden="true">↖</span></a>
  </div>
</section>
