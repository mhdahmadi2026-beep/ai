# v1beta — Google GenAI native API (docs: /fa/api-reference/v1beta)

Native Gemini schema via the official Google GenAI SDK. Methods: `generateContent`, `streamGenerateContent`, `embedContent`, `batchEmbedContents`, `countTokens`, `predict`. Full official docs: https://ai.google.dev/gemini-api/docs. Report discrepancies to t.me/AvalAISupport.

## Base URL / auth
- **Base URL `https://api.avalai.ir` (NO `/v1`)** for the Google SDK (`http_options={"api_version":"v1beta","base_url":"https://api.avalai.ir"}`; JS `httpOptions:{apiVersion:"v1beta", baseUrl:"https://api.avalai.ir"}`). Paths: `/v1beta/models/{model}:{method}`.
- Auth: `Authorization: Bearer $AVALAI_API_KEY` (recommended) **or** `x-goog-api-key: $AVALAI_API_KEY`. (The source's curl examples put `$AVALAI_API_KEY` inside single quotes in `-H 'Authorization: Bearer $AVALAI_API_KEY'` → the shell won't expand it; use double quotes.)
- Google models only (Gemini incl. Nano Banana image family). No other Google services.

## Models
Text/vision/audio: `gemini-3.8-flash` (`gemini-flash-latest` alias now points to it), `gemini-3.5-flash`, `gemini-3.1-pro-preview`, `gemini-3.1-flash-lite`, `gemini-3.1-flash-lite-preview`, `gemini-2.5-pro`, `gemini-2.5-flash`, `gemini-robotics-er-1.5-preview`. TTS: `gemini-3.8-flash-tts`, `gemini-3.8-flash-lite-tts`, `gemini-2.5-pro-preview-tts`, `gemini-2.5-flash-preview-tts`. Image (Nano Banana): `gemini-3.1-flash-image` (NB2, replaces imagen-4.0-generate/fast), `gemini-3-pro-image` (NB Pro, replaces imagen-4.0-ultra), `gemini-3.1-flash-lite-image` (NB2 Lite, 1K; replaces imagen-3.0-*), `gemini-2.5-flash-image` (**shuts down 2026-10-02 per page — i.e. already stopped/imminent; don't use**). **All `imagen-*` removed** (fa/news/2026-09-04-model-deprecations-and-migration-guide). Embeddings: `gemini-embedding-2` (alias `gemini-embedding-2-preview`, multimodal text/image/audio/video/PDF via `inline_data`), `gemini-embedding-001`.

## generateContent — `POST /v1beta/models/{model}:generateContent`
Body: `contents` (req; `{parts:[…], role:"user"|"model"}` — **only `user` and `model` roles**), `system_instruction` (`{parts:[{text}]}` — use this for system-level instructions), `generationConfig`, `safetySettings`, `tools`.
`generationConfig`: `maxOutputTokens`, `temperature` (0–2), `topP`, `topK`, `stopSequences`, `thinkingConfig` (`thinkingLevel` low|medium|high for Gemini 3.5/3.1; `thinkingBudget` tokens for 2.5 Flash, 0 disables), `responseModalities` (TTS: `["AUDIO"]`), `speechConfig`.
`speechConfig`: `voiceConfig.prebuiltVoiceConfig.voiceName` (e.g. `Kore`, `Charon`, `Puck`, `Fenrir`, `Zephyr`) or `multiSpeakerVoiceConfig.speakerVoiceConfigs[{speaker, voiceConfig}]`.
```bash
curl -X POST "https://api.avalai.ir/v1beta/models/gemini-3.5-flash:generateContent" -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"contents":[{"parts":[{"text":"…"}],"role":"user"}],"generationConfig":{"maxOutputTokens":1000,"temperature":0.7}}'
```
Response: `candidates[{content:{parts,role:"model"}, finishReason, index, safetyRatings}]`, `usageMetadata{promptTokenCount, candidatesTokenCount, totalTokenCount, …}`, `modelVersion`, `responseId`.

## streamGenerateContent — `POST …:streamGenerateContent`
Same body; response streamed (shown as a JSON array of partial response objects each with `candidates`, `usageMetadata`; final chunk has `finishReason`).

## Python SDK
Valid current usage (the page's first example `await client.agenerate_content(...)` / `agenerate_content_stream` with `max_tokens` is **not** a real google-genai API — flagged; use):
```python
from google import genai; from google.genai import types
client = genai.Client(api_key=os.environ["AVALAI_API_KEY"], http_options={"api_version":"v1beta","base_url":"https://api.avalai.ir"})
r = client.models.generate_content(model="gemini-2.5-flash", contents="…",
      config=types.GenerateContentConfig(max_output_tokens=100))
# async: await client.aio.models.generate_content(...) ; stream: client.models.generate_content_stream(...)
```
Multimodal: parts with `inline_data{mime_type, data(base64)}` (images must be base64, not external URLs).

## Gemini 3.8 native TTS (anchor `#gemini-38-native-text-to-speech`)
`gemini-3.8-flash-tts` (creative quality, emotion, regional accents, long-dialogue stability) / `gemini-3.8-flash-lite-tts` (throughput/latency). Text in → audio out only (no transcription, audio-input chat, Live API, reasoning). Only via native `/v1beta/models`, `/v1/chat/completions`, `/v1/audio/speech` — never `/v1/responses`, `/v1/messages`, legacy `/v1/text:synthesize`. Write the reply with a chat/reasoning model first.
- Each text part has `speechMetadata:{speaker, style}`; speaker must match a `speakerVoiceConfigs[].speaker`. Text is read verbatim → don't put delivery directions/speaker labels in spoken text. Don't send `thinkingConfig`, tools, image or audio input.
- Native non-streaming response defaults to **WAV** (`audio/wav`), unlike raw PCM default of `gemini-3.1-flash-tts-preview` and older Gemini TTS. Decoder: check `inlineData.mimeType`; `audio/wav` → write bytes as-is; `audio/L16` (24 kHz, mono, 16-bit) → wrap with `wave` header; anything else → error (don't guess from file extension).
```bash
curl --fail-with-body -sS https://api.avalai.ir/v1beta/models/gemini-3.8-flash-tts:generateContent -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" \
 -d '{"contents":[{"role":"user","parts":[{"text":"Welcome to AvalAI.","speechMetadata":{"speaker":"Host","style":"Warm and welcoming."}},{"text":"Have a wonderful day!","speechMetadata":{"speaker":"Guest","style":"Cheerful and relaxed."}}]}],
  "generationConfig":{"responseModalities":["AUDIO"],"speechConfig":{"multiSpeakerVoiceConfig":{"speakerVoiceConfigs":[{"speaker":"Host","voiceConfig":{"prebuiltVoiceConfig":{"voiceName":"Zephyr"}}},{"speaker":"Guest","voiceConfig":{"prebuiltVoiceConfig":{"voiceName":"Puck"}}}]}}}}' --output native-speech.json
```
```python
resp = json.loads(Path("native-speech.json").read_text())
for i, a in enumerate(p["inlineData"] for p in resp["candidates"][0]["content"]["parts"] if "inlineData" in p):
    data = base64.b64decode(a["data"], validate=True); mt = a["mimeType"].split(";",1)[0].strip().lower()
    if mt == "audio/wav": Path(f"speech-{i}.wav").write_bytes(data)
    elif mt == "audio/l16":
        with wave.open(f"speech-{i}.wav","wb") as o: o.setnchannels(1); o.setsampwidth(2); o.setframerate(24000); o.writeframes(data)
    else: raise ValueError(a["mimeType"])
```
Migration of old PCM TTS: fa/guides/text-to-speech#migrate-to-gemini-38-tts.

## Grounding with Google Search
Add `"tools":[{"google_search":{}}]` (SDK: `types.Tool(google_search=types.GoogleSearch())`; JS `config:{tools:[{googleSearch:{}}]}`). Legacy models used `google_search_retrieval` — use `google_search` for all current models. Supported: Gemini 3.1 Pro Preview, 3 Pro Preview, 3 Flash Preview, 2.5 Pro/Flash/Flash-Lite. Flow: analyze prompt → generate/run search queries → synthesize → grounded answer.
Response `candidates[].groundingMetadata`: `webSearchQueries[]`, `searchEntryPoint.renderedContent` (HTML/CSS widget you must render), `groundingChunks[{web:{uri,title}}]`, `groundingSupports[{segment{startIndex,endIndex,text}, groundingChunkIndices[]}]`. Inline citations: sort supports by `end_index` desc, insert `[i+1](uri)` after each segment.
Pricing: Gemini 3 models billed per search query the model chooses to run (multiple queries in one call = multiple billable uses); Gemini 2.5 and older billed per prompt using grounding. See pricing page.

## embedContent — `POST /v1beta/models/{model}:embedContent`
Body: `contents` [{parts:[{text}]}] (req), `embedding_config{task_type, output_dimensionality 128–3072}`. Models `gemini-embedding-2` / `gemini-embedding-001`. Response `{embeddings:[{values:[…]}]}`. Task types: SEMANTIC_SIMILARITY, CLASSIFICATION, CLUSTERING, RETRIEVAL_DOCUMENT, RETRIEVAL_QUERY, CODE_RETRIEVAL_QUERY, QUESTION_ANSWERING, FACT_VERIFICATION. MRL dims 3072 (default, pre-normalized) / 1536 / 768 / 512 / 256 / 128 — **normalize for dims < 3072**. SDK: `client.models.embed_content(model, contents, config=types.EmbedContentConfig(task_type=…, output_dimensionality=768))`. (JS snippet has stray `}` and puts `taskType`/`outputDimensionality` at top level; in the real SDK they go in `config`.) More in embeddings.md.

## batchEmbedContents — `POST …:batchEmbedContents`
Body `requests:[{model:"models/gemini-embedding-001", content:{parts:[{text}]}, task_type?, output_dimensionality?}]` (each request's `model` must match URL). Response `{embeddings:[{values}…]}`. The Python example just calls `embed_content` with a list.

## countTokens — `POST …:countTokens`
Body `contents` (req), optional `system_instruction`, `tools` (both counted). Response `{"totalTokens": N}`. SDK `client.models.count_tokens(model, contents, config=…)`. Rules of thumb: text ≈4 chars/token; images (Gemini 2.5+) ≤384 px both dims = 258 tokens, larger → 768×768 tiles × 258; audio 32 tokens/s; video 263 tokens/s.

## predict (image) — `POST …:predict`
`imagen-*` removed → Imagen-style `instances:[{prompt}]`, `parameters{sampleCount 1–8, aspectRatio ("1:1","9:16","16:9","3:4","4:3"), personGeneration, safetyFilterLevel, negativePrompt}` is documented only as a legacy shape (example still calls `gemini-3.1-flash-image:predict`, response `predictions[{bytesBase64Encoded, mimeType}]`, `metadata.tokenMetadata.outputImageCount`). **Prefer `:generateContent` (with `responseModalities` image) or `/v1/chat/completions`** for Nano Banana (fa/examples/generate_images_with_nano_banana_series). Decode: `base64.b64decode(pred["bytesBase64Encoded"])`.

## Errors / limits
200/400/401/429/500; error body `{error:{code,message,status:"INVALID_ARGUMENT"}}`. Rate limits same structure as other endpoints. Google models only; base URL without `/v1`; images as base64 (not external URLs).
Related: fa/providers/google, authentication, rate-limits, libraries, fa/examples/generate_images_with_nano_banana_series.
