# وضعیت مکالمه با Responses API

Responses API می‌تواند با `previous_response_id` وضعیت کوتاه‌مدت یک گردش‌کار را از یک پاسخ به پاسخ بعدی وصل کند. از این قابلیت زمانی استفاده کنید که مدل باید مکالمه را ادامه دهد، نتیجه ابزارهای قبلی را ببیند، یا بدون ارسال دوباره کل تاریخچه از یک پاسخ قبلی شاخه جدید بسازد.

> این راهنما با اقتباس از مستندات رسمی OpenAI درباره [وضعیت مکالمه](https://developers.openai.com/api/docs/guides/conversation-state)، [OpenAI Cookbook](https://developers.openai.com/cookbook/) و [openai/openai-cookbook](https://github.com/openai/openai-cookbook)، با تغییرات endpoint، کلید API و مدل‌های AvalAI تهیه شده است.

## چه زمانی از وضعیت مدیریت‌شده توسط API استفاده کنیم

از `previous_response_id` استفاده کنید وقتی:

- کاربر همان کار را در چند نوبت ادامه می‌دهد
- نمی‌خواهید در هر درخواست کل پیام‌ها را دوباره بسازید
- یک گردش‌کار reasoning یا tool باید آیتم‌های پاسخ قبلی را ببیند
- می‌خواهید از یک پاسخ مشخص شاخه بزنید و چند مسیر بعدی را مقایسه کنید

پایگاه داده برنامه شما همچنان منبع اصلی هویت کاربر، مجوزها، حافظه بلندمدت، رکوردهای کسب‌وکار و audit log است. وضعیت مدیریت‌شده توسط API فقط برای context مدل است و جایگزین state برنامه نمی‌شود.

برای اطلاعات منتخبی که باید میان جلسه‌های مستقل باقی بمانند، یک لایه متعلق به برنامه مانند [حافظه پایدار عامل با Embeddings](fa/examples/durable_agent_memory.md) بسازید؛ زنجیره پاسخ مدیریت‌شده توسط API را حافظه بلندمدت در نظر نگیرید.

## انتخاب استراتژی وضعیت

| استراتژی | زمان استفاده | ملاحظه |
|----------|--------------|---------|
| `previous_response_id` | وقتی می‌خواهید API نوبت‌ها را به هم وصل کند و context اخیر reasoning یا ابزار را نگه دارد | ساده‌ترین روش پیاده‌سازی است، اما `instructions` مهم را در هر نوبت دوباره بفرستید؛ context قبلی همچنان می‌تواند در مصرف ورودی حساب شود |
| ارسال دستی آیتم‌ها | وقتی کنترل stateless، کوتاه‌سازی سفارشی یا auditability سخت‌گیرانه نیاز دارید | کد بیشتری می‌خواهد، اما دقیقا تصمیم می‌گیرید کدام آیتم‌های `response.output` در `input` بعدی برگردند |
| شیء مکالمه پایدار | وقتی route شما صریحا پارامتر OpenAI-style `conversation` یا Conversations API را پشتیبانی می‌کند | برای threadهای سروری durable مفید است، اما availability به account و route وابسته است؛ آن را همزمان با `previous_response_id` نفرستید |
| فشرده‌سازی context | وقتی workflow چندین نوبت ادامه دارد یا خروجی ابزارها طولانی است | فقط وقتی route پشتیبانی می‌کند از compaction سمت سرور یا مستقل استفاده کنید، آیتم‌های compaction برگشتی را حفظ کنید، یا خودتان facts پایدار، شناسه‌ها، نتایج ابزار، فرض‌ها، blockerها و اقدام بعدی را خلاصه کنید |

برای workflowهای حساس به compliance یا کمینه‌سازی داده، ارسال دستی آیتم‌ها همراه با `store=False` را ترجیح دهید. اگر context استدلال باید بدون state ذخیره‌شده ادامه پیدا کند، به جای تکیه بر کل transcript، آیتم‌های خروجی لازم برای نوبت بعد را حفظ کنید.

`previous_response_id` مدیریت context است، نه حافظه رایگان. درخواست‌های زنجیره‌ای را طوری budget کنید که انگار ورودی‌های قبلی مرتبط هنوز بخشی از context مدل هستند؛ اگر thread بزرگ شد، آن را فشرده کنید یا فقط آیتم‌های لازم را دوباره ارسال کنید.

وقتی به `previous_response_id` تکیه می‌کنید، قصد استفاده از state ذخیره‌شده را با `store=True`/`store: true` روی پاسخ‌هایی که قرار است ادامه پیدا کنند صریح کنید. وقتی `store=False` می‌گذارید، الگوی ارسال دستی پایین را ترجیح دهید و آیتم‌های لازم از `response.output` را خودتان حمل کنید.

وقتی route پشتیبانی‌شده یک آیتم compaction برمی‌گرداند، با آن مثل state opaque رفتار کنید: آن را ویرایش نکنید، روی خودش خلاصه‌سازی نکنید و به کاربر نمایش ندهید. برای `/v1/responses/compact` مستقل، پنجره compact‌شده برگشتی را همان‌طور که هست به فراخوانی بعدی `/v1/responses` بدهید.

## نکات ذخیره‌سازی، نگه‌داری و هزینه

در جریان native مربوط به Responses در OpenAI، آبجکت‌های response به صورت پیش‌فرض ذخیره می‌شوند، برای Response objectها در حال حاضر پنجره نگه‌داری پیش‌فرض ۳۰ روزه مستند شده است، و تا وقتی `store=False` نگذارید می‌توان آن‌ها را بعدا retrieve کرد. شیءهای conversation و itemهای آن‌ها در رفتار مرجع OpenAI خارج از این TTL مخصوص Response object هستند. AvalAI همین شکل درخواست سازگار با OpenAI را در routeهای پشتیبانی‌شده دنبال می‌کند، اما زمان نگه‌داری، رفتار zero-retention و دسترسی به Conversations API می‌تواند به route، provider و تنظیمات حساب وابسته باشد. در سیستم‌های production، شناسه response در AvalAI، شناسه داخلی درخواست، مدل، context کاربر/tenant و مصرف token را در پایگاه داده خودتان ثبت کنید و hosted state را تنها audit trail ندانید.

حتی وقتی `previous_response_id` مدیریت transcript را از کد شما پنهان می‌کند، context قبلی مرتبط همچنان از بودجه ورودی مصرف می‌کند. اگر زنجیره بزرگ شد، facts پایدار و نتایج ابزارها را در یک state فشرده خلاصه کنید و سپس با ارسال دستی آیتم‌ها یا یک response chain تازه ادامه دهید.

context window را یک بودجه مشترک برای ورودی، خروجی تولیدشده و—در مدل‌های reasoning—توکن‌های reasoning بدانید. محدودیت توکن خروجی را طوری تنظیم کنید که برای پاسخ جا بماند، و پیش از اینکه workflow در حال رشد فضای پاسخ بعدی مدل را کم کند، نوبت‌های قدیمی را compact یا trim کنید.

اگر route انتخابی AvalAI از [حالت WebSocket در Responses](fa/guides/websocket-mode.md) پشتیبانی کند، `previous_response_id` را همان مکانیزم منطقی ادامه دادن در HTTP بدانید. همیشه مسیر recovery با full context داشته باشید: رفتار مرجع WebSocket در OpenAI از state محلی اتصال برای تازه‌ترین پاسخ قبلی استفاده می‌کند؛ بنابراین اگر ID در cache نبود یا قابل resolve نشد، به جای فرض recovery خودکار server، یک نوبت جدید با context کامل ارسال کنید.

## ادامه دادن مکالمه

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

first = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a concise AvalAI onboarding assistant.",
    input="Create a short onboarding checklist for a new API user.",
    store=True,
)

