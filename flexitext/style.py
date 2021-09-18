from flexitext.utils import multilinify, spacify
from flexitext.text import Text


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
        weight=None,
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
