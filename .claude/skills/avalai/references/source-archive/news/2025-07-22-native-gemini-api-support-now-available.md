<div dir="rtl">

# پشتیبانی بومی از API Gemini اکنون در دسترس است

**تاریخ:** 1403-04-31 / (2025-07-22)

## خلاصه

AvalAI اکنون از دسترسی بومی به مدل‌های Gemini با استفاده از SDK رسمی GenAI گوگل پشتیبانی می‌کند و به توسعه‌دهندگان گزینه سوم SDK را در کنار رویکردهای موجود سازگار با OpenAI و بومی Anthropic ارائه می‌دهد. این بهبود امکان یکپارچگی مستقیم با طرحواره یا اسکیمای API بومی گوگل را فراهم می‌کند در حالی که دسترسی یکپارچه از طریق زیرساخت AvalAI حفظ می‌شود.

---

## جزئیات

ما با افتخار اعلام می‌کنیم که AvalAI اکنون از دسترسی بومی به مدل‌های Gemini از طریق SDK رسمی GenAI گوگل پشتیبانی می‌کند. این اضافه گزینه‌های پشتیبانی SDK را گسترش می‌دهد و به توسعه‌دهندگان انعطاف بیشتری در نحوه یکپارچگی با مدل‌های هوش مصنوعی می‌دهد.

### سه رویکرد SDK اکنون در دسترس

AvalAI اکنون سه رویکرد متمایز برای دسترسی به مدل‌های هوش مصنوعی ارائه می‌دهد:

1. **SDK های سازگار با OpenAI** (رویکرد یکپارچه) - دسترسی به همه مدل‌ها از چندین ارائه دهنده با نحو یکسان OpenAI
2. **SDK های رسمی Anthropic** (رویکرد بومی) - استفاده از SDK های رسمی Anthropic برای دسترسی چندارائه دهنده
3. **SDK Google GenAI** (رویکرد بومی) - استفاده از SDK رسمی GenAI گوگل برای دسترسی بومی به مدل‌های Gemini

### پشتیبانی از SDK Google GenAI

پشتیبانی جدید بومی Gemini به توسعه‌دهندگان امکان استفاده از کتابخانه رسمی `genai` گوگل با زیرساخت AvalAI را می‌دهد و ارائه می‌کند:

- **طرحواره یا اسکیمای API بومی**: دسترسی مستقیم با استفاده از نقاط پایانی بومی `generateContent` و `streamGenerateContent` گوگل
- **احراز هویت انعطاف پذیر**: پشتیبانی از هر دو هدر `Authorization: Bearer` و `x-goog-api-key`
- **پشتیبانی از پاسخ جریانی**: پشتیبانی کامل از پاسخ‌های جریانی با `agenerate_content_stream`
- **قابلیت‌های چندوجهی**: پشتیبانی بومی از ورودی‌های متن، تصویر، صدا و ویدیو

### نمونه‌های استفاده

#### Python با SDK Google GenAI

```python
from google import genai
from google.genai.types import ContentDict, PartDict

# راه‌اندازی کلاینت
api_key = ("your-avalai-api-key",)  # با کلید واقعی خود جایگزین کنید
gemini_client = genai.Client(
    api_key=api_key, http_options={"base_url": "https://api.avalai.ir"}
)

# تولید محتوا
contents = ContentDict(
    parts=[PartDict(text="سلام، می‌توانید یک جوک کوتاه بگویید؟")],
    role="user",
)

response = await gemini_client.agenerate_content(
    contents=contents,
    model="gemini-2.0-flash",
    max_tokens=100,
)
print(response)
```

#### نمونه جریانی

```python
# تولید متن جریانی
response = await gemini_client.agenerate_content_stream(
    contents=contents,
    model="gemini-2.0-flash",
    max_tokens=500,
)

async for chunk in response:
    print(chunk)
```

#### دسترسی مستقیم API

```bash
# استفاده از هدر Authorization Bearer
curl -L -X POST 'https://api.avalai.ir/v1beta/models/gemini-flash:generateContent' \
  -H 'content-type: application/json' \
  -H 'Authorization: Bearer $AVALAI_API_KEY' \
  -d '{
 "contents": [
 {
 "parts": [{"text": "داستان کوتاهی درباره هوش مصنوعی بنویس"}],
 "role": "user"
 }
 ],
 "generationConfig": {
 "maxOutputTokens": 100
 }
 }'

# استفاده از فرمت هدر بومی گوگل
curl -L -X POST 'https://api.avalai.ir/v1beta/models/gemini-flash:generateContent' \
  -H 'content-type: application/json' \
  -H 'x-goog-api-key: $AVALAI_API_KEY' \
  -d '{
 "contents": [
 {
 "parts": [{"text": "داستان کوتاهی درباره هوش مصنوعی بنویس"}],
 "role": "user"
 }
 ],
 "generationConfig": {
 "maxOutputTokens": 100
 }
 }'
```

### محدودیت‌های مهم

- **فقط مدل‌های Gemini**: این پشتیبانی بومی منحصرا برای مدل‌های Gemini است. سایر سرویس‌ها یا مدل‌های گوگل از طریق این رویکرد پشتیبانی نمی‌شوند.
- **URL پایه**: هنگام استفاده از SDK Google GenAI، از `https://api.avalai.ir` به عنوان URL پایه استفاده کنید (بدون `/v1`)
- **فرمت نقطه پایانی**: نقاط پایانی بومی از الگوی `/v1beta/models/{model-name}:generateContent` پیروی می‌کنند

### نقاط پایانی موجود

- **تولید محتوا**: `/v1beta/models/{model-name}:generateContent`
- **تولید محتوای جریانی**: `/v1beta/models/{model-name}:streamGenerateContent`

### شروع کار

برای شروع استفاده از پشتیبانی بومی API Gemini:

1. SDK Google GenAI را نصب کنید: `pip install google-generativeai`
2. کلاینت خود را با URL پایه AvalAI پیکربندی کنید
3. از کلید API موجود AvalAI خود برای احراز هویت استفاده کنید
4. به هر مدل Gemini پشتیبانی شده از طریق طرحواره یا اسکیمای API بومی دسترسی پیدا کنید

---

## لینک‌های مرتبط

- [مرجع API v1beta SDK Google GenAI](fa/api-reference/v1beta.md)
- [مستندات مدل‌های گوگل](fa/providers/google.md)
- [مستندات کتابخانه‌ها](fa/libraries.md)
- [راهنمای احراز هویت API](fa/api-reference/authentication.md)

</div>