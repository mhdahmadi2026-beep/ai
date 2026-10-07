# احراز هویت / Authentication — https://docs.avalai.ir/fa/api-reference/authentication

## API keys
Every request must include an API key. Keys are in the dashboard https://chat.avalai.ir/platform/home.
> ⚠ **Security:** keep API keys safe. Never put them in client-side code or public repos — server-side only.

## Auth method: Bearer token (recommended)
`Authorization: Bearer $AVALAI_API_KEY`
```bash
curl https://api.avalai.ir/v1/chat/completions \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
"model": "gpt-5.6-luna",
"messages": [{"role": "user", "content": "Hello!"}]
}'
```
Responses equivalent (`messages`→`input`, system→`instructions`/`developer` item, `choices[0].message.content`→`response.output_text`, tools/multimodal → inspect `response.output` by `type`):
```bash
curl https://api.avalai.ir/v1/responses \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '
  {
    "model": "gpt-5.6-luna",
    "input": "Hello!",
    "instructions": "You are a helpful assistant."
  }'
```
(Other pages note native Anthropic/Google endpoints also accept `x-goog-api-key` for Google-native — see 04-libraries.)

### Client libraries
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)
```
```javascript
import { OpenAI } from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY, // use env vars
  baseURL: "https://api.avalai.ir/v1",
});
```
```go
package main

import (
	"os"

	openai "github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"),
	)
	_ = client
}
```

## API-key best practices
1. Never share keys — treat like passwords. 2. Use environment variables, don't hard-code. 3. Create separate keys for dev / test / production. 4. Limit key permissions (least privilege). 5. Rotate keys regularly. 6. Monitor key usage for unauthorized activity.

## Enterprise access controls
OpenAI's RBAC/Admin API docs are a useful *design pattern*: separate org-level management from project-level runtime access; grant permissions via groups or service accounts; verify access with a non-owner account before wide rollout. **AvalAI has not published OpenAI's org-management APIs** — map the pattern onto the AvalAI dashboard controls and your app's own IAM.
For production on AvalAI:
- issue a separate key per environment / service / tenant / reseller when isolation matters;
- separate admin, billing, support and model-serving credentials;
- when key restriction is available, allow only the routes/models that workload needs;
- in every access review remove unused keys, old users and stale CI secrets;
- log key create/delete/rotate, rate-limit changes and permission changes in your own audit trail.

## Admin automation boundaries
OpenAI Admin APIs use a separate Admin API key and are not valid for normal model endpoints. **AvalAI currently has no documented compatible Admin API** → don't set OpenAI-specific admin-key env vars for AvalAI, don't call OpenAI org-management routes through AvalAI, don't assume OpenAI SDK admin helpers manage AvalAI keys. Do AvalAI management only through the dashboard / documented AvalAI APIs; for user invites, key-lifecycle automation, rate-limit changes or audit-log export, treat as platform-management workflow and confirm a supported AvalAI route first.

## IP allowlist & network identity
OpenAI publishes egress IP ranges for its managed products (ChatGPT integrations, Codex cloud) — these reflect OpenAI infrastructure only, not a specific AvalAI customer/workspace/route. Don't use OpenAI IP ranges to authenticate your app's traffic to AvalAI or to represent AvalAI provider traffic.
- Authenticate every AvalAI request with `Authorization: Bearer $AVALAI_API_KEY`;
- where possible restrict egress of servers/CI runners to `https://api.avalai.ir/v1`;
- verify inbound webhooks/tools/callbacks with signatures, OAuth, mTLS or shared secrets if the upstream supports it;
- keep IP allowlists service-specific and auto-refresh them when a provider publishes changing ranges.

## Server & workload identity planning
OpenAI's enterprise auth docs describe **workload identity federation** (trusted cloud workloads swap OIDC tokens for short-lived API access tokens — no long-lived key). **AvalAI does not currently publish a workload-identity exchange endpoint** → architecture pattern only, not a current AvalAI feature.
For production on AvalAI today:
- keep `AVALAI_API_KEY` only in server-side secret stores (cloud secret manager, vault, CI secrets);
- for browser/mobile, issue short-lived session tokens from your own backend;
- separate AvalAI key per service/environment/tenant when isolation matters;
- log `avalai-request-id`, endpoint, model and a **hashed** `safety_identifier` for auditable requests without exposing raw PII;
- **rotate keys immediately** if a deployment, employee device, CI runner or repo secret may have leaked.
If AvalAI later adds workload identity, expect to: configure a trusted issuer, match workload claims to service-account / API-key scope, grant least privilege, and monitor token-exchange failures separately from normal API errors.

## Organization identifiers — ⚠ NOT IMPLEMENTED
> "ویژگی پیاده‌سازی نشده!" — under development, not yet available; will be announced via official channels.
Until org routing is enabled: **don't send an organization header or the SDK `organization` option.** For traffic/billing separation use separate API keys, separate environments, projects, or reseller/user metadata in your own app.

## Rate limits
429 when exceeded → /fa/guides/rate-limits (09-rate-limits.md).

## Key management in the dashboard (https://chat.avalai.ir/platform/home)
1. create new keys 2. delete existing keys 3. view key usage stats 4. set permissions & limits on keys.

## Troubleshooting auth
1. correct key? 2. key active & not expired? 3. correct auth method? 4. key has needed permissions? 5. check you haven't exceeded rate limits.
Still stuck → AvalAI support https://avalai.ir/contact-us-avalai.
