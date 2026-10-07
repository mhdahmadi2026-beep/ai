# Alibaba (Qwen) provider page (docs: /fa/providers/alibaba)

AvalAI serves the Qwen family through Alibaba's DashScope cloud. All models support `/v1/chat/completions`; `/v1/messages` and `/v1/responses` support is per-model. **Cross-check every id against 10-deprecations.md ("Alibaba Qwen legacy snapshots retired 13–31 May 2026") and live `/v1/models`** — this page still lists some retired ids (flagged ⛔ below).

## ⚠ `enable_thinking` rule (important)
- **Non-streaming** requests (`stream=False`) to most Qwen models must send `extra_body={"enable_thinking": False}` or DashScope may error.
- Thinking (`enable_thinking: True`) works **only with `stream=True`**; setting it without streaming → `invalid_request`.
- Qwen3.8 / 3.7 (and flash/27B) docs show `enable_thinking: True` + `reasoning_effort` (`low|medium|xhigh`) in `extra_body` for non-stream examples — treat per-model (Qwen3.8 examples omit the stream requirement); when in doubt, stream or send `enable_thinking: False`.
- `preserve_thinking` keeps reasoning across turns on agentic multi-turn flows (where supported).
```python
client.chat.completions.create(model="qwen3-8b", messages=[…], stream=False, extra_body={"enable_thinking": False})
client.chat.completions.create(model="qwen3-8b", messages=[…], stream=True,  extra_body={"enable_thinking": True})
```

## Qwen3.8 series (newest)
| model | ctx | in / cache-write / cached / out ($/1M) | inputs | thinking | endpoints |
|---|---|---|---|---|---|
| `qwen3.8-max` (flagship MoE 2.4T; long-horizon coding, pro work, multimodal, agentic; tools, structured output, prompt cache, web search, streaming) | 1,000,000 (≤991,000 input), out ≤128,000 | 2.00 / 2.50 / 0.25 / 6.00 | text, image, video | hybrid via `enable_thinking` (obey streaming rule) | chat full, messages full, responses **partial** |
| `qwen3.8-2.4t-a95b` (open-weight base of max; 2.4T total/95B active; **text-only, thinking mandatory**) | 262,144 | 2.00 / 2.50 / 0.25 / 6.00 | text | always on; `reasoning_effort` `low|medium|xhigh` (default `xhigh`); answer starts with `<think>…</think>`; `preserve_thinking` | chat, messages full; responses partial |
| `qwen3.8-flash` (alias of `qwen3.8-flash-next`; 125B MoE/6B active; hybrid Gated DeltaNet + sparse attention QSA; cheapest 3.8) | 262,144 | 0.15 / 0.20 / 0.016 / 0.47 | text, image, video | default on; `enable_thinking` per request; `reasoning_effort` low/medium/xhigh | chat, messages full; responses partial |
| `qwen3.8-27b` (compact dense VL) | 262,144 | 0.50 / 0.625 / 0.10 / 2.00 | text, image, video | default on | chat, messages full; responses partial |
Provider-reported benchmarks (not guarantees): flash — Toolathlon Verified 73.5, CoWorkBench 73.9, GPQA Diamond 91.7; 27B — Terminal Bench 2.1 73.0, SWE-bench Pro 61.7, OSWorld-Verified 84.3. News: fa/news/2026-08-03-qwen3-8-max-deepseek-v4-flash-upgrade, fa/news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added.
```python
client.chat.completions.create(model="qwen3.8-flash", messages=[…], extra_body={"enable_thinking": True, "reasoning_effort": "medium"})
client.chat.completions.create(model="qwen3.8-2.4t-a95b", messages=[…], extra_body={"reasoning_effort": "medium"})
client.chat.completions.create(model="qwen3.8-max", messages=[…], extra_body={"enable_thinking": False})
```

## Qwen3.7
- `qwen3.7-max` (prev flagship; agent foundation): ctx 1,000,000, out 65,536; in 2.50 / cache-write 3.125 / cached 0.25 / out 7.50; text+image+video; chat + responses(partial). Reported: SWE-Verified 80.4, SWE-Pro 60.6, Terminal-Bench 2.0 69.7, GPQA 92.4, HMMT 97.1, MCP-Atlas 76.4… Long-run demo: 35 h kernel optimization, 1,158 tool calls. Streaming-only thinking; `preserve_thinking` for multi-turn agents. Verify live price (`GET /v1/models/qwen3.7-max`).
- `qwen3.7-plus`: ctx up to 1,000,000, out 65,536; in 0.40 / 0.50 / 0.04 / out 1.60; chat only.

