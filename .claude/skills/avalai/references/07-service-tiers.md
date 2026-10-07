# سطوح سرویس / Service Tiers — https://docs.avalai.ir/fa/service-tiers

AvalAI service tiers let you trade cost vs performance per request. Default = best balance of speed and reliability. Full cost playbook (service tier + model choice + token budget + prompt caching + async jobs): /fa/guides/cost-optimization

## Comparison
| Tier | Description | Latency | Pricing | Credit-package coverage |
|---|---|---|---|---|
| `default` (recommended) | standard tier for production & interactive requests | low | standard rates | ✅ yes |
| `flex` (50% cheaper) | cost-optimized, higher latency | high (up to 15 min) | **50% discount** | ❌ no |
Best for: default → production & interactive; flex → batch & cost optimization.

> **OpenAI compatibility note:** OpenAI public docs also describe `service_tier: "auto"` and `"priority"`. On AvalAI the public, available values are **`default` and `flex`**. If porting an OpenAI sample with `"priority"` (or project-level priority settings), use `"default"` unless priority tier is explicitly enabled for your account. For fallback from flex, omit `service_tier` or set `"default"` → standard AvalAI processing path.

### Porting OpenAI `service_tier` samples
In OpenAI's Responses/Chat references the response contains the **actual** `service_tier` used, which may differ from requested (project-level setting, capacity fallback, priority ramp limits). Treat AvalAI's returned `service_tier` the same: **log it with `avalai-request-id`, endpoint, model, latency, token usage and final cost** so support/billing can show whether a request ran on `default` or `flex`.
When adapting OpenAI samples:
- Replace `OPENAI_API_KEY` → `AVALAI_API_KEY`; `https://api.openai.com/v1` → `https://api.avalai.ir/v1`.
- Keep `service_tier: "flex"` only for supported OpenAI-family models and workloads tolerating longer latency or retry when capacity is unavailable.
- Don't copy `service_tier: "priority"` into AvalAI examples unless priority processing is enabled for the account.
- For flex jobs raise SDK timeouts; retry idempotent work with exponential backoff or controlled fallback to default.

## `default` tier
Default for all API requests: standard processing on AvalAI's default production path; lower latency than flex; all models available; **credit-package coverage**; recommended for production, time-sensitive and interactive use. No need to specify; explicit form:
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.4",
    "messages": [{"role": "user", "content": "سلام!"}],
    "service_tier": "default"
  }'
```
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.chat.completions.create(
    model="gpt-5.4",
    messages=[{"role": "user", "content": "سلام!"}],
    service_tier="default",  # optional, this is the default
)
print(response.choices[0].message.content)
```
```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "gpt-5.4",
  messages: [{ role: "user", content: "سلام!" }],
  service_tier: "default"  // optional, this is the default
});
console.log(response.choices[0].message.content);
```
```go
package main

import (
	"context"
	"fmt"
	"os"

	openai "github.com/sashabaranov/go-openai"
)

func main() {
	config := openai.DefaultConfig(os.Getenv("AVALAI_API_KEY"))
	config.BaseURL = "https://api.avalai.ir/v1"
	client := openai.NewClientWithConfig(config)

	resp, err := client.CreateChatCompletion(
		context.Background(),
		openai.ChatCompletionRequest{
			Model: "gpt-5.4",
			Messages: []openai.ChatCompletionMessage{
				{Role: "user", Content: "سلام!"},
			},
			// service_tier defaults to "default"
		},
	)
	if err != nil {
		fmt.Printf("error: %v\n", err)
		return
	}
	fmt.Println(resp.Choices[0].Message.Content)
}
```
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
    'model' => 'gpt-5.4',
    'messages' => [
        ['role' => 'user', 'content' => 'سلام!']
    ],
    'service_tier' => 'default'  // optional, this is the default
];

$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($data));
curl_setopt($ch, CURLOPT_HTTPHEADER, [
    'Content-Type: application/json',
    'Authorization: Bearer ' . $apiKey
]);

