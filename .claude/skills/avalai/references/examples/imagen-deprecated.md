# Google Imagen models (DEPRECATED / removed) — slug probably /examples/imagen… (unconfirmed)

All `imagen-*` ids are removed from `data/models.json` (Models API). Don't use old `imagen-*` examples or the v1beta image `:predict` path (`instances:[{prompt}]`, `parameters.sampleCount`) in new AvalAI integrations. Page remains only to help migrate old bookmarks/snippets.

| Removed | Replacement |
|---|---|
| `imagen-4.0-ultra-generate-001` | `gemini-3-pro-image` (Nano Banana Pro) |
| `imagen-4.0-generate-001`, `imagen-4.0-fast-generate-001` | `gemini-3.1-flash-image` (Nano Banana 2) |
| `imagen-3.0-generate-002`, `imagen-3.0-generate-001`, `imagen-3.0-fast-generate-001` | `gemini-3.1-flash-lite-image` (Nano Banana 2 Lite) |

## Replacement guidance
- Google: Nano Banana family via `/v1/chat/completions` (`modalities:["image","text"]` → `choices[0].message.images[0]["image_url"]["url"]`, base64 data URL) or native v1beta `:generateContent`. **`gemini-2.5-flash-image` stops 2026-10-02 (already past)** → use Gemini 3.x image models.
- OpenAI `gpt-image-2` family on `/v1/images/generations|edits` for high quality, in-image text, compositing, mask editing (see guides/generate-images-gpt-image.md for stale-model warnings: prefer `gpt-image-2.5-flare`/`-sunburst`).
- Others still available: FLUX (`flux.2-pro`, `flux.1-kontext-pro`), Qwen Image, Seedream.
- Migration: old `POST /v1beta/models/imagen-4.0-fast-generate-001:predict` → chat call to `gemini-3.1-flash-image` (examples/nano-banana-image-generation.md). Note Imagen's `sampleCount` (1–8), `personGeneration`, negative prompts have no direct chat equivalent; aspect ratio via `generationConfig.imageConfig.aspectRatio` (top-level in raw HTTP / `extra_body` in Python SDK).
- Always verify availability via Models API / model browser, not docs.

## Notes / defects
- The page's Python sample names the result "Image URL" but it is a **base64 data URL** (large) — decode and save.
- Page links `fa/news/2026-09-04-model-deprecations-and-migration-guide.md` (not yet captured) and `data/models.json`.
- Earlier-captured `api-reference/v1beta.md` still documents Imagen-style `instances/parameters` — treat as legacy.
