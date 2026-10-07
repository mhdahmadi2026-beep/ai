# مرجع API تشخیص متن (OCR)

API تشخیص متن (OCR) محتوای ساختاریافته را با Mistral OCR 4 از اسناد و تصاویر استخراج می‌کند. مدل `mistral-ocr-4-0` علاوه بر Markdown، اطلاعات layout-aware مانند bounding box، طبقه‌بندی بلوک و confidence را برمی‌گرداند و از ۱۷۰ زبان پشتیبانی می‌کند.

> **توجه:** endpoint `v1/ocr` یک endpoint استاندارد OpenAI نیست. این یک سرویس تخصصی است که توسط AvalAI برای پردازش اسناد اضافه شده است.
>
> **به‌روزرسانی alias:** `mistral-ocr-latest` اکنون به `mistral-ocr-4-0` اشاره می‌کند و با قیمت OCR 4 محاسبه می‌شود. برای استقرار قابل بازتولید از `mistral-ocr-4-0` استفاده کنید.

## Endpoint

```
POST https://api.avalai.ir/v1/ocr
```

## بدنه درخواست

| پارامتر | نوع | الزامی | توضیحات |
| ------- | --- | ------ | ------- |
| `model` | string | بله | مدل OCR مورد استفاده (مثلا "mistral-ocr-4-0") |
| `document` | object | بله | سند برای پردازش. باید شامل `type` و فیلد URL باشد |
| `document.type` | string | بله | یا "document_url" برای PDF/اسناد یا "image_url" برای تصاویر |
| `document.document_url` | string | مشروط | URL سند (اگر type برابر "document_url" باشد الزامی است) |
| `document.image_url` | string | مشروط | URL تصویر (اگر type برابر "image_url" باشد الزامی است) |
| `pages` | array | خیر | لیست شاخص‌های صفحات خاص برای پردازش (از 0 شروع می‌شود) |
| `include_image_base64` | boolean | خیر | آیا تصاویر استخراج شده به صورت base64 برگردانده شوند |
| `image_limit` | integer | خیر | حداکثر تعداد تصاویر برای بازگشت |
| `image_min_size` | integer | خیر | حداقل اندازه (به پیکسل) برای تصاویر |
| `id` | string | خیر | شناسه اختیاری برای درخواست |
| `document_annotation_format` | object | خیر | فرمت خروجی برای حاشیه‌نویسی سطح سند. رجوع کنید به [فرمت‌های پاسخ](#فرمت‌های-پاسخ) |
| `bbox_annotation_format` | object | خیر | فرمت خروجی برای حاشیه‌نویسی کادر محدوده. رجوع کنید به [فرمت‌های پاسخ](#فرمت‌های-پاسخ) |
| `extract_header` | boolean | خیر | آیا سرصفحه‌های سند استخراج شوند. پیش‌فرض: `false` |
| `extract_footer` | boolean | خیر | آیا پاورقی‌های سند استخراج شوند. پیش‌فرض: `false` |
| `table_format` | string | خیر | فرمت جداول استخراج شده: `"markdown"` یا `"html"`. پیش‌فرض: `"markdown"` |

### مدل و قیمت‌گذاری

| شناسه مدل | endpoint | استخراج OCR | Annotation |
|----------|----------|----------------|------------|
| `mistral-ocr-4-0` | `v1/ocr` | $0.004/صفحه | $0.005/صفحه annotation‌شده |
| `mistral-ocr-latest` | `v1/ocr` | alias برای `mistral-ocr-4-0` | همان قیمت OCR 4 |

### نمونه‌های فرمت سند

**برای PDF و اسناد:**

```json
{
  "type": "document_url",
  "document_url": "https://example.com/document.pdf"

}
```

**برای تصاویر:**

```json
{
  "type": "image_url",
  "image_url": "https://example.com/image.png"

}
```

**برای محتوای base64:**

```json
{
  "type": "document_url",
  "document_url": "data:application/pdf;base64,JVBERi0xLjQKJ..."
}
```

### فرمت‌های پاسخ

API OCR از خروجی ساختاریافته JSON از طریق پارامترهای `document_annotation_format` و `bbox_annotation_format` پشتیبانی می‌کند. این امکان را به شما می‌دهد که نتایج OCR را به جای markdown ساده در فرمت JSON مشخص دریافت کنید.

#### انواع فرمت

| نوع | توضیحات |
| --- | ------- |
| `text` | پیش‌فرض. خروجی متن markdown را برمی‌گرداند |
| `json_object` | حالت JSON را فعال می‌کند. خروجی مدل JSON معتبر خواهد بود. باید از طریق پیام سیستم یا کاربر به مدل دستور دهید که JSON تولید کند |
| `json_schema` | حالت JSON Schema را فعال می‌کند. تضمین می‌کند که خروجی از JSON Schema ارائه شده پیروی می‌کند |

#### شی فرمت پاسخ

```json
{
  "type": "json_schema",
  "json_schema": {
    "name": "your_schema_name",
    "schema": {
      "type": "object",
      "properties": {
        "field1": {
          "type": "string"
        },
        "field2": {
          "type": "number"
        }
      },
      "required": [
        "field1",
        "field2"
      ]
    }
  }
}
```

#### مثال: استخراج داده ساختاریافته

می‌توانید از حالت JSON Schema برای استخراج داده ساختاریافته از اسناد استفاده کنید:

```json
{
  "model": "mistral-ocr-4-0",
  "document": {
    "type": "document_url",
    "document_url": "https://example.com/invoice.pdf"

  },
  "document_annotation_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "invoice_data",
      "schema": {
        "type": "object",
        "properties": {
          "invoice_number": { "type": "string" },
          "date": { "type": "string" },
          "total_amount": { "type": "number" },
          "vendor_name": { "type": "string" },
          "line_items": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "description": { "type": "string" },
                "quantity": { "type": "number" },
                "unit_price": { "type": "number" }
              }
            }
          }
        },
        "required": ["invoice_number", "date", "total_amount"]
      }
    }
  }
}
```

هنگام استفاده از `document_annotation_format`، خروجی ساختاریافته در فیلد `document_annotation` پاسخ به صورت رشته JSON برگردانده می‌شود.

## نمونه‌ها

### درخواست ساده OCR

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2201.04234"
    }
  }'

