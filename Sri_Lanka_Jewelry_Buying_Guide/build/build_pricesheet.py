#!/usr/bin/env python3
"""Owner-facing price-request sheet: photo of each piece + a blank line for his
retail price. No internal buy/margin numbers. One page, PDF."""
import os, base64, io
from PIL import Image
from common import ROOT

LG = os.path.join(ROOT, "Lunar_Gems")

# 5 pieces chosen to span the price ladder (owner-friendly names only).
ITEMS = [
    dict(img="LG-23", n=1, name="Dainty moonstone silver ring",
         desc="single small round moonstone, thin band", metal=False),
    dict(img="LG-06", n=2, name="Open-heart moonstone pendant",
         desc="heart outline with a single blue moonstone", metal=False),
    dict(img="LG-13", n=3, name="Crescent-moon moonstone ring (adjustable)",
         desc="crescent moon beside a round moonstone", metal=False),
    dict(img="LG-01", n=4, name="Sea-turtle moonstone bracelet",
         desc="row of oval moonstones with a turtle centre", metal=False),
    dict(img="LG-18", n=5, name="Moonstone station necklace",
         desc="line of oval moonstones along the chain", metal=True),
]

def data_uri(path, box=520, q=85):
    im = Image.open(path).convert("RGB")
    im.thumbnail((box, box))
    b = io.BytesIO(); im.save(b, "JPEG", quality=q)
    return "data:image/jpeg;base64," + base64.b64encode(b.getvalue()).decode()

CSS = """
*{box-sizing:border-box}
body{font-family:-apple-system,Segoe UI,Roboto,Helvetica,Arial,sans-serif;color:#222;margin:0;font-size:13px}
.wrap{max-width:820px;margin:0 auto;padding:20px 22px}
h1{font-family:Georgia,serif;font-size:22px;color:#123a4f;margin:0 0 6px}
.intro{font-size:13px;color:#333;margin-bottom:14px;line-height:1.5}
.row{display:flex;gap:16px;align-items:center;border:1px solid #e0dccf;border-radius:12px;padding:12px 14px;margin:11px 0;break-inside:avoid}
.row img{width:150px;height:150px;object-fit:cover;border-radius:9px;flex:0 0 auto;background:#f2eee6}
.info{flex:1;min-width:0}
.num{display:inline-block;background:#123a4f;color:#fff;font-weight:700;border-radius:50%;width:24px;height:24px;text-align:center;line-height:24px;font-size:13px;margin-right:8px}
.name{font-weight:700;font-size:16px;color:#123a4f;font-family:Georgia,serif}
.desc{color:#666;font-size:12px;margin:3px 0 12px}
.field{font-size:14px;margin-top:8px}
.field .lb{color:#333;font-weight:600}
.line{display:inline-block;border-bottom:1.5px solid #999;min-width:230px;height:22px;vertical-align:bottom}
.metal{margin-top:10px;font-size:13px}
.box{display:inline-block;width:15px;height:15px;border:1.5px solid #666;border-radius:3px;vertical-align:middle;margin:0 5px 0 12px}
.thanks{margin-top:18px;font-size:13px;color:#333;line-height:1.5}
@page{size:A4 portrait;margin:12mm 10mm}
"""

def build():
    rows = ""
    for it in ITEMS:
        uri = data_uri(os.path.join(LG, it["img"]+".jpg"))
        metal = ""
        if it["metal"]:
            metal = ('<div class="metal"><span class="lb" style="font-weight:600">Metal:</span>'
                     '<span class="box"></span> Silver <span class="box"></span> Gold '
                     '<span class="box"></span> Other: <span class="line" style="min-width:120px"></span></div>')
        rows += f"""<div class="row">
  <img src="{uri}" alt="{it['name']}">
  <div class="info">
    <div><span class="num">{it['n']}</span><span class="name">{it['name']}</span></div>
    <div class="desc">{it['desc']}</div>
    <div class="field"><span class="lb">Your retail price:</span> <span class="line"></span> &nbsp;(LKR or USD)</div>
    {metal}
  </div>
</div>"""
    html = f"""<!doctype html><html><head><meta charset="utf-8"><title>Lunar Gems — Price Request</title>
<style>{CSS}</style></head><body><div class="wrap">
<h1>Lunar Gems &mdash; a few retail prices, please</h1>
<div class="intro">Thank you again &mdash; we love everything! The moonstone flash on your pieces is beautiful and
exactly the quality we're looking for. As we plan for the U.S. market, could you kindly note your
<b>retail price</b> for these few pieces? This is just so we understand your pricing &mdash; nothing to work out
right now. Thank you so much!</div>
{rows}
<div class="thanks">Thank you very much &mdash; we're genuinely excited about working together. &#128522;</div>
</div></body></html>"""
    out = os.path.join(ROOT, "Lunar_Gems_Price_Request.html")
    open(out, "w").write(html)
    print("wrote", out)

if __name__ == "__main__":
    build()
