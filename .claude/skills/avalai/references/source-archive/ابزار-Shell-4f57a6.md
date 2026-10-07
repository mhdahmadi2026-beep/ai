# ابزار Shell

ابزار Shell به مدل اجازه می‌دهد برای کارهای قطعی مثل بررسی فایل‌ها، اجرای script، تبدیل داده یا تولید artifact درخواست command ترمینال بدهد. OpenAI هم containerهای Shell میزبانی‌شده و هم runtimeهای shell محلی را از مسیر `/v1/responses` مستند کرده است.

> این راهنما با اقتباس از [راهنمای رسمی ابزار Shell در OpenAI](https://developers.openai.com/api/docs/guides/tools-shell) تهیه شده و endpoint، کلید API، مدل و نکته‌های دسترسی برای AvalAI تطبیق داده شده است.

!> در AvalAI، Shell میزبانی‌شده به route، مدل و حساب وابسته است. شکل hosted با `tools: [{"type": "shell", ...}]` را فقط وقتی استفاده کنید که route انتخابی `/v1/responses` صریحا از آن پشتیبانی کند. در غیر این صورت commandها را در sandbox خودتان اجرا کنید و نتیجه را از طریق یک ابزار function سخت‌گیرانه یا loop مبتنی بر shell-call برگردانید.

## چه زمانی از Shell استفاده کنیم؟

| وظیفه | مسیر پیشنهادی AvalAI |
| --- | --- |
| اجرای ابزارهای CLI قطعی | Shell مدیریت‌شده توسط برنامه یا Shell میزبانی‌شده پس از تأیید route |
| بررسی repository یا فایل‌های متنی | sandbox محلی با mountهای read-only در صورت امکان |
| تولید report یا artifact | نوشتن در temp storage کنترل‌شده، سپس کپی فایل‌های تأییدشده به storage ماندگار |
| نصب package یا دسترسی شبکه | نیازمند allowlist، approval و audit log |
| اجرای commandهای ارسال‌شده توسط کاربر | به‌صورت پیش‌فرض اجتناب کنید؛ validation، sandbox و consent صریح لازم است |

برای تولید متن معمولی، ریاضی ساده، دسترسی وب نامحدود، مدیریت secretها، workflowهای TTY تعاملی یا commandهای مخرب بدون approval انسانی از Shell استفاده نکنید.

## شکل Hosted در Responses

این شکل را فقط بعد از تأیید پشتیبانی Shell میزبانی‌شده در staging برای route انتخابی AvalAI استفاده کنید.

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model=os.getenv("AVALAI_MODEL", "gpt-5.6-luna"),
    instructions=(
        "Use the shell only for safe, read-only inspection unless the user "
        "explicitly approves a write. Keep commands non-interactive."
    ),
    input="List the current working directory and show the Python version.",
    tools=[
        {
            "type": "shell",
            "environment": {"type": "container_auto"},
        }
    ],
    tool_choice="auto",
)

print(response.output_text)
for item in response.output:
    if item.type == "shell_call":
        print("Shell call:", item.call_id, item.action)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: process.env.AVALAI_MODEL ?? "gpt-5.6-luna",
  instructions:
    "Use the shell only for safe, read-only inspection unless the user explicitly approves a write. Keep commands non-interactive.",
  input: "List the current working directory and show the Python version.",
  tools: [
    {
      type: "shell",
      environment: { type: "container_auto" },
    },
  ],
  tool_choice: "auto",
});

console.log(response.output_text);
for (const item of response.output ?? []) {
  if (item.type === "shell_call") {
    console.log("Shell call:", item.call_id, item.action);
  }
}

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "Use the shell only for safe, read-only inspection unless the user explicitly approves a write. Keep commands non-interactive.",
    "input": "List the current working directory and show the Python version.",
    "tools": [
      {
        "type": "shell",
        "environment": { "type": "container_auto" }
      }
    ],
    "tool_choice": "auto"
  }'

