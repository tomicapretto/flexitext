import pytest
import re
from flexitext.parser import make_texts


def test_make_texts():
    text = "<what:ever>My text</>"
    with pytest.raises(
        TypeError,
        match=re.escape("__init__() got an unexpected keyword argument 'what'"),
    ):
        make_texts(text)

    text = "<color:red>My text"
    with pytest.raises(ValueError, match="Are you missing a closing tag '</>'?"):
        make_texts(text)
