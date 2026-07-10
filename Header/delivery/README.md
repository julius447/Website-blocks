# Ampy Header — implementation package (för Chris)

Den godkända, iOS-härdade headern, paketerad **på flera sätt så du kan välja**. Alla delar
**samma härdade kodbas** (`fluentsnippets/`) — det är garantin för 1-till-1 utan drift.
Prototyp/facit: `../index.html` · designbeslut: `../PORT-NOTES.md`.

> **Rekommendation:** Alternativ 1 (FluentSnippets + shortcode). Det är vad vårt leveranskontrakt
> föreskriver för en bespoke-komponent, det renderar exakt den godkända koden, och det är
> paritetsverifierat (se `preview/index.html`).

---

## Format 1 — FluentSnippets (rekommenderas)  →  `fluentsnippets/`

Tre snippets + self-hostade fonter. **Paritetsverifierad** mot facit (desktop + mobil).

| Fil | FluentSnippets-typ | Körs |
|---|---|---|
| `styles.css` | **CSS Snippet** | Frontend · `wp_head` |
| `backend.php` | **Functions – PHP Snippet** | **Frontend & Backend** (registrerar `[ampy_header]`) |
| `engine.js` | **JS Snippet** | Frontend · `wp_footer` |
| `fonts/` | ladda upp 6× woff2 → `wp-content/uploads/ampy-fonts/` | — |

**Steg:**
1. Klistra in de tre filerna **rått** (ingen auto-formattering) i tre snippets med placeringen ovan.
2. Ladda upp de sex Outfit-woff2 (se `fonts/README.md`).
3. Ladda upp de **två genererade produktbilderna** till `wp-content/uploads/` som
   `ampy-laddboxar-mega.webp` och `ampy-solcellsbatterier-mega.webp`
   (finns i `../assets/laddboxar.webp` / `batteri.webp` — döp om vid uppladdning; full-res PNG finns också).
4. I Bricks header-mall: lägg ett **Shortcode-element** överst och skriv `[ampy_header]`.
   (Inte Code-elementet — code-signature-friktion.) Headern är `position:fixed`; se till att
   header-mallen/sektionen inte ligger inuti en `transform`-ad Bricks-container (då tappar fixed sin
   förankring — se PORT-NOTES punkt 3).

## Format 2 — Bricks-JSON (klistra in i Bricks: Ctrl/Cmd+V)  →  `bricks/`

Tre varianter, alla i samma `bricksCopiedElements`-format som originalet:

- **`ampy-header--A-shortcode.json`** — en Header-section med ett Shortcode-element `[ampy_header]`.
  Kräver att CSS+JS-snippsen ovan är installerade. **1-till-1, verifierad kod.** *(Motsvarar Format 1.)*
- **`ampy-header--B-code-element.json`** — en Header-section med ett **självständigt** Code-element som
  bär `<style>` + markup + `<script>` inbakat. Kräver **inga** snippets (utom fonts + de två bilderna).
  **1-till-1, verifierad kod.** Nackdel: Bricks kan kräva code-signering för Code-element.
- **`ampy-header--C-native.json`** — headern ombyggd med **native Bricks-element** (nav-nested/dropdown/
  offcanvas) så den kan redigeras i Bricks-byggaren. ⚠️ **Redigerbar men INTE render-verifierad som A/B**,
  och de bespoke-beteendena (megamenylayout, pulsen, Evify-mobilen, iOS-scrollås) kräver ändå att
  `styles.css` + `engine.js` laddas globalt. Använd A eller B för garanterad pixelparitet; använd C bara
  om builder-redigerbarhet väger tyngre än exakthet.

---

## Öppna owner-beslut (oförändrade)
- CTA-kontrast (vit på teal ~3:1 — medvetet val).
- "Gratis rådgivning" pekar på `/offert/` (etikett vs. destination).
- Solcellsbatteri-bilden är SAJ + Homevolt tills Enershare-bilden kommer (då regenereras 3-produktsbilden).

## Paritetsbevis
`preview/index.html` inkluderar `fluentsnippets/styles.css` + `engine.js` **via referens** och klistrar in
shortcode-markupen — dvs. exakt de bytes du klistrar in i WordPress. Renderad desktop 1440 + mobil 375:
identisk med facit, inga konsolfel, iOS-scrollås/fokus verifierat.
