# RunwayML (video / image edit / TTS)

| id | type | endpoint | price |
|---|---|---|---|
| gen4.5 | video 2-10 s, `input_reference` image REQUIRED | `/v1/videos` | $0.12/s |
| gen4_turbo | video 2-10 s, input image required | `/v1/videos` | $0.05/s |
| gen4_image | image edit | `/v1/images/edits` | $0.05 (720p) / $0.08 (1080p) |
| gen4_image_turbo | image edit | `/v1/images/edits` | $0.02 |
| eleven_multilingual_v2 (via RunwayML) | TTS | `/v1/audio/speech` | $0.000015/char |

- Sizes: 1280x720 (default), 720x1280, 1920x1080, 1080x1920+; default 5 s.
- **`prompt` ≤ 1000 chars**, otherwise error. Multipart form (`-F`), `seconds` as string.
- Flow: `client.videos.create(...)` → poll `videos.retrieve(id)` (completed|failed) every ~10 s → `videos.retrieve_content(id)` stream to mp4. See api-reference/videos.md.
- For richer ElevenLabs models (turbo/flash v2.5, STT scribe) use the ElevenLabs provider page (not yet captured).
- Defects: gen4.5 price missing from the summary table; "Elo 1,247" marketing; JS sample misses polling.
