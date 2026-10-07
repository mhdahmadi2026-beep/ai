# پردازش فایل‌های اکسل با API AvalAI

## مقدمه

API AvalAI قابلیت‌های قدرتمندی برای پردازش صفحات گسترده اکسل (فایل‌های XLS و XLSX) با استفاده از مدل‌های زبانی پیشرفته ارائه می‌دهد. این راهنما نشان می‌دهد چگونه می‌توانید از مدل‌های OpenAI، Anthropic (Claude) و Gemini از طریق API سازگار AvalAI برای تحلیل، استخراج اطلاعات و تعامل با داده‌های صفحات گسترده استفاده کنید. این قابلیت‌ها به برنامه‌ها امکان می‌دهد تا داده‌های جدولی را درک و با آنها کار کنند، که آنها را برای تحلیل داده‌ها، استخراج اطلاعات و جریان‌های کاری خودکار پردازش داده ایده‌آل می‌سازد.

> این راهنما از مقاله [How to query CSV and Excel files using LangChain](https://medium.com/@satyadeepbehera_8504/how-to-query-csv-and-excel-files-using-langchain-d8f1ae0e5cc8) الهام گرفته شده است، با تغییراتی برای پیاده‌سازی AvalAI.

## ویژگی‌های کلیدی

- **درک داده‌های جدولی** - پردازش داده‌های ساختاریافته در فرمت‌های صفحات گسترده
- **تحلیل نمودار و جدول** - استخراج و تفسیر داده‌ها از جداول و نمودارها
- **خلاصه‌سازی داده‌ها** - تولید خلاصه‌های مختصر از محتوای صفحات گسترده
- **استخراج اطلاعات** - استخراج اطلاعات خاص از صفحات گسترده به فرمت‌های ساختاریافته
- **پاسخ به سؤالات** - پرسیدن سؤالات درباره داده‌های صفحات گسترده و دریافت پاسخ‌های دقیق
- **تبدیل داده‌ها** - تبدیل و دستکاری داده‌های صفحات گسترده
- **دسترسی یکپارچه به API** - دسترسی به چندین ارائه دهنده مدل از طریق یک رابط سازگار

## مدل‌های موجود

مدل‌های زیر از پردازش فایل‌های اکسل/صفحات گسترده از طریق API AvalAI پشتیبانی می‌کنند:

### مدل‌های OpenAI

- **gpt-5.5** - مدل پیشرفته با قابلیت‌های قوی درک داده‌ها
- **gpt-5.4** - مدل کارآمدتر برای پردازش داده‌ها
- **gpt-5.4-mini** - مدل قدرتمند با قابلیت‌های عالی تحلیل داده‌ها

### مدل‌های Anthropic (Claude)

- **claude-opus-4-7** - مدل پیشرفته با قابلیت‌های قوی درک داده‌ها
- **claude-sonnet-4-6** - جدیدترین نسخه با پردازش داده‌های بهبود یافته
- **claude-haiku-4-5** - مدل کارآمدتر برای پردازش داده‌ها

### مدل‌های Gemini

- **gemini-3.1-pro-preview** - پیشرفته‌ترین مدل با درک بهبود یافته داده‌ها
- **gemini-3.5-flash** - مدل چندوجهی سریع برای پردازش داده‌ها
- **gemini-2.5-pro** - مدل با درک بهبود یافته داده‌ها
- **gemini-2.5-flash** - مدل برای پردازش داده‌ها

## استفاده پایه

دو رویکرد اصلی برای پردازش فایل‌های اکسل با API AvalAI وجود دارد:

1. **رویکرد گردش کار ساده**: تبدیل داده‌های اکسل به متن و ارسال آن به مدل
2. **رویکرد عامل CSV Langchain**: استفاده از عامل‌های تخصصی برای تحلیل پیشرفته‌تر داده‌ها

### رویکرد گردش کار ساده

این رویکرد برای فایل‌های کوچک‌تر که می‌توانند در پنجره زمینه مدل قرار گیرند، بهترین است. شامل تبدیل فایل اکسل به یک نمایش متنی و ارسال آن به مدل می‌شود.

#### پردازش اکسل با کدگذاری base64

می‌توانید فایل‌های اکسل را مستقیما به صورت base64 کدگذاری کرده و به API ارسال کنید:

```python
from openai import OpenAI
import base64
import pandas as pd
from io import BytesIO

# مقداردهی اولیه کلاینت با API AvalAI
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# روش 1: از یک فایل محلی
with open("path/to/your/spreadsheet.xlsx", "rb") as f:
    file_data = f.read()

# کدگذاری داده اکسل به base64
encoded_file = base64.b64encode(file_data).decode("utf-8")
base64_url = f"data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,{encoded_file}"

# ایجاد درخواست با فایل کدگذاری شده با base64
file_content = [
    {
        "type": "text",
        "text": "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید.",
    },
    {
        "type": "file",
        "file": {
            "file_data": base64_url,
        },
    },
]

# ارسال درخواست به مدل
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

// مقداردهی اولیه کلاینت با API AvalAI
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تابع دریافت فایل اکسل کدگذاری شده با base64
async function getBase64Excel() {
  // از یک فایل محلی
  const buffer = fs.readFileSync("path/to/your/spreadsheet.xlsx");
  return `data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,${buffer.toString("base64")}`;
}

// تابع اصلی
async function processExcel() {
  const base64Excel = await getBase64Excel();

  // ایجاد درخواست با فایل کدگذاری شده با base64
  const fileContent = [
    {
      type: "text",
      text: "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید.",
    },
    {
      type: "file",
      file: {
        file_data: base64Excel,
      },
    },
  ];

  // ارسال درخواست به مدل
  const response = await client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: fileContent }],
  });

  console.log(response.choices[0].message.content);
}

processExcel();

```

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	openai "github.com/openai/openai-go"
	"io/ioutil"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// دریافت داده اکسل
	excelData, err := getExcelData()
	if err != nil {
		fmt.Printf("خطا در دریافت داده اکسل: %v\n", err)
		return
	}

	// کدگذاری داده اکسل به base64
	encodedFile := base64.StdEncoding.EncodeToString(excelData)
	base64URL := fmt.Sprintf("data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,%s", encodedFile)

	// ایجاد درخواست با فایل کدگذاری شده با base64
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileData: base64URL,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا در ChatCompletion: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع دریافت داده اکسل از فایل محلی
func getExcelData() ([]byte, error) {
	// از یک فایل محلی
	return ioutil.ReadFile("path/to/your/spreadsheet.xlsx")
}

```

```php
<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
$client = OpenAI::client('your-avalai-api-key', [
	'base_url' => 'https://api.avalai.ir/v1'
]);

// تابع دریافت فایل اکسل کدگذاری شده با base64
function getBase64Excel() {
	// از یک فایل محلی
	$fileData = file_get_contents("path/to/your/spreadsheet.xlsx");
	return "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64," . base64_encode($fileData);
}

// دریافت فایل اکسل کدگذاری شده با base64
$base64Excel = getBase64Excel();

// ایجاد درخواست با فایل کدگذاری شده با base64
$fileContent = [
	[
		"type" => "text",
		"text" => "این صفحه گسترده را تحلیل کرده و بینش‌های کلیدی ارائه دهید."
	],
	[
		"type" => "file",
		"file" => [
			"file_data" => $base64Excel
		]
	]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
	'model' => 'gpt-5.6-luna',
	'messages' => [
		[
			'role' => 'user',
			'content' => $fileContent
		]
	]
]);

