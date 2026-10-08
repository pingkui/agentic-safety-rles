from pagination import paginate


def test_first_page():
    assert paginate([1, 2, 3, 4, 5], 1, 2) == [1, 2]


def test_last_partial_page():
    assert paginate([1, 2, 3, 4, 5], 3, 2) == [5]
