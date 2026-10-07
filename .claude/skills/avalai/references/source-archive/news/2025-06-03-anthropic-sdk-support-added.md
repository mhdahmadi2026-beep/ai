# پشتیبانی از SDK رسمی Anthropic به AvalAI اضافه شد

**تاریخ:** 1404-03-13 / (2025-06-03)

## خلاصه

AvalAI اکنون از SDK های رسمی Anthropic پشتیبانی می‌کند و به توسعه‌دهندگان امکان استفاده از کتابخانه‌های کلاینت بومی Anthropic برای دسترسی به مدل‌های Claude از طریق سیستم API یکپارچه ما را می‌دهد. این بهبود انعطاف پذیری بیشتری برای توسعه‌دهندگان فراهم می‌کند و آنها را قادر می‌سازد بین SDK های سازگار با OpenAI یا SDK های رسمی Anthropic انتخاب کنند در حالی که دسترسی به همان مدل‌های قدرتمند Claude را حفظ می‌کنند.

---

## جزئیات

ما با افتخار اعلام می‌کنیم که AvalAI اکنون علاوه بر دسترسی API سازگار با OpenAI موجود، از SDK های رسمی Anthropic نیز پشتیبانی می‌کند. این بدان معناست که توسعه‌دهندگان اکنون می‌توانند از کتابخانه‌های کلاینت بومی Anthropic استفاده کنند در حالی که از سیستم API یکپارچه و قیمت‌گذاری رقابتی AvalAI بهره‌مند می‌شوند.

### چه تغییراتی ایجاد شده است

پیش از این، AvalAI از دسترسی به تمام مدل‌ها، از جمله سری Claude شرکت Anthropic، از طریق SDK ها و طرح API سازگار با OpenAI پشتیبانی می‌کرد. اکنون، کاربران گزینه اضافی استفاده از **SDK های رسمی Anthropic** با نحو و ویژگی‌های آشنای خود را دارند که تجربه توسعه بومی‌تری برای مدل‌های Claude فراهم می‌کند.

### مزایای کلیدی

- **انتخاب توسعه‌دهنده**: بین SDK OpenAI (رویکرد یکپارچه) یا SDK Anthropic (رویکرد بومی) انتخاب کنید
- **تجربه بومی**: از SDK های رسمی Anthropic با نحو و نام پارامترهای آشنا استفاده کنید
- **ویژگی‌های بتا**: دسترسی به فضای نام بتای Anthropic برای ویژگی‌های آزمایشی
- **احراز هویت یکسان**: همان کلید API AvalAI در هر دو رویکرد SDK کار می‌کند
- **بدون تغییرات شکننده**: پیاده‌سازی‌های موجود SDK OpenAI همچنان بدون تغییر کار می‌کنند

### زبان‌های برنامه‌نویسی پشتیبانی شده

ما از SDK های رسمی Anthropic برای زبان‌های برنامه‌نویسی زیر پشتیبانی می‌کنیم:

- **Python** - بسته `anthropic`
- **TypeScript/JavaScript** - بسته `@anthropic-ai/sdk`
- **Go** - بسته `anthropic-sdk-go`
- **Ruby** - gem `anthropic`

### شروع کار

#### Python

```python
import anthropic

client = anthropic.Anthropic(
    api_key="AVALAI_API_KEY",  # با کلید API واقعی خود جایگزین کنید
    base_url="https://api.avalai.ir",  # نقطه پایانی API AvalAI بدون /v1
)

message = client.messages.create(
    model="anthropic.claude-3-5-haiku-20241022-v1:0",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، کلود"}],
)
print(message.content)
```

#### TypeScript/JavaScript

```javascript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY, // با کلید API واقعی خود جایگزین کنید
  baseURL: "https://api.avalai.ir", // نقطه پایانی API AvalAI بدون /v1
});

const msg = await anthropic.messages.create({
  model: "anthropic.claude-3-5-haiku-20241022-v1:0",
  max_tokens: 1024,
  messages: [{ role: "user", content: "سلام، کلود" }],
});
console.log(msg);
```

