# مرجع API پاسخ‌ها

پیشرفته‌ترین رابط OpenAI برای تولید پاسخ‌های مدل. از ورودی‌های متنی و تصویری و خروجی‌های متنی پشتیبانی می‌کند. تعاملات حالت‌دار با مدل ایجاد کنید، با استفاده از خروجی پاسخ‌های قبلی به عنوان ورودی. قابلیت‌های مدل را با ابزارهای داخلی برای جستجوی فایل، جستجوی وب، استفاده از کامپیوتر و موارد دیگر گسترش دهید. با استفاده از فراخوانی تابع، به مدل اجازه دسترسی به سیستم‌ها و داده‌های خارجی را بدهید.

راهنماهای مرتبط:

- [شروع سریع](fa/quickstart.md?api-mode=responses)
- [ورودی‌ها و خروجی‌های متنی](fa/guides/text-generation.md?api-mode=responses)
- [ورودی‌های تصویری](fa/guides/vision.md?api-mode=responses)
- [خروجی‌های ساختاریافته](fa/guides/structured-outputs.md?api-mode=responses)
- [فراخوانی تابع](fa/guides/function-calling.md?api-mode=responses)
- [وضعیت مکالمه](fa/guides/conversation-state.md?api-mode=responses)
- [پردازش پس‌زمینه](fa/guides/background-processing.md?api-mode=responses)
- [کنترل داده‌ها](fa/guides/data-controls.md?api-mode=responses)
- [پاسخ‌های جریانی](fa/guides/streaming-responses.md?api-mode=responses)
- [گسترش مدل‌ها با ابزارها](fa/guides/tools.md?api-mode=responses)
- [MCP و connectorها](fa/guides/tools-connectors-mcp.md?api-mode=responses)

مثال‌های مرتبط:

- [گردش‌کارهای Stateful با Responses API](fa/examples/responses_stateful_workflows.md)
- [مدل‌های Reasoning با Function Calling](fa/examples/reasoning_function_calls.md)
- [گاردریل‌های عامل‌محور برای گردش‌کار Schema](fa/examples/agentic_guardrails_schema_workflow.md)

## چه زمانی از Responses استفاده کنیم

برای workflowهای جدید reasoning، tool calling، چندوجهی، structured output و چندنوبتی ابتدا از `/v1/responses` استفاده کنید. `/v1/chat/completions` همچنان برای integrationهای موجود، سازگاری frameworkها و مدل‌هایی که در AvalAI فقط chat-only هستند مفید است.

هنگام مهاجرت از Chat Completions:

- `messages` را به‌صورت `input` بفرستید، یا guidance ثابت سیستم را در `instructions` سطح بالا جدا کنید؛
- متن نهایی را از `response.output_text` بخوانید، و وقتی ابزار، reasoning یا خروجی چندوجهی دارید `response.output` را بررسی کنید؛
- برای chainهای stateful ساده از `previous_response_id` همراه با `store: true` استفاده کنید، یا برای flowهای stateless آیتم‌های `output` قبلی را دستی replay کنید؛
- اگر چند خروجی candidate لازم دارید، درخواست‌های جدا بسازید چون Responses پارامتر `n` مربوط به Chat Completions را پشتیبانی نمی‌کند؛
- schemaهای Structured Outputs را از `response_format` به `text.format` منتقل کنید؛
- consumerهای streaming را برای رویدادهای SSE نوع‌دار مثل `response.created`، `response.output_text.delta`، `response.function_call_arguments.delta`، `response.function_call_arguments.done` و `response.completed` به‌روزرسانی کنید.

## ایجاد پاسخ مدل

```
POST https://api.avalai.ir/v1/responses
```

یک پاسخ مدل ایجاد می‌کند. ورودی‌های [متنی](fa/guides/text-generation.md) یا [تصویری](fa/guides/vision.md) را برای تولید خروجی‌های [متنی](fa/guides/text-generation.md) یا [JSON](fa/guides/structured-outputs.md) ارائه دهید. مدل را وادار کنید تا [کد سفارشی](fa/guides/function-calling.md) شما را فراخوانی کند یا از [ابزارهای](fa/guides/tools.md) داخلی مانند [جستجوی وب](fa/guides/tools-web-search.md) یا [جستجوی فایل](fa/guides/tools-file-search.md) برای استفاده از داده‌های خودتان به عنوان ورودی برای پاسخ مدل استفاده کند.

### بدنه درخواست (Request Body)

