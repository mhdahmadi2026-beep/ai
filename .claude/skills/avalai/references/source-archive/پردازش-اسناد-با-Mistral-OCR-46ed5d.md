# پردازش اسناد با Mistral OCR

این راهنما نحوه استفاده از مدل قدرتمند `mistral-ocr-latest` برای تشخیص نوری کاراکتر (OCR) و درک اسناد را نشان می‌دهد. شما خواهید آموخت که چگونه متن و محتوای ساختاریافته را از اسناد PDF و تصاویر استخراج کنید در حالی که قالب‌بندی، ساختار و سلسله مراتب را حفظ می‌کنید.

## مقدمه

Mistral OCR یک مدل OCR پیشرفته است که به شما امکان می‌دهد اسناد را در مقیاس بالا با دقت زیاد پردازش کنید. این مثال هم قابلیت‌های پایه OCR و هم قابلیت‌های پیشرفته درک اسناد را پوشش می‌دهد.

### ویژگی‌های کلیدی

- استخراج محتوای متنی با حفظ ساختار و سلسله مراتب سند
- حفظ قالب‌بندی مانند سرفصل‌ها، پاراگراف‌ها، لیست‌ها و جداول
- ارائه نتایج در قالب مارک‌داون برای تجزیه و تحلیل و رندر آسان
- **خروجی JSON ساختاریافته** با حالت JSON Schema برای استخراج داده‌های یکپارچه
- پشتیبانی از طرح‌بندی‌های پیچیده شامل متن چند ستونی و محتوای ترکیبی
- پردازش اسناد در مقیاس بالا با دقت زیاد (تا 2000 صفحه در دقیقه)
- فرمت خروجی جدول قابل تنظیم (مارک‌داون یا HTML)
- به صورت ذاتی چندزبانه، قادر به تجزیه و تحلیل هزاران نوع خط، فونت و زبان
- عملکرد برتر نسبت به سایر مدل‌های پیشرو OCR در آزمون‌های معیار

### موارد استفاده

- **تحقیقات علمی**: تبدیل مقالات علمی با فرمول‌ها و نمودارهای پیچیده به فرمت‌های آماده هوش مصنوعی
- **عملیات تجاری**: پردازش رسیدها، فاکتورها و فرم‌ها برای استخراج داده
- **حفظ میراث تاریخی**: دیجیتال‌سازی اسناد و آثار تاریخی برای دسترسی گسترده‌تر
- **خدمات مشتری**: تبدیل مستندات و راهنماها به پایگاه‌های دانش نمایه‌شده
- **آموزش**: تبدیل یادداشت‌های سخنرانی و ارائه‌ها به محتوای قابل جستجو
- **حقوقی**: پردازش پرونده‌های نظارتی و اسناد حقوقی
- **مهندسی**: استخراج اطلاعات از متون فنی و نقشه‌ها

## OCR پایه با اسناد PDF

### استفاده از URL فایل PDF

می‌توانید یک سند PDF را با ارائه URL آن پردازش کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
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

python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا 100 صفحه
)

print(ocr_response)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  pages: Array.from({ length: 100 }, (_, i) => i), // پردازش تا 100 صفحه
});

console.log(ocrResponse);

go=:package main

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

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"pages": make([]int, 100), // Process pages 0-99
	}

	// Fill pages array
	for i := 0; i < 100; i++ {
		payload["pages"].([]int)[i] = i
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
    'model' => 'mistral-ocr-latest',
    'document' => [
        'type' => 'document_url',
        'document_url' => 'https://arxiv.org/pdf/1805.04770'
    ],
    'pages' => range(0, 99), // Process up to 100 pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
    echo 'Error: ' . curl_error($ch);
} else {
    // Decode and display the response
    $result = json_decode($response, true);
    print_r($result);
}

// Close cURL session
curl_close($ch);

```

### استفاده از PDF کدگذاری شده با Base64

از آنجا که اندپوینت `v1/files` هنوز به طور کامل در دسترس نیست، می‌توانید از کدگذاری base64 برای پردازش مستقیم فایل‌های PDF استفاده کنید:

```language-selector
bash=:# تبدیل PDF به base64
PDF_BASE64=$(base64 -i document.pdf) # در لینوکس از -w 0 برای عدم شکست خط استفاده کنید

# پردازش PDF کدگذاری شده
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-ocr-latest",
 "document": {
 "type": "document_url",
 "document_url": "data:application/pdf;base64,'"$PDF_BASE64"'"
 },
 "include_image_base64": true
}' -o ocr_output.json

