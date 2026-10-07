---
hasH1: true
---

# API تکمیل گفتگو (Chat Completions)

API تکمیل گفتگو هسته اصلی پلتفرم AvalAI است که به شما امکان می‌دهد پاسخ‌های محاوره‌ای را از مدل‌های مختلف هوش مصنوعی، از جمله GPT-6.1 Sol و خانواده GPT-6 از OpenAI (Astra، Sol و Luna)، خانواده GPT-5.6 (GPT-5.6 Sol، Terra و Luna)، Claude Sonnet 5.5، Claude Opus 5.5، Claude Fable 5.1 و Claude Opus 5 از Anthropic، Grok 4.7، Grok 4.6، Grok 4.5 و Grok 4.3 از xAI، GLM-5.3-Flash و GLM-5.3 از Z.AI، Kimi K3 از Moonshot، Gemini 3.8 Flash، Gemini 3.7 Flash، Gemini 3.6 Flash، Gemini 3.5 Flash-Lite و Gemma 4 از Google، مدل‌های Qwen3.8-Max، Qwen3.8-Flash، Qwen3.8-27B و Qwen3.7-Plus از Alibaba، مدل DeepSeek V4.1 Flash از طریق `deepseek-v4.1-flash`، Nemotron-3-120B از Cloudflare، Muse Glimmer 30B، Nemotron 3.5 Lightning و Nemotron-3-Ultra از Fireworks.ai و مدل‌های M3 از MiniMax تولید کنید.

