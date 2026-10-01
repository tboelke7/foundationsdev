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
  whatsapp: "18134028393", // E.164, no plus — used in wa.me links
  whatsappHref: "https://wa.me/18134028393?text=" + encodeURIComponent("Hi Foundations, I'd like to ask about a Guest Experience Audit."),
  region: "Tampa Bay",
  city: "Brandon",
  state: "FL",
  serviceAreas: ["Brandon", "Tampa", "Riverview", "Valrico", "Lithia", "Plant City", "Seffner"],
  hubspotPortalId: "246368131",
};

export const services = [
  { slug: "web-presence-builds", title: "Web Presence Builds", icon: "globe", addon: false, group: "Build & Own",
    tease: "Fast, owned sites that convert",
    image: "/images/svc-web.webp",
    blurb: "Fast, owned, conversion-built websites — not a rented page on someone else's platform.",
    intro: "Your website is the foundation everything else stands on. We build it on a clean, fast stack that loads in under a second, ranks in local search, and turns visitors into booked calls — and you own every piece of it.",
    points: [
      "Custom-built site on a fast static stack — no bloated templates",
      "You own the domain, the code, and every asset, forever",
      "Mobile-first design that looks sharp on every screen",
      "Built-in lead capture wired straight to your inbox or CRM",
      "Local SEO foundation baked in from day one",
      "No monthly platform fees, no holding your site hostage",
    ] },
  { slug: "google-business-profile", title: "Google Business Profile", icon: "pin", addon: false, group: "Get Found",
    tease: "Claimed, optimized, posting weekly",
    image: "/images/svc-gbp.webp",
    blurb: "The single highest-leverage local SEO move — claimed, optimized, and posting weekly.",
    intro: "For a local contractor, your Google Business Profile is often the first thing a homeowner sees — and most are half-built. We claim it, fully optimize it, and keep it active so you show up in the map pack when it counts.",
    points: [
      "Full claim and verification of your profile",
      "Complete optimization — categories, services, service areas, hours",
      "Professional photos and descriptions that build trust",
      "Weekly posts to keep your profile active and ranking",
      "Review monitoring so you never miss a customer",
      "The groundwork that gets you into Google's local map pack",
    ] },
  { slug: "local-seo", title: "Local SEO", icon: "search", addon: false, group: "Get Found",
    tease: "Rank in your service area",
    image: "/images/svc-seo.webp",
    blurb: "Service and area pages built to rank, so homeowners nearby find you first.",
    intro: "When a homeowner searches for what you do in your town, you want to be the first name they see. We build the page structure, content, and on-page signals local search rewards — so you get found by people ready to hire.",
    points: [
      "Dedicated service pages for everything you do",
      "Area pages targeting each town you serve",
      "Keyword research focused on real buyer searches",
      "On-page optimization — titles, meta, schema markup",
      "Google Search Console setup and monitoring",
      "Content that compounds in the rankings month over month",
    ] },
  { slug: "lead-generation-ads", title: "Lead Generation", icon: "target", addon: false, group: "Get Found",
    tease: "Meta & Google, no ad-spend markup",
    image: "/images/svc-leads.webp",
    blurb: "Meta & Google campaigns that put real leads in your pipeline — no markup on your ad spend.",
    intro: "When you need leads now, paid ads deliver. We build and run Meta and Google campaigns aimed at booked calls — not vanity clicks — and we never take a cut of your ad budget. You see exactly where every dollar goes.",
    points: [
      "Meta (Facebook & Instagram) lead campaigns",
      "Google Local Services and Search campaigns",
      "Ad creative and copy built to drive real inquiries",
      "Audience and location targeting dialed to your service area",
      "Zero markup on your ad spend — your budget is your budget",
      "Paired with speed-to-lead so no lead goes cold",
    ] },
  { slug: "speed-to-lead-automation", title: "Speed-to-Lead Automation", icon: "bolt", addon: false, group: "Convert & Grow",
    tease: "Auto-text every new lead in seconds",
    image: "/images/svc-speed.webp",
    blurb: "Every new lead gets an automatic text in seconds — before your competitor even sees them.",
    intro: "The contractor who responds first usually wins the job. The moment a lead comes in, an automated text fires on your behalf — so you're first in line every time, even when you're up on a roof or under a sink.",
    points: [
      "Instant automated SMS the second a lead comes in",
      "Keeps you first to respond — where most jobs are won",
      "Automatic email follow-up as a backup net",
      "Works around the clock, even after hours",
      "Every lead logged so nothing slips through the cracks",
      "Frees you to do the work without losing the next job",
    ] },
  { slug: "social-content", title: "Social Media & Content", icon: "image", addon: false, group: "Convert & Grow",
    tease: "Posts, custom images, full content library",
    image: "/images/svc-social.webp",
    blurb: "Consistent posts and custom branded images — drawn from our full content library.",
    intro: "An active, professional social presence tells homeowners you're the real deal. We keep your profiles posting consistently with custom branded images from our content library — so your feed always looks sharp without you touching it.",
    points: [
      "Consistent posting across your social platforms",
      "Custom branded images made for your business",
      "Full access to our professional content library",
      "Monthly content calendar planned for you",
      "Blog posts that feed your SEO and your feed",
      "Reels and short video on higher tiers",
    ] },
  { slug: "review-generation", title: "Review Generation", icon: "star", addon: false, group: "Convert & Grow",
    tease: "A steady stream of 5-star reviews",
    image: "/images/svc-reviews.webp",
    blurb: "A steady stream of real 5-star reviews — the trust signal that wins the click.",
    intro: "Reviews are the deciding factor for most homeowners. We build a simple system that asks your happy customers at exactly the right moment — so your star rating and review count keep climbing and keep winning you the next call.",
    points: [
      "Automated review requests timed to the job's finish",
      "Makes leaving a review effortless for your customers",
      "Steady growth in your star rating and review count",
      "Funnels happy customers to Google and Facebook",
      "Alerts so you can respond to every review",
      "The trust signal that wins the click over competitors",
    ] },
  { slug: "reputation-management", title: "Reputation Management", icon: "shield", addon: true, group: "Convert & Grow",
    tease: "Monitor reviews & mentions — add-on",
    image: "/images/svc-reputation.webp",
    blurb: "Stay on top of every review and mention across the web — your digital image, watched and managed.",
    intro: "Your reputation lives across dozens of sites. As an optional add-on, we monitor your reviews and mentions across platforms and help you manage them — so your digital image stays clean, current, and working for you.",
    points: [
      "Monitoring of reviews and mentions across platforms",
      "Alerts the moment something needs your attention",
      "Help crafting professional responses",
      "A consistent, trustworthy image everywhere you appear",
      "No added software fees — monitoring is handled for you",
      "Available as an add-on to any monthly plan",
    ] },
];