```

```python
import requests
import os

api_key = os.getenv("AVALAI_API_KEY")

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://arxiv.org/pdf/2201.04234",
        },
    },
)

result = response.json()
for page in result["pages"]:
    print(f"Page {page['index']}: {page['markdown'][:100]}...")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://arxiv.org/pdf/2201.04234"
    }
  })
});

const result = await response.json();
result.pages.forEach(page => {
  console.log(`Page ${page.index}: ${page.markdown.substring(0, 100)}...`);
});

```

```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
)

type OCRRequest struct {
	Model    string   `json:"model"`
	Document Document `json:"document"`
}

type Document struct {
	Type        string `json:"type"`
	DocumentURL string `json:"document_url"`
}

type OCRResponse struct {
	Pages []struct {
		Index    int    `json:"index"`
		Markdown string `json:"markdown"`
	} `json:"pages"`
	Model  string `json:"model"`
	Object string `json:"object"`
}

func main() {
	apiKey := "YOUR_AVALAI_API_KEY"
	url := "https://api.avalai.ir/v1/ocr"

	reqBody := OCRRequest{
		Model: "mistral-ocr-4-0",
		Document: Document{
			Type:        "document_url",
			DocumentURL: "https://arxiv.org/pdf/2201.04234",
		},
	}

	jsonData, _ := json.Marshal(reqBody)
	req, _ := http.NewRequest("POST", url, bytes.NewBuffer(jsonData))
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, _ := io.ReadAll(resp.Body)
	var result OCRResponse
	json.Unmarshal(body, &result)

	for _, page := range result.Pages {
		fmt.Printf("Page %d: %s...\n", page.Index, page.Markdown[:100])
	}
}

```

```php
<?php

$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

$data = [
    'model' => 'mistral-ocr-4-0',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/2201.04234'
    ]
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey,
    'Content-Length: ' . strlen($jsonData)
]);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);
curl_close($ch);

if ($err) {
    echo "cURL Error: " . $err;
} elseif ($httpcode >= 400) {
    echo "HTTP Error: " . $httpcode . "\n";
    echo $response;
} else {
    $responseData = json_decode($response, true);
    foreach ($responseData['pages'] as $page) {
        echo "Page " . $page['index'] . ": " . substr($page['markdown'], 0, 100) . "...\n";
    }
}
?>

