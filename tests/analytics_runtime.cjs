// Run after a strict HTML build: node tests/analytics_runtime.cjs [HTML file]
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const html = fs.readFileSync(process.argv[2] || path.join(__dirname, "../.build/site/index.html"), "utf8");
const source = html.match(/<script id="__analytics">([\s\S]*?)<\/script>/)[1];
let checks = 0;

function check(url, consent, expected, scriptSource = source) {
  const scripts = [];
  const context = {
    URL,
    location: new URL(url),
    window: {},
    __md_get: () => consent,
    document: {
      referrer: "https://example.org/from?private=value#section",
      querySelector: () => scripts[0] || null,
      createElement: () => ({ dataset: {} }),
      getElementById: () => ({ insertAdjacentElement: (_, element) => scripts.push(element) })
    }
  };
  vm.runInNewContext(scriptSource + "\n__md_analytics(); __md_analytics();", context);
  assert.equal(scripts.length, expected ? 1 : 0, url + " script count");
  if (expected) {
    assert.equal(scripts[0].src, "https://www.googletagmanager.com/gtag/js?id=G-VXDGRXQFT3");
    assert.equal(scripts[0].async, true);
    const calls = context.window.dataLayer.map((args) => Array.from(args));
    assert.equal(calls.length, 2, "one js call and one config call, including repeated initialization");
    assert.equal(calls[1][0], "config");
    assert.equal(calls[1][1], "G-VXDGRXQFT3");
    assert.equal(calls[1][2].page_location, context.location.origin + context.location.pathname);
    assert.equal(calls[1][2].page_referrer, "https://example.org/from");
    assert.equal(calls[1][2].allow_google_signals, false);
    assert.equal(calls[1][2].allow_ad_personalization_signals, false);
  } else {
    assert.equal(context.window.dataLayer, undefined, "blocked contexts must not initialize analytics");
  }
  checks++;
}

const publicUrl = "https://leeklim.github.io/ai-math-guide/";
check(publicUrl, { analytics: true }, true);
check(publicUrl + "part-1-foundations/M00/M00-01-symbols/?q=private#section", { analytics: true }, true);
check(publicUrl, undefined, false);
check(publicUrl, {}, false);
check(publicUrl, { analytics: false }, false);
check(publicUrl, { analytics: "true" }, false);
check("http://127.0.0.1:8001/ai-math-guide/", { analytics: true }, false);
check("http://localhost:8001/ai-math-guide/", { analytics: true }, false);
check("http://leeklim.github.io/ai-math-guide/", { analytics: true }, false);
check("https://example.org/ai-math-guide/", { analytics: true }, false);
check("https://leeklim.github.io/another-repo/", { analytics: true }, false);
check("https://leeklim.github.io/ai-math-guide-copy/", { analytics: true }, false);
check(publicUrl, { analytics: true }, false, source.replace("G-VXDGRXQFT3", ""));
check(publicUrl, { analytics: true }, false, source.replace("G-VXDGRXQFT3", "UA-123456"));
console.log(`GA4 runtime checks passed: ${checks} (mocked DOM; no Google requests)`);
