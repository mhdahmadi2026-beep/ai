# NVIDIA NIM (research-grade, ids `nvidia_nim.*`)

**Research/eval only, not production.** ~1/10 of prod prices. Rate limits (RPM): base 3, T1 5, T2 10, T3 15, T4 20, T5 30. For production use Groq/Fireworks/etc.

- Embeddings (`/v1/embeddings`, $0.002/1M): llama-based 300M–1B, `nvidia_nim.nv-embed-v1`, `bge-m3`.
- Rerank (`/v1/rerank`, $0.0002/query): `llama-3.2-nemoretriever-500m-rerank-v2`, `llama-3.2-nv-rerankqa-1b-v2`, `nv-rerankqa-mistral-4b-v3` (prefix `nvidia_nim.`).
- Chat: nemotron-parse ($0.01/$0.06), nvidia-nemotron-nano-9b-v2 ($0.004/$0.016), eurollm-9b-instruct ($0.022/$0.022), gemma-3-1b-it ($0.001/$0.005), gpt-oss-20b/120b, qwen3-next-80b-a3b-thinking, llama-4-scout-17b-16e-instruct ($0.027/$0.085), llama-3.1-nemotron-ultra-253b-v1, llama-3.3-nemotron-super-49b-v1.5.
- Vision: `nvidia_nim.nemotron-nano-12b-v2-vl` (base64 data URL image_url).
- Production NVIDIA: `nemotron-3-ultra` (via Fireworks.ai): $0.60 in / $0.12 cached / $2.40 out; chat ✅, responses partial.
- Many NIM ids probably deprecated — check 10-deprecations.md.
- Defects: typos "صطح"; "Chat Completions" link points to messages.md.
