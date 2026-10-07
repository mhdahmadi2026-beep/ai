# Laravel / PHP — complete AvalAI integration (Laravel 10/11/12, PHP ≥ 8.1)

Authored for this skill (not copied from the docs). Uses only Laravel's built-in `Http` client — no SDK needed, so nothing breaks when an SDK changes. **Not run against the live API in the sandbox → run the test-suite in §14 and one real call before production.** Replace `MODEL` with ids verified via `scripts/avalai_live.py check`.

Contents: 1 setup · 2 client service · 3 Chat/Responses · 4 streaming (SSE) · 5 tool calling · 6 structured output · 7 embeddings · 8 images/video · 9 audio STT/TTS · 10 files/OCR/PDF · 11 search · 12 Claude native Messages · 13 cost tracking (DB + User API) · 14 tests · 15 queues & rate limits · 16 security/ops checklist · 17 Artisan tools.

## 1. Setup
`.env`
```
AVALAI_API_KEY=...            # server-side only, never in Blade/JS/Inertia props
AVALAI_BASE_URL=https://api.avalai.ir/v1
AVALAI_DEFAULT_MODEL=gpt-6.1-sol      # verify live
AVALAI_TIMEOUT=120
AVALAI_USD_TOMAN_RATE=               # optional; set from today's rate for toman estimates
```
`config/avalai.php`
```php
<?php
return [
    'key'      => env('AVALAI_API_KEY'),
    'base_url' => env('AVALAI_BASE_URL', 'https://api.avalai.ir/v1'),
    'native_url' => env('AVALAI_NATIVE_URL', 'https://api.avalai.ir'),   // Anthropic/Google-native: NO /v1
    'model'    => env('AVALAI_DEFAULT_MODEL'),
    'timeout'  => (int) env('AVALAI_TIMEOUT', 120),
    'retries'  => 4,
    'usd_toman_rate' => env('AVALAI_USD_TOMAN_RATE'),
];
```
Register in `AppServiceProvider::register()`: `$this->app->singleton(\App\Services\AvalAI::class);` and (optional) alias `AvalAI` facade.

## 2. Client service (retry, request id, errors) — `app/Services/AvalAI.php`
```php
<?php
namespace App\Services;

use Illuminate\Http\Client\PendingRequest;
use Illuminate\Http\Client\RequestException;
use Illuminate\Http\Client\Response;
use Illuminate\Support\Facades\Http;
use Illuminate\Support\Facades\Log;

class AvalAIException extends \RuntimeException
{
    public function __construct(string $message, public readonly int $status = 0, public readonly ?string $requestId = null, public readonly ?array $body = null)
    {
        parent::__construct($message, $status);
    }
}

class AvalAI
{
    public function http(?string $base = null, int $timeout = null): PendingRequest
    {
        $key = config('avalai.key') ?: throw new AvalAIException('AVALAI_API_KEY is not configured');
        return Http::baseUrl($base ?? config('avalai.base_url'))
            ->withToken($key)
            ->acceptJson()
            ->timeout($timeout ?? config('avalai.timeout'))
            ->connectTimeout(10)
            // retry network errors, 429 and 5xx; honour Retry-After; never retry other 4xx
            ->retry(config('avalai.retries'), function (int $attempt, \Exception $e) {
                $resp = $e instanceof RequestException ? $e->response : null;
                $ra = $resp?->header('Retry-After');
                return $ra !== null && $ra !== '' ? (int) ceil((float) $ra * 1000) : min(30_000, (2 ** $attempt) * 500 + random_int(0, 500));
            }, function (\Exception $e) {
                if ($e instanceof RequestException) {
                    $s = $e->response->status();
                    return $s === 429 || $s >= 500;
                }
                return true; // ConnectionException etc.
            }, throw: false);
    }

    /** POST JSON, return decoded array + request id. */
    public function post(string $path, array $payload, ?int $timeout = null): array
    {
        $resp = $this->http(timeout: $timeout)->post($path, $payload);
        return $this->unwrap($resp, $path);
    }

    public function get(string $path, array $query = []): array
    {
        return $this->unwrap($this->http()->get($path, $query), $path);
    }

    public function unwrap(Response $resp, string $what = ''): array
    {
        $rid = $resp->header('avalai-request-id') ?: null;     // NOT x-request-id (dropped after 2026-10-15)
        if ($resp->failed()) {
            $body = $resp->json();
            Log::warning('avalai.error', ['path' => $what, 'status' => $resp->status(), 'request_id' => $rid, 'body' => $body]);
            throw new AvalAIException($body['error']['message'] ?? "HTTP {$resp->status()}", $resp->status(), $rid, is_array($body) ? $body : null);
        }
        $data = $resp->json() ?? [];
        $data['_request_id'] = $rid;
        return $data;
    }
}
```
Why `throw: false`: we map failures to our own exception carrying `request_id` for support tickets.

