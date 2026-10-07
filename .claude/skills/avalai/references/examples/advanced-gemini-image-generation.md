# Example: advanced image generation with Gemini (Nano Banana) — slug probably /examples/advanced_gemini_image_generation

Companion to examples/nano-banana-image-generation.md (Chat Completions recipes) and imagen-deprecated.md. This page = NATIVE Gemini API (v1beta) recipes via the Google GenAI SDK. Authoritative: providers/google.md, api-reference/v1beta.md, guides/gemini-safety-settings.md.

## Model status (today 2026-10-07)
`gemini-2.5-flash-image` **stopped 2026-10-02** → don't use for new work; use `gemini-3.1-flash-image` (Nano Banana 2) or `gemini-3-pro-image` (Pro: up to 4K `imageSize` 1K/2K/4K, thinking on by default, Google Search grounding, ≤14 reference images (5 high-fidelity)); `gemini-3.1-flash-lite-image` for speed/1K. Page claims 2.5 = 1K only, ≤3 input images, no search grounding.

## Native API (recommended)
- SDK: `genai.Client(api_key=KEY, http_options={"base_url":"https://api.avalai.ir"})` (api_version defaults to v1beta; no /v1). JS `@google/genai`: `httpOptions:{baseUrl:"https://api.avalai.ir"}` (**`baseUrl`, not `baseURL`**). Raw: `POST https://api.avalai.ir/v1beta/models/<id>:generateContent`, header `x-goog-api-key` (or Bearer).
- Generate: `client.models.generate_content(model, contents=[prompt])`; loop `response.parts`: `part.text` / `part.inline_data` (`part.as_image().save()`); JS `part.inlineData.data` (base64).
- Edit: `contents=[prompt, PIL.Image]` (Python); raw `parts:[{text},{inline_data:{mime_type,data}}]`.
- Config: `types.GenerateContentConfig(response_modalities=["TEXT","IMAGE"], image_config=types.ImageConfig(aspect_ratio="16:9", image_size="2K"), tools=[{"google_search":{}}])` (search grounding only on Pro/3.x).
- Multi-turn: `chat = client.chats.create(model=…, config=…)`; `chat.send_message(msg, config=…)` — native chat history keeps images, so iterative edits work (unlike Chat Completions text-only history).
- Aspect ratios: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (3.x models add extremes — google.md).
- OpenAI-compatible route: chat/completions + `modalities` + `extra_body.generationConfig.imageConfig` (see nano-banana-image-generation.md).

## Prompting
English prompts; specify subject, lighting, style, camera, aspect; for edits state keep/change; negative hints as plain-text phrases; match ratio to use. Safety: `safetySettings` (see gemini-safety-settings.md) — Imagen-era `person_generation`/`safety_filter_level` do NOT apply to Gemini image models.

## Defects of the source page (many calls don't exist)
- `client.models.generate_image(...)`, `types.GenerateImageConfig`, `response.image.save()`, `ai.getGenerativeModel(...).generateImage(...)`: these are NOT in the Google GenAI SDKs for Gemini image models (generate_images belongs to Imagen, now removed). Use `generate_content` (+`image_config`).
- `types.Part.from_image(image=…)` doesn't exist (use `contents=[image, prompt]` or `Part.from_bytes`). JS `ai.getGenerativeModel` is legacy-SDK API, not `@google/genai`.
- JS `httpOptions:{ baseURL }` wrong key (`baseUrl`); `extra_body:` object in the JS OpenAI SDK and raw cURL isn't a real parameter → put `generationConfig` at top level; `"imageSize":"4k"` should be `"4K"`.
- `client.images.generate(model="gemini-3-pro-image", size, quality="hd")` + `response.data[0].url`: `/v1/images/generations` isn't a documented route for Gemini image models (images.md: chat/completions); results are base64 data, not URLs.
- bash samples parse JSON with `grep -o '"data": "[^"]*"' | cut` — brittle (formatting/multiple parts/`jq` instead: `jq -r '.candidates[0].content.parts[]|select(.inlineData)|.inlineData.data'`); BSD/GNU base64 flag detection hack; Go sample unverified (`genai.ClientConfig.BaseURL` doesn't exist → `HTTPOptions.BaseURL`).
- Error handling imports `google.api_core.exceptions` (not what google-genai raises → `google.genai.errors.APIError`, `.code`).
- Comparison table: "2.5 Flash Image = stable" is now false; "3 Pro Image Preview" vs stable id `gemini-3-pro-image`; page's Responses-equivalent blocks are placeholders; support email support@avalai.ir; links `fa/examples/stability_ai_image_editing.md`, `fa/guides/generate-videos-using-veo.md`, `fa/providers/gemini.md` not captured (veo guide exists as guides/video-generation-veo.md).
