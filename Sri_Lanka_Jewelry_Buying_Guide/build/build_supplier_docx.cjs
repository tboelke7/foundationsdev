// Supplier questionnaire to send to Batcha Gems — photo + fill-in fields per piece.
const fs = require('fs');
const path = require('path');
const {
  Document, Packer, Paragraph, TextRun, ImageRun, HeadingLevel, AlignmentType,
  BorderStyle, ShadingType, Table, TableRow, TableCell, WidthType, PageBreak
} = require('docx');

const ROOT = path.resolve(__dirname, '..');
const recs = JSON.parse(fs.readFileSync(path.join(__dirname, 'selected_data.json')));
const DATE = '2026-09-09';
const NAVY = '123A4F', GOLD = 'B8862F', GREY = '5B6472', RED = 'A5362D';

const children = [];
const P = (runs, opts = {}) => new Paragraph({ spacing: { after: 40, ...(opts.spacing || {}) }, ...opts, children: runs });
const T = (text, o = {}) => new TextRun({ text, size: 19, ...o });

// field line with a blank underline
function field(label, hint) {
  const runs = [ new TextRun({ text: label + '  ', bold: true, size: 18, color: NAVY }) ];
  if (hint) runs.push(new TextRun({ text: hint + '  ', italics: true, size: 15, color: GREY }));
  runs.push(new TextRun({ text: '________________________________________', size: 18, color: 'B9B9B9' }));
  return new Paragraph({ spacing: { after: 24 }, children: runs });
}

// ---- Cover ----
children.push(P([new TextRun({ text: 'Batcha Gems — Product Information Request', bold: true, size: 34, color: NAVY, font: 'Georgia' })], { spacing: { after: 60 } }));
children.push(P([T('For listing on our U.S. website. Prepared ' + DATE + '.', { italics: true, color: GREY, size: 18 })], { spacing: { after: 120 } }));
children.push(P([
  T('Thank you again! We would love to list the following pieces on our U.S. site. To create accurate listings and work out our delivered cost, could you please fill in the details below for each numbered piece (the photos are your pieces, with our reference number BG-xx). Where a photo shows several pieces, please give the details for each piece separately (its own stock number). Feel free to reply on this document, by email, or on a spreadsheet — whatever is easiest.')
], { spacing: { after: 120 } }));

// ---- Global section box ----
const bd = { style: BorderStyle.SINGLE, size: 6, color: 'E6D4A3' };
children.push(new Table({
  width: { size: 10800, type: WidthType.DXA }, columnWidths: [10800],
  borders: { top: bd, bottom: bd, left: bd, right: bd, insideHorizontal: bd, insideVertical: bd },
  rows: [new TableRow({ children: [new TableCell({
    width: { size: 10800, type: WidthType.DXA },
    shading: { type: ShadingType.CLEAR, fill: 'F7F0DA' },
    margins: { top: 120, bottom: 120, left: 160, right: 160 },
    children: [
      P([new TextRun({ text: 'A few questions that apply to everything', bold: true, size: 22, color: '7A5A12' })], { spacing: { after: 60 } }),
      field('Can you export directly to the U.S. and handle the NGJA export paperwork on your side?'),
      field('Insured courier you use + typical cost & transit time to the U.S.:'),
      field('DELIVERED / LANDED price to our U.S. address (ZIP: __________) — including insured shipping, export fees and any duties — per piece, if you can quote it:'),
      field('Professional images: can you provide high-resolution photos (several angles, on a white background) and a short video for each piece — with permission for us to use them in our online listings?', 'format & turnaround?'),
      field('Accepted payment methods for international orders:'),
      field('Production / lead time if we re-order a piece:'),
      field('Return / exchange / warranty policy:'),
    ]
  })]})]
}));
children.push(P([T('')], { spacing: { after: 60 } }));

children.push(P([
  new TextRun({ text: 'For EACH piece below, please provide: ', bold: true, size: 19, color: NAVY }),
  T('stock #, gem & treatment, lab report, carat & size, metal & weight, price, sizing/variants, and whether it belongs to a set. Treatment and lab report are the most important for us — thank you!')
], { spacing: { after: 120 } }));
children.push(new Paragraph({ children: [new PageBreak()] }));

