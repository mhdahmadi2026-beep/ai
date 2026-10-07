# راهنمای ورودی‌های فایل

بیاموزید چگونه فایل‌ها را به عنوان ورودی به اندپوینت‌های API AvalAI با استفاده از URLها، کدگذاری Base64، یا شناسه فایل‌ها از Files API ارائه دهید.

## مروری کلی

API AvalAI از سه روش برای ارائه ورودی‌های فایل به اندپوینت‌های مختلف پشتیبانی می‌کند:

1. **URL** - ارائه لینک مستقیم به یک فایل با دسترسی عمومی
2. **Base64** - کدگذاری محتوای فایل به عنوان رشته Base64
3. **شناسه فایل (File ID)** - ابتدا فایل‌ها را به اندپوینت [`v1/files`](fa/api-reference/files.md) آپلود کنید، سپس با شناسه به آنها ارجاع دهید

> **📁 Files API در دسترس است**: فایل‌ها را یک بار در `v1/files` آپلود کنید و سپس در درخواست‌های پشتیبانی‌شده با `file_id` به آن‌ها ارجاع دهید. برای purposeهای پشتیبانی‌شده، محدودیت ذخیره‌سازی، محدودیت نرخ، نکته‌های قیمت‌گذاری و سازگاری مدل، [مرجع API فایل‌ها](fa/api-reference/files.md) را ببینید.

هر روش بسته به نیاز شما مزایای خود را دارد:

| روش | مناسب برای | مزایا | معایب |
|-----|-----------|-------|------|
| URL | فایل‌های با دسترسی عمومی | ساده، بدون نیاز به کدگذاری | نیاز به URL عمومی |
| Base64 | فایل‌های محلی، محتوای خصوصی | بدون مرحله upload جداگانه | اندازه درخواست را حدود یک‌سوم افزایش می‌دهد و باید زیر محدودیت route بماند |
| شناسه فایل | فایل‌های بزرگ، محتوای قابل استفاده مجدد | درخواست‌های تمیز، قابل استفاده مجدد | نیاز به مرحله upload و purpose پشتیبانی‌شده دارد |

## فایل‌ها چگونه پردازش می‌شوند؟

مدل ورودی فایل OpenAI هنگام تبدیل مثال‌ها به AvalAI بسیار مفید است:

- **PDFها**: مدل‌های دارای قابلیت بینایی می‌توانند هم متن استخراج‌شده و هم تصویر صفحه‌ها را دریافت کنند؛ این برای نمودار، جدول، فرم و layoutهای اسکن‌شده کمک می‌کند.
- **متن، کد و سندهای غنی**: سندهای غیر PDF معمولا پیش از ورود به context مدل به متن استخراج‌شده تبدیل می‌شوند.
- **Spreadsheetها**: جریان Responses در OpenAI از augmentation مخصوص spreadsheet استفاده می‌کند: تا اولین ۱۰۰۰ ردیف هر sheet را parse می‌کند و به جای ارسال همه سلول‌ها، metadata خلاصه و header اضافه می‌کند. برای join، aggregation، formula، reconciliation یا charting دقیق، از یک pipeline مخصوص spreadsheet بیرون از مدل استفاده کنید.
- **پایگاه دانش بزرگ**: همه فایل‌ها را داخل یک prompt نفرستید. وقتی retrieval روی تعداد زیادی سند لازم دارید از [RAG دستی با embeddings](/fa/examples/manual_rag_with_embeddings.md) یا [الگوهای file search](/fa/guides/tools-file-search.md) استفاده کنید.

?> پشتیبانی همچنان به endpoint، مدل، نوع فایل و محدودیت‌های حساب وابسته است. وقتی مثال‌های OpenAI با `input_file` را منتقل می‌کنید، آن‌ها را به route واقعی AvalAI که استفاده می‌کنید نگاشت کنید و با مدل انتخابی تست بگیرید.

برای migration به Responses، carrier ورودی را صریح نگه دارید: URL تصویر و data URL تصویر از `input_image.image_url` استفاده می‌کنند؛ سند عمومی از `input_file.file_url`؛ فایل آپلودشده از `input_file.file_id`؛ و سند Base64 از `input_file.filename` همراه با `input_file.file_data`.

### نقشه Carrier سازگار با OpenAI

هنگام تطبیق مثال‌های OpenAI با routeهای AvalAI، از این نقشه سریع استفاده کنید:

