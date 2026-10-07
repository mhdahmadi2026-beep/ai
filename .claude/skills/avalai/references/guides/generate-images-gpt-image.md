# Generating images with GPT Image models (docs.avalai.ir/fa/examples/generate_images_with_gpt_image — slug inferred from 10-deprecations)

> ⚠ **PAGE IS BEHIND THE CATALOG.** It centres `gpt-image-2` and presents `gpt-image-1.5`, `gpt-image-1`, `gpt-image-1-mini` as live options. Per 10-deprecations.md: `gpt-image-1-mini`, `gpt-image-1.5`, `chatgpt-image-latest` shut down **2026-12-01** → `gpt-image-2.5-sunburst`/`-flare`; `gpt-image-1` → same. Current defaults: **`gpt-image-2.5-flare`** (general/fast) and **`gpt-image-2.5-sunburst`** (precise edits) — see guides/image-generation.md (quality `xhigh`/`max` only on 2.5). Treat `gpt-image-2` as previous generation; **don't recommend 1.5/1/1-mini for new work**. Everything below is valid pattern guidance; swap the model id after checking `/v1/models`.

Prompts: English works best (models optimized for English); support t.me/AvalAISupport.

## Models (per page)
- **gpt-image-2**: best prompt adherence for multi-part prompts, higher visual fidelity, strong text rendering (typography/logos/signs), lower output cost vs 1.5 (text output $32→$10 /1M, image output $32→$30 /1M), works with both `/v1/images/generations` and `/v1/images/edits`. Pricing: text in $5.00/1M (cached $1.25), text out $10.00, image in $8.00 (cached $2.00), image out $30.00 per 1M tokens.
- **gpt-image-1.5** (shutdown 2026-12-01): text in $5/1M (cached $2), text out $32, image in $8, image out $32.
- **gpt-image-1**, **gpt-image-1-mini** (cheaper/faster; page says tiers 3–5; both being retired).
Features: instruction following, realism, quality/size/compression/transparency options, editing/combining multiple images, mask editing; optional Responses `image_generation` tool when the route supports it.

## Production prompt playbook
Short product/creative-brief style prompts: separate what changes from what must stay.
```text
Goal: <what the image is for>
Format: <photo, ad, slide, UI mockup, diagram, product shot>
Canvas: <size, aspect, orientation>
Subject: <main subject, product, person or interface>
Composition: <framing, angle, placement, empty space>
Style: <photorealistic, flat vector, editorial, 3D render, ...>
Text: "<exact text in image>", placement, typography, language
Constraints: no watermark, no extra text, preserve brand colors, keep layout clean
```
- Text in image: exact text in quotes + position + hierarchy; for small labels/dense infographics/multilingual start with `quality="high"`. Example: slide 1536x1024 with headline exactly "Revenue Signals", subtitle "Weekly pipeline health", constraints "no extra words, no watermark, readable text".
- Localization: "Translate all visible English text into Persian. Preserve the original layout, typography hierarchy, colors, icons, logo placement, spacing, arrows, and image content. Do not add new claims or extra text."
- Precise edit: "Change only the chair color to matte black. Keep the camera angle, room layout, lighting, shadows, wall color, floor texture, table position, and all other objects exactly the same."
- Multi-image: "Image 1 is the product photo. Image 2 is the lifestyle background. Place the product from Image 1 on the table in Image 2. Match perspective, contact shadow, color temperature, and scale. Preserve the product label exactly."

## Basic generation
```python
resp = client.images.generate(model="gpt-image-2",  # use current id e.g. gpt-image-2.5-flare
    prompt="…", size="1024x1024", quality="medium")
open("out.png","wb").write(base64.b64decode(resp.data[0].b64_json))
```
JS: `client.images.generate({model,prompt,size,quality})`, `Buffer.from(b64_json,"base64")`.

