# Example: speaker-aware meeting intelligence (/examples/speaker_aware_meeting_intelligence)

Adapted from OpenAI Cookbook. Script: `references/scripts/meeting_intelligence.py` (cleaned; `--selftest` runs offline: evidence/redaction/routing checks pass; the API calls themselves were NOT run). Related: examples/evidence-grounded-workflows.md (same quote-grounding idea), api-reference/audio.md, guides/speech-to-text.md.

## Pipeline
1. Validate file (≤25 MB) + diarized transcription: `client.audio.transcriptions.create(model=<STT>, file=f, response_format="diarized_json", chunking_strategy="auto", extra_body={known_speaker_names:[…≤4], known_speaker_references:[data-URL clips 2–10 s]})`.
2. Stable segment ids `seg_001…` (speaker/start/end/text).
3. Extraction via Responses (`gpt-4.1-mini`, `store:false`, strict `json_schema`: summary, `application_policy` flags {contractual claim, pricing promise, regulated content}, decisions, action_items {owner|null, text, due_date|null}, risks {severity low/medium/high}); every item needs `evidence_refs[{segment_id, quote}]` (minItems 1).
4. Deterministic validation: segment exists, quote non-blank and a substring of that segment's text.
5. Routing: evidence error OR medium/high risk OR any policy flag → `human_review_required`, else `ready_for_approved_sync` (never auto-write to CRM/ticket; idempotency before approved sync).
6. Redact emails/phones (regex only — use real PII/DLP for sensitive loads) → review payload.
Release gate = deterministic validator (not an LLM judge); evaluate on consented, human-labelled holdout: speaker-label/turn accuracy, action precision/recall, unsupported-claim rate, exact-quote validity, PII recall, reviewer override rate.

## ⚠ Model-availability conflict (important)
Page uses `gpt-live-transcribe` (+`diarized_json`, known-speaker refs). But `03-ai-workflows.md` says "do not use `gpt-transcribe`/`gpt-live-transcribe` in AvalAI requests", while 10-deprecations.md says the old transcription models incl. `gpt-4o-transcribe-diarize` shut down 2027-02-26 with `gpt-live-transcribe`/`gpt-transcribe` as replacements. Unresolved → confirm via `/v1/models` and guides/speech-to-text before building; the script reads `AVALAI_STT_MODEL`. Known-speaker support is route-dependent (page says so); fall back to generic `speaker_N` labels. Diarization gives no cross-recording identity. Realtime NOT used/available.

## Defects / caveats
- Page's validator only checks refs it's given: an item with an **empty `evidence_refs`** passes locally (schema `minItems` is a model-side constraint) → script adds a "has no evidence" check.
- `temperature=0` on the extraction call: fine for gpt-4.1-mini, drop for reasoning/Claude 5.x. Quote must match exactly (`quote not in segment_text`) — whitespace/Unicode normalisation (Persian ZWNJ, Arabic vs Persian ya/kaf) can cause false rejects; normalise both sides if needed.
- `application_policy` flags are model-decided → a missed flag silently skips review; also keep deterministic keyword checks for pricing/contract terms and sample audits.
- Redaction regex phone pattern also hits plain long numbers (invoice ids); email/phone only — names, addresses, national ids not covered; transcript segments are redacted in review output only, raw text remains in memory/logs.
- Data URLs of speaker clips go to the provider (consent + data-controls.md); known_speaker data size can exceed request limits.
- Response `segments[].speaker` may be None for unknown routes; fixture asserts check schema/validator only, not transcription quality.
- Doc says run on `/v1/audio/transcriptions` (post-call), not Realtime; 25 MB limit → split long meetings (chunking by time with overlap, re-id segments globally).
