# قالب‌بندی Citation

محصولات AI مبتنی بر منبع به citationهایی نیاز دارند که کاربر بتواند آن‌ها را بررسی کند. این راهنما الگوهای citation در مستندات OpenAI را برای برنامه‌های AvalAI که از `/v1/responses`، `/v1/chat/completions`، جستجوی وب یا RAG دستی استفاده می‌کنند، تطبیق می‌دهد.

!> citationهای ابزارهای hosted به route و مدل وابسته‌اند. وقتی AvalAI citationهای مدیریت‌شده توسط ارائه‌دهنده برمی‌گرداند، source IDهای برگشتی را حفظ کنید. برای retrieval دستی یا context تزریق‌شده، در برنامه خود source ID پایدار بسازید و از مدل بخواهید فقط همان IDها را cite کند.

## چه زمانی از Citation استفاده کنیم

وقتی پاسخ به محتوای retrieveشده، آپلودشده، جستجوشده یا دانش اختصاصی کسب‌وکار وابسته است، instructionهای citation اضافه کنید:

- دستیارهای RAG که از اسناد شما پاسخ می‌دهند.
- پاسخ‌های جستجوی وب که claimها باید به منبع برگردند.
- workflowهای compliance، حقوقی، پشتیبانی یا مالی که audit trail می‌خواهند.
- گزارش‌های طولانی که هر پاراگراف ممکن است به منابع متفاوت متکی باشد.

از مدل نخواهید برای راهنمایی عمومی، حافظه پشتیبانی‌نشده یا محتوایی که هرگز به مدل داده نشده citation بسازد.

## واحدهای قابل Citation را انتخاب کنید

پیش از نوشتن prompt مشخص کنید مدل دقیقا مجاز است چه چیزی را cite کند.

| واحد | مناسب برای | پیشنهاد AvalAI |
| --- | --- | --- |
| سند | provenance کلی | وقتی پشتیبانی در سطح صفحه کافی است. |
| بلوک / chunk | اکثر سیستم‌های RAG | انتخاب پیش‌فرض: پایدار، خوانا و به‌اندازه کافی دقیق. |
| بازه خط | audit و بررسی حقوقی | فقط وقتی retriever شما offset خط‌ها را قابل اعتماد ذخیره می‌کند. |

source IDها را در retryها پایدار نگه دارید. locatorهای UI را جدا ذخیره کنید: مدل باید `block_42` را خروجی دهد و برنامه شما آن ID را به URL، نام فایل، پاراگراف یا line highlight تبدیل کند.

**Source ID** و **locator** را دو مفهوم جدا در نظر بگیرید. Source ID همان token پایدار است که مدل خروجی می‌دهد، مثل `block_42` یا `turn0file1`. Locator شواهدی است که UI شما نمایش می‌دهد، مثل `L8-L13`، پاراگراف ۲۱، chunk هایلایت‌شده یا URL fragment. از مدل نخواهید locator بسازد مگر اینکه retriever همان locator را در همان درخواست فراهم کرده باشد.

## قالب Prompt

از قالب citation صریح و قابل parse استفاده کنید. OpenAI markerهای زیر را پیشنهاد می‌کند:

- `CITATION_START`: `\ue200`
- `CITATION_DELIMITER`: `\ue202`
- `CITATION_STOP`: `\ue201`
- خانواده citation: `cite`

برای context تزریق‌شده، به هر block یک ID بدهید و citation دقیق بخواهید:

```text
## Citations

The provided context contains citable blocks such as:
<BLOCK id="block_42"> ... </BLOCK>

Each block ID is a source reference. Cite only block IDs that appear in the provided context.

Write a citation as:
\ue200cite\ue202<block_id>\ue201

Rules:
- Place citations after punctuation.
- Do not place citations inside Markdown links, bold text, italics, or code fences.
- Do not write block IDs verbatim outside citation markers.
- Do not invent source IDs, URLs, titles, or line ranges.
- If the context does not support the answer, say what is missing instead of citing.
- If multiple blocks support a claim, cite each supporting block.
```

برای output مدیریت‌شده توسط ابزارهای provider، source IDهای برگشتی ابزار مثل `turn0file1`، `turn0url2` یا `turn1block0` را نگه دارید و از مدل بخواهید دقیقا همان IDها را cite کند.

از دو الگوی citation استفاده کنید:

- **Context برگشتی از ابزار:** IDها را دقیقا همان‌طور که ابزار برگردانده نگه دارید. اگر ابزار چند بار اجرا شود، پیشوند `turn#` ممکن است برای هر فراخوانی ابزار تغییر کند؛ بنابراین citationها را با IDهای برگشتی همان پاسخ validate کنید.
- **Context تزریق‌شده:** پیش از فراخوانی AvalAI، block ID پایدار بسازید. می‌توانید از ID ساده مثل `block_42` یا سبک `turn0block42` استفاده کنید؛ مهم این است که prompt و parser یک قالب ثابت داشته باشند.

