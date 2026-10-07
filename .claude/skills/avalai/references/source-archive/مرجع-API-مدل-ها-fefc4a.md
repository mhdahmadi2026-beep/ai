# مرجع API مدل‌ها

API مدل‌ها به شما امکان می‌دهد لیست مدل‌های موجود را مشاهده کرده و اطلاعات دقیق درباره مدل‌های خاص شامل قیمت‌گذاری، محدودیت‌های نرخ و قابلیت‌ها را دریافت کنید. AvalAI از هر دو فرمت API OpenAI و Anthropic پشتیبانی می‌کند.

## نقاط پایانی

| متد | نقطه پایانی | احراز هویت | توضیحات |
|-----|-------------|-------------|---------|
| GET | `/v1/models` | بله | لیست تمام مدل‌های موجود |
| GET | `/v1/models/{model_id}` | بله | دریافت اطلاعات یک مدل خاص |
| GET | `/public/models` | خیر | لیست عمومی مدل‌ها |

## تشخیص نوع احراز هویت

AvalAI به طور خودکار فرمت پاسخ را بر اساس هدر احراز هویت شما تشخیص می‌دهد:

| فرمت هدر | فرمت پاسخ |
|----------|-----------|
| `Authorization: Bearer API_KEY` | فرمت OpenAI |
| `x-api-key: API_KEY` | فرمت Anthropic |

## لیست مدل‌ها

تمام مدل‌های موجود را به همراه اطلاعات پایه درباره هر کدام لیست می‌کند.

### فرمت OpenAI

```
GET https://api.avalai.ir/v1/models
```

#### هدرهای درخواست

| هدر | الزامی | توضیحات |
|-----|--------|---------|
| `Authorization` | بله | توکن Bearer: `Bearer YOUR_API_KEY` |

#### نمونه درخواست (فرمت OpenAI)

```language-selector
bash=:curl https://api.avalai.ir/v1/models \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

models = client.models.list()

for model in models.data:
    print(f"{model.id} - {model.owned_by}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const models = await client.models.list();

for (const model of models.data) {
  console.log(`${model.id} - ${model.owned_by}`);
}

go=:package main

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

	models, err := client.Models.List(context.Background())
	if err != nil {
		panic(err)
	}

	for _, model := range models.Data {
		fmt.Printf("%s - %s\n", model.ID, model.OwnedBy)
	}
}

php=:<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$models = $client->models()->list();

foreach ($models->data as $model) {
    echo $model->id . " - " . $model->ownedBy . "\n";
}

```

#### پاسخ (فرمت OpenAI)

```json
{
  "object": "list",
  "data": [
    {
      "id": "glm-5.2",
      "object": "model",
      "owned_by": "zai",
      "min_tier": 0,
      "pricing": {
        "input": 1.4,
        "cached_input": 0.26,
        "output": 4.4
      },
      "mode": "chat",
      "max_tokens": 1000000,
      "max_input_tokens": 991000,
      "max_output_tokens": 128000,
      "supports_function_calling": true,
      "supports_prompt_caching": true,
      "supports_tool_choice": true
    },
    {
      "id": "kimi-k2.7-code",
      "object": "model",
      "owned_by": "moonshot",
      "min_tier": 0,
      "pricing": {
        "input": 1.045,
        "cached_input": 0.19,
        "output": 4.4
      },
      "mode": "chat",
      "max_tokens": 262144,
      "max_input_tokens": 262144,
      "max_output_tokens": 262144,
      "supports_function_calling": true,
      "supports_tool_choice": true,
      "supports_web_search": true
    }
  ]
}
```

### فرمت Anthropic

هنگام استفاده از هدر `x-api-key`، پاسخ از فرمت API Anthropic پیروی می‌کند.

#### هدرهای درخواست

| هدر | الزامی | توضیحات |
|-----|--------|---------|
| `x-api-key` | بله | کلید API شما |

#### نمونه درخواست (فرمت Anthropic)

