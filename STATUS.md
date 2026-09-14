# #003 EU Data Act SaaS Exit Audit — Canonical Technical Status

This file is the repository-side handoff for AI Venture Factory #003. Business-stage authority remains the central Google Sheet `AI Venture Factory｜案件台帳` and its `Stage Bゲート` tab.

## Production

- Public URL: https://hirokimm.github.io/data-act-exit-audit/
- Deployment: GitHub Pages via `.github/workflows/pages.yml`.
- Deployment identity: `health.json` records commit SHA, workflow run ID, repository and service identifier.
- Automated monitoring: scheduled every six hours; build/deploy/browser-QA failures create or refresh the repository alert issue.
- Production workflow verifies the public paid-pilot GitHub Issue route, sign-in/public-disclosure copy, issue-template existence, mobile/desktop browser QA, and the privacy-safe shared KPI transport contract.
- Resolve current main/deployment/workflow identities at runtime; do not treat a historical SHA or run number in documentation as permanently current.

## Current Stage B position

- Central ledger: **11/12 PASS**.
- B01/B02/B03/B04/B06/B07/B08/B09/B10/B11/B12 are PASS.
- B05 remains `未確認`: the static client sends namespaced `data_act_page_view`, `data_act_report_open`, `data_act_contact_open`, and `data_act_monetization_interest` events to the Factory Vercel KPI endpoint. Transport/CORS and synthetic event acceptance are verified, but retained/observable REAL production-event evidence is still required before PASS.
- 2026-09-14 user-observed Vercel Web Analytics showed `Visitors=0` and `Page Views=0` despite a real #003 iPhone page-open and real #002 use. That snapshot is insufficient evidence and must not be treated as retained measurement.
- The shared `/api/kpi` endpoint independently writes accepted namespaced events as `KPI` records to Vercel Runtime Logs. Runtime Logs remain the strongest verification path.
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

The shared #002 KPI endpoint accepts fixed namespaced #003 events only from exact origin `https://hirokimm.github.io`. Production verification has demonstrated CORS preflight and namespaced synthetic POST success. These checks establish transport reliability, not retained real-user measurement.

Two separate contamination classes have now been repaired:

1. #003 monitoring previously had automation paths that could create unmarked `data_act_*` traffic. Browser QA now uses `?avf_synthetic=1` to suppress client emission, and direct workflow KPI probes use `x-avf-synthetic: 1`.
2. A later shared-sink audit found that header-marked synthetic probes were correctly tagged `synthetic:true` in Runtime Logs but were still forwarded to Vercel Analytics without a discriminator. The shared sink now excludes `synthetic:true` records from Analytics entirely, with regression tests and green production verification on the repaired #002 lineage.

The shared sink now additionally assigns `evidenceVersion:2` **server-side** to every accepted #002/#003 record and carries that version into Analytics only for non-synthetic events. A client cannot choose or override the version. This gives #003 an objective shared-sink cutoff after the integrity repairs.

Evidence rule: historical unmarked `data_act_*` from before the #003 monitoring repair is ineligible, and pre-repair/versionless shared-sink records or Analytics counts are also ineligible as standalone B05 evidence. Eligible #003 evidence must be tied to a genuine production interaction, carry server-assigned `evidenceVersion:2`, have no `synthetic:true` marker, and occur under the repaired #003 monitoring regime. A retained unmarked Runtime Log `KPI` record remains the preferred proof; versioned post-repair Analytics may corroborate but does not by itself prove a genuine human interaction.

## Other Stage B evidence

- B01/B04: exact deployment identity and critical-path HTTP checks.
- B02/B03: live SaaS evidence scan and report generation during build.
- B07/B08/B09: indexable acquisition surface, trust pages and security/data-handling controls.
- B10: independent successful production mobile/desktop Chromium evidence remains authoritative.
- B11: dedicated ChatGPT Project `03｜EU Data Act・SaaS切替/データ出口監査`, central ledger and this repository provide durable linkage.
- B12: six-hour monitor and verified GitHub Issue alert path; synthetic monitoring is isolated from B05 evidence.

## Next priority

Obtain retained/observable REAL `data_act_*` production evidence under the repaired monitoring regime. Prefer `data_act_report_open`, `data_act_contact_open`, or `data_act_monetization_interest` and require the matching retained Runtime Log `KPI` record to contain server-assigned `evidenceVersion:2` and no `synthetic:true` marker. Do not PASS B05 from code, CORS, synthetic POST success, historical ambiguous traffic, pre-repair/versionless Analytics counts, or zero-valued Web Analytics alone.

Continue qualified B2B acquisition and paid-pilot demand validation in parallel; do not confuse Stage B gate completion with commercial traction.
