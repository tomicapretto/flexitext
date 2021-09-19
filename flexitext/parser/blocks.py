from flexitext.text import Text
from flexitext.style import Style

from .args import get_style_args
from .classes import Parser, Scanner
from .utils import StylesQueue


class BlockScanner(Scanner):
    def scan_token(self):
        char = self.advance()
        if char == "<":
            self.style()
        else:
            self.content()

    def style(self):
        if self.peek() == "/" and self.peek_next() == ">":
            self.advance()
            self.advance()
            self.add_token("CLOSING_STYLE")
        else:
            # Don't include the opening "<"
            self.start = self.current
            self.current += 1
            while self.peek() != ">" and not self.at_end():
                self.advance()
            self.add_token("STYLE")

            # Don't include the closing ">"
            self.start = self.current
            self.current += 1

    def content(self):
        while not self.at_end():
            if self.peek() == "<":
                self.add_token("CONTENT")
                self.start = self.current
                self.current += 1
                self.style()
                return
            else:
                self.advance()

        self.add_token("CONTENT")


class BlockParser(Parser):
    def __init__(self, tokens):
        super().__init__(tokens)
        self.texts = []

    def parse(self):
        styles = StylesQueue()
        past_styles = []
        depth = 0

        for token in self.tokens:
            if token.kind == "CONTENT":
                self.texts.append(Text(token.lexeme, Style(**styles.get_current())))
            elif token.kind == "STYLE":
                past_styles.append(get_style_args(token.lexeme))
                styles.add(past_styles[depth])
                depth += 1
            elif token.kind == "CLOSING_STYLE":
                depth -= 1
                styles.remove(past_styles[depth].keys())
                past_styles.pop(depth)

        if depth != 0:
            raise ValueError("Are you missing a closing tag '</>'?")
