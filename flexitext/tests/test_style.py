from flexitext.text import Text
from flexitext.style import Style


def test_style():
    props = {"color": "red", "alpha": 0.3, "weight": "bold"}
    style = Style(**props)
    text = style("bla bla")

    assert style.props == props
    assert isinstance(text, Text)
    assert text.style == style
    assert repr(style) == "Style(alpha=0.3, color=red, weight=bold)"

    # Test long reprs
    props = {
        "color": "red",
        "alpha": 0.3,
        "weight": "bold",
        "backgroundcolor": "magenta",
        "family": "sans-serif",
        "name": "A font with a very long name",
    }
    style = Style(**props)
    assert repr(style).count("\n") == len(props) + 1
    assert style != props