follow_up = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a concise AvalAI onboarding assistant.",
    previous_response_id=first.id,
    input="Make it specific to a Python backend developer.",
    store=True,
)

print(follow_up.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const first = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a concise AvalAI onboarding assistant.",
  input: "Create a short onboarding checklist for a new API user.",
  store: true,
});

const followUp = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a concise AvalAI onboarding assistant.",
  previous_response_id: first.id,
  input: "Make it specific to a Python backend developer.",
  store: true,
});

console.log(followUp.output_text);

```

```bash
FIRST_ID=$(curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "You are a concise AvalAI onboarding assistant.",
    "input": "Create a short onboarding checklist for a new API user.",
    "store": true
  }' | jq -r '.id')

curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d "{
    \"model\": \"gpt-5.5\",
    \"instructions\": \"You are a concise AvalAI onboarding assistant.\",
    \"previous_response_id\": \"$FIRST_ID\",
    \"input\": \"Make it specific to a Python backend developer.\",
    \"store\": true
  }"

```


## شاخه زدن از یک پاسخ قبلی

استفاده دوباره از همان `previous_response_id` به شما اجازه می‌دهد چند نوبت بعدی را از یک state پایه مقایسه کنید.

```python
base = client.responses.create(
    model="gpt-5.6-luna",
    input="Draft a support reply for a user whose API request returned 429.",
    store=True,
)

