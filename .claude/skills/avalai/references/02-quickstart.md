# شروع سریع / Quickstart — https://docs.avalai.ir/fa/quickstart

Recommended first-run path:
1. Install an SDK. 2. Set `AVALAI_API_KEY`. 3. Pick API style: `/v1/responses` for new text/reasoning/tool apps; `/v1/chat/completions` for existing chat integrations & widest provider compatibility. 4. Send first request, then use `/v1/models` and `avalai-request-id` for model discovery and cost tracking.

## 1. API key
1. Create an account in the dashboard https://chat.avalai.ir/platform/home
2. Go to API keys section. 3. Create a new key. 4. **Store it safely — shown only once.**
Set env var before running examples; keep it in shell profile / secret manager / deployment env. **Never** put it in source code, screenshots, issue reports, or browser-side JavaScript.
```bash
# macOS / Linux
export AVALAI_API_KEY="sk-..."
```
```powershell
# Windows PowerShell
setx AVALAI_API_KEY "sk-..."
```
Open a new terminal (or reload profile) afterwards.

## 2. Install & configure client
Three SDK approaches:
| Approach | Description |
|---|---|
| OpenAI-compatible SDKs | **Unified** — all models from many providers with the same syntax |
| Official Anthropic SDKs | **Native** — access Anthropic, OpenAI, AWS Bedrock, Vertex AI, Gemini models with native syntax |
| Google GenAI SDK | **Native** — Gemini models with Google's native API schema |
Read /fa/libraries before choosing a provider-native integration.

Install:
```bash
pip install openai                         # Python
npm install openai                         # Node.js
go get github.com/openai/openai-go         # Go
composer require openai-php/client         # PHP
```

### Base URL
AvalAI offers multiple domains for best connectivity by location/network. Doc lists:
1. **Main domain (recommended)** — `api.avalai.ir`, global CDN, best for optimal performance/lowest latency.
All endpoints/capabilities are identical across domains.

### Client configuration
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
```
```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});
```
```go
package main

import (
	openai "github.com/openai/openai-go"
	"os"
)

func main() {
	client := openai.NewClient(os.Getenv("AVALAI_API_KEY"))
	client.BaseURL = "https://api.avalai.ir/v1"
}
```
> Skill note: the Go snippet above is copied as published; the openai-go API differs by version (it normally uses `option.WithAPIKey/WithBaseURL`). Verify against the installed SDK version.
```php
<?php
require_once 'vendor/autoload.php';

// openai-php/client (https://github.com/openai-php/client)
$apiKey = getenv('AVALAI_API_KEY');
if (!$apiKey) {
    die("AvalAI API key not found. Please set the AVALAI_API_KEY environment variable.");
}
$customBaseUrl = 'https://api.avalai.ir/v1';

$client = OpenAI::factory()
    ->withApiKey($apiKey)
    ->withBaseUri($customBaseUrl)
    ->make();
