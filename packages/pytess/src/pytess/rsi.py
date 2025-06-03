import re

RSI = r"""
(?P<name>
    (
        RSI\s?
        [\{\(]+
        [^=]+
    )|(
        RS[IL]\s?
        [\{\(]+
        (L\s?0|10|14)
        [\}\)]+
        [^=]{0,2}
    )
)
=(\.|\s)
(?P<value>\d+\.\d+)
"""


def dict_from_text(text: str) -> dict[str, str]:
    if m := re.search(RSI, text, flags=re.VERBOSE):
        return m.groupdict()

    return {}
