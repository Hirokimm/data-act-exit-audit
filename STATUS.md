# #003 EU Data Act SaaS Exit Audit — Canonical Technical Status

This file is the repository-side handoff for AI Venture Factory #003. Business-stage authority remains the central Google Sheet `AI Venture Factory｜案件台帳` and its `Stage Bゲート` tab.

## Production

- Public URL: https://hirokimm.github.io/data-act-exit-audit/
- Deployment: GitHub Pages via `.github/workflows/pages.yml`.
- Deployment identity: `health.json` records commit SHA, workflow run ID, repository and service identifier.
- Automated monitoring: scheduled every six hours; build/deploy/browser-QA failures create or refresh the repository alert issue.
- Production workflow verifies the public paid-pilot GitHub Issue route, sign-in/public-disclosure copy, mobile/desktop browser QA, the privacy-safe shared KPI transport contract, and the decision-ready report structure.
- Resolve current main/deployment/workflow identities at runtime; do not treat a historical SHA or run number in documentation as permanently current.

## Current Stage B position

- Central ledger: **11/12 PASS**.
- B01/B02/B03/B04/B06/B07/B08/B09/B10/B11/B12 are PASS.
- B05 remains `未確認`: the static client sends namespaced `data_act_page_view`, `data_act_report_open`, `data_act_contact_open`, and `data_act_monetization_interest` events to the Factory Vercel KPI endpoint. Transport/CORS and synthetic event acceptance are verified, but retained/observable REAL production-event evidence is still required before PASS.
- B06 is PASS for a real non-binding paid-pilot lead route. It is not evidence of checkout, payment, revenue, conversion, pricing acceptance or willingness-to-pay.

## Product quality / user-value remediation — 2026-09-15

A genuine iPhone report-open exposed a material usability gap even though the technical E2E and Stage B checks were green: raw extracted snippets and word sequences dominated the report, so a non-specialist could not quickly answer “what is the issue and what should I do next?”. Under the Factory user-value policy, technical PASS alone was not treated as completion.

The report renderer was redesigned on main so each target now presents, in this order:
1. a plain-language verdict;
2. PASS / REVIEW / UNKNOWN counts and an interpretation statement;
3. prioritized recommended next actions tied to the affected dimensions;
4. source evidence only inside collapsed detail sections.

Raw public evidence is therefore preserved for auditability but demoted from the primary reading path. UNKNOWN is explicitly framed as an evidence gap rather than proof of non-compliance, and the report continues to state that it is not legal advice or certification.

Production verification is objective:
- product redesign commit `e6f53ebdf767246d9e8cf88316e34c9d111f967e` passed Public MVP run `34902973623` end to end;
- regression-guard commit `1d792d3f09d17b0a0c0b2a2e0ef691bc253cde38` adds build and production assertions for `How to use this report:`, `Recommended next actions`, and `View source evidence and scanner detail`;
- Public MVP run `34903202549` on that exact head completed build, Pages deployment, exact deployment-identity verification, production decision-structure checks, KPI transport verification, and mobile/desktop browser QA successfully.

This is an AI/user-perspective structural re-review and automated browser validation, not a claim that a fresh human comprehension study was performed after the redesign. The prior report-readability blocker is remediated at implementation/production level; Stage A still remains open because B05 is unresolved.

## B06 external red-team and remediation

Claude API Issue #12 independently reviewed the route and initially returned `CONDITIONAL`. It identified two material gaps: pre-click disclosure that submissions become public/indexable GitHub Issues requiring sign-in, and missing direct CTA-to-template E2E evidence.

HQ independently verified and remediated both findings:
- homepage and contact copy disclose before the CTA that GitHub sign-in is required and submitted issue content is public/may be indexed;
- the issue template carries a matching Public submission notice;
- CTA copy is `Open public paid-pilot inquiry`;
- production browser QA proved disclosure, CTA resolution and issue-template contents;
- subsequent successful Public MVP deployments preserved the route.

Final HQ decision keeps B06 PASS for **route existence only**. The completed Claude review issue has been closed after remediation.

## B05 shared KPI evidence

The shared #002 KPI endpoint accepts fixed namespaced #003 events only from exact origin `https://hirokimm.github.io`. Production verification has demonstrated CORS preflight and namespaced synthetic POST success. These checks establish transport reliability, not retained real-user measurement.

Two separate contamination classes have been repaired:

1. #003 monitoring previously had automation paths that could create unmarked `data_act_*` traffic. Browser QA now uses `?avf_synthetic=1` to suppress client emission, and direct workflow KPI probes use `x-avf-synthetic: 1`.
2. The shared sink previously forwarded header-marked synthetic probes to Vercel Analytics without a discriminator. The sink now excludes `synthetic:true` records from Analytics entirely, with regression tests and green production verification.

The shared sink assigns `evidenceVersion:2` **server-side** to every accepted #002/#003 record and carries that version into Analytics only for non-synthetic events. A client cannot choose or override the version.

Evidence rule: historical unmarked `data_act_*` from before the monitoring repair is ineligible, and pre-repair/versionless shared-sink records or Analytics counts are also ineligible as standalone B05 evidence. Eligible #003 evidence must be tied to a genuine production interaction, carry server-assigned `evidenceVersion:2`, have no `synthetic:true` marker, and occur under the repaired #003 monitoring regime. A retained unmarked Runtime Log `KPI` record remains the preferred proof.

## Other Stage B evidence

- B01/B04: exact deployment identity and critical-path HTTP checks.
- B02/B03: live SaaS evidence scan and report generation, plus the 2026-09-15 decision-ready output remediation and production regression guards.
- B07/B08/B09: indexable acquisition surface, trust pages and security/data-handling controls.
- B10: successful production mobile/desktop Chromium evidence remains authoritative; this is browser-emulated evidence, not a physical-device claim.
- B11: dedicated ChatGPT Project `03｜EU Data Act・SaaS切替/データ出口監査`, central ledger and this repository provide durable linkage.
- B12: six-hour repo monitor and verified GitHub Issue alert path; synthetic monitoring is isolated from B05 evidence. The separate Factory-HQ health monitor remains `REPAIRED_PENDING_VERIFY` until its own post-repair run succeeds.

## Next priority

1. Close B05 only with retained/observable REAL `data_act_*` production evidence under the repaired monitoring regime. Prefer `data_act_report_open`, `data_act_contact_open`, or `data_act_monetization_interest`, and require server-assigned `evidenceVersion:2` with no `synthetic:true` marker.
2. Preserve the new decision-ready report structure through the production regression guard; if genuine user feedback again shows that a target cannot be understood and acted on quickly, reopen Product Quality before promotion.
3. Continue qualified B2B acquisition and paid-pilot demand validation in the owning Growth/Monetization engines; do not confuse Stage B gate completion with commercial traction.
