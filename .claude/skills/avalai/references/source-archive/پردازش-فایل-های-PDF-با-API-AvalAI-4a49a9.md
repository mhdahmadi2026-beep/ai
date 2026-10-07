# پردازش فایل های PDF با API AvalAI

## مقدمه

API AvalAI قابلیت‌های قدرتمندی برای پردازش اسناد PDF با استفاده از مدل‌های زبانی پیشرفته ارائه می‌دهد. این راهنما نشان می‌دهد چگونه می‌توانید از مدل‌های Anthropic (Claude) و Gemini از طریق API سازگار با OpenAI AvalAI برای تحلیل، استخراج اطلاعات و تعامل با فایل‌های PDF استفاده کنید. این قابلیت‌ها به برنامه‌ها امکان می‌دهد تا محتوای متنی و تصویری درون اسناد را درک کنند، که آنها را برای تحلیل اسناد، استخراج اطلاعات و جریان‌های کاری خودکار پردازش اسناد ایده‌آل می‌سازد.

## ویژگی‌های کلیدی

- **درک متن و تصویر** - پردازش محتوای متنی و تصویری درون فایل‌های PDF
- **تحلیل نمودارها و جداول** - استخراج و تفسیر داده‌ها از نمودارها، جداول و دیاگرام‌ها
- **خلاصه‌سازی اسناد** - تولید خلاصه‌های مختصر از محتوای سند
- **استخراج اطلاعات** - استخراج اطلاعات خاص از اسناد به فرمت‌های ساختاریافته
- **پاسخ به سؤالات** - پرسیدن سؤالات درباره محتوای سند و دریافت پاسخ‌های دقیق
- **دسترسی یکپارچه به API** - دسترسی به چندین ارائه دهنده مدل از طریق یک رابط سازگار با OpenAI

## مدل‌های موجود

مدل‌های زیر از پردازش PDF از طریق API AvalAI پشتیبانی می‌کنند:

### مدل‌های Anthropic (Claude)

- **claude-opus-4-7** - مدل پیشرفته با قابلیت‌های قوی درک داده‌ها
- **claude-sonnet-4-6** - جدیدترین نسخه با پردازش داده‌های بهبود یافته
- **claude-haiku-4-5** - مدل کارآمدتر برای پردازش داده‌ها

### مدل‌های Gemini

- **gemini-3.1-pro-preview** - پیشرفته‌ترین مدل با درک بهبود یافته داده‌ها
- **gemini-3.5-flash** - مدل چندوجهی سریع برای پردازش داده‌ها
- **gemini-2.5-pro** - مدل با درک بهبود یافته داده‌ها
- **gemini-2.5-flash** - مدل برای پردازش داده‌ها

علاوه بر PDF، مدل‌های Gemini می‌توانند انواع فایل‌های زیر را نیز مستقیما با استفاده از کدگذاری base64 پردازش کنند:
- PDF - `application/pdf`
- JavaScript - `application/x-javascript`, `text/javascript`
- Python - `application/x-python`, `text/x-python`
- TXT - `text/plain`
- HTML - `text/html`
- CSS - `text/css`
- Markdown - `text/md`
- CSV - `text/csv`
- XML - `text/xml`
- RTF - `text/rtf`

> **نکته مهم**: مدل‌های Anthropic (Claude) از هر دو روش پردازش PDF مبتنی بر URL و کدگذاری base64 پشتیبانی می‌کنند، در حالی که مدل‌های Gemini فقط از روش کدگذاری base64 پشتیبانی می‌کنند.

## استفاده پایه

دو روش اصلی برای پردازش PDF‌ها با API AvalAI وجود دارد:

1. **روش مبتنی بر URL**: ارجاع به یک PDF میزبانی شده آنلاین
2. **روش مبتنی بر کدگذاری base64**: ارسال مستقیم فایل PDF به صورت داده کدگذاری شده

### پردازش PDF مبتنی بر URL