```


### پردازش صفحات خاص

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2201.04234"
    },
    "pages": [0, 1, 2]
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://arxiv.org/pdf/2201.04234",
        },
        "pages": [0, 1, 2],
    },
)

result = response.json()

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://arxiv.org/pdf/2201.04234"
    },
    pages: [0, 1, 2]
  })
});

const result = await response.json();

```


### استخراج تصاویر با OCR

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://arxiv.org/pdf/2201.04234"
    },
    "include_image_base64": true,
    "image_limit": 10,
    "image_min_size": 100
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://arxiv.org/pdf/2201.04234",
        },
        "include_image_base64": True,
        "image_limit": 10,
        "image_min_size": 100,
    },
)

result = response.json()
for page in result["pages"]:
    if page.get("images"):
        print(f"Page {page['index']} has {len(page['images'])} images")

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://arxiv.org/pdf/2201.04234"
    },
    include_image_base64: true,
    image_limit: 10,
    image_min_size: 100
  })
});

const result = await response.json();
result.pages.forEach(page => {
  if (page.images) {
    console.log(`Page ${page.index} has ${page.images.length} images`);
  }
});

```


### پردازش یک تصویر

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "image_url",
      "image_url": "https://example.com/image.png"
    }
  }'

```

```python
import requests

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {"type": "image_url", "image_url": "https://example.com/image.png"},
    },
)

result = response.json()
print(result["pages"][0]["markdown"])

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "image_url",
      image_url: "https://example.com/image.png"
    }
  })
});

const result = await response.json();
console.log(result.pages[0].markdown);

```


### استفاده از Mistral AI SDK

شما همچنین می‌توانید از SDK رسمی Mistral AI برای دسترسی به endpoint OCR با پیکربندی آن برای استفاده از URL سرور AvalAI استفاده کنید. این با SDK میسترال در پایتون و سایر زبان‌ها کار می‌کند، تا زمانی که SDK از URLهای سرور سفارشی پشتیبانی کند.

```python
from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="your-avalai-api-key")

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-4-0",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا 100 صفحه
)

print(ocr_response)
```

> **توجه:** همین رویکرد برای سایر SDKهای Mistral AI در زبان‌های مختلف (JavaScript، Go و غیره) نیز کار می‌کند، تا زمانی که اجازه تنظیم URL سرور سفارشی را بدهند. به سادگی SDK را برای اشاره به `https://api.avalai.ir` پیکربندی کنید و از کلید API AvalAI خود استفاده کنید.

برای اطلاعات بیشتر در مورد استفاده از SDKهای Mistral AI با AvalAI، [راهنمای Mistral AI SDK](fa/providers/mistralai.md) را مشاهده کنید.

### خروجی JSON ساختاریافته

از پارامتر `document_annotation_format` برای استخراج داده ساختاریافته از اسناد استفاده کنید. این برای پردازش فاکتورها، رسیدها، فرم‌ها و سایر اسناد ساختاریافته مفید است.

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://example.com/invoice.pdf"
    },
    "document_annotation_format": {
      "type": "json_schema",
      "json_schema": {
        "name": "invoice_data",
        "schema": {
          "type": "object",
          "properties": {
            "invoice_number": { "type": "string" },
            "date": { "type": "string" },
            "total_amount": { "type": "number" },
            "vendor_name": { "type": "string" }
          },
          "required": ["invoice_number", "total_amount"]
        }
      }
    }
  }'

```

```python
import requests
import json
import os

api_key = os.getenv("AVALAI_API_KEY")

# تعریف JSON Schema برای استخراج ساختاریافته
invoice_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "invoice_data",
        "schema": {
            "type": "object",
            "properties": {
                "invoice_number": {"type": "string"},
                "date": {"type": "string"},
                "total_amount": {"type": "number"},
                "vendor_name": {"type": "string"},
                "line_items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "description": {"type": "string"},
                            "quantity": {"type": "number"},
                            "unit_price": {"type": "number"},
                        },
                    },
                },
            },
            "required": ["invoice_number", "total_amount"],
        },
    },
}

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://example.com/invoice.pdf",
        },
        "document_annotation_format": invoice_schema,
    },
)

result = response.json()

