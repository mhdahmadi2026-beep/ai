# Code Interpreter

Code Interpreter به مدل اجازه می‌دهد Python را در یک container sandbox شده بنویسد و اجرا کند، نتیجه‌ها را بررسی کند و فایل‌های تولیدشده را برگرداند. OpenAI این قابلیت را به‌عنوان ابزار میزبانی‌شده `/v1/responses` با `tools: [{"type": "code_interpreter", ...}]` و تنظیمات `container` مستند کرده است.

> این راهنما با اقتباس از [راهنمای رسمی ابزار Code Interpreter در OpenAI](https://developers.openai.com/api/docs/guides/tools-code-interpreter) تهیه شده و endpoint، کلید API، مدل و نکته‌های دسترسی برای AvalAI تطبیق داده شده است.

!> در AvalAI، Code Interpreter میزبانی‌شده به route، مدل و حساب وابسته است. فقط وقتی از شکل میزبانی‌شده استفاده کنید که route انتخابی `/v1/responses` صریحا از `code_interpreter` پشتیبانی کند. در غیر این صورت اجرای کد را در backend محدود خودتان انجام دهید و فقط یک ابزار function باریک expose کنید.

## چه زمانی استفاده کنیم؟

| وظیفه | مسیر پیشنهادی AvalAI |
| --- | --- |
| ریاضی، تحلیل داده، بررسی CSV | Code Interpreter میزبانی‌شده وقتی فعال است؛ در غیر این صورت function Python مدیریت‌شده توسط برنامه |
| فایل‌های آپلودشده کاربر | فایل‌ها را در برنامه validate و ذخیره کنید، سپس file IDهای تأییدشده یا داده استخراج‌شده را بفرستید |
| نمودار یا artifact تولیدشده | اگر فعال است از container میزبانی‌شده فایل بگیرید، یا از storage خودتان استفاده کنید |
| بررسی و پیش‌پردازش تصویر | فقط وقتی file input و Code Interpreter فعال هستند اجازه دهید ابزار Python میزبانی‌شده تصویر را crop، zoom، rotate یا تحلیل کند؛ در غیر این صورت پردازش تصویر را در backend خودتان اجرا کنید |
| محاسبه تکرارشونده | وقتی مدل باید کد بنویسد، خطا را inspect کند و تا موفق شدن محاسبه یا تبدیل دوباره تلاش کند مفید است |
| automation تولیدی | ابزار backend قطعی با policy check و audit log را ترجیح دهید |

برای اجرای دلخواه و نامطمئن، دسترسی شبکه پنهان، مدیریت secretها، یا کارهایی که یک فراخوانی کتابخانه قطعی کافی است، از Code Interpreter استفاده نکنید.

برای workflowهای vision-heavy، policy تصویر را صریح نگه دارید: ابتدا نوع و اندازه فایل را validate کنید، metadata غیرضروری را حذف کنید، از مدل بخواهید هر transformation را توضیح دهد، و اگر کاربر audit trail لازم دارد تصویر اصلی و artifactهای تولیدشده را در سیستم خودتان ذخیره کنید.

## شکل Hosted در Responses

این شکل را فقط بعد از تأیید پشتیبانی Code Interpreter میزبانی‌شده برای مدل و route انتخابی AvalAI استفاده کنید.

OpenAI اشاره می‌کند که مدل این قابلیت hosted را با نام **python tool** می‌شناسد. promptهایی که «code interpreter» می‌گویند معمولا کار می‌کنند، اما در instructionهای production صریح بنویسید چه زمانی از «the python tool» استفاده شود و چه زمانی بدون اجرای کد پاسخ بدهد.

اگر درخواست کاربر حتما باید Python اجرا کند، روی routeهای پشتیبانی‌شده `tool_choice: "required"` بگذارید. اگر اجرای Python اختیاری است، انتخاب ابزار را automatic نگه دارید و به مدل بگویید فقط وقتی از tool استفاده کند که دقت، تکرارپذیری یا تولید artifact را بهتر می‌کند.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model=os.getenv("AVALAI_MODEL", "gpt-5.6-luna"),
    instructions=(
        "You are a careful data analyst. Use Python only when it improves "
        "accuracy, explain assumptions, and return the final answer clearly."
    ),
    input="Solve 3x + 11 = 14 and show the verification.",
    tools=[
        {
            "type": "code_interpreter",
            "container": {"type": "auto", "memory_limit": "4g"},
        }
    ],
)

