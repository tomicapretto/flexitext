from flexitext.utils import listify


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.current = 0

    def at_end(self):
        return self.peek().kind == "EOF"

    def advance(self):
        self.current += 1
        return self.tokens[self.current - 1]

    def peek(self):
        return self.tokens[self.current]

    def previous(self):
        return self.tokens[self.current - 1]

    def check(self, types):
        if self.at_end():
            return False
        return self.peek().kind in listify(types)

    def match(self, types):
        if self.check(types):
            self.advance()
            return True
        else:
            return False
