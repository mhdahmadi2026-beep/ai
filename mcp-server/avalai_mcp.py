#!/usr/bin/env python3
"""AvalAI knowledge MCP server (stdio, zero dependencies, Python >= 3.9).

Gives any MCP client (Claude Code, Claude Desktop, Cursor, Codex, ...) searchable access to the
whole AvalAI documentation corpus bundled in this repository + LIVE price/model data.

Tools
  avalai_search        BM25 full-text search over curated references and/or the verbatim source archive
  avalai_get_page      read a page (paged by chars) or one section by heading
  avalai_list_pages    list pages (filter by substring), curated + archive
  avalai_code_samples  find code samples by query and language (python, javascript, bash, php, go, ...)
  avalai_models        LIVE catalog from /public/models (grep / mode / tier filters)
  avalai_price         LIVE price + per-tier limits for model ids
  avalai_cost          LIVE cost estimate (long-context tiers, cache, reasoning, toman rate)
  avalai_check_models  are these ids served right now? (+ deprecation hint from docs)
  avalai_deprecation   look up an id/keyword in the complete deprecated-model list
  avalai_news          list news (newest first) or read one item
Resources   avalai://ref/<path>  every curated reference file
Prompts     avalai_integration_review, avalai_cost_plan, avalai_migrate_model

Env: AVALAI_DOCS_DIR (default: <repo>/.claude/skills/avalai/references), AVALAI_MCP_OFFLINE=1 (never touch network),
     AVALAI_MODELS_FILE (use a saved /public/models JSON instead of the network).
Run self-test:  python3 avalai_mcp.py --selftest
"""
from __future__ import annotations

import json
import math
import os
import re
import sys
import time
import urllib.error
import urllib.request
from collections import Counter, defaultdict
from pathlib import Path

SERVER_NAME = "avalai-docs"
SERVER_VERSION = "1.0.0"
PUBLIC_MODELS_URL = "https://api.avalai.ir/public/models"


# ----------------------------------------------------------------------------- corpus
def docs_dir() -> Path:
    env = os.environ.get("AVALAI_DOCS_DIR")
    if env:
        return Path(env)
    here = Path(__file__).resolve().parent
    for cand in (here.parent / ".claude/skills/avalai/references", here / "references", here.parent / "references"):
        if cand.is_dir():
            return cand
    raise SystemExit("AVALAI_DOCS_DIR not found; set it to the skill's references/ directory")


TOKEN_RE = re.compile(r"[A-Za-z0-9_]+(?:[.\-/:][A-Za-z0-9_]+)*|[؀-ۿ]+")


def tokenize(text: str) -> list[str]:
    out: list[str] = []
    for m in TOKEN_RE.finditer(text.lower()):
        t = m.group(0)
        out.append(t)
        if re.search(r"[.\-/:]", t):  # also index the parts: gpt-6.1-sol -> gpt, 6, 1, sol
            out.extend(p for p in re.split(r"[.\-/:]", t) if p)
    return out


class Page:
    __slots__ = ("rel", "kind", "title", "text")

    def __init__(self, rel: str, kind: str, title: str, text: str):
        self.rel, self.kind, self.title, self.text = rel, kind, title, text


class Chunk:
    __slots__ = ("page", "heading", "text", "tf", "length")


class Corpus:
    def __init__(self, root: Path):
        self.root = root
        self.pages: dict[str, Page] = {}
        self.chunks: list[Chunk] = []
        self.df: Counter = Counter()
        self.avg_len = 1.0
        self._load()

    def _load(self) -> None:
        for p in sorted(self.root.rglob("*.md")):
            rel = p.relative_to(self.root).as_posix()
            try:
                text = p.read_text(encoding="utf-8")
            except Exception:
                continue
            kind = "archive" if rel.startswith("source-archive/") else "curated"
            m = re.search(r"^# (.+)$", text, re.M)
            title = m.group(1).strip() if m else rel
            self.pages[rel] = Page(rel, kind, title, text)
            self._chunk(self.pages[rel])
        n = len(self.chunks) or 1
        self.avg_len = sum(c.length for c in self.chunks) / n
        for c in self.chunks:
            for t in c.tf:
                self.df[t] += 1

    def _chunk(self, page: Page) -> None:
        heading, buf, in_fence = page.title, [], False

        def flush():
            body = "\n".join(buf).strip()
            if len(body) < 40:
                return
            # split very long bodies
            for i in range(0, len(body), 2400):
                part = body[i:i + 2600]
                c = Chunk()
                c.page, c.heading, c.text = page, heading, part
                toks = tokenize(heading + " " + page.title + " " + part)
                c.tf = Counter(toks)
                c.length = len(toks) or 1
                self.chunks.append(c)

        for ln in page.text.split("\n"):
            if ln.startswith("```"):
                in_fence = not in_fence
            if not in_fence and re.match(r"^#{1,4} ", ln):
                flush()
                buf = []
                heading = ln.lstrip("# ").strip()
            buf.append(ln)
        flush()

    def search(self, query: str, limit: int = 8, scope: str = "all") -> list[tuple[float, Chunk]]:
        q = tokenize(query)
        if not q:
            return []
        n = len(self.chunks)
        scores: list[tuple[float, Chunk]] = []
        k1, b = 1.4, 0.75
        qset = set(q)
        for c in self.chunks:
            if scope != "all" and c.page.kind != scope:
                continue
            s = 0.0
            for t in qset:
                f = c.tf.get(t)
                if not f:
                    continue
                idf = math.log(1 + (n - self.df[t] + 0.5) / (self.df[t] + 0.5))
                s += idf * f * (k1 + 1) / (f + k1 * (1 - b + b * c.length / self.avg_len))
            if s:
                if c.page.kind == "curated":
                    s *= 1.15  # prefer curated knowledge over raw archive on ties
                low = c.heading.lower()
                s += 1.5 * sum(1 for t in qset if t in low)
                scores.append((s, c))
        scores.sort(key=lambda x: -x[0])
        # de-duplicate: max 2 chunks per page
        out, seen = [], Counter()
        for s, c in scores:
            if seen[c.page.rel] >= 2:
                continue
            seen[c.page.rel] += 1
            out.append((s, c))
            if len(out) >= limit:
                break
        return out


