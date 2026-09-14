#!/usr/bin/env python3
import argparse, html, json
from pathlib import Path

STATUS_CLASS = {"PASS":"pass", "REVIEW":"review", "UNKNOWN":"unknown"}
DIMENSION_LABELS = {
    "switching": "Switching / termination",
    "export": "Data export / portability",
    "open_interface": "Open interface / API",
    "fees": "Exit / switching fees",
    "pre_contract": "Pre-contract information",
}
ACTION_BY_DIMENSION = {
    "switching": "Confirm the customer-facing switching or termination process and document the operational hand-off steps.",
    "export": "Confirm the supported export path, formats, scope and any practical limits a customer would face when leaving.",
    "open_interface": "Confirm the documented API or other machine-readable interface available for customer data extraction or migration.",
    "fees": "Confirm whether any exit, egress, transfer or switching charges apply and where those terms are disclosed before purchase.",
    "pre_contract": "Confirm that the relevant exit, export and switching terms are clearly disclosed before contract commitment.",
}

def esc(value):
    return html.escape(str(value), quote=True)

def target_summary(result):
    statuses = {name: detail["status"] for name, detail in result["dimensions"].items()}
    unknown = [name for name, status in statuses.items() if status == "UNKNOWN"]
    review = [name for name, status in statuses.items() if status == "REVIEW"]
    passed = [name for name, status in statuses.items() if status == "PASS"]
    if unknown:
        verdict = "Evidence gap: public documentation is incomplete"
        meaning = f"{len(unknown)} of 5 dimensions have no qualifying public evidence in this scan. Treat these as verification gaps, not proof of non-compliance."
        priority = unknown + review
    elif review:
        verdict = "Manual review required before relying on the public evidence"
        meaning = f"All 5 dimensions surfaced evidence, but {len(review)} require interpretation before an operational or legal conclusion can be made."
        priority = review
    else:
        verdict = "Strong public evidence coverage in this technical scan"
        meaning = "All 5 dimensions surfaced direct positive evidence under the scanner's conservative rules. This is not a compliance certification."
        priority = []
    if priority:
        action_items = "".join(
            f'<li><strong>{esc(DIMENSION_LABELS.get(name, name))}:</strong> {esc(ACTION_BY_DIMENSION[name])}</li>'
            for name in priority[:3]
        )
    else:
        action_items = '<li>Keep the cited public evidence current and monitor these pages for material changes.</li>'
    counts = f'{len(passed)} PASS · {len(review)} REVIEW · {len(unknown)} UNKNOWN'
    return verdict, meaning, counts, action_items

def render(data):
    cards=[]
    for result in data["results"]:
        dims=[]
        for name, detail in result["dimensions"].items():
            status=detail["status"]
            items=[]
            for evidence in detail.get("evidence",[])[:3]:
                items.append(f'<li><a href="{esc(evidence["url"])}" rel="noreferrer">source</a><blockquote>{esc(evidence["snippet"])}</blockquote></li>')
            evidence_html=f'<ul>{"".join(items)}</ul>' if items else '<p class="muted">No qualifying public evidence captured.</p>'
            dims.append(f'<details class="dimension"><summary><span>{esc(DIMENSION_LABELS.get(name, name))}</span> <span class="badge {STATUS_CLASS.get(status,"unknown")}">{esc(status)}</span></summary>{evidence_html}</details>')
        verdict, meaning, counts, action_items = target_summary(result)
        cards.append(
            f'<article class="card"><div class="card-head"><div><h2>{esc(result["name"])}</h2><p class="statusline">{esc(counts)}</p></div></div>'
            f'<section class="decision"><h3>{esc(verdict)}</h3><p>{esc(meaning)}</p><h4>Recommended next actions</h4><ol>{action_items}</ol></section>'
            f'<details class="evidence-details"><summary>View source evidence and scanner detail</summary>{"".join(dims)}</details></article>'
        )
    threshold="met" if data["technical_threshold_met"] else "not met"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="index,follow,max-image-preview:large"><title>EU Data Act SaaS Exit Evidence Scan | Public evidence report</title><meta name="description" content="Decision-ready public-evidence report for SaaS switching, data export, open interfaces, fees and pre-contract disclosures in the EU Data Act context."><link rel="canonical" href="https://hirokimm.github.io/data-act-exit-audit/report.html"><meta property="og:type" content="article"><meta property="og:title" content="EU Data Act SaaS Exit Evidence Scan"><meta property="og:description" content="Decision-ready public-evidence report for SaaS switching and data-exit signals."><meta property="og:url" content="https://hirokimm.github.io/data-act-exit-audit/report.html"><style>:root{{font-family:Inter,system-ui,sans-serif;color:#151515;background:#f6f7f9}}body{{margin:0}}main{{max-width:1000px;margin:auto;padding:24px}}.hero,.card{{background:white;border:1px solid #ddd;border-radius:14px;padding:20px;margin-bottom:18px}}.hero h1,.card h2{{margin-top:0}}.summary{{font-size:1.08rem;line-height:1.55}}.decision{{background:#f8fafc;border:1px solid #dce3ea;border-radius:10px;padding:14px 16px;margin-top:12px}}.decision h3{{margin:0 0 8px;font-size:1.05rem}}.decision h4{{margin:14px 0 6px}}.decision ol{{margin:0;padding-left:22px}}.decision li{{margin:6px 0;line-height:1.45}}.statusline{{font-weight:650;color:#444;margin:.25rem 0 0}}details.evidence-details{{margin-top:14px;border-top:1px solid #e6e8eb;padding-top:12px}}details summary{{cursor:pointer;font-weight:650}}.dimension{{border-top:1px solid #eee;padding:10px 0}}.dimension summary{{display:flex;justify-content:space-between;gap:10px;align-items:center}}.badge{{font-size:.75rem;padding:3px 7px;border-radius:999px;white-space:nowrap}}.pass{{background:#dff7e8}}.review{{background:#fff1c7}}.unknown{{background:#e9ebef}}blockquote{{margin:8px 0;padding:10px;border-left:3px solid #bbb;background:#fafafa;overflow-wrap:anywhere}}a{{color:#1358a8}}.muted{{color:#666}}@media(max-width:600px){{main{{padding:12px}}.hero,.card{{padding:14px;border-radius:10px}}.decision{{padding:12px}}}}</style></head><body><main><section class="hero"><h1>EU Data Act SaaS Exit Evidence Scan</h1><p class="summary"><strong>{data["useful_count"]}/{data["target_count"]}</strong> targets met the scanner's technical public-evidence usefulness rule; threshold {esc(threshold)}.</p><p><strong>How to use this report:</strong> start with each target's verdict and recommended actions. Open the source-evidence section only when you need to validate the underlying wording.</p><p class="muted">Public-evidence screening only. PASS means direct positive evidence was found for the specific dimension; REVIEW needs interpretation; UNKNOWN means no qualifying evidence was collected and must not be read as non-compliance. This report is not legal advice.</p></section>{"".join(cards)}</main></body></html>'''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    data=json.loads(Path(args.input).read_text(encoding="utf-8"))
    Path(args.out).write_text(render(data),encoding="utf-8")

if __name__=="__main__":
    main()