python=:import base64
from mistralai import Mistral

# خواندن و کدگذاری فایل PDF
with open("document.pdf", "rb") as f:
    pdf_data = f.read()

base64_pdf = base64.b64encode(pdf_data).decode("utf-8")
document_url = f"data:application/pdf;base64,{base64_pdf}"

# پردازش PDF کدگذاری شده
client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {"type": "document_url", "document_url": document_url}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    pages=list(range(0, 100)),  # پردازش تا 100 صفحه
)

print(ocr_response)

javascript=:import fs from "fs";
import { Mistral } from "mistralai";

// خواندن و کدگذاری فایل PDF
const pdfData = fs.readFileSync("document.pdf");
const base64Pdf = pdfData.toString("base64");
const documentUrl = `data:application/pdf;base64,${base64Pdf}`;

// پردازش PDF کدگذاری شده
const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "document_url",
  document_url: documentUrl,
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  pages: Array.from({ length: 100 }, (_, i) => i),
});

console.log(ocrResponse);

go=:package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Read and encode the PDF file
	pdfBytes, err := ioutil.ReadFile("document.pdf")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	base64String := base64.StdEncoding.EncodeToString(pdfBytes)
	documentUrl := "data:application/pdf;base64," + base64String

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": documentUrl,
		},
		"pages": make([]int, 100), // Process pages 0-99
	}

	// Fill pages array
	for i := 0; i < 100; i++ {
		payload["pages"].([]int)[i] = i
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Read and encode the PDF file
$pdfData = file_get_contents('document.pdf');
$base64Pdf = base64_encode($pdfData);
$documentUrl = 'data:application/pdf;base64,' . $base64Pdf;

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'document_url',
 'document_url' => $documentUrl
 ],
 'pages' => range(0, 99), // Process up to 100 pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);

```

### پردازش صفحات خاص

می‌توانید با استفاده از پارامتر `pages` مشخص کنید که کدام صفحات پردازش شوند:

```language-selector
python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

# فقط صفحات 0، 1 و 5 را پردازش کنید
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    pages=[0, 1, 5],  # فقط صفحات خاص را پردازش کنید
)

print(ocr_response)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

// فقط صفحات 0، 1 و 5 را پردازش کنید
const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  pages: [0, 1, 5], // فقط صفحات خاص را پردازش کنید
});

console.log(ocrResponse);

bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-ocr-latest",
 "document": {
 "type": "document_url",
 "document_url": "https://arxiv.org/pdf/1805.04770"
 },
 "pages": [0, 1, 5],
 "include_image_base64": true
}' -o ocr_output.json

go=:package main

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

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":         "document_url",
			"document_url": "https://arxiv.org/pdf/1805.04770",
		},
		"pages": []int{0, 1, 5}, // Process only specific pages
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'document_url',
 'document_url' => 'https://arxiv.org/pdf/1805.04770'
 ],
 'pages' => [0, 1, 5], // Process only specific pages
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);

```

### نمونه خروجی

API OCR هم محتوای متن استخراج شده در قالب مارک‌داون و هم متادیتا در مورد ساختار سند را برمی‌گرداند:

```json
{
  "pages": [
    {
      "index": 1,
      "markdown": "# LEVERAGING UNLABELED DATA TO PREDICT OUT-OF-DISTRIBUTION PERFORMANCE \n\nSaurabh Garg*<br>Carnegie Mellon University<br>sgarg2@andrew.cmu.edu<br>Sivaraman Balakrishnan<br>Carnegie Mellon University<br>sbalakri@andrew.cmu.edu<br>Zachary C. Lipton<br>Carnegie Mellon University<br>zlipton@andrew.cmu.edu\n\n## Behnam Neyshabur\n\nGoogle Research, Blueshift team\nneyshabur@google.com\n\nHanie Sedghi<br>Google Research, Brain team<br>hsedghi@google.com\n\n\n#### Abstract\n\nReal-world machine learning deployments are characterized by mismatches between the source (training) and target (test) distributions that may cause performance drops...",
      "images": [],
      "dimensions": {
        "dpi": 200,
        "height": 2200,
        "width": 1700
      }
    }
    // صفحات اضافی...

  ],
  "model": "mistral-ocr-latest",
  "usage_info": {
    "pages_processed": 3,
    "doc_size_bytes": null
  }
}
```

## OCR با تصاویر

### استفاده از URL تصویر

می‌توانید تصاویر را با ارائه URL مستقیم پردازش کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-ocr-latest",
 "document": {
 "type": "image_url",
 "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"
 }
}' -o ocr_output.json

python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش تصویر از URL
document_param = {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
)

print(ocr_response)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// پردازش تصویر از URL
const documentParam = {
  type: "image_url",
  image_url:
    "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
});

console.log(ocrResponse);

go=:package main

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

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":      "image_url",
			"image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
		},
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'image_url',
 'image_url' => 'https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png'
 ],
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 print_r($result);
}

// Close cURL session
curl_close($ch);

```

