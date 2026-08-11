#!/usr/bin/env python3
"""Build the visual field-guide HTML files (portrait guide, cheat sheet,
landscape reference). PDFs are produced from these by make_pdfs.sh."""
import os
from common import (esc, show, money, is_na, load_all, group_by_band, band_order,
                    ROOT, SPEC_FIELDS)
from content import (CATEGORIES, BAND_LABELS, BAND_DESC, ROUND_MM, OVALS_MM,
                     CHECKLIST, RED_FLAGS, METHODOLOGY)
import econ

OUT = ROOT
DATE = econ.RESEARCH_DATE

# ---------------------------------------------------------------------------
# CSS
# ---------------------------------------------------------------------------
CSS = """
:root{
  --ink:#20242b; --muted:#5b6472; --line:#e3ddd0; --bg:#faf7f1; --card:#ffffff;
  --navy:#123a4f; --teal:#1c6b7d; --gold:#b8862f; --gold-soft:#f3e7c9;
  --good:#1c7a4a; --warn:#b3701a; --bad:#a5362d;
}
*{box-sizing:border-box}
html{-webkit-print-color-adjust:exact;print-color-adjust:exact}
body{margin:0;font-family:-apple-system,BlinkMacSystemFont,"Segoe UI",Roboto,Helvetica,Arial,sans-serif;
  color:var(--ink);background:var(--bg);line-height:1.5;font-size:15px}
.wrap{max-width:860px;margin:0 auto;padding:20px 18px 60px}
h1,h2,h3,h4{font-family:Georgia,"Times New Roman",serif;line-height:1.2;margin:0}
a{color:var(--teal);text-decoration:none;word-break:break-word}
.cover{background:linear-gradient(150deg,var(--navy),var(--teal));color:#fff;border-radius:14px;
  padding:34px 26px;margin-bottom:22px}
.cover h1{font-size:30px;color:#fff}
.cover .sub{opacity:.92;margin-top:8px;font-size:15px;max-width:600px}
.cover .meta{margin-top:16px;font-size:12.5px;opacity:.85}
.badgerow{display:flex;flex-wrap:wrap;gap:6px;margin-top:14px}
.pill{background:rgba(255,255,255,.16);border:1px solid rgba(255,255,255,.3);
  padding:3px 9px;border-radius:20px;font-size:11.5px}
.note{background:var(--gold-soft);border:1px solid #e6d4a3;border-radius:10px;padding:12px 14px;
  font-size:13px;margin:14px 0}
.note b{color:#7a5a12}
.warnbox{background:#fbeeea;border:1px solid #e7c3b8;border-radius:10px;padding:12px 14px;font-size:13px;margin:14px 0}
.toc{background:var(--card);border:1px solid var(--line);border-radius:10px;padding:14px 16px;margin-bottom:20px}
.toc h3{font-size:15px;margin-bottom:8px;color:var(--navy)}
.toc ol{margin:0;padding-left:20px;columns:2;column-gap:26px;font-size:13.5px}
.toc a{color:var(--ink)}
section{margin-top:30px}
.cat-h{border-bottom:3px solid var(--gold);padding-bottom:6px;margin-bottom:6px}
.cat-h h2{font-size:22px;color:var(--navy);display:flex;align-items:baseline;gap:10px;flex-wrap:wrap}
.cat-h .code{font-size:12px;background:var(--navy);color:#fff;padding:2px 8px;border-radius:5px;font-family:monospace}
.blurb{color:var(--muted);font-size:13.5px;margin:8px 0 14px}
.band{margin:18px 0;border:1px solid var(--line);border-radius:12px;overflow:hidden;background:var(--card);
  break-inside:avoid}
.band-h{background:#f0ece2;padding:10px 14px;border-bottom:1px solid var(--line)}
.band-h h3{font-size:16px;color:var(--navy)}
.band-h .desc{font-size:12.5px;color:var(--muted);margin-top:3px}
.band-body{padding:12px 14px}
.refbox{background:#f7f4ec;border:1px dashed #cdbf9c;border-radius:9px;padding:10px 12px;margin-bottom:12px;font-size:13px}
.refbox .rng{font-size:19px;color:var(--gold);font-weight:700;font-family:Georgia,serif}
.refbox .obs{color:var(--muted);font-size:12px;margin-top:3px}
.econ{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:10px}
.econ .box{border:1px solid var(--line);border-radius:8px;padding:9px 11px;background:#fff}
.econ h5{font-size:12.5px;text-transform:uppercase;letter-spacing:.04em;color:var(--teal);margin:0 0 6px}
.econ table{width:100%;border-collapse:collapse;font-size:12px}
.econ td{padding:2px 0;vertical-align:top}
.econ td.v{text-align:right;font-variant-numeric:tabular-nums;font-weight:600}
.verdict{display:inline-block;padding:2px 8px;border-radius:12px;font-size:11px;font-weight:700;color:#fff}
.v-Works{background:var(--good)} .v-Marginal{background:var(--warn)} .v-Avoid{background:var(--bad)}
.cards{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;margin-top:12px}
.card{border:1px solid var(--line);border-radius:10px;overflow:hidden;background:#fff;break-inside:avoid;
  display:flex;flex-direction:column}
.photo{position:relative;width:100%;aspect-ratio:1/1;background:#f2eee6;overflow:hidden}
.photo-fallback{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;
  text-align:center;padding:10px;color:#9a9384;font-size:11.5px}
.photo-fallback .big{font-size:26px;margin-bottom:4px}
.photo img{position:relative;z-index:1;width:100%;height:100%;object-fit:cover;display:block}
.card-b{padding:9px 11px;display:flex;flex-direction:column;gap:6px;flex:1}
.card-b .nm{font-size:13px;font-weight:700;line-height:1.25}
.card-b .rt{font-size:11.5px;color:var(--muted)}
.price{font-size:16px;font-weight:800;color:var(--navy);font-family:Georgia,serif}
.price .list{font-size:11px;color:#a99;text-decoration:line-through;font-weight:400;margin-left:6px}
.price .na{font-size:12px;color:var(--warn);font-weight:600}
.pos{display:inline-block;font-size:9.5px;text-transform:uppercase;letter-spacing:.04em;
  padding:2px 6px;border-radius:4px;background:#eef2f2;color:var(--teal);border:1px solid #d8e2e2}
.specs{border-top:1px solid var(--line);padding-top:6px;font-size:11px;display:grid;grid-template-columns:auto 1fr;gap:1px 8px}
.specs dt{color:var(--muted)} .specs dd{margin:0;font-weight:500}
.notes{font-size:11px;color:#4a5260;font-style:italic}
.conf{font-size:10px;color:#9a8f7a}
.src{font-size:11px}
/* size guide */
.sizewrap{background:#fff;border:1px solid var(--line);border-radius:12px;padding:16px}
.rounds{display:flex;flex-wrap:wrap;align-items:flex-end;gap:16px;margin-top:8px}
.rd{display:flex;flex-direction:column;align-items:center;gap:4px}
.rd .dot{background:radial-gradient(circle at 35% 30%,#eaf3ff,#7fb0d6 60%,#2f6b93);border-radius:50%;
  border:1px solid #33617f}
.rd .lb{font-size:11px;color:var(--muted)}
.ovals{display:flex;flex-wrap:wrap;align-items:flex-end;gap:20px;margin-top:16px}
.ov .sh{background:radial-gradient(circle at 35% 30%,#fff2f6,#d98fb0 60%,#a53d6b);border:1px solid #8a3560}
/* tables */
table.grid{width:100%;border-collapse:collapse;font-size:12.5px;margin-top:8px;background:#fff}
table.grid th,table.grid td{border:1px solid var(--line);padding:6px 8px;text-align:right;font-variant-numeric:tabular-nums}
table.grid th{background:var(--navy);color:#fff;font-weight:600;text-align:right}
table.grid td:first-child,table.grid th:first-child{text-align:left}
table.grid tr:nth-child(even) td{background:#faf8f3}
.check{columns:1;font-size:13.5px}
.check li{margin:5px 0}
ul.flags li{margin:6px 0;font-size:13.5px}
.foot{margin-top:40px;padding-top:14px;border-top:1px solid var(--line);font-size:11.5px;color:var(--muted)}
@media print{
  body{font-size:11px;background:#fff}
  .wrap{max-width:none;padding:0}
  a{color:var(--ink)}
  .cover{border-radius:0}
  section{break-inside:auto}
  .cards{grid-template-columns:repeat(3,1fr)}
}
@media(max-width:560px){.cards{grid-template-columns:1fr}.econ{grid-template-columns:1fr}.toc ol{columns:1}}
"""

