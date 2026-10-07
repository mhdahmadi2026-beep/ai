# مرجع API پیام‌ها

API پیام‌ها امکان دسترسی به مدل‌های Anthropic از طریق نقطه پایانی `v1/messages` API Claude را فراهم می‌کند. این نقطه پایانی بخشی از پشتیبانی چند ارائه دهنده AvalAI است که به شما امکان می‌دهد با مدل‌های Anthropic با استفاده از فرمت API بومی آنها تعامل داشته باشید. تمام مدل‌های Claude از جمله `claude-sonnet-5`، `claude-opus-4-8`، `claude-opus-4-7`، `claude-opus-4-6`، `claude-sonnet-4-6` و سایر فضاهای نام مدل پایه با مسیریابی هوشمند پشتیبانی می‌شوند. API پیام‌ها از Claude Sonnet 5 و Claude Opus 4.8 پشتیبانی کامل دارد، شامل قابلیت‌های جدید مانند پیام‌های `role: "system"` در میانه مکالمه (با حفظ hit کش پرامپت) و شی `stop_details` به‌طور عمومی مستند شده در پاسخ‌های امتناع.

## نقطه پایانی

```
POST https://api.avalai.ir/v1/messages
```

## بدنه درخواست

| پارامتر | نوع | ضروری | توضیحات |
| --------- | ---- | -------- | ----------- |
| `model` | string | بله | شناسه مدل Anthropic برای استفاده. برای گزینه‌های موجود به [مدل‌های Anthropic](fa/providers/anthropic.md) مراجعه کنید. |
| `messages` | array | بله | آرایه‌ای از اشیا پیام که نمایانگر تاریخچه مکالمه هستند. |
| `system` | string | خیر | دستورالعمل‌های سیستم که مدل را برای مکالمه آماده می‌کنند. |
| `max_tokens` | integer | بله | حداکثر تعداد توکن‌ها برای تولید. مقدار پیش‌فرض بسته به مدل متفاوت است. |
| `temperature` | number | خیر | دمای نمونه‌گیری بین 0 و 1. مقادیر بالاتر مانند 0.8 خروجی را تصادفی‌تر می‌کنند، در حالی که مقادیر پایین‌تر مانند 0.2 آن را متمرکزتر می‌کنند. مقدار پیش‌فرض 1 است. |
| `top_p` | number | خیر | جایگزینی برای دما، نمونه‌گیری هسته. مقدار پیش‌فرض 1 است. |
| `top_k` | integer | خیر | فقط از K گزینه برتر برای هر توکن بعدی نمونه‌گیری کنید. مقدار پیش‌فرض -1 (غیرفعال) است. |
| `stream` | boolean | خیر | اگر به true تنظیم شود، دلتاهای جزئی پیام ارسال خواهند شد. مقدار پیش‌فرض false است. |
| `stop_sequences` | array | خیر | دنباله‌های متنی سفارشی که باعث می‌شوند مدل تولید را متوقف کند. |
| `metadata` | object | خیر | متادیتای اختیاری برای گنجاندن در پاسخ. |

### شی پیام

هر پیام در آرایه `messages` باید ساختار زیر را داشته باشد:

| پارامتر | نوع | ضروری | توضیحات |
| --------- | ---- | -------- | ----------- |
| `role` | string | بله | نقش نویسنده پیام. یکی از: `user` یا `assistant`. |
| `content` | string یا array | بله | محتوای پیام. می‌تواند یک رشته یا آرایه‌ای از بلوک‌های محتوا هنگام استفاده از ورودی‌های چندرسانه‌ای باشد. |

## مثال‌ها

### تکمیل پیام پایه

```language-selector
bash=:curl https://api.avalai.ir/v1/messages \
  -H "Content-Type: application/json" \
  -H "x-api-key: $AVALAI_API_KEY" \
  -d '{
 "model": "anthropic.claude-sonnet-4-20250514-v1:0",
 "messages": [
 {
 "role": "user",
 "content": "سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟"
 }
 ],
 "max_tokens": 1024
}'

python=:from anthropic import Anthropic

client = Anthropic(
    api_key="AVALAI_API_KEY",
    base_url="https://api.avalai.ir",  # نقطه پایانی API AvalAI بدون /v1
)

response = client.messages.create(
    model="anthropic.claude-sonnet-4-20250514-v1:0",
    messages=[
        {
            "role": "user",
            "content": "سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟",
        }
    ],
    max_tokens=1024,
)

print(response.content)

javascript=:import { Anthropic } from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir", // نقطه پایانی API AvalAI بدون /v1
});

const response = await client.messages.create({
  model: "anthropic.claude-sonnet-4-20250514-v1:0",
  messages: [
    {
      role: "user",
      content:
        "سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟",
    },
  ],
  max_tokens: 1024,
});

console.log(response.content);

go=:package main

import (
	"context"
	"fmt"
	"os"

	"github.com/anthropic/anthropic-sdk-go"
)

func main() {
	client := anthropic.NewClient(
		anthropic.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		anthropic.WithBaseURL("https://api.avalai.ir"),
	)

	resp, err := client.Messages.Create(context.Background(), &anthropic.MessagesRequest{
		Model: "anthropic.claude-sonnet-4-20250514-v1:0",
		Messages: []anthropic.Message{
			{
				Role:    "user",
				Content: "سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟",
			},
		},
		MaxTokens: 1024,
	})

	if err != nil {
		fmt.Printf("Error: %v\n", err)
		return
	}

	fmt.Println(resp.Content)
}

php=:<?php
// مثال PHP برای API پیام‌ها از طریق AvalAI

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید واقعی خود جایگزین کنید
$apiUrl = 'https://api.avalai.ir/v1/messages';

$data = [
 'model' => 'claude-haiku-4-5',
 'messages' => [
 ['role' => 'user', 'content' => 'سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟']
 ],
 'max_tokens' => 1024
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
 'Content-Type: application/json',
 'x-api-key: ' . $apiKey,
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
 echo $response;
} else {
 $responseData = json_decode($response, true);
 echo "دستیار: " . $responseData['content'][0]['text'] . "\n";
}
?>

```