### استفاده از تصاویر کدگذاری شده با Base64

همچنین می‌توانید تصاویر را با استفاده از کدگذاری base64 پردازش کنید:

```language-selector
bash=:# تبدیل تصویر به base64
IMAGE_BASE64=$(base64 -i receipt.jpg) # در لینوکس از -w 0 برای عدم شکست خط استفاده کنید

# پردازش تصویر کدگذاری شده
curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-ocr-latest",
 "document": {
 "type": "image_url",
 "image_url": "data:image/jpeg;base64,'"$IMAGE_BASE64"'"
 }
}' -o ocr_output.json

python=:import base64
from mistralai import Mistral

# خواندن و کدگذاری فایل تصویر
with open("receipt.jpg", "rb") as f:
    image_data = f.read()

base64_image = base64.b64encode(image_data).decode("utf-8")
image_url = f"data:image/jpeg;base64,{base64_image}"

# پردازش تصویر کدگذاری شده
client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

document_param = {"type": "image_url", "image_url": image_url}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
)

print(ocr_response)

javascript=:import fs from "fs";
import { Mistral } from "mistralai";

// خواندن و کدگذاری فایل تصویر
const imageData = fs.readFileSync("receipt.jpg");
const base64Image = imageData.toString("base64");
const imageUrl = `data:image/jpeg;base64,${base64Image}`;

// پردازش تصویر کدگذاری شده
const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

const documentParam = {
  type: "image_url",
  image_url: imageUrl,
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
});

console.log(ocrResponse);

go=:package main

import (
	"bytes"
	"encoding/base64"
	"encoding/json"
	"fmt"
	"io/ioutil"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")

	// Read and encode the image file
	imageBytes, err := ioutil.ReadFile("receipt.jpg")
	if err != nil {
		fmt.Printf("Error reading file: %v\n", err)
		return
	}
	base64String := base64.StdEncoding.EncodeToString(imageBytes)
	imageUrl := "data:image/jpeg;base64," + base64String

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-ocr-latest",
		"document": map[string]interface{}{
			"type":      "image_url",
			"image_url": imageUrl,
		},
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/ocr", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Print response
	fmt.Println(string(body))
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/ocr';

// Read and encode the image file
$imageData = file_get_contents('receipt.jpg');
$base64Image = base64_encode($imageData);
$imageUrl = 'data:image/jpeg;base64,' . $base64Image;

// Create request payload
$payload = [
 'model' => 'mistral-ocr-latest',
 'document' => [
 'type' => 'image_url',
 'image_url' => $imageUrl
 ],
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
	echo 'Error: ' . curl_error($ch);
} else {
	// Decode and display the response
	$result = json_decode($response, true);
	print_r($result);
}

// Close cURL session
curl_close($ch);

```

### مثال: پردازش یک رسید

در اینجا یک مثال خاص از پردازش تصویر یک رسید و استخراج اطلاعات ساختاریافته آورده شده است:

```python
from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش تصویر رسید از URL
document_param = {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
)

# پاسخ OCR حاوی متن استخراج شده در قالب مارک‌داون است
receipt_text = ocr_response.pages[0].markdown
print(receipt_text)

# نمونه خروجی:
# RECEIPT
# THANK YOU FOR SHOPPING AT
# WHOLE FOODS MARKET
# STORE 10113 (415) 618-0066
# 450 RHODE ISLAND ST
# SAN FRANCISCO, CA 94107
# ...
```

## درک سند

می‌توانید Mistral OCR را با مدل‌های زبانی ترکیب کنید تا امکان تعامل زبان طبیعی با محتوای سند را فراهم کنید. این به شما امکان می‌دهد با پرسیدن سؤالات به زبان طبیعی، اطلاعات و بینش‌ها را از اسناد استخراج کنید.

### پاسخگویی به سؤالات با مقالات علمی

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-small-latest",
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "سؤال اصلی تحقیق مطرح شده در این مقاله چیست؟"
 },
 {
 "type": "document_url",
 "document_url": "https://arxiv.org/pdf/1805.04770"
 }
 ]
 }
 ]
}'