def page(title, body, landscape=False):
    size = "A4 landscape" if landscape else "A4 portrait"
    return f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{esc(title)}</title>
<style>{CSS}
@page{{size:{size};margin:12mm 10mm}}</style></head><body>{body}</body></html>"""


def price_html(r):
    p = r.get("price_current")
    if is_na(p) or money(p) is None:
        return '<span class="na">price not shown &middot; verify at listing</span>'
    val = money(p)
    out = f"${val:,.0f}" if val >= 100 else f"${val:,.2f}"
    lst = money(r.get("price_list"))
    if lst and lst > val * 1.02:
        out += f'<span class="list">${lst:,.0f}</span>'
    return out


def short_url(u):
    if is_na(u):
        return ""
    s = u.replace("https://", "").replace("http://", "").replace("www.", "")
    return s[:34] + ("…" if len(s) > 34 else "")


def card_html(r):
    img = r.get("image_url")
    photo_inner = (
        f'<div class="photo-fallback"><div class="big">&#128246;</div>'
        f'Photo at listing<br><span class="src">{esc(short_url(r.get("url")))}</span></div>'
    )
    if not is_na(img) and str(img).startswith("http"):
        photo_inner += (f'<img loading="lazy" src="{esc(img)}" alt="{esc(r.get("product_name"))}" '
                        f'onerror="this.style.display=\'none\'">')
    specs = []
    for label, key in SPEC_FIELDS:
        v = show(r.get(key))
        if v == "not disclosed":
            continue
        specs.append(f"<dt>{esc(label)}</dt><dd>{esc(v)}</dd>")
    specs_html = f'<dl class="specs">{"".join(specs)}</dl>' if specs else ""
    pos = show(r.get("positioning"))
    pos_html = f'<span class="pos">{esc(pos)}</span>' if pos != "not disclosed" else ""
    notes = show(r.get("notes"))
    notes_html = f'<div class="notes">{esc(notes)}</div>' if notes != "not disclosed" else ""
    url = r.get("url")
    link = f'<a class="src" href="{esc(url)}">View listing &rarr;</a>' if not is_na(url) else ""
    cert = show(r.get("certification"))
    return f"""<div class="card">
  <div class="photo">{photo_inner}</div>
  <div class="card-b">
    <div class="nm">{esc(show(r.get("product_name")))}</div>
    <div class="rt">{esc(show(r.get("retailer")))} {pos_html}</div>
    <div class="price">{price_html(r)}</div>
    {specs_html}
    {notes_html}
    {link}
  </div>
