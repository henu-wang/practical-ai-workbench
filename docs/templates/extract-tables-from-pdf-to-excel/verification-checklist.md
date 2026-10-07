# PDF table verification worksheet

Original template. Extraction output is a candidate dataset until checked.

- Source PDF and page:
- Detected table/output filename:
- Extraction environment/version:
- Reviewer/date:
- Status: UNCHECKED / CORRECTED / CHECKED

## Compare with the visible source

- [ ] Column names and their left-to-right order match.
- [ ] Number of data rows matches; repeated headers are not counted as data.
- [ ] First, last, and a middle row match cell by cell.
- [ ] Leading zeros in identifiers remain intact.
- [ ] Blank cells, multi-line cells, merged headings, and continued tables were checked.
- [ ] OCR ambiguities were resolved from the source rather than guessed.
- [ ] Formula-protection changes in the Excel copy are understood.
- [ ] Numeric/date conversion is deferred until an explicit schema is chosen.

## Corrections and schema

| Source page/cell | Extracted value | Checked value | Reason/evidence |
| --- | --- | --- | --- |
| | | | |

| Column | Intended type | Missing-value policy | Validation rule |
| --- | --- | --- | --- |
| Item code | Text | Flag for review | Preserve leading zeros |
| Quantity | Integer after review | Flag for review | Match visible source |
| Location | Text | Keep explicit blank | Match visible source |

## Fictional sample acceptance

Exactly 3 columns and 3 data rows. Item codes: 0012, 0047, 0105.
Quantities: 8, 3, 11. Locations: North shelf, South shelf, Overflow.
These are reference expectations, not a recorded extraction result.