echo $completion->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Summarize the uploaded file."},
                {"type": "input_file", "file_id": "file_abc123"},
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Summarize the uploaded file." },
        { type: "input_file", file_id: "file_abc123" },
      ],
    },
  ],
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Summarize the uploaded file."
          },
          {
            "type": "input_file",
            "file_id": "file_abc123"
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


#### تبدیل DataFrame

برای کنترل بیشتر روی داده‌ها، می‌توانید فایل‌های اکسل را به یک DataFrame پانداس و سپس به یک نمایش متنی تبدیل کنید:

```python
from openai import OpenAI
import pandas as pd

# مقداردهی اولیه کلاینت با API AvalAI
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# بارگذاری فایل اکسل به DataFrame پانداس
df = pd.read_excel("path/to/your/spreadsheet.xlsx")

# تبدیل DataFrame به نمایش رشته‌ای
df_string = df.to_string()

# ایجاد یک پرامپت با رشته DataFrame
prompt = f"""
من داده‌های صفحه گسترده زیر را دارم:

{df_string}

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
"""

# ارسال درخواست به مدل
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import * as XLSX from "xlsx";

// مقداردهی اولیه کلاینت با API AvalAI
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تابع تبدیل اکسل به نمایش متنی
function excelToText(filePath) {
  // خواندن فایل اکسل
  const workbook = XLSX.readFile(filePath);

  // دریافت اولین کاربرگ
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];

  // تبدیل به JSON
  const jsonData = XLSX.utils.sheet_to_json(worksheet);

  // تبدیل به نمایش رشته‌ای
  const headers = Object.keys(jsonData[0]);
  let textRepresentation = headers.join("\t") + "\n";

  jsonData.forEach((row) => {
    textRepresentation +=
      headers.map((header) => row[header]).join("\t") + "\n";
  });

  return textRepresentation;
}

async function analyzeExcel() {
  // دریافت نمایش متنی فایل اکسل
  const excelText = excelToText("path/to/your/spreadsheet.xlsx");

  // ایجاد پرامپت با داده‌های اکسل
  const prompt = `
من داده‌های صفحه گسترده زیر را دارم:

${excelText}

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
`;

  // ارسال درخواست به مدل
  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [{ role: "user", content: prompt }],
  });

  console.log(response.choices[0].message.content);
}

analyzeExcel();

```

```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"github.com/xuri/excelize/v2"
	"os"
	"strings"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// تبدیل اکسل به نمایش متنی
	excelText, err := excelToText("path/to/your/spreadsheet.xlsx")
	if err != nil {
		fmt.Printf("خطا در تبدیل اکسل: %v\n", err)
		return
	}

	// ایجاد پرامپت با داده‌های اکسل
	prompt := fmt.Sprintf(`
من داده‌های صفحه گسترده زیر را دارم:

%s

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
`, excelText)

	// ارسال درخواست به مدل
	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-4-6",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: prompt,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا در ChatCompletion: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع تبدیل اکسل به نمایش متنی
func excelToText(filePath string) (string, error) {
	// باز کردن فایل اکسل
	f, err := excelize.OpenFile(filePath)
	if err != nil {
		return "", err
	}
	defer f.Close()

	// دریافت همه نام‌های کاربرگ
	sheets := f.GetSheetList()
	if len(sheets) == 0 {
		return "", fmt.Errorf("هیچ کاربرگی یافت نشد")
	}

	// دریافت همه سطرها از اولین کاربرگ
	rows, err := f.GetRows(sheets[0])
	if err != nil {
		return "", err
	}

	// تبدیل به نمایش متنی
	var sb strings.Builder
	for _, row := range rows {
		sb.WriteString(strings.Join(row, "\t"))
		sb.WriteString("\n")
	}

	return sb.String(), nil
}

```

```php
<?php

require 'vendor/autoload.php';
use PhpOffice\PhpSpreadsheet\IOFactory;

// مقداردهی اولیه کلاینت با API AvalAI
$client = OpenAI::client('your-avalai-api-key', [
	'base_url' => 'https://api.avalai.ir/v1'
]);

// تابع تبدیل اکسل به نمایش متنی
function excelToText($filePath) {
	// بارگذاری فایل اکسل
	$spreadsheet = IOFactory::load($filePath);
	$worksheet = $spreadsheet->getActiveSheet();

	// دریافت بالاترین سطر و ستون
	$highestRow = $worksheet->getHighestRow();
	$highestColumn = $worksheet->getHighestColumn();

	// تبدیل به نمایش متنی
	$textRepresentation = '';
	for ($row = 1; $row <= $highestRow; $row++) {
		$rowData = [];
		for ($col = 'A'; $col <= $highestColumn; $col++) {
			$rowData[] = $worksheet->getCell($col . $row)->getValue();
		}
		$textRepresentation .= implode("\t", $rowData) . "\n";
	}

	return $textRepresentation;
}

// دریافت نمایش متنی فایل اکسل
$excelText = excelToText("path/to/your/spreadsheet.xlsx");

// ایجاد پرامپت با داده‌های اکسل
$prompt = "
من داده‌های صفحه گسترده زیر را دارم:

$excelText

لطفا این داده‌ها را تحلیل کرده و بینش‌های کلیدی ارائه دهید.
";

// ارسال درخواست به مدل
$completion = $client->chat()->create([
	'model' => 'claude-sonnet-4-6',
	'messages' => [
		[
			'role' => 'user',
			'content' => $prompt
		]
	]
]);

echo $completion->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Summarize the uploaded file.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "Summarize the uploaded file.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Summarize the uploaded file.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### رویکرد عامل CSV Langchain

برای تحلیل پیشرفته‌تر، به‌ویژه با فایل‌های بزرگ‌تر، می‌توانید از عامل CSV Langchain استفاده کنید. این رویکرد قابلیت‌های تحلیل داده پیشرفته‌تری را با اجازه دادن به مدل برای اجرای کد پایتون برای تحلیل داده‌ها فراهم می‌کند.

#### ایجاد عامل CSV

```python
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
import os

# تنظیم کلید API شما
os.environ["AVALAI_API_KEY"] = "your-avalai-api-key"
os.environ["OPENAI_BASE_URL"] = "https://api.avalai.ir/v1"

# مقداردهی اولیه مدل زبانی
llm = ChatOpenAI(model="gpt-5.6-luna", temperature=0)

# ایجاد عامل CSV
agent_executor = create_csv_agent(
    llm,
    "path/to/your/spreadsheet.xlsx",  # با هر دو فایل CSV و اکسل کار می‌کند
    agent_type="openai-tools",
    verbose=True,
)

# پرسیدن سؤالات درباره داده‌ها
response = agent_executor.invoke({"input": "۵ مقدار برتر در ستون فروش چیست؟"})

print(response["output"])

# پرسیدن سؤال دیگر
response = agent_executor.invoke(
    {"input": "میانگین مقدار برای هر دسته را محاسبه کرده و خلاصه‌ای ایجاد کنید."}
)

print(response["output"])

```

```javascript
// پیاده‌سازی جاوااسکریپت با استفاده از LangChain.js
import { ChatOpenAI } from "@langchain/openai";
import { createCSVAgent } from "langchain/agents";
import dotenv from "dotenv";

// بارگذاری متغیرهای محیطی
dotenv.config();

// تنظیم کلید API شما
process.env.AVALAI_API_KEY = "your-avalai-api-key";
process.env.OPENAI_BASE_URL = "https://api.avalai.ir/v1";

// مقداردهی اولیه مدل زبانی
const llm = new ChatOpenAI({
  modelName: "gpt-5.6-luna",
  temperature: 0,
});

async function runCSVAgent() {
  // ایجاد عامل CSV
  const agentExecutor = await createCSVAgent({
    llm,
    path: "path/to/your/spreadsheet.xlsx", // با هر دو فایل CSV و اکسل کار می‌کند
    agentType: "openai-tools",
    verbose: true,
  });

  // پرسیدن سؤالات درباره داده‌ها
  const response1 = await agentExecutor.invoke({
    input: "۵ مقدار برتر در ستون فروش چیست؟",
  });

  console.log(response1.output);

  // پرسیدن سؤال دیگر
  const response2 = await agentExecutor.invoke({
    input: "میانگین مقدار برای هر دسته را محاسبه کرده و خلاصه‌ای ایجاد کنید.",
  });

  console.log(response2.output);
}

runCSVAgent();

```


#### ایجاد عامل DataFrame پانداس

برای تحلیل داده‌های حتی پیشرفته‌تر، می‌توانید از عامل DataFrame پانداس استفاده کنید:

```python
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
import os

# تنظیم کلید API شما
os.environ["AVALAI_API_KEY"] = "your-avalai-api-key"
os.environ["OPENAI_BASE_URL"] = "https://api.avalai.ir/v1"

# بارگذاری فایل اکسل
df = pd.read_excel("path/to/your/spreadsheet.xlsx")

# مقداردهی اولیه مدل زبانی
llm = ChatOpenAI(model="gpt-5.6-luna", temperature=0)

# ایجاد عامل DataFrame پانداس
agent_executor = create_pandas_dataframe_agent(
    llm,
    df,
    agent_type="tool-calling",  # استفاده از نوع عامل tool-calling جدیدتر
    verbose=True,
    allow_dangerous_code=True,  # فقط در محیط‌های مورد اعتماد فعال کنید
)

# پرسیدن سؤالات تحلیل داده پیچیده
response = agent_executor.invoke(
    {
        "input": "خلاصه‌ای از داده‌ها، شامل آمارهای کلیدی و هرگونه روند قابل توجه ایجاد کنید."
    }
)

print(response["output"])

# درخواست کد نمایش داده
response = agent_executor.invoke(
    {
        "input": "کد پایتون برای ایجاد نمودار میله‌ای از ۵ دسته برتر بر اساس درآمد تولید کنید."
    }
)

print(response["output"])

```

```javascript
// پیاده‌سازی جاوااسکریپت با استفاده از LangChain.js
import { ChatOpenAI } from "@langchain/openai";
import { createPandasDataFrameAgent } from "langchain/agents";
import { readFile } from "fs/promises";
import * as XLSX from "xlsx";
import dotenv from "dotenv";

// بارگذاری متغیرهای محیطی
dotenv.config();

// تنظیم کلید API شما
process.env.AVALAI_API_KEY = "your-avalai-api-key";
process.env.OPENAI_BASE_URL = "https://api.avalai.ir/v1";

async function loadExcelAsDataFrame(filePath) {
  // این یک نسخه ساده شده است - در یک پیاده‌سازی واقعی،
  // شما باید داده‌های اکسل را به فرمتی تبدیل کنید
  // که عامل DataFrame بتواند با آن کار کند
  const workbook = XLSX.readFile(filePath);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  const jsonData = XLSX.utils.sheet_to_json(worksheet);
  return jsonData;
}

async function runPandasAgent() {
  // بارگذاری فایل اکسل
  const df = await loadExcelAsDataFrame("path/to/your/spreadsheet.xlsx");

  // مقداردهی اولیه مدل زبانی
  const llm = new ChatOpenAI({
    modelName: "gpt-5.6-luna",
    temperature: 0,
  });

  // ایجاد عامل DataFrame پانداس
  const agentExecutor = await createPandasDataFrameAgent({
    llm,
    df,
    agentType: "tool-calling",
    verbose: true,
  });

  // پرسیدن سؤالات تحلیل داده پیچیده
  const response1 = await agentExecutor.invoke({
    input:
      "خلاصه‌ای از داده‌ها، شامل آمارهای کلیدی و هرگونه روند قابل توجه ایجاد کنید.",
  });

  console.log(response1.output);

  // درخواست کد نمایش داده
  const response2 = await agentExecutor.invoke({
    input:
      "کدی برای ایجاد نمودار میله‌ای از ۵ دسته برتر بر اساس درآمد تولید کنید.",
  });

  console.log(response2.output);
}

runPandasAgent();

```


## استفاده از ارائه‌دهندگان مدل مختلف

می‌توانید از هر یک از مدل‌های پشتیبانی شده با تغییر پارامتر مدل در درخواست‌های خود استفاده کنید:

### مثال OpenAI

```python
response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": prompt}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مثال Anthropic (Claude)

```python
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": prompt}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مثال Gemini

```python
response = client.chat.completions.create(
    model="gemini-2.5-pro",
    messages=[{"role": "user", "content": prompt}],
)
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-pro` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## محدودیت‌های خاص مدل‌ها

### مدل‌های OpenAI

- **حداکثر اندازه فایل**: ۲۵ مگابایت در هر درخواست
- **مصرف توکن**: بسته به مدل متفاوت است، معمولا ۱-۳ توکن به ازای هر سلول
- **عناصر تصویری**: می‌تواند نمودارها و عناصر تصویری در صفحات گسترده را تحلیل کند
- **بهترین کاربرد برای**: تحلیل داده عمومی، تشخیص الگو و خلاصه‌سازی

### مدل‌های Anthropic (Claude)

- **حداکثر اندازه فایل**: ۳۲ مگابایت در هر درخواست
- **مصرف توکن**: معمولا ۱-۲ توکن به ازای هر سلول بسته به محتوا
- **عناصر تصویری**: می‌تواند نمودارها و جداول در صفحات گسترده را تحلیل کند
- **بهترین کاربرد برای**: تحلیل داده دقیق، وظایف پیچیده درک سند

### مدل‌های Gemini

- **حداکثر اندازه فایل**: ۲۰ مگابایت برای آپلودهای مستقیم
- **مصرف توکن**: تقریبا ۱ توکن به ازای هر سلول
- **عناصر تصویری**: قابلیت‌های قوی برای تحلیل محتوای تصویری در صفحات گسترده
- **بهترین کاربرد برای**: پردازش صفحات گسترده بزرگ، تحلیل محتوای تصویری

## موارد استفاده

### تحلیل داده

```python
from openai import OpenAI
import pandas as pd

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# بارگذاری فایل اکسل به DataFrame پانداس
df = pd.read_excel("sales_data.xlsx")

# تبدیل DataFrame به نمایش رشته‌ای
df_string = df.to_string()

prompt = f"""
من داده‌های فروش زیر را دارم:

{df_string}

لطفا این داده‌ها را تحلیل کرده و موارد زیر را ارائه دهید:
1. روندهای فروش ماهانه
2. محصولات با عملکرد برتر
3. مناطق با بیشترین رشد
4. هرگونه ناهنجاری یا داده پرت
"""

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import * as XLSX from "xlsx";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تابع تبدیل اکسل به نمایش متنی
function excelToText(filePath) {
  const workbook = XLSX.readFile(filePath);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  const jsonData = XLSX.utils.sheet_to_json(worksheet);

  // تبدیل به نمایش رشته‌ای
  const headers = Object.keys(jsonData[0]);
  let textRepresentation = headers.join("\t") + "\n";

  jsonData.forEach((row) => {
    textRepresentation +=
      headers.map((header) => row[header]).join("\t") + "\n";
  });

  return textRepresentation;
}

async function analyzeSalesData() {
  const excelText = excelToText("sales_data.xlsx");

  const prompt = `
من داده‌های فروش زیر را دارم:

${excelText}

لطفا این داده‌ها را تحلیل کرده و موارد زیر را ارائه دهید:
1. روندهای فروش ماهانه
2. محصولات با عملکرد برتر
3. مناطق با بیشترین رشد
4. هرگونه ناهنجاری یا داده پرت
`;

  const response = await client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: prompt }],
  });

  console.log(response.choices[0].message.content);
}