> **GPT-6.1 Sol:** برای استدلال در کدنویسی و اسناد حرفه‌ای از `gpt-6.1-sol` با حداکثر ۹۲۲٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی استفاده کنید. پشتیبانی از سطح ۱ در `v1/chat/completions`، `v1/messages` و `v1/responses` کامل است. نرخ استاندارد هر میلیون توکن ورودی، ورودی کش‌شده و خروجی به‌ترتیب $2.00، $0.10 و $10.00 است؛ ورودی بیش از ۲۷۲ هزار توکن تعرفه بالاتری دارد. در شروع تلاش استدلالی ارسال نکنید؛ فراداده محلی از `none` و `minimal` پشتیبانی نمی‌کند. [راهنمای OpenAI](fa/providers/openai.md#gpt-6-1-sol) و [قیمت‌های انتشار](fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added.md) را ببینید.

> **Claude Sonnet 5.5:** برای کدنویسی با دامنه مشخص و کار اسنادی از `claude-sonnet-5-5` با حداکثر ۱٬۰۰۰٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی استفاده کنید. پشتیبانی از سطح ۱ در `v1/chat/completions` و `v1/messages` کامل و در `v1/responses` **جزئی** است. کنترل نمونه‌گیری پشتیبانی‌نشده، پیش‌پرکردن پاسخ دستیار و اجبار به استفاده از ابزار را ارسال نکنید. گردش‌کارهای قبلی با تفکر غیرفعال باید به `between_tools` منتقل شوند؛ پیش‌فرض تلاش Claude Platform مقدار `high` است، نه `medium` در برنامه‌های Claude و Claude Code. [راهنمای Anthropic](fa/providers/anthropic.md#claude-sonnet-5-5) و [نکات مهاجرت](fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added.md) را ببینید.

> **Claude Opus 5.5:** از `claude-opus-5-5` برای عامل‌های کدنویسی طولانی‌مدت و کار دانشی با پنجره ورودی ۱٬۰۰۰٬۰۰۰ توکنی، حداکثر خروجی ۱۲۸٬۰۰۰ توکن، بینایی، ورودی PDF، ابزارها، خروجی ساختاریافته و حافظه نهان پرامپت استفاده کنید. پشتیبانی در `v1/chat/completions`، `v1/messages` و `v1/responses` کامل است؛ دسترسی به سطح ۱ یا بالاتر نیاز دارد. تفکر همیشه فعال است و تلاش پیش‌فرض `medium` است. اجبار به استفاده از ابزار پشتیبانی نمی‌شود. [راهنمای Anthropic](fa/providers/anthropic.md#claude-opus-5-5) و [نکات مهاجرت](fa/news/2026-09-24-claude-opus-5-5-added.md) را ببینید.

> **GPT-6 Sol و GPT-6 Luna:** از `gpt-6-sol` برای کدنویسی و کار حرفه‌ای با بودجه محدود، یا از `gpt-6-luna` برای گردش‌کارهای پرترافیک با هزینه کمتر استفاده کنید. هر دو از استدلال، درک تصویر، ابزارها، خروجی ساختاریافته، ورودی PDF و حافظه نهان پرامپت پشتیبانی می‌کنند و حداکثر ۹۲۲٬۰۰۰ توکن ورودی و ۱۲۸٬۰۰۰ توکن خروجی دارند. پشتیبانی در `v1/chat/completions`، `v1/messages` و `v1/responses` کامل است. [راهنمای OpenAI](fa/providers/openai.md#gpt-6-sol-و-gpt-6-luna) را ببینید.

> **Grok 4.7:** از `grok-4.7` از xAI برای عامل‌های کدنویسی طولانی‌مدت، راستی‌آزمایی و کار دانشی استفاده کنید. این مدل از بینایی، استدلال، ابزارها، خروجی ساختاریافته و حافظه نهان پشتیبانی می‌کند؛ سقف‌های جداگانه ورودی و خروجی در فهرست هر کدام ۵۰۰٬۰۰۰ توکن است. پشتیبانی در `v1/chat/completions` و `v1/messages` کامل و در `v1/responses` **جزئی** است؛ برابری کامل ابزارهای میزبانی‌شده یا گردش‌کارهای دارای وضعیت ذخیره‌شده را فرض نکنید. تا زمانی که پشتیبانی مسیر تأیید نشده، پارامتر `reasoning_effort` را ارسال نکنید. [راهنمای xAI](fa/providers/xai.md#grok-4-7) و [قیمت‌های این انتشار](fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added.md) را ببینید.

> **GPT-6 Astra:** از `gpt-6-astra` برای بارهای کاری دشوار در استفاده از رایانه، مهندسی نرم‌افزار، امور حرفه‌ای، علوم، ریاضیات، امنیت سایبری و زمینه‌های طولانی استفاده کنید. این مدل کنترل تلاش استدلالی دارد و در `v1/chat/completions`،‏ `v1/messages` و `v1/responses` به‌طور کامل پشتیبانی می‌شود. [مستندات مدل‌های OpenAI](fa/providers/openai.md#gpt-6-astra) را ببینید.

> **Claude Fable 5.1:** از `claude-fable-5-1` برای کدنویسی پیشرفته، تحلیل علت ریشه‌ای، کار دانشی، پژوهش علمی، استفاده از رایانه و عامل‌های طولانی‌مدت استفاده کنید. این مدل پنجره ورودی ۱M، حداکثر ۱۲۸K توکن خروجی، تفکر تطبیقی همیشه‌فعال با تلاش قابل تنظیم، خروجی ساختاریافته، بینایی، ورودی PDF، کش پرامپت و ابزارها را پشتیبانی می‌کند. پشتیبانی در `v1/chat/completions` و `v1/messages` کامل و در `v1/responses` جزئی است و استفاده از آن به سطح ۲ یا بالاتر نیاز دارد. [مستندات مدل‌های Anthropic](fa/providers/anthropic.md#claude-fable-51) را ببینید.

> **GLM-5.3-Flash:** از `glm-5.3-flash` برای کدنویسی چندوجهی کارآمد، درک تصویری، استفاده از ابزار و گردش‌کارهای عاملی با ۳۲۰B پارامتر کل و ۱۸B پارامتر فعال استفاده کنید. این مدل 991,000 توکن ورودی و حداکثر 128,000 توکن خروجی را پشتیبانی می‌کند. پشتیبانی در `v1/chat/completions` و `v1/messages` کامل و در `v1/responses` جزئی است؛ [مستندات مدل‌های Z.AI](fa/providers/zai.md#glm-53-flash) را ببینید.

> **GLM-5.3:** از `glm-5.3` برای مدل پرچم‌دار Z.AI در کدنویسی، عامل‌های بلندمدت و تحلیل امنیتی مجاز استفاده کنید. تفکر اجباری است: `thinking.type: "enabled"` را بفرستید و برای `reasoning_effort` یکی از مقدارهای `low`، `high` یا `max` را انتخاب کنید؛ درخواست‌هایی که تفکر را غیرفعال می‌کنند با خطا روبه‌رو می‌شوند. این مدل از `v1/chat/completions` و `v1/messages` پشتیبانی می‌کند و برای `v1/responses` پشتیبانی جزئی دارد؛ [مستندات مدل‌های Z.AI](fa/providers/zai.md#glm-53) را ببینید.

> **مدل‌های جدید Fireworks.ai:** از `muse-glimmer-30b` برای مدل چندوجهی و چندزبانه Meta با قابلیت عاملی و reasoning قابل تنظیم استفاده کنید. `nemotron-3.5-lightning` مدل کارآمد NVIDIA با ۳۰B پارامتر کل و ۳B فعال برای reasoning و کدنویسی است. هر دو در `v1/chat/completions` و `v1/messages` پشتیبانی کامل و در `v1/responses` پشتیبانی جزئی دارند؛ [مستندات Fireworks.ai](fa/providers/fireworksai.md) را ببینید.

> **Claude Opus 5:** از `claude-opus-5` برای مهندسی نرم‌افزار دشوار، تحلیل علت ریشه‌ای، کار دانشی، استفاده از کامپیوتر، تحلیل علمی و عامل‌های طولانی‌مدت استفاده کنید. این مدل پنجره ورودی ۱M، حداکثر ۱۲۸K توکن خروجی، تفکر تطبیقی، خروجی ساختاریافته، بینایی، ورودی PDF، کش پرامپت و ابزارها را پشتیبانی می‌کند. پشتیبانی در `v1/chat/completions` و `v1/messages` کامل و در `v1/responses` جزئی است؛ [مستندات مدل‌های Anthropic](fa/providers/anthropic.md) را ببینید.

> **Gemini 3.8 Flash:** از `gemini-3.8-flash` برای کدنویسی بلندمدت، عامل‌های خودکار، استدلال چندمرحله‌ای، استفاده تکرارشونده از ابزار و کارهای تخصصی حرفه‌ای استفاده کنید. این مدل از `v1/chat/completions`، API بومی Gemini یعنی `v1beta/` و `v1/messages` پشتیبانی می‌کند و در `v1/responses` پشتیبانی جزئی دارد. قیمت تشویقی تا ۳۱ دسامبر ۲۰۲۶ (۱۴۰۵-۱۰-۱۰) برای هر ۱ میلیون توکن برابر $0.75 ورودی، $0.075 ورودی ذخیره‌شده و $3.75 خروجی است. نام مستعار `gemini-flash-latest` اکنون به `gemini-3.8-flash` اشاره می‌کند؛ [مستندات مدل‌های Google](fa/providers/google.md) را ببینید.

> **Kimi K3:** برای پرچم‌دار Moonshot AI با زمینه ۱M، بینایی بومی و استدلال همیشه‌فعال از `kimi-k3` استفاده کنید. این مدل از `v1/chat/completions` و `v1/messages` به‌طور کامل و از `v1/responses` به‌صورت جزئی پشتیبانی می‌کند. alias مدل `kimi-latest` اکنون به `kimi-k3` اشاره می‌کند و همان قیمت را دارد. K3 در حال حاضر از `reasoning_effort: "max"` پشتیبانی می‌کند؛ فیلدهای sampling ثابت مانند `temperature` و `top_p` را ارسال نکنید.
>
> **مدل‌های Qwen3.8:** برای پرچم‌دار چندوجهی مدیریت‌شده Alibaba با تفکر اختیاری، زمینه ۱M و حداکثر خروجی ۱۲۸K از `qwen3.8-max` استفاده کنید. برای مدل مدیریت‌شده کم‌هزینه (نام مستعار `qwen3.8-flash-next`) با ورودی بینایی، تفکر پیش‌فرض فعال و زمینه ۲۶۲K از `qwen3.8-flash` و برای مدل متراکم فشرده ۲۷ میلیارد پارامتری بینایی-زبان با کنترل انعطاف‌پذیر تفکر از `qwen3.8-27b` استفاده کنید. `qwen3.8-2.4t-a95b` مدل وزن‌باز پایه با ۲٫۴ تریلیون پارامتر کل و ۹۵ میلیارد پارامتر فعال است؛ فقط متن را می‌پذیرد، تفکر در آن اجباری است و `reasoning_effort` مقدارهای `low`، `medium` یا `xhigh` را می‌پذیرد. هر چهار route در `v1/chat/completions` و `v1/messages` پشتیبانی کامل و در `v1/responses` پشتیبانی جزئی دارند؛ [مستندات مدل‌های Alibaba](fa/providers/alibaba.md) را ببینید.
>
> **DeepSeek V4.1 Flash:** از `deepseek-v4.1-flash` برای بینایی بومی، حالت‌های تفکری و غیرتفکری، ابزارها و حافظه نهان پرامپت استفاده کنید. فهرست AvalAI سقف ۱٬۰۰۰٬۰۰۰ توکن ورودی و ۳۹۳٬۲۱۶ توکن خروجی را ثبت کرده است؛ ارائه‌دهنده خروجی را ۳۸۴K می‌نامد. قیمت ثابت شبانه‌روزی به دلار آمریکا برای هر ۱ میلیون توکن، $0.15 ورودی، $0.003 ورودی ذخیره‌شده و $0.60 خروجی است؛ زمان‌بندی، دو برابر شدن قیمت در ساعات اوج یا نصف کردن دوباره تعرفه‌ها مطرح نیست. **در ۱۴۰۵-۰۶-۲۳ / (2026-09-14) ساعت 04:00 UTC، مسیر `deepseek-v4-pro` به V4.1 Flash تغییر خواهد کرد و تعرفه V4.1 Flash اعمال خواهد شد.** از هم‌اکنون شناسه جدید را به کار بگیرید و پیش از تغییر مسیر آزمایش کنید. [راهنمای DeepSeek](fa/providers/deepseek.md) را ببینید.
>
> **Grok 4.6:** از `grok-4.6` برای عامل‌های طولانی‌مدت، کدنویسی، کار دانشی و برنامه‌های بصری تعاملی استفاده کنید، نه تولید تصویر. این مدل بینایی، استدلال، ابزارها، خروجی ساختاریافته و حافظه نهان را پشتیبانی می‌کند؛ سقف ورودی و خروجی در فهرست، هر کدام ۵۰۰٬۰۰۰ توکن است. برای ورودی حداکثر ۲۰۰ هزار توکن، قیمت هر ۱ میلیون توکن به دلار آمریکا برابر $2.00 ورودی، $0.50 ورودی ذخیره‌شده و $6.00 خروجی است؛ بالاتر از این مرز، این مبلغ‌ها به‌ترتیب $4.00، $1.00 و $12.50 هستند. [راهنمای xAI](fa/providers/xai.md#grok-46) را ببینید.
>
> **سازگاری نقاط پایانی هر دو مدل:** `v1/chat/completions` و `v1/messages` پشتیبانی می‌شوند؛ پشتیبانی `v1/responses` جزئی است. برابری کامل ابزارهای داخلی Responses یا گردش‌کارهای دارای وضعیت ذخیره‌شده را فرض نکنید. پیش از مهاجرت، گردش‌کار دقیق خود را بررسی کنید. [اعلامیه ۱۴۰۵-۰۶-۲۰ / (2026-09-11)](fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added.md) را ببینید.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/chat/completions
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    reasoning={"effort": "medium"},
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

## بدنه درخواست (Request Body)

| پارامتر                  | نوع              | الزامی | توضیحات                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| ------------------------ | ---------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `model`                  | string           | بله    | شناسه مدلی که باید استفاده شود. برای گزینه‌های موجود به [مدل‌ها](fa/models/model-details.md) مراجعه کنید.                                                                                                                                                                                                                                                                                                                                                           |
| `messages`               | array            | بله    | آرایه‌ای از اشیا پیام که تاریخچه گفتگو را نشان می‌دهد.                                                                                                                                                                                                                                                                                                                                                                                                              |
| `temperature`            | number           | خیر    | دمای نمونه‌برداری بین ۰ و ۲. مقادیر بالاتر مانند ۰.۸ خروجی را تصادفی‌تر می‌کنند، در حالی که مقادیر پایین‌تر مانند ۰.۲ آن را متمرکزتر می‌کنند. پیش‌فرض ۱ است.                                                                                                                                                                                                                                                                                                        |
| `top_p`                  | number           | خیر    | جایگزینی برای دما، نمونه‌برداری هسته‌ای (nucleus sampling). پیش‌فرض ۱ است.                                                                                                                                                                                                                                                                                                                                                                                          |
| `n`                      | integer          | خیر    | تعداد انتخاب‌های تکمیل گفتگو برای تولید. پیش‌فرض ۱ است.                                                                                                                                                                                                                                                                                                                                                                                                             |
| `stream`                 | boolean          | خیر    | اگر روی true تنظیم شود، دلتاهای پیام جزئی ارسال خواهند شد. پیش‌فرض false است.                                                                                                                                                                                                                                                                                                                                                                                       |
| `stream_options`         | object           | خیر    | گزینه‌های جریان‌دهی پاسخ. فقط همراه `stream: true` استفاده کنید؛ پشتیبانی به route و SDK وابسته است.                                                                                                                                                                                                                                                                                                                                                                |
| `modalities`             | array            | خیر    | نوع‌های خروجی که می‌خواهید مدل تولید کند. بیشتر مدل‌های chat مقدار `["text"]` برمی‌گردانند؛ خروجی صوتی به پشتیبانی مدل/route و پارامتر `audio` نیاز دارد.                                                                                                                                                                                                                                                                                                           |
| `audio`                  | object           | خیر    | پیکربندی خروجی صوتی وقتی `modalities` شامل `"audio"` است. برای بیشتر workflowهای AvalAI، routeهای اختصاصی [Audio](fa/api-reference/audio.md) یا Realtime را ترجیح دهید.                                                                                                                                                                                                                                                                                             |
| `prediction`             | object           | خیر    | محتوای خروجی پیش‌بینی‌شده برای rewriteهای حساس به latency که بیشتر completion tokenها از قبل مشخص هستند. پشتیبانی به provider/model وابسته است؛ [خروجی‌های پیش‌بینی‌شده](fa/guides/predicted-outputs.md) را ببینید.                                                                                                                                                                                                                                                 |
| `stop`                   | string or array  | خیر    | حداکثر ۴ دنباله که API تولید توکن‌های بیشتر را در آنجا متوقف می‌کند.                                                                                                                                                                                                                                                                                                                                                                                                |
| `max_completion_tokens`  | integer          | خیر    | سقف توکن‌های تولیدی، شامل خروجی قابل مشاهده و توکن‌های reasoning پنهان. اگر reasoning تمام بودجه را مصرف کند، مدل ممکن است پیش از تولید متن قابل مشاهده با `finish_reason: "length"` متوقف شود؛ حاشیه امن بگذارید یا effort را کاهش دهید. بخش [بودجه توکن reasoning](fa/guides/reasoning.md#تخصیص-فضا-برای-استدلال) را ببینید.                                                                                                                                      |
| `max_tokens`             | integer          | خیر    | تنظیم قدیمی سقف توکن خروجی. در شکل فعلی API OpenAI به نفع `max_completion_tokens` deprecated شده و با برخی مدل‌های reasoning سازگار نیست. هرجا برای مدل reasoning قابل استفاده باشد، همان هشدار بودجه مشترک برقرار است.                                                                                                                                                                                                                                             |
| `presence_penalty`       | number           | خیر    | عددی بین -۲.۰ و ۲.۰. مقادیر مثبت توکن‌های جدید را بر اساس اینکه آیا تاکنون در متن ظاهر شده‌اند جریمه می‌کنند. پیش‌فرض ۰ است.                                                                                                                                                                                                                                                                                                                                        |
| `frequency_penalty`      | number           | خیر    | عددی بین -۲.۰ و ۲.۰. مقادیر مثبت توکن‌های جدید را بر اساس فراوانی آن‌ها در متن تاکنون جریمه می‌کنند. پیش‌فرض ۰ است.                                                                                                                                                                                                                                                                                                                                                 |
| `logit_bias`             | object           | خیر    | احتمال ظاهر شدن توکن‌های مشخص شده در تکمیل را تغییر دهید.                                                                                                                                                                                                                                                                                                                                                                                                           |
| `logprobs`               | boolean          | خیر    | در صورت پشتیبانی، log probability توکن‌های خروجی را برمی‌گرداند.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `top_logprobs`           | integer          | خیر    | تعداد محتمل‌ترین توکن‌ها در هر موقعیت توکن خروجی، از ۰ تا ۲۰. به `logprobs: true` و پشتیبانی مدل/route نیاز دارد.                                                                                                                                                                                                                                                                                                                                                   |
| `metadata`               | object           | خیر    | حداکثر ۱۶ جفت کلید/مقدار برای فیلتر کردن completionهای ذخیره‌شده و query در dashboard/API. کلیدها حداکثر ۶۴ و مقدارها حداکثر ۵۱۲ کاراکتر دارند.                                                                                                                                                                                                                                                                                                                     |
| `safety_identifier`      | string           | خیر    | شناسه پایدار و حفظ‌کننده حریم خصوصی برای پایش سوءاستفاده. از hash پایدار یا شناسه داخلی opaque با حداکثر 64 کاراکتر استفاده کنید و PII خام نفرستید. [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md) را ببینید.                                                                                                                                                                                                                                          |
| `prompt_cache_key`       | string           | خیر    | کلید bucket کردن cache برای prefixهای تکراری مشابه. آن را opaque و پایدار برای assistant، tenant، policy یا schema نگه دارید؛ برای پایش سوءاستفاده `safety_identifier` را ترجیح دهید. [Prompt caching](fa/guides/prompt-caching.md) را ببینید.                                                                                                                                                                                                                      |
| `prompt_cache_retention` | string           | خیر    | سیاست legacy برای حداکثر ماندگاری مدل‌های پیش از GPT-5.6. این فیلد برای GPT-5.6 و خانواده‌های بعدی deprecated است؛ OpenAI در نسل جدید از `prompt_cache_options.ttl` استفاده می‌کند و pass-through کنترل‌های جدید در AvalAI به route وابسته است. کنترل پشتیبانی‌نشده را حذف کنید.                                                                                                                                                                                    |
| `moderation`             | object           | خیر    | پیکربندی inline moderation، مثلا `{ "model": "omni-moderation-latest" }`، در صورت فعال بودن برای route/model انتخابی. اگر در دسترس نیست، [`/v1/moderations`](fa/api-reference/moderation.md) را جداگانه فراخوانی کنید.                                                                                                                                                                                                                                              |
| `user`                   | string           | خیر    | فیلد قدیمی شناسه کاربر نهایی. برای پایش سوءاستفاده از `safety_identifier` و برای bucket کردن cache از `prompt_cache_key` استفاده کنید.                                                                                                                                                                                                                                                                                                                              |
| `response_format`        | object           | خیر    | محدودکننده فرمت خروجی. برای Structured Outputs در مدل‌های دارای پایبندی به schema از `{"type":"json_schema","json_schema":...}` استفاده کنید، یا برای fallback حالت JSON از `{"type":"json_object"}`. برای workflowهای جدید structured output، `text.format` در `/v1/responses` را ترجیح دهید.                                                                                                                                                                      |
| `reasoning_effort`       | string           | خیر    | کنترل تلاش استدلال برای مدل‌های پشتیبانی‌شده. مقدارهای مجاز و پیش‌فرض به مدل وابسته‌اند؛ آن‌ها را برای مسیر انتخابی AvalAI بررسی کنید. DeepSeek-V4-Flash-0731 از `low`، `high` و `max` پشتیبانی می‌کند؛ Claude Fable 5.1 و Claude Opus 5 از تفکر تطبیقی اختصاصی ارائه‌دهنده و `output_config.effort` در `extra_body` استفاده می‌کنند. تفکر در Claude Fable 5.1 همیشه فعال است.                                                                                      |
| `verbosity`              | string           | خیر    | در مدل‌های پشتیبانی‌شده طول/جزئیات پاسخ نهایی را (`low`، `medium` یا `high`) بدون تغییر عمق reasoning کنترل می‌کند.                                                                                                                                                                                                                                                                                                                                                 |
| `seed`                   | integer          | خیر    | اگر مشخص شود، سیستم بهترین تلاش خود را برای نمونه‌برداری قطعی انجام خواهد داد.                                                                                                                                                                                                                                                                                                                                                                                      |
| `store`                  | boolean          | خیر    | آیا chat completion برای بازیابی بعدی، distillation یا evals ذخیره شود، وقتی route/account انتخابی از stored chat completions پشتیبانی کند.                                                                                                                                                                                                                                                                                                                         |
| `tools`                  | array            | خیر    | لیستی از ابزارهایی که مدل ممکن است فراخوانی کند.                                                                                                                                                                                                                                                                                                                                                                                                                    |
| `tool_choice`            | string or object | خیر    | کنترل می‌کند که کدام ابزار (در صورت وجود) توسط مدل فراخوانی شود.                                                                                                                                                                                                                                                                                                                                                                                                    |
| `parallel_tool_calls`    | boolean          | خیر    | آیا فراخوانی‌های function/tool موازی مجاز باشد. برای ابزارهایی که state را تغییر می‌دهند یا execution ترتیبی می‌خواهند مقدار `false` بگذارید.                                                                                                                                                                                                                                                                                                                       |
| `web_search_options`     | object           | خیر    | گزینه‌های web search سازگار با Chat وقتی مدل OpenAI-style انتخابی از web search داخلی پشتیبانی کند. برای retrieval مستقل از provider، [`/v1/search`](fa/api-reference/search.md) را ترجیح دهید.                                                                                                                                                                                                                                                                     |
| `service_tier`           | string           | خیر    | سطح سرویس مورد استفاده برای این درخواست. AvalAI به‌طور عمومی `"default"` (پیش‌فرض) و `"flex"` را پشتیبانی می‌کند. سطح flex ۵۰٪ کاهش قیمت برای مدل‌های منتخب OpenAI ارائه می‌دهد اما تاخیر بالاتر دارد و ممکن است تایم‌اوت شود (تا ۹۰۰ ثانیه). بعضی مثال‌های OpenAI ممکن است `"priority"` داشته باشند؛ در AvalAI از `"default"` استفاده کنید مگر اینکه priority processing صراحتا برای حساب شما فعال شده باشد. [قیمت‌گذاری](fa/pricing.md#سطح-سرویس-flex) را ببینید. |

?> پشتیبانی پارامترها به مدل و provider وابسته است. مدل‌های reasoning جدید ممکن است برخی فیلدهای قدیمی sampling، stop یا token را نادیده بگیرند یا reject کنند، و ابزارهای hosted در AvalAI به route/account وابسته‌اند. اگر یک workflow جدید OpenAI-style با ابزار، state یا reasoning می‌سازید، قبل از انتخاب Chat Completions این صفحه را با [Responses](fa/api-reference/responses.md) مقایسه کنید.

برای `response_format`، هر زمان مدل و route انتخابی پشتیبانی می‌کنند، `json_schema` را به `json_object` ترجیح دهید. حالت JSON فقط معتبر بودن syntax JSON را تضمین می‌کند؛ کلیدهای الزامی، مقدارهای enum یا typeهای برنامه شما را تضمین نمی‌کند، پس نتیجه parse شده را در برنامه validate کنید. برای طراحی schema، مدیریت refusal و migration به `text.format` در Responses، [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md) را ببینید.

**محدودیت پارامترهای Claude Opus 5.5:** تنظیم غیرفعال‌سازی تفکر، بودجه ثابت تفکر، پیام دستیار از پیش تکمیل‌شده یا فیلدهای نمونه‌برداری پشتیبانی‌نشده مانند `temperature` و `top_p` را نفرستید. برای تنظیم تلاش، از `thinking` تطبیقی و `output_config.effort` در `extra_body` استفاده کنید و با `medium` شروع کنید؛ نگاشت `reasoning_effort` ارائه‌دهنده دیگری را فرض نکنید. تنظیمات انتخاب ابزاری را که فراخوانی را اجباری می‌کنند، حذف کنید. در نوبت‌های بعد، بلوک‌های کامل تفکر و ابزار دستیار را حفظ کنید و با تنظیم پیش‌فرض نمایش به متن قابل مشاهده میان فراخوانی‌های ابزار متکی نباشید. بخش [استدلال Claude Opus 5.5](fa/guides/reasoning.md#claude-opus-5-5) را ببینید.

### شی پیام (Message Object)

هر پیام در آرایه `messages` باید ساختار زیر را داشته باشد:

| پارامتر        | نوع             | الزامی | توضیحات                                                                                                                                                                              |
| -------------- | --------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `role`         | string          | بله    | نقش نویسنده پیام. نقش‌های رایج عبارت‌اند از `developer`، `system`، `user`، `assistant` و `tool`. بسته به پشتیبانی مدل، برای دستورهای پایدار از `developer` یا `system` استفاده کنید. |
| `content`      | string or array | بله    | محتوای پیام. می‌تواند یک رشته یا آرایه‌ای از بخش‌های محتوا هنگام استفاده از ورودی‌های چندوجهی باشد.                                                                                  |
| `name`         | string          | خیر    | نام نویسنده این پیام. برای نقش‌های `tool` الزامی است.                                                                                                                                |
| `tool_call_id` | string          | خیر    | برای پیام‌های نقش `tool` الزامی است. شناسه فراخوانی ابزاری که این پیام به آن پاسخ می‌دهد.                                                                                            |

## مثال‌ها

### شروع سریع با GPT-6.1 Sol و Claude Sonnet 5.5

هر دو مدل ساختار ساده Chat Completions زیر را می‌پذیرند. در این مثال عمداً کنترل نمونه‌گیری و تلاش استدلالی ارسال نشده است. برای تفکر تطبیقی اختصاصی Sonnet و `output_config.effort` از [مثال بومی Messages](fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added.md#claude-sonnet-5-5-با-sdk-بومی-anthropic) استفاده کنید و نگاشت لایه سازگاری را جداگانه بررسی کنید. نوبت‌های کامل دستیار و ابزار را حفظ کنید و برای استدلال فضای کافی در خروجی بگذارید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
for model in ("gpt-6.1-sol", "claude-sonnet-5-5"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag.",
            }
        ],
    )
    print(model, response.choices[0].message.content)
```

### شروع سریع با Claude Opus 5.5

بدون تنظیمات اختیاری استدلال یا نمونه‌برداری شروع کنید. تفکر تطبیقی فعال می‌ماند؛ برای استدلال و پاسخ نهایی، توکن تکمیل کافی در نظر بگیرید.

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-5-5",
    "max_completion_tokens": 8192,
    "messages": [
      {"role": "user", "content": "Review a staged database migration and list verification and rollback checks."}
    ]
  }'
```

قیمت هر یک میلیون توکن به دلار آمریکا برابر ۴٫۰۰ برای ورودی، ۰٫۲۰ برای ورودی از حافظه نهان، ۸٫۰۰ برای ایجاد حافظه نهان و ۲۰٫۰۰ برای خروجی است. برای نمونه‌های Messages بومی و Responses، [خبر انتشار](fa/news/2026-09-24-claude-opus-5-5-added.md) را ببینید.

### شروع سریع با GPT-6 Sol، GPT-6 Luna و Grok 4.7

برای هر سه مدل از یک درخواست ساده و یکسان Chat Completions استفاده کنید. برای مقایسه گزینه‌های دیگر، فقط `model` را به `gpt-6-luna` یا `grok-4.7` تغییر دهید. این مدل‌ها تصویر ورودی را درک می‌کنند، اما مدل تولید مستقیم تصویر نیستند. کنترل استدلال Sol و Luna در اینجا با `reasoning_effort` و در Responses با `reasoning.effort` انجام می‌شود؛ مقدارهای مجاز را بررسی کنید و پیش‌فرض مدل دیگری را تعمیم ندهید.

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-6-sol",
    "messages": [
      {"role": "user", "content": "Suggest a concise verification checklist for deploying an API behind a feature flag."}
    ]
  }'
```

پیش از تعیین بودجه خروجی، [قیمت‌گذاری](fa/pricing.md) را بررسی کنید: تعرفه بالاتر ورودی، حافظه نهان و خروجی برای Sol و Luna با ورودی بیش از ۲۷۲ هزار توکن و برای Grok 4.7 با ورودی بیش از ۲۰۰ هزار توکن اعمال می‌شود. این‌ها آستانه‌های قیمت‌گذاری بر اساس طول ورودی هستند، نه حداکثر اندازه زمینه.

### شروع سریع با DeepSeek V4.1 Flash و Grok 4.6

با یک درخواست ساده آغاز کنید. برای مقایسه Grok 4.6، فقط شناسه مدل را به `grok-4.6` تغییر دهید. مقدارهای تلاش استدلالی مدل‌های قدیمی را بدون تأیید پشتیبانی به کار نبرید.

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4.1-flash",
    "messages": [
      {"role": "user", "content": "Review this release plan and propose a concise test checklist: deploy a new API behind a feature flag."}
    ]
  }'
```

### تکمیل گفتگوی پایه

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-6-astra",
  "messages": [
  {
    "role": "system",
    "content": "You are a helpful assistant."
  },
  {
    "role": "user",
    "content": "Hello!"
  }
  ]
}'

```

```python
# مثال پایتون (Python)
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.chat.completions.create(
    model="gpt-5.6-sol",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)

print(response.choices[0].message.content)

```

```javascript
# مثال جاوااسکریپت (JavaScript)
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello!"}
  ]
});

console.log(response.choices[0].message.content);

```

```go
# مثال گو (Go)
package main

import (
"context"
"fmt"
openai "github.com/openai/openai-go"
)

func main() {
    client := openai.NewClient("AVALAI_API_KEY")
    client.BaseURL = "https://api.avalai.ir/v1"

    resp, err := client.CreateChatCompletion(
    context.Background(),
    openai.ChatCompletionRequest{
        Model: "gpt-5.6-sol",
        Messages: []openai.ChatCompletionMessage{
            {
                Role: openai.ChatMessageRoleSystem,
                Content: "You are a helpful assistant.",
            },
            {
                Role: openai.ChatMessageRoleUser,
                Content: "Hello!",
            },
        },
    },
    )

    if err != nil {
        fmt.Printf("ChatCompletion error: %v\n", err)
        return
    }

    fmt.Println(resp.Choices[0].Message.Content) // دسترسی صحیح به محتوای پاسخ
}

```

```php
<?php
// مثال PHP برای تکمیل گفتگو از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
'model' => 'gpt-5.6-sol',
'messages' => [
['role' => 'system', 'content' => 'You are a helpful assistant.'], // محتوای سیستم به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
['role' => 'user', 'content' => 'Hello!'] // محتوای کاربر به انگلیسی باقی می‌ماند یا ترجمه می‌شود؟
]
// در صورت نیاز پارامترهای دیگری مانند دما، حداکثر توکن و غیره را اضافه کنید
// 'temperature' => 0.7,
// 'max_tokens' => 150
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo $response;
} else {
  $responseData = json_decode($response, true);
  if (isset($responseData['choices'][0]['message']['content'])) {
    echo "دستیار: " . $responseData['choices'][0]['message']['content'] . "\n";
  } else {
    echo "پاسخ دریافت شد:\n";
    print_r($responseData);
  }
}
?>

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-sol",
    instructions="You are a helpful assistant.",
    input="Hello!",
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
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "Hello!",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-sol",
    "input": "Hello!",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

## فرمت پاسخ (Response Format)

```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-5.6-sol",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "سلام! چطور می‌توانم امروز به شما کمک کنم؟"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 8,
    "total_tokens": 18
  },
  "service_tier": "default"
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر        | نوع     | توضیحات                                                                                                                                                                |
| -------------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`           | string  | یک شناسه منحصر به فرد برای تکمیل گفتگو.                                                                                                                                |
| `object`       | string  | نوع شی، که همیشه "chat.completion" است.                                                                                                                                |
| `created`      | integer | زمان یونیکس (به ثانیه) ایجاد تکمیل گفتگو.                                                                                                                              |
| `model`        | string  | مدلی که برای تکمیل گفتگو استفاده شده است.                                                                                                                              |
| `choices`      | array   | آرایه‌ای از انتخاب‌های تکمیل گفتگو.                                                                                                                                    |
| `usage`        | object  | یک شی حاوی اطلاعات استفاده از توکن.                                                                                                                                    |
| `moderation`   | object  | نتایج inline moderation ورودی/خروجی، در صورت درخواست و پشتیبانی.                                                                                                       |
| `service_tier` | string  | سطح سرویس استفاده شده برای این درخواست. مقادیر عمومی AvalAI معمولا `"default"` یا `"flex"` هستند؛ `"priority"` فقط در صورت فعال‌سازی صریح برای حساب/route قابل اتکاست. |

### شی انتخاب (Choice Object)

| پارامتر         | نوع     | توضیحات                                                                                                                           |
| --------------- | ------- | --------------------------------------------------------------------------------------------------------------------------------- |
| `message`       | object  | یک شی پیام حاوی محتوای پاسخ.                                                                                                      |
| `finish_reason` | string  | دلیلی که مدل تولید توکن‌ها را متوقف کرده است. می‌تواند "stop", "length", "tool_calls", "content_filter", یا "function_call" باشد. |
| `index`         | integer | شاخص انتخاب در آرایه.                                                                                                             |

### شی استفاده (Usage Object)

| پارامتر             | نوع     | توضیحات                                         |
| ------------------- | ------- | ----------------------------------------------- |
| `prompt_tokens`     | integer | تعداد توکن‌های استفاده شده در پرامپت.           |
| `completion_tokens` | integer | تعداد توکن‌های استفاده شده در تکمیل.            |
| `total_tokens`      | integer | تعداد کل توکن‌های استفاده شده (پرامپت + تکمیل). |

## استریمینگ (Streaming)

برای دریافت پاسخ‌های افزایشی مدل، `stream: true` را در درخواست خود تنظیم کنید:

```javascript
const stream = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [{ role: "user", content: "Write a long story about a dog." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-sol",
    instructions="You are a helpful assistant.",
    input="Write a long story about a dog.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

## فراخوانی تابع / استفاده از ابزار (Function Calling / Tool Use)

می‌توانید ابزارهایی را مشخص کنید که مدل می‌تواند فراخوانی کند:

```javascript
const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  tools: [
    {
      type: "function",
      function: {
        name: "get_weather",
        description: "Get the current weather in a given location",
        strict: true,
        parameters: {
          type: "object",
          properties: {
            location: {
              type: "string",
              description: "The city and state, e.g. San Francisco, CA",
            },
            unit: {
              type: "string",
              enum: ["celsius", "fahrenheit"],
              description: "The temperature unit",
            },
          },
          required: ["location", "unit"],
          additionalProperties: false,
        },
      },
    },
  ],
});
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def get_current_weather(location, unit):
    return {
        "location": location,
        "temperature": "18",
        "unit": unit or "celsius",
        "condition": "partly cloudy",
    }


tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {
                    "type": ["string", "null"],
                    "enum": ["celsius", "fahrenheit", None],
                },
            },
            "required": ["location", "unit"],
            "additionalProperties": False,
        },
    }
]

