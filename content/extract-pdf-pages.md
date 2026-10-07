## How to extract selected PDF pages

Choose a PDF and enter the pages you want to keep. Use commas for separate pages and a hyphen for a consecutive range: `1,3-5` selects pages 1, 3, 4, and 5. Download a new PDF containing that selection.

Numbers refer to the page's position in the file, starting at 1. A page printed with a Roman numeral or a different footer number still uses its position in the PDF. Check the page thumbnails in your reader when those two numbering systems differ.

The tool preserves the order you specify and removes repeated page numbers. For example, `3,1,3` produces page 3 followed by page 1, with no second copy of page 3.

## Try a reordered two-page extract

Use [source-a.pdf](../samples/source-a.pdf) and [source-b.pdf](../samples/source-b.pdf) to create the three-page example in [Merge PDF](../merge-pdf/). Put A first and B second when merging. The sample documents are fictional.

1. Select the resulting three-page PDF in this tool.
2. Enter `3,1` as your selection.
3. Generate and download the extracted PDF.
4. Open the download. The expected output has two pages: the page from source B first, followed by the first page from source A.

This example checks both extraction and order. A file with two pages in the opposite sequence would not pass the check.

## Check the selection before sharing

Compare every output page with the source. Check headings or other visible identifiers, not just the total number of pages. A range like `3-5` means three pages, whereas `3,5` means two.

If a requested number is outside the source document's page count, correct the selection instead of assuming it was ignored. Use whole positive page numbers and a valid ascending range. A PDF reader's printed page labels are not accepted in place of those numbers.

## Limits and sensitive documents

The input must fit within the 40 MiB limit. Encrypted or damaged PDFs are rejected. This tool creates a page selection; it does not compress the source, run OCR, or search for pages by their text.

Do not treat extraction as redaction. Removing a page is different from safely removing confidential content within a page. This output also does not preserve functional digital signatures or editable forms; keep the original when either matters.

For repeated page-selection tasks, [pdf-lib on TokRepo](https://tokrepo.com/en/workflows/asset-51d0242d) provides the PDF processing asset used here. A scripted workflow should validate page bounds and assert the expected sequence, especially when source documents change length.