## Qwen3.6
- `qwen3.6-plus`: 1M ctx; in 0.50 (>256K: 2.00), cache-write 0.625 (2.50), cached 0.05 (0.20), out 3.00 (6.00); text+image in; chat. SWE-bench Verified 78.8, Terminal-Bench 2.0 61.6, MCPMark 48.2…
- `qwen3.6-flash`: 1M ctx (256K tier), max out 64K; in 0.25 (>256K 1.00), cache-write 0.3125 (1.25), cached 0.025 (0.10), out 1.50 (>128K 4.00); text/image/video; chat. Replacement for retired `qwen-turbo`.
- `qwen3.6-27b`: 256K ctx; in 0.60, cached 0.06, out 3.60; VL; chat.
- `qwen3.6-35b-a3b`: 256K; in 0.248, cached 0.025, out 1.485; sparse MoE VL; chat.
- `qwen3.6-max-preview`: text-only, 256K (128K price tier), out 64K; in 1.30 (>128K 2.00), cache-write 1.625 (2.50), cached 0.13 (0.20), out 7.80 (12.00); chat.

## Older text series
- **Flash**: `qwen-flash`, `qwen-flash-2025-07-28` — 131,072 ctx, in ≤129,024, out ≤16,384, tiered price. (`qwen-turbo*` ⛔ retired May 2026 → `qwen-flash`/`qwen3.6-flash`.)
- **Plus**: `qwen-plus`, `-latest`, `-2025-09-11`, `-2025-07-28`, `-2025-07-14`, `-2025-04-28` — 131,072 ctx, out 16,384.
- **Qwen3 Max**: `qwen3-max` (flagship agentic coding; added 2026-06-05, see fa/news/2026-06-05-gemini-image-stable-and-qwen3-max-added), `qwen3-max-2026-01-23`, `qwen3-max-preview` (1T+); 262,144 ctx, in ≤258,048, out ≤32,768. (`qwen-max*` ⛔ retired → `qwen3.7-max`/`qwen3-max`/`qwen3.6-plus`/`qwen3.6-max-preview`.)
- **Qwen3.5**: `qwen3.5-plus` (1M ctx, out 32,768), `qwen3.5-plus-2026-02-15`, `qwen3.5-flash` (1M, out 16,384), open-weight `qwen3.5-397b-a17b` (131,072; 397B/17B active), `qwen3.5-35b-a3b` (131,072; 35B/3B active); hybrid Gated DeltaNet + sparse MoE; native VL (text/image/video); 201 languages; Apache 2.0 for open-weights. Prices ($/1M in / in>256K / cache-write / >256K / cached / >256K / out / >256K): plus 0.40/1.20/0.50/1.50/0.04/0.12/2.40/7.20; flash 0.10/0.30/0.125/0.375/0.01/0.03/0.40/1.20; 397b 0.60 in, 0.06 cached, 3.60 out; 35b-a3b 0.25 in, 0.12 cached, 2.00 out.
- **Qwen3 standard**: `qwen3-32b` (out 16,384), `qwen3-14b`, `qwen3-8b`, `qwen3-4b`, `qwen3-1.7b`, `qwen3-0.6b` (131,072 ctx, in 98,304; 1.7b/0.6b/4b ⛔ retired per deprecations). **A3B**: `qwen3-next-80b-a3b-thinking|instruct`, `qwen3-30b-a3b`, `-thinking-2507`, `-instruct-2507` (out 32,768). **A22B**: `qwen3-235b-a22b`, `-instruct-2507`, `-thinking-2507` (131,072 in; `qwen3-235b-a22b-thinking-250…` listed removed; NIM `qwen3-next-80b-a3b-thinking` removed).
- **QwQ**: `qwq-plus`, `qwq-plus-2025-03-05` (131,072; out 8,192; `qwq-32b` removed).
- **Long context**: `qwen2.5-7b-instruct-1m`, `qwen2.5-14b-instruct-1m` (1,008,192 ctx; ⛔ retired May 2026).
- **Coders**: `qwen3-coder-480b-a35b-instruct` (262,144, out 65,536), `qwen3-coder-next` (80B MoE/10B active, 1M ctx, in ≤997,952, out 65,536; **$0.30 in / $0.15 cached / $1.50 out**; agentic coding), `qwen3-coder-flash` + `-2025-07-28` (1M, tiered), `qwen3-coder-plus` + `-2025-07-22` (1M).
- **Translation `qwen-mt-*`** (92 languages incl. Persian/Dari, direct non-Chinese pairs; system message carries direction): `qwen-mt-plus`, `qwen-mt-turbo` (2,048 ctx), `qwen-mt-flash`, `qwen-mt-lite` (8,192).
- **Character/role-play**: `qwen-plus-character` (131,072; persona consistency, relationship memory).

## Vision-language
- Qwen3-VL: `qwen3-vl-32b-instruct` (131,072; out 8,192), `qwen3-vl-plus`, `qwen3-vl-flash` (131,072+; tiered pricing; very long docs, video ≤1 h, OCR, agent features).
- Qwen2.5-VL: `qwen2.5-vl-72b|32b|7b|3b-instruct` (131,072; ⛔ retired per deprecations list).
- `qwen-vl-ocr` (34,096 ctx? page shows 34,096; in ≤30,000, out 4,096). `qwen-vl-max/plus` ⛔ retired → `qwen3-vl-plus/flash`.