```

## 3. Choose API style
Prefer `/v1/responses` for new text generation when the chosen model supports it: uses `input`, final text in `response.output_text`, better for conversation state, reasoning and tools. Keep `/v1/chat/completions` for existing apps, broader provider coverage, and SDKs/frameworks that still require `messages`.
- Responses API → /fa/api-reference/responses (recommended for new apps: reasoning, structured output, tools)
- Chat Completions → /fa/api-reference/chat (existing chat integrations; chat-only models)
- Migration guide → /fa/guides/responses-vs-chat-completions (map `messages`→`input`, read `output_text`, choose state management)

## 4. First request
### Responses API (recommended)
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-5.6-luna",
    "instructions": "You are a helpful assistant.",
    "input": "سلام، دنیا!"
  }'
```
```python
response = client.responses.create(
    model="gpt-5.6-luna",
    instructions="You are a helpful assistant.",
    input="سلام، دنیا!",
)
print(response.output_text)
```
```javascript
const response = await client.responses.create({
  model: "gpt-5.6-luna",
  instructions: "You are a helpful assistant.",
  input: "سلام، دنیا!",
});
console.log(response.output_text);
```
```go
package main

import (
	"bytes"
	"encoding/json"
	"fmt"
	"io"
	"net/http"
	"os"
)

func main() {
	payload := map[string]any{
		"model":        "gpt-5.6-luna",
		"instructions": "You are a helpful assistant.",
		"input":        "سلام، دنیا!",
	}
	body, _ := json.Marshal(payload)
	req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1/responses", bytes.NewBuffer(body))
	req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
	req.Header.Set("Content-Type", "application/json")

	resp, err := http.DefaultClient.Do(req)
	if err != nil {
		panic(err)
	}
	defer resp.Body.Close()
	responseBody, _ := io.ReadAll(resp.Body)
	fmt.Println(string(responseBody))
}
```
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$payload = [
    'model' => 'gpt-5.6-luna',
    'instructions' => 'You are a helpful assistant.',
    'input' => 'سلام، دنیا!',
];
$ch = curl_init('https://api.avalai.ir/v1/responses');
curl_setopt_array($ch, [
    CURLOPT_RETURNTRANSFER => true,
    CURLOPT_POST => true,
    CURLOPT_HTTPHEADER => [
        'Authorization: Bearer ' . $apiKey,
        'Content-Type: application/json',
    ],
    CURLOPT_POSTFIELDS => json_encode($payload),
]);
$response = curl_exec($ch);
curl_close($ch);
echo $response;
```

### Required headers & rate limiting
- Every authenticated request: `Authorization: Bearer $AVALAI_API_KEY`; JSON bodies: `Content-Type: application/json`.
- On HTTP `429`: honor `Retry-After`, use exponential backoff **with jitter** and a max retry cap; never retry immediately. See /fa/rate-limits.

### Chat Completions (existing integrations / chat-only models)
```python
completion = client.chat.completions.create(
    model="gpt-5.6-luna",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"},
    ],
)
print(completion.choices[0].message.content)
```
```javascript
const completion = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Hello, world!" },
  ],
});
console.log(completion.choices[0].message.content);
```
```go
// as published (community go-openai style); verify against your SDK
resp, err := client.CreateChatCompletion(
	context.Background(),
	openai.ChatCompletionRequest{
		Model: "gpt-5.6-luna",
		Messages: []openai.ChatCompletionMessage{
			{Role: openai.ChatMessageRoleSystem, Content: "You are a helpful assistant."},
			{Role: openai.ChatMessageRoleUser, Content: "Hello, world!"},
		},
	},
)
if err != nil {
	fmt.Printf("ChatCompletion error: %v\n", err)
	return
}
fmt.Println(resp.Choices[0].Message.Content)
```
> The published page writes `model:` lowercase in Go — a typo; the struct field is `Model`.
```php
try {
    $response = $client->chat()->create([
        'model' => 'gpt-5.6-luna',
        'messages' => [
            ['role' => 'system', 'content' => 'You are a helpful assistant.'],
            ['role' => 'user', 'content' => 'Hello, world!'],
        ],
    ]);
    echo $response->choices[0]->message->content;
} catch (\Exception $e) {
    echo "خطا: " . $e->getMessage() . "\n";
}
```

## 5. Discover models & extend
- **Public model list, no auth:** `https://api.avalai.ir/public/models`
- **Authenticated list:** `/v1/models` with API key. Detail: `/v1/models/{id}`.

### Provider-specific parameters (non-OpenAI providers e.g. Stability AI, Anthropic)
Two ways to send params the OpenAI client doesn't support natively (details /fa/guides/provider-specific-params):
1. **`extra_body`** (Python):
```python
response = client.chat.completions.create(
    model="claude-sonnet-4-6",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello, world!"},
    ],
    extra_body={"provider_param1": "value1", "provider_param2": "value2"},
)
```
2. **Direct undocumented params** (TypeScript, `// @ts-expect-error`):
```javascript
const response = await client.chat.completions.create({
  model: "claude-sonnet-4-6",
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Hello, world!" },
  ],
  // @ts-expect-error undocumented parameter
  provider_param1: "value1",
  // @ts-expect-error another undocumented parameter
  provider_param2: "value2",
});
```
The library does not type-check at runtime: extra values are forwarded as-is to the provider API. For GET requests extras go to the query string; otherwise in the body. Explicit alternatives: request options `query`, `body`, `headers`.

