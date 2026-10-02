"""Scale everything by P.SCALE inside the em (UPM stays 1000).

Zoellipse Code's x-height becomes Zoellipse's (0.550 em x 0.96 = 0.528 em), so code
mixes with Zoellipse text at the same font size. Outlines, component offsets,
anchors, advance widths and the vertical metrics all scale together.
"""
from . import params as P

INFO = ("ascender", "descender", "capHeight", "xHeight",
        "openTypeHheaAscender", "openTypeHheaDescender", "openTypeHheaLineGap",
        "openTypeOS2TypoAscender", "openTypeOS2TypoDescender", "openTypeOS2TypoLineGap",
        "openTypeOS2WinAscent", "openTypeOS2WinDescent",
        "postscriptUnderlinePosition", "postscriptUnderlineThickness",
        "openTypeOS2StrikeoutPosition", "openTypeOS2StrikeoutSize",
        "openTypeOS2SubscriptXSize", "openTypeOS2SubscriptYSize",
        "openTypeOS2SubscriptXOffset", "openTypeOS2SubscriptYOffset",
        "openTypeOS2SuperscriptXSize", "openTypeOS2SuperscriptYSize",
        "openTypeOS2SuperscriptXOffset", "openTypeOS2SuperscriptYOffset")
LISTS = ("postscriptBlueValues", "postscriptOtherBlues", "postscriptFamilyBlues",
         "postscriptFamilyOtherBlues", "postscriptStemSnapH", "postscriptStemSnapV")


def s(v):
    return round(v * P.SCALE)


def transform(ufo):
    for g in ufo:
        for c in g.contours:
            for p in c.points:
                p.x, p.y = s(p.x), s(p.y)
        for comp in g.components:
            t = comp.transformation
            comp.transformation = (t[0], t[1], t[2], t[3], s(t[4]), s(t[5]))
        for a in g.anchors:
            a.x, a.y = s(a.x), s(a.y)
        for gl in g.guidelines or []:
            gl.x, gl.y = s(gl.x or 0), s(gl.y or 0)
        g.width = s(g.width)
    for pair, v in list(ufo.kerning.items()):
        ufo.kerning[pair] = s(v)
    i = ufo.info
    for k in INFO:
        if getattr(i, k) is not None:
            setattr(i, k, s(getattr(i, k)))
    for k in LISTS:
        if getattr(i, k):
            setattr(i, k, [s(v) for v in getattr(i, k)])


def win_metrics(fonts):
    """usWin* covering every glyph of every master (scaled outlines, incl. the
    heavy end, where JetBrains Mono's stacked accents already exceeded them)."""
    hi, lo = 0, 0
    for ufo in fonts:
        for g in ufo:
            b = g.getBounds(ufo)
            if b:
                hi, lo = max(hi, b.yMax), min(lo, b.yMin)
    for ufo in fonts:
        ufo.info.openTypeOS2WinAscent = max(ufo.info.openTypeOS2WinAscent or 0, int(hi) + 1)
        ufo.info.openTypeOS2WinDescent = max(ufo.info.openTypeOS2WinDescent or 0, int(-lo) + 1)
