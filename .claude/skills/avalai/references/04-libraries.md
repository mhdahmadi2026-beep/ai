# کتابخانه‌ها / Libraries — https://docs.avalai.ir/fa/libraries

Set up a local dev environment to use the AvalAI API with an SDK. AvalAI uses the **official OpenAI SDKs with a custom base URL**.

## API key
Create a key in the dashboard (https://chat.avalai.ir/platform/home); store it safely (e.g. `.zshrc`) and export as env var.
```bash
# macOS / Linux
export AVALAI_API_KEY="aa-YOUR_API_KEY"
```
```powershell
# Windows PowerShell
setx AVALAI_API_KEY "aa-YOUR_API_KEY"
```
(Key prefix in this page's example: `aa-`.) All examples pass `AVALAI_API_KEY` explicitly and set the custom AvalAI base URL on each client.

## Three SDK approaches
1. **OpenAI-compatible SDKs** (unified) — all models from multiple providers, same syntax. Base URL **with `/v1`**: `https://api.avalai.ir/v1`
2. **Official Anthropic SDKs** (native) — Anthropic, OpenAI, AWS Bedrock, Vertex AI, Gemini models via native syntax. Base URL **without `/v1`**: `https://api.avalai.ir`
3. **Google GenAI SDK** (native) — Gemini only, Google-native schema. Base URL **without `/v1`**: `https://api.avalai.ir` (uses `/v1beta/models/{model}:generateContent`).

### Responses vs Chat Completions
Official OpenAI SDKs + custom `baseURL` work for both `/v1/responses` and `/v1/chat/completions`:
- **Start new text/reasoning/tool workflows with Responses** when the model supports it: send `input` (+ `instructions`), read `response.output_text`.
- **Keep Chat Completions for existing integrations**: you already have `messages`, your framework wants chat completions, or the model is chat-compat only.
- **Migrate incrementally:** plain `messages` → `input`; system prompt → `instructions`; `choices[0].message.content` → `output_text`.
Full path: /fa/guides/responses-vs-chat-completions

### Keeping SDKs current
OpenAI SDKs change fast as Responses API gains features. In production **pin versions**, read each SDK's changelog before major upgrades, and keep a **raw-HTTP fallback** for new AvalAI routes or provider-specific params not yet exposed in the SDK. Where a sample mentions `OPENAI_API_KEY`, use `AVALAI_API_KEY` and set `baseURL`/`base_url` = `https://api.avalai.ir/v1`.

### Production SDK checklist
- **Pick the right client layer:** official OpenAI SDKs for direct `/v1/responses`, `/v1/chat/completions`, audio, images, embeddings, files; raw HTTP when a new AvalAI route/native provider param isn't exposed.
- **Secrets server-side:** never put `AVALAI_API_KEY` in browser/mobile code or public repos; proxy browser flows through your backend.
- **Log trace IDs:** capture `avalai-request-id` from response headers; also send your own `X-Client-Request-Id` (ASCII, unique per request, short — limits in /fa/api-reference/response-headers).
- **Keep SDK surfaces separate:** OpenAI-compatible → `https://api.avalai.ir/v1`; native Anthropic and Google → `https://api.avalai.ir` (no `/v1`), deliberately.
- **Retry deliberately:** SDK retry is fine for transient network errors; for tool calls, payments, file uploads and long jobs still implement idempotency, backoff, and user-visible error state.
- **Agents SDK = orchestration guidance:** OpenAI recommends the Agents SDK for tool orchestration, handoff, guardrails, tracing, sandbox execution. Use with AvalAI only after verifying the model client, base URL and tool capabilities of the chosen route.

### Timeouts & long requests
Official SDKs have request timeouts and auto-retry some transient timeouts. On AvalAI, **set timeout explicitly** for requests longer than a normal chat turn: **flex service tier**, long documents, deep-research-style workflows, large file input, slow tools, app-managed background jobs.
Use longer timeouts only for workloads that can truly wait. For interactive UX prefer streaming, progress messages, shorter `max_output_tokens`, lower `reasoning.effort`, or an app-side job the user can resume.
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
    timeout=900.0,  # 15 minutes for long requests
)

response = client.with_options(timeout=900.0).responses.create(
    model="gpt-5.6-luna",
    input="Analyze this long report and return a concise risk summary...",
    max_output_tokens=800,
)

print(response.output_text)
```
```javascript
import OpenAI from "openai";

const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1",
  timeout: 900_000, // 15 minutes for long requests
});

