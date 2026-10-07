# Cost optimization (docs.avalai.ir/fa/guides/cost-optimization)

Mostly: fewer tokens, fewer needless requests, right model, route non-urgent work to cheaper tiers. Verify every model/endpoint/account feature against AvalAI docs.

## Levers
| lever | how it cuts cost | see |
|---|---|---|
| fewer requests | merge steps, cache deterministic output, no LLM for fixed UI logic | production-best-practices |
| fewer input tokens | shorten retrieval chunks, compact old context, cache-friendly prompt | token-counting, compaction |
| fewer output tokens | explicit answer budget + `max_output_tokens`/`max_completion_tokens` | latency-optimization |
| smaller model | mini/flash/nano for simple tasks, frontier for hard ones | model-selection, pricing |
| reasoning budget | lower `reasoning.effort` when evals show quality holds | reasoning |
| cached tokens | stable instructions/schemas at the prompt start | prompt-caching |
| async/flex | non-urgent work on cheaper/queued processing | service-tiers, batch-processing |

## Cheaper per request (Responses)
```python
client.responses.create(model="gpt-5.4-mini", instructions="Answer in at most 5 bullets. Do not include background explanations.",
  input="Summarize the operational risks in this incident note: ...", reasoning={"effort":"low"}, text={"verbosity":"low"},
  max_output_tokens=300, store=False)
```
Chat Completions: `max_completion_tokens` + compact retrieved context. GPT-5.5 baselines: `medium` reasoning is a good quality starting point; once evals pass, compare `low` reasoning/verbosity on the same dataset. For compliance, safety, finance, code-migration or high-impact decisions only lower reasoning when eval + human review show the cheaper setting stays reliable.

