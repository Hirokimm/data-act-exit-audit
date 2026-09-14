# Monetization — canonical state

Last verified: 2026-09-15 00:32 JST

## B06 status

**PASS via a real production-reachable lead route.** B06 does not require payment collection; the Stage B criterion permits a genuine lead route when users can reach and test it. Production offers a non-binding paid-pilot inquiry for either a one-time SaaS exit evidence audit or recurring monitoring.

Verified production evidence:
- B06 remediation release verified on exact production commit `8307545349533315173a6fa4ce0b4133a75c3851`.
- Public MVP run `34849946991` attempt 2: build/deploy/browser QA SUCCESS.
- homepage/contact disclose that GitHub Issue submission is public/indexable and requires sign-in.
- CTA resolves for anonymous users to GitHub login while preserving the paid-pilot template return path.
- raw `.github/ISSUE_TEMPLATE/paid-pilot.md` contains the non-binding paid offer, one-time and recurring options, public-submission notice and sign-in requirement.
- Current main at this verification: `d5f9427a800f93dc203e28f51b401c375ec27968`.
- Latest Public MVP run `34862783277` completed **SUCCESS** on that exact head SHA after the newest measurable-referral changes, providing fresh regression evidence that the public monetization surface remains deployed.

This is a **lead/inquiry route, not checkout**. No payment, revenue, conversion, pricing acceptance, provider approval, or willingness-to-pay is claimed.

## Route ranking

1. **Primary target product: recurring monitoring + evidence report.** Strongest fit with recurring public-document change detection and low ongoing human labor; actual demand/CVR/retention remain unproven.
2. **Independent fallback: one-time paid exit-readiness audit/report.** Lower buyer commitment and operationally simpler; the same production paid-pilot route supports it.
3. **Current Stage-B transaction mechanism: public GitHub paid-pilot lead inquiry.** Real and testable, but GitHub sign-in/public-issue friction makes it a validation mechanism rather than the desired long-term checkout UX.
4. **Hosted checkout upgrade: Stripe Payment Links or another verified provider.** Add when qualified interest makes payment collection worth testing; do not block Stage B on this because the real lead route already exists.
5. **Merchant-of-record fallback: Lemon Squeezy/Paddle class provider if cross-border tax handling becomes material.** Provider terms and account eligibility must be reverified before activation.
6. **Display ads / generic affiliates: low priority.** They are poorly aligned with a focused B2B compliance-evidence workflow and require more traffic than direct paid leads.

## Current demand evidence

- Fresh repository issue search at 2026-09-15 00:32 JST did not reveal a user-created paid-pilot/pricing/monitoring inquiry; only existing internal/status issues matched the broad monetization search.
- Treat this as **no paid-pilot inquiry observed in the checked GitHub issue surface**, not as proof of zero demand.
- The newest referral-attribution code/workflows are measurement infrastructure only; they are not evidence of visits, intent or willingness-to-pay.

## Acceptance / evidence discipline

B06 remains PASS only while the real public inquiry route stays reachable and accurately disclosed. A broken, disabled or placeholder CTA would invalidate the evidence.

Do not confuse this with:
- payment-provider activation,
- a completed purchase,
- revenue,
- observed paid demand,
- pricing acceptance,
- or B05 persistent real-event retention.

Historical unmarked `data_act_*` events from before the latest monitor-contamination repair are not eligible real-user evidence. Post-fix retained events must be free of `synthetic:true` to support B05.

## Constraints

- Do not invent pricing, purchases, conversions or provider approval.
- Do not request credentials, private contracts, personal data, security secrets or confidential information in the public issue.
- Provider identity, payout, tax/legal acceptance, or irreversible account approvals are `WAITING_HUMAN` only when actually presented by a provider.
- Keep checkout as an independent monetization experiment, not a prerequisite for the already-valid lead route.

## Next monetization actions

- Measure real `data_act_monetization_interest` / contact / report engagement only after the post-fix retained-event evidence path is available.
- If qualified paid-pilot interest appears, reduce GitHub-sign-in friction with a hosted lead/checkout path and then test explicit pricing/payment.
- If meaningful qualified traffic produces no paid-pilot interest, revisit positioning/offer before introducing payment complexity.
