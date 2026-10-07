# Fine-tuning API (docs: /fa/api-reference/fine-tuning)

> ⛔ **NOT IMPLEMENTED on AvalAI** ("ویژگی پیاده‌سازی نشده"). Under development, unavailable. The page is a *future compatibility map*; examples aren't runnable until AvalAI announces fine-tunable base models/routes. `data/models.json` publishes no fine-tunable base model. **Never build features that depend on it; don't assume any current AvalAI model is trainable; keep any code behind a feature flag.** Suggest alternatives: prompting, structured outputs, few-shot, RAG/embeddings, caching.

OpenAI guidance (from page): build evals before training; start with high-quality JSONL chat examples; keep default hyperparameters unless evals justify changes.

## Planned endpoints (map only)
- `POST /v1/fine-tuning/jobs` — create
- `GET /v1/fine-tuning/jobs` (`limit` default 20, `after`) — list
- `GET /v1/fine-tuning/jobs/{id}` — retrieve
- `POST /v1/fine-tuning/jobs/{id}/cancel`
- `GET /v1/fine-tuning/jobs/{id}/events` (`limit` default 20, `after`)
- Conditional/not guaranteed: `POST …/pause`, `POST …/resume`, `GET …/checkpoints` (only if AvalAI announces support for your route/model).

## Create-job body
| param | type | req | notes |
|---|---|---|---|
| `model` | string | yes | fine-tunable base model id (none officially available) |
| `training_file` | string | yes | uploaded file id |
| `validation_file` | string | no | uploaded file id |
| `hyperparameters` | object | no | `n_epochs`, `batch_size`, `learning_rate_multiplier` (int/number or `"auto"`, default auto) |
| `suffix` | string | no | ≤64 chars appended to fine-tuned model name if supported |
| `method` | object | no | route/model dependent |

`method` types: `supervised` (prompt + ideal assistant reply; format/style/instruction-following) · `dpo` (preferred vs rejected pairs) · `reinforcement` (grader → numeric reward; needs eval, validated grader, safety checks; design grader before upload, keep validation prompts separate from training, base model must already partly solve the task).

Example (placeholder id): `{"model":"fine-tunable-model-id","training_file":"file-abc123","validation_file":"file-def456","hyperparameters":{"n_epochs":4}}`; SDK: `client.fine_tuning.jobs.create(...)` / `client.fineTuning.jobs.create({...})`. (Go snippet uses `openai.DefaultConfig`/`NewClientWithConfig` → go-openai API, not `openai-go` — source import mismatch.) PHP: plain cURL POST.

## Response job object
`id` (`ftjob-…`), `object:"fine_tuning.job"`, `model`, `created_at`, `finished_at`, `fine_tuned_model` (null until success), `organization_id`, `status` ∈ validating|preparing|queued|running|succeeded|failed|cancelled, `hyperparameters`, `training_file`, `validation_file`, `result_files[]`, `trained_tokens`.

## Events / metrics (provider+method dependent)
`train_loss`, `valid_loss`, token accuracy (SFT convergence/overfit) · `train_reward_mean`, `valid_reward_mean` (RFT) · per-grader score/usage · parse/runtime error rates. Metrics ≠ deploy approval: run external evals + safety checks before using any `fine_tuned_model`; treat each checkpoint id as a separate candidate, evaluate on held-out set, keep rollback to the previous prod model.

## Errors
400/401/403/404/429/500 standard.
Related: models, authentication, fa/guides/rate-limits.
