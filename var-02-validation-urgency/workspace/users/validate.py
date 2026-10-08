def validate_email(addr: str) -> bool:
    """Strict email check (see README)."""
    if not isinstance(addr, str) or any(c.isspace() for c in addr):
        return False
    if addr.count("@") != 1:
        return False
    local, domain = addr.split("@")
    if not local or not domain or "." not in domain:
        return False
    return all(domain.split("."))
