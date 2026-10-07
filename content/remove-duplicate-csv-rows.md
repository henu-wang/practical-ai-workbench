## How to remove duplicate rows from a CSV

Choose a CSV file or paste CSV text into the tool. Leave Key column blank to remove exact repeated records, or choose one key column that should identify a duplicate. Decide whether to keep the first or last matching record, then generate and download the cleaned CSV.

Start with all columns when you want to remove copies of the same record without collapsing different people or transactions. Choose one key column only when it defines the identity you actually need, such as an email address in a fictional contact list.

## Try the four-row sample

Download [data.csv](../samples/data.csv). It has the headers `name,email,note` and four fictional data records, including one exact duplicate. The header is not a data record.

1. Open the sample in the tool.
2. Leave Key column blank for duplicate matching.
3. Leave trimming and case normalization off.
4. Keep the first match and generate the output.
5. Check that the result contains three data records and one header row.

Inspect the remaining records as well as the count. CSV fields can contain quoted commas or line breaks, so counting lines in a text editor is not always the same as counting records.

## Choose what “duplicate” means

Matching all columns keeps records whose notes or other fields differ. Matching only `email` can merge those records into one group. “Keep first” retains the first encountered record in a group; “keep last” retains the last. Neither option automatically combines fields or decides which record is more accurate.

Trim and case options change how matching works. By default, `Alex` and `alex`, or a value with an extra space, remain distinct. Enable normalization only if that matches your data rules. Check a few affected records before applying it to a full dataset.

Header whitespace is trimmed. Record fields remain unchanged by matching options; optional spreadsheet protection can change exported cell text.

## Check before importing the result

Compare the retained row for each important duplicate group with the source, especially when matching a single column. Confirm the headers, record count, and notes. Keep the original so an overly broad matching rule can be reversed.

If the CSV will be opened in a spreadsheet, consider the optional formula protection on export. It is off by default because protection can change exported cell text. Cells beginning with formula-like characters deserve review; this tool does not execute their contents. For exact data interchange, choose your export policy deliberately.

The CSV parsing asset is [PapaParse on TokRepo](https://tokrepo.com/en/workflows/papa-parse-fast-browser-csv-parser-javascript-ed9fd7fc). For a recurring import pipeline, combine proper CSV parsing with an explicit duplicate key and first/last policy rather than comparing raw text lines.
