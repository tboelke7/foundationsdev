#!/usr/bin/env python3
"""Lunar Gems top-picks buying doc: photo + expected purchase price + expected
U.S. sale price per piece. Local images embed as base64 so they render in the PDF."""
import os, base64, io, csv
from PIL import Image
from common import ROOT
import econ

LG = os.path.join(ROOT, "Lunar_Gems")
DATE = econ.RESEARCH_DATE

# --- Selection -------------------------------------------------------------
# retail_lo/hi = estimated U.S. RETAIL (sale) range, USD.
# buy_tgt = target fair acquisition cost in Sri Lanka (USD).
# buy_max = walk-away ceiling (~40-45% of retail_lo, the field-guide rule).
# All assume genuine blue-sheen Ceylon moonstone in STERLING SILVER with good
# flash, and BULK import (one insured shipment amortised across many pieces).
PICKS = [
    dict(img="LG-13", rank=1, name="Crescent-moon adjustable ring",
         type="Ring (adjustable)", retail=(75,140), buy=(18,30), buy_max=40,
         why="Celestial 'moon + moonstone' theme is a top seller; adjustable band removes sizing risk; vivid centred blue flash. Best all-round mover."),
    dict(img="LG-01", rank=2, name="Sea-turtle moonstone line bracelet (~8 ovals)",
         type="Bracelet (statement)", retail=(140,260), buy=(45,80), buy_max=95,
         why="Coastal/turtle motif + row of blue-flash ovals = giftable statement piece. Highest single-piece ticket among the silver items."),
    dict(img="LG-10", rank=3, name="Three-stone oval moonstone ring",
         type="Ring (3-stone)", retail=(90,160), buy=(25,45), buy_max=55,
         why="The strongest, most vivid blue flash in the batch; 3-stone layout reads as 'fine jewelry'. Premium look for a silver price."),
    dict(img="LG-06", rank=4, name="Open-heart pendant with moonstone",
         type="Pendant", retail=(60,120), buy=(15,28), buy_max=38,
         why="Universal giftable heart shape; blue cab pops against open silver. Easy Valentine's/Mother's Day/anniversary seller."),
    dict(img="LG-21", rank=5, name="Moonstone cross pendant (11 cabs)",
         type="Pendant", retail=(95,180), buy=(28,55), buy_max=65,
         why="Faith jewelry is a huge, steady U.S. category; a full moonstone cross is distinctive and higher perceived value."),
    dict(img="LG-16", rank=6, name="Art-deco fan ring (accent arc + moonstone)",
         type="Ring (statement)", retail=(85,160), buy=(22,42), buy_max=55,
         why="Distinctive deco/celestial 'rising sun' design with pavé-look arc; looks far more expensive than its cost. Good margin."),
    dict(img="LG-24", rank=7, name="Faceted oval moonstone solitaire ring",
         type="Ring (solitaire)", retail=(70,140), buy=(18,35), buy_max=45,
         why="Faceted (not cabochon) moonstone reads as an alt-bridal / engagement stone; strong blue through the facets. On-trend."),
    dict(img="LG-23", rank=8, name="Dainty moonstone stacking ring",
         type="Ring (dainty)", retail=(32,65), buy=(7,15), buy_max=22,
         why="Minimalist stacking rings sell in volume at low price; cheap to acquire, great multiples. Buy a size run."),
    dict(img="LG-08", rank=9, name="Oval moonstone ring, polished leaf shoulders",
         type="Ring (solitaire)", retail=(60,120), buy=(15,30), buy_max=40,
         why="Clean classic oval with strong blue flash; flattering everyday ring, broad appeal."),
    dict(img="LG-05", rank=10, name="S-swirl three-stone pendant",
         type="Pendant", retail=(60,120), buy=(15,30), buy_max=40,
         why="Artisan modern swirl with three cabs (one strong blue); design-forward without being niche."),
    dict(img="LG-11", rank=11, name="Bypass round moonstone ring",
         type="Ring (modern)", retail=(50,95), buy=(12,24), buy_max=32,
         why="Minimal open-bypass band with vivid blue round cab; trendy, low cost, easy multiples."),
    dict(img="LG-20", rank=12, name="Oval moonstone stud earrings",
         type="Earrings (studs)", retail=(35,70), buy=(9,18), buy_max=24,
         why="Everyday basics; pair with the rings/pendants as sets to lift average order value. Volume item."),
    dict(img="LG-07", rank=13, name="Oval moonstone ring with green accents",
         type="Ring (accent)", retail=(65,125), buy=(16,32), buy_max=42,
         why="Green side-accents (chrome-diopside look) add colour contrast and perceived value; stamped 925. Distinctive."),
    dict(img="LG-18", rank=14, name="Moonstone station necklace (~16 ovals)  [CONFIRM METAL]",
         type="Necklace (station)", retail=(170,330), buy=(80,150), buy_max=150,
         why="Best hero piece — a full moonstone 'by-the-yard' necklace. BUT it looks yellow gold/vermeil, not silver: if solid gold, retail is $700-1,600+ and cost is far higher. Confirm metal before pricing."),
]

