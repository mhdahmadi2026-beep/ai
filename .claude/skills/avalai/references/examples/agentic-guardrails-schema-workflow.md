# Example: agentic guardrails for a schema-change workflow

Slug: `/examples/agentic_guardrails_schema_workflow`. Script: `references/scripts/schema_change_guardrails.py` (tested offline with a stubbed `openai`).

## Pattern
natural-language request → model parses to strict JSON (structured output) → **deterministic validation** → reviewable SQL draft → rollout plan → artifact `artifacts/schema_change_review.json` (CI/Promptfoo-evaluable).

## Design rules
- The model's parse is NOT trusted. Validate against a catalog (known schema.table), a column-name regex `[A-Z][A-Z0-9_]{1,62}`, an allowlist of data types, and duplicate columns.
- Forbidden-operation regex `\b(drop|delete|truncate|grant|revoke)\b` is applied to the **request text**.
- SQL is only a draft for human review; NEVER auto-execute. Template: `ALTER TABLE {schema}.{table} ADD COLUMN {column} {type};`.
- Rollout plan/downstream objects come from the catalog, not from the model (model-supplied `downstream_objects` is unverified).
- Structured output: Chat Completions `response_format.json_schema` or Responses `text={"format":{"type":"json_schema","name":"schema_change_request","strict":True,"schema":CHANGE_SCHEMA}}` then `json.loads(response.output_text)`.

## Tested behaviours (stubbed model)
Safe additive column → OK; destructive request → rejected; duplicate column, unknown table, non-allowlisted type (e.g. `BLOB; DROP TABLE X`) → rejected.

## Defects / caveats of the source page
- Keyword regex gives false positives ("drop-down" matches `\bdrop\b`); acceptable as fail-closed, but document it.
- `temperature=0` should be dropped for reasoning / Claude 5.x models.
- `nullable` requirement is not modelled.
- Promptfoo asserts rely on the exact string `"validation_errors": []`; companion provider `promptfoo_provider.py` returns `{"output": json.dumps(artifact)}`.
- Hosted File Search not needed; use manual RAG if catalog lookup grows.
