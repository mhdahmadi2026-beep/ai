# محدودیت‌های نرخ / Rate limits & account tiers — https://docs.avalai.ir/fa/rate-limits
(Title: «محدودیت نرخ API AvalAI، سطوح حساب و اعتبار رایگان ثبت‌نام»)

Rate limits cap how many API requests you can send in a period (fair use / abuse prevention). AvalAI implements them like OpenAI, with **automatic tier upgrades based on usage**.

## Tiers
Limits grow automatically — first by verifying a phone number, then via cumulative top-ups. **No application form, waiting period or manual approval:** the moment you meet a tier's condition, new limits activate immediately.

### Measured in 5 ways
- **RPM** requests/minute · **RPD** requests/day · **TPM** tokens/minute · **TPD** tokens/day · **IPM** images/minute.
You can hit whichever is reached first (e.g. 20 requests with only 100 tokens can hit RPM even though TPM isn't reached).

### Tier conditions
Tier depends on (1) account verification method — email only vs phone; (2) **cumulative total top-up** over account lifetime.
| Tier | How to reach | Free sign-up credit | Per-tier limits page |
|---|---|---|---|
| Base (Tier 0) | sign up with email only | 25,000 Toman | /fa/rate-limits-tier0 |
| Tier 1 | sign up with phone, or add & verify it later | total 200,000 Toman | /fa/rate-limits-tier1 |
| Tier 2 | cumulative top-up ≈ **$10** | sign-up credit stays until used | /fa/rate-limits-tier2 |
| Tier 3 | cumulative ≈ **$50** | " | /fa/rate-limits-tier3 |
| Tier 4 | cumulative ≈ **$250** | " | /fa/rate-limits-tier4 |
| Tier 5 | cumulative ≈ **$1,000** | " | /fa/rate-limits-tier5 |
Practical notes:
- 🎁 Sign up with phone and verify → up to **200,000 Toman** free API credit; no top-up needed.
- ✉️ Start with email → instant **25,000 Toman** at base tier.
- 📱 Add & verify phone later → **+175,000 Toman** (total 200,000 — not 200,000 on top of email credit) and immediate upgrade to Tier 1.
- ⚡ Upgrades are automatic & instant — no support ticket, no waiting.
- 💳 Top-ups are **cumulative**: tiers ≥2 depend on total historical top-ups, not current balance; **no credit is deducted for upgrading**.
- 💱 Top-ups are in rials; dollar equivalent for tier calculation uses the rate shown at https://chat.avalai.ir/platform. Toman credit is NOT auto-converted to USDT, only its equivalent is checked for tier access. You may convert Toman credit to Tether-equivalent (3% fee) at https://chat.avalai.ir/platform/billing/credit.
- 📈 **No monthly spend cap.** You can use your full credit balance any time.
- 🤖 Each tier unlocks more models and higher per-model limits; limits are defined per model and at org level. Per-model RPM/TPM by tier: use `tier_rate_limits` in `GET https://api.avalai.ir/public/models` (see 06-pricing.md) or the per-tier pages above.

### User API (`/user/v1`) rate limits (per user; your account-tier limit applies on all these endpoints)
| Tier | Requests / minute |
|---|---|
| Base (0) | 3 |
| 1 | 15 |
| 2 | 50 |
| 3 | 150 |
| 4 | 350 |
| 5 | 750 |
See /fa/api-reference/user.

## Rate-limit response headers
| Header | Meaning |
|---|---|
| `x-ratelimit-limit-requests` | max requests allowed in current window |
| `x-ratelimit-remaining-requests` | requests remaining in window |
| `x-ratelimit-reset-requests` | when the request window resets |
| `x-ratelimit-limit-tokens` | max tokens allowed in window |
| `x-ratelimit-remaining-tokens` | tokens remaining |
| `x-ratelimit-reset-tokens` | when the token window resets |

## Handling 429 errors
Exceeding a limit → HTTP **429 Too Many Requests**:
```json
{
  "error": {
    "message": "Rate limit exceeded for requests. Please try again in 30s.",
    "type": "rate_limit_error",
    "param": null,
    "code": "rate_limit_exceeded"
  }
}
```
Response may include `Retry-After: 30` (seconds to wait before retrying).

## Best practices
### Exponential backoff (with jitter, honoring Retry-After)
```python
import os
import random
import time
from openai import OpenAI, RateLimitError

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def with_backoff(call, max_retries=5, initial_delay=1, max_delay=60):
    delay = initial_delay
    for attempt in range(max_retries + 1):
        try:
            return call()
        except RateLimitError as error:
            if attempt == max_retries:
                raise
            retry_after = (
                int(error.headers.get("retry-after", 0)) if error.headers else 0
            )
            delay = max(delay, retry_after)
            sleep_time = delay + random.uniform(0, delay * 0.5)
            print(f"Rate limit exceeded. Retrying in {sleep_time:.2f}s...")
            time.sleep(sleep_time)
            delay = min(delay * 2, max_delay)


completion = with_backoff(
    lambda: client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": "سلام!"}],
    )
)

print(completion.choices[0].message.content)
```
> Skill note: in the openai Python SDK the headers are on `error.response.headers` (`RateLimitError` has no `.headers` attribute in many versions) — use `getattr(error, "response", None)` to read `retry-after` safely.
```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

async function withBackoff(call, maxRetries = 5, initialDelay = 1000, maxDelay = 60000) {
  let delay = initialDelay;

  for (let attempt = 0; attempt <= maxRetries; attempt++) {
    try {
      return await call();
    } catch (error) {
      if (error.status !== 429 || attempt === maxRetries) throw error;

      const retryAfter = error.headers?.["retry-after"]
        ? Number(error.headers["retry-after"]) * 1000
        : 0;
      delay = Math.max(delay, retryAfter);
      const sleepTime = delay + Math.random() * delay * 0.5;
      console.log(`Rate limit exceeded. Retrying in ${sleepTime / 1000}s...`);
      await new Promise((resolve) => setTimeout(resolve, sleepTime));
      delay = Math.min(delay * 2, maxDelay);
    }
  }
}

const completion = await withBackoff(() =>
  client.chat.completions.create({
    model: "gpt-5.6-luna",
    messages: [{ role: "user", content: "سلام!" }],
  }),
);

console.log(completion.choices[0].message.content);
```
```bash
#!/usr/bin/env bash
set -euo pipefail

payload='{"model":"gpt-5.6-luna","messages":[{"role":"user","content":"سلام!"}]}'
delay=1

for attempt in 0 1 2 3 4 5; do
  response=$(curl -sS -w "\n%{http_code}" https://api.avalai.ir/v1/chat/completions \
    -H "Content-Type: application/json" \
    -H "Authorization: Bearer $AVALAI_API_KEY" \
    -d "$payload")
  status="${response##*$'\n'}"
  body="${response%$'\n'*}"

  if [[ $status == "200" ]]; then
    echo "$body"
    break
  fi

  if [[ $status != "429" || $attempt == "5" ]]; then
    echo "$body" >&2
    exit 1
  fi

  echo "Rate limit exceeded. Retrying in ${delay}s..." >&2
  sleep "$delay"
  delay=$((delay * 2 > 60 ? 60 : delay * 2))
done
```
Responses API equivalent (`messages`→`input`, `response.output_text`), same pattern:
```python
response = with_backoff(
    lambda: client.responses.create(model="gpt-5.6-luna", input="سلام!")
)
print(response.output_text)
```
```javascript
const response = await withBackoff(() =>
  client.responses.create({ model: "gpt-5.6-luna", input: "سلام!" }),
);
console.log(response.output_text);
```
```bash
payload='{"model":"gpt-5.6-luna","input":"سلام!"}'   # POST https://api.avalai.ir/v1/responses, same retry loop as above
```

### Client-side limiting — token bucket (Python)
```python
import os
import time
import threading
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


class TokenBucket:
    """Token-bucket algorithm for rate limiting."""

    def __init__(self, tokens_per_second, max_tokens):
        self.tokens_per_second = tokens_per_second
        self.max_tokens = max_tokens
        self.tokens = max_tokens
        self.last_refill_time = time.time()
        self.lock = threading.Lock()

    def get_token(self, tokens=1):
        """Take tokens from the bucket; True if available else False."""
        with self.lock:
            self._refill()
            if self.tokens >= tokens:
                self.tokens -= tokens
                return True
            return False

    def _refill(self):
        """Refill the bucket based on elapsed time."""
        now = time.time()
        elapsed = now - self.last_refill_time
        new_tokens = elapsed * self.tokens_per_second
        if new_tokens > 0:
            self.tokens = min(self.tokens + new_tokens, self.max_tokens)
            self.last_refill_time = now


def make_chat_request(prompt):
    """Chat Completions request with local limiter."""
    while not rate_limiter.get_token():
        time.sleep(0.1)

    return client.chat.completions.create(
        model="gpt-5.6-luna",
        messages=[{"role": "user", "content": prompt}],
    )


def make_responses_request(prompt):
    """Responses API equivalent with the same limiter."""
    while not rate_limiter.get_token():
        time.sleep(0.1)

    return client.responses.create(model="gpt-5.6-luna", input=prompt)


# example: 10 requests/second, max burst 50
rate_limiter = TokenBucket(10, 50)
```

### Batch inputs where possible (e.g. embeddings)
```python
texts = [
    "روباه قهوه‌ای سریع از روی سگ تنبل می‌پرد.",
    "پنج جادوگر بوکسور به سرعت می‌پرند.",
    # ... 8 more texts
]

# one batched request instead of 10 separate ones
response = client.embeddings.create(model="text-embedding-3-small", input=texts)

embeddings = [item.embedding for item in response.data]
```

### Monitor usage via headers
```python
def track_usage(response):
    """Track API usage from response headers."""
    headers = response.headers

    requests_limit = int(headers.get("x-ratelimit-limit-requests", 0))
    requests_remaining = int(headers.get("x-ratelimit-remaining-requests", 0))
    requests_reset = int(headers.get("x-ratelimit-reset-requests", 0))

    tokens_limit = int(headers.get("x-ratelimit-limit-tokens", 0))
    tokens_remaining = int(headers.get("x-ratelimit-remaining-tokens", 0))
    tokens_reset = int(headers.get("x-ratelimit-reset-tokens", 0))

    requests_usage_pct = (
        100 - (requests_remaining / requests_limit * 100) if requests_limit else 0
    )
    tokens_usage_pct = (
        100 - (tokens_remaining / tokens_limit * 100) if tokens_limit else 0
    )

    print(f"Requests: {requests_remaining}/{requests_limit} ({requests_usage_pct:.1f}% used)")
    print(f"Tokens: {tokens_remaining}/{tokens_limit} ({tokens_usage_pct:.1f}% used)")

    if requests_usage_pct > 80 or tokens_usage_pct > 80:
        print("WARNING: API usage is high!")

    return {
        "requests": {"limit": requests_limit, "remaining": requests_remaining,
                     "reset": requests_reset, "usage_pct": requests_usage_pct},
        "tokens": {"limit": tokens_limit, "remaining": tokens_remaining,
                   "reset": tokens_reset, "usage_pct": tokens_usage_pct},
    }


# Chat Completions
raw_response = client.chat.completions.with_raw_response.create(
    model="gpt-5.6-luna", messages=[{"role": "user", "content": "سلام!"}]
)
completion = raw_response.parse()
usage_stats = track_usage(raw_response)
print(completion.choices[0].message.content)

# Responses API
raw_response = client.responses.with_raw_response.create(model="gpt-5.6-luna", input="سلام!")
response = raw_response.parse()
usage_stats = track_usage(raw_response)
print(response.output_text)
```
> Skill note: `int()` on `x-ratelimit-reset-*` can fail if the value is a duration string (e.g. `"1s"`, `"6m0s"`, as in OpenAI) — parse defensively.

### Request queue (high volume)
```python
import queue
import threading
import os
import time
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

request_queue = queue.Queue()


def process_queue():
    """Process queued requests with rate limiting."""
    requests_per_minute = 60  # adjust to your tier
    request_interval = 60 / requests_per_minute

    while True:
        request_func, callback = request_queue.get()

        try:
            result = request_func()
            if callback:
                callback(result, None)
        except Exception as e:
            if callback:
                callback(None, e)
        finally:
            request_queue.task_done()
            time.sleep(request_interval)


def make_chat_request(prompt):
    def request_func():
        return client.chat.completions.create(
            model="gpt-5.6-luna", messages=[{"role": "user", "content": prompt}]
        )

    def callback(result, error):
        if error:
            print(f"Error: {error}")
        else:
            print(f"Response: {result.choices[0].message.content}")

    request_queue.put((request_func, callback))


def make_responses_request(prompt):
    """Responses API equivalent for the same queue."""
    request_queue.put(
        (
            lambda: client.responses.create(model="gpt-5.6-luna", input=prompt),
            lambda result, error: print(error or result.output_text),
        )
    )


queue_thread = threading.Thread(target=process_queue, daemon=True)
queue_thread.start()

for i in range(10):
    make_chat_request(f"Request {i}: Tell me a fact about space")
```

## Strategies by scenario
**Interactive apps:** client-side throttling so users can't flood; loading indicators; cache responses for common queries.
**Batch processing:** ⚠ *"Feature not implemented"* — the (Batch API) capability is under development and not yet available on AvalAI; watch official channels. Meanwhile: schedule jobs off-peak; process in smaller batches to spread requests; retry with increasing delay between batches.
**High availability:** multiple API keys with load balancing; fallback mechanisms when limits hit; keep a token/request budget reserved for critical operations.

## Raising your limits
1. **Verify phone** → instantly Tier 1 (no top-up).
2. **Top up** → Tier 2+ (cumulative; each top-up moves you toward the next tier).
3. **Optimize** the implementation: batching, caching, right-sized model.
4. Check current tier & progress any time in your dashboard.
Upgrades are automatic & instant; **all your credit remains** after each upgrade.

## Conclusion
Limits may change as the API evolves — always consult the latest docs.
