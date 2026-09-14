#!/usr/bin/env python3
import argparse, html, json
from pathlib import Path

STATUS_CLASS = {"PASS":"pass", "REVIEW":"review", "UNKNOWN":"unknown"}

def esc(value):
    return html.escape(str(value), quote=True)

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
            dims.append(f'<section class="dimension"><h4>{esc(name)} <span class="badge {STATUS_CLASS.get(status,"unknown")}">{esc(status)}</span></h4>{evidence_html}</section>')
        useful="Useful evidence" if result["useful"] else "Needs more evidence"
        cards.append(f'<article class="card"><h2>{esc(result["name"])}</h2><p><strong>{esc(useful)}</strong> · {result["non_unknown_dimensions"]}/5 dimensions with evidence</p>{"".join(dims)}</article>')
    threshold="met" if data["technical_threshold_met"] else "not met"
    return f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>EU Data Act SaaS Exit Evidence Scan</title><style>:root{{font-family:Inter,system-ui,sans-serif;color:#151515;background:#f6f7f9}}body{{margin:0}}main{{max-width:1000px;margin:auto;padding:24px}}.hero,.card{{background:white;border:1px solid #ddd;border-radius:14px;padding:20px;margin-bottom:18px}}.grid{{display:grid;grid-template-columns:repeat(auto-fit,minmax(290px,1fr));gap:16px}}.dimension{{border-top:1px solid #eee;padding-top:10px}}.badge{{font-size:.75rem;padding:3px 7px;border-radius:999px}}.pass{{background:#dff7e8}}.review{{background:#fff1c7}}.unknown{{background:#e9ebef}}blockquote{{margin:8px 0;padding:10px;border-left:3px solid #bbb;background:#fafafa;overflow-wrap:anywhere}}a{{color:#1358a8}}.muted{{color:#666}}@media(max-width:600px){{main{{padding:12px}}.hero,.card{{padding:14px;border-radius:10px}}}}</style></head><body><main><section class="hero"><h1>EU Data Act SaaS Exit Evidence Scan</h1><p><strong>{data["useful_count"]}/{data["target_count"]}</strong> targets met the technical public-evidence usefulness rule; threshold {esc(threshold)}.</p><p class="muted">Public-evidence screening only. PASS means direct positive evidence was found for the specific dimension; REVIEW needs interpretation; UNKNOWN means no qualifying evidence was collected and must not be read as non-compliance. This report is not legal advice.</p></section><div class="grid">{"".join(cards)}</div></main></body></html>'''

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input",required=True)
    ap.add_argument("--out",required=True)
    args=ap.parse_args()
    data=json.loads(Path(args.input).read_text(encoding="utf-8"))
    Path(args.out).write_text(render(data),encoding="utf-8")

if __name__=="__main__":
    main()
