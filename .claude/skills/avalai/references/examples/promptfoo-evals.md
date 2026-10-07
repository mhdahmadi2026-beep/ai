# Evals with Promptfoo and AvalAI (docs.avalai.ir/fa/examples/promptfoo_evals_with_avalai)

Promptfoo = repo-local regression tests for prompts, model upgrades, routing logic and agent workflows; keeps evals next to app code and connects to AvalAI through the OpenAI-compatible SDK. Adapted from OpenAI Cookbook (moving-from-openai-evals-to-promptfoo, SchemaFlow). Use when: comparing two AvalAI models before shifting traffic; improving prompts and catching regressions; failing CI on quality drops; hosted AvalAI Evals API isn't enabled for your account (see guides/evals.md — hosted `/v1/evals` unavailable).

## OpenAI Evals concept → Promptfoo
| OpenAI eval | Promptfoo | AvalAI note |
|---|---|---|
| `data_source_config` | `tests[].vars` + documented fixture shape | keep human labels like `expected_label` next to user input |
| `testing_criteria` | `assert` blocks | deterministic checks before LLM-as-judge |
| `{{ item.correct_label }}` | `{{expected_label}}` / assertion `value` | human-reviewed ground truth |
| `{{ sample.output_text }}` | provider return `{"output": ...}` | for `/v1/responses` return `response.output_text` |
Write the dataset contract before the prompt (here: each case = `ticket` string + expected category).

## Setup
`npm install -g promptfoo`; `python3 -m pip install openai`; `AVALAI_API_KEY`, `AVALAI_BASE_URL=https://api.avalai.ir/v1`.
Provider `evals/support-ticket/avalai_eval_provider.py`: `MODEL=os.getenv("AVALAI_EVAL_MODEL","gpt-5.6-luna")`, `client=OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url=os.getenv("AVALAI_BASE_URL", …))`; `call_api(prompt, options, context)`: `ticket = (context or {}).get("vars",{}).get("ticket", prompt)`; Chat call with system "Classify the support ticket as exactly one of: Hardware, Software, Billing, Account, Other. Return only the label." + user ticket; `return {"output": resp.choices[0].message.content.strip()}`. Key stays on the eval machine, never in YAML.
Responses variant: `client.responses.create(model=MODEL, instructions=<same>, input=ticket, store=False)` → `{"output": response.output_text.strip()}` (for local/CI evals set `store=False`).
⚠ Both samples pass `temperature=0` — rejected by reasoning models / Claude 5.x; drop it for those models.

## Config `promptfooconfig.yaml`
```yaml
description: "AvalAI support-ticket classification regression eval"
prompts: ["{{ticket}}"]
providers:
  - id: "file://avalai_eval_provider.py"
    label: "avalai-gpt-5.5"      # ⚠ label ≠ default model gpt-5.6-luna; set label from AVALAI_EVAL_MODEL to avoid misleading reports
    config: { pythonExecutable: "python3" }
tests:
  - description: "monitor power issue"
    vars: { ticket: "My monitor will not turn on after I changed desks." }
    assert: [{ type: equals, value: "Hardware" }]
  - description: "invoice question"
    vars: { ticket: "Why was my card charged twice this month?" }
    assert: [{ type: equals, value: "Billing" }]
  - description: "password reset"
    vars: { ticket: "I cannot sign in and need to reset my password." }
    assert: [{ type: equals, value: "Account" }]
```
Judge criteria (use sparingly): small closed label sets → exact assertions; add `llm-rubric` only for semantic/multi-step behaviour, e.g. ambiguous ticket "The dashboard looks wrong and my bill changed after an upgrade." must choose Billing or Other, explain no extra facts, not invent account details. Calibrate judge checks on a small human-reviewed set before they can fail CI. (Page's YAML fragment is mis-indented; keep list items aligned under `tests:`.)

## Run
`cd evals/support-ticket && promptfoo validate config -c promptfooconfig.yaml && promptfoo eval -c promptfooconfig.yaml --no-cache && promptfoo view` (`--no-cache` while developing; drop once tests are stable).
Compare models: same config, different `AVALAI_EVAL_MODEL` (e.g. `gpt-5.4` vs `gpt-5.6-luna`; ⚠ page's second command has the typo `AVALAI_EVAL_model=` — env var names are case-sensitive and must be `AVALAI_EVAL_MODEL`); keep the dataset fixed; change ONE thing at a time (model, prompt, tool schema or retrieval context).

## CI (GitHub Actions)
`on: [pull_request, workflow_dispatch]`; steps: checkout@v4, setup-node@v4 (22), setup-python@v5 (3.11), `npm install -g promptfoo`, `pip install openai`, `promptfoo eval -c evals/support-ticket/promptfooconfig.yaml --no-cache` with env `AVALAI_API_KEY: ${{ secrets.AVALAI_API_KEY }}`, `AVALAI_BASE_URL`. Live evals cost money — keep PR evals small (smoke set), full suites before release; never expose secrets to fork PRs.

## Make evals useful
Real-user-like inputs (typos, short messages); negative cases that must refuse/escalate/return `Other`; deterministic assertions (`equals`, `contains`, regex) before LLM-as-judge; define the output contract first; keep human-labelled ground truth fixed when comparing prompts/models; keep previous results so reviewers see what got better/worse; small evals per PR, bigger sets before release.
Related: guides/evals.md, graders.md, agent-evals.md, red-teaming.md (red-team smoke yaml), optimizing-llm-accuracy.md.
