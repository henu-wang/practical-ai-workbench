## Quick answer

To remove duplicate CSV rows in pandas, decide whether a duplicate means the whole record or an identity key, then choose which occurrence to keep. Save a new file and a removal audit. Do not infer that two blank email addresses identify the same person, or turn leading-zero IDs into numbers while loading the file.

Get [the pandas data-cleaning asset on TokRepo](https://tokrepo.com/en/workflows/pandas-powerful-data-analysis-manipulation-python-1005b785?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=clean-csv-remove-duplicate-rows) for deduplication. The complementary [Papa Parse asset](https://tokrepo.com/en/workflows/papa-parse-fast-browser-csv-parser-javascript-ed9fd7fc?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=clean-csv-remove-duplicate-rows) supports the handoff into a JavaScript application: parse the resulting `cleaned.csv` and confirm the records survived import. Papa Parse does not deduplicate the file. If your destination is a spreadsheet, the Python output and manual checks are sufficient.

## Download the conservative recipe

- [Original Python script](../../templates/clean-csv-remove-duplicate-rows/clean_csv.py).
- [Messy sample CSV](../../templates/clean-csv-remove-duplicate-rows/messy.csv), with fictional contacts.
- [Cleaned sample](../../templates/clean-csv-remove-duplicate-rows/sample-output/cleaned.csv) and [removal audit](../../templates/clean-csv-remove-duplicate-rows/sample-output/duplicate-audit.csv).
- [Sample summary](../../templates/clean-csv-remove-duplicate-rows/sample-output/summary.json) and [run instructions](../../templates/clean-csv-remove-duplicate-rows/README.md).
- [JavaScript handoff check](../../templates/clean-csv-remove-duplicate-rows/validate_handoff.cjs) and [execution evidence](../../templates/clean-csv-remove-duplicate-rows/verification.json).

This is a local script and worked example, not an online upload service. The sample execution uses pandas 2.2.3; the verification record describes what was checked.

## 1. Choose the matching rule

The sample has six data records. Two are identical copies of Ada's contact. Another Ada record changes the email's case and note. Two other contacts have blank email fields.

| Rule | What it means |
| --- | --- |
| All columns, exact | Remove repeated complete records; changed notes remain separate. |
| Email, case-sensitive | Different email capitalization remains distinct. |
| Email, case-insensitive | Group email variants, but do not silently rewrite stored values. |
| Keep first / last | Select by source order; neither means “most accurate.” |

Pandas supports `drop_duplicates(subset=..., keep=...)`. Its `keep=False` removes every member of a repeated group, unlike keeping the first or last. The downloadable script deliberately offers only first/last and preserves blank identity-key rows. See the [official API](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.drop_duplicates.html).

## 2. Run on a small copy first

Put the script and sample in the same folder. With Python and pandas available, run:

```bash
python clean_csv.py messy.csv --key email --ignore-key-case \
  --keep last --output sample-output
```

The script parses CSV records rather than splitting raw lines: a quoted comma or a newline inside a note remains part of that field. It checks header names and record width before using pandas. UTF-8 input is required; it does not guess a broken encoding or accept an Excel workbook as CSV.

Loading keeps cell values as strings and disables automatic missing-value interpretation. That protects identifiers such as `0012`; it also means a text value such as `NA` is not silently erased. The [pandas import reference](https://pandas.pydata.org/docs/reference/api/pandas.read_csv.html) explains these controls.

## 3. Check the cleaned file and audit together

For the command above, six records become four: Bob, the last Ada record, Cy, and Dee, in source order. Ada's first two records appear in the audit with their original record numbers and the retained record number, 4. Blank-key records remain separate rather than collapsing together.

Confirm that `0012` is still written with its zeros, Bob's note still has its line break, and the retained Ada note says `updated phone`. Count CSV records with a parser, not physical lines. Check the removed rows before importing the result into another system.

Using `--trim-key` or `--ignore-key-case` changes comparison only; retained values are not normalized. A surrounding-space difference may be meaningful, so these options are off by default. The script will replace prior outputs in the selected folder but refuses to overwrite its source.

## 4. Check the JavaScript handoff

For an application that uses Papa Parse, pass the cleaned file's text to the parser with explicit settings:

```javascript
const result = Papa.parse(cleanedCsvText, {
  header: true, delimiter: ",", dynamicTyping: false, skipEmptyLines: true
});
if (result.errors.length) throw new Error("Check CSV parsing errors");
```

The [official parser documentation](https://www.papaparse.com/docs) explains these options. For this sample, confirm four records, the same four column names, the string ID `0012`, and Bob's complete multiline note. The downloadable Node check performs those assertions on pandas' output using Papa Parse 5.5.3. It is a local file handoff test; no destination application's full import workflow was tested. Stop on errors or a changed count before saving records in the destination.

## 5. Know what cleaning did not solve

Deduplication does not merge two partial profiles, decide the correct address, fuzzy-match names, or sanitize spreadsheet formulas. A kept record can still be wrong. Use a separate, documented rule when importing untrusted cells into a spreadsheet.

For recurring cleanup, reuse [pandas through TokRepo](https://tokrepo.com/en/workflows/pandas-powerful-data-analysis-manipulation-python-1005b785?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=clean-csv-remove-duplicate-rows), then use [Papa Parse](https://tokrepo.com/en/workflows/papa-parse-fast-browser-csv-parser-javascript-ed9fd7fc?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=clean-csv-remove-duplicate-rows) where the cleaned output enters a JavaScript workflow. Keep the removal audit alongside the imported data.
