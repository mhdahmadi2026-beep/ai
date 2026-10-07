# API تنظیم دقیق (Fine-tuning)

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در AvalAI در حال توسعه است و هنوز در دسترس نیست. این مرجع به‌عنوان نقشه سازگاری آینده نگه داشته شده است؛ مثال‌ها تا وقتی AvalAI routeها و مدل‌های پایه قابل تنظیم دقیق را اعلام نکند اجراشدنی نیستند.

API تنظیم دقیق به شما امکان می‌دهد مدل‌ها را با آموزش بر روی داده‌های خود برای مورد استفاده خاص خود سفارشی کنید.

?> مستندات فعلی OpenAI برای supervised fine-tuning توصیه می‌کند پیش از آموزش eval بسازید، با مثال‌های chat در JSONL و کیفیت بالا شروع کنید، و hyperparameterهای پیش‌فرض را نگه دارید مگر اینکه evalها دلیل روشنی برای تغییر نشان دهند. منبع فعلی AvalAI یعنی `data/models.json` هیچ مدل پایه قابل تنظیم دقیق را منتشر نکرده است.

## نقطه پایانی (Endpoint)

```
POST https://api.avalai.ir/v1/fine-tuning/jobs
```

## بدنه درخواست (Request Body)

| پارامتر           | نوع    | الزامی | توضیحات                                                                                              |
| ----------------- | ------ | ------ | ---------------------------------------------------------------------------------------------------- |
| `model`           | string | بله    | شناسه مدل پایه قابل تنظیم دقیق پشتیبانی‌شده. تا زمان اعلام رسمی، هیچ مدل فعلی AvalAI را قابل آموزش فرض نکنید. |
| `training_file`   | string | بله    | شناسه یک فایل آپلود شده که حاوی داده‌های آموزشی است.                                                 |
| `validation_file` | string | خیر    | شناسه یک فایل آپلود شده که حاوی داده‌های اعتبارسنجی است.                                             |
| `hyperparameters` | object | خیر    | ابرپارامترهای استفاده شده برای کار تنظیم دقیق.                                                       |
| `suffix`          | string | خیر    | رشته‌ای با حداکثر ۶۴ کاراکتر که در صورت پشتیبانی به نام مدل تنظیم دقیق شده شما اضافه می‌شود.          |
| `method`          | object | خیر    | روش تنظیم دقیق، مانند supervised fine-tuning، وقتی route از آن پشتیبانی کند.                          |

### شی method

`method` به route و model وابسته است. تا وقتی AvalAI methodهای پشتیبانی‌شده را منتشر نکرده، مثال‌ها را پشت feature flag نگه دارید.

| نوع method | سیگنال آموزشی | نکات برنامه‌ریزی |
| --- | --- | --- |
| `supervised` | مثال‌های prompt و پاسخ ایده‌آل assistant. | مناسب برای format، style و instruction-following پایدار. |
| `dpo` | pairهای پاسخ preferred و rejected. | مناسب وقتی انسان‌ها می‌توانند خروجی‌ها را مقایسه کنند اما یک answer قطعی وجود ندارد. |
| `reinforcement` | grader برای پاسخ‌های sampleشده reward عددی تولید می‌کند. | مناسب taskهای reasoning قابل اندازه‌گیری؛ به eval، اعتبارسنجی grader و safety check نیاز دارد. |

برای jobهای شبیه RFT، قبل از آپلود داده grader را طراحی کنید، promptهای validation را از promptهای training جدا نگه دارید، و مطمئن شوید مدل پایه بخشی از task را از قبل حل می‌کند. مدلی که هرگز task را حل نمی‌کند معمولا با RFT قابل bootstrap نیست.

### شی ابرپارامترها (Hyperparameters Object)

| پارامتر                    | نوع               | الزامی | توضیحات                                                                                                                                    |
| -------------------------- | ----------------- | ------ | ------------------------------------------------------------------------------------------------------------------------------------------ |
| `n_epochs`                 | integer or string | خیر    | تعداد دوره‌هایی (epochs) که مدل باید برای آن آموزش داده شود. یک دوره به یک چرخه کامل در مجموعه داده آموزشی اشاره دارد. پیش‌فرض "auto" است. |
| `batch_size`               | integer or string | خیر    | تعداد نمونه‌ها در هر دسته (batch). پیش‌فرض "auto" است.                                                                                     |
| `learning_rate_multiplier` | number or string  | خیر    | ضریب مقیاس‌بندی برای نرخ یادگیری. پیش‌فرض "auto" است.                                                                                      |

## مثال‌ها

### ایجاد یک کار تنظیم دقیق

