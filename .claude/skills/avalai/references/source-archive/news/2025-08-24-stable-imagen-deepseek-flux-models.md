# مدل‌های جدید اضافه شد: Imagen 4.0 پایدار، DeepSeek-V3.1، و مدل‌های FLUX

**تاریخ:** ۱۴۰۴-۰۶-۰۳ / (2025-08-24)

## خلاصه

ما با افتخار اعلام می‌کنیم که به‌روزرسانی‌های مهم مدل‌ها شامل نسخه‌های پایدار سری Google Imagen 4.0، DeepSeek-V3.1 با قابلیت‌های استدلال پیشرفته، و مدل‌های جدید Black Forest Labs از Azure AI را ارائه می‌دهیم. این افزوده‌ها پایداری بهبود یافته، استدلال پیشرفته، و قابلیت‌های پیشرفته تولید و ویرایش تصویر را فراهم می‌کنند.

---

## جزئیات

### Google Imagen 4.0 - نسخه‌های پایدار اکنون در دسترس

نسخه‌های پایدار سری Google Imagen 4.0 اکنون در دسترس هستند و نسخه‌های پیش‌نمایش قبلی را با قابلیت اطمینان و عملکرد بهبود یافته جایگزین می‌کنند:

- **imagen-4.0-generate-001**: تولید تصویر با کیفیت بالا با پایداری و ثبات بهبود یافته. از رزولوشن‌های تا 2048x2048 و نسبت‌های ابعاد متعدد پشتیبانی می‌کند. [مستندات](fa/models/imagen-4.0-generate-001.md)
- **imagen-4.0-fast-generate-001**: بهینه‌سازی شده برای سرعت با حفظ کیفیت، مناسب برای برنامه‌هایی که نیاز به تولید سریع تصویر دارند. [مستندات](fa/models/imagen-4.0-fast-generate-001.md)
- **imagen-4.0-ultra-generate-001**: تولید تصویر با کیفیت فوق‌العاده بالا با جزئیات استثنایی و واقع‌گرایی. از بالاترین رزولوشن خروجی تا 2816x1536 پشتیبانی می‌کند. [مستندات](fa/models/imagen-4.0-ultra-generate-001.md)

#### ویژگی‌های کلیدی مدل‌های پایدار Imagen 4.0:
- واترمارک دیجیتال و تایید
- تنظیمات امنیتی قابل تنظیم توسط کاربر
- بهبود پرامپت با استفاده از بازنویسی پرامپت
- قابلیت‌های تولید شخص
- نسبت‌های ابعاد متعدد و پشتیبانی از رزولوشن بالا

### DeepSeek-V3.1 - قابلیت‌های استدلال و عامل بهبود یافته

ما پشتیبانی از DeepSeek-V3.1، جدیدترین مدل DeepSeek.com، را آغاز کرده‌ایم. این مدل بهبودهای قابل توجهی در قابلیت‌های استدلال و عاملیت دارد. نام‌های قبلی مدل، یعنی `deepseek-chat` و `deepseek-reasoner`، از این پس به طور خودکار به DeepSeek-V3.1 منتقل می‌شوند.

- **deepseek-chat**: حالت غیرتفکری DeepSeek-V3.1 برای پاسخ‌های سریع و کارآمد
- **deepseek-reasoner**: حالت تفکری DeepSeek-V3.1 با قابلیت‌های استدلال پیشرفته

#### بهبودهای DeepSeek-V3.1:
- **استنتاج ترکیبی**: حالت‌های تفکری و غیرتفکری در یک مدل
- **تفکر سریع‌تر**: سریع‌تر به پاسخ‌ها می‌رسد نسبت به نسخه‌های قبلی
- **مهارت‌های عامل قوی‌تر**: استفاده بهبود یافته از ابزار و وظایف عامل چندمرحله‌ای
- **زمینه 128K**: پنجره زمینه گسترده برای هر دو حالت
- **عملکرد بهتر**: نتایج بهبود یافته در SWE-bench و Terminal-Bench
- **استدلال کارآمد**: بهبودهای قابل توجه در کارایی تفکر

