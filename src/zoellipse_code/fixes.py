"""Font-level additions for current Font Bakery / Google Fonts checks."""
from fontTools.ttLib import newTable
import unicodedata

from fontTools.ttLib.tables import ttProgram


def unmap_empty(ufo):
    """Drop code points of visible characters whose glyph is empty
    (JetBrains Mono maps U+16910, a Bamum letter, to an empty glyph)."""
    dropped = []
    for g in ufo:
        if g.unicodes and not g.contours and not g.components:
            keep = [u for u in g.unicodes if unicodedata.category(chr(u)) in ("Zs", "Cc", "Cf", "Mn", "Zl", "Zp")]
            if keep != g.unicodes:
                dropped += [f"U+{u:04X}" for u in g.unicodes if u not in keep]
                g.unicodes = keep
    return dropped


def unhinted_tables(font):
    """gasp (smooth at all sizes), prep with smart dropout control, meta (Latn)."""
    gasp = newTable("gasp")
    gasp.version = 1
    gasp.gaspRange = {0xFFFF: 0x000F}
    font["gasp"] = gasp
    prep = newTable("prep")
    prep.program = ttProgram.Program()
    prep.program.fromBytecode(bytes([0xB8, 0x01, 0xFF, 0x85, 0xB0, 0x04, 0x8D]))
    font["prep"] = prep
    meta = newTable("meta")
    meta.data = {"dlng": "Latn", "slng": "Latn"}
    font["meta"] = meta
