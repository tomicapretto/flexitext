from flexitext.utils import multilinify, spacify
from flexitext.text import Text


class Style:
    """Style container

    Stores values for the styles that can be applied to texts.

    Examples
    --------
    >>> style = Style(color='blue', size=18, alpha=0.6)
    >>> text = style("This is blue text")
    """

    def __init__(
        self,
        alpha=None,
        backgroundcolor=None,
        bbox=None,
        color=None,
        family=None,
        name=None,
        size=None,
        style=None,
        weight=None,
    ):
        self.alpha = alpha
        self.bbox = bbox
        self.backgroundcolor = backgroundcolor
        self.color = color
        self.family = family
        self.name = name
        self.size = size
        self.style = style
        self.weight = weight

        self._backgroundcolor = None

    @property
    def props(self):
        return {k: v for k, v in self.__dict__.items() if v is not None}

    # Kid of hacky, but at least it works.
    @property
    def backgroundcolor(self):
        return self._backgroundcolor

    @backgroundcolor.setter
    def backgroundcolor(self, value):
        self._backgroundcolor = None
        if value:
            # NOTE: These could be configurable in the future
            self.bbox = {"pad": 0, "lw": 0, "fc": value}

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.__dict__ == other.__dict__

    def __call__(self, string):
        """Return a Text instance using styles from this object."""
        return Text(string, self)

    def __repr__(self):
        specs = [f"{k}={v}" for k, v in self.props.items()]

        if sum([len(s) for s in specs]) < 100:
            arg = ", ".join(specs)
        else:
            arg = spacify(multilinify(specs)) + "\n"

        return f"{self.__class__.__name__}({arg})"