**نکته مهم**: فقط `deepseek-chat` و `deepseek-reasoner` به DeepSeek-V3.1 جدید هدایت می‌شوند. سایر نام‌های مدل مانند `deepseek-r1-0528` و `deepseek-v3-0324` از ارائه‌دهندگان مختلف (Azure و AWS Bedrock) استفاده می‌کنند و به DeepSeek-V3.1 نگاشت نمی‌شوند.

### مدل‌های BFL FLUX - تولید و ویرایش تصویر پیشرفته

مدل‌های جدید Black Forest Labs از Azure AI اکنون در دسترس هستند و قابلیت‌های پیشرفته تولید و ویرایش تصویر ارائه می‌دهند:

- **flux-1.1-pro**: مدل تولید تصویر پیشرفته که از نقطه پایانی `v1/images/generations` پشتیبانی می‌کند با عملکرد برتر در کیفیت تصویر، پیروی از پرامپت، و سرعت تولید. [مستندات](fa/models/flux-1.1-pro.md)
- **flux.1-kontext-pro**: مدل همه‌کاره که از هر دو نقطه پایانی `v1/images/generations` و `v1/images/edits` پشتیبانی می‌کند، در وظایف ویرایش متن و حفظ شخصیت عالی است. [مستندات](fa/models/flux.1-kontext-pro.md)

#### ویژگی‌های کلیدی مدل‌های Flux:
- **عملکرد بالا**: رتبه‌بندی برتر در معیارهای کیفیت تصویر و پیروی از پرامپت
- **تولید سریع**: تاخیرهای پایین‌تر به طور مداوم نسبت به مدل‌های رقیب
- **ویرایش همه‌کاره**: ویرایش متن پیشرفته و حفظ شخصیت (flux.1-kontext-pro)
- **نقاط پایانی متعدد**: پشتیبانی از گردش‌های کاری تولید و ویرایش

### نمونه‌های استفاده

#### مدل‌های Google Imagen 4.0

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="imagen-4.0-generate-001",
    prompt="منظره آرام کوهستانی با دریاچه‌ای شفاف که قله‌ها را در ساعت طلایی منعکس می‌کند",
    size="1024x1024",
    n=1,
    response_format="url",
)

print(response.data[0].url)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
 model: "imagen-4.0-generate-001",
 prompt: "منظره آرام کوهستانی با دریاچه‌ای شفاف که قله‌ها را در ساعت طلایی منعکس می‌کند",
 size: "1024x1024",
 n: 1,
 response_format: "url", // or b64_json
});

console.log(response.data[0].url);

bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "imagen-4.0-generate-001",
 "prompt": "منظره آرام کوهستانی با دریاچه‌ای شفاف که قله‌ها را در ساعت طلایی منعکس می‌کند",
 "size": "1024x1024",
 "n": 1,
 "response_format": "url"
 }'

```

#### مدل‌های DeepSeek-V3.1

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# استفاده از deepseek-chat (حالت غیرتفکری)
response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {
            "role": "user",
            "content": "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
        }
    ],
)

print(response.choices[0].message.content)

# استفاده از deepseek-reasoner (حالت تفکری)
reasoning_response = client.chat.completions.create(
    model="deepseek-reasoner",
    messages=[
        {
            "role": "user",
            "content": "این مسئله ریاضی پیچیده را حل کنید: اگر قطاری 120 مایل را در 2 ساعت طی کند، سپس سرعت خود را 25% افزایش دهد برای 3 ساعت بعدی، در مجموع چه مسافتی طی کرده است؟",
        }
    ],
)

print(reasoning_response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// استفاده از deepseek-chat (حالت غیرتفکری)
const response = await client.chat.completions.create({
 model: "deepseek-chat",
 messages: [
 {
 role: "user",
 content: "مفهوم درهم‌تنیدگی کوانتومی را به زبان ساده توضیح دهید",
 },
 ],
});

console.log(response.choices[0].message.content);

// استفاده از deepseek-reasoner (حالت تفکری)
const reasoningResponse = await client.chat.completions.create({
 model: "deepseek-reasoner",
 messages: [
 {
 role: "user",
 content: "این مسئله ریاضی پیچیده را حل کنید: اگر قطاری 120 مایل را در 2 ساعت طی کند، سپس سرعت خود را 25% افزایش دهد برای 3 ساعت بعدی، در مجموع چه مسافتی طی کرده است؟",
 },
 ],
});

console.log(reasoningResponse.choices[0].message.content);

```

