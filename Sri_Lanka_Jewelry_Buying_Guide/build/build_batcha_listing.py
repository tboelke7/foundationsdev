#!/usr/bin/env python3
"""Internal listing worksheet for the selected Batcha Gems pieces.
Embeds a thumbnail per row; landed cost + margin are live formulas so the
supplier's real numbers can be dropped in later."""
import json, os
from openpyxl import Workbook
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
from openpyxl.utils import get_column_letter
from openpyxl.drawing.image import Image as XLImage

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
recs = json.load(open(os.path.join(HERE, "selected_data.json")))
DATE = "2026-09-09"
NAVY = "123A4F"; GOLD = "B8862F"; GREEN = "1C7A4A"; LIGHT = "F0ECE2"; INPUT = "FFF7E0"
HEADW = Font(color="FFFFFF", bold=True, size=10)
thin = Side(style="thin", color="D8D2C4")
BORDER = Border(left=thin, right=thin, top=thin, bottom=thin)

wb = Workbook()

# ---- Assumptions sheet ----
asx = wb.active; asx.title = "Assumptions"
asx["A1"] = "Landed-cost assumptions (edit these — the worksheet formulas use them)"
asx["A1"].font = Font(bold=True, size=12, color=NAVY)
rows = [
    ("Import duty rate (finished gold jewelry)", 0.055, "HTS 7113 ~5–5.8%. Loose stones are often 0%. Confirm for your imports."),
    ("Default packaging per piece (USD)", 8, "Presentation box / padding."),
    ("Ship-to (U.S.) ZIP / city", "[ FILL IN ]", "Give this to Batcha for an insured-courier quote."),
    ("Note on shipping", "per-piece insured courier SL→US ~ $60–90 for one parcel; a batch amortises lower", ""),
]
asx["A2"] = "Item"; asx["B2"] = "Value"; asx["C2"] = "Note"
for c in ("A2", "B2", "C2"):
    asx[c].fill = PatternFill("solid", fgColor=NAVY); asx[c].font = HEADW
for i, (k, v, note) in enumerate(rows, start=3):
    asx[f"A{i}"] = k; asx[f"B{i}"] = v; asx[f"C{i}"] = note
    asx[f"B{i}"].fill = PatternFill("solid", fgColor=INPUT)
asx["B3"].number_format = "0.0%"
asx.column_dimensions["A"].width = 42; asx.column_dimensions["B"].width = 22; asx.column_dimensions["C"].width = 70
DUTY = "Assumptions!$B$3"

# ---- Main worksheet ----
ws = wb.create_sheet("Listing Worksheet")
COLS = [
    ("Ref", 8), ("Photo", 20), ("Piece / description", 40), ("Type", 16), ("Gem", 24),
    ("Metal", 22), ("Ring?", 6),
    ("Retail HEATED low", 11), ("HEATED high", 11), ("Retail UNHEATED low", 12), ("UNHEATED high", 12),
    ("Supplier trade price $", 13), ("Insured shipping $", 12), ("Export/NGJA + fees $", 13),
    ("US duty $ (auto)", 12), ("Packaging $", 10), ("LANDED TOTAL $ (auto)", 14),
    ("Target US retail $", 13), ("Margin $ (auto)", 12), ("Margin % (auto)", 11),
    ("Ring size / resize range", 22), ("Variants available", 22), ("Set components", 22),
    ("Cert / lab report", 20), ("Pro images rec'd?", 12), ("Notes", 46),
]
for j, (h, w) in enumerate(COLS, 1):
    c = ws.cell(row=1, column=j, value=h)
    c.fill = PatternFill("solid", fgColor=NAVY); c.font = HEADW
    c.alignment = Alignment(vertical="center", wrap_text=True); c.border = BORDER
    ws.column_dimensions[get_column_letter(j)].width = w
# color code header groups
def hdrfill(col, color):
    ws.cell(row=1, column=col).fill = PatternFill("solid", fgColor=color)
for col in (12, 13, 14, 16, 18, 21, 22, 23, 24, 25):  # input columns
    ws.cell(row=1, column=col).fill = PatternFill("solid", fgColor=GOLD)

