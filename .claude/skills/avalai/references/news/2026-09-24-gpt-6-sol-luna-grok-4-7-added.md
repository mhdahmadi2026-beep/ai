# News 2026-09-24 (1405-07-02): GPT-6 Sol, GPT-6 Luna, Grok 4.7 added (docs.avalai.ir/fa/news/2026-09-24-gpt-6-sol-luna-grok-4-7-added)

Rows also in `../providers/openai.md`, `../providers/xai.md`, `../06-pricing.md`.

| id | chat | messages | responses | limits |
|---|---|---|---|---|
| `gpt-6-sol` | full | full | full | 922K in / 128K out |
| `gpt-6-luna` | full | full | full | 922K in / 128K out |
| `grok-4.7` | full | full | **partial** | 500K in / 500K out (separate caps, not simultaneous) |

- Sol: budget coding agents, professional analysis, computer use, long chats. Luna: cheaper, high-traffic assistants, document processing, tool workflows. `gpt-6-astra` stays the strongest GPT-6; nothing auto-replaced. Both: text+image in, text out, reasoning, function calling, structured output, PDF, prompt cache. OpenAI-side cache improvements (stable reuse across effort/tool changes, explicit cache breakpoints) are NOT confirmed on all AvalAI routes — keep prefixes stable, measure.
- Price/1M (≤272K / >272K, threshold on input length; higher tier applies to the whole request):
  - sol: in 2.00/4.00, cached 0.20/0.40, cache-create 2.50/5.00, out 10.00/15.00
  - luna: in 0.10/0.20, cached 0.01/0.02, cache-create 0.125/0.25, out 0.50/0.75
  - grok-4.7 (≤200K / >200K): in 2.00/4.00, cached 0.50/1.00, out 6.00/12.50 (same as Grok 4.6; long-context tier, not the provider's fast variant).
- Grok 4.7: long-horizon coding agents, verification, docs/slides; start WITHOUT `reasoning_effort` (allowed/default values not defined by AvalAI); xAI fast variant and invite-only security features are NOT AvalAI routes. Start with Chat Completions; Responses partial → test tool round-trips, output format, continuation before migrating.
- These are vision-input models, NOT image generators: don't use in `/v1/images/*`; use `gpt-image-2.5-flare`/`gpt-image-2.5-sunburst` etc. Hosted `image_generation` tool in Responses is a separate capability to verify per model/route/account.
- Example response is illustrative: 100 in/50 out Sol = $0.0007 (70 toman @100,000). Include room for hidden reasoning tokens in output budget.