</div>"""


def econ_tables(R):
    o = econ.outright(R)
    c = econ.consignment(R)
    def row(lbl, val, pct=None):
        extra = f" ({pct*100:.0f}%)" if pct is not None else ""
        return f"<tr><td>{lbl}</td><td class='v'>${val:,.0f}{extra}</td></tr>"
    out = f"""<div class="box"><h5>Outright &mdash; you own it</h5><table>
      {row("Ideal cost to pay", o['ideal_cost'])}
      {row("Max cost", o['max_cost'])}
      {row("Landed allowance", o['landed_allowance'])}
      {row("Selling costs", o['selling_costs'])}
      <tr><td>Profit @ ideal</td><td class='v'>${o['profit_at_ideal']:,.0f} ({o['margin_at_ideal']*100:.0f}%)</td></tr>
    </table></div>"""
    con = f"""<div class="box"><h5>Consignment &mdash; jeweler holds it</h5><table>
      {row("Preferred jeweler net", c['pref_net'])}
      {row("Max jeweler net", c['max_net'])}
      {row("My fees per sale", c['fees'])}
      {row("My gross (pref)", c['gross_before_fees_pref'])}
      <tr><td>Net profit @ pref</td><td class='v'>${c['net_profit_pref']:,.0f} ({c['margin_pref']*100:.0f}%)</td></tr>
      <tr><td>Verdict</td><td class='v'><span class="verdict v-{c['verdict']}">{c['verdict']}</span></td></tr>
    </table></div>"""
    return f'<div class="econ">{out}{con}</div>'


def band_html(cat, code, band_key, recs):
    prices = [r["_price"] for r in recs if r["_price"]]
    lo, hi, mid, n = econ.practical_range(prices)
    label = BAND_LABELS.get(band_key, band_key.title())
    ref_code = f"{code}-{band_key.upper() if len(band_key)==1 else band_key[:3].upper()}"
    desc = BAND_DESC.get(cat, {}).get(band_key, "")
    # reference summary
    if lo and hi:
        rng = f"${lo:,.0f}&ndash;${hi:,.0f}" if lo != hi else f"~${lo:,.0f}"
        obs = ", ".join(f"${p:,.0f}" for p in sorted(prices))
        refR = mid or hi
        econ_h = econ_tables(refR)
        obs_line = f'<div class="obs">Observed asking prices ({n} priced of {len(recs)}): {obs}</div>'
    else:
        rng = "no priced comps"
        econ_h = ""
        obs_line = f'<div class="obs">{len(recs)} listing(s) found; none showed a price in search &mdash; verify at the URLs.</div>'
    desc_html = f'<div class="desc">{esc(desc)}</div>' if desc else ""
    cards = "".join(card_html(r) for r in recs)
    return f"""<div class="band">
  <div class="band-h"><h3>{esc(label)} &nbsp;<span class="code" style="font-size:11px;background:var(--gold);color:#fff;padding:1px 7px;border-radius:4px;font-family:monospace">{ref_code}</span></h3>{desc_html}</div>
  <div class="band-body">
    <div class="refbox">
      <div>Practical U.S. retail range: <span class="rng">{rng}</span></div>
      {obs_line}
    </div>
    {econ_h}
    <div class="cards">{cards}</div>
  </div>