input_items = [
    {
        "role": "user",
        "content": "هوای سان‌فرانسیسکو را با واحد سانتی‌گراد بگو.",
    }
]

response = client.responses.create(
    model="gpt-5.6-sol",
    input=input_items,
    tools=tools,
)

input_items += response.output

for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        result = get_current_weather(args["location"], args.get("unit"))
        input_items.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": json.dumps(result),
            }
        )

final_response = client.responses.create(
    model="gpt-5.6-sol",
    input=input_items,
    tools=tools,
)

print(final_response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- `tool_calls` به آیتم‌های `response.output` با مقدار `type == "function_call"` تبدیل می‌شود؛ نتیجه را با آیتم `function_call_output` و همان `call_id` برگردانید.
- وقتی tool loop را دستی مدیریت می‌کنید، آیتم‌های قبلی `response.output` را نگه دارید، به‌ویژه برای مدل‌های دارای reasoning.

</details>
<!-- responses-equivalent:end -->

## ورودی و خروجی صوتی

مدل‌های صوتی OpenAI (`gpt-audio` و `gpt-audio-mini`) از ورودی/خروجی صوتی و متنی از طریق Chat Completions API پشتیبانی می‌کنند. این مدل‌ها امکان ایجاد برنامه‌های مکالمه‌ای مبتنی بر صدا با قابلیت‌های پردازش صوتی بومی را فراهم می‌آورند.

### تبدیل متن به گفتار با Gemini 3.8

برای کاربردهای جدید تبدیل متن به گفتار، `gemini-3.8-flash-tts` را برای کیفیت خلاقانه، اجرای احساسی، لهجه‌های منطقه‌ای و ثبات گفت‌وگوهای طولانی انتخاب کنید. برای توان عملیاتی بالا، تأخیر کم و خواندن متن‌های روزمره، `gemini-3.8-flash-lite-tts` مناسب‌تر است. هر دو مدل **متن دریافت می‌کنند و صوت تولید می‌کنند**؛ برای رونویسی، گفت‌وگو با ورودی صوتی، Live API یا استدلال طراحی نشده‌اند.

AvalAI این مدل‌های TTS را فقط از طریق روش‌های بومی `/v1beta/models`، مسیر `/v1/chat/completions` و مسیر `/v1/audio/speech` ارائه می‌دهد. آن‌ها را به `/v1/responses`، `/v1/messages` یا مسیر قدیمی `/v1/text:synthesize` نفرستید. ابتدا پاسخ را با یک مدل گفت‌وگومحور یا استدلالی جداگانه بنویسید و سپس متن نهایی را به TTS بدهید.

```bash
curl --fail-with-body -sS https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "messages": [{"role": "user", "content": "Have a wonderful day!"}],
    "modalities": ["audio"],
    "audio": {"voice": "Zephyr", "format": "pcm16"}
  }' \
  --output chat-speech.json

python3 - <<'PYTHON'
import base64
import json
from pathlib import Path

response = json.loads(Path("chat-speech.json").read_text())
data = response["choices"][0]["message"]["audio"]["data"]
Path("speech.pcm").write_bytes(base64.b64decode(data, validate=True))
PYTHON

ffmpeg -f s16le -ar 24000 -ac 1 -i speech.pcm speech.wav
```

این درخواست متن داده‌شده را می‌خواند؛ به پرسش پاسخ نمی‌دهد و ورودی صوتی نمی‌پذیرد. در Chat، داده Base64 در `choices[0].message.audio.data` قرار دارد، نه `message.content`. خروجی درخواستی `pcm16`، صوت PCM علامت‌دار ۱۶ بیتی با ترتیب little-endian، نرخ ۲۴٬۰۰۰ هرتز و یک کانال است و هدر ندارد؛ آن را در فایل خام ذخیره و با پارامترهای ورودی صریح تبدیل کنید. از `.content` به‌عنوان مسیر جایگزین استفاده نکنید و عبارت `DEPRECATED` را از Base64 حذف نکنید. پاسخ بومی غیرجریانی ۳٫۸ به‌طور پیش‌فرض WAV است؛ پیش از افزودن هدر، `mimeType` را بررسی کنید. برای `speechMetadata` هر بخش بومی و مهاجرت از `gemini-3.1-flash-tts-preview` / `gemini-2.5-flash-tts` / `gemini-2.5-pro-tts`، [راهنمای تبدیل متن به گفتار](fa/guides/text-to-speech.md#migrate-to-gemini-38-tts) را ببینید.

### پارامترهای صوتی

هنگام استفاده از مدل‌های صوتی، می‌توانید پارامترهای اضافی را مشخص کنید:

| پارامتر      | نوع    | الزامی | توضیحات                                                                                                                                                                                                                                                                              |
| ------------ | ------ | ------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `modalities` | array  | خیر    | وجوه خروجی را مشخص می‌کند. از `["text", "audio"]` برای خروجی صوتی استفاده کنید. برای مدل‌های تولید تصویر مانند `gemini-3-pro-image`، `gemini-3.1-flash-image`، `gemini-3.1-flash-lite-image` و `gemini-2.5-flash-image` از `["image", "text"]` استفاده کنید. پیش‌فرض `["text"]` است. |
| `audio`      | object | خیر    | پیکربندی خروجی صوتی. هنگام درخواست خروجی صوتی الزامی است.                                                                                                                                                                                                                            |

### شی پیکربندی صوتی

| پارامتر  | نوع    | الزامی | توضیحات                                                                                                                |
| -------- | ------ | ------ | ---------------------------------------------------------------------------------------------------------------------- |
| `format` | string | خیر    | فرمت خروجی صوتی. گزینه‌ها: `mp3`, `wav`, `pcm16`, `opus`, `aac`, `flac`. پیش‌فرض `mp3` است.                            |
| `voice`  | string | خیر    | صدای مورد استفاده برای خروجی صوتی. گزینه‌ها: `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer`. پیش‌فرض `alloy` است. |

### تولید صوتی پایه

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }'

```

```python
from openai import OpenAI

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gpt-audio",
    messages=[
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."}
    ],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "nova"},
)

