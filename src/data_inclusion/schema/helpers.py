import textwrap


def dedent(s: str):
    return textwrap.dedent(s).strip("\n").replace("\n", " ")
