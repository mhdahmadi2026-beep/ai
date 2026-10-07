# Vision (image input) guide

Endpoints: `/v1/responses` (preferred for new multimodal flows) and `/v1/chat/completions` (legacy / routes chat-only). Support depends on model+provider route; test combo before prod.

## Models suggested by docs (verify against catalog/deprecations)
OpenAI gpt-5.5 (+gpt-5.4, -mini, -nano); Gemini 3.5-flash, 3.1-pro-preview, 3.1-flash-lite, 2.5-flash; Anthropic claude-opus-4-7/4-6, claude-sonnet-4-6; Z.AI glm-5v-turbo; Qwen VL; Gemini Robotics-ER `gemini-robotics-er-1.5-preview` (chat).

## Carriers
1. Public URL, 2. base64 data URL, 3. `file_id` (upload `purpose:"vision"` to `/v1/files`, use `{"type":"input_image","file_id":...}` in Responses only; needs file storage enabled), 4. PDF/`input_file` for document pages (extracted text + page images; embedded images in non-PDF docs lost unless converted to PDF).

## Shapes
- Chat: `content:[{type:"text",text}, {type:"image_url", image_url:{url, detail?}}]`
- Responses: `input:[{role:"user", content:[{type:"input_text",text}, {type:"input_image", image_url:"<url or data:...>", detail?}]}]` (image_url is a STRING here).
- Multiple images: several parts; label them ("Image A/B"); keep order; each adds tokens/latency.

## Requirements
PNG, JPEG, WEBP, non-animated GIF. Inline ≤ 20 MB per image on AvalAI (route may differ); OpenAI reference 512 MB payload/1500 images but don't rely on it. No watermarks/logos/NSFW; keep small text readable (crop/enlarge, don't crop context). Gemini: HEIC/HEIF also, up to 3,600 images.

## detail
`low` (~512px, cheap), `high` (text/UI/charts/small objects), `original` (supported models: dense screenshots/localization/computer-use), `auto` (provider decides; on gpt-5.5 auto/omitted behave like `original`). Set explicitly for predictable cost.

## Task design checklist
Choose carrier deliberately; set detail; label multi-image; ask for evidence/uncertainty (don't ask to guess identity/metadata/exact measurements); use Structured Outputs for downstream fields; redact secrets/faces/account numbers/EXIF location before upload.

## Limits
Not for medical imaging; weak on non-Latin text, rotated/flipped, panoramas/fisheye, dashed vs solid lines, precise spatial positions (chess), counting approximate, may hallucinate captions; ignores filenames/EXIF; CAPTCHAs blocked; images may be resized.

## Gemini specifics
- **Base64 only** via AvalAI (URL images unsupported for Gemini).
- Bounding boxes: ask for `[ymin, xmin, ymax, xmax]` normalized 0-1000; to pixels: /1000 × original width (x) / height (y).
- Segmentation (2.5+/3.1): ask for JSON list with box, mask, label.
- Tokens: Gemini 3.1/2.5 Flash 258 tokens if both dims ≤384px, else 768×768 tiles × 258.
- Robotics-ER: points [y,x] and boxes normalized 0-1000, trajectory/waypoints, task decomposition.

## Cost
Tokens depend on model family, image size, count, detail; OpenAI patch-based (32px) for new GPT-5 family vs 512px tiles for GPT-4o/4.1/o-series — don't assume across providers. Read `usage`, then check models/model-details and pricing.

## Defects
- Go Responses sample uses nonexistent `client.CreateResponse`, lowercase `model:`; Chat Go sample uses `openai.F` (openai-go v1) — mixed SDKs.
- "Responses equivalent" blocks use example.com image, not the user's data.
- gemini-3.1-pro-preview / opus-4-6/4-7 may be deprecated (see 10-deprecations.md).

## Audit addendum — `detail` values (image_url.detail / input_image.detail)
- `low`: reduced-resolution pass (OpenAI reference ≈512px view) — cheap; classification, captions, scene gist.
- `high`: higher fidelity — small text, layout, UI details, charts, small objects.
- `original` (supported models/routes, e.g. OpenAI gpt-5.4/5.5 families): preserves most spatial detail — dense screenshots, localization, computer-use-like analysis.
- `auto` (default): provider decides; on OpenAI gpt-5.5 `auto` and omitted behave like `original`; on some older families closer to `high` — check cost via `usage`.
- Multiple images: several `image_url` parts in `messages[].content` (Chat) or `input_image` parts in `input[].content` (Responses); each adds tokens + latency. Upload once with `purpose:"vision"` (Files API) and reference by `file_id` to avoid repeated base64. Rotated/upside-down images and tiny text hurt accuracy — enlarge text, don't crop critical context.
