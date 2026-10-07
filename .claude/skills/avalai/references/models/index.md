# Models catalog page (docs: /fa/models/index) — "پیدا کردن مدل مناسب"

Page type: catalog (`pageType: catalog`, section `models`). Its body is an interactive `<ModelExplorer />` Vue-style component — **the model list, prices, context windows, capabilities and benchmark comparisons are rendered dynamically and are NOT present in the pasted text**. To get that data use live sources instead of guessing:
- `GET https://api.avalai.ir/public/models` (no auth) or `GET /v1/models/{id}` (`extra.{metadata,pricing,rate_limits}`) — see api-reference/models.md.
- `06-pricing.md` (price catalog snapshot) and per-model pages `/fa/models/<id>` / `/fa/models/model-details` (still PENDING).

Static guidance on the page (model selection):
- First check **access, input/output modality, and endpoint compatibility** (chat vs responses vs messages vs v1beta; many models are PARTIAL on Responses).
- Compare AvalAI **price and context window** for your workload.
- Treat external benchmarks as comparative evidence, not a universal score.
- Provider filter available in the explorer; provider docs e.g. fa/providers/openai.
