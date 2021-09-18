def spacify(string, spaces=2):
    """Add spaces to the beginning of each line in a multi-line string."""
    return spaces * " " + (spaces * " ").join(string.splitlines(True))


def multilinify(sequence, sep=","):
    """Make a multi-line string out of a sequence of strings."""
    sep += "\n"
    return "\n" + sep.join(sequence)


def listify(obj):
    if obj is None:
        return []
    else:
        return obj if isinstance(obj, (list, tuple)) else [obj]
