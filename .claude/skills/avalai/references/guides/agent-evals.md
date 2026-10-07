# Agent workflow evals (guide) — no hosted trace grading / `/v1/evals` on AvalAI
Evaluate the WHOLE workflow, not only the final answer (tool calls, multi-turn state, guardrails, retrieval, handoffs). Use OpenAI trace/dataset/grader concepts as design reference only; run local/CI evals over logged typed `/v1/responses` output items. See guides/evals, guides/graders, guides/agents.

## What to log per run
Input context (user request, state strategy, retrieved snippets, model id); plan (goal, constraints, success criteria, stop condition); tool calls (name, JSON args, side effects, errors, retries, outputs); guardrail & handoff (moderation decisions, schema-validation failures, blocked actions, source/target of handoff + reason); state (`previous_response_id`, conversation id, selected files, citations, handoff target, assistant `phase` when replaying output items manually — preserve unchanged); final answer (user-visible output, cited evidence, refusal text, request id). Don't grade only `response.output_text`: most failures happen earlier (wrong tool, unsafe args, missing retrieval filter, loops, lost state).

## Levels
trace review (debug: log output items, tool I/O, request ids, timings) · trace grading (JSONL traces + Promptfoo/pytest/custom runner) · dataset evals (versioned cases in CI) · production monitoring (sample redacted real runs, feed failures back to dataset). Start with traces while behaviour is changing; move to datasets once good behaviour is clear.

## Triage questions per trace
right tool chosen / banned tools avoided / stopped after enough evidence? handoff happened when it should and carried right context? violated developer instruction, safety policy, schema rule, user limit? retrieved context/file ids/tool output actually support the answer? retries/empty results/timeouts → safe recovery or loop? final answer leaked tool internals, dropped required citation, overconfident? Convert repeating failures to deterministic graders first; LLM judge only for tone/reasoning quality/partial credit.

## Local trace-grading loop
1 pick representative traces (success, failure, edge case per tool path/handoff) 2 write grader contract (required tools, forbidden tools, safe-arg rules, required citations, stop condition) 3 deterministic checks first (parse trace JSON; fail fast on missing required tool call, invalid args, unsafe side effect, final answer w/o citation) 4 add LLM grading only for judgment (recovery quality, handoff reason, tone, partial-credit reasoning) 5 promote to dataset-based eval in CI on prompt/tool/model/routing changes.

## Trajectory rubric (explicit pass/fail first)
goal understanding · tool selection (needed tools only) · argument safety (complete, valid, within allowed side effects) · state handling (prior response state, user prefs, retrieved context) · error recovery (empty result, tool error, refusal, timeout, no loops) · grounding (cite retrieved evidence or state what's missing) · stop condition (no over-calling). High-impact workflows → add human review.

## Handoff / complexity decisions
Don't split into multiple agents just because it looks cleaner; prove with trace/dataset that a simple prompt/tool loop fails at a specific boundary. Add agent/handoff/retrieval step/guardrail only when eval shows: tool overload (wrong tool among many), policy conflict (stricter safety/compliance for one task), context loss (specialist needs focused context), recovery failure (can't handle empty/error/topic change). After adding handoff, add eval cases: "handoff must happen", "must NOT happen", "must return control" (catches circular routing & out-of-scope specialists).

## Portable JSONL trace case
```json
{"id":"refund-policy-tool-route","input":"Can I refund unused credits?","expected":{"must_call_tool":"search_policy","must_not_call_tools":["issue_refund"],"final_answer_must_cite":["refund-policy.md#credits"]},"trace":[{"type":"function_call","name":"search_policy","arguments":{"query":"unused credits refund policy"}},{"type":"function_call_output","name":"search_policy","output":{"source_id":"refund-policy.md#credits","text":"Unused credits are refundable within 14 days."}},{"type":"message","output_text":"Unused credits are refundable within 14 days [refund-policy.md#credits]."}]}
```
Grade deterministically: tool names, forbidden side effects, required citation, no unsupported claims.

## Logging with Responses
`trace_items = [item.model_dump() for item in response.output]`; log `{"response_id":..., "trace":...}`. If model returns a function call: execute in app, append `function_call_output`, continue loop; keep ALL loop steps in the trace. Manual replay (no `previous_response_id`): keep returned assistant item fields like `phase` unchanged (dropping them can make mid-run preambles look like final answers).

## CI checklist
Add an eval case for every production incident BEFORE changing the prompt; smoke trajectory evals on PRs touching prompts/tools/retrieval/routing; compare candidate model ids with identical dataset+tool schema; record latency, tool-call count, retries, token usage next to pass/fail; no secrets in trace fixtures (redacted samples in repo).

## Defects
- Sample tool lacks `strict` and function call items use `function_call_output` with `name` (not required by Responses).
- Trace JSONL schema (`type: message/output_text`) is illustrative, not OpenAI's raw item shape.