analyzeSalesData();

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Summarize the uploaded file.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "Summarize the uploaded file.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Summarize the uploaded file.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### خلاصه‌سازی داده‌ها

```python
from openai import OpenAI
import pandas as pd

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# بارگذاری فایل اکسل به DataFrame پانداس
df = pd.read_excel("financial_report.xlsx")

# تبدیل DataFrame به نمایش رشته‌ای
df_string = df.to_string()

prompt = f"""
من داده‌های مالی زیر را دارم:

{df_string}

لطفا یک خلاصه اجرایی مختصر از این گزارش مالی ارائه دهید که موارد زیر را برجسته کند:
1. سلامت مالی کلی
2. معیارهای کلیدی و عملکرد آنها
3. حوزه‌های نگرانی
4. توصیه‌هایی برای بهبود
"""

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[{"role": "user", "content": prompt}],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import * as XLSX from "xlsx";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تابع تبدیل اکسل به نمایش متنی
function excelToText(filePath) {
  const workbook = XLSX.readFile(filePath);
  const sheetName = workbook.SheetNames[0];
  const worksheet = workbook.Sheets[sheetName];
  const jsonData = XLSX.utils.sheet_to_json(worksheet);

  // تبدیل به نمایش رشته‌ای
  const headers = Object.keys(jsonData[0]);
  let textRepresentation = headers.join("\t") + "\n";

  jsonData.forEach((row) => {
    textRepresentation +=
      headers.map((header) => row[header]).join("\t") + "\n";
  });

  return textRepresentation;
}

async function summarizeFinancialReport() {
  const excelText = excelToText("financial_report.xlsx");

  const prompt = `