print(response.output_text)
for item in response.output:
    if item.type == "code_interpreter_call":
        print("Container:", item.container_id)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: process.env.AVALAI_MODEL ?? "gpt-5.6-luna",
  instructions:
    "You are a careful data analyst. Use Python only when it improves accuracy, explain assumptions, and return the final answer clearly.",
  input: "Solve 3x + 11 = 14 and show the verification.",
  tools: [
    {
      type: "code_interpreter",
      container: { type: "auto", memory_limit: "4g" },
    },
  ],
});

console.log(response.output_text);
for (const item of response.output ?? []) {
  if (item.type === "code_interpreter_call") {
    console.log("Container:", item.container_id);
  }
}

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "You are a careful data analyst. Use Python only when it improves accuracy, explain assumptions, and return the final answer clearly.",
    "input": "Solve 3x + 11 = 14 and show the verification.",
    "tools": [
      {
        "type": "code_interpreter",
        "container": { "type": "auto", "memory_limit": "4g" }
      }
    ]
  }'

```


## Containerها و فایل‌ها

ابزار میزبانی‌شده OpenAI از container sandbox شده استفاده می‌کند. در حالت auto، API یک container می‌سازد یا container فعال قبلی را از context آیتم `code_interpreter_call` دوباره استفاده می‌کند. در حالت explicit، ابتدا container ساخته می‌شود و پاسخ به ID همان container اشاره می‌کند.

برای مستندات AvalAI و برنامه‌های production:

- `memory_limit`، `file_ids`، استفاده مجدد از container، ساخت explicit با `/v1/containers` و annotation فایل‌های تولیدشده را قابلیت‌های hosted بدانید که نیازمند تأیید route هستند.
- tierهای حافظه مستندشده در OpenAI شامل `1g` به‌عنوان پیش‌فرض و همچنین `4g`، `16g` و `64g` است؛ tier بالاتر هزینه بیشتری دارد و برای کل عمر container اعمال می‌شود. پیش از اینکه tier قابل انتخاب کاربر بسازید، availability و pricing در AvalAI را تأیید کنید.
- containerهای hosted را ephemeral فرض کنید. containerهای OpenAI پس از **۲۰ دقیقه (20 minutes) inactivity** منقضی می‌شوند و داده‌های مرتبط را حذف می‌کنند؛ فایل‌های لازم را وقتی container فعال است download کنید و artifactهای durable را در سیستم خودتان نگه دارید.
- فرض نکنید container منقضی‌شده دوباره فعال می‌شود. container تازه بسازید و فایل‌های لازم را دوباره upload کنید. operationهایی مثل دریافت metadata یا اضافه/حذف فایل می‌توانند تا وقتی container فعال است، activity آن را تازه کنند.
- containerهای auto-mode ممکن است در routeهایی که API میزبانی‌شده container را expose می‌کنند از مسیر `/v1/containers` هم دیده شوند. این را یک قابلیت hosted بدانید، نه تضمینی قابل حمل برای همه routeهای مدل در AvalAI.
- فایل‌های کاربر را تا قبل از بررسی malware، اندازه، نوع و policy وارد context مدل نکنید.
- container ID، file ID، نام artifact تولیدشده و request ID را برای پشتیبانی log کنید.
- secret، credential پایگاه داده یا token خصوصی را وارد محیط اجرای کد نکنید.

وقتی hosted file support فعال باشد، فایل‌هایی که در input مدل قرار می‌گیرند ممکن است خودکار به container upload شوند. فایل‌هایی که Python تولید می‌کند، مثل chart یا CSV، می‌توانند به‌صورت annotation نوع `container_file_citation` برگردند و شامل `container_id`، `file_id` و filename باشند. این annotationها را parse کنید تا link دانلود بسازید یا artifactها را پیش از expire شدن container به storage خودتان منتقل کنید.

برای debug، routeهایی که پارامتر OpenAI-compatible با نام `include` را پشتیبانی می‌کنند می‌توانند `code_interpreter_call.outputs` را درخواست کنند تا برنامه شما خروجی اجرای Python را بررسی کند. پیش از نمایش به کاربر یا ثبت در log ماندگار، stdout، stderr، فایل‌های تولیدشده و tracebackها را redaction کنید.

فهرست upload پشتیبانی‌شده در OpenAI شامل فایل‌های source، سندهای office، PDF، CSV/JSON/XML، archive و نوع‌های رایج تصویر است. در برنامه‌های AvalAI همچنان allowlist محصولی داشته باشید و هر MIME type پشتیبانی‌شده را برای همه workflowها قبول نکنید.

### نگه‌داری داده و artifactها

در flow میزبانی‌شده `/v1/responses` در OpenAI، وقتی storage فعال باشد state پاسخ می‌تواند نگه‌داری شود، و containerهای میزبانی‌شده Code Interpreter می‌توانند تا زمان expire یا حذف container، state موقت را در filesystem container بنویسند. در AvalAI این رفتار را قابلیت hosted بدانید که ممکن است بر اساس route و حساب متفاوت باشد:

- برای workflowهایی که state سمت سرور لازم ندارند `store=false` بگذارید و هر قابلیتی را که به state پاسخ یا container وابسته است مستند کنید.
- نمودارها، CSVها، logها و artifactهای تولیدشده را تا وقتی container فعال است به storage خودتان کپی کنید؛ container میزبانی‌شده را storage ماندگار فرض نکنید.
- secretها و داده حساس را پیش از upload حذف کنید، چون stdout، stderr، tracebackها، فایل‌های تولیدشده و annotationها می‌توانند بخشی از خروجی tool یا log شوند.
- اگر runner جایگزین Python شما سرویس‌های third-party را فراخوانی می‌کند، توضیح دهید که آن سرویس‌ها سیاست نگه‌داری داده جداگانه دارند.

## جایگزین: ابزار Python مدیریت‌شده توسط برنامه

وقتی Code Interpreter میزبانی‌شده در دسترس نیست، اجرا را در backend خودتان نگه دارید و یک ابزار function سخت‌گیرانه expose کنید. این الگو در production اغلب امن‌تر است، چون packageها، دسترسی شبکه، timeout، storage و approvalها را خودتان کنترل می‌کنید.

```json
{
  "type": "function",
  "name": "run_python_analysis",
  "description": "Run a small approved Python analysis over prevalidated inputs.",
  "parameters": {
    "type": "object",
    "properties": {
      "task": {
        "type": "string",
        "description": "Short description of the analysis to run."
      },
      "code": {
        "type": "string",
        "description": "Python code that uses only approved libraries and input files."
      },
      "allowed_file_ids": {
        "type": "array",
        "items": {
          "type": "string"
        }
      }
    },
    "required": [
      "task",
      "code",
      "allowed_file_ids"
    ],
    "additionalProperties": false
  },
  "strict": true
}
```

چک‌لیست پیاده‌سازی:

1. کد تولیدشده را پیش از اجرا با allowlist بررسی کنید.
2. آن را در container بدون دسترسی شبکه پیش‌فرض، با محدودیت کوتاه CPU/حافظه و filesystem پاک اجرا کنید.
3. فقط فایل‌های ورودی تأییدشده را mount کنید و خروجی‌ها را در پوشه موقت بنویسید.
4. به جای مسیر خام filesystem، نتیجه ساختاریافته و URL امضاشده artifact را برگردانید.
5. برای jobهای پرهزینه، نوشتن بیرونی یا dataset حساس approval انسانی بگیرید.

وقتی این fallback را از طریق `/v1/responses` expose می‌کنید، آن را مثل هر ابزار function دیگر مدیریت کنید: آیتم `function_call` را بخوانید، job را در backend خودتان اجرا کنید، سپس یک `function_call_output` متناظر با همان `call_id` بفرستید. stdout، stderr، URL artifactها و خطاهای validation را فشرده نگه دارید تا مدل بتواند بدون دریافت log کامل یا فایل خام آن‌ها را خلاصه کند.

## چک‌لیست امنیت

- فقط packageهای allowlist شده را مجاز کنید و shell escape، subprocess و network call دلخواه را مگر با approval صریح مسدود کنید.
- secretها را از prompt، فایل، stdout، stderr و artifactهای تولیدشده حذف کنید.
- فایل‌های آپلودشده و تولیدشده را پیش از ذخیره یا نمایش scan کنید.
- زمان اجرا، حافظه، اندازه خروجی و تعداد artifact را محدود کنید.
- audit log شامل user ID، request ID، مدل، argumentهای tool، تصمیم policy و metadata artifact نگه دارید.
- نمودارها، CSVها و فایل‌های تولیدشده را تا پیش از validation داده غیرقابل اعتماد بدانید.

## مرتبط

- [استفاده از ابزارهای داخلی](fa/guides/tools.md)
- [فراخوانی تابع](fa/guides/function-calling.md)
- [جستجوی فایل](fa/guides/tools-file-search.md)
- [Responses API](fa/api-reference/responses.md)
