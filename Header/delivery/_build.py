#!/usr/bin/env python3
"""
Deterministic FluentSnippets packager for the Ampy header.
FORMAT ONLY — never changes a pixel/weight/word. It:
  - extracts CSS / header+drawer+dim markup / JS from index.html
  - rem -> px at 1rem = 10px
  - scopes every rule under one wrapper `.ampy-hdr-root`
  - :root tokens -> onto the wrapper
  - namespaces body-state classes (drawer-open->aph-open, menu-open->aph-menu)
  - prefixes @keyframes names (+ their animation: refs) to avoid theme collision
  - strips the demo scaffolding, the Google-Fonts <link>s, and global html/*/body bleed
  - writes raw candidates to delivery/_raw/ for review (final files are hand-finished)
"""
import re, pathlib

SRC = pathlib.Path("/Users/juliuscallahan/Desktop/Ampy Header Redesign/index.html")
OUT = pathlib.Path("/Users/juliuscallahan/Desktop/Ampy Header Redesign/delivery/_raw")
OUT.mkdir(parents=True, exist_ok=True)
html = SRC.read_text()

# ---- 1. extract the three payloads -----------------------------------------
css = re.search(r"<style>(.*?)</style>", html, re.S).group(1)
js  = re.search(r"<script>(.*?)</script>", html, re.S).group(1)
body = re.search(r"<body>(.*?)</body>", html, re.S).group(1)
# markup = everything up to <main class="demo"> (dim + header + drawer)
markup = body.split('<!-- ============================ DEMO PAGE', 1)[0]
markup = markup.split('<main class="demo">', 1)[0].strip()

# ---- 2. CSS: drop the demo scaffolding block, then strip all comments -------
css = re.sub(r"/\* ---- demo scaffolding ---- \*/.*?$", "", css, flags=re.S)
css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)   # comments corrupt the scoper; re-added clean later

# ---- 3. rem -> px (1rem = 10px), preserve non-rem px/%/etc ------------------
def rem_to_px(m):
    val = float(m.group(1)) * 10
    s = ("%f" % val).rstrip("0").rstrip(".")
    return s + "px"
css = re.sub(r"(-?[0-9]*\.?[0-9]+)rem", rem_to_px, css)

# ---- 4. namespace body-state classes (CSS + JS) ----------------------------
for a, b in (("drawer-open", "aph-open"), ("menu-open", "aph-menu")):
    css = css.replace("body." + a, "body." + b)
    js  = js.replace("'" + a + "'", "'" + b + "'").replace('"' + a + '"', '"' + b + '"')
    js  = js.replace("classList.contains('" + b + "')", "classList.contains('" + b + "')")

# ---- 5. prefix @keyframes names (avoid collision) --------------------------
for name in re.findall(r"@keyframes\s+([A-Za-z0-9_-]+)", css):
    css = re.sub(r"@keyframes\s+" + re.escape(name), "@keyframes aph-" + name, css)
    css = re.sub(r"(animation[^;{}]*?\b)" + re.escape(name) + r"\b", r"\g<1>aph-" + name, css)

# ---- 6. scope every rule under .ampy-hdr-root ------------------------------
# split the stylesheet into top-level chunks (rules + at-rules), brace-aware.
def split_blocks(s):
    out, depth, buf = [], 0, ""
    i = 0
    while i < len(s):
        c = s[i]
        buf += c
        if c == "{": depth += 1
        elif c == "}":
            depth -= 1
            if depth == 0:
                out.append(buf); buf = ""
        i += 1
    if buf.strip(): out.append(buf)
    return out

def scope_selector(sel):
    sel = sel.strip()
    if not sel: return sel
    if sel.startswith("@"): return sel
    if sel.startswith(":root"):
        return sel.replace(":root", ".ampy-hdr-root", 1)
    if re.match(r"^html\b", sel):
        return "__DROP__"                              # global html{} — dropped (see README)
    if re.match(r"^\*(\s|,|$)", sel):                  # the global reset
        return ".ampy-hdr-root " + sel
    if re.match(r"^body\.", sel):                      # body-state rules keep body ancestor
        # body.aph-open .dim  ->  body.aph-open .ampy-hdr-root .dim  (unless it targets body itself)
        parts = sel.split(None, 1)
        if len(parts) == 1: return sel                 # body.aph-open { } alone
        return parts[0] + " .ampy-hdr-root " + parts[1]
    if re.match(r"^body\b", sel):                      # base body{} — handled by hand
        return "__BODY__ " + sel
    return ".ampy-hdr-root " + sel

def scope_rule(block):
    m = re.match(r"^(.*?)\{(.*)\}\s*$", block, re.S)
    if not m: return block
    selraw, inner = m.group(1), m.group(2)
    sels = [scope_selector(s) for s in selraw.split(",")]
    if any(s == "__DROP__" for s in sels): return ""   # drop whole html rule
    sels = [s for s in sels if s]
    return ", ".join(sels) + "{" + inner + "}"

scoped = []
for block in split_blocks(css):
    b = block.strip()
    if not b: continue
    if b.startswith("@keyframes") or b.startswith("@font-face"):
        scoped.append(b); continue
    if b.startswith("@media") or b.startswith("@supports"):
        mm = re.match(r"^(@[^{]+)\{(.*)\}\s*$", b, re.S)
        cond, innerbody = mm.group(1), mm.group(2)
        inner_scoped = "".join(scope_rule(x) for x in split_blocks(innerbody))
        scoped.append(cond + "{\n" + inner_scoped + "}\n"); continue
    scoped.append(scope_rule(b))
css_scoped = "\n".join(x for x in scoped if x.strip())

# ---- 7. strip the Google-Fonts links from markup (self-host instead) -------
# (markup here is dim+header+drawer only; the <link>s live in <head>, not markup)

(OUT / "styles.raw.css").write_text(css_scoped)
(OUT / "markup.raw.html").write_text(markup)
(OUT / "engine.raw.js").write_text(js)
print("wrote raw candidates to", OUT)
print("css lines:", css_scoped.count(chr(10)))
print("rem left (should be 0):", len(re.findall(r"[0-9.]+rem", css_scoped)))
print("__BODY__ base rules to hand-fix:", css_scoped.count("__BODY__"))
print("keyframes:", re.findall(r"@keyframes\s+([\w-]+)", css_scoped))
