# Local graders for evals (guide) — **hosted graders NOT implemented on AvalAI**
Banner: feature in development. No hosted `/v1/evals`, grader validate/run endpoints. **Don't rewrite OpenAI `/v1/fine_tuning/alpha/graders/validate|run` to `api.avalai.ir`.** Build graders locally (CI). OpenAI hosted Evals/Graders platform deprecating: evals read-only 2026-10-31, shutdown 2026-11-30 (OpenAI context only). Keep datasets, grader code, rubrics, thresholds in repo.

## Core shape
Grader inputs: `item` (human-reviewed test row: prompt, reference answer, expected JSON/tool call), `sample` (model output from `/v1/responses`, `/v1/chat/completions` or native route), output `score` ∈ [0,1] + short reason. Names (portable to OpenAI): `item.reference_answer`, `sample.output_text`, `sample.output_json`, `sample.output_tools`, optional `sample.choices` (raw chat choices for migration debug), `sample.output_audio` (metadata/transcript). Keep normalized `sample.*` small/stable; store raw provider response separately for audit; grade on portable fields.

## Hosted concept → local
| OpenAI hosted | AvalAI today |
|---|---|
| `grader` JSON object | versioned Python/JS function or Promptfoo assertion |
| `{{ item.reference_answer }}` | dataset field (JSONL/CSV/YAML/fixture) |
| `{{ sample.output_text }}` | normalized `response.output_text` / chat content |
| `validate` endpoint | unit tests on known pass/fail fixtures |
| `run` endpoint | CI job generating samples via AvalAI and writing score artifacts |
| hosted report URL | Promptfoo report, pytest JSON/JUnit, own observability |
Template namespaces: `item.*` = dataset/reference; `sample.*` = generated output. Grader types: `string_check` (ops eq, neq, like, ilike), `text_similarity` (fuzzy, BLEU/GLEU, ROUGE, cosine/embedding), `score_model` (fixed judge model with rubric → numeric), `python` (deterministic local rules), `multi` (combine sub-scores with explicit formula e.g. `(tool_name + arguments)/2`).

## Pick smallest sufficient
string check (labels/ids/enums/required phrases; NOT when wording may vary); JSON schema (structured extraction/tool args; not for semantic quality); text similarity (summaries/paraphrase; NOT exact values/ids/money); LLM judge (subjective quality, helpfulness, safety, style, partial credit; NOT if deterministic check works); custom Python (business rules, numeric ranges, normalized dates, multi-field; NOT if needs network/secrets); multi-grader (independent checks; NOT if one failure should fail the row). Start deterministic; add LLM judge only when needed.

## Sample generation
Chat: `client.chat.completions.create(model=os.getenv("AVALAI_EVAL_MODEL"), messages=[{"role":"developer",...},{"role":"user",...}], temperature=0)`; Responses: `instructions=..., input=ticket` → `output_text.strip()` (temperature not accepted by reasoning/Claude 5.x models). Tool outputs: Responses → inspect `response.output` items; Chat → `message.tool_calls`.

## Examples
Dataset JSONL `{"item":{"ticket":"...","correct_label":"Hardware"}}`. Label grader: normalize (`strip().lower().replace(".","")`) → `{"score":1.0|0.0,"reason":...}`. Tool-call grader: no calls → 0; `name_score` exact, `argument_score` = parsed-JSON equality (`json.loads(arguments)`); `score = 0.5*name + 0.5*args`; exact JSON compare under-scores equivalents (`1` vs `1.0`, `CA` vs `California`, date formats) → normalize or semantic-grade parsed fields.

## Local Python grader rules
Deterministic, version-controlled `grade(sample, item)` reviewed with prompt/model changes; no network/API keys/secrets in CI graders; limit runtime+memory; return valid float or `{score, reason}`; fail-safe: exception/missing field/NaN/invalid → 0.0 with debug reason (mirror OpenAI hosted sandbox limits: no network, bounded runtime/memory/disk, small source).

## LLM judge
Calibrate with human-labelled examples before CI; pass/fail or pairwise > 1–10; rotate answer order (position bias); control length (verbosity bias); freeze judge model/prompt/temperature/rubric per release; keep disagreement + edge cases. Reward hacking pack (adversarial): shortcut keyword-stuffing answers, prompt-injection asking judge to ignore rubric/give full credit, over-long verbose answers hiding missing facts/unsafe tool calls, schema-valid JSON with wrong ID/date/amount/citation, human-rejected rows with high auto score. If they score well → tighten grader / add deterministic checks first / require human review gate; don't just lower threshold.
Calibration pack (`perfect > partial > wrong` ordering), e.g. reference "Reset the API key from the dashboard." vs identical / "Open the dashboard and rotate credentials." / "Contact billing support for an invoice." → expected_order 1/2/3. Before a grader may fail CI: correct ranking, rejects injection inside candidate, writes failure reason to CI artifacts; re-run on any change of judge model, rubric, temperature, prompt or length limit.

## Defects
- Banner "not implemented" + body gives full local workflow (both valid; local approach is the supported path).
- Chat sample uses `temperature=0` and role `developer` (not valid for every provider).
