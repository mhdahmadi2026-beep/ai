# معرفی / Introduction — https://docs.avalai.ir/fa/

**توسعه هوش مصنوعی با AvalAI.** Start with a real request, then follow the docs path matching your product. AvalAI works with OpenAI-compatible clients through one base URL.
Official-name note: users may search «اول ai», «اول ای آی», «هوش مصنوعی اول»; docs always write **AvalAI**.

## First request (Responses API)
1. **Create an API key** — open the AvalAI dashboard (https://chat.avalai.ir/platform/home), create a project key, keep it server-side only.
2. **Install a client** — OpenAI-compatible SDK for Python or JavaScript, or plain cURL.
3. **Run a Responses request** — set `AVALAI_API_KEY`, run the example, read `response.output_text`.

```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-6-astra",
    input="Give me one practical idea for a developer tool.",
)

print(response.output_text)
```
(Tabs on the page: Python, JavaScript, Bash — only Python was captured; JS/Bash PENDING.)

## Task paths
| Need | Page |
|---|---|
| متن و استدلال — stateful responses, structured output, reasoning workflows | /api-reference/responses |
| تصویر و بینایی — generate/edit/analyze images | /api-reference/images |
| صوت و گفتار — transcription and speech output | /api-reference/audio |
| ابزارها و بازیابی — connect models to functions, files, search, app data | /guides/tools |

## Models & cost
Compare documented capabilities first, then check current input/output prices. Latest announcements listed on the intro page (newest first):

| Date | Announcement | Model IDs / key facts | Link |
|---|---|---|---|
| 2026-09-30 | Gemini 3.8 Flash & Flash-Lite TTS | Flash: creative narration, accents, long-speech stability; Lite: high-volume voice-agent pipelines & read-aloud. Both support Persian. Promo token rate until 10 Dey 1405 (2026-12-31). See structured-request notes & audio template migration. | /news/2026-09-30-gemini-3-8-tts-models-added |
| 2026-09-30 | GPT-6.1 Sol & Claude Sonnet 5.5 | `gpt-6.1-sol`, `claude-sonnet-5-5` from tier 1; coding & document workflows. Both fully support Chat Completions and Messages; Responses full for Sol, partial for Sonnet. Standard rate per 1M tokens: input $2, output $10. Compare cache pricing and Sonnet thinking migration. | /news/2026-09-30-gpt-6-1-sol-claude-sonnet-5-5-added |
| 2026-09-24 | Claude Opus 5.5 (new Anthropic flagship) | `claude-opus-5-5`; long-running coding & knowledge work, always-on adaptive thinking, 1M-token input window; full Chat Completions, Messages, Responses; from tier 1; per 1M tokens: input $4, output $20. | /news/2026-09-24-claude-opus-5-5-added |
| 2026-09-24 | GPT-6 Sol, GPT-6 Luna, Grok 4.7 | `gpt-6-sol`, `gpt-6-luna` (OpenAI, low-cost reasoning), `grok-4.7` (xAI, long-running coding/knowledge work). All support Chat Completions & Messages; Responses full for Sol/Luna, partial for Grok. | /news/2026-09-24-gpt-6-sol-luna-grok-4-7-added |
| 2026-09-11 | GPT Image 2.5, DeepSeek V4.1 Flash, Grok 4.6 | Image gen/edit via Flare or Sunburst; reasoning agents with DeepSeek V4.1 Flash / Grok 4.6. DeepSeek off-peak rate is 24/7; migrate before V4-Pro routing change on 23 Shahrivar (2026-09-14). | /news/2026-09-11-gpt-image-2-5-deepseek-v4-1-grok-4-6-added |
| 2026-09-05 | GPT-6 Astra (new OpenAI flagship) | `gpt-6-astra`; hard computer tasks, software engineering, professional/science/cyber, long context; full Chat Completions, Messages, Responses. | /news/2026-09-05-gpt-6-astra-added |
| 2026-09-03 | Gemini 3.8 Flash | Long-running coding agents & tool workflows; promo rate until 10 Dey 1405 (Dec 31, 2026). Alias `gemini-flash-latest` now points to it. | /news/2026-09-03-gemini-3-8-flash-added |
| 2026-09-02 | Claude Fable 5.1 (new Anthropic flagship) | `claude-fable-5-1`; advanced coding, research, knowledge work, long agents; 1M input window, always-on adaptive thinking, cheaper cache reads. | /news/2026-09-02-claude-fable-5-1-added |
| 2026-08-29 | Alibaba Qwen3.8-27B & Qwen3.8-Flash | `qwen3.8-flash` (low-cost vision/agents), `qwen3.8-27b` (dense compact vision-language reasoning, flexible thinking control). | /news/2026-08-29-qwen3-8-27b-and-qwen3-8-flash-added |
| 2026-08-26 | Z.AI GLM-5.3-Flash | `glm-5.3-flash`; multimodal coding/agents; 320B total / 18B active params; 991K input window; promo price until 18 Shahrivar 1405. | /news/2026-08-26-glm-5-3-flash-added |
| 2026-08-18 | Z.AI GLM-5.3 | Complex coding workflows & long agents; mandatory thinking, selectable reasoning level, 1M-token context. | /news/2026-08-18-glm-5-3-added |
| 2026-08-15 | Alibaba open-weight Qwen3.8 & Qwen Image 3 | `qwen3.8-2.4t-a95b` (text, mandatory thinking); `qwen-image-3.0-pro`, `qwen-image-3.0` (image gen/edit). | /news/2026-08-15-qwen3-8-open-weight-and-qwen-image-3-added |
| — | Muse Glimmer 30B | Meta multimodal agentic model on Fireworks.ai: reasoning, tools, coding, multilingual. | /models/muse-glimmer-30b |
| — | Nemotron 3.5 Lightning | NVIDIA, 30B total / 3B active; reasoning, coding, RAG, agents. | /models/nemotron-3.5-lightning |
| — | Cache routing improvement | Per-user-and-model routing now prefers the last successful infrastructure within a sticky rolling 15-minute window. | /guides/prompt-caching |

Also: model browser (family, input/output type, context length, supported endpoints) → /models/index; pricing check → /pricing.

## Popular guides
| Guide | Purpose | URL |
|---|---|---|
| Structured output | Constrain response to a schema the app can validate | /guides/structured-outputs |
| Function calling | Let model request tools; execution controlled in your code | /guides/function-calling |
| Streaming | Show useful output as response events arrive | /guides/streaming-responses |
| Production readiness | Plan security, reliability, latency, cost up front | /guides/production-best-practices |

## Support & status
- Create ticket (send request details & error context): https://chat.avalai.ir/platform/support/create-ticket
- Service status & recent incidents: https://status.avalai.ir/
- Debug help: paste doc page links into AvalAI chat (https://chat.avalai.ir/chat) and ask the model.

## Page navigation
Previous: آخرین تغییرات (/news/) · Next: شروع سریع (/quickstart)
On-page anchors: first-request, task-paths, models-pricing, popular-guides, support-status.
