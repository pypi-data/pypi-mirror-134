import enum
import math, tempfile, pickle, inspect
from subprocess import call
from os import stat
from pathlib import Path

from typing import Optional, Callable, Tuple
from coldtype.geometry.primitives import add
from coldtype.geometry.edge import txt_to_edge
#from collections.abc import Callable

from collections import namedtuple
from fontTools.misc.transform import Transform
from random import randint, Random
from coldtype.img.blendmode import BlendMode

from coldtype.sh import sh
from coldtype.pens.draftingpens import DraftingPen, DraftingPens
from coldtype.interpolation import norm

from coldtype.geometry import Rect, Edge, Point, Line, Geometrical
from coldtype.color import normalize_color, hsl, rgb, bw


def _random_series(start=0, end=1, seed=0, count=5000):
    rnd = Random()
    rnd.seed(seed)
    rnds = []
    for x in range(count):
        rnds.append(start+rnd.random()*(end-start))
    return rnds


def listit(t):
    return list(map(listit, t)) if isinstance(t, (list, tuple)) else t


class DATPen(DraftingPen):
    """
    Main vector representation in Coldtype
    
    DATPen is a subclass of fontTools ``RecordingPen``
    """
    def __init__(self, *args, **kwargs):
        """**kwargs support is deprecated, should not accept any arguments"""
        super().__init__()
        self.single_pen_class = DATPen
        self.multi_pen_class = DATPens

        self._current_attr_tag = "default"
        self.clearAttrs()
        self.attr("default", **kwargs)
        self.typographic = False
        self._tag = "?"
        self._parent = None
        self.container = None
        self.glyphName = None
        self.data = {}
        self._visible = True

        for idx, arg in enumerate(args):
            if isinstance(arg, str):
                self.tag(arg)
            elif isinstance(arg, DraftingPen):
                self.replace_with(arg)
            elif isinstance(arg, Rect):
                self.rect(arg)
            elif isinstance(arg, Line):
                self.line(arg).s(rgb(0, 0.5, 1)).sw(5)
            elif isinstance(arg, Point):
                self.oval(Rect.FromCenter(arg, 50, 50))
    
    def __str__(self):
        v = "" if self._visible else "ø-"
        d = {**self.data}
        if "_last_align_rect" in d:
            del d["_last_align_rect"]
        if self.glyphName:
            return f"<{v}DP:'{self.glyphName}'/tag={self._tag}/data={self.data}>"
        else:
            return f"<{v}DP/tag={self._tag}/data:{self.data}>"
    
    def __len__(self):
        return len(self.value)
    
    def __bool__(self):
        return True
        return bool(len(self) > 0 or self._frame)
    
    def __add__(self, item):
        return DATPens([self, item])
    
    def __sub__(self, item):
        return DATPens([self])
    
    def to_code(self, classname="DATPen", additional_lines=[]):
        t = None
        if self._tag and self._tag != "?":
            t = self._tag
        out = f"({classname}()"
        if t:
            out += f"\n    .tag(\"{t}\")"

        if self.data:
            out += f"\n    .add_data({repr(self.data)})"

        for mv, pts in self.value:
            out += "\n"
            if len(pts) > 0:
                spts = ", ".join([f"{(x, y)}" for (x, y) in pts])
                out += f"    .{mv}({spts})"
            else:
                out += f"    .{mv}()"
        for k, v in self.attrs.get("default").items():
            if v:
                if k == "fill":
                    out += f"\n    .f({v.to_code()})"
                elif k == "stroke":
                    out += f"\n    .s({v['color'].to_code()})"
                    out += f"\n    .sw({v['weight']})"
                else:
                    print("No code", k, v)
        
        for la in additional_lines:
            out += f"\n    {la}"

        out += ")"
        return out
    
    def fvl(self):
        allpts = []
        for mv, pts in self.value:
            if len(pts) > 0:
                allpts.extend(pts)
        return allpts
    
    def getFrame(self, th=False, tv=False):
        return self.ambit(th=th, tv=tv)
    
    def repeatx(self, times=1):
        w = self.getFrame(th=1).point("SE").x
        copy = self.copy().translate(w, 0)
        copy_0_move, copy_0_data = copy.value[0]
        copy.value[0] = ("lineTo", copy_0_data)
        self.value = self.value[:-1] + copy.value
        if times > 1:
            self.repeatx(times-1)
        return self
    
    def fenced(self, *lines):
        if len(lines) == 1 and isinstance(lines[0], Rect):
            return self.intersection(DATPen().rect(lines[0]))
        return self.intersection(DATPen().fence(*lines))
    
    ƒ = fenced
    
    def smoothen(self):
        """Runs a catmull spline on the datpen, useful in combination as flatten+roughen+smooth"""
        dp = DATPen()
        for pts in self.skeletonPoints():
            _pts = [p[-1][-1] for p in pts]
            dp.catmull(_pts, close=True)
        self.value = dp.value
        return self
    
    def roughen(self, amplitude=10, threshold=10, ignore_ends=False, seed=None):
        """Randomizes points in skeleton"""
        if seed is not None:
            rs = _random_series(0, amplitude, seed=seed)
        else:
            rs = _random_series(0, amplitude, seed=randint(0, 5000))
        randomized = []
        _x = 0
        _y = 0
        for idx, (t, pts) in enumerate(self.value):
            if idx == 0 and ignore_ends:
                randomized.append([t, pts])
                continue
            if idx == len(self.value) - 1 and ignore_ends:
                randomized.append([t, pts])
                continue
            if t == "lineTo" or t == "curveTo":
                #jx = pnoise1(_x) * amplitude # should actually be 1-d on the tangent (maybe? TODO)
                #jy = pnoise1(_y) * amplitude
                jx = rs[idx*2] - amplitude/2
                jy = rs[idx*2+1] - amplitude/2
                randomized.append([t, [(x+jx, y+jy) for x, y in pts]])
                _x += 0.2
                _y += 0.3
            else:
                randomized.append([t, pts])
        self.value = randomized
        return self
    
    def dots(self, radius=4):
        """(Necessary?) Create circles at moveTo commands"""
        dp = DATPen()
        for t, pts in self.value:
            if t == "moveTo":
                x, y = pts[0]
                dp.oval(Rect((x-radius, y-radius, radius, radius)))
        self.value = dp.value
        return self
    
    def catmull(self, points, close=False):
        """Run a catmull spline through a series of points"""
        p0 = points[0]
        p1, p2, p3 = points[:3]
        pts = [p0]
        i = 1
        while i < len(points):
            pts.append([
                ((-p0[0] + 6 * p1[0] + p2[0]) / 6),
                ((-p0[1] + 6 * p1[1] + p2[1]) / 6),
                ((p1[0] + 6 * p2[0] - p3[0]) / 6),
                ((p1[1] + 6 * p2[1] - p3[1]) / 6),
                p2[0],
                p2[1]
            ])
            p0 = p1
            p1 = p2
            p2 = p3
            try:
                p3 = points[i + 2]
            except:
                p3 = p3
            i += 1
        self.moveTo(pts[0])
        for p in pts[1:]:
            self.curveTo((p[0], p[1]), (p[2], p[3]), (p[4], p[5]))
        if close:
            self.closePath()
        return self
    
    def pattern(self, rect, clip=False):
        dp_copy = DATPen()
        dp_copy.value = self.value

        for y in range(-1, 1):
            for x in range(-1, 1):
                dpp = DATPen()
                dp_copy.replay(dpp)
                dpp.translate(rect.w*x, rect.h*y)
                dpp.replay(self)
        
        self.translate(rect.w/2, rect.h/2)
        if clip:
            clip_box = DATPen().rect(rect)
            return self.intersection(clip_box)
        return self
    
    def fence(self, *edges):
        self.moveTo(edges[0][0])
        self.lineTo(edges[0][1])
        for edge in edges[1:]:
            self.lineTo(edge[0])
            self.lineTo(edge[1])
        self.closePath()
        return self
    
    def points(self):
        """Returns a list of points grouped by contour from the DATPen’s original contours; useful for drawing bezier skeletons; does not modify the DATPen"""
        contours = []
        for contour in self.skeletonPoints():
            _c = []
            for step, pts in contour:
                for pt in pts:
                    _c.append(Point(pt))
            contours.append(_c)
        return contours
    
    def flatpoints(self):
        """Returns a flat list of points from the DATPen’s original contours; does not modify the DATPen"""
        points = []
        for contour in self.skeletonPoints():
            for step, pts in contour:
                for pt in pts:
                    if len(points) == 0 or points[-1] != pt:
                        points.append(pt)
        return points
    
    def points_lookup(self):
        self.value = listit(self.value)
        lookup = []
        vi = 0
        while vi < len(self.value):
            pv = self.value[vi]
            t = pv[0]
            pvpts = self.value[vi][-1]
            for i, pt in enumerate(self.value[vi][-1]):
                lookup.append(dict(pt=Point(pt), vi=vi, i=i, t=t))
            vi += 1
        return lookup
    
    def mod_point(self, lookup, idx, x, y):
        pl = lookup[idx]
        pt = pl.get("pt")
        pt[0] += x
        pt[1] += y
        self.value[pl.get("vi")][-1][pl.get("i")] = pt
        return pt
    
    def lines(self):
        """Returns lines connecting point-representation of `flatpoints`"""
        ls = []
        pts = self.flatpoints()
        for idx, pt in enumerate(pts):
            if idx > 0:
                ls.append([pts[idx-1], pts[idx]])
        if len(ls) > 1:
            ls.append([pts[-1], pts[0]])
        return ls
    
    def skeletonPoints(self):
        """WIP"""
        all_points = []
        points = []
        self.pvl()
        for idx, (t, pts) in enumerate(self.value):
            if t == "moveTo":
                points.append(("moveTo", pts))
            elif t in ["curveTo", "qCurveTo"]:
                p0 = self.value[idx-1][-1][-1]
                points.append(("curveTo", [p0, *pts]))
            elif t == "lineTo":
                p0 = self.value[idx-1][-1][-1]
                points.append(("lineTo", [p0, *pts]))
            elif t == "closePath":
                all_points.append(points)
                points = []
                #points.append(("closePath", [None]))
        if len(points) > 0:
            all_points.append(points)
        return all_points
    
    def all_guides(self, field="defs", sw=1, l=0, a=0.15):
        dps = DATPens()
        for idx, (k, x) in enumerate(getattr(self, field).values.items()):
            c = hsl(idx/2.3, 1, l=0.35, a=a)
            if isinstance(x, Geometrical) or isinstance(x, DraftingPen):
                g = (DATPen(x)
                    .translate(l, 0)
                    .f(None)
                    .s(c).sw(sw))
                if k in ["gb", "gc", "gs", "gxb"]:
                    c = hsl(0.6, 1, 0.5, 0.25)
                    g.s(c).sw(2)
                dps += g
                dps += DATText(k, ["Helvetica", 24, dict(fill=c.with_alpha(a).darker(0.2))], Rect.FromCenter(g.bounds().pc, 24))
        return dps
    
    def preserve(self, tag, calls, dir=None):
        self.tag(tag)
        pdir = Path("preserved" or dir)
        pdir.mkdir(exist_ok=True, parents=True)
        tmp = (pdir / f"test_{tag}.pickle")
        self.data["_preserve"] = dict(calls=calls, pickle=str(tmp.absolute()))
        pickle.dump(self, open(str(tmp), "wb"))
        return self
    
    def editable(self, tag):
        self.tag(tag)
        self.editable = True
        return self
    
    def contain(self, rect):
        """For conveniently marking an arbitrary `Rect` container."""
        self.container = rect
        return self
    
    def blendmode(self, blendmode=None, show=False):
        if isinstance(blendmode, int):
            blendmode = BlendMode.Cycle(blendmode, show=show)
        elif isinstance(blendmode, str):
            blendmode = BlendMode[blendmode]
        
        if blendmode:
            return self.attr(blendmode=blendmode)
        else:
            return self.attr(field="blendmode")
        return self
    
    def clearFrame(self):
        """Remove the DATPen frame."""
        self._frame = None
        return self
    
    def addFrame(self, frame, typographic=False, passthru=False):
        """Add a new frame to the DATPen, replacing any old frame. Passthru ignored, there for compatibility"""
        self._frame = frame
        if typographic:
            self.typographic = True
        return self
    
    add_frame = addFrame
    
    def frameSet(self, th=False, tv=False):
        """Return a new DATPen represent
        ation of the frame of this DATPen."""
        return self.single_pen_class(fill=("random", 0.25)).rect(self.getFrame(th=th, tv=tv))
    
    def _repr_html_(self):
        if self.data.get("_notebook_shown"):
            return None
        
        from coldtype.notebook import show, DEFAULT_DISPLAY
        self.ch(show(DEFAULT_DISPLAY, th=1, tv=1))
        return None
    
    def at_rotation(self, degrees, fn:Callable[["DATPen"], None], point=None):
        self.rotate(degrees)
        fn(self)
        self.rotate(-degrees)
        return self
    
    # def at_scale(self, scale, fn:Callable[["DATPen"], None]):
    #     self.scale(scale)
    #     self.scale()
    #     # TODO
    #     return self
    
    def DiskCached(path:Path, build_fn: Callable[[], "DATPen"]):
        dpio = None
        fn_src = inspect.getsource(build_fn)
        if not path.exists():
            path.parent.mkdir(parents=True, exist_ok=True)
            dpio = build_fn()
        else:
            try:
                dpio = pickle.load(open(path, "rb"))
                old_fn_src = dpio.data.get("fn_src", "")
                if fn_src != old_fn_src:
                    dpio = build_fn()
            except pickle.PickleError:
                dpio = build_fn()
        
        dpio.data["fn_src"] = fn_src
        pickle.dump(dpio, open(path, "wb"))
        return dpio
    
    @staticmethod
    def WithRect(rect, fn):
        dp = DATPen()
        return fn(rect, dp)
    
    @staticmethod
    def With1000(fn):
        return DATPen.WithRect(Rect(1000, 1000), fn)
    
    # @staticmethod
    # def Easer(angle=1, fA=0.5, fB=0.9):
    #     return DATPen.With1000(lambda r, p:
    #         p.ease_curve(r.psw, r.pne, angle, fA, fB))