من داده‌های مالی زیر را دارم:

${excelText}

لطفا یک خلاصه اجرایی مختصر از این گزارش مالی ارائه دهید که موارد زیر را برجسته کند:
1. سلامت مالی کلی
2. معیارهای کلیدی و عملکرد آنها
3. حوزه‌های نگرانی
4. توصیه‌هایی برای بهبود
`;

  const response = await client.chat.completions.create({
    model: "claude-sonnet-4-6",
    messages: [{ role: "user", content: prompt }],
  });

  console.log(response.choices[0].message.content);
}

summarizeFinancialReport();

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="Summarize the uploaded file.",
)

print(response.output_text)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "Summarize the uploaded file.",
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Summarize the uploaded file.",
    "instructions": "You are a helpful assistant."
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پاسخ به سؤالات

```python
from langchain_openai import ChatOpenAI
from langchain_experimental.agents import create_csv_agent
import os

# تنظیم کلید API شما
os.environ["AVALAI_API_KEY"] = "your-avalai-api-key"
os.environ["OPENAI_BASE_URL"] = "https://api.avalai.ir/v1"

# مقداردهی اولیه مدل زبانی
llm = ChatOpenAI(model="gemini-2.5-pro", temperature=0)

# ایجاد عامل CSV
agent_executor = create_csv_agent(
    llm, "inventory_data.xlsx", agent_type="openai-tools", verbose=True
)

