# Monetization — canonical state

Last verified: 2026-09-15 06:10+ JST

## B06 status

**PASS via real production-reachable lead routes.** Production exposes two distinct non-binding paid-pilot paths: recurring monitoring + evidence report and a one-time exit-readiness audit. Each routes to its own purpose-built public GitHub Issue template. This remains a lead/inquiry route, not checkout; no payment, revenue, conversion, pricing acceptance or willingness-to-pay is claimed.

## Route ranking

| Route | Relative EV | Speed | Traffic dependence | Approval friction | Recurring value | Automation / labor | Platform risk | Reversibility |
|---|---|---|---|---|---|---|---|---|
| Recurring monitoring + evidence report | Highest current fit; demand/WTP unproven | High: live lead route | Low–medium | Low before payment | High | High automation potential as scans repeat | Low | High |
| One-time exit-readiness audit/report | Strong independent fallback | High: live lead route | Low–medium | Low | None | Medium; report generation should remain standardized | Low | High |
| Stripe Payment Links | First direct-checkout candidate after qualified interest | High after provider activation | Low | Provider onboarding/identity/payout may apply | Supports recurring/one-time | High once live | Medium provider dependence | High |
| Lemon Squeezy Merchant of Record | Independent cross-border checkout fallback | Medium | Low | Provider eligibility/onboarding | Supports recurring/one-time | High once live; MoR can reduce indirect-tax operations | Medium–high provider dependence | High |
| Paddle Merchant of Record | Second independent MoR fallback; useful if eligibility/support fit is better | Medium | Low | Provider eligibility/onboarding | Supports subscriptions/one-time checkout | High once live; MoR tax/billing model | Medium–high provider dependence | High |
| Stripe Managed Payments (MoR) | Additional future alternative inside Stripe ecosystem | Medium | Low | Eligibility/onboarding | Supports applicable digital-commerce use cases | High once live | Medium–high provider dependence | High |
| Display ads / generic affiliate | Low fit | Medium | High | External approval possible | Traffic/referral-driven | High | Medium–high | High |

Primary remains recurring monitoring; one-time audit remains an independent offer path. Checkout remains contingent on qualified interest rather than being added as empty UI.

## Current production evidence — refreshed 2026-09-15 06:10+ JST

- Offer-specific public templates remain present for recurring monitoring and one-time audit inquiries and retain explicit public/sign-in/non-confidential/non-binding disclosures.
- `public/contact.html` routes the two CTAs to the matching templates while retaining privacy-safe `offerType=monitoring|one_time` interest instrumentation.
- The monetization implementation itself was previously verified on product head `cd1c14fba48ee84be02e799fe9fc4cfd6c6e3739` with Public MVP run `34881885725` **SUCCESS**.
- The last fully verified canonical head before this documentation refresh was `6c45b077ca37f272ee3142788b34a177622f6609`, with Public MVP `34890723259` **SUCCESS** and IndexNow `34890906219` **SUCCESS** in the central ledger. Documentation-only commits created in this run must be re-verified before being used as production lineage evidence.
- The checked public Issue surface still has no verified user-created paid-pilot inquiry. This is not proof of zero demand.
- Fresh Gmail review found no Stripe/Lemon Squeezy/Paddle or affiliate/payment activation message attributable to #003.
- External-AI queue contains no newly completed monetization result that changes B06; the #003 launch-readiness red-team task is queued, not a result.

## Checkout fallback evidence

`PAYMENT_READINESS.md` now records four factual alternatives and an explicit activation rule without inventing a price or account state.

- **Stripe Payment Links:** first direct-checkout candidate after qualified interest. Japan pricing currently starts at 3.6% per successful card charge; Payment Links supports one-time and recurring payment links. Actual account/onboarding state is unverified.
- **Lemon Squeezy:** first independent MoR fallback. Current published base ecommerce pricing is 5% + $0.50 per transaction, with possible additional fees; it states that it handles sales-tax/VAT collection and filing as Merchant of Record. Eligibility/account approval is unverified.
- **Paddle:** second independent MoR fallback. Current published pay-as-you-go pricing is 5% + $0.50 per Checkout transaction and includes payments/billing plus cross-border tax/compliance handling under its MoR model. Seller/product eligibility is unverified.
- **Stripe Managed Payments:** additional future MoR alternative, currently advertised in Japan at 3.5% in addition to Payments fees for successful Managed Payments transactions; eligibility is unverified.
- No provider account activation, merchant approval, product price, checkout URL or payment has been verified for #003.

Official evidence:
- https://stripe.com/en-jp/payments/payment-links
- https://stripe.com/jp/pricing
- https://www.lemonsqueezy.com/pricing
- https://docs.lemonsqueezy.com/help/payments/sales-tax-vat
- https://www.paddle.com/pricing
- https://www.paddle.com/billing/japan

## Acceptance / evidence discipline

- B06 remains PASS only while at least one real public inquiry path is reachable and accurately disclosed.
- A placeholder, disabled CTA or fictitious checkout would not count.
- Do not infer payment-provider activation, purchases, revenue, demand, pricing acceptance or retention.
- Offer-level instrumentation becomes demand evidence only when genuine retained events exist.
- Public GitHub sign-in/visibility is a known conversion friction; do not add hosted checkout complexity before qualified interest justifies it.
- B05 retained real-event evidence remains a separate unresolved gate.

## Next monetization actions

1. Measure genuine paid-pilot interest split between `monitoring` and `one_time` once retained real-event evidence is available.
2. Keep both offer-specific inquiry routes live while evidence is insufficient to eliminate either.
3. If qualified interest appears, first reduce GitHub sign-in/public-issue friction with a hosted lead route, define evidence-based scope/price, then verify direct Stripe versus at least two independent MoR providers in the actual provider-account context.
4. If meaningful qualified traffic produces no paid-pilot interest, revisit positioning/offer before adding payment complexity.
5. Re-verify the newest documentation head in production before updating the central B06 evidence lineage.