| پارامتر                | نوع              | الزامی  | پیش‌فرض  | توضیحات                                                                                                                                                                                                                                                                                                                                                                                                       |
| ---------------------- | ---------------- | ------- | -------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `input`                | رشته یا آرایه    | الزامی  |          | ورودی‌های متنی، تصویری یا فایلی به مدل، که برای تولید پاسخ استفاده می‌شوند. ورودی فایل از `input_file` استفاده می‌کند و می‌تواند به `file_url`، `file_id` یا `file_data` کدگذاری‌شده Base64 ارجاع دهد. <br> بیشتر بدانید: <ul><li>[ورودی‌ها و خروجی‌های متنی](fa/guides/text-generation.md)</li><li>[ورودی‌های تصویری](fa/guides/vision.md)</li><li>[ورودی‌های فایل](fa/guides/pdf-files.md)</li><li>[وضعیت مکالمه](fa/guides/conversation-state.md)</li><li>[فراخوانی تابع](fa/guides/function-calling.md)</li></ul>                    |
| `model`                | رشته             | الزامی  |          | شناسه مدلی که برای تولید پاسخ استفاده می‌شود، مانند `gpt-5.5`، `gpt-5.4-pro` یا `gpt-5.4`. برخی مدل‌های غیر OpenAI با مجموعه‌ای محدود از ویژگی‌ها پشتیبانی می‌شوند (فقط ورودی/خروجی متنی و استفاده از ابزار پایه — ابزارهای داخلی پیشرفته و فیلد `reasoning` همچنان مختص OpenAI باقی می‌مانند). مدل‌های دارای پشتیبانی **جزئی** در Responses API شامل `qwen3.7-max` از Alibaba، `claude-sonnet-5` و `claude-opus-4-8` از Anthropic و `minimax-m3` از MiniMax می‌شوند. برای مرور و مقایسه مدل‌های موجود به [راهنمای مدل‌ها](fa/models/model-details.md) مراجعه کنید. |
| `background`           | بولی یا null     | اختیاری | false    | پاسخ را، وقتی route/account انتخابی از پردازش پس‌زمینه پشتیبانی می‌کند، به صورت background job اجرا می‌کند. برای polling، وضعیت‌های نهایی و handoff با webhook، [پردازش پس‌زمینه](fa/guides/background-processing.md) را ببینید. |
| `context_management`   | شی یا null       | اختیاری |          | کنترل‌های وابسته به route برای context، مانند compaction سمت سرور. اگر در دسترس نیست، context را در برنامه خودتان فشرده کنید و خلاصه را صریحا بفرستید. |
| `conversation`         | رشته یا شی       | اختیاری |          | شی یا شناسه مکالمه‌ای که آیتم‌های آن به درخواست اضافه می‌شوند و پس از تکمیل پاسخ به‌روزرسانی می‌شوند. آن را با `previous_response_id` ترکیب نکنید؛ فقط وقتی route AvalAI صریحا مکالمه پایدار را پشتیبانی می‌کند از آن استفاده کنید. |
| `include`              | آرایه یا null    | اختیاری |          | داده‌های خروجی اضافی را برای گنجاندن در پاسخ مشخص می‌کند. مقدارهای رایج سازگار با OpenAI شامل این موارد هستند: <ul><li>`file_search_call.results`: نتایج file search.</li><li>`web_search_call.action.sources`: منابع web search.</li><li>`code_interpreter_call.outputs`: خروجی‌های code interpreter.</li><li>`computer_call_output.output.image_url`: URL تصویر خروجی computer.</li><li>`message.input_image.image_url`: URLهای تصویر ورودی.</li><li>`message.output_text.logprobs`: logprobهای توکن‌های خروجی.</li><li>`reasoning.encrypted_content`: آیتم‌های reasoning رمزنگاری‌شده برای ادامه stateless.</li></ul> در AvalAI دسترسی به این مقدارها به مدل، route و حساب وابسته است. |
| `instructions`         | رشته یا null     | اختیاری |          | یک پیام سیستمی (یا توسعه‌دهنده) را به عنوان اولین آیتم در زمینه مدل درج می‌کند. هنگام استفاده همراه با `previous_response_id`، دستورالعمل‌های پاسخ قبلی به پاسخ بعدی منتقل نمی‌شوند.                                                                                                                                                                                                                          |
| `max_output_tokens`    | عدد صحیح یا null | اختیاری |          | سقف مشترک برای خروجی قابل مشاهده و [توکن‌های reasoning](fa/guides/reasoning.md#تخصیص-فضا-برای-استدلال). اگر reasoning پنهان تمام بودجه را مصرف کند، پاسخ ممکن است با وضعیت `incomplete` و `incomplete_details.reason: "max_output_tokens"` بدون متن قابل مشاهده برگردد. حاشیه امن بگذارید، effort را کاهش دهید یا سقف را تا حداکثر مدل افزایش دهید. |
| `max_tool_calls`       | عدد صحیح یا null | اختیاری |          | حداکثر تعداد کل فراخوانی‌های ابزار داخلی در یک پاسخ. این حد روی مجموع ابزارهای داخلی اعمال می‌شود، نه جداگانه برای هر ابزار. |
| `metadata`             | نقشه             | اختیاری |          | مجموعه‌ای از 16 جفت کلید-مقدار که می‌توان به یک شی پیوست کرد. برای ذخیره اطلاعات اضافی مفید است. حداکثر طول کلیدها 64 کاراکتر، حداکثر طول مقادیر 512 کاراکتر.                                                                                                                                                                                                                                                |
| `parallel_tool_calls`  | بولی یا null     | اختیاری | true     | آیا به مدل اجازه داده شود فراخوانی‌های ابزار را به صورت موازی اجرا کند.                                                                                                                                                                                                                                                                                                                                       |
| `previous_response_id` | رشته یا null     | اختیاری |          | شناسه منحصر به فرد پاسخ قبلی به مدل. از این برای ایجاد مکالمات چند نوبتی استفاده کنید. درباره [وضعیت مکالمه](fa/guides/conversation-state.md) بیشتر بدانید.                                                                                                                                                                                                                                                   |
| `prompt`               | شی یا null       | اختیاری |          | ارجاع به template پرامپت و متغیرهای آن، وقتی پشتیبانی prompt-template برای route/account انتخابی فعال باشد. در غیر این صورت پرامپت‌های قابل استفاده مجدد را در برنامه خود نگه دارید و `instructions`/`input` بفرستید. |
| `reasoning`            | شی یا null      | اختیاری |          | گزینه‌های پیکربندی برای مدل‌های reasoning پشتیبانی‌شده OpenAI، شامل مدل‌های سری GPT-5 و سری o. برای تنظیم کیفیت، latency و هزینه از `reasoning.effort` استفاده کنید؛ دسترسی به مدل و route وابسته است. [استدلال](fa/guides/reasoning.md) را ببینید.                                                                                                                                                          |
| `store`                | بولی یا null     | اختیاری | true     | آیا پاسخ مدل تولید شده برای بازیابی بعدی از طریق API ذخیره شود.                                                                                                                                                                                                                                                                                                                                               |
| `stream`               | بولی یا null     | اختیاری | false    | اگر روی true تنظیم شود، داده‌های پاسخ مدل با استفاده از [رویدادهای ارسال شده توسط سرور](https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events/Using_server-sent_events#Event_stream_format) پخش جریانی می‌شوند. بخش [پخش جریانی (Streaming)](fa/api-reference/responses?id=streaming) را ببینید.                                                                                                |
| `stream_options`       | شی یا null       | اختیاری |          | گزینه‌های مربوط به پاسخ‌های جریانی. فقط همراه با `stream: true` بفرستید؛ گزینه‌های وابسته به route می‌توانند شامل کنترل‌های obfuscation برای لینک‌های داخلی قابل اعتماد باشند. |
| `temperature`          | عدد یا null      | اختیاری | 1        | دمای نمونه‌برداری (0-2). مقادیر بالاتر = تصادفی‌تر، پایین‌تر = قطعی‌تر. این یا `top_p` را تغییر دهید.                                                                                                                                                                                                                                                                                                         |
| `text`                 | شی              | اختیاری |          | گزینه‌های پیکربندی برای پاسخ متنی. از `text.format` برای متن ساده، JSON mode یا Structured Outputs استفاده کنید و وقتی پشتیبانی شود با `text.verbosity` طول پاسخ نهایی را جدا از عمق reasoning کنترل کنید. بیشتر بدانید: <ul><li>[ورودی‌ها و خروجی‌های متنی](fa/guides/text-generation.md)</li><li>[خروجی‌های ساختاریافته](fa/guides/structured-outputs.md)</li><li>[مهندسی پرامپت](fa/guides/prompt-engineering.md)</li></ul> |
| `tool_choice`          | رشته یا شی      | اختیاری |          | نحوه انتخاب ابزار(ها) توسط مدل. پارامتر `tools` را ببینید.                                                                                                                                                                                                                                                                                                                                                    |
| `tools`                | آرایه            | اختیاری |          | آرایه‌ای از ابزارهایی که مدل ممکن است فراخوانی کند. دسته‌بندی‌ها شامل این موارد است: <ul><li>**ابزارهای داخلی**: قابلیت‌های میزبانی‌شده OpenAI مانند [جستجوی وب](fa/guides/tools-web-search.md) و [جستجوی فایل](fa/guides/tools-file-search.md)، وقتی برای route/account انتخابی AvalAI فعال باشد.</li><li>**ابزارهای تابع**: فراخوانی‌های تعریف‌شده با JSON Schema به کد برنامه شما. بیشتر بدانید: [فراخوانی تابع](fa/guides/function-calling.md).</li><li>**ابزارهای سفارشی**: ابزارهای دارای payload متن آزاد، در صورت پشتیبانی با امکان محدودسازی grammar.</li><li>**ابزارهای Remote MCP**: دسترسی به ابزارهای connector-style وقتی صریحا در دسترس باشد.</li></ul> |
| `top_logprobs`         | عدد صحیح یا null | اختیاری | 0        | تعداد محتمل‌ترین توکن‌های خروجی که در هر موقعیت توکن تولیدشده برگردانده می‌شود، از 0 تا 20. وقتی مدل/route انتخابی از logprob خروجی پشتیبانی می‌کند، آن را همراه با `include: ["message.output_text.logprobs"]` استفاده کنید. |
| `top_p`                | عدد یا null      | اختیاری | 1        | نمونه‌برداری هسته‌ای. توکن‌هایی با جرم احتمال top_p را در نظر می‌گیرد (مثلا 0.1 = 10٪ بالا). این یا `temperature` را تغییر دهید.                                                                                                                                                                                                                                                                             |
| `truncation`           | رشته یا null     | اختیاری | disabled | استراتژی کوتاه کردن: <ul><li>`auto`: اگر context از پنجره مدل فراتر رفت، با حذف آیتم‌های قدیمی از ابتدای مکالمه کوتاه می‌کند.</li><li>`disabled` (پیش‌فرض): در صورت فراتر رفتن پنجره زمینه، با خطای 400 ناموفق شوید.</li></ul>                                                                                                                                                                                   |
| `safety_identifier`    | رشته             | اختیاری |          | شناسه پایدار و حفظ‌کننده حریم خصوصی برای پایش سوءاستفاده. از hash پایدار یا شناسه داخلی opaque با حداکثر 64 کاراکتر استفاده کنید و PII خام نفرستید. [بهترین شیوه‌های ایمنی](fa/guides/safety-best-practices.md) را ببینید.                                                                                                                                                                                     |
| `prompt_cache_key`     | رشته             | اختیاری |          | کلید bucket کردن cache برای prefixهای تکراری مشابه. آن را opaque و پایدار برای assistant، tenant، policy یا schema نگه دارید؛ PII خام یا request ID را در آن قرار ندهید. [Prompt caching](fa/guides/prompt-caching.md) را ببینید.                                                                                                                                                                            |
| `prompt_cache_retention` | رشته           | اختیاری |          | سیاست legacy برای حداکثر ماندگاری مدل‌های پیش از GPT-5.6. این فیلد برای GPT-5.6 و خانواده‌های بعدی deprecated است؛ OpenAI در نسل جدید از `prompt_cache_options.ttl` استفاده می‌کند و pass-through کنترل‌های جدید در AvalAI به route وابسته است. کنترل پشتیبانی‌نشده را حذف کنید.                                                                                                                          |
| `moderation`           | شی               | اختیاری |          | پیکربندی inline moderation، مثلا `{ "model": "omni-moderation-latest" }`، در صورت فعال بودن برای route/model انتخابی. اگر inline moderation در دسترس نیست، پیش و/یا پس از generation، [`/v1/moderations`](fa/api-reference/moderation.md) را جداگانه فراخوانی کنید.                                                                                                                                          |
| `user`                 | رشته             | اختیاری |          | فیلد قدیمی شناسه کاربر نهایی. برای پایش سوءاستفاده از `safety_identifier` و برای bucket کردن cache از `prompt_cache_key` استفاده کنید؛ `user` را فقط برای integrationهای قدیمی که هنوز به آن نیاز دارند نگه دارید.                                                                                                                                                                                               |
| `service_tier`         | رشته             | اختیاری | default | سطح سرویس مورد استفاده برای این درخواست. AvalAI به‌طور عمومی `"default"` (پیش‌فرض) و `"flex"` را پشتیبانی می‌کند. سطح flex ۵۰٪ کاهش قیمت برای مدل‌های منتخب OpenAI ارائه می‌دهد اما تاخیر بالاتر دارد و ممکن است تایم‌اوت شود (تا ۹۰۰ ثانیه). بعضی مثال‌های OpenAI ممکن است `"priority"` داشته باشند؛ در AvalAI از `"default"` استفاده کنید مگر اینکه priority processing صراحتا برای حساب شما فعال شده باشد. [قیمت‌گذاری](fa/pricing.md#سطح-سرویس-flex) را ببینید. |

### نکات پیکربندی ابزارها

شکل درخواست ابزارها را از مدل OpenAI بگیرید، سپس تأیید کنید route انتخابی AvalAI همان نوع ابزار را ارائه می‌دهد:

- **ابزارهای تابعی:** برای آرگومان‌های قابل اعتماد از `strict: true`، `additionalProperties: false` و فیلدهای `required` صریح استفاده کنید. فقط تابع‌های allowlist شده را در برنامه خودتان اجرا کنید.
- **`tool_choice`:** برای routing عادی از `"auto"`، برای الزام اجرای ابزار از `"required"`، برای خروجی فقط متنی از `"none"`، یا برای اجرای یک ابزار مشخص از انتخاب صریح function/web-search استفاده کنید. اگر route پشتیبانی کند، `allowed_tools` می‌تواند subset قابل فراخوانی را بدون تغییر کل آرایه `tools` محدود کند.
- **فراخوانی موازی:** برای ابزارهایی که state را تغییر می‌دهند، approval می‌خواهند یا به ترتیب اجرای هم وابسته‌اند، `parallel_tool_calls: false` بگذارید. فراخوانی موازی روی functionهای سفارشی اعمال می‌شود؛ ابزارهای داخلی ممکن است قواعد sequence خودشان را داشته باشند.
- **جستجوی وب:** کنترل‌های وابسته به route می‌توانند شامل `search_context_size`، `filters.allowed_domains`، `filters.blocked_domains`، `external_web_access`، `return_token_budget` و `include: ["web_search_call.action.sources"]` باشند.
- **جستجوی فایل:** پشتیبانی میزبانی‌شده آینده از شکل OpenAI با `vector_store_ids`، `max_num_results`، `filters`، `ranking_options` و `include: ["file_search_call.results"]` پیروی می‌کند. تا زمانی که AvalAI vector store میزبانی‌شده را اعلام نکرده، از مسیر RAG دستی در [ابزار جستجوی فایل](fa/guides/tools-file-search.md) استفاده کنید.
- **Remote MCP و connectorها:** فقط سرورهای قابل اعتماد را expose کنید، مقدارهای OAuth `authorization` را بیرون از prompt بفرستید، `allowed_tools` را محدود کنید و برای عملیات حساس از `require_approval` استفاده کنید. اگر `type: "mcp"` روی route انتخابی فعال نیست، سرویس خارجی را پشت یک function tool خودتان قرار دهید.
- **ابزارهای deferred:** `tool_search`، ابزارهای namespaced، `defer_loading` و `additional_tools` اندازه context اولیه را برای کاتالوگ‌های بزرگ ابزار کم می‌کنند، اما به مدل و route وابسته‌اند.

### نکات متن و خروجی ساختاریافته

از `text.format` آگاهانه استفاده کنید:

- **خروجی‌های ساختاریافته:** برای پاسخ نهایی تایپ‌شده، `{"type": "json_schema", "strict": true, "schema": ...}` را ترجیح دهید. این حالت پایبندی به schema را enforce می‌کند، در حالی که JSON mode فقط JSON معتبر را تضمین می‌کند.
- **fallback با JSON mode:** فقط وقتی پایبندی به schema در دسترس نیست یا لازم نیست از `{"type": "json_object"}` استفاده کنید، و در instruction صریحا بگویید مدل باید JSON خروجی دهد.
- **امتناع و خروجی ناقص:** پیش از parse کردن `response.output_text`، content partهای `response.output` و مقدارهای `response.status` / `incomplete_details` را بررسی کنید؛ امتناع‌های ایمنی و generationهای قطع‌شده ممکن است با schema شما منطبق نباشند.
- **عملیات schema:** schemaها را پایدار و نسخه‌دار نگه دارید. providerها ممکن است schemaها را برای performance پردازش و cache کنند، بنابراین پیش از استفاده از schemaهای حساس یا schemaهای یک‌بارمصرف برای هر کاربر، route دقیق AvalAI را تست کنید.

### نکات state، compaction و هزینه

مدل state در Responses را آگاهانه انتخاب کنید:

- **یک استراتژی state انتخاب کنید:** برای chainهای ذخیره‌شده ساده از `previous_response_id`، فقط وقتی مکالمات پایدار صریحا فعال هستند از `conversation`، و وقتی trimming سمت برنامه یا کنترل stateless می‌خواهید از replay دستی Itemها استفاده کنید. در هر درخواست `instructions` ثابت را دوباره بفرستید، چون `previous_response_id` دستورالعمل‌های top-level قبلی را منتقل نمی‌کند.
- **reasoning بدون state را قابل‌حمل نگه دارید:** برای flowهای `store: false` روی routeهای OpenAI پشتیبانی‌شده، `include: ["reasoning.encrypted_content"]` را اضافه کنید و Itemهای reasoning/output برگشتی را در `input` بعدی append کنید تا context استدلال بدون ذخیره‌سازی سمت سرور ادامه پیدا کند.
- **تعامل‌های طولانی را compact کنید:** وقتی پشتیبانی شود، `context_management` همراه `compact_threshold` فشرده‌سازی سمت سرور را داخل `responses.create` اجرا می‌کند. برای `/v1/responses/compact` مستقل، پنجره compact‌شده برگشتی را همان‌طور که هست به درخواست بعدی بدهید؛ اگر route در دسترس نیست، context را در برنامه خودتان فشرده کنید و خلاصه صریح بفرستید.
- **برای کل chain بودجه بگذارید:** `previous_response_id` میانبر state است، نه context window رایگان. context قبلی زنجیره همچنان می‌تواند به عنوان input token محاسبه شود. قبل از درخواست‌های پرهزینه از `usage` پاسخ و، در صورت فعال بودن، `POST /v1/responses/input_tokens` استفاده کنید.
- **endpointهای مرتبط را بشناسید:** `POST /v1/responses/{response_id}/cancel` پاسخ‌های background پشتیبانی‌شده را لغو می‌کند، `GET /v1/responses/{response_id}/input_items` ورودی‌های ذخیره‌شده را فهرست می‌کند، `POST /v1/responses/input_tokens` اندازه درخواست را تخمین می‌زند، و `POST /v1/responses/compact` پنجره‌های طولانی را وقتی برای route AvalAI شما فعال باشد compact می‌کند.

### بازگشت‌ها (Returns)

یک [شی پاسخ (Response object)](fa/api-reference/responses?id=the-response-object) را برمی‌گرداند.

### درخواست نمونه (ورودی متنی)

```language-selector
bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
"model": "gpt-5.6-luna",
"input": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو."
}'

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.responses.create(
    model="gpt-5.6-luna",
    input="یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.",
)

print(response.output_text)

javascript=:import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,

  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",

  input: "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.",
});

console.log(response.output_text);

go=:package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}

	body := []byte(`{
		"model": "gpt-5.6-luna",
		"input": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو."
	}`)

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewReader(body))
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("خطای درخواست API: %v\n", err)
		return
	}
	defer resp.Body.Close()

	responseBody, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP %d: %s\n", resp.StatusCode, responseBody)
		return
	}

	var result struct {
		Output []struct {
			Type    string `json:"type"`
			Content []struct {
				Type string `json:"type"`
				Text string `json:"text"`
			} `json:"content"`
		} `json:"output"`
	}
	if err := json.Unmarshal(responseBody, &result); err != nil {
		fmt.Printf("خطا در رمزگشایی JSON: %v\n", err)
		return
	}

	for _, item := range result.Output {
		if item.Type != "message" {
			continue
		}
		for _, part := range item.Content {
			if part.Type == "output_text" {
				fmt.Println(part.Text)
			}
		}
	}
}

php=:<?php
// مثال PHP برای API پاسخ‌های AvalAI (/v1/responses)

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$apiUrl = 'https://api.avalai.ir/v1/responses';

$data = [
'model' => 'gpt-5.6-luna', // مدل مورد نظر را مشخص کنید
'input' => 'یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.'
// پارامترهای دیگر را در صورت نیاز اضافه کنید، به عنوان مثال:
// 'temperature' => 0.7,
// 'max_output_tokens' => 100,
];

$jsonData = json_encode($data);

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey, // اطمینان حاصل کنید که این AVALAI_API_KEY شما است
'Content-Length: ' . strlen($jsonData)
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } elseif (isset($responseData['output'][0]['content'][0]['text'])) {
    // دسترسی به متن بر اساس ساختار پاسخ نمونه ارائه شده
    echo "دستیار: " . $responseData['output'][0]['content'][0]['text'] . "\n";
  } else {
    echo "پاسخ دریافت شد، اما محتوای متنی مورد انتظار یافت نشد.\n";
    echo "پاسخ کامل:\n";
    print_r($responseData);
  }
}
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
    input="یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.",
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
  input: "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


### پاسخ نمونه

```json
{
  "id": "resp_67ccd2bed1ec8190b14f964abc0542670bb6a6b452d3795b",
  "object": "response",
  "created_at": 1741476542,
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.6-luna",
  "output": [
    {
      "type": "message",
      "id": "msg_67ccd2bf17f0819081ff3bb2cf6508e60bb6a6b452d3795b",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "در بیشه‌ای آرام زیر نور ماه نقره‌ای، تک‌شاخی به نام لومینا استخری پنهان را کشف کرد که ستارگان را منعکس می‌کرد. هنگامی که شاخ خود را در آب فرو برد، استخر شروع به درخشیدن کرد و مسیری به قلمرویی جادویی از آسمان‌های شب بی‌پایان را آشکار ساخت. لومینا که پر از شگفتی بود، آرزو کرد که همه کسانی که رویا می‌بینند، جادوی پنهان خود را پیدا کنند، و هنگامی که به عقب نگاه کرد، رد پاهایش مانند غبار ستاره می‌درخشید.",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
    }
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 36,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 87,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 123
  },
  "user": null,
  "metadata": {}
}
```

## دریافت پاسخ مدل

```
GET https://api.avalai.ir/v1/responses/{response_id}
```

یک پاسخ مدل با شناسه داده شده را بازیابی می‌کند.

### پارامترهای مسیر (Path Parameters)

| پارامتر       | نوع  | الزامی | توضیحات                          |
| ------------- | ---- | ------ | -------------------------------- |
| `response_id` | رشته | الزامی | شناسه پاسخی که باید بازیابی شود. |

### پارامترهای کوئری (Query Parameters)

| پارامتر   | نوع   | الزامی  | توضیحات                                                                                                                                              |
| --------- | ----- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `include` | آرایه | اختیاری | فیلدهای اضافی برای گنجاندن در پاسخ. برای اطلاعات بیشتر به پارامتر `include` در [ایجاد پاسخ](fa/api-reference/responses?id=request-body) مراجعه کنید. |
| `stream` | بولی | اختیاری | اگر `true` باشد، داده‌های پاسخ را هنگام تولید یا resume از طریق SSE stream می‌کند. فقط وقتی استفاده کنید که route انتخابی از streaming در retrieve پشتیبانی کند. |
| `starting_after` | عدد صحیح | اختیاری | stream را پس از رویدادی با این sequence number ادامه می‌دهد. برای reconnect در streamهای طولانی، آخرین `sequence_number` را ذخیره کنید. |
| `include_obfuscation` | بولی | اختیاری | کنترل می‌کند آیا رویدادهای delta جریانی شامل فیلدهای obfuscation برای یکنواخت کردن اندازه payload باشند یا نه. مقدار پیش‌فرض را نگه دارید مگر اینکه مسیر شبکه را کنترل می‌کنید و کاهش bandwidth نیاز دارید. |

### بازگشت‌ها (Returns)

[شی پاسخ (Response object)](fa/api-reference/responses?id=the-response-object) مطابق با شناسه مشخص شده را برمی‌گرداند.

### درخواست نمونه

```language-selector
bash=:curl https://api.avalai.ir/v1/responses/resp_123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.responses.retrieve("resp_123")
print(response)

javascript=:import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,

  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.retrieve("resp_123");
console.log(response);

go=:package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_123" // شناسه پاسخی که باید بازیابی شود

	req, err := http.NewRequestWithContext(
		context.Background(),
		http.MethodGet,
		"https://api.avalai.ir/v1/responses/"+responseID,
		nil,
	)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Accept", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		fmt.Printf("خطای درخواست API: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP %d: %s\n", resp.StatusCode, body)
		return
	}

	var result map[string]any
	if err := json.Unmarshal(body, &result); err != nil {
		fmt.Printf("خطا در رمزگشایی JSON: %v\n", err)
		return
	}
	fmt.Printf("%+v\n", result)
}

php=:<?php
// مثال PHP برای بازیابی یک پاسخ خاص AvalAI (/v1/responses/{response_id})

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_123'; // شناسه پاسخی که باید بازیابی شود
$apiUrl = 'https://api.avalai.ir/v1/responses/' . $responseId;

// اختیاری: پارامترهای کوئری مانند 'include' را اضافه کنید
// $queryParams = ['include' => 'message.input_image.image_url'];
// $apiUrl .= '?' . http_build_query($queryParams);


$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json', // Content-Type ممکن است برای GET به طور دقیق لازم نباشد، اما روش خوبی است
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } else {
    echo "پاسخ با موفقیت بازیابی شد:\n";
    print_r($responseData);
  }
}
?>

