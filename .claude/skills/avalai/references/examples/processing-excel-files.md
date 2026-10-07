# Example: processing Excel/spreadsheet files (slug probably /examples/processing_excel_files — unconfirmed)

Related: guides/pdf-files.md (spreadsheets = structured data), guides/rag-best-practices.md, examples/manual-rag-with-embeddings.md, guides/tools-code-interpreter.md.

## Approaches on the page
1. **Simple workflow** — (a) send xlsx as base64 `file` part on Chat Completions (`data:application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;base64,…`); (b) convert to text yourself (`pd.read_excel(...).to_string()`, SheetJS `sheet_to_json` → TSV, excelize, PhpSpreadsheet) and put it in the prompt. Small sheets only (must fit context).
2. **LangChain agents** — `create_csv_agent(llm, "file.xlsx", agent_type="openai-tools")`, `create_pandas_dataframe_agent(llm, df, agent_type="tool-calling", allow_dangerous_code=True)`; `ChatOpenAI(model=…, temperature=0)` with `OPENAI_BASE_URL=https://api.avalai.ir/v1`.
Models listed: gpt-5.5/5.4/5.4-mini; claude-opus-4-7/sonnet-4-6/haiku-4-5; gemini-3.1-pro-preview, 3.5-flash, 2.5-pro/flash. Claimed limits (unverified): OpenAI 25 MB, Claude 32 MB, Gemini 20 MB; ~1–3 tokens/cell.

## Recommended handling (my rule set)
- Prefer **(b) app-side conversion**: parse with pandas/openpyxl, drop unused columns/rows, keep header + types, send compact CSV/markdown or aggregates; process sheet by sheet; for large data compute stats in code and send only results (or retrieval/RAG). Don't rely on raw xlsx as a `file` part — support is route/model-dependent (guides/pdf-files.md: non-PDF docs = text only; spreadsheets should be extracted by your app).
- For math/aggregation/joins don't let the LLM "calculate" from pasted tables: run pandas yourself (or hosted code_interpreter only if the route supports it — usually app-managed instead) and have the model explain results; verify numbers.
- Dynamic code execution (pandas agent): executes LLM-written Python → only in sandbox/container with no secrets/network, never on untrusted files (spreadsheet content is prompt-injection input; formulas/cells can carry instructions). Keep `allow_dangerous_code` off unless isolated.
- Structured answers: JSON schema output; ask for cell/row references; cap tokens; log `usage`.
- Specify column meaning; mention sheet name; ISO dates; avoid `df.to_string()` for big frames (padding wastes tokens → `to_csv(index=False)`).
- Drop `temperature=0` on reasoning/Claude 5.x models.

## Defects of the source page
- `create_csv_agent` reads **CSV only** (`pd.read_csv`) — passing `.xlsx` fails; use `create_pandas_dataframe_agent` with `pd.read_excel`. LangChain.js has no `createCSVAgent`/`createPandasDataFrameAgent` exports (fictional) and `agentType:"openai-tools"` ≠ JS API.
- `ChatOpenAI` reads `OPENAI_API_KEY`, not `AVALAI_API_KEY` → set `api_key=os.environ["AVALAI_API_KEY"], base_url=…` explicitly (`OPENAI_BASE_URL` alone is not enough).
- `langchain_experimental` agents are unmaintained/dangerous by design (arbitrary code exec); the page admits `allow_dangerous_code=True`.
- Only the first sheet is read in all samples; `sheet_to_json` + `Object.keys(jsonData[0])` crashes on empty sheet; PHP `for ($col='A'; $col <= $highestColumn; $col++)` breaks beyond column Z (string comparison); Go sample has lowercase `model:` field (compile error) and non-existent `openai.ChatMessageContent/File` types; PHP `OpenAI::client(key,['base_url'])` is wrong (use `OpenAI::factory()->withBaseUri()`).
- Responses-equivalent blocks are generic ("Summarize the uploaded file", no file) — useless; `claude-sonnet-4-6`/`gemini-2.5-pro` via Chat Completions flagged "may not be on /v1/responses".
- Base64 xlsx sample uses `gpt-5.6-luna` while model list says gpt-5.5/5.4 — inconsistent; `claude-*` agent examples route Gemini through `ChatOpenAI` (works only via gateway).
- Visual claims ("analyses charts in spreadsheets") unsupported: charts inside xlsx are not rendered to the model.
- Privacy: financial/inventory data leaves your system → guides/data-controls.md.
