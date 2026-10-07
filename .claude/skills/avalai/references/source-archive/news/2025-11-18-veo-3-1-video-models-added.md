# افزودن مدل‌های تولید ویدیوی Veo 3.1

**تاریخ:** 1404-08-27 / (2025-11-18)

## خلاصه

ما از پشتیبانی مدل‌های تولید ویدیوی Veo 3.1 گوگل خبر می‌دهیم که دو گزینه برای ایجاد ویدیوهای مبتنی بر هوش مصنوعی ارائه می‌دهند: [`veo-3.1-generate-preview`](fa/providers/google.md#veo-3-1-generate-preview) برای خروجی با کیفیت بالا و [`veo-3.1-fast-generate-preview`](fa/providers/google.md#veo-3-1-fast-generate-preview) بهینه شده برای سرعت. هر دو مدل از طریق اندپوینت [`v1/videos`](fa/api-reference/videos.md) با پشتیبانی از تولید متن-به-ویدیو و تصویر-به-ویدیو قابل دسترسی هستند.

---

## جزئیات

### تولید ویدیو با Google Veo 3.1

ما سری Veo 3.1 گوگل را معرفی می‌کنیم که آخرین پیشرفت در فناوری تولید ویدیوی هوش مصنوعی است. این مدل‌ها به توسعه‌دهندگان امکان می‌دهند ویدیوهای با کیفیت بالا را از پرامپت‌های متنی یا تصاویر مرجع ایجاد کنند، با بهبود در تولید صدا و افزایش کیفیت بصری.

#### مدل‌های موجود

- **[`veo-3.1-generate-preview`](fa/providers/google.md#veo-3.1-generate-preview)**: کیفیت خروجی برتر با صدای بومی غنی، مکالمات طبیعی و جلوه‌های صوتی همگام‌سازی شده ارائه می‌دهد. بهترین انتخاب برای محتوای آماده تولید که نیاز به حداکثر وفاداری بصری و صوتی دارد.

- **[`veo-3.1-fast-generate-preview`](fa/providers/google.md#veo-3-1-fast-generate-preview)**: نسخه بهینه شده برای سرعت که کیفیت بالا را حفظ می‌کند در حالی که زمان‌های تولید سریع‌تری ارائه می‌دهد. ایده‌آل برای تکرار سریع، پروژه‌های با حجم بالا و برنامه‌هایی که نیاز به بازگشت سریع دارند.

**ویژگی‌های کلیدی:**

- **تولید صدای بومی**: ویدیوها شامل صدای همگام‌سازی شده با جلوه‌های صوتی طبیعی و صدای محیطی هستند
- **تصویر-به-ویدیوی پیشرفته**: بهبود در رعایت پرامپت و ثبات کاراکتر در صحنه‌ها
- **مدت زمان انعطاف‌پذیر**: تولید ویدیوهای 4، 6 یا 8 ثانیه‌ای (پیش‌فرض: 8 ثانیه)
- **رزولوشن‌های متعدد**: پشتیبانی از خروجی 720p و 1080p (نسبت تصویر 16:9)
- **گزینه‌های نسبت تصویر**: فرمت‌های 16:9 (افقی) و 9:16 (عمودی)
- **تصاویر مرجع**: هدایت تولید با تا 3 تصویر مرجع برای ثبات کاراکتر/سبک
- **پردازش ناهمزمان**: دریافت وضعیت برای تکمیل
- **گسترش ویدیو**: گسترش ویدیوهای موجود برای ایجاد توالی‌های طولانی‌تر

**جزئیات قیمت‌گذاری:**

| مدل | هزینه به ازای هر ثانیه |
|-------|-----------------|
| veo-3.1-fast-generate-preview | $0.15/ثانیه |
| veo-3.1-generate-preview | $0.40/ثانیه |

### نمونه‌های درخواست/پاسخ API

#### تولید یک ویدیو

```language-selector
bash=:curl https://api.avalai.ir/v1/videos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "veo-3.1-fast-generate-preview",
    "prompt": "گربه‌ای که در یک باغ آفتابی با توپ نخ بازی می‌کند",
    "seconds": "4"
  }'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

video = client.videos.create(
    model="veo-3.1-fast-generate-preview",
    prompt="گربه‌ای که در یک باغ آفتابی با توپ نخ بازی می‌کند",
    seconds="4",
)

print(f"Video ID: {video.id}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const video = await client.videos.create({
  model: "veo-3.1-fast-generate-preview",
  prompt: "گربه‌ای که در یک باغ آفتابی با توپ نخ بازی می‌کند",
  seconds: "4",
});

console.log(`Video ID: ${video.id}`);

```

#### پاسخ

```json
{
  "id": "video_abc123def456",
  "object": "video",
  "created_at": 1731916800,
  "status": "processing",
  "model": "veo-3.1-fast-generate-preview",
  "progress": 0,
  "seconds": "4"
}
```

#### بررسی وضعیت ویدیو

```language-selector
bash=:curl https://api.avalai.ir/v1/videos/video_abc123def456 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:import time

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve("video_abc123def456")

    if video_status.status == "completed":
        print(f"ویدیو آماده است! ID: {video_status.id}")
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    print(f"وضعیت: {video_status.status}, پیشرفت: {video_status.progress}%")
    time.sleep(10)

javascript=:// دریافت وضعیت برای تکمیل
while (true) {
  const videoStatus = await client.videos.retrieve("video_abc123def456");
  
  if (videoStatus.status === "completed") {
    console.log(`ویدیو آماده است! ID: ${videoStatus.id}`);
    break;
  } else if (videoStatus.status === "failed") {
    console.log(`تولید ناموفق بود: ${videoStatus.error}`);
    break;
  }
  
  console.log(`وضعیت: ${videoStatus.status}, پیشرفت: ${videoStatus.progress}%`);
  await new Promise(resolve => setTimeout(resolve, 10000));
}

```

#### پاسخ (تکمیل شده)

```json
{
  "id": "video_abc123def456",
  "object": "video",
  "created_at": 1731916800,
  "status": "completed",
  "model": "veo-3.1-fast-generate-preview",
  "progress": 100,
  "seconds": "4"
}
```

#### دانلود محتوای ویدیو

```language-selector
bash=:curl https://api.avalai.ir/v1/videos/video_abc123def456/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output video.mp4

python=:content = client.videos.download_content("video_abc123def456")
with open("video.mp4", "wb") as f:
    f.write(content.read())
print("ویدیو با موفقیت دانلود شد!")

javascript=:const content = await client.videos.downloadContent("video_abc123def456");
const buffer = Buffer.from(await content.arrayBuffer());
require('fs').writeFileSync('video.mp4', buffer);
console.log("ویدیو با موفقیت دانلود شد!");

```

### ویژگی‌های پیشرفته

#### تولید تصویر-به-ویدیو

از تصاویر مرجع برای هدایت تولید ویدیو و اطمینان از ثبات بصری استفاده کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/videos \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=veo-3.1-generate-preview" \
  -F "prompt=منظره زنده می‌شود با آب جاری و ابرهای متحرک" \
  -F "input_reference=@reference_image.jpg" \
  -F "seconds=8"

python=:video = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="منظره زنده می‌شود با آب جاری و ابرهای متحرک",
    input_reference=open("reference_image.jpg", "rb"),
    seconds="8",
)

print(f"تولید تصویر-به-ویدیو شروع شد: {video.id}")

javascript=:import fs from 'fs';

const video = await client.videos.create({
  model: "veo-3.1-generate-preview",
  prompt: "منظره زنده می‌شود با آب جاری و ابرهای متحرک",
  input_reference: fs.createReadStream("reference_image.jpg"),
  seconds: "8",
});

console.log(`تولید تصویر-به-ویدیو شروع شد: ${video.id}`);

```

#### کنترل نسبت تصویر و رزولوشن

ابعاد ویدیو را با استفاده از پارامتر `size` مشخص کنید:

```language-selector
bash=:# افقی 16:9 در 1080p
curl https://api.avalai.ir/v1/videos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "veo-3.1-generate-preview",
    "prompt": "تصویر هوایی پهپاد از شهر ساحلی در غروب خورشید",
    "size": "1920x1080",
    "seconds": "8"
  }'

# عمودی 9:16
curl https://api.avalai.ir/v1/videos \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "veo-3.1-fast-generate-preview",
    "prompt": "مدل فشن که در خیابان شهر راه می‌رود",
    "size": "1080x1920",
    "seconds": "6"
  }'

