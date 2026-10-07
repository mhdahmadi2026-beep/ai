# Meta (Llama) provider page (docs: /fa/providers/meta)

Llama via partners (AWS Bedrock, Vertex AI, Together AI). Use the integration-specific model id. ⚠ Many Llama/NIM ids were removed (10-deprecations.md: `llama-4-scout-17b-16e-instruct`, `llama-3.1-nemotron-ultra-253b-v1`, etc.) — verify via `/v1/models`.

## Llama 3.1 (Bedrock)
| model id (Bedrock) | ctx in / out | cutoff | in | out | use |
|---|---|---|---|---|---|
| `meta.llama3-1-405b-instruct-v1:0` | 128K / 4,096 | Mar 2024 | ~5.32 | ~16.00 | hardest tasks, research |
| `meta.llama3-1-70b-instruct-v1:0` | 128K / 2,048 | Mar 2024 | ~0.99 | ~0.99 | complex chat, content, RAG |
| `meta.llama3-1-8b-instruct-v1:0` | 128K / 2,048 | Mar 2024 | ~0.22 | ~0.22 | simple chat, summarization, classification |
## Llama 3.2 (preview)
`llama-3.2-90b-vision-instruct` (128K/2,048; text+image; price per provider e.g. Vertex). Page's example snippet uses `llama-4-scout-17b-16e-instruct` for the vision demo — id likely removed.
## Llama 4 Scout (preview via Together AI)
`llama-4-scout-17b-128e-instruct-fp8` (example id `together_ai/meta-llama/llama-4-scout-17b-128e-instruct-fp8`) and `llama-4-scout-17b-16e-instruct` (`together_ai/meta-llama/llama-4-scout-17b-16e-instruct`): 50 RPM, 400K TPM; experimental; price via AvalAI.
## Older
Llama 3 (8B/70B), Llama 2 (7B/13B/70B) via various providers — cheaper, smaller context.
Usage: `client.chat.completions.create(model="meta.llama3-1-70b-instruct-v1:0", …)`; id depends on provider.
