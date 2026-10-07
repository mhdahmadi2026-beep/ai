# مرجع API AvalAI

به مستندات مرجع API AvalAI خوش آمدید. AvalAI یک API یکپارچه ارائه می‌دهد که با ساختار API OpenAI سازگار است و به شما امکان می‌دهد از طریق یک رابط واحد و سازگار به مدل‌های چندین ارائه دهنده دسترسی داشته باشید.

## URL پایه

تمام درخواست‌های API باید به URL پایه زیر ارسال شوند:

```
https://api.avalai.ir/v1
```

## احراز هویت

تمام نقاط پایانی API نیاز به احراز هویت دارند. شما باید کلید API خود را در هدر `Authorization` هر درخواست وارد کنید. برای جزئیات بیشتر به راهنمای [احراز هویت](fa/api-reference/authentication.md) مراجعه کنید.

## نقطه شروع: سطح API مناسب را انتخاب کنید

نمای کلی API در OpenAI توصیه می‌کند قبل از کدنویسی، سطح API مناسب را انتخاب کنید. برای AvalAI از این checklist مسیریابی شروع کنید:

| نیاز | مسیر AvalAI | نکته |
| --- | --- | --- |
| برنامه جدید متنی، reasoning، چندوجهی یا ابزارمحور | [`/v1/responses`](fa/api-reference/responses.md) | وقتی route مدل انتخابی از Responses پشتیبانی می‌کند، این مسیر را برای state، ابزارها و شیء خروجی غنی‌تر ترجیح دهید. |
| یکپارچه‌سازی chat موجود یا سازگاری گسترده با providerها | [`/v1/chat/completions`](fa/api-reference/chat.md) | برای برنامه‌های chat بالغ و providerهایی که schema تکمیل گفتگو را ارائه می‌کنند نگه دارید. |
| گفتار یا فایل صوتی request-based | [`/v1/audio/*`](fa/api-reference/audio.md) | برای transcription، translation و text-to-speech با فایل محدود یا گفتار تولیدشده استفاده کنید. |
| صدای زنده یا session کم‌تاخیر | [راهنمای معماری Realtime](fa/guides/realtime-audio.md) | تا وقتی route متناظر AvalAI برای حساب شما فعال نشده، مستندات Realtime OpenAI را فقط راهنمای معماری بدانید. |
| گزارش استفاده، هزینه و reseller | [`user/v1`](fa/api-reference/user.md) | endpointهای اختصاصی AvalAI برای تراکنش‌ها، خلاصه استفاده و reconciliation صورتحساب. |
| مدیریت سازمانی | داشبورد AvalAI یا پشتیبانی | فرض نکنید endpointهای Administration شرکت OpenAI مستقیما به مدیریت حساب AvalAI نگاشت می‌شوند. |

## نقاط پایانی API

### پاسخ‌ها (Responses)

API پاسخ‌ها نقطه شروع پیشنهادی برای workflowهای جدید OpenAI-family در تولید متن، استدلال، چندوجهی و ابزارمحور است، وقتی route مدل انتخابی از آن پشتیبانی می‌کند.

[اطلاعات بیشتر در مورد پاسخ‌ها →](fa/api-reference/responses.md)

### تکمیل گفتگو (Chat Completions)

API تکمیل گفتگو همچنان برای یکپارچه‌سازی‌های chat موجود و routeهایی که schema چت را ارائه می‌دهند پشتیبانی می‌شود.

[اطلاعات بیشتر در مورد تکمیل گفتگو →](fa/api-reference/chat.md)

### تصاویر (Images)

API تصاویر به شما امکان می‌دهد با استفاده از مدل‌های هوش مصنوعی مانند DALL·E تصاویر را تولید و ویرایش کنید.

[اطلاعات بیشتر در مورد تصاویر →](fa/api-reference/images.md)

### بردارهای تعبیه‌سازی (Embeddings)

API بردارهای تعبیه‌سازی به شما امکان می‌دهد متن را به نمایش‌های برداری برای استفاده در جستجو، خوشه‌بندی و سایر وظایف یادگیری ماشین تبدیل کنید.

[اطلاعات بیشتر در مورد بردارهای تعبیه‌سازی →](fa/api-reference/embeddings.md)

### صدا (Audio)

API صدا قابلیت‌های رونویسی، ترجمه و تولید محتوای صوتی را فراهم می‌کند.

[اطلاعات بیشتر در مورد صدا →](fa/api-reference/audio.md)

### نظارت (Moderation)

API نظارت به شما کمک می‌کند محتوای بالقوه مضر در متن را شناسایی کنید.

[اطلاعات بیشتر در مورد نظارت →](fa/api-reference/moderation.md)

### API کاربر (User API)

API کاربر ردیابی دقیق هزینه، تاریخچه تراکنش‌ها و تحلیل استفاده را برای فراخوانی‌های API شما فراهم می‌کند. مناسب برای فروشندگان، سازمان‌های بزرگ و برنامه‌های تولیدی که به صورتحساب دقیق نیاز دارند.

