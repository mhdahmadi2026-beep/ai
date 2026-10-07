# News 2026-04-12-new-models-zai-cloudflare-google-alibaba: مدل‌های جدید اضافه شدند: GLM-5.1، GLM-5v-Turbo، Nemotron-3-120B، Gemma 4، Qwen3.6-Plus و Qwen-Image-2.0
URL: `https://docs.avalai.ir/fa/news/2026-04-12-new-models-zai-cloudflare-google-alibaba`
**تاریخ:** ۱۴۰۵-۰۱-۲۳ / (2026-04-12)

# مدل‌های جدید اضافه شدند: GLM-5.1، GLM-5v-Turbo، Nemotron-3-120B، Gemma 4، Qwen3.6-Plus و Qwen-Image-2.0

**تاریخ:** ۱۴۰۵-۰۱-۲۳ / (2026-04-12)

## خلاصه

ما افزودن هشت مدل جدید را اعلام می‌کنیم: GLM-5.1 مدل پرچمدار Z.AI با عملکرد پیشرو در کدنویسی عاملی و GLM-5v-Turbo مدل چندحالتی، NVIDIA Nemotron-3-120B-A12B از طریق Cloudflare AI با پنجره زمینه ۱ میلیون توکن، مدل‌های باز Gemma 4 از گوگل (نسخه‌های 26B و 31B) با کارایی پیشرو در صنعت، Qwen3.6-Plus از علی‌بابا با قابلیت‌های عاملی پیشرفته و زمینه ۱ میلیون توکن، و سری Qwen-Image-2.0 برای تایپوگرافی حرفه‌ای و تولید تصویر فوتورئالیستی.


## نمونه‌های درخواست/پاسخ API

### نمونه GLM-5.1

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5.1",
    "messages": [
      {
        "role": "user",
        "content": "یک تابع پایتون بنویسید که طولانی‌ترین زیردنباله مشترک دو رشته را با استفاده از برنامه‌نویسی پویا پیدا کند."
      }
    ]
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-1234567890",
  "created": 1744483200,
  "model": "glm-5.1",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "این یک تابع پایتون است که طولانی‌ترین زیردنباله مشترک را با استفاده از برنامه‌نویسی پویا پیدا می‌کند:\n\n
```python\ndef longest_common_subsequence(s1: str, s2: str) -> str:\n    m, n = len(s1), len(s2)\n    dp = [[0] * (n + 1) for _ in range(m + 1)]\n    \n    for i in range(1, m + 1):\n        for j in range(1, n + 1):\n            if s1[i-1] == s2[j-1]:\n                dp[i][j] = dp[i-1][j-1] + 1\n            else:\n                dp[i][j] = max(dp[i-1][j], dp[i][j-1])\n    \n    # بازگشت برای یافتن LCS\n    lcs = []\n    i, j = m, n\n    while i > 0 and j > 0:\n        if s1[i-1] == s2[j-1]:\n            lcs.append(s1[i-1])\n            i -= 1\n            j -= 1\n        elif dp[i-1][j] > dp[i][j-1]:\n            i -= 1\n        else:\n            j -= 1\n    \n    return ''.join(reversed(lcs))\n```",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 285,
    "prompt_tokens": 28,
    "total_tokens": 313
  },
  "estimated_cost": {
    "unit": "0.001423",
    "irt": 142.30,
    "exchange_rate": 100000
  }
}
```

### نمونه Gemma 4

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gemma-4-31b-it",
    "messages": [
      {
        "role": "user",
        "content": "مفهوم معماری mixture-of-experts در شبکه‌های عصبی را توضیح دهید."
      }
    ]
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-gemma4-9876543210",
  "created": 1744483200,
  "model": "gemma-4-31b-it",
  "object": "chat.completion",
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "Mixture-of-Experts (MoE) یک معماری شبکه عصبی است که از چندین زیرشبکه تخصصی (متخصصان) با مکانیزم دروازه‌بانی برای هدایت ورودی‌ها به متخصصان مرتبط‌ترین استفاده می‌کند...",
        "role": "assistant"
      }
    }
  ],
  "usage": {
    "completion_tokens": 250,
    "prompt_tokens": 18,
    "total_tokens": 268
  },
  "estimated_cost": {
    "unit": "0.000103",
    "irt": 10.3,
    "exchange_rate": 100000
  }
}
```

### نمونه Qwen-Image-2.0

#### درخواست

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "qwen-image-2.0",
    "prompt": "یک پوستر اینفوگرافیک حرفه‌ای که مقایسه مدل‌های هوش مصنوعی را با تایپوگرافی تمیز و طراحی مدرن نشان می‌دهد",
    "n": 1,
    "size": "1024x1024"
  }'
```

#### پاسخ

```json
{
  "created": 1744483200,
  "data": [
    {
      "url": "https://api.avalai.ir/files/generated/img-abc123...",

      "revised_prompt": "یک پوستر اینفوگرافیک حرفه‌ای که مقایسه مدل‌های هوش مصنوعی را با تایپوگرافی تمیز و طراحی مدرن نشان می‌دهد"
    }
  ],
  "estimated_cost": {
    "unit": "0.035",
    "irt": 3500.00,
    "exchange_rate": 100000
  }
}
```

---

## خلاصه قیمت‌گذاری

| مدل | ورودی | ورودی کش شده | خروجی | ویژه |
|-----|-------|--------------|-------|------|
| glm-5.1 | $۱.۵۴/۱M | $۰.۲۸۶/۱M | $۴.۸۴/۱M | - |
| glm-5v-turbo | $۱.۲۰/۱M | $۰.۲۴/۱M | $۴.۰۰/۱M | - |
| cf.nemotron-3-120b-a12b | $۰.۵۰/۱M | $۰.۰۵/۱M | $۱.۵۰/۱M | زمینه ۱M |
| gemma-4-26b-a4b-it | $۰.۱۳/۱M | $۰.۰۱۳/۱M | $۰.۴۰/۱M | - |
| gemma-4-31b-it | $۰.۱۴/۱M | $۰.۰۱۴/۱M | $۰.۴۰/۱M | - |
| qwen3.6-plus | $۰.۵۰/۱M | $۰.۰۵/۱M | $۳.۰۰/۱M | $۲.۰۰/$۶.۰۰ بالای ۲۵۶K |
| qwen-image-2.0-pro | رایگان | رایگان | $۰.۰۷۵/تصویر | - |
| qwen-image-2.0 | رایگان | رایگان | $۰.۰۳۵/تصویر | - |

---

## لینک‌های مستندات

- [مدل‌های Z.AI](fa/providers/zai.md)
- [مدل‌های Cloudflare AI](fa/providers/cloudflare.md)
- [مدل‌های گوگل](fa/providers/google.md)
- [مدل‌های علی‌بابا](fa/providers/alibaba.md)
- [قیمت‌گذاری](fa/pricing.md)
- [API Chat Completions](fa/api-reference/chat.md)
- [API Images](fa/api-reference/images.md)
