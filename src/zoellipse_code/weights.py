"""Match Zoellipse's stroke weight at every named weight.

Each named weight (user 100..800) is placed at the design location where
Zoellipse Code's n stem (after scaling) equals Zoellipse's n stem at that weight
(P.ZOELLIPSE_STEMS). Stems interpolate linearly between the masters, so the
location is found piecewise. Where Zoellipse is lighter than Zoellipse Code's
lightest master or heavier than its heaviest, the weight stays at the end of
the axis; consecutive weights keep at least P.MIN_STEP more stem so Bold and
ExtraBold stay distinct. A Regular master is interpolated at the new default
location (the variable font's default must be a master); outlines are exact
interpolations, nothing is redrawn.
"""
import copy

from fontTools.designspaceLib import SourceDescriptor
from fontTools.pens.basePen import BasePen
from fontmake.instantiator import Instantiator

from . import params as P


class _Poly(BasePen):
    def __init__(self, gs):
        super().__init__(gs)
        self.segs, self.cur, self.start = [], None, None

    def _moveTo(self, p):
        self.cur = self.start = p

    def _closePath(self):
        if self.cur != self.start:
            self.segs.append((self.cur, self.start))

    _endPath = _closePath

    def _lineTo(self, p):
        self.segs.append((self.cur, p))
        self.cur = p

    def _curveToOne(self, a, b, c):
        p0 = self.cur
        prev = p0
        for k in range(1, 17):
            t, u = k / 16, 1 - k / 16
            q = (u**3 * p0[0] + 3 * u * u * t * a[0] + 3 * u * t * t * b[0] + t**3 * c[0],
                 u**3 * p0[1] + 3 * u * u * t * a[1] + 3 * u * t * t * b[1] + t**3 * c[1])
            self.segs.append((prev, q))
            prev = q
        self.cur = c


def stem(ufo, slant):
    """Width of the n's left stem at 30% of the x-height (unslanted)."""
    pen = _Poly(ufo)
    ufo["n"].draw(pen)
    y = 0.3 * ufo.info.xHeight
    xs = sorted(x0 + (y - y0) * (x1 - x0) / (y1 - y0) - slant * y
                for (x0, y0), (x1, y1) in pen.segs if (y0 > y) != (y1 > y))
    return xs[1] - xs[0]


def design_for(target, masters):
    """Design location whose interpolated stem equals target (clamped)."""
    if target <= masters[0][1]:
        return masters[0][0]
    for (d0, s0), (d1, s1) in zip(masters, masters[1:]):
        if target <= s1:
            return d0 + (d1 - d0) * (target - s0) / (s1 - s0)
    return masters[-1][0]


def stem_at(d, masters):
    for (d0, s0), (d1, s1) in zip(masters, masters[1:]):
        if d <= d1:
            return s0 + (s1 - s0) * (d - d0) / (d1 - d0)
    return masters[-1][1]


def match(ds, slant):
    axis = ds.axes[0]
    masters = sorted((src.location[axis.name], stem(src.font, slant)) for src in ds.sources)
    users = sorted(P.ZOELLIPSE_STEMS)
    designs = [design_for(P.ZOELLIPSE_STEMS[u], masters) for u in users]
    designs[-1] = masters[-1][0]                      # heaviest weight = heaviest master
    for i in range(len(designs) - 2, -1, -1):         # keep weights distinct from the top down
        cap = design_for(stem_at(designs[i + 1], masters) / (1 + P.MIN_STEP), masters)
        designs[i] = min(designs[i], cap)
    designs[0] = masters[0][0]
    designs = [round(d, 1) for d in designs]
    for inst, d in zip(ds.instances, designs):        # instances are in weight order
        inst.location = {axis.name: d}
    reg_d = designs[users.index(P.DEFAULT_WGHT)]
    inst = ds.instances[users.index(P.DEFAULT_WGHT)]
    reg = Instantiator.from_designspace(ds).generate_instance(inst)   # with the old map/default
    axis.map = list(zip(users, designs))
    base = ds.sources[0].font
    reg.features.text = base.features.text
    reg.groups.update(copy.deepcopy(dict(base.groups)))
    for k, v in base.lib.items():
        reg.lib.setdefault(k, copy.deepcopy(v))
    reg.lib["public.glyphOrder"] = list(base.lib["public.glyphOrder"])
    reg.info.italicAngle = base.info.italicAngle
    for src in ds.sources:                            # JetBrains Mono's own 400 master
        if src.font.info.styleName == inst.styleName:
            src.font.info.styleName = src.styleName = inst.styleName + " Base"
            src.copyInfo = src.copyLib = src.copyFeatures = src.copyGroups = False
    reg.info.styleName = inst.styleName
    ds.sources.append(SourceDescriptor(font=reg, location={axis.name: reg_d}, styleName=inst.styleName,
                                       copyInfo=True, copyLib=True, copyFeatures=True, copyGroups=True))
    ds.sources.sort(key=lambda src: src.location[axis.name])
    axis.default = P.DEFAULT_WGHT
    return [(u, d, round(stem_at(d, masters))) for u, d in zip(users, designs)]
