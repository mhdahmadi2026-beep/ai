# News 2026-08-16 (1405-05-25): `x-request-id` → `avalai-request-id` (docs.avalai.ir/fa/news/2026-08-16-avalai-request-id-header-migration)

- CDNs may overwrite `x-request-id`, making cost lookup/support traces ambiguous → AvalAI now returns dedicated response header **`avalai-request-id`** (same UUID v7; works with `/user/v1/transactions/lookup`; matches body `request_id` e.g. Videos API).
- Transition: both headers returned (same value) **2026-08-16 → 2026-10-15 (1405-07-23)**; afterwards only `avalai-request-id`, and any `x-request-id` may belong to the CDN. **Deadline is 8 days after 2026-10-07 — update code now.**
- Request header `X-Client-Request-Id` and body `request_id` unchanged.
- Python: `r.headers.get("avalai-request-id")`; fallback `or r.headers.get("x-request-id")` only until the deadline. OpenAI SDK: `client.chat.completions.with_raw_response.create(...)` → `raw.headers.get("avalai-request-id")`, `raw.parse()`.
- Rate-limit headers seen: `x-ratelimit-{limit,remaining,reset}-{requests,tokens}` (reset like `50s`). Full reference: fa/api-reference/response-headers.
- Source note: page's JS example's "new header" and fallback variables are inconsistent but harmless.
