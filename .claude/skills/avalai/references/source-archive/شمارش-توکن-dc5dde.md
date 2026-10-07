# شمارش توکن

اندازه درخواست را پیش از ارسال ترافیک production تخمین بزنید.

## نمای کلی

شمارش توکن کمک می‌کند قبل از فراخوانی API بدانید درخواست در context window مدل جا می‌شود یا نه، هزینه تقریبی را پیش‌بینی کنید و ورودی‌های بزرگ را به مدل مناسب route کنید. مستندات فعلی OpenAI توصیه می‌کند همان payloadی را بشمارید که به Responses API می‌فرستید، چون تصویر، فایل، ابزار، schema، نقش پیام‌ها و قالب‌بندی درخواست می‌توانند توکن‌هایی اضافه کنند که tokenizerهای محلی متن نمی‌بینند.

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

در AvalAI، `POST /v1/responses/input_tokens` را به‌عنوان یک الگوی سازگار با OpenAI در نظر بگیرید، وقتی این route برای حساب، مدل و مسیر شما فعال باشد. اگر route فعال نبود، از تخمین محلی استفاده کنید، محدودیت‌های محافظه‌کارانه برای اندازه درخواست بگذارید و بعد از فراخوانی، با آبجکت `usage` پاسخ و [User API](fa/api-reference/user.md) هزینه واقعی را تطبیق دهید.

## گردش‌کار پیشنهادی

1. context window مدل را با [Models API](fa/api-reference/models.md) بررسی کنید.
2. وقتی route شمارش توکن در دسترس است، قبل از فراخوانی‌های پرهزینه input tokens را بشمارید.
3. ورودی‌های بیش از حد بزرگ را قبل از فراخوانی مدل reject، خلاصه، chunk یا به مدل مناسب route کنید.
4. برای توکن‌های خروجی و reasoning با `max_output_tokens` یا `max_completion_tokens` حاشیه امن بگذارید.
5. `usage` واقعی، `cached_tokens`، مدل، endpoint، service tier و `avalai-request-id` را log کنید.

## چیزهایی که Tokenizer محلی نمی‌بیند

tokenizerهای محلی متن برای تخمین سریع مفیدند، اما شکل کامل request در production را نشان نمی‌دهند. برای موارد زیر route شمارش API را ترجیح دهید:

- ورودی چندوجهی، شامل `input_image`، `file_id`، `file_url` و `file_data` به‌صورت Base64؛
- schema ابزارها، schema خروجی ساختاریافته، ابزارهای MCP و system instructionهای طولانی؛
- توکن‌های قالب‌بندی پنهان برای roleها، مرز پیام‌ها، tool callها و response channelها؛
- رفتار model-specific مثل reasoning، prompt caching، truncation و state مکالمه.

## مثال Responses API

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

payload = {
    "model": "gpt-5.6-luna",
    "instructions": "You are a concise support assistant.",
    "input": [
        {
            "role": "user",
            "content": "Summarize the refund policy in three bullets.",
        }
    ],
}

count = client.responses.input_tokens.count(**payload)
print(f"estimated input tokens: {count.input_tokens}")

if count.input_tokens > 120_000:
    raise ValueError("Input is too large; summarize or chunk it first.")

response = client.responses.create(
    **payload,
    max_output_tokens=500,
)
print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const payload = {
  model: "gpt-5.6-luna",
  instructions: "You are a concise support assistant.",
  input: [
    {
      role: "user",
      content: "Summarize the refund policy in three bullets.",
    },
  ],
};

const count = await client.responses.input_tokens.count(payload);
console.log(`estimated input tokens: ${count.input_tokens}`);

if (count.input_tokens > 120000) {
  throw new Error("Input is too large; summarize or chunk it first.");
}

const response = await client.responses.create({
  ...payload,
  max_output_tokens: 500,
});

console.log(response.output_text);

```

## بررسی سازگاری با cURL

قبل از وابسته کردن production به این route، این تست سریع را اجرا کنید. اگر AvalAI برای حساب یا مدل شما خطای unsupported-route برگرداند، fallback توضیح‌داده‌شده در بالا را نگه دارید.

```bash
curl https://api.avalai.ir/v1/responses/input_tokens \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "Tell me a joke."
  }'
```

## پیش‌برآورد CLI برای اسکریپت‌ها

CLI تولیدشده OpenAI می‌تواند input tokenها را با همان شکل payload در Responses بشمارد. اگر نسخه نصب‌شده شما از URL پایه سفارشی پشتیبانی می‌کند، آن را به AvalAI وصل کنید و از `--transform input_tokens` استفاده کنید تا scriptهای shell فقط عدد count را دریافت کنند:

```bash
OPENAI_API_KEY="$AVALAI_API_KEY" \
  OPENAI_BASE_URL="https://api.avalai.ir/v1" \
  openai responses:input-tokens count \
  --raw-output \
  --transform input_tokens <<'YAML'