> **توجه**: مدل‌های Anthropic (Claude) از هر دو روش پردازش PDF مبتنی بر URL و کدگذاری base64 پشتیبانی می‌کنند، در حالی که مدل‌های Gemini فقط از روش کدگذاری base64 پشتیبانی می‌کنند.

این روش به شما امکان می‌دهد مستقیما به یک سند PDF از طریق URL ارجاع دهید:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "claude-sonnet-5",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "این سند درباره چیست؟"},
 {
 "type": "file",
 "file": {
 "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
 }
 }
 ]
 }]
}'

python=:from openai import OpenAI

# مقداردهی اولیه کلاینت با API AvalAI
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# آدرس PDF
file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# ایجاد درخواست با ارجاع به فایل مبتنی بر URL
file_content = [
    {"type": "text", "text": "این سند درباره چیست؟"},
    {
        "type": "file",
        "file": {
            "file_id": file_url,
        },
    },
]

# ارسال درخواست به مدل
response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

// مقداردهی اولیه کلاینت با API AvalAI
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// آدرس PDF
const fileUrl =
  "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با ارجاع به فایل مبتنی بر URL
const fileContent = [
  { type: "text", text: "این سند درباره چیست؟" },
  {
    type: "file",
    file: {
      file_id: fileUrl,
    },
  },
];

// ارسال درخواست به مدل
const response = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: fileContent }],
});

console.log(response.choices[0].message.content);

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// آدرس PDF
	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	// ایجاد درخواست با ارجاع به فایل مبتنی بر URL
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

php=:<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// آدرس PDF
$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با ارجاع به فایل مبتنی بر URL
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
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
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

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

bash=:curl https://api.avalai.ir/v1/responses \
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

### پردازش PDF مبتنی بر کدگذاری base64

برای مواردی که نیاز به ارسال مستقیم PDF از سیستم محلی خود دارید یا زمانی که URL در دسترس نیست، می‌توانید از کدگذاری base64 استفاده کنید:

```language-selector
bash=:# ابتدا، فایل PDF را به base64 تبدیل کنید
BASE64_PDF=$(base64 -i /path/to/your/document.pdf | tr -d '\n')

# سپس درخواست API را با PDF کدگذاری شده با base64 ارسال کنید
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "claude-sonnet-5",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "این سند درباره چیست؟"},
 {
 "type": "file",
 "file": {
 "file_data": "data:application/pdf;base64,'$BASE64_PDF'"
 }
 }
 ]
 }]
}'

python=:from openai import OpenAI
import base64
import requests

# مقداردهی اولیه کلاینت با API AvalAI
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# روش 1: از یک URL
pdf_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
response = requests.get(pdf_url)
file_data = response.content

# روش 2: از یک فایل محلی
# with open("path/to/your/document.pdf", "rb") as f:
# 	file_data = f.read()

# کدگذاری داده PDF به base64
encoded_file = base64.b64encode(file_data).decode("utf-8")
base64_url = f"data:application/pdf;base64,{encoded_file}"

# ایجاد درخواست با فایل کدگذاری شده با base64
file_content = [
    {"type": "text", "text": "این سند درباره چیست؟"},
    {
        "type": "file",
        "file": {
            "file_data": base64_url,
        },
    },
]

# ارسال درخواست به مدل
response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";
import axios from "axios";
import fs from "fs";

// مقداردهی اولیه کلاینت با API AvalAI
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// تابع دریافت PDF کدگذاری شده با base64
async function getBase64PDF() {
  // روش 1: از یک URL
  const pdfUrl =
    "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";
  const response = await axios.get(pdfUrl, { responseType: "arraybuffer" });
  const buffer = Buffer.from(response.data);

  // روش 2: از یک فایل محلی
  // const buffer = fs.readFileSync("path/to/your/document.pdf");

  return `data:application/pdf;base64,${buffer.toString("base64")}`;
}

// تابع اصلی
async function processPDF() {
  const base64Pdf = await getBase64PDF();

  // ایجاد درخواست با فایل کدگذاری شده با base64
  const fileContent = [
    { type: "text", text: "این سند درباره چیست؟" },
    {
      type: "file",
      file: {
        file_data: base64Pdf,
      },
    },
  ];

  // ارسال درخواست به مدل
  const response = await client.chat.completions.create({
    model: "claude-sonnet-5",
    messages: [{ role: "user", content: fileContent }],
  });

  console.log(response.choices[0].message.content);
}

processPDF();

go=:package main

import (
	"context"
	"encoding/base64"
	"fmt"
	openai "github.com/openai/openai-go"
	"io/ioutil"
	"net/http"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// دریافت داده PDF
	pdfData, err := getPDFData()
	if err != nil {
		fmt.Printf("Error getting PDF data: %v\n", err)
		return
	}

	// کدگذاری داده PDF به base64
	encodedFile := base64.StdEncoding.EncodeToString(pdfData)
	base64URL := fmt.Sprintf("data:application/pdf;base64,%s", encodedFile)

	// ایجاد درخواست با فایل کدگذاری شده با base64
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
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
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

// تابع دریافت داده PDF از URL یا فایل محلی
func getPDFData() ([]byte, error) {
	// روش 1: از یک URL
	pdfURL := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
	resp, err := http.Get(pdfURL)
	if err != nil {
		return nil, err
	}
	defer resp.Body.Close()

	return ioutil.ReadAll(resp.Body)

	// روش 2: از یک فایل محلی
	// return ioutil.ReadFile("path/to/your/document.pdf")
}

php=:<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// تابع دریافت PDF کدگذاری شده با base64
function getBase64PDF() {
 // روش 1: از یک URL
 $pdfUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";
 $fileData = file_get_contents($pdfUrl);
 
 // روش 2: از یک فایل محلی
 // $fileData = file_get_contents("path/to/your/document.pdf");
 
 return "data:application/pdf;base64," . base64_encode($fileData);
}

// دریافت PDF کدگذاری شده با base64
$base64Pdf = getBase64PDF();

// ایجاد درخواست با فایل کدگذاری شده با base64
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_data" => $base64Pdf
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
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
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

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

bash=:curl https://api.avalai.ir/v1/responses \
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

## مشخص کردن فرمت

می‌توانید فرمت سند را به صورت صریح مشخص کنید تا از پردازش صحیح اطمینان حاصل شود:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "claude-sonnet-5",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "این سند درباره چیست؟"},
 {
 "type": "file",
 "file": {
 "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
 "format": "application/pdf"
 }
 }
 ]
 }]
}'

python=:from openai import OpenAI

# مقداردهی اولیه کلاینت با API AvalAI
client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

# آدرس PDF
file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

# ایجاد درخواست با مشخص کردن فرمت
file_content = [
    {"type": "text", "text": "این سند درباره چیست؟"},
    {"type": "file", "file": {"file_id": file_url, "format": "application/pdf"}},
]

# ارسال درخواست به مدل
response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

// مقداردهی اولیه کلاینت با API AvalAI
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// آدرس PDF
const fileUrl =
  "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با مشخص کردن فرمت
const fileContent = [
  { type: "text", text: "این سند درباره چیست؟" },
  {
    type: "file",
    file: {
      file_id: fileUrl,
      format: "application/pdf",
    },
  },
];

// ارسال درخواست به مدل
const response = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: fileContent }],
});

console.log(response.choices[0].message.content);

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	// آدرس PDF
	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	// ایجاد درخواست با مشخص کردن فرمت
	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "این سند درباره چیست؟",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
				Format: "application/pdf",
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

php=:<?php

require 'vendor/autoload.php';

// مقداردهی اولیه کلاینت با API AvalAI
$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// آدرس PDF
$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

// ایجاد درخواست با مشخص کردن فرمت
$fileContent = [
 [
 "type" => "text",
 "text" => "این سند درباره چیست؟"
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl,
 "format" => "application/pdf"
 ]
 ]
];

// ارسال درخواست به مدل
$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
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
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

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

bash=:curl https://api.avalai.ir/v1/responses \
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


## محدودیت‌های خاص مدل‌ها

### مدل‌های Anthropic (Claude)

- **حداکثر حجم فایل**: ۳۲ مگابایت در هر درخواست
- **حداکثر تعداد صفحات**: ۱۰۰ صفحه در هر سند
- **الزامات فرمت**: PDF استاندارد (بدون رمزگذاری یا پسورد)
- **مصرف توکن**: معمولا بین ۱٬۵۰۰ تا ۳٬۰۰۰ توکن برای هر صفحه بسته به تراکم محتوا
- **عناصر تصویری**: قابلیت تحلیل نمودارها، جداول و دیاگرام‌ها در فایل‌های PDF
- **بهترین کاربرد برای**: تحلیل دقیق اسناد، وظایف پیچیده درک اسناد

### مدل‌های Gemini

- **حداکثر حجم فایل**: ۲۰ مگابایت برای آپلود مستقیم (تا ۵۰ مگابایت با استفاده از File API)
- **حداکثر تعداد صفحات**: تا ۱٬۰۰۰ صفحه در هر سند
- **الزامات فرمت**: PDF استاندارد (بدون رمزگذاری یا پسورد)
- **مصرف توکن**: تقریبا ۲۵۸ توکن برای هر صفحه
- **عناصر تصویری**: قابلیت‌های قوی برای تحلیل محتوای تصویری در اسناد
- **بهترین کاربرد برای**: پردازش اسناد بزرگ، تحلیل محتوای تصویری

## موارد استفاده

### خلاصه‌سازی اسناد

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "claude-sonnet-5",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "خلاصه‌ای مختصر از این سند ارائه دهید."},
 {
 "type": "file",
 "file": {
 "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
 }
 }
 ]
 }]
}'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

file_content = [
    {"type": "text", "text": "خلاصه‌ای مختصر از این سند ارائه دهید."},
    {
        "type": "file",
        "file": {
            "file_id": file_url,
        },
    },
]

response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const fileUrl =
  "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

const fileContent = [
  { type: "text", text: "خلاصه‌ای مختصر از این سند ارائه دهید." },
  {
    type: "file",
    file: {
      file_id: fileUrl,
    },
  },
];

const response = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: fileContent }],
});

console.log(response.choices[0].message.content);

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "خلاصه‌ای مختصر از این سند ارائه دهید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

php=:<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

$fileContent = [
 [
 "type" => "text",
 "text" => "خلاصه‌ای مختصر از این سند ارائه دهید."
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
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
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

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

bash=:curl https://api.avalai.ir/v1/responses \
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


### استخراج اطلاعات

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "claude-sonnet-5",
 "messages": [{
 "role": "user",
 "content": [
 {"type": "text", "text": "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید."},
 {
 "type": "file",
 "file": {
 "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
 }
 }
 ]
 }]
}'

python=:from openai import OpenAI

client = OpenAI(api_key="your-avalai-api-key", base_url="https://api.avalai.ir/v1")

file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

file_content = [
    {
        "type": "text",
        "text": "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید.",
    },
    {
        "type": "file",
        "file": {
            "file_id": file_url,
        },
    },
]

response = client.chat.completions.create(
    model="claude-sonnet-5",
    messages=[{"role": "user", "content": file_content}],
)

print(response.choices[0].message.content)

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const fileUrl =
  "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

const fileContent = [
  {
    type: "text",
    text: "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید.",
  },
  {
    type: "file",
    file: {
      file_id: fileUrl,
    },
  },
];

const response = await client.chat.completions.create({
  model: "claude-sonnet-5",
  messages: [{ role: "user", content: fileContent }],
});

console.log(response.choices[0].message.content);

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("your-avalai-api-key")
	client.BaseURL = "https://api.avalai.ir/v1"

	fileUrl := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	fileContent := []openai.ChatMessageContent{
		{
			Type: openai.ChatMessageContentTypeText,
			Text: "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید.",
		},
		{
			Type: openai.ChatMessageContentTypeFile,
			File: &openai.ChatMessageFile{
				FileID: fileUrl,
			},
		},
	}

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-5",
			Messages: []openai.ChatCompletionMessage{
				{
					Role:    openai.ChatMessageRoleUser,
					Content: fileContent,
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("ChatCompletion error: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

php=:<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY'); // Or replace with your actual key: 'aa-YOUR_API_KEY'

if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}

// Your custom base URL
$customBaseUrl = 'https://api.avalai.ir/v1';

// Create a custom client instance using the factory
$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

$fileContent = [
 [
 "type" => "text",
 "text" => "تمام تاریخ‌های ذکر شده در این سند را استخراج کرده و به ترتیب زمانی فهرست کنید."
 ],
 [
 "type" => "file",
 "file" => [
 "file_id" => $fileUrl
 ]
 ]
];

$completion = $client->chat()->create([
 'model' => 'claude-sonnet-4-6',
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
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```language-selector
python=:import os
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

