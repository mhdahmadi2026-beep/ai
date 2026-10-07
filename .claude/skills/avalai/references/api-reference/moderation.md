# Moderation API — `POST https://api.avalai.ir/v1/moderations` (docs: /fa/api-reference/moderation)

Detect potentially harmful user input or model output (text; images with `omni-moderation-latest`; **no audio**). Treat as a policy *signal* (filter, review queue, account action, human escalation), not a complete safety system.

## Workflows
| workflow | when | how |
|---|---|---|
| standalone classification | policy signal for text/image without generating | `POST /v1/moderations` |
| generated-output moderation | scores for both request and generated reply | `moderation: {"model":"omni-moderation-latest"}` on supported `/v1/responses` or `/v1/chat/completions` routes; otherwise call `/v1/moderations` before and/or after generation |
| review/escalation | durable audit trail | store `flagged`, `categories`, `category_scores`, `category_applied_input_types`, response `id`, and your hashed `safety_identifier` |

## Request
| param | type | req | notes |
|---|---|---|---|
| `input` | string \| array \| content-item array | yes | with `omni-moderation-latest` may mix `{"type":"text","text":…}` and `{"type":"image_url","image_url":{"url":…}}` |
| `model` | string | no | `omni-moderation-latest`, `omni-moderation-2024-09-26`, `text-moderation-latest`, `text-moderation-stable`, `cf.llama-guard-3-8b` |
OpenAI image limit 20 MB — verify the AvalAI/provider limit before relying on it.

```bash
curl https://api.avalai.ir/v1/moderations -H "Content-Type: application/json" -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{"model":"omni-moderation-latest","input":"می‌خواهم آن‌ها را بکشم."}'
```
```python
r = client.moderations.create(model="omni-moderation-latest", input="…")
res = r.results[0]
if res.flagged:
    for cat, hit in res.categories.items():   # (SDK object: use res.categories.model_dump().items() if .items() missing)
        if hit: print(cat)
```
```javascript
const r = await client.moderations.create({ model: "omni-moderation-latest", input: "…" });
if (r.results[0].flagged) for (const [c, f] of Object.entries(r.results[0].categories)) if (f) console.log(c);
```
Text+image: `input:[{type:"text",text:"…"},{type:"image_url",image_url:{url:"https://…/image.png"}}]`.

### Inline output moderation (when route supports it)
```python
resp = client.responses.create(model="gpt-5.6-luna", input="…", moderation={"model":"omni-moderation-latest"})
resp.moderation.input.flagged; resp.moderation.output.flagged
```
- Check inline results **before** showing generated text. With streaming, scores arrive only after the whole output finishes (partial deltas = unmoderated).
- Inline moderation may return an **error object** for the input or output stage → check the result type before reading category scores.
- Moderation covers tool-call arguments/tool output when they appear in conversation content; it does NOT check tool names, descriptions, tool schemas, or response-format schemas.

### Multiple inputs
Array `input` → one `results[]` per input (distinct from async `/v1/batch`). Batch helper: loop `for i in range(0,len(texts),25)`. Hosted Batch API (fa/api-reference/batch) only if `/v1/moderations` is enabled for it on your account (⚠ rate-limits page says no Batch API — treat as unavailable).

## Response
```json
{"id":"modr-5MWoLO","model":"omni-moderation-latest","results":[{"flagged":true,"categories":{"violence":true,…},"category_scores":{"violence":0.9223177433,…},"category_applied_input_types":{"violence":["text"],…}}]}
```
Fields: `id`, `model`, `results[]` → `flagged` (primary signal), `categories` (bools), `category_scores` (0–1; custom thresholds may need retuning on model upgrades), `category_applied_input_types` (`text`/`image` per category).

### Categories (13)
| category | meaning | inputs |
|---|---|---|
| `sexual` | arousing/sexual-services content (excluding educational/health) | text+image |
| `sexual/minors` | sexual content involving <18 | text only |
| `hate`, `hate/threatening` | hateful on protected identity / with violence | text only |
| `harassment`, `harassment/threatening` | harassing language / with violence or serious harm | text only |
| `illicit`, `illicit/violent` | instructions/facilitation of illegal acts / also violence or weapons | text only |
| `self-harm`, `self-harm/intent`, `self-harm/instructions` | promoting / stated intent / instructions | text+image |
| `violence`, `violence/graphic` | depicting violence / graphic depiction | text+image |

## Models (all free except Llama Guard)
`omni-moderation-latest` (text+image, free) · `omni-moderation-2024-09-26` (pinned snapshot, free) · `text-moderation-latest` / `text-moderation-stable` (text, free) · `cf.llama-guard-3-8b` (Cloudflare Llama Guard; see pricing page).

## Best practices
- Layered filtering: client-side pre-filter → Moderation API → human review for borderline.
- Custom thresholds per category on `category_scores` (e.g. stricter `sexual/minors` ≈0.1, others 0.5):
```python
def is_content_allowed(result, custom=None):
    th = {"sexual":.5,"hate":.5,"harassment":.5,"self-harm":.5,"illicit":.5,"illicit/violent":.5,"sexual/minors":.1,
          "hate/threatening":.5,"violence/graphic":.5,"self-harm/intent":.5,"self-harm/instructions":.5,
          "harassment/threatening":.5,"violence":.5}
    th.update(custom or {})
    s = result.category_scores; s = s.model_dump() if hasattr(s,"model_dump") else s
    return all(s.get(k,0) < v for k,v in th.items())
```
- False positives: use scores not just `flagged`; secondary check for borderline; allow-list known-safe content.
- Policy: tell users your moderation policy, offer an appeal path, mind cultural context, update as language evolves.
- Errors: 400/401/403/404/429/500 (fa/guides/error-handling).
- Related: fa/models/model-details, authentication, fa/guides/rate-limits; fa/safety/content-policy (image API moderation_blocked errors → see images.md).
