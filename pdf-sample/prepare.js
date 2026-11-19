// MkDocs Exporter calls this hook before Paged.js splits the article into pages.
window.MkDocsExporter = {
  render: async () => {
    if (!window.MathJax?.startup?.promise) {
      throw new Error("MathJax did not load; refusing to paginate raw formulas.");
    }
    await MathJax.startup.promise;
    await document.fonts.ready;
    const errors = document.querySelectorAll("mjx-merror");
    if (errors.length) {
      throw new Error(`${errors.length} MathJax errors in the article.`);
    }
    // Hidden assistive MathML confuses Paged.js's overflow detection.
    // This only affects the temporary print document, not the website.
    document.querySelectorAll("mjx-assistive-mml").forEach(node => node.remove());
    for (const box of document.querySelectorAll(".admonition, details")) {
      if (box.getBoundingClientRect().height > 250 * 96 / 25.4) {
        box.classList.add("pdf-long");
      }
    }
    const formulas = Array.from(document.querySelectorAll("mjx-container"));
    formulas.forEach((formula, index) => formula.dataset.pdfFormula = String(index));
    console.info(`[mkdocs-exporter] Typeset ${formulas.length} formulas before pagination.`);
    new MutationObserver((_, observer) => {
      if (document.body.getAttribute("mkdocs-exporter") !== "true") return;
      observer.disconnect();
      const visible = new Set();
      for (const formula of document.querySelectorAll(".pagedjs_page [data-pdf-formula]")) {
        const rect = formula.getBoundingClientRect();
        const page = formula.closest(".pagedjs_page").getBoundingClientRect();
        if (rect.width > 0 && rect.height > 0 && rect.left >= page.left - 1 &&
            rect.right <= page.right + 1 && rect.top >= page.top - 1 && rect.bottom <= page.bottom + 1) {
          visible.add(formula.dataset.pdfFormula);
        } else {
          console.info(`[mkdocs-exporter] Formula ${formula.dataset.pdfFormula} on page ${formula.closest(".pagedjs_page").dataset.pageNumber}: ${JSON.stringify(rect)}; page: ${JSON.stringify(page)}`);
        }
      }
      if (visible.size !== formulas.length) {
        console.error(`[mkdocs-exporter] Formula layout check failed: ${visible.size}/${formulas.length} visible.`);
      } else {
        console.info(`[mkdocs-exporter] Verified ${visible.size} formulas within page bounds.`);
      }
    }).observe(document.body, {attributes: true});
  }
};
