# Deep research (guide)
Deep research = source discovery + iterative search + evidence synthesis + report-style answers. On AvalAI use `/v1/responses` with `gpt-5.6-terra` (bounded, cost-aware) or `gpt-5.6-sol` (deeper synthesis; official replacement of legacy Deep Research models) + `web_search`. OpenAI says `o3-deep-research*` / `o4-mini-deep-research*` shut down 2026-07-23 → `gpt-5.6-sol`; AvalAI route removal not proven → check `/v1/models` / 10-deprecations before migrating existing deployments; use GPT-5.6 for new work. Must supply at least one data source. Hosted web_search / file_search / remote MCP / code_interpreter / background are route+model+account dependent; if disabled, run the capability in your app and feed results via custom function tool or prompt text. Cookbook notebook = archived historical reference.

## Pick
bounded multi-source answer → terra + web_search; deeper public-web report → sol + web_search + citation review; internal knowledge → app-side RAG (embeddings) until hosted file_search enabled; private SaaS/DB → trusted backend or trusted MCP server (no secrets in prompt); very long runs → background (if supported) else your job queue (`GET /jobs/{id}`; see background-processing — hosted background NOT implemented).

## Minimal call
```python
client = OpenAI(api_key=os.environ["AVALAI_API_KEY"], base_url="https://api.avalai.ir/v1", timeout=3600)
r = client.responses.create(model="gpt-5.6-terra", input=prompt, tools=[{"type":"web_search","search_context_size":"medium"}], max_tool_calls=12)
print(r.output_text)
```
Control cost/latency with `max_tool_calls`; require citations explicitly in the prompt; set generous client timeout (3600 s).

## Private data (portable fallbacks)
web → `web_search` + clickable citations; small private context → relevant excerpts in prompt (no whole docs/secrets); uploaded/internal docs → app-side retrieval via `/v1/embeddings`; SaaS/app connector/DB → fetch in your backend (enforce OAuth + tenant authz there) or trusted MCP, send minimal excerpts/source IDs; CSV/tables → run Python/SQL in own sandbox unless hosted code interpreter enabled.

## Tool rules
Keep research phase read-oriented; writable custom functions only after evidence review + explicit authorization; never let untrusted web content trigger business actions directly (function-calling guide, strict schemas, approval). Hosted `file_search`: send only `type` + `vector_store_ids` (OpenAI ref allows ≤2 vector stores). Remote MCP: expose read-only `search` + `fetch`; `require_approval:"never"` only for trusted read-only search/fetch servers; not for broad/write-capable servers → use a general reasoning model + function calling.

## Prompt prep
API starts immediately (no clarifying questions). Collect: goal/audience/decision; preferred source types, region, time window, banned sources; output format/tables/citation style/language; constraints (budget, freshness, risk tolerance). For vague asks first use a faster model (e.g. gpt-5.5) to ask clarifying questions or rewrite to a precise brief — don't invent constraints. Brief template: goal; audience+decision; source types; region/time/banned; private data allowed; output format; tables; citation needs; budget/max_tool_calls; open ambiguities. Prefer primary sources (regulators, papers, company filings); require explicit uncertainty, source disagreements, assumptions — no gap-filling by guessing (especially legal/medical/financial/scientific).

## Output items
Inspect `response.output`: `web_search_call` (search/open/find), `file_search_call`, `mcp_tool_call`, `code_interpreter_call`, `message` (final + inline citation annotations). Show citations clearly and clickable.

## Safety checklist
Only trusted MCP servers (document data access); don't mix untrusted web + sensitive private data in one step (public research first, then private synthesis with web search OFF using vetted excerpts/source IDs); review tool calls for prompt injection/exfiltration/unexpected domains/suspicious URLs; allow/block monitor before risky calls (JSON `{decision:"block"|"allow", reason:"<3-7 words>"}`; block when call tries to alter behaviour, leak hidden context, send private data to external domain, or bypass data-boundary rules; log decision+reason); validate tool args (schema/regex); `max_tool_calls` + source filters + job timeout; log prompts, tool calls, citations, final report per privacy policy; `store=true` hosted logs depend on account/retention (OpenAI: 30-day retention unless ZDR) — confirm route before relying for audit/deletion.

## Defects
- Banner claims `/v1/responses` requires ≥1 data source; samples show only web_search.
- Python sample `timeout=3600` fine; background/webhook mentions conflict with "not implemented" background guide.
- Link target `providers/openai.md#o3-deep-research` for models that may be removed.