model: gpt-5.5
instructions: You are a concise support assistant.
input:
  - role: user
    content: Summarize the refund policy in three bullets.
YAML
```

از این الگو برای gateهای CI، scriptهای batch import و preflight پیش از upload فایل‌های بزرگ یا شروع jobهای background پرهزینه استفاده کنید. اگر نسخه CLI شما `OPENAI_BASE_URL` را رعایت نمی‌کند، از بررسی سازگاری با cURL استفاده کنید تا endpoint AvalAI صریح باشد.

## چه چیزهایی را بشماریم

- **پیام‌ها و instructions:** نقش‌ها، مرزهای پیام و قالب‌بندی می‌توانند فراتر از متن قابل مشاهده توکن اضافه کنند.
- **تصویرها و فایل‌ها:** برای ورودی چندوجهی از تخمین‌هایی مثل `characters / 4` استفاده نکنید؛ هرجا route فعال است، همان را به کار ببرید.
- **ابزارها و schemaها:** تعریف functionها و schemaهای structured output می‌توانند به یک prefix ثابت بزرگ تبدیل شوند.
- **state مکالمه:** همان history، استراتژی `previous_response_id` یا پیام‌های بازسازی‌شده‌ای را لحاظ کنید که واقعا ارسال می‌کنید.

## پیش‌برآورد برای Chat Completions

endpoint شمارش توکن OpenAI شکل درخواست Responses را می‌پذیرد. برای اپلیکیشن‌های موجود `/v1/chat/completions`، پیش از فراخوانی Chat Completions یک payload پیش‌برآورد بسازید که همان محتوا را بازتاب دهد:

| فیلد Chat Completions | شکل preflight برای شمارش توکن |
| --- | --- |
| `messages` | آرایه `input` با همان itemهای `role` و `content` |
| اولین پیام system/developer | `instructions`، یا وقتی ترتیب مهم است همان را به‌عنوان item در `input` نگه دارید |
| `tools` / schemaهای function | همان آرایه `tools`، اگر route سازگار با Responses انتخابی آن را پشتیبانی کند |
| `max_completion_tokens` | برای نسخه Responses معادل با `max_output_tokens` حاشیه خروجی رزرو کنید، اما روی درخواست واقعی Chat همان `max_completion_tokens` را نگه دارید |

از این count به‌عنوان سیگنال محافظه‌کارانه برای برنامه‌ریزی استفاده کنید، نه صورت‌حساب نهایی. پس از فراخوانی Chat، مقدار واقعی را با `usage.prompt_tokens`، `usage.completion_tokens`، `usage.prompt_tokens_details.cached_tokens` و رکورد transaction در User API AvalAI تطبیق دهید. مثال‌های Chat با ورودی/خروجی صوتی مستقیم را روی `/v1/chat/completions` نگه دارید؛ نزدیک‌ترین payload متنی/ابزاری را بشمارید و route واقعی را در staging اعتبارسنجی کنید.

## شمارش Payloadهای چندوجهی و ابزارها

همان request body را استفاده کنید که قرار است به `responses.create` بفرستید. مثال زیر image input و function tool schema را با هم می‌شمارد؛ هر دو مورد با تخمین محلی به‌راحتی کمتر از مقدار واقعی محاسبه می‌شوند.

```language-selector
python=:count = client.responses.input_tokens.count(
    model="gpt-5.6-luna",
    tools=[
        {
            "type": "function",
            "name": "lookup_order",
            "description": "Fetch a customer order by ID.",
            "parameters": {
                "type": "object",
                "properties": {"order_id": {"type": "string"}},
                "required": ["order_id"],
                "additionalProperties": False,
            },
        }
    ],
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_image", "image_url": "https://example.com/receipt.png"},
                {
                    "type": "input_text",
                    "text": "Extract the order ID and summarize the receipt.",
                },
            ],
        }
    ],
)

print(count.input_tokens)

javascript=:const count = await client.responses.input_tokens.count({
  model: "gpt-5.6-luna",
  tools: [
    {
      type: "function",
      name: "lookup_order",
      description: "Fetch a customer order by ID.",
      parameters: {
        type: "object",
        properties: { order_id: { type: "string" } },
        required: ["order_id"],
        additionalProperties: false,
      },
    },
  ],
  input: [
    {
      role: "user",
      content: [
        { type: "input_image", image_url: "https://example.com/receipt.png" },
        { type: "input_text", text: "Extract the order ID and summarize the receipt." },
      ],
    },
  ],
});

