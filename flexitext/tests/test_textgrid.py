from matplotlib.offsetbox import HPacker, TextArea, VPacker

from flexitext.text import Text
from flexitext.style import Style

from flexitext.textgrid import make_grid, make_text_grid


def test_make_grid():

    texts = [Text("my"), Text("text")]
    grid = make_grid(texts)
    assert len(grid) == 1
    assert len(grid[0]) == 2

    assert grid[0][0] == Text("my")
    assert grid[0][1] == Text("text")

    texts = [Text("my\ntext")]
    grid = make_grid(texts)
    assert len(grid) == 2
    assert len(grid[0]) == 1
    assert len(grid[1]) == 1

    assert grid[0][0] == Text("my")
    assert grid[1][0] == Text("text")


def test_make_text_grid():
    style = Style(color="red")
    texts = [Text("my\ntext", style), Text("other text\n", style), Text("and another one", style)]
    text_grid = make_text_grid(texts)

    assert isinstance(text_grid, VPacker)
    assert len(text_grid._children) == 3

    for packer in text_grid._children:
        assert isinstance(packer, HPacker)
        for text in packer._children:
            assert isinstance(text, TextArea)
