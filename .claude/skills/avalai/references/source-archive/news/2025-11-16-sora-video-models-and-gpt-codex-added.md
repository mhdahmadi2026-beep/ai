# افزودن مدل‌های تولید ویدیوی سری Sora-2 و مدل‌های پیشرفته GPT-5.1 Codex

**تاریخ:** 1404-08-25 / (2025-11-16)

## خلاصه

ما از پشتیبانی مدل‌های تولید ویدیوی Sora 2 از OpenAI و سری جدید GPT-5.1 Codex که برای وظایف عاملی (agentic) بهینه شده‌اند، خبر می‌دهیم. مدل‌های جدید [`sora-2`](fa/providers/openai.md#sora-2) و [`sora-2-pro`](fa/providers/openai.md#sora-2-pro) امکان تولید ویدیو به صورت برنامه‌نویسی را از طریق اندپوینت [`v1/videos`](fa/api-reference/videos.md) فراهم می‌کنند، در حالی که [`gpt-5.1-codex`](fa/providers/openai.md#gpt-5.1-codex) و [`gpt-5.1-codex-mini`](fa/providers/openai.md#gpt-5.1-codex-mini) قابلیت‌های استدلال پیشرفته برای تولید کد، اشکال‌زدایی و جریان‌های کاری عامل خودکار را از طریق اندپوینت [`v1/responses`](fa/api-reference/responses.md) ارائه می‌دهند.

---

## جزئیات

### تولید ویدیو با Sora 2

ما مدل‌های تولید ویدیوی Sora 2 از OpenAI را معرفی می‌کنیم که به توسعه‌دهندگان امکان می‌دهد ویدیوهای با کیفیت بالا را از پرامپت‌های متنی از طریق API ما ایجاد کنند. این مدل‌ها قابلیت‌های پیشرفته تولید ویدیو را با کنترل جامع بر وضوح تصویر، مدت زمان و جهت خلاقانه به ارمغان می‌آورند.

#### مدل‌های موجود

- **[`sora-2`](fa/providers/openai.md#sora-2)**: برای سرعت و انعطاف‌پذیری بهینه شده، ایده‌آل برای تکرار سریع، محتوای رسانه‌های اجتماعی و نمونه‌سازی اولیه. نتایج با کیفیت را به سرعت و با قیمت مقرون‌به‌صرفه تولید می‌کند.

- **[`sora-2-pro`](fa/providers/openai.md#sora-2-pro)**: خروجی با کیفیت بالاتر و آماده تولید ارائه می‌دهد. بهترین گزینه برای فیلمبرداری سینمایی، دارایی‌های بازاریابی و موقعیت‌هایی که نیاز به حداکثر وضوح بصری دارند.

**ویژگی‌های کلیدی:**

- **تولید ناهمزمان**: ارسال کارهای تولید ویدیو و بررسی برای تکمیل یا استفاده از webhooks برای اعلان‌ها
- **وضوح‌های انعطاف‌پذیر**: پشتیبانی از 720x1280، 1280x720 و 1024x1792 (فقط Pro)
- **کنترل مدت زمان**: تولید ویدیوهای 4 تا 8+ ثانیه
- **مراجع تصویر**: استفاده از تصاویر ورودی برای هدایت تولید ویدیو
- **قابلیت Remix**: تکرار روی ویدیوهای تکمیل شده با تنظیمات هدفمند
- **دارایی‌های پشتیبان**: دانلود تصاویر بندانگشتی و spritesheets همراه با ویدیوها

**جزئیات قیمت‌گذاری:**

| مدل | وضوح | هزینه به ازای هر ثانیه |
|-------|-----------|-----------------|
| sora-2 | 720x1280, 1280x720 | $0.10/ثانیه |
| sora-2-pro | 720x1280, 1280x720 | $0.30/ثانیه |
| sora-2-pro | 1024x1792, 1792x1024 | $0.50/ثانیه |

### نمونه‌های درخواست/پاسخ API

#### ایجاد یک ویدیو

```language-selector
bash=:curl https://api.avalai.ir/v1/videos \
  -H "Content-Type: multipart/form-data" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=sora-2" \
  -F "prompt=A calico cat playing a piano on stage" \
  -F "size=720x1280" \
  -F "seconds=4"

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

video = client.videos.create(
    model="sora-2",
    prompt="A calico cat playing a piano on stage",
    size="720x1280",
    seconds=4,
)

print(video.id)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const video = await client.videos.create({
  model: "sora-2",
  prompt: "A calico cat playing a piano on stage",
  size: "720x1280",
  seconds: 4,
});

console.log(video.id);

```

#### پاسخ

```json
{
  "id": "video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5",
  "object": "video",
  "created_at": 1758941485,
  "status": "queued",
  "model": "sora-2",
  "progress": 0,
  "seconds": "4",
  "size": "720x1280"
}
```

#### بررسی وضعیت ویدیو

```language-selector
bash=:curl https://api.avalai.ir/v1/videos/video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:video_status = client.videos.retrieve(
    "video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5"
)
print(f"Status: {video_status.status}, Progress: {video_status.progress}%")

javascript=:const videoStatus = await client.videos.retrieve("video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5");
console.log(`Status: ${videoStatus.status}, Progress: ${videoStatus.progress}%`);

```

#### پاسخ (تکمیل شده)

```json
{
  "id": "video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5",
  "object": "video",
  "created_at": 1758941485,
  "status": "completed",
  "model": "sora-2",
  "progress": 100,
  "seconds": "4",
  "size": "720x1280"
}
```

#### دانلود ویدیو

```language-selector
bash=:curl -L https://api.avalai.ir/v1/videos/video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output video.mp4

python=:content = client.videos.download_content(
    "video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5", variant="video"
)
content.write_to_file("video.mp4")

javascript=:const content = await client.videos.downloadContent("video_68d7512d07848190b3e45da0ecbebcde004da08e1e0678d5");
const buffer = Buffer.from(await content.arrayBuffer());
require('fs').writeFileSync('video.mp4', buffer);

```

### مدل‌های GPT-5.1 Codex

ما سری جدید GPT-5.1 Codex را معرفی می‌کنیم که به طور خاص برای وظایف عاملی، تولید کد و جریان‌های کاری استدلال پیشرفته بهینه شده‌اند.

#### مدل‌های موجود

- **[`gpt-5.1-codex`](fa/providers/openai.md#gpt-5.1-codex)**: مدل استدلال پیشرفته بهینه شده برای تولید کد پیچیده، اشکال‌زدایی و جریان‌های کاری عاملی چند مرحله‌ای. عملکرد برتر برای سیستم‌های خودکار که نیاز به استدلال فنی عمیق دارند، ارائه می‌دهد.

- **[`gpt-5.1-codex-mini`](fa/providers/openai.md#gpt-5.1-codex-mini)**: نسخه سبک‌وزن که قابلیت‌های عالی تولید کد را با نقطه قیمت دسترس‌تر ارائه می‌دهد. ایده‌آل برای وظایف عاملی با حجم بالا که کارایی هزینه اهمیت دارد.

**مهم:** این مدل‌ها به صورت انحصاری از طریق اندپوینت [`v1/responses`](fa/api-reference/responses.md) در دسترس هستند.

**ویژگی‌های کلیدی:**

- **بهینه‌سازی عاملی**: طراحی شده برای جریان‌های کاری عامل خودکار و استدلال چند مرحله‌ای
- **درک پیشرفته کد**: عملکرد برتر در تولید، بازسازی و اشکال‌زدایی کد
- **کش کردن پرامپت**: کاهش هزینه‌ها برای زمینه تکراری با قیمت‌گذاری ورودی کش شده
- **زمینه گسترده**: مدیریت پایگاه‌های کد بزرگ و مستندات گسترده
- **فراخوانی تابع**: پشتیبانی بومی برای استفاده از ابزار و الگوهای فراخوانی تابع

**جزئیات قیمت‌گذاری:**

| مدل | ورودی (به ازای 1M توکن) | ورودی کش شده (به ازای 1M توکن) | خروجی (به ازای 1M توکن) |
|-------|----------------------|------------------------------|------------------------|
| gpt-5.1-codex | $1.25 | $0.125 | $10.00 |
| gpt-5.1-codex-mini | $0.25 | $0.025 | $2.00 |

### نمونه‌های استفاده از SDK

#### استفاده از GPT-5.1 Codex برای تولید کد

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1-codex",
    "input": "Write a Python function to implement a binary search tree with insert, delete, and search operations."
  }'

python=:import requests

response = requests.post(
    "https://api.avalai.ir/v1/responses",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "gpt-5.1-codex",
        "input": "Write a Python function to implement a binary search tree with insert, delete, and search operations.",
    },
)

result = response.json()
print(result["choices"][0]["message"]["content"])

javascript=:const response = await fetch("https://api.avalai.ir/v1/responses", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "gpt-5.1-codex",
    "input": "Write a Python function to implement a binary search tree with insert, delete, and search operations."
  }),
});