console.log(count.input_tokens);

```

برای فایل‌های خصوصی، از [Files API](fa/api-reference/files.md) یا Base64 input مطابق route هدف استفاده کنید؛ فقط برای شمارش توکن، سند خصوصی را با URL عمومی منتشر نکنید.

برای ورودی‌های فایل، دقیقا همان representationی را بشمارید که قرار است به مدل بفرستید:

| شکل ورودی فایل | چه زمانی آن را بشماریم |
| --- | --- |
| `file_id` | فایل‌های خصوصی قابل استفاده مجدد که با `purpose="user_data"` در `/v1/files` آپلود شده‌اند. |
| `file_url` | فایل‌های عمومی یا URLهای HTTPS موقت که مستقیم به Responses داده می‌شوند. |
| `file_data` | فایل‌های محلی که به شکل data URL مبتنی بر Base64 ارسال می‌شوند. |

وقتی route و مدل انتخابی از PDF parsing دارای vision پشتیبانی کند، PDFها می‌توانند متن استخراج‌شده و تصویر صفحات را با هم وارد context مدل کنند. سندهای غیر PDF معمولا text-extracted هستند و فایل‌های spreadsheet-like ممکن است به‌جای شمارش خام تمام سلول‌ها، خلاصه یا augment شوند. همان payload واقعی `input_file` را بشمارید و سپس route نهایی را تست کنید، چون رفتار provider و محدودیت حساب در AvalAI می‌تواند متفاوت باشد.

## حاشیه امن برای توکن خروجی

usage گزارش‌شده برای خروجی می‌تواند شامل متن قابل مشاهده، reasoning tokens، قالب‌بندی tool call و توکن‌های غیرقابل مشاهده دیگر باشد. در همه ارائه‌دهندگان و مدل‌ها، توکن‌های reasoning پنهان با نرخ توکن خروجی مدل انتخابی محاسبه می‌شوند. وقتی `usage.output_tokens` از قبل آنها را شامل می‌شود، `usage.output_tokens_details.reasoning_tokens` تفکیک این مقدار است و نباید دوباره به آن اضافه شود. اگر route خروجی قابل مشاهده و reasoning را جدا گزارش می‌کند، همان نرخ توکن خروجی را برای هر دو مقدار به کار ببرید.

`max_output_tokens` یا `max_completion_tokens` را دقیقا برابر تعداد کلماتی که انتظار دارید تنظیم نکنید. این پارامترها بودجه مشترک تولید هستند، نه سهم رزروشده برای پاسخ قابل مشاهده. مدل reasoning می‌تواند سقف را در پردازش داخلی مصرف کند و هیچ متنی برنگرداند؛ در Responses به دنبال `status: "incomplete"` همراه با `incomplete_details.reason: "max_output_tokens"` باشید و در Chat Completions مقدار `finish_reason: "length"` را بررسی کنید. حاشیه امن بگذارید و سپس `usage.output_tokens`، `usage.output_tokens_details.reasoning_tokens` و طول پاسخ نهایی را در production مانیتور کنید. اگر بودجه تمام شد، سقف را افزایش دهید، در صورت پشتیبانی effort را کاهش دهید یا task را ساده‌تر کنید. بخش [بودجه توکن reasoning](fa/guides/reasoning.md#تخصیص-فضا-برای-استدلال) را ببینید.

## تخمین fallback

وقتی `/v1/responses/input_tokens` روی یک route در دسترس نیست:

- متن ساده را با tokenizer محلی فقط به‌عنوان lower bound تخمین بزنید؛
- برای roleها، ابزارها، schemaها، تصویرها، فایل‌ها و reasoning بودجه اضافه رزرو کنید؛
- قبل از API call محدودیت‌های محافظه‌کارانه برای اندازه request اعمال کنید؛
- پس از call، با `usage.input_tokens`، `usage.output_tokens`، `cached_tokens` و رکوردهای billing AvalAI مقدار واقعی را تطبیق دهید.

## منابع مرتبط

- [بهترین شیوه‌های استقرار](fa/guides/production-best-practices.md)
- [بهینه‌سازی تاخیر](fa/guides/latency-optimization.md)
- [کش کردن پرامپت](fa/guides/prompt-caching.md)
- [بهینه‌سازی هزینه](fa/guides/cost-optimization.md)
- [Responses در برابر Chat Completions](fa/guides/responses-vs-chat-completions.md)
- [Models API](fa/api-reference/models.md)
- اقتباس‌شده برای AvalAI از راهنمای OpenAI درباره [Counting tokens](https://developers.openai.com/api/docs/guides/token-counting).