```language-selector
bash=:curl https://api.avalai.ir/v1/models \
  -H "x-api-key: $AVALAI_API_KEY"

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",
)

models = client.models.list()

for model in models.data:
    print(f"{model.id} - {model.display_name}")

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const models = await client.models.list();

for (const model of models.data) {
  console.log(`${model.id} - ${model.display_name}`);
}

```

#### پاسخ (فرمت Anthropic)

```json
{
  "data": [
    {
      "id": "claude-sonnet-4-20250514",
      "created_at": "2025-02-19T00:00:00Z",
      "display_name": "Claude Sonnet 4",
      "type": "model"
    },
    {
      "id": "claude-3-5-sonnet-20241022",
      "created_at": "2024-10-22T00:00:00Z",
      "display_name": "Claude 3.5 Sonnet",
      "type": "model"
    }
  ],
  "first_id": "claude-sonnet-4-20250514",
  "has_more": true,
  "last_id": "claude-3-5-sonnet-20241022"
}
```

#### پارامترهای کوئری (فرمت Anthropic)

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `after_id` | string | خیر | برگرداندن نتایج بعد از این شناسه مدل |
| `before_id` | string | خیر | برگرداندن نتایج قبل از این شناسه مدل |
| `limit` | number | خیر | حداکثر تعداد مدل‌ها برای برگرداندن |

## مدل‌های عمومی

یک نقطه پایانی عمومی که لیست مدل‌های موجود را بدون نیاز به احراز هویت برمی‌گرداند. این برای نمایش گزینه‌های مدل به کاربران قبل از احراز هویت مفید است.

```
GET https://api.avalai.ir/public/models
```

### نمونه درخواست

```language-selector
bash=:curl https://api.avalai.ir/public/models

python=:import requests

response = requests.get("https://api.avalai.ir/public/models")
models = response.json()

for model in models["data"]:
    print(f"{model['id']} - {model['owned_by']}")

javascript=:const response = await fetch("https://api.avalai.ir/public/models");
const models = await response.json();

for (const model of models.data) {
  console.log(`${model.id} - ${model.owned_by}`);
}

go=:package main

import (
	"encoding/json"
	"fmt"
	"net/http"
)

func main() {
	resp, err := http.Get("https://api.avalai.ir/public/models")
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	var result map[string]interface{}
	json.NewDecoder(resp.Body).Decode(&result)

	data := result["data"].([]interface{})
	for _, model := range data {
		m := model.(map[string]interface{})
		fmt.Printf("%s - %s\n", m["id"], m["owned_by"])
	}
}

php=:<?php

$response = file_get_contents("https://api.avalai.ir/public/models");
$models = json_decode($response, true);

foreach ($models["data"] as $model) {
    echo $model["id"] . " - " . $model["owned_by"] . "\n";
}

```

فرمت پاسخ مشابه نقطه پایانی لیست با فرمت OpenAI است.

## دریافت اطلاعات مدل

اطلاعات دقیق درباره یک مدل خاص را دریافت می‌کند، شامل متادیتای اختصاصی AvalAI، قیمت‌گذاری و محدودیت‌های نرخ.

```
GET https://api.avalai.ir/v1/models/{model_id}
```

### پارامترهای مسیر

| پارامتر | نوع | الزامی | توضیحات |
|---------|-----|--------|---------|
| `model_id` | string | بله | شناسه مدل برای دریافت (مثلا `gpt-5.5`، `claude-sonnet-4.6`) |

### پاسخ فرمت OpenAI

هنگام استفاده از هدر `Authorization: Bearer`، پاسخ شامل فیلدهای استاندارد OpenAI به علاوه یک شیء `extra` اختصاصی AvalAI است.

#### نمونه درخواست (فرمت OpenAI)

