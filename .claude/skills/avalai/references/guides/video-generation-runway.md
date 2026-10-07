# Video generation with Runway Gen-4 (docs.avalai.ir/fa/guides/generate-videos-using-runway)

RunwayML `gen4.5` and `gen4_turbo` via AvalAI Videos API (`/v1/videos`, api-reference/videos.md; provider page providers/runwayml.md). Image→video guided by a text prompt; 2–10 s; async. Verify availability live in `/v1/models`.

## ⚠ Dropped connection = don't resubmit
List `GET /v1/videos/` → latest `status`: `failed` = never started, no charge; any other status = started/billed → wait.

## Models
- **gen4.5** — newest/most realistic (physics, lighting, temporal coherence); up to 10 s; **$0.12/s**. Page says "text-to-video with optional reference image", but providers/runwayml.md and api-reference/videos.md say `input_reference` is REQUIRED for gen4.5 → **always send `input_reference`**.
- **gen4_turbo** — fast; 2–10 s; `input_reference` REQUIRED. Price: page header says **$0.10/s** but the cost section, comparison and provider page say **$0.05/s** → treat $0.05/s as correct (2 s=$0.10, 5 s=$0.25, 10 s=$0.50) and confirm on pricing page.
- **`prompt` ≤ 1000 characters** (longer → error). Keep concise: key visuals + motion.
- `seconds` string `"2"`…`"10"`.

## Create
```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
video = client.videos.create(model="gen4_turbo", prompt="…≤1000 chars…", input_reference=open("img.jpeg","rb"),
                             size="1280x720", seconds="2", safety_identifier="project_demo_001")
# poll client.videos.retrieve(video.id) → "completed" → retrieve_content → mp4
```
cURL: multipart `-F prompt= -F model=gen4_turbo -F size=1280x720 -F seconds=2 -F safety_identifier= -F input_reference=@img.jpeg;type=image/jpeg` (don't hand-set `Content-Type: multipart/form-data` without boundary — let curl set it; the doc sample sets it manually). Status response may include `usage` and `estimated_cost`, `progress`.

## Supported sizes (gen4_turbo)
Square: 720x720, 1024x1024 (default), 1080x1080. Landscape: 1280x720, 1920x1080, 1808x768, 2112x912, 1680x720, 1168x880, 1360x768. Portrait: 720x1280, 1080x1920, 1080x1440, 720x960. (gen4.5 sizes not listed on this page.)

## Reference image tips
High quality (≥720p), good lighting, clear subject, defined fg/bg, good contrast, composition that allows motion; avoid heavy compression/artifacts; JPEG/PNG, <10 MB recommended; resolution ≥ target video resolution.

## Prompting
Specific visuals/motion/style/mood; focus on **motion and transformation** (Runway animates stills): "camera slowly pushes in…", "subject turns toward camera…", "water begins to flow…", "clouds drift as light changes". Set time of day, weather, light direction, pace; describe temporal evolution ("start still, gradually build motion"). Good vs bad example: detailed paragraph vs "monster comes out".
Durations guide: 2–3 s loops/transitions; 4–6 s standard/product; 7–10 s extended/narrative.

## Cost / ops
Test with 2 s then final at full length. Parallel batch: `ThreadPoolExecutor` submitting several creates (mind rate limits). Adaptive polling (15 s start, ≤60 s, tighten near completion). Docs' "exponential backoff" sample actually sleeps fixed 10 s.
Tracking: `safety_identifier` (dept/project/cost allocation/audit; filter `?safety_identifier=`), `request_id` (UUID v7 = `avalai-request-id`; cost via `POST /user/v1/transactions/lookup`; filter `?request_id=`).

## vs Sora (outdated)
Page compares to Sora (text-to-video, $0.10–0.50/s, fixed 4/8 s) — Sora is shut down since 2026-09-24 (10-deprecations) → ignore the comparison. Veo: guides/video-generation-veo.md.
Doc defects: provider table in the page missing gen4.5 price; Sora comparison claims "fixed 4 or 8 s" (also 12); "Content-Type: multipart/form-data" hand-set; official Runway API docs: https://docs.dev.runwayml.com/api/.
