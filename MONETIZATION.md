# Monetization — canonical state

Last verified: 2026-09-14 21:12 JST

## B06 status

**FAIL** — public production is live, but no genuine production-reachable checkout/payment endpoint has yet been verified. Placeholder CTAs do not count.

## Route ranking

1. **Primary product route: recurring monitoring + evidence report.** Best fit with recurring public-document change detection, low ongoing human labor, and recurring value. This remains the target product model; demand/CVR are not assumed.
2. **Independent product fallback: one-time paid exit-readiness audit/report.** Lower buyer commitment and operationally simple; useful for validating willingness-to-pay before recurring demand is established.
3. **Checkout stack — Stripe Payment Links first for implementation speed.** Official Japan documentation currently supports shareable one-time and recurring Payment Links; Payment Links are included with Payments, standard card pricing starts at 3.6% per successful card charge, and recurring charges also incur applicable Stripe Billing pricing. A provider-generated live link is still required before B06 can PASS.
4. **Checkout fallback — Lemon Squeezy Merchant of Record.** Official pricing currently publishes 5% + $0.50 per transaction as base ecommerce pricing, with possible additional fees; it supports no-code checkout and subscriptions and acts as Merchant of Record for sales-tax/VAT handling. This can reduce cross-border tax operational burden if onboarding eligibility is satisfied.
5. **Additional independent provider fallback — Paddle/MoR remains a candidate but is not promoted above the two verified options without fresh provider/account evidence.**

## Current account / approval evidence

- Gmail search at 2026-09-14 21:12 JST found no new message in the prior 2 days matching AdSense, Stripe, Semrush, Impact, Adobe, Partnerize, UPDF, CJ, Lemon Squeezy, Paddle, affiliate, or payment activation/onboarding terms.
- No payment-provider approval, live checkout URL, payout readiness, or legal/tax acceptance is therefore claimed.
- No demand, CVR, revenue, or approval rate is inferred.

## B06 acceptance test

B06 may move to PASS only after all of the following are evidenced:

1. a real provider-generated checkout/payment URL exists;
2. the production site exposes a user-reachable monetization CTA to that URL;
3. anonymous production reachability is tested end-to-end through the checkout landing surface;
4. checkout-click/conversion-near events are instrumented without sensitive user data;
5. required paid/affiliate disclosures are production-reachable.

## Constraints

- Do not invent or expose a checkout URL before a real provider-generated link exists.
- Provider identity, payout, tax/legal acceptance, or irreversible account approvals are `WAITING_HUMAN` only when actually presented by the provider.
- Routine dashboard/setup work is `WORK_ELIGIBLE`.
- A pending provider route never blocks research/preparation of independent fallbacks.

## Next action

Create a real hosted checkout for either the recurring offer or the one-time fallback, then wire the verified URL into production and instrument checkout-click/conversion-near events. Stripe Payment Links is the shortest currently verified implementation path; Lemon Squeezy remains the independent MoR fallback. If actual provider onboarding presents identity/payout/tax/legal acceptance, surface exactly that user-only step; otherwise continue autonomously.
