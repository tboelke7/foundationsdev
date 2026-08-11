"""Static content: category config, band definitions, checklist, red flags, size guide."""

# Order + display metadata for every gem category.
CATEGORIES = [
    dict(key="moonstone", name="Ceylon / Sri Lankan Moonstone", code="MS",
         folder="Moonstone", banded=True, priority=True,
         blurb=("Classic adularia moonstone with billowy blue adularescence (the "
                "'flash'). Sri Lanka is the benchmark origin for blue-sheen "
                "moonstone. Value is driven far more by the strength, colour and "
                "centering of the flash and by the stone's transparency than by "
                "size alone. A clean, glassy stone with a strong 3-D blue sheen "
                "beats a bigger, milky, weak-flash stone.")),
    dict(key="rainbow_moonstone", name="Rainbow Moonstone / White Labradorite", code="RM",
         folder="Rainbow_Moonstone", banded=False, priority=False,
         blurb=("Technically a white labradorite, not true moonstone. Transparent "
                "body with blue-to-multicolour flash. Far more abundant and cheaper "
                "than fine Ceylon blue-sheen moonstone; enormous supply on Etsy. "
                "Treat sub-$100 silver pieces as commodity. Value climbs only with "
                "solid gold, artisan makers, or unusually clean large stones.")),
    dict(key="sapphire", name="Ceylon / Sri Lankan Blue Sapphire", code="SA",
         folder="Sapphire", banded=True, priority=True,
         blurb=("The flagship Sri Lankan gem. Price per carat explodes with size, "
                "colour saturation (vivid medium-deep 'cornflower' to royal blue), "
                "clarity, and — critically — HEAT TREATMENT and a credible lab "
                "report. Unheated, well-saturated Ceylon sapphire with a GIA/GRS/"
                "SSEF/Gubelin report is a different market from heated commercial "
                "goods. Always separate heated vs unheated and confirm the report.")),
    dict(key="star_sapphire", name="Star Sapphire", code="ST",
         folder="Star_Sapphire", banded=False, priority=False,
         blurb=("Cabochon sapphire showing a 6-ray star (asterism). Value rests on "
                "a sharp, straight, centred star, good translucency and body colour "
                "(blue and grey-blue Ceylon are classic). Milky stones with weak or "
                "off-centre stars are common and cheap. Many strong comparables are "
                "vintage/estate rings.")),
    dict(key="padparadscha", name="Padparadscha Sapphire", code="PAD",
         folder="Padparadscha", banded=False, priority=False,
         blurb=("The pink-orange 'lotus' sapphire; Sri Lanka is the classic origin. "
                "A high-value niche - a true, lab-confirmed padparadscha colour "
                "commands large premiums, and the 'padparadscha' call on the report "
                "(AGL/GRS/GIA/SSEF) is itself part of the value. Heated vs unheated "
                "matters enormously.")),
    dict(key="cats_eye", name="Chrysoberyl Cat's Eye", code="CE",
         folder="Cats_Eye", banded=False, priority=False,
         blurb=("True chrysoberyl cymophane: a sharp chatoyant 'eye' with the "
                "'milk-and-honey' effect. Do not confuse with cheap quartz or "
                "glass 'cat's eye'. Value = eye sharpness, honey/greenish body "
                "colour, and translucency. Sri Lanka is a premier source.")),
    dict(key="alexandrite", name="Alexandrite (Colour-Change)", code="ALX",
         folder="Alexandrite", banded=False, priority=False,
         blurb=("Colour-change chrysoberyl - green/teal in daylight to red/purple "
                "under incandescent light. Among the highest price-per-carat "
                "coloured stones. Natural alexandrite with strong change and a lab "
                "report is rare and expensive; LAB-CREATED alexandrite is cheap and "
                "everywhere. Confirm natural vs synthetic on a report before paying "
                "natural prices.")),
    dict(key="spinel", name="Spinel", code="SP",
         folder="Spinel", banded=False, priority=False,
         blurb=("An under-rated Sri Lankan gem, typically UNTREATED (a selling "
                "point). Grey-blue, cobalt blue, pink, lavender, purple and red. "
                "Cobalt blue and vivid red are the premium end; grey and pale "
                "lavender are affordable. A 'no-heat' note and clean bright colour "
                "drive value.")),
    dict(key="zircon", name="Zircon (Natural Mineral)", code="ZR",
         folder="Zircon", banded=False, priority=False,
         blurb=("Genuine zircon - NOT cubic zirconia. Ceylon is famous for blue "
                "zircon (heated) plus white, honey, golden and green. High lustre "
                "and fire. An affordable-to-mid stone; value comes from size, "
                "vivid colour and clean cutting. Reject any 'CZ' listing.")),
    dict(key="hessonite", name="Hessonite Garnet", code="HES",
         folder="Hessonite", banded=False, priority=False,
         blurb=("Cinnamon / honey-orange grossular garnet with a characteristic "
                "'scotch-in-water' treacly look; Sri Lanka is a classic source and "
                "the astrological 'Gomed' stone. Generally untreated and "
                "affordable-to-mid; bright cinnamon-orange, clean stones are the "
                "premium end.")),
]

BAND_LABELS = {
    "A": "A · Small / Basic",
    "B": "B · Better Everyday",
    "C": "C · Premium",
    "D": "D · Hero / Collector",
    "affordable": "Affordable",
    "middle": "Middle-Market",
    "premium": "Premium",
    "artisan": "Artisan / One-of-a-kind",
    "luxury": "Luxury / Exceptional",
}
BANDED_ORDER = ["A", "B", "C", "D"]
GENERIC_ORDER = ["affordable", "middle", "premium", "artisan", "luxury"]

