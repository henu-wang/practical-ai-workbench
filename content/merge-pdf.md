## How to merge PDF files in the right order

Add your PDFs to the tool above, arrange the file list, and generate one PDF. Pages within each file keep their original order. The output follows the order shown in the list, so put the cover or introduction first before you download.

You can combine up to 10 PDF files, with a total input size of 40 MiB. This tool combines pages; it does not compress PDFs, recognize text in scans, or turn a scanned page into editable text.

## Try a three-page example

Download [source-a.pdf](../samples/source-a.pdf), which has two pages, and [source-b.pdf](../samples/source-b.pdf), which has one. These are fictional sample documents.

1. Add both files to the tool.
2. Put `source-a.pdf` above `source-b.pdf`. Use the up and down arrows if needed.
3. Generate and download the merged PDF.
4. Open it in your PDF reader. The expected result is three pages: the two pages from A, followed by the page from B.

To place B first, move it above A and generate a new file. Changing the file order does not rearrange individual pages inside A. For a custom sequence of individual pages, merge the files first and then use [Extract PDF pages](../extract-pdf-pages/).

## Check before sending the result

Count the output pages and compare that count with the sum of the source documents. Inspect the first page, each boundary between files, and the last page. A correct page count alone cannot tell you whether the attachments are in the right order.

Keep the originals until you have checked the download. If you accidentally include the same file twice, its pages can appear twice; choose the intended files again, leaving out the unwanted copy rather than expecting content deduplication.

## Files this tool cannot safely combine

Encrypted and damaged PDFs are rejected. If your reader can open a damaged file but the tool cannot, obtain a fresh copy or re-export it from the application that created it.

Do not use this output as a replacement for a digitally signed original. Signatures and editable forms are not preserved as functional features. For a form submission, check whether the recipient needs the original signed or fillable document instead of a combined reading copy.

For repeated document jobs, [pdf-lib on TokRepo](https://tokrepo.com/en/workflows/asset-51d0242d) is the asset behind this tool's PDF processing and a starting point for a scripted workflow. Validate page counts and order in that workflow too; automation does not remove those checks.
