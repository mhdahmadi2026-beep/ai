# Stability AI provider page (docs: /fa/providers/stability)

Image generation via AWS Bedrock; `client.images.generate(...)` with extras in `extra_body`. ⚠ 10-deprecations.md lists Stability ids as removed — **verify live; probably unavailable**.
- ⚠ Prompts must NOT contain **U+200C (ZWNJ / half-space)** → request fails. Use **English prompts** (weak Persian/non-English understanding).
- Models: `stability.sd3-large-v1:0` ~~deprecated~~; `stability.sd3-5-large-v1:0` (SD3.5 Large; realistic, strong prompt following); `stability.stable-image-core-v1:0` / `:1` (balanced quality/speed); `stability.stable-image-ultra-v1:0` / `:1` (highest quality).
- `extra_body` params: `negative_prompt`, `seed`, `mode` (`text-to-image`|`image-to-image`; default text-to-image), `strength` (default 0.8, with image-to-image), `output_format` (png), `aspect_ratio` (model-specific). Sizes: SD3 ≈512×512–1024×1024; Stable Image may support more ratios. `response_format` `url` or `b64_json`.
```python
client.images.generate(model="stability.stable-image-ultra-v1:1", prompt="…", size="1024x1024",
    extra_body={"seed":54321,"negative_prompt":"blurry","mode":"text-to-image"})
```
Best practices: detailed prompts, negative prompts, fixed seeds, right mode, structured prompt (subject → details → style → lighting).
