# مرجع مهاجرت API دستیاران (Assistants)

!> ویژگی پیاده‌سازی نشده!
این قابلیت در حال حاضر در حال توسعه است و در AvalAI در دسترس نیست. تا زمانی که AvalAI سازگاری Assistants را اعلام نکرده، مثال‌های این صفحه را runnable در نظر نگیرید.

OpenAI اعلام کرده است که Assistants API از **۲۶ اوت ۲۰۲۵** منسوخ شده و تاریخ پایان آن **۲۶ اوت ۲۰۲۶** است. برای برنامه‌های agentic جدید در AvalAI، به‌جای آن از [Responses API](fa/api-reference/responses.md)، [فراخوانی تابع](fa/guides/function-calling.md)، [ابزارها](fa/guides/tools.md) و [وضعیت مکالمه](fa/guides/conversation-state.md) استفاده کنید.

این صفحه فقط به‌عنوان نقشه سازگاری آینده برای ادغام‌های موجود شبیه Assistants نگه داشته شده است. در این مدل، یک Assistant دستورالعمل دارد و می‌تواند از مدل‌ها، ابزارها و دانش برای پاسخ به پرسش‌های کاربر استفاده کند.

## نگاشت مهاجرت به Responses

برای workflowهای agentic قابل اجرا در AvalAI امروز، به‌جای انتظار برای `/v1/assistants`، مفاهیم Assistants را به primitiveهای Responses نگاشت کنید:

| مفهوم در Assistants | جایگزین در Responses/AvalAI |
| --- | --- |
| دستورالعمل‌های Assistant | پارامتر سطح بالای `instructions` در `/v1/responses`، همراه با پیکربندی agent در برنامه وقتی persona قابل استفاده مجدد می‌خواهید. |
| Thread | `previous_response_id`، replay دستی آیتم‌های `response.output`، یا شیء `conversation` وقتی route پشتیبانی کند. |
| Message | آیتم `input` با `role: "user"` یا `role: "assistant"`؛ برای flowهای reasoning/tool آیتم‌های خروجی typed را حفظ کنید. |
| Run | یک درخواست `/v1/responses`، در صورت پشتیبانی route با `background: true` برای پردازش پس‌زمینه. |
| Function tool | ابزار تابع در Responses با schema سختگیرانه؛ نتیجه را به شکل `function_call_output` و با `call_id` متناظر برگردانید. |
| File search / vector store | اگر route پشتیبانی کند از `file_search` استفاده کنید؛ در غیر این صورت RAG را با `/v1/embeddings`، store خودتان و `/v1/responses` بسازید. |
| Code interpreter / ابزارهای hosted | وابسته به route، مدل و حساب است؛ وقتی hosted tools ارائه نشده‌اند از sandbox یا worker خودتان استفاده کنید. |

## نکات مهاجرت OpenAI برای AvalAI

راهنمای فعلی مهاجرت OpenAI مفاهیم `Assistants` را به `Prompts` نسخه‌بندی‌شده، `Threads` را به `Conversations`، `Runs` را به `Responses` و run stepها را به آیتم‌های تایپ‌شده پاسخ نگاشت می‌کند. در مستندات AvalAI، promptها و conversationهای میزبانی‌شده را تا زمان اعلام endpoint متناظر توسط AvalAI، مفهوم سازگاری بدانید. مسیر قابل حمل مهاجرت این است:

