# Multi-language clients (PHP, Go, Java, C#, Ruby, Rust, Node fetch, cURL)

Why this file: the docs only ship Python/JS/cURL (+ a few broken Go/PHP snippets). This file is **authored by the skill**, not copied from AvalAI. Raw-HTTP versions are the most reliable (they depend only on the wire protocol in `api-reference/*.md`); SDK versions depend on the SDK's version → **pin the version and verify the constructor names against that SDK's README** if a compile error appears. Replace `MODEL` with an id verified by `scripts/avalai_live.py check MODEL`.

Wire contract (all languages)
- Base: `https://api.avalai.ir/v1` · header `Authorization: Bearer $AVALAI_API_KEY` · `Content-Type: application/json`.
- Responses: `POST /responses` `{model,input}` → text in `output[].content[].text` (SDKs expose `output_text`; raw HTTP has NO `output_text` field — walk `output`).
- Chat: `POST /chat/completions` `{model,messages}` → `choices[0].message.content`.
- Read header **`avalai-request-id`** (not `x-request-id`, dropped after 2026-10-15) and log it. 429 → honor `Retry-After`, backoff+jitter, cap retries. Timeouts explicit (flex tier: 900 s).
- Anthropic-native: `POST https://api.avalai.ir/v1/messages` with `x-api-key`, `anthropic-version: 2023-06-01`, `max_tokens` required.
- Never put the key in browser/mobile code; read it from env/secret store.

## cURL (reference; streaming + request id)
```bash
curl -sS -D headers.txt https://api.avalai.ir/v1/chat/completions \
  -H "Authorization: Bearer $AVALAI_API_KEY" -H "Content-Type: application/json" \
  -d '{"model":"MODEL","messages":[{"role":"user","content":"Say hi"}]}' ; grep -i avalai-request-id headers.txt
# streaming (SSE): add "stream":true, use -N; lines "data: {...}" end with "data: [DONE]"
curl -N https://api.avalai.ir/v1/chat/completions -H "Authorization: Bearer $AVALAI_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"model":"MODEL","stream":true,"stream_options":{"include_usage":true},"messages":[{"role":"user","content":"Count to 5"}]}'
```

## PHP
Raw cURL (no dependency, PHP ≥ 7.4):
```php
<?php
function avalai(string $path, array $body, int $timeout = 120, int $maxRetries = 4): array {
    $key = getenv('AVALAI_API_KEY') ?: throw new RuntimeException('AVALAI_API_KEY not set');
    for ($attempt = 0; ; $attempt++) {
        $ch = curl_init('https://api.avalai.ir/v1' . $path);
        $headers = [];
        curl_setopt_array($ch, [
            CURLOPT_POST => true,
            CURLOPT_HTTPHEADER => ["Authorization: Bearer $key", 'Content-Type: application/json'],
            CURLOPT_POSTFIELDS => json_encode($body, JSON_UNESCAPED_UNICODE),
            CURLOPT_RETURNTRANSFER => true,
            CURLOPT_TIMEOUT => $timeout,
            CURLOPT_HEADERFUNCTION => function ($c, $h) use (&$headers) {
                $p = explode(':', $h, 2);
                if (count($p) === 2) $headers[strtolower(trim($p[0]))] = trim($p[1]);
                return strlen($h);
            },
        ]);
        $raw = curl_exec($ch);
        $code = curl_getinfo($ch, CURLINFO_HTTP_CODE);
        $err = curl_error($ch);
        curl_close($ch);
        $retryable = $raw === false || $code === 429 || $code >= 500;
        if ($retryable && $attempt < $maxRetries) {
            $wait = isset($headers['retry-after']) ? (float)$headers['retry-after'] : min(30, 2 ** $attempt) + mt_rand(0, 1000) / 1000;
            usleep((int)($wait * 1e6));
            continue;
        }
        if ($raw === false) throw new RuntimeException("network error: $err");
        $data = json_decode($raw, true, 512, JSON_THROW_ON_ERROR);
        if ($code >= 400) throw new RuntimeException("HTTP $code ({$headers['avalai-request-id']}): " . json_encode($data['error'] ?? $data));
        $data['_request_id'] = $headers['avalai-request-id'] ?? null;
        return $data;
    }
}
$r = avalai('/responses', ['model' => 'MODEL', 'input' => 'Give one tip for PHP devs.']);
$text = '';
foreach ($r['output'] as $item) foreach (($item['content'] ?? []) as $c) if (($c['type'] ?? '') === 'output_text') $text .= $c['text'];
echo $text, "\n", $r['_request_id'], "\n";
```
SDK `openai-php/client` (`composer require openai-php/client guzzlehttp/guzzle`):
```php
$client = OpenAI::factory()
    ->withApiKey(getenv('AVALAI_API_KEY'))
    ->withBaseUri('api.avalai.ir/v1')          // no scheme in many versions; if you get double https, pass with scheme
    ->withHttpClient(new \GuzzleHttp\Client(['timeout' => 120]))
    ->make();
$res = $client->chat()->create(['model' => 'MODEL', 'messages' => [['role' => 'user', 'content' => 'Hello']]]);
echo $res->choices[0]->message->content;
```
Laravel: put key in `.env` (`AVALAI_API_KEY`), `config/services.php` → `'avalai' => ['key' => env('AVALAI_API_KEY')]`; call from queued jobs for long requests; never expose via `.env` in public dir.

