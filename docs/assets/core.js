(function (root, factory) {
  if (typeof module === 'object' && module.exports) module.exports = factory(require('../vendor/pdf-lib-1.17.1.min.js'), require('../vendor/papaparse-5.5.3.min.js'));
  else root.Workbench = factory(root.PDFLib, root.Papa);
})(globalThis, function (PDFLib, Papa) {
  'use strict';
  function pageSelection(spec, count) {
    if (!Number.isInteger(count) || count < 1) throw new Error('This PDF has no pages.');
    if (!spec.trim()) throw new Error('Enter pages, for example 1,3-5.');
    const pages = [];
    for (const token of spec.split(',')) {
      const match = token.trim().match(/^(\d+)(?:\s*-\s*(\d+))?$/);
      if (!match) throw new Error('Use page numbers and ranges such as 1,3-5.');
      const first = Number(match[1]), last = Number(match[2] || match[1]);
      if (first < 1 || last > count || first > last) throw new Error(`Pages must be between 1 and ${count}; ranges must increase.`);
      for (let n = first; n <= last; n++) if (!pages.includes(n - 1)) pages.push(n - 1);
    }
    return pages;
  }
  async function loadPDF(bytes) {
    try { return await PDFLib.PDFDocument.load(bytes, { ignoreEncryption: false }); }
    catch (_) { throw new Error('Cannot read this PDF. Encrypted or damaged PDFs are not supported. Export an unlocked copy first.'); }
  }
  async function mergePDF(inputs) {
    if (inputs.length < 2) throw new Error('Choose at least two PDF files.');
    const output = await PDFLib.PDFDocument.create();
    for (const bytes of inputs) {
      const source = await loadPDF(bytes);
      for (const page of await output.copyPages(source, source.getPageIndices())) output.addPage(page);
    }
    return { bytes: await output.save(), pages: output.getPageCount() };
  }
  async function extractPDF(bytes, spec) {
    const source = await loadPDF(bytes), selection = pageSelection(spec, source.getPageCount());
    const output = await PDFLib.PDFDocument.create();
    for (const page of await output.copyPages(source, selection)) output.addPage(page);
    return { bytes: await output.save(), pages: output.getPageCount(), sourcePages: source.getPageCount(), selection: selection.map(n => n + 1) };
  }
  function parseCSV(text) {
    if (!text.trim()) throw new Error('Choose a CSV file or paste CSV text.');
    const parsed = Papa.parse(text.replace(/^\uFEFF/, ''), { skipEmptyLines: true, dynamicTyping: false });
    const errors = parsed.errors.filter(error => error.code !== 'UndetectableDelimiter');
    if (errors.length) throw new Error('CSV parsing error: ' + errors[0].message);
    if (!parsed.data.length) throw new Error('The CSV needs a header row.');
    const headers = parsed.data[0].map(h => String(h).trim());
    if (headers.some(h => !h)) throw new Error('Every column needs a non-empty header.');
    if (new Set(headers).size !== headers.length) throw new Error('Column headers must be unique. Rename duplicate headers first.');
    const rows = parsed.data.slice(1);
    for (let i = 0; i < rows.length; i++) if (rows[i].length !== headers.length) throw new Error(`Data row ${i + 1} has ${rows[i].length} values; expected ${headers.length}.`);
    return { headers, rows, delimiter: parsed.meta.delimiter };
  }
  function deduplicate(table, options = {}) {
    const column = options.column == null ? -1 : Number(options.column);
    if (!Number.isInteger(column) || column < -1 || column >= table.headers.length) throw new Error('Choose a valid duplicate key column.');
    const normalize = value => {
      let v = String(value);
      if (options.trim) v = v.trim();
      if (options.ignoreCase) v = v.toLocaleLowerCase('en-US');
      return v;
    };
    const seen = new Set(), kept = [];
    let indexed = table.rows.map((row, index) => ({ row, index }));
    if (options.keep === 'last') indexed.reverse();
    for (const item of indexed) {
      const values = column === -1 ? item.row : [item.row[column]];
      const key = JSON.stringify(values.map(normalize));
      if (!seen.has(key)) { seen.add(key); kept.push(item); }
    }
    kept.sort((a, b) => a.index - b.index);
    return { headers: table.headers, rows: kept.map(x => x.row), removed: table.rows.length - kept.length };
  }
  function csvOutput(table, escapeFormulae = false) {
    return Papa.unparse([table.headers, ...table.rows], { newline: '\r\n', escapeFormulae });
  }
  function jsonOutput(table) {
    return JSON.stringify(table.rows.map(row => Object.fromEntries(table.headers.map((header, i) => [header, row[i]]))), null, 2);
  }
  function fitSize(width, height, maxWidth, maxHeight) {
    if (![width, height, maxWidth, maxHeight].every(n => Number.isFinite(n) && n > 0)) throw new Error('Width and height must be positive numbers.');
    const scale = Math.min(1, maxWidth / width, maxHeight / height);
    return { width: Math.max(1, Math.round(width * scale)), height: Math.max(1, Math.round(height * scale)) };
  }
  async function convertImage(file, options) {
    if (!['image/png', 'image/jpeg', 'image/webp'].includes(file.type)) throw new Error('Choose a PNG, JPEG or WebP image. HEIC, SVG and GIF are not supported. Animation is not preserved.');
    if (file.size > 25 * 1024 * 1024) throw new Error('Choose an image smaller than 25 MiB.');
    const image = await createImageBitmap(file);
    try {
      if (image.width * image.height > 40e6) throw new Error('Images larger than 40 megapixels are not supported.');
      const size = fitSize(image.width, image.height, options.maxWidth, options.maxHeight);
      const canvas = document.createElement('canvas'); canvas.width = size.width; canvas.height = size.height;
      const context = canvas.getContext('2d');
      if (options.type === 'image/jpeg') { context.fillStyle = '#ffffff'; context.fillRect(0, 0, size.width, size.height); }
      context.drawImage(image, 0, 0, size.width, size.height);
      const blob = await new Promise(resolve => canvas.toBlob(resolve, options.type, options.quality));
      if (!blob || blob.type !== options.type) throw new Error('This browser could not encode the selected format. Try JPEG.');
      return { blob, ...size, originalWidth: image.width, originalHeight: image.height, inputBytes: file.size };
    } finally { image.close(); }
  }
  return { pageSelection, loadPDF, mergePDF, extractPDF, parseCSV, deduplicate, csvOutput, jsonOutput, fitSize, convertImage };
});
