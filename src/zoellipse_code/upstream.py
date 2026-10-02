"""Load the JetBrains Mono Glyphs sources as a designspace of in-memory UFOs."""
import logging

import glyphsLib
from glyphsLib import to_designspace

from . import params as P


def load(italic):
    """Designspace (sources hold ufoLib2 fonts) for the upright or italic family."""
    logging.getLogger("glyphsLib").setLevel(logging.ERROR)
    gs = glyphsLib.GSFont(str(P.GLYPHS_SOURCES[italic]))
    ds = to_designspace(gs, minimal=False)
    fix_axis_map(ds)
    for src in ds.sources:
        clean(src.font)
    return ds


def fix_axis_map(ds):
    """JetBrains Mono's "Axis Mappings" ({220: 200, ..., 634: 700}) is read by
    glyphsLib as user -> design, i.e. backwards; its build config puts the named
    weights at 100..800. Rebuild the map from the named instances' design locations."""
    # glyphsLib also adds a discrete "ital" axis (breaks gftools builder) and weight
    # labels computed from the backwards map; STAT comes from build.py / config.yaml.
    ds.axes = [a for a in ds.axes if not hasattr(a, "values")]
    axis = ds.axes[0]
    axis.axisLabels = []
    upright = [i for i in ds.instances]
    axis.map = [(100 * (n + 1), i.location[axis.name]) for n, i in enumerate(upright)]
    assert axis.map[0][1] == axis.minimum and axis.map[-1][1] == axis.maximum, axis.map
    axis.minimum, axis.default, axis.maximum = 100, 400, 800


def clean(ufo):
    """Drop backup layers and kerning that points at undefined groups."""
    for name in [layer.name for layer in ufo.layers if layer is not ufo.layers.defaultLayer]:
        del ufo.layers[name]
    groups = set(ufo.groups)
    for pair in list(ufo.kerning):
        if any(side.startswith("public.kern") and side not in groups for side in pair):
            del ufo.kerning[pair]
