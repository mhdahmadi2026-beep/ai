# News 2026-09-11 (1405-06-20): GPT Image 2.5, DeepSeek V4.1 Flash, Grok 4.6 (docs.avalai.ir/fa/news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added)

| id | endpoints |
|---|---|
| `gpt-image-2.5-flare`, `gpt-image-2.5-sunburst` | `/v1/images/generations`, `/v1/images/edits` ONLY (not chat/responses) |
| `deepseek-v4.1-flash` | chat, messages, responses (partial) |
| `grok-4.6` | chat, messages, responses (partial) |

- Flare = default general/fast/product/high-volume (OpenAI claims up to 50% lower latency vs GPT Image 2; unverified on AvalAI). Sunburst = detailed creative + pro editing. Both: better lighting/textures/reference-subject retention/successive edits (feed previous output back as input). ChatGPT-only features (Sketch, templates) not in API.
- DeepSeek V4.1 Flash: native image understanding, thinking/non-thinking, tools, JSON output, prompt cache; 552B MoE (8B active input / 16B output); catalog 1,000,000 in / 393,216 out (DeepSeek says 384K). Price (ALL hours, fixed off-peak): in $0.15, cached $0.003, out $0.60 per 1M.
- Grok 4.6: long-running agents, large-repo engineering; vision, reasoning, tools, structured output, cache; 500K in / 500K out (don't assume Grok 4.5's 1M). Price ≤200K: 2.00 / cached 0.50 / out 6.00; >200K: 4.00 / 1.00 / 12.50 (long-context tier, not a "fast" variant).
- GPT Image 2.5 token price/1M: text in 5.00 (cached 1.25), image in 8.00 (cached 2.00), text out 0.00, image out 30.00. Per 1024×1024 output image estimate (same for both models): low $0.00588, medium $0.01317, high $0.05268, xhigh $0.09366, max $0.21072 — OUTPUT only; prompt + reference-image tokens are extra; text-out 0 ≠ free. Quality values include `xhigh`, `max`.
- **DeepSeek V4-Pro rerouting: from 2026-09-14 04:00 UTC (1405-06-23) `deepseek-v4-pro` → `deepseek-v4.1-flash`, billed at V4.1 Flash rates** (already in effect as of 2026-10-07). Keeping the old id does NOT keep the old model. DeepSeek itself retires V4-Flash and V4-Flash-Vision-Exp (no extra AvalAI rerouting announced for those). New integrations: use `deepseek-v4.1-flash` directly.
- Example: `/v1/images/generations` body `{model,prompt,size:"1024x1024",quality:"medium",n:1}` → `data[].b64_json` + `usage{input_tokens,input_tokens_details,output_tokens}` + `estimated_cost`. Edits: multipart `-F model -F image=@file -F prompt -F size -F quality -F n` (let curl set boundary).
- Source-page notes: sample cost combines $0.01317 image out + $0.00010 text in (not a guaranteed price); base64 truncated.