// ---- Per-piece blocks ----
const IMG_W = 150;
let onPage = 0;
recs.forEach((rec) => {
  if (rec.multi === 2) return; // skip overview photo
  const h = Math.round(IMG_W * (rec.h / rec.w));
  const isMulti = rec.multi === 1;

  // header row: photo + ref/name
  const headerCells = [
    new TableCell({
      width: { size: 2400, type: WidthType.DXA },
      verticalAlign: 'center',
      margins: { top: 40, bottom: 40, left: 40, right: 60 },
      children: [new Paragraph({ alignment: AlignmentType.CENTER, children: [new ImageRun({ type: 'jpg', data: fs.readFileSync(rec.thumb), transformation: { width: IMG_W, height: h } })] })]
    }),
    new TableCell({
      width: { size: 8400, type: WidthType.DXA },
      verticalAlign: 'top',
      margins: { top: 40, bottom: 40, left: 80, right: 40 },
      children: (() => {
        const cc = [
          P([new TextRun({ text: `${rec.bg}  `, bold: true, size: 22, color: GOLD, font: 'monospace' }),
             new TextRun({ text: rec.name, bold: true, size: 20, color: NAVY, font: 'Georgia' })], { spacing: { after: 40 } }),
        ];
        if (isMulti) cc.push(P([new TextRun({ text: '⚠ This photo shows several pieces — please list EACH one separately (its own stock #, carat, size and price).', bold: true, size: 17, color: RED })], { spacing: { after: 40 } }));
        cc.push(field('Your stock / SKU #:'));
        cc.push(field('Gemstone, variety & colour:', 'e.g. Ceylon blue sapphire'));
        cc.push(field('Ceylon / Sri Lanka origin — documented?  Natural or synthetic?'));
        cc.push(new Paragraph({ spacing: { after: 24 }, children: [
          new TextRun({ text: 'Treatment — HEATED or UNHEATED? (and any other treatment):  ', bold: true, size: 18, color: RED }),
          new TextRun({ text: '________________________________', size: 18, color: 'B9B9B9' })]}));
        cc.push(field('Lab report? (GRS / GIA / SSEF / Lotus / GIT) — number, and included in price?'));
        cc.push(field('Carat weight — centre stone / total:'));
        cc.push(field('Main stone size (mm) & cut:'));
        cc.push(field('Diamonds (if any) — total ct, natural or lab-grown, colour/clarity:'));
        cc.push(field('Metal — type, purity (14k/18k/22k/platinum) & colour + gross weight (grams):'));
        cc.push(field('Handmade / cast / CAD?  One-of-a-kind or can it be re-made?'));
        if (rec.ring) cc.push(new Paragraph({ spacing: { after: 24 }, children: [
          new TextRun({ text: 'Ring size now + resizable range (min–max) + cost & time to resize:  ', bold: true, size: 18, color: NAVY }),
          new TextRun({ text: '____________________________', size: 18, color: 'B9B9B9' })]}));
        cc.push(field('Other versions available (gem colour / size / carat):'));
        cc.push(new Paragraph({ spacing: { after: 24 }, children: [
          new TextRun({ text: 'Part of a set? matching pieces available + their prices:  ', bold: true, size: 18, color: NAVY }),
          new TextRun({ text: (rec.set ? `(we think: ${rec.set})  ` : ''), italics: true, size: 15, color: GREY }),
          new TextRun({ text: '____________________', size: 18, color: 'B9B9B9' })]}));
        cc.push(field('Your trade price (USD) / normal retail (USD):'));
        cc.push(field('Delivered/landed price to our ZIP (incl. insured shipping + export + duty):'));
        cc.push(field('High-res photos + video available for this piece?  (Y / N)'));
        return cc;
      })()
    })
  ];
  const cellBorder = { style: BorderStyle.SINGLE, size: 4, color: 'D8D2C4' };
  children.push(new Table({
    width: { size: 10800, type: WidthType.DXA }, columnWidths: [2400, 8400],
    borders: { top: cellBorder, bottom: cellBorder, left: cellBorder, right: cellBorder, insideHorizontal: cellBorder, insideVertical: cellBorder },
    rows: [new TableRow({ cantSplit: true, children: headerCells })]
  }));
  children.push(P([T('')], { spacing: { after: 60 } }));
  onPage++;
  if (onPage % 2 === 0) children.push(new Paragraph({ children: [new PageBreak()] }));
});

children.push(P([new TextRun({ text: 'Thank you very much — this lets us build proper listings and price everything correctly for the U.S. market. We are excited to work together!', italics: true, size: 19, color: GREY })], { spacing: { before: 160 } }));

const doc = new Document({
  creator: 'Sri Lanka Jewelry Buying Guide',
  title: 'Batcha Gems — Product Information Request',
  styles: { default: { document: { run: { font: 'Calibri', size: 19 } } } },
  sections: [{
    properties: { page: { size: { width: 12240, height: 15840 }, margin: { top: 700, bottom: 700, left: 720, right: 720 } } },
    children
  }]
});
Packer.toBuffer(doc).then(buf => {
  const out = path.join(ROOT, 'Batcha_Supplier_Questionnaire.docx');
  fs.writeFileSync(out, buf);
  console.log('wrote', out, buf.length, 'bytes');
});