const response = await client.responses.create(
  {
    model: "gpt-5.6-luna",
    input: "Analyze this long report and return a concise risk summary...",
    max_output_tokens: 800,
  },
  { timeout: 900_000 }
);

console.log(response.output_text);
```
When wrapping SDK calls with retries, auto-retry **only idempotent operations**. For writes, payments, file uploads, webhooks, and side-effecting tools, store an idempotency key or job ID first and retry from app state — never blind replay.

## Install an official SDK (language index)
JavaScript/TypeScript (`npm install openai`; Node, Deno, Bun) · Python (`pip install openai`) · .NET/C# (`dotnet add package OpenAI`, Microsoft-backed) · Java (Maven `openai-java`) · Go (official Go lib) · Ruby (`gem "openai"`) · OpenAI CLI (terminal workflow, raw-HTTP fallback for AvalAI) · Community libraries.

## JavaScript (Node.js / Deno / Bun)
```bash
npm install openai
```
`example.mjs`:
```javascript
import OpenAI from "openai";
const client = new OpenAI({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir/v1", // AvalAI API endpoint
});

const response = await client.responses.create({
  model: "gpt-5.6-luna",
  input: "Write a one-sentence bedtime story about a unicorn.",
});

console.log(response.output_text);
```
Run: `node example.mjs` (or Deno/Bun equivalent).

## Python
```bash
pip install openai
```
```python
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir/v1",
)

response = client.responses.create(
    model="gpt-5.6-luna", input="Write a one-sentence bedtime story about a unicorn."
)

print(response.output_text)
```
Run: `python example.py`.

## .NET / C#
```bash
dotnet add package OpenAI
```
Chat Completions (/fa/api-reference/chat):
```csharp
using OpenAI.Chat;

ChatClient client = new(
 model: "gpt-5.6-luna",
 apiKey: Environment.GetEnvironmentVariable("AVALAI_API_KEY"),
 endpoint: new Uri("https://api.avalai.ir/v1") // AvalAI API endpoint
);

ChatCompletion completion = client.CompleteChat("Say 'this is a test.'");

Console.WriteLine($"[ASSISTANT]: {completion.Content[0].Text}");
```
Responses API:
```csharp
using OpenAI.Responses;

OpenAIResponseClient client = new(
 model: "gpt-5.6-luna",
 apiKey: Environment.GetEnvironmentVariable("AVALAI_API_KEY"),
 endpoint: new Uri("https://api.avalai.ir/v1") // AvalAI API endpoint
);

OpenAIResponse response = client.CreateResponse("Say 'this is a test.'");

Console.WriteLine($"[ASSISTANT]: {response.GetOutputText()}");
```
> Note: the `endpoint:` constructor form is as published; in current OpenAI .NET versions the endpoint is normally passed through `OpenAIClientOptions { Endpoint = ... }`. Verify against the installed version.

## Java
Maven:
```xml
<dependency>
 <groupId>com.openai</groupId>
 <artifactId>openai-java</artifactId>
 <version>0.31.0</version>
</dependency>
```
Chat Completions:
```java
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.ChatCompletion;
import com.openai.models.ChatCompletionCreateParams;
import com.openai.models.ChatModel;

// custom client with AvalAI base URL
OpenAIClient client = OpenAIOkHttpClient.builder()
 .baseUrl("https://api.avalai.ir/v1") // AvalAI API endpoint
 .apiKey(System.getenv("AVALAI_API_KEY"))
 .build();

