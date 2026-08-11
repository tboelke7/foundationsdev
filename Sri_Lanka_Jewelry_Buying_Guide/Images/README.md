# Images

These per-category folders are intentionally part of the deliverable structure, but they
are **empty of downloaded product photos**. The environment this guide was built in
enforces a network egress policy that **blocks downloading images and fetching retail
product pages** (every retail image host returned HTTP 403 at the proxy, and page fetches
were blocked). Routing around that policy was not permitted.

Rather than fabricate or substitute generic stock photos, no images were embedded.

### How to get the photos
- Open `../Jewelry_Buying_Field_Guide.html` **on a device with open internet**; product
  photos load where the listing exposes an image, and every card links to its listing.
- Or open the listing URLs in `../Sources.csv` / the `Comparables` tab of
  `../Retail_Comparables.xlsx` and save the images you want into the matching folder here.
- Or re-run `../build/` on a machine with open internet; the build can be extended to
  download each listing's primary image into these folders.

Folders: Moonstone, Rainbow_Moonstone, Sapphire, Star_Sapphire, Padparadscha, Cats_Eye,
Alexandrite, Spinel, Zircon, Hessonite.
