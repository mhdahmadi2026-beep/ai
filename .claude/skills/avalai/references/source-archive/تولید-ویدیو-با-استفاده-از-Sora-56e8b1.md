# تولید ویدیو با استفاده از Sora

نحوه تولید ویدیوهای مبتنی بر هوش مصنوعی با استفاده از مدل‌های Sora از OpenAI را از طریق AvalAI API بیاموزید.

## مقدمه

[API ویدیو](fa/api-reference/videos.md) AvalAI اندپوینت‌هایی برای تولید ویدیو با استفاده از مدل‌های Sora از OpenAI ارائه می‌دهد. این مدل‌های پیشرفته می‌توانند ویدیوهای واقع‌گرایانه و خلاقانه از توضیحات متنی ایجاد کنند، با پشتیبانی از:

- **متن به ویدیو:** ایجاد ویدیو از ابتدا بر اساس پرامپت‌های متنی دقیق
- **تصویر به ویدیو:** تولید ویدیو با شروع از یک تصویر مرجع
- **ریمیکس ویدیو:** تغییر و ریمیکس ویدیوهای موجود با پرامپت‌های جدید
- **پردازش ناهمزمان:** ایجاد job رندر، بررسی وضعیت، سپس دانلود assetهای ویدیوی تکمیل‌شده

این راهنما استفاده از این قابلیت‌ها را از طریق AvalAI برای ایجاد محتوای ویدیویی جذاب پوشش می‌دهد.

