# EU Data Act SaaS Switching & Data Portability Audit

Public technical-evidence audit for **EU Data Act SaaS switching, cloud exit readiness, data portability, export interfaces, and switching-fee evidence**. This is AI Venture Factory venture #003.

**Live audit:** https://hirokimm.github.io/data-act-exit-audit/?utm_source=github&utm_medium=referral&utm_campaign=repo-readme

## What it checks

The MVP collects only public evidence from SaaS websites and documentation and looks for observable signals relevant to switching and data exit, including:

- export and data-portability documentation;
- switching / termination guidance;
- API or other open-interface documentation;
- switching, egress, export, or related fee disclosures;
- public pre-contract information and help-center guidance;
- evidence changes across later scans.

The output is intentionally conservative: **PASS / REVIEW / UNKNOWN** is based on what can be observed publicly. `UNKNOWN` does not mean non-compliance, and the project does not make a legal-compliance determination.

## Who this is for

The public report is useful for SaaS operators, procurement teams, cloud/SaaS buyers, consultants, and product teams that want a fast technical evidence check before doing a deeper contractual or legal review.

## Why this exists

EU Data Act switching obligations create practical questions around SaaS data export, switching assistance, interfaces, documentation, and fees. Much of the first-pass evidence is already public but scattered across pricing pages, terms, help centers, trust pages, and API documentation. This project turns those public signals into a repeatable technical QA report.

## Current scope and limits

- Public web evidence only; no private contracts or authenticated customer data are accessed.
- No legal advice or certification.
- No claim that absence of public evidence proves a breach.
- Evidence is collected conservatively and should be reviewed before relying on it for procurement or compliance decisions.

## Try it

- [Open the live audit](https://hirokimm.github.io/data-act-exit-audit/?utm_source=github&utm_medium=referral&utm_campaign=repo-readme)
- [Read the current report](https://hirokimm.github.io/data-act-exit-audit/report.html?utm_source=github&utm_medium=referral&utm_campaign=repo-readme-report)
- [Inspect machine-readable results](https://hirokimm.github.io/data-act-exit-audit/results.json)

The two HTML links above carry coarse GitHub referral attribution. The JSON endpoint intentionally does not: it cannot execute the client KPI script, so adding a campaign parameter there would create an unmeasurable experiment.

For a paid-pilot request, use the clearly disclosed contact route on the live site. Submissions through GitHub require sign-in and may be public/indexable, as disclosed before the link.