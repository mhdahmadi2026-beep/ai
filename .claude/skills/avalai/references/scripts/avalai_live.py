#!/usr/bin/env python3
"""Live AvalAI catalog / price / cost helper (stdlib only, no key needed).

Source of truth: GET https://api.avalai.ir/public/models  (prices USD per 1M tokens, tier limits, endpoints).
Never quote prices from memory or from references/*.md without running this first.

  python3 -I avalai_live.py models [--grep gpt-6] [--mode chat] [--tier 1]
  python3 -I avalai_live.py price  gpt-6.1-sol
  python3 -I avalai_live.py check  gpt-6.1-sol claude-sonnet-5-5 whisper-1
  python3 -I avalai_live.py cost   gpt-6.1-sol --in 300000 --out 2000 [--cached 0] [--reasoning 0] [--rate 100000] [--tier 1]
  python3 -I avalai_live.py snapshot [--out live-snapshot.md]
  add  --file models.json  to work offline from a saved copy (also used by --selftest)
  python3 -I avalai_live.py --selftest
Exit codes: 0 ok, 1 usage/not found, 2 network error.
"""
import argparse, json, re, sys, time, urllib.request, urllib.error

URL = "https://api.avalai.ir/public/models"


def load(path=None):
    if path:
        with open(path, encoding="utf-8") as f:
            return json.load(f)["data"]
    req = urllib.request.Request(URL, headers={"User-Agent": "avalai-skill/1"})
    try:
        with urllib.request.urlopen(req, timeout=30) as r:
            return json.load(r)["data"]
    except (urllib.error.URLError, TimeoutError, ValueError) as e:
        print(f"network/parse error fetching {URL}: {e}\n"
              "Fallback: ask the user to open the URL and paste/save the JSON, then use --file.", file=sys.stderr)
        sys.exit(2)


def find(models, mid):
    for m in models:
        if m["id"] == mid:
            return m
    return None


def thresholds(pricing):
    """Return sorted list of (threshold_tokens, {base_key: rate}) from keys like input_above_272K."""
    out = {}
    for k, v in pricing.items():
        mt = re.fullmatch(r"(.+)_above_(\d+)([KkMm]?)", k)
        if mt:
            n = int(mt.group(2)) * {"": 1, "k": 1000, "m": 1_000_000}[mt.group(3).lower()]
            out.setdefault(n, {})[mt.group(1)] = v
    return sorted(out.items())


def cost(model, tin, tout, cached=0, reasoning=0, tier_note=True):
    """USD cost for ONE request. Higher long-context tier applies to the WHOLE request when
    total input tokens EXCEED the threshold (not just the excess). Reasoning tokens bill at output rate
    (add them to --out only if the provider's output count excludes them)."""
    p = dict(model.get("pricing", {}))
    rates = {k: v for k, v in p.items() if "_above_" not in k}
    for thr, over in thresholds(p):
        if tin > thr:                      # strictly greater; exactly threshold stays in lower band
            rates.update(over)
    r_in, r_out = rates.get("input"), rates.get("output")
    if r_in is None or r_out is None:
        raise ValueError(f"{model['id']}: non-token pricing {sorted(p)}; compute manually (per image/page/second/query).")
    r_cached = rates.get("cached_input", r_in)
    fresh = max(tin - cached, 0)
    usd = (fresh * r_in + cached * r_cached + (tout + reasoning) * r_out) / 1e6
    return usd, rates


def fmt_price(p):
    return ", ".join(f"{k}={v}" for k, v in sorted(p.items()))


def cmd_models(a, ms):
    n = 0
    for m in ms:
        if a.grep and not re.search(a.grep, m["id"], re.I):
            continue
        if a.mode and m.get("mode") != a.mode:
            continue
        if a.tier is not None and m.get("min_tier", 0) > a.tier:
            continue
        print(f"{m['id']:<40} {m.get('mode',''):<18} T{m.get('min_tier','?')} {fmt_price(m.get('pricing',{}))}")
        n += 1
    print(f"-- {n} models (USD per 1M tokens unless per_image/page/second/query)")


def cmd_price(a, ms):
    for mid in a.ids:
        m = find(ms, mid)
        if not m:
            print(f"{mid}: NOT in live catalog (removed/renamed? check references/10-deprecations.md)"); continue
        print(json.dumps({k: m.get(k) for k in ("id", "owned_by", "mode", "min_tier", "pricing", "max_input_tokens",
                                                "max_output_tokens", "supported_endpoints")}, indent=1, ensure_ascii=False))
        for t, lim in sorted((m.get("tier_rate_limits") or {}).items()):
            print(f"  tier {t}: {lim.get('max_requests_per_1_minute')} RPM / {lim.get('max_tokens_per_1_minute')} TPM")


