# QCQI 2.1 PDF sample

Open [qcqi-2.1.pdf](qcqi-2.1.pdf).

This sample exports the complete `docs/qcqi/2.1.md` chapter using MkDocs
Exporter 6.2.0 and the site's Material theme. It uses A4 paper, 10.5-point
text, colored definition/theorem/proof boxes, and page numbers. Short boxes
stay together; boxes longer than a page start on a fresh page and may split.

MathJax renders equations as vectors before pagination. Body text is
selectable; equations remain sharp when zooming but are not plain text.
The chapter's wording is preserved, including existing source formatting.

## Rebuild

From the repository root:

```bash
python3 -m venv /tmp/cs-notes-pdf-venv
/tmp/cs-notes-pdf-venv/bin/python -m pip install -r pdf-sample/requirements.txt
PLAYWRIGHT_BROWSERS_PATH=/tmp/cs-notes-pdf-browsers /tmp/cs-notes-pdf-venv/bin/python -m playwright install chromium --only-shell
PLAYWRIGHT_BROWSERS_PATH=/tmp/cs-notes-pdf-browsers /tmp/cs-notes-pdf-venv/bin/python pdf-sample/build.py
```

The browser needs its normal operating-system dependencies. The sample uses
the installed Noto Sans font (with DejaVu Sans as a fallback) and downloads
MathJax 3.2.2 from jsDelivr during the build.

The script stages just this chapter and its styles in a temporary directory,
runs MkDocs Exporter, validates the result, and writes `qcqi-2.1.pdf` here.
The production MkDocs configuration and deployment are unchanged.

## Validation

The build waits for MathJax, checks formula errors and page bounds, and runs
MkDocs in strict mode. Before replacing the sample PDF, `verify.py` checks
numbered blocks and prose fragments longer than 35 characters against the
Markdown source. This catches paragraph loss observed with the exporter's
pagination when short boxes were allowed to split freely. Formula appearance
and page layout also require visual inspection.

```bash
/tmp/cs-notes-pdf-venv/bin/python pdf-sample/verify.py
```
