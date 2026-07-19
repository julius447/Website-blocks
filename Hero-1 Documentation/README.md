# Ampy Hero 1 — komplett handover (startsidans section 1)

> **Ägargodkänd slutversion 2026-07-19.** Live-referens (exakt det som ska klonas):
> **https://julius447.github.io/Hero-1/** · källa: repo `julius447/Hero-1`.
> **Det som är godkänt är exakt dessa bytes — konvertera format, ändra aldrig design.**
> Värden, färger, brytpunkter och radbrytning är kanon ("approved rendering is canon").

Evify-inspirerad foto-hero: inramad bakgrundsbild med vit "safety line", vit rubrik + paragraf
vänsterställt över en midnatt-slöja, en enda CTA, och en trust-rad i bildens fot. Helt statisk
(ingen JS), byggd på Ampys produktions-tokens och Outfit.

---

## Filer i paketet

| Fil | Vad | Var den hamnar |
|---|---|---|
| **`hero-1-bricks.json`** | **Enklaste vägen** — klistras in direkt i Bricks | Bricks builder → paste |
| **`hero-1.css`** | Produktions-CSS, scopad `.ampy-hero1`, px-enheter | FluentSnippets **CSS-snippet** (eller Bricks Code-elementets CSS-pane — JSON:en bär redan samma CSS) |
| **`hero-1.html`** | Ren markup (godkänd copy hårdkodad + ACF-karta i kommentaren) | referens / Bricks code-element |
| **`hero-1.php`** | `[ampy_hero1]`-shortcode med ACF-fält + fallbacks (`php -l` ren) | FluentSnippets **PHP-snippet** — alternativ till JSON-vägen |
| **`assets/hero-1-bg.webp`** | Bakgrundsbilden, 2000×1654 (skärpt + korn) | Mediabiblioteket → `/wp-content/uploads/hero-1-bg.webp` |
| **`preview/index.html`** | Lokal parity-render som inkluderar `hero-1.css` **by reference** | öppna i webbläsare för QA |

---

## Godkänd copy (LÅST)

- **H1:** `Elinstallationer i hemmet,<br> gjort ordentligt.`
  `<br>` = medveten 2-radersbrytning på desktop (≥993px). På mobil göms brytet via CSS → rubriken
  wrappar naturligt (3 rader @360–414px, medvetet — se "Får inte fixas").
- **Paragraf:** `Våra egna behöriga elektriker hjälper dig i hela Sverige, med allt från elfel och elcentraler till laddbox och batterilagring.`
- **CTA:** `Kostnadsfri rådgivning` → `/kontakt/` (kanonisk knapp från CTA-biblioteket `julius447/CTA-website` → `radgivning-cta/`)
- **Trust:** `5,0 på Google` (länkad till Google Maps-listningen) · 5 stjärnor · `|` · `Över 3 000 installationer per år`

---

## Installation — JSON-vägen (rekommenderad)

1. **Bild:** ladda upp `assets/hero-1-bg.webp` till mediabiblioteket så URL:en blir
   `/wp-content/uploads/hero-1-bg.webp` (det är vad JSON/HTML pekar på; blir filnamnet ett annat,
   uppdatera `<img src>` i code-elementet).
2. **Klistra in:** kopiera **hela** `hero-1-bricks.json` → i Bricks på startsidan, Ctrl/Cmd-V.
   En sektion **"Hero 1 (Evify)"** med ett code-element landar.
3. **Signera koden:** code-elementet kommer osignerat (signaturer är sajt-specifika) → öppna det och
   klicka **"Sign code"** med ett konto som har code-execution-rättighet.
4. **Dynamiska fält (ACF):** `{acf_hero_text}` (paragraf) och `{acf_google_rating}` (5,0) är ACF-taggade
   i code-elementet — sätt fältvärdena till copyn ovan. **H1:an är hårdkodad** (låst, med `<br>`); vill
   du styra den via ACF, sätt fältet `hero_heading` till `Elinstallationer i hemmet,<br> gjort ordentligt.`
   och skriv ut med `<br>` tillåtet (PHP-vägen gör redan detta via `wp_kses`).
5. **Placering:** lägg sektionen **överst** på startsidan, direkt under headern. Mini-menyn (block 2)
   ligger kvar direkt under.

