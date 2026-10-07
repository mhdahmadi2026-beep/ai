# مرجع API فایل‌ها (Files)

API فایل‌ها به شما امکان می‌دهد فایل‌ها را آپلود، لیست، بازیابی و حذف کنید تا در نقاط پایانی مختلف AvalAI استفاده شوند. این اولین لایه سرویس بومی AvalAI است که یک سیستم مدیریت فایل سازگار با OpenAI ارائه می‌دهد که به طور یکپارچه با بیش از 26 ارائه‌دهنده و بیش از 410 مدل کار می‌کند.

> **وضعیت Files API**: مسیر `v1/files` برای upload، فهرست‌کردن، دریافت، حذف و استفاده دوباره از فایل‌ها در routeهای پشتیبانی‌شده AvalAI در دسترس است. قیمت‌گذاری، سهمیه ذخیره‌سازی و سازگاری مدل می‌تواند به سطح حساب و endpoint وابسته باشد؛ محدودیت‌های همین صفحه را بررسی کنید و برای نیازهای حسابی با [t.me/AvalAISupport](https://t.me/AvalAISupport) تماس بگیرید.

## چرا از API فایل‌ها استفاده کنیم؟

استفاده از API فایل‌ها به جای ورودی‌های فایل base64 یا URL درون‌خطی مزایای متعددی دارد:

1. **جلوگیری از انتقال مکرر فایل‌های بزرگ** - یک بار آپلود کنید، در درخواست‌های بعدی با `file_id` ارجاع دهید
2. **بهبود عملکرد** - فایل‌ها در سمت سرور ذخیره و به صورت داخلی بازیابی می‌شوند، که تأخیر را کاهش می‌دهد
3. **کاهش سربار شبکه** - کدگذاری Base64 حجم فایل را حدود ۳۳٪ افزایش می‌دهد؛ استفاده از `file_id` فقط یک رشته کوتاه است
4. **قابل استفاده مجدد در نقاط پایانی مختلف** - با `v1/chat/completions`، `v1/responses`، `v1/messages`، `v1/ocr` و `v1/images/edits` کار می‌کند

## آدرس پایه (Base URL)

```
https://api.avalai.ir/v1
```

## احراز هویت (Authentication)

تمام درخواست‌های API فایل‌ها نیاز به احراز هویت از طریق توکن Bearer دارند:

```http
Authorization: Bearer YOUR_AVALAI_API_KEY
```

## نقاط پایانی پشتیبانی شده

فایل‌های آپلود شده از طریق API فایل‌ها می‌توانند با نقاط پایانی زیر استفاده شوند:

| نقطه پایانی | توضیحات |
|-------------|---------|
| `v1/chat/completions` | تکمیل گفتگو سازگار با OpenAI |
| `v1/responses` | API پاسخ‌های OpenAI |
| `v1/messages` | API پیام‌های Anthropic |
| `v1/ocr` | نقطه پایانی پردازش OCR |
| `v1/images/edits` | نقاط پایانی ویرایش تصویر |

---

## آپلود فایل (Upload File)

یک فایل آپلود کنید که می‌تواند در نقاط پایانی مختلف استفاده شود.

```
POST https://api.avalai.ir/v1/files
```

### بدنه درخواست (فرم چندبخشی)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `file` | file | بله | شی فایل برای آپلود. حداکثر اندازه: ۱۲۸ مگابایت برای هر آپلود. |
| `purpose` | string | بله | هدف مورد نظر فایل آپلود شده. به [اهداف پشتیبانی شده](#اهداف-پشتیبانی-شده) مراجعه کنید. |
| `expires_after` | object | خیر | سیاست انقضا اختیاری برای فایل. |

### اهداف پشتیبانی شده

| هدف | توضیحات |
|-----|---------|
| `assistants` | استفاده در API دستیاران |
| `batch` | استفاده در API دسته‌ای |
| `fine-tune` | استفاده برای تنظیم دقیق مدل‌ها |
| `vision` | تصاویر برای تنظیم دقیق بینایی |
| `user_data` | نوع فایل انعطاف‌پذیر برای هر هدفی |
| `evals` | استفاده برای مجموعه داده‌های ارزیابی |
| `others` | مخصوص AvalAI: هدف عمومی برای هر مورد استفاده دیگر |

### انتخاب هدف مناسب

- برای فایل‌هایی که می‌خواهید به‌عنوان ورودی مدل `input_file` در `/v1/responses` یا routeهای پشتیبانی‌شده دیگر بفرستید، از `user_data` استفاده کنید.
- از `batch` فقط برای فایل‌های JSONL استفاده کنید که ورودی Batch API خواهند شد؛ فایل‌های batch از سیاست انقضای ارائه‌دهنده پیروی می‌کنند و رفتار مرجع OpenAI انقضای پیش‌فرض ۳۰ روزه است.
- از `assistants` فقط برای File Search میزبانی‌شده یا workflowهای vector-store شبیه Assistants استفاده کنید، آن هم وقتی این سطح‌ها فعال باشند.
- از `fine-tune` فقط برای datasetهای آموزشی یا validation با فرمت JSONL استفاده کنید که با schema الزامی route تنظیم دقیق انتخاب‌شده سازگار باشند.
- از `vision` فقط برای workflowهای تصویری‌ای استفاده کنید که به ذخیره‌سازی تصویر در File API نیاز دارند؛ نوع‌های رایج پشتیبانی‌شده در جریان‌های vision سازگار با OpenAI شامل `png`، `jpg`، `gif` و `webp` هستند و فقط مدل‌های vision-capable می‌توانند آن‌ها را مصرف کنند.
- فایل‌هایی را که دیگر لازم ندارید حذف کنید. فایل‌های غیر batch ممکن است تا حذف دستی باقی بمانند، مگر اینکه `expires_after` تنظیم کنید. برای برنامه‌ریزی retention، [کنترل داده‌ها](fa/guides/data-controls.md) را ببینید.

### قواعد فایل سازگار با OpenAI

Files API مرجع OpenAI چند سطح مصرف downstream را پشتیبانی می‌کند، اما هر سطح محدودیت فایل خودش را دارد. پیش از عرضه، مثال‌های upstream را با محدودیت‌های فعلی routeهای AvalAI تطبیق دهید:

| سطح مصرف | قاعده عملی |
|----------|------------|
| ورودی مستقیم فایل در `/v1/responses` | از `purpose="user_data"` استفاده کنید و فایل را به شکل `input_file` با `file_id` ارجاع دهید؛ وقتی reuse لازم نیست، `file_url` و base64 `file_data` جایگزین هستند. |
| Batch API | فقط از فایل‌های JSONL درخواست استفاده کنید؛ در مرجع OpenAI محدودیت Batch API برای فایل ورودی 200MB است، اما محدودیت حساب/آپلود AvalAI ممکن است کمتر باشد. |
| Fine-tuning | از datasetهای JSONL استفاده کنید و schema دقیق chat/completions مورد نیاز endpoint تنظیم دقیق هدف را validate کنید. |
| Hosted File Search یا ابزارهای شبیه Assistants | فقط وقتی سطح retrieval/vector-store میزبانی‌شده برای حساب شما فعال است، از `purpose="assistants"` استفاده کنید. |
| جریان‌های تصویر و vision | از مدل‌های image-capable و MIME typeهای تصویری پشتیبانی‌شده استفاده کنید؛ ابزارها به‌صورت خودکار محتوای تصویر را نمی‌خوانند مگر اینکه route فایل را صریحا به همان ابزار attach کند. |

### شی سیاست انقضا (Expiration Policy Object)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `anchor` | string | بله | نقطه لنگر برای انقضا. در حال حاضر فقط `"created_at"` پشتیبانی می‌شود. |
| `seconds` | integer | بله | تعداد ثانیه‌ها پس از زمان لنگر که فایل منقضی می‌شود. |

### مثال‌ها

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
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

# آپلود یک فایل
file = client.files.create(file=open("document.pdf", "rb"), purpose="user_data")

print(f"فایل آپلود شد: {file.id}")

# آپلود با انقضا (۳۰ روز)
file_with_expiry = client.files.create(
    file=open("temp_data.jsonl", "rb"),
    purpose="batch",
    expires_after={"anchor": "created_at", "seconds": 2592000},  # ۳۰ روز
)

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// آپلود یک فایل
const file = await client.files.create({
    file: fs.createReadStream("document.pdf"),
    purpose: "user_data",
});

console.log(`فایل آپلود شد: ${file.id}`);

// آپلود با انقضا (۳۰ روز)
const fileWithExpiry = await client.files.create({
    file: fs.createReadStream("temp_data.jsonl"),
    purpose: "batch",
    expires_after: {
        anchor: "created_at",
        seconds: 2592000,
    },
});

```

```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"io"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	file, err := os.Open("document.pdf")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	uploaded, err := client.Files.New(context.Background(), openai.FileNewParams{
		File:    openai.F[io.Reader](file),
		Purpose: openai.F(openai.FilePurposeUserData),
	})
	if err != nil {
		panic(err)
	}

	fmt.Printf("فایل آپلود شد: %s\n", uploaded.ID)
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/files';

$file = new CURLFile('document.pdf', 'application/pdf', 'document.pdf');

$data = [
    'file' => $file,
    'purpose' => 'user_data'
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $data);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
curl_close($ch);

if ($httpcode >= 400) {
    echo "خطا: " . $httpcode . "\n";
    echo $response;
} else {
    $fileData = json_decode($response, true);
    echo "فایل آپلود شد: " . $fileData['id'] . "\n";
}
?>

```


### پاسخ (Response)

```json
{
  "id": "file-EyVi0MrxuKTgBrvkVas5ZTGz",
  "object": "file",
  "bytes": 13264,
  "created_at": 1767210968,
  "expires_at": null,
  "filename": "document.pdf",
  "purpose": "user_data",
  "status": null,
  "status_details": null
}
```

---

## لیست فایل‌ها (List Files)

لیستی از فایل‌های متعلق به سازمان شما را برمی‌گرداند.

```
GET https://api.avalai.ir/v1/files
```

### پارامترهای کوئری (Query Parameters)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `purpose` | string | خیر | فیلتر بر اساس هدف (مثلا `user_data`، `fine-tune`). |
| `limit` | integer | خیر | تعداد فایل‌ها برای بازیابی (۱-۱۰۰۰۰). پیش‌فرض: ۱۰۰۰۰. |
| `order` | string | خیر | ترتیب مرتب‌سازی بر اساس `created_at`. یکی از `asc` یا `desc`. پیش‌فرض: `desc`. |
| `after` | string | خیر | یک مکان‌نما برای صفحه‌بندی. فایل‌ها را بعد از این شناسه فایل دریافت کنید. |

### مثال‌ها

```bash
# لیست تمام فایل‌ها
curl https://api.avalai.ir/v1/files \
  -H "Authorization: Bearer $AVALAI_API_KEY"

# لیست فایل‌ها با هدف خاص
curl "https://api.avalai.ir/v1/files?purpose=user_data&limit=10" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

# لیست تمام فایل‌ها
files = client.files.list()
for file in files.data:
    print(f"{file.id}: {file.filename} ({file.bytes} بایت)")

# لیست فایل‌ها با هدف خاص
user_files = client.files.list(purpose="user_data")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// لیست تمام فایل‌ها
const files = await client.files.list();
for (const file of files.data) {
    console.log(`${file.id}: ${file.filename} (${file.bytes} بایت)`);
}

// لیست فایل‌ها با هدف خاص
const userFiles = await client.files.list({ purpose: "user_data" });

```

```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	files, err := client.Files.List(context.Background(), openai.FileListParams{})
	if err != nil {
		panic(err)
	}

	for _, file := range files.Data {
		fmt.Printf("%s: %s (%d بایت)\n", file.ID, file.Filename, file.Bytes)
	}
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/files';

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$data = json_decode($response, true);
foreach ($data['data'] as $file) {
    echo $file['id'] . ": " . $file['filename'] . " (" . $file['bytes'] . " بایت)\n";
}
?>

```


### پاسخ (Response)

```json
{
  "object": "list",
  "data": [
    {
      "id": "file-EyVi0MrxuKTgBrvkVas5ZTGz",
      "object": "file",
      "bytes": 13264,
      "created_at": 1767210968,
      "expires_at": null,
      "filename": "document.pdf",
      "purpose": "user_data",
      "status": null,
      "status_details": null
    },
    {
      "id": "file-NWU5LYel4DIxFCITnrVRLLcA",
      "object": "file",
      "bytes": 53,
      "created_at": 1766585221,
      "expires_at": null,
      "filename": "mydata.jsonl",
      "purpose": "fine-tune",
      "status": null,
      "status_details": null
    }
  ],
  "first_id": "file-EyVi0MrxuKTgBrvkVas5ZTGz",
  "last_id": "file-NWU5LYel4DIxFCITnrVRLLcA",
  "has_more": false
}
```

---

## بازیابی فایل (Retrieve File)

اطلاعات یک فایل خاص را برمی‌گرداند.

```
GET https://api.avalai.ir/v1/files/{file_id}
```

### پارامترهای مسیر (Path Parameters)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `file_id` | string | بله | شناسه فایل برای بازیابی. |

### مثال‌ها

```bash
curl https://api.avalai.ir/v1/files/file-abc123 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

file = client.files.retrieve("file-abc123")
print(f"نام فایل: {file.filename}")
print(f"اندازه: {file.bytes} بایت")
print(f"هدف: {file.purpose}")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const file = await client.files.retrieve("file-abc123");
console.log(`نام فایل: ${file.filename}`);
console.log(`اندازه: ${file.bytes} بایت`);
console.log(`هدف: ${file.purpose}`);

```

```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	file, err := client.Files.Get(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	fmt.Printf("نام فایل: %s\n", file.Filename)
	fmt.Printf("اندازه: %d بایت\n", file.Bytes)
	fmt.Printf("هدف: %s\n", file.Purpose)
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$file = json_decode($response, true);
echo "نام فایل: " . $file['filename'] . "\n";
echo "اندازه: " . $file['bytes'] . " بایت\n";
echo "هدف: " . $file['purpose'] . "\n";
?>

```


### پاسخ (Response)

```json
{
  "id": "file-EyVi0MrxuKTgBrvkVas5ZTGz",
  "object": "file",
  "bytes": 13264,
  "created_at": 1767210968,
  "expires_at": null,
  "filename": "document.pdf",
  "purpose": "user_data",
  "status": null,
  "status_details": null
}
```

---

## حذف فایل (Delete File)

یک فایل را از فضای ذخیره‌سازی سازمان شما حذف می‌کند.

```
DELETE https://api.avalai.ir/v1/files/{file_id}
```

### پارامترهای مسیر (Path Parameters)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `file_id` | string | بله | شناسه فایل برای حذف. |

### مثال‌ها

```bash
curl -X DELETE https://api.avalai.ir/v1/files/file-abc123 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

deleted = client.files.delete("file-abc123")
print(f"حذف شد: {deleted.deleted}")

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

const deleted = await client.files.del("file-abc123");
console.log(`حذف شد: ${deleted.deleted}`);

```

```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	deleted, err := client.Files.Delete(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	fmt.Printf("حذف شد: %v\n", deleted.Deleted)
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE");
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo "حذف شد: " . ($result['deleted'] ? 'بله' : 'خیر') . "\n";
?>

```


### پاسخ (Response)

```json
{
  "id": "file-abc123",
  "object": "file",
  "deleted": true
}
```

---

## بازیابی محتوای فایل (Retrieve File Content)

محتوای یک فایل را دانلود می‌کند.

```
GET https://api.avalai.ir/v1/files/{file_id}/content
```

### پارامترهای مسیر (Path Parameters)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `file_id` | string | بله | شناسه فایل برای دانلود. |

### مثال‌ها

```bash
# دانلود محتوای فایل
curl https://api.avalai.ir/v1/files/file-abc123/content \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  --output downloaded_file.pdf

```

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

# دانلود محتوای فایل
content = client.files.content("file-abc123")

# ذخیره در فایل
with open("downloaded_file.pdf", "wb") as f:
    f.write(content.read())

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import fs from "fs";
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// دانلود محتوای فایل
const content = await client.files.content("file-abc123");
const buffer = Buffer.from(await content.arrayBuffer());
fs.writeFileSync("downloaded_file.pdf", buffer);

```

```go
// مثال Go
package main

import (
	"context"
	"io"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	content, err := client.Files.Content(context.Background(), "file-abc123")
	if err != nil {
		panic(err)
	}

	file, err := os.Create("downloaded_file.pdf")
	if err != nil {
		panic(err)
	}
	defer file.Close()

	io.Copy(file, content.Body)
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$fileId = 'file-abc123';
$apiUrl = "https://api.avalai.ir/v1/files/{$fileId}/content";

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Authorization: Bearer ' . $apiKey,
]);

$content = curl_exec($ch);
curl_close($ch);

file_put_contents('downloaded_file.pdf', $content);
echo "فایل با موفقیت دانلود شد\n";
?>

```


---

## شی فایل (File Object)

شی فایل یک سند را نشان می‌دهد که به AvalAI آپلود شده است.

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه منحصر به فرد برای فایل (مثلا `file-EyVi0MrxuKTgBrvkVas5ZTGz`). |
| `object` | string | نوع شی، همیشه `"file"`. |
| `bytes` | integer | اندازه فایل به بایت. |
| `created_at` | integer | زمان‌سنج Unix هنگام ایجاد فایل. |
| `expires_at` | integer یا null | زمان‌سنج Unix هنگام انقضای فایل، یا null اگر منقضی نمی‌شود. |
| `filename` | string | نام فایل. |
| `purpose` | string | هدف مورد نظر فایل. |
| `status` | string یا null | وضعیت فایل (استفاده برای عملیات ناهمزمان). |
| `status_details` | string یا null | جزئیات اضافی درباره وضعیت. |

---

## محدودیت‌های نرخ (Rate Limits)

عملیات فایل بر اساس سطح حساب شما محدود می‌شود:

### محدودیت‌های نرخ عملیات (در دقیقه)

| سطح | آپلودها | دانلودها | حذف‌ها |
|-----|---------|----------|--------|
| ۰ (رایگان) | ۳ | ۵ | ۱۰ |
| ۱ | ۱۰ | ۱۰۰ | ۱۰۰ |
| ۲ | ۵۰ | ۲۵۰ | ۲۵۰ |
| ۳ | ۲۵۰ | ۵۰۰ | ۵۰۰ |
| ۴ | ۵۰۰ | ۱٬۰۰۰ | ۱٬۰۰۰ |
| ۵ | ۱٬۵۰۰ | ۲٬۰۰۰ | ۵٬۰۰۰ |

### محدودیت‌های ذخیره‌سازی بر اساس سطح

هر سطح حساب یک محدودیت کل فضای ذخیره‌سازی دارد. پس از اتمام، آپلودها مسدود می‌شوند تا:
- فضای ذخیره‌سازی را با حذف فایل‌ها آزاد کنید، یا
- به سطح بالاتر ارتقا دهید

| سطح | حداکثر فضای ذخیره‌سازی |
|-----|------------------------|
| ۰ (رایگان) | ۲۵۰ مگابایت |
| ۱ | ۲ گیگابایت |
| ۲ | ۵ گیگابایت |
| ۳ | ۱۵ گیگابایت |
| ۴ | ۵۰ گیگابایت |
| ۵ | ۲۰۰ گیگابایت |

برای اطلاعات بیشتر درباره سطوح، به [محدودیت‌های نرخ](fa/guides/rate-limits.md) مراجعه کنید.

---

## استفاده از فایل‌ها در فراخوانی‌های API

پس از آپلود یک فایل، می‌توانید با `file_id` در نقاط پایانی پشتیبانی شده به آن ارجاع دهید.

> **⚠️ نکته سازگاری مدل**: پشتیبانی فایل به endpoint و مدل انتخابی وابسته است. در `/v1/responses`، برای فایل‌های آپلودشده با `purpose="user_data"` از `input_file.file_id`، برای سندهای عمومی از `input_file.file_url`، و برای سندهای Base64 درون‌خطی از `input_file.filename` همراه با `input_file.file_data` استفاده کنید. مدل‌های OpenAI دارای قابلیت بینایی می‌توانند از آیتم‌های PDF `input_file` استفاده کنند که متن استخراج‌شده را همراه تصویر صفحه‌ها وارد context می‌کند؛ سندهای غیر PDF معمولا text-extract می‌شوند و spreadsheetها را باید context خلاصه/augmented بدانید، نه داده دقیق همه سلول‌ها. در `/v1/chat/completions`، مدل‌های Gemini و سایر مدل‌های سندمحور همچنان می‌توانند انتخاب مناسب‌تری برای file partهای PDF باشند. مستندات مدل را بررسی کنید و برای مجموعه سندهای بزرگ از retrieval استفاده کنید.

### مثال: تکمیل گفتگو با فایل

```bash
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
            "text": "این سند را خلاصه کن"
          },
          {
            "type": "file",
            "file": {
              "file_id": "file-EyVi0MrxuKTgBrvkVas5ZTGz"
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
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)

# استفاده از فایل آپلود شده در تکمیل گفتگو
# نکته: پشتیبانی فایل به مدل و endpoint انتخابی وابسته است.
# Gemini همچنان انتخاب خوبی برای file partهای PDF در Chat Completions است.
response = client.chat.completions.create(
    model="gemini-2.5-flash",
    messages=[
        {
            "role": "user",
            "content": [
                {"type": "text", "text": "این سند را خلاصه کن"},
                {"type": "file", "file": {"file_id": "file-EyVi0MrxuKTgBrvkVas5ZTGz"}},
            ],
        }
    ],
)

print(response.choices[0].message.content)

```

```javascript
// مثال جاوااسکریپت (JavaScript)
import OpenAI from "openai";

const client = new OpenAI({
    apiKey: process.env.AVALAI_API_KEY,
    baseURL: "https://api.avalai.ir/v1",
});

// استفاده از فایل آپلود شده در تکمیل گفتگو
const response = await client.chat.completions.create({
    model: "gemini-2.5-flash",
    messages: [
        {
            role: "user",
            content: [
                { type: "text", text: "این سند را خلاصه کن" },
                { type: "file", file: { file_id: "file-abc123" } },
            ],
        },
    ],
});

console.log(response.choices[0].message.content);

```

```go
// مثال Go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	// استفاده از فایل آپلود شده در تکمیل گفتگو
	response, err := client.Chat.Completions.New(context.Background(), openai.ChatCompletionNewParams{
		Model: openai.F("gemini-2.5-flash"),
		Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
			openai.UserMessageParts(
				openai.TextPart("این سند را خلاصه کن"),
				openai.FilePart("file-abc123"),
			),
		}),
	})
	if err != nil {
		panic(err)
	}

	fmt.Println(response.Choices[0].Message.Content)
}

```

```php
<?php
// مثال PHP

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
    'model' => 'gemini-2.5-flash',
    'messages' => [
        [
            'role' => 'user',
            'content' => [
                ['type' => 'text', 'text' => 'این سند را خلاصه کن'],
                ['type' => 'file', 'file' => ['file_id' => 'file-abc123']],
            ],
        ],
    ],
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey,
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'] . "\n";
?>

```


<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `gemini-2.5-flash` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


---

## محدودیت‌ها

### محدودیت‌های فعلی

- **حداکثر اندازه فایل**: ۱۲۸ مگابایت در هر آپلود
- **محدودیت‌های ذخیره‌سازی**: بر اساس سطح (۲۵۰ مگابایت تا ۲۰۰ گیگابایت)
- **مثال‌های upstream ممکن است بزرگ‌تر باشند**: مستندات مرجع OpenAI برای بعضی محصولات محدودیت‌های per-file و project-level بزرگ‌تری ذکر می‌کند؛ این صفحه محدودیت‌های عمومی آپلود فایل و tierهای AvalAI را مستند می‌کند.

### نقاط پایانی پشتیبانی شده

در حال حاضر شناسه‌های فایل می‌توانند با موارد زیر استفاده شوند:
- `v1/chat/completions`
- `v1/responses`
- `v1/messages`
- `v1/ocr`
- `v1/images/edits`

---

## ذخیره‌سازی و امنیت

### زیرساخت ذخیره‌سازی

فایل‌ها در ارائه‌دهندگان ابری سطح سازمانی ذخیره می‌شوند:
- **AWS S3**
- **Google Cloud Platform (GCP)**
- **Cloudflare**

### امنیت

- فایل‌های آپلودشده را داده مشتری بدانید: secretها را فقط وقتی برای کار لازم هستند آپلود کنید، برای پردازش موقت از پنجره‌های کوتاه `expires_after` استفاده کنید و پس از پایان workflow فایل‌ها را حذف کنید.
- فرض نکنید همه providerها یا ابزارهای downstream رفتار retention یکسان دارند. پیش از ارسال فایل‌های regulated یا بسیار حساس، route، مدل و کنترل‌های حساب انتخاب‌شده را بررسی کنید.
- برای workloadهای حساس، به جای base64 درون logها و promptها از file ID استفاده کنید و filename یا metadataهایی را که ممکن است داده شخصی داشته باشند redaction کنید.

### گزارش امنیتی

اگر یک آسیب‌پذیری امنیتی کشف کردید، لطفا گزارش دهید به:
- **ایمیل**: security@avalai.ir
- **پاداش باگ** برای مسائل امنیتی بحرانی که می‌توانند داده‌های کاربران را در خطر قرار دهند در دسترس است

---

## مدیریت خطا (Error Handling)

| کد وضعیت | توضیحات |
|----------|---------|
| 400 | درخواست نامعتبر - فایل نامعتبر یا پارامترهای ناقص |
| 401 | غیرمجاز - کلید API نامعتبر |
| 403 | ممنوع - شما اجازه دسترسی به این فایل را ندارید |
| 404 | یافت نشد - فایل یافت نشد |
| 413 | حجم بیش از حد مجاز - فایل از محدودیت ۱۲۸ مگابایت بیشتر است |
| 429 | تعداد درخواست بیش از حد - محدودیت نرخ تجاوز شده |
| 507 | فضای ذخیره‌سازی ناکافی - محدودیت ذخیره‌سازی برای سطح شما تجاوز شده |

---

## منابع مرتبط

- [راهنمای ورودی‌های فایل](fa/guides/file-inputs.md) - درباره روش‌های مختلف ارائه ورودی‌های فایل بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - محدودیت‌های نرخ و سطوح را درک کنید
- [تکمیل گفتگو](fa/api-reference/chat.md) - از فایل‌ها در تکمیل گفتگو استفاده کنید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید

---

## پشتیبانی

- **گزارش باگ**: [t.me/AvalAISupport](https://t.me/AvalAISupport)
- **مسائل امنیتی**: security@avalai.ir