| ورودی | شکل Chat Completions | شکل Responses | نکته AvalAI |
|-------|----------------------|---------------|-------------|
| URL تصویر عمومی | `image_url.url` | `input_image.image_url` | برای routeهای مدل دارای قابلیت vision کاربرد دارد. |
| تصویر محلی | data URL مبتنی بر Base64 در `image_url.url` | data URL مبتنی بر Base64 در `input_image.image_url` | برای استفاده تکراری، با `purpose="vision"` آپلود کنید و `input_image.file_id` بفرستید. |
| URL عمومی PDF یا سند | فقط شکل provider-specific، مانند محتوای `file` در Claude | `input_file.file_url` | URL عمومی را داخل `file_id` نگذارید؛ `file_id` مخصوص فایل‌های uploadشده است. |
| PDF یا سند uploadشده | پشتیبانی provider-specific از `file_id` | `input_file.file_id` | وقتی فایل ورودی مدل است، با `purpose="user_data"` آپلود کنید. |
| PDF یا سند inline | بلوک فایل Base64 مخصوص provider | `input_file.filename` همراه `input_file.file_data` | data URL کامل مثل `data:application/pdf;base64,...` بیاورید. |
| Spreadsheet | بلوک فایل provider-specific | `input_file` برای خلاصه‌سازی سطح بالا | برای formula، join، chart و محاسبات auditشده از parsing سمت برنامه استفاده کنید. |

### چک‌لیست دقت برای سندها و Spreadsheetها

پیش از ارسال سندهای کاری، اسلایدها یا spreadsheetها به مدل، این موارد را بررسی کنید:

- **layout بصری را حفظ کنید:** ورودی‌های سند غیر PDF معمولا به متن استخراج‌شده تبدیل می‌شوند. تصاویر embedشده، نمودارها، دیاگرام‌ها، speaker noteها و جای‌گذاری عناصر در اسلاید ممکن است وارد context مدل نشوند. وقتی layout صفحه یا دقت نمودار مهم است، ابتدا فایل را به PDF تبدیل کنید.
- **ورودی مستقیم یا retrieval را درست انتخاب کنید:** فایل‌های کوچک و مخصوص همان task را مستقیم به صورت `input_file` بفرستید؛ وقتی کاربر به جستجو روی تعداد زیادی سند نیاز دارد از [RAG دستی با embeddings](/fa/examples/manual_rag_with_embeddings.md) یا [الگوهای file search](/fa/guides/tools-file-search.md) استفاده کنید.
- **Spreadsheet را context خلاصه‌شده بدانید:** جریان `input_file` در OpenAI برای spreadsheetها از augmentation مخصوص استفاده می‌کند و لزوما همه سلول‌ها را عینا وارد prompt نمی‌کند؛ مرجع OpenAI parsing تا اولین ۱۰۰۰ ردیف هر sheet همراه با metadata خلاصه و header را توضیح می‌دهد. رفتار AvalAI به route ارائه‌دهنده انتخابی وابسته است، بنابراین برای join، formula، reconciliation و charting از parser یا pipeline قطعی مخصوص spreadsheet استفاده کنید.
- **پس از استخراج اعتبارسنجی کنید:** در صورت امکان از مدل بخواهید page، row، sheet یا section identifier را ذکر کند و سپس facts برگشتی را پیش از نوشتن در دیتابیس یا نمایش تصمیم‌های مهم به کاربر verify کنید.

## اندپوینت‌های پشتیبانی شده

ورودی‌های فایل در چندین اندپوینت API AvalAI پشتیبانی می‌شوند:

- [`v1/chat/completions`](fa/api-reference/chat.md) - API اصلی چت برای مدل‌های OpenAI، Anthropic، Gemini
- [`v1/messages`](fa/api-reference/messages.md) - API Messages Anthropic
- [`v1/responses`](fa/api-reference/responses.md) - API Responses OpenAI
- [`v1/ocr`](fa/api-reference/ocr.md) - API OCR Mistral

## محدودیت‌های اندازه فایل

مدل‌ها و ارائه‌دهندگان مختلف محدودیت‌های متفاوتی برای داده‌های فایل درون‌خطی دارند:

| ارائه‌دهنده/مدل | حداکثر اندازه فایل | نکات |
|----------------|-------------------|------|
| **مدل‌های Gemini** | ۲۰ مگابایت | کل داده‌های درون‌خطی در درخواست |
| **Mistral OCR** | ۵۰ مگابایت | به ازای هر سند، تا ۱۰۰۰ صفحه |
| **مدل‌های OpenAI** | ۲۰ مگابایت | به ازای هر درخواست |
| **Anthropic (Claude)** | ۳۲ مگابایت | به ازای هر درخواست |
| **سایر مدل‌ها** | ۲۰ مگابایت | محدودیت پیش‌فرض |

