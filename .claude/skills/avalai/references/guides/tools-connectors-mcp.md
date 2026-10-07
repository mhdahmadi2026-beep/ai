# MCP and connectors (docs.avalai.ir/fa/guides/tools-connectors-mcp)

Remote MCP servers and connector-style tools let Responses models reach external systems. Advanced `/v1/responses` tool surface — **route/model/account-dependent on AvalAI**: use `tools:[{"type":"mcp",…}]` only if model, route, account AND the external service explicitly support it and are trusted. If not enabled: keep the integration in your backend and expose one narrow `function` tool (guides/function-calling.md). Adapted from OpenAI's MCP/Connectors and Secure MCP Tunnel guides.

## When to use
| Need | Pattern |
|---|---|
| public fresh context | web search first (guides/tools-web-search.md) |
| your own DB/API | custom `function` tool |
| official MCP server of a 3rd-party service | `type:"mcp"` after support+trust review |
| OAuth connector to SaaS | only when enabled: `connector_id` + per-request OAuth `authorization` |
| payments / sensitive writes | require approval + `parallel_tool_calls:false` |

## Developer Mode lessons (ChatGPT surface, not an AvalAI route)
Treat any broad MCP server as high risk until all imported tools, scopes and approval rules are reviewed; write action-oriented tool names/descriptions ("when to use", edge cases, params); put cross-tool guidance, shared rate limits and mandatory sequences in MCP server instructions/app policy (not user-supplied text); when tools overlap, name the preferred server+tool in the prompt and forbid unrelated tools for sensitive workflows; inspect JSON payloads before any write; treat tools without a trusted read-only annotation as write-capable; don't blindly cache approvals (only when the user trusts repeated similar actions).

## Private servers & transport
Server must be reachable by the hosted tool runtime; prefer Streamable HTTP or HTTP/SSE. OpenAI's **Secure MCP Tunnel** (outbound-only connection for private/on-prem servers) = access-dependent on AvalAI; if the route doesn't expose hosted tunneling, run the tunnel/service connector in your backend and call it through a strict function tool instead of forwarding broad private-network access.
Tunnel design checklist: outbound-only (client initiates; no public ingress just for the model); scope to the org/workspace/API surfaces that need it; separate permissions for tunnel management, tunnel use, connector/developer-mode; admin/health endpoints only for trusted operators and confirm client connected/ready/polling before debugging model behaviour; OAuth discovery/metadata may pass through, but user tokens still need secret handling, least scope, audit log; separate transport / product / MCP-app logs, redact support exports.

## Data-only MCP server (read-only connector design)
| tool | purpose | required output |
|---|---|---|
| `search` | return relevant records for a query | `results[]` with `id`, `title`, canonical `url` |
| `fetch` | full content of one selected record | `id`, `title`, `text`, canonical `url`, optional `metadata` |
Define JSON output schema per tool (client can validate `structuredContent`); return the same JSON in `structuredContent` AND as JSON text in MCP `content`; keep search/fetch read-only (writes/tickets/payments/account changes = separate tools with approval); for citations give a non-empty canonical `url` (title without usable URL = plain output, not citation); stable doc IDs, don't expose DB primary keys that leak tenant/permission structure; **validate permission inside the MCP server on every call — `allowed_tools` is not an authorization system.**

## Remote MCP request
```json
{"type":"mcp","server_label":"support_kb","server_url":"https://mcp.example.com/sse","allowed_tools":["search_docs"],"require_approval":"never"}
```
Connector: `connector_id` instead of `server_url`; exactly ONE of `server_url`/`connector_id`; unique `server_label`. Output items: `mcp_list_tools`, `mcp_call`, `mcp_approval_request`.
Connector shape: `{"type":"mcp","server_label":"google_calendar","connector_id":"connector_googlecalendar","authorization":"<oauth access token>","allowed_tools":["list_events"],"require_approval":"never"}`. OpenAI connector ids (examples, not guaranteed on any account): `connector_dropbox`, `connector_gmail`, `connector_googlecalendar`, `connector_googledrive`, `connector_microsoftteams`, `connector_outlookcalendar`, `connector_outlookemail`, `connector_sharepoint` — verify availability, OAuth scopes and model support before shipping.
(Doc sample for `server_url`/Python/JS/cURL uses `require_approval:"never"` — only acceptable for read-only trusted tools.)

