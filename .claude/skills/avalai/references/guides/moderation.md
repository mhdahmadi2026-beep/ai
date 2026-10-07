# Moderation guide
Endpoint `POST /v1/moderations` (see api-reference/moderation.md). Models: `omni-moderation-latest` (recommended; text+image, more categories), `text-moderation-latest` (legacy, text only). Pricing: check /fa/pricing (may be free). Check live availability via `/v1/models`.

## Workflow
1 classify input before generation (free text, images, URLs, files, retrieval content); 2 generate only after policy passes or route to refusal/safe-completion; 3 classify output before display (esp. public/social/education/minors); 4 tune thresholds via evals (`flagged` strong default; custom `category_scores` thresholds calibrated on product examples + human labels; recalibrate when provider model updates); 5 audit trail: `avalai-request-id`, model, route, hashed user or `safety_identifier`, categories, final action (no unnecessary personal data); 6 escalation path for blocked/borderline/appealed — never drop user requests silently.

## Calls
Text: `client.moderations.create(model="omni-moderation-latest", input="...")`. Multimodal: `input=[{"type":"text","text":...},{"type":"image_url","image_url":{"url":"https://... or data:image/png;base64,..."}}]` (omni only).

## Inline moderation (route-dependent)
`responses.create(..., moderation={"model":"omni-moderation-latest"})` → `response.moderation.input.flagged` / `.output.flagged`. A safe refusal about harmful topics can still score high → treat as signal, not auto-decision. Streaming: scores only after complete output (not with deltas). If unsupported for model/route → separate `POST /v1/moderations` before display/action. Covers tool-call arguments/outputs present in conversation; NOT tool names/descriptions/schemas/structured-output schemas → validate those separately.

## Response
`{id:"modr-...", model, results:[{flagged, categories:{…bool}, category_scores:{…0-1}, category_applied_input_types:{cat:["text","image"]}}]}` (`category_applied_input_types` omni only).

## Categories
| category | models | inputs |
|---|---|---|
| harassment, harassment/threatening, hate, hate/threatening | all | text |
| illicit, illicit/violent | omni only | text |
| self-harm, self-harm/intent, self-harm/instructions | all | text+image |
| sexual | all | text+image |
| sexual/minors | all | text |
| violence, violence/graphic | all | text+image |

## Defects
- Go samples use fictional `openai.ModerationRequest`/`client.Moderations` + `openai.NewClient("AVALAI_API_KEY")` (literal string) with openai-go.
- Python example image URL is example.com placeholder; inline-moderation sample uses `gpt-5.6-luna`.