## Token caps ≠ visible-answer budget (cost trap)
For reasoning models `max_output_tokens` (Responses), `max_completion_tokens` (Chat) and legacy `max_tokens` cover hidden reasoning AND visible output; they don't reserve room for the user-visible text. A request may burn billable output tokens and return empty text (e.g. 1,500 cap with `usage.output_tokens_details.reasoning_tokens` ≈ 1,500). "Answer ≤200 chars" limits the visible answer only, not internal reasoning.
**Detect budget exhaustion before retrying** (don't treat as provider outage/content-filter/success-with-empty): Responses → `status:"incomplete"` + `incomplete_details.reason:"max_output_tokens"` (output may contain only a reasoning item; `output_text` empty); Chat → `finish_reason:"length"` (content empty/truncated); usage → `reasoning_tokens` ≈ `output_tokens` with little/no visible text. Never parse/cache/show/bill an incomplete response as a usable answer. Log status, incomplete/finish reason, configured cap, visible text length, reasoning tokens, model, effort, prompt version, `avalai-request-id`.
### Optimize per successful answer
```text
cost_per_successful_answer = total_cost_of_initial_attempts_and_retries / number_of_usable_answers
wasted_reasoning_rate = reasoning_tokens_from_incomplete_no-text_responses / total_reasoning_tokens
```
A lower cap that causes billable failure + retry isn't cheaper. Per prompt category build a measured envelope (not one global cap): 1) measure P50/P95/P99 reasoning tokens + visible length on successes; 2) pick the lowest `reasoning.effort` passing quality+safety evals; 3) set cap = expected reasoning **+** final-answer margin (within model max); 4) alert on incomplete/no-text rate and repeated exhaustion per model+prompt version; 5) re-eval after changing model snapshot, tools, retrieved context, schema or prompt.
### Bounded recovery policy
On exhaustion retry only by explicit app policy with ONE controlled change by task risk: raise the cap, set `reasoning.effort` `low`/`none`, simplify/split the task, trim irrelevant context, or route to a better-fit model. Never retry unchanged (same billable failure); cap retries so one user action can't multiply cost. For high-impact tasks prefer a bigger budget, task splitting or human review over auto-lowering reasoning. (guides/reasoning.md; production-best-practices.)

## Route by task value
Tier 1: classification, extraction, short summary, formatting → small/cheap models. Tier 2: user-facing answers, multi-step tool workflows → stronger default model + strict output budget. Tier 3: high-value reasoning, code migration, compliance review → larger reasoning model, background processing, extra verification. Track accuracy, cost and latency separately — a cheaper model needing two retries can cost more than a stronger model that succeeds once.

## Budget guardrails (fail safe before spending)
- Per request: reject or downgrade requests exceeding your token-count budget before calling the model.
- Per workflow: cap retries, tool loops and parallel fan-out so one user action can't create unbounded calls.
- Per account/reseller: enforce daily/monthly/customer budgets via the User API (api-reference/user.md) + your billing records.
Over budget → explicit fallback: summarize context first, switch to a smaller model, route to `flex`, move to background processing, or ask the user to approve a costlier action. Never silently truncate compliance/safety/finance/migration context.

## Flex for non-urgent work
Public AvalAI tiers: `default` and `flex`. Send `service_tier:"flex"` only if the model supports it and the job tolerates slowness/temporary unavailability (see 07-service-tiers.md; −50% for select OpenAI models, up to ~900 s). OpenAI flex = lower cost for slower responses + possible `429 Resource Unavailable`. On AvalAI treat as best-effort unless your contract says otherwise: raise client timeout for long flex jobs (don't rely on SDK default), retry 429/resource-unavailable with exponential backoff, fall back to `default` only if completion matters more than cost, don't use flex for interactive checkout, account changes, safety-critical moderation or any path where capacity delay hurts UX. Converting an OpenAI sample with `service_tier:"priority"` → use `default` unless priority is explicitly enabled for your account/route. (Credit packages do NOT cover flex.)
```python
client.responses.create(model="gpt-5.4-mini", input="Generate 50 synthetic support-ticket examples for evaluation.", service_tier="flex", store=False)
```

## Batch & background
Many independent rows → batch-processing pattern or your own rate-limit-aware worker until hosted Batch is enabled for your route (hosted Batch NOT available on AvalAI). One long answer → background-processing guide or app-managed job table. Batch = offline throughput, not user-path latency. OpenAI Batch reference: separate capacity pool, 24 h completion window, `.jsonl` input, unique `custom_id`, result file order may differ from input order → join by `custom_id`; treat expired/failed rows as retryable work units. Good async candidates: evals/prompt comparisons, nightly enrichment, long reports, synthetic data, backfills/migration analysis.

## Measure real cost
Log: model, endpoint, service tier, prompt version, reasoning effort; configured output cap (`max_output_tokens`/`max_completion_tokens`/legacy `max_tokens`); response status, `incomplete_details.reason`, Chat `finish_reason`, visible text length; input/output/reasoning/cached tokens; `avalai-request-id`; estimated cost for quick UI feedback; final billing from the User API.
Use one unit-cost formula across candidate routes. Hidden reasoning tokens are billed at the model's output-token rate on all providers. Check the endpoint's usage semantics first: if `output_tokens` already includes reasoning (and `output_tokens_details.reasoning_tokens` is a breakdown), adding reasoning again double-counts.
```text
# output_tokens already includes reasoning
expected_cost = uncached_input_tokens*input_price + cached_input_tokens*cached_input_price + output_tokens*output_price + retry_rate*average_retry_cost
# route reports visible and reasoning as separate non-overlapping values
expected_cost = uncached_input*input_price + cached_input*cached_input_price + visible_output*output_price + reasoning_tokens*output_price + retry_rate*average_retry_cost
```
Keep prices symbolic, load from your current pricing source; reconcile estimates vs real AvalAI billing (providers may display reasoning usage differently). The comparison that matters: lowest expected cost per usable, quality-passing answer at needed retry rate and latency — not cheapest per token. Find the top ~10% most expensive workflows in the dashboard first; optimize prompt/model choice there before chasing small savings.
Related: pricing, service-tiers, latency-optimization, prompt-caching, token-counting, background-processing, batch-processing (captured), model-selection.