## فرمت پاسخ

```json
{
  "id": "msg_01xyzabcdef",
  "type": "message",
  "role": "assistant",
  "content": [
    {
      "type": "text",
      "text": "محاسبات کوانتومی یک زمینه جذاب است که از اصول مکانیک کوانتومی برای پردازش اطلاعات به روش‌هایی استفاده می‌کند که کامپیوترهای کلاسیک نمی‌توانند. به جای استفاده از بیت‌هایی که یا 0 یا 1 هستند، کامپیوترهای کوانتومی از بیت‌های کوانتومی یا 'کیوبیت‌ها' استفاده می‌کنند که می‌توانند به دلیل خاصیت کوانتومی به نام برهم‌نهی، همزمان در چندین حالت وجود داشته باشند..."
    }
  ],
  "model": "anthropic.claude-sonnet-4-20250514-v1:0",
  "stop_reason": "end_turn",
  "stop_sequence": null,
  "usage": {
    "input_tokens": 15,
    "output_tokens": 75
  }
}
```

## پارامترهای پاسخ

| پارامتر | نوع | توضیحات |
| --------- | ---- | ----------- |
| `id` | string | یک شناسه منحصر به فرد برای پیام. |
| `type` | string | نوع شی، که همیشه "message" است. |
| `role` | string | نقش نویسنده پیام، که برای پاسخ‌ها "assistant" است. |
| `content` | array | آرایه‌ای از بلوک‌های محتوا، معمولا حاوی متن. |
| `model` | string | مدل مورد استفاده برای تولید پیام. |
| `stop_reason` | string | دلیل توقف مدل در تولید توکن‌ها. می‌تواند "end_turn"، "max_tokens"، "stop_sequence" یا مقادیر دیگر باشد. |
| `stop_sequence` | string یا null | اگر مدل به دلیل تولید یک دنباله توقف متوقف شده باشد، این فیلد حاوی آن دنباله است. در غیر این صورت null است. |
| `usage` | object | یک شی حاوی اطلاعات استفاده از توکن. |

### بلوک محتوا

| پارامتر | نوع | توضیحات |
| --------- | ---- | ----------- |
| `type` | string | نوع بلوک محتوا. در حال حاضر "text" یا "image". |
| `text` | string | محتوای متنی اگر نوع "text" باشد. |

### شی استفاده

| پارامتر | نوع | توضیحات |
| --------- | ---- | ----------- |
| `input_tokens` | integer | تعداد توکن‌های استفاده شده در ورودی. |
| `output_tokens` | integer | تعداد توکن‌های استفاده شده در خروجی. |

## جریان‌سازی

برای دریافت پاسخ‌های تدریجی مدل، `stream: true` را در درخواست خود تنظیم کنید:

```javascript
const stream = await client.messages.create({
  model: "anthropic.claude-sonnet-4-20250514-v1:0",
  messages: [
    { role: "user", content: "داستانی درباره یک کامپیوتر کوانتومی بنویسید." },
  ],
  stream: true,
  max_tokens: 1024,
});

for await (const chunk of stream) {
  if (
    chunk.type === "content_block_delta" &&
    chunk.delta.type === "text_delta"
  ) {
    process.stdout.write(chunk.delta.text || "");
  }
}
```

## مدیریت خطا

API ممکن است کدهای خطای مختلفی را برگرداند:

| کد وضعیت | توضیحات |
| ----------- | ----------- |
| 400 | درخواست نامعتبر - درخواست شما نامعتبر است. |
| 401 | غیرمجاز - کلید API شما اشتباه است. |
| 403 | ممنوع - شما اجازه دسترسی به این منبع را ندارید. |
| 404 | یافت نشد - منبع مشخص شده یافت نشد. |
| 429 | درخواست‌های بیش از حد - شما از محدودیت نرخ خود فراتر رفته‌اید. |
| 500 | خطای داخلی سرور - ما مشکلی با سرور خود داشتیم. |

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## پشتیبانی چند ارائه دهنده

از ۱۹ خرداد ۱۴۰۴، پلتفرم AvalAI از فرمت API پیام‌های Anthropic برای دسترسی به مدل‌های چندین ارائه دهنده پشتیبانی می‌کند، از جمله:

- Anthropic (مدل‌های Claude)
- OpenAI
- AWS Bedrock
- Vertex AI
- Gemini
- MiniMax (شامل `minimax-m3` با پشتیبانی کامل از بلوک‌های thinking بومی و استفاده از ابزار)

این رویکرد API یکپارچه به شما امکان می‌دهد از همان ساختار کد برای دسترسی به مدل‌های ارائه‌دهندگان مختلف استفاده کنید و در عین حال سازگاری با کتابخانه‌های کلاینت Anthropic را حفظ کنید.

## منابع مرتبط

- [مدل‌های Anthropic](fa/providers/anthropic.md) - درباره مدل‌های Anthropic موجود بیاموزید
- [تکمیل گفتگو](fa/api-reference/chat.md) - API تکمیل گفتگو سازگار با OpenAI
- [احراز هویت](fa/api-reference/authentication.md) - درباره روش‌های احراز هویت بیاموزید
- [محدودیت‌های نرخ](fa/guides/rate-limits.md) - درباره محدودیت‌های نرخ API بیاموزید
