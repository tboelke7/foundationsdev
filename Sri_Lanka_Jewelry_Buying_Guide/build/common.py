"""Shared helpers: data loading, price parsing, band grouping."""
import json, os, re, glob, html
from content import (CATEGORIES, BAND_LABELS, BANDED_ORDER, GENERIC_ORDER,
                     BAND_DESC, SPEC_FIELDS)
import econ

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
DATA = os.path.join(ROOT, "data")

NA = {"", "not disclosed", "n/a", "na", "none", "none noted", "not shown",
      "not stated", "unknown", "not specified"}


def esc(x):
    return html.escape(str(x if x is not None else ""))


def is_na(v):
    return v is None or str(v).strip().lower() in NA


def show(v):
    """Display value, turning blanks into 'not disclosed'."""
    return "not disclosed" if is_na(v) else str(v).strip()


def money(s):
    """Extract the first plausible USD amount from a string; None if absent."""
    if s is None:
        return None
    s = str(s)
    m = re.search(r"(\d[\d,]*\.?\d*)", s.replace(",", ""))
    if not m:
        return None
    try:
        val = float(m.group(1))
    except ValueError:
        return None
    return val if val > 0 else None


def norm_band(cat, raw):
    """Map an agent's band string to a canonical key for the category."""
    b = (raw or "").strip().lower()
    if cat in ("moonstone", "sapphire"):
        for k in BANDED_ORDER:
            if b == k.lower():
                return k
        return "B"  # fallback middle
    for k in GENERIC_ORDER:
        if b.startswith(k):
            return k
    # crude fallback by price handled later
    return "middle"


def load_category(cat):
    path = os.path.join(DATA, f"{cat}.json")
    if not os.path.exists(path):
        return []
    with open(path) as f:
        recs = json.load(f)
    for r in recs:
        r["_price"] = money(r.get("price_current"))
        r["_list"] = money(r.get("price_list"))
        r["_band"] = norm_band(cat, r.get("band"))
        r["_cat"] = cat
    return recs


def load_all():
    out = {}
    for c in CATEGORIES:
        out[c["key"]] = load_category(c["key"])
    return out


def band_order(cat):
    return BANDED_ORDER if cat in ("moonstone", "sapphire") else GENERIC_ORDER


def group_by_band(cat, recs):
    order = band_order(cat)
    groups = {b: [] for b in order}
    for r in recs:
        b = r["_band"]
        groups.setdefault(b, []).append(r)
    # sort each band's records by price (priced first, ascending)
    for b in groups:
        groups[b].sort(key=lambda r: (r["_price"] is None, r["_price"] or 0))
    return [(b, groups[b]) for b in order if groups.get(b)]
