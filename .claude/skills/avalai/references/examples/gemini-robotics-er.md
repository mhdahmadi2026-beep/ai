# Example: AI in robotics with Gemini Robotics-ER 1.5 (slug probably /examples/… robotics; unconfirmed)

Model: `gemini-robotics-er-1.5-preview` (price ≈ in $0.30, out $2.50 per 1M; see providers/google.md, 06-pricing.md). Vision-language "embodied reasoning" model — perception/planning only, NOT a controller. Routes: native `/v1beta/models/gemini-robotics-er-1.5-preview:generateContent` (SDK `genai.Client(api_key=…, http_options={"api_version":"v1beta","base_url":"https://api.avalai.ir"})`, no /v1) or `/v1/chat/completions` (OpenAI image_url parts). Not on Responses (page's Responses variant switches to a different general model).

## Output conventions
- Points: `[{"point":[y,x],"label":"…"}]` — **[y, x] order**, integers normalized **0–1000**. Boxes: `{"box_2d":[ymin,xmin,ymax,xmax],"label":…}` 0–1000 ints. Trajectory: ordered labelled points `"0"`…`"15"`.
- Convert to pixels: `x_px = x/1000*W`, `y_px = y/1000*H`; then camera calibration / hand-eye transform to robot frame (page's `normalize_to_robot_coords` is a toy linear map).
- Config: `temperature` ~0.5; `thinkingConfig.thinkingBudget` 0 (fast detection) … 1000–2000 (complex reasoning); `tools=[code_execution]` lets it zoom/crop/read gauges (inspect `executable_code`, `code_execution_result` parts).

## Recipes
1. Find objects (point) · 2. Bounding boxes (≤25, "no masks, no code fences") · 3. Video tracking = per-frame queries (every N frames via OpenCV; not true tracking) · 4. Trajectory planning (start point + N waypoints) · 5. Spatial reasoning ("which object to remove to make room for laptop") & multi-step planning with pointed objects · 6. Task orchestration via function-style plan: give robot API (`move(x,y,high)`, `setGripperState(opened)`, `returnToOrigin()`), ask for JSON list of calls · 7. Code execution for dynamic tasks · 8. Consensus (query ×3, average) · 9. Multi-robot task allocation · 10. Safety monitoring & grasp planning (model-suggested; unvalidated).
Tips: plain language; crop/zoom ROI for small objects; good lighting; reduce image size for latency; batch with ThreadPool (bounded; rate limits); cache static prompt prefix (no explicit caching on AvalAI — implicit only); parse JSON defensively (strip ```json fences, regex `[\[{].*[\]}]`).

## Safety rules (mine — critical)
Never connect model output directly to actuators. Validate: JSON schema, coordinate range, workspace bounds, speed/force limits, collision check, allow-listed function names and argument ranges (reject unknown), max steps, human confirmation for risky moves, independent hardware e-stop, watchdog/timeouts; log every plan. Safety-monitoring prompts are advisory only — not a certified safety function. Treat on-image text as prompt injection.

## Defects of the source page
- Python SDK sample uses `http_options={"api_version":"v1beta","url":"https://api.avalai.ir"}` — key is **`base_url`**, not `url` (matches providers/google.md note).
- JS sample uses `@google/generative-ai` with `new GoogleGenerativeAI({apiKey, baseUrl})` and per-call `generationConfig`: that package takes just the key string (deprecated; use `@google/genai` with `httpOptions.baseUrl`). Go sample imports `option` without importing it, uses non-existent `openai.ImagePart` signature and a prompt without the required JSON schema; PHP sample lacks image prompt format details.
- cURL uses `base64 -w 0` (Linux only) and `Authorization: Bearer` (OK; alt `x-goog-api-key`).
- Responses variant targets `gpt-5.6-luna` (placeholder id) — no robotics-grade point/box guarantees; it's a migration of orchestration, not equivalent.
- Sample outputs use Persian labels but model prompts in English: label language follows prompt; keep labels English for downstream matching (`"block" in label.lower()` breaks with Persian labels).
- `next(...)` without default raises StopIteration when an object isn't found; `re.search(r"\[.*\]")` grabs wrong span with nested arrays; plan execution via `if func_name == …` with unvalidated `args`.
- `normalize_to_robot_coords` labels y→height but robot frames often flip axes; relative coordinates computed in normalized image space not metric space.
- "Caching automatically" claim for long prompts is unverified; "اجماع" averaging of points is fine for unimodal, wrong for multi-instance objects; `timeout`/retry missing; video loop `cv2` reads every 5th frame sequentially (cost = frames×call).
- Images hosted on ai.google.dev; link `fa/news/2025-10-28-gemini-robotics-er-model-added.md` (not captured); `fa/guides/function-calling.md` exists in index.