## 3. Chat Completions and Responses
```php
class AvalAI /* continued */
{
    public function chat(array $messages, ?string $model = null, array $extra = []): array
    {
        return $this->post('/chat/completions', ['model' => $model ?? config('avalai.model'), 'messages' => $messages] + $extra);
    }

    public function chatText(array $messages, ?string $model = null, array $extra = []): string
    {
        return $this->chat($messages, $model, $extra)['choices'][0]['message']['content'] ?? '';
    }

    /** Raw HTTP has NO output_text field — concatenate output_text parts. */
    public function responses(string|array $input, ?string $model = null, array $extra = []): array
    {
        return $this->post('/responses', ['model' => $model ?? config('avalai.model'), 'input' => $input] + $extra);
    }

    public static function outputText(array $resp): string
    {
        $t = '';
        foreach ($resp['output'] ?? [] as $item)
            foreach ($item['content'] ?? [] as $c)
                if (($c['type'] ?? '') === 'output_text') $t .= $c['text'];
        return $t;
    }
}
```
Usage: `$text = app(AvalAI::class)->chatText([['role'=>'system','content'=>'You are concise.'],['role'=>'user','content'=>'سلام']]);`
Rules: reasoning models → leave room in `max_completion_tokens`; don't send `temperature`/`top_p` to Claude Opus/Sonnet 5.x; Persian text → `JSON_UNESCAPED_UNICODE` is irrelevant with `Http` (it encodes UTF-8 correctly).