const result = await response.json();
console.log(result.choices[0].message.content);

```

#### نمونه پاسخ

```json
{
  "id": "resp-abc123",
  "created_at": 1763313239,
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "model": "gpt-5.1-codex",
  "object": "response",
  "output": [
    {
      "id": "rs_123",
      "summary": [],
      "type": "reasoning",
      "content": null,
      "encrypted_content": null,
      "status": null
    },
    {
      "id": "msg_123",
      "content": [
        {
          "annotations": [],
          "text": "Here's a comprehensive implementation of a binary search tree...\n\n
```python\nclass TreeNode:\n    def __init__(self, value):\n        self.value = value\n        self.left = None\n        self.right = None\n\nclass BinarySearchTree:\n    def __init__(self):\n        self.root = None\n    \n    def insert(self, value):\n        # Implementation...\n```",
          "type": "output_text",
          "logprobs": []
        }
      ],
      "role": "assistant",
      "status": "completed",
      "type": "message"
    }
  ],
  "parallel_tool_calls": true,
  "temperature": 1.0,
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "max_output_tokens": null,
  "previous_response_id": null,
  "reasoning": {
    "effort": "medium",
    "summary": null
  },
  "status": "completed",
  "text": {
    "format": {
      "type": "text"
    },
    "verbosity": "medium"
  },
  "truncation": "disabled",
  "usage": {
    "input_tokens": 9,
    "input_tokens_details": {
      "audio_tokens": null,
      "cached_tokens": 0,
      "text_tokens": null
    },
    "output_tokens": 15,
    "output_tokens_details": {
      "reasoning_tokens": 0,
      "text_tokens": null
    },
    "total_tokens": 24,
    "cost": null
  },
  "background": false,
  "max_tool_calls": null,
  "top_logprobs": 0,
  "estimated_cost": {
    "unit": "0.0001612500",
    "irt": 18.2,
    "exchange_rate": 112850
  }
}
```

#### استفاده از Codex-Mini برای وظایف عاملی

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.1-codex-mini",
    "input": "input": "Write a Python function to implement a binary search tree with insert, delete, and search operations."
  }'

python=:response = requests.post(
    "https://api.avalai.ir/v1/responses",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "gpt-5.1-codex-mini",
        "input": "Create a REST API endpoint in Express.js for user authentication with JWT tokens.",
    },
)

result = response.json()
print(result["choices"][0]["message"]["content"])

javascript=:const response = await fetch("https://api.avalai.ir/v1/responses", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "gpt-5.1-codex-mini",
    input: "Create a REST API endpoint in Express.js for user authentication with JWT tokens.",
  }),
});

const result = await response.json();
console.log(result.choices[0].message.content);

```

---

## لینک‌های مرتبط

- [مرجع API تولید ویدیو](fa/api-reference/videos.md)
- [راهنمای تولید ویدیو با استفاده از Sora](fa/guides/generate-videos-using-sora.md)
- [مرجع API Responses](fa/api-reference/responses.md)
- [مستندات مدل‌های OpenAI](fa/providers/openai.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای جریان‌های کاری عاملی](fa/guides/agents.md)
