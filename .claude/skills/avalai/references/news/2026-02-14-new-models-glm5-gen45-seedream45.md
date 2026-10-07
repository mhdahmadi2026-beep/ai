# News 2026-02-14-new-models-glm5-gen45-seedream45: دریافت وضعیت برای تکمیل
URL: `https://docs.avalai.ir/fa/news/2026-02-14-new-models-glm5-gen45-seedream45`
**تاریخ:** ۱۴۰۴-۱۱-۲۶ / (2026-02-14)

# مدل‌های جدید اضافه شد: GLM-5، Gen-4.5 و Seedream 4.5

**تاریخ:** ۱۴۰۴-۱۱-۲۶ / (2026-02-14)

## خلاصه

AvalAI سه مدل هوش مصنوعی جدید را معرفی می‌کند: GLM-5 از Z.AI، یک مدل پایه پرچمدار با عملکرد SOTA در کدنویسی و وظایف عامل‌محور؛ Gen-4.5 از RunwayML، مدل تولید ویدیوی برتر جهان با وفاداری بصری بی‌نظیر؛ و Seedream 4.5 از BytePlus، مدل پیشرفته تولید تصویر با قابلیت‌های بهبود یافته ویرایش چند تصویر و تایپوگرافی.


### RunwayML

ما دسترسی به **Gen-4.5** (`gen4.5`) را اعلام می‌کنیم، جدیدترین مدل تولید ویدیوی RunwayML با کیفیت حرکت و وفاداری بصری پیشرفته. [مستندات](fa/providers/runwayml.md)

**ویژگی‌های کلیدی:**

- **مدل برتر تولید ویدیوی جهان**: امتیاز 1,247 Elo در معیار Artificial Analysis Text to Video
- **کیفیت پیشرفته**: وفاداری بصری بی‌نظیر و پایبندی دقیق به پرامپت
- **دقت فیزیکی**: فیزیک واقع‌گرایانه با دینامیک مناسب، برخوردها و حرکت طبیعی
- **رندر صحنه‌های پیچیده**: صحنه‌های پیچیده و چند عنصری با ترکیب‌بندی تفصیلی
- **شخصیت‌های بیانگر**: احساسات ظریف، حرکات طبیعی و جزئیات صورت واقع‌گرایانه
- **انسجام زمانی**: حفظ هماهنگی در طول حرکت و زمان
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/videos`

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `gen4.5` |
| نوع | تولید ویدیو |
| مدت زمان | 2-10 ثانیه |
| رزولوشن‌ها | 1280x720، 720x1280، 1920x1080، 1080x1920 و بیشتر |
| قیمت‌گذاری | $0.12 به ازای هر ثانیه ویدیو |

---

### BytePlus

ما دسترسی به **Seedream 4.5** (`seedream-4-5-251128`) را اعلام می‌کنیم، مدل ارتقایافته تولید تصویر BytePlus با قابلیت‌های بهبود یافته ویرایش چند تصویر و تایپوگرافی. [مستندات](fa/providers/byteplus.md)

**ویژگی‌های کلیدی:**

- **بهبود همه‌جانبه**: مقیاس‌گذاری کلی مدل برای کیفیت بهبود یافته
- **ویرایش چند تصویر**: شناسایی دقیق موضوعات اصلی در ویرایش چند تصویر
- **حفظ تصویر مرجع**: حفظ دقیق جزئیات تصاویر مرجع
- **تایپوگرافی بهبود یافته**: بهبود بیشتر قابلیت‌های رندر متن متراکم
- **بصری حرفه‌ای**: ارائه خلاقیت‌های بصری حرفه‌ای با انسجام و وفاداری بالا
- **پشتیبانی نقطه پایانی**: در دسترس در `v1/images/generations` و `v1/images/edit`

| ویژگی | جزئیات |
|---------|---------|
| شناسه مدل | `seedream-4-5-251128` |
| نوع | تولید و ویرایش تصویر |
| حداکثر وضوح | 4K (4096x4096 پیکسل) |
| قیمت‌گذاری | $0.04 به ازای هر تصویر |

---

## خلاصه قیمت‌گذاری

| مدل | ارائه‌دهنده | نوع | قیمت‌گذاری |
|-------|----------|------|---------|
| `glm-5` | Z.AI | گفتگو | ورودی: $1.10/1M، کش‌شده: $0.22/1M، خروجی: $3.52/1M |
| `gen4.5` | RunwayML | ویدیو | $0.12 به ازای هر ثانیه |
| `seedream-4-5-251128` | BytePlus | تصویر | $0.04 به ازای هر تصویر |

---

## نمونه‌های درخواست و پاسخ API

### مثال گفتگوی GLM-5

#### درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "glm-5",
    "messages": [
      {
        "role": "user",
        "content": "یک درخت جستجوی دودویی با تعادل AVL در پایتون پیاده‌سازی کن."
      }
    ],
    "max_tokens": 4096,
    "temperature": 0.6
  }'
```

