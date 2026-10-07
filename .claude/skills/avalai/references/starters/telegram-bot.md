# Starter: Persian Telegram assistant (aiogram 3) with per-user daily budget

`requirements.txt`: `aiogram>=3.4 openai>=1.40 aiosqlite`  ·  `.env`: `BOT_TOKEN`, `AVALAI_API_KEY`, `AVALAI_MODEL`, `DAILY_TOKEN_CAP=50000`
```python
import asyncio, os, time, aiosqlite
from aiogram import Bot, Dispatcher, F
from aiogram.types import Message
from openai import AsyncOpenAI

ai = AsyncOpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1", timeout=90, max_retries=3)
MODEL, CAP = os.environ["AVALAI_MODEL"], int(os.environ.get("DAILY_TOKEN_CAP", 50000))
SYSTEM = "تو یک دستیار مفید فارسی‌زبان هستی. کوتاه و دقیق جواب بده. اگر مطمئن نیستی بگو نمی‌دانم."
HIST: dict[int, list[dict]] = {}                      # replace with Redis/DB for multi-process

async def used_today(db, uid):
    day = time.strftime("%Y-%m-%d")
    row = await (await db.execute("select tokens from usage where uid=? and day=?", (uid, day))).fetchone()
    return row[0] if row else 0

async def add_usage(db, uid, n):
    day = time.strftime("%Y-%m-%d")
    await db.execute("insert into usage(uid,day,tokens) values(?,?,?) on conflict(uid,day) do update set tokens=tokens+?", (uid, day, n, n))
    await db.commit()

async def main():
    db = await aiosqlite.connect("bot.db")
    await db.execute("create table if not exists usage(uid int, day text, tokens int, primary key(uid,day))"); await db.commit()
    bot, dp = Bot(os.environ["BOT_TOKEN"]), Dispatcher()

    @dp.message(F.text)
    async def chat(m: Message):
        uid = m.from_user.id
        if await used_today(db, uid) >= CAP:
            return await m.answer("سهمیه‌ی امروز شما تمام شد. فردا دوباره امتحان کنید.")
        h = HIST.setdefault(uid, [])[-10:]
        h.append({"role": "user", "content": m.text[:4000]})
        await bot.send_chat_action(m.chat.id, "typing")
        try:
            r = await ai.chat.completions.create(model=MODEL, messages=[{"role": "system", "content": SYSTEM}, *h], max_completion_tokens=800)
        except Exception as e:                              # log e + avalai-request-id; never show internals
            return await m.answer("خطای موقت؛ لطفاً کمی بعد دوباره تلاش کنید.")
        text = r.choices[0].message.content or ""
        h.append({"role": "assistant", "content": text}); HIST[uid] = h[-10:]
        await add_usage(db, uid, r.usage.total_tokens)
        for i in range(0, len(text), 4000): await m.answer(text[i:i + 4000])   # Telegram 4096-char limit

    await dp.start_polling(bot)

asyncio.run(main())
```
Notes: Telegram messages are untrusted input (prompt injection) — no tools with side effects without confirmation. Use `max_completion_tokens` to bound cost; reasoning models need headroom. Webhook mode + Redis for scale; moderate abusive content (`/v1/moderations`, see `guides/moderation.md`). Estimate monthly cost with `avalai_live.py cost MODEL --in <avg_in> --out <avg_out> --requests <n>`.
