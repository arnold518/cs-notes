// Isolated print configuration: one typesetting pass before pagination.
window.MathJax = {
  loader: {load: ["[tex]/color"]},
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true,
    packages: {"[+]": ["color"]}
  },
  options: {ignoreHtmlClass: ".*", processHtmlClass: "arithmatex"},
  svg: {fontCache: "local"}
};