### Alternativ — FluentSnippets (CSS + PHP)
- Lägg `hero-1.css` som en **CSS-snippet** (Run everywhere / på startsidan).
- Lägg `hero-1.php` som en **PHP-snippet** → ger shortcoden `[ampy_hero1]` med ACF-fält + fallbacks
  till exakt den godkända copyn. Placera `[ampy_hero1]` i en Bricks-sektion överst på sidan.

---

## Konfig-knoppar (de ENDA värden som får röras)

- **`--ampy-header-h` / `--ampy-header-h-m`** (överst i `.ampy-hero1`): **måste matcha den riktiga
  headerns höjd** — 76px desktop / 66px ≤992px i header-prototypen. Fel värde = hero-höjden stämmer
  inte mot viewporten (`100svh − header`).
- **`AMPY_HERO1_IMG`** i `hero-1.php` — om bild-URL:en avviker.

---

## Får INTE "fixas" (medvetna beslut — ändra dem och du bryter den godkända designen)

- **Rubrikens `<br>`** — desktop 2 rader ("Elinstallationer i hemmet," / "gjort ordentligt."), mobil
  3 rader. **Att radantalet på mobil är 3 är avsiktligt och OK** (rubriken är för lång för 2 rader i
  läsbar storlek; radantal påverkar inte konvertering så länge CTA:n ligger ovan vecket — det gör den).
- **Trust-raden:** `<strong>5,0</strong> på Google` ligger i EN span med vanligt mellanslag — splittra
  den **inte** i flera flex-barn (flex-gapet skapar då ett fult hål; det var en bugg vi tog bort).
  Baslinjerna är pixel-uppmätta (G-ikon 16px, stjärnor 13,5px, separator 1×15px) — behåll exakt.
- **Typografin är pinnad till Outfit** (till skillnad från mini-menyns block som ärver) — den godkända
  renderingen är Outfit 700 i H1. Sajten self-hostar redan Outfit; ingen extra font-laddning behövs.
- **Tre responsiva lägen** — desktop (>992) · mellanband **561–992** (centrerad tempererad komposition)
  · mobil **≤560** (textblocket **vertikalt centrerat** med 7vh optisk bias). Verifierat på
  1440/1280/1024/853/768/650/540/414/390/375 — rör inte brytpunkterna.
- **Veil-gradienterna** har tre varianter (desktop / 993–1200 / ≤560) — läsbarhets-kalibrerade mot
  just den här bilden.
- **`fetchpriority="high"` + `loading="eager"`** på bilden (LCP) och `aria-hidden` på dekorativa SVG:ar.

---

## QA efter implementation (5 min)

1. Öppna `preview/index.html` lokalt bredvid sajten — de ska vara **identiska** (desktop + 390px).
2. Desktop 1440: H1 = **2 rader**, paragraf = **2 rader**. Mobil 375–414: H1 = **3 rader**, paragraf =
   **3 rader**, textblocket **vertikalt centrerat** i bilden.
3. Trust-raden: allt på **en baslinje** på desktop; tvåraders-stack nere till vänster på mobil.
4. CTA → `/kontakt/`; Google-raden → Maps-listningen (ny flik).
5. Lighthouse: bilden ska vara **LCP-elementet**, inga CLS från heron.

---

## Öppna punkter (ägaren — INTE Chris)

- ⚑ **Header-CTA vs hero-CTA:** headern säger "Gratis rådgivning" → `/offert/`, heron "Kostnadsfri
  rådgivning" → `/kontakt/`. Två namn/mål för samma handling — enhetliga om ni vill (valfritt).
- ⚑ Bekräfta att **5,0** är aktuellt Google-betyg vid go-live (ACF-fältet `google_rating` styr).
- ⚑ Äkta AI-4K av bilden är kredit-gated (Higgsfield) — nuvarande 2000px är uppskalad (Lanczos + korn)
  och godkänd; 4K-filen byts rakt av på samma URL/filnamn när krediter finns.

---

## Versionshistorik (kort)

- **r1–r5.1** — riktning B (Evify-replika) vald, copy låst, proof-rad finess-byggd, 3-lägers-responsivt,
  bild 1 (trähuset) låst + uppskalad. Ägargodkänd "PERFEKTION".
- **r6** — H1 → "Elinstallationer i hemmet, gjort ordentligt." (tydligare elfirma); Google-länk → riktig
  Maps-URL.
- **r7** — CTA = "Kostnadsfri rådgivning" → `/kontakt/` (kanonisk knapp från `julius447/CTA-website`).