#### پاسخ

```json
{
  "id": "chatcmpl-abc123",
  "created": 1739574109,
  "model": "glm-5",
  "object": "chat.completion",
  "system_fingerprint": null,
  "choices": [
    {
      "finish_reason": "stop",
      "index": 0,
      "message": {
        "content": "اینجا یک پیاده‌سازی کامل از درخت AVL در پایتون است...",
        "role": "assistant",
        "thinking_blocks": [],
        "annotations": []
      }
    }
  ],
  "usage": {
    "completion_tokens": 512,
    "prompt_tokens": 20,
    "total_tokens": 532
  },
  "estimated_cost": {
    "unit": "0.0018254000",
    "irt": 239.89,
    "exchange_rate": 131350
  }
}
```

### مثال تولید ویدیوی Gen-4.5

#### درخواست

```bash
curl -X POST "https://api.avalai.ir/v1/videos" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F "prompt=نمای سینمایی از نهنگی که در میان رشته کوه زمستانی با ابرها پرواز می‌کند." \
  -F "model=gen4.5" \
  -F "size=1920x1080" \
  -F "seconds=5" \
  -F "input_reference=@reference_image.jpeg;type=image/jpeg"
```

#### پاسخ

```json
{
  "id": "video_abc123",
  "object": "video",
  "status": "processing",
  "model": "gen4.5",
  "created": 1739574109,
  "prompt": "نمای سینمایی از نهنگی که در میان رشته کوه زمستانی با ابرها پرواز می‌کند.",
  "request_id": "req_xyz789"
}
```

### مثال تولید تصویر Seedream 4.5

#### درخواست

```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "seedream-4-5-251128",
    "prompt": "عکاسی حرفه‌ای از محصول یک ساعت لوکس روی سطح مرمر",
    "size": "2K",
    "response_format": "url",
    "sequential_image_generation": "disabled",
    "watermark": false
  }'
```

#### پاسخ

```json
{
  "created": 1739574109,
  "data": [
    {
      "url": "https://api.avalai.ir/generated/image_abc123.png",

      "revised_prompt": null
    }
  ],
  "estimated_cost": {
    "unit": "0.04",
    "irt": 5254.00,
    "exchange_rate": 131350
  }
}
```

---

## نمونه‌های استفاده از SDK

### GLM-5 با پایتون

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="glm-5",
    messages=[
        {
            "role": "user",
            "content": "یک معماری میکروسرویس برای پلتفرم تجارت الکترونیک طراحی کن.",
        }
    ],
    max_tokens=4096,
    temperature=0.6,
)

print(response.choices[0].message.content)
```

### تولید ویدیوی Gen-4.5 با پایتون

```python
from openai import OpenAI
import time

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد درخواست تولید ویدیو
video = client.videos.create(
    model="gen4.5",
    prompt="نمای نزدیک از زن جوانی با ویژگی‌های چشمگیر و موهای بلوند پلاتینی.",
    input_reference=open("portrait_reference.jpeg", "rb"),
    size="1920x1080",
    seconds="5",
)

print(f"تولید ویدیو شروع شد: {video.id}")

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(video.id)

    if video_status.status == "completed":
        print(f"ویدیو آماده است! ID: {video.id}")
        # دانلود ویدیو
        with client.with_streaming_response.videos.retrieve_content(
            video.id
        ) as response:
            with open("output.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    time.sleep(10)
```

### تولید تصویر Seedream 4.5 با پایتون

```python
from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="seedream-4-5-251128",
    prompt="عکس محصول حرفه‌ای با تایپوگرافی بهبود یافته نشان دهنده 'تخفیف ۵۰٪'",
    size="2K",
    response_format="url",
    extra_body={"sequential_image_generation": "disabled", "watermark": False},
)

print(f"تصویر تولید شده: {response.data[0].url}")
```

---

## مستندات مرتبط

- [مدل‌های Z.AI](fa/providers/zai.md)
- [مدل‌های RunwayML](fa/providers/runwayml.md)
- [مدل‌های BytePlus](fa/providers/byteplus.md)
- [API تولید ویدیو](fa/api-reference/videos.md)
- [API تولید تصویر](fa/api-reference/images.md)
- [قیمت‌گذاری](fa/pricing.md)
