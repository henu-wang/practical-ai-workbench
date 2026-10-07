// Original sample check. Requires Papa Parse; passes cleaned CSV text into its API.
const fs = require('node:fs');
const assert = require('node:assert/strict');
const Papa = require(process.argv[3] || 'papaparse');
const input = process.argv[2] || 'sample-output/cleaned.csv';
const result = Papa.parse(fs.readFileSync(input, 'utf8'), {
  header: true, delimiter: ',', dynamicTyping: false, skipEmptyLines: true
});
assert.deepEqual(result.errors, []);
assert.deepEqual(result.meta.fields, ['customer_id', 'name', 'email', 'note']);
assert.equal(result.data.length, 4);
assert.deepEqual(result.data.map(row => row.customer_id), ['0013', '0012', '0014', '0015']);
assert.equal(result.data[0].note, 'line one\nline two');
assert.equal(result.data[1].email, 'ADA@example.test');
assert.equal(result.data[1].note, 'updated phone');
assert.equal(result.data.filter(row => row.email === '').length, 2);
console.log('PASS: cleaned.csv handoff, 4 records, identifiers and multiline text retained');
