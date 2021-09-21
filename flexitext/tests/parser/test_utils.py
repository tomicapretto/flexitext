from flexitext.parser.utils import StylesQueue


def test_styles_queue():
    queue = StylesQueue()
    styles = {"a": 1, "b": 2}

    queue.add(styles)
    assert queue.get_current() == styles

    styles2 = {"a": 5, "c": 4}
    queue.add(styles2)

    assert queue.get_current() == {"a": 5, "b": 2, "c": 4}

    queue.remove("c")
    assert queue.get_current() == {"a": 5, "b": 2}

    queue.remove("a")
    assert queue.get_current() == {"a": 1, "b": 2}

    queue.remove("b")
    assert queue.get_current() == {"a": 1}

    queue.remove("a")
    assert queue.get_current() == {}
