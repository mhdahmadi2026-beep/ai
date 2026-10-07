# درخواست‌های موازی سازگار با Rate Limit

Workerهای موازی برای embeddings، classification، extraction و jobهای batch بسیار مفید هستند. اما بدون throttle می‌توانند خطاهای `429` زیادی ایجاد کنند. این مثال یک الگوی عملی برای backoff، محدود کردن concurrency و pacing درخواست‌ها در AvalAI نشان می‌دهد.

> این راهنما با اقتباس از [OpenAI Cookbook رسمی](https://developers.openai.com/cookbook)، [دفترچه راهنمای rate limit](https://github.com/openai/openai-cookbook/blob/main/examples/How_to_handle_rate_limits.ipynb) و فایل [`api_request_parallel_processor.py`](https://github.com/openai/openai-cookbook/blob/main/examples/api_request_parallel_processor.py)، همراه با تغییرات لازم برای endpoint و کلید API در AvalAI تهیه شده است.

## استراتژی

این سه لایه را با هم استفاده کنید:

- خطاهای `429` و خطاهای موقت server را با exponential backoff و jitter دوباره امتحان کنید.
- تعداد requestهای همزمان را محدود کنید.
- requestها را با فاصله مناسب ارسال کنید تا worker پایین‌تر از RPM و TPM سطح شما بماند.
- وقتی headerهای rate limit در دسترس هستند، آن‌ها را بخوانید و پیش از صفر شدن request یا token سرعت را کم کنید.

## Python: Worker ناهمزمان با Backoff

پیش‌نیاز‌ها را نصب کنید:

```bash
pip install openai
export AVALAI_API_KEY="your-avalai-api-key"
```

```python
import asyncio
import os
import random
from collections.abc import Awaitable, Callable

from openai import AsyncOpenAI, RateLimitError, APIStatusError

client = AsyncOpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


async def with_backoff(
    operation: Callable[[], Awaitable],
    max_retries: int = 6,
    initial_delay: float = 1.0,
    max_delay: float = 60.0,
):
    delay = initial_delay

    for attempt in range(max_retries + 1):
        try:
            return await operation()
        except RateLimitError as exc:
            if attempt == max_retries:
                raise

            retry_after = 0
            if getattr(exc, "headers", None):
                retry_after = float(exc.headers.get("retry-after", 0) or 0)

            sleep_for = max(retry_after, delay) + random.uniform(0, delay * 0.25)
            await asyncio.sleep(sleep_for)
            delay = min(delay * 2, max_delay)
        except APIStatusError as exc:
            if exc.status_code < 500 or attempt == max_retries:
                raise
            await asyncio.sleep(delay + random.uniform(0, delay * 0.25))
            delay = min(delay * 2, max_delay)


async def classify_ticket(ticket: str) -> str:
    async def operation():
        return await client.responses.create(
            model="gpt-5.6-luna",
            instructions=(
                "Classify the ticket as Billing, Technical, Account, or Other. "
                "Return only the label."
            ),
            input=ticket,
        )

    response = await with_backoff(operation)
    return response.output_text.strip()


async def run_batch(tickets: list[str], max_concurrency: int = 5) -> list[str]:
    semaphore = asyncio.Semaphore(max_concurrency)

    async def guarded(ticket: str) -> str:
        async with semaphore:
            return await classify_ticket(ticket)

    return await asyncio.gather(*(guarded(ticket) for ticket in tickets))


if __name__ == "__main__":
    sample_tickets = [
        "I cannot log in after resetting my password.",
        "The invoice total looks wrong.",
        "Webhook delivery fails with a 500 error.",
        "How do I upgrade my tier?",
    ]

    labels = asyncio.run(run_batch(sample_tickets, max_concurrency=3))
    for ticket, label in zip(sample_tickets, labels):
        print(f"{label}: {ticket}")
```

## JavaScript: Concurrency و Retry

```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const sleep = (ms) => new Promise((resolve) => setTimeout(resolve, ms));

async function withBackoff(operation, maxRetries = 6) {
  let delay = 1000;

  for (let attempt = 0; attempt <= maxRetries; attempt += 1) {
    try {
      return await operation();
    } catch (error) {
      const retryable =
        error.status === 429 || (error.status >= 500 && error.status < 600);

      if (!retryable || attempt === maxRetries) throw error;

      const retryAfter = error.headers?.["retry-after"]
        ? Number(error.headers["retry-after"]) * 1000
        : 0;
      const jitter = Math.random() * delay * 0.25;
      await sleep(Math.max(retryAfter, delay) + jitter);
      delay = Math.min(delay * 2, 60000);
    }
  }
}

async function classifyTicket(ticket) {
  const response = await withBackoff(() =>
    client.responses.create({
      model: "gpt-5.6-luna",
      instructions:
        "Classify the ticket as Billing, Technical, Account, or Other. Return only the label.",
      input: ticket,
    }),
  );

  return response.output_text.trim();
}

async function runBatch(items, maxConcurrency = 3) {
  const results = new Array(items.length);
  let nextIndex = 0;

  async function worker() {
    while (nextIndex < items.length) {
      const current = nextIndex;
      nextIndex += 1;
      results[current] = await classifyTicket(items[current]);
    }
  }

  await Promise.all(
    Array.from({ length: maxConcurrency }, () => worker()),
  );

  return results;
}

const tickets = [
  "I cannot log in after resetting my password.",
  "The invoice total looks wrong.",
  "Webhook delivery fails with a 500 error.",
  "How do I upgrade my tier?",
];

console.log(await runBatch(tickets, 3));
```

## Pacing بر اساس Headerها

Backoff بعد از رخ دادن خطا کمک می‌کند. Pacing بر اساس headerها کمک می‌کند با خواندن مقدارهای جدید `x-ratelimit-remaining-*` و `x-ratelimit-reset-*` اصلا به خطا نزدیک نشوید. این کار برای jobهای طولانی مهم است، چون ممکن است request per minute یا token per minute زودتر تمام شود.

```python
import asyncio
import re


def parse_reset_seconds(value: str | None) -> float:
    if not value:
        return 0.0

    total = 0.0
    for amount, unit in re.findall(r"(\d+(?:\.\d+)?)(ms|s|m|h)", value):
        amount = float(amount)
        if unit == "ms":
            total += amount / 1000
        elif unit == "s":
            total += amount
        elif unit == "m":
            total += amount * 60
        elif unit == "h":
            total += amount * 3600

    return total


async def pace_from_headers(headers, floor: int = 2):
    remaining_requests = int(headers.get("x-ratelimit-remaining-requests", floor))
    remaining_tokens = int(headers.get("x-ratelimit-remaining-tokens", floor))

    if remaining_requests <= floor or remaining_tokens <= floor:
        wait_for = max(
            parse_reset_seconds(headers.get("x-ratelimit-reset-requests")),
            parse_reset_seconds(headers.get("x-ratelimit-reset-tokens")),
            1.0,
        )
        await asyncio.sleep(wait_for)


async def classify_ticket_with_headers(ticket: str) -> str:
    raw = await client.responses.with_raw_response.create(
        model="gpt-5.6-luna",
        instructions=(
            "Classify the ticket as Billing, Technical, Account, or Other. "
            "Return only the label."
        ),
        input=ticket,
    )

    await pace_from_headers(raw.headers)
    response = raw.parse()
    return response.output_text.strip()
```

این الگو را وقتی SDK شما response headerها را expose می‌کند، داخل worker استفاده کنید. retry wrapper را همچنان نگه دارید: headerها برای pacing برنامه‌ریزی‌شده مفیدند، اما `Retry-After` و exponential backoff برای burst، رقابت و خطاهای موقت server لازم هستند.

## cURL: احترام به Retry-After

```bash
#!/usr/bin/env bash
set -euo pipefail

payload='{
  "model": "gpt-5.6-luna",
  "instructions": "Classify the ticket as Billing, Technical, Account, or Other. Return only the label.",
  "input": "Webhook delivery fails with a 500 error."
}'

for attempt in 1 2 3 4 5; do
  response_file=$(mktemp)
  headers_file=$(mktemp)

  status=$(curl -sS -o "$response_file" -D "$headers_file" -w "%{http_code}" \
    https://api.avalai.ir/v1/responses \
    -H "Authorization: Bearer $AVALAI_API_KEY" \
    -H "Content-Type: application/json" \
    -d "$payload")

  if [ "$status" = "200" ]; then
    cat "$response_file"
    rm "$response_file" "$headers_file"
    exit 0
  fi

  if [ "$status" != "429" ]; then
    cat "$response_file"
    rm "$response_file" "$headers_file"
    exit 1
  fi

  retry_after=$(awk 'tolower($1)=="retry-after:" {print $2}' "$headers_file" | tr -d '\r')
  sleep_for=${retry_after:-$((attempt * attempt))}
  sleep "$sleep_for"

  rm "$response_file" "$headers_file"
done

echo "Request failed after retries" >&2
exit 1
```

## چک‌لیست Throughput

- حاشیه امن بگذارید: ۵۰ تا ۷۵ درصد RPM و TPM مستندشده سطح خود را هدف بگیرید.
- هم requestها و هم tokenها را track کنید؛ ممکن است یکی تمام شود و دیگری هنوز ظرفیت داشته باشد.
- برای workerهای طولانی از pacing بر اساس header استفاده کنید تا پیش از رسیدن به `429` سرعت کم شود.
- اگر `Retry-After` وجود داشت به آن احترام بگذارید؛ در غیر این صورت exponential backoff همراه با jitter استفاده کنید.
- وقتی پاسخ‌های کوتاه انتظار دارید، `max_output_tokens` را پایین‌تر بگذارید.
- برای classificationهای کوچک، وقتی latency اولویت اصلی نیست، چند task را batch کنید.
- نتیجه‌های partial را در طول مسیر ذخیره کنید تا job طولانی بعد از interruption قابل ادامه باشد.
- request ID و body خطا را در logها نگه دارید تا پشتیبانی و debugging ساده‌تر شود.

## لینک‌های مرتبط

- [محدودیت‌های نرخ](fa/guides/rate-limits.md)
- [هدرهای پاسخ](fa/api-reference/response-headers.md)
- [مدیریت خطا](fa/guides/error-handling.md)
- [بهترین شیوه‌های Production](fa/guides/production-best-practices.md)
