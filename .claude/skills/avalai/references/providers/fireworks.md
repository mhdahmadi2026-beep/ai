# Fireworks.ai hosted models
All three: chat ✅ full, `/v1/messages` ✅ full, `/v1/responses` ⚠️ partial (stateful/some fields missing; test before prod). Implicit provider caching.
| id | owner | ctx | in | cached | out | notes |
|---|---|---|---|---|---|---|
| muse-glimmer-30b | Meta | ≥131,072 | 0.35 | 0.04 | 1.50 | dense 30B, image+text in, 100+ langs, reasoning `low|medium|high|xhigh`, suggested temp 1.0 top_p 0.95 top_k 64 |
| nemotron-3.5-lightning | NVIDIA | 262,144 | 0.05 | 0.01 | 0.20 | hybrid MoE 30B/3B active (Mamba-2), thinking toggle, structured output, temp 1.0 top_p 0.95 |
| nemotron-3-ultra | NVIDIA | n/a | 0.60 | 0.12 | 2.40 | large reasoning/agentic |
Not documented: exact param name for reasoning level and thinking toggle — verify.