python=:from mistralai import Mistral
from mistralai.models import UserMessage

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# ایجاد یک پیام با هر دو متن و سند
message_content = [
    {"type": "text", "text": "سؤال اصلی تحقیق مطرح شده در این مقاله چیست؟"},
    {"type": "document_url", "document_url": "https://arxiv.org/pdf/1805.04770"},
]

messages = [UserMessage(role="user", content=message_content)]

# ارسال درخواست
response = client.chat.complete(model="mistral-small-latest", messages=messages)

print(response.choices[0].message.content)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// ایجاد یک پیام با هر دو متن و سند
const messages = [
  {
    role: "user",
    content: [
      { type: "text", text: "سؤال اصلی تحقیق مطرح شده در این مقاله چیست؟" },
      {
        type: "document_url",
        document_url: "https://arxiv.org/pdf/1805.04770",
      },
    ],
  },
];

// ارسال درخواست
const response = await client.chat.complete({
  model: "mistral-small-latest",
  messages: messages,
});

console.log(response.choices[0].message.content);

go=:package main

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

	// Create message content with both text and document
	textContent := map[string]interface{}{
		"type": "text",
		"text": "What is the main research question addressed in this paper?",
	}
	documentContent := map[string]interface{}{
		"type":         "document_url",
		"document_url": "https://arxiv.org/pdf/1805.04770",
	}

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-small-latest",
		"messages": []map[string]interface{}{
			{
				"role":    "user",
				"content": []map[string]interface{}{textContent, documentContent},
			},
		}
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Parse response to extract message content
	var result map[string]interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("Error parsing response: %v\n", err)
		return
	}

	// Extract and print the message content
	choices := result["choices"].([]interface{})
	firstChoice := choices[0].(map[string]interface{})
	message := firstChoice["message"].(map[string]interface{})
	content := message["content"].(string)

	fmt.Println(content)
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

// Create message content with both text and document
$messageContent = [
 ['type' => 'text', 'text' => 'What is the main research question addressed in this paper?'],
 ['type' => 'document_url', 'document_url' => 'https://arxiv.org/pdf/1805.04770']
];

// Create request payload
$payload = [
 'model' => 'mistral-small-latest',
 'messages' => [
 [
 'role' => 'user',
 'content' => $messageContent
 ]
 ]
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 echo $result['choices'][0]['message']['content'];
}