technical = client.responses.create(
    model="gpt-5.6-luna",
    previous_response_id=base.id,
    input="Rewrite it for a senior backend engineer.",
    store=True,
)

nontechnical = client.responses.create(
    model="gpt-5.6-luna",
    previous_response_id=base.id,
    input="Rewrite it for a non-technical account owner.",
    store=True,
)
```

## بازیابی یک پاسخ ذخیره‌شده

اگر `store` فعال باشد، می‌توانید یک پاسخ را بعدا برای logging، debugging یا پردازش با تاخیر بازیابی کنید.

```python
response = client.responses.retrieve("resp_abc123")
print(response.output_text)
```

برای درخواست‌هایی که نباید بعدا نگهداری شوند، `store=False` را تنظیم کنید.

## انتقال دستی Context

وقتی از `previous_response_id` استفاده نمی‌کنید، آیتم‌های لازم از `response.output` قبلی را به `input` درخواست بعدی اضافه کنید. نوع آیتم‌هایی مثل `message`، `reasoning`، `function_call` و `function_call_output` را حفظ کنید؛ حذف آیتم‌های ابزار یا reasoning می‌تواند نوبت بعدی را کم‌اعتمادتر کند.

برای flowهای tool-heavy با مدل‌های GPT-5-style، هر مقدار assistant `phase` برگشتی در output itemها را هم حفظ کنید. به‌روزرسانی‌های میانی assistant ممکن است `phase: "commentary"` داشته باشند و پاسخ کامل ممکن است `phase: "final_answer"` داشته باشد؛ اگر خروجی assistant را دستی replay می‌کنید، این مقدارها را بدون تغییر عبور دهید تا preamble میانی مثل پاسخ نهایی تفسیر نشود.

برای مدل‌های reasoning در flowهای stateless یا شبیه zero-retention، اگر route انتخابی AvalAI پشتیبانی می‌کند، آیتم‌های reasoning رمزنگاری‌شده را درخواست کنید: `include=["reasoning.encrypted_content"]`. سپس آیتم‌های خروجی برگشتی را در درخواست بعدی replay کنید و متن reasoning را خودتان آشکار یا جعل نکنید.

```python
first = client.responses.create(
    model="gpt-5.6-luna",
    input="Extract the action items from this support note: ...",
    store=False,
    include=["reasoning.encrypted_content"],  # اگر route پشتیبانی نمی‌کند حذف کنید
)

next_input = [
    *first.output,
    {
        "role": "user",
        "content": "Now turn those action items into a customer-safe reply.",
    },
]

second = client.responses.create(
    model="gpt-5.6-luna",
    input=next_input,
    store=False,
    include=["reasoning.encrypted_content"],
)
```

## بهترین شیوه‌ها

- شناسه response را در پایگاه داده خودتان کنار user، task و permission context ذخیره کنید.
- اگر `instructions` مهم هستند، در هر نوبت آن‌ها را صریح بنویسید؛ top-level instructions پاسخ قبلی به صورت خودکار به درخواست بعدی با `previous_response_id` منتقل نمی‌شود.
- `previous_response_id` را همزمان با شیء یا شناسه `conversation` نفرستید؛ برای هر درخواست فقط یکی از مکانیزم‌های state را انتخاب کنید.
- هنگام replay دستی خروجی assistant، فیلدهای `phase` برگشتی مانند `commentary` و `final_answer` را حفظ کنید و تاریخچه assistant را بازنویسی نکنید.
- از `metadata` برای شناسه‌های برنامه مثل `tenant_id`، `workflow_id` یا `request_id` استفاده کنید.
- برای عامل‌های طولانی‌مدت، [context قدیمی را فشرده کنید](fa/guides/compaction.md) و آن را به facts پایدار، پرسش‌های باز، اقدامات انجام‌شده و هدف بعدی تبدیل کنید.
- برای workflowهای هزینه و audit، به‌ویژه هنگام استفاده از state زنجیره‌ای، request ID و مصرف token را ثبت کنید.
- برای پاسخ‌های طولانی یا UI بلادرنگ از [پاسخ‌های جریانی](fa/guides/streaming-responses.md) استفاده کنید.
- وقتی گردش‌کار به دسترسی deterministic به سیستم‌های شما نیاز دارد، از [فراخوانی تابع](fa/guides/function-calling.md) استفاده کنید.

## مثال‌های مرتبط

- [گردش‌کارهای Stateful با Responses API](fa/examples/responses_stateful_workflows.md)
- [مدل‌های Reasoning با Function Calling](fa/examples/reasoning_function_calls.md)
- [حالت WebSocket در Responses](fa/guides/websocket-mode.md)
- [مرجع Responses API](fa/api-reference/responses.md)
