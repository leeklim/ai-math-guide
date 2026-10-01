window.MathJax = {
  loader: {
    load: ["[tex]/boldsymbol", "[tex]/mathtools"]
  },
  tex: {
    packages: {"[+]": ["boldsymbol", "mathtools"]},
    inlineMath: [["\\(", "\\)"], ["$", "$"]],
    displayMath: [["\\[", "\\]"], ["$$", "$$"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex|md-ellipsis"
  }
};

document$.subscribe(() => {
  MathJax.startup.promise.then(() => {
    MathJax.startup.output.clearCache();
    MathJax.typesetClear();
    MathJax.texReset();
    return MathJax.typesetPromise();
  });
});