```language-selector
bash=:curl https://api.avalai.ir/v1/models/gpt-5.5 \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

model = client.models.retrieve("gpt-5.6-luna")

print(f"Model: {model.id}")
print(f"Owned by: {model.owned_by}")

# دسترسی به داده‌های اضافی AvalAI (به عنوان فیلدهای اضافی در دسترس است)
print(f"Extra data: {model.model_extra}")

javascript=:import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const model = await client.models.retrieve("gpt-5.6-luna");

console.log(`Model: ${model.id}`);
console.log(`Owned by: ${model.owned_by}`);

go=:package main

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

	model, err := client.Models.Get(context.Background(), "gpt-5.6-luna")
	if err != nil {
		panic(err)
	}

	fmt.Printf("Model: %s\n", model.ID)
	fmt.Printf("Owned by: %s\n", model.OwnedBy)
}

php=:<?php

require 'vendor/autoload.php';

$apiKey = getenv('AVALAI_API_KEY');
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();

$model = $client->models()->retrieve('gpt-5.6-luna');

echo "Model: " . $model->id . "\n";
echo "Owned by: " . $model->ownedBy . "\n";

```

#### پاسخ (فرمت OpenAI با Extra اختصاصی AvalAI)

```json
{
  "id": "gpt-5.6-luna",
  "object": "model",
  "created": 1765622594,
  "owned_by": "openai",
  "extra": {
    "metadata": {
      "min_tier": 0,
      "mode": "chat",
      "max_tokens": 128000,
      "max_input_tokens": 1050000,
      "max_output_tokens": 128000,
      "supports_system_messages": true,
      "supports_function_calling": true,
      "supports_parallel_function_calling": true,
      "supports_vision": true,
      "supports_pdf_input": true,
      "supports_prompt_caching": true,
      "supports_tool_choice": true,
      "supports_response_schema": true
    },
    "pricing": {
      "input": 5.0,
      "cached_input": 0.5,
      "output": 30.0
    },
    "rate_limits": {
      "tiers": {
        "0": {
          "rpm": 3.0,
          "tpm": 40000.0
        },
        "1": {
          "rpm": 500.0,
          "tpm": 300000.0
        },
        "2": {
          "rpm": 5000.0,
          "tpm": 3000000.0
        },
        "3": {
          "rpm": 5000.0,
          "tpm": 4000000.0
        },
        "4": {
          "rpm": 10000.0,
          "tpm": 10000000.0
        },
        "5": {
          "rpm": 10000.0,
          "tpm": 30000000.0
        }
      },
      "current": {
        "tier": 5,
        "rpm": 10000.0,
        "tpm": 30000000.0
      }
    }
  }
}
```

### پاسخ فرمت Anthropic

هنگام استفاده از هدر `x-api-key`، پاسخ از فرمت مدل Anthropic به همراه شیء `extra` اختصاصی AvalAI پیروی می‌کند.

#### نمونه درخواست (فرمت Anthropic)

```language-selector
bash=:curl https://api.avalai.ir/v1/models/claude-sonnet-4-20250514 \
  -H "x-api-key: $AVALAI_API_KEY"

python=:import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",
)

model = client.models.retrieve("claude-sonnet-4-20250514")

print(f"Model: {model.id}")
print(f"Display name: {model.display_name}")
print(f"Created at: {model.created_at}")

javascript=:import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const model = await client.models.retrieve("claude-sonnet-4-20250514");

console.log(`Model: ${model.id}`);
console.log(`Display name: ${model.display_name}`);
console.log(`Created at: ${model.created_at}`);

```

#### پاسخ (فرمت Anthropic با Extra اختصاصی AvalAI)