```

## نکته‌های runtime میزبانی‌شده

containerهای Shell میزبانی‌شده OpenAI محیط‌های Linux موقت هستند. در AvalAI، هر مورد زیر را قابلیت وابسته به route بدانید و جداگانه verify کنید:

- Shell میزبانی‌شده ابزار Responses API است، نه ابزار Chat Completions.
- container میزبانی‌شده می‌تواند فایل موقت بنویسد و اگر route از container/file API پشتیبانی کند artifact قابل download برگرداند.
- container قابل استفاده مجدد، `container_reference`، skill bundleهای mountشده، فایل‌های inline و `domain_secrets` قابلیت‌های runtime میزبانی‌شده‌اند، نه تضمین قابل حمل.
- دسترسی شبکه باید به‌صورت پیش‌فرض خاموش باشد. اگر فعال شد، از allowlist سازمانی همراه `network_policy` محدودتر در سطح request استفاده کنید.
- هر endpoint ثالثی که command shell با آن تماس می‌گیرد، policy نگه‌داری داده و residency خودش را دارد.

## Skillها و Apply Patch

مستندات Shell، Skills و Apply Patch در OpenAI یک runtime ویرایش میزبانی‌شده غنی‌تر را توضیح می‌دهد: Skillها instructionها و فایل‌های قابل استفاده مجدد را mount می‌کنند، Shell کشف و تست را انجام می‌دهد و `apply_patch` عملیات ساخت/ویرایش/حذف فایل را ساختاریافته برمی‌گرداند. در AvalAI این ترکیب را فقط وقتی استفاده کنید که route انتخابی `/v1/responses` صریحا از هر ابزار پشتیبانی کند. در غیر این صورت runtime را در backend خودتان نگه دارید و ابزارهای function محدود expose کنید.

| الگوی OpenAI | تطبیق امن در AvalAI |
| --- | --- |
| `skill_reference` میزبانی‌شده | instructionهای workflow بازبینی‌شده را در docs مخزن یا فایل‌های محلی نگه دارید؛ فقط در runtime قابل اعتماد خودتان mount کنید. |
| Skillهای shell محلی | excerpt مربوط به `SKILL.md` یا مسیر فایل را به runner خودتان بدهید؛ پشتیبانی از upload میزبانی‌شده Skill را فرض نکنید. |
| `apply_patch_call` | diffها را در patch harness خودتان validate و اعمال کنید، سپس `apply_patch_call_output` با موفقیت یا شکست برگردانید. |
| حلقه Patch + shell | testها را در sandbox اجرا کنید، failureهای command را به مدل برگردانید و برای write یا command مخرب approval بگیرید. |

Skillها را مثل code و instruction ممتاز review کنید. Skill بدخواه یا بیش از حد گسترده می‌تواند انتخاب ابزارها را عوض کند، داده را از مسیر shell/network نشت دهد یا automation مخرب پیشنهاد کند. catalog باز Skill را در اختیار کاربر نهایی نگذارید؛ Skillهای تأییدشده را به workflowها و ruleهای approval محدود محصول map کنید.

## جایگزین: Shell مدیریت‌شده توسط برنامه

وقتی Shell میزبانی‌شده فعال نیست، execution را در backend خودتان نگه دارید. امن‌ترین الگوی قابل حمل یک ابزار function سخت‌گیرانه است که برنامه command کوچک و تأییدشده می‌خواهد، نه متن shell دلخواه:

```json
{
  "type": "function",
  "name": "run_safe_shell_task",
  "description": "Run an approved, non-interactive shell task in a locked-down sandbox.",
  "parameters": {
    "type": "object",
    "properties": {
      "task": {
        "type": "string"
      },
      "allowed_command": {
        "type": "string"
      },
      "working_directory": {
        "type": "string"
      }
    },
    "required": [
      "task",
      "allowed_command",
      "working_directory"
    ],
    "additionalProperties": false
  },
  "strict": true
}
```

چک‌لیست پیاده‌سازی:

1. commandها را با allowlist تطبیق دهید؛ متن خام تولیدشده توسط مدل را اجرا نکنید.
2. با environment پاک، بدون secretهای ارث‌بری‌شده، mountهای read-only در صورت امکان، و محدودیت کوتاه CPU/حافظه/زمان اجرا کنید.
3. `stdout`، `stderr`، exit code، وضعیت timeout و metadata artifact را capture کنید.
4. نتیجه فشرده را به‌صورت `function_call_output` برگردانید؛ فایل‌های بزرگ را در storage خودتان ذخیره کنید و فقط پس از scan، URL امضاشده برگردانید.
5. برای نصب package، دسترسی شبکه، write، delete، upload، ارسال email، پرداخت یا هر تغییر state خارجی approval بگیرید.

## چک‌لیست ایمنی

- خروجی command و محتوای دریافت‌شده از وب را ورودی غیرقابل اعتماد بدانید.
- API key، URL پایگاه داده، SSH key یا OAuth token را از مسیر prompt، argument command، stdout یا log ماندگار عبور ندهید.
- فقط commandهای غیرتعاملی را بپذیرید؛ promptهای TTY، درخواست رمز و daemonهای طولانی‌مدت را رد کنید مگر اینکه workflow صریحا برای آن طراحی شده باشد.
- user ID، `avalai-request-id`، مدل، برنامه command، تصمیم policy، نتیجه exit، فایل‌های لمس‌شده و artifact IDها را log کنید.
- Shell میزبانی‌شده، Code Interpreter و Computer Use را در docs محصول جدا نگه دارید: مدل execution، نیاز approval و رفتار artifact آن‌ها متفاوت است.

## مرتبط

- [استفاده از ابزارهای داخلی](fa/guides/tools.md)
- [Code Interpreter](fa/guides/tools-code-interpreter.md)
- [فراخوانی تابع](fa/guides/function-calling.md)
- [Responses API](fa/api-reference/responses.md)