> **توجه**: این محدودیت‌ها ممکن است با محدودیت‌های رسمی ارائه‌دهنده متفاوت باشد. اگر به محدودیت‌های بالاتر یا نیازهای خاصی دارید، با تیم پشتیبانی ما در [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

?> هنگام تطبیق مثال‌های OpenAI Responses، توجه کنید که مستندات عمومی OpenAI برای همان پلتفرم محدودیت ترکیبی `input_file` را توضیح می‌دهد. محدودیت‌های AvalAI می‌تواند بر اساس provider، endpoint، مسیر upload فایل و سیاست حساب متفاوت باشد؛ جدول بالا و [مرجع Files API](/fa/api-reference/files.md) را منبع AvalAI در نظر بگیرید.

## انواع فایل‌های پشتیبانی شده

### تصاویر
- JPEG (`.jpg`، `.jpeg`) - `image/jpeg`
- PNG (`.png`) - `image/png`
- GIF (`.gif`) - `image/gif` (غیر متحرک، فقط یک فریم)
- WebP (`.webp`) - `image/webp`

### اسناد
- PDF (`.pdf`) - `application/pdf`

### صوت
- MP3 (`.mp3`) - `audio/mp3` یا `audio/mpeg`
- WAV (`.wav`) - `audio/wav`
- M4A (`.m4a`) - `audio/m4a`
- FLAC (`.flac`) - `audio/flac`

### صفحات گسترده
- Excel (`.xlsx`) - `application/vnd.openxmlformats-officedocument.spreadsheetml.sheet`
- Excel قدیمی (`.xls`) - `application/vnd.ms-excel`

### ورودی‌های سند سازگار با OpenAI

برخی routeهای `/v1/responses` می‌توانند فرمت‌های OpenAI-style `input_file` مانند فایل‌های متن/کد (`.txt`، `.md`، `.json`، `.html`، `.xml` و فایل‌های source)، سندهای غنی (`.doc`، `.docx`، `.rtf`، `.odt`)، ارائه‌ها (`.ppt`، `.pptx`) و spreadsheetهای جداشده (`.csv`، `.tsv`) را نیز بپذیرند. در AvalAI این مورد را وابسته به provider و endpoint بدانید: وقتی fidelity بصری مهم است فایل را به PDF تبدیل کنید، و وقتی route یک MIME type را رد می‌کند آن را به متن ساده یا PDF تبدیل کنید.

## روش ۱: فایل‌های مبتنی بر URL

ساده‌ترین روش برای فایل‌های با دسترسی عمومی، ارائه URL مستقیم است.

### تصویر URL در Chat Completions

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-5.6-luna",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "در این تصویر چیست؟"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "https://example.com/sample-image.jpg"
          }
        }
      ]
    }
  ]
}'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چیست؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": "https://example.com/sample-image.jpg"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "در این تصویر چیست؟" },
        {
          type: "image_url",
          image_url: { url: "https://example.com/sample-image.jpg" },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "در این تصویر چیست؟",
						},
						{
							Type: "image_url",
							ImageURL: &openai.ImageURL{
								URL: "https://example.com/sample-image.jpg",
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'در این تصویر چیست؟'],
                [
                    'type' => 'image_url',
                    'image_url' => ['url' => 'https://example.com/sample-image.jpg']
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

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
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
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
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
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
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "https://example.com/image.png"
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


### URL PDF در Chat Completions

برای مدل‌های Anthropic (Claude)، می‌توانید PDFها را از طریق URL ارائه دهید:

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "claude-sonnet-4-6",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "این سند درباره چیست؟"
        },
        {
          "type": "file",
          "file": {
            "file_id": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
          }
        }
      ]
    }
  ]
}'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# URL فایل PDF
file_url = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این سند درباره چیست؟"},
                {"type": "file", "file": {"file_id": file_url}},
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const fileUrl = "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf";

const response = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این سند درباره چیست؟" },
        { type: "file", file: { file_id: fileUrl } },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	fileURL := "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "claude-sonnet-4-6",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند درباره چیست؟",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileID: fileURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$fileUrl = 'https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf';

$response = $client->chat()->create([
    'model' => 'claude-sonnet-4-6',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند درباره چیست؟'],
                ['type' => 'file', 'file' => ['file_id' => $fileUrl]]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `claude-sonnet-4-6` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. برای PDF عمومی، URL اصلی را نگه دارید و آن را با `input_file.file_url` بفرستید؛ `file_id` را فقط برای فایل‌های آپلودشده از `/v1/files` استفاده کنید.

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
                {"type": "input_text", "text": "این سند درباره چیست؟"},
                {
                    "type": "input_file",
                    "file_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
                },
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
        { type: "input_text", text: "این سند درباره چیست؟" },
        {
          type: "input_file",
          file_url:
            "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf",
        },
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
            "text": "این سند درباره چیست؟"
          },
          {
            "type": "input_file",
            "file_url": "https://www.w3.org/WAI/ER/tests/xhtml/testfiles/resources/pdf/dummy.pdf"
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `file.file_id` که URL دارد → `input_file.file_url`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### URL سند در OCR API

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "mistral-ocr-latest",
  "document": {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770"
  },
  "include_image_base64": true
}' -o ocr_output.json

```

```python
import os
from mistralai import Mistral

client = Mistral(
    server_url="https://api.avalai.ir", api_key=os.environ["AVALAI_API_KEY"]
)

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا ۱۰۰ صفحه
)

print(ocr_response)

```

```javascript
import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  pages: Array.from({ length: 100 }, (_, i) => i),
});

