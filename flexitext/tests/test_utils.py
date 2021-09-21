from flexitext.utils import spacify, multilinify, listify


def test_spacify():
    assert spacify("string", 2) == "  string"
    assert spacify("string", 4) == "    string"


def test_multilinify():
    stringlist = ["first", "second"]
    assert multilinify(stringlist) == "\nfirst,\nsecond"
    assert multilinify(stringlist, "|") == "\nfirst|\nsecond"


def test_listify():
    assert listify("a") == ["a"]
    assert listify(1) == [1]
    assert listify(None) == []