# داده ساختاریافته در document_annotation به صورت رشته JSON است
if result.get("document_annotation"):
    invoice_data = json.loads(result["document_annotation"])
    print(f"شماره فاکتور: {invoice_data.get('invoice_number')}")
    print(f"مبلغ کل: {invoice_data.get('total_amount')}")

```

```javascript
const invoiceSchema = {
  type: "json_schema",
  json_schema: {
    name: "invoice_data",
    schema: {
      type: "object",
      properties: {
        invoice_number: { type: "string" },
        date: { type: "string" },
        total_amount: { type: "number" },
        vendor_name: { type: "string" },
        line_items: {
          type: "array",
          items: {
            type: "object",
            properties: {
              description: { type: "string" },
              quantity: { type: "number" },
              unit_price: { type: "number" }
            }
          }
        }
      },
      required: ["invoice_number", "total_amount"]
    }
  }
};

const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://example.com/invoice.pdf"
    },
    document_annotation_format: invoiceSchema
  })
});

const result = await response.json();

// داده ساختاریافته در document_annotation به صورت رشته JSON است
if (result.document_annotation) {
  const invoiceData = JSON.parse(result.document_annotation);
  console.log(`شماره فاکتور: ${invoiceData.invoice_number}`);
  console.log(`مبلغ کل: ${invoiceData.total_amount}`);
}

```


### جداول در فرمت HTML

می‌توانید جداول را به جای markdown در فرمت HTML استخراج کنید:

```bash
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "mistral-ocr-4-0",
    "document": {
      "type": "document_url",
      "document_url": "https://example.com/document-with-tables.pdf"
    },
    "table_format": "html"
  }'

```

```python
import requests
import os

api_key = os.getenv("AVALAI_API_KEY")

response = requests.post(
    "https://api.avalai.ir/v1/ocr",
    headers={"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"},
    json={
        "model": "mistral-ocr-4-0",
        "document": {
            "type": "document_url",
            "document_url": "https://example.com/document-with-tables.pdf",
        },
        "table_format": "html",  # جداول در فرمت HTML برگردانده می‌شوند
    },
)

result = response.json()
for page in result["pages"]:
    print(page["markdown"])  # جداول در تگ‌های <table> HTML خواهند بود

```

```javascript
const response = await fetch("https://api.avalai.ir/v1/ocr", {
  method: "POST",
  headers: {
    "Authorization": `Bearer ${process.env.AVALAI_API_KEY}`,
    "Content-Type": "application/json"
  },
  body: JSON.stringify({
    model: "mistral-ocr-4-0",
    document: {
      type: "document_url",
      document_url: "https://example.com/document-with-tables.pdf"
    },
    table_format: "html"  // جداول در فرمت HTML برگردانده می‌شوند
  })
});

const result = await response.json();
result.pages.forEach(page => {
  console.log(page.markdown);  // جداول در تگ‌های <table> HTML خواهند بود
});

