"""
Shared economics engine for the Sri Lanka Jewelry Buying Guide.
All money math (outright purchase + virtual consignment) lives here so the
spreadsheet, the field-guide PDF, and the cheat sheet all use IDENTICAL numbers.

Every assumption is a labeled constant you can change in ONE place.
Nothing here is scraped or invented per-item; these are the buyer's working
economic rules of thumb. Retail values (R) come from the researched comparables.
"""

RESEARCH_DATE = "2026-08-11"

# ---------------------------------------------------------------------------
# ASSUMPTIONS  (edit these; everything else derives from them)
# ---------------------------------------------------------------------------
A = {
    # --- Acquisition targets, as a fraction of expected U.S. retail (R) ---
    "outright_ideal_pct": 0.40,   # ideal price to PAY when buying inventory outright
    "outright_max_pct":   0.50,   # do-not-exceed price when buying outright
    "consign_pref_pct":   0.50,   # preferred NET paid to the SL jeweler on a consignment sale
    "consign_max_pct":    0.60,   # upper WARNING level for jeweler net on consignment

    # --- Selling-side costs (fraction of R unless noted) ---
    "payment_processing_pct": 0.03,   # card / marketplace processing
    "returns_reserve_pct":    0.05,   # reserve for returns, damage, remakes
    "domestic_ship_flat":     12.0,   # ship to the U.S. customer (per sale, $)

    # --- Import / landed costs ---
    # Insured international parcel SL -> US: a floor plus a value-based add-on.
    "intl_ship_floor":     60.0,   # minimum insured courier parcel ($)
    "intl_ship_pct":       0.02,   # + this fraction of R for higher insured value
    "customs_duty_pct":    0.055,  # U.S. duty allowance on finished precious-metal jewelry
                                   # (HTS 7113 ~5.0-5.8%; LOOSE stones are often 0% -
                                   #  treat this as a conservative finished-jewelry allowance)
    "packaging_flat":      8.0,    # per piece packaging / presentation box ($)
}

# Minimum net margin (fraction of R) below which a consignment piece is "marginal".
CONSIGN_OK_MARGIN = 0.20
CONSIGN_MARGINAL_MARGIN = 0.10


def intl_ship_insure(R):
    """Insured international courier allowance for one piece, SL -> US."""
    return max(A["intl_ship_floor"], A["intl_ship_pct"] * R)


# ---------------------------------------------------------------------------
# OUTRIGHT PURCHASE  (I buy the piece and own the inventory)
# ---------------------------------------------------------------------------
def outright(R):
    ideal = A["outright_ideal_pct"] * R
    mx    = A["outright_max_pct"]  * R
    landed = intl_ship_insure(R) + A["customs_duty_pct"] * R + A["packaging_flat"]
    selling = (A["payment_processing_pct"] * R
               + A["returns_reserve_pct"] * R
               + A["domestic_ship_flat"])
    total_at_ideal = ideal + landed + selling
    total_at_max   = mx    + landed + selling
    profit_ideal = R - total_at_ideal
    profit_max   = R - total_at_max
    return {
        "retail": R,
        "ideal_cost": ideal,
        "max_cost": mx,
        "landed_allowance": landed,
        "selling_costs": selling,
        "total_cost_at_ideal": total_at_ideal,
        "profit_at_ideal": profit_ideal,
        "margin_at_ideal": profit_ideal / R if R else 0,
        "total_cost_at_max": total_at_max,
        "profit_at_max": profit_max,
        "margin_at_max": profit_max / R if R else 0,
    }


# ---------------------------------------------------------------------------
# VIRTUAL CONSIGNMENT / ATELIER  (jeweler keeps the piece until I sell it)
# ---------------------------------------------------------------------------
def consignment(R):
    pref_net = A["consign_pref_pct"] * R
    max_net  = A["consign_max_pct"]  * R
    # Fees I absorb per sale (piece ships from SL when it sells):
    fees = (A["payment_processing_pct"] * R
            + intl_ship_insure(R)
            + A["customs_duty_pct"] * R
            + A["packaging_flat"]
            + A["returns_reserve_pct"] * R)
    gross_pref = R - pref_net          # my gross dollars before fees, preferred payout
    gross_max  = R - max_net
    net_pref = gross_pref - fees
    net_max  = gross_max  - fees
    margin_pref = net_pref / R if R else 0
    if margin_pref >= CONSIGN_OK_MARGIN:
        verdict = "Works"
    elif margin_pref >= CONSIGN_MARGINAL_MARGIN:
        verdict = "Marginal"
    else:
        verdict = "Avoid"
    return {
        "retail": R,
        "pref_net": pref_net,
        "max_net": max_net,
        "fees": fees,
        "gross_before_fees_pref": gross_pref,
        "gross_before_fees_max": gross_max,
        "net_profit_pref": net_pref,
        "net_profit_max": net_max,
        "margin_pref": margin_pref,
        "margin_max": net_max / R if R else 0,
        "verdict": verdict,
    }


# Standard rows for the one-page quick reference sheet.
QUICK_REF_RETAILS = [250, 350, 500, 750, 1000, 1500, 2000, 2500, 5000]


def quick_ref_rows():
    rows = []
    for R in QUICK_REF_RETAILS:
        o = outright(R)
        c = consignment(R)
        rows.append({
            "retail": R,
            "ideal_outright": o["ideal_cost"],
            "max_outright": o["max_cost"],
            "pref_consign_net": c["pref_net"],
            "max_consign_net": c["max_net"],
            "landed_allowance": o["landed_allowance"],
            "profit_outright_ideal": o["profit_at_ideal"],
            "margin_outright_ideal": o["margin_at_ideal"],
            "net_consign_pref": c["net_profit_pref"],
            "margin_consign_pref": c["margin_pref"],
        })
    return rows


def practical_range(prices):
    """Given observed asking prices, return a defensible practical retail range.
    Uses a trimmed central band (drops the single lowest and highest when n>=5)
    so one outlier does not distort the range. Returns (low, high, mid, n)."""
    ps = sorted(p for p in prices if isinstance(p, (int, float)) and p > 0)
    if not ps:
        return (None, None, None, 0)
    n = len(ps)
    core = ps[1:-1] if n >= 5 else ps
    lo, hi = min(core), max(core)
    mid = round((lo + hi) / 2)
    # Round to tidy retail numbers.
    def tidy(x):
        if x < 300:   return round(x / 5) * 5
        if x < 1000:  return round(x / 25) * 25
        if x < 5000:  return round(x / 50) * 50
        return round(x / 100) * 100
    return (tidy(lo), tidy(hi), tidy(mid), n)


if __name__ == "__main__":
    import json
    print("Assumptions:", json.dumps(A, indent=2))
    print("\nQuick reference:")
    for r in quick_ref_rows():
        print(f"  R=${r['retail']:>5}  ideal_out=${r['ideal_outright']:>6.0f}  "
              f"max_out=${r['max_outright']:>6.0f}  pref_net=${r['pref_consign_net']:>6.0f}  "
              f"max_net=${r['max_consign_net']:>6.0f}  "
              f"out_profit=${r['profit_outright_ideal']:>6.0f} ({r['margin_outright_ideal']*100:.0f}%)  "
              f"con_net=${r['net_consign_pref']:>6.0f} ({r['margin_consign_pref']*100:.0f}%)")
