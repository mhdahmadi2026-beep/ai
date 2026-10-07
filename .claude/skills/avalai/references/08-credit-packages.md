# بسته‌های اعتباری / Credit Packages — https://docs.avalai.ir/fa/credit-packages

Support: https://t.me/AvalAISupport · Billing support: https://avalai.ir/contact-us-avalai
Live catalog API (source of the table): https://chat.avalai.ir/pay/data/credit-packages/templates/ · store: https://chat.avalai.ir/platform/billing/packages (marketplace view: `?marketplace`). **Always check live availability before recommending a package.**
Snapshot: 8 Mehr 1405 (2026-09-30 12:23 UTC): **29 available, 9 historical/unavailable**.

## What they are
Prepaid API credit packages for OpenAI, Gemini, Alibaba and top coding models: you pay X Toman, receive more credit value (e.g. pay 350,000 → get 500,000 Toman credit ≈ +25%… per page example), usable **only for specific models** and **within a limited period**. Current packages give **20%–40% discount**. API-focused only (no subscription services).

### Who should buy
- **New users: no need** — just top up the default account balance and use services directly (full model flexibility, no time limit).
- **Professional/enterprise users** with predictable usage, repeated use of specific models, wanting discounts, able to consume credit within a limited window. Validity currently **1 to 31 days**.

### Critical warnings
- **Positive overall balance required.** If the default account balance is zero/negative, API services are **disabled automatically**. Keep **≥ 100,000 Toman** in overall balance.
- **Flex tier is NOT covered** — `service_tier: "flex"` is charged from the standard balance; packages apply only to the standard tier (`default` / unspecified). (see 07-service-tiers)

