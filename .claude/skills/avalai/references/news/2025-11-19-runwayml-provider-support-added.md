# News 2025-11-19-runwayml-provider-support-added: ویرایش سریع تصویر
URL: `https://docs.avalai.ir/fa/news/2025-11-19-runwayml-provider-support-added`
**تاریخ:** 1404-08-28 / (2025-11-19)

# افزودن پشتیبانی از ارائه‌دهنده RunwayML

**تاریخ:** 1404-08-28 / (2025-11-19)

## خلاصه

AvalAI اکنون از RunwayML به عنوان یک ارائه‌دهنده جدید پشتیبانی می‌کند و قابلیت‌های پیشرفته تولید ویدیو، ویرایش تصویر و تبدیل متن به گفتار را به پلتفرم اضافه می‌کند. این یکپارچه‌سازی شامل چهار مدل جدید است: [`gen4_turbo`](fa/providers/runwayml.md) برای تولید ویدیو، [`gen4_image`](fa/providers/runwayml.md) و [`gen4_image_turbo`](fa/providers/runwayml.md) برای ویرایش تصویر، و [`eleven_multilingual_v2`](fa/providers/runwayml.md) برای تبدیل متن به گفتار چندزبانه.


## نمونه‌های API

### تولید ویدیو با gen4_turbo

تولید ویدیو با پشتیبانی از تصویر مرجع:

```language-selector
bash=:curl -X POST "https://api.avalai.ir/v1/videos" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: multipart/form-data" \
  -F prompt="در یخچال باز می‌شود. یک هیولای بنفش بامزه و چاق از آن بیرون می‌آید." \
  -F model="gen4_turbo" \
  -F size="1280x720" \
  -F seconds="2" \
  -F input_reference="@monster_original_720p.jpeg;type=image/jpeg"

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

# ایجاد ویدیو با تصویر مرجع
video = client.videos.create(
    prompt="در یخچال باز می‌شود. یک هیولای بنفش بامزه و چاق از آن بیرون می‌آید.",
    input_reference=open("monster_original_720p.jpeg", "rb"),
    model="gen4_turbo",
    size="1280x720",
    seconds="2",
)

print(f"تولید ویدیو شروع شد: {video.id}")

javascript=:import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// ایجاد ویدیو با تصویر مرجع
const video = await client.videos.create({
  prompt: "در یخچال باز می‌شود. یک هیولای بنفش بامزه و چاق از آن بیرون می‌آید.",
  input_reference: fs.createReadStream("monster_original_720p.jpeg"),
  model: "gen4_turbo",
  size: "1280x720",
  seconds: "2"
});

console.log(`تولید ویدیو شروع شد: ${video.id}`);

```

#### پاسخ نمونه

```json
{
  "id": "video_45d4cf58-6c37-43f1-b7ca-8f349f280a3e",
  "object": "video",
  "status": "completed",
  "created_at": 1732022400,
  "completed_at": 1732022450,
  "expires_at": null,
  "error": null,
  "progress": 100,
  "remixed_from_video_id": null,
  "seconds": "2",
  "size": "1280x720",
  "model": "gen4_turbo",
  "usage": {
    "duration_seconds": 2.0
  },
  "estimated_cost": {
    "unit": "0.1000000000",
    "irt": 11345.0,
    "exchange_rate": 113450
  }
}
```

