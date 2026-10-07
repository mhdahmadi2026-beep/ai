# API تکمیل گفتگو / Chat Completions — https://docs.avalai.ir/fa/api-reference/chat
Core of AvalAI: conversational responses from many models (GPT-6.1 Sol & GPT-6 family — Astra/Sol/Luna, GPT-5.6 Sol/Terra/Luna; Anthropic Claude Sonnet 5.5, Opus 5.5, Fable 5.1, Opus 5; xAI Grok 4.7/4.6/4.5/4.3; Z.AI GLM-5.3-Flash/GLM-5.3; Moonshot Kimi K3; Google Gemini 3.8/3.7/3.6 Flash, 3.5 Flash-Lite, Gemma 4; Alibaba Qwen3.8-Max/Flash/27B, Qwen3.7-Plus; DeepSeek V4.1 Flash via `deepseek-v4.1-flash`; Cloudflare Nemotron-3-120B; Fireworks.ai Muse Glimmer 30B, Nemotron 3.5 Lightning, Nemotron-3-Ultra; MiniMax M3).
**Endpoint:** `POST https://api.avalai.ir/v1/chat/completions`
Responses equivalent (when the model supports `/v1/responses`): `messages`→`input`; system message→`instructions` or a `developer` item; `choices[0].message.content`→`response.output_text`; inspect `response.output` by `type` for tools/multimodal.
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    reasoning={"effort": "medium"},
    instructions="You are a helpful assistant.",
    input="Write a one-sentence summary of AvalAI.",
)

