# #003 EU Data Act SaaS Exit Audit — Canonical Technical Status

This file is the repository-side handoff for AI Venture Factory #003. Business-stage authority remains the central Google Sheet `AI Venture Factory｜案件台帳` and its `Stage Bゲート` tab.

## Production

- Public URL: https://hirokimm.github.io/data-act-exit-audit/
- Deployment: GitHub Pages via `.github/workflows/pages.yml`.
- Deployment identity: `health.json` records commit SHA, workflow run ID, repository and service identifier.
- Automated monitoring: scheduled every six hours; build/deploy/browser-QA failures create or refresh the repository alert issue.
- Production workflow verifies the public paid-pilot GitHub Issue route, sign-in/public-disclosure copy, issue-template existence, mobile/desktop browser QA, and the privacy-safe shared KPI transport contract.
- Runtime verification at 2026-09-15 JST resolved main `7c7f14f3d57a83528b82ef0491fcdd081b62007b`. Its latest monetization documentation follows an already production-verified referral-attribution head; current Stage B state remains governed by the central ledger.

## Current Stage B position

- Central ledger: **11/12 PASS**.
- B01/B02/B03/B04/B06/B07/B08/B09/B10/B11/B12 are PASS.
- B05 remains `未確認`: the static client sends namespaced `data_act_page_view`, `data_act_report_open`, `data_act_contact_open`, and `data_act_monetization_interest` events to the Factory Vercel KPI endpoint. Transport/CORS and synthetic event acceptance are verified, but retained/observable REAL production-event evidence is still required before PASS.
- 2026-09-14 user-observed Vercel Web Analytics showed `Visitors=0` and `Page Views=0` despite a real #003 iPhone page-open and real #002 use. That path is insufficient evidence and must not be treated as retained measurement.
- The shared `/api/kpi` endpoint independently writes accepted namespaced events as `KPI` records to Vercel Runtime Logs before best-effort Analytics forwarding. Runtime Logs are therefore the current shortest verification path.
- B06 is PASS for a real non-binding paid-pilot lead route from homepage/contact to the repository `paid-pilot.md` issue template. It is not evidence of checkout, payment, revenue, conversion, pricing acceptance or willingness-to-pay.

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

The shared #002 KPI endpoint accepts fixed namespaced #003 events only from exact origin `https://hirokimm.github.io`. Production verification has demonstrated CORS preflight and namespaced synthetic POST success. These checks establish transport reliability, not retained measurement.

Measurement integrity was repaired before the current evidence window: automated browser QA uses `?avf_synthetic=1` so client KPI emission is suppressed, and direct workflow KPI probes carry `x-avf-synthetic: 1`. Historical unmarked `data_act_*` events from before that repair are ineligible because automation could have generated them. B05 stays `未確認` until a later retained unmarked real event is objectively observed.

## Other Stage B evidence

- B01/B04: exact deployment identity and critical-path HTTP checks.
- B02/B03: live SaaS evidence scan and report generation during build.
- B07/B08/B09: indexable acquisition surface, trust pages and security/data-handling controls.
- B10: independent successful production mobile/desktop Chromium evidence remains authoritative.
- B11: dedicated ChatGPT Project `03｜EU Data Act・SaaS切替/データ出口監査`, central ledger and this repository provide durable linkage.
- B12: six-hour monitor and verified GitHub Issue alert path; synthetic monitoring is isolated from B05 evidence.

## Next priority

Obtain retained/observable REAL `data_act_*` production evidence from shared Vercel Runtime Logs. Prefer a post-fix `data_act_report_open`, `data_act_contact_open`, or `data_act_monetization_interest` interaction and require the matching retained `KPI` record to have no `synthetic:true` marker. Do not PASS B05 from code, CORS, synthetic POST success, historical unmarked traffic, or zero-valued Web Analytics alone.

Continue qualified B2B acquisition and paid-pilot demand validation in parallel; do not confuse Stage B gate completion with commercial traction.