اگر citation در سطح خط را پشتیبانی می‌کنید، locator را به marker اضافه کنید:

```text
\ue200cite\ue202turn0file1\ue202L8-L13\ue201
```

فقط زمانی line range بخواهید که context بازیابی‌شده یا تزریق‌شده از قبل شماره خط قابل اعتماد داشته باشد.

## Annotationهای ابزارهای Hosted

وقتی یک route در AvalAI annotationهای ابزار hosted سازگار با OpenAI برمی‌گرداند، همان annotation را منبع حقیقت برای render کردن بدانید. برای خروجی‌های web search و deep research، annotation نوع `url_citation` می‌تواند URL منبع، عنوان و span کاراکتری متن مرتبط را داشته باشد. در flowهای streaming، رویدادهایی مثل `response.output_text.annotation.added` را جمع‌آوری کنید و بعد از `response.output_text.done` یا `response.completed` به متن نهایی وصل کنید.

برای UX citation در سطح کاربر از این قرارداد نمایش استفاده کنید:

- citationهای web-search را نزدیک claim پشتیبانی‌شده، واضح و قابل کلیک نشان دهید.
- وقتی provider برمی‌گرداند، مقدارهای `url`، `title`، `start_index` و `end_index` را حفظ کنید.
- اگر نتیجه URL قابل استفاده ندارد، آن را context عادی ابزار بدانید و به‌جای link خالی، source ID پایدار خودتان را cite کنید.
- پیش از نمایش link، citationهای فایل و ارجاع artifactهای تولیدشده را با permission کاربر فعلی validate کنید.
- به نام منبعی که فقط در prose آمده اعتماد نکنید؛ render را از annotationها یا source IDهایی انجام دهید که در همان request ساخته‌اید.

## قواعد کیفیت Grounding

این قواعد را به promptهای RAG، web-search، compliance، حقوقی یا مالی پرریسک اضافه کنید:

- فقط sourceهایی را cite کنید که مستقیما همان جمله یا clause را پشتیبانی می‌کنند.
- برای claimهای حساس به زمان یا regulated، sourceهای معتبر و به‌روز را ترجیح دهید.
- وقتی پاسخ viewpointها، vendorها، policyها یا منطقه‌ها را مقایسه می‌کند، از sourceهای متنوع استفاده کنید.
- اگر sourceها اختلاف دارند، sourceهای متعارض را cite کنید و اختلاف را دقیق توضیح دهید؛ آن را پنهان یا هموار نکنید.
- citation، URL، عنوان، line range یا source ID اختراع نکنید؛ اگر پشتیبانی کافی نیست، بگویید چه چیزی کم است.

## مثال RAG دستی

```language-selector
python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

blocks = [
    {
        "id": "pricing_2026_block_3",
        "title": "Pricing Policy",
        "text": "Enterprise customers receive usage alerts at 80% and 100% of their monthly budget.",
    },
    {
        "id": "support_sla_block_8",
        "title": "Support SLA",
        "text": "Priority support tickets receive an initial response within four business hours.",
    },
]

context = "\n\n".join(
    f'<BLOCK id="{block["id"]}" title="{block["title"]}">\n{block["text"]}\n</BLOCK>'
    for block in blocks
)

instructions = """Answer only from the citable blocks.
Use citations in the format \\ue200cite\\ue202<block_id>\\ue201.
Place citations after punctuation. Never invent block IDs."""

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions=instructions,
    input=[
        {"role": "developer", "content": f"Citable context:\n{context}"},
        {"role": "user", "content": "When do enterprise customers get budget alerts?"},
    ],
    store=False,
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const blocks = [
  {
    id: "pricing_2026_block_3",
    title: "Pricing Policy",
    text: "Enterprise customers receive usage alerts at 80% and 100% of their monthly budget.",
  },
  {
    id: "support_sla_block_8",
    title: "Support SLA",
    text: "Priority support tickets receive an initial response within four business hours.",
  },
];

const context = blocks
  .map((block) => `<BLOCK id="${block.id}" title="${block.title}">\n${block.text}\n</BLOCK>`)
  .join("\n\n");

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions:
    "Answer only from the citable blocks. Use citations in the format \\ue200cite\\ue202<block_id>\\ue201. Place citations after punctuation. Never invent block IDs.",
  input: [
    { role: "developer", content: `Citable context:\n${context}` },
    { role: "user", content: "When do enterprise customers get budget alerts?" },
  ],
  store: false,
});

console.log(response.output_text);

```

برای Chat Completions قدیمی، همین instructionها را در پیام `developer` یا `system` بگذارید و blockهای قابل citation را در یک پیام جدا قبل از سؤال کاربر ارسال کنید.