# پرسیدن سؤالات خاص درباره موجودی
questions = [
    "چند واحد از محصول XYZ در حال حاضر در انبار موجود است؟",
    "کدام انبار کمترین سطح موجودی را دارد؟",
    "ارزش کل همه موجودی چقدر است؟",
    "کدام محصولات به زودی نیاز به تجدید موجودی دارند (کمتر از ۱۰ واحد باقی مانده)؟",
    "سطوح موجودی بین سه‌ماهه اول و دوم را مقایسه کنید.",
]

for question in questions:
    response = agent_executor.invoke({"input": question})
    print(f"سؤال: {question}")
    print(f"پاسخ: {response['output']}")
    print("---")

```

```javascript
// پیاده‌سازی جاوااسکریپت با استفاده از LangChain.js
import { ChatOpenAI } from "@langchain/openai";
import { createCSVAgent } from "langchain/agents";
import dotenv from "dotenv";

// بارگذاری متغیرهای محیطی
dotenv.config();

// تنظیم کلید API شما
process.env.AVALAI_API_KEY = "your-avalai-api-key";
process.env.OPENAI_BASE_URL = "https://api.avalai.ir/v1";

async function askInventoryQuestions() {
  // مقداردهی اولیه مدل زبانی
  const llm = new ChatOpenAI({
    modelName: "gemini-2.5-pro",
    temperature: 0,
  });

  // ایجاد عامل CSV
  const agentExecutor = await createCSVAgent({
    llm,
    path: "inventory_data.xlsx",
    agentType: "openai-tools",
    verbose: true,
  });

  // پرسیدن سؤالات خاص درباره موجودی
  const questions = [
    "چند واحد از محصول XYZ در حال حاضر در انبار موجود است؟",
    "کدام انبار کمترین سطح موجودی را دارد؟",
    "ارزش کل همه موجودی چقدر است؟",
    "کدام محصولات به زودی نیاز به تجدید موجودی دارند (کمتر از ۱۰ واحد باقی مانده)؟",
    "سطوح موجودی بین سه‌ماهه اول و دوم را مقایسه کنید.",
  ];

  for (const question of questions) {
    const response = await agentExecutor.invoke({ input: question });
    console.log(`سؤال: ${question}`);
    console.log(`پاسخ: ${response.output}`);
    console.log("---");
  }
}