```


## فرمت پاسخ

```json
{
  "pages": [
    {
      "index": 0,
      "markdown": "# عنوان سند\n\nمحتوای متنی استخراج شده...",
      "dimensions": {
        "dpi": 200,
        "height": 2200,
        "width": 1700
      },
      "images": [
        {
          "image_base64": "base64string...",
          "bbox": {
            "x": 100,
            "y": 200,
            "width": 300,
            "height": 400
          }
        }
      ]
    }
  ],
  "model": "mistral-ocr-4-0",
  "usage_info": {
    "pages_processed": 29,
    "doc_size_bytes": 3002783
  },
  "document_annotation": null,
  "object": "ocr"
}
```

## فیلدهای پاسخ

| فیلد | نوع | توضیحات |
| ---- | --- | ------- |
| `pages` | array | لیست صفحات پردازش شده با محتوای استخراج شده |
| `pages[].index` | integer | شماره صفحه (از 0 شروع می‌شود) |
| `pages[].markdown` | string | متن استخراج شده در قالب Markdown |
| `pages[].dimensions` | object | ابعاد صفحه (dpi، ارتفاع، عرض به پیکسل) |
| `pages[].images` | array | تصاویر استخراج شده از صفحه (اگر include_image_base64=true) |
| `model` | string | مدل استفاده شده برای پردازش OCR |
| `usage_info` | object | آمار پردازش (صفحات پردازش شده، اندازه سند) |
| `usage_info.pages_processed` | integer | تعداد کل صفحات پردازش شده |
| `usage_info.doc_size_bytes` | integer | اندازه سند به بایت |
| `document_annotation` | object | توضیحات اختیاری در سطح سند |
| `object` | string | همیشه "ocr" برای پاسخ‌های OCR |

### شی ابعاد صفحه

| فیلد | نوع | توضیحات |
| ---- | --- | ------- |
| `dpi` | integer | نقطه در هر اینچ (وضوح) صفحه |
| `height` | integer | ارتفاع صفحه به پیکسل |
| `width` | integer | عرض صفحه به پیکسل |

### شی تصویر

| فیلد | نوع | توضیحات |
| ---- | --- | ------- |
| `image_base64` | string | داده تصویر کدگذاری شده با base64 |
| `bbox` | object | مختصات کادر محدوده تصویر |
| `bbox.x` | integer | مختصات X گوشه بالا-چپ |
| `bbox.y` | integer | مختصات Y گوشه بالا-چپ |
| `bbox.width` | integer | عرض تصویر به پیکسل |
| `bbox.height` | integer | ارتفاع تصویر به پیکسل |

## مدیریت خطا

API ممکن است کدهای خطای مختلفی برگرداند:

| کد وضعیت | توضیحات |
| -------- | ------- |
| 400 | درخواست نامعتبر - پارامترهای نامعتبر یا URL سند اشتباه |
| 401 | غیرمجاز - کلید API نامعتبر یا وجود ندارد |
| 403 | ممنوع - مجوزهای ناکافی یا سهمیه تمام شده |
| 404 | پیدا نشد - URL سند قابل دسترسی نیست |
| 413 | بار بیش از حد بزرگ - اندازه سند از حد مجاز بیشتر است |
| 429 | درخواست‌های بیش از حد - محدودیت نرخ فراتر رفته |
| 500 | خطای داخلی سرور - خطای پردازش سمت سرور |

برای اطلاعات بیشتر در مورد مدیریت خطاها، راهنمای [مدیریت خطا](fa/guides/error-handling.md) را مشاهده کنید.

## بهترین روش‌ها

1. **مشخص کردن صفحات**: هنگام پردازش اسناد بزرگ، از پارامتر `pages` برای استخراج فقط صفحات مورد نیاز استفاده کنید
2. **استخراج تصویر**: فقط زمانی که به تصاویر نیاز دارید `include_image_base64` را `true` تنظیم کنید تا اندازه پاسخ کاهش یابد
3. **فیلتر تصاویر**: از `image_min_size` برای فیلتر کردن تصاویر کوچک و نامرتبط مانند آیکون‌ها استفاده کنید
4. **URLهای سند**: اطمینان حاصل کنید که URLهای سند به صورت عمومی قابل دسترسی هستند یا برای اسناد خصوصی از محتوای base64 استفاده کنید
5. **مدیریت پاسخ‌های بزرگ**: برای مدیریت بارهای بزرگ پاسخ هنگام استخراج تصاویر از اسناد آماده باشید
6. **کش کردن نتایج**: برای اسناد با دسترسی مکرر، کش کردن نتایج OCR را در نظر بگیرید
7. **استفاده از JSON Schema برای داده ساختاریافته**: هنگام استخراج اطلاعات ساختاریافته (فاکتورها، فرم‌ها، رسیدها)، از `document_annotation_format` با JSON Schema برای خروجی یکنواخت و تایپ‌شده استفاده کنید
8. **جداول HTML برای یکپارچه‌سازی وب**: زمانی که نیاز به نمایش جداول استخراج شده در برنامه‌های وب دارید، از `table_format: "html"` استفاده کنید

## منابع مرتبط

- [پردازش اسناد با Mistral OCR](fa/examples/processing_documents_with_mistral_ocr.md) - راهنمای جامع با مثال‌ها
- [مدل Mistral OCR](fa/models/mistral-ocr-2512.md) - جزئیات و مشخصات مدل
- [راهنمای فایل‌های PDF](fa/guides/pdf-files.md) - درباره پردازش فایل‌های PDF بیاموزید
- [راهنمای بینایی](fa/guides/vision.md) - درباره قابلیت‌های پردازش تصویر بیاموزید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
