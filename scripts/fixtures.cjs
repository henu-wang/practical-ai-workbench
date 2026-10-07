const fs = require('node:fs');
const path = require('node:path');
const { PDFDocument } = require('../docs/vendor/pdf-lib-1.17.1.min.js');
(async () => {
 const dir = path.join(__dirname, '../docs/samples');
 for (const [name, pages] of [['source-a.pdf', [300, 350]], ['source-b.pdf', [420]]]) {
  const doc = await PDFDocument.create();
  pages.forEach((width, index) => { const page = doc.addPage([width, 400]); page.drawText(`${name} / Page ${index + 1}`, { x: 25, y: 340, size: 14 }); });
  fs.writeFileSync(path.join(dir, name), await doc.save());
 }
 fs.writeFileSync(path.join(dir, 'data.csv'), 'name,email,note\nAda,ada@example.test,"hello, world"\nBob,bob@example.test,follow up\nAda,ada@example.test,"hello, world"\nCy,cy@example.test,"line one\nline two"\n');
})();
