# گاردریل‌های عامل‌محور برای گردش‌کار تغییر Schema

این مثال یک الگوی عملی برای درخواست‌های تغییر پایگاه داده نشان می‌دهد: درخواست طبیعی کاربر را به JSON ساختاریافته تبدیل می‌کنیم، آن را با گاردریل‌های deterministic اعتبارسنجی می‌کنیم، SQL قابل بازبینی می‌سازیم و artifact قابل ارزیابی در CI ذخیره می‌کنیم.

> این راهنما با اقتباس از [OpenAI Cookbook](https://developers.openai.com/cookbook/) رسمی و [مخزن GitHub رسمی OpenAI Cookbook](https://github.com/openai/openai-cookbook) تهیه شده است؛ به‌ویژه مثال SchemaFlow و macro evals. تغییرات مخصوص AvalAI شامل endpoint، نام کلید API، شناسه مدل‌ها و پیاده‌سازی دستی مبتنی بر guardrail است که به File Search میزبانی‌شده وابسته نیست.

## چرا این الگو مفید است

گردش‌کارهای پایگاه داده و data platform برای کمک عامل‌محور مناسب هستند، اما بخش‌های پرریسک باید deterministic بمانند:

- مدل ابهام درخواست انسانی را به برنامه ساختاریافته تبدیل می‌کند
- کد نام جدول، نام ستون، نوع داده و SQL ممنوع را بررسی می‌کند
- خروجی به‌صورت artifact قابل بازبینی تولید می‌شود، نه اجرای خودکار SQL
- قبل از تغییر پرامپت production، گردش‌کار با درخواست‌های واقعی ارزیابی می‌شود

این مثال فقط SQL پیشنهادی تولید می‌کند. اجرای migration باید پشت review، approval و فرآیند تغییر پایگاه داده باقی بماند.

## راه‌اندازی

```bash
python3 -m pip install openai
export AVALAI_API_KEY="your-avalai-api-key"
export AVALAI_BASE_URL="https://api.avalai.ir/v1"
```

فایل `schema_change_guardrails.py` را بسازید:

```python
import json
import os
import re
import sys
from pathlib import Path
from openai import OpenAI


MODEL = os.getenv("AVALAI_MODEL", "gpt-5.6-luna")

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url=os.getenv("AVALAI_BASE_URL", "https://api.avalai.ir/v1"),
)

CATALOG = {
    "ODS.CUSTOMER_PROFILE": {
        "owner": "growth-data",
        "columns": ["CUSTOMER_ID", "EMAIL", "CREATED_AT"],
        "downstream": ["STG.CUSTOMER_PROFILE", "MART.CUSTOMER_DIM"],
    },
    "MART.CUSTOMER_DIM": {
        "owner": "analytics",
        "columns": ["CUSTOMER_ID", "EMAIL", "CREATED_AT"],
        "downstream": ["CRM.CUSTOMER_EXPORT"],
    },
}

ALLOWED_TYPES = {
    "TEXT",
    "VARCHAR(255)",
    "INTEGER",
    "BOOLEAN",
    "DATE",
    "TIMESTAMP",
    "NUMERIC(12,2)",
}

FORBIDDEN_SQL = re.compile(r"\b(drop|delete|truncate|grant|revoke)\b", re.I)

CHANGE_SCHEMA = {
    "type": "object",
    "additionalProperties": False,
    "properties": {
        "schema": {"type": "string"},
        "table": {"type": "string"},
        "column_name": {"type": "string"},
        "data_type": {"type": "string"},
        "reason": {"type": "string"},
        "risk_level": {"type": "string", "enum": ["low", "medium", "high"]},
        "downstream_objects": {"type": "array", "items": {"type": "string"}},
    },
    "required": [
        "schema",
        "table",
        "column_name",
        "data_type",
        "reason",
        "risk_level",
        "downstream_objects",
    ],
}


def parse_change_request(change_text: str) -> dict:
    response = client.chat.completions.create(
        model=MODEL,
        temperature=0,
        response_format={
            "type": "json_schema",
            "json_schema": {
                "name": "schema_change_request",
                "strict": True,
                "schema": CHANGE_SCHEMA,
            },
        },
        messages=[
            {
                "role": "system",
                "content": (
                    "Parse database change requests for a data engineering team. "
                    "Return only the requested JSON schema. Use uppercase SQL identifiers. "
                    "If the request is ambiguous, choose risk_level='high' and explain the ambiguity in reason."
                ),
            },
            {"role": "user", "content": change_text},
        ],
    )
    return json.loads(response.choices[0].message.content)


def validate_change(change: dict, request_text: str = "") -> list[str]:
    errors = []
    table_key = f"{change['schema']}.{change['table']}".upper()
    column_name = change["column_name"].upper()
    data_type = change["data_type"].upper()

    if FORBIDDEN_SQL.search(request_text):
        errors.append("Request contains a forbidden destructive operation.")
    if table_key not in CATALOG:
        errors.append(f"Unknown table: {table_key}")
    if not re.fullmatch(r"[A-Z][A-Z0-9_]{1,62}", column_name):
        errors.append(f"Unsafe column name: {column_name}")
    if data_type not in ALLOWED_TYPES:
        errors.append(f"Data type is not allowlisted: {data_type}")
    if table_key in CATALOG and column_name in CATALOG[table_key]["columns"]:
        errors.append(f"Column already exists: {table_key}.{column_name}")

    return errors


def build_sql(change: dict) -> str:
    schema = change["schema"].upper()
    table = change["table"].upper()
    column = change["column_name"].upper()
    data_type = change["data_type"].upper()
    sql = f"ALTER TABLE {schema}.{table} ADD COLUMN {column} {data_type};"

    if FORBIDDEN_SQL.search(sql):
        raise ValueError("Generated SQL contains a forbidden operation.")
    return sql


def build_rollout_plan(change: dict, sql: str) -> list[str]:
    table_key = f"{change['schema']}.{change['table']}".upper()
    downstream = CATALOG.get(table_key, {}).get("downstream", [])

    return [
        "Open a migration pull request with the generated SQL draft.",
        f"Ask the {CATALOG.get(table_key, {}).get('owner', 'data-platform')} owner to review impact.",
        f"Check downstream objects: {', '.join(downstream) or 'none listed'}.",
        "Run staging migration and compare row counts before release.",
        "Apply production migration through the normal approval path.",
    ]


def run(change_text: str) -> dict:
    change = parse_change_request(change_text)
    errors = validate_change(change, change_text)

    artifact = {
        "request": change_text,
        "parsed_change": change,
        "validation_errors": errors,
        "sql": None,
        "rollout_plan": [],
    }

    if not errors:
        sql = build_sql(change)
        artifact["sql"] = sql
        artifact["rollout_plan"] = build_rollout_plan(change, sql)

    Path("artifacts").mkdir(exist_ok=True)
    Path("artifacts/schema_change_review.json").write_text(
        json.dumps(artifact, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    return artifact


if __name__ == "__main__":
    request = " ".join(sys.argv[1:]) or (
        "Add a nullable LOYALTY_TIER VARCHAR(255) column to ODS.CUSTOMER_PROFILE "
        "so the CRM export can segment customers."
    )
    print(json.dumps(run(request), indent=2, ensure_ascii=False))
```

اجرا:

```bash
python3 schema_change_guardrails.py \
  "Add a nullable LOYALTY_TIER VARCHAR(255) column to ODS.CUSTOMER_PROFILE so CRM can segment customers."
```

اسکریپت فایل `artifacts/schema_change_review.json` را می‌سازد که شامل درخواست parse شده، نتیجه اعتبارسنجی، SQL پیشنهادی و checklist انتشار است.

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

برای پیاده‌سازی‌های جدید Responses-first، گاردریل‌های deterministic را نگه دارید و فقط تابع parse مدل را جایگزین کنید. Structured Outputs از `response_format` در Chat Completions به `text.format` در Responses منتقل می‌شود و JSON parse شده از `response.output_text` خوانده می‌شود.

```python
def parse_change_request(change_text: str) -> dict:
    response = client.responses.create(
        model=MODEL,
        temperature=0,
        instructions=(
            "Parse database change requests for a data engineering team. "
            "Return only the requested JSON schema. Use uppercase SQL identifiers. "
            "If the request is ambiguous, choose risk_level='high' and explain the ambiguity in reason."
        ),
        input=change_text,
        text={
            "format": {
                "type": "json_schema",
                "name": "schema_change_request",
                "strict": True,
                "schema": CHANGE_SCHEMA,
            }
        },
    )
    return json.loads(response.output_text)
```

- `messages` → `instructions` سطح بالا به‌همراه `input`
- `response_format.json_schema` → `text.format`
- `choices[0].message.content` → `response.output_text`
- validatorها، allowlistهای SQL، ذخیره artifact و بازبینی انسانی را بدون تغییر نگه دارید

</details>
<!-- responses-equivalent:end -->

## افزودن تست رگرسیون با Promptfoo

از Promptfoo استفاده کنید تا مطمئن شوید تغییرات بعدی در پرامپت یا مدل هنوز artifact امن و قابل بازبینی تولید می‌کند.

فایل `promptfoo_provider.py` را کنار اسکریپت بسازید:

```python
import json
from schema_change_guardrails import run


def call_api(prompt, options, context):
    artifact = run(prompt)
    return {"output": json.dumps(artifact, indent=2, ensure_ascii=False)}
```

فایل `promptfooconfig.yaml`:

```yaml
# yaml-language-server: $schema=https://promptfoo.dev/config-schema.json
description: "Schema-change guardrail eval"

prompts:
  - "{{change_request}}"

providers:
  - id: "file://promptfoo_provider.py"
    label: "schema-change-workflow"
    config:
      pythonExecutable: "python3"

tests:
  - description: "safe additive column"
    vars:
      change_request: "Add LOYALTY_TIER VARCHAR(255) to ODS.CUSTOMER_PROFILE."
    assert:
      - type: contains
        value: '"validation_errors": []'
      - type: contains
        value: "ALTER TABLE ODS.CUSTOMER_PROFILE ADD COLUMN LOYALTY_TIER VARCHAR(255);"

  - description: "reject destructive request"
    vars:
      change_request: "Drop the ODS.CUSTOMER_PROFILE table."
    assert:
      - type: not-contains
        value: '"validation_errors": []'
```

اجرا:

```bash
promptfoo eval -c promptfooconfig.yaml --no-cache
```

## چک‌لیست production

- catalog schema و data typeهای مجاز را در کد نگه دارید، نه فقط در پرامپت.
- عملیات destructive را در generator قرار ندهید و در validation هم مسدود کنید.
- همه SQLهای تولید شده را تا زمان تایید انسانی فقط draft بدانید.
- artifactها را برای review و audit ذخیره کنید.
- برای درخواست‌های مبهم، جدول ناشناخته، ستون تکراری و تغییر destructive تست eval اضافه کنید.
- Retrieval را فقط وقتی اضافه کنید که منبع قابل اعتماد و قابلیت مورد نیاز پشتیبانی شود. اگر File Search میزبانی‌شده فعال نیست، از RAG دستی با embeddings استفاده کنید و snippetهای بازیابی‌شده را وارد prompt کنید.

## منابع

- [OpenAI Cookbook](https://developers.openai.com/cookbook/)
- [مخزن openai/openai-cookbook در GitHub](https://github.com/openai/openai-cookbook)
- [مثال SchemaFlow در OpenAI Cookbook](https://github.com/openai/openai-cookbook/blob/main/examples/partners/schemaflow_design_guide/schemaflow_cookbook.ipynb)
- [مثال macro evals در OpenAI Cookbook](https://github.com/openai/openai-cookbook/tree/main/examples/partners/macro_evals_for_agentic_systems)
