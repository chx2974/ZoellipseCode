"""Zoellipse Code: every number that makes it differ from JetBrains Mono.

Zoellipse Code is a Modified Version of JetBrains Mono (OFL 1.1). The pipeline
loads the upstream Glyphs sources unchanged and applies the transforms below
in code. Units are JetBrains Mono's (UPM 1000).
"""
from pathlib import Path

FAMILY = "Zoellipse Code"
FILE = "ZoellipseCode"                  # file-name / PostScript-name prefix
VERSION = (1, 0)
VENDOR = "NONE"

ROOT = Path(__file__).resolve().parents[2]
UPSTREAM = ROOT / "upstream" / "jetbrains-mono"
GLYPHS_SOURCES = {False: UPSTREAM / "JetBrainsMono.glyphs",
                  True: UPSTREAM / "JetBrainsMono-Italic.glyphs"}

UPM = 1000
CAP = 730                            # JetBrains Mono cap height (before SCALE)
XH = 550                             # JetBrains Mono x-height (75% of cap, before SCALE)

# Everything scaled inside the em so the x-height equals Zoellipse's at the same
# font size: 550 x 0.96 = 528 = Zoellipse's 1056/2000. Cells become 576 wide.
SCALE = 0.96

# Weight matching: n stem of Zoellipse (per 1000 units) at each named weight,
# measured from the Zoellipse build on 2026-10-02. Each Zoellipse Code weight is put
# where its (scaled) n stem equals these; MIN_STEP keeps neighbours distinct.
ZOELLIPSE_STEMS = {100: 39, 200: 62, 300: 78, 400: 92, 500: 107, 600: 121, 700: 146, 800: 170}
MIN_STEP = 0.08
DEFAULT_WGHT = 400

# Superellipse feel: curves running from a horizontal to a vertical tangent get
# longer handles, as if an ellipse (n = 2) became a superellipse of exponent N.
SUPER_N = 2.4
SUPER_MIN_SPAN = 30                  # skip quarter curves smaller than this (joins, tiny details)

COPYRIGHT = ("Copyright 2026 The Zoellipse Code Project Authors (https://github.com/chx2974/ZoellipseCode); "
             "Copyright 2020 The JetBrains Mono Project Authors (https://github.com/JetBrains/JetBrainsMono)")
DESIGNER = "Charlie Champanhet; JetBrains Mono: Philipp Nurullin, Konstantin Bulenkov"
DESCRIPTION = ("Zoellipse Code is a Modified Version of JetBrains Mono "
               "with subtly superelliptic curves, a companion to Zoellipse.")
LICENSE = ("This Font Software is licensed under the SIL Open Font License, Version 1.1. "
           "This license is available with a FAQ at: https://openfontlicense.org")
LICENSE_URL = "https://openfontlicense.org"
