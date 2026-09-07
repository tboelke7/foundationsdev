// Build the Batcha Gems top-picks Word document.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, HeadingLevel, AlignmentType,
  BorderStyle, ShadingType, Table, TableRow, TableCell, WidthType, PageBreak
} = require('docx');

const ROOT = path.resolve(__dirname, '..');
const picks = JSON.parse(fs.readFileSync(path.join(__dirname, 'picks_batcha.json')));
const DATE = '2026-09-07';

const NAVY = '123A4F', GOLD = 'B8862F', GREEN = '1C7A4A', GREY = '5B6472';
const tagColor = t => t === 'Best-seller' ? GREEN : (t === 'Unique' ? GOLD : NAVY);

const children = [];

// ---- Title block ----
children.push(new Paragraph({
  spacing: { after: 60 },
  children: [new TextRun({ text: 'Batcha Gems — Colombo', bold: true, size: 40, color: NAVY, font: 'Georgia' })]
}));
children.push(new Paragraph({
  spacing: { after: 120 },
  children: [new TextRun({ text: 'Top Picks for the U.S. Market — Best-Sellers & Most Unique', size: 26, color: GOLD, font: 'Georgia' })]
}));
children.push(new Paragraph({
  spacing: { after: 160 },
  children: [new TextRun({ text: `Prepared ${DATE}. 15 pieces selected from the atelier photos — each with what I believe the piece to be and an estimated comfortable U.S. retail.`, size: 20, color: GREY, italics: true })]
}));

// ---- Caveat box ----
const boxBorder = { style: BorderStyle.SINGLE, size: 6, color: 'E6D4A3' };
children.push(new Table({
  width: { size: 10800, type: WidthType.DXA },
  columnWidths: [10800],
  borders: { top: boxBorder, bottom: boxBorder, left: boxBorder, right: boxBorder,
             insideHorizontal: boxBorder, insideVertical: boxBorder },
  rows: [new TableRow({ children: [new TableCell({
    width: { size: 10800, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: 'F7F0DA' },
    margins: { top: 100, bottom: 100, left: 140, right: 140 },
    children: [
      new Paragraph({ spacing: { after: 60 }, children: [
        new TextRun({ text: 'How to read the prices. ', bold: true, size: 19, color: '7A5A12' }),
        new TextRun({ text: '"Comfortable U.S. retail" is what a U.S. boutique or online seller could realistically ASK and achieve for a comparable finished piece — not what to pay for it, and not an appraisal. These are fine-jewelry pieces (genuine Ceylon sapphires set in gold with diamonds), so values run much higher than silver goods.', size: 19 })
      ]}),
      new Paragraph({ spacing: { after: 60 }, children: [
        new TextRun({ text: 'Each piece shows two estimates. ', bold: true, size: 19, color: '7A5A12' }),
        new TextRun({ text: '"Heated" assumes good-quality HEATED Ceylon sapphire (the commercial norm). "Unheated (with lab report)" assumes the main/center sapphire is natural unheated with a reputable report (GRS / GIA / SSEF / Lotus). Carats are estimated from the photos.', size: 19 })
      ]}),
      new Paragraph({ children: [
        new TextRun({ text: 'The unheated premium is largest on single-stone blue-sapphire pieces and much smaller on multi-color fancy-melee pieces (heat status there is commercially minor and rarely certified). It does not apply to the moonstone / cat’s-eye pieces (moonstone is untreated), and for star sapphire the key is “no diffusion” + a sharp natural star rather than heat. Always confirm carat, treatment + report, metal purity/weight, and total diamond carat.', size: 19, italics: true })
      ]})
    ]
  })]})]
}));
children.push(new Paragraph({ spacing: { after: 120 }, children: [new TextRun({ text: '' })] }));