NOTE_GOLD = ("LG-14 (yellow-gold ring with a colourless faceted stone) was excluded — it is not moonstone. "
             "LG-18 and the LG-22 pendants photograph as yellow gold / vermeil, not sterling; confirm the metal, "
             "as it changes both cost and resale materially.")

CSS = """
*{box-sizing:border-box}
body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#20242b;margin:0;background:#fff;font-size:13px;line-height:1.45}
.wrap{max-width:900px;margin:0 auto;padding:22px}
h1{font-family:Georgia,serif;font-size:24px;color:#123a4f;margin:0 0 4px}
.sub{color:#5b6472;font-size:13px;margin-bottom:6px}
.meta{font-size:11.5px;color:#8a8272;margin-bottom:16px}
.note{background:#f3e7c9;border:1px solid #e6d4a3;border-radius:9px;padding:10px 13px;font-size:12px;margin:12px 0}
.warn{background:#fbeeea;border:1px solid #e7c3b8;border-radius:9px;padding:10px 13px;font-size:12px;margin:12px 0}
table.sum{width:100%;border-collapse:collapse;font-size:11.5px;margin:10px 0 4px}
table.sum th,table.sum td{border:1px solid #e3ddd0;padding:5px 7px;text-align:right}
table.sum th{background:#123a4f;color:#fff;text-align:right}
table.sum td:nth-child(1),table.sum td:nth-child(2),table.sum th:nth-child(1),table.sum th:nth-child(2){text-align:left}
table.sum tr:nth-child(even) td{background:#faf8f3}
.card{display:flex;gap:14px;border:1px solid #e3ddd0;border-radius:12px;padding:12px;margin:12px 0;break-inside:avoid;background:#fff}
.card img{width:210px;height:210px;object-fit:cover;border-radius:9px;flex:0 0 auto;background:#f2eee6}
.cbody{flex:1;min-width:0}
.rk{display:inline-block;background:#b8862f;color:#fff;font-weight:700;font-size:11px;border-radius:5px;padding:1px 8px;margin-right:6px}
.nm{font-weight:700;font-size:15px;color:#123a4f;font-family:Georgia,serif}
.ty{color:#5b6472;font-size:11.5px;margin:2px 0 8px}
.prices{display:grid;grid-template-columns:1fr 1fr 1fr;gap:8px;margin:8px 0}
.pb{border:1px solid #e3ddd0;border-radius:8px;padding:7px 9px;text-align:center}
.pb .lb{font-size:10px;text-transform:uppercase;letter-spacing:.04em;color:#5b6472}
.pb .v{font-size:16px;font-weight:800;font-family:Georgia,serif}
.pb.sell .v{color:#1c7a4a}.pb.buy .v{color:#123a4f}.pb.max .v{color:#a5362d}
.mg{font-size:11.5px;color:#1c6b7d;font-weight:600;margin:4px 0}
.why{font-size:12px;color:#4a5260}
.foot{margin-top:22px;padding-top:12px;border-top:1px solid #e3ddd0;font-size:11px;color:#5b6472}
@media print{.wrap{max-width:none;padding:0 6mm}body{font-size:11.5px}}
"""

def data_uri(path, box=430, q=82):
    im = Image.open(path).convert("RGB")
    im.thumbnail((box, box))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

def mid(lo, hi): return round((lo+hi)/2)

def margin_note(p):
    r = mid(*p["retail"]); b = mid(*p["buy"])
    # bulk landed: buy + ~$6 amortised freight/duty + ~$2 pack
    landed = b + 6 + 2
    gm = (r - landed) / r if r else 0
    mult = r / landed if landed else 0
    return r, b, landed, gm, mult

def summary_table():
    rows = ""
    for p in PICKS:
        r, b, landed, gm, mult = margin_note(p)
        rows += (f"<tr><td>{p['rank']}. {p['name'].split('  [')[0]}</td><td>{p['type']}</td>"
                 f"<td>${p['retail'][0]}–${p['retail'][1]}</td>"
                 f"<td>${p['buy'][0]}–${p['buy'][1]}</td>"
                 f"<td>${p['buy_max']}</td>"
                 f"<td>~{gm*100:.0f}%</td><td>~{mult:.1f}×</td></tr>")
    return (f"<table class='sum'><tr><th>Piece</th><th>Type</th><th>Est. U.S. retail (sell)</th>"
            f"<th>Target buy (SL)</th><th>Max buy</th><th>Gross margin*</th><th>Markup*</th></tr>{rows}</table>")

