"""Catch missing prose at page boundaries in this exporter sample."""

from pathlib import Path
import re
import sys
import unicodedata

from bs4 import BeautifulSoup
import markdown
from pypdf import PdfReader
import yaml


ROOT = Path(__file__).resolve().parent.parent


def normalize(text):
    text = unicodedata.normalize("NFKC", text)
    text = re.sub(r"-\s+", "-", text)
    return re.sub(r"\s+", " ", text).strip()


def verify(pdf):
    config = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
    extensions = []
    settings = {}
    for extension in config["markdown_extensions"]:
        if isinstance(extension, dict):
            extensions.extend(extension)
            settings.update(extension)
        else:
            extensions.append(extension)
    source = (ROOT / "docs/qcqi/2.1.md").read_text()
    html = markdown.markdown(source, extensions=extensions, extension_configs=settings)
    soup = BeautifulSoup(html, "html.parser")
    # PDF extraction orders mathematical glyphs differently from HTML text.
    # Check prose independently; formula layout also needs visual inspection.
    for formula in soup.select(".arithmatex"):
        formula.decompose()
    reader = PdfReader(pdf)
    pages = [normalize(page.extract_text()) for page in reader.pages]
    text = normalize(" ".join(pages))
    fragments = [normalize(str(node)) for node in soup.find_all(string=True)]
    fragments = [fragment for fragment in fragments if len(fragment) > 35]
    missing = [fragment for fragment in fragments if fragment not in text]
    if missing:
        raise RuntimeError("Missing prose fragments:\n" + "\n".join(missing))
    blocks = re.findall(r'^!!! \w+ "(?:Definition|Concept|Example|Theorem) 2\.1\.(\d+)', source, re.M)
    absent = [number for number in blocks if not re.search(
        r"(?:Definition|Concept|Example|Theorem)\s+2\.1\." + number + r"\b", text
    )]
    if absent:
        raise RuntimeError(f"Missing numbered blocks: {absent}")
    if any(len(page) < 100 for page in pages):
        raise RuntimeError("Unexpected blank or nearly empty page")
    print(f"Verified {len(reader.pages)} pages, {len(blocks)} numbered blocks, "
          f"and {len(fragments)} prose fragments.")


if __name__ == "__main__":
    verify(Path(sys.argv[1]) if len(sys.argv) > 1 else ROOT / "pdf-sample/qcqi-2.1.pdf")