**توجه**: تصویر نمونه را برای تست دانلود کنید: [monster_original_720p.jpeg](https://docs.avalai.ir/fa/_media/img/monster_original_720p.jpeg)

### ویرایش تصویر با gen4_image

ویرایش تصاویر با قابلیت‌های پیشرفته هوش مصنوعی:

```language-selector
bash=:curl -i https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gen4_image" \
  -F "prompt=یک سفینه فضایی آینده‌نگر بر روی پس‌زمینه کهکشان رنگارنگ." \
  -F "image=@input_image.jpg" \
  -F "size=1920x1080"

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

# ویرایش تصویر
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gen4_image",
        image=image_file,
        prompt="یک سفینه فضایی آینده‌نگر بر روی پس‌زمینه کهکشان رنگارنگ.",
        size="1920x1080",
    )

print(f"URL تصویر ویرایش شده: {response.data[0].url}")

javascript=:import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// ویرایش تصویر
const response = await client.images.edit({
  model: "gen4_image",
  image: fs.createReadStream("input_image.jpg"),
  prompt: "یک سفینه فضایی آینده‌نگر بر روی پس‌زمینه کهکشان رنگارنگ.",
  size: "1920x1080"
});

console.log(`URL تصویر ویرایش شده: ${response.data[0].url}`);

```

#### پاسخ نمونه

```json
{
  "created": 1763557851,
  "data": [
    {
      "url": "https://image-generations.avalai.ir/serve/image-abc123.png?expires=1763644251&signature=xyz789",

      "b64_json": null,
      "revised_prompt": null
    }
  ],
  "estimated_cost": {
    "unit": "0.0850000000",
    "irt": 9643.25,
    "exchange_rate": 113450
  }
}
```

#### سایزهای پشتیبانی شده برای gen4_image و gen4_image_turbo

هر دو مدل ویرایش تصویر از رزولوشن‌های زیر پشتیبانی می‌کنند:

- `720x720` - فرمت مربع
- `960x720` / `720x960` - نسبت تصویر 4:3
- `1024x1024` - فرمت مربع (پیش‌فرض)
- `1080x1080` - فرمت مربع
- `1080x1440` / `1440x1080` - عمودی/افقی
- `1080x1920` / `1920x1080` - Full HD عمودی/افقی
- `1168x880` - فرمت پهن
- `1280x720` / `720x1280` - HD عمودی/افقی
- `1360x768` - صفحه پهن
- `1680x720` - فوق پهن
- `1808x768` - فرمت سینمایی
- `2112x912` - سینمایی فوق پهن

### ویرایش سریع تصویر با gen4_image_turbo

بهینه شده برای سرعت با کیفیت رقابتی:

```language-selector
bash=:curl -i https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gen4_image_turbo" \
  -F "prompt=نورپردازی غروب خورشید دراماتیک به صحنه اضافه کنید." \
  -F "image=@input_image.jpg" \
  -F "size=1024x1024"

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

# ویرایش سریع تصویر
with open("input_image.jpg", "rb") as image_file:
    response = client.images.edit(
        model="gen4_image_turbo",
        image=image_file,
        prompt="نورپردازی غروب خورشید دراماتیک به صحنه اضافه کنید.",
        size="1024x1024",
    )

print(f"URL تصویر ویرایش شده: {response.data[0].url}")

javascript=:import { OpenAI } from "openai";
import fs from 'fs';

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// ویرایش سریع تصویر
const response = await client.images.edit({
  model: "gen4_image_turbo",
  image: fs.createReadStream("input_image.jpg"),
  prompt: "نورپردازی غروب خورشید دراماتیک به صحنه اضافه کنید.",
  size: "1024x1024"
});

console.log(`URL تصویر ویرایش شده: ${response.data[0].url}`);

```

### تبدیل متن به گفتار با eleven_multilingual_v2

تولید گفتار طبیعی در زبان‌های متعدد:

```language-selector
bash=:curl https://api.avalai.ir/v1/audio/speech \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "eleven_multilingual_v2",
    "input": "به یکپارچه‌سازی RunwayML در AvalAI خوش آمدید. آینده خلاقیت مبتنی بر هوش مصنوعی را تجربه کنید.",
    "voice": "alloy"
  }' \
  --output speech.mp3

python=:from openai import OpenAI
from pathlib import Path

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

speech_file_path = Path("./speech.mp3")

response = client.audio.speech.create(
    model="eleven_multilingual_v2",
    voice="alloy",
    input="به یکپارچه‌سازی RunwayML در AvalAI خوش آمدید. آینده خلاقیت مبتنی بر هوش مصنوعی را تجربه کنید.",
)

response.stream_to_file(speech_file_path)
print(f"صدا ذخیره شد در {speech_file_path}")

javascript=:import fs from "fs";
import path from "path";
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const speechFile = path.resolve("./speech.mp3");

async function main() {
  const mp3 = await client.audio.speech.create({
    model: "eleven_multilingual_v2",
    voice: "alloy",
    input: "به یکپارچه‌سازی RunwayML در AvalAI خوش آمدید. آینده خلاقیت مبتنی بر هوش مصنوعی را تجربه کنید.",
  });
  
  const buffer = Buffer.from(await mp3.arrayBuffer());
  await fs.promises.writeFile(speechFile, buffer);
  console.log(`صدا ذخیره شد در ${speechFile}`);
}

main();

```

---

## شروع کار

برای شروع استفاده از مدل‌های RunwayML:

1. اطمینان حاصل کنید که یک حساب کاربری فعال AvalAI با اعتبار کافی دارید
2. از کلید API موجود AvalAI خود استفاده کنید - نیازی به پیکربندی اضافی نیست
3. نام مدل‌ها را در فراخوانی‌های API خود مشخص کنید: `gen4_turbo`، `gen4_image`، `gen4_image_turbo`، یا `eleven_multilingual_v2`
4. نمونه‌های کد بالا را برای زبان برنامه‌نویسی مورد نظر خود دنبال کنید

---

## لینک‌های مرتبط

- [مستندات مدل‌های RunwayML](fa/providers/runwayml.md)
- [مرجع API تولید ویدیو](fa/api-reference/videos.md)
- [مرجع API ویرایش تصویر](fa/api-reference/images.md)
- [مرجع API صدا](fa/api-reference/audio.md)
- [جزئیات قیمت‌گذاری](fa/pricing.md)
- [مستندات رسمی API RunwayML](https://docs.dev.runwayml.com/api/)