## Go
Raw `net/http`:
```go
package main

import (
	"bytes"; "encoding/json"; "fmt"; "io"; "math/rand"; "net/http"; "os"; "strconv"; "time"
)

func call(path string, body any) (map[string]any, string, error) {
	payload, _ := json.Marshal(body)
	client := &http.Client{Timeout: 120 * time.Second}
	for attempt := 0; ; attempt++ {
		req, _ := http.NewRequest("POST", "https://api.avalai.ir/v1"+path, bytes.NewReader(payload))
		req.Header.Set("Authorization", "Bearer "+os.Getenv("AVALAI_API_KEY"))
		req.Header.Set("Content-Type", "application/json")
		resp, err := client.Do(req)
		if err == nil && resp.StatusCode != 429 && resp.StatusCode < 500 {
			defer resp.Body.Close()
			b, _ := io.ReadAll(resp.Body)
			var out map[string]any
			if e := json.Unmarshal(b, &out); e != nil { return nil, "", e }
			rid := resp.Header.Get("avalai-request-id")
			if resp.StatusCode >= 400 { return out, rid, fmt.Errorf("HTTP %d (%s): %s", resp.StatusCode, rid, b) }
			return out, rid, nil
		}
		if attempt >= 4 { if err != nil { return nil, "", err }; return nil, "", fmt.Errorf("HTTP %d after retries", resp.StatusCode) }
		wait := time.Duration(1<<attempt)*time.Second + time.Duration(rand.Intn(1000))*time.Millisecond
		if resp != nil {
			if ra, e := strconv.ParseFloat(resp.Header.Get("Retry-After"), 64); e == nil { wait = time.Duration(ra * float64(time.Second)) }
			resp.Body.Close()
		}
		time.Sleep(wait)
	}
}

func main() {
	out, rid, err := call("/chat/completions", map[string]any{"model": "MODEL",
		"messages": []map[string]string{{"role": "user", "content": "Hello"}}})
	if err != nil { panic(err) }
	msg := out["choices"].([]any)[0].(map[string]any)["message"].(map[string]any)["content"]
	fmt.Println(msg, rid)
}
```
SDK `github.com/openai/openai-go` (v1+; check import path/version in its README):
```go
client := openai.NewClient(option.WithAPIKey(os.Getenv("AVALAI_API_KEY")), option.WithBaseURL("https://api.avalai.ir/v1/"))
resp, err := client.Chat.Completions.New(ctx, openai.ChatCompletionNewParams{
	Model:    "MODEL",
	Messages: []openai.ChatCompletionMessageParamUnion{openai.UserMessage("Hello")},
})
if err != nil { log.Fatal(err) }
fmt.Println(resp.Choices[0].Message.Content)
```