$response = curl_exec($ch);
curl_close($ch);

$result = json_decode($response, true);
echo $result['choices'][0]['message']['content'];
```
### Responses API equivalent (messages → `input`, text via `response.output_text`)
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4", "input": "سلام!", "service_tier": "default"}'
```
```python
response = client.responses.create(model="gpt-5.4", input="سلام!", service_tier="default")
print(response.output_text)
```
```javascript
const response = await client.responses.create({
  model: "gpt-5.4",
  input: "سلام!",
  service_tier: "default"
});
console.log(response.output_text);
```

## `flex` tier
**50% cost reduction** for selected OpenAI models, in exchange for much higher latency and possible delays.
> ⚠ Much higher latency than standard: slower processing; **server timeout up to 900 s (15 min)**; may time out or fail mid-processing; **no credit-package coverage**. Recommended for batch processing, non-time-sensitive jobs, cost optimization at high volume.

### Supported models (flex works ONLY for these OpenAI models; others → error)
| Model | Aliases |
|---|---|
| `gpt-5.5` | – |
| `gpt-5.4-pro` | – |
| `gpt-5.4` | – |
| `gpt-5.4-mini` | – |
| `gpt-5.4-nano` | – |
| `gpt-5.2-chat` | – |
| `gpt-5.2` | `gpt-5.2-2025-12-11` |
| `gpt-5.1` | `gpt-5.1-2025-11-13` |
| `gpt-5` | `gpt-5-2025-08-07` |
| `gpt-5-mini` | `gpt-5-mini-2025-08-07` |
| `gpt-5-nano` | `gpt-5-nano-2025-08-07` |
| `o3` | – |
| `o4-mini` | – |

### Flex pricing (USD per 1M tokens = 50% of standard)
| Model | Input | Cached input | Output |
|---|---|---|---|
| `gpt-5.5` | $2.50 | $0.25 | $15.00 |
| `gpt-5.4-pro` | $15.00 | N/A | $90.00 |
| `gpt-5.4` | $1.25 | $0.13 | $7.50 |
| `gpt-5.4-mini` | $0.375 | $0.0375 | $2.25 |
| `gpt-5.4-nano` | $0.10 | $0.01 | $0.625 |
| `gpt-5.2-chat` | $0.875 | $0.0875 | $7.00 |
| `gpt-5.2` | $0.875 | $0.0875 | $7.00 |
| `gpt-5.1` | $0.625 | $0.0625 | $5.00 |
| `gpt-5` | $0.625 | $0.0625 | $5.00 |
| `gpt-5-mini` | $0.125 | $0.0125 | $1.00 |
| `gpt-5-nano` | $0.025 | $0.0025 | $0.20 |
| `o3` | $1.00 | $0.25 | $4.00 |
| `o4-mini` | $0.55 | $0.138 | $2.20 |
Full pricing: 06-pricing.md (/fa/pricing#flex).

### Using flex: add `"service_tier": "flex"`
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5-mini",
    "messages": [{"role": "user", "content": "این سند را خلاصه کن..."}],
    "service_tier": "flex"
  }'
