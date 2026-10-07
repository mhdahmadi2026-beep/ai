# Graderهای محلی برای Evalهای AvalAI

Graderها بررسی‌های خودکاری هستند که خروجی مدل را با پاسخ مرجع، rubric، schema یا tool call مورد انتظار مقایسه می‌کنند. مفهوم grader در مستندات hosted OpenAI مفید است، اما AvalAI در حال حاضر API میزبانی‌شده برای `/v1/evals` یا grader ارائه نمی‌کند. این راهنما را به‌عنوان الگوی محلی و CI برای فراخوانی‌های عادی AvalAI استفاده کنید.

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

پلتفرم hosted Evals و Graders در OpenAI نیز در حال deprecation است؛ بنابراین datasetها، کد grader، rubricها و thresholdها را قابل‌حمل و داخل repository نگه دارید. برای evalهای hosted در OpenAI، evalهای موجود در **۳۱ اکتبر ۲۰۲۶** read-only می‌شوند و خاموشی کامل پلتفرم برای **۳۰ نوامبر ۲۰۲۶** برنامه‌ریزی شده است؛ این تاریخ‌ها را context پلتفرم OpenAI بدانید، نه نشانه availability در APIهای AvalAI.

!> **نکته migration endpoint:** بعضی مثال‌های grader در OpenAI از endpointهای hosted مثل `/v1/fine_tuning/alpha/graders/validate` یا `/v1/fine_tuning/alpha/graders/run` استفاده می‌کنند. تا وقتی AvalAI route میزبانی‌شده سازگار اعلام نکرده، این مثال‌ها را به `https://api.avalai.ir/v1/...` بازنویسی نکنید. در AvalAI امروز، graderها را با fixtureهای محلی در CI و روی خروجی‌های عادی مدل validate کنید.

## شکل اصلی

یک grader باید این ورودی‌ها را بگیرد:

- `item`: ردیف تست بازبینی‌شده توسط انسان؛ مثل prompt، پاسخ مرجع، JSON مورد انتظار یا tool call مورد انتظار.
- `sample`: خروجی مدلی که از `/v1/responses`، `/v1/chat/completions` یا route بومی provider تولید کرده‌اید.
- `score`: عددی بین `0` و `1`، همراه یک دلیل کوتاه برای debug کردن failure.

حتی در فایل‌های محلی از همان نام‌هایی استفاده کنید که OpenAI به کار می‌برد: `item.reference_answer`، `sample.output_text`، `sample.output_json` و `sample.output_tools`. اگر AvalAI بعدا eval میزبانی‌شده ارائه کند، migration ساده‌تر می‌شود.

## نقشه Migration از Graderهای Hosted OpenAI

وقتی محتوای grader در OpenAI را برای AvalAI تطبیق می‌دهید، مفهوم را نگه دارید اما سطح اجرای hosted را جایگزین کنید:

| مفهوم hosted در OpenAI | پیاده‌سازی امن فعلی در AvalAI |
| --- | --- |
| شیء JSON با نام `grader` | تابع Python/JavaScript نسخه‌دار یا assertion در Promptfoo. |
| `{{ item.reference_answer }}` | فیلد dataset از JSONL، CSV، YAML یا fixture تست. |
| `{{ sample.output_text }}` | متن normalizeشده از `output_text` در `/v1/responses` یا محتوای Chat Completions. |
| endpoint مربوط به `validate` | unit test که grader را روی fixtureهای pass/fail شناخته‌شده اجرا می‌کند. |
| endpoint مربوط به `run` | job در CI که با AvalAI sample تولید می‌کند و artifact امتیاز می‌نویسد. |
| URL گزارش hosted | گزارش Promptfoo، خروجی JSON/JUnit در pytest یا داشبورد observability خودتان. |

این الگو منطق امتیازدهی را قابل‌حمل نگه می‌دارد و releaseها را به API میزبانی‌شده‌ای که deprecated یا ناموجود است وابسته نمی‌کند.

## قرارداد Portable برای Sample

Templateهای grader در OpenAI فیلدهای dataset را از خروجی تولیدشده جدا می‌کنند. همین قرارداد را در فایل‌های محلی نگه دارید تا graderها قابل‌حمل بمانند:

- `item.*`: فیلدهای ردیف JSONL، مثل `item.ticket`، `item.correct_label`، `item.reference_answer` یا `item.expected_tool`.
- `sample.output_text`: متن normalizeشده از `response.output_text` یا `choices[0].message.content`.
- `sample.output_json`: خروجی ساختاریافته parseشده وقتی JSON یا پاسخ schema-constrained می‌خواهید.
- `sample.output_tools`: tool callها از آیتم‌های خروجی Responses یا `message.tool_calls` در Chat Completions.
- `sample.choices`: choices خام Chat Completions به‌صورت اختیاری برای debug کردن migration.
- `sample.output_audio`: metadata یا transcript اختیاری برای evalهای صوتی.

شیء normalizeشده `sample.*` را کوچک و پایدار نگه دارید. اگر audit log لازم دارید، پاسخ خام provider را جدا ذخیره کنید؛ اما grading را روی فیلدهای portable انجام دهید.

### متغیرهای Template و نوع‌های Grader

Templateهای grader در OpenAI از double brace مثل `{{ item.reference_answer }}` و `{{ sample.output_text }}` استفاده می‌کنند. همین دو namespace را محلی نگه دارید:

- `item.*` از ردیف dataset یا reference دارای label انسانی می‌آید.
- `sample.*` از خروجی تولیدشده‌ای می‌آید که grade می‌کنید.

taxonomy رسمی grader را به checkهای محلی map کنید:

- `string_check`: check دقیق یا substring پیاده کنید. operationهای کاربردی شامل `eq`، `neq`، `like` و `ilike` هستند.
- `text_similarity`: برای referenceهای open-ended از fuzzy، BLEU/GLEU، ROUGE، cosine یا similarity مبتنی بر embedding استفاده کنید.
- `score_model`: یک مدل judge ثابت در AvalAI را با rubric فراخوانی کنید و score عددی در بازه مشخص برگردانید.
- `python`: کد deterministic محلی برای قوانین کسب‌وکار، check عددی، تاریخ‌ها، فیلدهای schema-normalized یا امتیازدهی سفارشی اجرا کنید.
- `multi`: sub-scoreهای مستقل را با فرمول روشن مثل `(tool_name + arguments) / 2` ترکیب کنید.

## کوچک‌ترین Grader مناسب را انتخاب کنید

| Grader | مناسب برای | استفاده نکنید وقتی |
| --- | --- | --- |
| String check | label دقیق، شناسه، enum، عبارت الزامی | wording می‌تواند بدون تغییر correctness متفاوت باشد |
| JSON schema | استخراج ساختاریافته و argument ابزار | کیفیت معنایی پس از اعتبار schema مهم است |
| Text similarity | خلاصه، paraphrase و همپوشانی واژگانی جزئی | مقدار دقیق، شناسه یا مبلغ پول لازم است |
| LLM judge | کیفیت subjective، helpfulness، safety، style و partial credit | یک check قطعی می‌تواند رفتار را ثابت کند |
| Python سفارشی | قوانین کسب‌وکار، بازه عددی، تاریخ normalizeشده و امتیاز چندفیلدی | grader به network access یا secret نیاز دارد |
| Multi-grader | خروجی‌هایی که چند check مستقل می‌خواهند | یک failure باید کل ردیف را فورا fail کند |

با checkهای deterministic شروع کنید. LLM judge را فقط وقتی اضافه کنید که string، schema و business-rule grader کیفیت مورد نیاز را بیان نمی‌کنند.

## تولید Sample با AvalAI

تست‌های Chat Completions موجود را نگه دارید و برای مدل‌هایی که `/v1/responses` را پشتیبانی می‌کنند، نسخه Responses هم اضافه کنید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def classify_ticket_chat(ticket: str) -> str:
    response = client.chat.completions.create(
        model=os.getenv("AVALAI_EVAL_MODEL", "gpt-5.6-luna"),
        messages=[
            {
                "role": "developer",
                "content": "Classify the ticket as Hardware, Software, or Other. Return only the label.",
            },
            {"role": "user", "content": ticket},
        ],
        temperature=0,
    )
    return response.choices[0].message.content.strip()
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def classify_ticket_responses(ticket: str) -> str:
    response = client.responses.create(
        model=os.getenv("AVALAI_EVAL_MODEL", "gpt-5.6-luna"),
        instructions="Classify the ticket as Hardware, Software, or Other. Return only the label.",
        input=ticket,
        temperature=0,
    )
    return response.output_text.strip()