</div>"""


def category_html(cfg, recs):
    if not recs:
        return ""
    bands = group_by_band(cfg["key"], recs)
    inner = "".join(band_html(cfg["key"], cfg["code"], b, rs) for b, rs in bands)
    return f"""<section id="{cfg['key']}">
  <div class="cat-h"><h2>{esc(cfg['name'])} <span class="code">{esc(cfg['code'])}</span></h2></div>
  <div class="blurb">{esc(cfg['blurb'])}</div>
  {inner}
</section>"""


def size_guide_html():
    # true-mm circles and ovals via CSS mm units
    rounds = ""
    for mm in ROUND_MM:
        rounds += (f'<div class="rd"><div class="dot" style="width:{mm}mm;height:{mm}mm"></div>'
                   f'<div class="lb">{mm} mm</div></div>')
    ovals = ""
    for L, W in OVALS_MM:
        ovals += (f'<div class="rd ov"><div class="sh" style="width:{L}mm;height:{W}mm;border-radius:50%"></div>'
                  f'<div class="lb">{L}&times;{W} mm</div></div>')
    return f"""<section id="sizeguide">
  <div class="cat-h"><h2>Stone Size Visual Guide <span class="code">TO SCALE</span></h2></div>
  <div class="note"><b>Scaling caveat:</b> these shapes are drawn in real millimetres and print at
   true size on paper at 100% (no "fit to page" scaling). On a phone screen the size depends on your
   device, so always trust the printed numbers. Round sizes are diameters; ovals are length&times;width.</div>
  <div class="sizewrap">
    <h3 style="font-size:15px;color:var(--navy);margin-bottom:6px">Round (diameter)</h3>
    <div class="rounds">{rounds}</div>
    <h3 style="font-size:15px;color:var(--navy);margin:18px 0 6px">Oval / pear (length &times; width)</h3>
    <div class="ovals">{ovals}</div>
  </div>
  <div class="note" style="margin-top:12px">Rule of thumb for round stones: 5&nbsp;mm&asymp;0.5&nbsp;ct,
   6.5&nbsp;mm&asymp;1&nbsp;ct, 8&nbsp;mm&asymp;2&nbsp;ct (varies by stone density &mdash; sapphire &amp;
   zircon are denser and weigh more than the same-size moonstone).</div>
