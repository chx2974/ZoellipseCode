## FontBakery report

fontbakery version: 1.1.0







## Check results



<details><summary>[9] ZoellipseCode[wght].ttf</summary>
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

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594





* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, todhri, coptic, syriac, duployan, canadian-aboriginal, tifinagh, math, tai-le, malayalam, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
490 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>


> 
> This check heuristically looks for on-curve points which are close to, but
> do not sit on, significant boundary coordinates. For example, a point which
> has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as
> the baseline, here we also check for points near the x-height (but only for
> lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design
> may call for points in locations near the boundaries. As this check is liable
> to generate significant numbers of false positives, it will pass if there are
> more than 100 reported misalignments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Aogonek (U+0104): X=510.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=454.0,Y=-1.0 (should be at baseline 0?)

* Iogonek (U+012E): X=321.0,Y=-1.0 (should be at baseline 0?)

* Q (U+0051): X=300.0,Y=-2.0 (should be at baseline 0?)

* Q.half: X=237.5,Y=1.0 (should be at baseline 0?)

* eogonek (U+0119): X=383.0,Y=-1.0 (should be at baseline 0?)

* g (U+0067): X=398.0,Y=2.0 (should be at baseline 0?)

* g (U+0067): X=489.0,Y=1.0 (should be at baseline 0?)

* uni01F5 (U+01F5): X=398.0,Y=2.0 (should be at baseline 0?)

* uni01F5 (U+01F5): X=489.0,Y=1.0 (should be at baseline 0?)

* 46 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>

<details><summary>[9] ZoellipseCode-Italic[wght].ttf</summary>
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

<details>
    <summary>⚠️ <b>WARN</b> Validate size, and resolution of article images, and ensure article page has minimum length and includes visual assets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-article-images">googlefonts/article/images</a></summary>
    <div>


> 
> The purpose of this check is to ensure images (either raster or vector files)
> are not excessively large in filesize and resolution.
> 
> These constraints are loosely based on infrastructure limitations under
> default configurations.
> 
> It also ensures that the article page has a minimum length and includes
> at least one visual asset.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4594





* ⚠️ **WARN** <p>Family metadata at fonts/variable does not have an article.</p>
 [code: lacks-article]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Check for codepoints not covered by METADATA subsets. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-metadata-unreachable-subsetting">googlefonts/metadata/unreachable_subsetting</a></summary>
    <div>


> 
> This check ensures that all encoded glyphs in the font are covered by a
> subset declared in the METADATA.pb. Google Fonts splits the font into
> a set of subset fonts based on the contents of the `subsets` field and
> the subset definitions in the `glyphsets` repository.
> 
> Any encoded glyphs which are not by any of these subset definitions
> will not be served in the subsetted fonts, and so will be unreachable to
> the end user.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/4097
> See also: https://github.com/fonttools/fontbakery/pull/4273





* ⚠️ **WARN** <p>The following codepoints supported by the font are not covered by
any subsets defined in the font's metadata file, and will never
be served. You can solve this by either manually adding additional
subset declarations to METADATA.pb, or by editing the glyphset
definitions.</p>
<ul>
<li>U+02D8 BREVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02D9 DOT ABOVE: try adding one of: canadian-aboriginal, yi</li>
<li>U+02DB OGONEK: try adding one of: canadian-aboriginal, yi</li>
<li>U+0302 COMBINING CIRCUMFLEX ACCENT: try adding one of: cherokee, tifinagh, math, coptic</li>
<li>U+0306 COMBINING BREVE: try adding one of: tifinagh, old-permic</li>
<li>U+0307 COMBINING DOT ABOVE: try adding one of: old-permic, todhri, coptic, syriac, duployan, canadian-aboriginal, tifinagh, math, tai-le, malayalam, hebrew</li>
<li>U+030A COMBINING RING ABOVE: try adding one of: syriac, duployan</li>
<li>U+030B COMBINING DOUBLE ACUTE ACCENT: try adding one of: cherokee, osage</li>
<li>U+030C COMBINING CARON: try adding one of: cherokee, tai-le</li>
<li>U+030F COMBINING DOUBLE GRAVE ACCENT: not included in any glyphset definition
490 more.</li>
</ul>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
<p>Or you can add the above codepoints to one of the subsets supported by the font: <code>cyrillic</code>, <code>cyrillic-ext</code>, <code>greek</code>, <code>latin</code>, <code>latin-ext</code>, <code>symbols2</code>, <code>vietnamese</code></p>
 [code: unreachable-subsetting]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Are there any misaligned on-curve points? <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/universal.html#outline-alignment-miss">outline_alignment_miss</a></summary>
    <div>


> 
> This check heuristically looks for on-curve points which are close to, but
> do not sit on, significant boundary coordinates. For example, a point which
> has a Y-coordinate of 1 or -1 might be a misplaced baseline point. As well as
> the baseline, here we also check for points near the x-height (but only for
> lowercase Latin letters), cap-height, ascender and descender Y coordinates.
> 
> Not all such misaligned curve points are a mistake, and sometimes the design
> may call for points in locations near the boundaries. As this check is liable
> to generate significant numbers of false positives, it will pass if there are
> more than 100 reported misalignments.
> 




> Original proposal: https://github.com/fonttools/fontbakery/pull/3088





* ⚠️ **WARN** <p>The following glyphs have on-curve points which have potentially incorrect y coordinates:</p>
<pre><code>* Aogonek (U+0104): X=466.0,Y=-1.0 (should be at baseline 0?)

* Eogonek (U+0118): X=411.0,Y=-1.0 (should be at baseline 0?)

* Iogonek (U+012E): X=277.0,Y=-1.0 (should be at baseline 0?)

* Ohorn (U+01A0): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni1EDA (U+1EDA): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni1EE2 (U+1EE2): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni1EDC (U+1EDC): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni1EDE (U+1EDE): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni1EE0 (U+1EE0): X=584.0,Y=702.0 (should be at cap-height 701?)

* uni01EA (U+01EA): X=341.0,Y=-1.0 (should be at baseline 0?)

* 47 more.
</code></pre>
<p>Use -F or --full-lists to disable shortening of long lists.</p>
 [code: found-misalignments]



</div>
</details>

<details>
    <summary>⚠️ <b>WARN</b> Checking OS/2 achVendID. <a href="https://fontbakery.readthedocs.io/en/stable/fontbakery/checks/googlefonts.html#googlefonts-vendor-id">googlefonts/vendor_id</a></summary>
    <div>


> 
> Microsoft keeps a list of font vendors and their respective contact info. This
> list is updated regularly and is indexed by a 4-char "Vendor ID" which is
> stored in the achVendID field of the OS/2 table.
> 
> Registering your ID is not mandatory, but it is a good practice since some
> applications may display the type designer / type foundry contact info on some
> dialog and also because that info will be visible on Microsoft's website:
> 
> https://docs.microsoft.com/en-us/typography/vendors/
> 
> This check verifies whether or not a given font's vendor ID is registered in
> that list or if it has some of the default values used by the most common
> font editors.
> 
> Each new FontBakery release includes a cached copy of that list of vendor IDs.
> If you registered recently, you're safe to ignore warnings emitted by this
> check, since your ID will soon be included in one of our upcoming releases.
> 




> Original proposal: https://github.com/fonttools/fontbakery/issues/3943
> See also: https://github.com/fonttools/fontbakery/issues/4829





* ⚠️ **WARN** <p>OS/2 VendorID value 'NONE' is not yet recognized. If you registered it recently, then it's safe to ignore this warning message. Otherwise, you should set it to your own unique 4 character code, and register it with Microsoft at <a href="https://www.microsoft.com/typography/links/vendorlist.aspx">https://www.microsoft.com/typography/links/vendorlist.aspx</a></p>
 [code: unknown]



</div>
</details>
</div>
</details>




### Summary

| 💥 ERROR | ☠ FATAL | 🔥 FAIL | ⚠️ WARN | ⏩ SKIP | ℹ️ INFO | ✅ PASS | 🔎 DEBUG | 
| ---|---|---|---|---|---|---|---|
| 0 | 0 | 0 | 18 | 181 | 15 | 241 | 0 | 
| 0% | 0% | 0% | 4% | 40% | 3% | 53% | 0% | 



**Note:** The following loglevels were omitted in this report:


* SKIP
* INFO
* PASS
* DEBUG