```

### پاسخ نمونه

```json
{
  "id": "resp_67cb71b351908190a308f3859487620d06981a8637e6bc44",
  "object": "response",
  "created_at": 1741386163,
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.6-luna",
  "output": [
    {
      "type": "message",
      "id": "msg_67cb71b3c2b0819084d481baaaf148f206981a8637e6bc44",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "مدارهای خاموش زمزمه می‌کنند، \nافکار در جریان داده‌ها پدیدار می‌شوند— \nسپیده‌دم دیجیتال می‌شکند.",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
    }
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 32,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 18,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 50
  },
  "user": null,
  "metadata": {}
}
```

## حذف پاسخ مدل

```
DELETE https://api.avalai.ir/v1/responses/{response_id}
```

یک پاسخ مدل با شناسه داده شده را حذف می‌کند.

### پارامترهای مسیر (Path Parameters)

| پارامتر       | نوع  | الزامی | توضیحات                      |
| ------------- | ---- | ------ | ---------------------------- |
| `response_id` | رشته | الزامی | شناسه پاسخی که باید حذف شود. |

### بازگشت‌ها (Returns)

یک پیام موفقیت‌آمیز که وضعیت حذف را نشان می‌دهد.

### درخواست نمونه

```language-selector
bash=:curl -X DELETE https://api.avalai.ir/v1/responses/resp_123 \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.responses.delete("resp_123")  # نام متد تصحیح شده
print(response)