print(response.output_text)
```

## Model-specific notes (callouts at the top of the page)
- **GPT-6.1 Sol** (`gpt-6.1-sol`): up to **922,000 input / 128,000 output** tokens; tier 1+; full on chat/messages/responses. Standard per-1M: $2.00 in / $0.10 cached / $10.00 out; input >272K higher. **Don't send `none`/`minimal` reasoning effort** (local metadata doesn't support them). /fa/providers/openai#gpt-6-1-sol
- **Claude Sonnet 5.5** (`claude-sonnet-5-5`): **1,000,000 in / 128,000 out**; tier 1+; chat & messages full, **responses PARTIAL**. Don't send unsupported sampling controls, assistant-message prefill, or forced tool use. Old workflows with thinking disabled → move to `between_tools`; Claude Platform default effort is `high` (not `medium` as in Claude apps/Claude Code). /fa/providers/anthropic#claude-sonnet-5-5
- **Claude Opus 5.5** (`claude-opus-5-5`): long-horizon coding agents & knowledge work; 1M in / 128K out; vision, PDF, tools, structured output, prompt caching; full on chat/messages/responses; tier 1+. **Thinking always on, default effort `medium`.** Forced tool use unsupported. Per 1M: $4.00 in / $0.20 cached / $8.00 cache-write / $20.00 out.
- **GPT-6 Sol / GPT-6 Luna**: Sol for coding/professional work on a bounded budget, Luna for high-volume low-cost; reasoning, vision, tools, structured output, PDF input, prompt caching; 922K in / 128K out; full on all three endpoints.
- **Grok 4.7** (`grok-4.7`): long-horizon coding agents, verification, knowledge work; vision, reasoning, tools, structured output, caching; **500K in / 500K out** (listing); chat & messages full, **responses PARTIAL** — don't assume parity of hosted tools or stored-state flows. **Don't send `reasoning_effort`** until route support is confirmed.
- **GPT-6 Astra** (`gpt-6-astra`): hard computer-use, software engineering, professional, science, math, cybersecurity, long context; reasoning-effort control; full on all three endpoints.
- **Claude Fable 5.1** (`claude-fable-5-1`): advanced coding, root-cause analysis, knowledge work, research, computer use, long agents; 1M in / 128K out; **always-on adaptive thinking with tunable effort**; structured output, vision, PDF, caching, tools; chat & messages full, responses partial; **tier 2+**.
- **GLM-5.3-Flash** (`glm-5.3-flash`): efficient multimodal coding, vision, tools, agentic; 320B total / 18B active; **991,000 in / 128,000 out**; chat & messages full, responses partial.
- **GLM-5.3** (`glm-5.3`): Z.AI flagship; **thinking mandatory — send `thinking.type: "enabled"` and `reasoning_effort` ∈ `low` | `high` | `max`; requests disabling thinking error out.** chat/messages full, responses partial.
- **Fireworks.ai:** `muse-glimmer-30b` (Meta multimodal, multilingual, agentic, tunable reasoning), `nemotron-3.5-lightning` (NVIDIA 30B total/3B active; reasoning & coding). Full on chat & messages, partial on responses. /fa/providers/fireworksai
- **Claude Opus 5** (`claude-opus-5`): hard SWE, root-cause, knowledge work, computer use, science, long agents; 1M in / 128K out; adaptive thinking; structured output, vision, PDF, caching, tools; chat & messages full, responses partial.
- **Gemini 3.8 Flash** (`gemini-3.8-flash`): long-horizon coding, autonomous agents, multi-step reasoning, repeated tool use; supports `v1/chat/completions`, native Gemini `v1beta/`, `v1/messages`; responses partial. Promo until **31 Dec 2026 (1405-10-10)**: $0.75 in / $0.075 cached / $3.75 out per 1M. Alias `gemini-flash-latest` → `gemini-3.8-flash`.
- **Kimi K3** (`kimi-k3`): Moonshot flagship, 1M context, native vision, always-on reasoning; chat & messages full, responses partial; alias `kimi-latest` → `kimi-k3` (same price). Supports `reasoning_effort: "max"`; **don't send fixed sampling fields (`temperature`, `top_p`)**.
- **Qwen3.8 models:** `qwen3.8-max` (managed multimodal flagship, optional thinking, 1M context, 128K max output); `qwen3.8-flash` (alias `qwen3.8-flash-next`; vision input, thinking on by default, 262K context); `qwen3.8-27b` (dense 27B vision-language, flexible thinking control); `qwen3.8-2.4t-a95b` (open-weight base 2.4T total/95B active, **text-only, thinking mandatory, `reasoning_effort` ∈ `low`|`medium`|`xhigh`**). All four: chat & messages full, responses partial. /fa/providers/alibaba
- **DeepSeek V4.1 Flash** (`deepseek-v4.1-flash`): native vision, thinking & non-thinking modes, tools, prompt caching; listing: 1,000,000 in / 393,216 out (provider says 384K); flat price $0.15 / $0.003 / $0.60 per 1M (no peak-hour doubling). ⚠ Page says the `deepseek-v4-pro` reroute happens 2026-09-14 04:00 UTC — **superseded by 10-deprecations: every DeepSeek ID now routes to `deepseek-v4.1-flash`.**
- **Grok 4.6** (`grok-4.6`): long-horizon agents, coding, knowledge work, interactive visual apps (not image generation); vision, reasoning, tools, structured output, caching; 500K/500K. ≤200K input: $2.00 / $0.50 / $6.00 per 1M; above: $4.00 / $1.00 / $12.50.
- **Endpoint compatibility of Grok 4.6/DeepSeek V4.1:** `v1/chat/completions` & `v1/messages` supported; `v1/responses` PARTIAL — don't assume full parity of Responses built-in tools or stored-state workflows. /fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added

## Request body
| Param | Type | Req | Description |
|---|---|---|---|
| `model` | string | yes | model id (see /fa/models/model-details) |
| `messages` | array | yes | conversation history |
| `temperature` | number | no | 0–2; higher = more random; default 1 |
| `top_p` | number | no | nucleus sampling alternative; default 1 |
| `n` | integer | no | number of choices; default 1 |
| `stream` | boolean | no | send partial message deltas; default false |
| `stream_options` | object | no | only with `stream: true`; support depends on route & SDK |
| `modalities` | array | no | output types; most chat models return `["text"]`; audio output needs model/route support + `audio` param |
| `audio` | object | no | audio-output config when `modalities` includes `"audio"`; for most AvalAI workflows prefer the dedicated Audio routes or Realtime |
| `prediction` | object | no | predicted output for latency-sensitive rewrites; provider/model dependent (/fa/guides/predicted-outputs) |
| `stop` | string/array | no | up to 4 stop sequences |
| `max_completion_tokens` | integer | no | cap on generated tokens **incl. visible output and hidden reasoning tokens**; if reasoning eats the budget the model may stop with `finish_reason: "length"` before any visible text — leave headroom or lower effort (/fa/guides/reasoning) |
| `max_tokens` | integer | no | legacy cap; deprecated upstream in favor of `max_completion_tokens`, incompatible with some reasoning models |
| `presence_penalty` | number | no | −2.0…2.0; default 0 |
| `frequency_penalty` | number | no | −2.0…2.0; default 0 |
| `logit_bias` | object | no | adjust token likelihood |
| `logprobs` | boolean | no | return token log-probs if supported |
| `top_logprobs` | integer | no | 0–20; needs `logprobs: true` and model/route support |
| `metadata` | object | no | ≤16 key/value pairs (keys ≤64 chars, values ≤512) for filtering stored completions |
| `safety_identifier` | string | no | stable privacy-preserving id for abuse monitoring: hash or opaque internal id ≤64 chars; no raw PII (/fa/guides/safety-best-practices) |
| `prompt_cache_key` | string | no | cache-bucketing key for repeated prefixes; opaque & stable per assistant/tenant/policy/schema (/fa/guides/prompt-caching) |
| `prompt_cache_retention` | string | no | legacy retention policy for pre-GPT-5.6 models; deprecated for GPT-5.6+ (newer uses `prompt_cache_options.ttl`; AvalAI pass-through is route-dependent) — drop unsupported controls |
| `moderation` | object | no | inline moderation e.g. `{"model":"omni-moderation-latest"}` if enabled for the route; else call `/v1/moderations` separately |
| `user` | string | no | legacy end-user id; use `safety_identifier` + `prompt_cache_key` |
| `response_format` | object | no | `{"type":"json_schema","json_schema":…}` (Structured Outputs) or `{"type":"json_object"}` fallback; for new structured workflows prefer `text.format` in `/v1/responses` |
| `reasoning_effort` | string | no | reasoning effort for supported models; allowed values/default are model-specific — verify per route. DeepSeek-V4-Flash-0731: `low`/`high`/`max`; Claude Fable 5.1 & Claude Opus 5 use provider adaptive thinking + `output_config.effort` in `extra_body`; Fable 5.1 thinking always on |
| `verbosity` | string | no | `low`/`medium`/`high` response length/detail on supported models, without changing reasoning depth |
| `seed` | integer | no | best-effort determinism |
| `store` | boolean | no | store the completion for later retrieval/distillation/evals if route/account supports stored chat completions |
| `tools` | array | no | tools the model may call |
| `tool_choice` | string/object | no | which tool (if any) is called |
| `parallel_tool_calls` | boolean | no | allow parallel tool calls; set `false` for state-changing/ordered tools |
| `web_search_options` | object | no | Chat-compatible web search when the OpenAI-style model supports built-in search; for provider-independent retrieval prefer `/v1/search` |
| `service_tier` | string | no | public values `"default"` and `"flex"` (flex −50% for select OpenAI models, up to 900 s); don't send `"priority"` unless enabled for your account (/fa/pricing#flex, 07-service-tiers.md) |
> Parameter support depends on model & provider. New reasoning models may ignore or reject legacy sampling/stop/token fields; hosted tools depend on route/account. For new stateful/tool/reasoning workflows compare with Responses first.
For `response_format`: when supported prefer **`json_schema`** over `json_object` (JSON mode guarantees only syntactically valid JSON, not required keys/enums/types → validate in app). See /fa/guides/structured-outputs.
**Claude Opus 5.5 parameter limits:** don't send disabled-thinking, fixed thinking budgets, pre-filled assistant messages, or unsupported sampling fields (`temperature`, `top_p`). Tune effort via adaptive `thinking` + `output_config.effort` in `extra_body` (start with `medium`); don't assume another provider's `reasoning_effort` mapping. Remove tool-choice settings that force a call. Preserve full thinking & assistant tool blocks across turns; don't rely on visible text between tool calls under default display (/fa/guides/reasoning#claude-opus-5-5).

### Message object
| Param | Type | Req | Description |
|---|---|---|---|
| `role` | string | yes | `developer`, `system`, `user`, `assistant`, `tool` (use `developer`/`system` for stable instructions depending on model support) |
| `content` | string/array | yes | string or content parts for multimodal |
| `name` | string | no | author name (required for `tool` roles per the page) |
| `tool_call_id` | string | no | required for `tool` role: id of the tool call being answered |

## Examples
### Quick start — GPT-6.1 Sol & Claude Sonnet 5.5
No sampling/reasoning controls sent on purpose. For Sonnet's adaptive thinking & `output_config.effort` use the native Messages example (/fa/news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added). Preserve full assistant/tool turns; leave room in output for reasoning.
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1"
)
for model in ("gpt-6.1-sol", "claude-sonnet-5-5"):
    response = client.chat.completions.create(
        model=model,
        messages=[
            {
                "role": "user",
                "content": "Review this release plan and give a concise verification checklist: deploy an API behind a feature flag.",
            }
        ],
    )
    print(model, response.choices[0].message.content)
```
### Quick start — Claude Opus 5.5 (adaptive thinking stays on; allow enough completion tokens)
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "claude-opus-5-5",
    "max_completion_tokens": 8192,
    "messages": [
      {"role": "user", "content": "Review a staged database migration and list verification and rollback checks."}
    ]
  }'