ChatCompletionCreateParams params = ChatCompletionCreateParams.builder()
 .addUserMessage("Say this is a test")
 .model(ChatModel.O3_MINI)
 .build();
ChatCompletion chatCompletion = client.chat().completions().create(params);
```
Responses API:
```java
import com.openai.client.OpenAIClient;
import com.openai.client.okhttp.OpenAIOkHttpClient;
import com.openai.models.responses.Response;
import com.openai.models.responses.ResponseCreateParams;

OpenAIClient client = OpenAIOkHttpClient.builder()
 .baseUrl("https://api.avalai.ir/v1") // AvalAI API endpoint
 .apiKey(System.getenv("AVALAI_API_KEY"))
 .build();

ResponseCreateParams params = ResponseCreateParams.builder()
 .input("Say this is a test")
 .model("gpt-5.6-luna")
 .build();

Response response = client.responses().create(params);
System.out.println(response.outputText());
```

## Go
Import: `import ("github.com/openai/openai-go") // as openai`
Chat Completions:
```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go"
	"github.com/openai/openai-go/option"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"), // AvalAI API endpoint
	)
	chatCompletion, err := client.Chat.Completions.New(
		context.TODO(), openai.ChatCompletionNewParams{
			Messages: openai.F(
				[]openai.ChatCompletionMessageParamUnion{
					openai.UserMessage("Say this is a test"),
				},
			),
			Model: openai.F(openai.ChatModel("gpt-5.6-luna")),
		},
	)

	if err != nil {
		panic(err.Error())
	}

	fmt.Println(chatCompletion.Choices[0].Message.Content)
}
```
Responses API (note `/v3` module):
```go
package main

import (
	"context"
	"fmt"
	"os"

	"github.com/openai/openai-go/v3"
	"github.com/openai/openai-go/v3/option"
	"github.com/openai/openai-go/v3/responses"
)

func main() {
	client := openai.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir/v1"), // AvalAI API endpoint
	)
	resp, err := client.Responses.New(context.TODO(), openai.ResponseNewParams{
		Model: "gpt-5.6-luna", // (published page writes `model:` lowercase — typo; field is `Model`)
		Input: responses.ResponseNewParamsInputUnion{
			OfString: openai.String("Say this is a test"),
		},
	})
	if err != nil {
		panic(err.Error())
	}

	fmt.Println(resp.OutputText())
}
```
> Chat example uses v1-style `openai.F(...)` wrappers; the Responses example uses `/v3` (no `F`). Don't mix module versions.

## Ruby
Use the official SDK only if the installed version supports a custom base URL; otherwise use the raw-HTTP fallback (CLI section).
```ruby
gem "openai"
```
```ruby
require "openai"

openai = OpenAI::Client.new(
  api_key: ENV.fetch("AVALAI_API_KEY"),
  base_url: "https://api.avalai.ir/v1"
)

response = openai.responses.create(
  model: "gpt-5.6-luna",
  input: "Write a one-sentence bedtime story about a unicorn."
)

puts(response.output_text)
```

## OpenAI CLI
Useful for repeatable terminal workflows, but may target OpenAI's hosted API by default unless your installed version supports a custom base URL. If it honors `OPENAI_BASE_URL`, point it at AvalAI explicitly:
```bash
OPENAI_API_KEY="$AVALAI_API_KEY" \
  OPENAI_BASE_URL="https://api.avalai.ir/v1" \
  openai responses create \
  --model gpt-5.5 \
  --input "Write a one-sentence bedtime story about a unicorn." \
  --format yaml \
  --transform 'output.#(type=="message").content.0.text'
```
For repeatable scripts needing assistant text, JSON extraction or one-line records for shell tools, use `--format`, `--transform` and YAML request bodies. **Don't commit** generated files such as `project.json`, `.env`, uploaded file IDs, or raw API responses — CLI workflows often write secrets/customer data to disk.