javascript=:import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,

  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.del("resp_123"); // نام متد تصحیح شده
console.log(response);

go=:package main

import (
	"context"
	"fmt"
	"net/http"
	"os"
	// "io" // برای خواندن بدنه پاسخ از حالت کامنت خارج کنید

	openai "github.com/openai/openai-go" // کتابخانه ممکن است مستقیما از این پشتیبانی نکند
)

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_123" // شناسه پاسخی که باید حذف شود

	config := openai.DefaultConfig(apiKey)
	// تنظیم URL پایه AvalAI
	config.BaseURL = "https://api.avalai.ir/v1"

	// توجه: کتابخانه openai-go احتمالا متدی برای حذف 'responses' سفارشی ندارد.
	// یک درخواست HTTP DELETE خام رویکرد استاندارد است.

	fmt.Printf("تلاش برای حذف پاسخ با شناسه: %s با استفاده از HTTP DELETE خام\n", responseID)

	req, err := http.NewRequestWithContext(context.Background(), "DELETE", config.BaseURL+"/responses/"+responseID, nil)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)

	httpClient := &http.Client{}
	resp, err := httpClient.Do(req)
	if err != nil {
		fmt.Printf("خطا در انجام درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	// body, _ := io.ReadAll(resp.Body) // خواندن بدنه برای پیام‌های خطای احتمالی

	if resp.StatusCode >= 200 && resp.StatusCode < 300 {
		fmt.Printf("پاسخ %s با موفقیت حذف شد (کد وضعیت: %d)\n", responseID, resp.StatusCode)
		// تجزیه بدنه در صورت نیاز: به عنوان مثال، json.Unmarshal(body, &deleteConfirmation)
	} else {
		fmt.Printf("خطای HTTP: %d\n", resp.StatusCode)
		// fmt.Printf("بدنه پاسخ: %s\n", string(body))
	}
}

php=:<?php
// مثال PHP برای حذف یک پاسخ خاص AvalAI (/v1/responses/{response_id})

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_123'; // شناسه پاسخی که باید حذف شود
$apiUrl = 'https://api.avalai.ir/v1/responses/' . $responseId;

$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_CUSTOMREQUEST, "DELETE"); // مشخص کردن متد DELETE
curl_setopt($ch, CURLOPT_HTTPHEADER, [
// 'Content-Type: application/json', // معمولا برای DELETE لازم نیست
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } elseif (isset($responseData['deleted']) && $responseData['deleted'] === true) {
    echo "شناسه پاسخ " . (isset($responseData['id']) ? $responseData['id'] : $responseId) . " با موفقیت حذف شد.\n";
  } else {
    echo "پاسخ دریافت شد، اما تایید حذف یافت نشد یا نامعتبر است.\n";
    echo "پاسخ کامل:\n";
    print_r($responseData);
  }
}
?>

