const { test } = require('node:test');
const assert = require('node:assert/strict');
const W = require('../docs/assets/core.js');
const { PDFDocument } = require('../docs/vendor/pdf-lib-1.17.1.min.js');
async function fixture(widths) { const pdf = await PDFDocument.create(); for (const width of widths) pdf.addPage([width, 400]); return pdf.save(); }
test('merged PDF preserves file order and page geometry', async () => {
  const a = await fixture([300, 350]), b = await fixture([420]);
  const output = await W.mergePDF([a, b]); const pdf = await PDFDocument.load(output.bytes);
  assert.equal(output.pages, 3); assert.deepEqual(pdf.getPages().map(p => p.getWidth()), [300, 350, 420]);
});
test('PDF extraction respects requested order, deduplicates and rejects invalid pages', async () => {
  const output = await W.extractPDF(await fixture([300, 350, 420]), '3,1,3');
  const pdf = await PDFDocument.load(output.bytes);
  assert.deepEqual(output.selection, [3, 1]); assert.deepEqual(pdf.getPages().map(p => p.getWidth()), [420, 300]);
  for (const input of ['0', '4', '3-1', '1,banana', '']) assert.throws(() => W.pageSelection(input, 3));
});
test('PDF malformed input reports an actionable error', async () => { await assert.rejects(W.extractPDF(new Uint8Array([1, 2, 3]), '1'), /Cannot read this PDF/); });
test('CSV quoted commas, multiline cells, BOM and leading zeros survive JSON conversion', () => {
  const table = W.parseCSV('\ufeffid,note\r\n001,"hello, world"\r\n002,"first\nsecond"\r\n');
  const records = JSON.parse(W.jsonOutput(table));
  assert.equal(records[0].id, '001'); assert.equal(records[0].note, 'hello, world'); assert.equal(records[1].note, 'first\nsecond');
});
test('CSV ambiguous headers and ragged records fail instead of losing data', () => {
  assert.throws(() => W.parseCSV('name,name\na,b'), /unique/);
  assert.throws(() => W.parseCSV('name,\na,b'), /non-empty/);
  assert.throws(() => W.parseCSV('name,email\na,b,c'), /expected 2/);
});
test('dedup by a chosen key preserves first or last row in original order', () => {
  const table = W.parseCSV('name,email\nAda,A@x.test\nBob,b@x.test\nAda New,a@x.test');
  assert.equal(W.deduplicate(table, { column: 1 }).removed, 0);
  assert.deepEqual(W.deduplicate(table, { column: 1, ignoreCase: true }).rows.map(r => r[0]), ['Ada', 'Bob']);
  assert.deepEqual(W.deduplicate(table, { column: 1, ignoreCase: true, keep: 'last' }).rows.map(r => r[0]), ['Bob', 'Ada New']);
});
test('CSV serialization round-trips and formula protection is explicit', () => {
  const table = W.parseCSV('name,note\nAda,"hello, world"\nBob,=1+1');
  assert.deepEqual(W.parseCSV(W.csvOutput(table)).rows, table.rows);
  assert.match(W.csvOutput(table, true), /'=1\+1/);
  assert.equal(JSON.parse(W.jsonOutput(W.parseCSV('__proto__,id\nsafe,001')))[0].__proto__, 'safe');
});
test('image fit retains aspect ratio and does not enlarge inputs', () => {
  assert.deepEqual(W.fitSize(1200, 800, 600, 400), { width: 600, height: 400 });
  assert.deepEqual(W.fitSize(400, 200, 600, 400), { width: 400, height: 200 });
  assert.throws(() => W.fitSize(0, 800, 600, 400), /positive/);
});

test('single-column CSV uses the default comma delimiter without rejecting valid input', () => {
 const table=W.parseCSV('id\n001\n002'); assert.deepEqual(table.headers,['id']); assert.equal(JSON.parse(W.jsonOutput(table))[0].id,'001');
});