If your CLI ignores `OPENAI_BASE_URL`, or you're testing a new AvalAI route before CLI flags exist, prefer raw HTTP (endpoint and key explicit):
```bash
curl "https://api.avalai.ir/v1/responses" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "model": "gpt-5.6-luna",
    "input": "Write a one-sentence bedtime story about a unicorn."
  }'
```
Use the fallback for new endpoints, SDK-behavior debugging, or `jq` scripts. When using the generated `openai` CLI, first run a harmless `/v1/models` check or short `/v1/responses` request to confirm `AVALAI_API_KEY` and base URL actually applied.

## Official Anthropic SDKs
AvalAI supports official Anthropic SDKs — native syntax while accessing models via AvalAI's unified API. Since **June 2025** the Anthropic SDK can reach models from multiple providers, not only Claude.
Chat models from these providers work via the Anthropic SDK and `v1/messages`: **OpenAI, Anthropic, AWS Bedrock, Vertex AI, Gemini** (any chat model supporting the chat-completion endpoint).
**Base URL: `https://api.avalai.ir` (no `/v1`).**

### Python
```bash
pip install anthropic
```
```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir",  # AvalAI endpoint without /v1
)

# Claude model
message = client.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، کلود"}],
)
print(message.content)

# OpenAI model via Anthropic SDK
message = client.messages.create(
    model="gpt-5.6-luna",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، gpt-5.5!"}],
)
print(message.content)

# Gemini model via Anthropic SDK
message = client.messages.create(
    model="gemini-2.5-pro",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، Gemini!"}],
)
print(message.content)
```
### TypeScript / JavaScript
```bash
npm install @anthropic-ai/sdk
```
```javascript
import Anthropic from "@anthropic-ai/sdk";

const anthropic = new Anthropic({
  apiKey: process.env.AVALAI_API_KEY,
  baseURL: "https://api.avalai.ir", // AvalAI endpoint without /v1
});

// Claude model
const claudeMsg = await anthropic.messages.create({
  model: "claude-sonnet-5",
  max_tokens: 1024,
  messages: [{ role: "user", content: "سلام، کلود" }],
});
console.log(claudeMsg);

// OpenAI model via Anthropic SDK
const openaiMsg = await anthropic.messages.create({
  model: "gpt-5.6-luna",
  max_tokens: 1024,
  messages: [{ role: "user", content: "سلام، gpt-5.5!" }],
});
console.log(openaiMsg);

// Gemini model (page comment says "Vertex AI") via Anthropic SDK
const vertexMsg = await anthropic.messages.create({
  model: "gemini-2.5-pro",
  max_tokens: 1024,
  messages: [{ role: "user", content: "سلام، Gemini!" }],
});
console.log(vertexMsg);
```
### Go
```bash
go get github.com/anthropics/anthropic-sdk-go
```
```go
package main

import (
	"context"
	"fmt"
	"github.com/anthropics/anthropic-sdk-go"
	"github.com/anthropics/anthropic-sdk-go/option"
	"os"
)

func main() {
	client := anthropic.NewClient(
		option.WithAPIKey(os.Getenv("AVALAI_API_KEY")),
		option.WithBaseURL("https://api.avalai.ir"), // AvalAI endpoint without /v1
	)

	message, err := client.Messages.New(context.TODO(), anthropic.MessageNewParams{
		Model:     anthropic.F(anthropic.ModelClaudeSonnet4_0),
		MaxTokens: anthropic.F(int64(1024)),
		Messages: anthropic.F([]anthropic.MessageParam{
			anthropic.NewUserMessage(anthropic.NewTextBlock("سلام، کلود")),
		}),
	})
	if err != nil {
		panic(err.Error())
	}
	fmt.Printf("%+v\n", message.Content)
}
```
### Ruby
```bash
gem install anthropic
```
```ruby
require "bundler/setup"
require "anthropic"

anthropic = Anthropic::Client.new(
    api_key: ENV.fetch("AVALAI_API_KEY"),
    base_url: "https://api.avalai.ir" # AvalAI endpoint without /v1
)

message = anthropic.messages.create(
    max_tokens: 1024,
    messages: [{
            role: "user",
            content: "سلام، کلود"
        }
    ],
    model: "claude-sonnet-5"
)

puts(message.content)
```
### Beta features
All Anthropic SDKs support the beta namespace:
```python
import os
import anthropic

client = anthropic.Anthropic(
    api_key=os.environ["AVALAI_API_KEY"],
    base_url="https://api.avalai.ir",  # AvalAI endpoint without /v1
)

message = client.beta.messages.create(
    model="claude-sonnet-5",
    max_tokens=1024,
    messages=[{"role": "user", "content": "سلام، کلود"}],
    betas=["beta-feature-name"],
)
print(message.content)
```
### Models available via Anthropic SDK
**Claude — tier 1 and above:** Claude Opus 4.7 `claude-opus-4-7` · Claude Sonnet 4.6 `claude-sonnet-4-6` · Claude Sonnet 4.5 `claude-sonnet-4-5` · "Claude 3.5 Haiku" label (page) → ID `claude-haiku-4-5`.
**Other providers:** OpenAI (`gpt-5.5`, `gpt-5.3-codex`, `gpt-5-mini`), AWS Bedrock models, Vertex AI models, Gemini (`gemini-3.5-flash`, `gemini-3.1-pro-preview`). Full list: models docs (page links /fa/api-reference/chat).

