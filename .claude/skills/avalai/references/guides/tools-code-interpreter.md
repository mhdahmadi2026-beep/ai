# Code Interpreter (docs.avalai.ir/fa/guides/tools-code-interpreter)

Hosted OpenAI tool on `/v1/responses`: `tools:[{"type":"code_interpreter","container":{…}}]` — model writes+runs Python in a sandboxed container, inspects results, returns generated files. Adapted from OpenAI's guide.

> ⚠ **Route/model/account-dependent on AvalAI.** Use the hosted shape ONLY if the chosen `/v1/responses` route explicitly supports `code_interpreter`. Otherwise run code in your own restricted backend and expose one narrow `function` tool (see below). Default to the fallback unless support is confirmed.

## When to use
| Task | Path |
|---|---|
| math, data analysis, CSV inspection | hosted when enabled; else app-managed Python function |
| user-uploaded files | validate+store in your app, then send approved file IDs or extracted data |
| charts/artifacts | hosted container files if enabled; else your own storage |
| image inspection/pre-processing (crop/zoom/rotate/analyze) | hosted only when file input + CI enabled; else backend image processing |
| iterative computation (write code, inspect error, retry) | good fit |
| production automation | prefer deterministic backend tools with policy checks + audit log |
Don't use for arbitrary untrusted execution, hidden network access, secret handling, or when one deterministic library call suffices. Vision-heavy: validate type/size first, strip unneeded metadata, make the model explain each transformation, store originals + generated artifacts yourself if auditability is needed.

## Hosted shape (only after confirming support)
The model knows the tool as the **"python tool"** ("code interpreter" in prompts usually works; in production instructions say explicitly when to use "the python tool" vs answer without code). If Python MUST run → `tool_choice:"required"` (supported routes); if optional → leave automatic and tell the model to use it only when it improves accuracy, reproducibility or artifact generation.
```python
client.responses.create(model=os.getenv("AVALAI_MODEL","gpt-5.6-luna"),
  instructions="You are a careful data analyst. Use Python only when it improves accuracy, explain assumptions, and return the final answer clearly.",
  input="Solve 3x + 11 = 14 and show the verification.",
  tools=[{"type":"code_interpreter","container":{"type":"auto","memory_limit":"4g"}}])
# items: type == "code_interpreter_call" → item.container_id
```

## Containers & files (hosted features need route confirmation)
- Container modes: `auto` (API creates or reuses the active container from prior `code_interpreter_call` context) or explicit (create first via `/v1/containers`, reference its id).
- `memory_limit` tiers (OpenAI): `1g` default, `4g`, `16g`, `64g` — higher tier costs more, applies for the container's whole life; verify AvalAI availability/pricing before exposing a tier choice to users.
- **Ephemeral:** expire after **20 minutes of inactivity**, data deleted → download needed files while active; keep durable artifacts yourself; expired containers don't revive (create new, re-upload). Metadata reads / add-remove files refresh activity.
- Input-file inclusion may auto-upload files into the container; generated files (charts, CSV) return as `container_file_citation` annotations (`container_id`, `file_id`, filename) → parse to build download links or move to your storage before expiry.
- Debug: `include:["code_interpreter_call.outputs"]` (route permitting); redact stdout/stderr/files/tracebacks before showing users or persistent logs.
- OpenAI-supported uploads (source, office docs, PDF, CSV/JSON/XML, archives, images) — still keep your own allowlist; don't accept every MIME type everywhere.
- Never feed user files to the model before malware/size/type/policy checks; log container id, file ids, generated artifact names, request id; never place secrets/DB creds/private tokens in the execution environment.
- Data retention: with response storage enabled state may persist; set `store=false` when you don't need server-side state (and document features that depend on it); copy artifacts to own storage; strip secrets before upload (stdout/stderr/files/annotations can enter tool output or logs); third-party services called by your runner have their own retention policies.

## Fallback: app-managed Python tool
```json
{"type":"function","name":"run_python_analysis","description":"Run a small approved Python analysis over prevalidated inputs.",
 "parameters":{"type":"object","properties":{"task":{"type":"string","description":"Short description of the analysis to run."},
  "code":{"type":"string","description":"Python code that uses only approved libraries and input files."},
  "allowed_file_ids":{"type":"array","items":{"type":"string"}}},
  "required":["task","code","allowed_file_ids"],"additionalProperties":false},"strict":true}
```
Checklist: allowlist-check generated code before running; run in a container with no network by default, short CPU/memory limits, clean filesystem; mount only validated input files, write outputs to a temp dir; return structured result + signed artifact URL (not raw paths); human approval for costly jobs, external writes or sensitive datasets. Via `/v1/responses` handle like any function tool: read `function_call`, run in backend, send matching `function_call_output` with the same `call_id`; keep stdout/stderr/artifact URLs/validation errors compact.

## Security checklist
Allowlisted packages only; block shell escape, subprocess and arbitrary network calls without explicit approval; strip secrets from prompt/files/stdout/stderr/artifacts; scan uploaded and generated files before storing/showing; limit runtime, memory, output size, artifact count; audit log (user id, request id, model, tool args, policy decision, artifact metadata); treat charts/CSVs/generated files as untrusted until validated.
Pricing: hosted CI $0.03 per session (guides/tools.md / pricing).
Related: guides/tools.md, function-calling.md, tools-file-search.md, api-reference/responses.md.
