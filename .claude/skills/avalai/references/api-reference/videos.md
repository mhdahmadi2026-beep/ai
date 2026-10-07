# Videos API — `/v1/videos` (docs: /fa/api-reference/videos)

> ⚠ **STATUS WARNING.** OpenAI's Videos API and `sora-2`/`sora-2-pro` (+ dated snapshots) had a provider shutdown on **2026-09-24** with no replacement (10-deprecations.md); today is 2026-10-07 — **Sora models are likely unavailable**. This page still documents Sora, Google Veo and RunwayML routes. **Verify every video model id live (`/v1/models`) before use; don't build new features on Sora.** Veo (`veo-3.1-*`) and Runway (`gen4.5`, `gen4_turbo`) status isn't confirmed by this page vs. the shutdown — check live.

Async video generation: submit → poll → download. Models: Sora (`sora-2`, `sora-2-pro`), Veo (`veo-3.1-generate-001`, `veo-3.1-fast-generate-001`, `veo-3.1-generate-preview`, `veo-3.1-fast-generate-preview`), Runway (`gen4.5`, `gen4_turbo`).

## ⚠ If the connection drops — don't resubmit (double billing)
Generation/remix are asynchronous; the server starts processing immediately. After a disconnect: `GET https://api.avalai.ir/v1/videos/` (list), inspect the latest video `status`: `failed` → generation never started, **no charge**, safe to resubmit; anything else (`queued`/`processing`/`completed`) → started/finished and **billed**; wait for it instead of duplicating. (Can also find by `request_id`/`safety_identifier` filters.)

## Endpoints
- `POST /v1/videos` create (JSON or multipart w/ `input_reference`)
- `GET /v1/videos/{video_id}` retrieve status
- `GET /v1/videos` list; query `safety_identifier`, `request_id` (filters; `request_id` = the UUID v7 `avalai-request-id`)
- `DELETE /v1/videos/{video_id}` → `{"id","object":"video.deleted","deleted":true}`
- `POST /v1/videos/{video_id}/remix` body `{prompt}` → new video (`remixed_from_video_id` set)
- `GET /v1/videos/{video_id}/content` download file — **only when `status=="completed"`**

## OpenAI-compat notes
Supported contract = the endpoints above. Image reference via multipart `input_reference` (JPEG/PNG/WebP; match target `size`). Webhooks only if AvalAI enabled video events for your account, else poll with backoff. **Characters, extensions, edits (`/v1/videos/characters|extensions|edits`) NOT documented → don't assume.** Batch on `/v1/videos` only if AvalAI confirms (Batch isn't implemented). Download finished videos promptly and copy to your storage (content URLs aren't durable; object has `expires_at`). Guide: fa/guides/generate-videos-using-sora.

## Create body
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | see above |
| `prompt` | string | yes | ≤1000 chars |
| `seconds` | **string** | no | Sora: `"4"`, `"8"`, `"12"` (default `"4"`; min 4); durations should be multiples of 4 generally; unsupported → 400. Runway max 10 s |
| `size` | string | no | default `720x1280` |
| `input_reference` | file | no | multipart image reference |
| `safety_identifier` | string | no | ≤256 chars; internal tracking/filtering (see user.md) |
Sizes: Sora 2 → `720x1280`, `1280x720`. Sora 2 Pro → + `1024x1792`, `1792x1024`. Veo 3.1 (+fast, preview) → `720x1280`, `1280x720`, `1080x1920`, `1920x1080`.

## Examples
```python
video = client.videos.create(model="sora-2", prompt="A calico cat playing a piano on stage under dramatic spotlights", size="1280x720", seconds="4")
while video.status not in ["completed","failed"]:
    time.sleep(10); video = client.videos.retrieve(video.id)
# download: GET /v1/videos/{id}/content (client.videos.download_content in newer SDKs)
```
```bash
curl -X POST https://api.avalai.ir/v1/videos -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" -d '{"model":"sora-2","prompt":"…","size":"1280x720","seconds":"4"}'
# reference image (multipart; don't set Content-Type manually):
curl -X POST https://api.avalai.ir/v1/videos -H "Authorization: Bearer $AVALAI_API_KEY" -F prompt="…" -F model="sora-2" -F size="1280x720" -F seconds="4" -F input_reference="@monster_original_720p.jpeg;type=image/jpeg"
# remix
curl -X POST https://api.avalai.ir/v1/videos/{id}/remix -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" -d '{"prompt":"…"}'
# filter
curl "https://api.avalai.ir/v1/videos?safety_identifier=dept_123abc" -H "Authorization: Bearer $AVALAI_API_KEY"
```
(The first source curl lacks `Content-Type: application/json`. Python/JS use SDK `client.videos.create/retrieve/list/remix/delete`; JS remix uses `videoId`; list-with-filters uses raw `requests.get(params=…)`; source snippets contain a stray `api_key` variable.)

## Video object
`id`, `object:"video"`, `request_id` (= `avalai-request-id`, UUID v7; use for cost lookup), `status` ∈ queued|processing|completed|failed, `model`, `prompt`, `size`, `seconds`, `progress` (0–100), `remixed_from_video_id`, `safety_identifier`, `created_at`, `completed_at`, `expires_at`, `error`. List response `{object:"list", data:[…], first_id, last_id, has_more}`. (`created_at` shown as string in one sample, int in another.)

## Models & pricing
| model | max | sizes | $/second |
|---|---|---|---|
| `sora-2` | 12 s | 720x1280, 1280x720 | $0.10 |
| `sora-2-pro` | 12 s | + 1024x1792, 1792x1024 | $0.30 standard / $0.50 high-res |
| `gen4.5` (Runway; realism, image reference) | 10 s | multiple | $0.12 |
| `gen4_turbo` (Runway; fast, image reference) | 10 s | multiple | $0.10 |
(Veo pricing not on this page → pricing page.)

## Prompting tips
Be specific (subject, action, setting, lighting, camera movement: slow zoom-out, tracking shot, aerial drone), include temporal sequence, set mood. Reference image sets the scene; prompt describes motion/changes. Start with 4 s tests; poll every ~10 s; cache successes; retry failures with exponential backoff; monitor cost (esp. Sora 2 Pro high-res).

## Status machine
`queued` → `processing` → `completed` | `failed` (see `error`).

## Errors / moderation / limits
400 (unsupported size/duration, e.g. `invalid_size`), 401, 403 (tier/permissions), 404, 429, 500; error `{error:{message,type:"invalid_request_error",code}}`. Prompts and generated videos are moderated. Concurrency limits: Sora 2 ≤10, Sora 2 Pro ≤5 simultaneous generations; video has separate rate limits.
Related: fa/guides/generate-videos-using-sora, fa/providers/openai, authentication, error-handling, pricing, response-headers.md, user.md.
