# Shell tool (docs.avalai.ir/fa/guides/tools-shell)

Lets the model request terminal commands for deterministic tasks (inspect files, run scripts, convert data, make artifacts). OpenAI documents hosted Shell containers and local shell runtimes via `/v1/responses`. Adapted from OpenAI's guide.

> ⚠ **Hosted Shell is route/model/account-dependent on AvalAI.** Use `tools:[{"type":"shell",…}]` only if the chosen `/v1/responses` route explicitly supports it (confirm in staging). Otherwise run commands in YOUR sandbox and return results via a strict `function` tool or a shell-call loop. Default to the fallback.

## When to use
| Task | Path |
|---|---|
| deterministic CLI tools | app-managed shell, or hosted after route confirmation |
| inspect repo / text files | local sandbox, read-only mounts where possible |
| generate report/artifact | write to controlled temp storage, then copy approved files to durable storage |
| package install / network access | allowlist + approval + audit log |
| user-submitted commands | avoid by default; need validation, sandbox, explicit consent |
Don't use for plain text generation, simple math, unrestricted web access, secret handling, interactive TTY workflows, or destructive commands without human approval.

## Hosted shape (confirm support first)
```python
client.responses.create(model=os.getenv("AVALAI_MODEL","gpt-5.6-luna"),
  instructions="Use the shell only for safe, read-only inspection unless the user explicitly approves a write. Keep commands non-interactive.",
  input="List the current working directory and show the Python version.",
  tools=[{"type":"shell","environment":{"type":"container_auto"}}], tool_choice="auto")
# output items: type == "shell_call" → call_id, action
```
JS/cURL same body. Hosted shell = Responses API tool only (not Chat Completions).
Hosted-runtime notes (verify each): ephemeral Linux containers; may write temp files and return downloadable artifacts if the route supports container/file APIs; reusable containers, `container_reference`, mounted skill bundles, inline files and `domain_secrets` are hosted-runtime features, not portable guarantees; **network OFF by default** — if enabled use an org allowlist + tighter request-level `network_policy`; any third-party endpoint a command contacts has its own retention/residency policy.

## Skills & apply_patch (same route-dependence)
OpenAI's richer runtime: Skills mount reusable instructions/files, Shell does discovery/testing, `apply_patch` returns structured create/update/delete. Use only if the route explicitly supports each tool; otherwise keep the runtime in your backend.
| OpenAI pattern | safe AvalAI adaptation |
|---|---|
| hosted `skill_reference` | keep reviewed workflow instructions in repo docs/local files; mount only in your trusted runtime |
| local shell skills | give your runner the `SKILL.md` excerpt/path; don't assume hosted Skill upload |
| `apply_patch_call` | validate+apply diffs in your own harness, return `apply_patch_call_output` success/failure |
| patch + shell loop | run tests in sandbox, feed command failures back, approval for writes/destructive commands |
Review Skills as code/privileged instructions (a malicious/over-broad Skill can alter tool choice, exfiltrate via shell/network, suggest destructive automation); no open Skill catalog for end users; map approved Skills to specific workflows + approval rules. See guides/code-generation.md for the patch harness rules.

## Fallback: app-managed shell
```json
{"type":"function","name":"run_safe_shell_task","description":"Run an approved, non-interactive shell task in a locked-down sandbox.",
 "parameters":{"type":"object","properties":{"task":{"type":"string"},"allowed_command":{"type":"string"},"working_directory":{"type":"string"}},
  "required":["task","allowed_command","working_directory"],"additionalProperties":false},"strict":true}
```
Checklist: match commands against an allowlist (never run raw model-generated shell text); run with clean env, no inherited secrets, read-only mounts where possible, short CPU/memory/time limits; capture `stdout`, `stderr`, exit code, timeout status, artifact metadata; return a compact `function_call_output` (store big files yourself, return signed URL only after scan); approval for package install, network, write, delete, upload, email, payment or any external state change.

## Safety checklist
Treat command output and fetched web content as untrusted input; keep API keys/DB URLs/SSH keys/OAuth tokens out of prompts, command args, stdout, persistent logs; accept only non-interactive commands (reject TTY prompts, password requests, long-running daemons unless designed for them); log user id, `avalai-request-id`, model, command plan, policy decision, exit result, touched files, artifact ids; document Shell vs Code Interpreter vs Computer Use separately (different execution model, approval needs, artifact behavior).
Related: guides/tools.md, tools-code-interpreter.md, function-calling.md, api-reference/responses.md.
