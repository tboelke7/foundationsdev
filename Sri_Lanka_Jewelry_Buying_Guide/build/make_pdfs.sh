#!/usr/bin/env bash
# Render the HTML guides to PDF with headless Chromium.
set -e
CHROME=/opt/pw-browsers/chromium-1194/chrome-linux/chrome
BASE="$(cd "$(dirname "$0")/.." && pwd)"
render () {
  local html="$1" pdf="$2"
  "$CHROME" --headless --no-sandbox --disable-gpu --no-pdf-header-footer \
    --run-all-compositor-stages-before-draw --virtual-time-budget=8000 \
    --print-to-pdf="$BASE/$pdf" "$BASE/$html" 2>/dev/null
  echo "  $pdf  ($(stat -c%s "$BASE/$pdf" 2>/dev/null) bytes, $(pdfinfo "$BASE/$pdf" 2>/dev/null | awk '/Pages/{print $2}') pages)"
}
render "Jewelry_Buying_Field_Guide.html"  "Jewelry_Buying_Field_Guide.pdf"
render "Quick_Buying_Cheat_Sheet.html"    "Quick_Buying_Cheat_Sheet.pdf"
render "Reference_Guide_Landscape.html"   "Reference_Guide_Landscape.pdf"