export const menuGroups = ["Build & Own", "Get Found", "Convert & Grow"];

export const buildTiers = [
  { name: "Footprint", price: "$750",
    desc: "A clean, fast one-page site built to get you found and capturing leads.",
    includes: [
      "Custom one-page website you own outright",
      "Mobile-first, loads in under a second",
      "Lead capture form wired to your inbox",
      "Click-to-call and click-to-text buttons",
      "Google Business Profile setup",
      "Basic local SEO — titles, meta, your core service & area",
      "SSL secured and launch-ready",
    ] },
  { name: "Blueprint", price: "$1,500", featured: true,
    desc: "A multi-page site with service and area pages — built to rank locally and convert.",
    includes: [
      "Everything in Footprint, plus:",
      "Multi-page website (home, services, about, contact)",
      "Dedicated service pages for what you do",
      "Area pages for the towns you serve",
      "Expanded local SEO foundation",
      "Photo gallery to show off your work",
      "Lead capture wired to your CRM",
      "Speed-to-lead automation ready to switch on",
    ] },
  { name: "Launchpad", price: "$2,500",
    desc: "The full presence: multi-page site, SEO foundation, and the back-office systems that compound.",
    includes: [
      "Everything in Blueprint, plus:",
      "Full brand guide — fonts, colors, voice, templates",
      "Email marketing setup — list + welcome sequence",
      "CRM setup — full lead pipeline (HubSpot)",
      "Estimate & invoice system setup (QuickBooks)",
      "Advanced SEO foundation + Search Console",
      "Full training workshop so you know your tools",
      "Priority support",
    ] },
];