// ---- Pieces ----
const IMG_W = 300; // px display width
picks.forEach((p, i) => {
  const h = Math.round(IMG_W * (p.h / p.w));
  children.push(new Paragraph({
    heading: HeadingLevel.HEADING_2,
    spacing: { before: 160, after: 60 },
    keepNext: true,
    children: [
      new TextRun({ text: `${i + 1}.  ${p.title}   `, bold: true, size: 24, color: NAVY, font: 'Georgia' }),
      new TextRun({ text: `[${p.tag}]`, bold: true, size: 16, color: tagColor(p.tag) })
    ]
  }));
  children.push(new Paragraph({
    alignment: AlignmentType.CENTER,
    spacing: { after: 80 },
    keepNext: true,
    children: [new ImageRun({
      type: 'jpg',
      data: fs.readFileSync(p.file),
      transformation: { width: IMG_W, height: h }
    })]
  }));
  const line = (label, val) => new Paragraph({
    spacing: { after: 30 },
    children: [
      new TextRun({ text: `${label}  `, bold: true, size: 19, color: GREY }),
      new TextRun({ text: val, size: 19 })
    ]
  });
  children.push(line('Type / Gem / Metal:', `${p.jtype} · ${p.gem} · ${p.metal}`));
  children.push(line('What it is:', p.specifics));
  // Heated price line
  children.push(new Paragraph({
    spacing: { after: 20 },
    children: [
      new TextRun({ text: 'Est. U.S. retail — heated:  ', bold: true, size: 20, color: NAVY }),
      new TextRun({ text: `$${p.lo.toLocaleString()} – $${p.hi.toLocaleString()}`, bold: true, size: 22, color: GREEN })
    ]
  }));
  // Unheated price line (or N/A)
  const uhRun = (p.uh_lo && p.uh_hi)
    ? new TextRun({ text: `$${p.uh_lo.toLocaleString()} – $${p.uh_hi.toLocaleString()}`, bold: true, size: 22, color: GOLD })
    : new TextRun({ text: 'not applicable (untreated stone — see note)', italics: true, size: 19, color: GREY });
  children.push(new Paragraph({
    spacing: { after: 20 },
    children: [
      new TextRun({ text: 'Est. U.S. retail — unheated (w/ report):  ', bold: true, size: 20, color: NAVY }),
      uhRun
    ]
  }));
  children.push(new Paragraph({
    spacing: { after: 20 },
    children: [
      new TextRun({ text: 'Heated vs unheated:  ', bold: true, size: 17, color: GREY }),
      new TextRun({ text: p.heat, italics: true, size: 17, color: GREY })
    ]
  }));
  children.push(new Paragraph({
    spacing: { after: 60 },
    children: [new TextRun({ text: `Also confirm: ${p.note}`, italics: true, size: 17, color: GREY })]
  }));
  // light divider between pieces; Word paginates naturally (heading+image kept together)
  children.push(new Paragraph({
    spacing: { after: 60 },
    border: { bottom: { style: BorderStyle.SINGLE, size: 4, color: 'E3DDD0' } },
    children: [new TextRun({ text: '' })]
  }));
});

// ---- Footer note ----
children.push(new Paragraph({
  spacing: { before: 200 },
  border: { top: { style: BorderStyle.SINGLE, size: 4, color: 'CCCCCC' } },
  children: [new TextRun({
    text: 'Estimates only — not an appraisal or guaranteed resale value. All stones described as sapphire are assumed genuine Ceylon sapphire per the supplier (Batcha Gems, Colombo). Verify species, origin, treatment, carat, metal purity/weight and any lab reports on each piece before purchase, and get the supplier’s trade price and export/shipping terms.',
    size: 16, color: GREY, italics: true })]
}));

const doc = new Document({
  creator: 'Sri Lanka Jewelry Buying Guide',
  title: 'Batcha Gems — Top Picks',
  styles: { default: { document: { run: { font: 'Calibri', size: 20 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 720, bottom: 720, left: 720, right: 720 } } },
    children
  }]
});

Packer.toBuffer(doc).then(buf => {
  const out = path.join(ROOT, 'Batcha_Gems_Top_Picks.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, buf.length, 'bytes');
});
