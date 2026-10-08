// Verify GA4/banner removal and the production-only Cloudflare loader.
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const vm = require("node:vm");

const root = path.dirname(process.argv[2] || path.join(__dirname, "../.build/bilingual/site/index.html"));
function htmlFiles(directory) {
  return fs.readdirSync(directory, { withFileTypes: true }).flatMap((entry) => {
    const file = path.join(directory, entry.name);
    return entry.isDirectory() ? htmlFiles(file) : entry.name.endsWith(".html") ? [file] : [];
  });
}

const pages = htmlFiles(root);
assert.ok(pages.length > 0, "built HTML is required");
for (const file of pages) {
  const html = fs.readFileSync(file, "utf8");
  assert.doesNotMatch(html, /<script\b[^>]*\bid\s*=\s*["']__analytics["']/i, file + " analytics initializer");
  assert.doesNotMatch(html, /googletagmanager\.com|google-analytics\.com|G-VXDGRXQFT3|data-mmi-analytics/i, file + " Google analytics tag");
  assert.doesNotMatch(html, /data-md-component\s*=\s*["']consent["']/i, file + " consent banner");
  assert.doesNotMatch(html, /\bid\s*=\s*["']__consent["']|\bhref\s*=\s*["']#__consent["']/i, file + " consent control");
  const privacyLink = html.match(/class="site-privacy-link"\s+href="([^"]+)"/);
  assert.ok(privacyLink, file + " privacy footer");
  const english = /<html lang="en"/.test(html);
  const publicRoot = "https://leeklim.github.io/ai-math-guide/" + (english ? "en/" : "");
  const relative = path.relative(root, file).split(path.sep).join("/");
  const suffix = english && relative.startsWith("en/") ? relative.slice(3) : relative;
  assert.equal(
    new URL(privacyLink[1], publicRoot + suffix).href,
    publicRoot + "privacy/",
    file + " locale privacy destination",
  );
  assert.match(html, /id="__cloudflare_web_analytics"/, file + " Cloudflare loader");
}

const html = fs.readFileSync(path.join(root, "index.html"), "utf8");
const loader = html.match(/<script id="__cloudflare_web_analytics">([\s\S]*?)<\/script>/)[1];
let runtimeChecks = 0;
for (const [address, expected] of [
  ["https://leeklim.github.io/ai-math-guide/", 1],
  ["https://leeklim.github.io/ai-math-guide", 1],
  ["https://leeklim.github.io/ai-math-guide/en/privacy/", 1],
  ["http://127.0.0.1:8005/ai-math-guide/", 0],
  ["http://localhost:8005/ai-math-guide/en/", 0],
  ["http://[::1]:8005/ai-math-guide/", 0],
  ["http://leeklim.github.io/ai-math-guide/", 0],
  ["https://example.com/ai-math-guide/", 0],
  ["https://leeklim.github.io/other-repo/", 0],
  ["https://leeklim.github.io/ai-math-guide-other/", 0],
]) {
  const nodes = [];
  const context = vm.createContext({
    URL,
    window: { location: new URL(address) },
    document: {
      getElementById: (id) => nodes.find((node) => node.id === id),
      createElement: () => ({ attributes: {}, setAttribute(name, value) { this.attributes[name] = value; } }),
      body: { appendChild: (node) => nodes.push(node) },
    },
  });
  vm.runInContext(loader, context);
  vm.runInContext(loader, context);
  assert.equal(nodes.length, expected, address + " production scope/deduplication");
  if (expected) {
    assert.equal(nodes[0].src, "https://static.cloudflareinsights.com/beacon.min.js");
    assert.equal(nodes[0].type, "module");
    assert.equal(nodes[0].async, true);
    assert.match(JSON.parse(nodes[0].attributes["data-cf-beacon"]).token, /^[0-9a-f]{32}$/);
  }
  runtimeChecks++;
}
console.log(`GA4/consent absence and privacy links passed: ${pages.length} HTML files; Cloudflare scope/deduplication: ${runtimeChecks} checks (no network requests)`);