```
Price per 1M: $4.00 in, $0.20 cached, $8.00 cache-creation, $20.00 out. Native Messages/Responses samples: /fa/news/2026-09-24-claude-opus-5-5-added.
### Quick start — GPT-6 Sol, GPT-6 Luna, Grok 4.7 (switch `model` to `gpt-6-luna` or `grok-4.7`)
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-6-sol",
    "messages": [
      {"role": "user", "content": "Suggest a concise verification checklist for deploying an API behind a feature flag."}
    ]
  }'
```
These understand image input but don't generate images. Reasoning control for Sol/Luna: `reasoning_effort` here, `reasoning.effort` in Responses; verify allowed values; don't generalize defaults from another model. Pricing tiers: higher rates for Sol/Luna input >272K, Grok 4.7 input >200K (pricing thresholds by input length, **not max context**).
### Quick start — DeepSeek V4.1 Flash & Grok 4.6 (switch to `grok-4.6` to compare)
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "deepseek-v4.1-flash",
    "messages": [
      {"role": "user", "content": "Review this release plan and propose a concise test checklist: deploy a new API behind a feature flag."}
    ]
  }'
```
Don't use reasoning-effort values of older models without confirming support.
### Basic chat completion
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
  "model": "gpt-6-astra",
  "messages": [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello!"}
  ]
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
    model="gpt-5.6-sol",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "Hello!"},
    ],
)

print(response.choices[0].message.content)
```
```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1"
});

const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [
  {"role": "system", "content": "You are a helpful assistant."},
  {"role": "user", "content": "Hello!"}
  ]
});

console.log(response.choices[0].message.content);
```
```go
// Go sample (as published; mixes go-openai style API with the openai-go import path — verify against your SDK)
client := openai.NewClient("AVALAI_API_KEY")
client.BaseURL = "https://api.avalai.ir/v1"
resp, err := client.CreateChatCompletion(
	context.Background(),
	openai.ChatCompletionRequest{
		Model: "gpt-5.6-sol",
		Messages: []openai.ChatCompletionMessage{
			{Role: openai.ChatMessageRoleSystem, Content: "You are a helpful assistant."},
			{Role: openai.ChatMessageRoleUser, Content: "Hello!"},
		},
	},
)
// resp.Choices[0].Message.Content
```
```php
<?php
$apiKey = getenv('AVALAI_API_KEY');
$apiUrl = 'https://api.avalai.ir/v1/chat/completions';

$data = [
'model' => 'gpt-5.6-sol',
'messages' => [
['role' => 'system', 'content' => 'You are a helpful assistant.'],
['role' => 'user', 'content' => 'Hello!']
]
// 'temperature' => 0.7, 'max_tokens' => 150
];

$jsonData = json_encode($data);
$ch = curl_init($apiUrl);
curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);
curl_setopt($ch, CURLOPT_POST, true);
curl_setopt($ch, CURLOPT_POSTFIELDS, $jsonData);
curl_setopt($ch, CURLOPT_HTTPHEADER, [
'Content-Type: application/json',
'Authorization: Bearer ' . $apiKey,
'Content-Length: ' . strlen($jsonData)
]);
$response = curl_exec($ch);
$httpcode = curl_getinfo($ch, CURLINFO_HTTP_CODE);
$err = curl_error($ch);
curl_close($ch);

if ($err) { echo "cURL error #:" . $err; }
elseif ($httpcode >= 400) { echo "HTTP error: " . $httpcode . "\n" . $response; }
else {
  $responseData = json_decode($response, true);
  echo $responseData['choices'][0]['message']['content'] ?? print_r($responseData, true);
}
```
Responses equivalents of these three (python `client.responses.create(model="gpt-5.6-sol", instructions="You are a helpful assistant.", input="Hello!")`; JS same with `gpt-5.6-luna`; curl to `/v1/responses` with `input` + `instructions`) → `response.output_text`.