## Java (11+)
Raw `java.net.http`:
```java
import java.net.URI; import java.net.http.*; import java.time.Duration;

public class Avalai {
  static final HttpClient HTTP = HttpClient.newBuilder().connectTimeout(Duration.ofSeconds(10)).build();
  public static void main(String[] a) throws Exception {
    String body = "{\"model\":\"MODEL\",\"messages\":[{\"role\":\"user\",\"content\":\"Hello\"}]}";
    HttpRequest req = HttpRequest.newBuilder(URI.create("https://api.avalai.ir/v1/chat/completions"))
        .timeout(Duration.ofSeconds(120))
        .header("Authorization", "Bearer " + System.getenv("AVALAI_API_KEY"))
        .header("Content-Type", "application/json")
        .POST(HttpRequest.BodyPublishers.ofString(body)).build();
    HttpResponse<String> r = HTTP.send(req, HttpResponse.BodyHandlers.ofString());
    System.out.println(r.statusCode() + " " + r.headers().firstValue("avalai-request-id").orElse("-"));
    System.out.println(r.body()); // parse with Jackson/Gson; on 429/5xx retry with backoff using Retry-After
  }
}
```
SDK `com.openai:openai-java`:
```java
OpenAIClient client = OpenAIOkHttpClient.builder()
    .apiKey(System.getenv("AVALAI_API_KEY")).baseUrl("https://api.avalai.ir/v1").build();
ChatCompletionCreateParams p = ChatCompletionCreateParams.builder().model("MODEL").addUserMessage("Hello").build();
System.out.println(client.chat().completions().create(p).choices().get(0).message().content().orElse(""));
```

## C# / .NET 8
Raw HttpClient:
```csharp
using System.Net.Http.Headers; using System.Text; using System.Text.Json;
var http = new HttpClient { BaseAddress = new Uri("https://api.avalai.ir/v1/"), Timeout = TimeSpan.FromSeconds(120) };
http.DefaultRequestHeaders.Authorization = new AuthenticationHeaderValue("Bearer", Environment.GetEnvironmentVariable("AVALAI_API_KEY"));
var body = JsonSerializer.Serialize(new { model = "MODEL", messages = new[] { new { role = "user", content = "Hello" } } });
var resp = await http.PostAsync("chat/completions", new StringContent(body, Encoding.UTF8, "application/json"));
var rid = resp.Headers.TryGetValues("avalai-request-id", out var v) ? v.First() : "-";
resp.EnsureSuccessStatusCode(); // add Polly retry for 429/5xx honoring Retry-After
using var doc = JsonDocument.Parse(await resp.Content.ReadAsStringAsync());
Console.WriteLine(doc.RootElement.GetProperty("choices")[0].GetProperty("message").GetProperty("content").GetString() + " " + rid);
```
SDK `OpenAI` NuGet (2.x):
```csharp
using OpenAI; using OpenAI.Chat; using System.ClientModel;
var client = new OpenAIClient(new ApiKeyCredential(Environment.GetEnvironmentVariable("AVALAI_API_KEY")!),
    new OpenAIClientOptions { Endpoint = new Uri("https://api.avalai.ir/v1") });
ChatCompletion c = client.GetChatClient("MODEL").CompleteChat("Hello");
Console.WriteLine(c.Content[0].Text);
```