def cards():
    out = ""
    for p in PICKS:
        r, b, landed, gm, mult = margin_note(p)
        uri = data_uri(os.path.join(LG, p["img"]+".jpg"))
        out += f"""<div class="card">
  <img src="{uri}" alt="{p['name']}">
  <div class="cbody">
    <div><span class="rk">#{p['rank']}</span><span class="nm">{p['name']}</span></div>
    <div class="ty">{p['type']} &middot; sterling silver (assumed) &middot; blue-sheen moonstone</div>
    <div class="prices">
      <div class="pb sell"><div class="lb">Expected U.S. sale</div><div class="v">${p['retail'][0]}–${p['retail'][1]}</div></div>
      <div class="pb buy"><div class="lb">Target buy price</div><div class="v">${p['buy'][0]}–${p['buy'][1]}</div></div>
      <div class="pb max"><div class="lb">Don't pay over</div><div class="v">${p['buy_max']}</div></div>
    </div>
    <div class="mg">Bulk-import margin: ~{gm*100:.0f}% gross &middot; ~{mult:.1f}× markup on ~${landed} landed cost (target buy + ~$8 amortised freight/duty/packaging)</div>
    <div class="why">{p['why']}</div>
  </div>
</div>"""
    return out

def build():
    html = f"""<!doctype html><html><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Lunar Gems — Top Picks & Pricing</title><style>{CSS}
@page{{size:A4 portrait;margin:11mm 9mm}}</style></head><body><div class="wrap">
<h1>Lunar Gems — Top Picks for the U.S. Market</h1>
<div class="sub">14 pieces with the best resale potential, with an estimated purchase price and expected U.S. sale price for each.</div>
<div class="meta">Prepared {DATE}. Prices are ESTIMATES for genuine blue-sheen Ceylon moonstone in sterling silver, benchmarked to the U.S. retail field guide. Compare the "target buy" to Lunar Gems' actual quote.</div>
<div class="note"><b>How to read this:</b> <b>Expected U.S. sale</b> is a realistic online retail range. <b>Target buy price</b> is a fair Sri-Lanka acquisition cost to aim for. <b>Don't pay over</b> is the walk-away ceiling (~40–45% of the low retail). Margins assume you <b>import in bulk</b> — one insured shipment amortised across many pieces (~$8/pc). Bought one-at-a-time, the ~$60 insured-courier minimum wipes out the margin on the cheaper silver pieces, so batch them.</div>
<div class="warn"><b>Metal check:</b> {NOTE_GOLD}</div>
<h3 style="font-family:Georgia,serif;color:#123a4f;margin:14px 0 2px">Quick summary</h3>
{summary_table()}
<div class="meta">*Gross margin &amp; markup are on landed cost at the mid target buy + ~$8 bulk freight/duty/packaging, sold at mid retail.</div>
{cards()}
<div class="foot">Estimates only, not an appraisal or guaranteed resale value. Asking/retail comparables are reference points; actual sell-through depends on listing quality, photography, and demand. Confirm each piece's metal purity (look for a 925 stamp), stone (natural blue-sheen moonstone vs milky/white), and Lunar Gems' real trade price and export/shipping terms before buying. Assumes genuine sterling silver; solid-gold pieces (e.g. LG-18) carry higher cost and higher resale.</div>
</div></body></html>"""
    out_html = os.path.join(ROOT, "Lunar_Gems_Top_Picks.html")
    open(out_html, "w").write(html)
    # CSV of picks
    with open(os.path.join(ROOT, "Lunar_Gems_Top_Picks.csv"), "w", newline="") as f:
        w = csv.writer(f)
        w.writerow(["Rank","Image","Piece","Type","Retail low","Retail high",
                    "Target buy low","Target buy high","Max buy","Est landed (bulk)",
                    "Gross margin %","Markup x","Notes"])
        for p in PICKS:
            r,b,landed,gm,mult = margin_note(p)
            w.writerow([p["rank"], p["img"]+".jpg", p["name"], p["type"],
                        p["retail"][0], p["retail"][1], p["buy"][0], p["buy"][1],
                        p["buy_max"], landed, round(gm*100), round(mult,1), p["why"]])
    print("wrote Lunar_Gems_Top_Picks.html and .csv")

if __name__ == "__main__":
    build()
