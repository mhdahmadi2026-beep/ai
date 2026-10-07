# راهنمای نظارت (Moderation)

از [API نظارت](fa/api-reference/moderation.md) AvalAI برای بررسی اینکه آیا ورودی‌های متنی یا تصویری طبق خط‌مشی‌های محتوای تعریف‌شده، بالقوه مضر هستند یا خیر، استفاده کنید. این به تضمین ایمنی و انطباق در برنامه‌های شما کمک می‌کند.

اگر محتوای مضر شناسایی شود، می‌توانید اقدام اصلاحی انجام دهید، مانند فیلتر کردن محتوا یا پرچم‌گذاری حساب‌های کاربری. دسترسی به نقطه پایانی نظارت از طریق AvalAI ممکن است رایگان باشد یا مشمول قیمت‌گذاری خاصی باشد؛ لطفا [صفحه قیمت‌گذاری](fa/pricing.md) AvalAI را بررسی کنید.

AvalAI دسترسی به مدل‌های نظارت را فراهم می‌کند، که به طور بالقوه شامل موارد زیر است:

- **`omni-moderation-latest` (توصیه شده):** از دسته‌بندی‌های بیشتر و ورودی‌های چندوجهی (متن + تصویر) پشتیبانی می‌کند.
- **`text-moderation-latest` (میراثی):** فقط از ورودی‌های متنی و دسته‌بندی‌های کمتری پشتیبانی می‌کند.

برای مدل‌های نظارت موجود فعلی، [بررسی اجمالی مدل‌ها](fa/models/index.md) AvalAI را بررسی کنید.

## گردش‌کار تصمیم‌گیری Moderation

راهنمای moderation در OpenAI زمانی بیشترین ارزش را دارد که به یک workflow محصولی تبدیل شود، نه فقط یک API call جدا. برای برنامه‌های AvalAI:

1. **ورودی را پیش از generation طبقه‌بندی کنید** وقتی کاربر می‌تواند متن آزاد، تصویر، URL، فایل یا محتوای retrieval ارسال کند.
2. **فقط پس از عبور از policy تولید کنید** یا درخواست را به مسیر محدود safe-completion/refusal هدایت کنید.
3. **خروجی تولیدشده را پیش از نمایش طبقه‌بندی کنید** مخصوصا برای سطوح عمومی، اجتماعی، marketplace، آموزشی یا زیر ۱۸ سال.
4. **thresholdها را با eval تنظیم کنید:** `flagged` را سیگنال پیش‌فرض قوی بدانید، اما آستانه‌های سفارشی `category_scores` را با مثال‌های محصول و labelهای human review کالیبره کنید.
5. **ردپای review نگه دارید:** `avalai-request-id`، مدل، route، کاربر hash‌شده یا `safety_identifier`، دسته‌های moderation و اقدام نهایی محصول را بدون ذخیره داده شخصی غیرضروری log کنید.
6. **مسیر escalation تعریف کنید:** برای تصمیم‌های blocked، borderline و appealed مشخص کنید چه اتفاقی می‌افتد تا درخواست کاربر بی‌صدا حذف نشود.

## شروع سریع

### نظارت ورودی‌های متنی

اطلاعات طبقه‌بندی را برای یک ورودی متنی دریافت کنید:

