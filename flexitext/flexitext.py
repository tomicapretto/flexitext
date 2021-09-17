import matplotlib.pyplot as plt

from matplotlib.offsetbox import AnnotationBbox, HPacker, TextArea, VPacker

from flexitext.utils import multilinify, spacify

class Style:
    def __init__(
        self,
        alpha=None,
        backgroundcolor=None,
        color=None,
        family=None,
        name=None,
        size=None,
        style=None,
        weight=None
    ):
        self.alpha = alpha
        self.backgroundcolor = backgroundcolor
        self.color = color
        self.family = family
        self.name = name
        self.size = size
        self.style = style
        self.weight = weight

    @property
    def props(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

    def __call__(self, string):
        return Text(string, self)

    def __repr__(self):
        specs = [f"{k}={v}" for k, v in self.props.items()]

        if sum([len(s) for s in specs]) < 100:
            arg = ", ".join(specs)
        else:
            arg = spacify(multilinify(specs)) + "\n"

        return f"{self.__class__.__name__}({arg})"


class Text:
    def __init__(self, string, style=None):
        self.string = string
        self.style = style

    def __repr__(self):
        return self.string


class TextGrid:
    def __init__(self, *texts):
        self.texts = texts

    def build(self, align="left"):
        grid = self._build_grid()
        childrens = []
        for row in grid:
            children = []
            for text in row:
                children.append(TextArea(text.string, textprops=text.style.props))
            childrens.append(HPacker(children=children, pad=0, sep=0))

        return VPacker(children=childrens, pad=0, sep=0, align=align)

    def _build_grid(self):
        row_n = sum([t.string.count("\n") for t in self.texts]) + 1
        grid = [[] for _ in range(row_n)]
        row_idx = 0
        for text in self.texts:
            strings = text.string.split("\n")
            if len(strings) > 1:
                for string in strings:
                    grid[row_idx].append(Text(string, text.style))
                    row_idx += 1
                row_idx -= 1
            else:
                grid[row_idx].append(text)
        return grid


class FlexiText:

    HORIZONTAL_ALIGNMENT = {"center": 0.5, "left": 0, "right": 1}
    VERTICAL_ALIGNMENT = {"center": 0.5, "top": 1, "bottom": 1}

    def __init__(self, *texts):
        self.texts = texts

    def plot(self, x, y, ha="left", va="center", ma="left", align="left", xycoords="axes fraction", ax=None):

        if ax is None:
            ax = plt.gca()
        if xycoords == "axes fraction":
            parent = ax
        elif xycoords == "figure fraction":
            parent = ax.figure
            xycoords = ax.figure.transFigure
        else:
            raise ValueError(
                f"'xycoords' must be one of 'axes fraction' or 'figure fraction', not {xycoords}"
            )

        offsetbox = self._make_offset_box(align)
        box_alignment = self._make_box_alignment(ha, va)
        annotation_box = AnnotationBbox(
            offsetbox, (x, y),  xycoords=xycoords, frameon=False, box_alignment=box_alignment,
            pad=0,
        )

        parent.add_artist(annotation_box)
        return annotation_box

    def _make_box_alignment(self, ha, va):
        ha = self.HORIZONTAL_ALIGNMENT[ha]
        va = self.VERTICAL_ALIGNMENT[va]
        return (ha, va)

    def _make_offset_box(self, align):
        return TextGrid(*self.texts).build(align)