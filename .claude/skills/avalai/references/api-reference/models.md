# مرجع API مدل‌ها / Models API — https://docs.avalai.ir/fa/api-reference/models
List available models and get details (pricing, rate limits, capabilities). Supports **both OpenAI and Anthropic API formats**.

## Endpoints
| Method | Endpoint | Auth | Description |
|---|---|---|---|
| GET | `/v1/models` | yes | list all available models |
| GET | `/v1/models/{model_id}` | yes | details of one model |
| GET | `/public/models` | **no** | public model list |

## Auth-type detection (response format follows the auth header)
| Header | Response format |
|---|---|
| `Authorization: Bearer API_KEY` | OpenAI format |
| `x-api-key: API_KEY` | Anthropic format |

## List models
### OpenAI format — `GET https://api.avalai.ir/v1/models` (header `Authorization: Bearer YOUR_API_KEY`)
```bash
curl https://api.avalai.ir/v1/models \
  -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

models = client.models.list()

for model in models.data:
    print(f"{model.id} - {model.owned_by}")
```
```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
});

const models = await client.models.list();

for (const model of models.data) {
  console.log(`${model.id} - ${model.owned_by}`);
}
```
```go
models, err := client.Models.List(context.Background())   // client := openai.NewClient(option.WithAPIKey(...), option.WithBaseURL("https://api.avalai.ir/v1"))
if err != nil { panic(err) }
for _, model := range models.Data {
	fmt.Printf("%s - %s\n", model.ID, model.OwnedBy)
}
```
```php
$client = OpenAI::factory()->withApiKey($apiKey)->withBaseUri('https://api.avalai.ir/v1')->make();
$models = $client->models()->list();
foreach ($models->data as $model) { echo $model->id . " - " . $model->ownedBy . "\n"; }
```
Response (list items carry flat metadata: `id`, `object`, `owned_by`, `min_tier`, `pricing`, `mode`, `max_tokens`, `max_input_tokens`, `max_output_tokens`, `supports_*`):
```json
{
  "object": "list",
  "data": [
    {
      "id": "glm-5.2", "object": "model", "owned_by": "zai", "min_tier": 0,
      "pricing": {"input": 1.4, "cached_input": 0.26, "output": 4.4},
      "mode": "chat", "max_tokens": 1000000, "max_input_tokens": 991000, "max_output_tokens": 128000,
      "supports_function_calling": true, "supports_prompt_caching": true, "supports_tool_choice": true
    },
    {
      "id": "kimi-k2.7-code", "object": "model", "owned_by": "moonshot", "min_tier": 0,
      "pricing": {"input": 1.045, "cached_input": 0.19, "output": 4.4},
      "mode": "chat", "max_tokens": 262144, "max_input_tokens": 262144, "max_output_tokens": 262144,
      "supports_function_calling": true, "supports_tool_choice": true, "supports_web_search": true
    }
  ]
}
```
(sample prices differ slightly from 06-pricing, e.g. kimi-k2.7-code input 1.045 vs 0.95 — illustrative; trust live data.)
### Anthropic format — send `x-api-key`
```bash
curl https://api.avalai.ir/v1/models -H "x-api-key: $AVALAI_API_KEY"
```
```python
import anthropic

client = anthropic.Anthropic(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir",
)

models = client.models.list()

for model in models.data:
    print(f"{model.id} - {model.display_name}")
```
```javascript
import Anthropic from "@anthropic-ai/sdk";

const client = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir",
});

const models = await client.models.list();

for (const model of models.data) {
  console.log(`${model.id} - ${model.display_name}`);
}
```
Response:
```json
{
  "data": [
    {"id": "claude-sonnet-4-20250514", "created_at": "2025-02-19T00:00:00Z", "display_name": "Claude Sonnet 4", "type": "model"},
    {"id": "claude-3-5-sonnet-20241022", "created_at": "2024-10-22T00:00:00Z", "display_name": "Claude 3.5 Sonnet", "type": "model"}
  ],
  "first_id": "claude-sonnet-4-20250514",
  "has_more": true,
  "last_id": "claude-3-5-sonnet-20241022"
}
```
(Those example IDs are removed models — see 10-deprecations; illustrative only.)
Query params (Anthropic format): `after_id` (string), `before_id` (string), `limit` (number) — all optional.

## Public models — no auth
`GET https://api.avalai.ir/public/models` (useful to show model options before authentication). Format ≈ the OpenAI-format list.
```bash
curl https://api.avalai.ir/public/models
```
```python
import requests

response = requests.get("https://api.avalai.ir/public/models")
models = response.json()

for model in models["data"]:
    print(f"{model['id']} - {model['owned_by']}")
```
```javascript
const response = await fetch("https://api.avalai.ir/public/models");
const models = await response.json();

for (const model of models.data) {
  console.log(`${model.id} - ${model.owned_by}`);
}
```
> Note: the pricing page describes `/public/models` entries with `tier_rate_limits` (keyed `"0"`–`"5"` with `max_requests_per_1_minute` / `max_tokens_per_1_minute`) and `supported_endpoints`; this Models page shows `extra.rate_limits.tiers` with `rpm`/`tpm` on the authenticated retrieve endpoint. Both are per-tier limit sources — inspect the actual JSON.

