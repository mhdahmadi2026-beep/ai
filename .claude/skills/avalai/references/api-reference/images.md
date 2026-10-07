# Images API — `/v1/images/generations`, `/v1/images/edits` (docs: /fa/api-reference/images)

Create and edit images with models from several providers. Direct, portable path = these endpoints. Hosted `image_generation` tool in `/v1/responses` exists only if the chosen text model + route + account support it (see `fa/guides/image-generation.md#مسیر-مهاجرت-ابزار-تصویر-در-responses`).

## Model choice (OpenAI, newest)
- **`gpt-image-2.5-flare`** = default general choice, faster generation/editing.
- **`gpt-image-2.5-sunburst`** = professional product/ad edits, more precise, slower. Both support generations + edits.
- OpenAI claims Flare cuts generation time up to 50% vs GPT Image 2 — NOT an AvalAI latency guarantee.
- Multi-step edits: save every output, send it as the source image next turn, state what must stay unchanged.
- **Never** put an image-model id in the `model` field of `/v1/responses` (hosted image tool needs a separate text model). Sketch/ChatGPT templates are not API features on AvalAI.
- `gpt-6-sol`, `gpt-6-luna`, `grok-4.7` = vision/reasoning only, **not image generators** — never send to images endpoints. Sol/Luna full on chat/messages/responses; Grok 4.7 full on chat+messages, **partial** on responses. None of those support statements confirm hosted `image_generation` tool access — verify model/route/account. Portable flow: reasoning model analyses/describes → your app calls an image model.
- News: fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added, fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added.

## Generations — `POST https://api.avalai.ir/v1/images/generations`
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | e.g. `gpt-image-2.5-flare` / `-sunburst` |
| `prompt` | string | yes | for GPT Image give a structured description when layout/text/edit precision matters |
| `n` | int | no | default 1 |
| `size` | string | no | common OpenAI: `1024x1024`, `1024x1536`, `1536x1024`; `gpt-image-2` also valid custom sizes |
| `quality` | string | no | model-dependent: `low`/`medium`/`high`/`auto`; **only 2.5 Flare/Sunburst** also `xhigh`, `max` — never send to older models |
| `style` | string | no | legacy models (`vivid`/`natural`) |
| `response_format` | string | no | legacy: `url`/`b64_json`. GPT Image always Base64 → decode `data[0].b64_json` |
| `output_format` | string | no | `png`/`jpeg`/`webp` if route supports |
| `output_compression` | int | no | JPEG/WebP |
| `background` | string | no | keep `auto`/`opaque` unless model/route documents transparency (`gpt-image-2`: no transparent) |
| `moderation` | string | no | GPT Image routes; keep `auto` in prod, `low` only after safety review |
| `stream` | bool | no | if route supports |
| `partial_images` | int | no | 0–3 typically; may get fewer previews if final is quick |
| `user` | string | no | end-user id for abuse monitoring |

Output/cost notes: GPT Image → `data[0].b64_json`; legacy/provider routes may give `url`. Usage may include `input_tokens`/`output_tokens`/image-token details; size, quality, input images, partial previews affect cost+latency. Streaming events: `image_generation.partial_image`, `image_generation.completed`. Prefer `jpeg`/`webp`+`output_compression` for size/latency; `png` for lossless/alpha (only if model supports transparency).

### Basic example
```bash
curl https://api.avalai.ir/v1/images/generations \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"gpt-image-2.5-flare","prompt":"A cute baby sea otter floating on its back in the ocean","n":1,"size":"1024x1024","quality":"medium"}' \
  | jq -r '.data[0].b64_json' | base64 --decode >sea-otter.png
```
```python
import base64, os
from openai import OpenAI
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
r = client.images.generate(model="gpt-image-2.5-flare",
    prompt="A cute baby sea otter floating on its back in the ocean",
    n=1, size="1024x1024", quality="medium")
open("sea-otter.png","wb").write(base64.b64decode(r.data[0].b64_json))
```
```javascript
import fs from "fs"; import OpenAI from "openai";
const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY, baseURL: "https://api.avalai.ir/v1" });
const r = await client.images.generate({ model: "gpt-image-2.5-flare",
  prompt: "A cute baby sea otter floating on its back in the ocean", n: 1, size: "1024x1024", quality: "medium" });
fs.writeFileSync("sea-otter.png", Buffer.from(r.data[0].b64_json, "base64"));
```
Prompt patterns (text in image, localization, compositing, precise edits): fa/examples/generate_images_with_gpt_image.

