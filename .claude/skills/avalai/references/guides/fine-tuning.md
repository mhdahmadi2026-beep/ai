# Fine-tuning planning guide — **NOT implemented on AvalAI** (see api-reference/fine-tuning.md)
Banner: creating fine-tuning jobs is in development, unavailable; page = planning/migration guide. `data/models.json` lists NO fine-tunable base model → assume nothing is trainable via AvalAI. **Never emit** `fine_tuning.jobs.create`, `ft:` model ids, `purpose="fine-tune"` uploads as runnable code. OpenAI's own hosted FT platform winding down for new OpenAI users (OpenAI-specific; don't extrapolate). When AvalAI announces: check model-details, api-reference/fine-tuning, release news for base models, supported methods, training limits, file retention, billing.

## Benefits (when available)
Higher quality than prompting alone; more examples than fit in a prompt; token savings from shorter prompts; lower latency with smaller tuned model. Lifecycle: prepare+upload data → create job → evaluate (evals guide) & iterate data → use model.

## Methods (future compat map)
| method | for | not when |
|---|---|---|
| SFT | tone/format/instruction-following, cost/latency once prompting works | adding new factual knowledge (use RAG/tools) |
| vision FT | domain visual recognition (if base supports) | text task / generic vision |
| DPO | subjective preferences (style, politeness, ranking, refusal behaviour) | no reliable preferred/rejected pairs |
| RFT | complex reasoning with measurable reward + expert grader | experts disagree, base success 0%, task guessable |
RFT readiness: experts agree on a good answer; grader can score without hidden human judgement; base eval neither ~0 nor ~perfect; base solves some examples; can't be gamed by guessing; separate train/validation/final-test sets.

## Optimize BEFORE fine-tuning
1 model choice (stronger / reasoning effort) 2 better prompt 3 examples/context (few-shot, RAG, embeddings) 4 tools (function calling: deterministic APIs/DB/calculator/guardrails) 5 helper models (classifier, moderation, evaluator, router) 6 then SFT/DPO/RFT. FT on a weak prompt cements weak behaviour; keep best production prompt + tool instructions in training examples unless evals show removal is safe.
Use FT when: consistent style/tone/format; reliable output for complex instructions; many edge cases; skill hard to prompt ("show don't tell"); smaller tuned model for cost/latency.

## Dataset (JSONL, one example per line)
Chat format: `{"messages":[{"role":"system|user|assistant","content":"..."}]}`; assistant messages = ideal output; ≥1 assistant message; target areas where base model fails. Multi-turn: all assistant turns trained by default; `"weight":0` skips a turn, `1`/omitted trains. Include best system+user prompts in EVERY example (esp. <100 examples). Counts: minimum 10; start 50–100 high-quality, evaluate on holdout before adding data; no improvement → rethink task/data. Train/validation split (no overlap); fixed validation set before training; separate final test set for RFT-like flows (grader can be optimized against). Examples truncated beyond model max context (see model-details; count tokens with tiktoken for OpenAI models).
Cost estimate: `(base training price per 1M tokens /1,000,000) × tokens in training file × epochs`; validation tokens typically free.
Validation checklist: valid JSON per line; `messages` key; role+content per message; roles in {system,user,assistant}; ≥1 assistant message (except DPO); tokens within limit.
Quality before quantity: add examples of actual failures; remove contradictions/typos/style drift/unsafe claims from targets; match production distribution (don't over-represent refusals/tool calls/long answers); don't teach impossible capabilities; consistent annotation guidelines; small clean > big noisy; add data only when evals say it helps (compare full vs subset runs).

## Upload / job / use (template ONLY)
Upload JSONL with `purpose="fine-tune"`; job: `training_file`, `model` (supported base id), optional `validation_file`, `hyperparameters` (`n_epochs`, `learning_rate_multiplier`, `batch_size`), `suffix` (≤64 chars), `method` (`{"type":"dpo","dpo":{"hyperparameters":{"beta":0.1}}}`; default supervised). Manage: list, retrieve, `list_events`, cancel, `models.delete(ft_model)`. Tuned model id like `ft:<base>:<org>:<suffix>:<id>`; may take minutes after completion; also usable on `/v1/responses` as `model` if route supports.
Status → action: validating/preparing (check purpose, JSONL, token limit, image format, method fields); queued (record dataset version, model id, hyperparams, method, eval suite); running (events: loss, validation loss, token accuracy, reward metrics, grader/parse errors); succeeded (DON'T deploy yet: fixed evals, safety checks, side-by-side vs base); failed/cancelled (keep job id, events, file ids, request id). Pause/resume & checkpoint eval = conditional features.
Metrics event: `{"type":"metrics","data":{"step":100,"train_loss":...,"valid_loss":...,"train_mean_token_accuracy":...,"valid_mean_token_accuracy":...,"full_valid_loss":...}}`; `result_files` CSVs via Files API.
Checkpoints: compare final, each checkpoint, base, prompt-only baseline on same fixed eval; choose by validation not training metrics; RFT: inspect grader outputs/reward traces (reward hacking); promote only after safety + rollback to previous model id.
Iterate: fix data quality first; add quality examples for edge cases (doubling can help); hyperparameters — defaults first; underfit narrow tasks → more epochs; overfit/diversity loss → fewer; non-convergence → learning rate. RFT: watch `train_reward_mean`, `valid_reward_mean`, per-grader reward, parse errors, grader errors, reasoning tokens; train↑ valid flat/↓ = overfit grader/model; high parse errors → fix response schema/grader variables.
Vision FT (if supported): messages with content parts `text` + `image_url` (URL or base64); check provider image formats (PNG/JPEG/WEBP/non-animated GIF), size (<10 MB), content limits (no people/faces/children/CAPTCHAs); `detail:"low"` cuts tokens/cost.
DPO data: `{"input":{"messages":[...]},"preferred_output":[{"role":"assistant","content":"..."}],"non_preferred_output":[...]}`; `method={"type":"dpo"}`; beta (0 aggressive, 2 conservative, default auto); often SFT on preferred outputs first, then DPO.

## Safety / rollout
Run same eval suite on base, tuned, prompt-only baseline; slice by language, user segment, doc type, refusal type, tool path; safety checks (policy, privacy, hallucination, prompt injection, exfiltration); tuned model must not claim actions product can't do; rollback path; log model id, dataset version, eval run id, request id, production feedback tags; human review before training data upload / activation in regulated or high-impact domains.

## Defects
- Example claims about `ft:fine-tunable-model-id:avalai-org:...` are placeholders. "Limits" like <10 MB images are provider-specific.
- Formula line duplicated verbatim; `fine_tuned_model_id` sample uses chat completions + Responses equivalent.
