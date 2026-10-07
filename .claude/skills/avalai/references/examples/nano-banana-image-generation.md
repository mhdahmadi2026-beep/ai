# Example: image generation & editing with Nano Banana (Gemini image models) — slug probably /examples/generate_images_with_gemini_2_5_flash (or similar; unconfirmed)

Authoritative model/price tables: providers/google.md (Image models), api-reference/images.md, 06-pricing.md. This page = Chat Completions recipes.

## Models
| Name | id | use |
|---|---|---|
| Nano Banana 2 | `gemini-3.1-flash-image` | high volume, fast; `aspectRatio` + `imageSize` |
| Nano Banana Pro | `gemini-3-pro-image` | pro assets, complex instructions, text rendering; up to 4K |
| Nano Banana | `gemini-2.5-flash-image` | speed/low latency; only `aspectRatio` |
Use stable ids in production; `*-preview` aliases still work but are legacy. ⚠ **Conflict:** page treats `gemini-2.5-flash-image` as the main model, but 10-deprecations.md lists it as retired 2026-10-02 (today 2026-10-07) while providers/google.md calls it stable → verify live availability/ model list before using; default to `gemini-3.1-flash-image`. Also exists: `gemini-3.1-flash-lite-image` (providers/google.md).

## Generate (Chat Completions)
```python
r = client.chat.completions.create(model="gemini-3.1-flash-image",
    messages=[{"role":"user","content":"<English prompt>"}],
    modalities=["image","text"])           # REQUIRED, else no image
m = r.choices[0].message
url = m.images[0]["image_url"]["url"]      # "data:image/png;base64,…"  (images = extra field; guard if missing)
header, b64 = url.split(",",1); ext = header.split(";")[0].split("/")[1]
open(f"out.{ext}","wb").write(base64.b64decode(b64)); m.content  # optional accompanying text
```
Output is a base64 data URL in `message.images[]` (not a hosted URL) — payloads are big; save to storage immediately.

## Edit / transform
User content = `[{"type":"text",…},{"type":"image_url","image_url":{"url":<https URL or data:image/jpeg;base64,…>}}]`; multiple `image_url` parts = multi-image fusion/composition. Say what to change AND what to keep ("keep pose and expression exactly").

## Conversational editing — correct pattern
Page appends only the assistant TEXT (`content`) so the next turn has no image → model can't "see" the previous result. To iterate, re-send the previous image as an `image_url` part (assistant/user message with the data URL) or pass the saved file again with the new instruction. Same for "character consistency": supply the reference image each turn; a text-only reference ("same person as before") does NOT work.

## Gemini-specific params (non-OpenAI)
Python SDK: `extra_body={"generationConfig":{"imageConfig":{"aspectRatio":"16:9","imageSize":"4K"}}}`. aspectRatio: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (all 3 models; 3.1/lite have extras – see google.md). `imageSize` 1K/2K/4K only on 3.1-flash and 3-pro (use uppercase `"4K"`; page shows `"4k"` in code). Alternative: native `/v1beta` API with Google SDK (api-reference/v1beta.md; base_url without /v1) for full control.

## Prompting
English prompts work best (Persian prompts accepted but lower quality; Persian TEXT rendering best on `gemini-3-pro-image`). Be specific: style, lighting, composition, technical params; describe scene, not keywords; reference-based edits: state keep/change; use world knowledge (historical/cultural scenes) but verify accuracy.

## Specs (2.5 Flash Image, page)
32,768 in/out tokens, text+image in/out, cutoff Jun 2025, price in $0.30/1M; out text $2.50, image $30/1M tokens (≈ per-image costs in 06-pricing.md). Limits: text inside images inconsistent, very complex scenes, long latency for high quality.

## Error handling
No image → missing `modalities`, safety block, or empty `images` (check `finish_reason`/`content`); decode failures → split data URL once on first comma; log refusal text; retry only on 429/5xx (examples/rate-limit-safe-parallel-requests.md). Safety settings: guides/gemini-safety-settings.md.

## Defects of the source page (don't copy)
- cURL & JS samples put `"extra_body": {...}` inside the raw JSON body / SDK call: `extra_body` is a Python-SDK-only construct; in raw HTTP (and JS `openai` where unknown fields are passed top-level) send `generationConfig` at the TOP LEVEL of the body. As written the cURL sample does NOT apply the aspect ratio/size.
- JS sample `imageUrl.split(",", 2)` truncates base64 containing no commas fine but `split(",",2)` returns max 2 pieces OK; however Python `response.choices[0].message.images[0]["image_url"]` relies on untyped extra field.
- `safe_extract_image` has the success `print`/`return` wrongly indented inside the `with` block (works but fragile).
- Heading says "Gemini 3 Pro Image Preview" while using stable `gemini-3-pro-image`; comment "imageSize supported by …" fine but `"4k"` casing.
- All "Responses equivalent" blocks are generic placeholders (describe-image with example.com URL, `gpt-5.6-luna`) — NOT image generation. For OpenAI-style image API use `/v1/images/*` (api-reference/images.md).
- Comparison table with GPT Image 1 is stale (GPT Image 1.x shutdown 2026-12-01); the conclusion section repeats marketing.
- Support contact Telegram t.me/AvalAISupport; links guides/image-generation.md and providers/google.md.
