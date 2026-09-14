# #003 Payment / checkout readiness

Last verified: 2026-09-15 03:42 JST

Purpose: preserve an evidence-based checkout decision so a qualified paid-pilot lead can be converted quickly without inventing pricing or prematurely opening payment infrastructure. This document does **not** mean any payment account, merchant approval, tax setup, product price, checkout, or sale exists.

## Trigger before implementation

Do not add a paid checkout merely to satisfy B06; B06 already passes through real production lead routes. Implement checkout when there is qualified commercial interest or another concrete reason to reduce inquiry friction. Until then, keep scope/price non-binding.

## Route A — Stripe Payment Links

Current official Japan evidence checked 2026-09-15:

- Payment Links supports shareable one-time and recurring payment links.
- Payment Links is included in Stripe integrated pricing; recurring charges also invoke applicable Stripe Billing pricing.
- Stripe Japan currently lists card pricing starting at 3.6% per successful card charge, with additional fees for some cases such as currency conversion.
- Payment-provider account activation, identity/business verification, payout setup, tax/legal acceptance, and actual eligibility are not verified for this venture.

Why it is the default direct-payment candidate: fastest low-code path for a Japanese operator when we are prepared to own the merchant/tax/compliance workflow ourselves. That is a workflow judgment, not an eligibility claim.

Official sources:
- https://stripe.com/jp/payments/payment-links
- https://stripe.com/jp/pricing

## Route B — Lemon Squeezy Merchant of Record

Current official evidence checked 2026-09-15:

- Lemon Squeezy states a base ecommerce fee of 5% + $0.50 per transaction, with additional fees possible in certain cases.
- Its fee documentation currently lists possible additions including international, PayPal, and subscription fees.
- Lemon Squeezy states it acts as Merchant of Record and handles sales-tax/VAT collection and filing for transactions it processes.
- It supports both one-time and recurring products.
- Store/account approval, supported-business eligibility, identity/payout setup, and actual acceptance of #003 are not verified.

Why it remains the independent cross-border fallback: higher nominal transaction cost can be rational if Merchant-of-Record handling materially reduces EU VAT/sales-tax operational burden. Do not assume that benefit outweighs cost until the real offer, buyer geography, tax posture, and eligibility are known.

Official sources:
- https://www.lemonsqueezy.com/pricing
- https://docs.lemonsqueezy.com/help/getting-started/fees
- https://docs.lemonsqueezy.com/help/payments/sales-tax-vat

## Stripe Managed Payments note

Stripe Japan now also advertises a Merchant-of-Record service, Managed Payments, at 3.5% **in addition to** Payments fees for successful Managed Payments transactions, with coverage claims for indirect-tax handling in 75+ countries. Treat this as a third future alternative, not as active #003 infrastructure, until eligibility and exact applicable pricing are verified during onboarding.

Official source:
- https://stripe.com/jp/pricing

## Selection rule

When a qualified lead exists:

1. define the actual product first: recurring monitoring or one-time audit;
2. define the quoted price based on scope/evidence, not competitor imitation;
3. verify provider eligibility and total applicable fees in the real account/onboarding context;
4. prefer the lowest-complexity reversible checkout that satisfies buyer geography, tax/compliance, invoicing, and subscription needs;
5. instrument `checkout_started` / successful-payment evidence only after a real provider route exists; never treat a placeholder button as B06 or revenue evidence.

## Human boundary

Browser navigation and reversible setup are WORK_ELIGIBLE. Identity/business verification, bank/payout details, tax forms, legal acceptance, or irreversible provider submission remain user-only when actually presented. Queue such a blocker in `HUMAN_ACCELERATOR` only if it becomes the highest-leverage next step; do not notify routinely.