def cmd_check(a, ms):
    bad = 0
    for mid in a.ids:
        m = find(ms, mid)
        if not m:
            print(f"MISSING  {mid}  -> not served now; see references/10-deprecations.md"); bad = 1
        else:
            print(f"OK       {mid}  min_tier={m.get('min_tier')} mode={m.get('mode')} endpoints={m.get('supported_endpoints')}")
    sys.exit(bad)


def cmd_cost(a, ms):
    m = find(ms, a.id)
    if not m:
        print("model not in live catalog"); sys.exit(1)
    usd, rates = cost(m, a.tin, a.tout, a.cached, a.reasoning)
    print(f"model={a.id} rates(USD/1M)={fmt_price(rates)}")
    print(f"input={a.tin} (cached {a.cached}) output={a.tout} reasoning={a.reasoning}")
    print(f"cost per request = ${usd:.6f}")
    if a.rate:
        print(f"                 = {usd*a.rate:,.2f} toman @ {a.rate:,.0f} toman/USD (use the CURRENT rate; "
              "exact billing: /user/v1/transactions/lookup)")
    if a.requests:
        print(f"x {a.requests:,} requests = ${usd*a.requests:,.2f}")
    if a.tier is not None and m.get("tier_rate_limits"):
        lim = m["tier_rate_limits"].get(str(a.tier))
        print(f"tier {a.tier} limit: {lim}" if lim else f"tier {a.tier}: NO ACCESS (min_tier={m.get('min_tier')})")


def cmd_snapshot(a, ms):
    rows = [f"# AvalAI live snapshot — {time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime())}",
            "", "Source: GET /public/models. USD per 1M tokens unless noted.", "",
            "| id | mode | min_tier | pricing | in/out ctx |", "|---|---|---|---|---|"]
    for m in sorted(ms, key=lambda x: (x.get("owned_by", ""), x["id"])):
        rows.append(f"| `{m['id']}` | {m.get('mode','')} | {m.get('min_tier','')} | {fmt_price(m.get('pricing',{}))} | "
                    f"{m.get('max_input_tokens','')}/{m.get('max_output_tokens','')} |")
    text = "\n".join(rows) + "\n"
    if a.out:
        open(a.out, "w", encoding="utf-8").write(text); print(f"wrote {a.out} ({len(ms)} models)")
    else:
        print(text)


def selftest():
    ms = [{"id": "x", "mode": "chat", "min_tier": 1,
           "pricing": {"input": 2.0, "cached_input": 0.1, "output": 10.0, "input_above_272K": 4.0,
                       "cached_input_above_272K": 0.2, "output_above_272K": 15.0},
           "tier_rate_limits": {"1": {"max_requests_per_1_minute": 5, "max_tokens_per_1_minute": 9}}}]
    u, _ = cost(ms[0], 100, 50); assert abs(u - 0.0007) < 1e-12, u            # (100*2+50*10)/1e6
    u, _ = cost(ms[0], 272_000, 0); assert abs(u - 0.544) < 1e-9, u            # exactly threshold -> lower band
    u, r = cost(ms[0], 272_001, 1000); assert r["output"] == 15.0 and abs(u - (272_001*4 + 15000)/1e6) < 1e-9
    u, _ = cost(ms[0], 1000, 0, cached=1000); assert abs(u - 0.0001) < 1e-12
    assert thresholds(ms[0]["pricing"])[0][0] == 272_000
    print("selftest OK")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--file")
    sub = ap.add_subparsers(dest="cmd")
    s = sub.add_parser("models"); s.add_argument("--grep"); s.add_argument("--mode"); s.add_argument("--tier", type=int)
    for n in ("price", "check"):
        s = sub.add_parser(n); s.add_argument("ids", nargs="+")
    s = sub.add_parser("cost"); s.add_argument("id")
    s.add_argument("--in", dest="tin", type=int, required=True); s.add_argument("--out", dest="tout", type=int, required=True)
    s.add_argument("--cached", type=int, default=0); s.add_argument("--reasoning", type=int, default=0)
    s.add_argument("--rate", type=float); s.add_argument("--tier", type=int); s.add_argument("--requests", type=int)
    s = sub.add_parser("snapshot"); s.add_argument("--out")
    a = ap.parse_args()
    if a.selftest:
        return selftest()
    if not a.cmd:
        ap.print_help(); sys.exit(1)
    ms = load(a.file)
    {"models": cmd_models, "price": cmd_price, "check": cmd_check, "cost": cmd_cost, "snapshot": cmd_snapshot}[a.cmd](a, ms)


if __name__ == "__main__":
    main()