```language-selector
python=:# مثال پایتون با استفاده از API نظارت AvalAI
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

try:
    response = client.moderations.create(
        model="omni-moderation-latest",  # یا مدل دیگری که از طریق AvalAI در دسترس است
        input="متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.",
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")

javascript=:// مثال جاوااسکریپت با استفاده از API نظارت AvalAI
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY, // اطمینان حاصل کنید که AVALAI_API_KEY تنظیم شده است
  baseURL: "https://api.avalai.ir/v1", // از URL پایه AvalAI استفاده کنید
});

async function main() {
  try {
    const moderation = await client.moderations.create({
      model: "omni-moderation-latest", // یا مدل دیگری که از طریق AvalAI در دسترس است
      input: "متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.",
    });
    console.log(moderation);
  } catch (error) {
    console.error("Error calling moderation API: ", error);
  }
}
main();

bash=:# مثال cURL با استفاده از API نظارت AvalAI
curl https://api.avalai.ir/v1/moderations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "omni-moderation-latest",
  "input": "متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند."
}'

php=:<?php
// مثال PHP با استفاده از API نظارت AvalAI
require_once 'vendor/autoload.php';

// استفاده از کتابخانه کلاینت PHP OpenAI
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

try {
  // ایجاد درخواست نظارت
  $response = $client->moderations()->create([
  'model' => 'omni-moderation-latest',
  'input' => 'متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.'
  ]);

  // نمایش پاسخ
  print_r($response->toArray());
} catch (\Exception $e) {
  echo "خطا: " . $e->getMessage() . "\n";
}

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("AVALAI_API_KEY")
	client.BaseURL = "https://api.avalai.ir/v1"

	resp, err := client.Moderations(
		context.Background(),
		openai.ModerationRequest{
			Input: "متن نمونه‌ای که ممکن است خط‌مشی محتوا را نقض کند.",
			Model: openai.ModerationLatest,
		},
	)

	if err != nil {
		fmt.Printf("خطای نظارت: %v\n", err)
		return
	}

	// بررسی اینکه آیا متن پرچم‌گذاری شده است
	if resp.Results[0].Flagged {
		fmt.Println("این محتوا پرچم‌گذاری شده است!")
	}

	// بررسی دسته‌بندی‌های خاص
	for category, score := range resp.Results[0].CategoryScores {
		if score > 0.5 {
			fmt.Printf("محتوا برای %s با امتیاز %.2f پرچم‌گذاری شده است\n", category, score)
		}
	}
}

```

### نظارت ورودی‌های تصویر و متن (چندوجهی)

_نیاز به یک مدل نظارت چندوجهی مانند `omni-moderation-latest` دارد._

اطلاعات طبقه‌بندی را برای ورودی ترکیبی تصویر و متن دریافت کنید:

```language-selector
python=:# مثال پایتون با استفاده از نظارت چندوجهی AvalAI
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

try:
    response = client.moderations.create(
        model="omni-moderation-latest",  # اطمینان حاصل کنید که مدل از چندوجهی پشتیبانی می‌کند
        input=[
            {"type": "text", "text": "توضیحات همراه تصویر."},
            {
                "type": "image_url",
                "image_url": {
                    "url": "https://example.com/image_to_moderate.png"
                    # یا Base64: "url": "data:image/png;base64,abcdefg..."
                },
            },
        ],
    )
    print(response)
except Exception as e:
    print(f"An error occurred: {e}")

javascript=:// مثال جاوااسکریپت با استفاده از نظارت چندوجهی AvalAI
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function main() {
  try {
    const moderation = await client.moderations.create({
      model: "omni-moderation-latest", // اطمینان حاصل کنید که مدل از چندوجهی پشتیبانی می‌کند
      input: [
        { type: "text", text: "توضیحات همراه تصویر." },
        {
          type: "image_url",
          image_url: {
            url: "https://example.com/image_to_moderate.png",
            // یا Base64: url: "data:image/png;base64,abcdefg..."
          },
        },
      ],
    });
    console.log(moderation);
  } catch (error) {
    console.error("Error calling moderation API: ", error);
  }
}
main();

bash=:# مثال cURL با استفاده از نظارت چندوجهی AvalAI
curl https://api.avalai.ir/v1/moderations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "omni-moderation-latest",
  "input": [
  { "type": "text", "text": "توضیحات همراه تصویر." },
  {
    "type": "image_url",
    "image_url": {
      "url": "https://example.com/image_to_moderate.png"
    }
  }
  ]
}'

php=:<?php
// مثال PHP با استفاده از نظارت چندوجهی AvalAI
require_once 'vendor/autoload.php';

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

try {
  $response = $client->moderations()->create([
  'model' => 'omni-moderation-latest',
  'input' => [
  [
  'type' => 'text',
  'text' => 'توضیحات همراه تصویر.'
  ],
  [
  'type' => 'image_url',
  'image_url' => [
  'url' => 'https://example.com/image_to_moderate.png'
  // یا Base64: 'url' => 'data:image/png;base64,abcdefg...'
  ]
  ]
  ]
  ]);

  print_r($response->toArray());
} catch (\Exception $e) {
  echo "خطا: " . $e->getMessage() . "\n";
}

go=:package main

import (
	"context"
	"fmt"
	openai "github.com/openai/openai-go"
)

func main() {
	client := openai.NewClient("AVALAI_API_KEY")
	client.BaseURL = "https://api.avalai.ir/v1"

	// ایجاد ساختار ورودی برای نظارت چندوجهی
	input := []openai.ModerationInput{
		{
			Type: "text",
			Text: "توضیحات همراه تصویر.",
		},
		{
			Type: "image_url",
			ImageURL: &openai.ImageURL{
				URL: "https://example.com/image_to_moderate.png",
			},
		},
	}

	resp, err := client.Moderations(
		context.Background(),
		openai.ModerationRequest{
			Input: input,
			Model: "omni-moderation-latest",
		},
	)

	if err != nil {
		fmt.Printf("خطای نظارت: %v\n", err)
		return
	}

	// پردازش پاسخ
	if resp.Results[0].Flagged {
		fmt.Println("این محتوا پرچم‌گذاری شده است!")
	}

	// بررسی دسته‌بندی‌های خاص
	for category, score := range resp.Results[0].CategoryScores {
		if score > 0.5 {
			fmt.Printf("محتوا برای %s با امتیاز %.2f پرچم‌گذاری شده است\n", category, score)
		}
	}
}

```