```bash
curl https://api.avalai.ir/v1/fine-tuning/jobs \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "fine-tunable-model-id",
  "training_file": "file-abc123",
  "validation_file": "file-def456",
  "hyperparameters": {
    "n_epochs": 4
  }
}'

```

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.fine_tuning.jobs.create(
    model="fine-tunable-model-id",
    training_file="file-abc123",
    validation_file="file-def456",
    hyperparameters={"n_epochs": 4},
)

print(response)

```

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.fineTuning.jobs.create({
  model: "fine-tunable-model-id",
  training_file: "file-abc123",
  validation_file: "file-def456",
  hyperparameters: {
    n_epochs: 4,
  },
});

console.log(response);

```

```go
// مثال Go: ایجاد یک کار تنظیم دقیق از طریق AvalAI
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/openai/openai-go"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY") // یا با کلید خود جایگزین کنید
	if apiKey == "" {
		fmt.Println("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	baseURL := "https://api.avalai.ir/v1" // از URL پایه AvalAI استفاده کنید

	config := openai.DefaultConfig(apiKey)
	config.BaseURL = baseURL
	client := openai.NewClientWithConfig(config)

	req := openai.FineTuningJobRequest{
		Model:          "fine-tunable-model-id",
		TrainingFile:   "file-abc123",
		ValidationFile: "file-def456", // اختیاری
		Hyperparameters: &openai.Hyperparameters{
			NEpochs: 4, // اختیاری، مقدار نمونه
		},
		// Suffix: "my-custom-model", // اختیاری
	}

	resp, err := client.CreateFineTuningJob(context.Background(), req)
	if err != nil {
		fmt.Printf("خطا در ایجاد کار تنظیم دقیق: %v\n", err)
		return
	}

	fmt.Printf("کار تنظیم دقیق ایجاد شد: %+v\n", resp)
}

```

```php
<?php
// مثال PHP: ایجاد یک کار تنظیم دقیق از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/fine-tuning/jobs'; // از URL پایه AvalAI استفاده کنید

$data = [
'model' => 'fine-tunable-model-id',
'training_file' => 'file-abc123',
'validation_file' => 'file-def456', // اختیاری
'hyperparameters' => [ // اختیاری
'n_epochs' => 4
]
// 'suffix' => 'my-custom-model' // اختیاری
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
  echo "خطای cURL #:" . $err;
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "پاسخ: " . $response;
} else {
  echo "پاسخ ایجاد کار تنظیم دقیق:\n";
  echo $response;
  // $responseData = json_decode($response, true);
  // print_r($responseData);
}
?>

```


## فرمت پاسخ (Response Format)

