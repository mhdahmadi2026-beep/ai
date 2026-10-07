# Code generation (docs.avalai.ir/fa/guides/code-generation)

Write/review/refactor/debug code via OpenAI-compatible APIs. OpenAI recommends Responses for API-based coding workflows and Codex for agentic engineering; on AvalAI use `AVALAI_API_KEY` + `https://api.avalai.ir/v1`.

## Workflow choice
| Workflow | Path | Note |
|---|---|---|
| One-shot generate/debug | `/v1/responses` | `instructions` + short `input`, read `response.output_text` |
| Existing chat-based assistant | `/v1/chat/completions` | keep if stable; migrate flow by flow when you need Responses items/reasoning/tools |
| Repo editing/tests/review | Codex with AvalAI provider | guides/setup-codex.md |
| Large refactors | Responses + your own retrieval/tool loop | send only relevant files; preserve `response.output` items when tools/reasoning are used |

## apply_patch & Skills (route-dependent!)
- OpenAI's `apply_patch` tool (`tools:[{"type":"apply_patch"}]`, returns `apply_patch_call` items for create/update/delete) is **hosted-editing, route-dependent on AvalAI — not guaranteed**. If your route doesn't explicitly support it: ask the model for a plain unified diff and apply it in your own review flow / Codex session / patch harness.
- Harness rules (enforcement stays in YOUR app): restrict paths to allowed workspace and reject traversal; apply in scratch copy/transaction; return exactly one `apply_patch_call_output` per `call_id` with `status: "completed"|"failed"` + short error; run tests/linter/`git diff --check` after each round and feed failures back; require human approval for file deletion, dependency changes, generated binaries, migrations, wide rewrites.
- OpenAI Skills = versioned bundles with `SKILL.md` manifests. Treat as privileged instructions+code: review before use, map to specific product workflows, never let end users attach arbitrary Skills from a catalog. If hosted Skills are not enabled on your route, keep the knowledge in repo docs, prompt templates, tool descriptions or local runtime files.

## Task brief template
Goal · Allowed files (exact paths) · Context (only relevant source/docs/stack trace/API contract) · Constraints (non-goals: don't change public API, no new deps, keep RTL text) · Expected output (diagnosis / unified diff / replacement file / test plan / review note) · Verification (command to run).
```text
Goal: Fix the empty-state bug in the billing table.
Allowed files: src/components/BillingTable.tsx, tests/BillingTable.test.tsx
Context: The table renders nothing when invoices=[]; expected copy is "No invoices yet".
Constraints: Keep existing props and CSS classes. Do not add dependencies.
Expected output: Short diagnosis, minimal unified diff, and targeted test command.
Verification: npm test -- BillingTable.test.tsx
```
Use as `input`; keep stable behavior in `instructions`. With tool calls / reasoning items read `response.output`; use `response.output_text` only for final human-readable text.

## Model choice (verify availability in models/ pages)
`gpt-5.5` strong default · `gpt-5.3-codex` agentic Codex-style · `claude-opus-4-8` large codebases/long context · `kimi-k2.7-code` coding-focused alternative. (Samples use `gpt-5.6-luna` via `AVALAI_MODEL` env.)

## Frontend & docs-grounded agents
- Frontend: name framework, package manager, component library, files allowed to change; give screenshot, CSS tokens, accessibility + responsive breakpoints; ask for an implementation path, run the app, compare to visual target; state visible copy, theme tokens, RTL/LTR for bilingual products.
- Docs agents: don't trust model memory for API details — retrieve the doc page/changelog/internal convention first, pass only needed excerpts, require citations of used excerpts, and have the model mark uncertain API behavior as assumptions.

## Examples
Responses (Python):
```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1")
r = client.responses.create(model=os.getenv("AVALAI_MODEL","gpt-5.6-luna"),
    instructions="You are a senior software engineer. Return a concise diagnosis, then a minimal patch suggestion. Do not invent files.",
    input="Find the likely null pointer bug in this code:\n\n...", reasoning={"effort":"high"})
print(r.output_text)
```
JS equivalent: `client.responses.create({model, instructions, input, reasoning:{effort:"high"}})`, `response.output_text`; cURL: POST `/v1/responses` with same body. Chat Completions alternative: `messages=[{role:system},{role:user}]` → `choices[0].message.content`.
(Doc samples' Python/JS strings show `\\n` double-escaped from the page renderer — use a normal `\n`.)

## Prompting checklist
Specify language/framework/runtime version/allowed files; ask for a minimal patch OR a full replacement file, not both; include failing test output/stack trace/exact error; for big repos retrieve only relevant files and have the model list assumptions before changing code; for refactors state non-goals (public API, DB schema); run tests+linters before release — output is a draft.

## Review / diff / security
Plan first for multi-file tasks; prefer unified diffs or clearly named replacement files; ask for public API changes, migration steps, test coverage; run targeted tests first, wider later; treat generated code as untrusted (new deps, shell commands, file paths, SQL, regex, auth logic, network calls); for security-sensitive code request a threat-model pass with assumptions, input validation, authz checks, secrets boundaries.

## Migration notes
`messages`→`input` (+ top-level `instructions`); `choices[0].message.content`→`response.output_text`; for tool-using coding agents preserve typed `output` items (`reasoning`, `function_call`, `function_call_output`); if stuck on Chat Completions for predictable-output file edits see guides/predicted-outputs.md (not yet captured).

## Related (not yet captured): responses-vs-chat-completions, prompt-engineering, predicted-outputs. Captured: function-calling, setup-codex.
