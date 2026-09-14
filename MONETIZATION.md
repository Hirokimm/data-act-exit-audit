# Monetization — canonical state

Last verified: 2026-09-14 20:33 JST

## B06 status

**FAIL** — public production is live, but no genuine production-reachable checkout/payment endpoint has yet been verified. Placeholder CTAs do not count.

## Route ranking

1. **Primary: recurring monitoring + evidence report** — strongest fit with the product's recurring compliance/change-detection value and automation profile.
2. **Independent fallback: one-time paid exit-readiness audit/report** — lower commitment and simpler purchase decision; useful before recurring demand is proven.
3. **Payment-stack fallback:** prefer a no-code hosted checkout to minimize build work. Stripe Payment Links supports one-time and recurring payments in Japan; current official Japan pricing starts at 3.6% per successful card charge, with recurring Billing pricing applying separately. For EU/global tax-compliance simplification, Merchant-of-Record alternatives remain credible: Lemon Squeezy and Paddle both publish 5% + $0.50 base checkout pricing, with provider-specific/additional fees and eligibility to be verified at onboarding.

## Constraints

- Do not invent or expose a checkout URL before a real provider-generated link exists.
- Do not mark B06 PASS until a real user can reach/test the monetization path in production.
- Provider identity, payout, tax/legal acceptance, or irreversible account approvals are WAITING_HUMAN only when actually presented by the provider.
- Routine dashboard/setup work is WORK_ELIGIBLE.

## Next action

Create a real hosted checkout for the primary or one-time fallback, then wire the verified URL into the public site and instrument checkout-click/conversion events. If provider onboarding requests identity/payout/legal acceptance, surface exactly that user-only step; otherwise continue autonomously.
