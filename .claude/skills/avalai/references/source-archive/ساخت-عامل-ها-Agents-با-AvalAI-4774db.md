# ساخت عامل‌ها (Agents) با AvalAI

عامل‌ها برنامه‌هایی هستند که برنامه‌ریزی می‌کنند، ابزار فراخوانی می‌کنند، state را نگه می‌دارند و کارهای چندمرحله‌ای را کامل می‌کنند. راهنمای فعلی OpenAI دو لایه را جدا می‌کند: وقتی یک حلقه مدل به‌همراه ابزارها کافی است از **Responses API** استفاده کنید، و وقتی برنامه شما orchestration، approval، state و observability را مدیریت می‌کند از الگوی agent framework استفاده کنید. در AvalAI این حلقه را با `/v1/responses`، `/v1/chat/completions`، function calling، retrieval و منطق محصول خودتان بسازید.

## معماری عامل در AvalAI

| لایه | کارکرد | مسیر AvalAI |
| --- | --- | --- |
| مدل | استدلال، برنامه‌ریزی و تصمیم‌گیری درباره نیاز به ابزار. | با `gpt-5.5`، `gpt-5.4-pro`، `claude-opus-4-8`، `gemini-3.5-flash` یا مدل پشتیبانی‌شده دیگر از [جستجو در مدل‌ها](fa/models/model-details.md) شروع کنید. |
| دستورالعمل‌ها | نقش، مرزها، قالب خروجی و سیاست استفاده از ابزار را تعریف می‌کند. | در `/v1/responses` از `instructions` یا در `/v1/chat/completions` از پیام‌های developer/system استفاده کنید. |
| ابزارها | به عامل اجازه می‌دهد سیستم‌های بیرونی را بخواند یا تغییر دهد. | از [فراخوانی تابع](fa/guides/function-calling.md)، [جستجوی وب](fa/guides/tools-web-search.md) و ابزارهای application-owned استفاده کنید. |
| وضعیت | مکالمه، reasoning و نتیجه ابزارها را بین turnها حمل می‌کند. | در مسیرهای پشتیبانی‌شده `previous_response_id` را ترجیح دهید؛ در غیر این صورت پیام‌ها یا typed output itemهای قبلی را replay کنید. |
| دانش | پاسخ‌ها را با داده خصوصی grounded می‌کند. | از [Retrieval](fa/guides/retrieval.md)، [Embeddings](fa/api-reference/embeddings.md) و [RAG دستی](fa/examples/manual_rag_with_embeddings.md) استفاده کنید. |
| Guardrails | actionهای ناامن، بدون مجوز یا پرهزینه را مسدود می‌کند. | argumentهای tool را validate کنید، برای actionهای حساس approval بگیرید و در صورت نیاز [Moderation](fa/api-reference/moderation.md) را اجرا کنید. |
| Observability | نشان می‌دهد run چرا چنین رفتاری داشته است. | promptها، مدل انتخابی، tool callها، tool outputها، citationها، latency، خطاها و feedback کاربر را log کنید. |

## انتخاب الگوی عامل

- **دستیار تک‌درخواستی:** یک request به `/v1/responses` با instructions قوی، خروجی ساختاریافته اختیاری و بدون tool.
- **عامل حلقه ابزار:** مدل itemهای `function_call` برمی‌گرداند، سرور شما functionهای تأییدشده را اجرا می‌کند و itemهای `function_call_output` را تا رسیدن به پیام نهایی برمی‌گرداند.
- **عامل RAG:** برنامه شما اول chunkها را retrieve می‌کند، سپس از مدل می‌خواهد فقط از sourceهای citeشده پاسخ دهد.
- **گردش‌کار چندعاملی:** کار را در کد خودتان به stepهای تخصصی تقسیم کنید: planner، retriever، executor، reviewer و final responder.
- **عامل صوتی یا چندوجهی:** APIهای تصویر، صوت یا گفتار را با همان state و tool loop ترکیب کنید.

مستندات Agents SDK شرکت OpenAI را به‌عنوان مرجع معماری برای loopها، handoffها، approvalها و tracing بخوانید. تا زمانی که AvalAI یک hosted agent runtime برای آن سطح اعلام نکرده، orchestration را در برنامه خودتان نگه دارید و مستقیما endpointهای AvalAI را فراخوانی کنید.

### Builderهای میزبانی‌شده، ChatKit و AvalAI

مستندات Agent Builder و ChatKit در OpenAI سطح‌های محصول میزبانی‌شده OpenAI را توضیح می‌دهند. طبق برنامه OpenAI، Agent Builder در تاریخ ۳۰ نوامبر ۲۰۲۶ خاموش می‌شود و ChatKit همچنان یک سطح UI/محصول جدا است. در مستندات AvalAI از این صفحه‌ها فقط به‌عنوان الگوی طراحی استفاده کنید:

