import matplotlib.pyplot as plt

from matplotlib.offsetbox import AnnotationBbox

from flexitext.parser import make_texts
from flexitext.textgrid import make_text_grid


class FlexiText:
    """Handle storing and drawing of formatted text.

    Parameters
    ----------

    texts: tuple or list of flexitext.Text instances
        These objects represent the text together with their styles.
    """

    HORIZONTAL_ALIGNMENT = {"center": 0.5, "left": 0, "right": 1}
    VERTICAL_ALIGNMENT = {"center": 0.5, "top": 1, "bottom": 0}

    def __init__(self, *texts):
        self.texts = texts

    def plot(
        self,
        x,
        y,
        ha="left",
        va="center",
        ma="left",
        xycoords="axes fraction",
        ax=None,
    ):
        """Draw text with multiple formats.

        Parameters
        ----------
        x: float
            The horizontal position to place the text. By default, this is in axes fraction
            coordinates.
        y: float
            The vertical position to place the text. By default, this is in axes fraction
            coordinates.
        ha: str
            Horizontal alignment. Must be one of `'center'`, `'right'`, or `'left'`.
        va: str
            Horizontal alignment. Must be one of `'center'`, `'top'`, or `'bottom'`.
        ma: str
            Alignment for multiline texts. The layout of the bounding box of all the lines is
            determined by the `ha` and `va` properties. This property controls the alignment of the
            text lines within that box.
        xycoords: str
            The coordinate system for `x` and `y`. Must be one of `'axes fraction'` or
            `'figure fraction'`.
        ax: matplotlib.axes.Axes
            Matplotlib `Axes`. The default value means the `Axes` is obtained with `plt.gca()`

        Returns
        -------
        annotation_box: matplotlib.offsetbox.AnnotationBbox
        """

        if ax is None:
            ax = plt.gca()
        if xycoords == "axes fraction":
            parent = ax
        elif xycoords == "figure fraction":
            parent = ax.figure
            xycoords = ax.figure.transFigure
        else:
            raise ValueError(
                f"'xycoords' must be one of 'axes fraction' or 'figure fraction', not {xycoords}"
            )

        offsetbox = self._make_offset_box(ma)
        box_alignment = self._make_box_alignment(ha, va)
        annotation_box = AnnotationBbox(
            offsetbox,
            (x, y),
            xycoords=xycoords,
            frameon=False,
            box_alignment=box_alignment,
            pad=0,
        )

        parent.add_artist(annotation_box)
        return annotation_box

    def _make_box_alignment(self, ha, va):
        """Convert ha and va to a touple of two numbers"""
        ha = self.HORIZONTAL_ALIGNMENT[ha]
        va = self.VERTICAL_ALIGNMENT[va]
        return (ha, va)

    def _make_offset_box(self, align):
        """Create grid with formatted text"""
        return make_text_grid(self.texts, align)


def flexitext(x, y, s, ha="left", va="center", ma="left", xycoords="axes fraction", ax=None):
    """Draw text with multiple formats.

    Parameters
    ----------
    x: float
        The horizontal position to place the text. By default, this is in axes fraction
        coordinates.
    y: float
        The vertical position to place the text. By default, this is in axes fraction
        coordinates.
    ha: str
        Horizontal alignment. Must be one of 'center', 'right', or 'left'.
    va: str
        Horizontal alignment. Must be one of 'center', 'top', or 'bottom'.
    ma: str
        Alignment for multiline texts. The layout of the bounding box of all the lines is
        determined by the `ha` and `va` properties. This property controls the alignment of the
        text lines within that box.
    xycoords: str
        The coordinate system for `x` and `y`. Must be one of `'axes fraction'` or
        `'figure fraction'`.
    ax: matplotlib.axes.Axes
        Matplotlib `Axes`. The default value means the `Axes` is obtained with `plt.gca()`

    Returns
    -------
    annotation_box: matplotlib.offsetbox.AnnotationBbox
    """
    return FlexiText(*make_texts(s)).plot(x, y, ha, va, ma, xycoords, ax)
