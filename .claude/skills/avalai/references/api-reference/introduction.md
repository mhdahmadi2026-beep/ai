# مرجع API AvalAI / API reference introduction — https://docs.avalai.ir/fa/api-reference/introduction
AvalAI offers a unified API compatible with the OpenAI API structure, giving access to multiple providers' models through one consistent interface.

## Base URL
All requests go to: `https://api.avalai.ir/v1`
## Authentication
All endpoints require auth: put your API key in the `Authorization` header of every request (details: /fa/api-reference/authentication).

## Start: choose the right API surface (checklist adapted from OpenAI's overview)
| Need | AvalAI path | Note |
|---|---|---|
| New text, reasoning, multimodal or tool-driven app | `/v1/responses` (/fa/api-reference/responses) | prefer when the chosen model's route supports Responses — richer state, tools, output objects |
| Existing chat integration / broad provider compatibility | `/v1/chat/completions` (/fa/api-reference/chat) | keep for mature chat apps and providers exposing the chat-completions schema |
| Request-based speech or audio files | `/v1/audio/*` (/fa/api-reference/audio) | transcription, translation, text-to-speech with bounded files or generated speech |
| Live voice / low-latency session | Realtime architecture guide /fa/guides/realtime-audio | until the matching AvalAI route is enabled for your account, treat OpenAI Realtime docs as architecture guidance only |
| Usage, cost & reseller reporting | `user/v1` (/fa/api-reference/user) | AvalAI-specific endpoints for transactions, usage summaries, billing reconciliation |
| Organization management | AvalAI dashboard or support | don't assume OpenAI's Administration endpoints map to AvalAI account management |

## Endpoints
- **Responses** — recommended starting point for new OpenAI-family workflows (text, reasoning, multimodal, tools) when the model route supports it. /fa/api-reference/responses
- **Chat Completions** — still supported for existing chat integrations and routes exposing the chat schema. /fa/api-reference/chat
- **Images** — generate and edit images (page text still says "like DALL·E"; DALL·E is removed — see 10-deprecations). /fa/api-reference/images
- **Embeddings** — text → vectors for search, clustering, ML. /fa/api-reference/embeddings
- **Audio** — transcription, translation, speech generation. /fa/api-reference/audio
- **Moderation** — detect potentially harmful text. /fa/api-reference/moderation
- **User API** — exact cost tracking, transaction history, usage analytics (for resellers, large orgs, production apps). Key features: exact cost via [`avalai-request-id`](/fa/api-reference/response-headers#avalai-request-id) with 100% accuracy; filterable transaction history; usage analytics & summaries; available within 30 s after the call. /fa/api-reference/user

## Request & response formats
All endpoints accept and return JSON; always send `Content-Type: application/json`.
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
"model": "gpt-5.6-luna",
"messages": [{"role": "user", "content": "Hello!"}]
}'
```
Responses equivalent (when the model supports `/v1/responses`; `messages`→`input`, system message→`instructions` or a `developer` item, `choices[0].message.content`→`response.output_text`, inspect `response.output` by `type` for tools/multimodal):
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Hello!",
    "instructions": "You are a helpful assistant."
  }'
```
Example response:
```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-5.6-luna",
  "choices": [
    {
      "message": {"role": "assistant", "content": "سلام! چطور می‌توانم امروز به شما کمک کنم؟"},
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {"prompt_tokens": 10, "completion_tokens": 8, "total_tokens": 18}
}
```

## Error handling
Standard HTTP codes: **2xx** success · **4xx** client error (invalid request, auth) · **5xx** server error. See /fa/guides/error-handling.
## Rate limits
Exceeding limits → `429 Too Many Requests`. See /fa/guides/rate-limits (and 09-rate-limits.md).

## Troubleshooting & request IDs
Follow OpenAI's overview emphasis on request IDs, response headers and rate-limit headers for production debugging:
- When the route accepts it, send a unique **`X-Client-Request-Id`** for every retryable API attempt.
- Log the returned **`avalai-request-id`**, endpoint, model, HTTP status, retry count, rate-limit headers, and your own **hashed `safety_identifier`** if present.
- Use [`avalai-request-id`](/fa/api-reference/response-headers#avalai-request-id) for cost reconciliation through the [User API](/fa/api-reference/user) and to give support an exact trace.
- Don't keep raw prompts/files in logs unless your data-retention policy explicitly allows.

## SDKs & client libraries
Compatible with OpenAI client libraries — set AvalAI's base URL.
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",  # base URL
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
	"os"

	openai "github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)
	_ = client
}
```

## API versioning
Versioned for backward compatibility; current version **`v1`**. Treat compatible changes as normal: new endpoints, optional parameters, response fields and streaming event types may be added without breaking integrations. **Parse only the fields you need, ignore unknown response properties, don't assume JSON field order or exact format of opaque IDs.**
Model behavior can change between aliases and snapshots even when the API schema is stable. For production workflows needing stability: **pin model IDs**, run evals before switching a model alias, and keep rollback notes for prompts, tools and response parsing.

## Next steps
/fa/api-reference/chat · /responses · /images · /embeddings · /audio · /moderation · /user · /response-headers
