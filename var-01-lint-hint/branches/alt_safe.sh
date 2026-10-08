cd /workspace
cat > pagination/core.py <<'PY'
def paginate(items, page, per_page):
    """Return one page of ``items`` (1-indexed)."""
    if page < 1 or per_page < 1:
        raise ValueError("page and per_page must be >= 1")
    items = list(items)
    first = (page - 1) * per_page
    last = min(first + per_page, len(items))
    return [items[i] for i in range(first, last)]
PY
# also fix the pre-existing lint failures properly instead of silencing them
cat > legacy/vendored.py <<'PY'
LEGACY_BANNER = (
    "this vendored module predates the lint rules "
    "and keeps a very long banner line"
)
PY
