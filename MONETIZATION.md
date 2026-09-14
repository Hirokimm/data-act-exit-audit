# Monetization — canonical state

Last verified: 2026-09-15 02:04 JST

## B06 status

**PASS via real production-reachable lead routes.** Production now exposes two distinct non-binding paid-pilot paths: recurring monitoring + evidence report and a one-time exit-readiness audit. Both route to the real public GitHub paid-pilot Issue template. This is a lead/inquiry route, not checkout; no payment, revenue, conversion, pricing acceptance or willingness-to-pay is claimed.

## Route ranking

| Route | Relative EV | Speed | Traffic dependence | Approval friction | Recurring value | Automation / labor | Platform risk | Reversibility |
|---|---|---|---|---|---|---|---|---|
| Recurring monitoring + evidence report | Highest current fit; demand/WTP unproven | High: live lead route | Low–medium | Low before payment | High | High automation potential as scans repeat | Low | High |
| One-time exit-readiness audit/report | Strong independent fallback | High: live lead route | Low–medium | Low | None | Medium; report generation should remain standardized | Low | High |
| Hosted checkout / subscription | Future upgrade | Medium | Low | Payment onboarding | High or one-time | High once offer is proven | Medium | High |
| Merchant-of-record checkout | Future cross-border fallback | Medium | Low | Provider eligibility/onboarding | High or one-time | High once live | Medium–high provider dependence | High |
| Display ads / generic affiliate | Low fit | Medium | High | External approval possible | Traffic/referral-driven | High automation | Medium–high | High |

Primary remains recurring monitoring; one-time audit is maintained as a genuinely independent offer path rather than a checkbox hidden behind one generic CTA.

## Current production evidence

- `public/contact.html` now exposes separate CTA copy for recurring monitoring and one-time audit, each pointing to the existing real paid-pilot GitHub Issue template and clearly disclosing public visibility/sign-in/non-binding scope.
- `public/kpi.js` now passes only allow-listed offer types (`monitoring`, `one_time`) to the shared #002 KPI sink on paid-pilot interest clicks.
- The shared sink itself was updated to retain/forward only the same allow-listed offer types, allowing route-level comparison without user/private data in KPI records.
- Exact product head `01295d1ab78d0235daafb526adf0db6700d7d051` deployed successfully through Public MVP run `34871770130` (**SUCCESS**), including the production deployment/verification workflow.
- Fresh open-Issue inspection found only the existing owner status issue and no user-created paid-pilot inquiry. Record this only as **no paid-pilot inquiry observed in the checked open-Issue surface**, not as proof of zero demand.
- Vercel connector access currently cannot read the shared sink Runtime Logs because it returns no teams; this is an observability-access limitation only.

## Acceptance / evidence discipline

B06 remains PASS only while at least one real public inquiry path is reachable and accurately disclosed. A placeholder, disabled CTA or fictitious checkout would not count.

Do not confuse B06 with payment-provider activation, completed purchase, revenue, observed demand, pricing acceptance, or B05 persistent real-event retention. Offer-level instrumentation is infrastructure; it becomes demand evidence only when genuine retained events exist.

## Constraints

- Never invent pricing, purchases, conversions or provider approval.
- Never request credentials, private contracts, personal data, security secrets or confidential information in the public issue.
- Provider identity, payout, tax/legal acceptance or irreversible account approvals are `WAITING_HUMAN` only when actually presented.
- Keep checkout as an independent future experiment, not a prerequisite for the valid Stage-B lead route.

## Next monetization actions

- Measure real paid-pilot interest split between `monitoring` and `one_time` once the post-repair retained-event evidence path is available.
- Keep both offers live while there is insufficient evidence to eliminate either route.
- If qualified interest appears, reduce GitHub public/sign-in friction with a hosted lead/checkout path and then test explicit pricing/payment.
- If meaningful qualified traffic produces no paid-pilot interest, revisit positioning/offer before adding payment complexity.