### Responses hosted tool (only when model+account support it)
```python
response = client.responses.create(
    model="gpt-5.6-luna",
    input="Generate a friendly mascot for an API documentation site.",
    tools=[{"type":"image_generation","action":"generate","size":"1024x1024","quality":"medium"}],
)
calls = [i for i in response.output if i.type == "image_generation_call"]
if calls: open("docs-mascot.png","wb").write(base64.b64decode(calls[0].result))
```
(JS equivalent: `response.output.find(i => i.type === "image_generation_call")` → `Buffer.from(call.result,"base64")`.)

Tool options: `type`=`image_generation`; `action` `auto|generate|edit` (edit forces edit when image in context); `size`; `quality` (`low|medium|high|auto`); `output_format`; `output_compression`; `background` (`auto`/`opaque` unless transparency confirmed); `partial_images` (0–3); `input_image_mask` (object, usually file id).

## Provider-specific params (`extra_body`)
Non-OpenAI image models (Black Forest Labs, Alibaba, BytePlus, Google) need extra params via [`extra_body`](fa/guides/provider-specific-params); AvalAI auto-maps them to the provider. Common: `output_format`, `aspect_ratio`, `prompt_upsampling`, `safety_tolerance`, `samples`, `extras`, `image_strength`, `init_image_mode`, `init_image`.
```python
r = client.images.generate(model="flux-1.1-pro", prompt="اژدهای باشکوهی که در میان ابرها پرواز می‌کند",
    size="1024x1024",
    extra_body={"aspect_ratio":"16:9","output_format":"png","safety_tolerance":2,"prompt_upsampling":True},
    response_format="b64_json")  # FLUX: 'url' not supported
```
JS: pass `extra_body: {...}` with `// @ts-expect-error` (SDK has no such typed field; in the Node SDK prefer verifying it is actually forwarded).

### Alibaba Qwen image
Supports both OpenAI-SDK format and native **Dashscope** format on the same `/v1/images/generations`.
```python
# OpenAI format
client.images.generate(model="qwen-image", prompt="…", size="1328x1328", n=1, response_format="url")  # or b64_json
# edit (multipart via requests)
requests.post("https://api.avalai.ir/v1/images/edits",
  headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}"},
  files={"image": open("input_image.jpg","rb")},
  data={"model":"qwen-image-edit","prompt":"…"})
# Dashscope-native format
requests.post("https://api.avalai.ir/v1/images/generations",
  headers={"Authorization": f"Bearer {os.environ['AVALAI_API_KEY']}", "Content-Type":"application/json"},
  json={"model":"qwen-image",
        "input":{"messages":[{"role":"user","content":[{"text":"…"}]}]},
        "parameters":{"size":"1328*1328","prompt_extend":True,"watermark":False,"negative_prompt":"…"}})
```
Dashscope params: `prompt_extend`, `watermark`, `negative_prompt`, `size` (1328×1328, 1664×928, 1472×1140, 1140×1472, 928×1664), `seed`. NB size format: OpenAI-style uses `1328x1328`, Dashscope-native uses `1328*1328`. Params available depend on provider; consult per-model docs.

## Response
```json
{"created":1589478378,"data":[{"b64_json":"iVBORw0KGgo…","revised_prompt":"…"}]}
```
Legacy/provider routes with `response_format:"url"`: `data[].url` (e.g. `https://avalai-generated-images.storage.googleapis.com/image1.png`). Fields: `created` (unix s), `data[]` of `{b64_json?, url?, revised_prompt?}`.

## Edits — `POST https://api.avalai.ir/v1/images/edits` (multipart **or** JSON)
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | see supported list |
| `image` | file/file[] | multipart: yes | one or more sources (GPT Image routes accept several) |
| `images` | array | JSON: yes | each item object with **exactly one** of `image_url` (full URL / `data:` base64 URL) or `file_id`; up to 16 inputs on GPT Image routes when enabled |
| `mask` | file/object | no | multipart: file; JSON: object with exactly one of `image_url`/`file_id`. Same size+format as source; must have alpha channel; transparent area = editable |
| `prompt` | string | yes | describe the **entire final image**, not only the change |
| `n`, `size` | | no | size model-dependent |
| `quality` | string | no | `low|medium|high|auto`; Flare/Sunburst also `xhigh`,`max` |
| `response_format`, `output_format`, `output_compression`, `stream`, `partial_images`, `user` | | no | as above |
| `input_fidelity` | string | no | **do not send for `gpt-image-2`** (always high fidelity); for older routes use high for faces/logos/packaging/screenshots |

