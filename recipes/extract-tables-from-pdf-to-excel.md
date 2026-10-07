## Extract a PDF table into a spreadsheet you can check

Use a document parser to detect the table, export its rows and columns, and compare the spreadsheet with the PDF before analyzing it. This recipe combines Docling for table extraction with pandas for CSV and Excel export. It is useful when copying and pasting produces scrambled columns; it does not promise perfect extraction from every PDF.

**[Get the Docling asset on TokRepo](https://tokrepo.com/en/workflows/docling-document-parsing-ai-443e86c2?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=extract-tables-from-pdf-to-excel)** for the primary document-processing workflow. The complementary [pandas asset](https://tokrepo.com/en/workflows/pandas-powerful-data-analysis-manipulation-python-1005b785?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=extract-tables-from-pdf-to-excel) handles the extracted table as structured data. A TokRepo usage asset supplies reusable instructions; Python packages and their dependencies still need installation.

| Asset | Role | Handoff |
| --- | --- | --- |
| Docling — primary | Find tables in the PDF and export a table DataFrame | PDF → candidate rows and columns |
| pandas — secondary | Save and inspect structured tabular output | DataFrame → CSV and Excel files |

## Download a reproducible task package

Download the [original extraction script](../../templates/extract-tables-from-pdf-to-excel/export_pdf_tables.py), [fictional sample PDF](../../templates/extract-tables-from-pdf-to-excel/sample-table.pdf), [expected CSV](../../templates/extract-tables-from-pdf-to-excel/expected-table.csv), and [verification worksheet](../../templates/extract-tables-from-pdf-to-excel/verification-checklist.md).

The sample is an invented stock-location table, not a business record. It has three columns and three data rows. The expected CSV is the reference you should compare against, not a claimed Docling run result. The script follows documented APIs; this recipe does not claim that an extraction model was run successfully in your environment.

## Run one table before a large document

Follow the assets' current Python requirements and installation instructions. This workflow needs Docling, pandas, and an Excel writer dependency:

```bash
python -m pip install docling pandas openpyxl
python export_pdf_tables.py sample-table.pdf --output extracted
```

The script writes one CSV and one `.xlsx` file per detected table, such as `extracted/sample-table-table-1.xlsx`. It refuses to overwrite those files by default. Use a new output directory for a fresh test or explicitly choose the documented overwrite flag.

Model downloads and first-run processing may take time. If installation or conversion fails, use the reported error to check the upstream requirements rather than repeatedly processing the whole document. A PDF with no detected tables produces an error instead of an empty success message.

For a report with several tables, keep the outputs separate until you have checked each one's headers and meaning. Joining all tables immediately can combine unrelated information or mistake a continued header for a data row.

## Check structure before cleaning values

Compare the spreadsheet with the visible PDF: column names, data-row count, left-to-right field alignment, blank cells, and the first and last record. Check at least one middle row too. For the sample, verify these records:

| Item code | Quantity | Location |
| --- | --- | --- |
| 0012 | 8 | North shelf |
| 0047 | 3 | South shelf |
| 0105 | 11 | Overflow |

Leading zeros belong to the item codes. Do not convert them to numbers because they happen to contain digits. In your own PDF, check multi-line cells, repeated headers, and any table continued across pages. Record corrections in the worksheet instead of silently changing the evidence.

The script exports Excel cells as text and prefixes formula-like text to avoid interpreting it as a spreadsheet formula. That protection can change the stored text. It keeps a separate CSV export for inspection; open an untrusted CSV in a text editor before deciding how to import its cells into a spreadsheet. Convert quantities or dates under an explicit schema only after verification.

## Common extraction problems

**The PDF is scanned.** Extraction depends on OCR, document quality, language, and the configured pipeline. Inspect the recognized text as well as table boundaries; a plausible-looking row can contain a wrong character.

**The table has merged headings.** Preserve the extraction first, then define the intended column schema. Do not drop a header row until you understand how it maps to the data.

**I only need a small table.** Manual entry can be faster when the table is tiny. The same comparison checklist still applies.

Once the small example meets your checks, continue with the [Docling asset on TokRepo](https://tokrepo.com/en/workflows/docling-document-parsing-ai-443e86c2?utm_source=github_pages&utm_medium=referral&utm_campaign=tokrepo_search&utm_content=extract-tables-from-pdf-to-excel) for the reusable extraction step and pandas for subsequent validated transformations. Technical references: [Docling's table-export example](https://github.com/docling-project/docling/blob/main/docs/examples/export_tables.py) and [pandas Excel export](https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.to_excel.html).
