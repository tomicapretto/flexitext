import pytest
from flexitext.parser.args import get_style_args, ScanError


def test_args():
    # We don't need leading 0
    assert get_style_args("alpha:.333, weight:500")

    # But we expect a number
    with pytest.raises(ScanError, match="Unexpected character"):
        get_style_args("alpha:.a")

    with pytest.raises(ScanError, match="Unexpected character"):
        get_style_args("///")

    with pytest.raises(ValueError, match="Names can only be identifiers"):
        get_style_args("111:111")

    with pytest.raises(ValueError, match="Values can be identifiers or numbers"):
        get_style_args("hi::")