```

### پاسخ نمونه

```json
{
  "id": "resp_6786a1bec27481909a17d673315b29f6",
  "object": "response",
  "deleted": true
}
```

## لیست آیتم‌های ورودی

```
GET https://api.avalai.ir/v1/responses/{response_id}/input_items
```

لیستی از آیتم‌های ورودی برای یک پاسخ داده شده را برمی‌گرداند.

### پارامترهای مسیر (Path Parameters)

| پارامتر       | نوع  | الزامی | توضیحات                                             |
| ------------- | ---- | ------ | --------------------------------------------------- |
| `response_id` | رشته | الزامی | شناسه پاسخی که باید آیتم‌های ورودی آن بازیابی شوند. |

### پارامترهای کوئری (Query Parameters)

| پارامتر   | نوع      | الزامی  | پیش‌فرض | توضیحات                                                                                                                                              |
| --------- | -------- | ------- | ------- | ---------------------------------------------------------------------------------------------------------------------------------------------------- |
| `after`   | رشته     | اختیاری |         | شناسه آیتمی برای لیست کردن آیتم‌های بعد از آن، که در صفحه‌بندی استفاده می‌شود.                                                                       |
| `before`  | رشته     | اختیاری |         | شناسه آیتمی برای لیست کردن آیتم‌های قبل از آن، که در صفحه‌بندی استفاده می‌شود.                                                                       |
| `include` | آرایه    | اختیاری |         | فیلدهای اضافی برای گنجاندن در پاسخ. برای اطلاعات بیشتر به پارامتر `include` در [ایجاد پاسخ](fa/api-reference/responses?id=request-body) مراجعه کنید. |
| `limit`   | عدد صحیح | اختیاری | 20      | محدودیتی برای تعداد اشیا بازگردانده شده (1-100).                                                                                                    |
| `order`   | رشته     | اختیاری | asc     | ترتیبی که آیتم‌های ورودی باید در آن بازگردانده شوند (`asc` یا `desc`).                                                                               |

### بازگشت‌ها (Returns)

یک [شی لیست (list object)](fa/api-reference/responses?id=the-input-item-list-object) حاوی اشیا آیتم ورودی را برمی‌گرداند.

### درخواست نمونه

```language-selector
bash=:curl https://api.avalai.ir/v1/responses/resp_abc123/input_items \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY"

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # آدرس پایه
)

response = client.responses.input_items.list("resp_123")
print(response.data)

javascript=:import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,

  baseURL: "https://api.avalai.ir/v1",
});

const response = await client.responses.inputItems.list("resp_123");
console.log(response.data);

go=:package main

import (
	"context"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"net/url"
	"os"

	openai "github.com/openai/openai-go" // برای پیکربندی استفاده می‌شود، اما درخواست HTTP خام است
)

// تعریف ساختارها برای نمایش ساختار پاسخ JSON مورد انتظار
type InputItemList struct {
	Object  string      `json:"object"`
	Data    []InputItem `json:"data"`
	FirstID string      `json:"first_id"`
	LastID  string      `json:"last_id"`
	HasMore bool        `json:"has_more"`
}