#### مدل‌های BFL (FLUX) - تولید تصویر

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.generate(
    model="flux-1.1-pro",
    prompt="منظره شهری آینده‌نگرانه در غروب آفتاب با ماشین‌های پرنده و چراغ‌های نئون",
    size="1024x1024",
    n=1,
    response_format="b64_json",  # از 'url' پشتیبانی نمی کند
)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.generate({
 model: "flux-1.1-pro",
 prompt: "منظره شهری آینده‌نگرانه در غروب آفتاب با ماشین‌های پرنده و چراغ‌های نئون",
 size: "1024x1024",
 n: 1,
 response_format: "b64_json", // از 'url' پشتیبانی نمی کند
});

bash=:curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "flux-1.1-pro",
 "prompt": "منظره شهری آینده‌نگرانه در غروب آفتاب با ماشین‌های پرنده و چراغ‌های نئون",
 "size": "1024x1024",
 "n": 1,
 "response_format": "url"
 }'

```

#### مدل‌های BFL (FLUX) - ویرایش تصویر

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.images.edit(
    model="flux.1-kontext-pro",
    image=open("original_image.png", "rb"),
    prompt="متن روی تابلو را به 'خوش آمدید به AvalAI' تغییر دهید",
    size="1024x1024",
    n=1,
    response_format="b64_json",  # از 'url' پشتیبانی نمی کند
)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

const response = await client.images.edit({
 model: "flux.1-kontext-pro",
 image: fs.createReadStream("original_image.png"),
 prompt: "متن روی تابلو را به 'خوش آمدید به AvalAI' تغییر دهید",
 size: "1024x1024",
 n: 1,
 response_format: "b64_json", // از 'url' پشتیبانی نمی کند
});

bash=:curl https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F image="@original_image.png" \
  -F model="flux.1-kontext-pro" \
  -F prompt="متن روی تابلو را به 'خوش آمدید به AvalAI' تغییر دهید" \
  -F size="1024x1024" \
  -F n=1

```

### اطلاعات قیمت‌گذاری

مدل‌های جدید با قیمت‌گذاری رقابتی در دسترس هستند:

- **imagen-4.0-generate-001**: $0.04 در هر تصویر
- **imagen-4.0-fast-generate-001**: $0.02 در هر تصویر
- **imagen-4.0-ultra-generate-001**: $0.06 در هر تصویر
- **flux-1.1-pro**: $0.04 در هر تصویر
- **flux.1-kontext-pro**: $0.04 در هر تصویر
- **مدل‌های DeepSeek-V3.1**:
  - **deepseek-chat**: $0.07 / 1M tokens (cache hit), $0.27 / 1M tokens (cache miss), $1.10 / 1M tokens (output)
  - **deepseek-reasoner**: $0.14 / 1M tokens (cache hit), $0.55 / 1M tokens (cache miss), $2.19 / 1M tokens (output)
 - *مرجع قیمت‌گذاری: [قیمت‌گذاری API دیپ‌سیک](https://api-docs.deepseek.com/quick_start/pricing/)*

---

## لینک‌های مرتبط

- [مستندات مدل‌های Google Imagen](fa/providers/google.md?id=مدلهای-google-imagen-40)
- [مستندات مدل‌های DeepSeek](fa/providers/deepseek.md)
- [مستندات مدل‌های BFL (FLUX)](fa/providers/bfl.md)
- [راهنمای تولید تصویر](fa/guides/image-generation.md)
- [مرجع API تکمیل گفتگو](fa/api-reference/chat.md)
- [مرجع API تصاویر](fa/api-reference/images.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/guides/rate-limits.md)