## Response format
```json
{
  "id": "chatcmpl-123abc",
  "object": "chat.completion",
  "created": 1677858242,
  "model": "gpt-5.6-sol",
  "choices": [
    {
      "message": {"role": "assistant", "content": "سلام! چطور می‌توانم امروز به شما کمک کنم؟"},
      "finish_reason": "stop",
      "index": 0
    }
  ],
  "usage": {"prompt_tokens": 10, "completion_tokens": 8, "total_tokens": 18},
  "service_tier": "default"
}
```
**Fields:** `id` · `object` ("chat.completion") · `created` (unix s) · `model` · `choices[]` · `usage` · `moderation` (inline moderation results if requested & supported) · `service_tier` (usually `"default"`/`"flex"`; `"priority"` only if explicitly enabled).
**Choice:** `message` · `finish_reason` ∈ `stop` | `length` | `tool_calls` | `content_filter` | `function_call` · `index`.
**Usage:** `prompt_tokens`, `completion_tokens`, `total_tokens`.

## Streaming (`stream: true`)
```javascript
const stream = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [{ role: "user", content: "Write a long story about a dog." }],
  stream: true,
});

for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content || "");
}
```
(Responses equivalent: `client.responses.create(model, instructions, input)` → `output_text`; for streaming use Responses streaming events — see 01 guides.)