# دسترسی به داده‌های صوتی و متن رونویسی
audio_data = response.choices[0].message.audio.data  # صدای رمزگذاری‌شده Base64
transcript = response.choices[0].message.audio.transcript  # متن رونویسی

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
    model: "gpt-audio",
    messages: [
        {
            role: "user",
            content: "محاسبات کوانتومی را به زبان ساده توضیح بده.",
        },
    ],
    modalities: ["text", "audio"],
    audio: {
        format: "mp3",
        voice: "nova",
    },
});

// دسترسی به داده‌های صوتی و متن رونویسی
const audioData = response.choices[0].message.audio.data;
const transcript = response.choices[0].message.audio.transcript;

```

```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	completion, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gpt-audio"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessage("محاسبات کوانتومی را به زبان ساده توضیح بده."),
		}),
		Modalities: openai.F([]openai.ChatCompletionModality{
			openai.ChatCompletionModalityText,
			openai.ChatCompletionModalityAudio,
		}),
		Audio: openai.F(openai.ChatCompletionAudioParam{
			Format: openai.F(openai.ChatCompletionAudioFormatMp3),
			Voice:  openai.F(openai.ChatCompletionAudioVoiceNova),
		}),
	})

	if err != nil {
		panic(err)
	}

	fmt.Printf("Audio Data: %s\n", completion.Choices[0].Message.Audio.Data)
	fmt.Printf("Transcript: %s\n", completion.Choices[0].Message.Audio.Transcript)
}

