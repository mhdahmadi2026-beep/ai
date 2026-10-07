# Starter: Node/TS agent CLI with tools + approval gate

`npm i openai zod` · `.env`: `AVALAI_API_KEY`, `AVALAI_MODEL`
```ts
import OpenAI from "openai";
import { z } from "zod";
import * as readline from "node:readline/promises";
import { readFile } from "node:fs/promises";
const client = new OpenAI({ apiKey: process.env.AVALAI_API_KEY!, baseURL: "https://api.avalai.ir/v1", timeout: 120_000 });
const rl = readline.createInterface({ input: process.stdin, output: process.stdout });

const tools = [
  { type: "function" as const, function: { name: "read_file", description: "Read a UTF-8 text file inside ./workspace", strict: true,
    parameters: { type: "object", properties: { path: { type: "string" } }, required: ["path"], additionalProperties: false } } },
  { type: "function" as const, function: { name: "delete_file", description: "Delete a file inside ./workspace (needs human approval)", strict: true,
    parameters: { type: "object", properties: { path: { type: "string" } }, required: ["path"], additionalProperties: false } } },
];
const Path = z.object({ path: z.string().regex(/^[\w\-./]+$/).refine((p) => !p.includes("..")) });

const handlers: Record<string, (a: unknown) => Promise<unknown>> = {
  read_file: async (a) => ({ ok: true, data: (await readFile(`workspace/${Path.parse(a).path}`, "utf8")).slice(0, 20000) }),
  delete_file: async (a) => {
    const { path } = Path.parse(a);
    if ((await rl.question(`DELETE workspace/${path}? [y/N] `)).toLowerCase() !== "y") return { ok: false, error_code: "denied_by_user" };
    // await unlink(`workspace/${path}`)  ← enable deliberately
    return { ok: true };
  },
};

async function run(goal: string) {
  const messages: any[] = [{ role: "system", content: "You are a careful file assistant. Use tools; never guess file contents." }, { role: "user", content: goal }];
  for (let step = 0; step < 8; step++) {
    const r = await client.chat.completions.create({ model: process.env.AVALAI_MODEL!, messages, tools, parallel_tool_calls: false });
    const msg = r.choices[0].message; messages.push(msg);               // keep assistant msg unchanged
    if (!msg.tool_calls?.length) return msg.content;
    for (const c of msg.tool_calls) {
      let out: unknown;
      try { out = await handlers[c.function.name](JSON.parse(c.function.arguments)); }
      catch (e: any) { out = { ok: false, error_code: "bad_call", message: String(e.message).slice(0, 200) }; }
      messages.push({ role: "tool", tool_call_id: c.id, content: JSON.stringify(out) });
    }
  }
  throw new Error("max steps exceeded");
}
console.log(await run(process.argv.slice(2).join(" ") || "Summarize workspace/README.md"));
rl.close();
```
Principles shown: strict schemas, server-side validation (zod), path-traversal guard, approval for destructive actions, step cap, structured tool errors (`{ok:false,error_code}`), `parallel_tool_calls:false` for ordered side effects. Responses API variant: `examples/reasoning-function-calls.md`.
