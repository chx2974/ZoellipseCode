## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[5] ZoellipseCode[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1746 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 26 glyphs (1.46%) have a different width. You should check the widths of: ['A.half', 'B.half', 'C.half', 'D.half', 'E.half', 'F.half', 'G.half', 'H.half', 'I.half', 'K.half', 'L.half', 'N.half', 'O.half', 'P.half', 'Q.half', 'R.half', 'S.half', 'T.half', 'U.half', 'V.half', 'X.half', 'one.half', 'two.half', 'three.half', 'four.half', 'uniFEFF']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>


> 
> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright
> or quotesingle or comma or caron(comb). It should be composed with a
> distinctive glyph which doesn't look like an apostrophe.
> 
> Source:
> https://ilovetypography.com/2009/01/24/on-diacritics/
> http://diacritics.typo.cz/index.php?id=5
> https://www.typotheque.com/articles/lcaron
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3308







* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni2318 (U+2318): L&lt;&lt;237.0,184.0&gt;--&lt;179.0,184.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;118.0,246.0&gt;--&lt;118.0,301.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;458.0,246.0&gt;--&lt;458.0,301.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;237.0,526.0&gt;--&lt;179.0,526.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;118.0,410.0&gt;--&lt;118.0,465.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;458.0,465.0&gt;--&lt;458.0,410.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;339.0,526.0&gt;--&lt;397.0,526.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;397.0,184.0&gt;--&lt;339.0,184.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- NULL

- bar_bar_bar.liga

- f.cv02

- g.cv15

- u16910

- uni0306.cy

- uni0311.case

- uni0324.case

- uni0326.alt

- uni032E.case

- 5 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>


> 
> Microsoft's recommendations for OpenType Fonts states the following:
> 
> 'NOTE: The PostScript glyph name must be no longer than 31 characters,
> include only uppercase or lowercase English letters, European digits,
> the period or the underscore, i.e. from the set `[A-Za-z0-9_.]` and
> should start with a letter, except the special glyph name `.notdef`
> which starts with a period.'
> 
> https://learn.microsoft.com/en-us/typography/opentype/otspec181/recom#-post--table
> 
> 
> In practice, though, particularly in modern environments, glyph names
> can be as long as 63 characters.
> 
> According to the "Adobe Glyph List Specification" available at:
> 
> https://github.com/adobe-type-tools/agl-specification
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2832
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
ampersand_ampersand_ampersand.liga, ampersand_ampersand_ampersand.liga.cv15, asciitilde_asciitilde_greater.liga, braceleft_braceleft_hyphen_hyphen.liga, braceleft_exclam_hyphen_hyphen.liga, hyphen_hyphen_braceright_braceright.liga, less_numbersign_hyphen_hyphen.liga, numbersign_numbersign_numbersign.liga, numbersign_numbersign_numbersign_numbersign.liga, numbersign_underscore_parenleft.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>
</div>
</details>

<details><summary>[5] ZoellipseCode-Italic[wght].ttf</summary>
<div>
<details>
    <summary>⚠️ <b>WARN</b> Checking correctness of monospaced metadata. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/opentype.html#opentype-monospace">opentype/monospace</a></summary>
    <div>