## 4. Streaming (SSE) to the browser
Server proxies the stream (key stays server-side). Controller:
```php
use Illuminate\Http\Request;
use Symfony\Component\HttpFoundation\StreamedResponse;

public function stream(Request $r, \App\Services\AvalAI $ai): StreamedResponse
{
    $payload = ['model' => config('avalai.model'), 'stream' => true,
                'stream_options' => ['include_usage' => true],
                'messages' => [['role' => 'user', 'content' => $r->string('q')->toString()]]];

    return response()->stream(function () use ($ai, $payload) {
        @ob_end_flush();
        $resp = $ai->http()->withOptions(['stream' => true])->post('/chat/completions', $payload);
        $body = $resp->toPsrResponse()->getBody();
        $buf = '';
        while (!$body->eof()) {
            $buf .= $body->read(1024);
            while (($pos = strpos($buf, "\n")) !== false) {
                $line = trim(substr($buf, 0, $pos)); $buf = substr($buf, $pos + 1);
                if (!str_starts_with($line, 'data:')) continue;
                $data = trim(substr($line, 5));
                if ($data === '[DONE]') { echo "data: [DONE]\n\n"; flush(); return; }
                $json = json_decode($data, true);
                if (isset($json['usage'])) { /* record usage: dispatch(new RecordUsage(...)) */ }
                $delta = $json['choices'][0]['delta']['content'] ?? '';
                if ($delta !== '') { echo 'data: ' . json_encode(['t' => $delta], JSON_UNESCAPED_UNICODE) . "\n\n"; flush(); }
                if (connection_aborted()) return;      // client left → stop reading
            }
        }
    }, 200, ['Content-Type' => 'text/event-stream', 'Cache-Control' => 'no-cache', 'X-Accel-Buffering' => 'no']);
}
```
nginx: `proxy_buffering off` / `X-Accel-Buffering: no`; PHP-FPM `output_buffering=0`; Octane/Cloudflare may buffer → test. Browser: `fetch('/stream?q=…')` + `ReadableStream` (EventSource can't POST). If streaming + retries matter: retry only before the first byte.

## 5. Tool calling loop (function calling)
```php
public function agent(array $messages, array $tools, array $handlers, int $maxSteps = 8, ?string $model = null): array
{
    for ($i = 0; $i < $maxSteps; $i++) {
        $res = $this->chat($messages, $model, ['tools' => $tools]);
        $msg = $res['choices'][0]['message'];
        $messages[] = $msg;                                   // keep assistant message UNCHANGED (incl. tool_calls / thinking)
        if (empty($msg['tool_calls'])) return ['messages' => $messages, 'final' => $msg['content'] ?? '', 'last' => $res];
        foreach ($msg['tool_calls'] as $call) {
            $name = $call['function']['name'];
            $args = json_decode($call['function']['arguments'] ?? '{}', true);   // model-generated: VALIDATE
            try {
                if (!isset($handlers[$name]) || !is_array($args)) throw new \InvalidArgumentException("bad tool call $name");
                $out = $handlers[$name]($args);
            } catch (\Throwable $e) { $out = ['error' => $e->getMessage()]; }
            $messages[] = ['role' => 'tool', 'tool_call_id' => $call['id'], 'content' => json_encode($out, JSON_UNESCAPED_UNICODE)];
        }
    }
    throw new AvalAIException('tool loop exceeded max steps');
}
```
Tool schema: `['type'=>'function','function'=>['name'=>'get_order','description'=>'…','parameters'=>['type'=>'object','properties'=>['id'=>['type'=>'integer']],'required'=>['id']]]]`. Side-effect tools (refund, email, delete) → require human approval (queue a pending action, don't execute inside the loop). Scope handlers to the authenticated user (never trust ids from the model).

## 6. Structured output (JSON schema)
```php
$res = $ai->chat($messages, null, ['response_format' => ['type' => 'json_schema', 'json_schema' => [
    'name' => 'invoice', 'strict' => true,
    'schema' => ['type' => 'object', 'additionalProperties' => false,
        'properties' => ['total' => ['type' => 'number'], 'currency' => ['type' => 'string']],
        'required' => ['total', 'currency']]]]]);
$data = json_decode($res['choices'][0]['message']['content'], true, flags: JSON_THROW_ON_ERROR);
// still validate with Laravel: Validator::make($data, ['total'=>'required|numeric','currency'=>'required|string|size:3'])->validate();
```
Strict mode needs `additionalProperties:false` and all keys in `required`. Model support varies → check `supports_*` flags live. Fallback for models without schema support: ask for JSON, parse, validate, retry once with the validator error.

## 7. Embeddings (+ cosine search in PHP / pgvector)
```php
$emb = $ai->post('/embeddings', ['model' => 'EMBEDDING_MODEL', 'input' => $texts]);   // list of strings, check max batch/limits
$vectors = array_map(fn ($d) => $d['embedding'], $emb['data']);
function cosine(array $a, array $b): float { $d=$na=$nb=0.0; foreach ($a as $i=>$x){ $d+=$x*$b[$i]; $na+=$x*$x; $nb+=$b[$i]*$b[$i]; } return $d/(sqrt($na)*sqrt($nb)+1e-12); }
```
Store as JSON (small corpora) or Postgres `vector` (pgvector): migration `DB::statement('CREATE EXTENSION IF NOT EXISTS vector')`, column `vector(N)`, query `ORDER BY embedding <=> ?`. AvalAI has no hosted vector store/file_search → this is the RAG pattern (see `manual-rag-with-embeddings.md`).

## 8. Images (and video)
```php
$img = $ai->post('/images/generations', ['model' => 'IMAGE_MODEL', 'prompt' => $prompt, 'size' => '1024x1024', 'n' => 1], timeout: 300);
$b64 = $img['data'][0]['b64_json'] ?? null;            // or ['url'] depending on model
\Storage::disk('public')->put("ai/".uniqid().".png", base64_decode($b64, true));
// edits: multipart
$edit = $ai->http(timeout: 300)->asMultipart()
    ->attach('image', fopen($path, 'r'), 'in.png')
    ->post('/images/edits', ['model' => 'IMAGE_MODEL', 'prompt' => 'Change only the background']);
```
Gemini image models via chat: `modalities:["image","text"]`, image arrives as data URL in `choices[0].message.images[0].image_url.url` (see `nano-banana-image-generation.md`). Removed: Imagen, Sora/Videos API; check ids live.

## 9. Audio
```php
// STT (multipart). Verify the STT model live (old whisper-1/gpt-4o-*transcribe are being retired).
$t = $ai->http(timeout: 300)->asMultipart()->attach('file', fopen($wav, 'r'), 'a.wav')
        ->post('/audio/transcriptions', ['model' => 'STT_MODEL', 'language' => 'fa', 'response_format' => 'json'])->json('text');
// TTS: binary body (NOT JSON) — check status + content-type
$r = $ai->http(timeout: 300)->post('/audio/speech', ['model' => 'TTS_MODEL', 'voice' => 'alloy', 'input' => 'سلام', 'response_format' => 'mp3']);
abort_if($r->failed(), 502); \Storage::put('tts.mp3', $r->body());
```
Gemini 3.8 TTS: `voice` is an object `{"name":"Zephyr","languageCode":"fa-IR"}`; Chat route returns base64 PCM16 24 kHz (needs ffmpeg → wav/mp3).

## 10. Files, OCR, PDF
```php
$f = $ai->http()->asMultipart()->attach('file', fopen($pdf, 'r'), 'doc.pdf')->post('/files', ['purpose' => 'user_data'])->json();   // beta; set expires_after for sensitive docs
$res = $ai->chat([['role'=>'user','content'=>[['type'=>'text','text'=>'Summarize'],['type'=>'file','file'=>['file_id'=>$f['id']]]]]]);
// or inline base64 (≈ +33% size): ['type'=>'file','file'=>['filename'=>'doc.pdf','file_data'=>'data:application/pdf;base64,'.base64_encode(file_get_contents($pdf))]]
$ai->http()->delete("/files/{$f['id']}");              // clean up
```
OCR: Mistral OCR uses `/v1/ocr`-style route/`server_url` without `/v1` in the Mistral SDK — see `mistral-ocr-document-processing.md` for exact body; call with `$ai->post('/ocr', [...])` after verifying the body in the API reference.

## 11. Search API
```php
$s = $ai->post('/search/perplexity-search', ['query' => 'latest Laravel release', 'max_results' => 5, 'search_domain_filter' => ['laravel.com'], 'country' => 'US']);
foreach ($s['results'] as $r) echo "{$r['title']} {$r['url']}\n";
```
Per-query price $0.003–$0.025 (see `news/2025-10-26-search-api-launched.md`).

## 12. Claude native Messages (thinking, caching, large context)
```php
$m = $ai->http(base: config('avalai.native_url').'/v1')   // pass the ?string base explicitly
    ->withHeaders(['x-api-key' => config('avalai.key'), 'anthropic-version' => '2023-06-01'])
    ->withToken('')                                          // replace default Bearer
    ->post('/messages', ['model' => 'claude-sonnet-5-5', 'max_tokens' => 4096,
        'thinking' => ['type' => 'adaptive'], 'output_config' => ['effort' => 'high'],
        'messages' => [['role' => 'user', 'content' => 'Review this migration plan']]])->json();
$text = collect($m['content'])->where('type', 'text')->pluck('text')->implode('');
```
(`/v1/messages` also works with the Bearer header on AvalAI; keep full assistant content incl. thinking blocks for multi-turn. No `temperature/top_p/prefill/forced tool_choice` on Opus/Sonnet 5.x.)

## 13. Cost tracking — DB + exact billing via User API
Migration:
```php
Schema::create('ai_calls', function (Blueprint $t) {
    $t->id(); $t->foreignId('user_id')->nullable()->index();
    $t->string('feature')->index(); $t->string('model');
    $t->string('request_id')->nullable()->unique();          // avalai-request-id
    $t->unsignedInteger('prompt_tokens')->default(0); $t->unsignedInteger('completion_tokens')->default(0);
    $t->unsignedInteger('cached_tokens')->default(0); $t->unsignedInteger('reasoning_tokens')->default(0);
    $t->decimal('est_usd', 12, 6)->nullable();               // from estimated_cost.unit (NOT guaranteed)
    $t->decimal('exact_usd', 12, 6)->nullable();             // from User API lookup (cost.unit)
    $t->timestamp('reconciled_at')->nullable(); $t->timestamps();
});
```
Record after each call: `usage.prompt_tokens`, `completion_tokens`, `prompt_tokens_details.cached_tokens`, `completion_tokens_details.reasoning_tokens`, `estimated_cost.unit`, `_request_id`. Tag requests with `'safety_identifier' => 'user-'.$user->id` (per-user attribution + abuse tracing).
Reconcile job (schedule every 5 min; lookup is ready ≈30 s later, ≤1000 ids per call):
```php
class ReconcileAiCosts implements ShouldQueue {
    use Dispatchable, Queueable;
    public function handle(\App\Services\AvalAI $ai): void {
        \App\Models\AiCall::whereNull('reconciled_at')->where('created_at', '<', now()->subMinute())
            ->whereNotNull('request_id')->chunkById(500, function ($rows) use ($ai) {
                $res = $ai->http(base: 'https://api.avalai.ir/user/v1')->post('/transactions/lookup', ['transaction_ids' => $rows->pluck('request_id')->all()])->json();
                $by = collect($res['transactions'] ?? [])->keyBy('id');
                foreach ($rows as $r) if ($t = $by->get($r->request_id)) {
                    $r->update(['exact_usd' => $t['cost']['unit'], 'reconciled_at' => now()]);
                }
            });
    }
}
```
Estimate before sending: run `scripts/avalai_live.py cost …` offline or port its logic: long-context tier applies to the whole request when input > threshold; reasoning tokens bill at output rate; toman = USD × today's rate. Budget guard: per-user daily cap checked before each call (sum `COALESCE(exact_usd, est_usd)` for today); refuse/queue when exceeded.

## 14. Tests (no network) — `Http::fake`
```php
public function test_chat_text_and_request_id(): void
{
    Http::fake(['api.avalai.ir/v1/chat/completions' => Http::response(
        ['choices' => [['message' => ['role' => 'assistant', 'content' => 'hi']]], 'usage' => ['prompt_tokens' => 1, 'completion_tokens' => 1]],
        200, ['avalai-request-id' => 'rid-1'])]);
    config(['avalai.key' => 'test']);
    $r = app(AvalAI::class)->chat([['role' => 'user', 'content' => 'x']], 'm');
    $this->assertSame('rid-1', $r['_request_id']);
    Http::assertSent(fn ($req) => $req->hasHeader('Authorization', 'Bearer test') && $req['model'] === 'm');
}
public function test_retries_on_429_then_succeeds(): void
{
    Http::fake(['*' => Http::sequence()->push(['error' => ['message' => 'rate']], 429, ['Retry-After' => '0'])->push(['choices' => [['message' => ['content' => 'ok']]]], 200)]);
    $this->assertSame('ok', app(AvalAI::class)->chatText([['role' => 'user', 'content' => 'x']], 'm'));
}
public function test_error_carries_request_id(): void
{
    Http::fake(['*' => Http::response(['error' => ['message' => 'bad']], 400, ['avalai-request-id' => 'rid-9'])]);
    try { app(AvalAI::class)->chat([['role'=>'user','content'=>'x']], 'm'); $this->fail(); }
    catch (AvalAIException $e) { $this->assertSame('rid-9', $e->requestId); $this->assertSame(400, $e->status); }
}
```
In CI never call the real API; one nightly smoke test with a tiny prompt and a dedicated key.

## 15. Queues, rate limits, concurrency
- Long/batch work → queued job (`public $timeout = 900; public $tries = 3; public function backoff(): array { return [10, 30, 90]; }`).
- Respect per-model RPM/TPM of **your tier** (`avalai_live.py price MODEL`): job middleware `Illuminate\Queue\Middleware\RateLimited('avalai')` with `RateLimiter::for('avalai', fn () => Limit::perMinute($rpm * 0.6))`; for TPM use a Redis token bucket keyed by model. Target ≤ 50–75% of the limit.
- On 429 inside a job: `$this->release($retryAfter)` instead of sleeping the worker. Use `ShouldBeUnique` for idempotent jobs; store an idempotency key per business operation (avoid double billing on retries).
- Parallel fan-out: `Http::pool(fn ($pool) => [...])` — cap concurrency (chunks of N) so you don't self-DDoS your tier. Flex tier (`service_tier:"flex"`): timeout 900 s, not covered by credit packages, fall back to default on failure.

## 16. Security / ops checklist (Laravel)
- Key only in `.env`/secret manager; `config:cache` in prod; never expose via `config()` in views/Inertia shared props; rotate on leak.
- Authorize every AI endpoint (policies/gates), throttle per user (`throttle:30,1`) + budget cap; log `request_id`, user id, model, tokens (not prompts if sensitive; AvalAI says it doesn't store content, upstream providers have own policies).
- Treat model output as untrusted: escape in Blade (`{{ }}`), never `eval`/SQL-concat/`shell_exec` model text; validate tool args; human approval for side effects; prompt-injection defence for retrieved/web content.
- Handle `AvalAIException` → user-friendly Persian message; show request id to support.
- Monitoring: status page https://status.avalai.ir, alert on error rate and daily cost; circuit breaker (cache flag) on repeated 5xx; fallback model from another provider.
- Remember: model ids deprecate (see `10-deprecations.md`) — keep model names in config, not code; run `avalai:check-models` (below) in CI/cron.

## 17. Artisan commands
```php
// php artisan make:command AvalaiCheckModels
protected $signature = 'avalai:check-models {ids*}';
public function handle(): int {
    $models = collect(Http::acceptJson()->get('https://api.avalai.ir/public/models')->json('data'))->keyBy('id');   // no key needed
    $bad = 0;
    foreach ($this->argument('ids') as $id) {
        $m = $models->get($id);
        if (!$m) { $this->error("$id MISSING (deprecated/renamed)"); $bad = 1; continue; }
        $this->info("$id OK min_tier={$m['min_tier']} in={$m['pricing']['input']} out={$m['pricing']['output']} USD/1M");
    }
    return $bad;
}
```
Wire it into CI: `php artisan avalai:check-models $(grep -o "AVALAI_[A-Z_]*MODEL=.*" .env.example | cut -d= -f2)`.

See also: `php-official-samples.md` (docs' own PHP blocks, verbatim, flagged), `multi-language-clients.md`, `rate-limit-safe-parallel-requests.md`, `guides/error-handling.md`, `guides/production-best-practices.md`.
