# Monetization — canonical state

Last verified: 2026-09-15 03:40 JST

## B06 status

**PASS via real production-reachable lead routes.** Production exposes two distinct non-binding paid-pilot paths: recurring monitoring + evidence report and a one-time exit-readiness audit. Each now routes to its own purpose-built public GitHub Issue template. This remains a lead/inquiry route, not checkout; no payment, revenue, conversion, pricing acceptance or willingness-to-pay is claimed.

## Route ranking

| Route | Relative EV | Speed | Traffic dependence | Approval friction | Recurring value | Automation / labor | Platform risk | Reversibility |
|---|---|---|---|---|---|---|---|---|
| Recurring monitoring + evidence report | Highest current fit; demand/WTP unproven | High: live lead route | Low–medium | Low before payment | High | High automation potential as scans repeat | Low | High |
| One-time exit-readiness audit/report | Strong independent fallback | High: live lead route | Low–medium | Low | None | Medium; report generation should remain standardized | Low | High |
| Hosted lead + checkout/subscription | Future friction-reduction/conversion experiment | Medium | Low | Payment onboarding | High or one-time | High once offer is proven | Medium | High |
| Merchant-of-record checkout | Future cross-border fallback | Medium | Low | Provider eligibility/onboarding | High or one-time | High once live | Medium–high provider dependence | High |
| Display ads / generic affiliate | Low fit | Medium | High | External approval possible | Traffic/referral-driven | High | Medium–high | High |

Primary remains recurring monitoring; one-time audit remains an independent offer path.

## Current production evidence

- Added `.github/ISSUE_TEMPLATE/recurring-monitoring-pilot.md` for recurring public-evidence monitoring inquiries and `.github/ISSUE_TEMPLATE/one-time-audit-pilot.md` for one-time exit-readiness audit inquiries.
- Both templates explicitly disclose that the inquiry is public, requires GitHub sign-in, is non-binding, must not contain confidential information, and does not establish scope/pricing/delivery commitments or legal advice.
- `public/contact.html` now routes the recurring CTA directly to the recurring template and the one-time CTA directly to the one-time template while retaining privacy-safe `offerType=monitoring|one_time` interest instrumentation.
- Exact product head `cd1c14fba48ee84be02e799fe9fc4cfd6c6e3739` completed Public MVP run `34881885725` **SUCCESS**, verifying the production deployment after the offer-specific routing change.
- Fresh open-Issue inspection found no user-created paid-pilot inquiry. Record this only as **no paid-pilot inquiry observed in the checked open-Issue surface**, not as proof of zero demand.

## Acceptance / evidence discipline

- B06 remains PASS only while at least one real public inquiry path is reachable and accurately disclosed.
- A placeholder, disabled CTA or fictitious checkout would not count.
- Do not infer payment-provider activation, purchases, revenue, demand, pricing acceptance or retention.
- Offer-level instrumentation becomes demand evidence only when genuine retained events exist.
- Public GitHub sign-in/visibility is a known conversion friction; do not add hosted checkout complexity before qualified interest justifies it.

## Next monetization actions

- Measure genuine paid-pilot interest split between `monitoring` and `one_time` once retained real-event evidence is available.
- Keep both offer-specific inquiry routes live while evidence is insufficient to eliminate either.
- If qualified interest appears, reduce GitHub sign-in/public-issue friction with a hosted lead route and then test explicit pricing/checkout.
- If meaningful qualified traffic produces no paid-pilot interest, revisit positioning/offer before adding payment complexity.