## Retrieve a model — `GET https://api.avalai.ir/v1/models/{model_id}`
Path param `model_id` (string, required), e.g. `gpt-5.5`, `claude-sonnet-4.6`. Returns AvalAI-specific metadata, pricing and rate limits in an `extra` object.
### OpenAI format
```bash
curl https://api.avalai.ir/v1/models/gpt-5.5 -H "Authorization: Bearer $AVALAI_API_KEY"
```
```python
from openai import OpenAI

client = OpenAI(
    api_key="your-avalai-api-key",
    base_url="https://api.avalai.ir/v1",
)

model = client.models.retrieve("gpt-5.6-luna")

print(f"Model: {model.id}")
print(f"Owned by: {model.owned_by}")

# access AvalAI extra data (available as extra fields)
print(f"Extra data: {model.model_extra}")
```
```javascript
const model = await client.models.retrieve("gpt-5.6-luna");
console.log(`Model: ${model.id}`);
console.log(`Owned by: ${model.owned_by}`);
```
(Go: `client.Models.Get(ctx, "gpt-5.6-luna")`; PHP: `$client->models()->retrieve('gpt-5.6-luna')`.)
Response:
```json
{
  "id": "gpt-5.6-luna",
  "object": "model",
  "created": 1765622594,
  "owned_by": "openai",
  "extra": {
    "metadata": {
      "min_tier": 0, "mode": "chat",
      "max_tokens": 128000, "max_input_tokens": 1050000, "max_output_tokens": 128000,
      "supports_system_messages": true, "supports_function_calling": true,
      "supports_parallel_function_calling": true, "supports_vision": true,
      "supports_pdf_input": true, "supports_prompt_caching": true,
      "supports_tool_choice": true, "supports_response_schema": true
    },
    "pricing": {"input": 5.0, "cached_input": 0.5, "output": 30.0},
    "rate_limits": {
      "tiers": {
        "0": {"rpm": 3.0, "tpm": 40000.0},
        "1": {"rpm": 500.0, "tpm": 300000.0},
        "2": {"rpm": 5000.0, "tpm": 3000000.0},
        "3": {"rpm": 5000.0, "tpm": 4000000.0},
        "4": {"rpm": 10000.0, "tpm": 10000000.0},
        "5": {"rpm": 10000.0, "tpm": 30000000.0}
      },
      "current": {"tier": 5, "rpm": 10000.0, "tpm": 30000000.0}
    }
  }
}
```
(Example numbers for gpt-5.6-luna disagree with 06-pricing ($0.20/$1.20) — the sample is illustrative.)
### Anthropic format (`x-api-key`)
```bash
curl https://api.avalai.ir/v1/models/claude-sonnet-4-20250514 -H "x-api-key: $AVALAI_API_KEY"
```
```python
import anthropic

client = anthropic.Anthropic(api_key="your-avalai-api-key", base_url="https://api.avalai.ir")
model = client.models.retrieve("claude-sonnet-4-20250514")
print(f"Model: {model.id}")
print(f"Display name: {model.display_name}")
print(f"Created at: {model.created_at}")
```
Response: `{id, type:"model", display_name, created_at, extra:{metadata{…, search_context_cost_per_query{search_context_size_high/low/medium}}, pricing{input:3.0, cached_input:1.5, output:15.0}, rate_limits{tiers{"1":{rpm:10,tpm:80000},"2":{25,160000},"3":{50,400000},"4":{80,800000},"5":{100,1000000}}, current{tier:5,rpm:100,tpm:1000000}}}}` (tiers start at the model's `min_tier`, here 1).

## Response schema
**Model object (OpenAI):** `id`, `object` ("model"), `created` (unix time), `owned_by`.
**Model object (Anthropic):** `id`, `created_at` (ISO 8601), `display_name`, `type` ("model").
### AvalAI `extra` object — returned **only** by the retrieve endpoint
**metadata:** `min_tier` (0–5, minimum tier to use the model) · `mode` ∈ `chat`, `embedding`, `completion`, `image_generation`, `video_generation`, `audio_transcription`, `audio_speech`, `ocr`, `moderation`, `rerank`, `search` · `max_tokens`, `max_input_tokens`, `max_output_tokens` · booleans: `supports_system_messages`, `supports_function_calling`, `supports_parallel_function_calling`, `supports_vision`, `supports_pdf_input`, `supports_prompt_caching`, `supports_tool_choice`, `supports_response_schema` (also seen: `supports_web_search`).
**pricing** (varies by mode; USD):
- token-based (chat/embedding/completion): `input`, `cached_input`, `output` per 1M tokens; optional `audio_input`, `image_input`, `image_output`, `search_context_cost_per_query` (object).
- `image_generation`: `output_cost_per_image`, `output_cost_per_image_{resolution}` (e.g. `1920x1080`, `4096x4096`).
- `video_generation`: `output_cost_per_video_per_second`, `output_cost_per_video_per_second_{resolution}` (e.g. `720x1280`, `1792x1024`).
- `audio_transcription`: `input_cost_per_second`. `audio_speech`: `input_cost_per_character`. `ocr`: `input_cost_per_page`. `rerank` / `search`: `input_cost_per_query`.
**rate_limits:** `tiers` (object keyed by tier 0–5; each `{rpm, tpm}`) and `current` (`{tier, rpm, tpm}` for your account). Tiers & upgrade: 09-rate-limits.md.

## Errors
401 unauthorized (invalid/missing key) · 404 not found (model doesn't exist) · 429 rate limited · 500 internal error.

## Related
authentication.md · 09-rate-limits.md · /fa/models/index (overview by provider) · /fa/models/model-details · 06-pricing.md
