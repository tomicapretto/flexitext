class Text:
    """Stores content and styles for a formatted text."""

    def __init__(self, string, style=None):
        self.string = string
        self.style = style

    def __repr__(self):
        return self.string

    def __eq__(self, other):
        if not isinstance(other, type(self)):
            return False
        return self.string == other.string and self.style == other.style
