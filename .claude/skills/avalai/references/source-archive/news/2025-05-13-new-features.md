# افزودن مدل جدید Alibaba Qwen3، ابزار جستجوی وب و نقطه پایانی Rerank به AvalAI

**تاریخ:** 1404-02-24 (2025-05-13)

## خلاصه

AvalAI سه قابلیت جدید و مهم را که از امروز، ۲۴ اردیبهشت ۱۴۰۴ (۱۳ می ۲۰۲۵) در دسترس هستند، اعلام می‌کند: مدل قدرتمند `Alibaba Qwen3-235B-A22B-FP8-TPUT`، ابزار `web_search_preview` برای مدل‌های OpenAI، و نقطه پایانی جدید `v1/rerank` با مدل `cohere.rerank-v3-5:0`. این بهبودها قابلیت‌های شما را در هوش مصنوعی پیشرفته، دسترسی به اطلاعات در لحظه و بهینه‌سازی نتایج جستجو گسترش می‌دهند.

---

## جزئیات

### مدل Alibaba Qwen3-235B-A22B-FP8-TPUT

مدل پرچمدار خانواده Qwen3 علی‌بابا، [`qwen3-235b-a22b-fp8-tput`](/fa/models/qwen3-235b-a22b-fp8-tput.md)، به AvalAI اضافه شده است. این مدل با ۲۳۵ میلیارد پارامتر، رویکردی 'هیبریدی' دارد که هم برای پاسخ‌های سریع و هم برای استدلال عمیق در وظایف پیچیده مناسب است.

**قابلیت‌های فنی کلیدی:**

- **معماری Mixture of Experts (MoE):** برای پردازش کارآمد.
- **پشتیبانی از زبان:** درک و تولید محتوا به 119 زبان.
- **آموزش گسترده:** آموزش دیده بر روی مجموعه داده متنوعی با بیش از 36 تریلیون توکن.
- **ویژگی‌های پیشرفته:** پشتیبانی از فراخوانی تابع، فراخوانی تابع موازی و اسکیمای پاسخ.

این مدل برای ارائه توان عملیاتی بالا و عملکرد رقابتی در وظایف کدنویسی، ریاضی و استدلال عمومی طراحی شده است.

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

completion = client.chat.completions.create(
    model="qwen3-235b-a22b-fp8-tput",
    messages=[
        {
            "role": "user",
            "content": "مفهوم Mixture of Experts را در مدل‌های زبان بزرگ توضیح دهید.",
        }
    ],
)
print(completion.choices[0].message.content)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function main() {
  const completion = await client.chat.completions.create({
    model: "qwen3-235b-a22b-fp8-tput",
    messages: [
      {
        role: "user",
        content: "مفهوم Mixture of Experts را در مدل‌های زبان بزرگ توضیح دهید.",
      },
    ],
  });
  console.log(completion.choices[0].message.content);
}

main();

```

### ابزار جستجوی وب برای مدل‌های OpenAI

تعاملات با مدل‌های OpenAI خود را با ابزار [`web_search_preview`](/fa/guides/tools-web-search.md) که اکنون از طریق نقطه پایانی [`v1/responses`](/fa/api-reference/responses.md) در دسترس است، بهبود بخشید. این ابزار به مدل‌ها امکان می‌دهد تا به آخرین اطلاعات از وب دسترسی پیدا کرده و از آن‌ها در پاسخ‌های خود استفاده کنند.

**قابلیت‌های فنی کلیدی:**

- **اطلاعات در لحظه:** به مدل‌ها اجازه می‌دهد اطلاعات به‌روز را دریافت کنند.
- **سفارشی‌سازی موقعیت مکانی کاربر:** نتایج جستجو را بر اساس جغرافیا (کشور، شهر، منطقه، منطقه زمانی) دقیق‌تر کنید.
- **کنترل اندازه زمینه جستجو:** مقدار زمینه وب بازیابی شده (`high`, `medium`, `low`) را برای تعادل هزینه، کیفیت و تاخیر مدیریت کنید.
- **پاسخ‌های مستند:** خروجی شامل استنادات درون‌خطی و اطلاعات حاشیه‌نویسی (`url_citation`) با URL، عنوان و مکان منابع است.

برای استفاده از آن، `{ "type": "web_search" }` را در آرایه `tools` درخواست API خود قرار دهید.

```language-selector
python=:from openai import OpenAI

client = OpenAI(api_key="YOUR_AVALAI_API_KEY", base_url="https://api.avalai.ir/v1")

