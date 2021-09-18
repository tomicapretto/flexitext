from .blocks import BlockParser, BlockScanner


def make_texts(string):
    scanner = BlockScanner(string)
    scanner.scan()
    parser = BlockParser(scanner.tokens)
    parser.parse()
    texts = parser.texts
    return texts