```json
{
  "id": "anthropic.claude-sonnet-4-20250514-v1:0",
  "type": "model",
  "display_name": "Anthropic.Claude Sonnet 4 20250514 V1:0",
  "created_at": "2024-01-01T00:00:00Z",
  "extra": {
    "metadata": {
      "min_tier": 1,
      "mode": "chat",
      "max_tokens": 64000,
      "max_input_tokens": 1000000,
      "max_output_tokens": 64000,
      "supports_function_calling": true,
      "supports_vision": true,
      "supports_pdf_input": true,
      "supports_prompt_caching": true,
      "supports_tool_choice": true,
      "supports_response_schema": true,
      "search_context_cost_per_query": {
        "search_context_size_high": 0.01,
        "search_context_size_low": 0.01,
        "search_context_size_medium": 0.01
      }
    },
    "pricing": {
      "input": 3.0,
      "cached_input": 1.5,
      "output": 15.0
    },
    "rate_limits": {
      "tiers": {
        "1": {
          "rpm": 10.0,
          "tpm": 80000.0
        },
        "2": {
          "rpm": 25.0,
          "tpm": 160000.0
        },
        "3": {
          "rpm": 50.0,
          "tpm": 400000.0
        },
        "4": {
          "rpm": 80.0,
          "tpm": 800000.0
        },
        "5": {
          "rpm": 100.0,
          "tpm": 1000000.0
        }
      },
      "current": {
        "tier": 5,
        "rpm": 100.0,
        "tpm": 1000000.0
      }
    }
  }
}
```

## طرح پاسخ

### شیء مدل (فرمت OpenAI)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه مدل |
| `object` | string | همیشه "model" |
| `created` | integer | زمان یونیکس ایجاد مدل |
| `owned_by` | string | سازمانی که مالک مدل است |

### شیء مدل (فرمت Anthropic)

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `id` | string | شناسه مدل |
| `created_at` | string | زمان ایجاد مدل به فرمت ISO 8601 |
| `display_name` | string | نام قابل خواندن برای مدل |
| `type` | string | همیشه "model" |

### شیء Extra اختصاصی AvalAI

شیء `extra` فقط در نقطه پایانی دریافت مدل برگردانده می‌شود و حاوی اطلاعات اختصاصی AvalAI است.

#### شیء Metadata

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `min_tier` | integer | حداقل [سطح](fa/rate-limits.md) مورد نیاز برای استفاده از این مدل (۰-۵) |
| `mode` | string | حالت مدل. یکی از: `chat`, `embedding`, `completion`, `image_generation`, `video_generation`, `audio_transcription`, `audio_speech`, `ocr`, `moderation`, `rerank`, `search` |
| `max_tokens` | integer | حداکثر کل توکن‌ها |
| `max_input_tokens` | integer | حداکثر توکن‌های ورودی |
| `max_output_tokens` | integer | حداکثر توکن‌های خروجی |
| `supports_system_messages` | boolean | آیا مدل از پیام‌های سیستم پشتیبانی می‌کند |
| `supports_function_calling` | boolean | آیا مدل از فراخوانی تابع/ابزار پشتیبانی می‌کند |
| `supports_parallel_function_calling` | boolean | آیا مدل از فراخوانی موازی توابع پشتیبانی می‌کند |
| `supports_vision` | boolean | آیا مدل از ورودی‌های تصویری پشتیبانی می‌کند |
| `supports_pdf_input` | boolean | آیا مدل از ورودی‌های فایل PDF پشتیبانی می‌کند |
| `supports_prompt_caching` | boolean | آیا مدل از کش کردن پرامپت پشتیبانی می‌کند |
| `supports_tool_choice` | boolean | آیا مدل از پارامتر انتخاب ابزار پشتیبانی می‌کند |
| `supports_response_schema` | boolean | آیا مدل از طرح‌های خروجی ساختاریافته پشتیبانی می‌کند |

#### شیء Pricing

قیمت‌گذاری بسته به نوع مدل متفاوت است. فیلدهای موجود به حالت (mode) مدل بستگی دارد.

