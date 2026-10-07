# News 2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade: افزودن Qwen3.8-Max و ارتقای DeepSeek-V4-Flash
URL: `https://docs.avalai.ir/fa/news/2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade`
**تاریخ:** 1405-05-12 / (2026-08-03)

# افزودن Qwen3.8-Max و ارتقای DeepSeek-V4-Flash

**تاریخ:** 1405-05-12 / (2026-08-03)

## خلاصه

مدل پرچم‌دار جدید Alibaba با نام `qwen3.8-max` اکنون برای کدنویسی بلندمدت، کار حرفه‌ای، درک چندوجهی و گردش‌کارهای عاملی در AvalAI در دسترس است. شناسه موجود `deepseek-v4-flash` نیز اکنون به‌طور خودکار به DeepSeek-V4-Flash-0731، نسخه رسمی با قابلیت‌های عاملی قوی‌تر، هدایت می‌شود؛ هیچ تغییری در کد لازم نیست و قیمت‌گذاری بدون تغییر باقی می‌ماند.


## قیمت‌گذاری

قیمت‌ها به دلار آمریکا و به ازای ۱ میلیون توکن هستند.

| مدل                 | ورودی | ورودی کش‌شده | ورودی ایجاد کش | خروجی |
| ------------------- | ----- | ------------ | -------------- | ----- |
| `qwen3.8-max`       | $2.00 | $0.25        | $2.50          | $6.00 |
| `deepseek-v4-flash` | $0.14 | $0.0028      | —              | $0.28 |

ارتقای DeepSeek هیچ تغییری در نرخ‌های موجود `deepseek-v4-flash` ایجاد نمی‌کند.

---

## نمونه درخواست و پاسخ API

### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-max",
    "messages": [
      {
        "role": "user",
        "content": "این معماری پلتفرم را بررسی کن و یک برنامه پیاده‌سازی مرحله‌ای با دروازه‌های راستی‌آزمایی پیشنهاد بده."
      }
    ],
    "extra_body": {"enable_thinking": false}
  }'
```

### پاسخ

پاسخ کوتاه‌شده زیر ساختار استاندارد Chat Completions را نشان می‌دهد:

```json
{
  "id": "chatcmpl-qwen38-example",
  "created": 1785744000,
  "model": "qwen3.8-max",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "ابتدا مرزهای پایدار سرویس و معیارهای قابل اندازه‌گیری rollback را تعریف کنید. پیش از مهاجرت یک گردش‌کار کم‌ریسک پشت feature flag، observability و contract testها را اضافه کنید و فقط پس از عبور از هر دروازه راستی‌آزمایی، ترافیک را افزایش دهید.",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 55,
    "prompt_tokens": 23,
    "total_tokens": 78,
    "completion_tokens_details": null,
    "prompt_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": 23,
      "image_tokens": null
    }
  },
  "estimated_cost": {
    "unit": "0.0003760000",
    "irt": 57.6,
    "exchange_rate": 153200
  }
}
```

---

## نمونه‌های استفاده از SDK

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen3.8-max",
    "messages": [
      {
        "role": "user",
        "content": "برای این پلتفرم چندسرویسی یک برنامه پیاده‌سازی قابل اتکا طراحی کن."
      }
    ],
    "extra_body": {"enable_thinking": false}
  }'

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="qwen3.8-max",
    messages=[
        {
            "role": "user",
            "content": "برای این پلتفرم چندسرویسی یک برنامه پیاده‌سازی قابل اتکا طراحی کن.",
        }
    ],
    extra_body={"enable_thinking": False},
)

print(response.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "qwen3.8-max",
  messages: [
    {
      role: "user",
      content: "برای این پلتفرم چندسرویسی یک برنامه پیاده‌سازی قابل اتکا طراحی کن.",
    },
  ],
  extra_body: { enable_thinking: false },
});

console.log(response.choices[0].message.content);

```

### ادامه استفاده از DeepSeek-V4-Flash بدون تغییر

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4-flash",
    "messages": [
      {
        "role": "user",
        "content": "علت ریشه‌ای این استقرار ناموفق را پیدا کن و امن‌ترین اصلاح را پیشنهاد بده."
      }
    ],
    "reasoning_effort": "high"
  }'
```

همین شناسه پایدار مدل اکنون به‌طور خودکار از DeepSeek-V4-Flash-0731 استفاده می‌کند.

---

## لینک‌های مرتبط

- [جزئیات مدل Qwen3.8-Max](fa/models/qwen3.8-max.md)
- [نمای کلی مدل‌های Alibaba](fa/providers/alibaba.md)
- [نمای کلی مدل‌های DeepSeek](fa/providers/deepseek.md)
- [راهنمای مدل‌های استدلالی](fa/guides/reasoning.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [قیمت‌گذاری](fa/pricing.md)
