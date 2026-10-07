# پشتیبانی SDK Anthropic از چندین ارائه دهنده و افزودن مدل‌های جدید

**تاریخ:** 1404-03-19 / (2025-06-09)

## خلاصه

AvalAI پشتیبانی SDK Anthropic را برای شامل شدن چندین ارائه دهنده فراتر از مدل‌های Claude گسترش داده است که اکنون از OpenAI، Anthropic، AWS Bedrock، Vertex AI و Gemini پشتیبانی می‌کند. علاوه بر این، عملکرد سیستم به طور قابل توجهی بهبود یافته است با کاهش تاخیر ۳۰ درصدی و ظرفیت درخواست همزمان دو برابر. مدل‌های جدیدی از جمله Gemini 2.5 Pro Preview 06-05 و Codex Mini Latest از OpenAI اضافه شده‌اند.

---

## جزئیات

ما با افتخار چندین به‌روزرسانی عمده برای پلتفرم AvalAI را اعلام می‌کنیم که سازگاری، عملکرد و در دسترس بودن مدل‌ها را بهبود می‌بخشد.

### بهبود پشتیبانی SDK Anthropic

تنها چند روز پس از افزودن پشتیبانی از SDK رسمی Anthropic، ما قابلیت‌های آن را برای کار با چندین ارائه دهنده فراتر از مدل‌های خود Anthropic گسترش داده‌ایم. این بهبود قابل توجه به توسعه‌دهندگان امکان می‌دهد از SDK Anthropic با مدل‌های چت از:

- **OpenAI**
- **Anthropic**
- **AWS Bedrock**
- **Vertex AI**
- **Gemini**

هر مدل چت از این ارائه‌دهندگان که از نقطه پایانی تکمیل چت پشتیبانی می‌کند، اکنون می‌تواند از طریق SDK رسمی Anthropic و نقطه پایانی "v1/messages" در ساختار API Anthropic استفاده شود. این بهبود، سازگاری API AvalAI را بیش از پیش افزایش می‌دهد و به توسعه‌دهندگان انعطاف پذیری بیشتری در نحوه تعامل با سیستم API یکپارچه ما می‌دهد.

#### مثال Python

```python
import anthropic

client = anthropic.Anthropic(
    api_key="AVALAI_API_KEY",
    base_url="https://api.avalai.ir",  # نقطه پایانی API AvalAI بدون /v1
)

# استفاده از مدل OpenAI از طریق SDK Anthropic
message = client.messages.create(
    model="gpt-4o",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام!"}],
)
print(message.content)

# استفاده از مدل Gemini از طریق SDK Anthropic
message = client.messages.create(
    model="gemini-2.5-pro",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام!"}],
)
print(message.content)
```

#### مثال JavaScript

```javascript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
 apiKey: process.env.AVALAI_API_KEY,
 baseURL: "https://api.avalai.ir",  // نقطه پایانی API AvalAI بدون /v1
});

# استفاده از مدل Anthropic از طریق SDK Anthropic
const message = await anthropic.messages.create({
 model: "anthropic.claude-opus-4-20250514-v1:0",
 max_tokens: 1024,
 messages: [{ role: "user", content: "سلام!" }],
});
console.log(message.content);
```

### بهبود عملکرد سیستم

ما ارتقاهای قابل توجهی در زیرساخت سیستم API خود انجام داده‌ایم که منجر به:

- **کاهش ۳۰ درصدی تاخیر** در تمام نقاط پایانی API
- **عملکرد دو برابری سیستم** برای مدیریت درخواست‌های همزمان
- **بهبود توان عملیاتی کلی** برای تمام ارائه‌دهندگان مدل

این بهبودها تجربه‌ای سریعتر را به ویژه در زمان‌های اوج استفاده تضمین می‌کند و قابلیت اطمینان بهتری برای برنامه‌های تولیدی فراهم می‌کند.

### افزودن مدل‌های جدید

#### Gemini

- **gemini-2.5-pro-preview-06-05**: یک نسخه جدید از Gemini 2.5 Pro با عملکرد بهبود یافته در معیارهای سنجش در مقایسه با نسخه قبلی gemini-2.5-pro-preview-05-06. این مدل قیمت‌گذاری یکسانی را حفظ می‌کند در حالی که قابلیت‌های بهبود یافته‌ای ارائه می‌دهد.

#### OpenAI

- **codex-mini-latest**: یک مدل استدلال سریع که به طور خاص برای Codex CLI بهینه شده است. این مدل ارائه می‌دهد:
 - پنجره زمینه ۲۰۰,۰۰۰ توکنی
 - حداکثر ۱۰۰,۰۰۰ توکن خروجی
 - تاریخ قطع دانش ۳۱ مه ۲۰۲۴
 - پشتیبانی از توکن استدلال
 - قابلیت‌های ورودی متن و تصویر
 - خروجی متن

##### قیمت‌گذاری codex-mini-latest
- **ورودی**: ۱.۵۰ دلار به ازای هر ۱ میلیون توکن (ورودی کش شده: ۰.۳۷۵ دلار به ازای هر ۱ میلیون توکن)
- **خروجی**: ۶.۰۰ دلار به ازای هر ۱ میلیون توکن

##### ویژگی‌های پشتیبانی شده
- استریمینگ
- فراخوانی تابع
- خروجی‌های ساختاریافته

##### نقاط پایانی در دسترس
- تکمیل چت (v1/chat/completions)
- پاسخ‌ها (v1/responses)

برای جزئیات بیشتر در مورد محدودیت‌های نرخ و اطلاعات مخصوص سطح برای این مدل‌های جدید، لطفا به [مستندات محدودیت‌های نرخ](fa/guides/rate-limits.md) ما مراجعه کنید.

---

## لینک‌های مرتبط

- [راهنمای ادغام SDK Anthropic](fa/libraries.md)
- [مستندات مدل‌های موجود](fa/api-reference/chat.md)
- [محدودیت‌های نرخ و قیمت‌گذاری](fa/guides/rate-limits.md)
- [مرجع API](fa/api-reference/introduction.md)
- [اعلامیه قبلی SDK Anthropic](fa/news/2025-06-03-anthropic-sdk-support-added.md)