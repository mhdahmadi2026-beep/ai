# Starter: chat inside Laravel 11 (Blade + SSE)

Prereq: service class from `examples/laravel-complete-guide.md` §1–2 and §4 (streaming). Files:
`routes/web.php`
```php
Route::middleware(['auth', 'throttle:20,1'])->group(function () {
    Route::view('/chat', 'chat');
    Route::post('/chat/stream', [ChatController::class, 'stream']);
});
```
`app/Http/Controllers/ChatController.php` (uses the SSE controller from the guide; essentials)
```php
public function stream(Request $r, \App\Services\AvalAI $ai) {
    $data = $r->validate(['message' => 'required|string|max:4000']);
    abort_if($this->overBudget($r->user()), 429, 'سهمیه‌ی امروز تمام شد');
    $history = cache()->get("chat:{$r->user()->id}", []);
    $history[] = ['role' => 'user', 'content' => $data['message']];
    $payload = ['model' => config('avalai.model'), 'stream' => true, 'stream_options' => ['include_usage' => true],
                'safety_identifier' => 'user-'.$r->user()->id,
                'messages' => array_merge([['role' => 'system', 'content' => 'پاسخ‌ها را کوتاه و به زبان کاربر بده.']], array_slice($history, -12))];
    // …same response()->stream loop as the guide; accumulate $answer; on finish:
    // $history[] = ['role'=>'assistant','content'=>$answer]; cache()->put("chat:{$id}", $history, 3600); record usage in ai_calls.
}
```
`resources/views/chat.blade.php`
```blade
<div id="log" dir="auto"></div>
<form id="f"><input id="q" autocomplete="off" required><button>ارسال</button></form>
<script>
const log = document.getElementById('log');
document.getElementById('f').addEventListener('submit', async (e) => {
  e.preventDefault(); const q = document.getElementById('q').value; document.getElementById('q').value = '';
  const p = document.createElement('p'); p.textContent = '🧑 ' + q; log.append(p);
  const a = document.createElement('p'); a.textContent = '🤖 '; log.append(a);          // textContent = XSS-safe
  const res = await fetch('/chat/stream', { method: 'POST', headers: { 'Content-Type': 'application/json', 'X-CSRF-TOKEN': '{{ csrf_token() }}' }, body: JSON.stringify({ message: q }) });
  const rd = res.body.getReader(), dec = new TextDecoder(); let buf = '';
  for (;;) { const { done, value } = await rd.read(); if (done) break; buf += dec.decode(value, { stream: true });
    for (let i; (i = buf.indexOf('\n\n')) >= 0;) { const l = buf.slice(0, i).trim(); buf = buf.slice(i + 2);
      if (l.startsWith('data:') && l.slice(5).trim() !== '[DONE]') { const j = JSON.parse(l.slice(5)); if (j.t) a.textContent += j.t; } } }
});
</script>
```
Checklist: policies/gates for who may chat · queue long jobs · persist conversations (messages table) instead of cache for audit · moderation on user input if public · cost cap per user (`ai_calls` table in the guide) · Persian digits/RTL via `dir="auto"` · nginx `proxy_buffering off`.
