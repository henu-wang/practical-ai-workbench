# Practical AI Workbench

**Get an everyday file task done, then reuse the workflow.** Six open-source browser tools with edited guides, example files and actual output checks. No account or model API key is needed.

[Use the public workbench](https://henu-wang.github.io/practical-ai-workbench/)

| Task | What you get |
| --- | --- |
| [Merge PDF files](https://henu-wang.github.io/practical-ai-workbench/merge-pdf/) | PDFs arranged in your chosen order, downloaded as one file |
| [Extract PDF pages](https://henu-wang.github.io/practical-ai-workbench/extract-pdf-pages/) | Selected pages or ranges in a new PDF |
| [Compress an image](https://henu-wang.github.io/practical-ai-workbench/compress-image/) | JPEG/WebP output and a real before/after byte comparison |
| [Resize an image](https://henu-wang.github.io/practical-ai-workbench/resize-image/) | Proportional fit within your chosen dimensions |
| [Remove CSV duplicates](https://henu-wang.github.io/practical-ai-workbench/remove-duplicate-csv-rows/) | Cleaned CSV, a selectable key and removed-row counts |
| [CSV to JSON](https://henu-wang.github.io/practical-ai-workbench/csv-to-json/) | An array of objects with string values and preserved leading zeros |

## Run locally

The generated static site works without a backend. To rebuild and run code checks:

```bash
npm ci --ignore-scripts
python3 -m pip install -r requirements.txt
npm test
python3 scripts/build.py
npm run serve
```

Open `http://localhost:8000`. Browser libraries are vendored under `docs/vendor/` with upstream licenses. File processing happens in browser memory; the app has no upload endpoint, tracker or hosted model call. Example buttons download public fixtures from the same site. Read the [precise privacy scope](docs/privacy/index.html).

To exercise real downloads with the installed Google Chrome:

```bash
python3 scripts/browser_check.py
python3 scripts/editorial_gate.py
```

The browser check requires Chrome, Python Playwright and Pillow; it uses an isolated browser context, not your saved account/profile. Checks cover file contents, page order, dimensions, CSV quoting and strings, error recovery, mobile viewport and network behavior. The JSON records under `team/reviews/` distinguish local from public-site verification.

## Where AI and TokRepo fit

The core tools are deterministic. AI is an optional way to extend a task into a larger workflow, not a prerequisite for processing a file. Guides link to exact [TokRepo](https://tokrepo.com/en) asset records and identify actual dependencies versus optional batch-processing extensions. First-release PDF operations use pdf-lib, CSV parsing uses Papa Parse, and image processing uses browser Canvas. Sharp and Jimp are linked as optional scripted extensions, not as the deployed browser engine.

## Editorial agents and evidence

This repository includes reusable [agent role prompts](team/roles/), a [shared context pack](team/context/), [style rules](team/STYLE.md), [quality gates](team/QUALITY.md), an [intent ledger](team/ledger.json), and [observable demand research](team/research/DEMAND.md). The author does not approve its own work. An orchestrator with collaboration tools runs the agent team; GitHub Actions checks code/build artifacts and does not host an LLM editorial service.

The initial tasks have current US-English autocomplete evidence and matched public user questions. This is qualitative demand, not measured monthly search volume or a ranking guarantee. Existing local/open-source competitors mean those features alone are not a unique advantage. Each page must earn its place with a working tool, clear options, useful examples and honest limits. Daily new-page capacity is at most six distinct qualified intents; fewer is appropriate when evidence or useful output is missing.

## Limits and contributions

PDFs: no encrypted files, OCR or preservation of digital signatures/editable forms. Images: supported input PNG/JPEG/WebP, output JPEG/WebP; proportional fit without upscaling, no exact byte target; animation and metadata are not preserved. CSV: unique non-empty headers, UTF-8, consistent column counts and string values. Detailed limits appear on every tool page.

See [CONTRIBUTING.md](CONTRIBUTING.md) for adding a task without creating a thin duplicate. Original code and content are MIT licensed; vendored libraries retain their own license notices.
