# Image generation guide

See api-reference/images.md + providers (openai, google, bfl, byteplus, alibaba, runwayml). Deprecations (10-deprecations.md) override model lists below.

## Endpoint choice
- Default production: `/v1/images/generations` and `/v1/images/edits` (choose model yourself).
- `/v1/responses` + `tools:[{"type":"image_generation"}]` only if model+route+account support the hosted tool (separate capability from Responses endpoint support). Never put a GPT Image id in Responses `model`; use a main text model (e.g. gpt-5.x) which calls the tool. `action`: auto|generate|edit; `tool_choice={"type":"image_generation"}` to force; read `image_generation_call.result` (base64), `.revised_prompt`. Keep generated image/file ids in app state for multi-turn edits. If tool unavailable: Image API, save image, pass as context next turn.
- Streaming `partial_images` (1-3) route-dependent; previews aren't final assets; may cost tokens.
- `gpt-6-sol`, `gpt-6-luna`, `grok-4.7` understand images but are NOT image generators (don't use in images endpoints). Two-step: reasoning model writes a description → app sends it to `gpt-image-2.5-flare` (for edits, resend the source image).

## GPT Image models (direct API)
| model | generations | edits | note |
|---|---|---|---|
| gpt-image-2.5-flare | ✓ | ✓ | default general; fast (OpenAI claims -50% time vs v2) |
| gpt-image-2.5-sunburst | ✓ | ✓ | pro/precise edits, slower |
| gpt-image-2 | ✓ | ✓ | previous gen |
| gpt-image-1.5 | ✓ | ✗ | |
| gpt-image-1 | ✓ | ✓ | (shutdown 2026-12-01 per deprecations) |
| gpt-image-1-mini | ✓ | ✓ | cheap drafts (same shutdown note) |
Quality: low|medium|high; `xhigh`/`max` ONLY on 2.5 flare/sunburst. Output is base64 (`b64_json`); `output_format` png|jpeg|webp, `output_compression`. Transparent background not supported for gpt-image-2 (keep `auto`/`opaque`). Don't send `input_fidelity` to gpt-image-2 (always high); on older GPT Image use `high` for faces/logos/UI. `moderation:"auto"` in prod.
Pricing 2.5 (same for flare & sunburst, $/1M tokens): text in 5.00 / cached 1.25; image in 8.00 / cached 2.00; text out 0; image out 30.00. Est. image-output cost per 1024² : low 0.00588, medium 0.01317, high 0.05268, xhigh 0.09366, max 0.21072 (+ prompt input; edits add all reference image inputs).
Sizes: 1024x1024, 1536x1024, 1024x1536; gpt-image-2 custom: longest ≤3840, both multiples of 16, ratio ≤3:1, pixels 655,360–8,294,400 (>2560x1440 experimental).

## Other models (docs list)
Seedream `seedream-5-0-260128` (sequential up to 15, multi-image, 4K, t2i+i2i; see examples). Google Nano Banana: gemini-3.1-flash-image (default; replaces imagen-4 generate/fast), gemini-3-pro-image (replaces imagen ultra), gemini-3.1-flash-lite-image (<2s 1K), gemini-2.5-flash-image (**retires 2026-10-02 — already past; avoid**). ALL `imagen-*` removed. FLUX: flux.2-pro ($0.03 first MP, +0.015/MP, +0.015/MP per ref image; English only), flux-1.1-pro, flux.1-kontext-pro. Qwen: qwen-image-3.0-pro / 3.0 (gen+edit; 1K ≈$0.04, 2–4MP $0.075, $0.003 per ref image), qwen-image-2.0-pro $0.075, qwen-image-2.0 $0.04, z-image-turbo $0.015 (thinking $0.03), qwen-image-edit-plus $0.03, qwen-image, qwen-image-edit. English prompts work best everywhere. Variations: NOT implemented.

## Provider-specific params
Pass non-OpenAI params through `extra_body` (e.g. FLUX: `aspect_ratio`, `output_format`, `safety_tolerance`, `prompt_upsampling`, `samples`, `image_strength`, `init_image`, `init_image_mode`, `extras`). TS: `// @ts-expect-error` for extra_body. FLUX: use `response_format:"b64_json"` (see providers/bfl.md).
Qwen dual format: OpenAI SDK form (`size` e.g. "1328x1328") OR native DashScope JSON body `{model, input:{messages:[{role,content:[{text}]}]}, parameters:{size:"1328*1328", prompt_extend, watermark, negative_prompt, seed}}`; edits: content `[{image:url|base64},{text}]`. Aspect sizes 1328², 1664×928, 1472×1140, 1140×1472, 928×1664.

## Edits
Image + mask same dimensions, mask needs alpha; prompt describes the WHOLE desired final image + say what to keep unchanged. JSON edit form: `images:[{image_url:"data:image/png;base64,..."}]` (each object exactly one of image_url|file_id), mask same shape; multipart form for binary uploads (`image=@`, `mask=@`; <50MB guideline). Multi-turn: save last output and resend as source. In-memory: set `.name="x.png"` on BytesIO. Result may be `b64_json`, data URL in `url`, or http `url` → handle all three.

## Prompt brief template
Goal / Format / Canvas / Subject / Composition / Style / Text (exact, quoted) / Constraints (no watermark, preserve logo/layout/colors). low = draft, medium = general, high = dense text/infographic/product close-ups/final.

## Moderation & errors
Don't blind-retry blocked requests; log request id/endpoint/model/code. `moderation_blocked` (+ optional `moderation_details`: `moderation_stage` input|output|unknown, categories) and `image_generation_user_error` → change prompt/image/mask/size first. Show generic user message.

## Source defects
- Examples use `gpt-image-2` and `quality="medium"` fine; FLUX example uses `response_format="url"` (contradicts bfl.md: b64_json only).
- `data/models.json` is referenced (internal file) — not accessible.
- Responses sample uses gpt-5.6-luna. Cache rate line "text out $0.00".
- Python edit sample mixes in-memory sample with undefined `image` variable; Qwen edit sample uses `requests` with `files` + `data` while docs elsewhere show JSON.
