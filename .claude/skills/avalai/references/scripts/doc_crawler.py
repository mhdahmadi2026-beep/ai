#!/usr/bin/env python3
"""Crawler for AvalAI docs: news pages and model pages."""
import json, os, re, subprocess, sys, time

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
NEWS_DIR = os.path.join(BASE_DIR, "news")
MODELS_DIR = os.path.join(BASE_DIR, "models")
SOURCE_ARCHIVE_DIR = os.path.join(BASE_DIR, "source-archive")
LIVE_CATALOG_FILE = os.path.join(BASE_DIR, "live", "public-models-2026-10-07.json")

os.makedirs(NEWS_DIR, exist_ok=True)
os.makedirs(MODELS_DIR, exist_ok=True)
os.makedirs(os.path.join(SOURCE_ARCHIVE_DIR, "news"), exist_ok=True)
os.makedirs(os.path.join(SOURCE_ARCHIVE_DIR, "models"), exist_ok=True)

# Load live catalog
with open(LIVE_CATALOG_FILE, encoding="utf-8") as f:
    LIVE_MODELS = {m["id"]: m for m in json.load(f)["data"]}

def fetch_markdown(url):
    """Fetch raw markdown using curl with interface binding."""
    cmd = ["curl.exe", "--interface", "192.168.1.177", "-s", "--connect-timeout", "10", url]
    try:
        res = subprocess.check_output(cmd, stderr=subprocess.DEVNULL)
        text = res.decode("utf-8", errors="replace")
        if text.startswith("---") or "# " in text:
            return text
        return None
    except Exception as e:
        return None

def process_news_page(slug, raw_md):
    """Generate a clean, faithful reference markdown file from raw news markdown."""
    # Save verbatim in source-archive
    archive_path = os.path.join(SOURCE_ARCHIVE_DIR, "news", f"{slug}.md")
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write(raw_md)

    lines = raw_md.splitlines()
    title = slug
    date_str = ""
    for line in lines:
        if line.startswith("# "):
            title = line.lstrip("# ").strip()
        elif "**تاریخ:**" in line or "**تاریخ" in line:
            date_str = line.strip()

    # Extract clean text without HTML tags
    clean_lines = []
    in_frontmatter = False
    frontmatter_count = 0
    for line in lines:
        if line.strip() == "---":
            frontmatter_count += 1
            if frontmatter_count <= 2:
                in_frontmatter = (frontmatter_count == 1)
                continue
        if in_frontmatter:
            continue
        # Remove noisy HTML divs/styles if any
        if line.strip().startswith("<div") or line.strip().startswith("</div>") or line.strip().startswith("<style"):
            continue
        clean_lines.append(line)

    body = "\n".join(clean_lines).strip()
    
    header = f"# News {slug}: {title}\nURL: `https://docs.avalai.ir/fa/news/{slug}`\n{date_str}\n\n"
    ref_content = header + body + "\n"
    
    ref_path = os.path.join(NEWS_DIR, f"{slug}.md")
    with open(ref_path, "w", encoding="utf-8") as f:
        f.write(ref_content)
    return True

def process_model_page(model_id, raw_md):
    """Generate a comprehensive model reference from model page markdown and live catalog."""
    archive_path = os.path.join(SOURCE_ARCHIVE_DIR, "models", f"{model_id}.md")
    with open(archive_path, "w", encoding="utf-8") as f:
        f.write(raw_md)

    # Parse frontmatter componentData if present
    comp = {}
    m_json = re.search(r"componentData:\s*(\{.+?\})\s*\n---", raw_md, re.DOTALL)
    if m_json:
        try:
            comp = json.loads(m_json.group(1)).get("model", {})
        except Exception:
            pass

    live = LIVE_MODELS.get(model_id, {})
    comp = comp or {}
    ext = comp.get("external") or {}
    pricing_info = comp.get("pricing") or live.get("pricing") or {}
    caps = comp.get("capabilities") or []
    specs = comp.get("specifications") or {}

    owner = live.get("owned_by", comp.get("owner", "unknown"))
    mode = live.get("mode", "chat")
    min_tier = live.get("min_tier", 0)
    endpoints = live.get("supported_endpoints", ["/v1/chat/completions"])
    max_in = live.get("max_input_tokens") or specs.get("maxInputTokens") or ext.get("contextLength") or "N/A"
    max_out = live.get("max_output_tokens") or specs.get("maxOutputTokens") or ext.get("maxCompletionTokens") or "N/A"

    doc_lines = [
        f"# Model: `{model_id}`",
        f"URL: `https://docs.avalai.ir/fa/models/{model_id}` · Provider: `{owner}` · Mode: `{mode}` · Min Tier: `{min_tier}`",
        "",
        "## Overview & Token Limits",
        f"- **Max input tokens (Context)**: `{max_in:,}`" if isinstance(max_in, int) else f"- **Max input tokens**: `{max_in}`",
        f"- **Max output tokens**: `{max_out:,}`" if isinstance(max_out, int) else f"- **Max output tokens**: `{max_out}`",
        f"- **Endpoints supported**: {', '.join(f'`{e}`' for e in endpoints)}",
        "",
        "## Pricing (USD per 1M tokens)",
        "| Metric | Rate ($/1M) |",
        "|---|---:|",
    ]

    p_dict = live.get("pricing", {})
    if not p_dict and isinstance(ext.get("pricing"), dict):
        p_dict = ext["pricing"]

    for k, v in sorted(p_dict.items()):
        doc_lines.append(f"| `{k}` | ${v} |")

    # Long-context overrides
    ext_pricing = ext.get("pricing") if isinstance(ext.get("pricing"), dict) else {}
    overrides = ext_pricing.get("overrides") if isinstance(ext_pricing.get("overrides"), list) else []
    if overrides:
        doc_lines.extend(["", "### Long-context Tier Overrides", "| Threshold (tokens) | Prompt ($/1M) | Completion ($/1M) | Cache Read ($/1M) |", "|---|---:|---:|---:|"])
        for ov in overrides:
            doc_lines.append(f"| >{ov.get('minPromptTokens', 0):,} | ${float(ov.get('prompt', 0))*1e6:.2f} | ${float(ov.get('completion', 0))*1e6:.2f} | ${float(ov.get('inputCacheRead', 0))*1e6:.2f} |")

    # Capabilities
    if caps:
        doc_lines.extend(["", "## Capabilities", ", ".join(f"`{c}`" for c in sorted(caps))])

    # Rate limits per tier
    tier_limits = live.get("tier_rate_limits", {})
    if tier_limits:
        doc_lines.extend(["", "## Tier Rate Limits", "| Tier | RPM | TPM |", "|---|---:|---:|"])
        for t, lim in sorted(tier_limits.items(), key=lambda x: int(x[0])):
            doc_lines.append(f"| Tier {t} | {lim.get('max_requests_per_1_minute', 'N/A'):,} | {lim.get('max_tokens_per_1_minute', 'N/A'):,} |")

    # FAQ or summary
    faq = comp.get("faq", [])
    if faq:
        doc_lines.extend(["", "## FAQ & Quirks"])
        for item in faq:
            doc_lines.append(f"- **{item.get('question')}**: {item.get('answer')}")

    ref_path = os.path.join(MODELS_DIR, f"{model_id}.md")
    with open(ref_path, "w", encoding="utf-8") as f:
        f.write("\n".join(doc_lines) + "\n")
    return True

if __name__ == "__main__":
    print("Crawler script ready.")
