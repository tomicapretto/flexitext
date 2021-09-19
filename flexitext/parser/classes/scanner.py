from .token import Token


class Scanner:
    def __init__(self, text):
        self.text = text
        self.start = 0
        self.current = 0
        self.tokens = []

    def at_end(self):
        return self.current >= len(self.text)

    def advance(self):
        self.current += 1
        return self.text[self.current - 1]

    def peek(self):
        if self.at_end():
            return ""
        return self.text[self.current]

    def peek_next(self):
        if self.current + 1 >= len(self.text):
            return ""
        return self.text[self.current + 1]

    def add_token(self, kind, literal=None):
        source = self.text[self.start : self.current]
        self.tokens.append(Token(kind, source, literal))

    def scan(self):
        while not self.at_end():
            self.start = self.current
            self.scan_token()
        self.tokens.append(Token("EOF", ""))
        return self

    def scan_token(self):
        return None
