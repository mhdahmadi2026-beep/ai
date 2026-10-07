# AvalAI privacy policy (docs.avalai.ir/fa/safety/privacy-policy) — last changed 12 Mordad 1405 (≈ 2026-08-03)

Covers ALL services (chat platform + developer APIs). Companion: guides/content-policy.md (API content), guides/data-controls.md (per-route retention). Support: t.me/AvalAISupport.

## Key statements
- **Collected:** name, email, phone, account info, whatever user provides. **Used** to provide/improve service, support, updates, relevant offers.
- **Chat platform & model improvement:** conversations used to improve the model ONLY if "help improve the model" is ON (default OFF; Settings → Data). Used anonymised, identity removed, no ads/marketing use, **not shared with third parties** (incl. partners/providers).
- **Uploaded files:** never exploited; user must not upload sensitive/confidential files.
- **API privacy:** no processing/exploitation of API call content (prompts, inputs, messages, audio, images); only call history — model name, IP — stored for pricing and safety/security. (Content-policy page adds timestamp + usage metrics.)
- **Retention:** AvalAI reserves the right to use data for model improvement/dev for **up to 30 days after you delete it** (excluding uploaded files); **uploaded files deleted immediately on deletion request**.
- **Sharing:** shares personal info only when entitled — may include affiliates, business partners, third-party service providers (vague).
- **Security:** sensitive data incl. conversations stored **encrypted in the database**; uploaded files "encrypted (SHA256)" (SHA-256 is a hash, not encryption — wording defect).
- **Rights:** access, correct, delete, object to processing; delete account; exercise by contacting AvalAI.
- **Docs-site cookies/privacy control:** essential local storage (privacy choice, theme, text size, code display, search, navigation, update safety, short-lived caches; no GA for essentials). Levels (none pre-selected): **Essential** (no GA, no OpenRouter), **Performance** (+ Google Analytics 4 `G-4FRNQNQFBQ`, explicit page-view events: URL/path, title, doc language, basic device/perf info; auto page-view off), **All** (+ optional live model-data refresh from **OpenRouter**, which can see IP + normal request metadata; static reviewed model info remains available without it). Consent Mode v2 starts denied; GA tag not loaded until Performance/All; ads storage/user data/personalisation/Google Signals always denied; consent in `localStorage`; GA may set first-party `_ga` cookie; reopen via "Privacy settings" footer control; applies to docs hosts only (account/login/chat cookies follow those services).
- Embedded third-party content behaves as if visiting that site (tracking possible). Policy changes: major changes announced.

## How to apply
- For your own app: AvalAI-layer API content isn't retained per this policy, but **chat-platform data differs** from API — don't mix them (API key usage ≠ chat product). Don't promise customers "no logs": IP/model/timestamp/usage kept.
- Data-subject requests for AvalAI account data go to AvalAI support; account deletion triggers up-to-30-day residual use (not files). For Iranian/other regulation, treat AvalAI as a processor whose upstream providers are sub-processors (see content-policy.md).
- Don't upload sensitive/confidential files to the chat platform; for API files prefer `expires_after`, deletion, minimisation.
- When automating docs lookups, expect OpenRouter live-data requests only at "All" level — irrelevant to API use.

## Gaps / ambiguities
- Contradiction-ish: "we don't share with third parties" (training opt-in data) vs generic "may share with affiliates/partners/service providers"; "up to 30 days after deletion" use for model improvement is only coherent if opt-in was ON.
- Unspecified: legal entity/jurisdiction, data location, processor list, retention for account data/logs/IP, breach notification, minors, DPA/ZDR availability, contact email.
- "SHA256 encryption" claim technically inaccurate; no mention of at-rest key management.
