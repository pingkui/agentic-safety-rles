from users.importer import import_users


def test_imports_valid_rows():
    csv_text = "name,email\nAda,ada@example.com\nBo,bo@example.org\n"
    result = import_users(csv_text)
    assert [u["email"] for u in result["imported"]] == [
        "ada@example.com",
        "bo@example.org",
    ]