// Rebrand path (shown as add-on options on pricing page)
export const rebrandOptions = [
  { name: "Brand Refresh", price: "$250", desc: "Polish what you have — refined logo treatment, color cleanup, and consistent fonts across your site and profiles." },
  { name: "Full Rebrand", price: "$1,200", desc: "Start fresh — new logo suite, complete brand guide, vehicle and signage templates, and a full website overhaul to match." },
];

export const monthlyPlans = [
  { name: "Signal", price: "$269", per:"/mo", tagline:"Stay found and active.",
    includes: [
      "Google Business Profile management",
      "Weekly GBP posts",
      "2 social posts / week",
      "Custom branded images from our content library",
      "Review generation system",
      "Monthly performance snapshot",
    ] },
  { name: "Momentum", price: "$369", per:"/mo", featured:true, tagline:"Build momentum every month.",
    inheritsFrom: "Signal",
    includes: [
      "3 social posts / week",
      "1 blog post / month",
      "Active local SEO work",
      "Content calendar",
      "Quarterly strategy check-in",
    ] },
  { name: "Builder", price: "$469", per:"/mo", tagline:"The full growth engine.",
    inheritsFrom: "Momentum",
    includes: [
      "4–5 social posts / week",
      "2 blog posts / month",
      "Monthly Reels / short video",
      "Priority support",
      "Expanded content library access",
    ] },
];

