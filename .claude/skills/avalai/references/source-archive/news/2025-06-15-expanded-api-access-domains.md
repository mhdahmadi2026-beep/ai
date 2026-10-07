# گسترش دسترسی API از طریق سه دامنه جدید

**تاریخ:** 1404-03-25 / (2025-06-15)

## خلاصه

AvalAI دسترسی به خدمات API خود را از طریق سه دامنه مختلف گسترش داده است تا مشکلات اتصال کاربران را حل کند. این دامنه‌ها شامل دامنه اصلی با CDN داخلی، دامنه ثانویه با CDN داخلی و دامنه جدید با شبکه Cloudflare برای کاربران خارج از کشور می‌باشد.

---

## جزئیات

ما با هدف بهبود تجربه کاربری و حل مشکلات اتصال که برخی از کاربران با آن مواجه بوده‌اند، دسترسی به خدمات API AvalAI را از طریق سه دامنه مختلف فراهم کرده‌ایم.

### دامنه‌های در دسترس

#### 1. دامنه اصلی
- **آدرس**: `api.avalai.ir`
- **CDN**: شبکه توزیع محتوای داخلی
- **بهترین برای**: کاربران داخل کشور با اتصال پایدار

#### 2. دامنه ثانویه
- **آدرس**: `api.avalapis.ir`
- **CDN**: شبکه توزیع محتوای داخلی
- **بهترین برای**: کاربران داخل کشور که با دامنه اصلی مشکل اتصال دارند (تاخیر یا latency در این دامنه بیشتر است)

#### 3. دامنه جدید (جدیدترین)
- **آدرس**: `api.avalai.org`
- **CDN**: شبکه Cloudflare
- **بهترین برای**: کاربران خارج از کشور یا کسانی که به اتصال پایدارتر نیاز دارند

### نحوه استفاده

کاربران می‌توانند بسته به شرایط شبکه خود، از هر یک از این دامنه‌ها استفاده کنند. تمام API endpoint ها و قابلیت‌ها در هر سه دامنه یکسان هستند.

#### مثال Python

```python
import requests

# استفاده از دامنه اصلی
api_url_main = "https://api.avalai.ir/v1/chat/completions"

# استفاده از دامنه ثانویه
api_url_secondary = "https://api.avalapis.ir/v1/chat/completions"

# استفاده از دامنه جدید (Cloudflare)
api_url_cloudflare = "https://api.avalai.org/v1/chat/completions"

headers = {
    "Authorization": "Bearer $AVALAI_API_KEY",
    "Content-Type": "application/json",
}

data = {"model": "gpt-4o", "messages": [{"role": "user", "content": "سلام!"}]}

# انتخاب دامنه مناسب بر اساس موقعیت و شرایط شبکه
response = requests.post(api_url_cloudflare, headers=headers, json=data)
```

#### مثال JavaScript

```javascript
// تنظیم base URL بر اساس موقعیت جغرافیایی
const baseURLs = {
  domestic_primary: "https://api.avalai.ir",
  domestic_secondary: "https://api.avalapis.ir",
  international: "https://api.avalai.org",
};

// انتخاب دامنه مناسب
const selectedBaseURL = baseURLs.international; // برای کاربران خارج از کشور

const response = await fetch(`${selectedBaseURL}/v1/chat/completions`, {
  method: "POST",
  headers: {
    Authorization: "Bearer $AVALAI_API_KEY",
    "Content-Type": "application/json",
  },
  body: JSON.stringify({
    model: "gpt-4o",
    messages: [{ role: "user", content: "سلام!" }],
  }),
});
```

#### مثال cURL

```bash
# دامنه اصلی (CDN داخلی)
curl -X POST "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "messages": [{"role": "user", "content": "سلام!"}]}'

# دامنه ثانویه (CDN داخلی)
curl -X POST "https://api.avalapis.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "messages": [{"role": "user", "content": "سلام!"}]}'

# دامنه جدید (Cloudflare)
curl -X POST "https://api.avalai.org/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-4o", "messages": [{"role": "user", "content": "سلام!"}]}'
```

### توصیه‌های استفاده

#### برای کاربران داخل کشور
1. ابتدا از `api.avalai.ir` استفاده کنید
2. در صورت مشکل اتصال، از `api.avalapis.ir` استفاده کنید
3. اگر هر دو دامنه مشکل داشت، از `api.avalai.org` استفاده کنید

#### برای کاربران خارج از کشور
- از `api.avalai.org` استفاده کنید زیرا از شبکه Cloudflare بهره می‌برد و اتصال پایدارتری فراهم می‌کند

### تست اتصال

برای تست کیفیت اتصال به هر دامنه، می‌توانید از endpoint زیر استفاده کنید:

```bash
# تست دامنه اصلی
curl -I https://api.avalai.ir/public/models

# تست دامنه ثانویه
curl -I https://api.avalapis.ir/public/models

# تست دامنه جدید
curl -I https://api.avalai.org/public/models
```

### نکات مهم

- تمام سه دامنه دارای قابلیت‌ها و API endpoint های یکسان هستند
- کلید API شما در هر سه دامنه قابل استفاده است
- محدودیت‌های نرخ و قیمت‌گذاری در همه دامنه‌ها یکسان است
- امنیت و رمزنگاری در هر سه دامنه در بالاترین سطح حفظ شده است

---

## لینک‌های مرتبط

- [راهنمای شروع سریع](fa/quickstart.md)
- [مرجع API](fa/api-reference/introduction.md)
- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [بهترین شیوه‌های تولید](fa/guides/production-best-practices.md)