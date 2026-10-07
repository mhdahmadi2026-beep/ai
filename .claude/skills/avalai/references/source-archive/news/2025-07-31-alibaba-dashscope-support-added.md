# پشتیبانی کامل از مدل‌های Alibaba از طریق DashScope در دسترس است

**تاریخ:** 1404-05-09 / (2025-07-31)

## خلاصه

اکنون در AvalAI، دسترسی کامل و بومی به کل اکوسیستم مدل‌های Qwen شرکت Alibaba از طریق پلتفرم رسمی ابری DashScope فراهم شده است. این یکپارچگی، دسترسی مستقیم توسعه‌دهندگان به مدل‌های پیشرفته هوش مصنوعی Alibaba را با حفظ سادگی API ما میسر می‌سازد.

---

## جزئیات

دسترسی کامل و بومی به کل اکوسیستم مدل‌های Qwen شرکت Alibaba را از طریق پلتفرم رسمی ابری [DashScope](https://dashscope.console.aliyun.com/) آن‌ها هم اکنون در AvalAI ممکن است. این یکپارچگی به توسعه‌دهندگان دسترسی مستقیم به پیشرفته‌ترین مدل‌های هوش مصنوعی Alibaba را می‌دهد در حالی که سادگی API یکپارچه ما را حفظ می‌کند.

### پوشش کامل خانواده مدل‌ها

این انتشار شامل پشتیبانی جامع از همه خانواده‌های اصلی مدل‌های Qwen است:

#### سری Qwen Turbo
مدل‌های با کارایی بالا که برای سرعت و بهره‌وری بهینه‌سازی شده‌اند:
- **qwen-turbo**: آخرین مدل turbo با پنجره زمینه 131K
- **qwen-turbo-latest**: نسخه همیشه به‌روز مدل turbo
- **qwen-turbo-2025-04-28**: نسخه تاریخ‌دار مشخص برای سازگاری

#### سری Qwen Plus
مدل‌های متعادل که عملکرد عالی در وظایف متنوع ارائه می‌دهند:
- **qwen-plus**: مدل پیشرفته عمومی با زمینه 131K
- **qwen-plus-latest**: جدیدترین نسخه مدل plus
- **qwen-plus-2025-07-14**: آخرین انتشار پایدار
- **qwen-plus-2025-04-28**: نسخه پایدار قبلی

#### سری Qwen Max
مدل‌های پریمیوم برای پرتقاضاترین کاربردها:
- **qwen-max**: مدل سطح بالا با قابلیت‌های استدلال پیشرفته
- **qwen-max-latest**: مدل پرچمدار فعلی
- **qwen-max-2025-01-25**: نسخه پایدار تولید

#### مدل‌های بینایی-زبانی
مدل‌های چندوجهی برای درک متن و تصویر:
- **سری Qwen 2.5 VL**: qwen2.5-vl-72b-instruct، qwen2.5-vl-32b-instruct، qwen2.5-vl-7b-instruct، qwen2.5-vl-3b-instruct
- **سری Qwen VL**: qwen-vl-max، qwen-vl-plus، qwen-vl-ocr برای وظایف بینایی تخصصی

#### سری QVQ Max
مدل‌های استدلال پیشرفته با قابلیت‌های پاسخ به سوالات بصری:
- **qvq-max**: مدل استدلال پیشرفته
- **qvq-max-latest**: جدیدترین مدل استدلال
- **qvq-max-2025-03-25**: نسخه پایدار استدلال

#### سری Qwen 3
مدل‌های نسل بعدی با قابلیت‌های بهبود یافته:
- **مدل‌های استاندارد**: qwen3-32b، qwen3-14b، qwen3-8b، qwen3-4b، qwen3-1.7b، qwen3-0.6b
- **مدل‌های A3B**: qwen3-30b-a3b با انواع thinking و instruct
- **مدل‌های A22B**: qwen3-235b-a22b با قابلیت‌های استدلال تخصصی

#### مدل‌های تخصصی
مدل‌های ساخته‌شده برای موارد استفاده خاص:
- **QWQ Plus**: مدل‌های استدلال پیشرفته (qwq-plus، qwq-plus-2025-03-05)
- **سری MT**: مدل‌های ترجمه ماشینی (qwen-mt-plus، qwen-mt-turbo)
- **سری Coder**: مدل‌های متمرکز بر برنامه‌نویسی (qwen3-coder-480b-a35b-instruct، qwen3-coder-plus)
- **زمینه طولانی**: مدل‌های زمینه توسعه‌یافته مانند qwen2.5-7b-instruct-1m و qwen2.5-14b-instruct-1m

### یکپارچگی API

همه مدل‌های Alibaba اکنون از طریق نقاط پایانی استاندارد ما قابل دسترسی هستند:

**پشتیبانی اصلی**: نقطه پایانی `v1/chat/completions` با پشتیبانی کامل از ویژگی‌ها
**پشتیبانی محدود**: نقطه پایانی `v1/messages` برای تعاملات پایه

### مثال‌های استفاده

```language-selector
python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",
)

# استفاده از Qwen Plus برای وظایف عمومی
response = client.chat.completions.create(
    model="qwen-plus",
    messages=[
        {"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح دهید."}
    ],
    max_tokens=500,
)

print(response.choices[0].message.content)

# استفاده از Qwen VL برای وظایف بینایی
response = client.chat.completions.create(
    model="qwen2.5-vl-72b-instruct",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "آنچه در این تصویر می‌بینید را توصیف کنید."},
                {
                    "type": "image_url",
                    "image_url": {
                        "url": "https://dashscope.oss-cn-beijing.aliyuncs.com/images/256_1.png"
                    },
                },
            ],
        }
    ],
)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir/v1",
});

// استفاده از Qwen Max برای استدلال پیچیده
const response = await client.chat.completions.create({
 model: "qwen-max",
 messages: [
 {
 role: "user",
 content: "این پازل منطقی را حل کنید: اگر همه گل‌های رز، گل هستند و برخی گل‌ها قرمز هستند، آیا می‌توانیم نتیجه بگیریم که برخی گل‌های رز قرمز هستند؟"
 }
 ],
 max_tokens: 300
});

console.log(response.choices[0].message.content);

// استفاده از Qwen Coder برای وظایف برنامه‌نویسی
const codeResponse = await client.chat.completions.create({
 model: "qwen3-coder-plus",
 messages: [
 {
 role: "user",
 content: "یک تابع Python برای محاسبه اعداد فیبوناچی با استفاده از برنامه‌نویسی پویا بنویسید."
 }
 ]
});

```

### ویژگی‌های کلیدی

- **یکپارچگی بومی**: دسترسی مستقیم به زیرساخت رسمی DashScope شرکت Alibaba
- **پوشش جامع**: بیش از 40 مدل در همه موارد استفاده اصلی
- **API یکپارچه**: دسترسی به همه مدل‌ها از طریق نقاط پایانی سازگار با OpenAI
- **قابلیت‌های پیشرفته**: پشتیبانی از ورودی‌های چندوجهی، زمینه‌های طولانی و وظایف تخصصی
- **آماده تولید**: قابلیت اطمینان سطح سازمانی از طریق زیرساخت رسمی Alibaba Cloud

### مشخصات مدل‌ها

همه مدل‌ها شامل مشخصات دقیق برای پنجره‌های زمینه، محدودیت‌های توکن و قابلیت‌ها هستند. برای اطلاعات کامل قیمت‌گذاری، لطفا به مستندات [جزئیات مدل‌ها](fa/models/model-details.md) مراجعه کنید.

---

## لینک‌های مرتبط

- [مستندات مدل‌های Alibaba](fa/providers/alibaba.md)
- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [مرجع API پیام‌ها](fa/api-reference/messages.md)
- [جزئیات مدل‌ها و قیمت‌گذاری](fa/models/model-details.md)
- [کنسول رسمی DashScope](https://dashscope.console.aliyun.com/)