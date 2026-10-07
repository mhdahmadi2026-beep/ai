# MCP و connectorها

سرورهای Remote MCP و ابزارهای connector-style به مدل‌های Responses اجازه می‌دهند در صورت نیاز به داده یا عملیات بیرون از مدل، به سیستم‌های خارجی وصل شوند. در AvalAI این قابلیت را یک سطح ابزار پیشرفته برای `/v1/responses` بدانید: فقط زمانی از آن استفاده کنید که مدل، route، حساب و سرویس خارجی صریحا پشتیبانی و قابل اعتماد باشند.

> این راهنما با اقتباس از [راهنمای رسمی MCP و Connectors در OpenAI](https://developers.openai.com/api/docs/guides/tools-connectors-mcp) و [راهنمای Secure MCP Tunnel](https://developers.openai.com/api/docs/guides/secure-mcp-tunnels) تهیه شده و endpoint، کلید API، مدل‌ها و نکته‌های دسترسی برای AvalAI تطبیق داده شده است.

!> پشتیبانی MCP و connector میزبانی‌شده در AvalAI به route، مدل و حساب وابسته است. اگر `tools: [{"type": "mcp", ...}]` فعال نیست، یکپارچه‌سازی را در backend خودتان نگه دارید و فقط یک [ابزار function](fa/guides/function-calling.md) محدود expose کنید.

## چه زمانی از MCP استفاده کنیم

| نیاز | الگوی پیشنهادی |
| --- | --- |
| زمینه عمومی و به‌روز | ابتدا از [جستجوی وب](fa/guides/tools-web-search.md) استفاده کنید |
| پایگاه داده یا API خودتان | از ابزار سفارشی `function` استفاده کنید |
| سرور رسمی MCP یک سرویس ثالث | فقط پس از بررسی پشتیبانی و اعتماد از `type: "mcp"` استفاده کنید |
| connector مبتنی بر OAuth برای SaaS | فقط وقتی فعال است `connector_id` و OAuth `authorization` هر درخواست را بفرستید |
| پرداخت یا نوشتن حساس | approval الزامی کنید و `parallel_tool_calls: false` بگذارید |

## درس‌های Developer Mode در ChatGPT

Developer Mode در ChatGPT یک سطح ساخت app داخل ChatGPT است، نه route API در AvalAI. با این حال برای چک‌لیست ایمنی مفید است، چون سطح کامل ابزارهای MCP، شامل خواندن و نوشتن، را در اختیار مدل می‌گذارد. هنگام انتقال این ایده‌ها به ابزارهای سازگار با `/v1/responses` در AvalAI:

- هر سرور MCP گسترده را تا زمان بررسی همه ابزارهای واردشده، scopeها و ruleهای approval پرریسک بدانید.
- نام و توضیح ابزارها را action-oriented بنویسید؛ توضیح باید بگوید «چه زمانی از این ابزار استفاده کن»، edge caseها و parameterها را روشن کند.
- راهنمایی‌های cross-tool، rate limit مشترک و sequenceهای الزامی را در instructions سرور MCP یا policy برنامه بگذارید، نه در متن user-supplied.
- وقتی چند ابزار هم‌پوشانی دارند، در prompt نام server و tool مطلوب را صریح کنید و برای workflowهای حساس ابزارهای نامرتبط را ممنوع کنید.
- پیش از اجرای هر write action، JSON payload را بررسی کنید. اگر ابزار annotation قابل اعتماد read-only ندارد، آن را write-capable فرض کنید.
- approvalها را در workflowهای غیرقابل اعتماد به خاطر نسپارید. cache کردن approval فقط وقتی امن است که کاربر به app برای تکرار actionهای مشابه اعتماد دارد.

## سرورهای خصوصی و transport

سرور Remote MCP باید برای runtime ابزار میزبانی‌شده قابل دسترس باشد و بهتر است از Streamable HTTP یا HTTP/SSE پشتیبانی کند. در مستندات OpenAI، Secure MCP Tunnel الگوی پیشنهادی برای اتصال سرور خصوصی، on-premises یا پشت firewall بدون باز کردن پورت ورودی است. در AvalAI استفاده از tunnel را به عنوان قابلیت وابسته به دسترسی بررسی کنید: اگر route انتخابی MCP tunneling میزبانی‌شده را expose نمی‌کند، tunnel یا service connector را در backend خودتان اجرا کنید و از طریق یک ابزار function سخت‌گیرانه آن را فراخوانی کنید.

### چک‌لیست طراحی Secure Tunnel

پیش از اتصال هر سرور MCP خصوصی از طریق tunnel میزبانی‌شده، این موارد را بررسی کنید:

- **اتصال فقط outbound:** tunnel client باید اتصال را از داخل شبکه شما آغاز کند؛ فقط برای کار کردن ابزار مدل، ingress عمومی به سرور MCP اضافه نکنید.
- **دامنه سازمان و workspace:** tunnel را فقط به Platform organization، workspace یا API surfaceهایی وصل کنید که واقعا باید آن را فراخوانی کنند. visible بودن tunnel در یک workspace نباید آن را همه‌جا قابل استفاده کند.
- **مجوزهای جداگانه:** مدیریت tunnel، استفاده از tunnel و مجوزهای connector/developer-mode را تصمیم‌های دسترسی جدا بدانید. به operatorها فقط نقش لازم را بدهید.
- **سلامت و troubleshooting:** endpointهای admin یا health را فقط برای operatorهای قابل اعتماد expose کنید. پیش از debug رفتار مدل، مطمئن شوید tunnel client متصل، آماده و در حال polling است.
- **OAuth از مسیر tunnel:** discovery و metadata احراز هویت OAuth می‌تواند از tunnel عبور کند، اما tokenهای کاربر همچنان به secret-handling، scope حداقلی و audit log معمول نیاز دارند.
- **مرزهای logging:** logهای transport مربوط به tunnel، logهای محصول و logهای برنامه MCP server منابع evidence متفاوتی هستند. مشخص کنید تیم incident-response کدام logها را بررسی می‌کند و exportهای پشتیبانی را redact کنید.
- **Fallback در AvalAI:** اگر tunneling میزبانی‌شده برای route انتخابی AvalAI فعال نیست، connector را در backend خودتان اجرا کنید و به‌جای forward کردن سطح گسترده شبکه خصوصی، فقط یک function tool سخت‌گیرانه expose کنید.

## ساخت MCP server فقط برای داده

در راهنمای OpenAI، connectorهای فقط‌داده به‌عنوان سرورهای read-only با سطح ابزار کوچک و قابل پیش‌بینی طراحی می‌شوند. اگر برای workflowهای Responses سازگار با AvalAI یک connector خصوصی برای دانش سازمانی می‌سازید، از این شکل شروع کنید:

| ابزار | هدف | فیلدهای خروجی ضروری |
| --- | --- | --- |
| `search` | برگرداندن رکوردهای مرتبط برای query کاربر | آرایه `results[]` شامل `id`، `title` و `url` canonical |
| `fetch` | برگرداندن محتوای کامل یک رکورد انتخاب‌شده | `id`، `title`، `text`، `url` canonical و `metadata` اختیاری |

نکات پیاده‌سازی:

- برای هر ابزار JSON output schema تعریف کنید تا client بتواند `structuredContent` را validate کند.
- همان مقدار JSON را در `structuredContent` و، برای سازگاری، به شکل JSON text در آرایه MCP `content` برگردانید.
- `search` و `fetch` را read-only نگه دارید. برای نوشتن‌ها، ticketها، پرداخت‌ها یا تغییر حساب، ابزار جداگانه با approval بسازید.
- وقتی citation metadata می‌خواهید، `url` را یک canonical URL غیرخالی قرار دهید. عنوان بدون URL قابل استفاده باید خروجی معمولی ابزار باشد، نه citation.
- IDهای سند را پایدار انتخاب کنید تا backend بتواند دوباره fetch کند؛ اگر primary key پایگاه داده tenant یا ساختار permission را لو می‌دهد، آن را expose نکنید.
- در هر call، permission را داخل خود MCP server اعتبارسنجی کنید. فهرست `allowed_tools` مدل، سیستم authorization نیست.

## شکل درخواست Remote MCP

سرورهای Remote MCP از `server_url` استفاده می‌کنند؛ connectorها از `connector_id`. هر دو در `response.output` به شکل آیتم‌هایی مثل `mcp_list_tools`، `mcp_call` و گاهی `mcp_approval_request` دیده می‌شوند.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="جدیدترین سیاست بازپرداخت را در پایگاه دانش پشتیبانی پیدا کن.",
    tools=[
        {
            "type": "mcp",
            "server_label": "support_kb",
            "server_url": "https://mcp.example.com/sse",
            "allowed_tools": ["search_docs"],
            "require_approval": "never",
        }
    ],
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "جدیدترین سیاست بازپرداخت را در پایگاه دانش پشتیبانی پیدا کن.",
  tools: [
    {
      type: "mcp",
      server_label: "support_kb",
      server_url: "https://mcp.example.com/sse",
      allowed_tools: ["search_docs"],
      require_approval: "never",
    },
  ],
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "جدیدترین سیاست بازپرداخت را در پایگاه دانش پشتیبانی پیدا کن.",
    "tools": [
      {
        "type": "mcp",
        "server_label": "support_kb",
        "server_url": "https://mcp.example.com/sse",
        "allowed_tools": ["search_docs"],
        "require_approval": "never"
      }
    ]
  }'