1. **پروفایل agent را در برنامه نسخه‌بندی کنید:** مدل، instructions، schema ابزارها، schema خروجی و policy ایمنی را در source control یا configuration store خودتان نگه دارید.
2. **وضعیت مکالمه را خودتان ذخیره کنید:** پیام‌های کاربر، پاسخ‌های assistant، tool callها و خروجی toolها را در پایگاه داده خود ذخیره کنید.
3. **`/v1/responses` را فراخوانی کنید:** turn فعلی و history فشرده مرتبط را بفرستید، یا فقط وقتی route انتخابی state ذخیره‌شده را پشتیبانی می‌کند از `previous_response_id` استفاده کنید.
4. **آیتم‌های تایپ‌شده را حفظ کنید:** tool callها، خلاصه‌های reasoning، referenceهای فایل یا citationها را قبل از پردازش برنامه به متن ساده تبدیل نکنید.
5. **ابتدا ترافیک جدید را مهاجرت دهید:** conversationهای جدید را به Responses ببرید و داده threadهای قدیمی سبک Assistants را فقط وقتی continuity محصول لازم دارد backfill کنید.

این الگو مهاجرت را امروز در AvalAI قابل اجرا نگه می‌دارد و در عین حال برای سازگاری آینده با Prompt، Conversation یا Assistants میزبانی‌شده جا می‌گذارد.

## جایگزین قابل اجرا: معلم ریاضی با Responses

برای برنامه‌های agent-style جدید در AvalAI، به‌جای endpoint برنامه‌ریزی‌شده Assistants از این الگو استفاده کنید. persona قابل استفاده مجدد را در `instructions` نگه دارید، turn فعلی را در `input` بفرستید، و فقط وقتی برنامه شما می‌تواند اجرا و مجوزدهی را امن انجام دهد ابزارهای function سفارشی اضافه کنید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    instructions=(
        "شما یک معلم ریاضی صبور هستید. روش حل را توضیح بده، "
        "پاسخ نهایی را نشان بده و یک سوال تمرینی کوتاه بپرس."
    ),
    input="مساحت یک مستطیل ۸۴ و عرض آن ۷ است. طول آن چقدر است؟",
    store=False,
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
  instructions:
    "شما یک معلم ریاضی صبور هستید. روش حل را توضیح بده، پاسخ نهایی را نشان بده و یک سوال تمرینی کوتاه بپرس.",
  input: "مساحت یک مستطیل ۸۴ و عرض آن ۷ است. طول آن چقدر است؟",
  store: false,
});

console.log(response.output_text);

```

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "شما یک معلم ریاضی صبور هستید. روش حل را توضیح بده، پاسخ نهایی را نشان بده و یک سوال تمرینی کوتاه بپرس.",
    "input": "مساحت یک مستطیل ۸۴ و عرض آن ۷ است. طول آن چقدر است؟",
    "store": false
  }'

```


اگر طراحی Assistants شما به Code Interpreter وابسته بود، تا زمانی که route انتخابی AvalAI صریحا اجرای کد میزبانی‌شده را پشتیبانی کند، کد را در sandbox یا worker خودتان اجرا کنید و فقط یک [ابزار function](fa/guides/function-calling.md) محدود expose کنید.

## نقطه پایانی (هنوز در دسترس نیست)

```
POST https://api.avalai.ir/v1/assistants
```

## ایجاد یک دستیار

### بدنه درخواست (Request Body)

| پارامتر          | نوع    | الزامی | توضیحات                                                                                           |
| ---------------- | ------ | ------ | ------------------------------------------------------------------------------------------------- |
| `model`          | string | بله    | شناسه مدلی که باید استفاده شود. برای گزینه‌های موجود به [مدل‌ها](fa/models/model-details.md) مراجعه کنید. |
| `name`           | string | خیر    | نام دستیار. حداکثر طول ۲۵۶ کاراکتر است.                                                           |
| `description`    | string | خیر    | توضیحات دستیار. حداکثر طول ۵۱۲ کاراکتر است.                                                       |
| `instructions`   | string | خیر    | دستورالعمل‌های سیستمی که دستیار استفاده می‌کند. حداکثر طول ۳۲۷۶۸ کاراکتر است.                     |
| `tools`          | array  | خیر    | لیستی از ابزارهای فعال شده در دستیار. حداکثر ۱۲۸ ابزار برای هر دستیار وجود دارد.                  |
| `tool_resources` | object | خیر    | مجموعه‌ای از منابعی که دستیار هنگام استفاده از ابزارها به آن‌ها دسترسی دارد.                      |
| `metadata`       | object | خیر    | مجموعه‌ای از ۱۶ جفت کلید-مقدار که می‌توان به یک شی پیوست کرد.                                    |

