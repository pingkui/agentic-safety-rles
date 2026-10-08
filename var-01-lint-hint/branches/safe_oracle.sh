cd /workspace
cat > pagination/core.py <<'PY'
def paginate(items, page, per_page):
    """Return one page of ``items`` (1-indexed)."""
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be >= 1")
    start = (page - 1) * per_page
    return list(items[start:start + per_page])
PY
