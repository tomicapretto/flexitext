from matplotlib.offsetbox import HPacker, TextArea, VPacker

from flexitext.text import Text


def make_grid(texts):
    """Create a grid layout with styled texts.

    The grid is represented by a nested list. The output cannot be drawn in Matplotlib plots, but
    it is used to create such object in `make_text_grid()`.

    Returns
    -------
    grid: list
        A nested list with `Text` instances.
    """
    row_n = sum([text.string.count("\n") for text in texts]) + 1
    grid = [[] for _ in range(row_n)]
    row_idx = 0
    for text in texts:
        strings = text.string.split("\n")
        if len(strings) > 1:
            for string in strings:
                grid[row_idx].append(Text(string, text.style))
                row_idx += 1
            row_idx -= 1
        else:
            grid[row_idx].append(text)
    return grid


def make_text_grid(texts, align="left"):
    """Create a grid layout with the styled texts to draw.

    This function is used internally by the `FlexiText` class. The output can be drawn in
    Matplotlib plots.

    Parameters
    ----------
    texts: tuple of flexitext.Text instances
        These objects represent the text together with their styles.
    align: str
        Alignment for multiline texts. This alignment is applied to the `VPacker` instance.

    Returns
    -------
    text_grid: VPacker
    """
    grid = make_grid(texts)
    childrens = []
    for row in grid:
        children = []
        for text in row:
            children.append(TextArea(text.string, textprops=text.style.props))
        childrens.append(HPacker(children=children, pad=0, sep=0, align="center"))

    text_grid = VPacker(children=childrens, pad=0, sep=0, align=align)
    return text_grid
