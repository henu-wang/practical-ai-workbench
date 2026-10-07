"""Original recipe glue: detected PDF tables -> CSV + text-only Excel.

Uses documented Docling and pandas interfaces. No model-runtime verification
is implied by this file. Review each extracted table against its source PDF.
"""

import argparse
from pathlib import Path


def spreadsheet_safe_text(value):
    """Prefix formula-like text; this deliberately changes those cell values."""
    text = str(value)
    return "'" + text if text.lstrip().startswith(("=", "+", "-", "@")) else text


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("pdf", type=Path)
    parser.add_argument("--output", type=Path, default=Path("extracted"))
    parser.add_argument("--overwrite", action="store_true")
    args = parser.parse_args()
    if not args.pdf.is_file() or args.pdf.suffix.lower() != ".pdf":
        parser.error("Input must be an existing PDF file.")

    from docling.document_converter import DocumentConverter

    result = DocumentConverter().convert(args.pdf)
    tables = result.document.tables
    if not tables:
        raise SystemExit("No tables detected. Inspect the PDF and pipeline settings.")

    targets = []
    for number in range(1, len(tables) + 1):
        base = args.output / f"{args.pdf.stem}-table-{number}"
        targets.append((Path(str(base) + ".csv"), Path(str(base) + ".xlsx")))
    if not args.overwrite:
        existing = [str(path) for pair in targets for path in pair if path.exists()]
        if existing:
            raise SystemExit("Output exists; choose a new folder or --overwrite: " + ", ".join(existing))

    args.output.mkdir(parents=True, exist_ok=True)
    for table, (csv_path, excel_path) in zip(tables, targets):
        frame = table.export_to_dataframe(doc=result.document)
        frame.to_csv(csv_path, index=False)
        text_frame = frame.astype("string").fillna("")
        safe_frame = text_frame.map(spreadsheet_safe_text)
        safe_frame.columns = [spreadsheet_safe_text(name) for name in frame.columns]
        safe_frame.to_excel(excel_path, index=False, engine="openpyxl")
        print(f"{len(frame)} rows, {len(frame.columns)} columns -> {csv_path}, {excel_path}")
    print("Extraction complete. Verification against the PDF is still required.")


if __name__ == "__main__":
    main()