DATPensEnumerable = namedtuple("DATPensEnumerable", ["i", "el", "e", "len", "k"])


class DATPens(DraftingPens, DATPen):
    """
    A set/collection of DATPen’s
    
    Behaves like a list but can be queried somewhat like a DOM
    """
    def __init__(self, pens=[]):
        DraftingPens.__init__(self) # TODO pass pens

        self.single_pen_class = DATPen
        self.locals = dict(DP=DATPen)
        self.subs = {
            "□": "ctx.bounds()",
            "■": "_dps.bounds()"
        }

        self.append(pens)
        #if isinstance(pens, DraftingPen):
        #    self.append(pens)
        #else:
        #    for pen in pens:
        #        self.append(pen)
    
    def __str__(self):
        v = "" if self.visible else "ø-"
        d = {**self.data}
        if "_last_align_rect" in d:
            del d["_last_align_rect"]
        out = f"<{v}DPS/len={len(self._pens)}/tag={self._tag}/data={d})>"
        if hasattr(self, "glyphName") and self.glyphName:
            return out[:-1] + f":::glyphName:{self.glyphName}>"
        return out
    
    def __len__(self):
        return len(self._pens)
    
    def to_code(self):
        out = "(DATPens()"

        t = None
        if self._tag and self._tag != "?":
            t = self._tag
        if t:
            out += f"\n    .tag(\"{t}\")"
        
        if self.data:
            out += f"\n    .add_data({repr(self.data)})"

        for pen in self._pens:
            for idx, line in enumerate(pen.to_code().split("\n")):
                if idx == 0:
                    out += f"\n    .append{line}"
                else:
                    out += f"\n    {line}"
            out += ""

        out += ")"
        return out
    
    def copy(self, with_data=False):
        """Get a completely new copy of this whole set of pens,
        usually done so you can duplicate and further modify a
        DATPens without mutating the original"""
        dps = DATPens()
        for p in self._pens:
            dps.append(p.copy(with_data=with_data))
        return dps
    
    def __getitem__(self, index):
        return self._pens[index]
    
    def indexed_subset(self, indices):
        """Take only the pens at the given indices"""
        dps = DATPens()
        for idx, p in enumerate(self._pens):
            if idx in indices:
                dps.append(p.copy())
        return dps
    
    def __setitem__(self, index, pen):
        self._pens[index] = pen
    
    def __iadd__(self, item):
        return self.append(item)
    
    def __add__(self, item):
        return self.append(item)
    
    def __sub__(self, item):
        return self
    
    def _appendable(self, pen, allow_blank=False):
        if callable(pen):
            pen = pen(self)
        
        if pen or allow_blank:
            if isinstance(pen, Geometrical):
                dp = DATPen(pen)
                dp._parent = self
                return [dp]
            elif isinstance(pen, DATPen):
                pen._parent = self
                return [pen]
            elif isinstance(pen, DraftingPens):
                dps = DATPens(pen._pens)
                dps._parent = self
                return [dps]
            elif isinstance(pen, DraftingPen):
                dp = DATPen(pen)
                dp._parent = self
                return [dp]
            else:
                try:
                    out = []
                    for p in pen:
                        if p:
                            if hasattr(p, "_parent"):
                                p._parent = self
                            out.append(p)
                    return out
                except TypeError:
                    #print("appending non-pen", type(pen))
                    return [pen]
                    #print(">>> append rejected", pen)
        return []
    
    def insert(self, index, pen):
        if callable(pen):
            pen = pen(self)
        
        for app in self._appendable(pen):
            self._pens.insert(index, app)
        return self
    
    def append(self, pen, allow_blank=False):
        if callable(pen):
            pen = pen(self)

        for app in self._appendable(pen, allow_blank):
            self._pens.append(app)
        return self
    
    ap = append
    
    def extend(self, pens):
        if hasattr(pens, "_pens"):
            self.append(pens)
        else:
            for p in pens:
                if p:
                    if hasattr(p, "value"):
                        self.append(p)
                    else:
                        self.extend(p)
        return self
        
    # def reversePens(self):
    #     """Reverse the order of the pens; useful for overlapping glyphs from the left-to-right rather than right-to-left (as is common in OpenType applications)"""
    #     self._pens = list(reversed(self._pens))
    #     return self
    
    # def removeBlanks(self):
    #     """Remove blank pens from the set"""
    #     nonblank_pens = []
    #     for pen in self._pens:
    #         if not pen.removeBlanks():
    #             nonblank_pens.append(pen)
    #     self._pens = nonblank_pens
    #     return self
    
    def clearFrames(self):
        """Get rid of any non-bounds-derived pen frames;
        i.e. frames set by Harfbuzz"""
        for p in self._pens:
            p.clearFrame()
        return self
    
    def addFrame(self, frame, typographic=False, passthru=False):
        """Add a frame that isn't derived from the bounds"""
        if passthru:
            for p in self._pens:
                p.addFrame(frame, typographic=typographic)
        else:
            self._frame = frame
            self.typographic = typographic
        return self
    
    add_frame = addFrame
    
    def getFrame(self, th=False, tv=False):
        """Get the frame of the DATPens;
        `th` means `(t)rue (h)orizontal`;
        `ty` means `(t)rue (v)ertical`;
        passing either ignores a non-bounds-derived frame
        in either dimension"""
        if self._frame and (th == False and tv == False):
            return self._frame
        else:
            try:
                union = self._pens[0].ambit(th=th, tv=tv)
                for p in self._pens[1:]:
                    union = union.union(p.ambit(th=th, tv=tv))
                return union
            except Exception as e:
                return Rect(0,0,0,0)
    
    # def bounds(self):
    #     """Calculated bounds of a DATPens"""
    #     return self.getFrame(th=1, tv=1)
    
    # def pen(self):
    #     """A flat representation of this set as a single pen"""
    #     dp = DATPen()
    #     fps = self.collapse()
    #     for p in fps._pens:
    #         dp.record(p)
    #     if len(fps._pens) > 0:
    #         for k, attrs in fps._pens[0].attrs.items():
    #             dp.attr(tag=k, **attrs)
    #     dp.addFrame(self.getFrame())
    #     return dp
    
    # def realize(self):
    #     for k, v in self._register.values.items():
    #         self.append(DATPen(v).tag(k))
    #     return self
    
    # def align(self, rect, x=Edge.CenterX, y=Edge.CenterY, th=True, tv=False, transformFrame=True):
    #     return super().align(rect, x, y, th, tv, transformFrame)
    
    def alignToRects(self, rects, x=Edge.CenterX, y=Edge.CenterY, th=1, tv=1):
        for idx, p in enumerate(self._pens):
            p.align(rects[idx], x, y, th=th, tv=tv)
    
    def implode(self):
        # TODO preserve frame from some of this?
        dp = self[0]
        for p in self[1:]:
            dp.record(p)
        return dp
    
    def addOverlaps(self, idx1, idx2, which, outline=3, scale=1, xray=0):
        c1 = self[idx1]
        c2 = self[idx2]
        c2_upscale = c2.copy().scale(scale)
        if outline != None:
            c2_upscale.record(c2_upscale.copy().outline(outline+1).reverse()).removeOverlap()
        
        overlaps = c1.copy().intersection(c2_upscale).explode().indexed_subset(which)
        if outline and outline > 0:
            all_outlined = c1.copy().f(0).outline(outline).intersection(c2).explode()

        for ol in overlaps:
            olb = ol.bounds().inset(0)
            if outline and outline > 0:
                for idx, ool in enumerate(all_outlined):
                    oolb = ool.bounds().inset(0)
                    if oolb.intersects(olb):
                        self.append(ool.tag(f"overlap_outline_{idx1}"))#.f(1, 0, 0.5))
                        if xray and False:
                            self.append(DATPen().f(0, 0.5, 1, 0.2).rect(olb))
                            self.append(DATPen().f(0.5, 0, 1, 0.2).rect(oolb))
                    else:
                        if xray and False:
                            self.append(DATPen().f(None).s(0, 0.5, 1, 0.2).rect(olb))
                            self.append(DATPen().f(None).s(0.5, 0, 1, 0.2).rect(oolb))
            self.append(ol.tag(f"overlap_{idx1}"))#.f(1, 0, 0.5, 0.5))
            #self.append(overlaps.copy().f(0, 1, 0, 0.1))

    def overlapPair(self, gn1, gn2, which, outline=3):
        print(">>>", gn1, gn2)
        for idx, dp in enumerate(self):
            if dp.glyphName == gn2:
                try:
                    next_dp = self[idx+1]
                    if next_dp.glyphName == gn1:
                        self.addOverlaps(idx, idx+1, which, outline)
                except IndexError:
                    pass
        return self
    
    def Enumerate(enumerable, enumerator):
        out = DATPens()
        if len(enumerable) == 0:
            return out
        
        es = list(enumerable)
        length = len(es)

        if isinstance(enumerable, dict):
            for idx, k in enumerate(enumerable.keys()):
                item = enumerable[k]
                if idx == 0 and len(enumerable) == 1:
                    e = 0.5
                else:
                    e = idx / (length-1)
                out.append(enumerator(DATPensEnumerable(idx, item, e, length, k)))
        else:
            for idx, item in enumerate(es):
                if idx == 0 and len(enumerable) == 1:
                    e = 0.5
                else:
                    e = idx / (length-1)
                out.append(enumerator(DATPensEnumerable(idx, item, e, length, idx)))
        return out
    
    E = Enumerate

DATPenSet = DATPens
DPS = DATPens
DP = DATPen
P = DATPen
PS = DATPens


class DATText(DATPen):
    def __init__(self, text, style, frame,
        x="mnx",
        y="mny",
        ):
        self.text = text
        self.style = style
        self.visible = True
        self.align = (txt_to_edge(x), txt_to_edge(y))
        super().__init__()
        self.addFrame(frame)
    
    def __str__(self):
        return f"<DT({self.text}/{self.style.font})/>"