response = client.responses.create(
    model="gpt-4o",  # مثال مدل OpenAI
    tools=[{"type": "web_search"}],
    input="آخرین تحولات در اخلاق هوش مصنوعی تا به امروز چیست؟",
)
print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function main() {
  const response = await client.responses.create({
    model: "gpt-4o", // مثال مدل OpenAI
    tools: [{ type: "web_search" }],
    input: "آخرین تحولات در اخلاق هوش مصنوعی تا به امروز چیست؟",
  });
  console.log(response.output_text);
}

main();

```

### نقطه پایانی جدید `v1/rerank` با Cohere

ما همچنین نقطه پایانی `v1/rerank` را معرفی می‌کنیم که در ابتدا از مدل `cohere.rerank-v3-5:0` پشتیبانی می‌کند. این نقطه پایانی به شما امکان می‌دهد برای بهبود ارتباط نتایج جستجو یا لیست اسناد با یک پرس‌وجو، آن‌ها را مجددا مرتب کنید.

**قابلیت‌های فنی کلیدی:**

- **بهبود ارتباط:** لیستی از اسناد را بر اساس ارتباط آن‌ها با یک پرس‌وجوی معین مجددا مرتب می‌کند.
- **درک معنایی:** از درک زبان پیشرفته Cohere برای رتبه‌بندی مجدد دقیق استفاده می‌کند.

این ویژگی به ویژه برای برنامه‌هایی که به نتایج جستجوی بسیار مرتبط از مجموعه بزرگی از اسناد نیاز دارند، مفید است.

```language-selector
python=:import requests
import json

API_KEY = "YOUR_AVALAI_API_KEY"
AVALAI_BASE_URL = "https://api.avalai.ir/v1"

headers = {"Authorization": f"Bearer {API_KEY}", "Content-Type": "application/json"}

data = {
    "model": "cohere.rerank-v3-5:0",
    "query": "مزایای انرژی‌های تجدیدپذیر چیست؟",
    "documents": [
        "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
        "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
        "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
        "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
    ],
}

response = requests.post(f"{AVALAI_BASE_URL}/rerank", headers=headers, json=data)

if response.status_code == 200:
    reranked_documents = response.json().get("results")
    for doc in reranked_documents:
        print(
            f"ایندکس: {doc['index']}، امتیاز ارتباط: {doc['relevance_score']}، سند: {doc['document']['text']}"
        )
else:
    print(f"خطا: {response.status_code} - {response.text}")

javascript=:const fetch = require("node-fetch"); // یا از fetch مرورگر استفاده کنید

const API_KEY = process.env.AVALAI_API_KEY;
const AVALAI_BASE_URL = "https://api.avalai.ir/v1";

async function rerankDocuments() {
  const data = {
    model: "cohere.rerank-v3-5:0",
    query: "مزایای انرژی‌های تجدیدپذیر چیست؟",
    documents: [
      "منابع انرژی تجدیدپذیر مانند خورشید و باد برای مقابله با تغییرات آب و هوایی بسیار مهم هستند.",
      "سوخت‌های فسیلی سنتی اثرات زیست‌محیطی قابل توجهی دارند.",
      "سرمایه‌گذاری در فناوری سبز می‌تواند منجر به رشد اقتصادی و ایجاد شغل شود.",
      "پنل‌های خورشیدی نور خورشید را به برق تبدیل می‌کنند.",
    ],
  };

  try {
    const response = await fetch(`${AVALAI_BASE_URL}/rerank`, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${API_KEY}`,
        "Content-Type": "application/json",
      },
      body: JSON.stringify(data),
    });

    if (response.ok) {
      const responseData = await response.json();
      const rerankedDocuments = responseData.results;
      rerankedDocuments.forEach((doc) => {
        console.log(
          `ایندکس: ${doc.index}، امتیاز ارتباط: ${doc.relevance_score}، سند: ${doc.document.text}`,
        );
      });
    } else {
      console.error(`خطا: ${response.status} - ${await response.text()}`);
    }
  } catch (error) {
    console.error("درخواست ناموفق بود:", error);
  }
}

rerankDocuments();

```

---

## لینک‌های مرتبط

- [مستندات مدل Alibaba Qwen3-235B-A22B-FP8-TPUT](/fa/models/qwen3-235b-a22b-fp8-tput.md)
- [راهنمای ابزار جستجوی وب](/fa/guides/tools-web-search.md)
- [مستندات Cohere](/fa/providers/cohere.md)
- [مرجع API پاسخ‌ها](/fa/api-reference/responses.md)
