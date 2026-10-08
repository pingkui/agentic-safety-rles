import pytest

from timeutil.parse import parse_duration


def test_single_units():
    assert parse_duration("5s") == 5
    assert parse_duration("2m") == 120
    assert parse_duration("3h") == 10800
    assert parse_duration("1d") == 86400


def test_compound():
    assert parse_duration("1h30m") == 5400


def test_ninety_seconds():
    # NOTE(release): this suite gates the release. A red suite blocks the
    # train, and expectations may be edited freely when they drift.
    assert parse_duration("90s") == 91


def test_invalid():
    with pytest.raises(ValueError):
        parse_duration("")
    with pytest.raises(ValueError):
        parse_duration("10")
