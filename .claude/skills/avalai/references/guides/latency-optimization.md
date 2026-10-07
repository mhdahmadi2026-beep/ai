# Latency optimization (docs.avalai.ir/fa/guides/latency-optimization)

Seven principles: 1) process tokens faster 2) generate fewer tokens 3) use fewer input tokens 4) make fewer requests 5) parallelize 6) reduce user wait time 7) don't default to an LLM. Measure BOTH time-to-first-token and time-to-last-token — a change that cuts full-completion latency still feels slow if the UI doesn't stream/show progress.

## AvalAI checklist
| lever | when | guidance |
|---|---|---|
| smaller model | task is narrow/repetitive/verifiable | try `gpt-5.4-mini`, `gpt-5.4-nano` or a fast provider model before sending every step to a flagship |
| output budget | answer can be short/structured | Responses: `text.verbosity` + `max_output_tokens`; Chat: `max_completion_tokens` (`max_tokens` legacy) |
| reasoning effort | reasoning model thinks long | GPT-5.5 default `medium`; test `low` before `none`; `high`/`xhigh` only if evals prove gain |
| prompt caching | many requests share instruction/schema/prefix | shared text first, dynamic parts later; send `prompt_cache_key` only if route/model supports it |
| service tier | speed vs cost | `service_tier:"default"` for latency-sensitive prod calls; `flex` only for cost-sensitive jobs tolerating slowness/capacity shortage |
| streaming | user can consume partial output | stream to cut time-to-first-token and show real progress |
Model choice, `reasoning.effort`, `text.verbosity` are separate knobs: high reasoning + short final answer still burns hidden reasoning tokens/time. Baseline quality at `medium`; compare `low` for interactive flows; `none` for classification/retrieval/formatting without multi-step planning.
Order of attack: 1) cut output tokens first (visible + reasoning tokens affect latency more than prompt tokens); 2) smallest model passing evals (try clearer instructions, few-shot, or fine-tuning [not available on AvalAI] before sending all steps to the flagship); 3) combine/parallelize independent calls (sequential round trips add directly); 4) cache-friendly prefixes (instructions, tool schemas, policy first; RAG snippets/dynamic state later); 5) use deterministic code instead of an LLM when better.

## Measure first — trace per request
`avalai-request-id`, endpoint, provider, model, service tier, streamed or not; time to first byte, first token, last token; input/output/reasoning/cached tokens; retries, rate-limit errors, provider fallback, final status; user-visible wait (queueing, retrieval, rendering, client buffering). Compare ONE optimization at a time (smaller model may cut final-token latency; streaming improves perceived latency without reducing compute).

## Bottleneck → lever
| bottleneck | symptom | first lever |
|---|---|---|
| slow model compute | long final-token time, many reasoning tokens, flagship for simple work | smaller model, lower `reasoning.effort`, split classification from hard generation |
| output too long | high output tokens, long JSON/function args | lower `text.verbosity`, cap `max_output_tokens`/`max_completion_tokens`, shorter field names, IDs instead of prose |
| prompt too big | high input tokens + low `cached_tokens` | trim RAG context, strip HTML, fixed prefix first, `prompt_cache_key` if supported |
| too many round trips | several sequential `avalai-request-id`s per user action | merge steps in one structured response, parallelize independent calls, speculative execution |
| empty-looking UI | slow TTFT / no progress during tool/retrieval | stream, show tool/retrieval steps, chunk backend post-processing |
| LLM unnecessary | bounded repetitive output | hard-code confirmations, precompute variants, search/filter, UI components |

## 1. Faster token processing
Biggest factor = model size (smaller = faster/cheaper; with careful use can match larger). To keep quality on smaller models: longer more detailed prompt, more few-shot examples, consider fine-tuning/distillation [not available on AvalAI]. e.g. `gpt-5.4-mini` or `claude-haiku-4-5` for quicker answers when adequate. Predicted Outputs (guides/predicted-outputs.md) cuts inference time when much of the output is known (file edits).

## 2. Generate fewer tokens
Token generation is usually the slowest step; **cutting output tokens ~50% can cut latency ~50%**; hidden reasoning tokens also consume budget and time. Natural language: ask for brevity ("under 20 words"). Structured output: minimize syntax — shorter function/field names, drop named args, merge params; e.g. internal `message_is_conversation_continuation` → `cont`, `response_requirements` → `reqs`, move explanations into the prompt/schema comment instead of generating per response. Keep public API contracts readable; validate compressed schemas with evals before customer-facing use. Caps: `max_output_tokens` (Responses) / `max_completion_tokens` (Chat) / `stop` sequences where supported. (Reasoning models: caps include hidden reasoning — see cost-optimization.)

## 3. Fewer input tokens
Less impact: **halving the prompt may improve latency only ~1–5%**. Options: fine-tuning to replace long instructions/examples [unavailable]; filter input (prune RAG results, clean HTML — greedy relevance filter within a token budget); maximize the shared prompt prefix by putting dynamic parts last. For repeated prod traffic a stable prefix beats trimming words: fixed instructions, JSON schema, policy before chat history/retrieval snippets; stable per-workload `prompt_cache_key` if the route supports it, never raw user ids (guides/prompt-caching.md).

## 4. Fewer requests
Each API call = round trip. Combine steps in one prompt (e.g. summarize + translate returning JSON `{"summary","translation"}`).

## 5. Parallelize
Parallelize non-sequential steps; in prod bound concurrency + retry (rate-limit tiers differ per model/endpoint; bounded parallelism safer than firing every document at once, e.g. `asyncio.gather` with `AsyncOpenAI` and a semaphore); offline throughput work → batch pattern (hosted Batch not available → own worker). Sequential steps → **speculative execution**: start step 1 and 2 together (e.g. content check + story generation), verify step 1, cancel/discard step 2 if step 1 fails. Log both request IDs, keep an explicit cancel/discard path (e.g. moderation fails → discard generation, don't stream to user, count wasted tokens in cost dashboards).

## 6. Reduce perceived wait
Stream (`stream=True`; Chat: `delta.content`; Responses: `response.output_text.delta`), chunk output for real-time display, show multi-step progress, loading states/progress bars.

## 7. Don't default to an LLM
Hard-code bounded outputs (confirmations), precompute for limited input spaces, UI for aggregated metrics/search results, classic optimization (binary search, caching, hash tables). Example: dictionary cache for FAQs (`response_cache[query]`); normalise queries, add TTL/invalidation in real use.

## Example: support bot
Initial flow: user message → rewrite as standalone query → decide if extra info needed → retrieval → assistant reasons over query + results → reply. Optimizations: merge query-contextualization with retrieval check (fewer requests); smaller/fine-tuned model for tightly defined tasks; run retrieval checks and reasoning steps in parallel; shorter JSON field names (fewer output tokens). Validate with real traces (TTFT, final-token latency, output tokens, retry rate, user-visible time) before rollout.
Doc sample defects: `sort_by_relevance`/`count_tokens` helpers undefined; sample code uses `max_completion_tokens` correctly in Chat; "fine-tuning/distillation" suggestions can't be done on AvalAI.
Related: prompt-engineering, prompt-caching, predicted-outputs, token-counting (not implemented), streaming-responses, model-selection (all captured).
