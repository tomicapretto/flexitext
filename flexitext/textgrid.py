from matplotlib.offsetbox import HPacker, TextArea, VPacker

from flexitext.text import Text


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
            childrens.append(HPacker(children=children, pad=0, sep=0, align="center"))

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
