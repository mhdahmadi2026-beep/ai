# Evals (guide) — **hosted `/v1/evals` NOT provided by AvalAI**
Don't build on `https://api.avalai.ir/v1/evals`. Use local/CI evals with normal AvalAI API calls; keep datasets/rubrics/thresholds in portable repo files so they can migrate if AvalAI later ships hosted evals (then keep local suite as source of truth; verify real schema, don't assume OpenAI parity). OpenAI's hosted Evals: existing evals read-only **2026-10-31** (already ~past soon: today 2026-10-07 → 24 days), full shutdown **2026-11-30** — another reason not to couple to its object model. Durable part: objective → dataset → metrics → run/compare → continuous eval.

## Local assets
Dataset (representative prompts, expected labels/reference answers/rubrics); data schema per row (like `data_source_config`); runner (Promptfoo, pytest, small script, CI); models (prod vs candidate via env var); assertions (exact match, JSON schema, semantic similarity, LLM judge, tool-call accuracy, refusal behaviour, latency/cost thresholds). Example: examples/promptfoo_evals_with_avalai.

## Design loop
1 define objective 2 collect dataset (production-like, edge cases, multilingual, malformed, adversarial) 3 define metrics (pass/fail, exact match, rubric score, tool-call accuracy, retrieval precision/recall, human review) 4 run & compare prod vs candidate (prompt/model id/routing) 5 continuous eval (add production failures; run every release). No vibe-based evals; write measurable criteria before changing prompt/model.

## Anti-patterns
generic metrics only (BLEU/ROUGE/perplexity) → add task-specific checks; biased/too-clean dataset → mix logs, edge cases, multilingual, adversarial; vibes → define pass/fail first; uncalibrated automatic graders → compare to human labels, keep disagreement cases; only end-to-end score → measure boundaries separately (classification, retrieval, tool call, final answer, safety). Prefer comparable tasks: pairwise, classification, rubric scoring, tool-call accuracy.

## Flywheel
Instrument (request id, model id, prompt version, tool calls, retrieved doc ids, tokens, latency, user-visible failures) → mine failures/tickets/red-team/reviewer disagreements into rows → calibrate graders on small human-labelled batch → gate (smoke eval each PR, full suite before model/prompt/retrieval/tool-schema change) → refresh (dedupe, keep hard cases, add new failure modes). Row metadata: `case_id`, `source`, `risk_level`, `expected_behavior`, `owner`, `added_after_incident`.

## Provider / deployment comparison
Fix dataset+rubric; vary `model`, endpoint (`/v1/responses`, `/v1/chat/completions`, native), provider-specific options. Label each run by provider path, endpoint, feature flags, region, service tier. Tool support is a separate dimension (function calls, MCP, web/file search, streaming may differ per route). Add privacy/safety assertions when data crosses provider boundary (refusal, prompt injection, source leak, redacted logging). Promote only if accuracy, latency, cost, quota, safety gates pass for THAT route.

## Dataset contract
JSONL `{"item":{"ticket_text":"...","correct_label":"Hardware"}}`; `item.*` = prompt vars + ground truth; `sample.output_text` = candidate output (store for debugging). Annotation fields: `item.*`, `sample.output_text`, `human_rating` (pass|fail|better_than_baseline|needs_review), `output_feedback`, `grader_score`. Subjective/expert tasks → SME-annotate a small batch first; keep human/grader disagreements to refine the rubric (don't delete).

## Promptfoo example
```yaml
description: Classify IT support tickets
prompts: ["Classify the support ticket as Hardware, Software, or Other.\nReturn only the label.\n\nTicket: {{ticket_text}}"]
providers:
  - {id: "openai:chat:gpt-5.5", label: production, config: {apiHost: "https://api.avalai.ir/v1", apiKey: "${AVALAI_API_KEY}"}}
  - {id: "openai:chat:gpt-5.4", label: candidate, config: {apiHost: "https://api.avalai.ir/v1", apiKey: "${AVALAI_API_KEY}"}}
tests: [{vars: {ticket_text: "...", correct_label: Hardware}, assert: [{type: equals, value: Hardware}]}]
```
Run `AVALAI_API_KEY=... promptfoo eval -c evals/x.yaml`; store JSON/HTML as CI artifact; compare `production` vs `candidate`; promote only if pass rate, latency, cost OK and no high-risk regression. (Check Promptfoo's OpenAI provider uses `apiBaseUrl`, not `apiHost`; verify.) Runner code: Chat `temperature=0` classifier; Responses version `instructions=…, input=ticket` → `output_text` (don't send temperature to reasoning/Claude 5.x models).

## What to eval
| architecture | focus |
|---|---|
| single prompt | instruction following, classification, formatting |
| RAG | context recall, citation accuracy, hallucination rate |
| tool workflows | tool selection, argument extraction, error handling |
| agents | handoff accuracy, stop conditions, user safety |
| multimodal | modality coverage, OCR/vision accuracy, refusals |
Multi-step: eval each boundary (intent classification, ID extraction, tool-arg correctness, final reply). Edge cases: multilingual/mixed/typos/very short; broken JSON/XML/Markdown/CSV/logs; conflicting user instructions overriding developer; long conversations with key fact mid/start; ambiguous/empty/stale tool outputs; repeated tool calls, wrong arg extraction, circular handoff, refusal paths. Add the failing production case to the dataset BEFORE changing prompt/model/schema/retrieval.

## LLM-as-judge
Calibrate against human labels before gating CI. Pairwise or pass/fail > vague 1–10; keep response lengths similar (verbosity bias); swap order in pairwise (position bias); validate judge-human agreement; strong model (e.g. gpt-5.5) first, then cheaper once rubric stable. Smallest sufficient grader: string check (labels/ids/enums), JSON schema (before semantic scoring), semantic similarity (wording variance OK), LLM judge (rubric quality/safety/helpfulness/partial credit), tool workflows → grade tool name AND arguments (semantic grading for normalized addresses/dates/units). See guides/graders (not captured).
Layering: deterministic checks (labels, JSON validity, required citations, tool name, arg shape) gate every PR; semantic/retrieval scores (similarity, context recall/precision, citation grounding) threshold + human sampling; LLM judge calibrate first; human review mandatory for high-impact domains/new rubrics/grader disagreements/incidents. Keep evaluator outputs in separate columns/artifacts.

## Agent trajectory evals
Plan (goal/constraints/stop), tool order+safe args, state handling (`previous_response_id`, retrieved context, tool outputs, user limits across turns), recovery (tool error, empty retrieval, refusal, timeout, no loops), final answer (explains result, evidence, no unsupported claims). Log typed output items, tool-call args, tool outputs, request ids, pass/fail reason. See guides/agent-evals (not captured).

## CI/release checklist
Smoke evals each PR; full suite before model id/prompt/tool/retrieval change; record model, endpoint, prompt version, request id, latency, input/output/cached tokens, pass/fail reason; add new production failures before prompt fix; human review for safety/compliance/financial decisions.

## Defects
- Date note: page says hosted OpenAI evals become read-only 2026-10-31.
- Promptfoo config uses `apiHost` (verify against Promptfoo docs).
- Responses sample passes `temperature=0` (rejected by some reasoning models).
