# Provider-specific parameters (guide)
Params outside the OpenAI spec (BFL, Stability, Google, Anthropic, MiniMax, Qwen, DeepSeek…) pass through the OpenAI-compatible API via **`extra_body`** (Python SDK) — AvalAI detects provider from the model and maps non-OpenAI fields to the provider API; invalid params are filtered. TS/JS: extra fields directly with `// @ts-expect-error` (or `extra_body` object with the same comment); raw HTTP: put them at top level of the JSON body (cURL sample nests them in `"extra_body"` — contradicts; for raw HTTP use top-level fields, verify). Use for: fine control, reproducibility (seed), quality/speed tuning (steps/guidance), safety tolerance/filters, specialised edit ops. Params only work with models of that provider (e.g. `cfg_scale` is ignored by OpenAI image models).

## Common params
Image gen: `cfg_scale` (1–20, ~7.5), `steps` (10–150, 20–50), `seed`, `sampler` (K_DPM_2_ANCESTRAL, K_EULER), `negative_prompt`, `style_preset` (photographic, digital-art, fantasy-art), `aspect_ratio` ("16:9","1:1","9:16"), `output_format` (png|jpeg|webp), `samples` (1–10), `guidance_scale` (1–30), `num_inference_steps` (10–150), `safety_checker` (bool).
Advanced: `prompt_upsampling`, `safety_tolerance` (0 strict … 6 lenient; BFL), `image_strength` (0–1), `init_image_mode` (image_strength|step_schedule), `init_image` (base64), `clip_guidance_preset` (FAST_BLUE, FAST_GREEN), `extras`, `strength`, `fidelity`, `control_strength` (0–2).
Style/composition: `change_strength`, `style_strength`, `composition_fidelity`, `style_image` (base64), `select_prompt`, `grow_mask` (px).
Chat/reasoning: `merge_reasoning_content_in_choices`, `chat_template_kwargs`, `enable_thinking`, `reasoning_split` (MiniMax M2.5 → `reasoning_details`), `parameters` (generic container).
Gemini: `generationConfig` (e.g. `imageConfig`, `thinkingConfig`), `safety_settings`.

## Examples
- BFL: `images.generate(model="flux-1.1-pro", extra_body={"aspect_ratio":"16:9","output_format":"png","safety_tolerance":2,"prompt_upsampling":True})` (FLUX needs `response_format:"b64_json"` — see providers/bfl.md).
- Stability (`stability.sd3-5-large-v1:0`, `stability.stable-image-inpaint-v1:0`, `…style-transfer-v1:0`, `…search-replace-v1:0`): `cfg_scale 8, steps 40, sampler K_DPM_2_ANCESTRAL, seed, negative_prompt, style_preset`; edit extras `strength, guidance_scale, safety_checker`; style transfer `style_image, style_strength, composition_fidelity, change_strength`; search-replace `select_prompt, grow_mask, fidelity, control_strength`. **English prompts required.** ⚠ Stability models likely removed/deprecated on AvalAI (see providers/stability.md + 10-deprecations).
- Imagen: ALL `imagen-*` removed → Nano Banana family.
- Gemini image via Chat (`/v1/chat/completions`): `modalities=["image","text"]`, `extra_body={"generationConfig":{"imageConfig":{"aspectRatio":"16:9"}}}`; result `choices[0].message.images[0]["image_url"]["url"]`. `imageConfig.aspectRatio`: 1:1, 2:3, 3:2, 3:4, 4:3, 4:5, 5:4, 9:16, 16:9, 21:9 (gemini-2.5-flash-image [retired 2026-10-02], gemini-3-pro-image); `imageSize` "1K"|"2K"|"4K" only gemini-3-pro-image (sample writes "4k" lowercase; docs table says "4K" — use `"4K"`). Native v1beta route gives full Gemini params via Google SDK.
- Gemini safety (chat): `extra_body={"safety_settings":[{"category":"HARM_CATEGORY_HARASSMENT","threshold":"BLOCK_MEDIUM_AND_ABOVE"},{"category":"HARM_CATEGORY_HATE_SPEECH","threshold":"BLOCK_LOW_AND_ABOVE"},{"category":"HARM_CATEGORY_SEXUALLY_EXPLICIT",...},{"category":"HARM_CATEGORY_DANGEROUS_CONTENT","threshold":"BLOCK_ONLY_HIGH"}]}` — replaces separate moderation calls (guides/gemini-safety-settings not captured).
- Anthropic chat sample (doc): `claude-sonnet-5` with `enable_thinking`, `merge_reasoning_content_in_choices`, `chat_template_kwargs`, `parameters` — ⚠ looks invented: for Claude 5.x use `thinking:{"type":"adaptive"}` + `output_config.effort` (see reasoning guide); OpenAI chat sample `safety_checker`, `parameters.reasoning_mode` also not real OpenAI params.
- MiniMax M2.5: default thinking inline `<think>…</think>` in content; `reasoning_split:True` → `message.reasoning_details` + clean `content`. Multi-turn: append full assistant message incl. `reasoning_details` (`getattr(msg,"reasoning_details",None)`).

## Best practices
Start with defaults, add params gradually; use sensible ranges (avoid cfg_scale 50, steps 200, safety_tolerance 6 for general use); try/except with fallback to base params; document successful configs (named presets e.g. STABILITY_PHOTOREALISTIC / ARTISTIC); A/B test values; fixed `seed` for reproducible production, no seed for experiments; presets: speed (steps 15, cfg 6, K_EULER), quality (steps 50, cfg 8, K_DPM_2_ANCESTRAL), consistency (fixed seed, cfg 7.5, steps 30).
Troubleshooting: params no effect → wrong model/provider; invalid values → valid ranges; wrong names (`guidance_scale`/`num_steps` vs Stability `cfg_scale`/`steps`) → use provider's names. Check model compat, validate names vs provider docs, change one param at a time, use error handling.

## Defects
- `steps: 20 - 50` in Python sample evaluates to −30 (arithmetic!) — use a number.
- Quickstart link claims "basic provider params".
- Stability/Claude samples likely stale (see above); cURL `extra_body` nesting.