// Close cURL session
curl_close($ch);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `mistral-small-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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


### استخراج اطلاعات از رسیدها

همچنین می‌توانید از درک سند برای استخراج اطلاعات خاص از رسیدها استفاده کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "mistral-small-latest",
 "messages": [
 {
 "role": "user",
 "content": [
 {
 "type": "text",
 "text": "اطلاعات زیر را از این رسید استخراج کنید: نام فروشگاه، تاریخ، مبلغ کل و لیست اقلام خریداری شده با قیمت‌ها."
 },
 {
 "type": "image_url",
 "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"
 }
 ]
 }
 ]
}'

python=:from mistralai import Mistral
from mistralai.models import UserMessage

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# ایجاد یک پیام با هر دو متن و تصویر
message_content = [
    {
        "type": "text",
        "text": "اطلاعات زیر را از این رسید استخراج کنید: نام فروشگاه، تاریخ، مبلغ کل و لیست اقلام خریداری شده با قیمت‌ها.",
    },
    {
        "type": "image_url",
        "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
    },
]

messages = [UserMessage(role="user", content=message_content)]

# ارسال درخواست
response = client.chat.complete(model="mistral-small-latest", messages=messages)

print(response.choices[0].message.content)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// ایجاد یک پیام با هر دو متن و تصویر
const messages = [
  {
    role: "user",
    content: [
      {
        type: "text",
        text: "اطلاعات زیر را از این رسید استخراج کنید: نام فروشگاه، تاریخ، مبلغ کل و لیست اقلام خریداری شده با قیمت‌ها.",
      },
      {
        type: "image_url",
        image_url:
          "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
      },
    ],
  },
];

// ارسال درخواست
const response = await client.chat.complete({
  model: "mistral-small-latest",
  messages: messages,
});

console.log(response.choices[0].message.content);

go=:package main

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

	// Create message content with both text and image
	textContent := map[string]interface{}{
		"type": "text",
		"text": "Extract the following information from this receipt: store name, date, total amount, and list of purchased items with prices.",
	}
	imageContent := map[string]interface{}{
		"type":      "image_url",
		"image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
	}

	// Create request payload
	payload := map[string]interface{}{
		"model": "mistral-small-latest",
		"messages": []map[string]interface{}{
			{
				"role":    "user",
				"content": []map[string]interface{}{textContent, imageContent},
			},
		}
	}

	// Convert payload to JSON
	payloadBytes, err := json.Marshal(payload)
	if err != nil {
		fmt.Printf("Error creating JSON payload: %v\n", err)
		return
	}

	// Create request
	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/chat/completions", bytes.NewBuffer(payloadBytes))
	if err != nil {
		fmt.Printf("Error creating request: %v\n", err)
		return
	}

	// Set headers
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Authorization", "Bearer "+apiKey)

	// Send request
	client := &http.Client{}
	resp, err := client.Do(req)
	if err != nil {
		fmt.Printf("Error sending request: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// Read response
	body, err := ioutil.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("Error reading response: %v\n", err)
		return
	}

	// Parse response to extract message content
	var result map[string]interface{}
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("Error parsing response: %v\n", err)
		return
	}

	// Extract and print the message content
	choices := result["choices"].([]interface{})
	firstChoice := choices[0].(map[string]interface{})
	message := firstChoice["message"].(map[string]interface{})
	content := message["content"].(string)

	fmt.Println(content)
}

php=:<?php

// API configuration
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

// Create message content with both text and image
$messageContent = [
 ['type' => 'text', 'text' => 'Extract the following information from this receipt: store name, date, total amount, and list of purchased items with prices.'],
 ['type' => 'image_url', 'image_url' => 'https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png']
];

// Create request payload
$payload = [
 'model' => 'mistral-small-latest',
 'messages' => [
 [
 'role' => 'user',
 'content' => $messageContent
 ]
 ]
];

// Initialize cURL session
$ch = curl_init($apiUrl);

// Set cURL options
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($payload));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'Authorization: Bearer ' . $apiKey
]);

// Execute the request
$response = curl_exec($ch);

// Check for errors
if (curl_errno($ch)) {
 echo 'Error: ' . curl_error($ch);
} else {
 // Decode and display the response
 $result = json_decode($response, true);
 echo $result['choices'][0]['message']['content'];
}

// Close cURL session
curl_close($ch);

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API مدل این نسخه روی `gpt-5.5` تنظیم شده، چون `mistral-small-latest` ممکن است در داده‌های فعلی AvalAI برای `/v1/responses` فعال نباشد.</summary>

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
                {"type": "input_text", "text": "Describe this image."},
                {"type": "input_image", "image_url": "https://example.com/image.png"},
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
        { type: "input_text", text: "Describe this image." },
        { type: "input_image", image_url: "https://example.com/image.png" },
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


## ویژگی‌های پیشرفته

### خروجی JSON ساختاریافته

API OCR از حالت‌های خروجی JSON بومی پشتیبانی می‌کند که به شما امکان می‌دهد داده‌های ساختاریافته را مستقیما از اسناد استخراج کنید. این برای پردازش فاکتورها، رسیدها، فرم‌ها و سایر اسنادی که به داده‌های ساختاریافته یکپارچه نیاز دارند مفید است.

#### استفاده از حالت JSON Object

با تنظیم `document_annotation_format` به `{"type": "json_object"}` حالت JSON را فعال کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "mistral-ocr-latest",
  "document": {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"
  },
  "document_annotation_format": {
    "type": "json_object"
  }
}'

python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش رسید با فرمت خروجی JSON
document_param = {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    document_annotation_format={"type": "json_object"},
)

# فیلد document_annotation حاوی JSON ساختاریافته خواهد بود
print(ocr_response.document_annotation)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// پردازش رسید با فرمت خروجی JSON
const documentParam = {
  type: "image_url",
  image_url:
    "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  document_annotation_format: { type: "json_object" },
});

// فیلد document_annotation حاوی JSON ساختاریافته خواهد بود
console.log(ocrResponse.document_annotation);

```

#### استفاده از حالت JSON Schema

برای کنترل بیشتر بر ساختار خروجی، از حالت JSON Schema برای تعریف دقیق فیلدهایی که می‌خواهید استخراج کنید استفاده کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "mistral-ocr-latest",
  "document": {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png"
  },
  "document_annotation_format": {
    "type": "json_schema",
    "json_schema": {
      "name": "receipt",
      "schema": {
        "type": "object",
        "properties": {
          "store_name": {"type": "string"},
          "date": {"type": "string"},
          "total": {"type": "number"},
          "items": {
            "type": "array",
            "items": {
              "type": "object",
              "properties": {
                "name": {"type": "string"},
                "price": {"type": "number"}
              }
            }
          }
        },
        "required": ["store_name", "total"]
      }
    }
  }
}'

