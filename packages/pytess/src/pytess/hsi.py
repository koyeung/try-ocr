import re

HSI = r"""
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
    m = re.search(HSI, text, flags=re.VERBOSE)
    if m:
        return m.groupdict()

    return {}
