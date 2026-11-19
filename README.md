# cs-notes

Computer science study notes built with MkDocs Material, covering paper reviews,
mathematical foundations of deep learning, reinforcement learning, and quantum
computation and information.

## Local development

Use Python 3.13 to match CI.

```bash
python3.13 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
mkdocs serve
```

## Repository layout

- `docs/paper-review/`: paper reviews, figures, and reference PDFs.
- `docs/mfdnn/format/`: formatted deep-learning course notes.
- `docs/rl/`: reinforcement-learning table of contents and authoring material.
- `docs/qcqi/`: quantum computation and information notes and references.
- `docs/assets/`: shared stylesheets and MathJax configuration.
- `mkdocs.yml`: site settings and published navigation.
- `formatter/`: legacy Markdown and LaTeX formatting tools.
- `pdf-sample/`: a separate PDF export example with its own requirements.

Reinforcement learning currently has only a table-of-contents page in navigation.
Planned chapters appear as plain text until their notes are exported.
Blueprints, mapping files, raw textbook Markdown, original MFDNN source pages,
and LaTeX source/intermediate files are excluded from the generated site.
Unfinished paper reviews and the empty QCQI superdense-coding page are retained
as local drafts and excluded from the generated site and search index.
Reference PDFs and the MFDNN compiled PDF remain available.

## Validation and publishing

```bash
mkdocs build --strict
```

GitHub Actions installs the pinned requirements, builds in strict mode, and
deploys to GitHub Pages when changes are pushed to `main` or `master`.
