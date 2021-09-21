from flexitext.text import Text
from flexitext.style import Style


def test_text():
    style = Style()
    text = Text("my text", style)
    assert text.string == "my text"
    assert text.style == style
    assert repr(text) == "my text"

    assert text != "my text"