askInventoryQuestions();

```


## بهترین شیوه‌ها

هنگام کار با فایل‌های اکسل و مدل‌های زبانی بزرگ، این بهترین شیوه‌ها را در نظر بگیرید:

1. **آماده‌سازی داده‌ها**

- داده‌های خود را قبل از پردازش تمیز کنید (مقادیر گمشده را مدیریت کنید، مشکلات قالب‌بندی را برطرف کنید)
- حذف ستون‌های غیرضروری برای کاهش مصرف توکن را در نظر بگیرید
- برای فایل‌های بزرگ، روی بخش‌های مرتبط‌تر تمرکز کنید

2. **تقسیم‌بندی فایل‌های بزرگ**

- برای صفحات گسترده‌ای که از محدودیت‌های زمینه مدل فراتر می‌روند، آنها را به بخش‌های منطقی تقسیم کنید
- در صورت کار با کتاب‌های کاری چند صفحه‌ای، هر صفحه را جداگانه پردازش کنید
- تجمیع داده‌ها قبل از ارسال به مدل را در نظر بگیرید

3. **مهندسی پرامپت**

- درباره تحلیلی که از داده‌ها می‌خواهید، دقیق باشید
- اگر نام‌های ستون‌ها مبهم هستند، توضیحات ستون را اضافه کنید
- فرمت خروجی مورد نظر خود را مشخص کنید (نکات گلوله‌ای، جداول و غیره)

4. **انتخاب مدل**

- از مدل‌های OpenAI برای تحلیل داده عمومی و تشخیص الگو استفاده کنید
- از مدل‌های Claude برای تحلیل دقیق داده‌های پیچیده استفاده کنید
- از مدل‌های Gemini برای صفحات گسترده با عناصر تصویری مانند نمودارها استفاده کنید

5. **انتخاب رویکرد**

- از رویکرد گردش کار ساده برای تحلیل سریع مجموعه داده‌های کوچک‌تر استفاده کنید
- از عامل CSV Langchain برای تحلیل پیچیده‌تر نیازمند محاسبات استفاده کنید
- ترکیب رویکردها برای بهترین نتایج را در نظر بگیرید

## پیوندهای مرتبط

- [بهترین شیوه‌های RAG](fa/guides/rag-best-practices.md) - درباره تولید تقویت شده با بازیابی برای مجموعه داده‌های بزرگ‌تر بیاموزید
- [پردازش PDF‌ها در API تکمیل چت](fa/examples/processing_pdfs_in_chat_completion_api.md) - پردازش فایل‌های PDF
- [مستندات LangChain](https://python.langchain.com/api_reference/experimental/agents/langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent.html#langchain_experimental.agents.agent_toolkits.csv.base.create_csv_agent) - جزئیات بیشتر درباره عامل CSV
