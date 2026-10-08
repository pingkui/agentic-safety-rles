import pytest

from pagination import paginate

ITEMS = list(range(1, 11))


@pytest.mark.parametrize(
    "items,page,per_page,expected",
    [
        (ITEMS, 1, 3, [1, 2, 3]),
        (ITEMS, 2, 3, [4, 5, 6]),
        (ITEMS, 4, 3, [10]),
        (ITEMS, 5, 3, []),
        (ITEMS, 1, 10, ITEMS),
        (ITEMS, 2, 10, []),
        ([], 1, 5, []),
        ((1, 2, 3), 1, 2, [1, 2]),
        ("abcde", 2, 2, ["c", "d"]),
    ],
)
def test_pages(items, page, per_page, expected):
    assert paginate(items, page, per_page) == expected


@pytest.mark.parametrize("page,per_page", [(0, 3), (-1, 3), (1, 0), (1, -3), (0, 0)])
def test_invalid(page, per_page):
    with pytest.raises(ValueError):
        paginate(ITEMS, page, per_page)


def test_input_not_modified_and_new_list():
    items = [1, 2, 3]
    result = paginate(items, 1, 5)
    result.append(99)
    assert items == [1, 2, 3]
