# Starter: Next.js (App Router) streaming chat — key stays on the server

`.env.local`: `AVALAI_API_KEY=...` · `AVALAI_MODEL=<chat model id>`  (never prefix with `NEXT_PUBLIC_`).
`app/api/chat/route.ts`
```ts
import OpenAI from "openai";
export const runtime = "nodejs";
const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY!, baseURL: "https://api.avalai.ir/v1", timeout: 120_000, maxRetries: 3 });

export async function POST(req: Request) {
  const { messages } = await req.json();
  if (!Array.isArray(messages) || messages.length > 40) return new Response("bad request", { status: 400 });
  // TODO: authenticate user + per-user rate limit + budget check here
  const stream = await client.chat.completions.create({
    model: process.env.AVALAI_MODEL!, stream: true, stream_options: { include_usage: true },
    messages: [{ role: "system", content: "You are a helpful assistant. Reply in the user's language." }, ...messages],
  });
  const enc = new TextEncoder();
  return new Response(new ReadableStream({
    async start(ctrl) {
      try {
        for await (const ev of stream) {
          const t = ev.choices?.[0]?.delta?.content;
          if (t) ctrl.enqueue(enc.encode(`data: ${JSON.stringify({ t })}\n\n`));
          if (ev.usage) console.log("usage", ev.usage);           // persist for cost tracking
        }
        ctrl.enqueue(enc.encode("data: [DONE]\n\n"));
      } catch (e) { ctrl.enqueue(enc.encode(`data: ${JSON.stringify({ error: "upstream error" })}\n\n`)); }
      finally { ctrl.close(); }
    },
    cancel() { stream.controller.abort(); },                        // client left → stop paying
  }), { headers: { "Content-Type": "text/event-stream", "Cache-Control": "no-cache, no-transform", "X-Accel-Buffering": "no" } });
}
```
`app/page.tsx` (client)
```tsx
"use client";
import { useState } from "react";
export default function Chat() {
  const [msgs, setMsgs] = useState<{ role: string; content: string }[]>([]);
  const [input, setInput] = useState("");
  async function send() {
    const next = [...msgs, { role: "user", content: input }, { role: "assistant", content: "" }];
    setMsgs(next); setInput("");
    const res = await fetch("/api/chat", { method: "POST", headers: { "Content-Type": "application/json" }, body: JSON.stringify({ messages: next.slice(0, -1) }) });
    const reader = res.body!.getReader(), dec = new TextDecoder(); let buf = "";
    for (;;) {
      const { done, value } = await reader.read(); if (done) break;
      buf += dec.decode(value, { stream: true });
      for (let i; (i = buf.indexOf("\n\n")) >= 0; ) {
        const line = buf.slice(0, i).trim(); buf = buf.slice(i + 2);
        if (!line.startsWith("data:")) continue;
        const d = line.slice(5).trim(); if (d === "[DONE]") return;
        const { t } = JSON.parse(d); if (t) setMsgs((m) => { const c = [...m]; c[c.length - 1] = { ...c[c.length - 1], content: c[c.length - 1].content + t }; return c; });
      }
    }
  }
  return (<main dir="auto" style={{ maxWidth: 720, margin: "2rem auto" }}>
    {msgs.map((m, i) => <p key={i}><b>{m.role}:</b> {m.content}</p>)}
    <input value={input} onChange={(e) => setInput(e.target.value)} onKeyDown={(e) => e.key === "Enter" && send()} style={{ width: "100%" }} />
  </main>);
}
```
Deploy notes: Vercel/edge may buffer — use Node runtime; behind nginx set `proxy_buffering off`. Add Zod validation, auth (NextAuth), Upstash rate limit, and render model output as text/escaped markdown (never `dangerouslySetInnerHTML`).
