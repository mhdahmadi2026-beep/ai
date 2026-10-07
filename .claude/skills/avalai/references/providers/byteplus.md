# BytePlus (Seedream) provider page (docs: /fa/providers/byteplus)

Use English prompts (≤600 words). Support: t.me/AvalAISupport. ⚠ deprecations list `seedream-4-0-250828`, `seedream-4-5-251128` as removed → use 5.0.
## `seedream-5-0-260128` — Seedream 5.0
Text→image & image editing; ≤4K (4096²); JPEG/PNG; inputs: text, image URL, Base64; batch up to **15 images/request**; **≤10 reference images**; streaming supported; built-in chain-of-thought prompt optimization; MJ-style aesthetics; strong typography. **$0.035/image.**
Endpoints `/v1/images/generations`, `/v1/images/edits`.
```python
client.images.generate(model="seedream-5-0-260128", prompt="…", size="4K", response_format="url",
    extra_body={"sequential_image_generation":"disabled","watermark":False})
client.images.edit(model="seedream-5-0-260128", image="https://…jpg", prompt="…", size="2K", response_format="url", extra_body={…})
# multi-image blend: extra_body={"image":[url1,url2,url3],"sequential_image_generation":"disabled","size":"2K","watermark":False}
# streaming (raw HTTP): {"model":…,"prompt":…,"size":"2K","stream":True,"sequential_image_generation":"auto","sequential_image_generation_options":{"max_images":3}}
```
(Python SDK `images.edit(image=<url str>)` isn't valid in the OpenAI SDK — upload file or use raw HTTP.)
Params: `size` "1K"|"2K"|"4K" or "WxH" (default 2048x2048); `response_format` url|b64_json; extras: `sequential_image_generation` auto|disabled, `sequential_image_generation_options{max_images 1–15}`, `stream`, `watermark` (default true — set false), `image` (string/array). Recommended sizes: 1:1 2048², 4:3 2304×1728, 3:4 1728×2304, 16:9 2560×1440, 9:16 1440×2560, 3:2 2496×1664, 2:3 1664×2496, 21:9 3024×1296; aspect 1:16–16:1.
Input images: JPEG/PNG only, ≤10 MB, ≤6000×6000, aspect 1:3–3:1. Limits: moderation filters; high-res slower; max 15 images per request incl. references; **result URLs expire after 24 h** (download promptly). Guide fa/examples/generate_images_with_seedream_4.