> این راهنما مفاهیم مستندات رسمی OpenAI درباره [Video generation with Sora](https://developers.openai.com/api/docs/guides/video-generation) را برای endpointها، کلید API، دسترسی مدل و پشتیبانی routeهای AvalAI تطبیق می‌دهد.

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

AvalAI دسترسی به دو مدل تولید ویدیوی Sora را فراهم می‌کند که هر کدام برای موارد استفاده مختلف بهینه شده‌اند:

### sora-2

بهترین برای نیازهای استاندارد تولید ویدیو:
- **پشتیبانی رزولوشن:** 720x1280 (عمودی) و 1280x720 (افقی)
- **مدت زمان:** حداقل 4 ثانیه. مقادیر پشتیبانی‌شده از طریق Videos API AvalAI عبارت‌اند از `"4"`، `"8"` و `"12"`. برای iteration با 4 تا 8 ثانیه شروع کنید و فقط وقتی shot به زمان بیشتری نیاز دارد مدت را افزایش دهید.
- **قیمت:** $0.10 به ازای هر ثانیه
- **موارد استفاده:** محتوای شبکه‌های اجتماعی، مواد بازاریابی، ویدیوهای با کیفیت استاندارد
- **پردازش:** ناهمزمان با دریافت وضعیت

### sora-2-pro

طراحی شده برای محتوای حرفه‌ای و با کیفیت بالا:
- **پشتیبانی رزولوشن:** تمام رزولوشن‌های sora-2 به علاوه 1024x1792 (عمودی فوق‌العاده) و 1792x1024 (افقی فوق‌العاده)
- **مدت زمان:** حداقل 4 ثانیه. مقادیر پشتیبانی‌شده از طریق Videos API AvalAI عبارت‌اند از `"4"`، `"8"` و `"12"`. کلیپ‌های طولانی‌تر و رزولوشن‌های بالاتر زمان پردازش و هزینه بیشتری دارند.
- **قیمت:** $0.30 به ازای هر ثانیه (رزولوشن‌های استاندارد)، $0.50 به ازای هر ثانیه (رزولوشن‌های فوق‌العاده)
- **موارد استفاده:** محتوای حرفه‌ای، تولیدات با کیفیت بالا، ویدیوهای سینمایی
- **پردازش:** ناهمزمان با دریافت وضعیت

هر دو مدل از تصاویر مرجع و قابلیت‌های ریمیکس ویدیو پشتیبانی می‌کنند.

> **⚠️ هشدار: مدت زمان باید مضربی از 4 ثانیه باشد**
>
> برای مدل‌های Sora، **حداقل مدت زمان ویدیو 4 ثانیه** است و مقادیر پشتیبانی‌شده برای پارامتر `seconds` عبارت‌اند از `"4"`، `"8"` و `"12"`. مدل‌های تولید ویدیو معمولا فقط مدت‌زمان‌هایی را می‌پذیرند که مضربی از 4 ثانیه باشند؛ این الگو در بیشتر مدل‌ها رایج است، اما برای همه مدل‌ها تضمین نمی‌شود. درخواست مدت زمان پشتیبانی‌نشده با خطای `400 Bad Request` مواجه خواهد شد.

## نکات گردش‌کار Sora از OpenAI برای AvalAI

مستندات فعلی Sora در OpenAI یک چرخه production کامل را توضیح می‌دهد: ایجاد job رندر، پایش وضعیت، دانلود MP4، نگه‌داری assetهای پشتیبان و استفاده از عملیات تکمیلی برای reference، character، extension، edit یا صف‌های batch. در AvalAI ابتدا routeهای مستندشده `/v1/videos` را استفاده کنید و قابلیت‌های میزبانی‌شده جدید OpenAI را تا زمانی که در مرجع API AvalAI نیامده‌اند وابسته به route بدانید.

| گردش‌کار | مفهوم در OpenAI | مسیر AvalAI امروز |
| -------- | --------------- | ----------------- |
| شروع رندر | `POST /v1/videos` یک job با `id`، `status` و progress برمی‌گرداند | از `POST https://api.avalai.ir/v1/videos` با `model`، `prompt`، `size`، `seconds` و در صورت نیاز `safety_identifier` استفاده کنید. |
| پایش پیشرفت | polling با `GET /v1/videos/{video_id}` یا webhook | هر 10 تا 20 ثانیه polling کنید؛ webhook را فقط اگر AvalAI برای حساب یا route شما فعال کرده باشد استفاده کنید. |
| دانلود خروجی | `GET /v1/videos/{video_id}/content` فایل MP4 را stream می‌کند | خروجی را سریع دانلود و در storage خودتان کپی کنید؛ URL خروجی تولید را long-term hosting فرض نکنید. |
| هدایت فریم اول | تصویر `input_reference` با اندازه هدف | از `input_reference` multipart با JPEG، PNG یا WebP استفاده کنید و تا حد امکان اندازه تصویر را با `size` هدف هماهنگ نگه دارید. |
| ادامه یا ویرایش ویدیو | OpenAI مسیرهای `/videos/extensions` و `/videos/edits` را مستند کرده و remixهای قدیمی را جایگزین می‌کند | تا زمانی که extensions یا edits برای route شما فهرست نشده‌اند، از route مستندشده remix در AvalAI استفاده کنید. |
| صف‌های آفلاین بزرگ | OpenAI ویدیو را از طریق Batch API هم مستند می‌کند | فقط وقتی مرجع API یا تیم پشتیبانی AvalAI تأیید کرد از batch/video استفاده کنید؛ در غیر این صورت صف و polling را در برنامه خودتان پیاده کنید. |

برای promptهای قابل‌اعتماد، **نوع shot، سوژه، کنش، محیط، حرکت دوربین، نورپردازی و زمان‌بندی** را توصیف کنید. از شخصیت‌های دارای کپی‌رایت، موسیقی دارای کپی‌رایت، افراد واقعی، چهره‌های عمومی و آپلود human likeness خودداری کنید مگر اینکه AvalAI دسترسی لازم را برای حساب شما فعال کرده باشد.

## تولید ساده ویدیو

ساده‌ترین راه برای تولید ویدیو، ارائه یک پرامپت متنی است. API درخواست شما را به صورت ناهمزمان پردازش می‌کند و شما می‌توانید وضعیت تکمیل را بررسی کنید.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد درخواست تولید ویدیو
video = client.videos.create(
    model="sora-2",
    prompt="دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب",
    size="1280x720",
    seconds="4",
    safety_identifier="project_abc123",  # اختیاری: برای ردیابی داخلی
)

print(f"تولید ویدیو شروع شد: {video.id}")
print(f"شناسه درخواست: {video.request_id}")  # شناسه سراسری درخواست

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
# ایجاد درخواست تولید ویدیو
curl -X POST https://api.avalai.ir/v1/videos \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=sora-2" \
  -F "prompt=دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب" \
  -F "size=1280x720" \
  -F "seconds=4" \
  -F "safety_identifier=project_abc123"

# پاسخ شامل request_id برای ردیابی است:
# {"id": "video_...", "request_id": "019b47a0-ece8-75b2-8a4c-40fcf4b49479", ...}

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
        model: 'sora-2',
        prompt: 'دریاچه‌ای آرام در غروب خورشید با کوه‌ها در پس‌زمینه، موج‌های ملایم روی سطح آب',
        size: '1280x720',
        seconds: '4',
        safety_identifier: 'project_abc123'  // اختیاری: برای ردیابی داخلی
    });

    console.log(`تولید ویدیو شروع شد: ${video.id}`);
    console.log(`شناسه درخواست: ${video.request_id}`);  // شناسه سراسری درخواست

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