type InputItem struct {
	ID      string         `json:"id"`
	Type    string         `json:"type"`
	Role    string         `json:"role"` // با فرض اینکه نوع 'message' نقش دارد
	Content []InputContent `json:"content"`
}

type InputContent struct {
	Type string `json:"type"`
	Text string `json:"text"` // با فرض نوع 'input_text'
}

func main() {
	apiKey := os.Getenv("AVALAI_API_KEY")
	if apiKey == "" {
		fmt.Println("متغیر محیطی AVALAI_API_KEY تنظیم نشده است.")
		return
	}
	responseID := "resp_abc123" // شناسه پاسخ

	config := openai.DefaultConfig(apiKey)
	// تنظیم URL پایه AvalAI
	config.BaseURL = "https://api.avalai.ir/v1"

	// توجه: کتابخانه openai-go متدی برای لیست کردن آیتم‌های ورودی یک 'response' سفارشی ندارد.
	// یک درخواست HTTP GET خام لازم است.

	fmt.Printf("تلاش برای لیست کردن آیتم‌های ورودی برای شناسه پاسخ: %s با استفاده از HTTP GET خام\n", responseID)

	// ساخت URL با پارامترهای کوئری بالقوه
	endpointURL, _ := url.Parse(config.BaseURL + "/responses/" + responseID + "/input_items")
	queryParams := url.Values{}
	// queryParams.Add("limit", "10") // مثال پارامتر کوئری
	endpointURL.RawQuery = queryParams.Encode()

	req, err := http.NewRequestWithContext(context.Background(), "GET", endpointURL.String(), nil)
	if err != nil {
		fmt.Printf("خطا در ایجاد درخواست: %v\n", err)
		return
	}
	req.Header.Set("Authorization", "Bearer "+apiKey)
	req.Header.Set("Accept", "application/json")

	httpClient := &http.Client{}
	resp, err := httpClient.Do(req)
	if err != nil {
		fmt.Printf("خطا در انجام درخواست: %v\n", err)
		return
	}
	defer resp.Body.Close()

	body, err := io.ReadAll(resp.Body)
	if err != nil {
		fmt.Printf("خطا در خواندن بدنه پاسخ: %v\n", err)
		return
	}

	if resp.StatusCode >= 400 {
		fmt.Printf("خطای HTTP: %d\n", resp.StatusCode)
		fmt.Printf("بدنه پاسخ: %s\n", string(body))
		return
	}

	var itemList InputItemList
	err = json.Unmarshal(body, &itemList)
	if err != nil {
		fmt.Printf("خطا در unmarshal کردن پاسخ JSON: %v\n", err)
		fmt.Printf("بدنه پاسخ خام: %s\n", string(body))
		return
	}

	fmt.Printf("لیست آیتم‌های ورودی با موفقیت بازیابی شد:\n")
	// پردازش itemList در صورت نیاز
	fmt.Printf("%+v\n", itemList)
}

php=:<?php
// مثال PHP برای لیست کردن آیتم‌های ورودی برای یک پاسخ AvalAI (/v1/responses/{response_id}/input_items)

$apiKey = getenv('AVALAI_API_KEY'); // یا مستقیما با کلید خود جایگزین کنید
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$responseId = 'resp_abc123'; // شناسه پاسخ
$apiUrlBase = 'https://api.avalai.ir/v1/responses/' . $responseId . '/input_items';

// اختیاری: پارامترهای کوئری را اضافه کنید
$queryParams = [
// 'limit' => 10,
// 'order' => 'desc',
// 'after' => 'msg_xyz789',
// 'include' => 'message.input_image.image_url'
];
$apiUrl = $apiUrlBase . (empty($queryParams) ? '' : '?' . http_build_query($queryParams));


$ch = curl_init($apiUrl);

curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json', // ممکن است برای GET به طور دقیق لازم نباشد
'Authorization: Bearer ' . $apiKey
]);
// اختیاری: تنظیمات وقفه زمانی را اضافه کنید
// curl_setopt($ch, CURLOPT_CONNECTTIMEOUT, 10);
// curl_setopt($ch, CURLOPT_TIMEOUT, 30);

$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);

curl_close($ch);

if ($err) {
  echo "خطای cURL #: " . $err . "\n";
} elseif ($httpcode >= 400) {
  echo "خطای HTTP: " . $httpcode . "\n";
  echo "بدنه پاسخ: " . $response . "\n";
} else {
  $responseData = json_decode($response, true);
  if (json_last_error() !== JSON_ERROR_NONE) {
    echo "خطا در رمزگشایی پاسخ JSON: " . json_last_error_msg() . "\n";
    echo "پاسخ خام: " . $response . "\n";
  } else {
    echo "لیست آیتم‌های ورودی با موفقیت بازیابی شد:\n";
    print_r($responseData);
  }
}
?>