# Human-written band descriptors for the two priority categories (match the
# buyer's M1..M4 style). Others are summarised automatically from the data.
BAND_DESC = {
    "moonstone": {
        "A": "3-5 mm, simple sterling setting, ordinary flash. Studs & small pendants.",
        "B": "~6-8 mm, stronger blue flash, sterling or gold vermeil. Everyday rings & pendants.",
        "C": "~8-12 mm, strong centred blue sheen, better transparency, artisan setting.",
        "D": "Exceptional stone, solid gold or significant handmade setting, named artisan / one-of-one.",
    },
    "sapphire": {
        "A": "Small accent stones or sub-0.5 ct; sterling or low-karat gold; heated commercial goods.",
        "B": "~0.5-1.5 ct, 14k gold, good blue, heated. The everyday Ceylon-sapphire sweet spot.",
        "C": "~1.5-3 ct, vivid blue, 18k/platinum, often a lab report; unheated starts to appear.",
        "D": "3 ct+, fine unheated Ceylon colour, platinum/18k, GIA/GRS/SSEF/Gubelin report.",
    },
}

# Fields shown in each comparable card's spec grid (label, json key).
SPEC_FIELDS = [
    ("Jewelry type", "jewelry_type"),
    ("Gemstone", "gemstone_type"),
    ("Claimed origin", "claimed_origin"),
    ("Dimensions (mm)", "stone_dimensions_mm"),
    ("Carat", "carat_weight"),
    ("Shape / cut", "shape_cut"),
    ("Treatment", "treatment"),
    ("Metal", "metal"),
    ("Metal weight", "metal_weight"),
    ("Setting", "setting_style"),
    ("Construction", "construction"),
    ("Certification", "certification"),
]

# ---- Stone size visual guide -------------------------------------------------
ROUND_MM = [3, 4, 5, 6, 8, 10, 12, 15]
OVALS_MM = [(6, 4), (8, 6), (10, 8), (12, 10)]  # (length, width)

# ---- Shopping checklist ------------------------------------------------------
CHECKLIST = [
    "Gem species (e.g. corundum, chrysoberyl, feldspar, garnet, spinel, zircon)",
    "Variety (e.g. blue sapphire, padparadscha, cat's eye, moonstone)",
    "Sri Lankan / Ceylon origin? — claimed vs documented",
    "Natural or synthetic / lab-created?",
    "Carat weight (get the actual number)",
    "Dimensions in mm (length × width × depth)",
    "Colour (hue, tone, saturation — in daylight AND indoor light)",
    "Clarity (eye-clean? inclusions? windows?)",
    "Cut / shape and quality of cutting (symmetry, polish, windowing)",
    "Treatment (none / heat / diffusion / glass-fill / irradiation / dye)",
    "Heated or unheated? (sapphire, padparadscha, zircon especially)",
    "Lab certificate? Which lab? (GIA, GRS, SSEF, Gübelin, AGL, GIT, Lotus)",
    "Metal type (silver, gold, platinum)",
    "Metal purity (925, 9k/10k/14k/18k/22k, Pt950)",
    "Metal weight in grams",
    "Handmade / cast / CAD-made?",
    "Maker / workshop name",
    "Workshop location (city / area)",
    "Normal Sri Lankan RETAIL (tourist) price",
    "Outright TRADE price (what they'll actually sell to you for)",
    "Consignment / net price (if they'll hold it until you sell)",
    "Export capability & paperwork (NGJA export licence / dealer can ship)",
    "Shipping cost (insured courier to the U.S.)",
    "Insurance included / available?",
    "Can they PRODUCE / REPLACE this piece (repeatable) or is it unique?",
    "Is the piece one-of-a-kind or reproducible to order?",
]

# ---- Red flags ---------------------------------------------------------------
RED_FLAGS = [
    "Origin claimed but NO documentation on an expensive stone.",
    "\"Unheated sapphire\" with no lab report at a high price.",
    "Seller won't give you the carat weight or the mm dimensions.",
    "Metal purity is vague (\"gold colour\", \"German silver\", no hallmark).",
    "Tourist retail price presented as \"wholesale\" or \"special price for you\".",
    "Price justified mainly by a story (mine visit, family, luck) rather than the stone.",
    "A big premium with no visible stone quality (weak flash / weak star / dull colour) to justify it.",
    "\"Certificate\" from an unknown local lab, or a photocopy that doesn't match the stone.",
    "Cat's-eye / colour-change / star that only shows under the seller's single spotlight.",
    "Reluctance to let you examine the stone loose, in daylight, or with a loupe.",
    "\"Alexandrite\" or \"zircon\" that is suspiciously cheap and abundant (likely synthetic / CZ).",
    "No export paperwork or courier — you can't legally/practically get it home.",
    "Glue lines, doublets, foil backs, or a closed/backed setting hiding the pavilion.",
]

METHODOLOGY = (
    "All prices in this guide are ASKING prices observed via web search on "
    "2026-08-11 from U.S.-facing retail and marketplace listings. They are "
    "reference points, NOT confirmed sale prices. Marketplace (Etsy/1stDibs) "
    "asking prices can sit above realised sale prices; where sales/review counts "
    "were visible they are noted. Because this build environment blocks direct "
    "page fetching, individual listing specs that were not visible in search "
    "results are marked \"not disclosed\" rather than guessed, and every listing "
    "should be re-verified at its URL before you rely on it. Practical retail "
    "ranges are derived from the observed listings (trimmed of single high/low "
    "outliers), never set first and back-filled."
)
