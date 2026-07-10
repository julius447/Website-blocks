# Header

Ampy header / navigation redesign (prototype). Self-contained `index.html` +
generated product imagery in `assets/`.

- Real Ampy `ap*` tokens, real ampy.se assets, HemSol scroll model, EVFi mega-menu IA.
- Verified in-browser on desktop, iPad (1024) and mobile (375).
- Loads Outfit via Google Fonts for the prototype; production self-hosts it (GDPR).

## assets/  (product photos — hand these to the developer)
- `laddboxar.webp` (1400px, ~19 kB) + `laddboxar-produktbild.png` (2400px full-res)
  — Easee Charge Up front, Zaptec Go back-left, Charge Amps Luna back-right.
  Generated with Higgsfield **Nano Banana Pro** from the real product packshots.
- `batteri.webp` (1400px) + `solcellsbatterier-produktbild.png` (2400px full-res)
  — SAJ front + Homevolt behind. **INTERIM: 2 of 3** — the Enershare image was not
  available, so the final 3-unit shot (SAJ front · Homevolt right · Enershare left)
  still needs the Enershare source photo, then a re-generate.

## Locked / applied this round (owner feedback r3)
1. Menu background = site bg `#f5f9ff` (verified), grey separator line kept.
2. Tjänster: expert card removed → 4 balanced columns, one-line descriptions.
3. Produkter: icon container → generated product photo per tile.
5. Produkter: Guider & verktyg pulled in (killed the right-side whitespace).
6. Lösningar: 4 cards (Privatperson→/elektriker/ added), copy length-balanced.
7. CTA: solid teal `#00a991` (no gradient), pulse dot kept, hover = darker teal, no move.
8. Mobile: Evify pattern — "MENY" eyebrow, flat accordions, "Ring en expert" call CTA.

Next: convert to Bricks paste-JSON + 3-file FluentSnippets.
