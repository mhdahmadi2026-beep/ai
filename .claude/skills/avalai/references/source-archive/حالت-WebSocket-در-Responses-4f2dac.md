# حالت WebSocket در Responses

از حالت WebSocket در Responses برای گردش‌کارهای طولانی و ابزارمحور استفاده کنید؛ جایی که اتصال پایدار و ورودی‌های incremental می‌تواند latency هر turn را کم کند.

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

> این راهنما با اقتباس از مستندات رسمی OpenAI درباره [WebSocket Mode](https://developers.openai.com/api/docs/guides/websocket-mode)، [وضعیت مکالمه](https://developers.openai.com/api/docs/guides/conversation-state) و [compaction](https://developers.openai.com/api/docs/guides/compaction)، با تغییرات endpoint، کلید API، نکات availability در routeهای AvalAI و مسیر fallback تهیه شده است.

## Availability در AvalAI

OpenAI حالت WebSocket را به‌عنوان transport پایدار برای `/v1/responses` مستند کرده است. در AvalAI آن را وابسته به route، مدل و حساب بدانید. پیش از تکیه بر `wss://api.avalai.ir/v1/responses`، پشتیبانی را در staging تأیید کنید؛ اگر route شما URL متفاوتی دارد، آن را در `AVALAI_RESPONSES_WS_URL` تنظیم کنید.

اگر حالت WebSocket در دسترس نبود، همان شکل درخواست Responses را از طریق HTTP نگه دارید:

- وقتی state میزبانی‌شده پشتیبانی می‌شود و policy نگهداری داده اجازه می‌دهد، از `POST /v1/responses` همراه `previous_response_id` استفاده کنید؛
- وقتی رفتار stateless یا `store: false` می‌خواهید، آیتم‌های لازم را دستی replay کنید؛
- برای نمایش تدریجی متن در UI، از `stream: true` روی SSE استفاده کنید.

## چه زمانی استفاده کنیم

حالت WebSocket برای workflowهایی مناسب است که round tripهای زیاد بین مدل و ابزار دارند:

- loopهای agentic coding با خروجی ابزارهای تکراری؛
- workerهای orchestration که یک task را در چندین turn فعال نگه می‌دارند؛
- زنجیره‌های ابزار کم‌latency که reconnect در هر turn هزینه اضافه ایجاد می‌کند؛
- workflowهای stateful که از قبل از `previous_response_id` استفاده می‌کنند.

برای promptهای تک‌مرحله‌ای، clientهای مرورگر که نباید API key نگه دارند، یا workloadهایی که می‌خواهند چند پاسخ موازی را روی یک socket اجرا کنند، از این حالت استفاده نکنید. هر اتصال WebSocket باید مالک یک response در حال اجرا باشد.

## مدل Transport

| موضوع | رفتار |
| --- | --- |
| اتصال | یک WebSocket پایدار به route مربوط به Responses باز کنید. |
| ایجاد turn | یک event JSON با نوع `response.create` بفرستید. payload شبیه `POST /v1/responses` است؛ فیلدهای مخصوص transport مثل `stream` و `background` استفاده نمی‌شوند. |
| ادامه turn | یک `response.create` دیگر با `previous_response_id` و فقط input itemهای جدید بفرستید. |
| Cache | اتصال فعال می‌تواند آخرین previous response را برای continuation سریع در حافظه نگه دارد. |
| هم‌زمانی | responseها sequential اجرا می‌شوند؛ برای workflowهای موازی socket جدا بسازید. |
| طول عمر | برای reconnect قبل از رسیدن به محدودیت مستند ۶۰ دقیقه برنامه داشته باشید. |

## اتصال و ایجاد Response

ابتدا WebSocket client نصب کنید:

```bash
pip install websocket-client
npm install ws
```

```language-selector
python=:import json
import os
from websocket import create_connection

ws = create_connection(
    os.getenv("AVALAI_RESPONSES_WS_URL", "wss://api.avalai.ir/v1/responses"),
    header=[f"Authorization: Bearer {os.environ['AVALAI_API_KEY']}"],
)

ws.send(
    json.dumps(
        {
            "type": "response.create",
            "model": "gpt-5.6-luna",
            "store": False,
            "input": [
                {
                    "type": "message",
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Find the bottleneck in this worker.",
                        }
                    ],
                }
            ],
            "tools": [],
        }
    )
)

while True:
    event = json.loads(ws.recv())
    if event["type"] == "response.output_text.delta":
        print(event["delta"], end="", flush=True)
    elif event["type"] == "response.completed":
        response_id = event["response"]["id"]
        print(f"\ncompleted: {response_id}")
        break
    elif event["type"] in {"response.failed", "error"}:
        raise RuntimeError(event)

javascript=:import WebSocket from "ws";

const ws = new WebSocket(
  process.env.AVALAI_RESPONSES_WS_URL ?? "wss://api.avalai.ir/v1/responses",
  {
    headers: {
      Authorization: `Bearer ${process.env.AVALAI_API_KEY}`,
    },
  },
);

ws.on("open", () => {
  ws.send(
    JSON.stringify({
      type: "response.create",
      model: "gpt-5.6-luna",
      store: false,
      input: [
        {
          type: "message",
          role: "user",
          content: [
            { type: "input_text", text: "Find the bottleneck in this worker." },
          ],
        },
      ],
      tools: [],
    }),
  );
});

ws.on("message", (data) => {
  const event = JSON.parse(data.toString());
  if (event.type === "response.output_text.delta") {
    process.stdout.write(event.delta);
  } else if (event.type === "response.completed") {
    console.log(`\ncompleted: ${event.response.id}`);
    ws.close();
  } else if (event.type === "response.failed" || event.type === "error") {
    throw new Error(JSON.stringify(event));
  }
});

```

## ادامه با ورودی‌های Incremental

پس از کامل شدن response اول، socket را باز نگه دارید و فقط input itemهای جدید را همراه آخرین `previous_response_id` بفرستید.

```language-selector
python=:ws.send(
    json.dumps(
        {
            "type": "response.create",
            "model": "gpt-5.6-luna",
            "store": False,
            "previous_response_id": response_id,
            "input": [
                {
                    "type": "function_call_output",
                    "call_id": "call_123",
                    "output": "The worker spends 70% of time waiting on Redis.",
                },
                {
                    "type": "message",
                    "role": "user",
                    "content": [
                        {
                            "type": "input_text",
                            "text": "Suggest the safest optimization.",
                        }
                    ],
                },
            ],
            "tools": [],
        }
    )
)

javascript=:ws.send(
  JSON.stringify({
    type: "response.create",
    model: "gpt-5.6-luna",
    store: false,
    previous_response_id: responseId,
    input: [
      {
        type: "function_call_output",
        call_id: "call_123",
        output: "The worker spends 70% of time waiting on Redis.",
      },
      {
        type: "message",
        role: "user",
        content: [
          { type: "input_text", text: "Suggest the safest optimization." },
        ],
      },
    ],
    tools: [],
  }),
);

```

`instructions` مهم را در هر turn دوباره ارسال کنید. `previous_response_id` در routeهای پشتیبانی‌شده context پاسخ را حمل می‌کند، اما instructionهای top-level را خودکار دائمی نمی‌کند.

## State، نگهداری داده و Recovery

loopهای WebSocket را با fallback صریح طراحی کنید:

| وضعیت | اقدام پیشنهادی |
| --- | --- |
| `store: true` و response قبلی persist شده است | reconnect کنید و با `previous_response_id` به‌همراه input itemهای جدید ادامه دهید. |
| `store: false`، flow شبیه ZDR، یا ID خارج از cache | chain تازه‌ای با `previous_response_id: null` شروع کنید و context کامل یا compacted window بفرستید. |
| `previous_response_not_found` | به‌عنوان response تازه با context کامل retry کنید؛ فرض نکنید سرور همیشه chain را hydrate می‌کند. |
| `websocket_connection_limit_reached` | WebSocket جدید باز کنید و از آخرین state پایدار ادامه دهید. |
| continuation ناموفق (`4xx` یا `5xx`) | پیش از retry، state را از log برنامه خودتان بازسازی کنید. |

حتی وقتی `previous_response_id` ارسال payload را ساده‌تر می‌کند، هزینه درخواست‌های chained را طوری بودجه‌بندی کنید که context قبلی مرتبط همچنان می‌تواند input token حساب شود.

## الگوهای Compaction

برای agentهای طولانی، WebSocket continuation را با [فشرده‌سازی Context](fa/guides/compaction.md) ترکیب کنید:

- **Compaction سمت سرور:** اگر route از `context_management` همراه `compact_threshold` پشتیبانی می‌کند، روی socket به‌صورت عادی با آخرین `previous_response_id` و فقط input itemهای جدید ادامه دهید.
- **`/v1/responses/compact` مستقل:** وقتی endpoint compact در دسترس است، آن را از طریق HTTP فراخوانی کنید، سپس response جدیدی روی WebSocket با compacted window برگشتی به‌عنوان `input` شروع کنید؛ `previous_response_id` را حذف کنید یا `null` بگذارید.
- **Fallback قابل حمل:** state را در برنامه خود با `/v1/responses` خلاصه کنید، طبق policy نگهداری ذخیره کنید و همراه turn بعدی بفرستید.

آیتم‌های compaction رمزنگاری‌شده یا opaque را ویرایش نکنید. compacted windowهای برگشتی را state ماشینی برای درخواست بعدی بدانید.

## مسیر مهاجرت از HTTP Responses

1. workflow را با `POST /v1/responses` معمولی بسازید.
2. تا وقتی state handling درست شود، `previous_response_id` یا replay دستی itemها را اضافه کنید.
3. اگر UI به متن تدریجی نیاز دارد، `stream: true` را اضافه کنید.
4. فقط workerهای طولانی و ابزارمحور واجد شرایط را پس از تأیید staging به WebSocket منتقل کنید.
5. مسیر HTTP را برای recovery، routeهای پشتیبانی‌نشده و workflowهای حساس به compliance نگه دارید.

## چک‌لیست Production

- URL دقیق WebSocket، پشتیبانی مدل و entitlement حساب را در staging تأیید کنید.
- API key را فقط روی سرورهای قابل اعتماد نگه دارید؛ کلید server را در مرورگر افشا نکنید.
- task ID، response ID، request ID، context کاربر/tenant و usage را در سیستم خودتان ذخیره کنید.
- برای هر socket فقط یک response در حال اجرا enforce کنید؛ برای کار موازی connection pool بسازید.
- قبل از ۶۰ دقیقه reconnect کنید و از context کامل، context فشرده یا response ID ذخیره‌شده recover کنید.
- `previous_response_not_found`، بسته شدن connection، timeout، `429` و خطاهای provider-specific `4xx`/`5xx` را handle کنید.

## راهنماهای مرتبط

- [مرجع Responses API](fa/api-reference/responses.md)
- [وضعیت مکالمه](fa/guides/conversation-state.md)
- [پاسخ‌های جریانی](fa/guides/streaming-responses.md)
- [فشرده‌سازی Context](fa/guides/compaction.md)
- [مدیریت خطا](fa/guides/error-handling.md)