#### Go

```go
package main

import (
	"context"
	"fmt"
	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey("your-avalai-api-key"),    // با کلید API واقعی خود جایگزین کنید
		option.WithBaseURL("https://api.avalai.ir"), // نقطه پایانی AvalAI بدون /v1
	)

	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.F(anthropic.ModelClaudeSonnet4_0),
		MaxTokens: anthropic.F(int64(1024)),
		Messages: anthropic.F([]anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("کواترنیون چیست؟")),
		}),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", message.Content)
}
```

#### Ruby

```ruby
require "bundler/setup"
require "anthropic"

anthropic = Anthropic::Client.new(
    api_key: "your-avalai-api-key", # با کلید API واقعی خود جایگزین کنید
    base_url: "https://api.avalai.ir" # نقطه پایانی AvalAI بدون /v1
)

message = anthropic.messages.create(
    max_tokens: 1024,
    messages: [{
            role: "user",
            content: "سلام، کلود"
        }
    ],
    model: "anthropic.claude-3-5-haiku-20241022-v1:0"
)

puts(message.content)
```

### پشتیبانی از ویژگی‌های بتا

تمام SDK های Anthropic شامل پشتیبانی از فضای نام بتا برای دسترسی به ویژگی‌های آزمایشی هستند:

```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",  # نقطه پایانی API AvalAI بدون /v1
)

message = client.beta.messages.create(
    model="anthropic.claude-3-5-haiku-20241022-v1:0",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، کلود"}],
    betas=["beta-feature-name"],
)
print(message.content)
```

### مثال cURL

همچنین می‌توانید از درخواست‌های HTTP مستقیم با طرح API Anthropic استفاده کنید:

```bash
curl https://api.avalai.ir/v1/messages \
  --header "x-api-key: $AVALAI_API_KEY" \
  --header "content-type: application/json" \
  --data '{
 "model": "anthropic.claude-3-5-haiku-20241022-v1:0",
 "max_tokens": 1024,
 "messages": [
 {"role": "user", "content": "سلام دنیا"}
 ]
 }'
```

### مدل‌های Claude موجود

تمام مدل‌های Claude موجود از طریق AvalAI می‌توانند با استفاده از SDK های OpenAI یا Anthropic مورد دسترسی قرار گیرند:

- **Claude Opus 4** - `anthropic.claude-opus-4-20250514-v1:0`
- **Claude Sonnet 4** - `anthropic.claude-sonnet-4-20250514-v1:0`
- **Claude 3.7 Sonnet** - `anthropic.claude-3-7-sonnet-20250219-v1:0`
- **Claude 3.5 Sonnet** - `anthropic.claude-3-5-sonnet-20241022-v2:0`
- **Claude 3.5 Haiku** - `anthropic.claude-3-5-haiku-20241022-v1:0`
- **Claude 3 Opus** - `anthropic.claude-3-opus-20240229-v1:0`
- **Claude 3 Sonnet** - `anthropic.claude-3-sonnet-20240229-v1:0`
- **Claude 3 Haiku** - `anthropic.claude-3-haiku-20240307-v1:0`

برای فهرست کامل مدل‌های موجود، [مستندات مدل‌های Anthropic](fa/providers/anthropic.md) ما را ببینید.

---

## لینک‌های مرتبط

- [مستندات کتابخانه‌های به‌روزرسانی شده](fa/libraries.md) - راهنمای کامل راه‌اندازی SDK
- [راهنمای شروع سریع](fa/quickstart.md) - در عرض چند دقیقه شروع کنید
- [مدل‌های Anthropic](fa/providers/anthropic.md) - مدل‌های Claude موجود
- [مرجع API](fa/api-reference/introduction.md) - مستندات تفصیلی API
- [راهنمای احراز هویت](fa/api-reference/authentication.md) - راه‌اندازی کلید API و بهترین شیوه‌ها
