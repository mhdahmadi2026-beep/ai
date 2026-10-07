# News 2026-02-17-new-models-qwen35-minimax-m25: مدل‌های جدید اضافه شدند: Qwen3.5 Plus، Qwen3.5-397B و MiniMax M2.5
URL: `https://docs.avalai.ir/fa/news/2026-02-17-new-models-qwen35-minimax-m25`
**تاریخ:** ۱۴۰۴-۱۱-۲۸ / (2026-02-17)

# مدل‌های جدید اضافه شدند: Qwen3.5 Plus، Qwen3.5-397B و MiniMax M2.5

**تاریخ:** ۱۴۰۴-۱۱-۲۸ / (2026-02-17)

## خلاصه

AvalAI چهار مدل جدید هوش مصنوعی را معرفی می‌کند: Qwen3.5 Plus و Qwen3.5-397B-A17B از Alibaba، با معماری هیبریدی شامل توجه خطی و ترکیب پراکنده متخصصین برای درک چندوجهی بهبود یافته؛ و MiniMax M2.5 با M2.5-Lightning، مدل‌های SOTA برای کدنویسی، استفاده عاملی از ابزار و وظایف بهره‌وری دنیای واقعی با کارایی هزینه‌ای بی‌سابقه.


### MiniMax

ما دسترسی به **MiniMax M2.5** (`minimax-m2.5`) و **MiniMax M2.5-Lightning** (`minimax-m2.5-lightning`) را اعلام می‌کنیم، جدیدترین مدل‌های MiniMax که برای بهره‌وری دنیای واقعی با عملکرد SOTA در کدنویسی و وظایف عاملی طراحی شده‌اند. [مستندات](fa/providers/minimax.md)

#### minimax-m2.5

**ویژگی‌های کلیدی:**

- **عملکرد SOTA در کدنویسی**: ۸۰.۲٪ در SWE-Bench Verified، ۵۱.۳٪ در Multi-SWE-Bench
- **جستجو و فراخوانی ابزار پیشرفته**: ۷۶.۳٪ در BrowseComp با مدیریت زمینه
- **۳۷٪ سریع‌تر از M2.1**: بهبود تجزیه وظیفه و کارایی توکن
- **معماری Spec-Writing**: مدل به طور فعال ویژگی‌ها، ساختار و طراحی UI را قبل از کدنویسی برنامه‌ریزی می‌کند
- **استدلال داخلی**: محتوای تفکر در تگ‌های `<think>` قابل جداسازی با پارامتر `reasoning_split`
- **۱۰+ زبان برنامه‌نویسی**: Go، C، C++، TypeScript، Rust، Kotlin، Python، Java، JavaScript، PHP، Lua، Dart، Ruby
- **چرخه توسعه کامل**: از طراحی سیستم 0-to-1 تا بررسی و آزمایش کد 90-to-100
- **یکپارچه‌سازی کار اداری**: همکاری عمیق با متخصصان مالی، حقوقی و علوم اجتماعی
- **مقرون به صرفه**: ۱ دلار برای ۱ ساعت عملیات مداوم با ۱۰۰ توکن/ثانیه
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `minimax-m2.5` |
| پنجره زمینه | ۲۰۴,۰۰۰ توکن |
| سرعت خروجی | ~۵۰ توکن در ثانیه |
| قیمت ورودی | $0.30 / 1M توکن |
| ورودی کش‌شده | $0.03 / 1M توکن |
| ایجاد کش | $0.375 / 1M توکن |
| قیمت خروجی | $1.20 / 1M توکن |

#### minimax-m2.5-lightning

**ویژگی‌های کلیدی:**

