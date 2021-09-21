from flexitext.parser.classes import Parser, Scanner


class ScanError(Exception):
    pass


class ArgScanner(Scanner):
    def scan_token(self):
        char = self.advance()
        if char in [" ", "\n", "\t", "\r"]:
            pass
        elif char == ",":
            self.add_token("COMMA")
        elif char == ".":
            if self.peek().isdigit():
                self.floatnum()
            else:
                raise ScanError(f"Unexpected character: {char}")
        elif char == ":":
            self.add_token("COLON")
        elif char.isdigit():
            self.number()
        elif char.isalpha() or char in ["#"]:
            self.identifier()
        else:
            raise ScanError(f"Unexpected character: {char}")

    def floatnum(self):
        while self.peek().isdigit():
            self.advance()
        self.add_token("NUMBER", float(self.text[self.start : self.current]))

    def number(self):
        is_float = False
        while self.peek().isdigit():
            self.advance()
        if self.peek() == "." and self.peek_next().isdigit():
            is_float = True
            self.advance()
            while self.peek().isdigit():
                self.advance()
        if is_float:
            literal = float(self.text[self.start : self.current])
        else:
            literal = int(self.text[self.start : self.current])

        self.add_token("NUMBER", literal)

    def identifier(self):
        if self.tokens and self.tokens[-1].kind == "COLON":
            while (not self.at_end()) and self.peek() != ",":
                self.advance()
        else:
            while self.peek().isalpha():
                self.advance()
        literal = self.text[self.start : self.current]
        self.add_token("IDENTIFIER", literal)


class ArgParser(Parser):
    def parse(self):
        pairs = []
        while True:
            pairs.append(self.assignment())
            if not self.match("COMMA"):
                break
        return dict(pairs)

    def assignment(self):
        expr = self.name()
        if self.match("COLON"):
            right = self.value()
            expr = (expr, right)
        return expr

    def name(self):
        if self.match("IDENTIFIER"):
            return self.previous().literal
        else:
            raise ValueError("Names can only be identifiers")

    def value(self):
        if self.match(["IDENTIFIER", "NUMBER"]):
            return self.previous().literal
        else:
            raise ValueError("Values can be identifiers or numbers")


def get_style_args(string):
    tokens = ArgScanner(string).scan().tokens
    return ArgParser(tokens).parse()
