# تولید ویدیو با استفاده از Veo

نحوه تولید ویدیوهای مبتنی بر هوش مصنوعی با استفاده از مدل‌های Veo 3.1 گوگل را از طریق AvalAI API بیاموزید.

## مقدمه

[API ویدیو](fa/api-reference/videos.md) AvalAI اندپوینت‌هایی برای تولید ویدیو با استفاده از مدل‌های Veo 3.1 گوگل ارائه می‌دهد. این مدل‌های پیشرفته می‌توانند ویدیوهای واقع‌گرایانه با صدای بومی از توضیحات متنی ایجاد کنند، با پشتیبانی از:

- **متن به ویدیو:** ایجاد ویدیو از ابتدا بر اساس پرامپت‌های متنی دقیق
- **تصویر به ویدیو:** تولید ویدیو با شروع از یک تصویر مرجع
- **تصاویر مرجع:** حفظ ثبات کاراکتر با استفاده از تصاویر مرجع (مواد تشکیل‌دهنده به ویدیو)
- **گسترش ویدیو:** توسعه ویدیوهای موجود برای ایجاد سکانس‌های طولانی‌تر
- **صدای بومی:** تولید صدای غنی شامل دیالوگ، جلوه‌های صوتی و صدای محیطی
- **پردازش ناهمزمان:** تولید ویدیوهای تا 8 ثانیه با دریافت وضعیت

این راهنما استفاده از این قابلیت‌ها را از طریق AvalAI برای ایجاد محتوای ویدیویی جذاب با صدای همگام‌سازی شده پوشش می‌دهد.