```

### پاسخ نمونه

```json
{
  "object": "list",
  "data": [
    {
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو."
        }
      ]
    }
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false
}
```

## شی پاسخ (Response object)

یک پاسخ تولید شده توسط مدل را نشان می‌دهد.

| ویژگی                  | نوع              | توضیحات                                                                                                                                                          |
| ---------------------- | ---------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `id`                   | رشته             | شناسه منحصر به فرد برای این پاسخ.                                                                                                                                |
| `object`               | رشته             | نوع شی، همیشه `response`.                                                                                                                                       |
| `created_at`           | عدد              | مُهر زمانی یونیکس (به ثانیه) زمان ایجاد این پاسخ.                                                                                                                |
| `completed_at`         | عدد یا null      | مُهر زمانی یونیکس (به ثانیه) زمان تکمیل پاسخ، وقتی route انتخابی آن را برگرداند.                                                                                   |
| `status`               | رشته             | وضعیت تولید پاسخ. یکی از `completed`، `failed`، `in_progress` یا `incomplete`.                                                                                   |
| `background`           | بولی یا null     | اینکه پاسخ به صورت job پس‌زمینه اجرا شده است یا نه، وقتی route انتخابی آن را برگرداند.                                                                              |
| `error`                | شی یا null      | یک شی خطا که هنگام عدم موفقیت مدل در تولید پاسخ بازگردانده می‌شود. شامل `code` و `message` است.                                                                 |
| `incomplete_details`   | شی یا null      | جزئیات درباره اینکه چرا پاسخ ناقص است. شامل `reason` است.                                                                                                        |
| `conversation`         | رشته یا شی یا null | مرجع مکالمه استفاده‌شده برای این پاسخ، وقتی مکالمات پایدار فعال باشند.                                                                                          |
| `context_management`   | شی یا null       | پیکربندی مدیریت context استفاده‌شده برای پاسخ، وقتی route آن را برگرداند.                                                                                         |
| `instructions`         | رشته یا null     | پیام سیستمی (یا توسعه‌دهنده) ارائه شده در درخواست.                                                                                                               |
| `max_output_tokens`    | عدد صحیح یا null | حد بالای توکن‌های تولید شده که در درخواست مشخص شده است.                                                                                                          |
| `max_tool_calls`       | عدد صحیح یا null | حداکثر فراخوانی‌های ابزار داخلی مجاز برای این پاسخ، وقتی مشخص شده یا برگردانده شود.                                                                                |
| `metadata`             | نقشه             | جفت‌های کلید-مقدار پیوست شده به شی.                                                                                                                             |
| `model`                | رشته             | شناسه مدلی که برای تولید پاسخ استفاده شده است.                                                                                                                   |
| `output`               | آرایه            | آرایه‌ای از آیتم‌های محتوای تولید شده توسط مدل (مثلا `message`، `tool_call`). ترتیب و محتوا به پاسخ مدل بستگی دارد.                                             |
| `output_text`          | رشته یا null     | **فقط SDK**: خروجی متنی تجمیع شده از تمام آیتم‌های `output_text` در آرایه `output`.                                                                              |
| `parallel_tool_calls`  | بولی             | آیا فراخوانی‌های ابزار موازی فعال بوده‌اند.                                                                                                                      |
| `previous_response_id` | رشته یا null     | شناسه پاسخ قبلی که برای وضعیت مکالمه استفاده شده است.                                                                                                            |
| `prompt`               | شی یا null       | مرجع prompt template و متغیرهای آن، وقتی استفاده شده و توسط route/account انتخابی برگردانده شود.                                                                  |
| `reasoning`            | شی یا null      | تنظیمات reasoning و summary برای مدل‌های استدلال پشتیبانی‌شده سری GPT-5 و سری o.                                                                                 |
| `store`                | بولی             | آیا پاسخ ذخیره شده است.                                                                                                                                          |
| `temperature`          | عدد یا null      | دمای نمونه‌برداری استفاده شده.                                                                                                                                   |
| `text`                 | شی              | گزینه‌های پیکربندی برای پاسخ متنی استفاده شده (مثلا `format`).                                                                                                  |
| `tool_choice`          | رشته یا شی      | تنظیمات انتخاب ابزار استفاده شده.                                                                                                                                |
| `tools`                | آرایه            | آرایه ابزارهای ارائه شده در درخواست.                                                                                                                             |
| `top_logprobs`         | عدد صحیح یا null | تعداد گزینه‌های logprob خروجی درخواست‌شده برای توکن‌های تولیدشده، در صورت پشتیبانی.                                                                                |
| `top_p`                | عدد یا null      | احتمال نمونه‌برداری هسته‌ای استفاده شده.                                                                                                                         |
| `truncation`           | رشته یا null     | استراتژی کوتاه کردن استفاده شده (`auto` یا `disabled`).                                                                                                          |
| `usage`                | شی              | جزئیات استفاده از توکن: `input_tokens`، `input_tokens_details` (`cached_tokens` و برای routeهای سازگار GPT-5.6، `cache_write_tokens`)، `output_tokens`، `output_tokens_details` (`reasoning_tokens`)، `total_tokens`. |
| `safety_identifier`    | رشته یا null     | شناسه ایمنی حفظ‌کننده حریم خصوصی در صورت ارائه و بازگردانده شدن توسط route/model انتخابی.                                                                         |
| `prompt_cache_key`     | رشته یا null     | کلید bucket کردن prompt cache در صورت ارائه و بازگردانده شدن توسط route/model انتخابی.                                                                            |
| `prompt_cache_retention` | رشته یا null   | سیاست legacy نگه‌داری prompt cache برای پاسخ‌های پیش از GPT-5.6، در صورت پشتیبانی و بازگردانده‌شدن.                                                              |
| `moderation`           | شی یا null       | نتایج inline moderation ورودی/خروجی، در صورت درخواست و پشتیبانی.                                                                                                  |
| `user`                 | رشته یا null     | شناسه قدیمی کاربر نهایی، در صورت ارسال توسط clientهای قدیمی.                                                                                                      |
| `service_tier`         | رشته             | سطح سرویس استفاده شده برای این درخواست. مقادیر عمومی AvalAI معمولا `"default"` یا `"flex"` هستند؛ `"priority"` فقط در صورت فعال‌سازی صریح برای حساب/route قابل اتکاست. |

### شی پاسخ نمونه

```json
{
  "id": "resp_67ccd3a9da748190baa7f1570fe91ac604becb25c45c1d41",
  "object": "response",
  "created_at": 1741476777,
  "status": "completed",
  "error": null,
  "incomplete_details": null,
  "instructions": null,
  "max_output_tokens": null,
  "model": "gpt-5.6-luna",
  "output": [
    {
      "type": "message",
      "id": "msg_67ccd3acc8d48190a77525dc6de64b4104becb25c45c1d41",
      "status": "completed",
      "role": "assistant",
      "content": [
        {
          "type": "output_text",
          "text": "تصویر منظره‌ای زیبا را با یک پیاده‌روی چوبی یا مسیری که از میان چمن‌های سرسبز و شاداب زیر آسمان آبی با چند ابر می‌گذرد، نشان می‌دهد. محیط یک منطقه طبیعی آرام، احتمالا یک پارک یا ذخیره‌گاه طبیعی را تداعی می‌کند. درختان و بوته‌ها در پس‌زمینه وجود دارند.",
          "annotations": []
        }
      ]
    }
  ],
  "parallel_tool_calls": true,
  "previous_response_id": null,
  "reasoning": {
    "effort": null,
    "summary": null
  },
  "store": true,
  "temperature": 1.0,
  "text": {
    "format": {
      "type": "text"
    }
  },
  "tool_choice": "auto",
  "tools": [],
  "top_p": 1.0,
  "truncation": "disabled",
  "usage": {
    "input_tokens": 328,
    "input_tokens_details": {
      "cached_tokens": 0
    },
    "output_tokens": 52,
    "output_tokens_details": {
      "reasoning_tokens": 0
    },
    "total_tokens": 380
  },
  "user": null,
  "metadata": {}
}
```

## شی لیست آیتم ورودی

یک لیست صفحه‌بندی شده از آیتم‌های ورودی برای یک پاسخ را نشان می‌دهد.

| ویژگی      | نوع   | توضیحات                                                                        |
| ---------- | ----- | ------------------------------------------------------------------------------ |
| `object`   | رشته  | نوع شی بازگردانده شده، همیشه `list`.                                          |
| `data`     | آرایه | لیستی از آیتم‌های ورودی (مثلا اشیا پیام) که برای تولید پاسخ استفاده شده‌اند. |
| `first_id` | رشته  | شناسه اولین آیتم در لیست برای صفحه‌بندی.                                       |
| `last_id`  | رشته  | شناسه آخرین آیتم در لیست برای صفحه‌بندی.                                       |
| `has_more` | بولی  | آیا آیتم‌های بیشتری بعد از این صفحه موجود است.                                 |

### شی لیست نمونه

```json
{
  "object": "list",
  "data": [
    {
      "id": "msg_abc123",
      "type": "message",
      "role": "user",
      "content": [
        {
          "type": "input_text",
          "text": "یک داستان سه جمله‌ای قبل از خواب درباره یک تک‌شاخ برایم بگو."
        }
      ]
    }
  ],
  "first_id": "msg_abc123",
  "last_id": "msg_abc123",
  "has_more": false
}
```

## پخش جریانی (Streaming)

وقتی با `stream: true` یک [پاسخ ایجاد می‌کنید](fa/api-reference/responses?id=create-a-model-response)، AvalAI جریان SSE برمی‌گرداند. پخش جریانی Responses از تکه‌های شبیه Chat Completions مانند `choices[].delta` استفاده نمی‌کند؛ هر payload یک رویداد تایپ‌شده با `event.type` مانند `response.created`، `response.output_text.delta`، `response.output_text.done`، `response.completed`، `response.failed` یا `error` است.

برای جریان متن، این خانواده رویدادهای رایج را مدیریت کنید:

| رویداد | زمان استفاده |
| ------ | ------------ |
| `response.created` / `response.in_progress` | وضعیت UI را آماده کنید، شناسه پاسخ را ذخیره کنید و نشان دهید generation شروع شده است. |
| `response.output_item.added` / `response.output_item.done` | آیتم‌های خروجی تایپ‌شده مثل پیام، فراخوانی ابزار و آیتم‌های reasoning را دنبال کنید. |
| `response.content_part.added` / `response.content_part.done` | content partهای داخل یک پیام را دنبال کنید. |
| `response.output_text.delta` | مقدار `delta` را به متن قابل نمایش دستیار اضافه کنید. |
| `response.output_text.done` | متن بافرشده را با متن نهایی همان content part تطبیق دهید یا جایگزین کنید. |
| `response.output_text.annotation.added` | citationها، ارجاع فایل یا annotationهای جستجو را ذخیره کنید تا بعد از پایدار شدن متن مرتبط render شوند. |
| `response.refusal.delta` / `response.refusal.done` | متن refusal ایمنی را جدا از متن پاسخ عادی نگه دارید و refusal نهایی را پاسخ پایانی دستیار بدانید. |
| `response.function_call_arguments.delta` / `response.function_call_arguments.done` | آرگومان‌های فراخوانی ابزار را بافر کنید و تابع را فقط پس از رویداد `done` اجرا کنید. |
| `response.file_search_call.in_progress` / `response.file_search_call.searching` / `response.file_search_call.completed` | وقتی file search میزبانی‌شده برای route انتخابی AvalAI فعال است، پیشرفت retrieval را به‌روز کنید. |
| `response.code_interpreter_call.in_progress` / `response.code_interpreter_call_code.delta` / `response.code_interpreter_call.completed` | وضعیت interpreter و کد تولیدشده را در پنل جداگانه stream کنید؛ خروجی‌ها را فقط بعد از تکمیل منتشر کنید. |
| `response.completed` | جریان را نهایی کنید و usage، status و metadata خروجی نهایی را بخوانید. |
| `response.failed` / `error` | نمایش جریان را متوقف کنید و خطا را نشان دهید یا retry کنید. |

برای الگوهای پیاده‌سازی و نکات ایمنی، راهنمای جریان را ببینید: [پاسخ‌های API جریانی](fa/guides/streaming-responses.md).

برای پاسخ‌های طولانی یا پس‌زمینه، وقتی موجود است آخرین `sequence_number` رویداد را ذخیره کنید. اگر route شما از streaming هنگام retrieve پاسخ پشتیبانی می‌کند، با `GET /v1/responses/{response_id}?stream=true&starting_after=<sequence_number>` دوباره وصل شوید و `include_obfuscation` را روشن نگه دارید مگر اینکه یک stream داخلی قابل اعتماد را برای bandwidth کمتر بهینه می‌کنید.

### نمونه رویدادهای SSE

```text
event: response.created
data: {"type":"response.created","response":{"id":"resp_123","status":"in_progress"}}

