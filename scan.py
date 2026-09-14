#!/usr/bin/env python3
import argparse, json, re, ssl, time
from html import unescape
from pathlib import Path
from urllib.parse import urlparse
from urllib.request import Request, urlopen

UA = "AI-Venture-Factory-DataAct-MVP/0.2 (+public-evidence-only)"
MAX_BYTES = 1_500_000
TIMEOUT = 15

DIMENSIONS = {
    "switching": [r"switch(?:ing)?", r"migrat(?:e|ion)", r"termination", r"transition assistance", r"business continuity"],
    "export": [r"data export", r"export (?:your|customer|account|workspace|project|organization|content|data)", r"export (?:its|the) customer content", r"download (?:your|customer|account|workspace|organization|content|data)", r"data portability", r"retrieve.{0,80}(?:customer|account|your) data", r"copy of.{0,80}(?:customer|account|your) data"],
    "open_interface": [r"\bapi\b", r"open interface", r"interoperab", r"developer platform", r"developer api"],
    "fees": [r"egress fee", r"switching fee", r"export fee", r"termination fee", r"data transfer fee", r"additional fee"],
    "pre_contract": [r"terms of service", r"customer terms", r"pricing", r"subscription", r"contract", r"agreement"],
}
TAG_RE = re.compile(r"<[^>]+>")
SPACE_RE = re.compile(r"\s+")

def host_matches(url, expected_domains):
    host = (urlparse(url).hostname or "").lower().rstrip(".")
    domains = expected_domains if isinstance(expected_domains, list) else [expected_domains]
    return any(host == d.lower().rstrip(".") or host.endswith("." + d.lower().rstrip(".")) for d in domains)

def clean_html(raw):
    text = raw.decode("utf-8", errors="replace")
    text = re.sub(r"(?is)<script.*?</script>|<style.*?</style>|<noscript.*?</noscript>", " ", text)
    return SPACE_RE.sub(" ", unescape(TAG_RE.sub(" ", text))).strip()

def fetch_public(url, expected_domains):
    p = urlparse(url)
    if p.scheme != "https" or not host_matches(url, expected_domains):
        return {"url": url, "ok": False, "error": "seed_not_https_or_domain_mismatch"}
    req = Request(url, headers={"User-Agent": UA, "Accept": "text/html,application/xhtml+xml;q=0.9,*/*;q=0.1"})
    try:
        with urlopen(req, timeout=TIMEOUT, context=ssl.create_default_context()) as r:
            final = r.geturl()
            if not host_matches(final, expected_domains):
                return {"url": url, "final_url": final, "ok": False, "error": "cross_domain_redirect"}
            ctype = (r.headers.get("Content-Type") or "").lower()
            if "text/html" not in ctype and "text/plain" not in ctype:
                return {"url": url, "final_url": final, "ok": False, "error": "unsupported_content_type", "content_type": ctype}
            raw = r.read(MAX_BYTES + 1)
            if len(raw) > MAX_BYTES:
                return {"url": url, "final_url": final, "ok": False, "error": "response_too_large"}
            return {"url": url, "final_url": final, "ok": True, "status": getattr(r, "status", 200), "text": clean_html(raw)}
    except Exception as e:
        return {"url": url, "ok": False, "error": f"{type(e).__name__}: {str(e)[:180]}"}

def evidence_for(text, url, patterns, limit=3):
    hits = []
    low = text.lower()
    for pat in patterns:
        for m in re.finditer(pat, low, re.I):
            start, end = max(0, m.start()-140), min(len(text), m.end()+220)
            snippet = SPACE_RE.sub(" ", text[start:end]).strip()
            if snippet and all(snippet != h["snippet"] for h in hits):
                hits.append({"url": url, "pattern": pat, "snippet": snippet[:500]})
            if len(hits) >= limit:
                return hits
    return hits

def classify_dimension(name, evidence):
    if not evidence:
        return "UNKNOWN"
    return "PASS" if name in {"export", "open_interface"} else "REVIEW"

def scan_target(target, delay=0.35):
    pages = []
    aggregated = {k: [] for k in DIMENSIONS}
    allowed_domains = target.get("domains") or target.get("domain")
    for seed in target["seeds"]:
        page = fetch_public(seed, allowed_domains)
        pages.append({k: v for k, v in page.items() if k != "text"})
        if page.get("ok"):
            for dim, patterns in DIMENSIONS.items():
                aggregated[dim].extend(evidence_for(page["text"], page.get("final_url", seed), patterns))
        time.sleep(delay)
    dimensions = {d: {"status": classify_dimension(d, ev), "evidence": ev[:5]} for d, ev in aggregated.items()}
    non_unknown = sum(1 for d in dimensions.values() if d["status"] != "UNKNOWN")
    useful = any(p.get("ok") for p in pages) and non_unknown >= 3
    return {"name": target["name"], "domains": allowed_domains if isinstance(allowed_domains, list) else [allowed_domains], "useful": useful, "non_unknown_dimensions": non_unknown, "dimensions": dimensions, "pages": pages}

def run(targets):
    results = [scan_target(t) for t in targets]
    useful_count = sum(1 for r in results if r["useful"])
    return {"method_version": "0.2", "disclaimer": "Public-evidence screening only; UNKNOWN is not non-compliance and REVIEW requires interpretation.", "success_criterion": ">=7/10 targets useful, where useful means >=3/5 non-UNKNOWN dimensions and >=1 successful public fetch", "useful_count": useful_count, "target_count": len(results), "technical_threshold_met": len(results) >= 10 and useful_count >= 7, "results": results}

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--targets", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    targets = json.loads(Path(args.targets).read_text(encoding="utf-8"))
    report = run(targets)
    Path(args.out).write_text(json.dumps(report, ensure_ascii=False, indent=2), encoding="utf-8")
    print(json.dumps({k: report[k] for k in ("useful_count", "target_count", "technical_threshold_met")}, ensure_ascii=False))

if __name__ == "__main__":
    main()
