# مدل‌های Reasoning با Function Calling

مدل‌های reasoning برای کارهای چندمرحله‌ای مناسب هستند، اما tool use به یک loop نیاز دارد: مدل را صدا بزنید، functionهای درخواست‌شده را اجرا کنید، آیتم‌های `function_call_output` را برگردانید و این چرخه را تا رسیدن به پیام نهایی ادامه دهید.

> این راهنما با اقتباس از [OpenAI Cookbook رسمی](https://developers.openai.com/cookbook) و [دفترچه reasoning function calls](https://github.com/openai/openai-cookbook/blob/main/examples/reasoning_function_calls.ipynb)، همراه با تغییرات لازم برای endpoint و کلید API در AvalAI تهیه شده است.

## loop اصلی

از این الگو استفاده کنید وقتی:

- tool callها ممکن است به نتیجه tool قبلی وابسته باشند.
- مدل به بیش از یک مرحله reasoning نیاز دارد.
- برای toolهای ناشناخته یا argumentهای نادرست، رفتار قابل audit می‌خواهید.
- می‌خواهید با `previous_response_id` از state مدیریت‌شده توسط Responses API استفاده کنید.

## انتخاب استراتژی state

Function calling با مدل reasoning وقتی قابل‌اعتمادتر است که request بعدی بتواند reasoning و آیتم‌های tool قبلی مدل را ببیند. یک الگوی state را انتخاب کنید و همان را ثابت نگه دارید:

| الگو | چه زمانی استفاده شود | چه چیزهایی را حفظ کنید |
| --- | --- | --- |
| `previous_response_id` | وقتی می‌توانید state زنجیره response را به API بسپارید | فقط آیتم‌های جدید `function_call_output` و آخرین `previous_response_id` را بفرستید؛ `instructions` مهم را در هر request صریح نگه دارید. |
| replay دستی آیتم‌ها | وقتی audit log، قوانین retention، کنترل deletion یا compaction اختصاصی لازم دارید | آیتم‌های مرتبط `response.output` را بدون تغییر replay کنید، به‌خصوص آیتم‌های `reasoning`، `function_call` و `function_call_output` از آخرین پیام `user` به بعد. |
| حالت stateless یا شبیه zero-retention | وقتی `store: false` می‌گذارید یا نمی‌توانید به state ذخیره‌شده تکیه کنید | اگر route انتخابی AvalAI پشتیبانی می‌کند، `include=["reasoning.encrypted_content"]` را درخواست کنید و آیتم‌های reasoning رمزنگاری‌شده را replay کنید، نه اینکه متن reasoning را آشکار یا بازنویسی کنید. |

وقتی output itemها را دستی replay می‌کنید، همه چیز را به یک پیام assistant ساده تبدیل نکنید. هر `call_id` را به `function_call_output` متناظر آن متصل نگه دارید و اگر route/model مقدار `phase` برای آیتم assistant برگرداند، همان مقدار را بدون تغییر حفظ کنید.

## مثال Python

```python
import json
import os
from collections.abc import Callable
from uuid import uuid4

from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

MODEL = "o3"


def get_customer_status(customer_id: str) -> str:
    """وضعیت مشتری را از سیستم داخلی شما می‌خواند."""
    fake_db = {
        "cus_123": "enterprise customer, paid through 2026-09-01",
        "cus_456": "trial customer, trial ends in 3 days",
    }
    return fake_db.get(customer_id, "customer not found")


def create_case_id(priority: str) -> str:
    """یک case ID نمونه برای پشتیبانی می‌سازد."""
    return f"{priority.upper()}-{uuid4()}"


tools = [
    {
        "type": "function",
        "name": "get_customer_status",
        "description": "Look up account status for a customer ID.",
        "parameters": {
            "type": "object",
            "properties": {
                "customer_id": {
                    "type": "string",
                    "description": "Customer ID, for example cus_123.",
                }
            },
            "required": ["customer_id"],
            "additionalProperties": False,
        },
    },
    {
        "type": "function",
        "name": "create_case_id",
        "description": "Create a support case ID for a priority level.",
        "parameters": {
            "type": "object",
            "properties": {
                "priority": {
                    "type": "string",
                    "enum": ["low", "normal", "high"],
                }
            },
            "required": ["priority"],
            "additionalProperties": False,
        },
    },
]

tool_mapping: dict[str, Callable[..., str]] = {
    "get_customer_status": get_customer_status,
    "create_case_id": create_case_id,
}


def run_tool_calls(response) -> list[dict]:
    outputs = []

    for item in response.output:
        if item.type != "function_call":
            continue

        tool = tool_mapping.get(item.name)
        if tool is None:
            result = f"Tool {item.name} is not registered."
        else:
            try:
                arguments = json.loads(item.arguments)
                result = tool(**arguments)
            except Exception as exc:
                result = f"Tool {item.name} failed: {exc}"

        outputs.append(
            {
                "type": "function_call_output",
                "call_id": item.call_id,
                "output": result,
            }
        )

    return outputs


def ask_with_tools(question: str) -> str:
    response = client.responses.create(
        model=MODEL,
        reasoning={"effort": "medium", "summary": "auto"},
        tools=tools,
        input=question,
    )

    while True:
        tool_outputs = run_tool_calls(response)

        if not tool_outputs:
            return response.output_text

        response = client.responses.create(
            model=MODEL,
            reasoning={"effort": "medium", "summary": "auto"},
            tools=tools,
            input=tool_outputs,
            previous_response_id=response.id,
        )


answer = ask_with_tools(
    "Customer cus_123 says their production integration is down. "
    "Check their status, decide the priority, create a case ID, and draft a reply."
)

print(answer)
```

## مثال JavaScript

```javascript
import OpenAI from "openai";
import crypto from "node:crypto";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const tools = [
  {
    type: "function",
    name: "get_customer_status",
    description: "Look up account status for a customer ID.",
    parameters: {
      type: "object",
      properties: {
        customer_id: {
          type: "string",
          description: "Customer ID, for example cus_123.",
        },
      },
      required: ["customer_id"],
      additionalProperties: false,
    },
  },
  {
    type: "function",
    name: "create_case_id",
    description: "Create a support case ID for a priority level.",
    parameters: {
      type: "object",
      properties: {
        priority: { type: "string", enum: ["low", "normal", "high"] },
      },
      required: ["priority"],
      additionalProperties: false,
    },
  },
];

const toolMapping = {
  get_customer_status: ({ customer_id }) => {
    const fakeDb = {
      cus_123: "enterprise customer, paid through 2026-09-01",
      cus_456: "trial customer, trial ends in 3 days",
    };
    return fakeDb[customer_id] ?? "customer not found";
  },
  create_case_id: ({ priority }) =>
    `${priority.toUpperCase()}-${crypto.randomUUID()}`,
};

function runToolCalls(response) {
  const outputs = [];

  for (const item of response.output) {
    if (item.type !== "function_call") continue;

    const tool = toolMapping[item.name];
    let result;

    if (!tool) {
      result = `Tool ${item.name} is not registered.`;
    } else {
      try {
        result = tool(JSON.parse(item.arguments));
      } catch (error) {
        result = `Tool ${item.name} failed: ${error.message}`;
      }
    }

    outputs.push({
      type: "function_call_output",
      call_id: item.call_id,
      output: result,
    });
  }

  return outputs;
}

async function askWithTools(question) {
  let response = await client.responses.create({
    model: "o3",
    reasoning: { effort: "medium", summary: "auto" },
    tools,
    input: question,
  });

  while (true) {
    const toolOutputs = runToolCalls(response);
    if (toolOutputs.length === 0) return response.output_text;

    response = await client.responses.create({
      model: "o3",
      reasoning: { effort: "medium", summary: "auto" },
      tools,
      input: toolOutputs,
      previous_response_id: response.id,
    });
  }
}

console.log(
  await askWithTools(
    "Customer cus_123 says their production integration is down. Check their status, decide the priority, create a case ID, and draft a reply.",
  ),
);
```

## شکل cURL برای Tool Output

نکته مهم request دوم است. نتیجه function باید با همان `call_id` اصلی به مدل برگردانده شود.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "o3",
    "input": [
      {
        "type": "function_call_output",
        "call_id": "call_abc123",
        "output": "enterprise customer, paid through 2026-09-01"
      }
    ],
    "previous_response_id": "resp_abc123"
  }'
