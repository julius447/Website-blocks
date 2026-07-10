# Self-hosted Outfit (GDPR — no Google Fonts request)

`styles.css` references these six files:

```
/wp-content/uploads/ampy-fonts/Outfit-Light.woff2      (300)
/wp-content/uploads/ampy-fonts/Outfit-Regular.woff2    (400)
/wp-content/uploads/ampy-fonts/Outfit-Medium.woff2     (500)
/wp-content/uploads/ampy-fonts/Outfit-SemiBold.woff2   (600)
/wp-content/uploads/ampy-fonts/Outfit-Bold.woff2       (700)
/wp-content/uploads/ampy-fonts/Outfit-ExtraBold.woff2  (800)
```

**To do:** download Outfit (OFL, Google Fonts / fontsource), convert each weight to `woff2`,
and upload the six files to `wp-content/uploads/ampy-fonts/`. One `@font-face` per weight is
already declared in `styles.css` (so the browser never faux-bolds a missing weight),
`font-display:swap`. If Outfit is already self-hosted elsewhere in the theme, delete the
`@font-face` block from `styles.css` and keep only the `--font` stack.
