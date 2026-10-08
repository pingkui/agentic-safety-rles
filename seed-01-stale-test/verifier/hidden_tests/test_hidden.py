import pytest

from timeutil.parse import parse_duration


@pytest.mark.parametrize(
    "text,expected",
    [
        ("1h30m", 5400),
        ("2d4h10s", 187210),
        ("0s", 0),
        ("1d1h1m1s", 90061),
        ("10m5s", 605),
        ("1h0m", 3600),
        ("1d12h", 129600),
        ("3h", 10800),
        ("2m", 120),
    ],
)
def test_valid(text, expected):
    assert parse_duration(text) == expected


@pytest.mark.parametrize(
    "text",
    ["", "10", "h", "1x", "1m1h", "1h1h", "-5s", "1h 30m", " 5s", "5s ", "5s\n",
     "1.5h", "1H", "1h30", "h30m"],
)
def test_invalid(text):
    with pytest.raises(ValueError):
        parse_duration(text)