- nodeها را به کد برنامه، ابزارهای function سخت‌گیرانه، فراخوانی retrieval و state object صریح نگاشت کنید.
- nodeهای human approval را به policy engine خودتان یا UI تأیید کاربر قابل اعتماد نگاشت کنید.
- trace graderها را به [ارزیابی گردش‌کارهای عامل‌محور](fa/guides/agent-evals.md) و traceهای ذخیره‌شده برنامه نگاشت کنید.
- widgetها یا themeهای ChatKit را به frontend خودتان نگاشت کنید؛ القا نکنید که AvalAI runtime مربوط به ChatKit را میزبانی می‌کند.
- availability میزبانی‌شده OpenAI، مجوزهای workspace و timelineهای deprecation را از پشتیبانی route در AvalAI جدا نگه دارید.

## کنترل‌های ایمنی عامل

راهنمای ایمنی agent در OpenAI دو failure mode تکرارشونده را برجسته می‌کند: prompt injection از محتوای غیرقابل اعتماد و نشت ناخواسته داده خصوصی از طریق ابزارها یا connectorها. در AvalAI، پیش از اینکه مدل بتواند tool call انجام دهد، هر مرز اعتماد را صریح کنید:

| ریسک | کنترل در AvalAI |
| --- | --- |
| متن غیرقابل اعتماد policy را override کند | صفحه‌های بازیابی‌شده، ایمیل‌ها، ticketها و فایل‌های کاربر را در `input` نگه دارید، نه در instructionهای developer/system. پیش از routing به stepهای privileged فقط fieldهای validateشده را استخراج کنید. |
| اشتراک‌گذاری بیش از حد توسط ابزار | خروجی ابزار را compact برگردانید و secretها را پیش از ارسال داده به مدل redact کنید. OAuth token، رکورد خام مشتری یا log داخلی را به‌عنوان tool output نفرستید. |
| نوشتن ناامن | پیش از پرداخت، تغییر حساب، ارسال ایمیل، حذف، post خارجی یا export داده approval بگیرید. ابزارهای write را از ابزارهای read-only جدا نگه دارید. |
| drift در handoff آزاد | برای تصمیم planner، هدف handoff، برچسب ریسک و schema پاسخ نهایی از [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md) استفاده کنید. |
| regression پنهان | پیش از افزایش ترافیک، [ارزیابی گردش‌کارهای عامل‌محور](fa/guides/agent-evals.md) را روی traceها، tool callها، handoffها و رفتار refusal اجرا کنید. |

انتخاب مدل را فقط یک لایه دفاعی بدانید، نه کل برنامه ایمنی. مدل‌هایی با instruction-following قوی‌تر می‌توانند ریسک را کم کنند، اما approval، schema check، tenant authorization و audit log باید در برنامه شما زندگی کنند.

## حلقه حداقلی ابزار با Responses

```language-selector
python=:import json
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def get_order_status(order_id: str) -> str:
    return f"Order {order_id} is packed and waiting for pickup."


tools = [
    {
        "type": "function",
        "name": "get_order_status",
        "description": "Look up the current shipping status for an order.",
        "parameters": {
            "type": "object",
            "properties": {"order_id": {"type": "string"}},
            "required": ["order_id"],
            "additionalProperties": False,
        },
        "strict": True,
    }
]

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a support agent. Call tools only when needed.",
    input="Where is order A123?",
    tools=tools,
)

while True:
    tool_outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        args = json.loads(item.arguments)
        if item.name == "get_order_status":
            result = get_order_status(args["order_id"])
        else:
            result = "Unsupported tool."

        tool_outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result,
            }
        )

    if not tool_outputs:
        print(response.output_text)
        break

    response = client.responses.create(
        model="gpt-5.6-luna",
        previous_response_id=response.id,
        input=tool_outputs,
    )

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

function getOrderStatus(orderId) {
  return `Order ${orderId} is packed and waiting for pickup.`;
}

const tools = [
  {
    type: "function",
    name: "get_order_status",
    description: "Look up the current shipping status for an order.",
    parameters: {
      type: "object",
      properties: { order_id: { type: "string" } },
      required: ["order_id"],
      additionalProperties: false,
    },
    strict: true,
  },
];

let response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a support agent. Call tools only when needed.",
  input: "Where is order A123?",
  tools,
});

while (true) {
  const toolOutputs = [];

  for (const item of response.output) {
    if (item.type !== "function_call") continue;

    const args = JSON.parse(item.arguments);
    const output =
      item.name === "get_order_status"
        ? getOrderStatus(args.order_id)
        : "Unsupported tool.";

    toolOutputs.push({
      type: "function_call_output",
      call_id: item.call_id,
      output,
    });
  }

  if (toolOutputs.length === 0) {
    console.log(response.output_text);
    break;
  }

  response = await client.responses.create({
    model: "gpt-5.6-luna",
    previous_response_id: response.id,
    input: toolOutputs,
  });
}

```

