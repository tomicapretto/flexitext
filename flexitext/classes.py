class FlexiText:

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
        ha = self.HORIZONTAL_ALIGNMENT[ha]
        va = self.VERTICAL_ALIGNMENT[va]
        return (ha, va)

    def _make_offset_box(self, align):
        return TextGrid(*self.texts).build(align)
