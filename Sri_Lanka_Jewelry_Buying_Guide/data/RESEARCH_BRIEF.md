# Shared research brief — Sri Lanka jewelry buying guide

You are gathering REAL current U.S. retail comparables for gemstone jewelry, to help
a buyer estimate U.S. resale value while shopping in Sri Lanka.

## Environment constraints (IMPORTANT)
- `WebSearch` WORKS. Use it heavily. It returns real retailer titles, URLs, and often
  price points / specs inside the result snippet text.
- `WebFetch` and `curl` are BLOCKED by network egress policy for retail sites. Do NOT
  depend on them. If you try WebFetch and it errors "egress blocked", stop trying it and
  rely on WebSearch snippets. (You may try WebFetch once on a product URL; if blocked, move on.)
- You CANNOT download images. Just record the product URL and, if visible in a search
  result, an image URL. Do not attempt curl downloads.

## Rules
- Use ONLY reputable U.S.-facing sellers: Ross-Simons, Blue Nile, Brilliant Earth, Angara,
  JTV/Gem Shopping, Etsy sellers with strong sales/reviews, 1stDibs, Gem Breakfast, Omi Gems,
  The Natural Sapphire Company, Leibish, specialty gem jewelers, reputable independents.
- AVOID as primary sources: Alibaba, Temu, Amazon commodity listings, obvious fake-sale
  pricing, unverifiable dropship sites.
- NEVER invent prices, dimensions, carat, treatment, or any spec. If a field is not visible
  in search results, write exactly "not disclosed".
- Every price is an ASKING price observed via web search on 2026-08-11. Record it, and note
  that the listing page was not directly fetchable in this environment (so it needs live
  verification). Distinguish asking price from proven sale value.
- For Etsy/marketplace listings, note sales count / reviews / "bestseller" if visible.
- Do NOT pad to hit a quota with bad examples. Quality over quantity. It is fine to return
  fewer if credible listings are scarce.

## For each comparable, capture these fields (JSON keys):
band, product_name, retailer, price_current, price_list, url, image_url, jewelry_type,
gemstone_type, claimed_origin, stone_dimensions_mm, carat_weight, shape_cut, treatment,
metal, metal_weight, setting_style, construction, certification, positioning,
price_confidence, notes

- band: for moonstone & blue sapphire use "A" (small/basic), "B" (better everyday),
  "C" (premium), "D" (hero/collector). For other stones use "affordable", "middle",
  "premium", "artisan", or "luxury". Best-guess band from price + description.
- construction: handmade / artisan / cast / mass-produced / not disclosed
- positioning: commodity / boutique / artisan / fine jewelry / luxury
- price_confidence: short note, e.g. "price in search snippet, verify on page" or
  "price not shown in results".
- notes: one line on why this is a useful comparable (size, flash quality, metal, maker).

## Output
1. Write a JSON array of records to the output path you are given (valid JSON, UTF-8).
2. Return a SHORT summary: how many found, the observed price range, band coverage,
   and any notable gaps. Keep the summary under 150 words.

## Search tips
Run many targeted queries, e.g.:
- "<gem> <jewelry type> <metal> site:etsy.com"
- "<gem> pendant Ross-Simons price"
- "natural <gem> ring 14k gold price <retailer>"
- "Ceylon <gem> unheated certified <jewelry type> price"
Vary size (mm), metal (sterling, 14k gold, vermeil), and quality words (strong blue flash,
top blue, vivid). Aim to span affordable -> middle -> premium -> artisan -> luxury.
