# فشرده‌سازی Context

عامل‌ها و گفت‌وگوهای طولانی به‌مرور context بیشتری از نیاز مدل جمع می‌کنند. فشرده‌سازی، نوبت‌های قدیمی را به یک بسته state کوچک‌تر تبدیل می‌کند و در عین حال facts، نتیجه ابزارها، تصمیم‌ها و کارهای باز لازم برای نوبت بعد را نگه می‌دارد.

OpenAI برای Responses API فشرده‌سازی server-side و standalone را مستند کرده است. در AvalAI این کنترل‌های hosted را route-dependent در نظر بگیرید: فقط وقتی از آن‌ها استفاده کنید که مدل و حساب انتخابی شما صریحا از `context_management`، `compact_threshold` یا `/v1/responses/compact` پشتیبانی کند. الگوی portable زیر با route استاندارد AvalAI یعنی `/v1/responses` کار می‌کند.

## چه چیزهایی را حفظ کنیم

context قدیمی را به یک handoff پایدار تبدیل کنید:

- **هدف:** objective فعلی کاربر و معیارهای موفقیت.
- **State:** facts پایدار، شناسه‌ها، ترجیحات کاربر و محدودیت‌ها.
- **اقدام‌ها:** tool callهای انجام‌شده، side effectها و رکوردهای خارجی تغییرکرده.
- **شواهد:** citationها، نام فایل‌ها، request IDها یا object IDهای لازم برای نوبت بعد.
- **Blockerها:** پرسش‌های باز، callهای ناموفق، retryها یا محدودیت‌های ایمنی.
- **قدم بعدی:** اقدام مشخصی که مدل باید اکنون انجام دهد.

خروجی ابزارهای اخیر، تصمیم‌های ایمنی یا permission checkهایی را که نوبت بعد باید دقیق روی آن‌ها reasoning کند حذف نکنید.

## انتخاب Strategy

| Strategy | چه زمانی استفاده شود | نکته AvalAI |
| --- | --- | --- |
| خلاصه‌سازی مدیریت‌شده در برنامه | وقتی رفتار portable بین providerها یا کنترل دقیق state ذخیره‌شده می‌خواهید. | هرجا `/v1/responses` کار کند قابل استفاده است، اما کیفیت summary به prompt و validation شما وابسته است. |
| فشرده‌سازی server-side | وقتی route انتخابی از `context_management` و `compact_threshold` به سبک OpenAI پشتیبانی می‌کند. | compaction item برگشتی را opaque بدانید و در stateless chaining بدون تغییر append کنید. |
| compact endpoint مستقل | وقتی قبل از نوبت بعد کنترل صریح می‌خواهید و route از `/v1/responses/compact` پشتیبانی می‌کند. | compacted window برگشتی را همان‌طور که هست به درخواست بعدی بدهید؛ prune نکنید. |
| truncation دستی | وقتی فقط باید turnهای قدیمی و نامرتبط chat حذف شوند. | آخرین درخواست کاربر، خروجی ابزارها، شناسه‌ها، محدودیت‌های policy و approvalهای انسانی را verbatim نگه دارید. |

## فشرده‌سازی مدیریت‌شده در برنامه

با یک درخواست معمولی `/v1/responses` یک state object فشرده بسازید، آن را در برنامه خود ذخیره کنید و همراه نوبت بعدی کاربر دوباره بفرستید.

```language-selector
python=:import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

transcript = [
    {"role": "user", "content": "Help me debug this billing integration..."},
    {"role": "assistant", "content": "First I checked the webhook logs..."},
    {"role": "user", "content": "The failed request ID is req_123."},
]

compact = client.responses.create(
    model="gpt-5.6-luna",
    instructions=(
        "Compact the conversation into JSON with keys: goal, facts, "
        "decisions, completed_actions, blockers, next_step. Preserve IDs."
    ),
    input=json.dumps(transcript, ensure_ascii=False),
    store=False,
)

state = compact.output_text

next_response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="Use the compacted state as prior context. Do not invent missing details.",
    input=[
        {"role": "developer", "content": f"Compacted prior state:\n{state}"},
        {"role": "user", "content": "Now draft the fix plan."},
    ],
    store=False,
)

print(next_response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const transcript = [
  { role: "user", content: "Help me debug this billing integration..." },
  { role: "assistant", content: "First I checked the webhook logs..." },
  { role: "user", content: "The failed request ID is req_123." },
];

const compact = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions:
    "Compact the conversation into JSON with keys: goal, facts, decisions, completed_actions, blockers, next_step. Preserve IDs.",
  input: JSON.stringify(transcript),
  store: false,
});

const nextResponse = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "Use the compacted state as prior context. Do not invent missing details.",
  input: [
    { role: "developer", content: `Compacted prior state:\n${compact.output_text}` },
    { role: "user", content: "Now draft the fix plan." },
  ],
  store: false,
});

console.log(nextResponse.output_text);

```

## مرز فشرده‌سازی Hosted

وقتی یک route از فشرده‌سازی hosted به سبک OpenAI پشتیبانی می‌کند:

