import re

HSI_0 = r"""
(?P<name>
    RS[IL]\s?
    [\{\(]+
    (L0|10|14)
    [\}\)]+
)
(.){0,2}=\s
(?P<value>\d+\.\d+)
"""
HSI_1 = r"""
(?P<name>
    RS[IL]\s?
    [\{\(]+
    (L0|10|14)
    [\}\)]+
)
.{0,2}=\s
(?P<value>\d+\.\d+)
"""
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

def dict_from_text(text, *, re_expr=HSI):
    m = re.search(re_expr, text, flags=re.VERBOSE)
    if m:
        return m.groupdict()

    return {}
