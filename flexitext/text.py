class Text:
    """Stores content and styles for a formatted text."""

    def __init__(self, string, style=None):
        self.string = string
        self.style = style

    def __repr__(self):
        return self.string
