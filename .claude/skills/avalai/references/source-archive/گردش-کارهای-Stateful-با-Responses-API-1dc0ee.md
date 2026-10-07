# گردش‌کارهای Stateful با Responses API

Responses API زمانی کاربردی است که بخواهید API وضعیت گفتگو، ابزارهای میزبانی‌شده و ورودی‌های چندوجهی را بدون بازسازی کامل تاریخچه پیام‌ها در هر نوبت مدیریت کند. این مثال الگوهای عملی ادامه دادن گفتگو، شاخه‌سازی از پاسخ قبلی و بررسی پاسخ‌ها را از طریق AvalAI نشان می‌دهد.

> این راهنما با اقتباس از [OpenAI Cookbook رسمی](https://developers.openai.com/cookbook) و [دفترچه نمونه Responses API](https://github.com/openai/openai-cookbook/blob/main/examples/responses_api/responses_example.ipynb)، همراه با تغییرات لازم برای endpoint و کلید API در AvalAI تهیه شده است.

## چه زمانی از این الگو استفاده کنیم

- می‌خواهید بدون ارسال دوباره کل تاریخچه، گفتگو را ادامه دهید.
- لازم است از یک پاسخ قبلی شاخه جدیدی بسازید و مسیر دیگری را امتحان کنید.
- یک سطح API واحد برای تولید متن و ابزارهایی مانند جستجوی وب می‌خواهید.
- در حال مهاجرت از Chat Completions هستید و مدل ساده‌تری برای مدیریت state می‌خواهید.

## آماده‌سازی

SDK رسمی OpenAI را نصب و کلید AvalAI را تنظیم کنید:

```bash
pip install openai
export AVALAI_API_KEY="your-avalai-api-key"
```

برای Node.js:

```bash
npm install openai
export AVALAI_API_KEY="your-avalai-api-key"
```

## گفتگوی Stateful پایه

ابتدا یک response بسازید و سپس با `previous_response_id` آن را ادامه دهید.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

first = client.responses.create(
    model="gpt-5.6-luna",
    input="Give me a concise deployment checklist for a small API service.",
)

print(first.output_text)

follow_up = client.responses.create(
    model="gpt-5.6-luna",
    input="Now turn that checklist into five acceptance criteria.",
    previous_response_id=first.id,
)

print(follow_up.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const first = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "Give me a concise deployment checklist for a small API service.",
});

console.log(first.output_text);

const followUp = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "Now turn that checklist into five acceptance criteria.",
  previous_response_id: first.id,
});

console.log(followUp.output_text);

bash=:FIRST_RESPONSE=$(curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "Give me a concise deployment checklist for a small API service."
  }')

FIRST_ID=$(printf "%s" "$FIRST_RESPONSE" | jq -r ".id")

curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"gpt-5.5\",
    \"input\": \"Now turn that checklist into five acceptance criteria.\",
    \"previous_response_id\": \"$FIRST_ID\"
  }"

```

## تصمیم‌های State، نگه‌داری و هزینه

`previous_response_id` ساده‌ترین راه برای ادامه دادن یک thread است، اما همچنان به state سمت سرویس تکیه دارد. انتخاب state را صریح کنید:

- وقتی می‌خواهید AvalAI از یک response ذخیره‌شده سمت سرور ادامه دهد، از `previous_response_id` استفاده کنید.
- وقتی کنترل دقیق retention، replay قطعی یا fallback برای مسیرهایی لازم است که response قبلی را resolve نمی‌کنند، تاریخچه را دستی نگه دارید.
- برای CI، eval یا دیباگ حساس، مگر اینکه retrieval بعدی لازم دارید، `store=false` بگذارید.
- اگر continuation به دلیل resolve نشدن response قبلی شکست خورد، درخواست را با context کامل و بدون `previous_response_id` دوباره ارسال کنید.
- برای کل زنجیره بودجه بگذارید: input قبلی در thread همچنان می‌تواند به‌عنوان input token حساب شود و مدل‌های reasoning نیز reasoning token را داخل context window مصرف می‌کنند.

```language-selector
python=:history = [{"role": "user", "content": "Draft a rollback checklist for a payment API."}]

first = client.responses.create(
    model="gpt-5.6-luna",
    input=history,
    store=False,
)

# فقط output_text را نگه ندارید؛ آیتم‌های ساختاریافته خروجی را حفظ کنید.
history.extend(first.output)
history.append(
    {"role": "user", "content": "Now make it safe for a junior on-call engineer."}
)

second = client.responses.create(
    model="gpt-5.6-luna",
    input=history,
    store=False,
)

print(second.output_text)