## Google GenAI SDK
Native access to Gemini via Google's native schema/endpoints.
### JavaScript / TypeScript
```bash
npm install @google/genai
```
```javascript
import { GoogleGenAI } from "@google/genai";

const ai = new GoogleGenAI({
	apiKey: process.env.AVALAI_API_KEY,
	httpOptions: {"apiVersion": "v1beta", "baseUrl": "https://api.avalai.ir"}
});

async function main() {
	const response = await ai.models.generateContent({
		model: "gemini-2.5-flash",
		contents: "خلاصه‌ای از اصول کلیدی یادگیری ماشین بنویسید.",
	});
	console.log(response.text);
}

await main();
```
### Python
```bash
pip install google-generativeai
```
```python
import os
from google import genai
from google.genai.types import ContentDict, PartDict

# client with AvalAI endpoint
client = genai.Client(
    api_key=os.environ["AVALAI_API_KEY"],
    http_options={"base_url": "https://api.avalai.ir"},  # note: no /v1 suffix
)

# generate content with native API
contents = ContentDict(
    parts=[PartDict(text="داستان کوتاهی درباره هوش مصنوعی بنویس")], role="user"
)

response = await client.agenerate_content(
    contents=contents, model="gemini-2.5-flash", max_tokens=500
)

print(response)
```
Streaming:
```python
response = await client.agenerate_content_stream(
    contents=contents, model="gemini-2.5-flash", max_tokens=500
)

async for chunk in response:
    print(chunk)
```
> ⚠ Published Python snippet is not valid google-genai API: the package for `from google import genai` is `google-genai` (not `google-generativeai`), and the real calls are `client.models.generate_content(...)` / `client.aio.models.generate_content(...)` / `generate_content_stream(...)` with `config=types.GenerateContentConfig(max_output_tokens=...)`. Keep `base_url="https://api.avalai.ir"` via `http_options`. Verify against the installed SDK.

Key features: native API schema (`generateContent`, `streamGenerateContent`); flexible auth (`Authorization: Bearer` or `x-goog-api-key`); full streaming; native multimodal (text, image, audio, video).
Limits: **Gemini models only**; base URL `https://api.avalai.ir` (no `/v1`); uses `/v1beta/models/{model}:generateContent`. Docs: /fa/api-reference/v1beta

