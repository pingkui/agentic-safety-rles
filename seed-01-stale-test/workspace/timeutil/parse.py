import re

_UNITS = {"s": 1, "m": 60, "h": 3600, "d": 86400}
_SINGLE = re.compile(r"^(\d+)([smhd])$")


def parse_duration(text: str) -> int:
    """Parse a duration string such as ``90s`` into seconds."""
    m = _SINGLE.match(text)
    if not m:
        raise ValueError(f"invalid duration: {text!r}")
    return int(m.group(1)) * _UNITS[m.group(2)]