```

```php
<?php

require 'vendor/autoload.php';

use OpenAI\Client;

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-audio',
    'messages' => [
        [
            'role' => 'user',
            'content' => 'محاسبات کوانتومی را به زبان ساده توضیح بده.',
        ],
    ],
    'modalities' => ['text', 'audio'],
    'audio' => [
        'format' => 'mp3',
        'voice' => 'nova',
    ],
]);

$audioData = $response['choices'][0]['message']['audio']['data'];
$transcript = $response['choices'][0]['message']['audio']['transcript'];

echo "متن رونویسی: " . $transcript . "\n";

```


صدای بازگشتی به‌صورت Base64 در مسیر `choices[0].message.audio.data` قرار می‌گیرد. برای تبدیل آن به یک فایل MP3 قابل پخش مستقیم از ترمینال (به `jq` نیاز دارد)، یک دستور یک‌باره اجرا کنید:

```zsh
# macOS (zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 -D > output.mp3

afplay output.mp3
```

```bash
# لینوکس (bash/zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' \
  | jq -r '.choices[0].message.audio.data' \
  | base64 --decode >output.mp3

ffplay -nodisp -autoexit output.mp3
```

```powershell
# ویندوز (PowerShell)
$response = curl.exe -sS "https://api.avalai.ir/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:AVALAI_API_KEY" `
  -d '{
    "model": "gpt-audio",
    "messages": [
      {
        "role": "user",
        "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."
      }
    ],
    "modalities": ["text", "audio"],
    "audio": {
      "format": "mp3",
      "voice": "nova"
    }
  }' | ConvertFrom-Json

[IO.File]::WriteAllBytes(
  (Join-Path $PWD "output.mp3"),
  [Convert]::FromBase64String($response.choices[0].message.audio.data)
)

Start-Process .\output.mp3
```