Streaming edit events: `image_edit.partial_image`, `image_edit.completed` — partials are previews; store the completed output.
Request formats: multipart for local files (`image`/`image[]`, binary mask); JSON with `images:[{"image_url":"data:image/png;base64,…"}]` (public HTTPS URL or Files-API `file_id` also OK). If a route is multipart-only, upload the raw file instead of Base64.

### Edit models
OpenAI: `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini` · BFL: `flux.1-kontext-pro` · Google: `gemini-3.1-flash-image` (Nano Banana 2; via `/v1/chat/completions` or `/v1beta/`, NOT `/v1/images/edits`; all `imagen-*` removed) · Alibaba: `qwen-image-3.0-pro`, `qwen-image-3.0`, `qwen-image-2.0-pro`, `qwen-image-2.0`, `qwen-image-edit-plus`, `qwen-image-edit`.

### curl edit (Sunburst; Flare identical, swap model)
```bash
curl --fail-with-body https://api.avalai.ir/v1/images/edits \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -F "model=gpt-image-2.5-sunburst" -F "image=@input_image.png" \
  -F "prompt=Change only the background to warm white. Keep the product, logo, texture, camera angle, and composition unchanged." \
  -F "size=1024x1024" -F "quality=high" -F "n=1" >sunburst-response.json \
  && jq -er '.data[0].b64_json' sunburst-response.json | base64 --decode >sunburst-edit.png
```
### SDK edit
```python
with open("input_image.png","rb") as f:
    r = client.images.edit(model="gpt-image-2", image=f, prompt="رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید", size="1024x1024", n=1)
open("edited_image.png","wb").write(base64.b64decode(r.data[0].b64_json))
```
```javascript
const r = await client.images.edit({ model:"gpt-image-2", image: fs.createReadStream("input_image.png"),
  prompt:"رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید", size:"1024x1024", n:1 });
fs.writeFileSync("edited_image.png", Buffer.from(r.data[0].b64_json,"base64"));
```
### JSON edit with Base64 (no SDK)
Result may be `data[0].b64_json`, a `data:` URL in `data[0].url`, or a downloadable URL → handle all three.
```bash
IMAGE_BASE64=$(base64 -i input_image.png | tr -d '\n')   # Linux: base64 -w 0
curl https://api.avalai.ir/v1/images/edits -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"gpt-image-2","prompt":"رنگین کمانی در آسمان بالای کوه‌ها اضافه کنید","images":[{"image_url":"data:image/png;base64,'"$IMAGE_BASE64"'"}],"size":"1024x1024","n":1}' \
 | jq -r '.data[0] | if .b64_json then .b64_json elif (.url // "" | startswith("data:")) then (.url | split(",")[1]) else error("no b64_json or data URL") end' \
 | base64 --decode >edited_image.png
```
```python
def save_image_result(image, output_path):
    if image.get("b64_json"): b = base64.b64decode(image["b64_json"])
    elif image.get("url","").startswith("data:"): b = base64.b64decode(image["url"].split(",",1)[1])
    elif image.get("url"):
        r = requests.get(image["url"], timeout=120); r.raise_for_status(); b = r.content
    else: raise ValueError(f"No image payload found: {image}")
    open(output_path,"wb").write(b)
# POST json={"model":"gpt-image-2","prompt":…,"images":[{"image_url":f"data:image/png;base64,{b64}"}],"size":"1024x1024","n":1}
```

## Pricing / cost (USD per 1M tokens)
**GPT Image 2.5 (Flare & Sunburst, same rates)**: text in $5.00 · image in $8.00 · cached text in $1.25 · cached image in $2.00 · text out $0.00 · image out $30.00.
Estimated **output-image share only** per 1024x1024: low $0.00588 · medium $0.01317 · high $0.05268 · xhigh $0.09366 · max $0.21072. Add prompt text tokens + all reference-image input tokens (cached rate only when eligible). `low` for drafts, `medium` general, `high/xhigh/max` finals; iterate with `low`, render the approved one at `high`.