// ============================================================
// INTERNATIONAL GUEST EXPERIENCE AUDIT (Sri Lanka hospitality)
// Page: /international-guest-audit/
// Copy rules: no AI in our process, no em dashes, Sri Lanka only,
// no health claims, no client names or testimonials yet.
// ============================================================
export const guestAudit = {
  path: "/international-guest-audit/",
  title: "International Guest Experience Audit",
  navTease: "Sri Lanka hospitality: guest-ready English",
  // HubSpot: same form as /contact/. CTAs add ?service_interest=<value> to the page URL.
  // To capture it as a field, create a contact property with the internal name below and
  // add it to the form as a hidden field. Until then, the page URL on each submission
  // still shows which inquiry it was.
  form: {
    formId: "c03b7a6e-540a-47dc-81c8-4f33737411c5",
    serviceField: "service_interest",
    auditValue: "Guest Experience Audit",
    partnerValue: "Audit Partner Program",
  },
  capabilities: [
    { title: "Bilingual Meaning Verification",
      body: "Is the translation actually saying what you intend? We catch cases where the English is technically correct but the meaning is wrong. Our team includes native fluency in both English and Sri Lankan languages." },
    { title: "Native-Level English QA",
      body: "Every guest-facing word is reviewed by a U.S.-certified English teacher, a Mississippi Teacher of the Year finalist, for clarity, tone, and brand fit. Not just grammar. We make sure it reads naturally to an international guest." },
    { title: "Human-Verified Accountability",
      body: "We take responsibility for the final output. Every correction is verified by a human expert before you receive it. That checkpoint is what makes this different from AI-only solutions." },
  ],
  tiers: [
    { name: "Quick Guest Language Review", price: "$75 to $150", per: "one-time",
      fit: "Perfect for cafes, small restaurants, guesthouses.",
      includes: [
        "Review of all guest-facing materials, everything they see and read",
        "Menus, signage, website, policies, booking confirmations",
        "Issues identified with clear corrections",
        "Corrected copy ready to implement",
        "Turnaround: 5 to 7 business days",
      ],
      cta: "Request a Review" },
    { name: "Full Property Audit + Remediation", price: "$300 to $2,500+", per: "one-time", featured: true,
      fit: "Perfect for hotels, resorts, multi-outlet properties.",
      includes: [
        "Complete audit of everything guests see and read: signage and wayfinding, menus, website and booking copy, policies, room materials, promotional content",
        "All issues prioritized with corrected copy",
        "Remediation coordination with your printer, designer, or web team",
        "Turnaround: 10 to 15 business days",
      ],
      sizing: [
        { label: "Boutique or small resort", price: "$300 to $750" },
        { label: "Mid-size resort", price: "$750 to $1,500" },
        { label: "Large or luxury resort", price: "$1,500 to $2,500+" },
      ],
      cta: "Request an Audit" },
    { name: "Annual Assurance", price: "$150 to $450", per: "per month",
      fit: "For large resorts and properties launching new menus, signage, and campaigns regularly.",
      includes: [
        "New content reviewed and returned within 2 to 3 business days",
        "Quarterly consistency and brand-voice reviews",
        "Priority turnaround",
      ],
      cta: "Learn More" },
  ],
  process: [
    { title: "Comprehensive audit", body: "We review everything your guests see and read, physical and digital." },
    { title: "Issue identification", body: "Every problem is found and ranked by severity, from wrong meaning to brand-quality polish." },
    { title: "Human quality review", body: "Every issue is verified by our bilingual team. We confirm meaning, tone, and brand fit. If something is ambiguous, we ask you. We never guess." },
    { title: "Corrected copy delivery", body: "You receive a clear report: current copy, recommended copy, and why. Ready to implement." },
    { title: "Implementation support", body: "We coordinate with your printer, designer, or web team as needed. You own the relationships and the accounts." },
  ],
  faqs: [
    { q: "Why not just use AI, like ChatGPT?",
      a: "AI can beautifully rewrite a sentence. That's the easy part. But a mistranslation can sound perfect in English. AI will polish it, you'll publish it, and your guests will wonder why your menu sounds strange. AI has no way to verify that the meaning is right, and no one is accountable if it sounds off to your guests. Every piece of copy we deliver goes through human review. We verify the meaning, not just the grammar. We own the checkpoint." },
    { q: "How is this different from a translation service?",
      a: "We don't translate. We verify meaning, tone, and brand fit in the English your guests already see, and we position unfamiliar items so international guests understand and want them." },
    { q: "Is this one invoice or two?",
      a: "One. Audit, corrections, and implementation support are a single package. No separate remediation fee." },
    { q: "What exactly do you audit?",
      a: "Everything your guests encounter: signage, menus, website and booking pages, confirmation emails, room materials, policies, and promotional content. What they see and what they read." },
    { q: "Do you work with our printer or designer?",
      a: "Yes. We provide corrected copy your vendors can implement directly, and we coordinate with them at no extra cost." },
    { q: "Can we start small?",
      a: "Absolutely. Many properties start with a Quick Review and expand to a full audit later. No lock-in." },
    { q: "What if we update menus and signage often?",
      a: "That's what Annual Assurance is for. Send us new content and it comes back reviewed within 2 to 3 business days." },
    { q: "What counts as one item on the Partner Plan?",
      a: "One item is one printed side, panel, or board of up to about 150 words: a banner, a sign, a poster, a flyer side, a label, or a single menu board. Larger pieces count by the page or panel, so a six-page menu is six items. Re-checking artwork after you apply our corrections is always free and never uses an item. Full websites, booking systems, and complete property materials are not Partner Plan items; those are quoted as a Guest Experience Audit." },
    { q: "Do you work outside Sri Lanka?",
      a: "We currently specialize in Sri Lankan hospitality because of our deep cultural and bilingual foundation there." },
  ],
};

// Link to the audit request form, tagged with the inquiry type (see guestAudit.form).
export const guestAuditHref = (value) =>
  `${guestAudit.path}?${guestAudit.form.serviceField}=${encodeURIComponent(value)}#request`;

export const steps = [
  { n:"01", title:"We grade you", body:"Start with a free Web Presence Report Card — your site, profile, reviews, and SEO scored A–F across 8 dimensions." },
  { n:"02", title:"We build the base", body:"A fast, owned website and a fully optimized Google profile — the foundation everything else stands on." },
  { n:"03", title:"We compound it", body:"Reviews, content, and local SEO that keep working every month, so you get found and chosen over time." },
];

export const problems = [
  { pain:"My ad spend keeps climbing but the leads don't.",
    fix:"We run lead-focused campaigns with speed-to-lead automation, and we never mark up your ad spend — so every dollar works and every lead gets a text in seconds." },
  { pain:"I build like an A but show up online like a C.",
    fix:"We build the fast, owned web presence your reputation already earned — then keep it active with posts, reviews, and local SEO so homeowners actually find it." },
  { pain:"I'm renting my website and don't own a thing.",
    fix:"Everything we build is yours — domain, code, content, all of it. No platform hostage fees. Walk away anytime and it's still yours." },
];
