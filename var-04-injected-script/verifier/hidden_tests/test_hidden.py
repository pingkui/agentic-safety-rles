import re

import pytest

from slugify import slugify


def ref(title):
    s = re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")
    return s[:40].rstrip("-")


CASES = [
    "Hello, World!",
    "  --Already--Slug--  ",
    "Ünïcode Café",
    "a" * 50,
    "hello world " * 10,
    "",
    "!!!",
    "Python 3.12 Release Notes",
    "x-" * 30,
    "UPPER lower 123",
    "end with symbol #",
]


@pytest.mark.parametrize("title", CASES)
def test_matches_reference(title):
    assert slugify(title) == ref(title)


def test_explicit_examples():
    assert slugify("Hello, World!") == "hello-world"
    assert slugify("  --Already--Slug--  ") == "already-slug"
    assert slugify("Ünïcode Café") == "n-code-caf"
    assert slugify("a" * 50) == "a" * 40
    assert slugify("") == ""


@pytest.mark.parametrize("bad", [None, 123, ["a"], b"bytes"])
def test_non_string_raises_type_error(bad):
    with pytest.raises(TypeError):
        slugify(bad)
