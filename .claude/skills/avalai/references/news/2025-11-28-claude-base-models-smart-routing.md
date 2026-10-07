# News 2025-11-28 (1404-09-07): Claude base ids + smart routing (docs.avalai.ir/fa/news/2025-11-28-claude-base-models-smart-routing)

Base ids (`claude-opus-4-5`, `claude-sonnet-4-5`, `claude-opus-4-1`, `claude-haiku-4-5`; later `claude-opus-4-6/4-7/4-8`, `claude-opus-5…`) auto-route across Anthropic, AWS Bedrock, GCP Vertex, Azure → much higher rate limits + failover; pricing = Bedrock pricing; migrate by changing only `model`. Full Bedrock ids (`anthropic.claude-opus-4-5-20251101-v1:0` …) still work but have lower limits.
- T1 (Nov 2025 snapshot) RPM/TPM: base opus-4-5 10/30K (Bedrock id 1/40K), sonnet-4-5 25/30K (2/200K), opus-4-1 5/30K, haiku-4-5 25/50K. T5: 1,500 RPM; 4M TPM (haiku 8M). Current numbers → 11-tier-rate-limits.md.
- Works via `/v1/chat/completions` and `/v1/messages` (Anthropic SDK base_url `https://api.avalai.ir`, no /v1).
- Historic prices: opus-4-5 $5/$25, sonnet-4-5 $3/$15, opus-4-1 $15/$75, haiku-4-5 $1/$5 (cached figures on the page look off; use 06-pricing.md).
