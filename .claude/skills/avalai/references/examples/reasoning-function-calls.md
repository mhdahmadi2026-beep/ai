# Reasoning models with function calling (docs.avalai.ir/fa/examples/reasoning_function_calls)

Multi-step tool use needs a loop: call the model → run requested functions → return `function_call_output` items → repeat until a final message. Adapted from OpenAI Cookbook `reasoning_function_calls.ipynb`. Use when tool calls may depend on earlier results, the model needs several reasoning steps, you want auditable handling of unknown tools/bad args, or you want API-managed state via `previous_response_id`.

## Pick ONE state strategy (and keep it)
Function calling with reasoning models is more reliable when the next request can see the earlier reasoning + tool items.
| pattern | when | what to preserve |
|---|---|---|
| `previous_response_id` | API-managed response-chain state is OK | send only new `function_call_output` items + latest `previous_response_id`; **resend important `instructions` every request** |
| manual item replay | audit log, retention rules, deletion control, custom compaction | replay relevant `response.output` items UNCHANGED, esp. `reasoning`, `function_call`, `function_call_output` from the latest `user` message onward |
| stateless / zero-retention-like | `store:false` or can't rely on stored state | if the route supports it, `include=["reasoning.encrypted_content"]` and replay the encrypted reasoning items (don't reveal/rewrite reasoning text) |
When replaying manually don't collapse everything into a plain assistant message; keep each `call_id` paired with its `function_call_output`; keep `phase` (if the route/model returns it) unchanged.

## Python loop (verified shape)
```python
MODEL = "o3"   # ⚠ doc sample; o3 snapshots shut down 2026-12-11 (10-deprecations: → gpt-5.6-sol/terra) → use a current reasoning model
tools = [{"type":"function","name":"get_customer_status","description":"Look up account status for a customer ID.",
          "parameters":{"type":"object","properties":{"customer_id":{"type":"string"}},"required":["customer_id"],"additionalProperties":False}},
         {"type":"function","name":"create_case_id","description":"Create a support case ID for a priority level.",
          "parameters":{"type":"object","properties":{"priority":{"type":"string","enum":["low","normal","high"]}},"required":["priority"],"additionalProperties":False}}]
tool_mapping = {"get_customer_status": get_customer_status, "create_case_id": create_case_id}

def run_tool_calls(response):
    outs=[]
    for item in response.output:
        if item.type != "function_call": continue
        tool = tool_mapping.get(item.name)
        if tool is None: result = f"Tool {item.name} is not registered."
        else:
            try: result = tool(**json.loads(item.arguments))
            except Exception as exc: result = f"Tool {item.name} failed: {exc}"
        outs.append({"type":"function_call_output","call_id":item.call_id,"output":result})
    return outs

response = client.responses.create(model=MODEL, reasoning={"effort":"medium","summary":"auto"}, tools=tools, input=question)
while True:
    outs = run_tool_calls(response)
    if not outs: return response.output_text
    response = client.responses.create(model=MODEL, reasoning={"effort":"medium","summary":"auto"}, tools=tools,
                                       input=outs, previous_response_id=response.id)
```
Sample tools: fake DB (`cus_123` enterprise paid through 2026-09-01; `cus_456` trial ends in 3 days), `create_case_id` → `f"{priority.upper()}-{uuid4()}"`. JS version identical (`crypto.randomUUID()`, `JSON.parse(item.arguments)`, `toolMapping`).
cURL second request shape: `{"model":…, "input":[{"type":"function_call_output","call_id":"call_abc123","output":"…"}], "previous_response_id":"resp_abc123"}` — result must carry the ORIGINAL `call_id`.
Notes/defects: add `strict:true` to the tool schemas; add a **max-iterations cap** (the doc loop is unbounded — page itself lists this as a risk); `output` must be a string (JSON-encode objects); `reasoning.summary:"auto"` availability is route/model dependent; `previous_response_id` requires stored responses (don't combine with `store:false`); `parallel_tool_calls:false` for state-changing tools.

## Errors to handle
Unknown tool name → return structured error output (don't crash); invalid JSON arguments → return the parse error so the model can self-correct; tool timeout → return the timeout result or cancel the workflow; repeated tool calls → cap loop count; sensitive tool output → redact before sending to the model when full output isn't needed.

## Best practices
Narrow explicit tool schemas; validate arguments in your app even with strict schemas; log tool name, call id, latency, result; use `previous_response_id` when API-managed state fits; when advancing context manually, pass reasoning and function-call items through UNCHANGED (no summarising); for strict audit/retention/deletion persist conversation items in your own system in the right order.
Related: function-calling.md, reasoning.md, conversation-state.md, production-best-practices.md, responses-vs-chat-completions.md.