می‌توانید یک تصویر مرجع برای هدایت تولید ویدیو ارائه دهید. این برای ایجاد ویدیوهایی که از عناصر بصری خاص شروع می‌شوند یا آن‌ها را شامل می‌شوند مفید است.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# ایجاد ویدیو با تصویر مرجع
video = client.videos.create(
    model="sora-2-pro",
    prompt="منظره زنده می‌شود با آب جاری و ابرهای متحرک، پرندگان در بالای سر پرواز می‌کنند",
    input_reference=open("reference_image.jpg", "rb"),
    size="1792x1024",
    seconds="8",
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
  -F "model=sora-2-pro" \
  -F "prompt=منظره زنده می‌شود با آب جاری و ابرهای متحرک، پرندگان در بالای سر پرواز می‌کنند" \
  -F "input_reference=@reference_image.jpg;type=image/jpeg" \
  -F "size=1792x1024" \
  -F "seconds=8"

# دریافت وضعیت (تکرار تا تکمیل)
curl -X GET https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# دانلود زمانی که تکمیل شد
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
        model: 'sora-2-pro',
        prompt: 'منظره زنده می‌شود با آب جاری و ابرهای متحرک، پرندگان در بالای سر پرواز می‌کنند',
        input_reference: fs.createReadStream('reference_image.jpg'),
        size: '1792x1024',
        seconds: '8'
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


## ریمیکس ویدیو

ویدیوهای موجود را با پرامپت‌های جدید ریمیکس کنید تا تغییرات یا اصلاحات ایجاد کنید. از اندپوینت `/videos/{video_id}/remix` استفاده کنید.

```python
from openai import OpenAI
import time

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

# ریمیکس ویدیوی موجود
remixed_video = client.videos.remix(
    video_id="video_691bab4a12248190b1e9123d8648ff4d",
    prompt="گربه به تماشاچیان تشویق‌کننده تعظیم می‌کند",
)

print(f"ریمیکس ویدیو شروع شد: {remixed_video.id}")

# دریافت وضعیت برای تکمیل
while True:
    video_status = client.videos.retrieve(remixed_video.id)

    if video_status.status == "completed":
        print(f"ویدیوی ریمیکس شده آماده است! ID: {video_status.id}")

        # دانلود ویدیوی ریمیکس شده
        with client.with_streaming_response.videos.retrieve_content(
            remixed_video.id
        ) as response:
            with open("remixed_output.mp4", "wb") as f:
                for chunk in response.iter_bytes():
                    f.write(chunk)
        print("ویدیوی ریمیکس شده دانلود شد")
        break
    elif video_status.status == "failed":
        print(f"ریمیکس ناموفق بود: {video_status.error}")
        break

    time.sleep(10)

```

```bash
# ریمیکس ویدیوی موجود
curl -X POST https://api.avalai.ir/v1/videos/video_691bab4a12248190b1e9123d8648ff4d/remix \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "prompt": "گربه به تماشاچیان تشویق‌کننده تعظیم می‌کند"
  }'

# دریافت وضعیت
curl -X GET https://api.avalai.ir/v1/videos/video_691bb11c9f1481908d6c5a0c463fcd94 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# دانلود زمانی که تکمیل شد
curl -X GET https://api.avalai.ir/v1/videos/video_691bb11c9f1481908d6c5a0c463fcd94/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output remixed_output.mp4

```

```javascript
import OpenAI from 'openai';
import fs from 'fs';

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: 'https://api.avalai.ir/v1'
});

async function remixVideo() {
    // ریمیکس ویدیوی موجود
    const remixedVideo = await client.videos.remix(
        'video_691bab4a12248190b1e9123d8648ff4d',
        {
            prompt: 'گربه به تماشاچیان تشویق‌کننده تعظیم می‌کند'
        }
    );

    console.log(`ریمیکس ویدیو شروع شد: ${remixedVideo.id}`);

    // دریافت وضعیت برای تکمیل
    while (true) {
        const videoStatus = await client.videos.retrieve(remixedVideo.id);
        
        if (videoStatus.status === 'completed') {
            console.log(`ویدیوی ریمیکس شده آماده است! ID: ${videoStatus.id}`);
            
            // دانلود ویدیوی ریمیکس شده
            const response = await client.videos.retrieveContent(remixedVideo.id);
            const buffer = Buffer.from(await response.arrayBuffer());
            fs.writeFileSync('remixed_output.mp4', buffer);
            console.log('ویدیوی ریمیکس شده دانلود شد');
            break;
        } else if (videoStatus.status === 'failed') {
            console.log(`ریمیکس ناموفق بود: ${videoStatus.error}`);
            break;
        }

        await new Promise(resolve => setTimeout(resolve, 10000));
    }
}

remixVideo();

```


## بررسی وضعیت ویدیو

برای برنامه‌های تولیدی، دریافت وضعیت راهی قابل اعتماد برای بررسی زمان تکمیل تولید ویدیو فراهم می‌کند.

```python
from openAI import OpenAI
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

    print("تایم‌اوت در انتظار تکمیل ویدیو")
    return False


# مثال استفاده
video = client.videos.create(
    model="sora-2", prompt="صحنه‌ای آرام از باغ", size="1280x720", seconds="4"
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
    
    console.log('تایم‌اوت در انتظار تکمیل ویدیو');
    return false;
}

// مثال استفاده
const video = await client.videos.create({
    model: 'sora-2',
    prompt: 'صحنه‌ای آرام از باغ',
    size: '1280x720',
    seconds: '4'
});

await checkVideoStatus(video.id);

```


## بهترین شیوه‌ها برای پرامپت‌نویسی

ایجاد پرامپت‌های مؤثر برای تولید ویدیوهای با کیفیت بالا حیاتی است. این دستورالعمل‌ها را دنبال کنید:

### توصیفی و خاص باشید

توضیحات دقیق شامل موارد زیر ارائه دهید:
- **عناصر بصری:** رنگ‌ها، نورپردازی، ترکیب‌بندی
- **حرکت:** حرکات دوربین، اقدامات سوژه
- **سبک:** سینمایی، واقع‌گرایانه، هنری
- **حال و هوا:** جوی، پرانرژی، آرام

**مثال خوب:**
```
توله سگ گلدن رتریور در یک چمنزار آفتابی در زمان طلایی بازی می‌کند،
دوربین آهسته توله را دنبال می‌کند که در میان علف‌های بلند می‌دود،
عمق میدان سینمایی با افکت بوکه، رنگ‌آمیزی گرم
```

**مثال ضعیف:**
```
سگی که بازی می‌کند
```

### حرکات دوربین را مشخص کنید

دستورالعمل‌های حرکت دوربین را در صورت لزوم اضافه کنید:
- "دوربین به سمت چپ می‌چرخد تا نشان دهد..."
- "زوم آهسته به سوژه..."
- "تصویر هوایی پهپاد در حال پایین آمدن..."
- "شات تعقیبی دستی که دنبال می‌کند..."

### زمینه صحنه را تنظیم کنید

زمان، مکان و جو را مشخص کنید:
- زمان روز (ساعت طلایی، نیمه‌شب، سحر)
- شرایط آب و هوا (مه‌آلود، آفتابی، بارانی)
- جزئیات مکان (خیابان شهری، پاکی جنگل، ساحل)
- نورپردازی (سایه‌های دراماتیک، نور محیطی ملایم)

### از توصیفات زمانی استفاده کنید

نحوه تکامل صحنه را توصیف کنید:
- "شروع با نمای نزدیک، سپس عقب کشیدن برای نمایش..."
- "خورشید به تدریج بر فراز کوه‌ها طلوع می‌کند..."
- "امواج با شدت فزاینده به صخره‌ها برخورد می‌کنند..."

## راهنمای رزولوشن و مدت زمان

### انتخاب رزولوشن مناسب

رزولوشن‌های مختلف اهداف متفاوتی دارند:

**افقی (1280x720, 1792x1024)**
- بهترین برای: محتوای سینمایی، مناظر، صحنه‌های گسترده
- مورد استفاده: ویدیوهای یوتیوب، ارائه‌ها، محتوای وب

**عمودی (720x1280, 1024x1792)**
- بهترین برای: شبکه‌های اجتماعی (استوری اینستاگرام، تیک‌تاک، ریلز)
- مورد استفاده: محتوای موبایل‌محور، پلتفرم‌های ویدیوی عمودی

**ملاحظات مدت زمان**

حداقل مدت زمان پشتیبانی‌شده در مدل‌های Sora برابر با 4 ثانیه است و مقادیر مجاز `seconds` عبارت‌اند از `"4"`، `"8"` و `"12"` (مضرب‌های 4 ثانیه).

- **کوتاه (4 ثانیه):** کلیپ‌های سریع شبکه‌های اجتماعی، حلقه‌ها
- **متوسط (8 ثانیه):** بخش‌های داستان، دموهای محصول
- **بلند (12 ثانیه):** ایجاد صحنه، توالی‌های روایی و spotهای کامل‌تر. فقط وقتی prompt، حرکت و قاب‌بندی پایدار شد استفاده کنید، چون jobهای طولانی‌تر latency و هزینه را افزایش می‌دهند.

## استراتژی‌های بهینه‌سازی هزینه

بهینه‌سازی هزینه‌ها با حفظ کیفیت:

### 1. ابتدا با sora-2 تست کنید

از مدل استاندارد برای تکرارهای اولیه استفاده کنید:
```python
# ابتدا با sora-2 تست کنید
response = requests.post(
    "https://api.avalai.ir/v1/videos",
    json={
        "model": "sora-2",  # $0.10/ثانیه
        "prompt": "پرامپت تست شما",
        "size": "1280x720",
        "seconds": 4,  # با مدت زمان کوتاه‌تر شروع کنید
    },
)
```

### 2. از مدت زمان مناسب استفاده کنید

فقط مدت زمانی که نیاز دارید را تولید کنید:
- 4 ثانیه: حلقه‌های سریع، انتقال‌ها ($0.40 - $1.20)
- 8 ثانیه: کلیپ‌های استاندارد ($0.80 - $2.40)
- 12 ثانیه: صحنه‌های کامل ($1.20 - $3.60)

### 3. رزولوشن را عاقلانه انتخاب کنید

رزولوشن‌های فوق‌العاده (1024x1792, 1792x1024) با sora-2-pro $0.50/ثانیه هزینه دارند:
- فقط زمانی استفاده کنید که کیفیت بالا ضروری است
- رزولوشن استاندارد را برای شبکه‌های اجتماعی در نظر بگیرید
- ابتدا با رزولوشن پایین‌تر تست کنید

### 4. درخواست‌های مشابه را دسته‌بندی کنید

چندین ویدیوی مرتبط را به صورت دسته‌ای تولید کنید:
```python
prompts = ["صحنه 1: شات باز...", "صحنه 2: سکانس اکشن...", "صحنه 3: شات پایانی..."]

for prompt in prompts:
    requests.post(
        "https://api.avalai.ir/v1/videos",
        json={"model": "sora-2", "prompt": prompt, "size": "1280x720", "seconds": 4},
    )
```

## رفع مشکلات رایج

### مشکلات رایج و راه‌حل‌ها

#### تایم‌اوت تولید
اگر تولید بیشتر از حد انتظار طول کشید:
- مدت زمان تایم‌اوت دریافت وضعیت را افزایش دهید
- وضعیت ویدیو را برای پیام‌های خطا بررسی کنید
- از backoff نمایی در منطق دریافت وضعیت استفاده کنید

#### پارامتر اندازه نامعتبر
اطمینان حاصل کنید اندازه با قابلیت‌های مدل مطابقت دارد:
- **sora-2:** فقط 720x1280، 1280x720
- **sora-2-pro:** تمام اندازه‌ها شامل رزولوشن‌های فوق‌العاده

#### رد پرامپت
اگر پرامپت‌ها رد شدند:
- محتوای صریح یا خشونت را حذف کنید
- از ارجاعات کاراکترهای دارای حق نشر خودداری کنید
- از اصطلاحات توصیفی به جای برندی استفاده کنید

#### مشکلات مرجع تصویر/ویدیو
هنگام استفاده از مراجع:
- اطمینان حاصل کنید کدگذاری base64 صحیح است
- محدودیت‌های اندازه فایل را بررسی کنید (تصاویر: 20MB، ویدیوها: 512MB)
- نوع MIME را در URL داده تایید کنید

## ردیابی و شناسایی

API ویدیو قابلیت‌های ردیابی داخلی برای جریان‌های کاری سازمانی و معماری‌های چند سرویسی فراهم می‌کند.

### شناسه درخواست (Request ID)

هر پاسخ ویدیو شامل فیلد `request_id` است - یک UUID v7 که درخواست را به طور منحصر به فرد شناسایی می‌کند. این همان شناسه‌ای است که در هدر پاسخ `avalai-request-id` برگردانده می‌شود:

```python
video = client.videos.create(
    model="sora-2",
    prompt="پرامپت ویدیوی شما",
    size="1280x720",
    seconds="4",
)

# دسترسی به شناسه درخواست برای ردیابی
print(f"شناسه درخواست: {video.request_id}")
# خروجی: شناسه درخواست: 019b47a0-ece8-75b2-8a4c-40fcf4b49479
```

از `request_id` برای موارد زیر استفاده کنید:
- ردیابی هزینه‌ها از طریق جستجوی تراکنش [User API](/fa/api-reference/user.md)
- همبستگی درخواست‌ها در زیرساخت لاگ‌گیری
- رفع اشکال مشکلات با تیکت‌های پشتیبانی
- فیلتر کردن ویدیوها هنگام لیست کردن: `GET /v1/videos?request_id=019b47a0-...`

### شناسه ایمنی (Safety Identifier)

پارامتر اختیاری `safety_identifier` به شما امکان می‌دهد شناسه ردیابی خود را به درخواست‌های ویدیو پیوست کنید:

```python
video = client.videos.create(
    model="sora-2",
    prompt="ویدیوی نمایش محصول",
    size="1280x720",
    seconds="4",
    safety_identifier="marketing_campaign_2025_q1",  # شناسه داخلی شما
)
```

این برای موارد زیر مفید است:
- **ردیابی بخش‌ها**: برچسب‌گذاری درخواست‌ها با کدهای بخش (`dept_marketing`، `dept_engineering`)
- **مدیریت پروژه**: مرتبط کردن ویدیوها با شناسه‌های پروژه (`project_12345`)
- **تخصیص هزینه**: ردیابی هزینه‌ها در واحدهای تجاری مختلف
- **هماهنگی سرویس‌های همزمان**: زمانی که چندین سرویس نیاز به استعلام همان ویدیو دارند

فیلتر کردن ویدیوها بر اساس `safety_identifier`:
```bash
curl -X GET "https://api.avalai.ir/v1/videos?safety_identifier=marketing_campaign_2025_q1" \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```

## منابع مرتبط

- [مرجع API ویدیو](fa/api-reference/videos.md) - مستندات کامل API
- [مدل‌های OpenAI](fa/providers/openai.md) - مشخصات مدل‌های Sora
- [راهنمای قیمت‌گذاری](fa/pricing.md) - اطلاعات دقیق قیمت‌گذاری
- [راهنمای تولید تصویر](fa/guides/image-generation.md) - تولید محتوای بصری مرتبط
- [بهترین شیوه‌ها](fa/guides/best-practices.md) - دستورالعمل‌های کلی استفاده از API
- [مدیریت خطا](fa/guides/error-handling.md) - استراتژی‌های جامع مدیریت خطا
