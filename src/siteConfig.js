// ============================================================
// FOUNDATIONS — single source of truth. Edit this file only.
// ============================================================
export const site = {
  name: "Foundations Business Development",
  shortName: "Foundations",
  tagline: "Build the base. Build the business.",
  domain: "foundationsdev.com",
  url: "https://foundationsdev.com",
  email: "troy@bdfoundations.com",
  phone: "(813) 402-8393",
  phoneRaw: "8134028393",
  region: "Tampa Bay",
  city: "Brandon",
  state: "FL",
  serviceAreas: ["Brandon", "Tampa", "Riverview", "Valrico", "Lithia", "Plant City", "Seffner"],
  hubspotPortalId: "246368131",
};

// icon = key matched in the Icon.astro component
export const services = [
  { slug: "web-presence-builds", title: "Web Presence Builds", icon: "globe", addon: false,
    blurb: "Fast, owned, conversion-built websites — not a rented page on someone else's platform.",
    body: "We build your site on a clean static stack that loads fast and ranks. You own the domain, the code, and every asset. No monthly platform hostage fees, no markup on your ad spend." },
  { slug: "google-business-profile", title: "Google Business Profile", icon: "pin", addon: false,
    blurb: "The single highest-leverage local SEO move — claimed, optimized, and posting weekly.",
    body: "Most contractors leave their Google Business Profile half-built. We claim it, fully optimize it, and keep it active with weekly posts so you show up when homeowners search nearby." },
  { slug: "lead-generation-ads", title: "Lead Generation", icon: "target", addon: false,
    blurb: "Meta & Google campaigns that put real leads in your pipeline — no markup on your ad spend.",
    body: "We run Meta and Google Local Services campaigns built to generate booked calls, not vanity clicks. You see exactly what's spent. We never mark up your ad budget." },
  { slug: "speed-to-lead-automation", title: "Speed-to-Lead Automation", icon: "bolt", addon: false,
    blurb: "Every new lead gets an automatic text in seconds — before your competitor even sees them.",
    body: "When a lead comes in, an automated SMS fires instantly. The contractor who responds first usually wins the job. We make sure that's always you." },
  { slug: "review-generation", title: "Review Generation", icon: "star", addon: false,
    blurb: "A steady stream of real 5-star reviews — the trust signal that wins the click.",
    body: "We build a simple system that asks happy customers for reviews at the right moment, so your star rating and review count keep climbing and keep earning you the next call." },
  { slug: "reputation-management", title: "Reputation Management", icon: "shield", addon: true,
    blurb: "Stay on top of every review and mention across the web — your digital image, watched and managed.",
    body: "An optional add-on: we monitor and help manage your reviews and social mentions across platforms so your reputation stays clean and current. Built on a no-extra-cost monitoring tool, it keeps you in the loop without adding software fees — you just respond when it matters." },
];

export const buildTiers = [
  { name: "Footprint", price: "$750", desc: "A clean, fast one-page site built to capture leads. Perfect to get found and start converting." },
  { name: "Blueprint", price: "$1,500", desc: "A multi-page site with service and area pages — built to rank locally and convert.", featured: true },
  { name: "Launchpad", price: "$2,500", desc: "The full presence: multi-page site, SEO foundation, and the systems to compound over time." },
];

export const monthlyPlans = [
  { name: "Signal", price: "$269", per:"/mo", desc: "Google Business Profile posting, review generation, and basic maintenance." },
  { name: "Momentum", price: "$369", per:"/mo", desc: "Everything in Signal plus ongoing content and active local SEO work.", featured: true },
  { name: "Builder", price: "$469", per:"/mo", desc: "The full engine: content, SEO, reviews, and priority support." },
];

export const steps = [
  { n:"01", title:"We grade you", body:"Start with a free Web Presence Report Card — your site, profile, reviews, and SEO scored A–F across 8 dimensions." },
  { n:"02", title:"We build the base", body:"A fast, owned website and a fully optimized Google profile — the foundation everything else stands on." },
  { n:"03", title:"We compound it", body:"Reviews, content, and local SEO that keep working every month, so you get found and chosen over time." },
];