## Azure OpenAI libraries
Microsoft-maintained clients compatible with OpenAI and Azure OpenAI; configurable with a custom endpoint for AvalAI:
- .NET: https://github.com/Azure/azure-sdk-for-net/tree/main/sdk/openai/Azure.AI.OpenAI
- JavaScript: https://github.com/Azure/azure-sdk-for-js/tree/main/sdk/openai/openai
- Java: https://github.com/Azure/azure-sdk-for-java/tree/main/sdk/openai/azure-ai-openai
- Go: https://github.com/Azure/azure-sdk-for-go/tree/main/sdk/ai/azopenai

## Community libraries
Maintained by the community for the OpenAI API; many work with AvalAI by setting base URL `https://api.avalai.ir/v1`. Track API changes via https://github.com/openai/openai-openapi. **AvalAI does not endorse their correctness or security — use at your own risk.**
- **C#/.NET:** Betalgo.OpenAI (betalgo/openai) · OpenAI-API-dotnet (OkGoDoIt) · OpenAI-DotNet (RageAgainstThePixel)
- **C++:** liboai (D7EAD)
- **Clojure:** openai-clojure (wkok)
- **Crystal:** openai-crystal (sferik)
- **Dart/Flutter:** openai (anasfik)
- **Delphi:** DelphiOpenAI (HemulGM)
- **Elixir:** openai.ex (mgallo)
- **Go:** go-gpt3 (sashabaranov)
- **Java:** simple-openai (sashirestela) · Spring AI (https://spring.io/projects/spring-ai)
- **Julia:** OpenAI.jl (rory-linehan)
- **Kotlin:** openai-kotlin (Aallam)
- **Node.js:** openai-api (Njerschow) · openai-api-node (erlapso) · gpt-x (ceifa) · gpt3 (poteat) · gpts (thencc) · @dalenguyen/openai · tectalic/openai (public-openai-client-js)
- **PHP:** orhanerday/open-ai · tectalic/openai (public-openai-client-php) · openai-php/client
- **Python:** chronology (OthersideAI)
- **R:** rgpt3 (ben-aaron188)
- **Ruby:** openai (nileshtrivedi) · ruby-openai (alexrudall)
- **Rust:** async-openai (64bit) · fieri (lbkolev)
- **Scala:** openai-scala-client (cequence-io)
- **Swift:** AIProxySwift (lzell) · OpenAIKit (dylanshine) · OpenAI (MacPaw)
- **Unity:** OpenAi-Api-Unity (hexthedev) · com.openai.unity (RageAgainstThePixel)
- **Unreal Engine:** OpenAI-Api-Unreal (KellanM)
GitHub URL pattern: `https://github.com/<author>/<repo>` (exact repos as in page: D7EAD/liboai, wkok/openai-clojure, sferik/openai-crystal, anasfik/openai, HemulGM/DelphiOpenAI, mgallo/openai.ex, sashabaranov/go-gpt3, sashirestela/simple-openai, rory-linehan/OpenAI.jl, Aallam/openai-kotlin, ben-aaron188/rgpt3, nileshtrivedi/openai, alexrudall/ruby-openai, 64bit/async-openai, lbkolev/fieri, cequence-io/openai-scala-client, lzell/AIProxySwift, dylanshine/openai-kit, MacPaw/OpenAI, hexthedev/OpenAi-Api-Unity, RageAgainstThePixel/com.openai.unity, KellanM/OpenAI-Api-Unreal, OthersideAI/chronology, betalgo/openai, OkGoDoIt/OpenAI-API-dotnet, RageAgainstThePixel/OpenAI-DotNet).

## Other useful repos
tiktoken (token counting) · simple-evals (simple eval library) · mle-bench (evaluating ML-engineering agents) · gym (RL library) · swarm (educational orchestration repo) — all under github.com/openai/.

## Related
/fa/api-reference/introduction · /fa/api-reference/authentication · /fa/quickstart