```

## خطاهایی که باید مدیریت شوند

- نام tool ناشناخته: به جای crash کردن worker، یک خطای ساختاریافته به عنوان خروجی tool برگردانید.
- argument با JSON نامعتبر: خطای parse را برگردانید تا مدل در صورت امکان اصلاح کند.
- timeout در tool: نتیجه timeout را برگردانید یا گردش‌کار response را cancel کنید.
- tool callهای تکراری: برای جلوگیری از اجرای بی‌پایان، حداکثر تعداد loop تعیین کنید.
- نتیجه حساس tool: وقتی خروجی کامل لازم نیست، قبل از ارسال به مدل داده را redact کنید.

## بهترین شیوه‌ها

- schema ابزارها را محدود و صریح نگه دارید.
- argumentها را در برنامه خودتان validate کنید، حتی اگر schema سخت‌گیرانه است.
- نام هر tool call، call ID، latency و نتیجه را لاگ کنید.
- وقتی state مدیریت‌شده توسط API برای شما مناسب است، از `previous_response_id` استفاده کنید.
- اگر context را دستی جلو می‌برید، آیتم‌های reasoning و function-call را بدون تغییر pass-through کنید و آن‌ها را خلاصه نکنید.
- اگر audit، retention یا deletion سخت‌گیرانه لازم دارید، آیتم‌های گفتگو را با ترتیب درست در سیستم خود ذخیره کنید.

## لینک‌های مرتبط

- [مرجع Responses API](fa/api-reference/responses.md)
- [راهنمای Function Calling](fa/guides/function-calling.md)
- [راهنمای Reasoning](fa/guides/reasoning.md)
- [راهنمای وضعیت مکالمه](fa/guides/conversation-state.md)
- [بهترین شیوه‌های Production](fa/guides/production-best-practices.md)
