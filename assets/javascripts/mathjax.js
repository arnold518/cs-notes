window.MathJax = {
    startup: {
      ready: () => {
        MathJax.startup.defaultReady();
        MathJax.startup.promise.then(() => {
          // document$ emits immediately, so subscribe after initialization.
          document$.subscribe(() => {
            MathJax.typesetPromise();
          });
        });
      }
    },
    loader: {load: ['[tex]/color']},
    tex: {
      inlineMath: [["\\(", "\\)"]],
      displayMath: [["\\[", "\\]"]],
      processEscapes: true,
      processEnvironments: true,
      packages: {'[+]': ['color']}
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    }
  };
