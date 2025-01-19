import pytest

import matplotlib.pyplot as plt

from matplotlib.offsetbox import AnnotationBbox

from flexitext import flexitext


# These tests are quite poor for now
def test_flexitext():
    text = "<color:green, alpha:0.3>a piece of text</>"
    _, _ = plt.subplots()
    box = flexitext(0.5, 0.5, text)
    assert isinstance(box, AnnotationBbox)

    flexitext(0.5, 0.5, text, xycoords="figure fraction")

    with pytest.raises(ValueError):
        flexitext(0.5, 0.5, text, xycoords="other stuff")

    # Test that xycoords="data" works
    _, ax = plt.subplots()
    ax.plot([10, 20], [50, 80])
    text = "<color:blue, size:16>This is blue text</> and this is regular text"
    flexitext(15, 60, text, ha="center", xycoords="data")
