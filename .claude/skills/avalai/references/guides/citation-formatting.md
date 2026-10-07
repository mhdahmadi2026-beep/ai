# Citation formatting (docs.avalai.ir/fa/guides/citation-formatting)

Source-grounded products need verifiable citations. Patterns adapted from OpenAI for `/v1/responses`, `/v1/chat/completions`, web search and manual RAG.

> Hosted-tool citations are route/model-dependent. When AvalAI returns provider-managed citations, preserve the returned source IDs. For manual retrieval / injected context, build stable source IDs in your app and instruct the model to cite only those IDs.

## When to cite
RAG assistants answering from your docs; web-search answers; compliance/legal/support/finance workflows needing an audit trail; long reports where paragraphs rely on different sources. Don't make the model cite general knowledge, unsupported memory or content never given to it.

## Citable units
| unit | good for | note |
|---|---|---|
| document | overall provenance | when page-level support suffices |
| block/chunk | most RAG systems | **default**: stable, readable, precise enough |
| line range | audit / legal review | only if your retriever reliably stores line offsets |
Keep source IDs stable across retries. **Source ID** (token the model outputs, e.g. `block_42`, `turn0file1`) ≠ **locator** (evidence the UI shows: `L8-L13`, paragraph 21, highlighted chunk, URL fragment). The model emits `block_42`; your app maps it to URL/file/paragraph/line highlight. Don't let the model invent locators unless the retriever supplied them in that request.

## Prompt format (OpenAI markers)
`CITATION_START` = ``, `CITATION_DELIMITER` = ``, `CITATION_STOP` = ``, family `cite`.
```text
## Citations
The provided context contains citable blocks such as:
<BLOCK id="block_42"> ... </BLOCK>
Each block ID is a source reference. Cite only block IDs that appear in the provided context.
Write a citation as: cite<block_id>
Rules:
- Place citations after punctuation.
- Do not place citations inside Markdown links, bold text, italics, or code fences.
- Do not write block IDs verbatim outside citation markers.
- Do not invent source IDs, URLs, titles, or line ranges.
- If the context does not support the answer, say what is missing instead of citing.
- If multiple blocks support a claim, cite each supporting block.
```
Tool-managed output: keep tool-returned IDs (`turn0file1`, `turn0url2`, `turn1block0`) and tell the model to cite exactly those; with multiple tool runs the `turn#` prefix can change per call → validate citations against the IDs returned in the same response. Injected context: build stable block ids before calling AvalAI (`block_42` or `turn0block42`), same format in prompt and parser. Line-level: `citeturn0file1L8-L13` — only when retrieved/injected context already has trustworthy line numbers.
⚠ **Escaping pitfall:** the page's Python/JS RAG samples write `\\ue200…` inside normal string literals, which sends the literal 6-character text `` (backslash-u…) to the model, while the parser expects the real private-use code points U+E200/E202/E201. Pick one: send the real characters (`""` single-escaped in the source) or — more robust — use plain ASCII markers such as `[[cite:block_42]]` and a matching regex; keep prompt and parser identical.

## Hosted tool annotations
When a route returns OpenAI-compatible annotations, treat them as the source of truth: web search / deep research `url_citation` (URL, title, character span `start_index`/`end_index`). Streaming: collect `response.output_text.annotation.added` events, attach after `response.output_text.done` / `response.completed`. UX contract: web-search citations visible, clickable, near the supported claim; keep `url`,`title`,`start_index`,`end_index`; if a result has no usable URL treat it as ordinary tool context and cite your own stable source id instead of an empty link; validate file citations and generated-artifact references against the current user's permissions before showing links; don't trust source names that appear only in prose — render from annotations or source ids you created in that request.

## Grounding quality rules (add to RAG/web/compliance/legal/finance prompts)
Cite only sources that directly support that sentence/clause; prefer authoritative, current sources for time-sensitive or regulated claims; use diverse sources when comparing viewpoints/vendors/policies/regions; when sources conflict, cite the conflicting sources and explain the disagreement (don't smooth it); never invent citations/URLs/titles/line ranges — say what's missing.

## Manual RAG example (Responses)
Blocks `{id,title,text}` → `<BLOCK id="…" title="…">text</BLOCK>` joined; `instructions="Answer only from the citable blocks. Use citations in the format …cite…<block_id>…. Place citations after punctuation. Never invent block IDs."`; `input=[{"role":"developer","content":"Citable context:\n"+context},{"role":"user","content":question}]`, `store=False`. Legacy Chat: same instructions in a `developer`/`system` message and the citable blocks in a separate message before the question.

## Parse & render
Post-process before display: resolve source IDs in your DB, replace markers with links/footnotes/inline chips; parser handles single-source, multi-source and optional locator (`^L\d+(?:-L\d+)?$`); source ids `^[A-Za-z0-9_-]+$`; regex = START `cite` DELIM (.*?) STOP (DOTALL), split on DELIM, last part = locator if it matches, drop the marker when parts are empty/invalid; return clean text + `{source_ids, locator, start, end}`. (Python `extract_citations`, JS `extractCitations` in the page; JS escape helper `escapeRegExp`.)

## Production checklist
Store per retrieved block: `source_id`, title, URL/file id, chunk text, optional line range; validate cited ids, multi-source markers and locators against the blocks given in that request; reject/repair malformed citations before rendering — never show raw `…` to end users; strip/render markers before returning content; log final answer text, selected source ids and rendered locators for audit; citation = grounding evidence, NOT access control — tenant/permission checks belong in retrieval.
Related: api-reference/responses, tools-web-search (captured), tools-file-search (captured; hosted not available), retrieval (captured), examples/manual_rag_with_embeddings (not captured).