python=:from mistralai import Mistral
import json

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# تعریف JSON schema برای استخراج رسید
receipt_schema = {
    "type": "json_schema",
    "json_schema": {
        "name": "receipt",
        "schema": {
            "type": "object",
            "properties": {
                "store_name": {"type": "string"},
                "date": {"type": "string"},
                "total": {"type": "number"},
                "items": {
                    "type": "array",
                    "items": {
                        "type": "object",
                        "properties": {
                            "name": {"type": "string"},
                            "price": {"type": "number"},
                        },
                    },
                },
            },
            "required": ["store_name", "total"],
        },
    },
}

# پردازش رسید با JSON schema
document_param = {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    document_annotation_format=receipt_schema,
)

# تجزیه پاسخ JSON ساختاریافته
receipt_data = json.loads(ocr_response.document_annotation)
print(f"فروشگاه: {receipt_data.get('store_name')}")
print(f"جمع کل: ${receipt_data.get('total')}")
for item in receipt_data.get("items", []):
    print(f"  - {item['name']}: ${item['price']}")

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// تعریف JSON schema برای استخراج رسید
const receiptSchema = {
  type: "json_schema",
  json_schema: {
    name: "receipt",
    schema: {
      type: "object",
      properties: {
        store_name: { type: "string" },
        date: { type: "string" },
        total: { type: "number" },
        items: {
          type: "array",
          items: {
            type: "object",
            properties: {
              name: { type: "string" },
              price: { type: "number" },
            },
          },
        },
      },
      required: ["store_name", "total"],
    },
  },
};

// پردازش رسید با JSON schema
const documentParam = {
  type: "image_url",
  image_url:
    "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  document_annotation_format: receiptSchema,
});

// تجزیه پاسخ JSON ساختاریافته
const receiptData = JSON.parse(ocrResponse.document_annotation);
console.log(`فروشگاه: ${receiptData.store_name}`);
console.log(`جمع کل: $${receiptData.total}`);
for (const item of receiptData.items || []) {
  console.log(`  - ${item.name}: $${item.price}`);
}

```

#### نمونه پاسخ JSON Schema

هنگام استفاده از حالت JSON Schema، فیلد `document_annotation` در پاسخ حاوی JSON ساختاریافته مطابق با schema شما خواهد بود:

```json
{
  "store_name": "WHOLE FOODS MARKET",
  "date": "2024-01-15",
  "total": 45.67,
  "items": [
    {
      "name": "Organic Apples",
      "price": 5.99
    },
    {
      "name": "Almond Milk",
      "price": 4.49
    },
    {
      "name": "Whole Grain Bread",
      "price": 3.99
    }
  ]
}
```

### فرمت جدول HTML

می‌توانید نحوه استخراج جداول از اسناد را با استفاده از پارامتر `table_format` کنترل کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "mistral-ocr-latest",
  "document": {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770"
  },
  "table_format": "html",
  "pages": [0]
}'

python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش سند با فرمت جدول HTML
document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    table_format="html",  # گزینه‌ها: "markdown" (پیش‌فرض) یا "html"
    pages=[0],
)

# جداول در سند به صورت HTML قالب‌بندی خواهند شد
print(ocr_response.pages[0].markdown)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// پردازش سند با فرمت جدول HTML
const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  table_format: "html", // گزینه‌ها: "markdown" (پیش‌فرض) یا "html"
  pages: [0],
});

// جداول در سند به صورت HTML قالب‌بندی خواهند شد
console.log(ocrResponse.pages[0].markdown);

```

### استخراج سربرگ و پاورقی

می‌توانید سربرگ‌ها و پاورقی‌های سند را به صورت جداگانه با استفاده از پارامترهای `extract_header` و `extract_footer` استخراج کنید:

```language-selector
bash=:curl https://api.avalai.ir/v1/ocr \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "mistral-ocr-latest",
  "document": {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770"
  },
  "extract_header": true,
  "extract_footer": true,
  "pages": [0, 1, 2]
}'

python=:from mistralai import Mistral

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش سند با استخراج سربرگ/پاورقی
document_param = {
    "type": "document_url",
    "document_url": "https://arxiv.org/pdf/1805.04770",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
    extract_header=True,
    extract_footer=True,
    pages=[0, 1, 2],
)

print(ocr_response)

javascript=:import { Mistral } from "mistralai";

const client = new Mistral({
  apiKey: "avalai-api-key",
  baseURL: "https://api.avalai.ir",
});

// پردازش سند با استخراج سربرگ/پاورقی
const documentParam = {
  type: "document_url",
  document_url: "https://arxiv.org/pdf/1805.04770",
};

const ocrResponse = await client.ocr.process({
  model: "mistral-ocr-latest",
  document: documentParam,
  extract_header: true,
  extract_footer: true,
  pages: [0, 1, 2],
});

console.log(ocrResponse);

```