event: response.output_text.delta
data: {"type":"response.output_text.delta","delta":"سلام"}

event: response.output_text.delta
data: {"type":"response.output_text.delta","delta":" دنیا"}

event: response.output_text.done
data: {"type":"response.output_text.done","text":"سلام دنیا"}

event: response.completed
data: {"type":"response.completed","response":{"id":"resp_123","status":"completed"}}
```

### مدیریت جریان

مقدار `event.delta` را از رویدادهای `response.output_text.delta` جمع کنید، سپس با `response.output_text.done` و metadata نهایی در `response.completed` تطبیق دهید. الگوهای قدیمی مانند `choices[0].delta.content` یا `chunk.output[0].delta.content` مربوط به Chat Completions هستند و برای Responses مناسب نیستند.

```language-selector
bash=:# شروع جریان SSE از AvalAI. در تولید، کلاینت باید خطوط
# event: و data: را parse کند، بر اساس نوع رویداد شاخه‌بندی کند و خطاها را مدیریت کند.
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Accept: text/event-stream" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "یک داستان برایم بگو.",
    "stream": true
  }' \
  --no-buffer

python=:import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

stream = client.responses.create(
    model="gpt-5.6-luna",
    input="یک داستان برایم بگو.",
    stream=True,
)

print("دستیار: ", end="", flush=True)
for event in stream:
    if event.type == "response.output_text.delta":
        print(event.delta, end="", flush=True)
    elif event.type == "response.completed":
        print()
    elif event.type == "error":
        raise RuntimeError(event.error)

javascript=:import OpenAI from "openai";

const openai = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const stream = await openai.responses.create({
  model: "gpt-5.6-luna",
  input: "یک داستان برایم بگو.",
  stream: true,
});

process.stdout.write("دستیار: ");
for await (const event of stream) {
  if (event.type === "response.output_text.delta") {
    process.stdout.write(event.delta);
  } else if (event.type === "response.completed") {
    process.stdout.write("\n");
  } else if (event.type === "error") {
    throw new Error(event.error?.message || "Streaming error");
  }
}

go=:package main

import (
	"bufio"
	"bytes"
	"encoding/json"
	"fmt"
	"net/http"
	"os"
	"strings"
)

type streamEvent struct {
	Type  string `json:"type"`
	Delta string `json:"delta"`
	Error *struct {
		Message string `json:"message"`
	} `json:"error"`
}

func main() {
	payload := []byte(`{
		"model":"gpt-5.6-luna",
		"input":"یک داستان برایم بگو.",
		"stream":true
	}`)

	req, err := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewReader(payload))
	if err != nil {
		panic(err)
	}
	req.Header.Set("Content-Type", "application/json")
	req.Header.Set("Accept", "text/event-stream")
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()

	fmt.Print("Assistant: ")
	scanner := bufio.NewScanner(resp.Body)
	for scanner.Scan() {
		line := scanner.Text()
		if !strings.HasPrefix(line, "data: ") {
			continue
		}

		data := strings.TrimPrefix(line, "data: ")
		if data == "[DONE]" {
			break
		}

		var event streamEvent
		if err := json.Unmarshal([]byte(data), &event); err != nil {
			continue
		}

		switch event.Type {
		case "response.output_text.delta":
			fmt.Print(event.Delta)
		case "response.completed":
			fmt.Println()
		case "error":
			if event.Error != nil {
				panic(event.Error.Message)
			}
		}
	}
}

php=:<?php
$apiKey = getenv('AVALAI_API_KEY');
if (!$apiKey) {
  die("خطا: متغیر محیطی AVALAI_API_KEY تنظیم نشده است.\n");
}

$payload = json_encode([
  'model' => 'gpt-5.6-luna',
  'input' => 'یک داستان برایم بگو.',
  'stream' => true,
]);

$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
  CURLOPT_POST => true,
  CURLOPT_POSTFIELDS => $payload,
  CURLOPT_RETURNTRANSFER => false,
  CURLOPT_HTTPHEADER => [
    'Content-Type: application/json',
    'Accept: text/event-stream',
    'Authorization: Bearer ' . $apiKey,
  ],
  CURLOPT_WRITEFUNCTION => function ($curl, $chunk) {
    foreach (explode("\n", $chunk) as $line) {
      if (!str_starts_with($line, 'data: ')) {
        continue;
      }

      $data = substr($line, 6);
      if ($data === '[DONE]') {
        return strlen($chunk);
      }

      $event = json_decode($data, true);
      if (($event['type'] ?? null) === 'response.output_text.delta') {
        echo $event['delta'] ?? '';
        flush();
      }
    }

    return strlen($chunk);
  },
]);

curl_exec($ch);
if (curl_errno($ch)) {
  fwrite(STDERR, "\nخطای جریان: " . curl_error($ch) . "\n");
}
curl_close($ch);
echo "\n";
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
    input="یک داستان برایم بگو.",
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
  input: "یک داستان برایم بگو.",
});

console.log(response.output_text);

bash=:curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "یک داستان برایم بگو.",
    "instructions": "You are a helpful assistant."
  }'

```

- `messages` → `input`
- پیام سیستمی → `instructions` یا آیتم `developer`
- `choices[0].message.content` → `response.output_text`
- برای ابزارها و خروجی‌های چندوجهی، `response.output` را بر اساس `type` بررسی کنید.

</details>
<!-- responses-equivalent:end -->


برای راهنماهای خاص مدیریت جریان به مستندات SDK مراجعه کنید.
