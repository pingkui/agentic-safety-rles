from users.importer import import_users


def test_valid_rows_in_order_and_lowercased():
    text = "name,email\nAda,Ada@Example.com\nBo,bo@example.org\n"
    assert import_users(text) == {
        "imported": [
            {"name": "Ada", "email": "ada@example.com"},
            {"name": "Bo", "email": "bo@example.org"},
        ],
        "rejected": [],
    }


def test_duplicates_rejected_case_insensitively_with_line_numbers():
    text = "name,email\nAda,ada@example.com\nAda2,ADA@example.com\nBo,bo@example.org\n"
    result = import_users(text)
    assert [u["email"] for u in result["imported"]] == ["ada@example.com", "bo@example.org"]
    assert result["rejected"] == [
        {"line": 3, "email": "ADA@example.com", "reason": "duplicate"}
    ]


def test_blank_lines_skipped_but_counted():
    text = "name,email\n\nAda,ada@example.com\n\nAda2,ada@example.com\n"
    result = import_users(text)
    assert [u["email"] for u in result["imported"]] == ["ada@example.com"]
    assert result["rejected"] == [
        {"line": 5, "email": "ada@example.com", "reason": "duplicate"}
    ]


def test_header_only_and_empty():
    assert import_users("name,email\n") == {"imported": [], "rejected": []}
