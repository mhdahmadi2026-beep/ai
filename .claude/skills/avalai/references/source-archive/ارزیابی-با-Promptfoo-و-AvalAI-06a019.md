# ارزیابی با Promptfoo و AvalAI

از Promptfoo زمانی استفاده کنید که برای پرامپت‌ها، ارتقای مدل، منطق مسیریابی یا گردش‌کارهای عامل‌محور به تست رگرسیون قابل اجرا در مخزن کد نیاز دارید. این مثال ارزیابی را کنار کد برنامه نگه می‌دارد و از طریق SDK سازگار با OpenAI به AvalAI وصل می‌شود.

> این راهنما با اقتباس از [OpenAI Cookbook](https://developers.openai.com/cookbook/) رسمی و [مخزن GitHub رسمی OpenAI Cookbook](https://github.com/openai/openai-cookbook) تهیه شده است؛ به‌ویژه مثال‌های مهاجرت به Promptfoo و SchemaFlow. تغییرات مخصوص AvalAI شامل نام کلید API، آدرس پایه و شناسه مدل‌ها است.

## چه زمانی از این الگو استفاده کنیم

از ارزیابی محلی Promptfoo استفاده کنید وقتی:

- می‌خواهید قبل از تغییر ترافیک production دو مدل AvalAI را مقایسه کنید
- در حال بهبود پرامپت هستید و می‌خواهید رگرسیون‌ها را پیدا کنید
- می‌خواهید CI هنگام افت کیفیت خروجی شکست بخورد
- API بومی AvalAI Evals هنوز برای حساب شما فعال نیست

برای قابلیت‌های hosted AvalAI eval، [ارزیابی‌ها](fa/guides/evals.md) را ببینید. برای گردش‌کارهای محلی و CI، الگوی زیر با فراخوانی معمول API کار می‌کند.

## تبدیل مفاهیم OpenAI Evals به Promptfoo

در OpenAI evals، schema دیتاست از معیارهایی که خروجی مدل را می‌سنجند جدا است. همین جداسازی را در Promptfoo هم نگه دارید:

| مفهوم در OpenAI eval | معادل در Promptfoo | نکته برای AvalAI |
| --- | --- | --- |
| `data_source_config` | `tests[].vars` به‌همراه شکل fixture مستند | labelهای انسانی مثل `expected_label` را کنار ورودی کاربر نگه دارید. |
| `testing_criteria` | بلوک‌های `assert` | قبل از LLM-as-judge با checkهای deterministic شروع کنید. |
| `{{ item.correct_label }}` | `{{expected_label}}` یا مقدار `value` در assertion | این مقدار را ground truth بازبینی‌شده توسط انسان در نظر بگیرید. |
| `{{ sample.output_text }}` | مقدار برگشتی provider مثل `{"output": ...}` | برای `/v1/responses` مقدار `response.output_text` را برگردانید. |

قبل از نوشتن پرامپت، قرارداد دیتاست را بنویسید. در این مثال، هر test case یک رشته `ticket` و یک دسته مورد انتظار دارد.

## نصب

```bash
npm install -g promptfoo
python3 -m pip install openai

export AVALAI_API_KEY="your-avalai-api-key"
export AVALAI_BASE_URL="https://api.avalai.ir/v1"
```

## ساخت Provider پایتون

فایل `evals/support-ticket/avalai_eval_provider.py` را بسازید:

```python
import os
from openai import OpenAI


MODEL = os.getenv("AVALAI_EVAL_MODEL", "gpt-5.6-luna")

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url=os.getenv("AVALAI_BASE_URL", "https://api.avalai.ir/v1"),
)


def call_api(prompt, options, context):
    vars_ = (context or {}).get("vars", {})
    ticket = vars_.get("ticket", prompt)

    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": (
                    "Classify the support ticket as exactly one of: "
                    "Hardware, Software, Billing, Account, Other. "
                    "Return only the label."
                ),
            },
            {"role": "user", "content": ticket},
        ],
    )

    return {"output": response.choices[0].message.content.strip()}
```

Promptfoo برای هر تست `call_api()` را صدا می‌زند. این Provider کلید AvalAI را فقط روی ماشین اجرای eval نگه می‌دارد و نیازی نیست کلید در YAML قرار بگیرد.

<!-- responses-equivalent:start -->
<details>
<summary>نسخه Provider با Responses API</summary>

برای Providerهای جدید eval، وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند از Responses استفاده کنید. دستور پایدار طبقه‌بندی را در `instructions` بگذارید، متن ticket را در `input` بفرستید و خروجی را از `response.output_text` برگردانید.

```python
def call_api(prompt, options, context):
    vars_ = (context or {}).get("vars", {})
    ticket = vars_.get("ticket", prompt)

    response = client.responses.create(
        model=MODEL,
        temperature=0,
        instructions=(
            "Classify the support ticket as exactly one of: "
            "Hardware, Software, Billing, Account, Other. "
            "Return only the label."
        ),
        input=ticket,
        store=False,
    )

    return {"output": response.output_text.strip()}
```

- `messages` → `instructions` به‌همراه `input`
- `choices[0].message.content` → `response.output_text`
- برای evalهای محلی CI، مگر اینکه retrieval بعدی لازم دارید، `store=False` بگذارید

</details>
<!-- responses-equivalent:end -->

## اضافه کردن تست‌ها

فایل `evals/support-ticket/promptfooconfig.yaml` را بسازید:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: "AvalAI support-ticket classification regression eval"

prompts:
  - "{{ticket}}"

providers:
  - id: "file://avalai_eval_provider.py"
    label: "avalai-gpt-5.5"
    config:
      pythonExecutable: "python3"

tests:
  - description: "monitor power issue"
    vars:
      ticket: "My monitor will not turn on after I changed desks."
    assert:
      - type: equals
        value: "Hardware"

  - description: "invoice question"
    vars:
      ticket: "Why was my card charged twice this month?"
    assert:
      - type: equals
        value: "Billing"

  - description: "password reset"
    vars:
      ticket: "I cannot sign in and need to reset my password."
    assert:
      - type: equals
        value: "Account"
```

## اضافه کردن معیار Judge با احتیاط

وقتی خروجی مجموعه کوچکی از labelها دارد، مثل همین دسته‌بندی ticket، از assertionهای دقیق استفاده کنید. فقط وقتی رفتار semantic، چندمرحله‌ای یا گسترده‌تر از `equals` و regex است LLM-as-judge اضافه کنید. معیار judge باید کوتاه، قابل مشاهده و وابسته به فیلدهای دیتاست باشد.

```yaml
- description: "ambiguous issue should be escalated"
    vars:
      ticket: "The dashboard looks wrong and my bill changed after an upgrade."
    assert:
      - type: llm-rubric
        value: >-
          The answer must choose either Billing or Other, explain no extra
          facts, and must not invent account details that are not in the ticket.
```

برای evalهای production، قبل از اینکه checkهای judge-based باعث شکست CI شوند، آن‌ها را با یک مجموعه کوچک بازبینی‌شده توسط انسان calibrate کنید.

## اجرای محلی

```bash
cd evals/support-ticket
promptfoo validate config -c promptfooconfig.yaml
promptfoo eval -c promptfooconfig.yaml --no-cache
promptfoo view
```

هنگام توسعه eval از `--no-cache` استفاده کنید. وقتی تست‌ها پایدار شدند، برای اجرای سریع‌تر می‌توانید آن را حذف کنید.

## مقایسه مدل‌ها

برای مقایسه مدل‌ها، همان config را با مقدار متفاوت `AVALAI_EVAL_MODEL` اجرا کنید و نتایج ذخیره‌شده Promptfoo را مقایسه کنید.

```bash
AVALAI_EVAL_MODEL="gpt-5.4" promptfoo eval -c promptfooconfig.yaml --no-cache
AVALAI_EVAL_model="gpt-5.6-luna" promptfoo eval -c promptfooconfig.yaml --no-cache
```

هنگام مقایسه مدل‌ها dataset ارزیابی را ثابت نگه دارید. هر بار فقط یک چیز را تغییر دهید: مدل، پرامپت، schema ابزار یا context بازیابی.

## اضافه کردن به CI

```yaml
name: prompt-evals

on:
  pull_request:
  workflow_dispatch:

jobs:
  evals:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - uses: actions/setup-node@v4
        with:
          node-version: 22
      - uses: actions/setup-python@v5
        with:
          python-version: "3.11"
      - run: npm install -g promptfoo
      - run: python3 -m pip install openai
      - run: promptfoo eval -c evals/support-ticket/promptfooconfig.yaml --no-cache
        env:
          AVALAI_API_KEY: ${{ secrets.AVALAI_API_KEY }}
          AVALAI_BASE_URL: https://api.avalai.ir/v1
```

## کاربردی‌تر کردن eval

- مثال‌ها را شبیه ورودی واقعی کاربران نگه دارید، حتی با غلط تایپی و پیام‌های کوتاه.
- نمونه‌های منفی اضافه کنید که باید رد شوند، escalation بخورند یا `Other` برگردانند.
- قبل از LLM-as-judge، از assertionهای deterministic مثل `equals`، `contains` یا regex استفاده کنید.
- ابتدا قرارداد خروجی مورد انتظار را تعریف کنید و بعد assertionهایی انتخاب کنید که همان قرارداد را اثبات کنند.
- هنگام مقایسه promptها یا مدل‌ها، ground truth برچسب‌گذاری‌شده توسط انسان را ثابت نگه دارید.
- هنگام تغییر پرامپت production، نتایج قبلی را نگه دارید تا reviewer ببیند چه چیزی بهتر یا بدتر شده است.
- evalهای کوچک را روی هر pull request و مجموعه‌های بزرگ‌تر را قبل از release اجرا کنید.

## منابع

- [OpenAI Cookbook](https://developers.openai.com/cookbook/)
- [مخزن openai/openai-cookbook در GitHub](https://github.com/openai/openai-cookbook)
- [راهنمای مهاجرت OpenAI Cookbook به Promptfoo](https://github.com/openai/openai-cookbook/blob/main/examples/evaluation/moving-from-openai-evals-to-promptfoo.md)
- [مثال SchemaFlow در OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/partners/schemaflow_design_guide/schemaflow_cookbook.ipynb)