INPUT_COLS = {12, 13, 14, 16, 18, 21, 22, 23, 24, 25}
r = 2
for rec in recs:
    row = r
    ws.row_dimensions[row].height = 92
    ws.cell(row, 1, rec["bg"])
    # photo in col 2
    try:
        img = XLImage(rec["thumb"]); img.height = 118; img.width = int(118 * rec["w"] / rec["h"])
        ws.add_image(img, f"B{row}")
    except Exception as e:
        ws.cell(row, 2, "(img)")
    ws.cell(row, 3, rec["name"])
    ws.cell(row, 4, rec["type"])
    ws.cell(row, 5, rec["gem"])
    ws.cell(row, 6, rec["metal"])
    ws.cell(row, 7, "Y" if rec["ring"] else "")
    ws.cell(row, 8, rec["h_lo"]); ws.cell(row, 9, rec["h_hi"])
    ws.cell(row, 10, rec["u_lo"] if rec["u_lo"] else ("n/a" if rec["multi"] == 0 else ""))
    ws.cell(row, 11, rec["u_hi"] if rec["u_hi"] else "")
    # inputs blank (12,13,14), packaging default 8 (16 unless overview)
    if rec["multi"] != 2:
        ws.cell(row, 16, 8)
    # duty auto (15)
    ws.cell(row, 15, f'=IF($L{row}="","",ROUND({DUTY}*$L{row},2))')
    # landed total auto (17)
    ws.cell(row, 17, f'=IF($L{row}="","",SUM($L{row},$M{row},$N{row},$O{row},$P{row}))')
    # target retail prefill = heated high (18) editable
    if rec["h_hi"]:
        ws.cell(row, 18, rec["h_hi"])
    # margin auto (19,20)
    ws.cell(row, 19, f'=IF(OR($R{row}="",$Q{row}=""),"",$R{row}-$Q{row})')
    ws.cell(row, 20, f'=IF(OR($R{row}="",$S{row}=""),"",$S{row}/$R{row})')
    ws.cell(row, 21, "resize? →" if rec["ring"] else "")
    ws.cell(row, 23, rec["set"])
    ws.cell(row, 26, rec["notes"])
    # formatting
    for j in range(1, 27):
        cell = ws.cell(row, j)
        cell.border = BORDER
        cell.alignment = Alignment(vertical="top", wrap_text=True, horizontal="left")
        if j in (8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19):
            cell.number_format = '$#,##0'
        if j == 20:
            cell.number_format = '0%'
        if j in INPUT_COLS:
            cell.fill = PatternFill("solid", fgColor=INPUT)
    r += 1

ws.freeze_panes = "C2"
ws.auto_filter.ref = f"A1:Z{r-1}"

# ---- Legend / how-to sheet ----
leg = wb.create_sheet("How to use", 0)
lines = [
    ("Batcha Gems — Listing & Landed-Cost Worksheet", 14, NAVY, True),
    (f"Prepared {DATE}. {len(recs)} selected pieces (photos). Gold-headed columns are INPUTS you fill after Batcha replies.", 10, "5B6472", False),
    ("", 10, "000000", False),
    ("Workflow:", 11, NAVY, True),
    ("1. Send Batcha the questionnaire (Batcha_Supplier_Questionnaire.docx) to get: trade price, treatment/cert, carat, metal weight, sizes, variants, set prices, and an insured landed quote to your ZIP.", 10, "000000", False),
    ("2. Type their trade price into 'Supplier trade price', plus insured shipping and any export/NGJA fees. US duty, landed total, and margin calculate automatically.", 10, "000000", False),
    ("3. 'Target US retail' is pre-filled with my HEATED high estimate — overwrite it with the column that matches the confirmed treatment (use the UNHEATED figures if a report confirms unheated).", 10, "000000", False),
    ("4. Rows marked 'MULTIPLE' in Notes are display trays: ask Batcha to itemize each piece (one row each) with its own SKU, carat, size and price.", 10, "000000", False),
    ("", 10, "000000", False),
    ("Assumptions (duty %, packaging, ship-to ZIP) live on the 'Assumptions' tab — change the duty rate there and every row updates.", 10, "5B6472", False),
    ("Estimates are asking-price reference, not appraisals. Confirm treatment + lab report on every significant stone.", 10, "A5362D", False),
]
for i, (t, sz, col, b) in enumerate(lines, 1):
    c = leg.cell(row=i, column=1, value=t)
    c.font = Font(size=sz, color=col, bold=b); c.alignment = Alignment(wrap_text=True, vertical="top")
leg.column_dimensions["A"].width = 130

out = os.path.join(ROOT, "Batcha_Listing_Worksheet.xlsx")
wb.save(out)
print("wrote", out)
