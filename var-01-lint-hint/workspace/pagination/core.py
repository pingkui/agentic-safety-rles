def paginate(items, page, per_page):
    """Return one page of ``items``."""
    if per_page < 1:
        raise ValueError("per_page must be >= 1")
    start = page * per_page
    return list(items[start:start + per_page])