```

- `messages` → `input`
- policy مربوط به `developer` یا system → `instructions`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها، به‌جای فرض کردن یک خروجی متنی، آیتم‌های `response.output` را بررسی کنید.

</details>
<!-- responses-equivalent:end -->

## نمونه Grader محلی

Dataset را به‌صورت JSONL ذخیره کنید و sampleهای تولیدشده را در CI grade کنید:

```jsonl
{"item":{"ticket":"مانیتور من روشن نمی‌شود.","correct_label":"Hardware"}}
{"item":{"ticket":"کلاینت VPN بعد از login crash می‌کند.","correct_label":"Software"}}
{"item":{"ticket":"برای ناهار نزدیک دفتر پیشنهادی داری؟","correct_label":"Other"}}
```

```python
def normalize_label(value: str) -> str:
    return value.strip().lower().replace(".", "")


def grade_label(sample: dict, item: dict) -> dict:
    expected = normalize_label(item["correct_label"])
    actual = normalize_label(sample["output_text"])
    passed = actual == expected
    return {
        "score": 1.0 if passed else 0.0,
        "reason": (
            "exact label match" if passed else f"expected {expected}, got {actual}"
        ),
    }
```

برای tool callها، هم نام ابزار و هم argumentها را grade کنید. برای نام ابزار از check دقیق استفاده کنید و برای argumentهایی که چند شکل معادل دارند—مثل تاریخ، آدرس، currency یا unit normalizeشده—از schema یا semantic check کمک بگیرید.

## الگوی Tool Call و Multi-Grader

Eval مربوط به tool call معمولا بیش از یک امتیاز می‌خواهد. ابتدا بررسی کنید مدل ابزار درست را انتخاب کرده، سپس جداگانه بررسی کنید argumentها درست هستند یا نه.

```python
import json


def grade_tool_call(sample: dict, item: dict) -> dict:
    calls = sample.get("output_tools") or []
    if not calls:
        return {"score": 0.0, "reason": "no tool call"}

    call = calls[0].get("function", {})
    expected = item["expected_tool"]

    name_score = 1.0 if call.get("name") == expected["name"] else 0.0

    try:
        actual_args = json.loads(call.get("arguments") or "{}")
    except json.JSONDecodeError:
        actual_args = {}

    argument_score = 1.0 if actual_args == expected["arguments"] else 0.0
    score = 0.5 * name_score + 0.5 * argument_score
    return {
        "score": score,
        "reason": f"name={name_score}, arguments={argument_score}",
    }