## نظارت روی محتوای تولیدشده به‌صورت Inline

وقتی route انتخابی AvalAI از inline moderation سازگار با OpenAI پشتیبانی می‌کند، می‌توانید امتیازهای moderation را در همان فراخوانی `/v1/responses` یا `/v1/chat/completions` که پاسخ را تولید می‌کند درخواست کنید. این الگو زمانی مفید است که هم پاسخ تولیدشده و هم سیگنال ایمنی برای ورودی/خروجی را با هم لازم دارید.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="برای یک درخواست خطرناک، یک امتناع کوتاه و جایگزین امن بنویس.",
    moderation={"model": "omni-moderation-latest"},
)

if response.moderation.input.flagged or response.moderation.output.flagged:
    print("پیش از نمایش پاسخ، آن را وارد صف review کنید.")
else:
    print(response.output_text)
```

Inline moderation را سیگنال policy بدانید، نه تصمیم نهایی خودکار. حتی یک refusal امن هم ممکن است امتیاز بالا بگیرد، چون درباره محتوای مضر صحبت می‌کند. در پاسخ‌های streaming، امتیازهای moderation فقط پس از کامل شدن کل خروجی تولیدشده آماده می‌شوند و همراه deltaهای جزئی نمی‌آیند. اگر inline moderation برای مدل یا route انتخابی فعال نیست، پیش از نمایش یا اقدام downstream، `POST /v1/moderations` را جداگانه فراخوانی کنید.

در workflowهای ابزارمحور، moderation می‌تواند argumentهای tool call و خروجی tool را وقتی در محتوای گفتگو آمده‌اند پوشش دهد. اما نام ابزار، توضیح ابزار، schema ابزار یا schema خروجی ساختاریافته را moderation نمی‌کند؛ این سطوح را جداگانه validate کنید.

### درک پاسخ

پاسخ API جزئیات مربوط به نقض‌های احتمالی خط‌مشی را ارائه می‌دهد:

```json
{
  "id": "modr-...", // شناسه درخواست نظارت

  "model": "omni-moderation-latest", // مدل استفاده شده

  "results": [
    {
      "flagged": true, // اگر هر دسته‌بندی بالاتر از آستانه پرچم‌گذاری شود، True است

      "categories": {
        // پرچم‌های بولی برای هر دسته‌بندی

        "sexual": false,
        "hate": false,
        "harassment": false,
        "self-harm": false,
        "sexual/minors": false,
        "hate/threatening": false,
        "violence/graphic": false,
        "self-harm/intent": false,
        "self-harm/instructions": false,
        "harassment/threatening": false,
        "violence": true, // مثال: برای خشونت پرچم‌گذاری شده است

        // دسته‌بندی‌های خاص Omni:

        "illicit": false,
        "illicit/violent": false
      },
      "category_scores": {
        // امتیازات اطمینان (۰-۱) برای هر دسته‌بندی

        "sexual": 0.0001,
        "hate": 0.0002,
        // ... امتیازات دیگر

        "violence": 0.987, // مثال: اطمینان بالا برای خشونت

        "violence/graphic": 0.123
        // ... امتیازات omni

      },
      // فقط برای مدل‌های omni وجود دارد:

      "category_applied_input_types": {
        "sexual": ["text", "image"], // کدام نوع ورودی باعث پرچم‌گذاری شده است

        "hate": ["text"],
        // ... دسته‌بندی‌های دیگر

        "violence": ["image"] // مثال: تصویر باعث پرچم‌گذاری خشونت شده است

      }
    }
  ]
}
```

- **`flagged`**: پرچم کلی (`true` اگر امتیاز هر دسته‌بندی از آستانه‌های داخلی فراتر رود).
- **`categories`**: پرچم‌های بولی که نشان می‌دهند آیا یک دسته‌بندی نقض شده است یا خیر.
- **`category_scores`**: امتیاز اطمینان مدل (۰ تا ۱) برای هر نقض دسته‌بندی. از این امتیازات برای خط‌مشی‌های سفارشی استفاده کنید، اما توجه داشته باشید که ممکن است در صورت به‌روزرسانی مدل زیربنایی توسط ارائه دهنده، نیاز به تنظیم مجدد داشته باشند.
- **`category_applied_input_types`** (فقط مدل‌های Omni): نشان می‌دهد که آیا ورودی `text` یا `image` (یا هر دو) به پرچم‌گذاری یک دسته‌بندی کمک کرده است یا خیر.

## طبقه‌بندی‌های محتوا

نقطه پایانی نظارت محتوا را در چندین دسته‌بندی بررسی می‌کند. در دسترس بودن و پشتیبانی از نوع ورودی (متن/تصویر) به مدل مورد استفاده بستگی دارد (مدل‌های `omni` به طور کلی از دسته‌بندی‌های بیشتر و ورودی تصویر پشتیبانی می‌کنند).

| دسته‌بندی                | توضیحات                                                                                                   | مدل‌ها   | ورودی‌های پشتیبانی شده |
| :----------------------- | :-------------------------------------------------------------------------------------------------------- | :------- | :--------------------- |
| `harassment`             | بیان، تحریک یا ترویج زبان آزاردهنده نسبت به هر هدفی.                                                      | همه      | فقط متن                |
| `harassment/threatening` | آزار و اذیتی که شامل تهدید به خشونت یا آسیب جدی نیز می‌شود.                                               | همه      | فقط متن                |
| `hate`                   | بیان، تحریک یا ترویج نفرت بر اساس ویژگی‌های محافظت شده (نژاد، جنسیت، مذهب و غیره).                        | همه      | فقط متن                |
| `hate/threatening`       | محتوای نفرت‌انگیز که شامل تهدید به خشونت یا آسیب جدی نسبت به گروه هدف نیز می‌شود.                         | همه      | فقط متن                |
| `illicit`                | مشاوره یا دستورالعمل برای ارتکاب اعمال غیرقانونی (مانند نحوه دزدی از مغازه).                              | فقط Omni | فقط متن                |
| `illicit/violent`        | محتوای غیرقانونی که به خشونت یا تهیه سلاح نیز اشاره دارد.                                                 | فقط Omni | فقط متن                |
| `self-harm`              | ترویج، تشویق یا به تصویر کشیدن اعمال خودآزاری (خودکشی، بریدن، اختلالات خوردن).                            | همه      | متن و تصویر            |
| `self-harm/intent`       | گوینده قصد خود را برای انجام خودآزاری بیان می‌کند.                                                        | همه      | متن و تصویر            |
| `self-harm/instructions` | تشویق یا ارائه دستورالعمل برای خودآزاری.                                                                  | همه      | متن و تصویر            |
| `sexual`                 | محتوایی که برای برانگیختن هیجان جنسی یا ترویج خدمات مستهجن در نظر گرفته شده است (به استثنای آموزش/سلامت). | همه      | متن و تصویر            |
| `sexual/minors`          | محتوای مستهجن شامل افراد زیر ۱۸ سال.                                                                      | همه      | فقط متن                |
| `violence`               | به تصویر کشیدن مرگ، خشونت یا آسیب فیزیکی.                                                                 | همه      | متن و تصویر            |
| `violence/graphic`       | به تصویر کشیدن مرگ، خشونت یا آسیب فیزیکی با جزئیات گرافیکی.                                               | همه      | متن و تصویر            |

_(توجه: "همه" معمولا به هر دو `omni-moderation-latest` و `text-moderation-latest` اشاره دارد. "فقط Omni" به دسته‌بندی‌هایی اشاره دارد که با `omni-moderation-latest` و اسنپ‌شات‌های آن اضافه شده‌اند)._