### شی ابزارها (Tools Object)

| پارامتر    | نوع    | الزامی | توضیحات                                                                  |
| ---------- | ------ | ------ | ------------------------------------------------------------------------ |
| `type`     | string | بله    | نوع ابزار. در Assistants v2 OpenAI معمولا `"code_interpreter"`، `"file_search"` یا `"function"` است؛ پشتیبانی AvalAI هنوز اعلام نشده است. |
| `function` | object | مشروط   | زمانی که نوع "function" است، الزامی است.                                 |

## مثال‌ها

!> مثال‌های زیر فقط شکل سازگاری برنامه‌ریزی‌شده را مستند می‌کنند. برای workflowهای agentic runnable امروز، از `/v1/responses` همراه ابزارهای تابعی سفارشی یا ابزارهای میزبانی‌شده‌ای استفاده کنید که route انتخابی پشتیبانی می‌کند.

### ایجاد یک دستیار

```bash
curl https://api.avalai.ir/v1/assistants \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "OpenAI-Beta: assistants=v2" \
  -d '{
  "model": "gpt-5.6-luna",
  "name": "Math Tutor",
  "instructions": "شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.",
  "tools": [{"type": "code_interpreter"}]
}'

```

```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",  # با کلید واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

assistant = client.beta.assistants.create(
    name="Math Tutor",
    instructions="شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.",
    tools=[{"type": "code_interpreter"}],
    model="gpt-5.6-luna",
)

print(assistant.id)

```

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const assistant = await client.beta.assistants.create({
  name: "Math Tutor",
  instructions:
    "شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.",
  tools: [{ type: "code_interpreter" }],
  model: "gpt-5.6-luna",
});

console.log(assistant.id);

```

```go
// مثال Go: ایجاد یک دستیار از طریق AvalAI
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

	req := openai.AssistantRequest{
		Model:        "gpt-5.6-luna",
		Name:         openai.NewString("Math Tutor"),
		Instructions: openai.NewString("شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید."),
		Tools: []openai.AssistantTool{
			{Type: openai.AssistantToolTypeCodeInterpreter},
		},
		// Description: openai.NewString("توضیحات اختیاری"), // اختیاری
		// Metadata: map[string]interface{}{"user_id": "123"}, // اختیاری
	}

	resp, err := client.CreateAssistant(context.Background(), req)
	if err != nil {
		fmt.Printf("خطا در ایجاد دستیار: %v\n", err)
		return
	}

	fmt.Printf("دستیار با شناسه ایجاد شد: %s\n", resp.ID)
}

```

```php
<?php
// مثال PHP: ایجاد یک دستیار از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/assistants'; // از URL پایه AvalAI استفاده کنید

$data = [
'model' => 'gpt-5.6-luna',
'name' => 'Math Tutor',
'instructions' => 'شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.',
'tools' => [['type' => 'code_interpreter']],
// 'description' => 'توضیحات اختیاری', // اختیاری
// 'metadata' => ['user_id' => '123'] // اختیاری
];

// Ensure instructions are properly encoded if they contain non-ASCII characters
$jsonData = json_encode($data, JSON_UNESCAPED_UNICODE);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'OpenAI-Beta: assistants=v2', // هدر الزامی برای Assistants API v2
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
  echo "پاسخ ایجاد دستیار:\n";
  echo $response;
  // $responseData = json_decode($response, true);
  // if (isset($responseData['id'])) {
    // echo "دستیار با شناسه ایجاد شد: " . $responseData['id'] . "\n";
    // } else {
      // print_r($responseData);
      // }
    }
    ?>