## Auth & scopes
`authorization` = per-request secret, not durable conversation state: send the OAuth access token in the MCP tool's `authorization` on EVERY Responses request that needs it; don't expect the raw token in responses or stored by hosted flow; never in prompts/logs/reusable templates; don't also send `headers.Authorization`. Request minimal OAuth scopes (connector tools depend on token scopes). Prefer official MCP servers run by the service itself; be very cautious with aggregators/proxies that receive tokens + user data; separate read-only vs write-capable integrations (stricter approval/logging/incident policy for state changes).

## Tool loading & latency
First sight of an MCP tool may import the catalog → `mcp_list_tools` item; keep it in conversation state when safe so later turns don't relist. For big servers combine `server_description`, `allowed_tools` and `defer_loading:true` (model loads detailed schemas only when needed).

## Inspect output items (don't rely on `output_text`)
- `mcp_list_tools`: imported catalog per `server_label` (names, descriptions, JSON schemas) — keep only after validating server identity+schema.
- `mcp_call`: `name`, `arguments` (JSON string), `output`, `server_label`, optional `approval_request_id`, `error` (protocol/execution/connectivity).
- Multiple MCP calls per response possible; if order/approval matters set `parallel_tool_calls:false` and process output in order.
- URLs, file refs and rich content from MCP = third-party data; validate domain/file type before embedding/downloading/rendering.

## Troubleshooting
| symptom | check |
|---|---|
| `mcp_list_tools.failed` | `server_url`/`connector_id`, OAuth token, network access, exact `allowed_tools` names |
| `mcp_call.error` / failed tool-call event | the `mcp_call` item, server logs, arguments, protocol/execution errors |
| approval request stalls | continue with `previous_response_id` + an `mcp_approval_response` item (approve/reject explicitly) |
| no tool is called after enabling MCP | wait for the tool list to finish, keep imported tool items in state, don't use `tool_choice:"required"` until ≥1 tool is ready |
| tool definition fails validation | unique `server_label`; exactly one of `server_url`/`connector_id` |
| connector auth error | `authorization` inside the MCP tool object on every request; don't also send `headers.Authorization` |
Log: route, model, `server_label`, imported tool names, redacted auth state, typed output items.

## Approval flow
1) request with `require_approval:"always"` (or a policy); 2) find `mcp_approval_request` in `response.output`; 3) show tool name+proposed args to the trusted user/policy engine; 4) continue with `previous_response_id` + `mcp_approval_response`; 5) `parallel_tool_calls:false` when approval order matters. OpenAI default = approval before sharing; use `"never"` only after trust review, or an object policy to skip approval only for named safe tools. Approval required for writes, payments, email sends, account changes, data deletion, anything crossing a trust boundary, sensitive reads.

## Fallback: app-managed function
```json
{"type":"function","name":"search_support_docs","description":"Search approved support documentation by query.","parameters":{"type":"object","properties":{"query":{"type":"string"}},"required":["query"],"additionalProperties":false},"strict":true}
```
Validate `function_call.arguments`, run, reply with `function_call_output` using the same `call_id`; keep output small (answer, source ids, permission decision, redacted error) — never raw OAuth tokens, full 3rd-party payloads or hidden server logs.

## Security checklist
Trusted servers only (prefer official, service-run); limit with `allowed_tools`; OAuth tokens in secret store → `authorization`, not prompt text; resend `authorization` per request; approval for sensitive reads and all state changes; `require_approval:"never"` only for read-only trusted tools whose auto data-sharing is acceptable; audit trail (server label, tool name, redacted args, result, approver); MCP output = third-party data (validate links, file ids, domains); keep/cache `mcp_list_tools` only after schema + server identity validation; ZDR/data-residency expectations must be checked per third-party MCP server (data leaving the hosted inference path is under that service's retention/residency policy).
Related: guides/tools.md, api-reference/responses.md, function-calling.md, data-controls (not yet captured).