**`gpt-image-2` edits** are fully token-billed: estimate = prompt text tokens ($5) + all reference-image tokens ($8; $2 cached) + output image tokens ($30). Approx output-image cost (OpenAI calculator; not fixed, excludes prompt/reference tokens):
| quality | 1024x1024 | 1024x1536 | 1536x1024 |
|---|---|---|---|
| low | ~$0.008 | ~$0.012 | ~$0.012 |
| medium | ~$0.032 | ~$0.048 | ~$0.048 |
| high | ~$0.125 | ~$0.187 | ~$0.187 |
(Source page: low = drafts/small assets; medium = most marketing/social/mockups; high = final production assets, print, packaging, precise UI mockups.) Use OpenAI's calculator for exact estimates; real cost via `avalai-request-id` + User API lookup.

## Image-generation models (per page table)
| provider | model | endpoints |
|---|---|---|
| BytePlus | `seedream-5-0-260128` (CoT reasoning, MJ-style aesthetics, prompt optimisation), `seedream-4-5-251128` (multi-image edit) | generations, edits |
| OpenAI | `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst`, `gpt-image-2`, `gpt-image-1.5` | generations, edits |
| OpenAI | `gpt-image-1`, `gpt-image-1-mini` (page says **tiers 3,4,5 only**) | generations, edits |
| BFL | `flux.2-pro` (per-megapixel pricing), `flux-1.1-pro`, `flux.1-kontext-pro` | generations (kontext also edits) |
| Google | `gemini-2.5-flash-image` (Nano Banana) | chat/completions |
| Google | `gemini-3-pro-image` (Nano Banana Pro), `gemini-3.1-flash-image` (Nano Banana 2, up to 4K), `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite, <2 s, 1K) | chat/completions, `v1beta/` |
| Google | `gemini-3-pro-image-preview`, `gemini-3.1-flash-image-preview` — legacy preview aliases; use the non-preview ids | chat/completions |
| Google | `imagen-4.0-{ultra-generate,generate,fast-generate}-001`, `imagen-3.0-{generate-002,generate-001,fast-generate-001}` | ❌ REMOVED (→ `gemini-3-pro-image` for ultra; `gemini-3.1-flash-image` otherwise) |
| Alibaba | `qwen-image-3.0-pro`, `qwen-image-3.0` ($0.04 at 1K/~1MP, $0.075 at 2–4MP, $0.003 per reference image) | generations, edits |
| Alibaba | `qwen-image-2.0-pro` (typography, native 2K; generations + edits), `qwen-image-2.0` (generations, edits), `z-image-turbo` (ultra-fast, thinking mode), `qwen-image` | generations (+edits where listed) |
| Alibaba | `qwen-image-edit-plus` (generations+edits), `qwen-image-edit` (edits) | |
| Cloudflare | `cf.flux-2-klein-9b`, `cf.flux-2-klein-4b`, `cf.flux-2-dev`, `cf.lucid-origin`, `cf.phoenix-1.0` | generations |

**Variations** (`POST /v1/images/variations`): no supported variation model listed → compatibility placeholder; use `/edits` with a source image or `/generations` with a detailed brief.

## Errors & moderation
400 bad request (e.g. prompt too long) · 401 bad key · 403 forbidden · 404 not found · 429 rate limit · 500 server. See fa/guides/error-handling.
Input-fixable image errors: **do not auto-retry** with the same prompt/mask/source. Moderation errors: `error.code = "moderation_blocked"`, optional `moderation_details`: `moderation_stage` ∈ `input|output|unknown`, `categories` (generic: `harassment`, `self-harm`, `sexual`, `violence`…). Log details for dev/support; show end users a short generic actionable message. All image requests are moderated (fa/safety/content-policy).

## Related
fa/models/model-details · fa/examples/generate_images_with_gpt_image · fa/guides/image-generation · authentication · fa/guides/rate-limits.

## ⚠ Source inconsistencies to respect
- `seedream-4-5-*`, `gpt-image-1/1-mini/1.5` appear here as live but deprecations page lists gpt-image-1/1-mini/1.5 shutting down 2026-12-01 and some Seedream/Imagen ids removed — **live `/v1/models` + 10-deprecations.md win**.
- Responses example uses `gpt-5.6-luna` (id differs from `gpt-6-luna` elsewhere); verify via `/v1/models`.
- Edit examples use `gpt-image-2` while headline recommends 2.5 Flare/Sunburst; edit table lists `gemini-3.1-flash-image` under `/v1/images/edits` section but it is only reachable via chat/v1beta.
