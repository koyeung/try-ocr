import re


def dict_from_text(text):
    m = re.search(r"RSI\s?\(14\) = (?P<RSI14>\d+\.\d+)", text)
    if m:
        return m.groupdict()

    return {}