```
```python
response = client.chat.completions.create(
    model="gpt-5-mini",
    messages=[{"role": "user", "content": "این سند را خلاصه کن..."}],
    service_tier="flex",
)
print(response.choices[0].message.content)
print(f"service tier used: {response.service_tier}")
```
```javascript
const response = await client.chat.completions.create({
  model: "gpt-5-mini",
  messages: [{ role: "user", content: "این سند را خلاصه کن..." }],
  service_tier: "flex"
});
console.log(response.choices[0].message.content);
console.log(`service tier used: ${response.service_tier}`);
```
```go
// as published: go-openai (sashabaranov); the page's snippet only has a comment
// "set service_tier to flex" and does NOT actually set a field — go-openai's
// ChatCompletionRequest may not expose ServiceTier in older versions; use raw HTTP if so.
resp, err := client.CreateChatCompletion(
	context.Background(),
	openai.ChatCompletionRequest{
		Model: "gpt-5-mini",
		Messages: []openai.ChatCompletionMessage{
			{Role: "user", Content: "این سند را خلاصه کن..."},
		},
	},
)
```
```php
$data = [
    'model' => 'gpt-5-mini',
    'messages' => [['role' => 'user', 'content' => 'این سند را خلاصه کن...']],
    'service_tier' => 'flex'
];
// ... same curl boilerplate as default; read $result['service_tier']
```
Responses API:
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5-mini", "input": "این سند را خلاصه کن...", "service_tier": "flex"}'
```
```python
response = client.responses.create(model="gpt-5-mini", input="این سند را خلاصه کن...", service_tier="flex")
print(response.output_text)
print(f"service tier used: {response.service_tier}")
```
```javascript
const response = await client.responses.create({
  model: "gpt-5-mini",
  input: "این سند را خلاصه کن...",
  service_tier: "flex"
});
console.log(response.output_text);
console.log(`service tier used: ${response.service_tier}`);
```

### Response format — every response carries `service_tier`
```json
{
  "id": "chatcmpl-123",
  "created": 1765789075,
  "model": "gpt-5-mini-2025-08-07",
  "object": "chat.completion",
  "choices": [
    {"finish_reason": "stop", "index": 0, "message": {"content": "این خلاصه است...", "role": "assistant"}}
  ],
  "usage": {"completion_tokens": 150, "prompt_tokens": 50, "total_tokens": 200},
  "service_tier": "flex",
  "estimated_cost": {"unit": "0.0001875000", "irt": 24.63, "exchange_rate": 131350}
}
```