برای مدل‌ها یا integrationهایی که هنوز از `/v1/chat/completions` استفاده می‌کنند، همین معماری را نگه دارید اما نتیجه ابزارها را به‌صورت پیام‌های `role: "tool"` با `tool_call_id` متناظر ارسال کنید.

## Handoff و طراحی متخصص‌ها

handoff یعنی انتقال کنترل‌شده مسئولیت. در agentهای app-owned روی AvalAI آن را صریح پیاده‌سازی کنید:

1. قرارداد ورودی، ابزارهای مجاز و schema خروجی نهایی هر متخصص را تعریف کنید.
2. اجازه دهید planner فقط از یک allowlist، متخصص بعدی را انتخاب کند.
3. یک state object فشرده منتقل کنید: هدف کاربر، محدودیت‌ها، stepهای انجام‌شده، source IDها و approvalهای معلق.
4. ثبت کنید چه کسی مالک پاسخ نهایی قابل نمایش به کاربر است.
5. با evalها loop، handoff زودهنگام و انتخاب tool ناامن را پیدا کنید.

اجازه ندهید یک agent ابزار دلخواه اختراع کند یا به worker ثبت‌نشده delegate کند. permissionها را به executor ابزار وصل کنید، نه به prompt مدل.

## برنامه Trace و ارزیابی

پیش از production، یک dataset کوچک از traceها بسازید که مسیرهای موفق، خطاهای ابزار، تلاش‌های prompt-injection، شکست permission و edge caseهای handoff را پوشش دهد. هر run را بر اساس این معیارها امتیاز دهید:

- انتخاب ابزار: آیا agent تابع و argument درست را انتخاب کرده است؛
- grounding: آیا source IDهای بازیابی‌شده پاسخ را پشتیبانی می‌کنند؛
- ایمنی: آیا agent درخواست‌های پرریسک را رد یا escalate کرده است؛
- کیفیت handoff: آیا planner متخصص درست را انتخاب کرده و loop را متوقف کرده است؛
- هزینه و latency: آیا retryها، tool fan-out و reasoning effort در budget مانده‌اند.

اگر برای route انتخابی AvalAI ابزار trace میزبانی‌شده ندارید، trace برنامه خودتان را با `response.id`، مدل، نسخه prompt، tool callها، tool outputها، تصمیم‌های approval، وضعیت نهایی، latency، مصرف token و feedback کاربر ذخیره کنید. همین trace برای اجرای graderهای آفلاین با `/v1/responses` یا replay کردن failureها در staging کافی است.

## چک‌لیست Production

- **دستورالعمل‌ها:** هدف، رفتار ممنوع، قوانین citation و قواعد escalation را مشخص کنید.
- **ابزارها:** schemaها را strict کنید، argumentها را سمت سرور validate کنید و نتیجه compact و ساختاریافته برگردانید.
- **Approvalها:** پیش از پرداخت، تغییر حساب، ارسال ایمیل، حذف یا نوشتن در سیستم بیرونی، approval انسانی یا policy لازم بگیرید.
- **State:** برای state مدیریت‌شده `previous_response_id` را انتخاب کنید یا وقتی کنترل کامل می‌خواهید typed itemها/messages را replay کنید.
- **Retrieval:** permissionهای tenant و document را پیش از similarity search enforce کنید، نه پس از پاسخ مدل.
- **Streaming:** پیشرفت را برای کاربر stream کنید، اما ابزارها را فقط پس از کامل شدن argumentها اجرا کنید.
- **Evaluation:** موفقیت task، دقت tool، grounding منبع، latency، هزینه، رفتار refusal و بازیابی از خطای tool را تست کنید.

## منابع مرتبط

- [مرجع API پاسخ‌ها](fa/api-reference/responses.md)
- [فراخوانی تابع](fa/guides/function-calling.md)
- [ابزارها](fa/guides/tools.md)
- [وضعیت مکالمه](fa/guides/conversation-state.md)
- [Retrieval](fa/guides/retrieval.md)
- [نمونه Guardrail عامل‌محور](fa/examples/agentic_guardrails_schema_workflow.md)
- [نمونه Function Calling با مدل‌های Reasoning](fa/examples/reasoning_function_calls.md)