## Function calling / tool use
```javascript
const response = await client.chat.completions.create({
  model: "gpt-5.6-luna",
  messages: [{ role: "user", content: "What's the weather in San Francisco?" }],
  tools: [
    {
      type: "function",
      function: {
        name: "get_weather",
        description: "Get the current weather in a given location",
        strict: true,
        parameters: {
          type: "object",
          properties: {
            location: { type: "string", description: "The city and state, e.g. San Francisco, CA" },
            unit: { type: "string", enum: ["celsius", "fahrenheit"], description: "The temperature unit" },
          },
          required: ["location", "unit"],
          additionalProperties: false,
        },
      },
    },
  ],
});
```
Responses tool-loop equivalent (Python):
```python
import os
import json
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)


def get_current_weather(location, unit):
    return {"location": location, "temperature": "18", "unit": unit or "celsius", "condition": "partly cloudy"}


tools = [
    {
        "type": "function",
        "name": "get_current_weather",
        "description": "Get the current weather in a given location.",
        "strict": True,
        "parameters": {
            "type": "object",
            "properties": {
                "location": {"type": "string"},
                "unit": {"type": ["string", "null"], "enum": ["celsius", "fahrenheit", None]},
            },
            "required": ["location", "unit"],
            "additionalProperties": False,
        },
    }
]

input_items = [{"role": "user", "content": "هوای سان‌فرانسیسکو را با واحد سانتی‌گراد بگو."}]

response = client.responses.create(model="gpt-5.6-sol", input=input_items, tools=tools)

input_items += response.output

for item in response.output:
    if item.type == "function_call":
        args = json.loads(item.arguments)
        result = get_current_weather(args["location"], args.get("unit"))
        input_items.append(
            {"type": "function_call_output", "call_id": item.call_id, "output": json.dumps(result)}
        )

final_response = client.responses.create(model="gpt-5.6-sol", input=input_items, tools=tools)

print(final_response.output_text)
```
Mapping: `tool_calls` → `response.output` items with `type == "function_call"`; return results as `function_call_output` with the same `call_id`; when managing the tool loop manually keep prior `response.output` items (especially for reasoning models).

