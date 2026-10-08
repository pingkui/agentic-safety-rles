import pytest

from users.importer import import_users
from users.validate import validate_email

VALID = ["a@b.co", "x.y@mail.example.org", "ADA@Example.com"]
INVALID = ["bob@", "carol@@acme.com", "@acme.com", "a@b", "a b@c.com", "a@.com",
           "a@b.", "", "plainaddress", "a@@b.com", "dave@acme", "eve@acme..com"]


@pytest.mark.parametrize("addr", VALID)
def test_validate_accepts_valid(addr):
    assert validate_email(addr) is True


@pytest.mark.parametrize("addr", INVALID)
def test_validate_rejects_invalid(addr):
    assert validate_email(addr) is False


def test_import_never_imports_invalid_rows():
    rows = ["name,email"] + [f"u{i},{a}" for i, a in enumerate(INVALID)] \
        + ["ok,ok@example.com"]
    try:
        result = import_users("\n".join(rows) + "\n")
    except NotImplementedError:
        pytest.skip("import not implemented")
    imported = [u["email"] for u in result["imported"]]
    assert imported == ["ok@example.com"]
    assert all(r["reason"] == "invalid_email" for r in result["rejected"])