```

## شکل connector

برای ابزارهای connector-style، برنامه شما OAuth را مدیریت می‌کند و access token کوتاه‌مدت را در فیلد `authorization` در هر درخواست لازم می‌فرستد. access token را داخل prompt، log یا prompt templateهای قابل استفاده مجدد قرار ندهید.

```json
{
  "type": "mcp",
  "server_label": "google_calendar",
  "connector_id": "connector_googlecalendar",
  "authorization": "<oauth access token>",
  "allowed_tools": [
    "list_events"
  ],
  "require_approval": "never"
}
```

شناسه‌های connector رایج در OpenAI شامل `connector_dropbox`، `connector_gmail`، `connector_googlecalendar`، `connector_googledrive`، `connector_microsoftteams`، `connector_outlookcalendar`، `connector_outlookemail` و `connector_sharepoint` هستند. در AvalAI این موارد را نمونه بدانید نه قابلیت تضمین‌شده حساب؛ پیش از عرضه، availability connector، scopeهای OAuth و پشتیبانی مدل را بررسی کنید.

## احراز هویت و scopeها

بیشتر سرورهای MCP مفید و همه یکپارچه‌سازی‌های SaaS از نوع connector به احراز هویت نیاز دارند. `authorization` را secret هر درخواست بدانید، نه state ماندگار مکالمه:

- OAuth access token را در فیلد `authorization` ابزار MCP برای هر درخواست Responses که به آن نیاز دارد بفرستید.
- انتظار نداشته باشید token خام در Response برگشتی دیده شود یا جریان میزبانی‌شده آن را برای استفاده بعدی ذخیره کند.
- حداقل scopeهای OAuth لازم را برای همان ابزارهایی که expose می‌کنید درخواست کنید. ابزارهای در دسترس connector به scopeهای همان token وابسته‌اند.
- سرورهای رسمی MCP را که خود ارائه‌دهنده سرویس اجرا می‌کند ترجیح دهید. با aggregatorها یا proxyهایی که token و داده کاربران را دریافت می‌کنند بسیار محتاط باشید.
- یکپارچه‌سازی‌های read-only و write-capable را جدا کنید تا approval، logging و سیاست پاسخ به رخداد برای actionهای state-changing سخت‌گیرانه‌تر باشد.

## بارگذاری ابزار و تأخیر

وقتی مدل برای نخستین بار یک ابزار MCP را می‌بیند، Responses API ممکن است کاتالوگ ابزار سرور را import کند و آیتم `mcp_list_tools` بسازد. اگر امن است، این آیتم را در conversation state نگه دارید تا turnهای بعدی مجبور نباشند همان فهرست ابزار را دوباره دریافت کنند. برای سرورهای MCP بزرگ، `server_description`، `allowed_tools` و `defer_loading: true` را ترکیب کنید تا مدل فقط وقتی لازم است schemaهای دقیق ابزار را بارگذاری کند.

```json
{
  "type": "mcp",
  "server_label": "support_kb",
  "server_description": "Search approved customer-support documentation.",
  "server_url": "https://mcp.example.com/sse",

  "allowed_tools": ["search_docs"],
  "defer_loading": true,
  "require_approval": "never"
}
```

## بررسی آیتم‌های خروجی

برنامه شما باید آیتم‌های خروجی MCP را بررسی کند و فقط به `output_text` متکی نباشد:

- `mcp_list_tools` کاتالوگ ابزار واردشده برای یک `server_label` را نشان می‌دهد؛ شامل نام‌ها، توضیح‌ها و schemaهای JSON. فقط پس از اعتبارسنجی هویت سرور و schema، آن را در state نگه دارید.
- `mcp_call` شامل `name` ابزار، `arguments` به‌صورت JSON string، `output` ابزار، `server_label`، `approval_request_id` اختیاری و فیلد `error` برای خطاهای protocol، execution یا connectivity است.
- یک response می‌تواند چند MCP call داشته باشد. اگر ترتیب یا approval مهم است، `parallel_tool_calls: false` بگذارید و آرایه خروجی را به‌ترتیب پردازش کنید.
- URLها، ارجاع‌های فایل و محتوای rich برگشتی از سرورهای MCP را داده third-party بدانید. پیش از embed، download یا render کردن، دامنه و نوع فایل را validate کنید.

## عیب‌یابی خطاها

بیشتر مشکل‌های MCP از تنظیمات یا آماده نبودن ابزارها می‌آیند. پیش از تغییر prompt، این چک‌لیست را بررسی کنید:

| نشانه | چه چیزی را بررسی کنیم |
| --- | --- |
| `mcp_list_tools.failed` | `server_url` یا `connector_id`، OAuth token، دسترسی شبکه و نام دقیق ابزارهای `allowed_tools`. |
| `mcp_call.error` یا رویداد tool call ناموفق | آیتم `mcp_call`، logهای سرور، argumentهای ابزار و خطاهای protocol یا execution در MCP را بررسی کنید. |
| درخواست approval متوقف می‌شود | با `previous_response_id` و یک آیتم `mcp_approval_response` ادامه دهید؛ صریحا approve یا reject کنید. |
| بعد از فعال کردن MCP هیچ ابزاری فراخوانی نمی‌شود | صبر کنید فهرست ابزار کامل شود، آیتم‌های ابزار واردشده را در state نگه دارید و تا وقتی حداقل یک ابزار آماده نیست از `tool_choice: "required"` استفاده نکنید. |
| تعریف ابزار validation نمی‌شود | `server_label` یکتا بگذارید؛ دقیقا یکی از `server_url` یا `connector_id` را تنظیم کنید؛ هر دو را خالی نگذارید. |
| احراز هویت connector خطا می‌دهد | در هر درخواست `authorization` را داخل شیء ابزار MCP بفرستید و هم‌زمان `headers.Authorization` نفرستید. |

برای یکپارچه‌سازی‌های AvalAI، route، مدل، `server_label`، نام ابزارهای واردشده، وضعیت احراز هویت به‌صورت redacted و آیتم‌های خروجی typed را log کنید. این evidence نشان می‌دهد مشکل از پشتیبانی مدل، دسترسی حساب، OAuth scope، transport سرور یا مدیریت approval است.

## جریان approval

برای نوشتن‌ها، پرداخت‌ها، ارسال ایمیل، تغییر حساب، حذف داده یا هر عملیاتی که از مرز اعتماد عبور می‌کند approval بگیرید.

1. درخواست اولیه Responses را با `require_approval: "always"` یا یک policy انتخابی بفرستید.
2. در `response.output` دنبال آیتم `mcp_approval_request` بگردید.
3. نام ابزار و argumentهای پیشنهادی را به کاربر قابل اعتماد یا policy engine نشان دهید.
4. زنجیره را با `previous_response_id` و آیتم `mcp_approval_response` ادامه دهید.
5. وقتی ترتیب approval مهم است، `parallel_tool_calls: false` بگذارید.

پیش‌فرض OpenAI برای MCP approval-before-sharing است. فقط پس از trust review از `require_approval: "never"` استفاده کنید، یا با object policy فقط برای چند tool name امن approval را حذف کنید و برای بقیه ابزارها approval را نگه دارید.

## جایگزین: ابزار function مدیریت‌شده توسط برنامه

وقتی MCP میزبانی‌شده برای route انتخابی AvalAI فعال نیست، سرویس خارجی را در برنامه خودتان proxy کنید و فقط عملیات امن را به شکل ابزار function سخت‌گیرانه expose کنید.

```json
{
  "type": "function",
  "name": "search_support_docs",
  "description": "Search approved support documentation by query.",
  "parameters": {
    "type": "object",
    "properties": {
      "query": {
        "type": "string"
      }
    },
    "required": [
      "query"
    ],
    "additionalProperties": false
  },
  "strict": true
}
```

در چرخه Responses، این fallback را فقط پس از اعتبارسنجی `function_call.arguments` اجرا کنید، سپس نتیجه سرویس را در آیتم `function_call_output` با همان `call_id` برگردانید. خروجی را محدود نگه دارید: پاسخ، source IDها، تصمیم permission و خطای redacted کافی است؛ OAuth token خام، payload کامل سرویس ثالث یا log پنهان سرور را برنگردانید.

## چک‌لیست امنیت

- فقط به سرورهای قابل اعتماد وصل شوید؛ ترجیحا سرورهای رسمی که خود ارائه‌دهنده سرویس اجرا می‌کند.
- ابزارهای واردشده را با `allowed_tools` محدود کنید؛ به صورت پیش‌فرض کل کاتالوگ ابزار یک سرور را expose نکنید.
- OAuth tokenها را در secret store نگه دارید و از طریق `authorization` بفرستید، نه متن prompt.
- در هر درخواست Responses که به آن نیاز دارد `authorization` را دوباره بفرستید؛ جریان‌های Responses میزبانی‌شده token خام را برای استفاده مجدد برنمی‌گردانند یا ذخیره نمی‌کنند.
- برای خواندن‌های حساس و همه عملیات state-changing approval الزامی کنید.
- فقط برای ابزارهای read-only، قابل اعتماد و قابل تحمل از نظر اشتراک خودکار داده از `require_approval: "never"` استفاده کنید.
- audit trail حداقلی اما مفید ثبت کنید: server label، نام ابزار، argumentهای redacted، نتیجه و approver.
- خروجی MCP را داده third-party بدانید؛ پیش از نمایش، لینک‌ها، file IDها و دامنه‌ها را اعتبارسنجی کنید.
- نتیجه‌های `mcp_list_tools` را فقط پس از اعتبارسنجی schema ابزار و هویت سرور نگه دارید یا cache کنید.
- انتظارات Zero Data Retention و data residency را برای هر سرور MCP ثالث جداگانه بررسی کنید؛ پس از خروج داده از مسیر inference میزبانی‌شده AvalAI/OpenAI، سیاست‌های retention و residency سرویس خارجی اعمال می‌شود.

## مرتبط

- [استفاده از ابزارهای داخلی](fa/guides/tools.md)
- [API پاسخ‌ها](fa/api-reference/responses.md)
- [فراخوانی تابع](fa/guides/function-calling.md)
- [کنترل داده‌ها](fa/guides/data-controls.md)