python=:# افقی 16:9 در 1080p
video_landscape = client.videos.create(
    model="veo-3.1-generate-preview",
    prompt="تصویر هوایی پهپاد از شهر ساحلی در غروب خورشید",
    size="1920x1080",
    seconds="8",
)

# عمودی 9:16
video_portrait = client.videos.create(
    model="veo-3.1-fast-generate-preview",
    prompt="مدل فشن که در خیابان شهر راه می‌رود",
    size="1080x1920",
    seconds="6",
)

javascript=:// افقی 16:9 در 1080p
const videoLandscape = await client.videos.create({
  model: "veo-3.1-generate-preview",
  prompt: "تصویر هوایی پهپاد از شهر ساحلی در غروب خورشید",
  size: "1920x1080",
  seconds: "8",
});

// عمودی 9:16
const videoPortrait = await client.videos.create({
  model: "veo-3.1-fast-generate-preview",
  prompt: "مدل فشن که در خیابان شهر راه می‌رود",
  size: "1080x1920",
  seconds: "6",
});

```

### بهترین شیوه‌های پرامپت‌نویسی

برای دریافت بهترین نتایج از مدل‌های Veo 3.1:

**توصیفی و خاص باشید**
- جزئیات بصری را شامل شوید: رنگ‌ها، نورپردازی، ترکیب‌بندی
- حرکت را مشخص کنید: حرکات دوربین، اقدامات سوژه
- سبک را تعریف کنید: سینمایی، واقع‌گرایانه، هنری
- حال و هوا را تنظیم کنید: جوی، پرانرژی، آرام

**نشانه‌های صوتی را شامل شوید**
- **دیالوگ**: از گیومه برای گفتار خاص استفاده کنید (مثلا `"این باید کلید باشد،" او زمزمه کرد.`)
- **جلوه‌های صوتی**: صداها را به صراحت توصیف کنید (مثلا `صدای جیغ لاستیک‌ها، غرش موتور`)
- **صدای محیطی**: چشم‌انداز صوتی محیط را توصیف کنید (مثلا `یک صدای ضعیف و وحشتناک در پس‌زمینه طنین‌انداز می‌شود`)

**حرکت دوربین را مشخص کنید**
- "دوربین به سمت چپ می‌چرخد تا نشان دهد..."
- "زوم آهسته به سمت سوژه..."
- "تصویر هوایی پهپاد در حال پایین آمدن..."
- "شات تعقیبی دستی که دنبال می‌کند..."

**مثال پرامپت خوب:**
```
توله سگ گلدن رتریور در یک چمنزار آفتابی در ساعت طلایی بازی می‌کند،
دوربین به آرامی توله را دنبال می‌کند که در میان علف‌های بلند می‌دود،
عمق میدان سینمایی با افکت بوکه، رنگ‌آمیزی گرم
```

**مثال پرامپت ضعیف:**
```
سگی که بازی می‌کند
```

### مقایسه مدل‌ها

| ویژگی | veo-3.1-generate-preview | veo-3.1-fast-generate-preview |
|---------|-------------------------|------------------------------|
| **کیفیت** | بالاترین | بالا |
| **سرعت** | استاندارد | سریع‌تر |
| **صدا** | غنی، طبیعی | با کیفیت بالا |
| **هزینه/ثانیه** | $0.40 | $0.15 |
| **بهترین برای** | محتوای تولیدی | تکرار سریع، حجم بالا |
| **حداکثر مدت زمان** | 8 ثانیه | 8 ثانیه |
| **رزولوشن‌ها** | 720p, 1080p | 720p, 1080p |

---

## لینک‌های مرتبط

- [مرجع API ویدیو](fa/api-reference/videos.md)
- [راهنمای تولید ویدیو با استفاده از Veo](fa/guides/generate-videos-using-veo.md)
- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [اطلاعات قیمت‌گذاری](fa/pricing.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [بهترین شیوه‌ها](fa/guides/best-practices.md)