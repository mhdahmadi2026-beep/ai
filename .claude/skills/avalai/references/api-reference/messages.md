# Messages API (Anthropic format) — `POST https://api.avalai.ir/v1/messages` (docs: /fa/api-reference/messages)

Native Anthropic Messages format via AvalAI's multi-provider routing. Supports Claude (`claude-sonnet-5`, `claude-opus-4-8`, `claude-opus-4-7`, `claude-opus-4-6`, `claude-sonnet-4-6`, other Claude base namespaces; also `claude-haiku-4-5` in PHP example). Full support for Claude Sonnet 5 and Opus 4.8 incl. mid-conversation `role:"system"` messages (keeps prompt-cache hits) and public `stop_details` object in refusal responses. (Claude 3.x/4.0/4.1 IDs are removed — see 10-deprecations.md; the page's `anthropic.claude-sonnet-4-20250514-v1:0` examples are stale → use a current id from `/v1/models`.)

**Multi-provider (since 19 Khordad 1404):** same format also reaches OpenAI, AWS Bedrock, Vertex AI, Gemini, MiniMax (`minimax-m3` with native thinking blocks + tool use) models. Some models are Chat-only or partial — check `/v1/models`. Gemini 3.8 TTS is NOT available here.

## Auth / base URL
- **Anthropic SDK base URL = `https://api.avalai.ir` (no `/v1`)** — SDK appends `/v1/messages`. Raw HTTP: `https://api.avalai.ir/v1/messages` with header `x-api-key: $AVALAI_API_KEY` (Bearer also accepted per auth page). Key from env, server-side only.

## Request
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | Anthropic-style model id |
| `messages` | array | yes | `{role: user|assistant, content: string | content-block[]}` (blocks for multimodal) |
| `system` | string | no | system prompt (Messages has no `system` role in the array, except the mid-conversation `role:"system"` feature on supported Claude models) |
| `max_tokens` | int | **yes** | required (unlike OpenAI) |
| `temperature` | number | no | 0–1, default 1 (don't send on adaptive-thinking Claude models Opus 5.5/Fable 5.1/Opus 5 — see chat.md) |
| `top_p` | number | no | default 1 |
| `top_k` | int | no | default −1 (disabled) |
| `stream` | bool | no | SSE |
| `stop_sequences` | array | no | |
| `metadata` | object | no | |
(Tools, thinking, caching blocks etc. follow Anthropic's standard schema; not detailed on this page.)

```python
from anthropic import Anthropic
client = Anthropic(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir")  # no /v1
r = client.messages.create(model="<claude-id>", max_tokens=1024,
    messages=[{"role":"user","content":"سلام! آیا می‌توانید به من کمک کنید تا محاسبات کوانتومی را درک کنم؟"}])
print(r.content[0].text)
```
```javascript
import Anthropic from "@anthropic-ai/sdk";
const client = new Anthropic({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir" });
```
```bash
curl https://api.avalai.ir/v1/messages -H "Content-Type: application/json" -H "x-api-key: $AVALAI_API_KEY" \
  -d '{"model":"<claude-id>","max_tokens":1024,"messages":[{"role":"user","content":"…"}]}'
```
Go sample (`github.com/anthropic/anthropic-sdk-go`, `MessagesRequest`) doesn't match the real SDK (`github.com/anthropics/anthropic-sdk-go`, `client.Messages.New(ctx, anthropic.MessageNewParams{…})`) — flagged; PHP: cURL with `x-api-key` and `anthropic-version` header may be needed by some routes — read `content[0].text`.

## Response
`{id:"msg_…", type:"message", role:"assistant", content:[{type:"text", text}], model, stop_reason: end_turn|max_tokens|stop_sequence|…, stop_sequence, usage:{input_tokens, output_tokens}}`. Content blocks: `text`, `image` (and thinking/tool_use on supporting models). Refusals carry `stop_details` on Sonnet 5 / Opus 4.8.

## Streaming
`stream:true`; handle `content_block_delta` with `delta.type === "text_delta"` → `delta.text` (Anthropic event stream: message_start, content_block_start/delta/stop, message_delta, message_stop).

## Errors
400/401/403/404/429/500; see error-handling. Related: providers/anthropic, chat, authentication, rate-limits.
