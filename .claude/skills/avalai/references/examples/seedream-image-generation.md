# Example: image generation/editing with Seedream (slug /examples/generate_images_with_seedream_4 or newer — unconfirmed)

Provider: BytePlus/ByteDance. Reference: providers/byteplus.md, api-reference/images.md, 06-pricing.md ($0.035/image for `seedream-5-0-260128`; check live prices). Only model on this page: **`seedream-5-0-260128`** (CoT reasoning, MJ-style aesthetics, prompt optimisation, t2i + i2i). Older ids (`seedream-4-0-250828`, `seedream-4-5-*`) may be removed/deprecated → verify via `/v1/models` and 10-deprecations.md.

## Features
Sequential image generation (batches), multi-image reference fusion, up to 4K, streaming, `watermark` control, English prompts best.

## Calls (OpenAI Images API + provider params)
```python
client.images.generate(model="seedream-5-0-260128", prompt="…", size="2K", response_format="url",
    extra_body={"sequential_image_generation":"disabled","watermark":False})   # response.data[0].url
client.images.edit(model=…, image=open("in.png","rb"), prompt=…, size="2K", extra_body={…})
```
- `size`: `"1K"|"2K"|"4K"` or explicit `"WxH"` (e.g. `3024x1296` = 21:9, `1440x2560` = 9:16).
- Sequential: `sequential_image_generation:"auto"` + `sequential_image_generation_options:{"max_images":N}` → `response.data` has several images (model decides count; max_images is an upper bound, billed per image generated).
- Multi-image fusion: `extra_body={"image":[url1,url2,url3], …}` on generations (URLs must be publicly reachable).
- Raw HTTP (cURL): provider params at TOP LEVEL of body (`sequential_image_generation`, `watermark`, `size`, `response_format`); edits via JSON with `"image":"https://…"` URL.
- Streaming: `POST /v1/images/generations` with `"stream":true` → SSE lines `data: {...}` with `data[].url/size`.
- Output: hosted URLs (temporary — download/store promptly; typical provider TTL ~24 h, unverified).

## Prompting & ops
Specific subject + style + lighting + composition + technical specs; for edits state change and keep; use 1K for web/fast, 4K for print (slower, costlier); iterate cheaply at 1K; cap `max_images`; retry with backoff on 429/5xx (examples/rate-limit-safe-parallel-requests.md).

## Defects of the source page
- JS sample passes `extra_body: {...}` as an option with `@ts-expect-error`: in the Node SDK unknown top-level keys ARE forwarded, but `extra_body` is NOT a JS-SDK concept → it sends a literal `extra_body` field that the gateway may ignore. Put `sequential_image_generation`, `watermark`, etc. directly in the options object (hide TS error) or use raw `fetch`.
- Python multi-image sample puts `size` inside `extra_body` while other samples use the top-level `size`; `size="3024x1296"` (21:9) and others unverified against supported pixel limits.
- Streaming sample: `line.decode().replace("data: ","")` crashes/skips on `[DONE]` and non-JSON lines (silently `continue`s); no `event:` handling; use an SSE parser.
- "Streaming for batches" tip shows `extra_body={"stream": True,…}` with the SDK → SDK `stream` mishandles; use raw requests.
- `images.edit(image=open(...))` multipart vs cURL JSON edit with URL — both forms shown; which one the gateway accepts depends on route (test).
- Error handler retries ALL exceptions incl. 400/content-policy (wasteful) and `time.sleep(2**attempt)` without jitter.
- `response.data[0].size` printed but not guaranteed in OpenAI schema; sample "تنوع‌های سبک" asks 4 variants in one prompt (sequential mode may return fewer).
- Page title/intro mention only 5.0 while links/index and pricing page list 4.x; `fa/pricing.md` link not captured; content/moderation: provider may reject prompts (see guides/safety-checks.md).
