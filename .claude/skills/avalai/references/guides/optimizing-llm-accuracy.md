# Optimizing LLM accuracy (docs.avalai.ir/fa/guides/optimizing-llm-accuracy)

Maximize correctness and consistent behaviour. Treat accuracy work as a **release cycle**, not a one-off prompt rewrite: 1) define the user-visible failure and its business cost; 2) build a small eval set (representative prompts, expected behaviour, unacceptable answers); 3) diagnose whether the failure comes from missing context, inconsistent model behaviour, or unsafe tool/retrieval flow; 4) change ONE lever, re-run the same evals before shipping.

## AvalAI optimization loop (hosted training/eval are route-dependent)
1. **Baseline with evals** before changing prompt/model/retrieval/tool schema (local or CI eval).
2. **Improve the request**: sharper developer instructions, only the necessary context, few-shot examples where desired behaviour is hard to describe.
3. **Compare model & endpoint**: `/v1/responses`, `/v1/chat/completions`, native provider routes — only where the model supports them.
4. **Prepare training data only after eval evidence**: good input/output examples + hold-out rows — but **hosted fine-tuning is NOT available** on AvalAI (`data/models.json` publishes none) — don't present it as an executable path until AvalAI announces supported base models/routes.
5. **Feed production failures back**: each important failure becomes an eval row before the next prompt/routing change.
Flow: dataset → baseline → one change → compare → rollout decision.

## Mental model: two axes
- **Context optimization** — model lacks knowledge / outdated / needs proprietary data → maximizes **answer accuracy**.
- **LLM optimization** — inconsistent results, format problems, wrong tone/style, inconsistent reasoning → maximizes **behaviour consistency**.
Decision table:
| symptom | first lever | AvalAI implementation |
|---|---|---|
| no access to private/new/domain facts | context optimization | RAG, file input, web/search tools, explicit reference text |
| has the facts but wrong format/tone/style | LLM behaviour | tighten instructions, examples, schemas; `reasoning.effort` / `text.verbosity` on `/v1/responses` |
| same mistake repeats on similar inputs | stronger examples now; plan fine-tuning later | production-like examples, stronger few-shot/schema guidance, hold-out eval set for future hosted training |
| long context loses key facts | retrieval & context layout | test context size and chunk position; bigger window ≠ better accuracy |

## Prompt engineering first
Usually the best start; for summarization/translation/code gen it may suffice. It forces you to define what "accurate" means. Strategies: clear instructions (format/tone/constraints); split complex tasks into subtasks; give the model time to "think"; test changes systematically; provide reference text; use external tools (calculation, data retrieval, verification). Example: adding few-shot examples to a baseline Icelandic sentence-correction prompt raised BLEU 62 → 70.

## Evaluation
Build a good eval set (questions + correct answers) before advanced optimization; with 20+ examples and understood failure causes you have a baseline. Automate with ROUGE/BERTScore for quick comparisons, or a strong judge model + rubric calibrated on human-reviewed examples.
### Judge-model calibration (LLM-as-judge)
Useful for subjective quality, safety, helpfulness, partial credit, but has position bias, verbosity bias, rubric drift — only when simpler checks can't measure quality. 1) deterministic expected answer → string/enum/JSON schema/tool-arg checks first; 2) write the rubric as pass/fail or pairwise criteria before asking for scores; 3) calibrate on human-labelled data + log disagreements; 4) rotate answer order in pairwise comparisons and control length so the judge doesn't favour longer answers; 5) freeze judge model, rubric, temperature and prompt version per eval run — if any changes, re-run the production baseline.
Production-like evals: same retrieved-context format, tool output, schema, safety limits as prod; record pass/fail **reasons** not just a score; add every real production failure before changing the prompt; quick smoke eval on each model/prompt/retrieval/routing change + fuller suite pre-launch; record per run: model id, endpoint (`/v1/responses`, `/v1/chat/completions` or native), temperature, retrieval settings, routing rule.

## Context memory vs learned memory
- **In-context memory problems** (model lacks info) → RAG / relevant context.
- **Learned-memory problems** (needs consistent behaviour patterns) → today on AvalAI: clearer instructions, examples, structured output, tool constraints, model routing; keep high-quality examples for future hosted fine-tuning when AvalAI announces routes.
Additive, can be combined.

## RAG
Retrieve relevant content to augment the prompt before generation. RAG fails in two places: **retrieval problems** (wrong/irrelevant context) and **LLM problems** (misuses correct context) → tune both retrieval system and LLM instructions. (guides/retrieval.md, tools-file-search.md — hosted vector stores unavailable; build retrieval app-side.)

## Fine-tuning (planning only)
Continue training on a smaller domain dataset to improve task accuracy and efficiency (same accuracy with fewer tokens/smaller models). Hosted fine-tuning for base models is not published on AvalAI → guide = preparation: build dataset, eval and rollout criteria now; don't call it an AvalAI execution path until announced. Best practices: baseline with prompt engineering first; quality over quantity (start with 50+ high-quality examples); examples representative of real inputs; "prompt baking" — log pilot prompts/outputs, turn them into real training examples, remove secrets and low-quality rows; keep a hold-out set so training-score gains don't hide overfitting; if production uses RAG, include RAG context in fine-tuning examples (else the model learns an easier task than production).

## Combining approaches
Short prompts/schemas/examples reduce repeated instruction tokens; teach complex behaviour via prompt examples now (fine-tuning only when a supported AvalAI route exists); inject private/new/task-specific info with RAG, file context, search and tools. OpenAI's Icelandic case study = mental model, not an AvalAI recipe: few-shot improved behaviour, fine-tuning raised consistency in that historical OpenAI setup, and adding RAG **lowered** the score because the task needed learned behaviour, not extra context → eval-first: RAG only when failures come from missing context; stronger prompt/schema/routing/future fine-tuning when failures come from inconsistent behaviour.

## How accurate is "good enough"?
Business: identify key success/failure cases + costs; compute break-even accuracy (see model-selection.md: loss/(gain+loss)); measure empirical stats (CSAT, decision accuracy, time-to-resolution). Technical: design for graceful failure; trade accuracy vs UX vs operating cost; when confidence is low or a wrong answer is costly ask a clarifying question or hand off to a human; for high-impact actions (payments, medical/legal/security decisions, irreversible writes) prefer assistant mode over full automation.
Related: prompt-engineering, model-selection, fine-tuning (planning), evals, OpenAI model-optimization + evaluation-best-practices guides (all captured except OpenAI external).