console.log(ocrResponse);

```

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	requestBody := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]string{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"include_image_base64": true,
	}

	jsonBody, _ := json.Marshal(requestBody)

	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(jsonBody))
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := ioutil.ReadAll(resp.Body)
	fmt.Println(string(body))
}

```

```php
<?php

$apiKey = getenv('AVALAI_API_KEY');

$data = [
    'model' => 'mistral-ocr-latest',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/1805.04770'
    ],
    'include_image_base64' => true
];

$ch = curl_init('https://api.avalai.ir/v1/ocr');
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

echo $response;

```


## روش ۲: فایل‌های کدگذاری شده با Base64

برای فایل‌های محلی یا محتوای خصوصی، فایل را به صورت Base64 کدگذاری کرده و در درخواست قرار دهید.

### فرمت Data URL

فایل‌های کدگذاری شده با Base64 از فرمت data URL استفاده می‌کنند:

```
data:{mime_type};base64,{encoded_data}
```

برای مثال:
- تصویر: `data:image/jpeg;base64,/9j/4AAQSkZJRg...`
- PDF: `data:application/pdf;base64,JVBERi0xLjQK...`
- صوت: `data:audio/mp3;base64,SUQzAwAAAAA...`

### تصویر با Base64 در Chat Completions

```bash
# کدگذاری تصویر به base64
IMAGE_BASE64=$(base64 -i image.jpg | tr -d '\n') # در لینوکس از -w 0 استفاده کنید

curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-5.6-luna",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "در این تصویر چیست؟"
        },
        {
          "type": "image_url",
          "image_url": {
            "url": "data:image/jpeg;base64,'"$IMAGE_BASE64"'"
          }
        }
      ]
    }
  ]
}'

```

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# خواندن و کدگذاری تصویر
with open("image.jpg", "rb") as image_file:
    image_data = image_file.read()