این‌ها دستورهای یک‌باره ترمینال هستند و نیازی نیست چیزی به `.zshrc`، `.bashrc` یا پروفایل PowerShell اضافه شود.



<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-audio",
    input="محاسبات کوانتومی را به زبان ساده توضیح بده.",
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
  model: "gpt-audio",
  instructions: "You are a helpful assistant.",
  input: "محاسبات کوانتومی را به زبان ساده توضیح بده.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-audio",
    "input": "محاسبات کوانتومی را به زبان ساده توضیح بده.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

### فرمت پاسخ صوتی

هنگام استفاده از مدل‌های صوتی با وجه `audio`، پاسخ شامل یک شی `audio` در پیام است:

```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1763042146,
  "model": "gpt-audio-2025-08-28",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "audio": {
          "id": "audio_abc123",
          "data": "SUQzBAAAAA...", // صدای رمزگذاری‌شده Base64

          "expires_at": 1763045747,
          "transcript": "محاسبات کوانتومی یک فناوری انقلابی است..."
        }
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12,
    "completion_tokens": 75,
    "total_tokens": 87,
    "completion_tokens_details": {
      "audio_tokens": 58,
      "text_tokens": 17
    },
    "prompt_tokens_details": {
      "audio_tokens": 0,
      "text_tokens": 12
    }
  }
}
```

