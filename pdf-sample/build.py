"""Build just QCQI 2.1 with MkDocs Exporter in a temporary staging directory."""

from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

import yaml

from verify import verify


SAMPLE = Path(__file__).resolve().parent
ROOT = SAMPLE.parent


def main():
    with tempfile.TemporaryDirectory(prefix="cs-notes-pdf-") as temporary:
        stage = Path(temporary)
        docs = stage / "docs"
        (docs / "qcqi").mkdir(parents=True)
        shutil.copy2(ROOT / "docs/qcqi/2.1.md", docs / "qcqi/2.1.md")
        shutil.copytree(ROOT / "docs/assets", docs / "assets")

        config = yaml.safe_load((ROOT / "mkdocs.yml").read_text())
        config["docs_dir"] = str(docs)
        config["site_dir"] = str(stage / "site")
        config["nav"] = [{"Linear Algebra": "qcqi/2.1.md"}]
        # Use installed fonts, avoiding a separate Google Fonts request.
        config["theme"]["font"] = False
        config["theme"]["palette"] = {"scheme": "default"}
        # SVG keeps each formula atomic when Paged.js fragments long boxes.
        config["extra_javascript"] = [
            "assets/javascripts/pdf-mathjax.js",
            "https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js",
        ]
        shutil.copy2(SAMPLE / "mathjax.js", docs / "assets/javascripts/pdf-mathjax.js")
        config["plugins"] = [{"exporter": {"formats": {"pdf": {
            "enabled": True,
            "concurrency": 1,
            "stylesheets": [str(SAMPLE / "print.scss")],
            "scripts": [str(SAMPLE / "prepare.js")],
            "browser": {"timeout": 120000, "debug": True},
        }}}}]
        configuration = stage / "mkdocs.yml"
        configuration.write_text(yaml.safe_dump(config, sort_keys=False))
        subprocess.run(
            [sys.executable, "-m", "mkdocs", "build", "--strict", "--config-file", str(configuration)],
            check=True,
        )
        generated = list((stage / "site").rglob("*.pdf"))
        if len(generated) != 1:
            raise RuntimeError(f"Expected one PDF, found {generated}")
        verify(generated[0])
        output = SAMPLE / "qcqi-2.1.pdf"
        shutil.copy2(generated[0], output)
        print(f"Sample PDF: {output}")


if __name__ == "__main__":
    main()