## Web search (`qwen3-max` only)
Since Dec 2025 only `qwen3-max` and `qwen3-max-2025-09-23` support it. `extra_body={"enable_search": True, "search_options": {"search_strategy": "agent"}}` (strategy must be `agent` for international regions). Model decides whether to search. Billing = normal model tokens (search results inflate input) **+ $10.00 per 1,000 search-policy calls**. (JS example puts `enable_search` at top-level — with the OpenAI JS SDK extra fields pass through the body; Python uses `extra_body`.)

## Image models (`/v1/images/*`, see images.md)
| model | $/image | notes |
|---|---|---|
| `qwen-image-3.0-pro`, `qwen-image-3.0` | $0.04 (~1 MP) / $0.075 (2–4 MP) / $0.003 per reference image; accounting rate $40/1M output tokens | generations + edits |
| `qwen-image-2.0-pro` | $0.06 | typography, near-zero text error in 40+ langs, native 2K |
| `qwen-image-2.0` | $0.04 | photorealism, 2K, gen+edit |
| `qwen-image` | $0.035 | 1:1, 4:3, 3:4, 16:9, 9:16 (1328×1328, 1664×928, 1472×1140, 1140×1472, 928×1664) |
| `qwen-image-edit` | $0.045 | edits |
| `qwen-image-edit-plus` | $0.03 | bg removal, inpainting, style transfer, recolor, structure control |
| `z-image-turbo` | $0.015 std / $0.030 thinking | fast, 512×512–2048×2048, 42 preset ratios |
Both OpenAI format and Dashscope-native (`input.messages`, `parameters{size:"1328*1328", prompt_extend, watermark, negative_prompt, seed}`) are accepted.

## Embeddings (see embeddings.md)
- `text-embedding-v4`: 64–2,048 dims (2048/1536/**1024 default**/768/512/256/128/64), **$0.07/1M**; `extra_body={"text_type":"query"|"document","instruct":"…English task instruction"}`; dense+sparse; ≤10 texts/request; (page table says 8,192 tokens; embeddings page says 1024 — verify).
- `text-embedding-v3`: 512–1,024 (1024 default/768/512), $0.07/1M, 50+ languages, ≤10 texts.
- `tongyi-embedding-vision-plus` (1,152 dims, $0.09/1M) and `tongyi-embedding-vision-flash` (768 dims; image/video $0.03, text $0.09): multimodal, same semantic space, ≤8 images/request, video ≤10 MB (MP4/MPEG/AVI/MOV/MPG/WEBM/FLV/MKV), images JPG/PNG/BMP (base64/URL). Native input shape via `extra_body={"input":{"contents":[{"text":…},{"image":url}]}}` (set SDK `input="placeholder"`) or raw HTTP.
Best practice: 1024 dims default; higher (1536/2048) for precision; lower for cost; query vs document `text_type`; batch ≤10.

## Rerank (see rerank.md)
`qwen3-rerank`: ≤500 docs, ≤4,000 tokens/doc, ≤30,000 tokens/request, 100+ languages, **$0.10/1M input, cached $0.0035/1M**; response includes `model`, `results[]`, `usage.total_tokens`.

## Endpoints & practice
Chat Completions full (tools, streaming, system, temperature, multimodal); Messages limited for most (Qwen3.8 flagship family full); Responses per-model/partial. Choose: Flash (high volume), Plus (balanced), Qwen3.x Max (complex/agentic), VL (images), Coder (code). Manage context windows; use dated versions for reproducibility. Pricing/limits: fa/models/model-details; DashScope console https://dashscope.console.aliyun.com/.

## Source anomalies
- Lists retired ids (qwen-max/turbo/vl-max/vl-plus note, plus qwen2.5-vl, qwen3-0.6b/1.7b/4b, qwen2.5-*-1m) as available in tables though banners say retired; trust deprecations + live list.
- `qwen-vl-ocr` context 34,096 as printed.
- Responses-equivalent blocks wrongly replace Qwen with `gpt-5.6-luna` (copy artifacts) — ignore.

## Audit addendum — extra ids and flags from the source page
- Qwen-Plus snapshots: `qwen-plus`, `qwen-plus-latest`, `qwen-plus-2025-09-11`, `-2025-07-28`, `-2025-07-14`, `-2025-04-28`; `qwen3-coder-plus` (1M ctx, 997,952 in, 65,536 out) and `qwen3-coder-plus-2025-07-22`.
- Vision: `qwen2.5-vl-{72b,32b,7b,3b}-instruct` — each 131,072 ctx, 129,024 in, 8,192 out. `qwq*`/`qvq-max*` legacy → see 10b-deprecations-complete.md.
- Legacy `qwen-turbo*` (turbo, -latest, -2025-04-28) retired 13–31 May 2026 → `qwen-flash` / `qwen3.6-flash`.
- Web search: `extra_body={"enable_search": true}` (+ `search_options.search_strategy` must be `"agent"` for international regions); model decides whether to search.
- Embeddings (`text-embedding-v4` only): `text_type: "query"` for user queries, `"document"` for stored docs.
- `reasoning_effort` ∈ `low|medium|xhigh` (default `xhigh`) on Qwen3.8 2.4T; answer begins with `<think>…</think>`.