### پردازش دسته‌ای

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و هنوز در AvalAI در دسترس نیست. ما انتشار آن را از طریق کانال‌های رسمی خود اعلام خواهیم کرد. منتظر به‌روزرسانی‌های ما باشید!

برای پردازش کارآمد چندین سند، می‌توانید از پردازش دسته‌ای استفاده کنید:

```python
from mistralai import Mistral
import os

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# دایرکتوری حاوی فایل‌های PDF
pdf_directory = "documents/"

# پردازش همه فایل‌های PDF در دایرکتوری
for filename in os.listdir(pdf_directory):
    if filename.endswith(".pdf"):
        file_path = os.path.join(pdf_directory, filename)

# ایجاد پارامتر سند
document_param = {
    "type": "document_url",
    "document_url": f"file://{file_path}",
}

# پردازش سند
ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
)

# ذخیره نتایج
output_file = os.path.join("results/", f"{filename}.md")
with open(output_file, "w") as f:
    for page in ocr_response.pages:
        f.write(f"# صفحه {page.index}\n\n")
        f.write(page.markdown)
        f.write("\n\n")

print(f"فایل {filename} پردازش شد")
```

### خروجی ساختاریافته

می‌توانید با استفاده از مدل‌های زبانی، خروجی ساختاریافته از نتایج OCR درخواست کنید:

```python
from mistralai import Mistral
from mistralai.models import UserMessage
import json

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

# پردازش تصویر رسید
document_param = {
    "type": "image_url",
    "image_url": "https://raw.githubusercontent.com/mistralai/cookbook/refs/heads/main/mistral/ocr/receipt.png",
}

ocr_response = client.ocr.process(
    model="mistral-ocr-latest",
    document=document_param,
)

# استخراج متن OCR
receipt_text = ocr_response.pages[0].markdown

# درخواست خروجی JSON ساختاریافته
message_content = [
    {
        "type": "text",
        "text": f"""
اینجا یک متن رسید استخراج شده با استفاده از OCR است:

{receipt_text}

اطلاعات زیر را در قالب JSON استخراج کنید:
- store_name: نام فروشگاه
- date: تاریخ خرید
- items: آرایه‌ای از اقلام خریداری شده، هر کدام با "name" و "price"
- subtotal: مبلغ جمع جزئی
- tax: مبلغ مالیات
- total: مبلغ کل

فقط JSON معتبر را بدون هیچ متن دیگری برگردانید.
""",
    }
]

messages = [UserMessage(role="user", content=message_content)]

# ارسال درخواست
response = client.chat.complete(model="mistral-small-latest", messages=messages)

# تجزیه پاسخ JSON
structured_data = json.loads(response.choices[0].message.content)
print(json.dumps(structured_data, indent=2))
```

## عیب‌یابی

### مشکلات رایج و راه حل‌ها

#### مشکل: کیفیت پایین OCR

**راه حل**: اگر کیفیت OCR پایینی را تجربه می‌کنید، موارد زیر را امتحان کنید:

- اطمینان حاصل کنید که تصویر سند وضوح کافی دارد (حداقل 200 DPI)
- مطمئن شوید که سند به درستی جهت‌گیری شده است
- اگر از یک سند اسکن شده استفاده می‌کنید، بررسی کنید که اسکن واضح باشد و کنتراست خوبی داشته باشد
- برای تصاویر، فرمت‌های مختلف را امتحان کنید (PNG اغلب برای متن بهتر از JPEG عمل می‌کند)

#### مشکل: خطا در کدگذاری Base64

**راه حل**: هنگام استفاده از کدگذاری base64، اطمینان حاصل کنید:

- نوع MIME صحیح مشخص شده است (`data:application/pdf;base64,` برای PDF‌ها، `data:image/jpeg;base64,` برای تصاویر JPEG)
- در رشته base64 شکست خط وجود ندارد (در لینوکس از گزینه `-w 0` با دستور base64 استفاده کنید)
- اندازه فایل از محدودیت 50 مگابایت تجاوز نمی‌کند

