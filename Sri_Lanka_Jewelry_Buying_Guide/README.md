# Sri Lanka Gemstone Jewelry — U.S. Retail Field Guide

A practical buying tool for sourcing Sri Lankan gemstone jewelry in Sri Lanka.
Match a piece in a shop to comparable current U.S. retail listings, estimate what
it could realistically sell for in the U.S., then **work backward** to what you
should be willing to pay — outright or on virtual consignment.

Researched **2026-08-11**. **141 real U.S.-facing retail comparables** across 10 gem
categories.

## What's here

| File | What it is |
|------|-----------|
| `Jewelry_Buying_Field_Guide.pdf` | The main visual guide (A4 portrait, phone-friendly). Cover, quick-reference table, assumptions, all 10 gem categories in quality/price bands with per-band buy/consignment economics, to-scale stone-size chart, shopping checklist, red flags. |
| `Jewelry_Buying_Field_Guide.html` | Same guide as a web page — **open this on your phone with internet and the product photos load** (the PDF shows placeholders, see note below). |
| `Quick_Buying_Cheat_Sheet.pdf` | One-page work-backward table + category reality-check + top red flags. Print it / keep it on your phone. |
| `Reference_Guide_Landscape.pdf` | Wide landscape tables of every comparable (printable). |
| `Retail_Comparables.xlsx` | Sortable workbook — `Comparables` (all 141, autofilter), `Band Analysis`, `Quick Reference`, `Assumptions`, `Sources`. |
| `Sources.csv` | Every listing: retailer, product, price, URL, research date, confidence. |
| `Images/` | One subfolder per gem category (see image note below). |
| `build/` | The Python that generates everything. Edit `build/econ.py` to re-tune the pricing math, then re-run (see below). |

## How to use it in a shop

1. Identify the gem category and rough band (size / quality / metal).
2. Read the **Practical U.S. retail range** for that band.
3. Read the **Outright** and **Consignment** boxes: the *ideal* and *max* price to pay,
   and whether consignment even makes sense after fees.
4. Compare the seller's asking price to your max. If there's room, it's worth pursuing;
   if not, walk (or negotiate to your number).
5. Run the **Shopping Checklist** and watch the **Red Flags** before committing.

## ⚠️ Read this about the numbers and the photos

- **Asking price ≠ proven value.** Every price is an *asking* price observed via web
  search on 2026-08-11 from U.S. retail/marketplace listings. They are reference points,
  not confirmed sale prices. Re-verify each at its URL before you rely on it.
- **Photos:** this guide was built in a locked-down environment whose network policy
  blocked downloading images and fetching product pages. So product **photos could not be
  embedded**, and specs not visible in search snippets are marked *"not disclosed"* rather
  than guessed. Open the **HTML** guide online to see photos where the listing exposes an
  image; otherwise each card links to the listing. To produce a fully photo-embedded
  offline PDF, re-run the build on a machine with open internet (see `build/`).
- **Not an appraisal.** This is a market-comparison and margin tool, not a valuation or
  legal/customs advice. Confirm duty and export rules for your situation.

## Rebuilding

```bash
cd build
python3 build_guide.py      # -> HTML guides
bash    make_pdfs.sh        # -> PDFs (uses headless Chromium)
python3 build_xlsx.py       # -> Retail_Comparables.xlsx + Sources.csv
```

Pricing assumptions (acquisition %, fees, shipping, duty) all live in `build/econ.py`.
