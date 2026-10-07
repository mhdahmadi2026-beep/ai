# Predicted Outputs (docs.avalai.ir/fa/guides/predicted-outputs)

Cuts latency when much of the response is known in advance — typically regenerating a text/code file after a small change: send the current file as `prediction.content`; the model can reuse matching tokens faster. OpenAI documents it for **Chat Completions** only (`prediction` parameter). Availability on AvalAI depends on the upstream provider and model. Page suggests OpenAI-family `gpt-4.1`, `gpt-4.1-mini`, `gpt-4.1-nano`, `gpt-4o`, `gpt-4o-mini` where enabled for the account — ⚠ several of these ids have deprecation entries in 10-deprecations.md (e.g. `gpt-4.1-nano`, `gpt-4o-2024-05-13` → `gpt-5.6-*`): verify the model is live (`/v1/models`) and that it accepts `prediction` before building on it.

## Use when
Regenerating a code file, Markdown doc, config or template; most of the final text will equal the original; you can provide the full expected text as the prediction; latency gain > the cost risk of rejected prediction tokens. Don't use when the answer is mostly new, uses tools, has audio output, or generates several choices.

## vs prompt caching
| technique | speeds up | best for |
|---|---|---|
| Predicted Outputs | output generation when most completion tokens are known | regenerating code/Markdown/config/template/text files after a small change |
| prompt caching | repeated input prefixes | fixed instructions, JSON schema, policy text, repeated RAG setup |
Combine for edit workflows where route/model support both: stable instruction/schema first (cached), then the current file as `prediction.content`.

## Chat Completions example
Replace `username` with `email` in a TypeScript class; the file is both input and prediction.
```python
completion = client.chat.completions.create(
    model=os.getenv("AVALAI_MODEL", "gpt-4.1"),
    messages=[
        {"role": "user", "content": "Replace the username property with an email property. Respond only with code, with no markdown formatting."},
        {"role": "user", "content": code},
    ],
    prediction={"type": "content", "content": code},
)
print(completion.choices[0].message.content)
print(completion.usage.completion_tokens_details)   # accepted/rejected prediction tokens
```
cURL: build the JSON with `jq -n --arg code "$CODE_CONTENT"` → `{model, messages:[…], prediction:{type:"content", content:$code}}`; JS: `prediction:{type:"content", content: code}`, `completion.usage?.completion_tokens_details`.

## Responses API: no `prediction`
`prediction` is NOT a Responses parameter. Migrating this non-streaming workflow → drop `prediction`; use `instructions` ("Return only the complete updated TypeScript file. Do not use markdown."), `input` (content parts `input_text`: task + file), `store=False`, read `response.output_text`. If accepted/rejected-token accounting matters, keep Chat Completions. Mapping: `messages`→`input`; system/developer prompt→`instructions`; `choices[0].message.content`→`response.output_text`; `prediction`→no direct equivalent; `accepted/rejected_prediction_tokens`→no Responses usage equivalent.

## Usage details
`completion_tokens_details.accepted_prediction_tokens` (matched the final output, helped latency) and `rejected_prediction_tokens` (didn't match; **may still be billed like completion tokens**). If rejected is consistently high for a workload, drop `prediction` or make it closer to the expected output.

## Where the prediction may match
Not required to be one contiguous block at the start; it can match before and after new text (e.g. adding a route mid-file: unchanged imports, existing routes, startup code all count as accepted). For patch-style tasks: send the whole current file as `prediction.content`; ask for the full updated file (not a diff); keep formatting/comments/surrounding text stable; watch rejected tokens to find prompts causing needless rewrites.

## Streaming
Works with `stream=True` (matched parts may arrive faster): iterate chunks, print `delta.content`. Responses equivalent for transport only: `stream=True`, handle `response.output_text.delta` events (no prediction speed-up).

## Limits (OpenAI's Chat Completions implementation; provider/model dependent)
Text output only; `n` > 1 unsupported; no `logprobs`; positive `presence_penalty`/`frequency_penalty` unsupported; audio input/output and `modalities` incompatible; **`max_completion_tokens` unsupported with prediction**; tool/function calling currently unsupported with prediction.
Related: api-reference/chat (not captured), api-reference/responses, responses-vs-chat-completions (not captured), streaming-responses (captured), prompt-caching (captured).