#### مشکل: تایم‌اوت در اسناد بزرگ

**راه حل**: برای اسناد بزرگ:

- به جای کل سند، صفحات خاصی را پردازش کنید
- سند را به قطعات کوچکتر تقسیم کنید
- پارامتر تایم‌اوت را در پیکربندی کلاینت خود افزایش دهید
- برای اسناد بسیار بزرگ از پردازش دسته‌ای استفاده کنید

### مدیریت خطا

همیشه مدیریت خطای مناسب را در کد خود پیاده‌سازی کنید:

```python
from mistralai import Mistral
from mistralai.exceptions import MistralAPIError

client = Mistral(server_url="https://api.avalai.ir", api_key="avalai-api-key")

try:
    document_param = {
        "type": "document_url",
        "document_url": "https://example.com/document.pdf",
    }

    ocr_response = client.ocr.process(
        model="mistral-ocr-latest",
        document=document_param,
    )

    print(ocr_response)

except MistralAPIError as e:
    if e.status_code == 413:
        print("خطا: سند بسیار بزرگ است (بیش از 50 مگابایت)")
    elif e.status_code == 415:
        print("خطا: فرمت فایل پشتیبانی نمی‌شود")
    elif e.status_code == 429:
        print("خطا: محدودیت نرخ فراتر رفته است، بعدا دوباره امتحان کنید")
    elif e.status_code >= 500:
        print("خطا: خطای سرور، بعدا دوباره امتحان کنید")
    else:
        print(f"خطای API: {e}")
except Exception as e:
    print(f"خطای غیرمنتظره: {e}")
```

## بهترین شیوه‌ها

### بهینه‌سازی برای دقت

1. **از اسناد با کیفیت بالا استفاده کنید**: هر زمان که ممکن است، به جای اسناد اسکن شده از PDF‌های دیجیتال اصلی برای بهترین نتایج استفاده کنید.

2. **فرمت‌های مختلف را آزمایش کنید**: برای اسناد اسکن شده، با فرمت‌ها و وضوح‌های تصویر مختلف آزمایش کنید تا تعادل بهینه بین اندازه فایل و کیفیت OCR را پیدا کنید.

3. **پیش‌پردازش تصاویر**: برای اسناد دشوار، پیش‌پردازش تصاویر را برای بهبود کنتراست، حذف نویز یا اصلاح کجی قبل از پردازش OCR در نظر بگیرید.

4. **نتایج را اعتبارسنجی کنید**: منطق اعتبارسنجی را برای بررسی نتایج OCR در برابر الگوهای مورد انتظار پیاده‌سازی کنید (به عنوان مثال، بررسی اینکه تاریخ‌های استخراج شده از فرمت معتبری پیروی می‌کنند).

5. **از درک سند به صورت تکراری استفاده کنید**: برای استخراج اطلاعات پیچیده، یک رویکرد چند مرحله‌ای را در نظر بگیرید که در آن نتایج اولیه OCR برای تعیین سؤالات پیگیری تحلیل می‌شوند.

### بهینه‌سازی عملکرد

1. **فقط صفحات مورد نیاز را پردازش کنید**: هنگام کار با اسناد چند صفحه‌ای، با استفاده از پارامتر `pages` فقط صفحاتی را که نیاز دارید مشخص کنید.

2. **پردازش دسته‌ای**: برای حجم زیادی از اسناد، پردازش دسته‌ای را با مدیریت خطا و منطق تلاش مجدد مناسب پیاده‌سازی کنید.

3. **ذخیره‌سازی در حافظه پنهان**: برای جلوگیری از پردازش تکراری اسناد یکسان، ذخیره‌سازی در حافظه پنهان را برای نتایج OCR پیاده‌سازی کنید.

4. **پردازش موازی**: برای اسناد مستقل، پردازش موازی را برای بهبود توان عملیاتی در نظر بگیرید.

5. **نظارت بر استفاده**: برای ماندن در محدوده‌های نرخ و بهینه‌سازی هزینه‌ها، استفاده از API خود را پیگیری کنید.

## منابع مرتبط

- [مدل‌های Mistral AI](fa/providers/mistralai.md)
- [اعلامیه OCR](fa/news/2025-05-15-mistral-ocr-latest-added.md)
- [راهنمای فایل‌های PDF](fa/guides/pdf-files.md)
- [پردازش اسناد با PDF‌ها](fa/examples/processing_pdfs_in_chat_completion_api.md)
- [راهنمای بینایی](fa/guides/vision.md)
