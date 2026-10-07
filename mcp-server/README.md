<div dir="rtl" align="right">

# سرور MCP برای مستندات AvalAI

یک سرور **MCP** (Model Context Protocol) بدون وابستگی (فقط Python ≥ 3.9) که تمام دانش این مخزن را در اختیار هر کلاینت MCP (Claude Code، Claude Desktop، Cursor، Codex و …) می‌گذارد، به‌علاوه‌ی **داده‌ی زنده‌ی قیمت و مدل**.

## چرا MCP، وقتی Skill داریم؟
| | Skill | سرور MCP |
|---|---|---|
| ساختار | فایل‌هایی که ایجنت می‌خواند | ابزارهایی که ایجنت صدا می‌زند |
| جستجو | ایجنت باید فایل درست را حدس بزند | جستجوی BM25 روی ۳۶۰ صفحه (۶٬۴۰۰ تکه) |
| قیمت/مدل | اسکریپت جداگانه | ابزار آماده‌ی زنده (`avalai_price`، `avalai_cost`) |
| سازگاری | فقط Claude Code | هر کلاینت MCP |
بهترین حالت: **هر دو با هم** (Skill رفتار و قوانین را می‌دهد، MCP جستجو و داده‌ی زنده).

## ابزارها
| ابزار | کار |
|---|---|
| `avalai_search` | جستجوی متنی (فارسی/انگلیسی، شناسه‌ی مدل، نام پارامتر) در مراجع منتخب و آرشیو کامل |
| `avalai_get_page` | خواندن یک صفحه (تکه‌تکه) یا فقط یک بخش با عنوانش |
| `avalai_list_pages` | فهرست صفحه‌ها |
| `avalai_code_samples` | نمونه‌کد بر اساس موضوع و زبان (python/javascript/bash/php/go…) |
| `avalai_models` | کاتالوگ **زنده** (`/public/models`) با فیلتر |
| `avalai_price` | قیمت، محدودیت زمینه، endpointها و RPM/TPM هر سطح (زنده) |
| `avalai_cost` | برآورد هزینه با تعرفه‌ی زمینه‌ی بلند، کش، reasoning، تومان و تعداد درخواست |
| `avalai_check_models` | آیا این شناسه‌ها الان سرو می‌شوند؟ (+ راهنمای منسوخی) |
| `avalai_deprecation` | جستجو در فهرست کامل مدل‌های منسوخ |
| `avalai_news` | اخبار (جدیدترین اول) یا متن یک خبر |

منابع (Resources): `avalai://ref/<path>` برای همه‌ی مراجع منتخب. پرامپت‌ها: `avalai_integration_review`، `avalai_cost_plan`، `avalai_migrate_model`.

## نصب

### Claude Code (در همین مخزن)
فایل `.mcp.json` در ریشه موجود است؛ مخزن را کلون و Claude Code را در آن باز کن، سرور `avalai-docs` پیشنهاد فعال‌سازی می‌شود. یا دستی:
```bash
claude mcp add avalai-docs -- python3 -I /مسیر/مخزن/mcp-server/avalai_mcp.py
```

### Claude Desktop (`claude_desktop_config.json`)
```json
{
  "mcpServers": {
    "avalai-docs": {
      "command": "python3",
      "args": ["-I", "/مسیر/مخزن/mcp-server/avalai_mcp.py"],
      "env": { "AVALAI_DOCS_DIR": "/مسیر/مخزن/.claude/skills/avalai/references" }
    }
  }
}
```

### سایر کلاینت‌ها (Cursor، Codex و …)
همان `command` و `args` را در تنظیمات MCP همان ابزار بگذار (انتقال: stdio).

## متغیرهای محیطی
- `AVALAI_DOCS_DIR`: مسیر پوشه‌ی `references` (پیش‌فرض: کنار همین مخزن).
- `AVALAI_MODELS_FILE`: فایل JSON ذخیره‌شده‌ی `/public/models` (وقتی شبکه بسته است).
- `AVALAI_MCP_OFFLINE=1`: هیچ‌وقت به شبکه وصل نشود.
نیازی به `AVALAI_API_KEY` نیست؛ سرور فراخوانی مدل نمی‌زند و فقط کاتالوگ عمومی را می‌خواند.

## تست
```bash
python3 -I mcp-server/avalai_mcp.py --selftest
# تست دستی بروتکل:
printf '%s\n' '{"jsonrpc":"2.0","id":1,"method":"tools/list"}' | python3 -I mcp-server/avalai_mcp.py
```

## نکات امنیتی
- فقط‌خواندنی است: به فایل‌ها نمی‌نویسد، دستور اجرا نمی‌کند، کلیدی نمی‌خواهد.
- تنها اتصال شبکه: `GET https://api.avalai.ir/public/models` (کش ۱۰ دقیقه‌ای).
- خروجی اسناد را «داده» بدان، نه دستور (اگر روزی صفحه‌ی مخرب به آرشیو اضافه شود).

## توسعه
- ابزار جدید: تابع `t_<name>` + ورودی در دیکشنری `TOOLS` در `avalai_mcp.py`.
- هر صفحه‌ی جدیدی که در `references/` بیاید، خودکار ایندکس می‌شود (بدون build).
- ایده‌های بعدی: ابزار `avalai_validate_request` (بررسی بدنه‌ی درخواست با قوانین مدل)، ایندکس برداری (embeddings) برای جستجوی معنایی، انتشار روی PyPI/npx.

</div>