</section>"""


def quickref_html():
    rows = econ.quick_ref_rows()
    trs = ""
    for r in rows:
        trs += (f"<tr><td>${r['retail']:,}</td>"
                f"<td>${r['ideal_outright']:,.0f}</td>"
                f"<td>${r['max_outright']:,.0f}</td>"
                f"<td>${r['pref_consign_net']:,.0f}</td>"
                f"<td>${r['max_consign_net']:,.0f}</td>"
                f"<td>${r['landed_allowance']:,.0f}</td>"
                f"<td>${r['profit_outright_ideal']:,.0f}</td>"
                f"<td>${r['net_consign_pref']:,.0f}</td></tr>")
    return f"""<section id="quickref">
  <div class="cat-h"><h2>Quick Reference &mdash; Work-Backward Table</h2></div>
  <table class="grid">
    <tr><th>Expected U.S. Retail</th><th>Ideal Outright Cost</th><th>Max Outright Cost</th>
        <th>Preferred Consign. Net</th><th>Max Consign. Net</th><th>Landed Allow.</th>
        <th>Outright Profit @ideal</th><th>Consign. Net Profit @pref</th></tr>
    {trs}
  </table>
  <div class="conf" style="margin-top:6px">All figures derived from the assumptions below. "Net" columns = dollars paid to the Sri Lankan jeweler.</div>
</section>"""


def assumptions_html():
    A = econ.A
    items = [
        ("Ideal outright cost", f"{A['outright_ideal_pct']*100:.0f}% of retail"),
        ("Max outright cost", f"{A['outright_max_pct']*100:.0f}% of retail"),
        ("Preferred consignment net (to jeweler)", f"{A['consign_pref_pct']*100:.0f}% of retail"),
        ("Max consignment net (warning level)", f"{A['consign_max_pct']*100:.0f}% of retail"),
        ("Payment processing", f"{A['payment_processing_pct']*100:.0f}% of retail"),
        ("Returns / damage reserve", f"{A['returns_reserve_pct']*100:.0f}% of retail"),
        ("Insured international shipping (SL&rarr;US)", f"max(${A['intl_ship_floor']:.0f}, {A['intl_ship_pct']*100:.0f}% of retail) per piece"),
        ("U.S. import duty allowance (finished jewelry)", f"{A['customs_duty_pct']*100:.1f}% of value (loose stones often 0%)"),
        ("Packaging / presentation", f"${A['packaging_flat']:.0f} per piece"),
        ("Domestic shipping to U.S. buyer", f"${A['domestic_ship_flat']:.0f} per sale"),
    ]
    lis = "".join(f"<tr><td>{k}</td><td class='v' style='text-align:right;font-weight:600'>{v}</td></tr>" for k, v in items)
    return f"""<section id="assumptions">
  <div class="cat-h"><h2>Assumptions &amp; Formulas</h2></div>
  <div class="note"><b>How to use:</b> estimate the U.S. retail (R) from the comparable bands, then read
   your buy targets. <b>Outright:</b> pay &le; {A['outright_ideal_pct']*100:.0f}% of R (never above
   {A['outright_max_pct']*100:.0f}%). <b>Consignment:</b> the jeweler's net should sit
   {A['consign_pref_pct']*100:.0f}&ndash;{A['consign_max_pct']*100:.0f}% of R; above
   {A['consign_max_pct']*100:.0f}% there is too little margin left after fees.</div>
  <table class="grid"><tr><th>Assumption</th><th>Default value</th></tr>{lis}</table>
  <div class="conf" style="margin-top:6px">Change these in <code>build/econ.py</code> to re-tune the whole guide. <b>Small pieces (&lt;~$300 retail) show thin or negative margins</b> because the ~${A['intl_ship_floor']:.0f} insured-shipping floor is charged once per piece &mdash; commodity items only work when you <b>import several at once and amortise one shipment</b> across them. The per-piece math here is the conservative single-unit case.</div>
</section>"""


def checklist_html():
    lis = "".join(f'<li>&#9744; {esc(x)}</li>' for x in CHECKLIST)
    flags = "".join(f"<li>&#9873; {esc(x)}</li>" for x in RED_FLAGS)
    return f"""<section id="checklist">
  <div class="cat-h"><h2>Shopping Checklist &mdash; Ask Every Seller</h2></div>
  <ul class="check">{lis}</ul>
  <div class="cat-h" style="margin-top:24px"><h2 style="color:var(--bad)">Red Flags &mdash; Do Not Buy Yet</h2></div>
  <div class="warnbox"><ul class="flags" style="margin:0;padding-left:18px">{flags}</ul></div>