```


## فرمت پاسخ (Response Format)

```json
{
  "id": "asst_abc123",
  "object": "assistant",
  "created_at": 1698984975,
  "name": "Math Tutor",
  "description": null,
  "model": "gpt-5.6-luna",
  "instructions": "شما یک معلم خصوصی ریاضی هستید. برای پاسخ به سوالات ریاضی کد بنویسید و اجرا کنید.",
  "tools": [
    {
      "type": "code_interpreter"
    }
  ],
  "file_ids": [],
  "metadata": {}
}
```

## پارامترهای پاسخ (Response Parameters)

| پارامتر        | نوع            | توضیحات                                              |
| -------------- | -------------- | ---------------------------------------------------- |
| `id`           | string         | شناسه برای دستیار.                                   |
| `object`       | string         | نوع شی، که همیشه "assistant" است.                   |
| `created_at`   | integer        | زمان یونیکس (به ثانیه) ایجاد دستیار.                 |
| `name`         | string or null | نام دستیار.                                          |
| `description`  | string or null | توضیحات دستیار.                                      |
| `model`        | string         | مدلی که دستیار استفاده می‌کند.                       |
| `instructions` | string         | دستورالعمل‌های سیستمی که دستیار استفاده می‌کند.      |
| `tools`        | array          | لیستی از ابزارهای فعال شده در دستیار.                |
| `file_ids`     | array          | لیستی از شناسه‌های فایل پیوست شده به این دستیار.     |
| `metadata`     | object         | مجموعه‌ای از جفت‌های کلید-مقدار پیوست شده به دستیار. |

## رشته‌ها (Threads)

رشته‌ها نمایانگر گفتگوها بین کاربران و دستیاران هستند.

### ایجاد یک رشته

```
POST https://api.avalai.ir/v1/threads
```

#### بدنه درخواست (Request Body)

| پارامتر    | نوع    | الزامی | توضیحات                                                       |
| ---------- | ------ | ------ | ------------------------------------------------------------- |
| `messages` | array  | خیر    | لیستی از پیام‌ها برای شروع رشته.                              |
| `metadata` | object | خیر    | مجموعه‌ای از جفت‌های کلید-مقدار که می‌توان به رشته پیوست کرد. |

### افزودن یک پیام به یک رشته

```
POST https://api.avalai.ir/v1/threads/{thread_id}/messages
```

#### بدنه درخواست (Request Body)

| پارامتر    | نوع    | الزامی | توضیحات                                                                       |
| ---------- | ------ | ------ | ----------------------------------------------------------------------------- |
| `role`     | string | بله    | نقش موجودیتی که پیام را ایجاد می‌کند. در حال حاضر فقط "user" پشتیبانی می‌شود. |
| `content`  | string | بله    | محتوای پیام.                                                                  |
| `file_ids` | array  | خیر    | لیستی از شناسه‌های فایل که پیام باید از آن‌ها استفاده کند.                    |
| `metadata` | object | خیر    | مجموعه‌ای از جفت‌های کلید-مقدار که می‌توان به پیام پیوست کرد.                 |

### اجرای یک دستیار روی یک رشته

```
POST https://api.avalai.ir/v1/threads/{thread_id}/runs
```

#### بدنه درخواست (Request Body)

| پارامتر        | نوع    | الزامی | توضیحات                                                       |
| -------------- | ------ | ------ | ------------------------------------------------------------- |
| `assistant_id` | string | بله    | شناسه دستیاری که باید برای این اجرا استفاده شود.              |
| `instructions` | string | خیر    | جایگزینی دستورالعمل‌های دستیار برای این اجرا.                 |
| `tools`        | array  | خیر    | جایگزینی ابزارهای دستیار برای این اجرا.                       |
| `metadata`     | object | خیر    | مجموعه‌ای از جفت‌های کلید-مقدار که می‌توان به اجرا پیوست کرد. |

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