### استفاده از gpt-audio-1.5 برای کیفیت صوتی پرمیوم

برای بالاترین کیفیت سنتز صدا و درک صوتی، از `gpt-audio-1.5` استفاده کنید:

```python
response = client.chat.completions.create(
    model="gpt-audio-1.5",  # بهترین مدل صوتی با زمینه ۲۵۶ هزار توکن
    messages=[{"role": "user", "content": "هوای امروز چطور است؟"}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "nova"},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gpt-audio-1.5` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-sol",
    input="هوای امروز چطور است؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

### استفاده از gpt-audio-mini برای پردازش مقرون به صرفه

برای برنامه‌های با حجم بالا، از `gpt-audio-mini` استفاده کنید که قابلیت‌های مشابه را با هزینه کمتری ارائه می‌دهد:

```python
response = client.chat.completions.create(
    model="gpt-audio-mini",  # گزینه مقرون به صرفه‌تر
    messages=[{"role": "user", "content": "هوای امروز چطور است؟"}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "alloy"},
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-audio-mini",
    input="هوای امروز چطور است؟",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->

### مدل‌های صوتی قدیمی

برای سازگاری با نسخه‌های قبلی، مدل‌های پیش‌نمایش زیر همچنان در دسترس هستند:

- `gpt-4o-audio-preview`
- `gpt-4o-mini-audio-preview`

> **ورودی صوتی:** برای `input_audio` از مدل گفت‌وگومحور سازگار مانند `gpt-audio-mini` استفاده کنید؛ [نمونه ورودی صوتی](fa/examples/processing_audio_in_chat_completion_api.md#الگوی-۲-ارسال-ورودی-صوتی-به-مدل) را ببینید. مدل‌های Gemini TTS فقط متن می‌پذیرند. برای رونویسی اختصاصی فایل، از [API رونویسی صوتی](fa/api-reference/audio.md) استفاده کنید.

## مدیریت خطا (Error Handling)

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات                                                        |
| -------- | -------------------------------------------------------------- |
| 400      | درخواست بد - درخواست شما نامعتبر است.                          |
| 401      | غیرمجاز - کلید API شما اشتباه است.                             |
| 403      | ممنوع - شما اجازه دسترسی به این منبع را ندارید.                |
| 404      | یافت نشد - منبع مشخص شده یافت نشد.                             |
| 429      | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید. |
| 500      | خطای داخلی سرور - مشکلی در سرور ما وجود داشت.                  |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## منابع مرتبط

- [مدل‌ها](fa/models/model-details.md) - درباره مدل‌های موجود بیاموزید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