</section>"""


def build_field_guide(data):
    cats = [c for c in CATEGORIES if data.get(c["key"])]
    toc = ["quickref", "assumptions"] + [c["key"] for c in cats] + ["sizeguide", "checklist", "sources"]
    toc_names = {"quickref": "Quick Reference table", "assumptions": "Assumptions & formulas",
                 "sizeguide": "Stone size visual guide", "checklist": "Shopping checklist & red flags",
                 "sources": "Sources & method"}
    for c in cats:
        toc_names[c["key"]] = c["name"]
    toc_html = "".join(f'<li><a href="#{k}">{esc(toc_names[k])}</a></li>' for k in toc)
    total = sum(len(v) for v in data.values())

    cover = f"""<div class="cover">
      <h1>Sri Lanka Gemstone Jewelry &mdash; U.S. Retail Field Guide</h1>
      <div class="sub">A practical buying tool: match a piece in a Sri Lankan shop to comparable U.S. retail,
        estimate what it could sell for, and work backward to what you should pay.</div>
      <div class="badgerow">
        <span class="pill">{total} real retail comparables</span>
        <span class="pill">10 gem categories</span>
        <span class="pill">Outright + consignment math</span>
        <span class="pill">Researched {DATE}</span>
      </div>
      <div class="meta">Prices are ASKING prices observed via web search on {DATE} &mdash; reference points, not
        confirmed sale values. Verify each at its listing URL before you rely on it.</div>
    </div>"""

    body = [f'<div class="wrap">', cover,
            f'<div class="toc"><h3>Contents</h3><ol>{toc_html}</ol></div>',
            f'<div class="note"><b>Reading a card:</b> each comparable shows the retailer, current asking price '
            f'(struck-through list price if on sale), the disclosed stone/metal specs, and a link. Blank fields '
            f'are marked "not disclosed" &mdash; nothing is invented. Photos load when you are online; in the '
            f'printed PDF a placeholder points to the listing.</div>',
            quickref_html(), assumptions_html()]
    for c in cats:
        body.append(category_html(c, data[c["key"]]))
    body.append(size_guide_html())
    body.append(checklist_html())
    body.append(f"""<section id="sources"><div class="cat-h"><h2>Sources &amp; Method</h2></div>
      <div class="note">{esc(METHODOLOGY)}</div>
      <div class="conf">Full clickable source list with every URL and the research date is in
      <code>Sources.csv</code> and the <code>Sources</code> tab of <code>Retail_Comparables.xlsx</code>.</div></section>""")
    body.append(f'<div class="foot">Sri Lanka Gemstone Jewelry U.S. Retail Field Guide &middot; generated {DATE} &middot; '
                f'asking prices are reference points, not proven sale values &middot; not an appraisal.</div>')
    body.append("</div>")
    return page("Sri Lanka Gemstone Jewelry — U.S. Retail Field Guide", "".join(body))


def build_cheat_sheet(data):
    A = econ.A
    rows = econ.quick_ref_rows()
    trs = ""
    for r in rows:
        trs += (f"<tr><td>${r['retail']:,}</td><td>${r['ideal_outright']:,.0f}</td>"
                f"<td>${r['max_outright']:,.0f}</td><td>${r['pref_consign_net']:,.0f}</td>"
                f"<td>${r['max_consign_net']:,.0f}</td></tr>")
    # per-category quick range summary
    cat_rows = ""
    for c in CATEGORIES:
        recs = data.get(c["key"], [])
        prices = [r["_price"] for r in recs if r["_price"]]
        if prices:
            lo, hi, mid, n = econ.practical_range(prices)
            cat_rows += f"<tr><td>{esc(c['name'])}</td><td>${min(prices):,.0f}&ndash;${max(prices):,.0f}</td><td>{n}/{len(recs)}</td></tr>"
        else:
            cat_rows += f"<tr><td>{esc(c['name'])}</td><td>&mdash;</td><td>0/{len(recs)}</td></tr>"
    flags = "".join(f"<li>{esc(x)}</li>" for x in RED_FLAGS[:8])
    body = f"""<div class="wrap">
      <div class="cover" style="padding:22px"><h1 style="font-size:22px">Quick Buying Cheat Sheet</h1>
        <div class="sub">Stand in the shop &rarr; estimate U.S. retail &rarr; read your max price.</div>
        <div class="meta">Researched {DATE}. Asking-price reference, not an appraisal.</div></div>
      <section><div class="cat-h"><h2>Work-Backward Table</h2></div>
        <table class="grid"><tr><th>Expected U.S. Retail</th><th>Ideal Outright</th><th>Max Outright</th>
          <th>Preferred Consign. Net</th><th>Max Consign. Net</th></tr>{trs}</table>
        <div class="conf" style="margin-top:6px">Outright = pay {A['outright_ideal_pct']*100:.0f}&ndash;{A['outright_max_pct']*100:.0f}% of retail.
          Consignment net to jeweler = {A['consign_pref_pct']*100:.0f}&ndash;{A['consign_max_pct']*100:.0f}% of retail.
          Add landed costs: ~${A['intl_ship_floor']:.0f}+ insured shipping, {A['customs_duty_pct']*100:.1f}% duty, 3% processing, 5% returns reserve.</div>
      </section>
      <section><div class="cat-h"><h2>Category Reality Check (observed asking-price spans)</h2></div>
        <table class="grid"><tr><th>Gem category</th><th>Observed asking-price span</th><th>Priced comps</th></tr>{cat_rows}</table>
      </section>
      <section><div class="cat-h"><h2 style="color:var(--bad)">Top Red Flags</h2></div>
        <div class="warnbox"><ul style="margin:0;padding-left:18px">{flags}</ul></div>
      </section>
      <div class="foot">Full detail, photos and per-band economics in the Field Guide PDF &middot; {DATE}.</div>
    </div>"""
    return page("Quick Buying Cheat Sheet", body)


def build_landscape(data):
    # wide comparable tables per category
    secs = []
    for c in CATEGORIES:
        recs = data.get(c["key"], [])
        if not recs:
            continue
        trs = ""
        for r in sorted(recs, key=lambda r: (r["_price"] is None, r["_price"] or 0)):
            price = f"${r['_price']:,.0f}" if r["_price"] else "n/d"
            trs += (f"<tr><td>{esc(show(r.get('product_name')))}</td>"
                    f"<td>{esc(show(r.get('retailer')))}</td>"
                    f"<td style='text-align:right'>{price}</td>"
                    f"<td>{esc(show(r.get('jewelry_type')))}</td>"
                    f"<td>{esc(show(r.get('stone_dimensions_mm')))}</td>"
                    f"<td>{esc(show(r.get('carat_weight')))}</td>"
                    f"<td>{esc(show(r.get('treatment')))}</td>"
                    f"<td>{esc(show(r.get('metal')))}</td>"
                    f"<td>{esc(show(r.get('certification')))}</td>"
                    f"<td>{esc(show(r.get('positioning')))}</td></tr>")
        secs.append(f"""<section><div class="cat-h"><h2>{esc(c['name'])} <span class="code">{esc(c['code'])}</span></h2></div>
          <table class="grid" style="font-size:10.5px"><tr><th>Product</th><th>Retailer</th><th>Price</th>
            <th>Type</th><th>Dim mm</th><th>Carat</th><th>Treatment</th><th>Metal</th><th>Cert</th><th>Positioning</th></tr>
          {trs}</table></section>""")
    body = f"""<div class="wrap" style="max-width:none">
      <div class="cover" style="padding:20px"><h1 style="font-size:22px">Retail Comparables &mdash; Landscape Reference</h1>
      <div class="sub">All researched U.S. listings, sortable in the companion spreadsheet.</div>
      <div class="meta">Asking prices observed {DATE}; "n/d" = price not shown in search. Verify at source.</div></div>
      {''.join(secs)}
      <div class="foot">{esc(METHODOLOGY)}</div></div>"""
    return page("Retail Comparables — Landscape Reference", body, landscape=True)


def main():
    data = load_all()
    with open(os.path.join(OUT, "Jewelry_Buying_Field_Guide.html"), "w") as f:
        f.write(build_field_guide(data))
    with open(os.path.join(OUT, "Quick_Buying_Cheat_Sheet.html"), "w") as f:
        f.write(build_cheat_sheet(data))
    with open(os.path.join(OUT, "Reference_Guide_Landscape.html"), "w") as f:
        f.write(build_landscape(data))
    n = sum(len(v) for v in data.values())
    print(f"Built HTML guides from {n} comparables across "
          f"{sum(1 for v in data.values() if v)} categories.")


if __name__ == "__main__":
    main()