- فشرده‌سازی server-side می‌تواند داخل `responses.create` و پس از یک `compact_threshold` تنظیم‌شده اجرا شود؛
- فشرده‌سازی standalone می‌تواند یک context window فشرده برای فراخوانی بعدی `/v1/responses` برگرداند؛
- آیتم‌های compaction رمزنگاری‌شده opaque هستند، بنابراین آن‌ها را همان‌طور که برگشته‌اند به جلو منتقل کنید و ویرایش نکنید؛
- اگر از `previous_response_id` استفاده می‌کنید، chain مدیریت‌شده توسط سرور را دستی prune نکنید.

اگر این کنترل‌ها روی route AvalAI شما در دسترس نیستند، از فشرده‌سازی مدیریت‌شده در برنامه و [وضعیت مکالمه](fa/guides/conversation-state.md) استفاده کنید.

خروجی compact میزبانی‌شده یک خلاصه انسانی نیست. آن را machine state برای فراخوانی بعدی مدل بدانید: فقط اگر policy نگه‌داری شما اجازه می‌دهد ذخیره‌اش کنید، بدون تغییر به جلو منتقلش کنید، و هر audit summary انسانی را به‌عنوان artifact جداگانه در برنامه خود نگه دارید.

### رفتار فشرده‌سازی Hosted

هنگام تطبیق الگوی فشرده‌سازی hosted در OpenAI با AvalAI، این قواعد را رعایت کنید:

- فشرده‌سازی server-side داخل `responses.create` و بعد از عبور rendered token count از `compact_threshold` اجرا می‌شود؛ در این حالت endpoint compact جداگانه را فراخوانی نمی‌کنید.
- سرور ممکن است یک compaction item رمزنگاری‌شده در `response.output` یا stream پاسخ emit کند. آن item را state opaque مدل بدانید.
- در stateless input-array chaining، همه output itemهای برگشتی را به input بعدی append کنید. پس از تست، می‌توانید itemهای قبل از جدیدترین compaction item را حذف کنید تا اندازه درخواست و long-tail latency کمتر شود.
- در chaining با `previous_response_id` فقط ورودی جدید کاربر را بفرستید و از prune دستی پرهیز کنید؛ chain مدیریت‌شده توسط سرور مسئول حمل state فشرده‌شده است.
- برای `/v1/responses/compact` مستقل، output برگشتی canonical context window بعدی است. آن را همان‌طور که هست به فراخوانی بعدی `/v1/responses` بدهید و compact output را prune نکنید.

### شکل فشرده‌سازی Server-Side

این شکل را فقط پس از تأیید پشتیبانی route از `context_management` استفاده کنید. threshold باید پایین‌تر از context window مدل باشد و برای output و reasoning tokens حاشیه امن بگذارد.

```language-selector
python=:conversation = [
    {
        "type": "message",
        "role": "user",
        "content": "Start a long support investigation.",
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    input=conversation,
    store=False,
    context_management=[{"type": "compaction", "compact_threshold": 200_000}],
)

# Append output items, including any encrypted compaction item.
conversation.extend(response.output)

javascript=:const conversation = [
  {
    type: "message",
    role: "user",
    content: "Start a long support investigation.",
  },
];

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: conversation,
  store: false,
  context_management: [
    { type: "compaction", compact_threshold: 200000 },
  ],
});

// Append output items, including any encrypted compaction item.
conversation.push(...response.output);

```

### شکل Compact Endpoint مستقل

وقتی `/v1/responses/compact` در دسترس است، current window را پیش از اضافه کردن پیام بعدی کاربر compact کنید. windowای که به compact endpoint می‌فرستید همچنان باید در context window مدل انتخاب‌شده جا شود.

```language-selector
python=:compacted = client.responses.compact(
    model="gpt-5.6-luna",
    input=long_input_items,
)

next_input = [
    *compacted.output,
    {
        "type": "message",
        "role": "user",
        "content": "Continue from the compacted state.",
    },
]

next_response = client.responses.create(
    model="gpt-5.6-luna",
    input=next_input,
    store=False,
)

javascript=:const compacted = await client.responses.compact({
  model: "gpt-5.6-luna",
  input: longInputItems,
});

const nextInput = [
  ...compacted.output,
  {
    type: "message",
    role: "user",
    content: "Continue from the compacted state.",
  },
];

const nextResponse = await client.responses.create({
  model: "gpt-5.6-luna",
  input: nextInput,
  store: false,
});

```

## بهترین شیوه‌ها

- قبل از نزدیک شدن درخواست‌ها به context limit مدل فشرده‌سازی کنید، نه بعد از شروع خطاها.
- آخرین درخواست کاربر و خروجی‌های ابزار حیاتی را verbatim نگه دارید.
- JSON فشرده‌شده را قبل از ذخیره یا ارسال در درخواست بعدی validate کنید.
- مصرف token را قبل و بعد از فشرده‌سازی ثبت کنید تا اثر هزینه و تاخیر را بسنجید.
- اگر از stateless input-array chaining استفاده می‌کنید، فقط پس از تست اینکه نوبت بعد state لازم را دارد، می‌توانید itemهای قبل از جدیدترین hosted compaction item را حذف کنید.
- اگر از `previous_response_id` استفاده می‌کنید، اجازه دهید chain مدیریت‌شده توسط سرور state را حمل کند و از prune دستی پرهیز کنید.
- برای workflowهای production، فشرده‌سازی را با [شمارش توکن](fa/guides/token-counting.md) و [کش کردن پرامپت](fa/guides/prompt-caching.md) ترکیب کنید.
