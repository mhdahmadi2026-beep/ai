#!/usr/bin/env python3
"""Build / refresh the semantic index for the AvalAI MCP server (incremental, resumable).

  export AVALAI_API_KEY=...
  python3 build_index.py --list-models                  # embedding models available to you (live)
  python3 build_index.py --model <embedding-model> --dry-run          # chunk count + token/cost estimate
  python3 build_index.py --model <embedding-model> [--dimensions 512]  # build (only new/changed chunks are embedded)
  python3 build_index.py --fake                          # offline demo vectors (NOT semantic) for testing

Output: index/meta.json + index/vectors.f16 (float16, L2-normalised). Commit them to share the index
(512-dim ≈ 6.6 MB for ~6.4k chunks). The server then runs hybrid search automatically; set the SAME
AVALAI_EMBED_MODEL (+ AVALAI_EMBED_DIMENSIONS) and AVALAI_API_KEY for query-time embedding.
"""
import argparse, json, os, struct, sys, time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import avalai_mcp as M


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--model", default=os.environ.get("AVALAI_EMBED_MODEL"))
    ap.add_argument("--dimensions", type=int, default=int(os.environ.get("AVALAI_EMBED_DIMENSIONS", "0")) or None)
    ap.add_argument("--batch", type=int, default=48)
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--list-models", action="store_true")
    ap.add_argument("--fake", action="store_true", help="hashed vectors for tests (no network)")
    ap.add_argument("--rebuild", action="store_true", help="ignore existing vectors")
    a = ap.parse_args()

    if a.list_models:
        for m in M.live_models():
            if m.get("mode") == "embedding":
                print(m["id"], m.get("pricing"), "max_in", m.get("max_input_tokens"), "T", m.get("min_tier"))
        return
    if a.fake:
        os.environ["AVALAI_EMBED_FAKE"] = "1"
        a.model = a.model or "fake-hash"
    if not a.model:
        sys.exit("need --model (see --list-models) or AVALAI_EMBED_MODEL")
    os.environ["AVALAI_EMBED_MODEL"] = a.model

    corpus = M.corpus()
    chunks = corpus.chunks
    ids = [M.chunk_id(c) for c in chunks]
    old = {}
    old_meta = None
    if not a.rebuild and (M.INDEX_DIR / "meta.json").exists():
        vi = M.VectorIndex()
        if vi.load() and vi.meta.get("model") == a.model and vi.dim == (a.dimensions or vi.dim) or (vi.meta and vi.meta.get("model") == a.model and not a.dimensions):
            old_meta = vi.meta
            for cid, p in vi.pos.items():
                row = vi.mat[p]
                old[cid] = [float(x) for x in row]
    todo = [i for i, cid in enumerate(ids) if cid not in old]
    chars = sum(len(M.chunk_input(chunks[i])) for i in todo)
    est_tokens = int(chars / 3.2)  # conservative for mixed Persian/English/code
    print(f"chunks: {len(chunks)} | reuse: {len(chunks) - len(todo)} | to embed: {len(todo)} | ~{est_tokens:,} tokens")
    try:
        mm = next((m for m in M.live_models() if m["id"] == a.model), None)
        if mm and "input" in mm.get("pricing", {}):
            print(f"estimated cost ~ ${est_tokens * mm['pricing']['input'] / 1e6:.4f} at ${mm['pricing']['input']}/1M tokens (live price; verify)")
    except Exception as e:
        print(f"(live price unavailable: {str(e)[:80]})")
    if a.dry_run:
        return

    vecs: dict[str, list[float]] = dict(old)
    t0 = time.time()
    for s in range(0, len(todo), a.batch):
        part = todo[s:s + a.batch]
        out = M.embed_texts([M.chunk_input(chunks[i]) for i in part], a.dimensions)
        for i, v in zip(part, out):
            vecs[ids[i]] = M._normalize(v)
        done = s + len(part)
        print(f"  embedded {done}/{len(todo)}  ({time.time() - t0:.0f}s)", flush=True)
    dim = len(next(iter(vecs.values())))
    M.INDEX_DIR.mkdir(parents=True, exist_ok=True)
    with open(M.INDEX_DIR / "vectors.f16", "wb") as f:
        for cid in ids:
            f.write(struct.pack(f"<{dim}e", *vecs[cid]))
    meta = {"model": a.model, "dim": dim, "dimensions": a.dimensions, "built_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
            "count": len(ids), "ids": ids, "fake": bool(a.fake)}
    (M.INDEX_DIR / "meta.json").write_text(json.dumps(meta), encoding="utf-8")
    print(f"wrote {M.INDEX_DIR} ({len(ids)} vectors × {dim} dims, {(M.INDEX_DIR / 'vectors.f16').stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