### Model IDs listed on the Quickstart page (as published — may lag the news list in 01)
- **OpenAI:** `gpt-5.6-sol`, `gpt-5.6-terra`, `gpt-5.6-luna`, `gpt-5.5`, `gpt-5.4-pro`, `gpt-5.3-codex`, `gpt-image-2`, …
- **Anthropic:** `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, `claude-haiku-4-5`, …
- **Google:** `gemini-3.5-flash`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite`, `gemini-3.1-flash-image`, `gemini-embedding-2`, `gemini-3-flash-preview`, `gemini-2.5-pro`, `gemma-4-26b-a4b-it`, …
- **xAI:** `grok-4.3`, `grok-4.20-reasoning`, `grok-4.20-non-reasoning`, `grok-4-1-fast-reasoning`, …
- **DeepSeek:** `deepseek-v4-pro`, `deepseek-v4-flash`, `deepseek-chat`, …
- **Alibaba:** `qwen3.7-max`, `qwen3.7-plus`, `qwen3.6-plus`, `qwen3.6-flash`, `qwen3.6-max-preview`, `qwen-image-2.0-pro`, `qwen-image-2.0`, …
- **Moonshot.ai:** `kimi-k2.7-code`, `kimi-k2.7-code-highspeed`, `kimi-k2.6`, `kimi-k2-thinking`, `kimi-latest`, …
- **Z.AI:** `glm-5.2`, `glm-5.1`, `glm-5v-turbo`, `glm-5-turbo`, …
- **MiniMax:** `minimax-m3`, `minimax-m2.7`, `minimax-m2.7-highspeed`, `minimax-m2.5`, …
- **Fireworks.ai:** `nemotron-3-ultra` and other fast open-source models.
- Also Meta, Mistral, Cohere, Cloudflare, BytePlus and others.
Other IDs seen in examples: `gpt-5.4-mini`.

### Listing via API
```python
models = client.models.list()
for model in models.data:
    print(f"{model.id} - {model.owned_by}")

# details incl. pricing, capabilities, rate limits
model = client.models.retrieve("gpt-5.6-luna")
print(model)
```
```bash
curl https://api.avalai.ir/public/models                                   # no auth
curl https://api.avalai.ir/v1/models -H "Authorization: Bearer $AVALAI_API_KEY"
curl https://api.avalai.ir/v1/models/gpt-5.5 -H "Authorization: Bearer $AVALAI_API_KEY"
```
Full list: /fa/models/model-details · /fa/api-reference/models

## 6. Track usage & cost (optional; recommended for production, resellers, enterprises)
**User API** gives exact cost tracking.

### Request ID
Every API response carries header `avalai-request-id` (/fa/api-reference/response-headers#avalai-request-id). The OpenAI SDK response object does not expose headers directly — use an HTTP client / raw response, or inspect logs.
```python
response = client.chat.completions.create(
    model="gpt-5.4-mini", messages=[{"role": "user", "content": "سلام!"}]
)
```
```bash
curl -i "https://api.avalai.ir/v1/chat/completions" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.4-mini", "messages": [{"role": "user", "content": "سلام"}]}'
# look for: avalai-request-id: 019ac4a0-a8f4-7041-845f-3ea8f15dcf1a

curl -i "https://api.avalai.ir/v1/responses" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model": "gpt-5.6-luna", "input": "سلام"}'
```

### Exact cost lookup (available within 30 seconds)
```python
import requests, os

response = requests.post(
    "https://api.avalai.ir/user/v1/transactions/lookup",
    headers={
        "Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}",
        "Content-Type": "application/json",
    },
    json={"transaction_ids": ["019ac4a0-a8f4-7041-845f-3ea8f15dcf1a"]},
)
data = response.json()  # exact cost in USD and Toman with full transaction detail
```
Why User API: 100% exact cost (unlike `estimated_cost` in responses); billing for resellers without disputes; usage analytics by model/provider/date/hour; full transaction history for compliance.
More: /fa/api-reference/user · /fa/resellers/cost-tracking-guide · /fa/resellers/enterprise-guide

### Debug with doc URLs
Paste any docs.avalai.ir page URL into a message at https://chat.avalai.ir; the model can read that page and: explain sections, help debug, produce implementation examples, answer interactively.

## Next steps (links)
- Anthropic SDK multi-provider support: /fa/news/2025-06-09-anthropic-sdk-multi-provider-support ; original: /fa/news/2025-06-03-anthropic-sdk-support-added
- Libraries: /fa/libraries · API reference: /fa/api-reference/introduction · Auth: /fa/api-reference/authentication
- Guides: /fa/guides/production-best-practices · Content policy (data handling & privacy): /fa/safety/content-policy

## ⚠ Consistency notes for the skill
- Quickstart examples use older IDs (`gpt-5.6-luna`, `claude-sonnet-4-6`) while the home page news lists newer ones (`gpt-6-astra`, `claude-sonnet-5-5`…). Treat model IDs as examples; confirm live via `/public/models` before hard-coding.
- Quickstart text still says Responses is "recommended for GPT-5.5 apps" (stale wording).
