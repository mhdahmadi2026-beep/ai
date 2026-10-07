<div dir="rtl" align="right">

# اسکیل AvalAI برای Claude Code و ایجنت‌های هوش مصنوعی

یک **مرجع کامل و ساخت‌یافته از مستندات AvalAI** (درگاه سازگار با OpenAI در `https://api.avalai.ir/v1`) که به شکل **Skill** برای [Claude Code](https://claude.com/claude-code) ساخته شده است؛ تا ایجنت هنگام توسعه، مثل یک متخصص AvalAI رفتار کند: مدل درست انتخاب کند، قیمت را حساب کند، کد استاندارد بنویسد و در دام مدل‌های منسوخ یا نمونه‌کدهای خراب مستندات نیفتد.

> این پروژه **رسمی AvalAI نیست**. محتوا از صفحه‌های مستندات (https://docs.avalai.ir/fa/) بازنویسی و خلاصه شده و جاهایی که صفحه‌ی منبع خطا دارد، همان‌جا یادداشت شده است. **قیمت‌ها، شناسه‌ی مدل‌ها و محدودیت‌ها همیشه باید زنده بررسی شوند** (پایین‌تر توضیح داده شده).

## ویژگی‌ها
- **Playbook ایجنت** در ابتدای `SKILL.md`: پروتکل ۵ مرحله‌ای، جدول «کار ← فایل مرجع» و فهرست اشتباه‌های رایج.
- **ابزار زنده‌ی قیمت و هزینه** (`avalai_live.py`، بدون وابستگی و بدون نیاز به کلید): بررسی وجود مدل، قیمت، محدودیت هر سطح و محاسبه‌ی هزینه (تعرفه‌ی زمینه‌ی بلند، توکن کش‌شده، reasoning، تبدیل به تومان).
- **مرجع API**: Responses، Chat Completions، Messages، Images، Videos، Audio، Embeddings، Moderation، Rerank، Search، OCR، Files، User API، هدرهای پاسخ، `v1beta` (Gemini بومی).
- **راهنماها** (بیش از ۸۰ فایل): استدلال، ابزارها، خروجی ساختاریافته، استریم، کش پرامپت، RAG، ارزیابی، امنیت، سیاست محتوا، حریم خصوصی، وضعیت سرویس، راه‌اندازی ابزارها (Claude Code، Codex، Aider، OpenCode، VS Code، n8n، Open WebUI، 9Router، Hermes).
- **ارائه‌دهندگان و مدل‌ها**: OpenAI، Anthropic، Google، xAI، DeepSeek، Mistral، Meta، Alibaba و … همراه با جدول قیمت و محدودیت هر سطح حساب (T0 تا T5).
- **منسوخ‌شده‌ها و مهاجرت**: فهرست مدل‌های حذف‌شده با جایگزین پیشنهادی.
- **اخبار تاریخ‌دار** (۲۰۲۵ تا اکتبر ۲۰۲۶): مدل‌های جدید، تغییر هدر `avalai-request-id`، تعرفه‌ی DeepSeek، مسیریابی کش و …
- **مثال‌های عملی**: PDF، اکسل، صوت، OCR، تولید تصویر (Nano Banana، Seedream، GPT Image)، رباتیک، جلسه‌ی چندگوینده، RAG، حافظه‌ی پایدار، ارزیابی با promptfoo و …
- **کلاینت‌های چندزبانه**: PHP، Go، Java، C#، Ruby، Rust، Node (fetch)، cURL، با retry، timeout و ثبت شناسه‌ی درخواست.
- **اسکریپت‌های آماده**: guardrail تغییر اسکیما، تحلیل جلسه با تفکیک گوینده، حافظه‌ی پایدار، بنچمارک تأخیر و … (اجرای `--selftest` در دسترس برخی از آن‌ها).

## سرور MCP و ایندکس معنایی
پوشه‌ی `mcp-server/` یک سرور MCP بدون وابستگی است (جستجوی ترکیبی BM25 + embeddings، قیمت/هزینه‌ی زنده، نمونه‌کد، فهرست منسوخ‌ها، اخبار و پروژه‌های آماده). راهنمای کامل: [`mcp-server/README.md`](mcp-server/README.md). فایل `.mcp.json` برای Claude Code آماده است.

## پروژه‌های آماده (Starters)
بلوپرینت‌های کامل در `.claude/skills/avalai/references/starters/`: چت+RAG با FastAPI، چت استریم با Next.js، ربات تلگرام فارسی، چت Laravel، ایجنت CLI با Node، OCR→JSON، دستیار صوتی.

## نصب

### Claude Code (پیشنهادی)
پوشه‌ی اسکیل را در پروژه‌ات کپی کن:

```bash
git clone https://github.com/mhdahmadi2026-beep/ai.git /tmp/avalai-skill
mkdir -p .claude/skills
cp -r /tmp/avalai-skill/.claude/skills/avalai .claude/skills/
```

برای همه‌ی پروژه‌ها: به‌جای `.claude/skills` از `~/.claude/skills` استفاده کن. Claude Code به‌صورت خودکار اسکیل را با نام `avalai` می‌شناسد و وقتی کار به AvalAI، `api.avalai.ir` یا `AVALAI_API_KEY` مربوط شود، آن را فعال می‌کند.

### ایجنت‌های دیگر (Cursor، Codex، Aider و …)
فایل `AGENTS.md` در ریشه‌ی مخزن ایجنت را به اسکیل هدایت می‌کند. در غیر این صورت به ایجنت بگو `.claude/skills/avalai/SKILL.md` و `references/00-index.md` را بخواند.

## استفاده‌ی سریع

۱. کلید API را در محیط تنظیم کن (هرگز در کد کلاینت/مرورگر نگذار):

```bash
export AVALAI_API_KEY="..."
```

۲. اولین فراخوانی با Responses API:

```python
import os
from openai import OpenAI

client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
r = client.responses.create(model="gpt-6-astra", input="یک ایده‌ی کاربردی برای ابزار توسعه‌دهندگان بده.")
print(r.output_text)
```

۳. قبل از ذکر هر قیمت یا شناسه‌ی مدل، **زنده** بررسی کن:

```bash
S=.claude/skills/avalai/references/scripts/avalai_live.py
python3 -I $S check gpt-6.1-sol claude-sonnet-5-5          # مدل‌ها هنوز سرو می‌شوند؟
python3 -I $S price gpt-6.1-sol                            # قیمت + محدودیت هر سطح
python3 -I $S models --grep claude --mode chat --tier 1    # فهرست مدل‌ها
python3 -I $S cost gpt-6.1-sol --in 300000 --out 2000 --requests 1000 --rate 100000
python3 -I $S snapshot --out live-snapshot.md              # خروجی Markdown از کل کاتالوگ
```
(`--rate` نرخ **امروز** تومان به ازای هر دلار است؛ روزانه تغییر می‌کند. اگر شبکه بسته بود، JSON را از `https://api.avalai.ir/public/models` ذخیره کن و با `--file models.json` استفاده کن.)

## ساختار پوشه
```
.claude/skills/avalai/
├─ SKILL.md                  # Playbook ایجنت + قوانین کاری (بخوان: START HERE)
├─ README.md
└─ references/
   ├─ 00-index.md            # نقشه‌ی همه‌ی صفحه‌ها و وضعیت ثبت
   ├─ 01…11-*.md             # مقدمه، کوییک‌استارت، کتابخانه‌ها، قیمت، سطوح، اعتبار، محدودیت‌ها، منسوخ‌ها
   ├─ api-reference/         # مرجع API
   ├─ guides/                # راهنماها
   ├─ providers/  models/    # ارائه‌دهندگان و مدل‌ها
   ├─ examples/              # مثال‌ها (شامل multi-language-clients.md)
   ├─ news/                  # اخبار تاریخ‌دار
   ├─ resellers/             # راهنمای نمایندگان فروش و ردیابی هزینه
   ├─ scripts/               # avalai_live.py و اسکریپت‌های کمکی
   └─ MISSING-PAGES.md       # صفحه‌هایی که هنوز ثبت نشده‌اند
```

## اصول کاری اسکیل (خلاصه)
- **داده‌ی زنده > حافظه**: قیمت، سطح دسترسی، محدودیت و پشتیبانی endpoint در هر مدل تغییر می‌کنند؛ اول `avalai_live.py`.
- **پایه‌ی آدرس**: OpenAI SDK → `https://api.avalai.ir/v1` ؛ Anthropic و Google SDK → `https://api.avalai.ir` (**بدون** `/v1`).
- **هزینه‌ی دقیق**: شناسه‌ی `avalai-request-id` را ذخیره کن و ~۳۰ ثانیه بعد با `POST /user/v1/transactions/lookup` هزینه‌ی واقعی را بگیر (فیلد `cost.unit`). از ۱۵ اکتبر ۲۰۲۶ هدر `x-request-id` دیگر برگردانده نمی‌شود.
- **تولید حرفه‌ای**: timeout صریح، retry فقط برای 429/5xx با `Retry-After` و jitter، اعتبارسنجی آرگومان ابزارها، تأیید انسانی قبل از اقدام‌های جانبی، و بدون کلید در سمت کاربر.
- **ایجنت‌ها**: ابتدا فایل مرجع مناسب را بخوانند؛ اگر چیزی در فایل‌ها «snapshot/PENDING/تضاد» علامت خورده، زنده تأیید کنند یا از کاربر بپرسند.

## محدودیت‌ها و صداقت
- AvalAI این‌ها را ارائه **نمی‌دهد** (طبق مستندات): vector store/file_search میزبانی‌شده، endpoint شمارش توکن، Batch میزبانی‌شده، Realtime، Assistants، fine-tuning و کنترل صریح prompt caching. ابزارهای میزبانی‌شده بسته به مدل و مسیر متفاوتند.
- بعضی نمونه‌کدهای مستندات منبع خطا دارند (مثلاً SDKهای ساختگی یا فیلدهای غلط)؛ در فایل‌های مرجع علامت‌گذاری شده‌اند.
- نمونه‌کدهای نوشته‌شده توسط خود اسکیل (مثلاً چندزبانه) روی API واقعی اجرا نشده‌اند؛ قبل از پروداکشن تست کن.
- تعدادی صفحه هنوز ثبت نشده است؛ فهرستشان در `references/MISSING-PAGES.md`.

## مشارکت و به‌روزرسانی
- صفحه‌ی جدید یا تغییر مستندات؟ متن صفحه را به ایجنت بده تا مرجع مربوط را به‌روز کند و ردیف `00-index.md` و قوانین `SKILL.md` را هم تغییر دهد.
- قبل از ثبت قیمت در فایل‌ها، تاریخ و منبع را بنویس؛ عددهای گذرا (مثل تعرفه‌ی تشویقی) را با تاریخ پایان ثبت کن.

## مجوز
محتوای مستندات متعلق به AvalAI است و این مخزن فقط خلاصه و راهنمای کاربردی آن را برای توسعه‌ی کمک‌شده با ایجنت نگه می‌دارد. اسکریپت‌ها و نمونه‌های نوشته‌شده توسط این پروژه برای استفاده‌ی آزاد هستند؛ قبل از انتشار گسترده، مجوز دلخواه خودت را (مثلاً MIT) اضافه کن.

</div>
