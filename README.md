# Zoellipse Code

Zoellipse Code is a monospace variable font, the companion of Zoellipse. It is a
Modified Version of [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
by Philipp Nurullin and Konstantin Bulenkov. Version 1.000.

Designer: Charlie Champanhet. License: SIL OFL 1.1. Built in code (Python) from the unmodified JetBrains Mono Glyphs sources in
`upstream/jetbrains-mono/` (pinned commit 1937130).

## What changed compared to JetBrains Mono

1. **Curves**: a slight superellipse feel. The handles of quarter curves
   (horizontal to vertical) are lengthened the same way as in Zoellipse, which
   lands at about superellipse exponent 2.65 on JetBrains Mono's already
   flat-sided rounds.
2. **Build fixes**: the weight axis mapping is read correctly so the named
   instances sit at 100 to 800 (Bold = 700); an empty glyph mapped to U+16910
   is unmapped; gasp, prep and meta tables are added.
3. **Sized to match Zoellipse**: everything is scaled to 96% inside the em, so
   the x-height (0.528 em) equals Zoellipse's and code mixes with Zoellipse text at
   the same font size. Every glyph is 576 units wide (0.576 em, UPM 1000).
   On its own, Zoellipse Code looks 4% smaller than JetBrains Mono at the same
   size.
4. **Weights matched to Zoellipse**: each named weight sits where its stems
   equal Zoellipse's at that weight (exact from ExtraLight to SemiBold; Bold and
   ExtraBold come as close as JetBrains Mono's heaviest master allows; Thin
   stays a little darker than Zoellipse Thin).
5. **Renamed** to Zoellipse Code.

Everything else is JetBrains Mono: code ligatures (`calt`), the `zero`
feature (slashed and dotted zero alternates), proportions, italic at 9
degrees, about 1780 glyphs.

## Fonts

Weight axis `wght` 100-800, default Regular 400. Named instances: Thin 100,
ExtraLight 200, Light 300, Regular 400, Medium 500, SemiBold 600, Bold 700,
ExtraBold 800.

- `fonts/variable/ZoellipseCode[wght].ttf` / `.woff2`
- `fonts/variable/ZoellipseCode-Italic[wght].ttf` / `.woff2`

The two are linked by the STAT `ital` axis.

## Web usage

```css
@font-face {
  font-family: "Zoellipse Code";
  src: url("fonts/variable/ZoellipseCode%5Bwght%5D.woff2") format("woff2"),
       url("fonts/variable/ZoellipseCode%5Bwght%5D.ttf") format("truetype");
  font-weight: 100 800;
  font-style: normal;
  font-display: swap;
}
@font-face {
  font-family: "Zoellipse Code";
  src: url("fonts/variable/ZoellipseCode-Italic%5Bwght%5D.woff2") format("woff2"),
       url("fonts/variable/ZoellipseCode-Italic%5Bwght%5D.ttf") format("truetype");
  font-weight: 100 800;
  font-style: italic;
  font-display: swap;
}
code { font-family: "Zoellipse Code", ui-monospace, monospace; }
```

Ligatures are on by default; turn them off with
`font-variant-ligatures: none`. Slashed or dotted zero:
`font-feature-settings: "zero"`.

## Pairing with Zoellipse

Zoellipse Code has the same x-height and stroke weights as Zoellipse, so inline code
needs no size adjustment:

```css
body { font-family: "Zoellipse", sans-serif; }
code { font-family: "Zoellipse Code", monospace; }
```

## Build

Generated from the unmodified JetBrains Mono Glyphs sources in
`upstream/jetbrains-mono/`. Requirements: Python 3.10+ (`python3`) and `make`;
the first `make` creates a local virtualenv in `.venv/` from
`requirements-dev.txt` (pinned versions).
```
make build     # write sources/ and the variable fonts into fonts/variable/
make check     # check_outlines, check_squircle
make qa        # Font Bakery reports in qa/
make release   # build + check + dist/ (variable + static fonts, zip)
make gfbuild   # rebuild from sources/ with gftools builder (Google Fonts)
make serve     # http://localhost:8003/specimen/
```

## License
SIL Open Font License 1.1, no Reserved Font Name. See `OFL.txt`, `AUTHORS.txt`,
`CONTRIBUTORS.txt` and `FONTLOG.txt`.
Copyright 2026 The Zoellipse Code Project Authors; copyright 2020 The JetBrains
Mono Project Authors.