javascript=:import OpenAI from "openai";

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

bash=:curl https://api.avalai.ir/v1/responses \
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


## عیب‌یابی

### مشکلات رایج

- **فایل بیش از حد بزرگ است**: اگر با خطاهای مربوط به اندازه فایل مواجه می‌شوید، سعی کنید اندازه PDF را کاهش داده یا آن را به اسناد کوچکتر تقسیم کنید.
- **فرمت شناسایی نشد**: اطمینان حاصل کنید که هنگام ارسال سند، فرمت صحیح (`application/pdf`) را مشخص می‌کنید.
- **خطاهای تجزیه و تحلیل**: برخی از فایل‌های PDF با قالب‌بندی پیچیده یا محتوای اسکن شده ممکن است به درستی پردازش نشوند. سعی کنید از PDF‌های با کیفیت بالاتر با کدگذاری متن مناسب استفاده کنید.
- **محدودیت‌های توکن**: اگر سند شما از محدودیت توکن مدل فراتر رفت، در نظر بگیرید که آن را در بخش‌های جداگانه پردازش کنید یا بخش‌های مختلف را جداگانه خلاصه کنید.

### بهینه‌سازی عملکرد

- **متن پرسش را پس از PDF قرار دهید**: برای بهترین نتایج، پرسش متنی خود را پس از PDF در درخواست قرار دهید.
- **برای فایل‌های بزرگتر از روش مبتنی بر URL استفاده کنید**: روش مبتنی بر URL معمولا برای فایل‌های بزرگتر کارآمدتر است.
- **دستورالعمل‌های واضح مشخص کنید**: در پرسش‌های خود درباره اطلاعاتی که می‌خواهید از سند استخراج کنید، دقیق باشید.
- **از دمای پایین‌تر استفاده کنید**: برای وظایف استخراج واقعیت، تنظیم دمای پایین‌تر (مثلا ۰.۲) می‌تواند دقت را بهبود بخشد.

## بهترین شیوه‌ها

1. **سازگاری فایل را از قبل بررسی کنید**: اطمینان حاصل کنید که PDF شما دارای رمز عبور نیست و به درستی قالب‌بندی شده است.
2. **پشتیبانی مدل را تایید کنید**: قبل از ارسال درخواست‌ها، بررسی کنید که مدل انتخابی شما از پردازش PDF پشتیبانی می‌کند.
3. **پرسش‌های خود را ساختاربندی کنید**: درباره کاری که می‌خواهید مدل با سند انجام دهد، مشخص باشید.
4. **با اسناد بزرگ به طور مناسب برخورد کنید**: اگر اسناد از محدودیت‌های صفحه فراتر می‌روند، آنها را به بخش‌های منطقی تقسیم کنید.
5. **استفاده از توکن را در نظر بگیرید**: به خصوص برای اسناد بزرگ، از پیامدهای استفاده از توکن آگاه باشید.

## پیوندهای مرتبط

- [مرجع API تکمیل چت](fa/api-reference/chat.md)
- [راهنمای انتخاب مدل](fa/guides/model-selection.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [راهنمای فایل‌های PDF](fa/guides/pdf-files.md)