base64_image = base64.b64encode(image_data).decode("utf-8")

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "در این تصویر چیست؟"},
                {
                    "type": "image_url",
                    "image_url": {"url": f"data:image/jpeg;base64,{base64_image}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// خواندن و کدگذاری تصویر
const imageData = fs.readFileSync("image.jpg");
const base64Image = imageData.toString("base64");

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "در این تصویر چیست؟" },
        {
          type: "image_url",
          image_url: { url: `data:image/jpeg;base64,${base64Image}` },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری تصویر
	imageData, err := ioutil.ReadFile("image.jpg")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Image := base64.StdEncoding.EncodeToString(imageData)
	dataURL := "data:image/jpeg;base64," + base64Image

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "در این تصویر چیست؟",
						},
						{
							Type: "image_url",
							ImageURL: &openai.ImageURL{
								URL: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری تصویر
$imageData = file_get_contents('image.jpg');
$base64Image = base64_encode($imageData);

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'در این تصویر چیست؟'],
                [
                    'type' => 'image_url',
                    'image_url' => ['url' => 'data:image/jpeg;base64,' . $base64Image]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، تصویر را به شکل data URL نگه دارید و آن را با `input_image.image_url` ارسال کنید.

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("image.jpg", "rb") as image_file:
    base64_image = base64.b64encode(image_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "Describe this image."},
                {
                    "type": "input_image",
                    "image_url": f"data:image/jpeg;base64,{base64_image}",
                },
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import fs from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const base64Image = fs.readFileSync("image.jpg", "base64");

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "Describe this image." },
        {
          type: "input_image",
          image_url: `data:image/jpeg;base64,${base64Image}`,
        },
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
            "text": "Describe this image."
          },
          {
            "type": "input_image",
            "image_url": "data:image/jpeg;base64,..."
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `image_url.url` → `input_image.image_url`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### PDF با Base64 در Chat Completions

```bash
# کدگذاری PDF به base64
PDF_BASE64=$(base64 -i document.pdf | tr -d '\n') # در لینوکس از -w 0 استفاده کنید

curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gemini-2.5-flash",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "این سند را خلاصه کنید"
        },
        {
          "type": "file",
          "file": {
            "file_data": "data:application/pdf;base64,'"$PDF_BASE64"'"
          }
        }
      ]
    }
  ]
}'

```

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# خواندن و کدگذاری PDF
with open("document.pdf", "rb") as pdf_file:
    pdf_data = pdf_file.read()

base64_pdf = base64.b64encode(pdf_data).decode("utf-8")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این سند را خلاصه کنید"},
                {
                    "type": "file",
                    "file": {"file_data": f"data:application/pdf;base64,{base64_pdf}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// خواندن و کدگذاری PDF
const pdfData = fs.readFileSync("document.pdf");
const base64Pdf = pdfData.toString("base64");

const response = await client.chat.completions.create({
  model: "gemini-2.5-flash",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این سند را خلاصه کنید" },
        {
          type: "file",
          file: { file_data: `data:application/pdf;base64,${base64Pdf}` },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری PDF
	pdfData, err := ioutil.ReadFile("document.pdf")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Pdf := base64.StdEncoding.EncodeToString(pdfData)
	dataURL := "data:application/pdf;base64," + base64Pdf

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند را خلاصه کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری PDF
$pdfData = file_get_contents('document.pdf');
$base64Pdf = base64_encode($pdfData);

$response = $client->chat()->create([
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کنید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:application/pdf;base64,' . $base64Pdf]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، PDF محلی را با `input_file.filename` و `input_file.file_data` به صورت inline نگه دارید.

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("document.pdf", "rb") as pdf_file:
    base64_pdf = base64.b64encode(pdf_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": "این PDF را خلاصه کن."},
                {
                    "type": "input_file",
                    "filename": "document.pdf",
                    "file_data": f"data:application/pdf;base64,{base64_pdf}",
                },
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import fs from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const base64Pdf = fs.readFileSync("document.pdf", "base64");

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_text", text: "این PDF را خلاصه کن." },
        {
          type: "input_file",
          filename: "document.pdf",
          file_data: `data:application/pdf;base64,${base64Pdf}`,
        },
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
            "text": "این PDF را خلاصه کن."
          },
          {
            "type": "input_file",
            "filename": "document.pdf",
            "file_data": "data:application/pdf;base64,..."
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `file.file_data` در Chat → `input_file.file_data` در Responses
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### صوت با Base64 در Chat Completions

```bash
# کدگذاری صوت به base64
AUDIO_BASE64=$(base64 -i audio.mp3 | tr -d '\n')

curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gemini-2.5-flash",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "این صوت را رونویسی کنید"
        },
        {
          "type": "file",
          "file": {
            "file_data": "data:audio/mp3;base64,'"$AUDIO_BASE64"'"
          }
        }
      ]
    }
  ]
}'

```

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# خواندن و کدگذاری صوت
with open("audio.mp3", "rb") as audio_file:
    audio_data = audio_file.read()

base64_audio = base64.b64encode(audio_data).decode("utf-8")

response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این صوت را رونویسی کنید"},
                {
                    "type": "file",
                    "file": {"file_data": f"data:audio/mp3;base64,{base64_audio}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// خواندن و کدگذاری صوت
const audioData = fs.readFileSync("audio.mp3");
const base64Audio = audioData.toString("base64");

const response = await client.chat.completions.create({
  model: "gemini-2.5-flash",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این صوت را رونویسی کنید" },
        {
          type: "file",
          file: { file_data: `data:audio/mp3;base64,${base64Audio}` },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری صوت
	audioData, err := ioutil.ReadFile("audio.mp3")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Audio := base64.StdEncoding.EncodeToString(audioData)
	dataURL := "data:audio/mp3;base64," + base64Audio

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gemini-2.5-flash",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این صوت را رونویسی کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری صوت
$audioData = file_get_contents('audio.mp3');
$base64Audio = base64_encode($audioData);

$response = $client->chat()->create([
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این صوت را رونویسی کنید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:audio/mp3;base64,' . $base64Audio]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

وقتی مدل Responses انتخابی در AvalAI ورودی صوت inline را نمی‌پذیرد، از این مسیر migration استفاده کنید. مثال Chat Completions بالا را برای مدل‌های صوتی مستقیم نگه دارید، یا ابتدا صوت را با [Speech to Text](fa/guides/speech-to-text.md) transcribe کنید و سپس transcript را برای خلاصه‌سازی، extraction یا reasoning بعدی به `/v1/responses` بفرستید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

transcript = os.environ["AUDIO_TRANSCRIPT"]

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="Transcript را خلاصه کن و action itemها را فهرست کن.",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_text", "text": f"Transcript:\n{transcript}"},
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

const transcript = process.env.AUDIO_TRANSCRIPT;

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "Transcript را خلاصه کن و action itemها را فهرست کن.",
  input: [
    {
      role: "user",
      content: [{ type: "input_text", text: `Transcript:\n${transcript}` }],
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
    "instructions": "Transcript را خلاصه کن و action itemها را فهرست کن.",
    "input": [
      {
        "role": "user",
        "content": [
          {
            "type": "input_text",
            "text": "Transcript:\nمتن transcript را اینجا قرار دهید."
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- بایت‌های صوت inline → ابتدا transcribe کنید، یا فقط پس از تأیید پشتیبانی مدل انتخابی از schema صوتی route-specific استفاده کنید
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### اکسل با Base64 در Chat Completions

```bash
# کدگذاری فایل اکسل به base64
EXCEL_BASE64=$(base64 -i spreadsheet.xlsx | tr -d '\n')

curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-5.6-luna",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید"
        },
        {
          "type": "file",
          "file": {
            "file_data": "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,'"$EXCEL_BASE64"'"
          }
        }
      ]
    }
  ]
}'

```

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# خواندن و کدگذاری فایل اکسل
with open("spreadsheet.xlsx", "rb") as excel_file:
    excel_data = excel_file.read()

base64_excel = base64.b64encode(excel_data).decode("utf-8")
mime_type = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "user",
            "content": [
                {
                    "type": "text",
                    "text": "این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید",
                },
                {
                    "type": "file",
                    "file": {"file_data": f"data:{mime_type};base64,{base64_excel}"},
                },
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";
import fs from "fs";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// خواندن و کدگذاری فایل اکسل
const excelData = fs.readFileSync("spreadsheet.xlsx");
const base64Excel = excelData.toString("base64");
const mimeType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet";

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید" },
        {
          type: "file",
          file: { file_data: `data:${mimeType};base64,${base64Excel}` },
        },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"encoding/base64"
	"fmt"
	"io/ioutil"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// خواندن و کدگذاری فایل اکسل
	excelData, err := ioutil.ReadFile("spreadsheet.xlsx")
	if err != nil {
		fmt.Printf("خطا در خواندن فایل: %v\n", err)
		return
	}
	base64Excel := base64.StdEncoding.EncodeToString(excelData)
	mimeType := "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
	dataURL := fmt.Sprintf("data:%s;base64,%s", mimeType, base64Excel)

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileData: dataURL,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

// خواندن و کدگذاری فایل اکسل
$excelData = file_get_contents('spreadsheet.xlsx');
$base64Excel = base64_encode($excelData);
$mimeType = 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet';

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این صفحه گسترده را تحلیل کنید و نکات کلیدی را ارائه دهید'],
                [
                    'type' => 'file',
                    'file' => ['file_data' => 'data:' . $mimeType . ';base64,' . $base64Excel]
                ]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، برای spreadsheet نام فایل و MIME type spreadsheet را در `file_data` بیاورید و پیش از استفاده از پاسخ، rowها یا formulaهای استخراج‌شده را verify کنید.

```python
import base64
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

with open("data.xlsx", "rb") as spreadsheet_file:
    base64_sheet = base64.b64encode(spreadsheet_file.read()).decode("utf-8")

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {
                    "type": "input_text",
                    "text": "این spreadsheet را تحلیل کن و trendهای اصلی را خلاصه کن.",
                },
                {
                    "type": "input_file",
                    "filename": "data.xlsx",
                    "file_data": (
                        "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,"
                        + base64_sheet
                    ),
                },
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import fs from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const base64Sheet = fs.readFileSync("data.xlsx", "base64");

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        {
          type: "input_text",
          text: "این spreadsheet را تحلیل کن و trendهای اصلی را خلاصه کن.",
        },
        {
          type: "input_file",
          filename: "data.xlsx",
          file_data:
            `data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,${base64Sheet}`,
        },
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
            "text": "این spreadsheet را تحلیل کن و trendهای اصلی را خلاصه کن."
          },
          {
            "type": "input_file",
            "filename": "data.xlsx",
            "file_data": "data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,..."
          }
        ]
      }
    ]
  }'

```


- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- payload اکسل Base64 → `input_file.filename` همراه با `input_file.file_data`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


## روش ۳: استفاده از Files API (v1/files)

برای فایل‌های بزرگ یا زمانی که نیاز به استفاده مجدد از فایل‌ها در چندین درخواست دارید، ابتدا آنها را به اندپوینت [`v1/files`](fa/api-reference/files.md) آپلود کنید و با شناسه به آنها ارجاع دهید.

> **وضعیت Files API**: مسیر `v1/files` برای ورودی‌های فایل قابل استفاده مجدد در دسترس است. برای محدودیت نرخ، محدودیت ذخیره‌سازی، نکته‌های قیمت‌گذاری، purposeهای پشتیبانی‌شده و سازگاری endpoint، [مرجع API فایل‌ها](fa/api-reference/files.md) را ببینید.

### چرا از Files API استفاده کنیم؟

1. **جلوگیری از انتقال مکرر فایل‌های بزرگ** - یک بار آپلود کنید، با `file_id` ارجاع دهید
2. **بهبود عملکرد** - فایل‌ها در سمت سرور ذخیره می‌شوند، فراخوانی‌های API سریع‌تر
3. **کاهش سربار شبکه** - بدون سربار کدگذاری Base64 در هر درخواست
4. **قابل استفاده مجدد در اندپوینت‌های مختلف** - با `v1/chat/completions`، `v1/responses`، `v1/messages`، `v1/ocr`، `v1/images/edits` کار می‌کند

### آپلود فایل

```bash
curl https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F purpose="user_data" \
  -F file="@document.pdf"

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# آپلود فایل
file = client.files.create(file=open("document.pdf", "rb"), purpose="user_data")

print(f"فایل با شناسه آپلود شد: {file.id}")

```

```javascript
import fs from "fs";
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// آپلود فایل
const file = await client.files.create({
  file: fs.createReadStream("document.pdf"),
  purpose: "user_data",
});

console.log(`فایل با شناسه آپلود شد: ${file.id}`);

```

```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// آپلود فایل
	fileReq := openai.FileRequest{
		FilePath: "document.pdf",
		Purpose:  "user_data",
	}
	file, err := client.CreateFile(context.Background(), fileReq)
	if err != nil {
		fmt.Printf("خطا در آپلود فایل: %v\n", err)
		return
	}
	fmt.Printf("فایل با شناسه آپلود شد: %s\n", file.ID)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// آپلود فایل
$file = $client->files()->create([
    'purpose' => 'user_data',
    'file' => fopen('document.pdf', 'r'),
]);

echo "فایل با شناسه آپلود شد: " . $file->id . "\n";

```


### استفاده از شناسه فایل در Chat Completions

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-5.6-luna",
  "messages": [
    {
      "role": "user",
      "content": [
        {
          "type": "text",
          "text": "این سند را خلاصه کنید"
        },
        {
          "type": "file",
          "file": {
            "file_id": "file-abc123xyz"
          }
        }
      ]
    }
  ]
}'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

# با فرض اینکه فایل قبلا با شناسه "file-abc123xyz" آپلود شده است
file_id = "file-abc123xyz"

response = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این سند را خلاصه کنید"},
                {"type": "file", "file": {"file_id": file_id}},
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

// با فرض اینکه فایل قبلا با شناسه "file-abc123xyz" آپلود شده است
const fileId = "file-abc123xyz";

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    {
      role: "user",
      content: [
        { type: "text", text: "این سند را خلاصه کنید" },
        { type: "file", file: { file_id: fileId } },
      ],
    },
  ],
});

console.log(response.choices[0].message.content);

```

```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	// با فرض اینکه فایل قبلا آپلود شده است
	fileID := "file-abc123xyz"

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			model: "gpt-5.6-luna",
			Messages: []openai.ChatCompletionMessage{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ChatMessageContent{
						{
							Type: "text",
							Text: "این سند را خلاصه کنید",
						},
						{
							Type: "file",
							File: &openai.ChatMessageFile{
								FileID: fileID,
							},
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.Choices[0].Message.Content)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

// با فرض اینکه فایل قبلا آپلود شده است
$fileId = 'file-abc123xyz';

$response = $client->chat()->create([
    'model' => 'gpt-5.6-luna',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کنید'],
                ['type' => 'file', 'file' => ['file_id' => $fileId]]
            ]
        ]
    ]
]);

echo $response->choices[0]->message->content;

```


### استفاده از شناسه فایل در Responses API

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-5.6-luna",
  "input": [
    {
      "role": "user",
      "content": [
        {
          "type": "input_file",
          "file_id": "file-abc123xyz"
        },
        {
          "type": "input_text",
          "text": "اولین موضوع در این سند چیست؟"
        }
      ]
    }
  ]
}'

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

file_id = "file-abc123xyz"

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {
            "role": "user",
            "content": [
                {"type": "input_file", "file_id": file_id},
                {"type": "input_text", "text": "اولین موضوع در این سند چیست؟"},
            ],
        }
    ],
)

print(response.output_text)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const fileId = "file-abc123xyz";

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: [
        { type: "input_file", file_id: fileId },
        { type: "input_text", text: "اولین موضوع در این سند چیست؟" },
      ],
    },
  ],
});

console.log(response.output_text);

```

```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"

	fileID := "file-abc123xyz"

	resp, err := client.CreateResponse(
		context.Background(),
		openai.ResponseRequest{
			model: "gpt-5.6-luna",
			Input: []openai.ResponseInput{
				{
					Role: openai.ChatMessageRoleUser,
					Content: []openai.ResponseContent{
						{
							Type:   "input_file",
							FileID: fileID,
						},
						{
							Type: "input_text",
							Text: "اولین موضوع در این سند چیست؟",
						},
					},
				},
			},
		},
	)

	if err != nil {
		fmt.Printf("خطا: %v\n", err)
		return
	}

	fmt.Println(resp.OutputText)
}

```

```php
<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$fileId = 'file-abc123xyz';

$response = $client->responses()->create([
    'model' => 'gpt-5.6-luna',
    'input' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'input_file', 'file_id' => $fileId],
                ['type' => 'input_text', 'text' => 'اولین موضوع در این سند چیست؟']
            ]
        ]
    ]
]);

echo $response->outputText;

```


## ملاحظات خاص مدل‌ها

### مدل‌های Gemini

- **Base64 اجباری**: مدل‌های Gemini نیاز به تصاویر کدگذاری شده با Base64 دارند؛ ورودی‌های تصویر مبتنی بر URL پشتیبانی نمی‌شوند
- **محدودیت کل**: ۲۰ مگابایت کل داده‌های فایل درون‌خطی در یک درخواست
- **تعداد فایل**: تا ۳۶۰۰ فایل تصویری در هر درخواست برای Gemini 2.5 Pro، 2.0 Flash، 1.5 Pro و 1.5 Flash

### مدل‌های OpenAI

- برای `/v1/responses`، برای سندهای عمومی از `input_file.file_url`، برای فایل‌های آپلودشده با `purpose="user_data"` از `input_file.file_id`، و برای سندهای Base64 درون‌خطی از `input_file.filename` همراه با `input_file.file_data` استفاده کنید.
- پردازش PDF که تصویر صفحه‌ها را هم وارد context می‌کند به مدل‌های vision-capable مانند `gpt-5.5` یا `gpt-5.4` نیاز دارد.
- ورودی‌های سند غیر PDF معمولا text-extract می‌شوند؛ تصاویر embedشده و نمودارها قابل اتکا نیستند مگر اینکه ابتدا سند را به PDF تبدیل کنید.
- برای مجموعه‌های بزرگ یا تکرارشونده سندها، به‌جای ارسال همه اسناد به صورت مستقیم در context با `input_file`، از retrieval روی فایل‌های chunkشده استفاده کنید.

### مدل‌های Anthropic (Claude)

- پشتیبانی از هر دو روش URL و Base64 برای PDFها و تصاویر
- محدودیت ۳۲ مگابایت در هر درخواست

### Mistral OCR

- پشتیبانی تا ۵۰ مگابایت به ازای هر سند
- امکان پردازش تا ۱۰۰۰ صفحه در هر سند
- پشتیبانی از هر دو نوع `document_url` و `image_url`

## بهترین شیوه‌ها

1. **انتخاب روش مناسب**:
   - از **URLها** برای فایل‌های با دسترسی عمومی استفاده کنید تا اندازه درخواست کاهش یابد
   - از **Base64** برای فایل‌های محلی زیر محدودیت‌های اندازه استفاده کنید
   - از **شناسه فایل** برای فایل‌های بزرگ یا زمانی که محتوا را مجددا استفاده می‌کنید، استفاده کنید

2. **مدیریت محدودیت‌های اندازه**:
   - قبل از ارسال اندازه فایل را بررسی کنید
   - در صورت امکان تصاویر را فشرده کنید
   - اسناد بزرگ را به قطعات کوچکتر تقسیم کنید
   - برای فایل‌های زیاد یا پرسش‌های تکراری از knowledge base، retrieval را ترجیح دهید

3. **بهینه‌سازی عملکرد**:
   - URLها ممکن است به دلیل واکشی شبکه تاخیر ایجاد کنند
   - Base64 اندازه بدنه درخواست را حدود ۳۳٪ افزایش می‌دهد
   - شناسه‌های فایل برای استفاده مکرر کارآمدترین هستند

4. **مدیریت خطا**:
   - قبل از کدگذاری نوع MIME را اعتبارسنجی کنید
   - خطاهای کدگذاری را به درستی مدیریت کنید
   - فرمت‌های فایل پشتیبانی شده برای هر مدل را بررسی کنید

## عیب‌یابی

### تجاوز از اندازه فایل

```
Error: File size exceeds maximum allowed limit
```

**راه‌حل**: جدول محدودیت‌های اندازه فایل در بالا را بررسی کنید. برای فایل‌های بزرگتر از Files API استفاده کنید یا فایل را فشرده کنید.

### نوع MIME نامعتبر

```
Error: Unsupported file type
```

**راه‌حل**: مطمئن شوید که از نوع MIME پشتیبانی شده استفاده می‌کنید. پسوند فایل و فرمت کدگذاری را دوباره بررسی کنید.

### مشکلات کدگذاری Base64

```
Error: Invalid base64 encoding
```

**راه‌حل**:
- مطمئن شوید که در رشته base64 خط جدید وجود ندارد (در لینوکس از `-w 0` یا `| tr -d '\n'` استفاده کنید)
- بررسی کنید که فرمت data URL درست باشد: `data:{mime_type};base64,{data}`

### عدم دسترسی به URL

```
Error: Unable to fetch file from URL
```

**راه‌حل**:
- مطمئن شوید که URL به صورت عمومی قابل دسترسی است (بدون نیاز به احراز هویت)
- بررسی کنید که URL نوع محتوای صحیح را برمی‌گرداند
- تأیید کنید که URL از HTTPS استفاده می‌کند

## منابع مرتبط

- [راهنمای ورودی‌های فایل PDF](fa/guides/pdf-files.md)
- [راهنمای بینایی](fa/guides/vision.md)
- [راهنمای پردازش صوت](fa/guides/audio-processing.md)
- [API Chat Completions](fa/api-reference/chat.md)
- [API Responses](fa/api-reference/responses.md)
- [API Messages](fa/api-reference/messages.md)
- [API OCR](fa/api-reference/ocr.md)
- [پردازش فایل‌های اکسل](fa/examples/processing_excel_files_in_chat_completion_api.md)
- [پردازش PDFها در Chat Completions](fa/examples/processing_pdfs_in_chat_completion_api.md)
