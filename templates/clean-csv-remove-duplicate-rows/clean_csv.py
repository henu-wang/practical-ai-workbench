"""Conservative pandas deduplication with an audit; never overwrite the input."""
import argparse
import csv
import json
from pathlib import Path
import pandas as pd


def clean(source, output, keys=None, keep='first', trim=False, ignore_case=False):
    source, output = Path(source), Path(output)
    targets = [output / n for n in ('cleaned.csv', 'duplicate-audit.csv', 'summary.json')]
    if source.resolve() in [p.resolve() for p in targets]:
        raise ValueError('The output would overwrite the source. Choose another folder.')
    with source.open(encoding='utf-8-sig', newline='') as handle:
        records = list(csv.reader(handle, strict=True))
    if not records:
        raise ValueError('The CSV is empty.')
    headers = records[0]
    if not headers or any(not h.strip() for h in headers) or len(set(headers)) != len(headers):
        raise ValueError('Use unique, non-empty column headers. Headers are not renamed.')
    reserved = {'audit_source_record', 'audit_retained_source_record', 'audit_reason'}
    if reserved.intersection(headers):
        raise ValueError('Rename headers that exactly match reserved audit field names.')
    for index, row in enumerate(records[1:], 1):
        if len(row) != len(headers):
            raise ValueError(f'Data record {index}: expected {len(headers)} fields, got {len(row)}.')
    frame = pd.read_csv(source, encoding='utf-8-sig', dtype=str, keep_default_na=False,
                        na_filter=False, on_bad_lines='error')
    if list(frame.columns) != headers or len(frame) != len(records) - 1:
        raise ValueError('CSV parsers disagree on the headers or record count.')
    columns = keys or headers
    if not columns or any(key not in headers for key in columns):
        raise ValueError('Every chosen key must exactly match a header.')
    compared = frame[columns].copy()
    if trim:
        compared = compared.apply(lambda col: col.str.strip())
    if ignore_case:
        compared = compared.apply(lambda col: col.str.casefold())
    # A missing identity key must not collapse unrelated records into one group.
    missing = frame[columns].apply(lambda col: col.str.strip().eq('')).any(axis=1) if keys else pd.Series(False, index=frame.index)
    removed = compared.duplicated(keep=keep) & ~missing
    kept = frame.loc[~removed].copy()
    representative = {}
    order = list(frame.index)
    if keep == 'first':
        order.reverse()
    for index in order:
        representative[tuple(compared.loc[index])] = int(index) + 1
    audit = frame.loc[removed].copy()
    audit.insert(0, 'audit_source_record', [int(i) + 1 for i in audit.index])
    audit.insert(1, 'audit_retained_source_record',
                 [representative[tuple(compared.loc[i])] for i in audit.index])
    audit.insert(2, 'audit_reason', 'duplicate_matching_rule')
    output.mkdir(parents=True, exist_ok=True)
    kept.to_csv(targets[0], index=False, encoding='utf-8', lineterminator='\n')
    audit.to_csv(targets[1], index=False, encoding='utf-8', lineterminator='\n')
    summary = {'input_records': len(frame), 'output_records': len(kept),
               'removed_records': int(removed.sum()), 'missing_key_records_retained': int(missing.sum()),
               'key_columns': columns, 'keep': keep, 'trim_comparison_only': trim,
               'casefold_comparison_only': ignore_case, 'pandas_version': pd.__version__}
    targets[2].write_text(json.dumps(summary, indent=2) + '\n', encoding='utf-8')
    return summary


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('source')
    parser.add_argument('--output', default='cleaned-output')
    parser.add_argument('--key', action='append', help='Exact header; repeat for a combined key.')
    parser.add_argument('--keep', choices=['first', 'last'], default='first')
    parser.add_argument('--trim-key', action='store_true')
    parser.add_argument('--ignore-key-case', action='store_true')
    args = parser.parse_args()
    try:
        result = clean(args.source, args.output, args.key, args.keep, args.trim_key, args.ignore_key_case)
    except (ValueError, UnicodeError, csv.Error, OSError, pd.errors.ParserError) as error:
        parser.exit(2, f'Could not clean CSV: {error}\n')
    print(json.dumps(result, indent=2))