javascript=:const history = [
  { role: "user", content: "Draft a rollback checklist for a payment API." },
];

const first = await client.responses.create({
  model: "gpt-5.6-luna",
  input: history,
  store: false,
});

// فقط output_text را نگه ندارید؛ آیتم‌های ساختاریافته خروجی را حفظ کنید.
history.push(...first.output);
history.push({
  role: "user",
  content: "Now make it safe for a junior on-call engineer.",
});

const second = await client.responses.create({
  model: "gpt-5.6-luna",
  input: history,
  store: false,
});

console.log(second.output_text);

```

## شاخه‌سازی از یک پاسخ قبلی

شاخه‌سازی به شما اجازه می‌دهد از یک پاسخ قبلی مسیر جدیدی بسازید، بدون اینکه مسیر اصلی را تغییر دهید. این کار برای A/B تست پرامپت، تولید لحن‌های متفاوت یا تلاش دوباره با محدودیت جدید مفید است.

```language-selector
python=:forked = client.responses.create(
    model="gpt-5.6-luna",
    input=(
        "Use the same original checklist, but rewrite it for a solo developer "
        "who deploys manually once per week."
    ),
    previous_response_id=first.id,
)

print(forked.output_text)

javascript=:const forked = await client.responses.create({
  model: "gpt-5.6-luna",
  input:
    "Use the same original checklist, but rewrite it for a solo developer who deploys manually once per week.",
  previous_response_id: first.id,
});

console.log(forked.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d "{
    \"model\": \"gpt-5.5\",
    \"input\": \"Use the same original checklist, but rewrite it for a solo developer who deploys manually once per week.\",
    \"previous_response_id\": \"$FIRST_ID\"
  }"

```

## دریافت دوباره یک Response ذخیره‌شده

برای لاگ‌گیری، دیباگ یا پردازش با تاخیر بعد از یک گردش‌کار پس‌زمینه، می‌توانید response را دوباره دریافت کنید. اگر retrieval بعدی لازم دارید، response را با `store=true` بسازید؛ در غیر این صورت `store=false` را ترجیح دهید و فقط فیلدهای مورد نیاز برنامه را نگه دارید.

```language-selector
python=:stored = client.responses.retrieve(first.id)

print(stored.id)
print(stored.output_text)

javascript=:const stored = await client.responses.retrieve(first.id);

console.log(stored.id);
console.log(stored.output_text);

bash=:curl "https://api.avalai.ir/v1/responses/$FIRST_ID" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

## افزودن جستجوی وب

وقتی پاسخ به اطلاعات تازه نیاز دارد، ابزار `web_search` را اضافه کنید. اگر رابط کاربری شما به لینک منبع نیاز دارد، در پرامپت صریحا درخواست citation کنید.

```language-selector
python=:response = client.responses.create(
    model="gpt-5.6-luna",
    input="Find the latest AvalAI documentation updates and summarize them with sources.",
    tools=[{"type": "web_search"}],
)

print(response.output_text)

for item in response.output:
    print(item.type)

javascript=:const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input:
    "Find the latest AvalAI documentation updates and summarize them with sources.",
  tools: [{ type: "web_search" }],
});

console.log(response.output_text);

for (const item of response.output) {
  console.log(item.type);
}

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "Find the latest AvalAI documentation updates and summarize them with sources.",
    "tools": [{"type": "web_search"}]
  }'

```

## نکات Production

- فقط وقتی response ID را ذخیره کنید که واقعا به ادامه دادن یا audit گفتگو نیاز دارید.
- اگر کنترل دقیق retention، deletion یا compliance لازم دارید، تاریخچه گفتگو را در سیستم خودتان نگه دارید.
- هنگام replay دستی state، آیتم‌های ساختاریافته `response.output` را append کنید تا tool callها و reasoning itemها حفظ شوند.
- برای گردش‌کارهای قابل پیش‌بینی، instructionهای ثابت را پایدار نگه دارید و جزئیات متغیر کاربر را در آخرین input قرار دهید.
- هنگام استفاده از ابزارها، `response.output` را بررسی کنید؛ `output_text` برای متن نهایی ساده است، اما tool callها و annotationها در آیتم‌های ساختاریافته خروجی قرار دارند.
- `response.id`، مدل، latency و `usage` را لاگ کنید تا بررسی هزینه و پشتیبانی ساده‌تر شود.

## لینک‌های مرتبط

- [مرجع Responses API](fa/api-reference/responses.md)
- [Responses در مقابل Chat Completions](fa/guides/responses-vs-chat-completions.md)
- [استفاده از ابزارهای داخلی](fa/guides/tools.md)
- [راهنمای جستجوی وب](fa/guides/tools-web-search.md)