## Error handling
### Unsupported model
```bash
curl -i https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "claude-sonnet-5", "messages": [{"role": "user", "content": "سلام"}], "service_tier": "flex"}'
```
```json
{
  "error": {
    "message": "Model 'claude-sonnet-4-6' does not support service_tier='flex'. Flex tier is only available for supported OpenAI models such as gpt-5.5, gpt-5.4, gpt-5.4-mini, gpt-5, gpt-5-mini, gpt-5-nano, o3, and o4-mini. See https://docs.avalai.ir/fa/service-tiers for more information.",
    "type": "invalid_request",
    "param": null,
    "code": "invalid_request",
    "request_id": "019b214f-4f5d-7321-8a3a-59f89d473c7c"
  }
}
```
(The docs' request uses `claude-sonnet-5` but the sample message names `claude-sonnet-4-6` — inconsistency in source. Error shape: `error.{message,type,param,code,request_id}`; type/code `invalid_request`.)

### Retry with fallback to default (recommended in production)
```python
import os
from openai import OpenAI
import time

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def make_request_with_fallback(messages, model="gpt-5-mini", max_retries=3):
    """Try flex first, fall back to standard on failure."""
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            service_tier="flex",
            timeout=900,  # 15-minute timeout for flex
        )
        return response, "flex"
    except Exception as e:
        print(f"flex failed: {e}. Falling back to standard tier...")

    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model=model, messages=messages, service_tier="default"
            )
            return response, "default"
        except Exception as e:
            if attempt < max_retries - 1:
                time.sleep(2**attempt)  # exponential backoff
            else:
                raise e


messages = [{"role": "user", "content": "سلام!"}]
response, tier_used = make_request_with_fallback(messages)
print(f"response received using tier {tier_used}")
```
```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

async function makeRequestWithFallback(messages, model = "gpt-5-mini", maxRetries = 3) {
  try {
    const response = await client.chat.completions.create({
      model: model,
      messages: messages,
      service_tier: "flex"
    }, { timeout: 900000 }); // 15-minute timeout for flex
    return { response, tierUsed: "flex" };
  } catch (error) {
    console.log(`flex failed: ${error.message}. Falling back to standard tier...`);
  }

  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await client.chat.completions.create({
        model: model,
        messages: messages,
        service_tier: "default"
      });
      return { response, tierUsed: "default" };
    } catch (error) {
      if (attempt < maxRetries - 1) {
        await new Promise(resolve => setTimeout(resolve, Math.pow(2, attempt) * 1000));
      } else {
        throw error;
      }
    }
  }
}

const messages = [{ role: "user", content: "سلام!" }];
const { response, tierUsed } = await makeRequestWithFallback(messages);
console.log(`response received using tier ${tierUsed}`);
```
Responses API variants:
```python
def make_response_with_fallback(prompt, model="gpt-5-mini", max_retries=3):
    try:
        response = client.responses.create(model=model, input=prompt, service_tier="flex", timeout=900)
        return response, "flex"
    except Exception as error:
        print(f"flex failed: {error}. Falling back to standard tier...")

    for attempt in range(max_retries):
        try:
            response = client.responses.create(model=model, input=prompt, service_tier="default")
            return response, "default"
        except Exception:
            if attempt < max_retries - 1:
                time.sleep(2**attempt)
            else:
                raise


response, tier_used = make_response_with_fallback("سلام!")
print(response.output_text)
```
```javascript
async function makeResponseWithFallback(prompt, model = "gpt-5-mini", maxRetries = 3) {
  try {
    const response = await client.responses.create({ model, input: prompt, service_tier: "flex" }, { timeout: 900000 });
    return { response, tierUsed: "flex" };
  } catch (error) {
    console.log(`flex failed: ${error.message}. Falling back to standard tier...`);
  }
  for (let attempt = 0; attempt < maxRetries; attempt++) {
    try {
      const response = await client.responses.create({ model, input: prompt, service_tier: "default" });
      return { response, tierUsed: "default" };
    } catch (error) {
      if (attempt < maxRetries - 1) {
        await new Promise((resolve) => setTimeout(resolve, Math.pow(2, attempt) * 1000));
      } else {
        throw error;
      }
    }
  }
}
```

## Best practices
**Use `default` for:** interactive apps (chatbots, real-time assistants, UIs); time-sensitive work; production workflows where reliability is critical; when you want credit packages to cover costs; **migrating from OpenAI Priority** when the upstream sample has `service_tier: "priority"` and priority isn't enabled on your AvalAI account.
**Use `flex` for:** batch processing; background jobs (scheduled work, data analysis, content generation); cost optimization when you can tolerate delays; non-production workloads (testing, dev, experiments).
**Hybrid:** `default` for user-facing/time-sensitive; `flex` for background/batch/cost-sensitive; implement fallback flex → default on failure/timeout.
**About Priority processing:** OpenAI Priority is for user-facing high-value traffic needing lower, steadier latency than standard; not a replacement for offline data processing, evals, or batch/spiky workloads. In AvalAI docs/examples don't send `service_tier: "priority"` unless your account & route explicitly support it; use `default` for latency-sensitive production, `flex` only for cost-sensitive jobs that tolerate slower or temporarily unavailable capacity.

## Credit packages and service tiers
> ⚠ **Credit packages cover ONLY standard-tier usage.** With `service_tier: "flex"`, cost is deducted from your standard account balance, not from credit-package allocation. More: 08-credit-packages.md (/fa/credit-packages).

## API reference
`service_tier` is supported on: Chat Completions (/fa/api-reference/chat) and Responses (/fa/api-reference/responses).

## Related
/fa/pricing · /fa/credit-packages · /fa/guides/production-best-practices (observability & fallback planning for service tiers) · /fa/api-reference/chat · /fa/api-reference/responses · /fa/guides/error-handling

## ⚠ Consistency notes
- Flex supported-model list (here) is **larger** than the flex price table on the pricing page (06-pricing.md lists only gpt-5.2/5.1/5/mini/nano/o3/o4-mini). This page (service-tiers) has the newer list incl. gpt-5.5, 5.4 family, 5.2-chat. Prefer this page; if a flex request is rejected, fall back to default.
- The error-message example enumerates only some supported models; the table above is authoritative.
- `gpt-5.4-pro` flex cached input price: N/A.
