# #003 EU Data Act SaaS Exit Audit — Canonical Technical Status

This file is the repository-side handoff for AI Venture Factory #003. Business-stage authority remains the central Google Sheet `AI Venture Factory｜案件台帳` and its `Stage Bゲート` tab.

## Production

- Public URL: https://hirokimm.github.io/data-act-exit-audit/
- Deployment: GitHub Pages via `.github/workflows/pages.yml`
- Deployment identity: `health.json` records commit SHA, workflow run ID, repository and service identifier.
- Automated monitoring: scheduled every six hours; build/deploy/browser-QA failures create or refresh the repository alert issue.
- Production workflow verifies the public paid-pilot GitHub Issue route, sign-in/public-disclosure copy, issue-template existence, mobile/desktop browser QA, and the privacy-safe KPI transport contract.

## Stage B technical evidence

- B01/B04: production identity and critical-path HTTP checks are enforced in the Pages workflow.
- B02/B03: live SaaS evidence scan and report generation run during every build.
- B05 remains `未確認`: the static client now sends namespaced `data_act_page_view`, `data_act_report_open`, `data_act_contact_open`, and `data_act_monetization_interest` events to the Factory Vercel KPI endpoint. The application event payload is only the fixed event name, credentials are omitted, the CSP permits only the intended sink, and Privacy discloses the measurement. The shared endpoint forwards accepted events to Vercel Analytics. Synthetic transport success is not sufficient; retained/observable production event evidence is still required before PASS.
- B06: production exposes a real non-binding paid-pilot lead route from the homepage/contact page to the repository `paid-pilot.md` issue template. No payment, revenue, conversion or provider approval is claimed.
- B07/B08/B09: indexable acquisition surface, public trust pages and security/data-handling controls are deployed and tested.
- B10: production browser QA is enforced on mobile and desktop Chromium.
- B11: dedicated ChatGPT Project `03｜EU Data Act・SaaS切替/データ出口監査`, central ledger, and this repository provide durable canonical linkage.
- B12: six-hour monitor and GitHub Issue alert path are verified.

## Current verification note

The first Public MVP run after wiring the shared KPI sink built and deployed the Pages artifact successfully but its post-deploy verification failed while the upstream #002 KPI CORS contract was still converging. That is an inter-service deployment race, not evidence of a scanner or Pages build failure. A later run must pass the CORS + namespaced-event production checks before this wiring is treated as verified.

## Next build priorities

1. Get a green Public MVP run with exact Pages deployment identity plus the shared KPI CORS/namespaced-event checks.
2. Observe real retained production `data_act_*` events in Vercel Analytics for B05; do not PASS from code or synthetic smoke alone.
3. Keep the paid-pilot lead route available while independently preparing hosted checkout options; do not regress B06 by replacing a working lead route with an unverified placeholder.

Never infer PASS from code presence alone. Record run/commit evidence in the central ledger and GitHub before changing a gate.