**قیمت‌گذاری استاندارد مبتنی بر توکن (مدل‌های chat، embedding، completion):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input` | number | هزینه به ازای هر ۱ میلیون توکن ورودی (دلار) |
| `cached_input` | number | هزینه به ازای هر ۱ میلیون توکن ورودی کش شده (دلار) |
| `output` | number | هزینه به ازای هر ۱ میلیون توکن خروجی (دلار) |
| `audio_input` | number | (اختیاری) هزینه به ازای هر ۱ میلیون توکن ورودی صوتی (دلار) |
| `image_input` | number | (اختیاری) هزینه به ازای هر ۱ میلیون توکن ورودی تصویر (دلار) |
| `image_output` | number | (اختیاری) هزینه به ازای هر ۱ میلیون توکن خروجی تصویر (دلار) |
| `search_context_cost_per_query` | object | (اختیاری) قیمت‌گذاری زمینه جستجو برای مدل‌های چت دارای قابلیت جستجو |

**مدل‌های تولید تصویر (`mode: image_generation`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `output_cost_per_image` | number | هزینه پایه به ازای هر تصویر تولید شده (دلار) |
| `output_cost_per_image_{resolution}` | number | هزینه به ازای هر تصویر در رزولوشن خاص (مثلا `1920x1080`، `4096x4096`) |

**مدل‌های تولید ویدیو (`mode: video_generation`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `output_cost_per_video_per_second` | number | هزینه پایه به ازای هر ثانیه ویدیو (دلار) |
| `output_cost_per_video_per_second_{resolution}` | number | هزینه به ازای هر ثانیه در رزولوشن خاص (مثلا `720x1280`، `1792x1024`) |

**مدل‌های رونویسی صوتی (`mode: audio_transcription`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input_cost_per_second` | number | هزینه به ازای هر ثانیه ورودی صوتی (دلار) |

**مدل‌های تبدیل متن به گفتار (`mode: audio_speech`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input_cost_per_character` | number | هزینه به ازای هر کاراکتر متن ورودی (دلار) |

**مدل‌های OCR (`mode: ocr`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input_cost_per_page` | number | هزینه به ازای هر صفحه پردازش شده (دلار) |

**مدل‌های رتبه‌بندی مجدد (`mode: rerank`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input_cost_per_query` | number | هزینه به ازای هر پرس‌وجوی رتبه‌بندی مجدد (دلار) |

**مدل‌های جستجو (`mode: search`):**

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `input_cost_per_query` | number | هزینه به ازای هر پرس‌وجوی جستجو (دلار) |

#### شیء Rate Limits

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `tiers` | object | محدودیت‌های نرخ برای هر سطح (۰-۵) |
| `current` | object | محدودیت‌های نرخ فعلی شما بر اساس سطحتان |

هر سطح شامل:

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `rpm` | number | درخواست در دقیقه |
| `tpm` | number | توکن در دقیقه |

شیء `current` همچنین شامل:

| فیلد | نوع | توضیحات |
|------|-----|---------|
| `tier` | integer | سطح فعلی شما |

برای اطلاعات بیشتر درباره سطوح و نحوه ارتقا، به [محدودیت‌های نرخ](fa/rate-limits.md) مراجعه کنید.

## مدیریت خطا

| کد وضعیت | توضیحات |
|----------|---------|
| 401 | غیرمجاز - کلید API نامعتبر یا وجود ندارد |
| 404 | یافت نشد - مدل وجود ندارد |
| 429 | درخواست‌های بیش از حد - محدودیت نرخ برخورد کرده |
| 500 | خطای داخلی سرور |

## منابع مرتبط

- [احراز هویت](fa/api-reference/authentication.md) - آشنایی با روش‌های احراز هویت
- [محدودیت‌های نرخ](fa/rate-limits.md) - درک محدودیت‌های نرخ مبتنی بر سطح
- [نمای کلی مدل‌ها](fa/models/index.md) - مرور مدل‌های موجود بر اساس ارائه‌دهنده
- [جزئیات مدل‌ها](fa/models/model-details.md) - مشخصات دقیق مدل‌ها
- [قیمت‌گذاری](fa/pricing.md) - اطلاعات قیمت‌گذاری
