# Gemini safety settings (docs.avalai.ir/fa/guides/gemini-safety-settings)

Built-in Gemini content filtering configured inside the generation request — alternative to a separate Moderation API call (see guides/moderation.md, api-reference/moderation.md).

## vs Moderation API
| | Moderation API | Gemini safety settings |
|---|---|---|
| calls | separate call | in the same call |
| latency | extra round trip | none |
| cost | separate call | included in generation |
| timing | before/after | real-time during generation |
| categories | OpenAI moderation | Google harm categories |
Use Moderation API for non-Gemini models, pre-screening user input, detailed category scores for compliance, consistent cross-provider moderation. Use Gemini settings when already on Gemini, minimizing calls/latency, per-request thresholds. Combine for sensitive apps (pre-check user input with `client.moderations.create(input=...)`, then Gemini with safety settings).

## Categories (4)
`HARM_CATEGORY_HARASSMENT`, `HARM_CATEGORY_HATE_SPEECH`, `HARM_CATEGORY_SEXUALLY_EXPLICIT`, `HARM_CATEGORY_DANGEROUS_CONTENT`. (Google also has civic-integrity in some versions – not documented here.)

## Thresholds
`OFF` (filter fully off) · `BLOCK_NONE` (show everything, similar to OFF) · `BLOCK_ONLY_HIGH` · `BLOCK_MEDIUM_AND_ABOVE` · `BLOCK_LOW_AND_ABOVE` (strictest). **Default for Gemini 2.5 and Gemini 3 models = `OFF`; older models = `BLOCK_MEDIUM_AND_ABOVE`.** Docs table lists defaults OFF for gemini-2.5-flash, 2.5-pro, 3.5-flash, 3.1-pro-preview.
Inconsistency: native examples "disable" with `OFF`; Go and the OpenAI-compat examples use `BLOCK_NONE` → both exist; prefer `OFF` for Gemini 2.5+/3.

## Native Gemini API (base `https://api.avalai.ir`, no /v1; v1beta path)
- Python `google-genai`: `genai.Client(api_key=..., http_options={"base_url":"https://api.avalai.ir"})`; `config=types.GenerateContentConfig(safety_settings=[types.SafetySetting(category=..., threshold=...)])`.
- JS `@google/genai`: `httpOptions:{baseUrl:"https://api.avalai.ir"}`; `config:{safetySettings:[{category: HarmCategory.X, threshold: HarmBlockThreshold.Y}]}` (plain strings like `"OFF"` for off).
- cURL: `POST https://api.avalai.ir/v1beta/models/gemini-2.5-flash:generateContent` with header `x-goog-api-key: $AVALAI_API_KEY`, body `{"contents":[{"parts":[{"text":...}]}],"safetySettings":[{"category":...,"threshold":...}]}` (camelCase in raw JSON).
- Go sample uses the deprecated `github.com/google/generative-ai-go/genai` + `option.WithEndpoint` (Go SDK mismatch warning from earlier pages): don't emit; use raw HTTP.

## OpenAI-compatible Chat (`/v1/chat/completions`)
Pass `safety_settings` (snake_case, list of `{category, threshold}`): Python `extra_body={"safety_settings":[...]}`; raw HTTP / JS: top-level `safety_settings` (JS needs `// @ts-expect-error`). Go OpenAI SDK has no `extra_body` → use raw HTTP (sample just omits safety settings). Only Gemini models. See guides/provider-specific-params.md. The "Responses equivalent" blocks in the page swap in `gpt-5.6-luna` and do NOT carry safety settings (they're irrelevant to Gemini) — ignore them.

## Handling blocked responses
Check `response.prompt_feedback.block_reason` (prompt blocked), `candidates[].safety_ratings[]` (`category`, `probability` NEGLIGIBLE|LOW|MEDIUM|HIGH, `blocked`). Raw JSON: `promptFeedback.blockReason`/`safetyRatings`, `candidates[].safetyRatings` (camelCase). Always handle empty/blocked candidates (no `.text`). Blocked content isn't billed for video/audio models (per Veo page).

## Warnings / best practices
Turning filters off allows potentially harmful content — implement your own filtering. Start from defaults, test edge cases, handle blocked outputs, log block events, combine with Moderation API for sensitive apps, document threshold choices for compliance.
Doc defect: safety-best-practices and moderation-guide pages not yet captured; model ids `gemini-2.5-*` may be retired/outdated (check 10-deprecations: gemini-2.5-flash-image retired 2026-10-02).
