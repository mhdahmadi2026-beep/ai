# Responses در مقابل Chat Completions

مقایسه Responses API و Chat Completions API.

این راهنما تفاوت‌های کلیدی بین [Responses API](fa/api-reference/responses.md) و [Chat Completions API](fa/api-reference/chat.md) را توضیح می‌دهد و به شما کمک می‌کند رویکرد مناسب را برای برنامه خود انتخاب کنید.

> این راهنما با اقتباس از مستندات رسمی OpenAI درباره [مهاجرت به Responses API](https://developers.openai.com/api/docs/guides/migrate-to-responses)، [فراخوانی تابع](https://developers.openai.com/api/docs/guides/function-calling) و [Structured Outputs](https://developers.openai.com/api/docs/guides/structured-outputs)، با تغییرات endpoint، کلید API و نکات availability در routeهای AvalAI تهیه شده است.

## چرا Responses API؟

Responses API جدیدترین API اصلی و یک API اولیه عامل (agentic) است که سادگی Chat Completions را با توانایی انجام وظایف عامل‌محور بیشتر ترکیب می‌کند. با تکامل قابلیت‌های مدل، Responses API یک پایه انعطاف‌پذیر برای ساخت برنامه‌های کاربردی اقدام‌محور فراهم می‌کند، از جمله ابزارهای داخلی که به route و مدل وابسته‌اند:

* [جستجوی وب](fa/guides/tools-web-search.md)
* [جستجوی فایل](fa/guides/tools-file-search.md)
* [استفاده از کامپیوتر](fa/guides/tools-computer-use.md)
* code interpreter، image generation، Remote MCP و حلقه‌های function سفارشی، هرجا route انتخابی AvalAI از آن‌ها پشتیبانی کند

OpenAI همچنین Responses را پایه مناسب‌تری برای گردش‌کارهای reasoning، loopهای ابزار تایپ‌شده، stateful context با `previous_response_id`، ورودی منعطف با `input` و `instructions` سطح بالا، و قابلیت‌های مدل‌های آینده معرفی می‌کند. در AvalAI این مزیت‌ها را وابسته به route و مدل بدانید: برای flowهای جدید متنی، reasoning و ابزارمحور به سبک OpenAI، وقتی مدل انتخابی از `/v1/responses` پشتیبانی می‌کند با Responses شروع کنید؛ Chat Completions را برای ادغام‌های پایدار موجود یا providerهایی که فقط chat compatibility دارند نگه دارید.

## مقایسه قابلیت‌ها

| قابلیت | Chat Completions API | Responses API |
|------------|---------------------|--------------|
| تولید متن | ✓ | ✓ |
| صوتی | ✓ | وابسته به route/مدل؛ در صورت دسترسی از `/v1/audio` یا routeهای Realtime استفاده کنید |
| بینایی | ✓ | ✓ |
| خروجی‌های ساختاریافته | ✓ | ✓ |
| فراخوانی تابع | ✓ | ✓ |
| جستجوی وب | | وابسته به route/مدل |
| جستجوی فایل | | وابسته به route/مدل |
| استفاده از کامپیوتر | | وابسته به route/مدل |
| مفسر کد | | برنامه‌ریزی‌شده / وابسته به route |
| Remote MCP / connectorها | | وابسته به route/مدل/حساب |
| تولید تصویر به‌عنوان ابزار | | وابسته به route/مدل؛ در غیر این صورت از `/v1/images` استفاده کنید |
| خلاصه‌های reasoning | | وابسته به route/مدل |

AvalAI شکل درخواست سازگار با OpenAI را حفظ می‌کند، اما ابزارهای hosted در همه ارائه‌دهنده‌ها عمومی نیستند. پیش از انتشار migration، مدل و route انتخابی را در صفحه ارائه‌دهنده یا مرجع API مربوط بررسی کنید. برای بازیابی وب مستقل از ارائه‌دهنده، از AvalAI [`/v1/search`](fa/api-reference/search.md) استفاده کنید مگر اینکه route انتخابی Responses صریحا از `web_search` پشتیبانی کند.

## Chat Completions API از بین نمی‌رود

Chat Completions API یک استاندارد صنعتی برای ساخت برنامه‌های هوش مصنوعی است و برای ادغام‌های موجود همچنان پشتیبانی می‌شود. Responses API برای پروژه‌های جدید به سبک OpenAI توصیه می‌شود، چون گردش‌کارهای استفاده از ابزار، اجرای کد، مدیریت وضعیت و قابلیت‌های مدل‌های آینده را ساده‌تر می‌کند.

## یک API حالت‌مند و رویدادهای معنایی

رویدادها با Responses API ساده‌تر هستند. این API دارای معماری قابل پیش‌بینی و رویداد‌محور است، در حالی که Chat Completions API به طور مداوم به فیلد محتوا اضافه می‌کند همچنان که توکن‌ها تولید می‌شوند—که نیاز به پیگیری دستی تفاوت‌ها بین هر وضعیت دارد. منطق مکالمه چند مرحله‌ای و استدلال با Responses API آسان‌تر قابل پیاده‌سازی است.

Responses API به وضوح رویدادهای معنایی را منتشر می‌کند که دقیقا آنچه تغییر کرده است (مانند افزودن متن خاص) را مشخص می‌کند، بنابراین می‌توانید ادغام‌هایی را بنویسید که هدف آنها رویدادهای خاص منتشر شده (مانند تغییرات متن) باشد، که ادغام را ساده‌تر می‌کند و ایمنی نوع را بهبود می‌بخشد.

## دسترسی به مدل در هر API

هر زمان که امکان‌پذیر باشد، تمام مدل‌های جدید به هر دو API Chat Completions و Responses اضافه خواهند شد. برخی مدل‌ها ممکن است فقط از طریق Responses API در دسترس باشند اگر از ابزارهای داخلی استفاده کنند (مانند مدل‌های استفاده از کامپیوتر)، یا چندین نوبت تولید مدل را در پس زمینه فعال کنند (مانند o1-pro). صفحات جزئیات هر [مدل](fa/models/model-details.md) نشان خواهد داد که آیا از Chat Completions، Responses یا هر دو پشتیبانی می‌کنند.

## مسیر مهاجرت

مهاجرت را برای هر ادغام به صورت مرحله‌ای انجام دهید:

1. endpoint را از `POST /v1/chat/completions` به `POST /v1/responses` تغییر دهید.
2. `messages` ساده را به `input` منتقل کنید؛ راهنمایی پایدار system یا developer را در `instructions` سطح بالا قرار دهید.
3. متن نهایی را از `response.output_text` بخوانید، نه از `choices[0].message.content`.
4. برای استدلال، ابزارها، فایل‌ها، تصویر یا خروجی چندوجهی، روی `response.output` پیمایش کنید و بر اساس `type` هر آیتم تصمیم بگیرید.
5. برای گردش‌کارهای چندمرحله‌ای، بین `previous_response_id` برای وضعیت مدیریت‌شده توسط API یا ارسال دوباره آیتم‌های خروجی قبلی برای کنترل stateless انتخاب کنید.
6. مصرف‌کننده‌های streaming را برای رویدادهای تایپ‌شده Responses به‌روزرسانی کنید، نه chunkهای `delta` در Chat Completions.
7. schemaهای خروجی ساختاریافته را از `response_format` به `text.format` منتقل کنید.
8. اگر function calling را مهاجرت می‌دهید، نتیجه ابزار را به صورت آیتم‌های `function_call_output` با `call_id` متناظر برگردانید.
9. schemaهای تابع را برای Responses به‌روزرسانی کنید: ابزارها internally tagged هستند و schemaهای سازگار ممکن است به strict mode normalize شوند مگر اینکه `strict: false` بگذارید.
10. تصمیم بگیرید وضعیت ذخیره‌شده را نگه می‌دارید (`store: true`) یا نگهداری را صریحا با `store: false` غیرفعال می‌کنید.

### نقشه فیلدهای مهاجرت

هنگام به‌روزرسانی request builderها، wrapperهای SDK و parserهای stream از این نقشه استفاده کنید:

| فیلد یا رفتار در Chat Completions | معادل در Responses | نکته مهاجرت در AvalAI |
| --- | --- | --- |
| `messages` | `input` به‌صورت رشته یا آرایه‌ای از Itemهای ورودی | transcriptهای ساده اغلب مستقیم منتقل می‌شوند؛ راهنمایی پایدار system/developer را وقتی باید روی همه turnها اعمال شود به `instructions` جدا کنید. |
| `choices[0].message.content` | `response.output_text` یا `response.output` | برای متن ساده از `output_text` استفاده کنید؛ برای ابزارها، reasoning، تصویر یا خروجی چندوجهی Itemهای تایپ‌شده `output` را بررسی کنید. |
| `choices[].message.tool_calls` | Itemهای `response.output` با `type: "function_call"` | نتیجه ابزار را به‌صورت Itemهای `function_call_output` با همان `call_id` برگردانید. |
| `response_format` | `text.format` | در صورت پشتیبانی JSON Schema سخت‌گیرانه را ترجیح دهید؛ fallback با JSON mode را فقط وقتی نگه دارید که پایبندی به schema در دسترس نیست. |
| `reasoning_effort` | `reasoning.effort` | فقط روی مدل/routeهایی استفاده کنید که کنترل reasoning را ارائه می‌کنند؛ رفتار را برای هر provider جدا verify کنید. |
| `n` برای چند انتخاب | پشتیبانی نمی‌شود | اگر چند candidate می‌خواهید چند درخواست Responses جدا بفرستید و هزینه هرکدام را حساب کنید. |
| chunkهای stream مانند `choices[].delta` | رویدادهای SSE تایپ‌شده مثل `response.created`، `response.output_text.delta`، `response.completed`، `error` و رویدادهای آرگومان function call | قبل از تغییر endpoint، مصرف‌کننده stream را بازنویسی کنید؛ بر اساس `event.type` شاخه‌بندی کنید و رویدادهای غیرمتنی را به بافر متن UI اضافه نکنید. |
| `user` | `safety_identifier` و/یا `prompt_cache_key` | شناسه‌های opaque و حفظ‌کننده حریم خصوصی را ترجیح دهید؛ PII خام یا request ID را به‌عنوان cache key نفرستید. |

### چک‌لیست rollout تدریجی

- با یک مسیر ساده تولید متن شروع کنید و بعد سراغ مسیرهای tool-heavy بروید.
- قبل از هدایت ترافیک production، رفتار، latency، مصرف token و خطاها را مقایسه کنید.
- Chat Completions را برای ادغام‌های پایدار موجود فعال نگه دارید و هر flow را جداگانه مهاجرت دهید.
- برای گردش‌کارهای حساس به compliance یا stateless، فرض نکنید `previous_response_id` همیشه مجاز است؛ آیتم‌های خروجی موردنیاز را صریحا دوباره ارسال کنید.
- به خاطر داشته باشید `previous_response_id` مدیریت context را ساده می‌کند، اما context قبلی در درخواست‌های زنجیره‌ای همچنان می‌تواند در مصرف ورودی حساب شود.

هر flow مهاجرت‌شده را پیش از افزایش ترافیک اندازه‌گیری کنید:

| معیار | چه چیزی را مقایسه کنید |
| --- | --- |
| کیفیت خروجی | promptهای طلایی، نرخ موفقیت reasoning/tool، اعتبار Structured Output و رفتار refusal. |
| latency | زمان تا اولین token در stream، latency کامل پاسخ، زمان تکمیل job پس‌زمینه و tail latency هر provider. |
| هزینه | tokenهای ورودی/خروجی، tokenهای reasoning، نرخ hit در prompt cache در صورت نمایش و هزینه‌های اضافه tool call. |
| قابلیت اتکا | کدهای خطا، رفتار retry، پاسخ‌های incomplete، قطع stream و idempotency فراخوانی ابزار. |
| compliance | اینکه flow از `store: true`، `previous_response_id`، encrypted reasoning، replay دستی Itemها یا ذخیره‌سازی سمت برنامه استفاده می‌کند. |

### Statefulness، ذخیره‌سازی و compliance

راهنمای migration OpenAI سه الگوی state را برجسته می‌کند که حفظ آن‌ها در ادغام‌های AvalAI مفید است:

- **State مدیریت‌شده توسط API:** وقتی route انتخابی AvalAI state پاسخ‌های قبلی را ذخیره می‌کند و policy شما اجازه continuity سمت سرور را می‌دهد، از `previous_response_id` استفاده کنید. `instructions` پایدار را در هر درخواست دوباره ارسال کنید و فرض نکنید پاسخ قبلی آن‌ها را منتقل می‌کند.
- **State مدیریت‌شده توسط برنامه:** وقتی عملیات stateless، replay قطعی یا کنترل سخت‌گیرانه‌تر retention می‌خواهید، `store: false` بگذارید و آیتم‌های input/output قبلی لازم را خودتان دوباره ارسال کنید.
- **تداوم reasoning:** اگر route از آیتم‌های encrypted reasoning پشتیبانی می‌کند، آن‌ها را با `include: ["reasoning.encrypted_content"]` درخواست کنید و در turnهای بعدی برگردانید. اگر پشتیبانی نمی‌کند، آیتم‌های عادی `reasoning`، `function_call` و `function_call_output` را حفظ کنید یا از `previous_response_id` استفاده کنید.

`previous_response_id` را میان‌بری برای کاهش هزینه در نظر نگیرید: context قبلی در زنجیره پاسخ همچنان می‌تواند به عنوان input token محاسبه شود. برای بارهای کاری regulated، حالت state انتخابی را مستند کنید و پیش از فعال‌سازی در production آن را با نیازهای data-retention خود تطبیق دهید.

### ابزارهای Native در برابر Functionهای سفارشی

وقتی یک مسیر Chat Completions پر از ابزار را مهاجرت می‌دهید، ابتدا تصمیم بگیرید هر ابزار باید به قابلیت native در Responses تبدیل شود یا به صورت function سفارشیِ مدیریت‌شده توسط اپلیکیشن باقی بماند.

- برای بازیابی وب مستقل از ارائه‌دهنده از AvalAI `/v1/search` استفاده کنید؛ `web_search` در Responses را فقط وقتی به کار ببرید که route و مدل انتخاب‌شده صریحا از آن پشتیبانی کنند.
- برای پایگاه‌داده‌های داخلی، CRM، سیستم‌های billing، APIهای خصوصی، عملیات نوشتنی و هر side effect که باید توسط سرور شما authorize شود، functionهای سفارشی را نگه دارید. همیشه argumentها را سمت سرور validate کنید و قبل از اجرای action، retryها را idempotent طراحی کنید.
- ابزارهای hosted مانند file search، code interpreter، computer use، image generation، Remote MCP و connectorها را در AvalAI وابسته به route، مدل و حساب در نظر بگیرید. یک مسیر fallback از طریق لایه retrieval خودتان، sandbox، endpoint تصویر، workflow فایل یا MCP proxy مدیریت‌شده توسط اپلیکیشن نگه دارید.
- در مهاجرت‌های tool-heavy همراه با reasoning، هنگام حمل دستی context آیتم‌های خروجی typed را حذف نکنید. آیتم‌های `reasoning`، `function_call` و `function_call_output` را حفظ کنید، اگر پاسخ `phase` داشت آن را هم نگه دارید، یا وقتی وضعیت ذخیره‌شده مجاز است از `previous_response_id` استفاده کنید.
- بیشتر دستورالعمل‌های مخصوص ابزار را در description همان ابزار بنویسید: ابزار چه کاری می‌کند، چه زمانی استفاده شود، inputهای لازم چیست، چه side effectهایی دارد، retry آن چقدر امن است و خطاهای رایج چیست. دستورهای system یا developer را برای policyهای سراسری نگه دارید که روی همه ابزارها اعمال می‌شوند.

## مقایسه کد

مثال‌های زیر نحوه انجام یک فراخوانی API اساسی به [Chat Completions API](fa/api-reference/chat.md) و [Responses API](fa/api-reference/responses.md) را نشان می‌دهد.

### مثال تولید متن

هر دو API تولید خروجی از مدل‌ها را آسان می‌کنند. یک تکمیل به آرایه `messages` نیاز دارد، اما یک پاسخ به `input` (رشته یا آرایه، همانطور که در زیر نشان داده شده است) نیاز دارد.

```language-selector
python=:# Chat Completions API
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

completion = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {"role": "user", "content": "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."}
    ],
)

print(completion.choices[0].message.content)

# Responses API
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input=[
        {"role": "user", "content": "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."}
    ],
)

print(response.output_text)

javascript=:// Chat Completions API
import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const completion = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    {
      role: "user",
      content: "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.",
    },
  ],
});

console.log(completion.choices[0].message.content);

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: [
    {
      role: "user",
      content: "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.",
    },
  ],
});

console.log(response.output_text);

bash=:# Chat Completions API
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "gpt-5.6-luna",
 "messages": [
 {
 "role": "user",
 "content": "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."
 }
 ]
 }'

# Responses API
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
 "model": "gpt-5.6-luna",
 "input": [
 {
 "role": "user",
 "content": "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."
 }
 ]
 }'

go=:// Chat Completions API
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
	"github.com/openai/openai-go/v3/responses"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)

	// Chat Completions API
	completion, err := client.Chat.Completions.New(
		context.Background(),
		openai.ChatCompletionNewParams{
			Model: openai.F(openai.ChatModel("gpt-5.6-luna")),
			Messages: openai.F([]openai.ChatCompletionMessageParamUnion{
				openai.UserMessage("یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."),
			}),
		},
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(completion.Choices[0].Message.Content)

	// Responses API
	response, err := client.Responses.New(
		context.Background(),
		openai.ResponseNewParams{
			model: "gpt-5.6-luna",
			Input: responses.ResponseNewParamsInputUnion{
				OfString: openai.String("یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس."),
			},
		},
	)
	if err != nil {
		panic(err)
	}
	fmt.Println(response.OutputText())
}

php=:<?php
// Chat Completions API
require 'vendor/autoload.php';

$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$result = $client->chat()->create([
 'model' => 'gpt-5.6-luna',
 'messages' => [
 ['role' => 'user', 'content' => 'یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.'],
 ],
]);

echo $result->choices[0]->message->content;

// Responses API
$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('https://api.avalai.ir/v1')
    ->make();

$result = $client->responses()->create([
 'model' => 'gpt-5.6-luna',
 'input' => [
 ['role' => 'user', 'content' => 'یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.'],
 ],
]);

echo $result->output_text;
?>

```

<!-- responses-equivalent:start -->
<details>
<summary>نسخه معادل Responses API</summary>

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
    instructions="You are a helpful assistant.",
    input="یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک داستان خواب یک جمله‌ای درباره یک تک‌شاخ بنویس.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


وقتی پاسخی از Responses API دریافت می‌کنید، فیلدها کمی متفاوت هستند. به جای `message`، یک شی `response` تایپ شده با `id` خاص خود دریافت می‌کنید. پاسخ‌ها به طور پیش‌فرض ذخیره می‌شوند. تکمیل‌های چت برای حساب‌های جدید به طور پیش‌فرض ذخیره می‌شوند. برای غیرفعال کردن ذخیره‌سازی هنگام استفاده از هر یک از API‌ها، `store: false` را تنظیم کنید.

**پاسخ Chat Completions API:**
```json
[
  {
    "index": 0,
    "message": {
      "role": "assistant",
      "content": "زیر نور ملایم ماه، لونا تک‌شاخ در میان مزارع پر از گرد و غبار ستاره‌ای می‌رقصید و برای هر کودک خوابیده، رد پایی از رویاها به جا می‌گذاشت.",
      "refusal": null
    },
    "logprobs": null,
    "finish_reason": "stop"
  }
]
```

**پاسخ Responses API:**
```json
[
  {
    "id": "msg_67b73f697ba4819183a15cc17d011509",
    "type": "message",
    "role": "assistant",
    "content": [
      {
        "type": "output_text",
        "text": "زیر نور ملایم ماه، لونا تک‌شاخ در میان مزارع پر از گرد و غبار ستاره‌ای می‌رقصید و برای هر کودک خوابیده، رد پایی از رویاها به جا می‌گذاشت.",
        "annotations": []
      }
    ]
  }
]
```

## تفاوت‌های کلیدی

* Responses API مقدار `output` را برمی‌گرداند، در حالی که Chat Completions API آرایه `choices` را برمی‌گرداند.
* Responses در هر درخواست یک candidate تولید می‌کند؛ Chat Completions با `n` از چند choice پشتیبانی می‌کند. اگر چند candidate می‌خواهید، چند درخواست Responses جداگانه بفرستید.
* شکل API خروجی‌های ساختاریافته متفاوت است. به جای `response_format`، از `text.format` در Responses استفاده کنید. اطلاعات بیشتر را در راهنمای [خروجی‌های ساختاریافته](structured-outputs.md) بیاموزید.
* شکل API فراخوانی تابع متفاوت است—هم برای پیکربندی تابع در درخواست و هم برای فراخوانی‌های تابع ارسال شده در پاسخ. تفاوت کامل را در [راهنمای فراخوانی تابع](function-calling.md) مشاهده کنید.
* استدلال متفاوت است. به جای `reasoning_effort` در Chat Completions، از `reasoning.effort` با Responses API استفاده کنید. جزئیات بیشتر را در راهنمای [استدلال](reasoning.md) بخوانید.
* SDK پاسخ‌ها دارای یک کمک‌کننده `output_text` است که SDK تکمیل‌های چت ندارد.
* وضعیت مکالمه: شما باید وضعیت مکالمه را در Chat Completions خودتان مدیریت کنید، در حالی که Responses دارای `previous_response_id` است که به شما در مکالمات طولانی کمک می‌کند.
* پاسخ‌ها به طور پیش‌فرض ذخیره می‌شوند. تکمیل‌های چت برای حساب‌های جدید به طور پیش‌فرض ذخیره می‌شوند. برای غیرفعال کردن ذخیره‌سازی، `store: false` را تنظیم کنید.
* Streaming رویدادمحور است. به جای خواندن فقط chunkهای `delta`، رویدادهای تایپ‌شده‌ای مثل `response.created`، `response.output_text.delta`، `response.completed`، `error`، `response.function_call_arguments.delta` و `response.function_call_arguments.done` را مدیریت کنید.
* گردش‌کارهای ابزار و reasoning مبتنی بر item هستند. وقتی context را دستی جلو می‌برید، آیتم‌های `reasoning`، `function_call` و `function_call_output` را حفظ کنید.

## خطاهای رایج هنگام مهاجرت

هنگام انتقال کد production از Chat Completions به Responses مراقب این موارد باشید:

* خواندن `choices[0].message.content` به جای `response.output_text` یا `response.output`.
* فرض اینکه همه آیتم‌های `response.output` پیام هستند؛ reasoning، فراخوانی ابزار و function call نوع‌های آیتم جداگانه دارند.
* حذف آیتم‌های `reasoning`، `function_call` یا `function_call_output` هنگام replay دستی context.
* برگرداندن نتیجه تابع بدون `call_id` متناظر.
* فرض اینکه schemaهای تابع Chat Completions پس از انتقال به Responses همچنان non-strict می‌مانند؛ `strict`، `required` و `additionalProperties` را بررسی کنید.
* ارسال `response_format` به `/v1/responses` به جای `text.format`.
* استفاده دوباره از handlerهای streaming مربوط به Chat Completions بدون شاخه‌بندی بر اساس رویدادهای تایپ‌شده Responses.
* فرض اینکه `previous_response_id` هزینه ورودی context قبلی را حذف می‌کند؛ context زنجیره‌ای همچنان می‌تواند به عنوان input حساب شود.

## این برای API‌های موجود به چه معناست

### Chat Completions

Chat Completions API همچنان پرکاربردترین API است. پشتیبانی از آن با مدل‌ها و قابلیت‌های جدید ادامه خواهد یافت. اگر برای برنامه خود به ابزارهای داخلی نیاز ندارید، می‌توانید با اطمینان به استفاده از Chat Completions ادامه دهید.

مدل‌های جدید همچنان به Chat Completions منتشر خواهند شد هر زمان که قابلیت‌های آنها به ابزارهای داخلی یا چندین فراخوانی مدل وابسته نباشد. وقتی برای قابلیت‌های پیشرفته طراحی شده مخصوصا برای گردش‌کارهای عامل آماده هستید، Responses API توصیه می‌شود.

## Assistants

بر اساس بازخورد توسعه‌دهندگان از نسخه بتای Assistants API، بهبودهای کلیدی در Responses API گنجانده شده است تا آن را انعطاف پذیرتر، سریع‌تر و استفاده از آن آسان‌تر شود. Responses API نشان‌دهنده مسیر آینده برای ساخت عامل‌ها در AvalAI است.

OpenAI اعلام کرده است که Assistants API از **۲۶ اوت ۲۰۲۵** منسوخ شده و تاریخ پایان آن **۲۶ اوت ۲۰۲۶** است. در مستندات AvalAI، مثال‌های agentic جدید را Responses-first بنویسید و ارجاع‌های Assistants را فقط برای ادغام‌های موجود یا نکته‌های migration نگه دارید.

هنگام مهاجرت برنامه‌های شبیه Assistants، assistants/threads/runs را به state در Responses، ابزارها، `previous_response_id` و storage مدیریت‌شده در برنامه خودتان نگاشت کنید. قبل از فرض کردن برابری کامل ابزارهای hosted OpenAI، بررسی کنید route انتخابی AvalAI کدام ابزارها را پشتیبانی می‌کند.

## منابع مرتبط

- [فراخوانی تابع](fa/guides/function-calling.md)
- [Realtime و صوت زنده](fa/guides/realtime-audio.md)
- [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)
- [ابزارها](fa/guides/tools.md)
- [استدلال](fa/guides/reasoning.md)