## Ruby
Raw `net/http`:
```ruby
require "net/http"; require "json"
def avalai(path, body, retries: 4)
  uri = URI("https://api.avalai.ir/v1#{path}")
  retries.times.each do |i|
    http = Net::HTTP.new(uri.host, uri.port); http.use_ssl = true; http.read_timeout = 120
    req = Net::HTTP::Post.new(uri, "Authorization" => "Bearer #{ENV.fetch('AVALAI_API_KEY')}", "Content-Type" => "application/json")
    req.body = body.to_json
    res = http.request(req)
    if res.code.to_i == 429 || res.code.to_i >= 500
      sleep((res["retry-after"] || (2**i + rand)).to_f); next
    end
    raise "HTTP #{res.code} (#{res['avalai-request-id']}): #{res.body}" if res.code.to_i >= 400
    return JSON.parse(res.body).merge("_request_id" => res["avalai-request-id"])
  end
  raise "retries exhausted"
end
r = avalai("/chat/completions", { model: "MODEL", messages: [{ role: "user", content: "Hello" }] })
puts r.dig("choices", 0, "message", "content")
```
Gem `ruby-openai`: `OpenAI::Client.new(access_token: ENV["AVALAI_API_KEY"], uri_base: "https://api.avalai.ir", api_version: "v1")` (then `client.chat(parameters: {model: "MODEL", messages: [...]})`) — verify uri_base/api_version semantics for your gem version.

## Rust (reqwest + serde_json + tokio)
```rust
use serde_json::{json, Value};
#[tokio::main]
async fn main() -> Result<(), Box<dyn std::error::Error>> {
    let key = std::env::var("AVALAI_API_KEY")?;
    let client = reqwest::Client::builder().timeout(std::time::Duration::from_secs(120)).build()?;
    let resp = client.post("https://api.avalai.ir/v1/chat/completions")
        .bearer_auth(key)
        .json(&json!({"model":"MODEL","messages":[{"role":"user","content":"Hello"}]}))
        .send().await?;
    let rid = resp.headers().get("avalai-request-id").and_then(|v| v.to_str().ok()).unwrap_or("-").to_string();
    let status = resp.status();
    let v: Value = resp.json().await?;
    if !status.is_success() { return Err(format!("HTTP {status} ({rid}): {v}").into()); }
    println!("{} {rid}", v["choices"][0]["message"]["content"]);
    Ok(())
}
```

## Node/TS without SDK (fetch, Node ≥18) incl. streaming
```ts
const res = await fetch("https://api.avalai.ir/v1/chat/completions", {
  method: "POST",
  headers: { Authorization: `Bearer ${process.env.AVALAI_API_KEY}`, "Content-Type": "application/json" },
  body: JSON.stringify({ model: "MODEL", stream: true, messages: [{ role: "user", content: "Hi" }] }),
  signal: AbortSignal.timeout(120_000),
});
if (!res.ok) throw new Error(`HTTP ${res.status} ${res.headers.get("avalai-request-id")}: ${await res.text()}`);
const dec = new TextDecoder(); let buf = "";
for await (const chunk of res.body as any) {
  buf += dec.decode(chunk, { stream: true });
  for (let i; (i = buf.indexOf("\n")) >= 0; ) {
    const line = buf.slice(0, i).trim(); buf = buf.slice(i + 1);
    if (!line.startsWith("data:")) continue;
    const d = line.slice(5).trim(); if (d === "[DONE]") continue;
    process.stdout.write(JSON.parse(d).choices?.[0]?.delta?.content ?? "");
  }
}
```

## Tool calling over raw HTTP (any language)
Request adds `"tools":[{"type":"function","function":{"name":"get_weather","description":"…","parameters":{"type":"object","properties":{"city":{"type":"string"}},"required":["city"]}}}]`. If `choices[0].message.tool_calls` is present: execute each, append the assistant message **unchanged** plus one `{"role":"tool","tool_call_id":<id>,"content":"<json string>"}` per call, re-POST. Validate arguments (they're model-generated JSON strings); cap loop iterations (e.g. 8); require human approval before side effects. Claude/Gemini via `/v1/messages`: `tool_use` blocks → reply with `tool_result` blocks in the next `user` message; keep thinking blocks intact.

## Cost + billing in any language
1. Run `scripts/avalai_live.py cost MODEL --in N --out M` for estimates (live prices, long-context tiers, toman rate via `--rate`).
2. Exact: store `avalai-request-id` per call; ≥30 s later `POST /user/v1/transactions/lookup {"transaction_ids":[…≤1000]}` → read `cost.unit` (USD) — not `total_cost_usd`.