## Parse و Render کردن Citationها

پیش از نمایش پاسخ، خروجی مدل را post-process کنید. source IDها را در پایگاه داده خود resolve کنید و marker خام را با link، footnote یا chipهای inline جایگزین کنید. Parser باید citationهای تک‌منبعی، چند منبع پشتیبان و locatorهای اختیاری مثل line range را پشتیبانی کند.

```language-selector
python=:import re

CITATION_START = "\ue200"
CITATION_DELIMITER = "\ue202"
CITATION_STOP = "\ue201"

SOURCE_ID_RE = re.compile(r"^[A-Za-z0-9_-]+$")
LINE_LOCATOR_RE = re.compile(r"^L\d+(?:-L\d+)?$")

TOKEN_RE = re.compile(
    re.escape(CITATION_START)
    + r"cite"
    + re.escape(CITATION_DELIMITER)
    + r"(.*?)"
    + re.escape(CITATION_STOP),
    re.DOTALL,
)


def extract_citations(text):
    citations = []

    def replace(match):
        parts = [
            part.strip()
            for part in match.group(1).split(CITATION_DELIMITER)
            if part.strip()
        ]
        if not parts:
            return ""

        locator = None
        if LINE_LOCATOR_RE.fullmatch(parts[-1]):
            locator = parts.pop()

        if not parts or any(not SOURCE_ID_RE.fullmatch(part) for part in parts):
            return ""

        citations.append(
            {
                "source_ids": parts,
                "locator": locator,
                "start": match.start(),
                "end": match.end(),
            }
        )
        return ""

    clean_text = TOKEN_RE.sub(replace, text).strip()
    return clean_text, citations


answer, citations = extract_citations(
    "Budget alerts are sent at 80% and 100%. \ue200cite\ue202pricing_2026_block_3\ue202support_sla_block_8\ue201"
)

print(answer)
print(citations)

javascript=:const CITATION_START = "\ue200";
const CITATION_DELIMITER = "\ue202";
const CITATION_STOP = "\ue201";
const sourceIdRe = /^[A-Za-z0-9_-]+$/;
const lineLocatorRe = /^L\d+(?:-L\d+)?$/;

function escapeRegExp(value) {
  return value.replace(/[.*+?^${}()|[\]\\]/g, "\\$&");
}

const citationRe = new RegExp(
  `${escapeRegExp(CITATION_START)}cite${escapeRegExp(CITATION_DELIMITER)}` +
    `([\\s\\S]*?)` +
    `${escapeRegExp(CITATION_STOP)}`,
  "g"
);

function extractCitations(text) {
  const citations = [];
  const cleanText = text
    .replace(citationRe, (raw, body, offset) => {
      const parts = body
        .split(CITATION_DELIMITER)
        .map((part) => part.trim())
        .filter(Boolean);

      if (parts.length === 0) {
        return "";
      }

      let locator = null;
      if (lineLocatorRe.test(parts[parts.length - 1])) {
        locator = parts.pop();
      }

      if (parts.length === 0 || parts.some((part) => !sourceIdRe.test(part))) {
        return "";
      }

      citations.push({
        sourceIds: parts,
        locator,
        start: offset,
        end: offset + raw.length,
      });
      return "";
    })
    .trim();

  return { cleanText, citations };
}

console.log(
  extractCitations("Budget alerts are sent at 80% and 100%. \ue200cite\ue202pricing_2026_block_3\ue202support_sla_block_8\ue201")
);

```

## چک‌لیست Production

- همراه هر block retrieveشده، `source_id`، عنوان، URL/file ID، متن chunk و line range اختیاری را ذخیره کنید.
- citation IDها، markerهای چندمنبعی و locatorها را با blockهایی که در همان request داده‌اید validate کنید.
- citationهای malformed را پیش از render کردن reject یا repair کنید؛ هرگز marker خام `\ue200...\ue201` را به کاربر نهایی نشان ندهید.
- markerهای خام citation را پیش از برگشت محتوا به کاربر حذف یا render کنید.
- متن نهایی پاسخ، source IDهای انتخاب‌شده و locatorهای renderشده را برای audit لاگ کنید.
- citation را evidence برای grounding بدانید، نه کنترل دسترسی؛ بررسی tenant و permission باید در لایه retrieval انجام شود.

## منابع مرتبط

- [مرجع API پاسخ‌ها](/fa/api-reference/responses.md)
- [ابزار جستجوی وب](/fa/guides/tools-web-search.md)
- [ابزار File Search](/fa/guides/tools-file-search.md)
- [راهنمای Retrieval](/fa/guides/retrieval.md)
- [RAG دستی با Embeddings](/fa/examples/manual_rag_with_embeddings.md)