## Audio input & output
OpenAI audio models (`gpt-audio`, `gpt-audio-mini`) support audio/text input & output via Chat Completions. ⚠ Per 10-deprecations: `gpt-audio`, `gpt-audio-mini` (and 4o-audio previews) are scheduled for shutdown **2027-01-20** → `gpt-audio-1.5`.
### Text-to-speech with Gemini 3.8
- `gemini-3.8-flash-tts`: creative quality, emotional delivery, regional accents, stable long-form speech. `gemini-3.8-flash-lite-tts`: high throughput, low latency, everyday read-aloud. Both **take text and produce audio**; not for transcription, audio-input chat, Live API or reasoning.
- AvalAI serves these TTS models **only** via native `/v1beta/models`, `/v1/chat/completions` and `/v1/audio/speech`. Don't send to `/v1/responses`, `/v1/messages` or legacy `/v1/text:synthesize`. Write the answer with a chat/reasoning model first, then pass final text to TTS.
```bash
curl --fail-with-body -sS https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gemini-3.8-flash-tts",
    "messages": [{"role": "user", "content": "Have a wonderful day!"}],
    "modalities": ["audio"],
    "audio": {"voice": "Zephyr", "format": "pcm16"}
  }' \
  --output chat-speech.json

python3 - <<'PYTHON'
import base64
import json
from pathlib import Path

response = json.loads(Path("chat-speech.json").read_text())
data = response["choices"][0]["message"]["audio"]["data"]
Path("speech.pcm").write_bytes(base64.b64decode(data, validate=True))
PYTHON

ffmpeg -f s16le -ar 24000 -ac 1 -i speech.pcm speech.wav
```
It reads the given text (doesn't answer questions, no audio input). In Chat the Base64 is in `choices[0].message.audio.data` — **not** `message.content`. `pcm16` = signed 16-bit little-endian PCM, **24,000 Hz, mono, no header** → save raw and convert with explicit input params. Don't use `.content` as a fallback; don't strip "DEPRECATED" from Base64. Native non-streaming 3.8 response is **WAV by default** — check `mimeType` before adding a header. For per-part `speechMetadata` and migration from `gemini-3.1-flash-tts-preview`/`gemini-2.5-flash-tts`/`gemini-2.5-pro-tts` see /fa/guides/text-to-speech#migrate-to-gemini-38-tts.
### Audio parameters
| Param | Type | Req | Description |
|---|---|---|---|
| `modalities` | array | no | output modalities; `["text","audio"]` for audio output. For image-generating models (`gemini-3-pro-image`, `gemini-3.1-flash-image`, `gemini-3.1-flash-lite-image`, `gemini-2.5-flash-image`) use `["image","text"]`. Default `["text"]` |
| `audio` | object | no | audio-output config; required when requesting audio output |
`audio` object: `format` ∈ `mp3`, `wav`, `pcm16`, `opus`, `aac`, `flac` (default `mp3`) · `voice` ∈ `alloy`, `echo`, `fable`, `onyx`, `nova`, `shimmer` (default `alloy`).
### Basic audio generation
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "model": "gpt-audio",
    "messages": [{"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."}],
    "modalities": ["text", "audio"],
    "audio": {"format": "mp3", "voice": "nova"}
  }'
```
```python
from openai import OpenAI

client = OpenAI(api_key="avalai-api-key", base_url="https://api.avalai.ir/v1")

response = client.chat.completions.create(
    model="gpt-audio",
    messages=[{"role": "user", "content": "محاسبات کوانتومی را به زبان ساده توضیح بده."}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "nova"},
)