- **استنتاج فوق‌سریع**: ~۱۰۰ توکن در ثانیه (۲ برابر سریع‌تر از سایر مدل‌های پیشرو)
- **همان قابلیت‌های M2.5**: هوش یکسان با توان عملیاتی بالاتر
- **هم‌تراز با Claude Opus 4.6**: مطابقت سرعت تکمیل با مدل‌های پیشرو
- **عملیات کم‌هزینه**: ۰.۳۰ دلار در ساعت با ۱۰۰ TPS عملیات مداوم
- **پشتیبانی کامل از کش**: کش زمینه برای بهینه‌سازی هزینه
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/chat/completions`

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `minimax-m2.5-lightning` |
| پنجره زمینه | ۲۰۴,۰۰۰ توکن |
| سرعت خروجی | ~۱۰۰ توکن در ثانیه |
| قیمت ورودی | $0.30 / 1M توکن |
| ورودی کش‌شده | $0.03 / 1M توکن |
| ایجاد کش | $0.375 / 1M توکن |
| قیمت خروجی | $2.40 / 1M توکن |

**موارد استفاده:**
- کدنویسی عاملی و مهندسی نرم‌افزار (SWE-Bench Verified 80.2%)
- پروژه‌های برنامه‌نویسی چند زبانه
- وظایف جستجو و تحقیق پیچیده
- اتوماسیون کار اداری (Word، PowerPoint، Excel)
- مدل‌سازی و تحلیل مالی
- کمک کد بلادرنگ

---

## خلاصه قیمت‌گذاری

| مدل | ارائه‌دهنده | نوع | قیمت‌گذاری |
|-------|----------|------|---------|
| `qwen3.5-plus` | Alibaba | گفتگو | ورودی: $0.40/1M، کش‌شده: $0.04/1M، خروجی: $2.40/1M (طبقه‌ای بالای ۲۵۶K) |
| `qwen3.5-397b-a17b` | Alibaba | گفتگو | ورودی: $0.60/1M، کش‌شده: $0.06/1M، خروجی: $3.60/1M |
| `minimax-m2.5` | MiniMax | گفتگو | ورودی: $0.30/1M، کش‌شده: $0.03/1M، خروجی: $1.20/1M |
| `minimax-m2.5-lightning` | MiniMax | گفتگو | ورودی: $0.30/1M، کش‌شده: $0.03/1M، خروجی: $2.40/1M |

---

## نمونه‌های درخواست و پاسخ API

### مثال گفتگوی Qwen3.5 Plus

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.5-plus",
    "messages": [
      {
        "role": "user",
        "content": "یک سیستم عامل هوشمند طراحی کن که بتواند به طور خودکار گردش‌های کاری چندمرحله‌ای پیچیده را مدیریت کند."
      }
    ],
    "max_tokens": 4096,
    "stream": false,
    "extra_body": {"enable_thinking": false}
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1739794897,
  "model": "qwen3.5-plus",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "این یک طراحی جامع برای سیستم عامل هوشمند است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 1024,
    "prompt_tokens": 25,
    "total_tokens": 1049
  },
  "estimated_cost": {
    "unit": "0.0024596",
    "irt": 323.11,
    "exchange_rate": 131350
  }
}
```

### مثال کدنویسی MiniMax M2.5

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.5",
    "messages": [
      {
        "role": "user",
        "content": "یک خزنده وب همزمان با محدودیت نرخ در Rust با مدیریت خطای مناسب پیاده‌سازی کن."
      }
    ],
    "max_tokens": 4096
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-abc456",
  "created": 1739794897,
  "model": "minimax-m2.5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "این یک پیاده‌سازی کامل از خزنده وب همزمان با محدودیت نرخ در Rust است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 2048,
    "prompt_tokens": 30,
    "total_tokens": 2078
  },
  "estimated_cost": {
    "unit": "0.0024666",
    "irt": 324.03,
    "exchange_rate": 131350
  }
}
```

### مثال پاسخ سریع MiniMax M2.5-Lightning

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.5-lightning",
    "messages": [
      {
        "role": "user",
        "content": "تفاوت بین async/await و Promises در جاوااسکریپت را توضیح بده."
      }
    ]
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-def789",
  "created": 1739794897,
  "model": "minimax-m2.5-lightning",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "تفاوت‌های کلیدی بین async/await و Promises در جاوااسکریپت عبارتند از...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 512,
    "prompt_tokens": 18,
    "total_tokens": 530
  },
  "estimated_cost": {
    "unit": "0.0012339",
    "irt": 162.08,
    "exchange_rate": 131350
  }
}
```

### MiniMax M2.5 با جداسازی استدلال

از `reasoning_split` برای جداسازی فرآیند تفکر مدل از پاسخ نهایی استفاده کنید:

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "minimax-m2.5",
    "messages": [
      {
        "role": "user",
        "content": "25 ضرب در 37 چند است؟"
      }
    ],
    "extra_body": {
      "reasoning_split": true
    }
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-xyz123",
  "created": 1739794897,
  "model": "minimax-m2.5",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "پاسخ 925 است.",
        "role": "assistant",
        "reasoning_details": "بگذارید 25 * 37 را قدم به قدم محاسبه کنم:\n25 * 37 = 25 * (30 + 7) = 750 + 175 = 925"
      }
    }
  ],
  "usage": {
    "completion_tokens": 45,
    "prompt_tokens": 12,
    "total_tokens": 57
  }
}
```

> **توجه:** بدون `reasoning_split`، محتوای تفکر به صورت درون‌خطی با تگ‌های `<think>` در فیلد `content` ظاهر می‌شود. هنگام مدیریت مکالمات چندنوبتی با فراخوانی ابزار، همیشه پیام پاسخ کامل (شامل فیلدهای `tool_calls` و `reasoning_details`) را در تاریخچه پیام خود حفظ کنید.

---

## مستندات مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مستندات مدل‌های MiniMax](fa/providers/minimax.md)
- [پارامترهای اختصاصی ارائه‌دهنده](fa/guides/provider-specific-params.md)
- [قیمت‌گذاری](fa/pricing.md)
- [راهنمای مدل‌های استدلال](fa/guides/reasoning.md)
