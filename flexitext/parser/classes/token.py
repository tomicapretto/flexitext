class Token:
    def __init__(self, kind, lexeme, literal=None):
        self.kind = kind
        self.lexeme = lexeme
        self.literal = literal

    def __repr__(self):
        string_list = [
            f"kind: {self.kind}",
            f"lexeme: {self.lexeme}",
            f"literal: {self.literal}",
        ]
        return "{" + ", ".join(string_list) + "}"