### Package structure
Amount paid · credit value · value ratio (% extra) · scope (models/services) · validity period · per-user purchase cap.
- Scope: usage outside scope is billed at **standard rates, no discount**. Mixed use: credit consumed by model coverage. **Package credit is consumed before the general balance**, but the general balance must still stay positive.
- Validity fixed at **1, 7, 30 or 31 days**; credit auto-expires at end (no grace, effective exactly at end). Non-transferable between accounts/packages; expired packages can't be renewed; no pre-purchase/reservation of a package to start after the current one ends.
- **One active package per template ID** when card says "cap 1 purchase per user" (e.g. while `d-g3050s` is active you can't buy another `d-g3050s`). Packages of different types/template IDs can be held simultaneously. Cards saying "cap 2" allow up to two active of that type.
- Packages are bound to the buyer's account.

## Package catalog (template id → pay → receive, validity, discount)
Amounts in Toman. "Cap 1" = max 1 active per user unless noted.

### Gemini packages (selected Gemini)
| Name | ID | Pay | Receive | Valid | Discount |
|---|---|---:|---:|---|---|
| Daily basic | `d-g3050s` | 300,000 | 500,000 | 1 d | 40% |
| Daily professional | `d-g6010m` | 600,000 | 1,000,000 | 1 d | 40% |
| Daily enterprise | `d-g3550l` | 3,500,000 | 5,000,000 | 1 d | 30% |
| Weekly basic | `w-g1420s` | 1,400,000 | 2,000,000 | 7 d | 30% |
| Weekly professional | `w-g3550m` | 3,500,000 | 5,000,000 | 7 d | 30% |
| Weekly enterprise | `w-g7010l` | 7,000,000 | 10,000,000 | 7 d | 30% |
| Monthly | `m-g8010m` | 8,000,000 | 10,000,000 | 30 d | 20% |
| Monthly enterprise | `m-g5070l` | 50,000,000 | 70,000,000 | 30 d | 28.57% |
**Covered models:** gemini-3.8-flash, gemini-3.7-flash, gemini-3.6-flash, gemini-3.5-flash, gemini-3.5-flash-lite, gemini-3.1-flash-lite-image, gemini-3.1-flash-image, gemini-3.1-pro-preview, gemini-3.1-flash-lite

### Vibe Coder packages
| Name | ID | Pay | Receive | Valid | Discount |
|---|---|---:|---:|---|---|
| Daily basic | `d-b3550s` | 300,000 | 500,000 | 1 d | 40% |
| Daily professional | `d-b1420m` | 1,200,000 | 2,000,000 | 1 d | 40% |
| Daily enterprise | `d-b3550l` | 3,000,000 | 5,000,000 | 1 d | 40% |
| Weekly basic | `w-b8010s` | 700,000 | 1,000,000 | 7 d | 30% |
| Weekly professional | `w-b1620m` | 1,400,000 | 2,000,000 | 7 d | 30% |
| "Monthly enterprise" (listed under weekly; id `m-b5070l`; **validity printed 7 d**) | `m-b5070l` | 50,000,000 | 70,000,000 | 7 d (as printed) | 28.57% |
| Weekly enterprise | `w-b4050l` | 3,500,000 | 5,000,000 | 7 d | 30% |
**Covered models:** gpt-6.1-sol, gpt-6-astra, gpt-6-sol, gpt-6-luna, deepseek-v4.1-flash, glm-5.3, qwen3.8-max, kimi-k3, claude-opus-5, claude-sonnet-5, gpt-5.6-sol, glm-5.3-flash, glm-5.2, minimax-m3, nemotron-3-ultra, kimi-k2.6, nemotron-3.5-lightning, muse-glimmer-30b

### OpenAI packages (selected OpenAI)
| Name | ID | Pay | Receive | Valid | Discount |
|---|---|---:|---:|---|---|
| Daily basic | `d-o3050s` | 300,000 | 500,000 | 1 d | 40% |
| Daily professional | `d-o6010m` | 600,000 | 1,000,000 | 1 d | 40% |
| Daily enterprise | `d-o3550l` | 3,500,000 | 5,000,000 | 1 d | 30% |
| Weekly basic | `w-o1420s` | 1,400,000 | 2,000,000 | 7 d | 30% |
| Weekly enterprise | `w-o7010l` | 7,000,000 | 10,000,000 | 7 d | 30% |
| Monthly enterprise | `m-o5070l` | 50,000,000 | 70,000,000 | 30 d | 28.57% |
**Covered models:** gpt-6.1-sol, gpt-6-sol, gpt-6-luna, gpt-5.6-sol, gpt-5.6-terra, gpt-5.6-luna, gpt-5.5, gpt-image-2, gpt-5.4, gpt-5.4-mini, gpt-5.4-nano, gpt-5.3-codex, text-embedding-3-large, text-embedding-3-small

### Alibaba packages (selected Alibaba)
| Name | ID | Pay | Receive | Valid | Discount |
|---|---|---:|---:|---|---|
| Daily basic | `d-a3550s` | 350,000 | 500,000 | 1 d | 30% |
| Daily professional | `d-a7010m` | 700,000 | 1,000,000 | 1 d | 30% |
| Daily enterprise | `d-a3550l` | 3,500,000 | 5,000,000 | 1 d | 30% |
| Weekly basic | `w-a1620s` | 1,600,000 | 2,000,000 | 7 d | 20% |
| Weekly professional | `w-a4050m` | 4,000,000 | 5,000,000 | 7 d | 20% |
| Weekly enterprise | `w-a8010l` | 8,000,000 | 10,000,000 | 7 d | 20% |
| Monthly enterprise | `m-a5062l` | 50,000,000 | 62,500,000 | 30 d | 20% |
**Covered models:** qwen3.8-max, qwen3.6-flash, qwen3.6-35b-a3b, qwen3.6-27b, qwen3.5-flash, qwen3-coder-next, qwen3.5-27b, qwen3.5-35b-a3b, qwen3.5-122b-a10b, qwen3.5-397b-a17b, qwen3.5-plus, qwen3-max, qwen3-next-80b-a3b-thinking, qwen3-next-80b-a3b-instruct, qwen3-coder-flash, qwen3-coder-plus, qwen3-coder-480b-a35b-instruct, qwen3-235b-a22b-instruct-2507, qwen3-235b-a22b, qwen3-32b, qwen3-30b-a3b, qwen3-30b-a3b-instruct-2507, qwen3-30b-a3b-thinking-2507, qwen3-14b, qwen3-8b, qwen3-4b, qwen3-vl-32b-instruct, qwen3-vl-flash, qwen3-vl-plus, qwen-flash, qwen-plus, qwen-image-edit, qwen-image-plus, qwen-image-edit-plus, qwen-mt-flash, qwen-mt-lite, qwen-mt-plus, text-embedding-v4, text-embedding-v3

### Special Enterprise — "منتخب OpenAI سازمانی ویژه" (AVAILABLE)
`m-o1013xl`: pay **999,999,999** → receive **1,350,000,000** Toman; **31 days**; **cap 2 purchases per user**; discount 25.93%. Covered: same 14 OpenAI models as the OpenAI packages above.

### UNAVAILABLE / historical (kept for reference only; not purchasable)
**Claude (Anthropic)** — last pay → credit, validity 1/7/30 d:
- `historical-claude-daily-basic`: 350,000 → 500,000 (1 d) · `historical-claude-daily-professional`: 700,000 → 1,000,000 (1 d) · `historical-claude-daily-enterprise`: 3,500,000 → 5,000,000 (1 d)
- `historical-claude-weekly-basic`: 1,600,000 → 2,000,000 (7 d) · `…-weekly-professional`: 4,000,000 → 5,000,000 (7 d) · `…-weekly-enterprise`: 8,000,000 → 10,000,000 (7 d)
- `historical-claude-monthly-enterprise`: 50,000,000 → 62,500,000 (30 d)
- Historical covered models: claude-opus-4-5, claude-opus-4-1, claude-sonnet-4-5, claude-haiku-4-5, anthropic.claude-opus-4-1-20250805-v1:0, anthropic.claude-sonnet-4-5-20250929-v1:0, anthropic.claude-haiku-4-5-20251001-v1:0, anthropic.claude-opus-4-20250514-v1:0, anthropic.claude-sonnet-4-20250514-v1:0, anthropic.claude-3-7-sonnet-20250219-v1:0
**Web search monthly enterprise** `m-ws5062l`: 50,000,000 → 62,500,000 (30 d); covered: perplexity-search.
**Special Enterprise XL (historical)** `m-s1011xl`: 999,999,999 → 1,100,000,000 (31 d). Historical covered: gemini-2.5-flash-image, gemini-2.5-pro, gemini-2.5-flash, gemini-2.5-flash-lite, gemini-2.5-flash-image-preview, gemini-2.0-flash, gemini-2.0-flash-lite, gpt-5-chat, gpt-5-mini, gpt-5-nano, o4-mini, o3-mini, gpt-4.1, gpt-4.1-mini, gpt-4.1-nano, gpt-4o, gpt-4o-mini, gpt-4o-transcribe, gpt-4o-mini-transcribe, gpt-4o-mini-tts, perplexity-search, google_pse-search.
⚠ Note: there are currently **no Claude/Anthropic packages available**.

## Buying
Prereqs: logged in; pay by bank card or existing wallet balance; one-time OTP (6-digit SMS) to confirm.
Steps: browse https://chat.avalai.ir/platform/billing/packages?marketplace → choose package & quantity → payment method → OTP → package added immediately.

## Managing
Package dashboard (same URL): active/expired packages, usage stats, expiry timeline, remaining credit. Statuses: **active, expired, exhausted, promotional**. Tracking: live balance, usage analytics, per-model breakdown, expiry alerts.

## Conditional cancellation → wallet refund policy
Cancellation allowed only if ALL true at final confirmation:
- request made strictly before `purchased_at + 24 hours`;
- consumed credit ≤ **5.00%** of nominal package credit (exactly 5.00% allowed);
- package active, not previously cancelled, linked to a confirmed `Payment` with positive `paid_amount` and positive `allocated_paid_amount`;
- wallet-return amount positive (manual/promotional packages without Payment allocation are ineligible).
Formulas: `consumed_irt = amount_irt - remaining_irt` · `wallet_return = allocated_paid_amount - consumed_irt`.
Needs a one-time code via SMS (verified email only if SMS unavailable). On confirm: conditions re-checked with locks; package deactivated, remaining credit removed, only `wallet_return` added to `Credit.remaining_irt`. **This is an account-credit adjustment, never a bank refund.** Expired or ineligible packages can't be cancelled.

## Best practices
Choose: analyze usage patterns → compute value vs standard rates → check validity fits your consumption window → confirm package covers your models. Maximize: use package credit first on high-use/high-value models; track expiry; batch heavy work inside validity; prefer covered models.

## Troubleshooting
- Package not appearing: re-check payment completion & OTP; check account verification; contact support if paid but missing.
- Credits not applied: ensure model is in scope; package still valid; credit not exhausted.
- Payment issues: enough wallet balance / card funds; complete OTP.
- Sudden service cutoff: check overall balance is positive (≥100,000 Toman recommended); top up → services re-enable automatically.

### Verify whether a request used package credit
Use `avalai-request-id` with the transaction lookup API:
```bash
curl https://api.avalai.ir/user/v1/transactions/lookup \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer $AVALAI_API_KEY" \
  -d '{
    "transaction_ids": ["YOUR-REQUEST-ID"]
  }'
```
Response example:
```json
{
  "transactions": [
    {
      "id": "019b4a90-bfed-7cc1-97c1-7abcc10e7e75",
      "model": "qwen3-max",
      "cost": {
        "unit": "0.00007800",
        "paid_unit": "0.00007800",
        "paid_irt": "0",
        "paid_grant_irt": "10.35",
        "source": "credit_package",
        "currency": "UNIT"
      },
      "packages": [
        {
          "id": "7794",
          "template_id": "d-a3550s",
          "name": "منتخب Alibaba روزانه پایه",
          "remaining_irt": "499507.15",
          "end_date": "2025-12-24T09:24:02.705Z"
        }
      ]
    }
  ]
}
```
| Field | Meaning |
|---|---|
| `cost.source` | `"credit_package"` if a package was used; `"balance"` if deducted from overall balance |
| `cost.paid_irt` | amount deducted from overall balance (0 if package covered it) |
| `cost.paid_grant_irt` | amount deducted from the credit package |
| `packages` | active package details used |
| `packages[].remaining_irt` | remaining package balance |
| `packages[].end_date` | package expiry time |
Dashboard CSV: https://chat.avalai.ir/platform/usage/reports → choose range → generate **CSV report** (cost source, package info, billing details) — for auditing, monthly reconciliation, accounting export, usage analysis.

## Related
/fa/pricing · /fa/api-reference/user · /fa/resellers/cost-tracking-guide · /fa/api-reference/authentication · /fa/guides/rate-limits · billing support https://avalai.ir/contact-us-avalai

## ⚠ Notes on source inconsistencies
- Page example says pay 350,000 → receive 500,000 "≈25% more"; actual ratio (500/350) is ~42.9% more credit = 30% discount. Discount % on cards = (credit − pay)/credit.
- "Vibe Coder monthly enterprise" `m-b5070l` is listed under the weekly group with validity 7 d, but its ID prefix `m-` suggests monthly; verify live.
- Page says validity "1 to 31 days" in one place and "1, 7, 30 or 31" in another (consistent).