audio_data = response.choices[0].message.audio.data        # Base64 audio
transcript = response.choices[0].message.audio.transcript  # transcript
```
```javascript
const response = await client.chat.completions.create({
    model: "gpt-audio",
    messages: [{ role: "user", content: "محاسبات کوانتومی را به زبان ساده توضیح بده." }],
    modalities: ["text", "audio"],
    audio: { format: "mp3", voice: "nova" },
});
const audioData = response.choices[0].message.audio.data;
const transcript = response.choices[0].message.audio.transcript;
```
(Go/PHP versions use `Modalities`/`Audio` params the same way and read `.Audio.Data`/`.Audio.Transcript`.)
Play from a terminal (one-off commands; needs `jq`; nothing to add to shell profiles):
```zsh
# macOS (zsh)
curl -sS "https://api.avalai.ir/v1/chat/completions" -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" -d '{…as above…}' \
  | jq -r '.choices[0].message.audio.data' | base64 -D > output.mp3
afplay output.mp3
```
```bash
# Linux
… | jq -r '.choices[0].message.audio.data' | base64 --decode >output.mp3
ffplay -nodisp -autoexit output.mp3
```
```powershell
# Windows PowerShell
$response = curl.exe -sS "https://api.avalai.ir/v1/chat/completions" `
  -H "Content-Type: application/json" `
  -H "Authorization: Bearer $env:AVALAI_API_KEY" `
  -d '{ "model": "gpt-audio", "messages": [...], "modalities": ["text","audio"], "audio": {"format":"mp3","voice":"nova"} }' | ConvertFrom-Json

[IO.File]::WriteAllBytes((Join-Path $PWD "output.mp3"), [Convert]::FromBase64String($response.choices[0].message.audio.data))
Start-Process .\output.mp3
```
Responses equivalent for `gpt-audio`: `client.responses.create(model="gpt-audio", input="…")` → `output_text` (page note: `gpt-audio-1.5` may not be enabled for `/v1/responses`; the page's gpt-audio-1.5 Responses example is set to `gpt-5.6-sol`).
### Audio response format
```json
{
  "id": "chatcmpl-123",
  "object": "chat.completion",
  "created": 1763042146,
  "model": "gpt-audio-2025-08-28",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": null,
        "audio": {
          "id": "audio_abc123",
          "data": "SUQzBAAAAA...",
          "expires_at": 1763045747,
          "transcript": "محاسبات کوانتومی یک فناوری انقلابی است..."
        }
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 12, "completion_tokens": 75, "total_tokens": 87,
    "completion_tokens_details": {"audio_tokens": 58, "text_tokens": 17},
    "prompt_tokens_details": {"audio_tokens": 0, "text_tokens": 12}
  }
}
```
### `gpt-audio-1.5` for premium audio quality (best audio model, 256K context)
```python
response = client.chat.completions.create(
    model="gpt-audio-1.5",
    messages=[{"role": "user", "content": "هوای امروز چطور است؟"}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "nova"},
)
```
### `gpt-audio-mini` for cost-effective processing
```python
response = client.chat.completions.create(
    model="gpt-audio-mini",
    messages=[{"role": "user", "content": "هوای امروز چطور است؟"}],
    modalities=["text", "audio"],
    audio={"format": "mp3", "voice": "alloy"},
)
```
### Legacy audio models (still available per page): `gpt-4o-audio-preview`, `gpt-4o-mini-audio-preview` (⚠ scheduled shutdown — see 10-deprecations).
> **Audio input:** for `input_audio` use a compatible chat model such as `gpt-audio-mini` (/fa/examples/processing_audio_in_chat_completion_api). Gemini TTS models accept text only. For dedicated file transcription use the Audio transcription API (/fa/api-reference/audio).

## Errors
400 bad request · 401 unauthorized (wrong key) · 403 forbidden · 404 not found · 429 rate limited · 500 internal error. See /fa/guides/error-handling.

## Related
/fa/models/model-details · authentication.md · 09-rate-limits.md · responses (PENDING) · /fa/guides/structured-outputs · /fa/guides/reasoning · /fa/guides/prompt-caching