```json
{
  "id": "ftjob-abc123",
  "object": "fine_tuning.job",
  "model": "fine-tunable-model-id",
  "created_at": 1677858242,
  "finished_at": null,
  "fine_tuned_model": null,
  "organization_id": "org-123",
  "status": "running",
  "hyperparameters": {
    "n_epochs": 4
  },
  "training_file": "file-abc123",
  "validation_file": "file-def456",
  "result_files": [],
  "trained_tokens": null
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر            | نوع             | توضیحات                                                                                                                    |
| ------------------ | --------------- | -------------------------------------------------------------------------------------------------------------------------- |
| `id`               | string          | شناسه برای کار تنظیم دقیق.                                                                                                 |
| `object`           | string          | نوع شی، که همیشه "fine_tuning.job" است.                                                                                   |
| `model`            | string          | مدل پایه‌ای که در حال تنظیم دقیق است.                                                                                      |
| `created_at`       | integer         | زمان یونیکس (به ثانیه) ایجاد کار تنظیم دقیق.                                                                               |
| `finished_at`      | integer or null | زمان یونیکس (به ثانیه) پایان کار تنظیم دقیق.                                                                               |
| `fine_tuned_model` | string or null  | نام مدل تنظیم دقیق شده، اگر کار با موفقیت به پایان رسیده باشد.                                                             |
| `organization_id`  | string          | سازمانی که مالک کار تنظیم دقیق است.                                                                                        |
| `status`           | string          | وضعیت کار تنظیم دقیق. می‌تواند "validating", "preparing", "queued", "running", "succeeded", "failed", یا "cancelled" باشد. |
| `hyperparameters`  | object          | ابرپارامترهای استفاده شده برای کار تنظیم دقیق.                                                                             |
| `training_file`    | string          | شناسه فایل استفاده شده برای آموزش.                                                                                         |
| `validation_file`  | string or null  | شناسه فایل استفاده شده برای اعتبارسنجی.                                                                                    |
| `result_files`     | array           | آرایه‌ای از شناسه‌های فایل تولید شده در طول کار تنظیم دقیق.                                                                |
| `trained_tokens`   | integer or null | تعداد توکن‌های آموزش داده شده در طول کار تنظیم دقیق.                                                                       |

## لیست کارهای تنظیم دقیق

```
GET https://api.avalai.ir/v1/fine-tuning/jobs
```

### پارامترهای کوئری (Query Parameters)

| پارامتر | نوع     | الزامی | توضیحات                                               |
| ------- | ------- | ------ | ----------------------------------------------------- |
| `limit` | integer | خیر    | تعداد کارهای تنظیم دقیق برای بازیابی. پیش‌فرض ۲۰ است. |
| `after` | string  | خیر    | شناسه برای آخرین کار از درخواست صفحه‌بندی قبلی.       |

## بازیابی کار تنظیم دقیق

```
GET https://api.avalai.ir/v1/fine-tuning/jobs/{fine_tuning_job_id}
```

## لغو کار تنظیم دقیق

```
POST https://api.avalai.ir/v1/fine-tuning/jobs/{fine_tuning_job_id}/cancel
```

## لیست رویدادهای تنظیم دقیق

```
GET https://api.avalai.ir/v1/fine-tuning/jobs/{fine_tuning_job_id}/events
```

### پارامترهای کوئری (Query Parameters)

| پارامتر | نوع     | الزامی | توضیحات                                            |
| ------- | ------- | ------ | -------------------------------------------------- |
| `limit` | integer | خیر    | تعداد رویدادها برای بازیابی. پیش‌فرض ۲۰ است.       |
| `after` | string  | خیر    | شناسه برای آخرین رویداد از درخواست صفحه‌بندی قبلی. |

### نکات event و metric

payload رویدادها به provider و method وابسته است. وقتی این داده‌ها ارائه شوند، از آن‌ها برای debug کردن job استفاده کنید و فقط به وضعیت نهایی تکیه نکنید:

| خانواده metric | کاربرد |
| --- | --- |
| `train_loss`، `valid_loss` و token accuracy | بررسی همگرایی SFT و نشانه‌های overfit. |
| `train_reward_mean`، `valid_reward_mean` | پایش پیشرفت reward در RFT و drift در validation. |
| score و usage مخصوص هر grader | پیدا کردن graderهای ضعیف، کند یا پرهزینه. |
| نرخ خطاهای parse و runtime | تشخیص schema پاسخ نامعتبر، variable اشتباه در grader یا خطای format در tool-call. |

metricهای training مجوز deploy نیستند. پیش از استفاده از هر `fine_tuned_model` در production، eval suite بیرونی و safety checkها را اجرا کنید.

## endpointهای چرخه عمر مشروط

برخی سیستم‌های upstream برای fine-tuning کنترل‌های چرخه عمر اضافی مانند pause، resume و checkpoint ارائه می‌کنند. این‌ها endpoint تضمین‌شده AvalAI نیستند؛ فقط وقتی استفاده کنید که AvalAI پشتیبانی route و model شما را اعلام کرده باشد.

| عملیات | شکل مسیر مشروط | هدف |
| --- | --- | --- |
| توقف موقت job | `POST /v1/fine-tuning/jobs/{fine_tuning_job_id}/pause` | توقف training و ایجاد checkpoint برای ارزیابی، در صورت پشتیبانی. |
| ادامه job | `POST /v1/fine-tuning/jobs/{fine_tuning_job_id}/resume` | ادامه training از آخرین checkpoint، در صورت پشتیبانی. |
| فهرست checkpointها | `GET /v1/fine-tuning/jobs/{fine_tuning_job_id}/checkpoints` | مقایسه مدل‌های کاندیدای میانی با مدل نهایی و مدل پایه. |

شیء checkpoint معمولا شامل model ID مربوط به checkpoint، step number، زمان ایجاد و metricهاست. هر checkpoint model ID را یک کاندیدای جدا بدانید: آن را روی مجموعه held-out ارزیابی کنید، safety checkها را اجرا کنید و rollback به مدل production قبلی را نگه دارید.

## مدیریت خطا (Error Handling)

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات                                                        |
| -------- | -------------------------------------------------------------- |
| 400      | درخواست بد - درخواست شما نامعتبر است.                          |
| 401      | غیرمجاز - کلید API شما اشتباه است.                             |
| 403      | ممنوع - شما اجازه دسترسی به این منبع را ندارید.                |
| 404      | یافت نشد - منبع مشخص شده یافت نشد.                             |
| 429      | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید. |
| 500      | خطای داخلی سرور - مشکلی در سرور ما وجود داشت.                  |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## منابع مرتبط

- [مدل‌ها](fa/models/model-details.md) - درباره مدل‌های موجود بیاموزید
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
