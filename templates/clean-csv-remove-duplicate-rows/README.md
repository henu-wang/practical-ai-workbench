# Original CSV cleaning sample

All names, IDs, and addresses are fictional. The `.test` addresses do not
identify real customers. This is original code and data, not copied pandas/PapaParse source.

Requirements: Python with pandas. The checked execution used pandas 2.2.3.

```bash
python -m pip install pandas==2.2.3
python clean_csv.py messy.csv --key email --ignore-key-case --keep last --output sample-output
```

Six data records become four. Records 1 and 2 are removed in favor of record 4
under this explicit email/casefold/keep-last rule. Blank-key records 5 and 6
are retained separately. The multiline note and leading-zero IDs remain strings.

The output folder contains cleaned.csv, duplicate-audit.csv and summary.json.
Reusing that folder replaces earlier outputs, but the script rejects a target
that would overwrite the source file. Keep source backups and compare results
before an import. Whole-row comparison is the default when --key is omitted.

This handles UTF-8 comma-separated CSV with unique nonempty headers and uniform
record width. It does not fuzzy-match, fix encoding, merge conflicting values,
remove spreadsheet formulas, or automatically decide which identity key is correct.
# JavaScript destination check

For a Node destination, obtain Papa Parse through its TokRepo asset and follow the official package setup. With the package available, run:

```bash
node validate_handoff.cjs sample-output/cleaned.csv
```

The optional third argument accepts the path to an existing Papa Parse CommonJS module. The check reads local CSV text and confirms headers, records, leading zeros, multiline text, and blank keys. It does not install software, upload files, or save records into your application. Execution evidence is in `verification.json`.