_CORPUS: Corpus | None = None


def corpus() -> Corpus:
    global _CORPUS
    if _CORPUS is None:
        _CORPUS = Corpus(docs_dir())
    return _CORPUS



# ----------------------------------------------------------------------------- semantic index (optional)
import hashlib
import struct
import threading

INDEX_DIR = Path(os.environ.get("AVALAI_INDEX_DIR", str(Path(__file__).resolve().parent / "index")))


def chunk_id(c: "Chunk") -> str:
    return hashlib.sha1((c.page.rel + "\x00" + c.heading + "\x00" + c.text).encode("utf-8")).hexdigest()[:16]


def chunk_input(c: "Chunk") -> str:
    """Text actually embedded: title + heading give the model the context the chunk body lacks."""
    return f"{c.page.title} › {c.heading}\n{c.text}"[:6000]


def _fake_embed(texts: list[str], dim: int = 256) -> list[list[float]]:
    """Deterministic hashed bag-of-words (tests / offline demo ONLY, not semantic)."""
    out = []
    for t in texts:
        v = [0.0] * dim
        for tok in tokenize(t):
            h = int(hashlib.md5(tok.encode()).hexdigest(), 16)
            v[h % dim] += 1.0 if (h >> 8) & 1 else -1.0
        out.append(v)
    return out