## Responses image tool (route-dependent)
Default to `/v1/images/generations` for single-step. Use `tools:[{"type":"image_generation","action":"generate","size":"1024x1024","quality":"medium"}]` on `/v1/responses` only if model+account support the hosted tool and the image is part of a conversation/agent/multi-turn edit. `model` = a Responses-capable text model (e.g. `gpt-5.6-luna`); `action`: `generate` (force new), `edit` (only with an input image in context), `auto`; `tool_choice:{"type":"image_generation"}` to force a call (else the model may answer in text). Read `response.output` items `type=="image_generation_call"` → `.result` base64, `.revised_prompt`; if none → fall back to `/v1/images/generations`. Keep `previous_response_id` / file path / image_generation_call id for follow-ups.

## Output options
- `size`: `1024x1024`, `1024x1536`, `1536x1024`, `auto` (default). gpt-image-2 also accepts flexible custom sizes: longest side ≤3840 px, both sides multiples of 16, long:short ≤3:1, total pixels 655,360–8,294,400; start with 1024x1024 / 1024x1536 / 1536x1024 / 2560x1440 and test larger outputs for latency, cost and stability on your route.
- `quality`: `low` | `medium` | `high` | `auto` (default).
- `output_format` (`png`/`jpeg`/`webp`) + `output_compression` 0–100 for jpeg/webp.
- Transparent background: model/route-dependent; OpenAI's current guide says `gpt-image-2` does NOT support `background="transparent"` → use `auto`/`opaque`; on models that support it use `output_format` png/webp with alpha.

## Editing (`POST /v1/images/edits`, multipart)
Prefer the newest model for production edits where identity/labels/layout/fidelity matter. For `gpt-image-2` **don't send `input_fidelity`** (inputs auto-processed at high fidelity); on older routes that expose it use `high` for faces, logos, packaging, UI screenshots. `client.images.edit(model, image=file, prompt, [mask=file])` → `data[0].b64_json`; up to **10** input images (`image=[f1,f2]`); mask with alpha channel for region edits (mask leakage beyond boundaries can happen). Build an alpha mask from a B/W mask with PIL: `mask=Image.open("bw.png").convert("L"); rgba=mask.convert("RGBA"); rgba.putalpha(mask); save PNG`.

## Streaming partial images (route-dependent)
`client.images.generate(..., stream=True, partial_images=2)`; events `image_generation.partial_image` (`partial_image_index`, `b64_json`). Partial = preview only; save the final asset from the complete response.

## Editing cost (gpt-image-2, token-based, no per-edit flat fee)
Pay for prompt text tokens ($5/1M) + input image tokens per reference image ($8/1M, cached $2/1M) + output image tokens ($30/1M) — output tokens dominate. Approx output-only costs (OpenAI calculator estimates, not fixed rates): low 1024² ≈ $0.008, 1024x1536/1536x1024 ≈ $0.012; medium ≈ $0.032 / $0.048; high ≈ $0.125 / $0.187. Quality guide: low = drafts/small assets/automated pipelines; medium = most marketing/content visuals; high = final production assets (hero product shots, print, packaging, detailed UI mockups). Cost tips: iterate at `quality="low"`, re-run only the approved edit at `high`; smallest reference resolution that keeps needed detail; cache repeated references where supported; prefer `1024x1024` when portrait/landscape isn't needed (fewest output tokens per quality).

## Which model (page's guidance; map to 2.5)
New production workflow, best adherence/fidelity, readable text/UI/labels/logos/infographics, edits that keep identity/layout/camera → newest (use `gpt-image-2.5-flare`/`-sunburst`). Legacy validated workflows needing temporary backward compatibility → migrate before 2026-12-01. Cheap/high-volume prototyping → `quality="low"` on the current model (mini is being retired).

## Best practices / limitations
Precise detailed prompts; state style/medium; use reference images; test quality settings; masks + invariants for local edits; store `revised_prompt` for debugging; keep Responses image state (file path/id/`previous_response_id`/`image_generation_call` id) before follow-ups. Limits: outputs may not match the prompt exactly; very complex scenes may not fully render; text rendering can be inconsistent; mask leakage; complex prompts slower than text requests (design queues/loading states); transparent bg model-dependent (not gpt-image-2).
Related: guides/image-generation.md (current defaults/migration), api-reference/images.md, providers/openai.
