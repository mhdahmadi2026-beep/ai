# Video generation with Veo 3.1 (docs.avalai.ir/fa/guides/generate-videos-using-veo)

Google Veo 3.1 via AvalAI Videos API (`/v1/videos`, see api-reference/videos.md): text→video, image→video, reference images (character consistency), video extension, **native audio** (dialogue, SFX, ambience), async. Status vs the 2026-09-24 Sora shutdown is NOT stated for Veo → verify live in `/v1/models` before use.

## ⚠ Dropped connection = don't resubmit
List `GET /v1/videos/`, check latest `status`: `failed` → not started, not billed, safe to resend; otherwise started/billed → wait. Filter by `request_id` / `safety_identifier`.

## Models
| Model | Price | Notes |
|---|---|---|
| `veo-3.1-generate-001` | $0.40/s | highest quality, rich audio (dialogue+SFX+ambient) |
| `veo-3.1-fast-generate-001` | $0.15/s | speed/cost: prototyping, social, backend, A/B; audio with SFX |
Both: 16:9 and 9:16; 720p and 1080p (**1080p only 16:9**); `seconds` `"4"|"6"|"8"` (default 8); support input image, reference images, extension. `…-preview` ids also listed in api-reference/videos.md.

## Create (SDK)
```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
video = client.videos.create(model="veo-3.1-fast-generate-001", prompt="...", size="1280x720", seconds="4", safety_identifier="project_demo_001")
print(video.id, video.request_id)
# poll client.videos.retrieve(id) every ~10 s → "completed" → client.with_streaming_response.videos.retrieve_content(id)
```
- Raw HTTP here uses **JSON** (`Content-Type: application/json`) for text-only create; **multipart `-F`** when sending files.
- Image→video: multipart `input_reference=@img.jpg;type=image/jpeg` (used as first frame; good for animating objects, drawings, natural scenes). Example: `size=1920x1080`, `seconds=6`.
- Reference images (≤3, character/object/style consistency): `reference_images=[file,file,file]` (Python/JS) / repeated `-F "reference_images=@x.jpg;type=image/jpeg"`. Page says this uses an **AvalAI extension to the OpenAI SDK** (not in stock SDK typing → may need `extra_body`/raw HTTP; test).
- Extend: `client.videos.extend(video_id=..., prompt=..., seconds="8")` / `POST /v1/videos/{id}/extend` JSON `{prompt, seconds}`. Continues from the **last second (24 frames)** of the existing video; chain for ≥1 min; dialogue/audio continues only if present in that last second; extended videos count as new generations (billed). (`videos.extend` isn't in the stock OpenAI SDK — AvalAI extension; use raw HTTP if the SDK lacks it.)

## `size` → aspect ratio/resolution mapping
| size | orientation | aspect | resolution |
|---|---|---|---|
| 1280x720 | landscape | 16:9 | 720p |
| 1920x1080 | landscape | 16:9 | 1080p |
| 720x1280 | portrait | 9:16 | 720p |
| 1080x1920 | portrait | 9:16 | 1080p |
Rules: `height>width` → 9:16 else 16:9; resolution from the smaller side (≥1080→1080p, ≥720→720p, ≥2160 or larger side ≥3840 →4k — the docs list the 4k rule after the others, effectively unreachable as written; 4k "if supported"). No `size` → 720p 16:9. **1080p portrait is NOT supported** by Veo although the table and the social-media sample use `1080x1920` — expect 400/clamp; use `720x1280`.
Override via `extra_body` (wins over `size`): `{"aspectRatio":"9:16","resolution":"1080p","negativePrompt":"...","personGeneration":"allow_adult"}`; `aspect_ratio` (snake_case) also accepted.

## Prompting
Elements: subject, action, style (sci-fi, noir, cartoon…), camera position/motion (aerial, eye-level, top-down, dolly, POV), composition (wide/close-up/two-shot), focus/lens (shallow, macro, wide-angle), ambiance (blue tones, night, warm). Add time/weather/location/lighting and temporal evolution ("start close-up then pull back").
Audio cues: dialogue in quotes (`"This must be the key," he whispered`), explicit SFX ("tires screeching, engine roar"), ambience ("distant birds, rustling leaves"). Example mixes shot + labelled speakers + sounds.

## Cost
Iterate with `veo-3.1-fast` + 4 s + 720p (1080p only 16:9; use 720p for vertical). Costs fast: 4/6/8 s = $0.60/0.90/1.20 (docs range `$0.60–$1.60` etc. mixes models: std 8 s = $3.20). Build long content by extension.

## Limits
- Latency 11 s min, up to ~6 min at peak (set poll timeout accordingly; docs' "exponential backoff" example actually sleeps fixed 10 s).
- **Videos stored on server only 2 days → download within 2 days.**
- SynthID watermark on all outputs.
- Safety filters can block video/audio; **blocked = not charged**; revise prompt, avoid offensive dialogue.
- EU/UK/CH/MENA: person-generation restrictions; Veo 3.1 only `allow_adult`.
- Reference images: JPEG/PNG, ≤20 MB, clear and relevant.

## Patterns
Sequences: generate scenes separately (each its own call, `"seconds":"8"`); product demos with fast model + audio SFX; per-platform configs (story 9:16/4 s, shorts 9:16/8 s, feed 16:9/4 s). Tracking: `safety_identifier` (dept/project/cost allocation/audit; filter `?safety_identifier=`), `request_id` (UUID v7 = `avalai-request-id`; cost via `POST /user/v1/transactions/lookup`; filter `?request_id=`).
Doc sample defects: sequence sample puts the literal "AVALAI_API_KEY" as the bearer; sequence sample lacks polling; some samples call `client` in snippets without defining it.
