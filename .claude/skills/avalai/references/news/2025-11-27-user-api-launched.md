# News 2025-11-27 (1404-09-06): User API (docs.avalai.ir/fa/news/2025-11-27-user-api-launched)

Base `https://api.avalai.ir/user/v1` (Bearer key). Exact cost within ~30 s of a call (response `estimated_cost` is NOT guaranteed → don't bill from it).
- `GET /transactions` (filters: model, provider, created_after, safety_identifier, limit; returns total/page/page_size/has_more), `POST /transactions/lookup` body `{"transaction_ids":[…≤1000]}` → `transactions[]`, `summary{requested,found,not_found_ids}`, `GET /transactions/summary?group_by=day|…` (breakdown, by_model/provider/safety_identifier/api_key), `GET /health`.
- Transaction id = request id: originally header `x-request-id`; **now use `avalai-request-id` (x-request-id dropped after 2026-10-15)**.
- Tag requests with `safety_identifier` (e.g. `customer-12345`) for per-customer/department attribution and filter on it later.
- Transaction record: tokens (prompt/completion/reasoning/cached + details), `cost{unit,paid_unit,paid_irt,paid_grant_irt,source,currency}`, `grants`, `packages` (credit package remaining/scope), `api_key_suffix`, `ip_address`.
- **Source defect:** all Python/JS samples read `cost.total_cost_usd`, which is NOT in the documented response (fields are `cost.unit` etc.); also `response.headers` doesn't exist on an OpenAI SDK object (use `with_raw_response`). Parse `cost.unit` (USD) after verifying a real response.
- Reseller flow: call → store request id with customer → wait ≥30 s → lookup → bill.