def embed_texts(texts: list[str], dimensions: int | None = None) -> list[list[float]]:
    """OpenAI-compatible /embeddings call (AvalAI by default). Env: AVALAI_API_KEY (or EMBED_API_KEY),
    EMBED_BASE_URL (default https://api.avalai.ir/v1), AVALAI_EMBED_MODEL, AVALAI_EMBED_DIMENSIONS."""
    if os.environ.get("AVALAI_EMBED_FAKE"):
        return _fake_embed(texts, dimensions or 256)
    key = os.environ.get("EMBED_API_KEY") or os.environ.get("AVALAI_API_KEY")
    if not key:
        raise RuntimeError("AVALAI_API_KEY not set (needed to embed the query / build the index)")
    base = os.environ.get("EMBED_BASE_URL", "https://api.avalai.ir/v1").rstrip("/")
    model = os.environ.get("AVALAI_EMBED_MODEL")
    if not model:
        raise RuntimeError("AVALAI_EMBED_MODEL not set (pick one with avalai_models mode=embedding)")
    body = {"model": model, "input": texts}
    if dimensions:
        body["dimensions"] = dimensions
    delay = 1.0
    for attempt in range(5):
        req = urllib.request.Request(base + "/embeddings", data=json.dumps(body).encode(), method="POST",
                                     headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json", "User-Agent": "avalai-mcp/1"})
        try:
            with urllib.request.urlopen(req, timeout=120) as r:
                data = json.load(r)["data"]
            data.sort(key=lambda d: d["index"])
            return [d["embedding"] for d in data]
        except urllib.error.HTTPError as e:
            if e.code in (429, 500, 502, 503, 504) and attempt < 4:
                ra = e.headers.get("Retry-After")
                time.sleep(float(ra) if ra else delay)
                delay = min(delay * 2, 30)
                continue
            raise RuntimeError(f"embeddings HTTP {e.code}: {e.read()[:300]!r} (avalai-request-id={e.headers.get('avalai-request-id')})")
        except (urllib.error.URLError, TimeoutError) as e:
            if attempt < 4:
                time.sleep(delay)
                delay = min(delay * 2, 30)
                continue
            raise RuntimeError(f"embeddings network error: {e}")
    raise RuntimeError("embeddings failed")


def _normalize(v: list[float]) -> list[float]:
    n = math.sqrt(sum(x * x for x in v)) or 1.0
    return [x / n for x in v]


class VectorIndex:
    """float16 matrix on disk (index/vectors.f16 + index/meta.json). numpy used when available."""

    def __init__(self):
        self.meta: dict | None = None
        self.ids: list[str] = []
        self.pos: dict[str, int] = {}
        self.dim = 0
        self.mat = None
        self._np = None
        self._lock = threading.Lock()

    def load(self) -> bool:
        mp, vp = INDEX_DIR / "meta.json", INDEX_DIR / "vectors.f16"
        if not (mp.exists() and vp.exists()):
            return False
        self.meta = json.loads(mp.read_text(encoding="utf-8"))
        self.ids, self.dim = self.meta["ids"], self.meta["dim"]
        self.pos = {i: k for k, i in enumerate(self.ids)}
        raw = vp.read_bytes()
        try:
            import numpy as np  # optional speed-up
            self._np = np
            self.mat = np.frombuffer(raw, dtype=np.float16).reshape(-1, self.dim).astype(np.float32)
        except Exception:
            n = len(raw) // 2
            flat = struct.unpack(f"<{n}e", raw)
            self.mat = [flat[i * self.dim:(i + 1) * self.dim] for i in range(len(self.ids))]
        return True

    def top(self, qvec: list[float], k: int, allowed: set[int] | None = None) -> list[tuple[float, str]]:
        q = _normalize(qvec)
        if len(q) != self.dim:
            raise RuntimeError(f"query dim {len(q)} != index dim {self.dim}; use the same model/dimensions as the index ({self.meta.get('model')}, {self.dim})")
        if self._np is not None:
            sc = self.mat @ self._np.array(q, dtype=self._np.float32)
            order = self._np.argsort(-sc)
            res = []
            for i in order:
                if allowed is not None and int(i) not in allowed:
                    continue
                res.append((float(sc[i]), self.ids[int(i)]))
                if len(res) >= k:
                    break
            return res
        sc = []
        for i, row in enumerate(self.mat):
            if allowed is not None and i not in allowed:
                continue
            sc.append((sum(a * b for a, b in zip(row, q)), i))
        sc.sort(reverse=True)
        return [(s, self.ids[i]) for s, i in sc[:k]]


_VINDEX: VectorIndex | None = None
_QCACHE: dict[str, list[float]] = {}


def vindex() -> VectorIndex | None:
    global _VINDEX
    if _VINDEX is None:
        v = VectorIndex()
        _VINDEX = v if v.load() else None
    return _VINDEX


def semantic_search(query: str, limit: int, scope: str) -> list[tuple[float, "Chunk"]]:
    vi = vindex()
    if vi is None:
        raise RuntimeError("no semantic index (run mcp-server/build_index.py once)")
    c = corpus()
    if not hasattr(c, "_by_id"):
        c._by_id = {chunk_id(ch): ch for ch in c.chunks}
    if query not in _QCACHE:
        dims = vi.dim if vi.meta.get("dimensions") else None
        _QCACHE[query] = embed_texts([query], dims)[0]
    allowed = None
    if scope != "all":
        allowed = {vi.pos[cid] for cid, ch in c._by_id.items() if ch.page.kind == scope and cid in vi.pos}
    return [(s, c._by_id[cid]) for s, cid in vi.top(_QCACHE[query], limit * 4, allowed) if cid in c._by_id]


def hybrid_search(query: str, limit: int, scope: str, mode: str) -> tuple[list[tuple[float, "Chunk"]], str]:
    """mode: bm25 | semantic | hybrid | auto (hybrid when index+embeddings are usable, else bm25)."""
    c = corpus()
    if mode == "bm25":
        return c.search(query, limit, scope), "bm25"
    try:
        sem = semantic_search(query, limit, scope)
    except Exception as e:
        if mode == "semantic":
            raise
        return c.search(query, limit, scope), f"bm25 (semantic unavailable: {str(e)[:120]})"
    if mode == "semantic":
        return _dedupe(sem, limit), "semantic"
    lex = c.search(query, limit * 4, scope)
    fused: dict[int, float] = defaultdict(float)
    byid: dict[int, "Chunk"] = {}
    for rank, (_, ch) in enumerate(lex):
        fused[id(ch)] += 1.0 / (60 + rank)
        byid[id(ch)] = ch
    for rank, (_, ch) in enumerate(sem):
        fused[id(ch)] += 1.0 / (60 + rank)
        byid[id(ch)] = ch
    ranked = sorted(((s, byid[i]) for i, s in fused.items()), key=lambda x: -x[0])
    return _dedupe(ranked, limit), "hybrid (BM25 + embeddings, RRF)"


def _dedupe(items, limit):
    out, seen = [], Counter()
    for s, ch in items:
        if seen[ch.page.rel] >= 2:
            continue
        seen[ch.page.rel] += 1
        out.append((s, ch))
        if len(out) >= limit:
            break
    return out


# ----------------------------------------------------------------------------- live data
_MODELS_CACHE: tuple[float, list[dict]] | None = None


def live_models(force: bool = False) -> list[dict]:
    global _MODELS_CACHE
    if _MODELS_CACHE and not force and time.time() - _MODELS_CACHE[0] < 600:
        return _MODELS_CACHE[1]
    f = os.environ.get("AVALAI_MODELS_FILE")
    if f:
        data = json.loads(Path(f).read_text(encoding="utf-8"))["data"]
    elif os.environ.get("AVALAI_MCP_OFFLINE"):
        raise RuntimeError("offline mode: set AVALAI_MODELS_FILE to a saved /public/models JSON")
    else:
        req = urllib.request.Request(PUBLIC_MODELS_URL, headers={"User-Agent": "avalai-mcp/1"})
        try:
            with urllib.request.urlopen(req, timeout=30) as r:
                data = json.load(r)["data"]
        except (urllib.error.URLError, TimeoutError, ValueError) as e:
            raise RuntimeError(
                f"cannot fetch {PUBLIC_MODELS_URL}: {e}. Ask the user to save that JSON and set AVALAI_MODELS_FILE; "
                "until then label any number from the docs as an unverified snapshot."
            )
    _MODELS_CACHE = (time.time(), data)
    return data


def _thresholds(pricing: dict) -> list[tuple[int, dict]]:
    out: dict[int, dict] = {}
    for k, v in pricing.items():
        mt = re.fullmatch(r"(.+)_above_(\d+)([KkMm]?)", k)
        if mt:
            n = int(mt.group(2)) * {"": 1, "k": 1000, "m": 1_000_000}[mt.group(3).lower()]
            out.setdefault(n, {})[mt.group(1)] = v
    return sorted(out.items())


def compute_cost(model: dict, tin: int, tout: int, cached: int = 0, reasoning: int = 0) -> tuple[float, dict]:
    p = dict(model.get("pricing", {}))
    rates = {k: v for k, v in p.items() if "_above_" not in k}
    for thr, over in _thresholds(p):
        if tin > thr:  # strictly greater; higher band applies to the WHOLE request
            rates.update(over)
    if "input" not in rates or "output" not in rates:
        raise ValueError(f"{model['id']} has non-token pricing {sorted(p)}; compute per image/page/second/query manually")
    r_cached = rates.get("cached_input", rates["input"])
    fresh = max(tin - cached, 0)
    usd = (fresh * rates["input"] + cached * r_cached + (tout + reasoning) * rates["output"]) / 1e6
    return usd, rates


# ----------------------------------------------------------------------------- tools
def _text(s: str) -> dict:
    return {"content": [{"type": "text", "text": s}]}


def _err(s: str) -> dict:
    return {"content": [{"type": "text", "text": s}], "isError": True}


def t_search(a: dict) -> dict:
    q = a.get("query", "")
    scope = a.get("scope", "all")
    limit = int(a.get("limit", 8))
    try:
        res, used = hybrid_search(q, limit, scope, a.get("mode", "auto"))
    except RuntimeError as e:
        return _err(str(e))
    if not res:
        return _text(f"No results for {q!r}. Try other keywords (model ids, parameter names, Persian or English).")
    out = [f"_search mode: {used}_\n"]
    for i, (s, c) in enumerate(res, 1):
        snippet = c.text.strip()
        if len(snippet) > int(a.get("snippet_chars", 900)):
            snippet = snippet[: int(a.get("snippet_chars", 900))] + " …"
        out.append(f"### {i}. {c.page.title} › {c.heading}\n`{c.page.rel}` ({c.page.kind}, score {s:.3f})\n\n{snippet}\n")
    out.append("\nUse avalai_get_page(path, section=…) for full text. Prices/ids from docs are snapshots — confirm with avalai_price / avalai_check_models.")
    return _text("\n".join(out))


def t_index_status(a: dict) -> dict:
    vi = vindex()
    if vi is None:
        return _text(f"No semantic index at {INDEX_DIR}. Search uses BM25 only. Build once: AVALAI_API_KEY=… AVALAI_EMBED_MODEL=<embedding model> python3 mcp-server/build_index.py")
    c = corpus()
    cur = {chunk_id(ch) for ch in c.chunks}
    have = set(vi.ids)
    return _text(json.dumps({"model": vi.meta.get("model"), "dim": vi.dim, "dimensions_param": vi.meta.get("dimensions"),
                             "built_at": vi.meta.get("built_at"), "chunks_in_index": len(have), "chunks_in_docs": len(cur),
                             "missing_from_index": len(cur - have), "stale_in_index": len(have - cur),
                             "hint": "run build_index.py again (incremental) if missing/stale > 0"}, indent=1))


def t_get_page(a: dict) -> dict:
    path = a.get("path", "")
    pg = corpus().pages.get(path)
    if not pg:
        cands = [r for r in corpus().pages if path and path.lower() in r.lower()][:10]
        return _err(f"No such page {path!r}. Similar: {cands}")
    text = pg.text
    sec = a.get("section")
    if sec:
        lines, keep, level, on = text.split("\n"), [], 0, False
        in_fence = False
        for ln in lines:
            if ln.startswith("```"):
                in_fence = not in_fence
            m = None if in_fence else re.match(r"^(#{1,6}) (.+)$", ln)
            if m:
                if on and len(m.group(1)) <= level:
                    break
                if not on and sec.lower() in m.group(2).lower():
                    on, level = True, len(m.group(1))
            if on:
                keep.append(ln)
        if not keep:
            return _err(f"Section {sec!r} not found in {path}")
        text = "\n".join(keep)
    off, mx = int(a.get("offset", 0)), int(a.get("max_chars", 12000))
    chunk = text[off: off + mx]
    tail = f"\n\n[… {len(text) - off - mx} more chars; call again with offset={off + mx}]" if off + mx < len(text) else ""
    return _text(f"# {pg.title}  ({pg.rel}, {len(text)} chars)\n\n{chunk}{tail}")


def t_list_pages(a: dict) -> dict:
    flt = a.get("filter", "").lower()
    kind = a.get("kind", "all")
    rows = [f"- `{p.rel}` — {p.title}" for p in corpus().pages.values()
            if (kind == "all" or p.kind == kind) and (not flt or flt in p.rel.lower() or flt in p.title.lower())]
    return _text(f"{len(rows)} pages\n" + "\n".join(rows[: int(a.get("limit", 200))]))


FENCE_RE = re.compile(r"```([A-Za-z0-9_+\-]*)\n(.*?)```", re.S)


def t_code_samples(a: dict) -> dict:
    lang = a.get("language", "").lower()
    q = tokenize(a.get("query", ""))
    lang_alias = {"js": "javascript", "node": "javascript", "ts": "typescript", "sh": "bash", "curl": "bash", "laravel": "php"}
    lang = lang_alias.get(lang, lang)
    hits = []
    for pg in corpus().pages.values():
        for m in FENCE_RE.finditer(pg.text):
            l, code = m.group(1).lower(), m.group(2)
            if lang and l != lang:
                continue
            low = code.lower()
            sc = sum(1 for t in set(q) if t in low) + sum(2 for t in set(q) if t in pg.title.lower())
            if sc and (len(code) > 60):
                hits.append((sc + (0.5 if pg.kind == "curated" else 0), pg, l, code))
    hits.sort(key=lambda x: -x[0])
    if not hits:
        return _text("No code samples matched. Try avalai_search or another language.")
    out = []
    for sc, pg, l, code in hits[: int(a.get("limit", 4))]:
        out.append(f"### {pg.title} (`{pg.rel}`)\n```{l}\n{code.rstrip()[:int(a.get('max_chars', 3500))]}\n```")
    out.append("\nSamples may be stale/broken (see notes in the page). Verify model ids with avalai_check_models. PHP/Laravel vetted code: examples/laravel-complete-guide.md")
    return _text("\n\n".join(out))


def t_models(a: dict) -> dict:
    ms = live_models()
    rows, n = [], 0
    for m in ms:
        if a.get("grep") and not re.search(a["grep"], m["id"], re.I):
            continue
        if a.get("mode") and m.get("mode") != a["mode"]:
            continue
        if a.get("max_tier") is not None and m.get("min_tier", 0) > int(a["max_tier"]):
            continue
        n += 1
        if n <= int(a.get("limit", 60)):
            pr = ", ".join(f"{k}={v}" for k, v in sorted(m.get("pricing", {}).items()))
            rows.append(f"{m['id']} | {m.get('mode','')} | T{m.get('min_tier','?')} | {pr}")
    return _text(f"{n} matching models (USD per 1M tokens unless per image/page/second/query); showing {len(rows)}\n" + "\n".join(rows))


def _find(ms: list[dict], mid: str) -> dict | None:
    return next((m for m in ms if m["id"] == mid), None)


def t_price(a: dict) -> dict:
    ms = live_models()
    out = []
    for mid in a.get("ids", []):
        m = _find(ms, mid)
        if not m:
            out.append(f"{mid}: NOT in live catalog (removed/renamed). Use avalai_deprecation.")
            continue
        d = {k: m.get(k) for k in ("id", "owned_by", "mode", "min_tier", "pricing", "max_input_tokens", "max_output_tokens", "supported_endpoints")}
        lim = "; ".join(f"T{t}: {v.get('max_requests_per_1_minute')} RPM / {v.get('max_tokens_per_1_minute')} TPM"
                        for t, v in sorted((m.get("tier_rate_limits") or {}).items()))
        out.append(json.dumps(d, ensure_ascii=False, indent=1) + "\nlimits: " + lim)
    return _text("\n\n".join(out))


def t_cost(a: dict) -> dict:
    m = _find(live_models(), a["model"])
    if not m:
        return _err(f"{a['model']} not in live catalog")
    try:
        usd, rates = compute_cost(m, int(a["input_tokens"]), int(a["output_tokens"]),
                                  int(a.get("cached_tokens", 0)), int(a.get("reasoning_tokens", 0)))
    except ValueError as e:
        return _err(str(e))
    lines = [f"model={a['model']} applied rates (USD/1M): {json.dumps(rates)}",
             f"per request: ${usd:.6f}"]
    if a.get("toman_rate"):
        lines.append(f"≈ {usd * float(a['toman_rate']):,.2f} toman @ {float(a['toman_rate']):,.0f} toman/USD (use TODAY's rate)")
    if a.get("requests"):
        lines.append(f"× {int(a['requests']):,} requests = ${usd * int(a['requests']):,.2f}")
    lines.append("Long-context band applies to the whole request when input > threshold; reasoning tokens bill at the output rate; "
                 "exact billing: POST /user/v1/transactions/lookup with avalai-request-id.")
    return _text("\n".join(lines))


def t_check(a: dict) -> dict:
    ids = a.get("ids", [])
    try:
        ms = live_models()
    except RuntimeError as e:
        return _err(str(e))
    out = []
    for mid in ids:
        m = _find(ms, mid)
        if m:
            out.append(f"OK       {mid}  min_tier={m.get('min_tier')} mode={m.get('mode')} endpoints={m.get('supported_endpoints')}")
        else:
            hint = _deprecation_hint(mid)
            out.append(f"MISSING  {mid}  → not served now. {hint}")
    return _text("\n".join(out))


def _deprecation_hint(term: str) -> str:
    pg = corpus().pages.get("10b-deprecations-complete.md")
    if not pg:
        return ""
    lines = [ln.strip() for ln in pg.text.split("\n") if term.lower() in ln.lower()]
    return ("Docs: " + " | ".join(lines[:3])[:400]) if lines else "Not found in deprecation list (maybe a typo/new id)."


def t_deprecation(a: dict) -> dict:
    term = a.get("query", "")
    pg = corpus().pages.get("10b-deprecations-complete.md")
    hits = [ln.strip() for ln in (pg.text.split("\n") if pg else []) if term.lower() in ln.lower()]
    extra = corpus().pages.get("10-deprecations.md")
    ex = [ln.strip() for ln in (extra.text.split("\n") if extra else []) if term.lower() in ln.lower()]
    if not hits and not ex:
        return _text(f"{term!r} not in deprecation docs. Check live: avalai_check_models.")
    return _text("From complete list:\n" + "\n".join(hits[:25]) + "\n\nFrom curated summary:\n" + "\n".join(ex[:15]))


def t_news(a: dict) -> dict:
    slug = a.get("slug")
    if slug:
        for rel, pg in corpus().pages.items():
            if rel.startswith("news/") and slug in rel:
                return _text(pg.text)
        return _err(f"news {slug!r} not captured locally; see news/index.md for the URL https://docs.avalai.ir/fa/news/<slug>")
    idx = corpus().pages.get("news/index.md")
    lines = [ln for ln in (idx.text.split("\n") if idx else []) if ln.startswith("| `")]
    return _text("\n".join(lines[: int(a.get("limit", 25))]))


def t_starters(a: dict) -> dict:
    name = a.get("name")
    pages = {r: p for r, p in corpus().pages.items() if r.startswith("starters/") and r != "starters/README.md"}
    if not name:
        return _text("Project starters (full blueprints; pass name to read one):\n" + "\n".join(f"- {r[9:-3]}: {p.title}" for r, p in pages.items())
                     + "\n\n" + corpus().pages["starters/README.md"].text)
    for r, p in pages.items():
        if name.lower() in r.lower():
            return _text(p.text)
    return _err(f"unknown starter {name!r}; call without name to list")


TOOLS = {
    "avalai_starters": (t_starters, "Ready-to-run project blueprints on AvalAI (FastAPI RAG, Next.js streaming chat, Telegram bot, Laravel chat, Node agent CLI, OCR→JSON, voice assistant). Call without name to list. Use when the user wants to build an app.",
                        {"type": "object", "properties": {"name": {"type": "string"}}}),
    "avalai_search": (t_search, "Hybrid semantic + keyword search (BM25 + embeddings via RRF when the index exists; BM25 otherwise) across AvalAI docs: curated references + verbatim source archive. Use for any 'how/what/which parameter/price/limit' question.",
                      {"type": "object", "properties": {
                          "query": {"type": "string", "description": "Keywords: model ids, parameter names, Persian or English"},
                          "scope": {"type": "string", "enum": ["all", "curated", "archive"], "default": "all"},
                          "mode": {"type": "string", "enum": ["auto", "hybrid", "semantic", "bm25"], "default": "auto",
                                   "description": "auto = hybrid (BM25+embeddings) when an index and AVALAI_API_KEY exist, else BM25"},
                          "limit": {"type": "integer", "default": 8}, "snippet_chars": {"type": "integer", "default": 900}},
                          "required": ["query"]}),
    "avalai_index_status": (t_index_status, "Status of the optional semantic (embeddings) index: model, dimensions, freshness.",
                            {"type": "object", "properties": {}}),
    "avalai_get_page": (t_get_page, "Read a docs page by path (from search results) in slices, or just one section by heading text.",
                        {"type": "object", "properties": {"path": {"type": "string"}, "section": {"type": "string"},
                                                          "offset": {"type": "integer", "default": 0}, "max_chars": {"type": "integer", "default": 12000}},
                         "required": ["path"]}),
    "avalai_list_pages": (t_list_pages, "List available docs pages (filter by substring of path/title; kind curated|archive).",
                          {"type": "object", "properties": {"filter": {"type": "string"}, "kind": {"type": "string", "enum": ["all", "curated", "archive"]},
                                                            "limit": {"type": "integer", "default": 200}}}),
    "avalai_code_samples": (t_code_samples, "Find code samples from the docs by topic and language (python, javascript, bash, php, go, ...). For Laravel use language=php.",
                            {"type": "object", "properties": {"query": {"type": "string"}, "language": {"type": "string"},
                                                              "limit": {"type": "integer", "default": 4}, "max_chars": {"type": "integer", "default": 3500}},
                             "required": ["query"]}),
    "avalai_models": (t_models, "LIVE model catalog from AvalAI /public/models (no key). Filter by regex grep, mode (chat, embedding, image_generation, video_generation, audio_speech, audio_transcription, ocr, rerank, search), max_tier.",
                      {"type": "object", "properties": {"grep": {"type": "string"}, "mode": {"type": "string"},
                                                        "max_tier": {"type": "integer"}, "limit": {"type": "integer", "default": 60}}}),
    "avalai_price": (t_price, "LIVE price, context limits, endpoints and per-tier RPM/TPM for exact model ids.",
                     {"type": "object", "properties": {"ids": {"type": "array", "items": {"type": "string"}}}, "required": ["ids"]}),
    "avalai_cost": (t_cost, "LIVE cost estimate for one request (and N requests, toman). Handles long-context bands, cached input, reasoning tokens.",
                    {"type": "object", "properties": {"model": {"type": "string"}, "input_tokens": {"type": "integer"}, "output_tokens": {"type": "integer"},
                                                      "cached_tokens": {"type": "integer", "default": 0}, "reasoning_tokens": {"type": "integer", "default": 0},
                                                      "requests": {"type": "integer"}, "toman_rate": {"type": "number", "description": "toman per USD, TODAY's rate"}},
                     "required": ["model", "input_tokens", "output_tokens"]}),
    "avalai_check_models": (t_check, "Are these model ids served right now? Adds deprecation hint from docs when missing.",
                            {"type": "object", "properties": {"ids": {"type": "array", "items": {"type": "string"}}}, "required": ["ids"]}),
    "avalai_deprecation": (t_deprecation, "Look up a model id/keyword in the complete deprecated-models list + curated migration notes.",
                           {"type": "object", "properties": {"query": {"type": "string"}}, "required": ["query"]}),
    "avalai_news": (t_news, "List AvalAI news (newest first, with slugs) or read a captured news item by slug fragment.",
                    {"type": "object", "properties": {"slug": {"type": "string"}, "limit": {"type": "integer", "default": 25}}}),
}

PROMPTS = {
    "avalai_integration_review": ("Review code that calls AvalAI against best practices.",
                                  [{"name": "code_or_path", "description": "Code or file path to review", "required": True}],
                                  "Review the following AvalAI integration. First call avalai_search for the relevant topics (errors, rate limits, streaming, tools), "
                                  "avalai_check_models for every model id used, and avalai_price for costs. Report: wrong base URL (/v1 vs none), key handling, retries/timeouts, "
                                  "avalai-request-id logging, deprecated ids, missing tool-arg validation, cost risks. Subject:\n\n{code_or_path}"),
    "avalai_cost_plan": ("Plan monthly cost + throughput for a workload.",
                         [{"name": "workload", "description": "Requests/day, token sizes, models, tier", "required": True}],
                         "Plan cost and rate-limit headroom for: {workload}\nUse avalai_price (tier limits) and avalai_cost per model; include cache/reasoning effects, "
                         "long-context bands and a toman estimate (ask for today's rate). Give a table and a recommendation."),
    "avalai_migrate_model": ("Migrate away from a deprecated/removed model id.",
                             [{"name": "model", "description": "Old model id", "required": True}],
                             "Migrate off {model}: use avalai_deprecation and avalai_check_models, propose replacements with avalai_price, list behavior differences "
                             "(params, endpoints, tool/thinking rules) and give a test plan."),
}


# ----------------------------------------------------------------------------- JSON-RPC
def handle(msg: dict) -> dict | None:
    mid, method, params = msg.get("id"), msg.get("method"), msg.get("params") or {}

    def ok(result):
        return {"jsonrpc": "2.0", "id": mid, "result": result}

    def fail(code, message):
        return {"jsonrpc": "2.0", "id": mid, "error": {"code": code, "message": message}}

    if method == "initialize":
        return ok({"protocolVersion": params.get("protocolVersion", "2024-11-05"),
                   "capabilities": {"tools": {}, "resources": {}, "prompts": {}},
                   "serverInfo": {"name": SERVER_NAME, "version": SERVER_VERSION},
                   "instructions": "AvalAI knowledge base. For any price/model/limit use the live tools (avalai_price/avalai_cost/avalai_check_models); "
                                   "use avalai_search + avalai_get_page for documentation; never quote prices from memory."})
    if method in ("notifications/initialized", "notifications/cancelled") or (method or "").startswith("notifications/"):
        return None
    if method == "ping":
        return ok({})
    if method == "tools/list":
        return ok({"tools": [{"name": n, "description": d, "inputSchema": s} for n, (_, d, s) in TOOLS.items()]})
    if method == "tools/call":
        name, args = params.get("name"), params.get("arguments") or {}
        if name not in TOOLS:
            return fail(-32602, f"unknown tool {name}")
        try:
            return ok(TOOLS[name][0](args))
        except KeyError as e:
            return ok(_err(f"missing argument: {e}"))
        except Exception as e:  # never crash the server
            return ok(_err(f"{type(e).__name__}: {e}"))
    if method == "resources/list":
        return ok({"resources": [{"uri": f"avalai://ref/{p.rel}", "name": p.title, "mimeType": "text/markdown"}
                                 for p in corpus().pages.values() if p.kind == "curated"]})
    if method == "resources/read":
        uri = params.get("uri", "")
        rel = uri.replace("avalai://ref/", "", 1)
        pg = corpus().pages.get(rel)
        if not pg:
            return fail(-32002, f"resource not found: {uri}")
        return ok({"contents": [{"uri": uri, "mimeType": "text/markdown", "text": pg.text}]})
    if method == "prompts/list":
        return ok({"prompts": [{"name": n, "description": d, "arguments": a} for n, (d, a, _) in PROMPTS.items()]})
    if method == "prompts/get":
        n = params.get("name")
        if n not in PROMPTS:
            return fail(-32602, f"unknown prompt {n}")
        d, a, tpl = PROMPTS[n]
        args = params.get("arguments") or {}
        text = tpl
        for k, v in args.items():
            text = text.replace("{" + k + "}", str(v))
        return ok({"description": d, "messages": [{"role": "user", "content": {"type": "text", "text": text}}]})
    if mid is None:
        return None
    return fail(-32601, f"method not found: {method}")


def serve() -> None:
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        try:
            msg = json.loads(line)
        except json.JSONDecodeError:
            sys.stdout.write(json.dumps({"jsonrpc": "2.0", "id": None, "error": {"code": -32700, "message": "parse error"}}) + "\n")
            sys.stdout.flush()
            continue
        for m in (msg if isinstance(msg, list) else [msg]):
            resp = handle(m)
            if resp is not None:
                sys.stdout.write(json.dumps(resp, ensure_ascii=False) + "\n")
                sys.stdout.flush()


def selftest() -> None:
    os.environ["AVALAI_MCP_OFFLINE"] = "1"
    fx = {"data": [{"id": "x-sol", "mode": "chat", "min_tier": 1,
                    "pricing": {"input": 2.0, "cached_input": 0.1, "output": 10.0, "input_above_272K": 4.0, "cached_input_above_272K": 0.2, "output_above_272K": 15.0},
                    "tier_rate_limits": {"1": {"max_requests_per_1_minute": 5, "max_tokens_per_1_minute": 9}}}]}
    import tempfile
    tmp = Path(tempfile.gettempdir()) / "avalai_mcp_fixture.json"
    tmp.write_text(json.dumps(fx))
    os.environ["AVALAI_MODELS_FILE"] = str(tmp)
    r = handle({"jsonrpc": "2.0", "id": 1, "method": "initialize", "params": {"protocolVersion": "2025-03-26"}})
    assert r["result"]["serverInfo"]["name"] == SERVER_NAME
    names = {t["name"] for t in handle({"jsonrpc": "2.0", "id": 2, "method": "tools/list"})["result"]["tools"]}
    assert "avalai_search" in names and "avalai_cost" in names, names
    c = handle({"jsonrpc": "2.0", "id": 3, "method": "tools/call", "params": {"name": "avalai_cost", "arguments": {"model": "x-sol", "input_tokens": 100, "output_tokens": 50}}})
    assert "0.000700" in c["result"]["content"][0]["text"], c
    c = handle({"jsonrpc": "2.0", "id": 4, "method": "tools/call", "params": {"name": "avalai_cost", "arguments": {"model": "x-sol", "input_tokens": 272001, "output_tokens": 0}}})
    assert "1.088004" in c["result"]["content"][0]["text"], c
    s = handle({"jsonrpc": "2.0", "id": 5, "method": "tools/call", "params": {"name": "avalai_search", "arguments": {"query": "avalai-request-id header migration"}}})
    assert "request" in s["result"]["content"][0]["text"].lower()
    k = handle({"jsonrpc": "2.0", "id": 6, "method": "tools/call", "params": {"name": "avalai_code_samples", "arguments": {"query": "chat completions", "language": "php"}}})
    assert "```php" in k["result"]["content"][0]["text"]
    d = handle({"jsonrpc": "2.0", "id": 7, "method": "tools/call", "params": {"name": "avalai_deprecation", "arguments": {"query": "imagen"}}})
    assert "imagen" in d["result"]["content"][0]["text"].lower()
    rr = handle({"jsonrpc": "2.0", "id": 8, "method": "resources/list"})
    assert len(rr["result"]["resources"]) > 50
    assert handle({"jsonrpc": "2.0", "id": 9, "method": "prompts/get", "params": {"name": "avalai_cost_plan", "arguments": {"workload": "W"}}})["result"]["messages"]
    # semantic pipeline with fake vectors (offline)
    import tempfile
    global INDEX_DIR, _VINDEX
    old_dir, INDEX_DIR, _VINDEX = INDEX_DIR, Path(tempfile.mkdtemp()), None
    os.environ.update(AVALAI_EMBED_FAKE="1", AVALAI_EMBED_MODEL="fake-hash")
    chunks = corpus().chunks[:300]
    ids = [chunk_id(c) for c in chunks]
    vecs = [_normalize(v) for v in embed_texts([chunk_input(c) for c in chunks])]
    (INDEX_DIR / "vectors.f16").write_bytes(b"".join(struct.pack(f"<{len(v)}e", *v) for v in vecs))
    (INDEX_DIR / "meta.json").write_text(json.dumps({"model": "fake-hash", "dim": len(vecs[0]), "dimensions": None, "ids": ids}))
    res, used = hybrid_search("rate limit retry", 3, "all", "auto")
    assert res and used.startswith("hybrid"), used
    st = handle({"jsonrpc": "2.0", "id": 10, "method": "tools/call", "params": {"name": "avalai_starters", "arguments": {}}})
    assert "fastapi-chat-rag" in st["result"]["content"][0]["text"]
    INDEX_DIR, _VINDEX = old_dir, None
    print(f"selftest OK ({len(corpus().pages)} pages, {len(corpus().chunks)} chunks)")


if __name__ == "__main__":
    if "--selftest" in sys.argv:
        selftest()
    else:
        serve()
