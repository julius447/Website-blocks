# Header — implementation notes for the Bricks/WordPress port

The prototype (`index.html`) is verified correct **as a standalone page**. The items below are
things that MUST be handled when converting it into the live Bricks/WP theme — they are *conversion*
concerns, deliberately left as-is in the prototype. Source: 5-agent code audit (iOS, responsive, JS,
a11y, portability), 2026-07-10.

## Blocking (do these or it breaks)

1. **Do NOT ship `html{font-size:62.5%}`.** The whole stylesheet is authored at 1rem = 10px. Setting
   62.5% globally shrinks every other plugin/theme element that uses `rem`. Convert every `rem` → `px`
   (×10) during the port — this matches our FluentSnippets delivery rule (rem→px). Leave existing literal
   `px` values (shadows `0 4px 14px…`, logo `130px/100px/84px/76px`, `border-radius:3px`, all `1px`
   borders) untouched.

2. **Self-host Outfit (GDPR).** The prototype loads Outfit from `fonts.googleapis.com`. In production:
   remove the 3 `<link>` tags, add `@font-face` for Outfit 300–800 as self-hosted woff2 with
   `font-display:swap`. The fallback `system-ui,-apple-system,sans-serif` is already in `--font`, so the
   header degrades gracefully if the font is slow.

3. **Mount the header at top level of `<body>`, outside any transformed Bricks container.** `.hdr`,
   `.mega`, `.drawer`, `.dim` are `position:fixed`. If ANY ancestor has `transform`, `filter`,
   `perspective`, `backdrop-filter`, or `will-change:transform` (Bricks sets these for animations/sticky),
   that ancestor becomes the containing block and the fixed header/drawer will scroll away. Keep the
   markup out of transformed wrappers.

4. **Keep body-state rules + `:root` GLOBAL — do not nest them under a Bricks wrapper.** These must match
   `body`/`:root` at the top level: `body.drawer-open{overflow:hidden}`, `body.menu-open .dim`,
   `body.drawer-open .dim`, `body.menu-open .hdr`, `body{padding-top:var(--header-h)}`, all `:root` custom
   properties, and the JS `document.body.classList` toggles. Only the component rules may be wrapper-scoped.
   The `body{padding-top}` that offsets the fixed bar must stay on `body` (or be handled by the theme).

## Should do

5. **Namespace the CSS custom props** when moving them to the shared `:root` (e.g. `--font`→`--aphdr-font`,
   `--line`→`--aphdr-line`, `--container`, `--ink`, `--t`, `--wrap`, `--r-*`). Generic names risk clashing
   with Bricks globals / other plugins.

6. **WP admin bar offset (logged-in users only).** The fixed header (`top:0; z-index:100`) renders under
   the admin bar (`z-index:99999`, 32/46px tall). Add:
   ```css
   body.admin-bar .hdr{top:32px}
   @media (max-width:782px){ body.admin-bar .hdr{top:46px} }
   ```
   and bump `body padding-top` accordingly. Front-end visitors are unaffected.

7. **Re-point assets.** (a) `assets/laddboxar.webp` and `assets/batteri.webp` are the two generated product
   composites — upload to the WP media library and re-point (they 404 at any WP path otherwise). (b) The
   `https://ampy.se/wp-content/uploads/…` logo/icons/segment images already resolve on the live domain but
   should be re-pointed to media-library/relative URLs so staging + domain moves don't 404. (c) The two
   `*-produktbild.png` (3.6 MB full-res) in `/assets` are **unused by the HTML** — they're just the
   hi-res masters for you; don't ship them to the front-end.

8. **`viewport-fit=cover`** is set in the prototype meta (needed so the drawer's `env(safe-area-inset-*)`
   padding and the header's safe-area guards actually resolve on notched iPhones). In WP the viewport meta
   is theme-owned — make sure the theme's meta includes `viewport-fit=cover`.

9. **`scrollbar-gutter:stable` on `html`** is a global choice (prevents layout shift when the mega opens).
   Keep it at the theme level or drop it — your call.

## Strip

10. Remove the `.demo` `<main>` (the "Prototyp v5…" hero + `.filler` blocks) and the `.demo` CSS block —
    that's prototype scaffolding only, cleanly separable, no header markup depends on it. The `<title>` is
    a prototype string too.

## Already hardened in the prototype (no action needed)
iOS body scroll-lock (position:fixed pattern), safe-area insets, `-webkit-backdrop-filter`,
`-webkit-tap-highlight-color`, `@media (hover:hover)` guard for iPad, `dvh`+`vh` fallbacks, `inert`
+`aria-hidden` fallback, reduced-motion accordion handling, focus return to the burger on close,
disclosure `aria-controls`, opaque focus ring, 300px+ no-overflow, per-item hover timers.