**ویژگی‌های کلیدی:**
- ردیابی دقیق هزینه با استفاده از [`avalai-request-id`](fa/api-reference/response-headers.md#avalai-request-id) از هدرهای پاسخ با دقت 100٪
- تاریخچه تراکنش‌ها با قابلیت فیلتر
- تحلیل و خلاصه استفاده
- در دسترس ظرف 30 ثانیه پس از فراخوانی API

[اطلاعات بیشتر در مورد API کاربر →](fa/api-reference/user.md)

## فرمت‌های درخواست و پاسخ

تمام نقاط پایانی API داده‌های JSON را می‌پذیرند و برمی‌گردانند. اطمینان حاصل کنید که هدر `Content-Type: application/json` را در درخواست‌های خود وارد کنید.

### مثال درخواست

```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
"model": "gpt-5.6-luna",
"messages": [{"role": "user", "content": "Hello!"}]
}'
```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند، این نسخه را کنار مثال Chat Completions استفاده کنید. `messages` به `input` منتقل می‌شود و متن نهایی از `response.output_text` خوانده می‌شود.

```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Hello!",
    "instructions": "You are a helpful assistant."
  }'
```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### مثال پاسخ

```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-5.6-luna",
  "choices": [
    {
      "message": {
        "role": "assistant",
        "content": "سلام! چطور می‌توانم امروز به شما کمک کنم؟"
      },
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {
    "prompt_tokens": 10,
    "completion_tokens": 8,
    "total_tokens": 18
  }
}
```

## مدیریت خطا

API AvalAI از کدهای پاسخ HTTP متعارف برای نشان دادن موفقیت یا شکست درخواست API استفاده می‌کند. به طور کلی:

- 2xx: موفقیت
- 4xx: خطای کلاینت (به عنوان مثال، درخواست نامعتبر، خطای احراز هویت)
- 5xx: خطای سرور

برای اطلاعات بیشتر در مورد مدیریت خطاها، به راهنمای [مدیریت خطا](fa/guides/error-handling.md) مراجعه کنید.

## محدودیت‌های نرخ

درخواست‌های API مشمول محدودیت نرخ هستند. هنگامی که از محدودیت‌های نرخ خود فراتر می‌روید، پاسخ 429 Too Many Requests دریافت خواهید کرد. برای اطلاعات بیشتر، به راهنمای [محدودیت‌های نرخ](fa/guides/rate-limits.md) مراجعه کنید.

## عیب‌یابی و شناسه‌های درخواست

نمای کلی OpenAI روی request IDها، هدرهای پاسخ و هدرهای rate-limit برای عیب‌یابی production تأکید می‌کند. همین الگو را برای AvalAI به‌کار ببرید:

- وقتی route می‌پذیرد، برای هر تلاش retryپذیر API یک `X-Client-Request-Id` یکتا بفرستید.
- `avalai-request-id` برگشتی، endpoint، model، وضعیت HTTP، تعداد retry، هدرهای rate-limit و `safety_identifier` hashشده خودتان را در صورت وجود log کنید.
- از [`avalai-request-id`](fa/api-reference/response-headers.md#avalai-request-id) برای reconciliation هزینه از طریق [User API](fa/api-reference/user.md) و دادن trace دقیق به پشتیبانی استفاده کنید.
- promptها و فایل‌های خام را در log نگه ندارید مگر اینکه policy نگه‌داری داده شما صراحتا اجازه دهد.

## SDKها و کتابخانه‌های کلاینت

AvalAI با کتابخانه‌های کلاینت OpenAI سازگار است. می‌توانید با مشخص کردن URL پایه AvalAI از این کتابخانه‌ها استفاده کنید:

### پایتون (Python)

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)
```

### جاوااسکریپت/تایپ‌اسکریپت (JavaScript/TypeScript)

```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});
```

### گو (Go)

```go
package main

import (
	"os"

	openai "github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)
	_ = client
}
```

## نسخه‌بندی API

API AvalAI برای اطمینان از سازگاری به عقب در حین تکامل، نسخه‌بندی شده است. نسخه فعلی `v1` است.

تغییرهای سازگار API را عادی در نظر بگیرید: ممکن است endpointهای جدید، پارامترهای اختیاری، فیلدهای پاسخ و نوع eventهای streaming بدون شکستن integrationهای موجود اضافه شوند. فقط فیلدهایی را parse کنید که برنامه شما لازم دارد، propertyهای ناشناخته پاسخ را نادیده بگیرید، و روی ترتیب فیلدهای JSON یا قالب دقیق شناسه‌های opaque فرض شکننده نسازید.

رفتار مدل حتی وقتی schema API پایدار است می‌تواند بین aliasها و snapshotها تغییر کند. برای workflowهای production، جایی که ثبات مهم است model ID را pin کنید، پیش از تغییر alias مدل eval اجرا کنید، و برای promptها، ابزارها و response parsing یادداشت rollback نگه دارید.

## مراحل بعدی

مستندات دقیق برای هر نقطه پایانی API را کاوش کنید:

- [تکمیل گفتگو](fa/api-reference/chat.md)
- [پاسخ‌ها](fa/api-reference/responses.md)
- [تصاویر](fa/api-reference/images.md)
- [بردارهای تعبیه‌سازی](fa/api-reference/embeddings.md)
- [صدا](fa/api-reference/audio.md)
- [نظارت](fa/api-reference/moderation.md)
- [API کاربر](fa/api-reference/user.md) - ردیابی هزینه و تحلیل استفاده
- [هدرهای پاسخ](fa/api-reference/response-headers.md) - درک هدرهای پاسخ API