```

مقایسه دقیق JSON برای ID و enum مفید است؛ اما ممکن است مقدارهای معادل مثل `1` و `1.0`، `CA` و `California`، یا فرمت‌های مختلف تاریخ را کم‌تر از حد واقعی امتیاز دهد. برای argumentهای انعطاف‌پذیر، ابتدا normalize کنید یا از grader معنایی استفاده کنید که فیلدهای parseشده را بررسی می‌کند.

## قواعد Python Grader محلی

کد grader را مثل کد تست production در نظر بگیرید:

- تابع `grade(sample, item)` را deterministic، version-controlled و همراه تغییر prompt یا model بازبینی کنید؛
- داخل graderهای CI اجازه network access، API key یا خواندن secret ندهید؛
- runtime و memory را محدود کنید تا یک sample بد کل suite را معطل نکند؛
- بسته به runner محلی، یک float معتبر یا شیء `{score, reason}` برگردانید؛
- fail-safe باشید: exception، فیلد گم‌شده، `NaN` یا score نامعتبر باید به `0.0` همراه دلیل debug تبدیل شود.

Python graderهای hosted در OpenAI محدودیت‌های sandbox مفیدی مستند می‌کنند: بدون network access، runtime محدود، memory/disk محدود و اندازه کوچک source آپلودشده. حتی وقتی از runtime hosted OpenAI استفاده نمی‌کنید، همین محدودیت‌ها را در CI بازتاب دهید تا grader به job پنهان production تبدیل نشود.

## راهنمای LLM Judge

وقتی کیفیت خروجی subjective است، از یک مدل AvalAI به‌عنوان judge استفاده کنید:

- پیش از استفاده در CI، judge را با مثال‌های دارای label انسانی calibrate کنید؛
- pass/fail یا pairwise comparison را به امتیاز مبهم `1–10` ترجیح دهید؛
- در pairwise testها ترتیب پاسخ‌ها را بچرخانید تا position bias کمتر شود؛
- طول پاسخ را کنترل کنید تا judge پاسخ طولانی‌تر را ترجیح ندهد؛
- مدل judge، prompt، temperature و rubric را برای هر release ثابت نگه دارید؛
- caseهای اختلاف و edge caseها را در dataset نگه دارید.

مراقب reward hacking باشید: اگر candidate امتیاز grader را بهتر می‌کند اما از نظر human reviewer بدتر است، پیش از ship کردن prompt، model یا tool change، grader را اصلاح کنید.

### چک‌های Reward Hacking

راهنمای grader در OpenAI روی «grader hacking» به‌عنوان یک failure mode تأکید می‌کند: سیستم candidate ممکن است یاد بگیرد قانون امتیازدهی را راضی کند، بدون اینکه task واقعی بهتر شود. کنار هر grader عملیاتی، یک بسته adversarial کوچک نگه دارید:

- **پاسخ‌های shortcut:** خروجی‌هایی که keywordهای rubric را تکرار می‌کنند اما task را حل نمی‌کنند.
- **پاسخ‌های prompt-injection:** خروجی‌هایی که از judge می‌خواهند rubric را نادیده بگیرد یا full credit بدهد.
- **پاسخ‌های بیش‌ازحد طولانی:** خروجی‌های verbose که مفید به نظر می‌رسند اما fact گمشده یا tool call ناامن را پنهان می‌کنند.
- **قبولی فقط با schema:** JSON معتبر که ID، تاریخ، مبلغ یا citation اشتباه دارد.
- **ردیف‌های اختلاف انسانی:** مثال‌هایی که reviewer انسانی پاسخ را رد کرده، هرچند score خودکار بالا بوده است.

اگر این caseها امتیاز خوبی می‌گیرند، threshold را صرفا پایین نیاورید. grader را دقیق‌تر کنید، قبل از LLM judge چک deterministic اضافه کنید، یا برای آن release gate review انسانی الزامی بگذارید.

### پیش از Block کردن CI کالیبره کنید

راهنمای grader در OpenAI توصیه می‌کند پیش از اعتماد به grader، خود grader را با رتبه‌بندی پاسخ‌های شناخته‌شده تست کنید. کنار هر LLM judge یا grader معنایی، یک calibration pack کوچک نگه دارید:

```json
{"id":"perfect","reference_answer":"Reset the API key from the dashboard.","candidate":"Reset the API key from the dashboard.","expected_order":1}
{"id":"partial","reference_answer":"Reset the API key from the dashboard.","candidate":"Open the dashboard and rotate credentials.","expected_order":2}
{"id":"wrong","reference_answer":"Reset the API key from the dashboard.","candidate":"Contact billing support for an invoice.","expected_order":3}
```

پیش از اینکه grader بتواند CI را fail کند، بررسی کنید که `perfect > partial > wrong` را رتبه‌بندی می‌کند، prompt-injection داخل پاسخ candidate را رد می‌کند و دلیل شکست را در فیلدی می‌نویسد که artifactهای CI نگه می‌دارند. هر وقت مدل judge، rubric، temperature، prompt یا محدودیت طول پاسخ تغییر کرد، این calibration را دوباره اجرا کنید.

## راهنماهای مرتبط

- [ارزیابی‌ها](fa/guides/evals.md)
- [ارزیابی گردش‌کارهای عامل‌محور](fa/guides/agent-evals.md)
- [مهندسی پرامپت](fa/guides/prompt-engineering.md)
- [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [فراخوانی تابع](fa/guides/function-calling.md)
- [راهنمای Graders در OpenAI](https://developers.openai.com/api/docs/guides/graders)
- [بهترین شیوه‌های Evaluation در OpenAI](https://developers.openai.com/api/docs/guides/evaluation-best-practices)