> 
> There are various metadata in the OpenType spec to specify if a font is
> monospaced or not. If the font is not truly monospaced, then no monospaced
> metadata should be set (as sometimes they mistakenly are...)
> 
> Requirements for monospace fonts:
> 
> * post.isFixedPitch - "Set to 0 if the font is proportionally spaced,
> non-zero if the font is not proportionally spaced (monospaced)"
> (https://www.microsoft.com/typography/otspec/post.htm)
> 
> * hhea.advanceWidthMax must be correct, meaning no glyph's width value
> is greater. (https://www.microsoft.com/typography/otspec/hhea.htm)
> 
> * OS/2.panose.bProportion must be set to 9 (monospace) on latin text fonts.
> 
> * OS/2.panose.bSpacing must be set to 3 (monospace) on latin hand written
> or latin symbol fonts.
> 
> * Spec says: "The PANOSE definition contains ten digits each of which currently
> describes up to sixteen variations. Windows uses bFamilyType, bSerifStyle
> and bProportion in the font mapper to determine family type. It also uses
> bProportion to determine if the font is monospaced."
> (https://www.microsoft.com/typography/otspec/os2.htm#pan
> https://monotypecom-test.monotype.de/services/pan2)
> 
> * OS/2.xAvgCharWidth must be set accurately.
> "OS/2.xAvgCharWidth is used when rendering monospaced fonts,
> at least by Windows GDI"
> (http://typedrawers.com/discussion/comment/15397/#Comment_15397)
> 
> Also we should report an error for glyphs not of average width.
> 
> 
> Please also note:
> 
> Thomas Phinney told us that a few years ago (as of December 2019), if you gave
> a font a monospace flag in Panose, Microsoft Word would ignore the actual
> advance widths and treat it as monospaced.
> 
> Source: https://typedrawers.com/discussion/comment/45140/#Comment_45140
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The OpenType spec recommends at <a href="https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table">https://learn.microsoft.com/en-us/typography/opentype/spec/recom#hhea-table</a> that hhea.numberOfHMetrics be set to 3 but this font has 1730 instead.
Please read <a href="https://github.com/fonttools/fonttools/issues/3014">https://github.com/fonttools/fonttools/issues/3014</a> to decide whether this makes sense for your font.</p>
 [code: bad-numberOfHMetrics]



* ⚠️ **WARN** <p>Font is monospaced but 27 glyphs (1.53%) have a different width. You should check the widths of: ['A.half', 'B.half', 'C.half', 'D.half', 'E.half', 'F.half', 'G.half', 'H.half', 'I.half', 'K.half', 'L.half', 'M.half', 'N.half', 'O.half', 'P.half', 'Q.half', 'R.half', 'S.half', 'T.half', 'U.half', 'V.half', 'X.half', 'one.half', 'two.half', 'three.half', 'four.half', 'uniFEFF']</p>
 [code: mono-outliers]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check accent of Lcaron, dcaron, lcaron, tcaron <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#alt-caron">alt_caron</a></summary>
    <div>


> 
> Lcaron, dcaron, lcaron, tcaron should NOT be composed with quoteright
> or quotesingle or comma or caron(comb). It should be composed with a
> distinctive glyph which doesn't look like an apostrophe.
> 
> Source:
> https://ilovetypography.com/2009/01/24/on-diacritics/
> http://diacritics.typo.cz/index.php?id=5
> https://www.typotheque.com/articles/lcaron
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3308







* ⚠️ **WARN** <p>dcaron is decomposed and therefore could not be checked. Please check manually.</p>
 [code: decomposed-outline]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check there are no overlapping path segments <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#overlapping-path-segments">overlapping_path_segments</a></summary>
    <div>


> 
> Some rasterizers encounter difficulties when rendering glyphs with
> overlapping path segments.
> 
> A path segment is a section of a path defined by two on-curve points.
> When two segments share the same coordinates, they are considered
> overlapping.
> 




> Original proposal: https://github.com/google/fonts/issues/7594#issuecomment-2401909084





* ⚠️ **WARN** <p>The following glyphs have overlapping path segments:</p>
<pre><code>* uni2318 (U+2318): L&lt;&lt;237.0,184.0&gt;--&lt;178.0,184.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;118.0,245.0&gt;--&lt;118.0,301.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;458.0,245.0&gt;--&lt;458.0,301.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;237.0,526.0&gt;--&lt;178.0,526.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;118.0,410.0&gt;--&lt;118.0,466.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;458.0,466.0&gt;--&lt;458.0,410.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;339.0,526.0&gt;--&lt;398.0,526.0&gt;&gt; has the same coordinates as a previous segment.

* uni2318 (U+2318): L&lt;&lt;398.0,184.0&gt;--&lt;339.0,184.0&gt;&gt; has the same coordinates as a previous segment.
</code></pre>
 [code: overlapping-path-segments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check font contains no unreachable glyphs <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#unreachable-glyphs">unreachable_glyphs</a></summary>
    <div>


> 
> Glyphs are either accessible directly through Unicode codepoints or through
> substitution rules.
> 
> In Color Fonts, glyphs are also referenced by the COLR table. And mathematical
> fonts also reference glyphs via the MATH table.
> 
> Any glyphs not accessible by these means are redundant and serve only
> to increase the font's file size.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3160





* ⚠️ **WARN** <p>The following glyphs could not be reached by codepoint or substitution rules:</p>
<pre><code>- NULL

- bar_bar_bar.liga

- dollar.cv14

- eight.dnom

- eight.numr

- exclam_equal.liga.ss19.001

- exclam_equal_equal.liga.ss19.001

- five.dnom

- five.numr

- four.dnom

- 22 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: unreachable-glyphs]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Glyph names are all valid? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#valid-glyphnames">valid_glyphnames</a></summary>
    <div>


> 
> Microsoft's recommendations for OpenType Fonts states the following:
> 
> 'NOTE: The PostScript glyph name must be no longer than 31 characters,
> include only uppercase or lowercase English letters, European digits,
> the period or the underscore, i.e. from the set `[A-Za-z0-9_.]` and
> should start with a letter, except the special glyph name `.notdef`
> which starts with a period.'
> 
> https://learn.microsoft.com/en-us/typography/opentype/otspec181/recom#-post--table
> 
> 
> In practice, though, particularly in modern environments, glyph names
> can be as long as 63 characters.
> 
> According to the "Adobe Glyph List Specification" available at:
> 
> https://github.com/adobe-type-tools/agl-specification
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/2832
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>The following glyph names may be too long for some legacy systems which may expect a maximum 31-characters length limit:
ampersand_ampersand_ampersand.liga, ampersand_ampersand_ampersand.liga.cv15, asciitilde_asciitilde_greater.liga, braceleft_braceleft_hyphen_hyphen.liga, braceleft_exclam_hyphen_hyphen.liga, exclam_equal_equal.liga.ss19.001, hyphen_hyphen_braceright_braceright.liga, less_numbersign_hyphen_hyphen.liga, numbersign_numbersign_numbersign.liga, numbersign_numbersign_numbersign_numbersign.liga, numbersign_underscore_parenleft.liga and semicolon_semicolon_semicolon.liga</p>
 [code: legacy-long-names]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 10 | 39 | 6 | 187 | 0 | 
| 0% | 0% | 0% | 4% | 16% | 2% | 77% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
