# Video generation with Sora (docs.avalai.ir/fa/guides/video-generation)

> ⚠ **LIKELY UNAVAILABLE.** `sora-2`, `sora-2-pro` (+ dated snapshots) and OpenAI's Videos API were shut down by the provider on **2026-09-24** with no replacement (10-deprecations.md; today 2026-10-07). This guide page still documents Sora as live — contradicts the deprecation table. **Don't build new features on Sora; verify any video model live via `/v1/models`** (Veo `veo-3.1-*`, Runway `gen4.5`/`gen4_turbo` per api-reference/videos.md). Kept for patterns that carry over to other video models.

Async API (`/v1/videos`, see api-reference/videos.md): create job → poll → download MP4. Modes: text→video, image→video (`input_reference`), remix existing video.

## ⚠ Dropped connection = don't resubmit (double billing)
List `GET /v1/videos/` and check latest `status`: `failed` → never started, no charge, safe to resend; `queued|processing|completed` → started/billed, wait for it. Can filter by `request_id` / `safety_identifier`.

## Models (as documented — see warning)
- `sora-2`: 720x1280, 1280x720; `seconds` `"4"|"8"|"12"` (min 4, multiples of 4; other values → 400); $0.10/s.
- `sora-2-pro`: also 1024x1792, 1792x1024; $0.30/s standard res, $0.50/s large res.
- Both support reference image + remix. Cost examples: sora-2 4/8/12 s = $0.40/0.80/1.20; pro up to $3.60 at 12 s large.
- `seconds` is a STRING. Docs' cost-optimization Python samples use `requests.post(json={... "seconds": 4})` (int, JSON) while real examples use multipart/SDK strings → use the SDK with string.

## OpenAI Sora concepts vs AvalAI route (route-dependent)
| Workflow | AvalAI today |
|---|---|
| start render | `POST /v1/videos` (`model,prompt,size,seconds`, optional `safety_identifier`) |
| progress | poll `GET /v1/videos/{id}` every 10–20 s; webhooks only if enabled for account |
| download | `GET /v1/videos/{id}/content` → copy to own storage quickly (don't treat as long-term hosting) |
| first-frame guidance | multipart `input_reference` (JPEG/PNG/WebP), match size to target |
| extend/edit | `/videos/extensions` and `/videos/edits` NOT listed → use documented `/remix` only |
| Batch API for video | only if AvalAI confirms; else own queue + polling |
Avoid copyrighted characters/music, real people/public figures, human-likeness uploads unless enabled.

## Python (SDK)
```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
video = client.videos.create(model="sora-2", prompt="...", size="1280x720", seconds="4", safety_identifier="project_abc123")
print(video.id, video.request_id)          # request_id = UUID v7 = avalai-request-id
while True:
    v = client.videos.retrieve(video.id)
    if v.status == "completed":
        with client.with_streaming_response.videos.retrieve_content(video.id) as r, open("out.mp4","wb") as f:
            for c in r.iter_bytes(): f.write(c)
        break
    if v.status == "failed": print(v.error); break
    time.sleep(10)
```
cURL: `-F model= -F prompt= -F size= -F seconds= [-F safety_identifier=] [-F input_reference=@img.jpg;type=image/jpeg]`; remix: `POST /v1/videos/{id}/remix` JSON `{"prompt":...}`; content: `GET /v1/videos/{id}/content --output x.mp4`. JS SDK: `client.videos.create/retrieve/retrieveContent/remix`.
Doc sample defects: status-check example has `from openAI import OpenAI` (typo; must be `openai`); polling "with exponential backoff" example actually sleeps a fixed 10 s; `progress` field may be absent.

## Prompting
Be specific: visuals (colour, lighting, composition), motion (camera moves: pan, slow zoom, drone descent, handheld tracking; subject action), style (cinematic/realistic), mood, time of day, weather, location, temporal evolution ("start close-up then pull back"). Shot type, subject, action, setting, camera, lighting, timing. Vertical sizes for social, horizontal for cinematic.

## Cost strategy
Iterate on `sora-2` + 4 s + lower res first; only use 12 s / pro / large res when prompt+motion+framing are stable; batch related prompts via your own queue.

## Troubleshooting
Timeout → raise poll limit (docs: 60 attempts × 10 s), inspect `error`; invalid size → sora-2 only 720x1280/1280x720; prompt rejected → remove explicit/violent/copyrighted/brand references; reference issues: docs mention base64 + size limits (images 20 MB, videos 512 MB) but the API takes multipart files – verify.

## Tracking
`request_id` (UUID v7, also header `avalai-request-id`) → cost via `POST /user/v1/transactions/lookup`, log correlation, support tickets, filter `GET /v1/videos?request_id=`. `safety_identifier` → department/project tags, cost allocation, multi-service lookup (`?safety_identifier=`).