> **⚠️ مهم: اگر ارتباط قطع شد**
>
> عملیات تولید ویدیو و ریمیکس به صورت **ناهمزمان** هستند - سرور بلافاصله پس از دریافت درخواست شما، پردازش را شروع می‌کند. اگر ارتباط شما در حین یا پس از ارسال قطع شود، **فورا درخواست جدیدی برای تولید ارسال نکنید**، زیرا این کار ممکن است منجر به شارژ تکراری شود.
>
> **در صورت قطع ارتباط چه باید کرد:**
>
> 1. از [endpoint لیست ویدیوها](#لیست-ویدیوها) برای دریافت تمام ویدیوهای خود استفاده کنید:
>
>    curl -X GET https://api.avalai.ir/v1/videos/ \
>      -H "Authorization: Bearer $AVALAI_API_KEY"
>
>
> 2. فیلد `status` آخرین ویدیوی خود را بررسی کنید:
>    - اگر `status == "failed"`: ویدیو شروع به تولید نکرده و **هیچ هزینه‌ای اعمال نخواهد شد**. می‌توانید با خیال راحت درخواست جدیدی ارسال کنید.
>    - اگر `status` چیزی غیر از `"failed"` باشد (مثل `"queued"`، `"processing"`، `"completed"`): تولید **شروع شده یا تکمیل شده است** و **هزینه محاسبه خواهد شد**. منتظر تکمیل این ویدیو بمانید به جای ایجاد درخواست تکراری.
>
> این روش به شما کمک می‌کند از استفاده غیرضروری از اعتبار و تولیدهای تکراری ویدیو جلوگیری کنید.

## کدام مدل را استفاده کنیم؟

AvalAI دسترسی به دو مدل تولید ویدیوی Veo 3.1 را فراهم می‌کند که هر کدام برای موارد استفاده مختلف بهینه شده‌اند:

### veo-3.1-generate-001

بهترین برای تولید ویدیوی با کیفیت بالا و صدای غنی:
- **نسبت تصویر:** 16:9 (افقی) و 9:16 (عمودی)
- **رزولوشن:** 720p و 1080p (فقط 16:9)
- **مدت زمان:** 4، 6 یا 8 ثانیه (پیش‌فرض: 8)
- **صدا:** تولید صدای بومی با دیالوگ، جلوه‌های صوتی و صدای محیطی
- **قیمت:** $0.40 به ازای هر ثانیه
- **موارد استفاده:** محتوای حرفه‌ای، ویدیوهای بازاریابی، تولیدات با کیفیت بالا
- **پردازش:** ناهمزمان با دریافت وضعیت

### veo-3.1-fast-generate-001

طراحی شده برای سرعت و مقرون‌به‌صرفه بودن با حفظ کیفیت بالا:
- **نسبت تصویر:** 16:9 (افقی) و 9:16 (عمودی)
- **رزولوشن:** 720p و 1080p (فقط 16:9)
- **مدت زمان:** 4، 6 یا 8 ثانیه (پیش‌فرض: 8)
- **صدا:** تولید صدای بومی با جلوه‌های صوتی
- **قیمت:** $0.15 به ازای هر ثانیه
- **موارد استفاده:** نمونه‌سازی سریع، محتوای شبکه‌های اجتماعی، سرویس‌های backend، تست A/B
- **پردازش:** ناهمزمان با زمان تولید سریع‌تر

هر دو مدل از تصاویر مرجع، گسترش ویدیو و تصاویر مرجع برای ثبات کاراکتر پشتیبانی می‌کنند.

## تولید ساده ویدیو

ساده‌ترین راه برای تولید ویدیو، ارائه یک پرامپت متنی است. API درخواست شما را به صورت ناهمزمان پردازش می‌کند و شما می‌توانید وضعیت تکمیل را بررسی کنید.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد درخواست تولید ویدیو
video = client.videos.create(
    model="veo-3.1-fast-generate-001",
    prompt="دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب، صداهای محیطی نرم آب",
    size="1280x720",
    seconds="4",
    safety_identifier="project_demo_001",  # اختیاری: برای ردیابی داخلی
)

print(f"تولید ویدیو شروع شد: {video.id}")
print(f"Request ID: {video.request_id}")  # برای ردیابی هزینه استفاده کنید

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(video.id)

    if video_status.status == "completed":
        print(f"ویدیو آماده است! ID: {video.id}")

        # دانلود محتوای ویدیو
        with client.with_streaming_response.videos.retrieve_content(
            video.id
        ) as response:
            with open("output.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        print("ویدیو در output.mp4 دانلود شد")
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    time.sleep(10)

```

```bash
# ایجاد درخواست تولید ویدیو با safety_identifier برای ردیابی
curl -X POST https://api.avalai.ir/v1/videos \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "veo-3.1-fast-generate-001",
    "prompt": "دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب، صداهای محیطی نرم آب",
    "size": "1280x720",
    "seconds": "4",
    "safety_identifier": "project_demo_001"
  }'

# بررسی وضعیت تولید
curl -X GET https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# دانلود ویدیوی تکمیل شده
curl -X GET https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output video.mp4

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function generateVideo() {
    // ایجاد درخواست تولید ویدیو
    const video = await client.videos.create({
        model: 'veo-3.1-fast-generate-001',
        prompt: 'دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب، صداهای محیطی نرم آب',
        size: '1280x720',
        seconds: '4',
        safety_identifier: 'project_demo_001'  // اختیاری: برای ردیابی داخلی
    });

    console.log(`تولید ویدیو شروع شد: ${video.id}`);
    console.log(`Request ID: ${video.request_id}`);  // برای ردیابی هزینه استفاده کنید

    // دریافت وضعیت برای تکمیل
    while (true) {
        const videoStatus = await client.videos.retrieve(video.id);

        if (videoStatus.status === 'completed') {
            console.log(`ویدیو آماده است! ID: ${video.id}`);

            // دانلود محتوای ویدیو
            const response = await client.videos.retrieveContent(video.id);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync('output.mp4', buffer);
            console.log('ویدیو در output.mp4 دانلود شد');
            break;
        } else if (videoStatus.status === 'failed') {
            console.log(`تولید ناموفق بود: ${videoStatus.error}`);
            break;
        }

        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

generateVideo();

```


## استفاده از تصاویر مرجع

می‌توانید یک تصویر مرجع برای هدایت تولید ویدیو ارائه دهید. Veo از تصویر ورودی به عنوان فریم اولیه استفاده می‌کند، که آن را برای انیمیشن اشیاء روزمره، زنده کردن نقاشی‌ها و طراحی‌ها، و اضافه کردن حرکت و صدا به صحنه‌های طبیعی عالی می‌کند.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد ویدیو با تصویر مرجع
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="منظره زنده می‌شود با آب جاری و ابرهای در حال حرکت، پرندگان در حال پرواز، باد ملایم در میان درختان",
    input_reference=open("reference_image.jpg", "rb"),
    size="1920x1080",
    seconds="6",
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
            with open("landscape_video.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        print("ویدیو دانلود شد")
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    time.sleep(10)

```

```bash
# ایجاد ویدیو با تصویر مرجع
curl -X POST https://api.avalai.ir/v1/videos \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=veo-3.1-generate-001" \
  -F "prompt=منظره زنده می‌شود با آب جاری و ابرهای در حال حرکت، پرندگان در حال پرواز، باد ملایم در میان درختان" \
  -F "input_reference=@reference_image.jpg;type=image/jpeg" \
  -F "size=1920x1080" \
  -F "seconds=6"

# دریافت وضعیت (تکرار تا تکمیل)
curl -X GET https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# دانلود پس از تکمیل
curl -X GET https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output landscape_video.mp4

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function generateVideoWithImage() {
    // ایجاد ویدیو با تصویر مرجع
    const video = await client.videos.create({
        model: 'veo-3.1-generate-001',
        prompt: 'منظره زنده می‌شود با آب جاری و ابرهای در حال حرکت، پرندگان در حال پرواز، باد ملایم در میان درختان',
        input_reference: fs.createReadStream('reference_image.jpg'),
        size: '1920x1080',
        seconds: '6'
    });

    console.log(`تولید ویدیو شروع شد: ${video.id}`);

    // دریافت وضعیت برای تکمیل
    while (true) {
        const videoStatus = await client.videos.retrieve(video.id);

        if (videoStatus.status === 'completed') {
            console.log(`ویدیو آماده است! ID: ${video.id}`);

            // دانلود ویدیو
            const response = await client.videos.retrieveContent(video.id);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync('landscape_video.mp4', buffer);
            console.log('ویدیو دانلود شد');
            break;
        } else if (videoStatus.status === 'failed') {
            console.log(`تولید ناموفق بود: ${videoStatus.error}`);
            break;
        }

        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

generateVideoWithImage();

```


## تصاویر مرجع برای ثبات کاراکتر

Veo 3.1 به شما امکان می‌دهد تا 3 تصویر مرجع از یک کاراکتر، شی یا صحنه ارائه دهید تا ثبات را در تولیدات ویدیویی حفظ کنید. این برای حفظ ظاهر کاراکتر در چندین شات یا اعمال یک استایل خاص عالی است.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد ویدیو با تصاویر مرجع برای ثبات کاراکتر
# توجه: این ویژگی از افزونه AvalAI به OpenAI SDK استفاده می‌کند
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="کاراکتر در جنگل قدم می‌زند و با کنجکاوی اطراف را کاوش می‌کند",
    reference_images=[
        open("character_ref_1.jpg", "rb"),
        open("character_ref_2.jpg", "rb"),
        open("character_ref_3.jpg", "rb"),
    ],
    size="1280x720",
    seconds="8",
)

print(f"تولید ویدیو شروع شد: {video.id}")

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(video.id)

    if video_status.status == "completed":
        print(f"ویدیو با کاراکتر ثابت آماده است! ID: {video.id}")

        # دانلود ویدیو
        with client.with_streaming_response.videos.retrieve_content(
            video.id
        ) as response:
            with open("character_video.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        print("ویدیو دانلود شد")
        break
    elif video_status.status == "failed":
        print(f"تولید ناموفق بود: {video_status.error}")
        break

    time.sleep(10)

```

```bash
# ایجاد ویدیو با تصاویر مرجع
curl -X POST https://api.avalai.ir/v1/videos \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=veo-3.1-generate-001" \
  -F "prompt=کاراکتر در جنگل قدم می‌زند و با کنجکاوی اطراف را کاوش می‌کند" \
  -F "reference_images=@character_ref_1.jpg;type=image/jpeg" \
  -F "reference_images=@character_ref_2.jpg;type=image/jpeg" \
  -F "reference_images=@character_ref_3.jpg;type=image/jpeg" \
  -F "size=1280x720" \
  -F "seconds=8"

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function generateWithCharacterConsistency() {
    const video = await client.videos.create({
        model: 'veo-3.1-generate-001',
        prompt: 'کاراکتر در جنگل قدم می‌زند و با کنجکاوی اطراف را کاوش می‌کند',
        reference_images: [
            fs.createReadStream('character_ref_1.jpg'),
            fs.createReadStream('character_ref_2.jpg'),
            fs.createReadStream('character_ref_3.jpg')
        ],
        size: '1280x720',
        seconds: '8'
    });

    console.log(`تولید ویدیو شروع شد: ${video.id}`);

    // دریافت وضعیت و دانلود...
    while (true) {
        const videoStatus = await client.videos.retrieve(video.id);

        if (videoStatus.status === 'completed') {
            const response = await client.videos.retrieveContent(video.id);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync('character_video.mp4', buffer);
            console.log('ویدیو دانلود شد');
            break;
        } else if (videoStatus.status === 'failed') {
            console.log(`ناموفق: ${videoStatus.error}`);
            break;
        }
        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

generateWithCharacterConsistency();

```


## گسترش ویدیو

ویدیوهای تولید شده با Veo خود را گسترش دهید تا سکانس‌های طولانی‌تر ایجاد کنید. گسترش از ثانیه نهایی (24 فریم) ویدیوی موجود شما استفاده می‌کند و عمل را ادامه می‌دهد، که به شما امکان می‌دهد ویدیوهایی به طول یک دقیقه یا بیشتر با زنجیره‌ای کردن چندین گسترش ایجاد کنید.

**توجه:** صدا/دیالوگ فقط در صورتی به طور موثر گسترش می‌یابد که در ثانیه آخر ویدیو حضور داشته باشد.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# گسترش یک ویدیوی موجود
extended_video = client.videos.extend(
    video_id="video_691bab4a12248190b1e9123d8648ff4d",
    prompt="پاراگلایدر به آرامی بر فراز دره‌های پوشیده از گل پایین می‌آید",
    seconds="8",
)

print(f"گسترش ویدیو شروع شد: {extended_video.id}")

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(extended_video.id)

    if video_status.status == "completed":
        print(f"ویدیوی گسترش‌یافته آماده است! ID: {video_status.id}")

        # دانلود ویدیوی گسترش‌یافته
        with client.with_streaming_response.videos.retrieve_content(
            extended_video.id
        ) as response:
            with open("extended_output.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        print("ویدیوی گسترش‌یافته دانلود شد")
        break
    elif video_status.status == "failed":
        print(f"گسترش ناموفق بود: {video_status.error}")
        break

    time.sleep(10)

```

```bash
# گسترش یک ویدیوی موجود
curl -X POST https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d/extend \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "پاراگلایدر به آرامی بر فراز دره‌های پوشیده از گل پایین می‌آید",
    "seconds": "8"
  }'

# دریافت وضعیت
curl -X GET https://api.avalai.ir/v1/videos/video_691bb11c9f1481908d6c5a0c463fcd94 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# دانلود پس از تکمیل
curl -X GET https://api.avalai.ir/v1/videos/video_691bb11c9f1481908d6c5a0c463fcd94/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output extended_output.mp4

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function extendVideo() {
    // گسترش یک ویدیوی موجود
    const extendedVideo = await client.videos.extend(
        'video_691bab4a12248190b1e9123d8648ff4d',
        {
            prompt: 'پاراگلایدر به آرامی بر فراز دره‌های پوشیده از گل پایین می‌آید',
            seconds: '8'
        }
    );

    console.log(`گسترش ویدیو شروع شد: ${extendedVideo.id}`);

    // دریافت وضعیت برای تکمیل
    while (true) {
        const videoStatus = await client.videos.retrieve(extendedVideo.id);

        if (videoStatus.status === 'completed') {
            console.log(`ویدیوی گسترش‌یافته آماده است! ID: ${videoStatus.id}`);

            // دانلود ویدیوی گسترش‌یافته
            const response = await client.videos.retrieveContent(extendedVideo.id);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync('extended_output.mp4', buffer);
            console.log('ویدیوی گسترش‌یافته دانلود شد');
            break;
        } else if (videoStatus.status === 'failed') {
            console.log(`گسترش ناموفق بود: ${videoStatus.error}`);
            break;
        }

        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

extendVideo();

```


## بررسی وضعیت ویدیو

برای برنامه‌های تولید، دریافت وضعیت یک روش قابل اعتماد برای بررسی زمان تکمیل تولید ویدیو فراهم می‌کند.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")


def check_video_status(video_id):
    """دریافت وضعیت برای تکمیل ویدیو با backoff نمایی"""
    max_attempts = 60
    wait_time = 10

    for attempt in range(max_attempts):
        video_status = client.videos.retrieve(video_id)

        if video_status.status == "completed":
            print(f"ویدیو {video_id} تکمیل شد!")

            # دانلود ویدیو
            with client.with_streaming_response.videos.retrieve_content(
                video_id
            ) as response:
                with open(f"video_{video_id}.mp4", "wb") as f:
                    for chunk in response.iter_bytes():
                        f.write(chunk)

            return True

        elif video_status.status == "failed":
            print(f"تولید ویدیو ناموفق بود: {video_status.error}")
            return False

        print(f"وضعیت: {video_status.status}, پیشرفت: {video_status.progress}%")
        time.sleep(wait_time)

    print("زمان انتظار برای تکمیل ویدیو به پایان رسید")
    return False


# مثال استفاده
video = client.videos.create(
    model="veo-3.1-fast-generate-001",
    prompt="صحنه باغ آرام با آواز پرندگان",
    size="1280x720",
    seconds="4",
)

check_video_status(video.id)

```

```bash
# دریافت وضعیت ویدیو
VIDEO_ID="video_691bab4a12248190b1e9123d8648ff4d"

while true; do
  STATUS=$(curl -s -X GET https://api.avalai.ir/v1/videos/$VIDEO_ID \
    -H "Authorization: Bearer $AVALAI_API_KEY" | jq -r '.status')

  if [ "$STATUS" = "completed" ]; then
    echo "ویدیو تکمیل شد! در حال دانلود..."
    curl -X GET https://api.avalai.ir/v1/videos/$VIDEO_ID/content \
      -H "Authorization: Bearer $AVALAI_API_KEY" \
      --output video_$VIDEO_ID.mp4
    break
  elif [ "$STATUS" = "failed" ]; then
    echo "تولید ویدیو ناموفق بود"
    break
  else
    echo "وضعیت: $STATUS - در حال انتظار..."
    sleep 10
  fi
done

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function checkVideoStatus(videoId) {
    const maxAttempts = 60;
    const waitTime = 10000;

    for (let attempt = 0; attempt < maxAttempts; attempt++) {
        const videoStatus = await client.videos.retrieve(videoId);

        if (videoStatus.status === 'completed') {
            console.log(`ویدیو ${videoId} تکمیل شد!`);

            // دانلود ویدیو
            const response = await client.videos.retrieveContent(videoId);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync(`video_${videoId}.mp4`, buffer);

            return true;
        } else if (videoStatus.status === 'failed') {
            console.log(`تولید ویدیو ناموفق بود: ${videoStatus.error}`);
            return false;
        }

        console.log(`وضعیت: ${videoStatus.status}, پیشرفت: ${videoStatus.progress}%`);
        await new Promise(resolve => setTimeout(resolve, waitTime));
    }

    console.log('زمان انتظار برای تکمیل ویدیو به پایان رسید');
    return false;
}

// مثال استفاده
const video = await client.videos.create({
    model: 'veo-3.1-fast-generate-001',
    prompt: 'صحنه باغ آرام با آواز پرندگان',
    size: '1280x720',
    seconds: '4'
});

await checkVideoStatus(video.id);

```


## بهترین شیوه‌ها برای نوشتن پرامپت

ایجاد پرامپت‌های موثر برای تولید ویدیوهای با کیفیت بالا با Veo حیاتی است. این راهنماها را دنبال کنید:

### توصیفی و دقیق باشید

پرامپت‌های خوب توصیفی و واضح هستند. این عناصر را در پرامپت خود بگنجانید:

- **موضوع:** شی، شخص، حیوان یا منظره (منظره شهری، طبیعت، وسایل نقلیه، توله سگ‌ها)
- **عمل:** کاری که موضوع انجام می‌دهد (راه رفتن، دویدن، چرخاندن سر)
- **استایل:** جهت خلاقانه (علمی-تخیلی، فیلم ترسناک، فیلم نوآر، کارتونی، استایل‌های انیمیشن)
- **موقعیت و حرکت دوربین:** [اختیاری] نمای هوایی، سطح چشم، شات بالا به پایین، شات dolly
- **ترکیب‌بندی:** [اختیاری] شات عریض، نمای نزدیک، تک‌شات، دو-شات
- **فوکوس و جلوه‌های لنز:** [اختیاری] فوکوس کم، فوکوس عمیق، فوکوس نرم، لنز ماکرو، لنز زاویه عریض
- **فضا:** [اختیاری] تن‌های آبی، شب، تن‌های گرم، شرایط نوری

**مثال خوب:**
```
توله سگ گلدن رتریور در چمنزار آفتابی در زمان طلایی بازی می‌کند،
دوربین به آرامی توله سگ را دنبال می‌کند که در علف‌های بلند می‌دود،
عمق میدان سینمایی با افکت bokeh، درجه‌بندی رنگ گرم،
صداهای خش‌خش ملایم و پارس نرم
```

**مثال ضعیف:**
```
سگی در حال بازی
```

### پرامپت‌نویسی برای صدا

Veo 3.1 صدای بومی همگام‌سازی شده با ویدیو تولید می‌کند. می‌توانید نشانه‌هایی برای موارد زیر ارائه دهید:

**دیالوگ:** از گیومه برای گفتار خاص استفاده کنید
```
"این باید کلید باشد"، او زمزمه کرد، صدایش در سالن خالی طنین‌انداز شد
```

**جلوه‌های صوتی (SFX):** صداها را به صراحت توصیف کنید
```
جیغ بلند لاستیک‌ها، غرش موتور، له شدن فلز
```

**صدای محیطی:** منظر صوتی محیط را توصیف کنید
```
یک زمزمه ضعیف و عجیب در پس‌زمینه طنین‌انداز می‌شود، جیک‌جیک دور پرندگان، خش‌خش برگ‌ها در باد
```

**مثال با صدای غنی:**
```
شات عریض از جنگل مه‌آلود شمال غربی اقیانوس آرام. دو کوهنورد خسته،
یک مرد و یک زن، از میان سرخس‌ها عبور می‌کنند وقتی مرد ناگهان می‌ایستد.
مرد: (دست روی چاقو) "این خرس معمولی نیست." زن: (صدا با ترس)
"پس چیست؟" صدای پوست درخت خشن، شکستن شاخه‌ها، قدم‌های روی زمین مرطوب.
```

### مشخص کردن حرکات دوربین

دستورالعمل‌های حرکت دوربین را در صورت مرتبط بودن بگنجانید:
- "دوربین به چپ حرکت می‌کند تا نشان دهد..."
- "زوم آهسته روی موضوع..."
- "شات هوایی پهپاد در حال نزول..."
- "شات POV از وسیله نقلیه در حرکت..."
- "شات dolly ردیاب دنبال کننده..."

### تعیین بافت صحنه

زمان، مکان و فضا را مشخص کنید:
- زمان روز (زمان طلایی، نیمه شب، سحر، غروب)
- شرایط آب و هوایی (مه‌آلود، آفتابی، بارانی، طوفانی)
- جزئیات مکان (خیابان شهری، پاکی جنگل، ساحل، کوه‌ها)
- نورپردازی (سایه‌های دراماتیک، نور محیطی نرم، درخشش نئون)

### استفاده از توضیحات زمانی

توصیف کنید چگونه صحنه تحول می‌یابد:
- "شروع با نمای نزدیک، سپس عقب کشیدن برای نشان دادن..."
- "خورشید به تدریج بر فراز کوه‌ها طلوع می‌کند..."
- "امواج با شدت فزاینده به صخره‌ها می‌کوبند..."
- "دوربین به آرامی به داخل حرکت می‌کند تا نشان دهد..."

## راهنمای رزولوشن و نسبت تصویر

### نحوه نگاشت `size` به نسبت تصویر و رزولوشن

API ویدیوی AvalAI پارامتر استاندارد `size` به شکل `"WIDTHxHEIGHT"` را می‌پذیرد و به‌طور خودکار نسبت تصویر و رزولوشن متناظر Veo را اعمال می‌کند:

| مقدار `size` | جهت‌گیری | نسبت تصویر | رزولوشن |
|--------------|----------|------------|---------|
| `1280x720`   | افقی     | `16:9`     | `720p`  |
| `1920x1080`  | افقی     | `16:9`     | `1080p` |
| `720x1280`   | عمودی    | `9:16`     | `720p`  |
| `1080x1920`  | عمودی    | `9:16`     | `1080p` |

**قوانین نگاشت:**

- **نسبت تصویر** از روی جهت‌گیری محاسبه می‌شود: اگر `height > width` باشد، درخواست با `9:16` ارسال می‌شود؛ در غیر این صورت `16:9`.
- **رزولوشن** از روی ضلع کوچک‌تر محاسبه می‌شود: `≥1080` → `1080p`، `≥720` → `720p`، `≥2160` (یا ضلع بزرگ‌تر `≥3840`) → `4k`.
- اگر `size` ارسال نکنید، مقدار پیش‌فرض Veo یعنی `720p` با نسبت `16:9` اعمال می‌شود.

به این ترتیب هر مقدار `WIDTHxHEIGHT` پشتیبانی‌شده، رزولوشن و جهت‌گیری صحیح را تولید می‌کند و نیازی نیست برای اندازه‌های استاندارد، نسبت تصویر یا رزولوشن را جداگانه تنظیم کنید.

### پیشرفته: بازنویسی مستقیم نسبت تصویر و رزولوشن

می‌توانید `size` را کنار بگذارید و فیلدهای بومی Veo را از طریق `extra_body` ارسال کنید. مقادیر موجود در `extra_body` نسبت به مقادیر استنباط‌شده از `size` اولویت دارند. این روش برای مواردی مفید است که مثلا ویدیوی 9:16 با رزولوشن 1080p می‌خواهید، یا نیاز به تنظیم `negativePrompt`، `personGeneration` و غیره دارید.

```python
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="یک کوچه شلوغ سایبرپانک در شب",
    seconds="6",
    extra_body={
        "aspectRatio": "9:16",  # "16:9" یا "9:16"
        "resolution": "1080p",  # "720p"، "1080p" یا "4k" (در صورت پشتیبانی)
        # "negativePrompt": "تار، کیفیت پایین",
        # "personGeneration": "allow_adult",
    },
)
```

برای راحتی، `aspect_ratio` (با خط زیر) نیز در `extra_body` پذیرفته می‌شود و معادل `aspectRatio` در نظر گرفته می‌شود.

### انتخاب رزولوشن مناسب

Veo از دو رزولوشن اصلی با نیازهای خاص نسبت تصویر پشتیبانی می‌کند:

**رزولوشن 720p**
- **افقی (16:9):** `1280x720` یا هر اندازه 16:9 که ضلع کوچک‌تر آن `720` است
- **عمودی (9:16):** `720x1280` یا هر اندازه 9:16 که ضلع کوچک‌تر آن `720` است
- بهترین برای: شبکه‌های اجتماعی، محتوای وب، پلتفرم‌های موبایل
- مورد استفاده: استوری اینستاگرام، تیک‌تاک، ریلز، یوتیوب شورتز

**رزولوشن 1080p (فقط 16:9)**
- **افقی:** `1920x1080`
- بهترین برای: محتوای وب با کیفیت بالا، ویدیوهای حرفه‌ای
- مورد استفاده: یوتیوب، ارائه‌ها، مواد بازاریابی
- **توجه:** فقط برای نسبت تصویر 16:9 موجود است

### ملاحظات مدت زمان

- **کوتاه (4 ثانیه):** کلیپ‌های سریع شبکه‌های اجتماعی، حلقه‌ها، انتقال‌ها
- **متوسط (6 ثانیه):** بخش‌های داستان، نمایش محصول
- **بلند (8 ثانیه):** ایجاد صحنه، توالی‌های روایی، اعمال دقیق

## استراتژی‌های بهینه‌سازی هزینه

هزینه‌ها را بهینه کنید در حالی که کیفیت را حفظ می‌کنید:

### 1. با veo-3.1-fast برای تست شروع کنید

از مدل سریع برای تکرارهای اولیه استفاده کنید:
```python
# ابتدا با veo-3.1-fast تست کنید
response = client.videos.create(
    model="veo-3.1-fast-generate-001",  # $0.15/ثانیه
    prompt="پرامپت تست شما",
    size="1280x720",
    seconds="4",  # با مدت زمان کوتاه‌تر شروع کنید
)
```

### 2. از مدت زمان مناسب استفاده کنید

فقط مدت زمانی که نیاز دارید تولید کنید:
- 4 ثانیه: حلقه‌های سریع، انتقال‌ها ($0.60 - $1.60)
- 6 ثانیه: کلیپ‌های استاندارد ($0.90 - $2.40)
- 8 ثانیه: صحنه‌های کامل ($1.20 - $3.20)

### 3. رزولوشن را با دقت انتخاب کنید

1080p فقط برای نسبت تصویر 16:9 پشتیبانی می‌شود:
- از 720p برای ویدیوهای عمودی (9:16) استفاده کنید
- فقط زمانی از 1080p استفاده کنید که کیفیت بالا ضروری است
- ابتدا با 720p برای اصلاح پرامپت‌ها تست کنید

### 4. ویدیوها را به صورت استراتژیک گسترش دهید

محتوای طولانی‌تر با گسترش ویدیوهای موجود ایجاد کنید:
```python
# تولید ویدیوی پایه (8 ثانیه)
base_video = client.videos.create(
    model="veo-3.1-fast-generate-001", prompt="صحنه آغازین...", seconds="8"
)

# چندین بار گسترش برای محتوای طولانی‌تر
extended_1 = client.videos.extend(
    video_id=base_video.id, prompt="ادامه عمل...", seconds="8"
)
```

## مدیریت خطا و عیب‌یابی

### مشکلات رایج و راه‌حل‌ها

#### زمان انتظار تولید
اگر تولید بیشتر از حد انتظار طول بکشد:
- مدت زمان timeout دریافت وضعیت را افزایش دهید (تا 6 دقیقه در ساعات اوج)
- وضعیت ویدیو را برای پیام‌های خطا بررسی کنید
- از backoff نمایی در منطق دریافت وضعیت استفاده کنید

#### پارامتر size نامعتبر
اطمینان حاصل کنید `size` با قابلیت‌های مدل مطابقت دارد. جهت‌گیری از روی `height > width` استنباط می‌شود (عمودی → `9:16`، در غیر این صورت `16:9`) و رزولوشن از روی ضلع کوچک‌تر (`720` → `720p`، `1080` → `1080p`):

- **720p:** `1280x720` (16:9) یا `720x1280` (9:16)
- **1080p:** `1920x1080` (فقط 16:9 — Veo از 1080p عمودی پشتیبانی نمی‌کند)

اگر به کنترل دقیق نیاز دارید، `aspectRatio` و `resolution` را از طریق `extra_body` ارسال کنید — این مقادیر نسبت به آنچه از `size` استنباط می‌شود اولویت دارند.

#### فیلترهای ایمنی صدا
Veo 3.1 ممکن است
ویدیوها را به دلیل فیلترهای ایمنی مسدود کند:
- در صورت مسدود شدن ویدیو هزینه‌ای دریافت نمی‌شود
- پرامپت‌ها را اصلاح کنید تا از نقض سیاست محتوا جلوگیری شود
- دیالوگ یا توضیحات صوتی تهاجمی را حذف کنید

#### مشکلات مرجع تصویر
هنگام استفاده از مراجع:
- اطمینان حاصل کنید تصاویر به درستی فرمت شده‌اند (JPEG، PNG)
- محدودیت‌های اندازه فایل را بررسی کنید (تصاویر: 20MB)
- تایید کنید تصویر واضح و مرتبط با پرامپت است

## موارد استفاده پیشرفته

### ایجاد توالی‌های ویدیویی

ویدیوهای مرتبط تولید کنید که یک توالی را تشکیل می‌دهند:

```python
import requests

scenes = [
    {
        "prompt": "شات وسیع شهر آینده‌نگرانه در سحر، دوربین به آرامی به جلو حرکت می‌کند، صداهای محیطی شهر",
        "seconds": "8",
    },
    {
        "prompt": "شات متوسط خیابان شلوغ با وسایل نقلیه پرنده، دوربین به راست حرکت می‌کند، زمزمه موتورها و گفتگوی جمعیت",
        "seconds": "8",
    },
    {
        "prompt": "نمای نزدیک قهرمان که از پنجره بیرون نگاه می‌کند، دوربین به آرامی زوم می‌کند، موسیقی تاملی",
        "seconds": "8",
    },
]

generation_ids = []
for i, scene in enumerate(scenes):
    response = requests.post(
        "https://api.avalai.ir/v1/videos",
        headers={"Authorization": "Bearer AVALAI_API_KEY"},
        json={
            "model": "veo-3.1-generate-001",
            "prompt": scene["prompt"],
            "size": "1920x1080",
            "seconds": scene["seconds"],
        },
    )
    generation_ids.append(response.json()["id"])

print(f"توالی با {len(generation_ids)} صحنه تولید شد")
```

### ویدیوهای نمایشی محصول

دموهای جذاب محصول با صدا ایجاد کنید:

```python
product_prompts = {
    "hero": "گوشی هوشمند شیک به آرامی در پس‌زمینه سفید می‌چرخد، نورپردازی دراماتیک با سایه‌های نرم، سبک عکاسی حرفه‌ای محصول، صدای whoosh ظریف",
    "feature_1": "نمای نزدیک صفحه گوشی که رابط برنامه را نشان می‌دهد، انگشت به نرمی محتوا را لمس می‌کند، المان‌های UI مدرن، صداهای tap نرم",
    "feature_2": "گوشی در دست در حال پرداخت در ترمینال، انیمیشن تیک سبز، سناریوی استفاده واقعی، بوق تایید پرداخت",
}

for key, prompt in product_prompts.items():
    response = client.videos.create(
        model="veo-3.1-fast-generate-001",
        prompt=prompt,
        size="1280x720",
        seconds="6",
    )
    print(f"تولید شد {key}: {response.id}")
```

### محتوای شبکه‌های اجتماعی

بهینه‌سازی برای پلتفرم‌های مختلف:

```python
social_configs = {
    "instagram_story": {
        "size": "1080x1920",  # عمودی
        "seconds": "4",
        "prompt": "محتوای سبک زندگی پرانرژی با رنگ‌های زنده، موسیقی پس‌زمینه شاد",
    },
    "youtube_short": {
        "size": "1080x1920",  # عمودی
        "seconds": "8",
        "prompt": "آغاز جذب توجه با قلاب در 3 ثانیه اول، روایت واضح",
    },
    "twitter_feed": {
        "size": "1280x720",  # افقی
        "seconds": "4",
        "prompt": "پیام واضح به سرعت ارائه شده، ترکیب‌بندی متن-دوستانه، صدای مختصر",
    },
}

for platform, config in social_configs.items():
    video = client.videos.create(model="veo-3.1-fast-generate-001", **config)
    print(f"تولید شده برای {platform}: {video.id}")
```

## ردیابی و شناسایی

### استفاده از safety_identifier برای ردیابی داخلی

پارامتر `safety_identifier` به شما امکان می‌دهد درخواست‌های ویدیو را با سیستم‌های ردیابی داخلی خود مرتبط کنید. این برای موارد زیر مفید است:

- **ردیابی دپارتمان:** شناسایی اینکه کدام تیم یا دپارتمان ویدیو را تولید کرده است
- **مدیریت پروژه:** مرتبط کردن ویدیوها با پروژه‌ها یا کمپین‌های خاص
- **تخصیص هزینه:** ردیابی هزینه‌ها در واحدهای تجاری مختلف
- **مسیرهای حسابرسی:** نگهداری سوابق برای اهداف انطباق

```python
# مثال: استفاده از safety_identifier برای ردیابی دپارتمان
video = client.videos.create(
    model="veo-3.1-fast-generate-001",
    prompt="ویدیوی دمو محصول با روایت حرفه‌ای",
    size="1920x1080",
    seconds="8",
    safety_identifier="marketing_dept_q4_campaign",
)
```

### فیلتر ویدیوها بر اساس شناسه

می‌توانید لیست ویدیوهای خود را با استفاده از پارامتر `safety_identifier` فیلتر کنید:

```bash
# لیست تمام ویدیوها برای یک دپارتمان خاص
curl -X GET "https://api.avalai.ir/v1/videos?safety_identifier=marketing_dept_q4_campaign" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

### استفاده از request_id برای ردیابی هزینه

هر پاسخ ویدیو شامل یک `request_id` (UUID v7) است که می‌توانید برای ردیابی دقیق هزینه استفاده کنید:

```python
video = client.videos.create(
    model="veo-3.1-generate-001",
    prompt="پرامپت ویدیوی شما",
    size="1920x1080",
    seconds="8",
)

# ذخیره request_id برای جستجوی هزینه
request_id = video.request_id
print(f"Request ID برای ردیابی هزینه: {request_id}")

# بعدا از /user/v1/transactions/lookup برای دریافت هزینه‌های دقیق استفاده کنید
```

همچنین می‌توانید ویدیوها را بر اساس `request_id` فیلتر کنید تا یک ویدیوی خاص را پیدا کنید:

```bash
curl -X GET "https://api.avalai.ir/v1/videos?request_id=019b4797-14a2-79a0-8635-2cf8dd84820c" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

برای جزئیات بیشتر در مورد ردیابی هزینه، به مستندات [Response Headers](fa/api-reference/response-headers.md) و [User API](fa/api-reference/user.md) مراجعه کنید.

## محدودیت‌ها و ملاحظات

### تاخیر درخواست
- **حداقل:** 11 ثانیه
- **حداکثر:** 6 دقیقه در ساعات اوج
- برای برنامه‌های حساس به زمان برنامه‌ریزی کنید

### نگهداری ویدیو
- ویدیوهای تولید شده روی سرور به مدت **2 روز** ذخیره می‌شوند
- ویدیوهای خود را ظرف 2 روز دانلود کنید تا نسخه محلی ذخیره شود
- ویدیوهای گسترش‌یافته به عنوان ویدیوهای جدید تولید شده در نظر گرفته می‌شوند

### واترمارک
- ویدیوهای ایجاد شده توسط Veo با استفاده از **SynthID** واترمارک می‌شوند
- این ابزار گوگل برای واترمارک و شناسایی محتوای تولید شده با هوش مصنوعی است
- ویدیوها را می‌توان با استفاده از پلتفرم تایید SynthID تایید کرد

### فیلترهای ایمنی
- ویدیوهای تولید شده از فیلترهای ایمنی عبور می‌کنند
- فرآیندهای بررسی حفظ حافظه به کاهش ریسک‌های حریم خصوصی، حق نسخه‌برداری و تعصب کمک می‌کند
- صدا ممکن است به دلیل فیلترهای ایمنی مسدود شود (در صورت مسدود شدن هزینه‌ای دریافت نمی‌شود)

### محدودیت‌های منطقه‌ای
- در مکان‌های EU، UK، CH و MENA، محدودیت‌های خاصی برای تولید شخص اعمال می‌شود
- Veo 3.1: فقط تنظیم `allow_adult` پشتیبانی می‌شود

## منابع مرتبط

- [مرجع API ویدیو](fa/api-reference/videos.md) - مستندات کامل API
- [مدل‌های گوگل](fa/providers/google.md) - تمام مدل‌های هوش مصنوعی گوگل از جمله Veo
- [قیمت‌گذاری](fa/pricing.md) - اطلاعات دقیق قیمت‌گذاری
- [راهنمای انتخاب مدل](fa/guides/model-selection.md) - انتخاب مدل مناسب برای نیازهای شما

## خلاصه

مدل‌های Veo 3.1 قابلیت‌های قدرتمند تولید ویدیو با پشتیبانی صدای بومی را از طریق AvalAI API ارائه می‌دهند. نکات کلیدی:

- **دو گزینه مدل:** نسخه‌های استاندارد ($0.40/ثانیه) و سریع ($0.15/ثانیه)
- **صدای بومی:** دیالوگ، جلوه‌های صوتی و صدای محیطی به صورت خودکار تولید می‌شود
- **مدت زمان انعطاف‌پذیر:** 4، 6 یا 8 ثانیه در هر تولید
- **رزولوشن‌های متعدد:** 720p (16:9 و 9:16) و 1080p (فقط 16:9)؛ `size` به‌طور خودکار به نسبت تصویر و رزولوشن صحیح نگاشت می‌شود
- **بازنویسی پیشرفته:** در صورت نیاز `aspectRatio` و `resolution` را مستقیما از طریق `extra_body` ارسال کنید
- **ویژگی‌های پیشرفته:** تصویر به ویدیو، تصاویر مرجع، گسترش ویدیو
- **گردش کار ناهمزمان:** الگوی تولید، دریافت وضعیت، دانلود
- **بهینه‌سازی هزینه:** با مدل سریع شروع کنید، از مدت زمان مناسب استفاده کنید

با Veo آزمایش کنید تا محتوای ویدیویی جذاب با صدای همگام‌سازی شده برای برنامه‌های خود ایجاد کنید.
